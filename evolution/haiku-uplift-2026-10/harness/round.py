#!/usr/bin/env python3
"""Coordinator for the Haiku uplift program (haiku-uplift-2026-10).

Usage: round.py build|render-designer|render|blind|score|apply|mark|extend|status ...

Every subcommand reads and writes only files under the program root (<root>/<skill>/) and
the program LEDGER.md. Arms are named in skills.json with their executor model: hs (Haiku
with the skill), hn (Haiku alone), ss (Sonnet with the skill), sn (Sonnet alone). An arm with
"reuse" takes its replies from that arm label in an earlier round on the same pack ("source"). The coordinator never reads pack/keys.json or pack/notes.md: the key
verifier prompts are the only place keys are rendered. Each round runs on a snapshot of
this harness (<round>/harness/), which is frozen with freeze.py at build, so later harness
changes never void or alter an earlier round.
"""
import argparse
import datetime
import importlib.util
import io
import json
import os
import random
import re
import shutil
import statistics
import string
import subprocess
import sys
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIVE_SCRIPTS = HERE.parent.parent.parent / "skills" / "skill-gauntlet" / "scripts"
STATES = ["pending", "designed", "frozen", "ran", "blinded", "judged", "scored", "applied"]
PACK_FILES = ["brief-1.md", "brief-2.md", "brief-3.md", "framing-hype.md", "framing-skeptical.md",
              "negative.md", "notes.md", "keys.json"]
BRIEFS = ["brief-1", "brief-2", "brief-3"]
INPUT_STEMS = BRIEFS + ["framing-hype", "framing-skeptical", "negative"]
DIMS = ["V1", "V2", "V3", "V4", "G1", "G2", "G3"]
RESERVED = {"V1", "V2", "V3", "V4", "G1", "G2", "G3"}
WORKER = "gauntlet-worker"  # Read/Write-only agent type: no Skill tool, so skills cannot leak into any arm
PERSONAS = {
    "J-A": "a domain practitioner who has to act on this advice in the situation described. You value "
           "correctness, specificity and whether you could act on it tomorrow.",
    "J-B": "a skeptical reviewer who checks every claim against the facts given. You penalize invented facts, "
           "padding and confident hand-waving, and reward honest uncertainty.",
}
GRADES = {"✓": 1.0, "✔": 1.0, "~": 0.5, "✗": 0.0, "✘": 0.0}
SNAPSHOT = ["gates.py", "round.py", "run-jobs.js", "rubric.md", "PREREG-TEMPLATE.md", "skills.json"]


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


def _strip_fence(text: str) -> str:
    """Instruments sometimes wrap JSON in a ```json fence; unwrapping is lossless."""
    m = re.fullmatch(r"\s*```[a-zA-Z]*\s*\n(.*?)\n\s*```\s*", text, re.S)
    return m.group(1) if m else text


def _load(rd: Path, name: str):
    return json.loads(_strip_fence((rd / name).read_text()))


def _scripts(rd: Path) -> Path:
    snap = rd / "harness" / "scripts"
    return snap if snap.is_dir() else LIVE_SCRIPTS


# ---------------------------------------------------------------- ledger

def _ledger() -> Path:
    return root() / "LEDGER.md"


def _rows():
    lines = _ledger().read_text().splitlines()
    return lines, [i for i, l in enumerate(lines) if l.startswith("| ") and l.split("|")[1].strip().isdigit()]


def _cells_of(line: str) -> list:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def get_state(skill: str) -> str:
    lines, idx = _rows()
    for i in idx:
        cells = _cells_of(lines[i])
        if cells[1] == skill:
            return cells[2]
    sys.exit(f"{skill}: not in LEDGER.md")


def set_state(skill: str, state: str, **cols) -> None:
    if state not in STATES:
        sys.exit(f"unknown state {state}")
    lines, idx = _rows()
    names = ["n", "skill", "state", "validation", "rewrite", "commit", "tokens"]
    for i in idx:
        cells = _cells_of(lines[i])
        if cells[1] == skill:
            row = dict(zip(names, cells + [""] * (len(names) - len(cells))))
            row["state"] = state
            row.update({k: str(v) for k, v in cols.items() if v is not None})
            lines[i] = "| " + " | ".join(row[n] for n in names) + " |"
            _ledger().write_text("\n".join(lines) + "\n")
            return
    sys.exit(f"{skill}: not in LEDGER.md")


def mark(skill: str, state: str) -> None:
    set_state(skill, state)


def status() -> str:
    lines, idx = _rows()
    nxt = next((c[1] for c in (_cells_of(lines[i]) for i in idx) if c[2] != "applied"), None)
    table = "\n".join(lines[i] for i in [idx[0] - 2, idx[0] - 1] + idx) if idx else ""
    return table + f"\n\nnext: {nxt or 'none (program complete)'}"


# ---------------------------------------------------------------- build / designer / extend

def validate_pack(rd: Path) -> list:
    problems = [f"missing pack/{f}" for f in PACK_FILES if not (rd / "pack" / f).is_file()]
    kf = rd / "pack" / "keys.json"
    if kf.is_file():
        try:
            keys = json.loads(_strip_fence(kf.read_text()))
        except json.JSONDecodeError as e:
            return problems + [f"keys.json is not JSON: {e}"]
        for b in BRIEFS:
            items = keys.get(b)
            if not isinstance(items, list) or len(items) < 2:
                problems.append(f"keys.json: {b} needs at least 2 keys")
                continue
            for k in items:
                for field in ("id", "text"):
                    if not isinstance(k, dict) or not k.get(field):
                        problems.append(f"keys.json: {b} key missing {field}")
                if not isinstance(k, dict) or k.get("split") != "held-out":
                    problems.append(f"keys.json: {b} key {k.get('id') if isinstance(k, dict) else k} split must be held-out")
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


