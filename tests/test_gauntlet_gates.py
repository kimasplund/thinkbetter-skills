import inspect
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "evolution" / "gauntlet-2026-10" / "harness"))

from gates import ArmStats, compare, finalize, paired, rewrite_gate, sign_test_p, validation_gate  # noqa: E402

BRIEFS = ("brief-1", "brief-2", "brief-3")


def stats(value=5.0, guards=(5.0, 5.0, 5.0), key=0.5, per_brief=None, ceremony=0.0, leaks=0.0, ratio=1.0,
          neg=True, framing=True):
    """per_brief: optional {dim: [b1, b2, b3]} overriding the flat value for that dim."""
    flat = {**{d: value for d in ("V1", "V2", "V3", "V4")}, **dict(zip(("G1", "G2", "G3"), guards))}
    briefs = {}
    for i, b in enumerate(BRIEFS):
        dims = {d: (per_brief[d][i] if per_brief and d in per_brief else v) for d, v in flat.items()}
        dims["value"] = sum(dims[d] for d in ("V1", "V2", "V3", "V4")) / 4
        dims["key"] = per_brief["key"][i] if per_brief and "key" in per_brief else key
        briefs[b] = dims
    judge = {d: sum(briefs[b][d] for b in BRIEFS) / 3 for d in flat}
    return ArmStats(judge=judge, briefs=briefs, audit_ceremony=ceremony, audit_leaks=leaks, n_replies=6,
                    word_ratio=ratio, key_rate=sum(briefs[b]["key"] for b in BRIEFS) / 3,
                    negative_ok=neg, framing_ok=framing)


class GateTest(unittest.TestCase):
    def test_sign_test_values(self):
        self.assertAlmostEqual(sign_test_p(6, 0), 0.03125)
        self.assertAlmostEqual(sign_test_p(5, 1), 0.21875)
        self.assertEqual(sign_test_p(0, 0), 1.0)

    def test_compare_claim_must_clear_band(self):
        self.assertEqual(compare(0.6, 1.0, 0.5, claim=True), "NOISE")
        self.assertEqual(compare(0.6, 0.3, 0.5, claim=True), "PASS")
        self.assertEqual(compare(0.0, 1.0), "PASS")

    def test_paired_margin_and_band_cancel_brief_difficulty(self):
        s = stats(per_brief={"V1": [7, 4, 5], "V2": [7, 4, 5], "V3": [7, 4, 5], "V4": [7, 4, 5]})
        n = stats(per_brief={"V1": [6, 3, 4], "V2": [6, 3, 4], "V3": [6, 3, 4], "V4": [6, 3, 4]})
        margin, band = paired(s, n, "value")
        self.assertAlmostEqual(margin, 1.0)
        self.assertAlmostEqual(band, 0.0)

    def test_validated_when_all_pass(self):
        r = validation_gate(stats(value=6), stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["verdict"], "VALIDATED", r)

    def test_guard_drop_outside_band_fails(self):
        r = validation_gate(stats(value=6, guards=(5, 3.5, 5)), stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["verdict"], "NOT VALIDATED")
        self.assertEqual(r["conditions"]["guard_judge_G2"], "FAIL")

    def test_guard_drop_inside_band_is_noise(self):
        s = stats(value=6, per_brief={"G1": [5.2, 4.4, 4.8]})
        r = validation_gate(s, stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["conditions"]["guard_judge_G1"], "NOISE")
        self.assertEqual(r["verdict"], "INCONCLUSIVE", r)

    def test_value_via_keys_only(self):
        r = validation_gate(stats(value=5.1, key=0.75), stats(value=5.0, key=0.5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["conditions"]["value"], "PASS", r)

    def test_ranking_unit_is_one_per_ranking(self):
        s, n = stats(value=6), stats(value=5, framing=None)
        self.assertEqual(validation_gate(s, n, 3, 3, 0.9, True)["conditions"]["ranking"], "PASS")
        self.assertEqual(validation_gate(s, n, 2, 4, 0.9, True)["conditions"]["ranking"], "NOISE")
        self.assertEqual(validation_gate(s, n, 0, 6, 0.9, True)["conditions"]["ranking"], "FAIL")

    def test_length_ratio_guard(self):
        r = validation_gate(stats(value=6, ratio=2.5), stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["conditions"]["guard_audit_length"], "FAIL")

    def test_audit_band_is_one_hit_in_total(self):
        r = validation_gate(stats(value=6, ceremony=5 / 6), stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["conditions"]["guard_audit_ceremony"], "FAIL")

    def test_negative_fixture_failure_fails(self):
        r = validation_gate(stats(value=6, neg=False), stats(value=5, framing=None), 6, 0, 0.9, True)
        self.assertEqual(r["verdict"], "NOT VALIDATED")

    def test_low_agreement_inconclusive(self):
        r = validation_gate(stats(value=6), stats(value=5, framing=None), 6, 0, 0.7, True)
        self.assertEqual(r["verdict"], "INCONCLUSIVE")

    def test_freeze_failure_void(self):
        r = validation_gate(stats(value=6), stats(value=5, framing=None), 6, 0, 0.9, False)
        self.assertEqual(r["verdict"], "VOID")

    def test_rewrite_gate_has_no_agreement_condition(self):
        self.assertEqual(list(inspect.signature(rewrite_gate).parameters), ["c", "o", "freeze_ok"])

    def test_rewrite_keep_and_noninferiority(self):
        self.assertEqual(rewrite_gate(stats(value=4.9), stats(value=5.0), True)["verdict"], "KEEP")

    def test_rewrite_value_drop_reverts(self):
        self.assertEqual(rewrite_gate(stats(value=4.2), stats(value=5.0), True)["verdict"], "REVERT")

    def test_rewrite_length_growth_reverts(self):
        r = rewrite_gate(stats(value=5.0, ratio=1.6), stats(value=5.0, ratio=1.2), True)
        self.assertEqual(r["conditions"]["guard_audit_length"], "FAIL")

    def test_finalize_after_extension(self):
        self.assertEqual(finalize("validation", "INCONCLUSIVE", True), "NOT VALIDATED")
        self.assertEqual(finalize("rewrite", "INCONCLUSIVE", True), "REVERT")
        self.assertEqual(finalize("validation", "INCONCLUSIVE", False), "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()
