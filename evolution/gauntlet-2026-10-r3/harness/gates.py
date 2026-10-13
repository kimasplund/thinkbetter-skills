"""Pre-registered gate logic for the 2026-10 follow-up program (gauntlet-2026-10-r2).

Every condition evaluates to PASS, FAIL or NOISE. NOISE means the margin sits on the
failing or unconfirmed side but inside the noise band, so it is not yet evidence either
way. The spec this implements is docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md
(including Amendment 1, made after the pre-pilot review and before any round ran).

Noise band (Amendment 1): margins are brief-paired. For each brief, the arm difference is
taken on that brief's means; the margin is the mean of those differences and the band is
their max-min. Pairing cancels brief difficulty, and the band narrows as runs are added.

Amendment 3 (fixed before any follow-up round ran):
- the value claim also passes when the mean gain is at least +0.5 and every brief is positive;
- a judge-guard deficit no larger than BAND_FLOOR is NOISE, never a FAIL, however narrow the band;
- one extra auditor hit in total is tolerated; two or more fail;
- the framing pair runs on every arm, and a skill flip is NOISE when the comparison arm flips too.
"""
from dataclasses import dataclass
from math import comb

GUARDS = ("G1", "G2", "G3")
VALUES = ("V1", "V2", "V3", "V4")
AGREEMENT_FLOOR = 0.80
LENGTH_CAP = 2.0       # skill replies may run at most 2x the no-skill median length per brief
LENGTH_GROWTH = 0.25   # a rewrite may not lengthen replies by more than this ratio over the shipped text
BAND_FLOOR = 0.25      # a judge-guard deficit up to this size is never decisive
AUDIT_TOLERANCE = 1    # extra auditor hits, in total, that still pass


@dataclass
class ArmStats:
    judge: dict            # dim -> pooled mean over all main replies and judges
    briefs: dict           # brief -> {dim: mean, "value": mean of V1-V4, "key": key rate}
    audit_ceremony: float  # ceremony hits per main reply (lower is better)
    audit_leaks: float     # leak hits per main reply (lower is better)
    n_replies: int         # main replies in this arm
    word_ratio: float      # mean over briefs of (arm median words / no-skill median words)
    key_rate: float        # ✓=1, ~=0.5, ✗=0, averaged over keys x replies
    negative_ok: bool
    framing_ok: bool | None  # None when the arm ran no framing pair

    @property
    def value_mean(self) -> float:
        return sum(self.judge[d] for d in VALUES) / len(VALUES)