def _code(rng, used: set, *alphabets) -> str:
    while True:
        c = "".join(rng.choice(a) for a in alphabets)
        if c not in used and c not in RESERVED:
            used.add(c)
            return c


def _cell(stem: str, kind: str, code: str, run: int) -> dict:
    return {"cell": f"{stem}--{code}--r{run}", "kind": kind, "input": f"pack/{stem}.md", "arm": code, "run": run}


def _ref(spec: dict, arm: str) -> str:
    return spec.get("new_ref", "HEAD") if arm == "new" else spec.get("old_ref", "v1.0.0")


def _snapshot_harness(rd: Path) -> None:
    h, dest = root() / "harness", rd / "harness"
    (dest / "prompts").mkdir(parents=True, exist_ok=True)
    (dest / "scripts").mkdir(exist_ok=True)
    for f in SNAPSHOT:
        if (h / f).is_file():
            shutil.copy2(h / f, dest / f)
    for p in (h / "prompts").glob("*.md"):
        shutil.copy2(p, dest / "prompts" / p.name)
    for f in ("normalize.py", "scorecard.py", "freeze.py"):
        shutil.copy2(LIVE_SCRIPTS / f, dest / "scripts" / f)


def _freeze_files(rd: Path) -> list:
    files = [p for p in sorted((rd / "harness").rglob("*")) if p.is_file() and "__pycache__" not in p.parts]
    files += [p for p in sorted((rd / "pack").iterdir()) if p.is_file()]
    files += [p for p in sorted((rd / "arms").rglob("*")) if p.is_file()]
    files += [p for p in sorted((rd / "raw").glob("*.md"))] if (rd / "raw").is_dir() else []  # reused replies
    files += [rd / "cells.json", rd / "PRE-REGISTRATION.md"]
    return [str(f) for f in files]


def _sanitize_text(text: str) -> str:
    return text.replace(str(Path.home()), "~")


def _reuse(rd: Path, spec: dict, codes: dict, runs) -> list:
    """Copy replies of reused arms from the source round, for the runs it has. Returns the copies."""
    src = repo() / spec["source"]
    src_code = {name: code for code, name in _load(src, "SEALED.json")["arms"].items()}
    log = json.loads((rd / "reuse.json").read_text()) if (rd / "reuse.json").is_file() else {}
    copied = []
    for arm, cfg in spec["arms"].items():
        if not cfg.get("reuse"):
            continue
        for b in BRIEFS:
            for run in runs:
                s = src / "raw" / f"{b}--{src_code[cfg['reuse']]}--r{run}.md"
                if s.is_file():
                    d = rd / "raw" / f"{b}--{codes[arm]}--r{run}.md"
                    d.parent.mkdir(exist_ok=True)
                    shutil.copy2(s, d)
                    log[d.stem] = str(s.relative_to(repo()))
                    copied.append(d)
    (rd / "reuse.json").write_text(json.dumps(log, indent=1, sort_keys=True))
    return copied


def build(skill: str, seed=None) -> dict:
    rd = round_dir(skill)
    if (rd / "SEALED.json").exists():
        sys.exit(f"{skill}: already built (SEALED.json exists); a frozen round is never rebuilt")
    spec = load_spec(skill)
    src = repo() / spec["source"]
    (rd / "pack").mkdir(parents=True, exist_ok=True)
    for f in PACK_FILES:
        if not (rd / "pack" / f).exists() and (src / "pack" / f).is_file():
            shutil.copy2(src / "pack" / f, rd / "pack" / f)
    problems = validate_pack(rd)
    if problems:
        sys.exit(f"{skill}: pack invalid: " + "; ".join(problems))
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    used, codes = set(), {}
    for arm in spec["arms"]:
        codes[arm] = _code(rng, used, string.ascii_lowercase, string.digits)
    created = []
    try:
        for arm, cfg in spec["arms"].items():
            if cfg.get("skill_ref"):
                _extract(cfg["skill_ref"], skill, rd / "arms" / codes[arm])
                created.append(rd / "arms" / codes[arm])
        _snapshot_harness(rd)
        created.append(rd / "harness")
        cells = [_cell(b, "main", codes[arm], run) for b in BRIEFS for arm in spec["arms"] for run in (1, 2)]
        (rd / "cells.json").write_text(json.dumps(cells, indent=1))
        created.append(rd / "cells.json")
        created += _reuse(rd, spec, codes, (1, 2))
        created.append(rd / "reuse.json")
        text = (rd / "harness" / "PREREG-TEMPLATE.md").read_text()
        arms_text = "; ".join(f"{a} = {c['model']}" + (" with the skill" if c.get("skill_ref") else " alone") +
                              (f" (replies reused from arm '{c['reuse']}' of `{spec['source']}`)" if c.get("reuse") else "")
                              for a, c in spec["arms"].items())
        for k, v in {"skill": skill, "date": datetime.date.today().isoformat(), "arms": arms_text,
                     "source": spec["source"], "cells": str(len(cells)),
                     "freeze": "Recorded in FREEZE.md (written right after registration)."}.items():
            text = text.replace("{" + k + "}", v)
        (rd / "PRE-REGISTRATION.md").write_text(text)
        created.append(rd / "PRE-REGISTRATION.md")
        reg = subprocess.run([sys.executable, str(_scripts(rd) / "freeze.py"), "register", str(rd / "state"),
                              *_freeze_files(rd)], capture_output=True, text=True)
        if reg.returncode != 0:
            raise RuntimeError(reg.stderr.strip() or reg.stdout.strip())
    except (RuntimeError, SystemExit) as e:
        for p in created + [rd / "state"]:
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            else:
                p.unlink(missing_ok=True)
        sys.exit(f"{skill}: build failed and was rolled back: {e}")
    (rd / "FREEZE.md").write_text("# Verifier freeze\n\n```\n" + _sanitize_text(reg.stdout.strip()) + "\n```\n")
    (rd / "SEALED.json").write_text(json.dumps({"arms": {c: a for a, c in codes.items()}}, indent=1))
    set_state(skill, "frozen")
    return {"cells": len(cells), "arms": len(codes)}


