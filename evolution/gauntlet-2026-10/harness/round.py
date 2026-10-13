#!/usr/bin/env python3
"""Coordinator for the 2026-10 suite gauntlet.

Usage: round.py build|render|render-designer|blind|score|apply|mark|extend|status ...

Each subcommand reads and writes only files under evolution/gauntlet-2026-10/<skill>/ and
the program LEDGER.md. The coordinator never reads pack/keys.json or pack/notes.md; the
key verifier prompts are the only place keys are rendered.
"""
import argparse
import datetime
import io
import json
import os
import random
import string
import subprocess
import sys
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GAUNTLET_SCRIPTS = HERE.parent.parent.parent / "skills" / "skill-gauntlet" / "scripts"
STATES = ["pending", "designed", "frozen", "ran", "blinded", "judged", "scored", "applied"]
PACK_FILES = ["brief-1.md", "brief-2.md", "brief-3.md", "framing-hype.md", "framing-skeptical.md",
              "negative.md", "notes.md", "keys.json"]
BRIEFS = ["brief-1", "brief-2", "brief-3"]


def root() -> Path:
    return Path(os.environ.get("GAUNTLET_ROOT", HERE.parent))


def repo() -> Path:
    return Path(os.environ.get("GAUNTLET_REPO", HERE.parent.parent.parent))


def round_dir(skill: str) -> Path:
    return root() / skill


def load_spec(skill: str) -> dict:
    for row in json.loads((root() / "harness" / "skills.json").read_text()):
        if row["skill"] == skill:
            return row
    sys.exit(f"{skill}: not in harness/skills.json")


# ---------------------------------------------------------------- ledger

def _ledger() -> Path:
    return root() / "LEDGER.md"


def _rows():
    lines = _ledger().read_text().splitlines()
    return lines, [i for i, l in enumerate(lines) if l.startswith("| ") and l.split("|")[1].strip().isdigit()]


def get_state(skill: str) -> str:
    lines, idx = _rows()
    for i in idx:
        cells = [c.strip() for c in lines[i].strip("|").split("|")]
        if cells[1] == skill:
            return cells[2]
    sys.exit(f"{skill}: not in LEDGER.md")


def set_state(skill: str, state: str, **cols) -> None:
    if state not in STATES:
        sys.exit(f"unknown state {state}")
    lines, idx = _rows()
    names = ["n", "skill", "state", "validation", "rewrite", "commit", "tokens"]
    for i in idx:
        cells = [c.strip() for c in lines[i].strip("|").split("|")]
        if cells[1] == skill:
            row = dict(zip(names, cells + [""] * (len(names) - len(cells))))
            row["state"] = state
            row.update({k: str(v) for k, v in cols.items() if v is not None})
            lines[i] = "| " + " | ".join(row[n] for n in names) + " |"
            _ledger().write_text("\n".join(lines) + "\n")
            return
    sys.exit(f"{skill}: not in LEDGER.md")


# ---------------------------------------------------------------- build

def validate_pack(rd: Path) -> list:
    problems = [f"missing pack/{f}" for f in PACK_FILES if not (rd / "pack" / f).is_file()]
    kf = rd / "pack" / "keys.json"
    if kf.is_file():
        try:
            keys = json.loads(kf.read_text())
        except json.JSONDecodeError as e:
            return problems + [f"keys.json is not JSON: {e}"]
        for b in BRIEFS:
            items = keys.get(b)
            if not isinstance(items, list) or len(items) < 2:
                problems.append(f"keys.json: {b} needs at least 2 keys")
                continue
            for k in items:
                for field in ("id", "text"):
                    if not k.get(field):
                        problems.append(f"keys.json: {b} key missing {field}")
                if k.get("split") != "held-out":
                    problems.append(f"keys.json: {b} key {k.get('id')} split must be held-out")
    return problems


