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
            if (rd / "raw" / f"{c['cell']}.md").is_file():
                continue  # already ran; extensions and re-runs only render what is missing
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


def _prior_fixtures(skill: str) -> list:
    r = repo()
    found = []
    for pattern in ("evolution/**/fixtures/*.json", "evolution/**/briefs/*.md", "examples/**/*.md",
                    "skills/skill-gauntlet/references/fixtures.md"):
        found += r.glob(pattern)
    for other in root().iterdir():
        if other.is_dir() and other.name not in (skill, "harness"):
            pack = other / "pack"
            found += [f for f in pack.glob("*.md") if f.name != "notes.md"] if pack.is_dir() else []
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
    added = []
    for b in BRIEFS:
        for code in sealed["arms"]:
            for run in (3, 4):
                added.append(_cell(b, "main", code, run))
    (rd / "cells.json").write_text(json.dumps(cells + added, indent=1))
    sealed["extended"] = True
    (rd / "SEALED.json").write_text(json.dumps(sealed, indent=1))
    set_state(skill, "frozen")
    return {"added": len(added)}


# ---------------------------------------------------------------- score

DIMS = ["V1", "V2", "V3", "V4", "G1", "G2", "G3"]
GRADE = {"✓": 1.0, "~": 0.5, "✗": 0.0}
RANKING_RE = __import__("re").compile(r"```ranking\s*\n(.*?)\n```", __import__("re").S)


def agreement(rows: list) -> float:
    """Share of (code, dim) cells scored by both judges that agree within 1 point."""
    by = {}
    for r in rows:
        by.setdefault(r["code"], {})[r["judge"]] = r
    pairs = [(j[a][d], j[b][d]) for j in by.values() if len(j) >= 2
             for a, b in [sorted(j)[:2]] for d in DIMS]
    return sum(abs(x - y) <= 1 for x, y in pairs) / len(pairs) if pairs else 0.0


def pairwise(rankings: list, codes_a: set, codes_b: set) -> tuple:
    wins = losses = 0
    for order in rankings:
        pos = {c: i for i, c in enumerate(order)}
        for a in codes_a & pos.keys():
            for b in codes_b & pos.keys():
                wins += pos[a] < pos[b]
                losses += pos[a] > pos[b]
    return wins, losses


def _words(path: Path) -> int:
    return len(path.read_text().split())