def _fill(template: str, **values) -> str:
    for k, v in values.items():
        template = template.replace("{" + k + "}", str(v))
    return template


def _prior_fixtures(skill: str) -> list:
    r = repo()
    found = []
    for pattern in ("evolution/**/fixtures/*.json", "evolution/**/briefs/*.md", "examples/**/*.md",
                    "skills/skill-gauntlet/references/fixtures.md"):
        found += r.glob(pattern)
    own = round_dir(skill).resolve()
    for pack in [*root().glob("*/pack"), *r.glob("evolution/gauntlet-*/*/pack")]:
        if pack.is_dir() and pack.parent.resolve() != own and pack.parent.name != "harness":
            found += [f for f in pack.glob("*.md") if f.name != "notes.md"]
    return sorted({str(f) for f in found})


def render_designer(skill: str) -> Path:
    spec = load_spec(skill)
    rd = round_dir(skill).resolve()
    (rd / "jobs").mkdir(parents=True, exist_ok=True)
    (rd / "pack").mkdir(exist_ok=True)
    avoid = _prior_fixtures(skill)
    text = _fill((root() / "harness" / "prompts" / "designer.md").read_text(), skill=skill,
                 skill_dir=repo() / "skills" / skill, key_type=spec["key_type"], pack=rd / "pack",
                 avoid=("\n" + "\n".join(f"- {a}" for a in avoid)) if avoid else "(none yet)")
    out = rd / "jobs" / "designer.md"
    out.write_text(text)
    return out


def extend(skill: str) -> dict:
    rd = round_dir(skill)
    sealed, cells = _load(rd, "SEALED.json"), _load(rd, "cells.json")
    if sealed.get("extended"):
        sys.exit(f"{skill}: already extended once; the gate allows a single extension")
    added = [_cell(b, "main", code, run) for b in BRIEFS for code in sealed["arms"] for run in (3, 4)]
    (rd / "cells.json").write_text(json.dumps(cells + added, indent=1))
    codes = {name: code for code, name in sealed["arms"].items()}
    reused = _reuse(rd, load_spec(skill), codes, (3, 4))
    am = subprocess.run([sys.executable, str(_scripts(rd) / "freeze.py"), "amend", str(rd / "state"), "--reason",
                         "pre-registered extension: main runs 3-4 for every arm", str(rd / "cells.json"),
                         *[str(p) for p in reused]], capture_output=True, text=True)
    if am.returncode != 0:
        sys.exit(f"{skill}: freeze amend failed: {am.stderr.strip() or am.stdout.strip()}")
    sealed["extended"] = True
    (rd / "SEALED.json").write_text(json.dumps(sealed, indent=1))
    set_state(skill, "frozen")
    return {"added": len(added), "reused": len(reused)}


# ---------------------------------------------------------------- render / blind

def _raw_ok(rd: Path, cell: str) -> bool:
    p = rd / "raw" / f"{cell}.md"
    return p.is_file() and p.read_text().strip() != ""


def _write_jobs(rd: Path, phase: str, jobs: list) -> list:
    (rd / "jobs").mkdir(exist_ok=True)
    (rd / "jobs" / f"{phase}.json").write_text(json.dumps(jobs, indent=1))
    return jobs


def _stage_inputs(rd: Path) -> None:
    """Executors and judges read copies in inputs/, never pack/ (which holds the sealed keys)."""
    (rd / "inputs").mkdir(exist_ok=True)
    for stem in INPUT_STEMS:
        (rd / "inputs" / f"{stem}.md").write_text((rd / "pack" / f"{stem}.md").read_text())
    (rd / "inputs" / "rubric.md").write_text((rd / "harness" / "rubric.md").read_text())


def _auditor_rules(rd: Path) -> str:
    text = (rd / "PRE-REGISTRATION.md").read_text()
    start = text.index("**Auditor rule text")
    return text[start:text.index("No goalpost movement", start)].strip()


def _job(jid: str, prompt: str, model: str, effort: str) -> dict:
    return {"id": jid, "prompt": prompt, "model": model, "effort": effort, "agent": WORKER}


