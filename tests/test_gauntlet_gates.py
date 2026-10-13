import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "evolution" / "gauntlet-2026-10" / "harness"))

from gates import ArmStats, compare, finalize, rewrite_gate, sign_test_p, validation_gate  # noqa: E402


def stats(value=5.0, guards=(5.0, 5.0, 5.0), spread=0.5, ceremony=0.0, leaks=0.0, key=0.5,
          key_spread=0.1, neg=True, framing=True):
    judge = {d: value for d in ("V1", "V2", "V3", "V4")}
    judge.update(dict(zip(("G1", "G2", "G3"), guards)))
    return ArmStats(judge=judge, spread={**{d: spread for d in judge}, "value": spread},
                    audit_ceremony=ceremony, audit_leaks=leaks, key_rate=key, key_spread=key_spread,
                    negative_ok=neg, framing_ok=framing)


class GateTest(unittest.TestCase):
    def test_sign_test_values(self):
        self.assertAlmostEqual(sign_test_p(6, 0), 0.03125)
        self.assertAlmostEqual(sign_test_p(5, 1), 0.21875)
        self.assertEqual(sign_test_p(0, 0), 1.0)

    def test_compare_claim_must_clear_band(self):
        self.assertEqual(compare(0.6, 1.0, 0.5, claim=True), "NOISE")
        self.assertEqual(compare(0.6, 0.3, 0.5, claim=True), "PASS")
        self.assertEqual(compare(0.0, 1.0), "PASS")  # non-inferiority passes at zero margin

    def test_validated_when_all_pass(self):
        r = validation_gate(stats(value=6, spread=0.3), stats(value=5, spread=0.3, framing=None), 16, 4, 0.9, True)
        self.assertEqual(r["verdict"], "VALIDATED", r)

    def test_guard_drop_outside_band_fails(self):
        r = validation_gate(stats(value=6, guards=(5, 3.5, 5)), stats(value=5, framing=None), 16, 4, 0.9, True)
        self.assertEqual(r["verdict"], "NOT VALIDATED")
        self.assertEqual(r["conditions"]["guard_judge_G2"], "FAIL")

    def test_guard_drop_inside_band_is_noise(self):
        r = validation_gate(stats(value=6, guards=(4.8, 5, 5), spread=0.5), stats(value=5, spread=0.3, framing=None),
                            16, 4, 0.9, True)
        self.assertEqual(r["verdict"], "INCONCLUSIVE", r)

    def test_value_via_keys_only(self):
        r = validation_gate(stats(value=5.1, key=0.75), stats(value=5.0, key=0.5, framing=None), 16, 4, 0.9, True)
        self.assertEqual(r["conditions"]["value"], "PASS", r)

    def test_ranking_not_significant_is_noise(self):
        r = validation_gate(stats(value=6, spread=0.3), stats(value=5, spread=0.3, framing=None), 5, 4, 0.9, True)
        self.assertEqual(r["conditions"]["ranking"], "NOISE")

    def test_negative_fixture_failure_fails(self):
        r = validation_gate(stats(value=6, spread=0.3, neg=False), stats(value=5, spread=0.3, framing=None),
                            16, 4, 0.9, True)
        self.assertEqual(r["verdict"], "NOT VALIDATED")

    def test_low_agreement_inconclusive(self):
        r = validation_gate(stats(value=6, spread=0.3), stats(value=5, spread=0.3, framing=None), 16, 4, 0.7, True)
        self.assertEqual(r["verdict"], "INCONCLUSIVE")

    def test_freeze_failure_void(self):
        r = validation_gate(stats(value=6), stats(value=5, framing=None), 16, 4, 0.9, False)
        self.assertEqual(r["verdict"], "VOID")

    def test_rewrite_keep_and_noninferiority(self):
        r = rewrite_gate(stats(value=4.9, spread=0.3), stats(value=5.0, spread=0.3), True)
        self.assertEqual(r["verdict"], "KEEP", r)

    def test_rewrite_value_drop_reverts(self):
        r = rewrite_gate(stats(value=4.2, spread=0.3), stats(value=5.0, spread=0.3), True)
        self.assertEqual(r["verdict"], "REVERT")

    def test_finalize_after_extension(self):
        self.assertEqual(finalize("validation", "INCONCLUSIVE", True), "NOT VALIDATED")
        self.assertEqual(finalize("rewrite", "INCONCLUSIVE", True), "REVERT")
        self.assertEqual(finalize("validation", "INCONCLUSIVE", False), "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()
