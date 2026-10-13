#!/usr/bin/env python3
"""Build claude.ai / Claude Desktop upload zips, one per skill.

Usage: build_zips.py [--with-overlays] [--out DIR] [skill ...]

Each zip has the skill folder at its root. SKILL.md frontmatter is reduced to the six
Agent Skills spec keys, because claude.ai rejects Claude Code-only keys (model, context,
agent, user-invocable, ...). Files come from `git ls-files`, so local overlays excluded
via .gitignore or .git/info/exclude never ship; --with-overlays adds them back for a
personal upload.
"""
import argparse
import subprocess
import sys
import zipfile
from pathlib import Path

import yaml

from validate_skills import parse_frontmatter

SPEC_KEYS = ("name", "description", "license", "compatibility", "metadata", "allowed-tools")


def strip_frontmatter(text: str) -> str:
    meta, _ = parse_frontmatter(text)
    body = text[text.find("\n---", 4) + 4:]
    kept = {k: meta[k] for k in SPEC_KEYS if k in meta}
    return "---\n" + yaml.safe_dump(kept, sort_keys=False, allow_unicode=True, width=10**6) + "---" + body


def skill_files(repo: Path, skill: str, with_overlays: bool) -> list[str]:
    def ls(*flags: str) -> list[str]:
        out = subprocess.run(["git", "ls-files", *flags, "--", f"skills/{skill}"],
                             cwd=repo, capture_output=True, text=True, check=True)
        return out.stdout.splitlines()

    files = ls()
    if with_overlays:
        files += ls("--others", "--ignored", "--exclude-standard")
    return sorted(f for f in set(files) if "__pycache__" not in f)


def build_zip(repo: Path, skill: str, out_dir: Path, with_overlays: bool = False) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{skill}.zip"
    prefix = f"skills/{skill}/"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in skill_files(repo, skill, with_overlays):
            arcname = f"{skill}/{rel[len(prefix):]}"
            if rel == prefix + "SKILL.md":
                z.writestr(arcname, strip_frontmatter((repo / rel).read_text(encoding="utf-8")))
            else:
                z.write(repo / rel, arcname)
    return target


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--with-overlays", action="store_true")
    ap.add_argument("--out", type=Path, default=Path("dist"))
    ap.add_argument("skills", nargs="*")
    args = ap.parse_args(argv)
    repo = Path(__file__).resolve().parent.parent
    skills = args.skills or sorted(p.name for p in (repo / "skills").iterdir() if p.is_dir())
    out = args.out if args.out.is_absolute() else Path.cwd() / args.out
    for skill in skills:
        path = build_zip(repo, skill, out, args.with_overlays)
        print(f"{path} ({len(zipfile.ZipFile(path).namelist())} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