def render(skill: str, phase: str) -> list:
    rd = round_dir(skill).resolve()
    prompts = rd / "harness" / "prompts"
    sealed = _load(rd, "SEALED.json")
    jobs = []
    if phase == "exec":
        _stage_inputs(rd)
        out_dir = rd / "jobs" / "exec"
        out_dir.mkdir(parents=True, exist_ok=True)
        for c in _load(rd, "cells.json"):
            if _raw_ok(rd, c["cell"]):
                continue  # already ran; extensions and re-runs only render what is missing
            cfg = load_spec(skill)["arms"][sealed["arms"][c["arm"]]]
            none = not cfg.get("skill_ref")
            tpl = (prompts / ("executor-none.md" if none else "executor-skill.md")).read_text()
            text = _fill(tpl, skill_dir=rd / "arms" / c["arm"], input=rd / "inputs" / f"{Path(c['input']).stem}.md",
                         output=rd / "raw" / f"{c['cell']}.md", run=rd)
            (out_dir / f"{c['cell']}.md").write_text(text)
            jobs.append(_job(c["cell"], f"jobs/exec/{c['cell']}.md", cfg["model"], "medium"))
        return _write_jobs(rd, "exec", jobs)
    if phase != "judge":
        sys.exit(f"unknown phase {phase}")
    if sealed.get("extended"):
        for d in ("scores", "audit", "keys"):
            if (rd / d).is_dir() and any((rd / d).iterdir()) and not (rd / f"{d}-pre-ext").exists():
                (rd / d).rename(rd / f"{d}-pre-ext")
    plan = _load(rd, "jobs/judge-plan.json")
    out_dir = rd / "jobs" / "judge"
    out_dir.mkdir(parents=True, exist_ok=True)
    blind_path = lambda code: rd / "blind" / f"{code}.md"  # noqa: E731
    for n, (jid, persona) in enumerate(PERSONAS.items()):
        for b in BRIEFS:
            codes = plan["main"][b] if n % 2 == 0 else list(reversed(plan["main"][b]))  # per-judge order
            text = _fill((prompts / "judge.md").read_text(), judge_id=jid, persona=persona, run=rd,
                         input=rd / "inputs" / f"{b}.md", rubric=rd / "inputs" / "rubric.md", n=len(codes),
                         reports="\n".join(f"- {blind_path(c)}" for c in codes), brief=b,
                         output=rd / "scores" / f"{jid}-{b}.md")
            (out_dir / f"{jid}-{b}.md").write_text(text)
            jobs.append(_job(f"{jid}-{b}", f"jobs/judge/{jid}-{b}.md", "opus", "high"))
    mains = [c for b in BRIEFS for c in plan["main"][b]]
    text = _fill((prompts / "auditor.md").read_text(), rule_text=_auditor_rules(rd), run=rd,
                 main_list="\n".join(f"- {blind_path(c)}" for c in mains),
                 pairs_list="\n".join(f"- {p['pair']}: {blind_path(p['codes'][0])} and {blind_path(p['codes'][1])}"
                                      for p in plan["framing_pairs"]),
                 neg_list="\n".join(f"- {blind_path(c)}" for c in plan["negative"]),
                 output=rd / "audit" / "audit.json")
    (out_dir / "auditor.md").write_text(text)
    jobs.append(_job("auditor", "jobs/judge/auditor.md", "sonnet", "high"))
    keys = _load(rd, "pack/keys.json")
    for b in BRIEFS:
        text = _fill((prompts / "verifier.md").read_text(), input=rd / "inputs" / f"{b}.md", run=rd,
                     reports="\n".join(f"- {blind_path(c)}" for c in plan["main"][b]),
                     keys="\n".join(f"- {k['id']}: {k['text']}" for k in keys[b]),
                     output=rd / "keys" / f"{b}.json")
        (out_dir / f"verifier-{b}.md").write_text(text)
        jobs.append(_job(f"verifier-{b}", f"jobs/judge/verifier-{b}.md", "sonnet", "high"))
    for d in ("scores", "audit", "keys"):
        (rd / d).mkdir(exist_ok=True)
    return _write_jobs(rd, "judge", jobs)


def _used_codes() -> set:
    f = root() / "used-codes.json"
    return set(json.loads(f.read_text())) if f.exists() else set()


def blind(skill: str, seed=None, ack=None) -> dict:
    rd = round_dir(skill).resolve()
    cells = _load(rd, "cells.json")
    missing = [c["cell"] for c in cells if not _raw_ok(rd, c["cell"])]
    if missing:
        sys.exit(f"{skill}: missing or empty raw outputs, re-run these cells first: {', '.join(missing)}")
    sealed = _load(rd, "SEALED.json")
    mapping = dict(sealed.get("blind", {}))
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    used = _used_codes() | set(mapping.values())
    for c in cells:
        if f"{c['cell']}.md" not in mapping:
            mapping[f"{c['cell']}.md"] = _code(rng, used, string.ascii_uppercase, string.digits, string.ascii_uppercase)
    (rd / "state").mkdir(exist_ok=True)
    mfile = rd / "state" / "blind-mapping.json"
    mfile.write_text(json.dumps(mapping, indent=1))
    norm = subprocess.run([sys.executable, str(_scripts(rd) / "normalize.py"), str(mfile), str(rd / "raw"),
                           str(rd / "blind"), "--strip-h2-ordinals"], capture_output=True, text=True)
    if norm.returncode != 0:
        sys.exit(f"{skill}: normalize failed: {norm.stderr.strip() or norm.stdout.strip()}")
    scan = [l for l in norm.stdout.split("LEAK SCAN", 1)[-1].splitlines()[1:]
            if l.startswith("  ") and l.strip() != "clean"]
    if scan and not ack:
        sys.exit(f"{skill}: leak scan found {len(scan)} file(s) with arm or version tells; inspect them, then re-run "
                 f"with --ack-leaks '<reason>' if they are harmless:\n" + "\n".join(scan))
    if scan:
        (rd / "leak-ack.md").write_text(f"# Leak-scan acknowledgement\n\nReason: {ack}\n\n" + "\n".join(scan) + "\n")
    sealed["blind"] = mapping
    (rd / "SEALED.json").write_text(json.dumps(sealed, indent=1))
    (root() / "used-codes.json").write_text(json.dumps(sorted(used - RESERVED)))
    code_of = lambda c: mapping[f"{c['cell']}.md"]  # noqa: E731
    plan_file = rd / "jobs" / "judge-plan.json"
    previous = json.loads(plan_file.read_text()) if plan_file.is_file() else None
    plan = {"main": {}, "framing_pairs": [], "negative": []}
    for b in BRIEFS:
        codes = [code_of(c) for c in cells if c["kind"] == "main" and Path(c["input"]).stem == b]
        rng.shuffle(codes)
        plan["main"][b] = codes
    if previous:  # an extension adds main runs only; framing and negative labels must not move
        plan["framing_pairs"], plan["negative"] = previous["framing_pairs"], previous["negative"]
    else:
        framed_arms = [a for a in sealed["arms"] if any(c["kind"] == "framing" and c["arm"] == a for c in cells)]
        rng.shuffle(framed_arms)
        for i, arm in enumerate(framed_arms, 1):
            pair = [code_of(c) for reg in ("framing-hype", "framing-skeptical")
                    for c in cells if c["kind"] == "framing" and c["arm"] == arm and Path(c["input"]).stem == reg]
            plan["framing_pairs"].append({"pair": f"P{i}", "codes": pair})
        plan["negative"] = [code_of(c) for c in cells if c["kind"] == "negative"]
        rng.shuffle(plan["negative"])
    (rd / "jobs").mkdir(exist_ok=True)
    plan_file.write_text(json.dumps(plan, indent=1))
    set_state(skill, "blinded")
    return {"blind": len(mapping), "leak_hits": len(scan)}


