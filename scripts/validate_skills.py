#!/usr/bin/env python3
"""Validate every skill against the Agent Skills spec and scan tracked files for private data.

Usage: validate_skills.py [--repo PATH]

Skill checks (skills/<dir>/SKILL.md): frontmatter parses; name is spec-valid and equals
<dir>; description is 1-1024 chars; metadata maps strings to strings and carries a semver
metadata.version; every Markdown link into references/, scripts/ or assets/ resolves.

Privacy checks (every `git ls-files` path): no /home/<user>/ paths, no email address other
than noreply@anthropic.com, nothing from the optional local .privacy-denylist (one
case-insensitive literal per line, '#' lines ignored; the file itself is git-ignored).

Exit 0 only when everything passes.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
LINK_RE = re.compile(r"\]\(((?:references|scripts|assets)/[^)#\s]+)")
HOME_RE = re.compile(r"/home/[a-z_][a-z0-9_-]*/")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
EMAIL_ALLOW = {"noreply@anthropic.com"}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("no frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, text[end + 4:].lstrip("\n")


def check_skill(skill_dir: Path) -> list[str]:
    tag = f"{skill_dir.name}: "
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [tag + "missing SKILL.md"]
    try:
        meta, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except (ValueError, yaml.YAMLError) as e:
        return [tag + f"frontmatter: {e}"]

    errors = []
    name = meta.get("name")
    if not isinstance(name, str) or len(name) > 64 or not NAME_RE.match(name):
        errors.append(tag + f"invalid name {name!r}")
    elif name != skill_dir.name:
        errors.append(tag + f"name {name!r} does not match directory")

    desc = meta.get("description")
    if not isinstance(desc, str) or not 1 <= len(desc.strip()) <= 1024:
        errors.append(tag + f"description must be 1-1024 chars (got {len(desc) if isinstance(desc, str) else desc!r})")

    md = meta.get("metadata")
    if not isinstance(md, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in md.items()):
        errors.append(tag + "metadata must map strings to strings")
    if not isinstance(md, dict) or not SEMVER_RE.match(str(md.get("version", ""))):
        errors.append(tag + "metadata.version must be a semver string")

    for target in LINK_RE.findall(body):
        if not (skill_dir / target).exists():
            errors.append(tag + f"broken link {target}")
    return errors


def check_privacy(repo: Path, files: list[str], denylist: list[str]) -> list[str]:
    deny = [d.lower() for d in denylist]
    hits = []
    for rel in files:
        try:
            lines = (repo / rel).read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            continue
        for n, line in enumerate(lines, 1):
            if HOME_RE.search(line):
                hits.append(f"{rel}:{n}: home path")
            for m in EMAIL_RE.finditer(line):
                if m.group(0).lower() not in EMAIL_ALLOW:
                    hits.append(f"{rel}:{n}: email {m.group(0)}")
            low = line.lower()
            for d in deny:
                if d in low:
                    hits.append(f"{rel}:{n}: denylisted term")
    return hits


def tracked_files(repo: Path) -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=repo, capture_output=True, text=True, check=True)
    return out.stdout.splitlines()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args(argv)
    repo = args.repo

    skill_dirs = sorted(p for p in (repo / "skills").iterdir() if p.is_dir()) if (repo / "skills").is_dir() else []
    errors = [e for d in skill_dirs for e in check_skill(d)]

    denylist_file = repo / ".privacy-denylist"
    denylist = []
    if denylist_file.is_file():
        denylist = [l.strip() for l in denylist_file.read_text().splitlines() if l.strip() and not l.startswith("#")]
    files = tracked_files(repo)
    errors += check_privacy(repo, files, denylist)

    for e in errors:
        print(f"FAIL {e}")
    if errors:
        return 1
    print(f"OK: {len(skill_dirs)} skills, {len(files)} files scanned"
          + (f" (denylist: {len(denylist)} terms)" if denylist else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
