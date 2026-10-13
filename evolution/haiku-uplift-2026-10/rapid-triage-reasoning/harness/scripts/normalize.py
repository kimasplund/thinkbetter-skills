#!/usr/bin/env python3
"""Normalize raw executor outputs into blind judge-facing copies.

Usage: normalize.py <mapping.json> <raw_dir> <blind_dir> [--strip-h2-ordinals] [extra_leak_regex ...]
       normalize.py -h | --help

Python 3, standard library only.
mapping.json: flat {"<raw filename>.md": "<CODE>", ...} (also accepted nested under
any keys), or the nested form {"main": {brief: {cell: CODE}}, "framing"|"fixture"|
"controls"|"neutral": {cell: CODE}} for raw files named <brief>-<cell>.md. Codes
become <CODE>.md in blind_dir. Exits 1 with a warning if nothing could be mapped.
Leak scan reports regex hits for manual inspection; NEVER auto-fixes (a hit may
be natural language, e.g. 'they champion it').
Coordinator-only: the mapping file must never reach judges or executors.
"""
import json, os, re, sys, hashlib

DEFAULT_LEAKS = [
    (re.compile(r"(?i)\b(skill\.md|the skill|this skill|skill's)\b"), "method"),
    (re.compile(r"(?i)\b(champion|challenger|candidate)\b"), "version"),
]

def collect(obj, out):
    """Gather flat {"raw.md": "CODE"} pairs from any depth of the mapping."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k.endswith(".md") and isinstance(v, str):
                out[k] = v
            else:
                collect(v, out)
    elif isinstance(obj, list):
        for v in obj: collect(v, out)
    return out

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)
    argv = [a for a in sys.argv[1:] if a != "--strip-h2-ordinals"]
    strip_ordinals = "--strip-h2-ordinals" in sys.argv[1:]
    if len(argv) < 3:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(2)
    mapping_path, raw_dir, blind_dir = argv[0], argv[1], argv[2]
    extra = [(re.compile(p, re.I), "extra") for p in argv[3:]]
    patterns = DEFAULT_LEAKS + extra
    with open(mapping_path) as fh:
        mapping = json.load(fh)

    raw2code = {}
    main = mapping.get("main", {}) if isinstance(mapping, dict) else {}
    for brief, cells in main.items():
        if not isinstance(cells, dict): continue
        for cell, code in cells.items():
            if isinstance(code, str): raw2code[f"{brief}-{cell}.md"] = code
    for section in ("framing", "fixture", "controls", "neutral"):
        cells = mapping.get(section, {}) if isinstance(mapping, dict) else {}
        if not isinstance(cells, dict): continue
        for cell, code in cells.items():
            if not isinstance(code, str): continue
            prefix = "" if section in ("neutral",) else f"{section}-"
            raw2code[f"{prefix}{cell}.md"] = code
    # flat {"raw.md": "CODE"} entries, at the top level or under any key
    collect(mapping, raw2code)
    if not raw2code:
        print("WARNING: mapping produced no raw -> code entries; nothing normalized "
              "(expected flat {\"raw.md\": \"CODE\"} or the nested main/framing/... form)",
              file=sys.stderr)
        sys.exit(1)

    os.makedirs(blind_dir, exist_ok=True)
    done, missing, leaks = [], [], {}
    for raw_name, code in sorted(raw2code.items()):
        src = os.path.join(raw_dir, raw_name)
        if not os.path.exists(src):
            missing.append(raw_name); continue
        text = open(src).read()
        hits = [(lbl, m.group(0)) for pat, lbl in patterns for m in pat.finditer(text)]
        if hits: leaks[raw_name] = hits
        norm = text.strip() + "\n"
        if strip_ordinals:
            # neutralize template format tells: '## 1. The X' -> '## The X' in every blind copy
            norm = re.sub(r"^(## )\d+[.)]\s+", r"\1", norm, flags=re.M)
        open(os.path.join(blind_dir, f"{code}.md"), "w").write(norm)
        done.append(f"{raw_name} -> {code}.md ({len(norm)} chars, sha {hashlib.sha1(norm.encode()).hexdigest()[:8]})")

    print("NORMALIZED:");  print("\n".join(done) if done else "  (none)")
    print("\nMISSING RAW:"); print("\n".join(missing) if missing else "  (none)")
    print("\nLEAK SCAN (inspect, do not auto-fix):")
    if leaks:
        for k, v in leaks.items(): print(f"  {k}: {v}")
    else:
        print("  clean")

if __name__ == "__main__":
    main()
