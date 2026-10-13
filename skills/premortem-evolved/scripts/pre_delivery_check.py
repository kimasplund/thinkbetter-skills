#!/usr/bin/env python3
"""Pre-delivery mechanical check for premortem reports.

Usage: pre_delivery_check.py <report.md>
       pre_delivery_check.py -h | --help

Python 3, standard library only.

FAIL (exit 1):
  - machinery leaks (stage/section ordinals, screen narration, gate names,
    audit-handoff or file-append apparatus, unfilled [bracketed] template tokens)
  - probability ladder: sum outside 95-105, any ascending step, more than one
    tied rung, or a tied rung with no tie-break wording near the tied modes

WARN (exit 0): exactly one tied rung with tie-break wording present — every
enumerated pair still needs its own written tie-break sentence; verify by
reading the printed lines, not from memory.

No ladder found: passes with a note (a deflated short answer has no ladder).
"""
import re
import sys
from itertools import combinations
from pathlib import Path

if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
    print(__doc__.strip())
    sys.exit(0)
if len(sys.argv) != 2:
    sys.exit("usage: pre_delivery_check.py <report.md>")

path = sys.argv[1]
try:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
except OSError as exc:
    sys.exit(f"error: cannot read {path}: {exc.strerror or exc}")

fail, warn = [], []

LEAKS = [
    (r"(?i)\bstages?\s*\d", "stage ordinal"),
    (r"(?i)\bsections?\s*\d", "section ordinal"),
    (r"(?i)low[- ]stakes screen|proportionality screen|the screen (says|fails|leaves|warranted)", "screen machinery"),
    (r"(?i)delivery check|generation count|evidence tag", "process machinery"),
    (r"(?im)^\s*[*#_>]*\s*audit handoff", "audit machinery"),
    (r"(?i)append (the )?(scoring|answer) to (this|the) file", "file-append machinery"),
    (r"(?i)calibration review,\s*\[", "calibration coda placeholder"),
    (r"(?im)^\s*#{1,4}\s*[^\n]*calibration", "calibration coda heading"),
]
WARN_LEAKS = [
    (r"(?i)audit trail|treasury", "audit-domain language — verify it is substantive plan content, not machinery"),
]
TOKEN = re.compile(r"\[[^\]\n]{1,60}\]")
# Whole words only: "[Monday]" is plan content, "[date]" is an unfilled token.
TOKEN_WORDS = re.compile(
    r"(?i)\b(?:changes?|days?|dates?|modes?|their|at most|duplicates?|signals?|guards?|"
    r"plan names?|reasons?|horizons?|optional|their words|months? \d)\b"
)
# Any bracketed text that is verbatim a placeholder from this skill's own report template is unfilled.
try:
    _template = (Path(__file__).resolve().parent.parent / "SKILL.md").read_text(encoding="utf-8")
    TEMPLATE_TOKENS = {m.lower() for m in re.findall(r"\[[^\]\n]{1,60}\](?!\()", _template)}
except OSError:
    TEMPLATE_TOKENS = set()

for i, ln in enumerate(lines, 1):
    for pat, label in LEAKS:
        if re.search(pat, ln):
            fail.append(f"leak ({label}) L{i}: {ln.strip()[:100]}")
    for pat, label in WARN_LEAKS:
        if re.search(pat, ln):
            warn.append(f"{label} L{i}: {ln.strip()[:80]}")
    for m in TOKEN.finditer(ln):
        if TOKEN_WORDS.search(m.group(0)) or m.group(0).lower() in TEMPLATE_TOKENS:
            fail.append(f"unfilled template token L{i}: {m.group(0)}")

# --- ladder lint: '**Probability:** ~NN%' lines in order of appearance ---
probs = []  # (lineno, share)
for i, ln in enumerate(lines, 1):
    m = re.search(r"\*\*Probability:\*\*\s*~?\s*(\d{1,2})\s*%", ln)
    if m:
        probs.append((i, int(m.group(1))))

if not probs:
    warn.append("no '**Probability:** ~NN%' ladder lines found — confirm this is a deflated short answer, not a full report missing its ladder")
else:
    shares = [s for _, s in probs]
    total = sum(shares)
    if abs(total - 100) > 5:
        fail.append(f"ladder sums to {total}, outside 95-105")
    elif total != 100:
        warn.append(f"ladder sums to {total}, not exactly 100")

    for (l1, a), (l2, b) in zip(probs, probs[1:]):
        if b > a:
            fail.append(f"ladder ascends: {a}% (L{l1}) then {b}% (L{l2}) — ranking must be probability order")

    # tied rungs
    rungs = {}
    for ln, s in probs:
        rungs.setdefault(s, []).append(ln)
    tied = {s: ls for s, ls in rungs.items() if len(ls) > 1}
    if len(tied) > 1:
        fail.append(f"more than one tied rung: {sorted(tied)} — at most one tie per autopsy")

    mode_no = {ln: idx + 1 for idx, (ln, _) in enumerate(probs)}
    TIE_LINE = re.compile(r"(?i)tie[- ]?break|tied (with|rung|at|modes)|breaks the tie|broken on|outranks?|within the tie|ordered (first|second|third|fourth)")
    tie_lines = [(i, l) for i, l in enumerate(lines, 1) if TIE_LINE.search(l)]

    for s, ls in tied.items():
        nums = {mode_no[l] for l in ls}
        pairs = list(combinations(sorted(nums), 2))
        pair_txt = ", ".join(f"(#{a}, #{b})" for a, b in pairs)
        covered = False
        for tl, txt in tie_lines:
            mentioned = sum(1 for n in nums if re.search(rf"#\s*{n}\b|mode\s+{n}\b", txt, re.I))
            if any(abs(tl - l) <= 2 for l in ls):
                mentioned += 1  # tie-break sits on a tied mode's own line — self counts
            if mentioned >= 2 or re.search(rf"(?<!\d){s}\s*%", txt):
                covered = True
                break
        if covered:
            warn.append(f"tied rung at {s}% — pairs: {pair_txt} — tie-break wording found; verify EACH pair has its own written ordering sentence")
        else:
            fail.append(f"tied rung at {s}% — pairs: {pair_txt} — NO tie-break wording naming these modes or this rung anywhere in the report")

print(f"checked: {path}")
if fail:
    print("\nFAIL:")
    for f_ in fail:
        print("  " + f_)
if warn:
    print("\nWARN:" if not fail else "\nWARN (still failing):")
    for w in warn:
        print("  " + w)
if not fail:
    print("\nPASS" + (" (with warnings above)" if warn else " — clean"))
sys.exit(1 if fail else 0)