def score(skill: str, extended: bool = False) -> dict:
    sys.path.insert(0, str(HERE))
    sys.path.insert(0, str(GAUNTLET_SCRIPTS))
    import gates
    import scorecard

    rd = round_dir(skill).resolve()
    jobs = _load(rd, "jobs/judge.json")
    expected = {j["id"]: (rd / "scores" / f"{j['id']}.md" if j["id"].startswith("J-") else
                          rd / "audit" / "audit.json" if j["id"] == "auditor" else
                          rd / "keys" / f"{j['id'][len('verifier-'):]}.json") for j in jobs}
    missing = [i for i, p in expected.items() if not p.is_file()]
    if missing:
        sys.exit(f"{skill}: missing instrument outputs, re-run these jobs first: {', '.join(missing)}")
    freeze_ok = subprocess.run([sys.executable, str(GAUNTLET_SCRIPTS / "freeze.py"), "verify", str(rd / "state")],
                               capture_output=True, text=True).returncode == 0

    sealed, cells = _load(rd, "SEALED.json"), {c["cell"]: c for c in _load(rd, "cells.json")}
    info = {}
    for fname, code in sealed["blind"].items():
        c = cells[fname[:-3]]
        info[code] = {"arm": sealed["arms"][c["arm"]], "kind": c["kind"], "stem": Path(c["input"]).stem}
    rows, _dims = scorecard.load(str(rd / "scores"))
    rankings = []
    for f in sorted((rd / "scores").glob("*.md")):
        for block in RANKING_RE.findall(f.read_text()):
            for line in block.strip().splitlines()[1:]:
                parts = line.split(",", 2)
                if len(parts) == 3:
                    rankings.append(parts[2].split())
    audit = _load(rd, "audit/audit.json")
    keyfiles = {b: _load(rd, f"keys/{b}.json") for b in BRIEFS}
    plan = _load(rd, "jobs/judge-plan.json")

    arms = list(dict.fromkeys(sealed["arms"].values()))
    neg_code = {info[c]["arm"]: c for c in plan["negative"]}
    none_words = _words(rd / "blind" / f"{neg_code['none']}.md")
    stats = {}
    for arm in arms:
        mains = [c for c, i in info.items() if i["arm"] == arm and i["kind"] == "main"]
        per = {c: {d: [] for d in DIMS} for c in mains}
        for r in rows:
            if r["code"] in per:
                for d in DIMS:
                    per[r["code"]][d].append(r[d])
        means = {c: {d: sum(v) / len(v) for d, v in ds.items() if v} for c, ds in per.items()}
        scored = [m for m in means.values() if len(m) == len(DIMS)]
        judge = {d: sum(m[d] for m in scored) / len(scored) for d in DIMS}
        spread = {d: max(m[d] for m in scored) - min(m[d] for m in scored) for d in DIMS}
        vals = [sum(m[d] for d in gates.VALUES) / 4 for m in scored]
        spread["value"] = max(vals) - min(vals)
        krates = []
        for c in mains:
            grades = [GRADE.get(g, 0.0) for k, g in keyfiles[info[c]["stem"]].get(c, {}).items() if k != "evidence"]
            krates.append(sum(grades) / len(grades) if grades else 0.0)
        rep = audit["reports"]
        nc = neg_code[arm]
        pair = next((p for p in plan["framing_pairs"] if p["codes"] and info[p["codes"][0]]["arm"] == arm), None)
        stats[arm] = gates.ArmStats(
            judge=judge, spread=spread,
            audit_ceremony=sum(len(rep.get(c, {}).get("ceremony", [])) for c in mains) / len(mains),
            audit_leaks=sum(len(rep.get(c, {}).get("leaks", [])) for c in mains) / len(mains),
            key_rate=sum(krates) / len(krates), key_spread=max(krates) - min(krates),
            negative_ok=(_words(rd / "blind" / f"{nc}.md") <= 1.5 * none_words
                         and not audit.get("negative", {}).get(nc, {}).get("ceremony", False)),
            framing_ok=None if pair is None else bool(audit.get("framing", {}).get(pair["pair"], {}).get("invariant")))
    codes_of = lambda arm: {c for c, i in info.items() if i["arm"] == arm and i["kind"] == "main"}  # noqa: E731
    agree = agreement(rows)
    w, l = pairwise(rankings, codes_of("new"), codes_of("none"))
    val = gates.validation_gate(stats["new"], stats["none"], w, l, agree, freeze_ok)
    val["verdict"] = gates.finalize("validation", val["verdict"], extended)
    rew = None
    if "old" in stats:
        rew = gates.rewrite_gate(stats["new"], stats["old"], freeze_ok, agree)
        rew["wins"], rew["losses"] = pairwise(rankings, codes_of("new"), codes_of("old"))
        rew["verdict"] = gates.finalize("rewrite", rew["verdict"], extended)
    verdict = {"skill": skill, "validation": val, "rewrite": rew, "agreement": round(agree, 3),
               "freeze_ok": freeze_ok, "extended": extended,
               "arms": {a: {"value_mean": round(s.value_mean, 2), **{d: round(s.judge[d], 2) for d in DIMS},
                            "key_rate": round(s.key_rate, 3), "ceremony": round(s.audit_ceremony, 2),
                            "leaks": round(s.audit_leaks, 2), "negative_ok": s.negative_ok,
                            "framing_ok": s.framing_ok, "value_spread": round(s.spread["value"], 2)}
                        for a, s in stats.items()}}
    (rd / "verdict.json").write_text(json.dumps(verdict, indent=1, ensure_ascii=False))
    lines = [f"# Scorecard: {skill}", "",
             f"Agreement {agree:.2f} · freeze {'OK' if freeze_ok else 'FAILED'} · extended {extended}", "",
             "| arm | value | " + " | ".join(DIMS) + " | keys | ceremony | leaks | negative | framing |",
             "|---" * (len(DIMS) + 7) + "|"]
    for a, s in stats.items():
        lines.append(f"| {a} | {s.value_mean:.2f}±{s.spread['value']:.2f} | " +
                     " | ".join(f"{s.judge[d]:.2f}" for d in DIMS) +
                     f" | {s.key_rate:.2f} | {s.audit_ceremony:.2f} | {s.audit_leaks:.2f} | "
                     f"{'ok' if s.negative_ok else 'FAIL'} | {'-' if s.framing_ok is None else ('ok' if s.framing_ok else 'FAIL')} |")
    for name, g in (("Validation (new vs none)", val), ("Rewrite (new vs old)", rew)):
        if g:
            lines += ["", f"**{name}: {g['verdict']}**" + (f" (wins {g['wins']}, losses {g['losses']})" if "wins" in g else ""),
                      " · ".join(f"{k} {v}" for k, v in g["conditions"].items())]
    (rd / "scorecard.md").write_text("\n".join(lines) + "\n")
    set_state(skill, "scored", validation=val["verdict"], rewrite=rew["verdict"] if rew else "-")
    return verdict


# ---------------------------------------------------------------- apply / status

VALIDATION_TEXT = {"VALIDATED": "validated", "NOT VALIDATED": "not validated", "VOID": "void (re-run)"}


def mark(skill: str, state: str) -> None:
    set_state(skill, state)


def status() -> str:
    lines, idx = _rows()
    nxt = next((c[1] for c in ([x.strip() for x in lines[i].strip("|").split("|")] for i in idx)
                if c[2] != "applied"), None)
    table = "\n".join(lines[i] for i in [idx[0] - 2, idx[0] - 1] + idx) if idx else ""
    return table + f"\n\nnext: {nxt or 'none (program complete)'}"