# ---------------------------------------------------------------- instrument parsing (strict)

def _norm_code(c: str) -> str:
    c = c.strip().strip("`").upper()
    return c[:-3] if c.endswith(".MD") else c


def _blocks(text: str, kind: str) -> list:
    return re.findall(r"```" + kind + r"\s*\n(.*?)\n\s*```", text, re.S)


def _parse_judge(path: Path, jid: str, brief: str, codes: list, problems: list):
    text = path.read_text()
    tag = path.stem
    scores, ranks = _blocks(text, "scores"), _blocks(text, "ranking")
    if len(scores) != 1 or len(ranks) != 1:
        problems.append(f"{tag}: needs exactly one scores block and one ranking block "
                        f"(found {len(scores)} and {len(ranks)})")
        return [], []
    lines = [l for l in scores[0].strip().splitlines() if l.strip()]
    header = [h.strip().lower() for h in lines[0].split(",")]
    if header != ["judge", "code"] + [d.lower() for d in DIMS] + ["total"]:
        problems.append(f"{tag}: unexpected scores header {lines[0]!r}")
        return [], []
    rows, seen = [], []
    for l in lines[1:]:
        cells = [c.strip() for c in l.split(",")]
        if len(cells) != len(header):
            problems.append(f"{tag}: malformed row {l!r}")
            continue
        code = _norm_code(cells[1])
        try:
            vals = [int(float(x)) if float(x).is_integer() else None for x in cells[2:9]]
        except ValueError:
            vals = [None]
        if cells[0].upper() != jid.upper():
            problems.append(f"{tag}: row judge {cells[0]!r} is not {jid}")
        if code not in codes:
            problems.append(f"{tag}: code {cells[1]!r} is not a reply of {brief}")
        elif any(v is None or not 1 <= v <= 7 for v in vals):
            problems.append(f"{tag}: scores for {code} must be integers 1-7")
        else:
            rows.append({"judge": jid, "code": code, **dict(zip(DIMS, map(float, vals)))})
            seen.append(code)
    if sorted(seen) != sorted(codes):
        problems.append(f"{tag}: must score each of {len(codes)} replies exactly once (missing "
                        f"{sorted(set(codes) - set(seen))}, duplicates {sorted({c for c in seen if seen.count(c) > 1})})")
    order = None
    for l in ranks[0].strip().splitlines():
        parts = l.split(",", 2)
        if len(parts) == 3 and parts[1].strip() == brief:
            order = [_norm_code(c) for c in re.split(r"[\s,]+", parts[2]) if c.strip()]
    if order is None or sorted(order) != sorted(codes):
        problems.append(f"{tag}: ranking must list each reply of {brief} exactly once")
        order = []
    return rows, order


def _check_audit(audit, mains: list, negs: list, pairs: list, problems: list, framing_codes=()) -> None:
    def strlist(x):
        return isinstance(x, list) and all(isinstance(i, str) for i in x)
    if not isinstance(audit, dict):
        problems.append("audit.json: not an object")
        return
    reps = audit.get("reports")
    if isinstance(reps, dict):  # framing replies are judged under "framing" only; stray report entries are dropped
        reps = {k: v for k, v in reps.items() if _norm_code(k) not in set(framing_codes)}
        audit["reports"] = reps
    if not isinstance(reps, dict) or {_norm_code(k) for k in reps} != set(mains) | set(negs):
        problems.append("audit.json: reports must cover exactly every main and negative reply")
    for k, v in (reps.items() if isinstance(reps, dict) else []):
        if not (isinstance(v, dict) and strlist(v.get("ceremony")) and strlist(v.get("leaks"))):
            problems.append(f"audit.json: reports[{k}] needs ceremony and leaks as lists of strings")
    fr = audit.get("framing", {} if not pairs else None)
    if not isinstance(fr, dict) or set(fr) != set(pairs):
        problems.append(f"audit.json: framing must cover exactly {sorted(pairs)}")
    for k, v in (fr.items() if isinstance(fr, dict) else []):
        if not (isinstance(v, dict) and isinstance(v.get("invariant"), bool)):
            problems.append(f"audit.json: framing[{k}].invariant must be true or false")
    ng = audit.get("negative", {} if not negs else None)
    if not isinstance(ng, dict) or {_norm_code(k) for k in ng} != set(negs):
        problems.append("audit.json: negative must cover exactly every negative reply")
    for k, v in (ng.items() if isinstance(ng, dict) else []):
        if not (isinstance(v, dict) and isinstance(v.get("ceremony"), bool)):
            problems.append(f"audit.json: negative[{k}].ceremony must be true or false")


