import math
import os
import random
import re

LADDER = (5, 10, 15, 20, 30, 40)
MISS_LADDER = (5, 10, 20, 30, 50, 70, 90)
CODE_LETTERS = "FQRUXYZ"
LEAK_PATTERNS = (
    r"(?i)\b(stage|step|section|phase)\s*#?\d+",
    r"(?i)\b(screen|gate|checklist|slot|level)\b",
    r"(?i)\b(desk synthesis|blind round|direct answer|diversity test|stop rule|cut rule|habit-excluded|cheapest fast option|competent default slot)\b",
    r"(?i)\b\d+\s+(candidates|options)\s+(generated|considered)\b",
    r"(?i)\b(tripwire|assumption|row|graft|finalist)\s+#?\d+\b",
)
BLIND_PATTERNS = (
    r"(?i)\b(incumbent|status quo|current plan|already (planned|bought|ordered)|existing plan|champion|challenger|decoy|favou?rite)\b",
    r"(?i)\b(option-synthesis|premortem-evolved|skill-gauntlet|generator|dossier writer)\b",
)


def ladder_check(ranked, complete=True, cap=40):
    """ranked: [(label, pct), ...] in report order. Returns violations ([] = clean).
    complete=True for a full autopsy (shares sum to ~100); False for a partial list such as
    three killing modes (shares may sum below 100, never above)."""
    problems = []
    vals = [p for _, p in ranked]
    for label, p in ranked:
        if p not in LADDER:
            problems.append(f"{label}: {p} is off the ladder {LADDER}")
    if vals and max(vals) > cap:
        problems.append(f"top share {max(vals)} > ~{cap}: say the option is dominated by one risk")
    tied = 0
    for i in range(len(vals) - 1):
        if vals[i] < vals[i + 1]:
            problems.append(f"out of order: {ranked[i][0]} ({vals[i]}) above {ranked[i + 1][0]} ({vals[i + 1]})")
        elif vals[i] == vals[i + 1]:
            tied += 1
    if tied > 1:
        problems.append(f"{tied} tied adjacent pairs: at most one tie, spanning exactly two modes")
    total = sum(vals)
    if complete and vals and not 90 <= total <= 110:
        problems.append(f"shares sum to {total}, not ~100")
    if not complete and total > 100:
        problems.append(f"partial shares sum to {total} > 100")
    return problems


def leak_scan(text, extra=None, blind=False):
    """Literal scan of a finished report (blind=True adds identity tells for blind dossiers).
    Returns [(line_no, match, line)]. Inspect every hit by hand; never auto-fix: a project's own
    'Gate 1' or 'Stage 0' is content."""
    pats = list(LEAK_PATTERNS) + (list(BLIND_PATTERNS) if blind else []) + list(extra or [])
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for p in pats:
            for m in re.finditer(p, line):
                hits.append((n, m.group(0), line.strip()[:160]))
    return hits


def blind_copies(src_paths, out_dir, judges, seed=None, strip_ordinals=True):
    """Copy dossiers to random codes, give each judge its own random order, scan for identity
    leaks. Returns {'codes': {code: src}, 'orders': {judge: [codes]}, 'leaks': {code: hits}}.
    The return value is the sealed mapping: save it OUTSIDE out_dir."""
    rng = random.Random(seed)
    os.makedirs(out_dir, exist_ok=True)
    codes = {}
    for src in src_paths:
        code = None
        while code is None or code in codes or code in judges:
            code = rng.choice(CODE_LETTERS) + rng.choice(CODE_LETTERS) + str(rng.randint(2, 9))
        with open(src, encoding="utf-8") as fh:
            text = fh.read().strip() + "\n"
        if strip_ordinals:
            text = re.sub(r"^(#{1,6} )\d+[.)]\s+", r"\1", text, flags=re.M)
        with open(os.path.join(out_dir, code + ".md"), "w", encoding="utf-8") as fh:
            fh.write(text)
        codes[code] = src
    orders = {}
    for j in judges:
        order = list(codes)
        rng.shuffle(order)
        orders[j] = order
    leaks = {}
    for code in codes:
        with open(os.path.join(out_dir, code + ".md"), encoding="utf-8") as fh:
            hits = leak_scan(fh.read(), blind=True)
        if hits:
            leaks[code] = hits
    return {"codes": codes, "orders": orders, "leaks": leaks}


def read_scores(paths):
    """Parse ```scores blocks (judge,code,<dims>,total) from judge or auditor files."""
    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        for block in re.findall(r"```scores\s*\n(.*?)\n```", text, flags=re.S):
            lines = [x.strip() for x in block.strip().splitlines() if x.strip()]
            head = [h.strip() for h in lines[0].split(",")]
            for line in lines[1:]:
                vals = [v.strip() for v in line.split(",")]
                if len(vals) != len(head):
                    continue
                row = dict(zip(head, vals))
                for k in head:
                    if k not in ("judge", "code"):
                        try:
                            row[k] = float(row[k])
                        except ValueError:
                            pass
                rows.append(row)
    return rows


def sign_test_p(wins, losses):
    """One-sided exact sign test, ties dropped: P(X >= wins | n = wins + losses, p = 0.5)."""
    n = wins + losses
    if n == 0:
        return 1.0
    return sum(math.comb(n, k) for k in range(wins, n + 1)) / 2 ** n


def compare_to_incumbent(rows, incumbent, challengers, dims):
    """Per challenger: mean paired margin per dim vs the incumbent (same judge), spread across
    judges, sign-test wins/losses/p over judge x dim cells, plus inter-judge agreement.
    Cells are not independent: treat p as a screen, not a proof."""
    by = {}
    for r in rows:
        by.setdefault(r["code"], {})[r["judge"]] = r
    inc = by.get(incumbent, {})
    out = {}
    for c in challengers:
        ch = by.get(c, {})
        shared = [j for j in ch if j in inc]
        margin, wins, losses = {}, 0, 0
        for d in dims:
            diffs = [ch[j][d] - inc[j][d] for j in shared]
            margin[d] = round(sum(diffs) / len(diffs), 2) if diffs else None
            wins += sum(1 for x in diffs if x > 0)
            losses += sum(1 for x in diffs if x < 0)
        spread = {d: (max(ch[j][d] for j in ch) - min(ch[j][d] for j in ch)) if ch else None for d in dims}
        out[c] = {"judges": shared, "margin": margin, "spread": spread, "wins": wins,
                  "losses": losses, "sign_p": round(sign_test_p(wins, losses), 4)}
    cells = within = 0
    for js in by.values():
        names = list(js)
        for i in range(len(names)):
            for k in names[i + 1:]:
                for d in dims:
                    cells += 1
                    within += abs(js[names[i]][d] - js[k][d]) <= 1
    out["agreement"] = f"{within}/{cells} cells within 1 pt" if cells else "no shared codes"
    return out
