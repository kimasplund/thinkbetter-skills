"""Pre-registered gate logic for the 2026-10 suite gauntlet program.

Every condition evaluates to PASS, FAIL or NOISE. NOISE means the margin sits on the
failing or unconfirmed side but inside the noise band, so it is not yet evidence either
way. The spec this implements is docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md.
"""
from dataclasses import dataclass
from math import comb

GUARDS = ("G1", "G2", "G3")
VALUES = ("V1", "V2", "V3", "V4")
AGREEMENT_FLOOR = 0.80
AUDIT_BAND = 1.0  # auditor counts are whole hits; a one-hit difference is noise


@dataclass
class ArmStats:
    judge: dict          # dim -> pooled mean, 1-7
    spread: dict         # dim (and "value") -> within-arm max-min of per-report means
    audit_ceremony: float  # mean ceremony hits per report (lower is better)
    audit_leaks: float     # mean leak hits per report (lower is better)
    key_rate: float        # ✓=1, ~=0.5, ✗=0, averaged over keys x reports
    key_spread: float
    negative_ok: bool
    framing_ok: bool | None  # None for the no-skill arm

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
    """PASS / NOISE / FAIL for `margin >= need`.

    A claim of improvement (claim=True) must also clear the band: a margin inside the
    within-arm spread is not evidence of a difference.
    """
    if margin >= need and (not claim or margin > band):
        return "PASS"
    if abs(margin - need) < band or (claim and margin >= need):
        return "NOISE"
    return "FAIL"


def _band(a: ArmStats, b: ArmStats, dim: str) -> float:
    return max(a.spread.get(dim, 0.0), b.spread.get(dim, 0.0))


def _guards(x: ArmStats, y: ArmStats) -> dict:
    """x must not be worse than y on any guard, on both instruments."""
    cond = {f"guard_judge_{g}": compare(x.judge[g] - y.judge[g], _band(x, y, g)) for g in GUARDS}
    cond["guard_audit_ceremony"] = compare(y.audit_ceremony - x.audit_ceremony, AUDIT_BAND)
    cond["guard_audit_leaks"] = compare(y.audit_leaks - x.audit_leaks, AUDIT_BAND)
    return cond


MECHANICAL = ("guard_audit_ceremony", "guard_audit_leaks", "negative", "framing")


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
    cond = _guards(s, n)
    v = compare(s.value_mean - n.value_mean, _band(s, n, "value"), 0.5, claim=True)
    k = compare(s.key_rate - n.key_rate, max(s.key_spread, n.key_spread), 0.10, claim=True)
    cond["value"] = "PASS" if "PASS" in (v, k) else ("NOISE" if "NOISE" in (v, k) else "FAIL")
    p = sign_test_p(wins, losses)
    if p <= 0.2:
        cond["ranking"] = "PASS" if wins >= losses else "FAIL"
    else:
        cond["ranking"] = "NOISE"
    cond["negative"] = "PASS" if s.negative_ok else "FAIL"
    cond["framing"] = "PASS" if s.framing_ok else "FAIL"
    cond["agreement"] = "PASS" if agreement >= AGREEMENT_FLOOR else "NOISE"
    return {"verdict": _verdict(cond, agreement, freeze_ok, "VALIDATED", "NOT VALIDATED"),
            "conditions": cond, "wins": wins, "losses": losses, "sign_p": round(p, 4)}


def rewrite_gate(c: ArmStats, o: ArmStats, freeze_ok: bool, agreement: float = 1.0) -> dict:
    cond = _guards(c, o)
    cond["keys"] = compare(c.key_rate - o.key_rate, max(c.key_spread, o.key_spread))
    cond["value"] = compare(c.value_mean - o.value_mean, _band(c, o, "value"), -0.25)
    cond["negative"] = "PASS" if c.negative_ok else "FAIL"
    cond["framing"] = "PASS" if c.framing_ok else "FAIL"
    return {"verdict": _verdict(cond, agreement, freeze_ok, "KEEP", "REVERT"), "conditions": cond}


def finalize(family: str, verdict: str, extended: bool) -> str:
    """After the one permitted extension, INCONCLUSIVE resolves to the conservative reading."""
    if extended and verdict == "INCONCLUSIVE":
        return "NOT VALIDATED" if family == "validation" else "REVERT"
    return verdict