def sign_test_p(wins: int, losses: int) -> float:
    """Two-sided exact binomial test at p=0.5; ties are excluded by the caller."""
    n = wins + losses
    if n == 0:
        return 1.0
    tail = sum(comb(n, k) for k in range(min(wins, losses) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def compare(margin: float, band: float, need: float = 0.0, claim: bool = False) -> str:
    """PASS / NOISE / FAIL for `margin >= need`. A claim of improvement must also clear the band."""
    if margin >= need and (not claim or margin > band):
        return "PASS"
    if abs(margin - need) < band or (claim and margin >= need):
        return "NOISE"
    return "FAIL"


def brief_diffs(a: ArmStats, b: ArmStats, field: str) -> list:
    return [a.briefs[x][field] - b.briefs[x][field] for x in sorted(a.briefs) if x in b.briefs]


def paired(a: ArmStats, b: ArmStats, field: str) -> tuple:
    """Brief-paired margin (mean of per-brief differences) and band (their max-min)."""
    diffs = brief_diffs(a, b, field)
    if not diffs:
        return 0.0, 0.0
    return sum(diffs) / len(diffs), (max(diffs) - min(diffs)) if len(diffs) > 1 else 0.0


def _audit(x: ArmStats, y: ArmStats) -> dict:
    """x may carry at most AUDIT_TOLERANCE more ceremony or leak hits than y, in total."""
    n = max(1, min(x.n_replies, y.n_replies))
    tolerated = AUDIT_TOLERANCE / n + 1e-9
    return {"guard_audit_ceremony": "PASS" if x.audit_ceremony - y.audit_ceremony <= tolerated else "FAIL",
            "guard_audit_leaks": "PASS" if x.audit_leaks - y.audit_leaks <= tolerated else "FAIL"}


def _judge_guard(margin: float, band: float) -> str:
    """x >= y on a guard dimension. A deficit inside the band, or no larger than BAND_FLOOR, is NOISE."""
    if margin >= 0:
        return "PASS"
    return "NOISE" if -margin < band or -margin <= BAND_FLOOR else "FAIL"


def _guards(x: ArmStats, y: ArmStats) -> dict:
    cond = {f"guard_judge_{g}": _judge_guard(*paired(x, y, g)) for g in GUARDS}
    cond.update(_audit(x, y))
    return cond


def _framing(x: ArmStats, y: ArmStats) -> str:
    """x keeps its recommendation across framings. A flip is NOISE when y also flipped."""
    if x.framing_ok:
        return "PASS"
    return "NOISE" if y.framing_ok is False else "FAIL"


MECHANICAL = ("guard_audit_ceremony", "guard_audit_leaks", "guard_audit_length", "negative", "framing")


def _verdict(cond: dict, agreement: float, freeze_ok: bool, ok: str, bad: str) -> str:
    if not freeze_ok:
        return "VOID"
    if agreement < AGREEMENT_FLOOR:
        # Degraded mode: judge-derived readings are unreliable, mechanical failures stay decisive.
        return bad if any(cond.get(m) == "FAIL" for m in MECHANICAL) else "INCONCLUSIVE"
    if "FAIL" in cond.values():
        return bad
    if "NOISE" in cond.values():
        return "INCONCLUSIVE"
    return ok


def validation_gate(s: ArmStats, n: ArmStats, wins: int, losses: int, agreement: float, freeze_ok: bool) -> dict:
    """wins/losses count forced rankings (one per judge x brief) where S's replies placed above N's."""
    cond = _guards(s, n)
    cond["guard_audit_length"] = "PASS" if s.word_ratio <= LENGTH_CAP else "FAIL"
    vm, vb = paired(s, n, "value")
    km, kb = paired(s, n, "key")
    v = "PASS" if vm >= 0.5 and all(d > 0 for d in brief_diffs(s, n, "value")) else compare(vm, vb, 0.5, claim=True)
    k = compare(km, kb, 0.10, claim=True)
    cond["value"] = "PASS" if "PASS" in (v, k) else ("NOISE" if "NOISE" in (v, k) else "FAIL")
    p = sign_test_p(wins, losses)
    cond["ranking"] = "PASS" if wins >= losses else ("FAIL" if p <= 0.2 else "NOISE")
    cond["negative"] = "PASS" if s.negative_ok else "FAIL"
    cond["framing"] = _framing(s, n)
    cond["agreement"] = "PASS" if agreement >= AGREEMENT_FLOOR else "NOISE"
    return {"verdict": _verdict(cond, agreement, freeze_ok, "VALIDATED", "NOT VALIDATED"),
            "conditions": cond, "wins": wins, "losses": losses, "sign_p": round(p, 4)}


def rewrite_gate(c: ArmStats, o: ArmStats, freeze_ok: bool) -> dict:
    cond = _guards(c, o)
    cond["guard_audit_length"] = "PASS" if c.word_ratio <= o.word_ratio + LENGTH_GROWTH else "FAIL"
    cond["keys"] = compare(*paired(c, o, "key"))
    vm, vb = paired(c, o, "value")
    cond["value"] = compare(vm, vb, -0.25)
    cond["negative"] = "PASS" if c.negative_ok else "FAIL"
    cond["framing"] = _framing(c, o)
    return {"verdict": _verdict(cond, 1.0, freeze_ok, "KEEP", "REVERT"), "conditions": cond}


def finalize(family: str, verdict: str, extended: bool) -> str:
    """After the one permitted extension, INCONCLUSIVE resolves to the conservative reading."""
    if extended and verdict == "INCONCLUSIVE":
        return "NOT VALIDATED" if family == "validation" else "REVERT"
    return verdict