def _extract(ref: str, skill: str, dest: Path) -> None:
    try:
        tar = subprocess.run(["git", "-C", str(repo()), "archive", ref, f"skills/{skill}"],
                             capture_output=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        sys.exit(f"{skill}: cannot read skills/{skill} at {ref}: {e.stderr.decode().strip()}")
    prefix = f"skills/{skill}/"
    with tarfile.open(fileobj=io.BytesIO(tar)) as t:
        for m in t.getmembers():
            if m.isfile() and m.name.startswith(prefix):
                out = dest / m.name[len(prefix):]
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(t.extractfile(m).read())


def _code(rng, used: set, first: str, second: str) -> str:
    while True:
        c = rng.choice(first) + rng.choice(second)
        if c not in used:
            used.add(c)
            return c


def _cell(stem: str, kind: str, code: str, run: int) -> dict:
    return {"cell": f"{stem}--{code}--r{run}", "kind": kind, "input": f"pack/{stem}.md", "arm": code, "run": run}


def freeze_files(rd: Path) -> list:
    h = root() / "harness"
    files = sorted(p for p in (rd / "pack").iterdir() if p.is_file())
    files += sorted((h / "prompts").glob("*.md"))
    files += [h / f for f in ("rubric.md", "PREREG-TEMPLATE.md", "gates.py", "round.py", "skills.json", "run-jobs.js")]
    files += [GAUNTLET_SCRIPTS / f for f in ("normalize.py", "scorecard.py", "freeze.py")]
    return [str(f) for f in files if f.is_file()]


def build(skill: str, seed=None) -> dict:
    rd = round_dir(skill)
    if (rd / "SEALED.json").exists():
        sys.exit(f"{skill}: already built (SEALED.json exists); a frozen round is never rebuilt")
    problems = validate_pack(rd)
    if problems:
        sys.exit(f"{skill}: pack invalid: " + "; ".join(problems))
    spec = load_spec(skill)
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    used = set()
    codes = {arm: _code(rng, used, string.ascii_lowercase, string.digits) for arm in spec["arms"]}
    for arm, code in codes.items():
        if arm != "none":
            _extract("HEAD" if arm == "new" else "v1.0.0", skill, rd / "arms" / code)
    cells = []
    for b in BRIEFS:
        for arm in spec["arms"]:
            for run in (1, 2):
                cells.append(_cell(b, "main", codes[arm], run))
    for reg in ("framing-hype", "framing-skeptical"):
        for arm in spec["arms"]:
            if arm != "none":
                cells.append(_cell(reg, "framing", codes[arm], 1))
    for arm in spec["arms"]:
        cells.append(_cell("negative", "negative", codes[arm], 1))
    (rd / "cells.json").write_text(json.dumps(cells, indent=1))
    (rd / "SEALED.json").write_text(json.dumps({"arms": {c: a for a, c in codes.items()}}, indent=1))
    reg = subprocess.run([sys.executable, str(GAUNTLET_SCRIPTS / "freeze.py"), "register", str(rd / "state"),
                          *freeze_files(rd)], capture_output=True, text=True)
    if reg.returncode != 0:
        sys.exit(f"{skill}: freeze register failed: {reg.stderr.strip() or reg.stdout.strip()}")
    text = (root() / "harness" / "PREREG-TEMPLATE.md").read_text()
    for k, v in {"skill": skill, "date": datetime.date.today().isoformat(), "arms": ", ".join(spec["arms"]),
                 "cells": str(len(cells)), "gates": " + ".join(spec["gates"]), "freeze": reg.stdout.strip()}.items():
        text = text.replace("{" + k + "}", v)
    (rd / "PRE-REGISTRATION.md").write_text(text)
    set_state(skill, "frozen")
    return {"cells": len(cells), "arms": len(codes)}


# ---------------------------------------------------------------- render / blind

PERSONAS = {
    "J-A": "a domain practitioner who has to act on this advice in the situation described. You value "
           "correctness, specificity and whether you could act on it tomorrow.",
    "J-B": "a skeptical reviewer who checks every claim against the facts given. You penalize invented facts, "
           "padding and confident hand-waving, and reward honest uncertainty.",
}
RESERVED = {"V1", "V2", "V3", "V4", "G1", "G2", "G3"}
INPUT_STEMS = BRIEFS + ["framing-hype", "framing-skeptical", "negative"]


def _fill(template: str, **values) -> str:
    for k, v in values.items():
        template = template.replace("{" + k + "}", str(v))
    return template


def _load(rd: Path, name: str):
    return json.loads((rd / name).read_text())


def _write_jobs(rd: Path, phase: str, jobs: list) -> list:
    (rd / "jobs").mkdir(exist_ok=True)
    (rd / "jobs" / f"{phase}.json").write_text(json.dumps(jobs, indent=1))
    return jobs


def _stage_inputs(rd: Path) -> None:
    """Executors and judges read copies in inputs/, never pack/ (which holds the sealed keys)."""
    (rd / "inputs").mkdir(exist_ok=True)
    for stem in INPUT_STEMS:
        (rd / "inputs" / f"{stem}.md").write_text((rd / "pack" / f"{stem}.md").read_text())
    (rd / "inputs" / "rubric.md").write_text((root() / "harness" / "rubric.md").read_text())


def _auditor_rules(rd: Path) -> str:
    text = (rd / "PRE-REGISTRATION.md").read_text()
    start = text.index("**Auditor rule text")
    end = text.index("No goalpost movement", start)
    return text[start:end].strip()


def render(skill: str, phase: str) -> list:
    rd = round_dir(skill).resolve()
    prompts = root() / "harness" / "prompts"
    sealed = _load(rd, "SEALED.json")
    jobs = []
    if phase == "exec":
        _stage_inputs(rd)
        out_dir = rd / "jobs" / "exec"
        out_dir.mkdir(parents=True, exist_ok=True)
        for c in _load(rd, "cells.json"):
            none = sealed["arms"][c["arm"]] == "none"
            tpl = (prompts / ("executor-none.md" if none else "executor-skill.md")).read_text()
            stem = Path(c["input"]).stem
            text = _fill(tpl, skill_dir=rd / "arms" / c["arm"], input=rd / "inputs" / f"{stem}.md",
                         output=rd / "raw" / f"{c['cell']}.md", run=rd)
            (out_dir / f"{c['cell']}.md").write_text(text)
            jobs.append({"id": c["cell"], "prompt": f"jobs/exec/{c['cell']}.md", "model": "sonnet", "effort": "medium"})
        return _write_jobs(rd, "exec", jobs)
    if phase != "judge":
        sys.exit(f"unknown phase {phase}")
    plan = _load(rd, "jobs/judge-plan.json")
    out_dir = rd / "jobs" / "judge"
    out_dir.mkdir(parents=True, exist_ok=True)
    blind = lambda code: rd / "blind" / f"{code}.md"  # noqa: E731
    for jid, persona in PERSONAS.items():
        for b in BRIEFS:
            codes = plan["main"][b]
            text = _fill((prompts / "judge.md").read_text(), judge_id=jid, persona=persona, run=rd,
                         input=rd / "inputs" / f"{b}.md", rubric=rd / "inputs" / "rubric.md", n=len(codes),
                         reports="\n".join(f"- {blind(c)}" for c in codes), brief=b,
                         output=rd / "scores" / f"{jid}-{b}.md")
            (out_dir / f"{jid}-{b}.md").write_text(text)
            jobs.append({"id": f"{jid}-{b}", "prompt": f"jobs/judge/{jid}-{b}.md", "model": "opus", "effort": "high"})
    mains = [c for b in BRIEFS for c in plan["main"][b]]
    text = _fill((prompts / "auditor.md").read_text(), rule_text=_auditor_rules(rd), run=rd,
                 main_list="\n".join(f"- {blind(c)}" for c in mains),
                 pairs_list="\n".join(f"- {p['pair']}: {blind(p['codes'][0])} and {blind(p['codes'][1])}"
                                      for p in plan["framing_pairs"]),
                 neg_list="\n".join(f"- {blind(c)}" for c in plan["negative"]),
                 output=rd / "audit" / "audit.json")
    (out_dir / "auditor.md").write_text(text)
    jobs.append({"id": "auditor", "prompt": "jobs/judge/auditor.md", "model": "sonnet", "effort": "high"})
    keys = _load(rd, "pack/keys.json")
    for b in BRIEFS:
        text = _fill((prompts / "verifier.md").read_text(), input=rd / "inputs" / f"{b}.md", run=rd,
                     reports="\n".join(f"- {blind(c)}" for c in plan["main"][b]),
                     keys="\n".join(f"- {k['id']}: {k['text']}" for k in keys[b]),
                     output=rd / "keys" / f"{b}.json")
        (out_dir / f"verifier-{b}.md").write_text(text)
        jobs.append({"id": f"verifier-{b}", "prompt": f"jobs/judge/verifier-{b}.md", "model": "sonnet", "effort": "high"})
    for d in ("scores", "audit", "keys"):
        (rd / d).mkdir(exist_ok=True)
    return _write_jobs(rd, "judge", jobs)


def _used_codes() -> set:
    f = root() / "used-codes.json"
    return set(json.loads(f.read_text())) if f.exists() else set()


def blind(skill: str, seed=None) -> dict:
    rd = round_dir(skill).resolve()
    cells = _load(rd, "cells.json")
    missing = [c["cell"] for c in cells if not (rd / "raw" / f"{c['cell']}.md").is_file()]
    if missing:
        sys.exit(f"{skill}: missing raw outputs, re-run these cells first: {', '.join(missing)}")
    sealed = _load(rd, "SEALED.json")
    mapping = sealed.get("blind", {})
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    used = _used_codes() | RESERVED | set(mapping.values())
    for c in cells:
        key = f"{c['cell']}.md"
        if key not in mapping:
            while True:
                code = rng.choice(string.ascii_uppercase) + rng.choice(string.digits) + rng.choice(string.ascii_uppercase)
                if code not in used:
                    used.add(code)
                    mapping[key] = code
                    break
    sealed["blind"] = mapping
    (rd / "SEALED.json").write_text(json.dumps(sealed, indent=1))
    (root() / "used-codes.json").write_text(json.dumps(sorted(used - RESERVED)))
    (rd / "state").mkdir(exist_ok=True)
    mfile = rd / "state" / "blind-mapping.json"
    mfile.write_text(json.dumps(mapping, indent=1))
    norm = subprocess.run([sys.executable, str(GAUNTLET_SCRIPTS / "normalize.py"), str(mfile), str(rd / "raw"),
                           str(rd / "blind"), "--strip-h2-ordinals"], capture_output=True, text=True)
    if norm.returncode != 0:
        sys.exit(f"{skill}: normalize failed: {norm.stderr.strip() or norm.stdout.strip()}")
    scan = norm.stdout.split("LEAK SCAN", 1)[-1].splitlines()[1:]
    leak_hits = sum(1 for l in scan if l.startswith("  ") and l.strip() != "clean")
    code_of = lambda c: mapping[f"{c['cell']}.md"]  # noqa: E731
    plan = {"main": {}, "framing_pairs": [], "negative": []}
    for b in BRIEFS:
        codes = [code_of(c) for c in cells if c["kind"] == "main" and Path(c["input"]).stem == b]
        rng.shuffle(codes)
        plan["main"][b] = codes
    skill_arms = [a for a, name in sealed["arms"].items() if name != "none"]
    rng.shuffle(skill_arms)
    for i, arm in enumerate(skill_arms, 1):
        pair = [code_of(c) for reg in ("framing-hype", "framing-skeptical")
                for c in cells if c["kind"] == "framing" and c["arm"] == arm and Path(c["input"]).stem == reg]
        plan["framing_pairs"].append({"pair": f"P{i}", "codes": pair})
    plan["negative"] = [code_of(c) for c in cells if c["kind"] == "negative"]
    rng.shuffle(plan["negative"])
    (rd / "jobs").mkdir(exist_ok=True)
    (rd / "jobs" / "judge-plan.json").write_text(json.dumps(plan, indent=1))
    set_state(skill, "blinded")
    return {"blind": len(mapping), "leak_hits": leak_hits}


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build").add_argument("skill")
    r = sub.add_parser("render")
    r.add_argument("skill")
    r.add_argument("phase", choices=["exec", "judge"])
    sub.add_parser("blind").add_argument("skill")
    args = ap.parse_args(argv)
    if args.cmd == "build":
        res = build(args.skill)
        print(f"{args.skill}: built {res['cells']} cells across {res['arms']} arms; state frozen")
    elif args.cmd == "render":
        jobs = render(args.skill, args.phase)
        print(f"{args.skill}: rendered {len(jobs)} {args.phase} jobs -> jobs/{args.phase}.json")
    elif args.cmd == "blind":
        res = blind(args.skill)
        print(f"{args.skill}: blinded {res['blind']} replies; leak-scan hits: {res['leak_hits']}; state blinded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
