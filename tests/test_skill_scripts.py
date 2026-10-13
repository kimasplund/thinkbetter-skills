"""Tests for the helper scripts shipped inside skills (run via subprocess)."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRE_DELIVERY = ROOT / "skills" / "premortem-evolved" / "scripts" / "pre_delivery_check.py"
NORMALIZE = ROOT / "skills" / "skill-gauntlet" / "scripts" / "normalize.py"

LADDER = (
    "### 1. First\n**Probability:** ~60% - one\n"
    "### 2. Second\n**Probability:** ~30% - two\n"
    "### 3. Third\n**Probability:** ~10% - three\n"
)


def run(script, *args):
    return subprocess.run(
        [sys.executable, str(script), *args], capture_output=True, text=True, timeout=60
    )


class PreDeliveryCheckTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def report(self, extra=""):
        p = self.dir / "report.md"
        p.write_text(LADDER + extra)
        return p

    def test_help_flags_print_usage_and_exit_zero(self):
        for flag in ("--help", "-h"):
            r = run(PRE_DELIVERY, flag)
            self.assertEqual(r.returncode, 0, flag)
            self.assertIn("Usage", r.stdout)
            self.assertNotIn("Traceback", r.stderr)

    def test_missing_file_is_one_line_error_without_traceback(self):
        r = run(PRE_DELIVERY, str(self.dir / "nope.md"))
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(len(r.stderr.strip().splitlines()), 1)

    def test_weekday_in_brackets_is_not_a_template_token(self):
        r = run(PRE_DELIVERY, str(self.report("\nThe pilot slipped past [Monday] again.\n")))
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("unfilled template token", r.stdout)

    def test_every_shipped_template_placeholder_fails(self):
        skill_md = (ROOT / "skills" / "premortem-evolved" / "SKILL.md").read_text()
        tokens = set(re.findall(r"\[[^\]\n]{1,60}\](?!\()", skill_md))
        self.assertGreater(len(tokens), 10)
        for token in sorted(tokens):
            r = run(PRE_DELIVERY, str(self.report(f"\nNote: {token}\n")))
            self.assertEqual(r.returncode, 1, token)
            self.assertIn("unfilled template token", r.stdout, token)

    def test_plural_placeholder_words_fail(self):
        for token in ("[days]", "[reasons]", "[signals]", "[failure modes]"):
            r = run(PRE_DELIVERY, str(self.report(f"\nNote: {token}\n")))
            self.assertEqual(r.returncode, 1, token)

    def test_real_template_tokens_still_fail(self):
        for token in ("[date]", "[plan name]", "[Optional, high-stakes only]", "[month 3]"):
            r = run(PRE_DELIVERY, str(self.report(f"\nHorizon: {token}\n")))
            self.assertEqual(r.returncode, 1, token)
            self.assertIn("unfilled template token", r.stdout, token)

    def test_existing_leak_patterns_still_fail(self):
        r = run(PRE_DELIVERY, str(self.report("\nAs Stage 3 showed, it failed.\n")))
        self.assertEqual(r.returncode, 1)
        self.assertIn("stage ordinal", r.stdout)

    def test_clean_report_passes(self):
        r = run(PRE_DELIVERY, str(self.report()))
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("PASS", r.stdout)


class NormalizeTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.raw = self.dir / "raw"
        self.blind = self.dir / "blind"
        self.raw.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def mapping(self, data):
        p = self.dir / "mapping.json"
        p.write_text(json.dumps(data))
        return p

    def test_flat_mapping_produces_coded_files(self):
        (self.raw / "raw.md").write_text("# Report\nbody\n")
        r = run(NORMALIZE, str(self.mapping({"raw.md": "K7"})), str(self.raw), str(self.blind))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual((self.blind / "K7.md").read_text(), "# Report\nbody\n")
        self.assertIn("raw.md -> K7.md", r.stdout)

    def test_nested_mapping_still_works(self):
        (self.raw / "b1-champ.md").write_text("alpha\n")
        (self.raw / "framing-hyped.md").write_text("beta\n")
        (self.raw / "ctl1.md").write_text("gamma\n")
        m = {
            "main": {"b1": {"champ": "AA"}},
            "framing": {"hyped": "BB"},
            "neutral": {"ctl1": "CC"},
        }
        r = run(NORMALIZE, str(self.mapping(m)), str(self.raw), str(self.blind))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for code, text in (("AA", "alpha"), ("BB", "beta"), ("CC", "gamma")):
            self.assertEqual((self.blind / f"{code}.md").read_text(), text + "\n")

    def test_flat_mapping_nested_under_arbitrary_key(self):
        (self.raw / "x.md").write_text("one\n")
        r = run(NORMALIZE, str(self.mapping({"round2": {"x.md": "ZZ"}})), str(self.raw), str(self.blind))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.blind / "ZZ.md").exists())

    def test_nothing_mapped_warns_and_exits_nonzero(self):
        r = run(NORMALIZE, str(self.mapping({"notes": "nothing useful"})), str(self.raw), str(self.blind))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("warning", (r.stdout + r.stderr).lower())

    def test_help_prints_usage_without_traceback(self):
        r = run(NORMALIZE, "--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("Usage", r.stdout)
        self.assertNotIn("Traceback", r.stderr)

    def test_no_args_prints_usage_and_exits_2(self):
        r = run(NORMALIZE)
        self.assertEqual(r.returncode, 2)
        self.assertIn("Usage", r.stdout + r.stderr)
        self.assertNotIn("IndexError", r.stderr)


if __name__ == "__main__":
    unittest.main()