def _quote_text(s: str) -> str:
    return re.sub(r"[\W_]+", " ", s.lower()).strip()


def _check_quotes(audit, rd: Path, problems: list) -> None:
    """Every auditor quote must appear in the reply it is credited to (a trailing "(annotation)" is ignored)."""
    reps = audit.get("reports") if isinstance(audit, dict) else None
    for code, rep in (reps.items() if isinstance(reps, dict) else []):
        path = rd / "blind" / f"{_norm_code(code)}.md"
        text = _quote_text(path.read_text()) if path.is_file() else ""
        for kind in ("ceremony", "leaks"):
            for q in (rep.get(kind) or []) if isinstance(rep, dict) else []:
                core = _quote_text(re.sub(r"\s*\([^)]*\)\s*$", "", str(q)))
                if core and core not in text:
                    problems.append(f"audit.json: {kind} quote not found in {_norm_code(code)}: {str(q)[:60]!r}")


def _parse_keys(data, brief: str, codes: list, key_ids: list, problems: list) -> dict:
    out = {}
    if not isinstance(data, dict):
        problems.append(f"keys/{brief}.json: not an object")
        return out
    norm = {_norm_code(k): v for k, v in data.items()}
    if set(norm) != set(codes):
        problems.append(f"keys/{brief}.json: must grade exactly the {len(codes)} replies of {brief}")
    for code in codes:
        grades = norm.get(code, {})
        rates = []
        for kid in key_ids:
            g = str(grades.get(kid, "")).strip() if isinstance(grades, dict) else ""
            if g not in GRADES:
                problems.append(f"keys/{brief}.json: {code} key {kid} grade {g!r} is not ✓, ~ or ✗")
            else:
                rates.append(GRADES[g])
        out[code] = sum(rates) / len(rates) if rates else 0.0
    return out


def agreement(rows: list) -> float:
    """Share of (code, dim) cells scored by both judges that agree within 1 point."""
    by = {}
    for r in rows:
        by.setdefault(r["code"], {})[r["judge"]] = r
    pairs = [(j[a][d], j[b][d]) for j in by.values() if len(j) >= 2 for a, b in [sorted(j)[:2]] for d in DIMS]
    return sum(abs(x - y) <= 1 for x, y in pairs) / len(pairs) if pairs else 0.0


def ranking_outcomes(orders: list, codes_a: set, codes_b: set) -> tuple:
    """One outcome per ranking: arm a wins if its replies' mean position beats arm b's."""
    wins = losses = 0
    for order in orders:
        pos = {c: i for i, c in enumerate(order)}
        pa = [pos[c] for c in codes_a if c in pos]
        pb = [pos[c] for c in codes_b if c in pos]
        if pa and pb:
            ma, mb = sum(pa) / len(pa), sum(pb) / len(pb)
            wins += ma < mb
            losses += ma > mb
    return wins, losses