def _revert(skill: str) -> None:
    """Make skills/<skill> exactly its v1.0.0 files, keeping the current frontmatter, patch-bumped."""
    import re
    sd = repo() / "skills" / skill
    current = (sd / "SKILL.md").read_text()
    fm_text = current[:current.find("\n---", 4) + 4]

    def bump(m):
        major, minor, patch = (int(x) for x in m.group(2).split("."))
        return f"{m.group(1)}{major}.{minor}.{patch + 1}{m.group(3)}"
    fm_text, n = re.subn(r'(\n  version: ")(\d+\.\d+\.\d+)(")', bump, fm_text, count=1)
    if n != 1:
        sys.exit(f"{skill}: cannot find metadata.version in frontmatter")
    old = subprocess.run(["git", "-C", str(repo()), "show", f"v1.0.0:skills/{skill}/SKILL.md"],
                         capture_output=True, text=True, check=True).stdout
    old_body = old[old.find("\n---", 4) + 4:]
    for p in sorted(sd.rglob("*"), reverse=True):
        if p.is_file():
            p.unlink()
        elif p.is_dir():
            p.rmdir()
    _extract("v1.0.0", skill, sd)
    (sd / "SKILL.md").write_text(fm_text + old_body)


def apply(skill: str) -> dict:
    rd = round_dir(skill)
    v = _load(rd, "verdict.json")
    val = v["validation"]["verdict"]
    rew = v["rewrite"]["verdict"] if v.get("rewrite") else None
    if "INCONCLUSIVE" in (val, rew):
        sys.exit(f"{skill}: verdict is INCONCLUSIVE; run the extension (round.py extend) and score --extended first")
    reverted = rew == "REVERT"
    if reverted:
        _revert(skill)
        check = subprocess.run([sys.executable, str(HERE.parent.parent.parent / "scripts" / "validate_skills.py"),
                                "--repo", str(repo())], capture_output=True, text=True)
        if check.returncode != 0:
            sys.exit(f"{skill}: revert left the repo invalid:\n{check.stdout}")
    status_text = f"Gauntlet 2026-10: {VALIDATION_TEXT[val]}"
    if rew:
        status_text += "; rewrite kept" if rew == "KEEP" else "; rewrite reverted"
    status_text += f" ([scorecard](evolution/gauntlet-2026-10/{skill}/scorecard.md))"
    readme = repo() / "README.md"
    lines = readme.read_text().split("\n")
    for i, l in enumerate(lines):
        if l.startswith(f"| [{skill}](skills/{skill}/) |"):
            cells = l.split(" | ")
            cells[-1] = status_text + " |"
            lines[i] = " | ".join(cells)
    readme.write_text("\n".join(lines))
    arms = v.get("arms", {})
    note = [f"# Research note: {skill}", "",
            f"- Validation (new vs none): **{val}**" + (f"; rewrite (new vs old): **{rew}**" if rew else ""),
            f"- Agreement {v.get('agreement')}, freeze {'OK' if v.get('freeze_ok') else 'FAILED'}, "
            f"extended {v.get('extended')}"]
    for a, s in arms.items():
        note.append(f"- {a}: value {s.get('value_mean')} (spread {s.get('value_spread')}), keys {s.get('key_rate')}, "
                    f"ceremony {s.get('ceremony')}, leaks {s.get('leaks')}, negative "
                    f"{'ok' if s.get('negative_ok') else 'FAIL'}, framing {s.get('framing_ok')}")
    note += ["", "## Autopsy", "", "(The coordinator writes 3 to 5 lines here from scorecard.md: what drove the verdict, "
             "design vs compliance, anything not chased.)", ""]
    (rd / "research-note.md").write_text("\n".join(note))
    set_state(skill, "applied", validation=val, rewrite=rew or "-")
    return {"readme": status_text, "reverted": reverted}


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build").add_argument("skill")
    r = sub.add_parser("render")
    r.add_argument("skill")
    r.add_argument("phase", choices=["exec", "judge"])
    sub.add_parser("blind").add_argument("skill")
    s = sub.add_parser("score")
    s.add_argument("skill")
    s.add_argument("--extended", action="store_true")
    sub.add_parser("apply").add_argument("skill")
    m = sub.add_parser("mark")
    m.add_argument("skill")
    m.add_argument("state", choices=STATES)
    sub.add_parser("status")
    sub.add_parser("render-designer").add_argument("skill")
    sub.add_parser("extend").add_argument("skill")
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
    elif args.cmd == "score":
        score(args.skill, extended=args.extended)
        print((round_dir(args.skill) / "scorecard.md").read_text())
    elif args.cmd == "apply":
        r = apply(args.skill)
        print(f"{args.skill}: applied; README -> {r['readme']}; reverted: {r['reverted']}")
    elif args.cmd == "mark":
        mark(args.skill, args.state)
        print(f"{args.skill}: state {args.state}")
    elif args.cmd == "status":
        print(status())
    elif args.cmd == "render-designer":
        print(f"{args.skill}: designer prompt -> {render_designer(args.skill)}")
    elif args.cmd == "extend":
        print(f"{args.skill}: extension added {extend(args.skill)['added']} cells; state frozen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
