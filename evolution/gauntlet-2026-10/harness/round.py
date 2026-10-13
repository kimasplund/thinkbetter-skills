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


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build").add_argument("skill")
    args = ap.parse_args(argv)
    if args.cmd == "build":
        r = build(args.skill)
        print(f"{args.skill}: built {r['cells']} cells across {r['arms']} arms; state frozen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