def _gates_module(rd: Path):
    name = "gates_" + re.sub(r"\W", "_", str(rd))
    spec = importlib.util.spec_from_file_location(name, rd / "harness" / "gates.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # dataclasses resolve annotations through sys.modules
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- score

def score(skill: str) -> dict:
    rd = round_dir(skill).resolve()
    gates = _gates_module(rd)
    sealed, cells = _load(rd, "SEALED.json"), {c["cell"]: c for c in _load(rd, "cells.json")}
    extended = bool(sealed.get("extended"))
    jobs = _load(rd, "jobs/judge.json")
    paths = {j["id"]: (rd / "scores" / f"{j['id']}.md" if j["id"].startswith("J-") else
                       rd / "audit" / "audit.json" if j["id"] == "auditor" else
                       rd / "keys" / f"{j['id'][len('verifier-'):]}.json") for j in jobs}
    missing = [i for i, p in paths.items() if not p.is_file()]
    if missing:
        sys.exit(f"{skill}: missing instrument outputs, re-run these jobs first: {', '.join(missing)}")
    freeze_ok = subprocess.run([sys.executable, str(_scripts(rd) / "freeze.py"), "verify", str(rd / "state")],
                               capture_output=True, text=True).returncode == 0
    info = {}
    for fname, code in sealed["blind"].items():
        c = cells[fname[:-3]]
        info[code] = {"arm": sealed["arms"][c["arm"]], "kind": c["kind"], "stem": Path(c["input"]).stem}
    plan = _load(rd, "jobs/judge-plan.json")
    problems, rows, orders = [], [], []
    for jid in PERSONAS:
        for b in BRIEFS:
            r, o = _parse_judge(rd / "scores" / f"{jid}-{b}.md", jid, b, plan["main"][b], problems)
            rows += r
            orders.append(o)
    try:
        audit = _load(rd, "audit/audit.json")
    except json.JSONDecodeError as e:
        audit = None
        problems.append(f"audit.json: not valid JSON ({e})")
    mains = [c for b in BRIEFS for c in plan["main"][b]]
    _check_audit(audit, mains, plan["negative"], [p["pair"] for p in plan["framing_pairs"]], problems,
                 framing_codes=[c for p in plan["framing_pairs"] for c in p["codes"]])
    if not problems:
        _check_quotes(audit, rd, problems)
    pack_keys = _load(rd, "pack/keys.json")
    key_rate = {}
    for b in BRIEFS:
        try:
            data = _load(rd, f"keys/{b}.json")
        except json.JSONDecodeError as e:
            problems.append(f"keys/{b}.json: not valid JSON ({e})")
            continue
        key_rate.update(_parse_keys(data, b, plan["main"][b], [k["id"] for k in pack_keys[b]], problems))
    if problems:
        sys.exit(f"{skill}: instrument outputs failed validation; re-run the named jobs with identical prompts:\n- "
                 + "\n- ".join(problems))
    reports = {_norm_code(k): v for k, v in audit["reports"].items()}
    words = {c: len((rd / "blind" / f"{c}.md").read_text().split()) for c in info}
    per_reply = {}
    for r in rows:
        per_reply.setdefault(r["code"], []).append(r)
    reply_mean = {c: {d: sum(x[d] for x in rs) / len(rs) for d in DIMS} for c, rs in per_reply.items()}
    arm_codes = lambda arm, b: [c for c in plan["main"][b] if info[c]["arm"] == arm]  # noqa: E731
    base_median = {b: statistics.median(words[c] for c in arm_codes("sn", b)) for b in BRIEFS}
    stats = {}
    for arm in dict.fromkeys(sealed["arms"].values()):
        arm_mains = [c for c in mains if info[c]["arm"] == arm]
        briefs = {}
        for b in BRIEFS:
            cs = arm_codes(arm, b)
            dims = {d: sum(reply_mean[c][d] for c in cs) / len(cs) for d in DIMS}
            dims["value"] = sum(dims[d] for d in gates.VALUES) / len(gates.VALUES)
            dims["key"] = sum(key_rate[c] for c in cs) / len(cs)
            briefs[b] = dims
        stats[arm] = gates.ArmStats(
            judge={d: sum(reply_mean[c][d] for c in arm_mains) / len(arm_mains) for d in DIMS}, briefs=briefs,
            audit_ceremony=sum(len(reports[c]["ceremony"]) for c in arm_mains) / len(arm_mains),
            audit_leaks=sum(len(reports[c]["leaks"]) for c in arm_mains) / len(arm_mains),
            n_replies=len(arm_mains),
            word_ratio=sum(statistics.median(words[c] for c in arm_codes(arm, b)) / max(1, base_median[b])
                           for b in BRIEFS) / len(BRIEFS),
            key_rate=sum(key_rate[c] for c in arm_mains) / len(arm_mains),
            negative_ok=True, framing_ok=True)  # this program runs main briefs only
    codes_of = lambda arm: {c for c in mains if info[c]["arm"] == arm}  # noqa: E731
    agree = agreement(rows)
    w, l = ranking_outcomes(orders, codes_of("hs"), codes_of("sn"))
    reaches = gates.reaches_gate(stats["hs"], stats["sn"], w, l, agree, freeze_ok)
    reaches["verdict"] = gates.finalize("reaches", reaches["verdict"], extended)
    uplift = {}
    for name, a, b in (("haiku_uplift", "hs", "hn"), ("sonnet_uplift", "ss", "sn")):
        wa, la = ranking_outcomes(orders, codes_of(a), codes_of(b))
        g = gates.validation_gate(stats[a], stats[b], wa, la, agree, freeze_ok)
        g["conditions"] = {k: v for k, v in g["conditions"].items() if k not in ("negative", "framing")}
        g["verdict"] = gates.finalize("validation", g["verdict"], extended)
        uplift[name] = g
    verdict = {"skill": skill, "reaches": reaches, **uplift, "agreement": round(agree, 3),
               "freeze_ok": freeze_ok, "extended": extended,
               "arms": {a: {"value_mean": round(s.value_mean, 2), **{d: round(s.judge[d], 2) for d in DIMS},
                            "key_rate": round(s.key_rate, 3), "ceremony": round(s.audit_ceremony, 2),
                            "leaks": round(s.audit_leaks, 2), "word_ratio": round(s.word_ratio, 2)}
                        for a, s in stats.items()}}
    (rd / "verdict.json").write_text(json.dumps(verdict, indent=1, ensure_ascii=False))
    lines = [f"# Scorecard: {skill}", "",
             f"Agreement {agree:.2f} · freeze {'OK' if freeze_ok else 'FAILED'} · extended {extended}", "",
             "| arm | value | " + " | ".join(DIMS) + " | keys | ceremony | leaks | length vs sn |",
             "|---" * (len(DIMS) + 6) + "|"]
    for a in ("hs", "hn", "ss", "sn"):
        s = stats[a]
        lines.append(f"| {a} | {s.value_mean:.2f} | " + " | ".join(f"{s.judge[d]:.2f}" for d in DIMS) +
                     f" | {s.key_rate:.2f} | {s.audit_ceremony:.2f} | {s.audit_leaks:.2f} | {s.word_ratio:.2f} |")
    for title, g, a, b in (("Haiku+skill reaches Sonnet alone (hs vs sn)", reaches, "hs", "sn"),
                           ("Haiku uplift (hs vs hn)", uplift["haiku_uplift"], "hs", "hn"),
                           ("Sonnet uplift (ss vs sn)", uplift["sonnet_uplift"], "ss", "sn")):
        vm, vb = gates.paired(stats[a], stats[b], "value")
        km, kb = gates.paired(stats[a], stats[b], "key")
        lines += ["", f"**{title}: {g['verdict']}** · rankings won {g['wins']}, lost {g['losses']} · "
                      f"value margin {vm:+.2f} (band {vb:.2f}) · key margin {km:+.2f} (band {kb:.2f})",
                  " · ".join(f"{k} {v}" for k, v in g["conditions"].items())]
    (rd / "scorecard.md").write_text("\n".join(lines) + "\n")
    if get_state(skill) != "applied":  # re-scoring a finished round must not reopen it
        set_state(skill, "scored", validation=reaches["verdict"], rewrite=uplift["haiku_uplift"]["verdict"])
    return verdict


# ---------------------------------------------------------------- apply

def _sanitize_round(rd: Path) -> None:
    for p in rd.rglob("*"):
        if p.is_file() and "state" not in p.relative_to(rd).parts and p.suffix in (".md", ".json", ".txt", ".js", ".py"):
            text = p.read_text()
            if str(Path.home()) in text:
                p.write_text(_sanitize_text(text))


def apply(skill: str, accept_inconclusive_uplift: str = None) -> dict:
    """This program changes no skill and no README row: apply records the verdict and the research note.

    An INCONCLUSIVE uplift comparison (hs vs hn, ss vs sn) is accepted only with a recorded reason, as a
    disclosed ruling; an INCONCLUSIVE reaches verdict never is.
    """
    rd = round_dir(skill)
    if get_state(skill) == "applied":
        sys.exit(f"{skill}: already applied; a verdict is applied exactly once")
    v = _load(rd, "verdict.json")
    verdicts = [v["reaches"]["verdict"], v["haiku_uplift"]["verdict"], v["sonnet_uplift"]["verdict"]]
    if "VOID" in verdicts:
        sys.exit(f"{skill}: verdict is VOID (freeze verify failed); the round must be re-run, not applied")
    if verdicts[0] == "INCONCLUSIVE" or ("INCONCLUSIVE" in verdicts[1:] and not accept_inconclusive_uplift):
        sys.exit(f"{skill}: verdict is INCONCLUSIVE; run round.py extend and the extension cells first")
    if not (rd / "research-note.md").exists():
        note = [f"# Research note: {skill} (Haiku uplift)", "",
                f"- Haiku with the skill vs Sonnet alone: **{verdicts[0]}**",
                f"- Haiku with the skill vs Haiku alone: **{verdicts[1]}**",
                f"- Sonnet with the skill vs Sonnet alone: **{verdicts[2]}**",
                f"- Agreement {v.get('agreement')}, freeze {'OK' if v.get('freeze_ok') else 'FAILED'}, "
                f"extended {v.get('extended')}"]
        for a, s in v.get("arms", {}).items():
            note.append(f"- {a}: value {s.get('value_mean')}, keys {s.get('key_rate')}, ceremony {s.get('ceremony')}, "
                        f"leaks {s.get('leaks')}, length x{s.get('word_ratio')} of sn")
        if accept_inconclusive_uplift and "INCONCLUSIVE" in verdicts[1:]:
            note.append(f"- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. "
                        f"Reason: {accept_inconclusive_uplift}")
        note += ["", "## Autopsy", "", "(The coordinator writes 3 to 5 lines here from scorecard.md.)", ""]
        (rd / "research-note.md").write_text("\n".join(note))
    _sanitize_round(rd)
    set_state(skill, "applied", validation=verdicts[0], rewrite=verdicts[1])
    return {"reaches": verdicts[0], "haiku_uplift": verdicts[1]}


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("build", "blind", "score", "apply", "render-designer", "extend"):
        sp = sub.add_parser(name)
        sp.add_argument("skill")
        if name == "apply":
            sp.add_argument("--accept-inconclusive-uplift", default=None,
                            help="recorded reason for applying with an INCONCLUSIVE uplift comparison")
        if name == "blind":
            sp.add_argument("--ack-leaks", default=None, help="reason the leak-scan hits are harmless")
    r = sub.add_parser("render")
    r.add_argument("skill")
    r.add_argument("phase", choices=["exec", "judge"])
    m = sub.add_parser("mark")
    m.add_argument("skill")
    m.add_argument("state", choices=STATES)
    sub.add_parser("status")
    args = ap.parse_args(argv)
    if args.cmd == "build":
        res = build(args.skill)
        print(f"{args.skill}: built {res['cells']} cells across {res['arms']} arms; state frozen")
    elif args.cmd == "render-designer":
        print(f"{args.skill}: designer prompt -> {render_designer(args.skill)}")
    elif args.cmd == "render":
        jobs = render(args.skill, args.phase)
        print(f"{args.skill}: rendered {len(jobs)} {args.phase} jobs -> jobs/{args.phase}.json")
    elif args.cmd == "blind":
        res = blind(args.skill, ack=args.ack_leaks)
        print(f"{args.skill}: blinded {res['blind']} replies; leak-scan hits: {res['leak_hits']}; state blinded")
    elif args.cmd == "score":
        score(args.skill)
        print((round_dir(args.skill) / "scorecard.md").read_text())
    elif args.cmd == "apply":
        res = apply(args.skill, accept_inconclusive_uplift=args.accept_inconclusive_uplift)
        print(f"{args.skill}: applied; reaches sonnet: {res['reaches']}; haiku uplift: {res['haiku_uplift']}")
    elif args.cmd == "extend":
        print(f"{args.skill}: extension added {extend(args.skill)['added']} cells; state frozen")
    elif args.cmd == "mark":
        mark(args.skill, args.state)
        print(f"{args.skill}: state {args.state}")
    elif args.cmd == "status":
        print(status())
    return 0


if __name__ == "__main__":
    sys.exit(main())
