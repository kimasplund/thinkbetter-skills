"""Tests for the 2026-10 follow-up program harness (evolution/gauntlet-2026-10-r2/harness).

The October harness stays as it ran; these tests cover what Amendment 3 changed: the value sign
path, the guard band floor, one tolerated audit hit, framing on every arm, quote verification,
configurable refs and the candidate adoption rule.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REAL = Path(__file__).resolve().parent.parent
HARNESS = REAL / "evolution" / "gauntlet-2026-10-r2" / "harness"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


g2 = _load("gates_r2", HARNESS / "gates.py")
gr = _load("round_r2", HARNESS / "round.py")

BRIEFS = ("brief-1", "brief-2", "brief-3")
KEYS = {f"brief-{i}": [{"id": f"k{i}a", "text": f"secret key alpha {i}", "split": "held-out"},
                       {"id": f"k{i}b", "text": f"secret key beta {i}", "split": "held-out"}] for i in (1, 2, 3)}


def stats(value=5.0, guards=(5.0, 5.0, 5.0), key=0.5, per_brief=None, ceremony=0.0, leaks=0.0, ratio=1.0,
          neg=True, framing=True, n=6):
    flat = {**{d: value for d in ("V1", "V2", "V3", "V4")}, **dict(zip(("G1", "G2", "G3"), guards))}
    briefs = {}
    for i, b in enumerate(BRIEFS):
        dims = {d: (per_brief[d][i] if per_brief and d in per_brief else v) for d, v in flat.items()}
        dims["value"] = sum(dims[d] for d in ("V1", "V2", "V3", "V4")) / 4
        dims["key"] = per_brief["key"][i] if per_brief and "key" in per_brief else key
        briefs[b] = dims
    judge = {d: sum(briefs[b][d] for b in BRIEFS) / 3 for d in flat}
    return g2.ArmStats(judge=judge, briefs=briefs, audit_ceremony=ceremony, audit_leaks=leaks, n_replies=n,
                       word_ratio=ratio, key_rate=sum(briefs[b]["key"] for b in BRIEFS) / 3,
                       negative_ok=neg, framing_ok=framing)


def values(*per):
    return {d: list(per) for d in ("V1", "V2", "V3", "V4")}


class GateAmendment3Test(unittest.TestCase):
    def test_value_passes_on_sign_path_when_band_is_wide(self):
        s = stats(per_brief=values(6.53, 7.34, 6.28))
        n = stats(value=6.0, framing=None)
        r = g2.validation_gate(s, n, 6, 0, 0.98, True)
        self.assertEqual(r["conditions"]["value"], "PASS", r)
        self.assertEqual(r["verdict"], "VALIDATED", r)

    def test_value_sign_path_needs_every_brief_positive(self):
        s = stats(per_brief=values(7.5, 7.0, 5.9))
        r = g2.validation_gate(s, stats(value=6.0, framing=None), 6, 0, 0.98, True)
        self.assertNotEqual(r["conditions"]["value"], "PASS", r)

    def test_value_sign_path_needs_half_a_point(self):
        s = stats(per_brief=values(6.3, 6.3, 6.4))
        r = g2.validation_gate(s, stats(value=6.0, framing=None), 6, 0, 0.98, True)
        self.assertNotEqual(r["conditions"]["value"], "PASS", r)

    def test_zero_band_guard_deficit_up_to_floor_is_noise(self):
        s = stats(value=6, guards=(4.75, 5, 5))
        r = g2.validation_gate(s, stats(value=5, framing=None), 6, 0, 0.98, True)
        self.assertEqual(r["conditions"]["guard_judge_G1"], "NOISE", r)

    def test_guard_deficit_beyond_floor_still_fails(self):
        s = stats(value=6, guards=(4.5, 5, 5))
        r = g2.validation_gate(s, stats(value=5, framing=None), 6, 0, 0.98, True)
        self.assertEqual(r["conditions"]["guard_judge_G1"], "FAIL", r)

    def test_one_extra_audit_hit_is_tolerated_two_are_not(self):
        n = stats(value=5, framing=None)
        self.assertEqual(g2.validation_gate(stats(value=6, ceremony=1 / 6), n, 6, 0, 0.98, True)
                         ["conditions"]["guard_audit_ceremony"], "PASS")
        self.assertEqual(g2.validation_gate(stats(value=6, ceremony=2 / 6), n, 6, 0, 0.98, True)
                         ["conditions"]["guard_audit_ceremony"], "FAIL")
        self.assertEqual(g2.validation_gate(stats(value=6, leaks=3 / 12, n=12), stats(value=5, framing=None, n=12),
                                            6, 0, 0.98, True)["conditions"]["guard_audit_leaks"], "FAIL")

    def test_framing_flip_is_noise_when_the_baseline_also_flips(self):
        s = stats(value=6, framing=False)
        self.assertEqual(g2.validation_gate(s, stats(value=5, framing=False), 6, 0, 0.98, True)
                         ["conditions"]["framing"], "NOISE")
        self.assertEqual(g2.validation_gate(s, stats(value=5, framing=True), 6, 0, 0.98, True)
                         ["conditions"]["framing"], "FAIL")
        self.assertEqual(g2.validation_gate(s, stats(value=5, framing=None), 6, 0, 0.98, True)
                         ["conditions"]["framing"], "FAIL")

    def test_rewrite_gate_uses_the_same_floor_and_framing_rule(self):
        r = g2.rewrite_gate(stats(guards=(4.75, 5, 5), framing=False), stats(framing=False), True)
        self.assertEqual(r["conditions"]["guard_judge_G1"], "NOISE", r)
        self.assertEqual(r["conditions"]["framing"], "NOISE", r)


def git(repo, *a):
    return subprocess.run(["git", *a], cwd=repo, check=True, capture_output=True, text=True).stdout


class R2Fixture(unittest.TestCase):
    """A temp repo whose tag v1.2.0 holds the shipped skills and whose HEAD holds the candidates."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        for s in ("demo-skill", "demo-two"):
            d = self.repo / "skills" / s
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text(f"---\nname: {s}\ndescription: d\nmetadata:\n  version: \"2.2.1\"\n---\n\nSHIPPED BODY\n")
        git(self.repo, "init", "-q")
        git(self.repo, "add", ".")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-qm", "shipped")
        git(self.repo, "tag", "v1.0.0")
        git(self.repo, "tag", "v1.2.0")
        for s in ("demo-skill", "demo-two"):
            (self.repo / "skills" / s / "SKILL.md").write_text(
                f"---\nname: {s}\ndescription: d\nmetadata:\n  version: \"2.3.0\"\n---\n\nCANDIDATE BODY\n")
        (self.repo / "skills" / "demo-two" / "added.md").write_text("candidate-only file\n")
        git(self.repo, "add", ".")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-qm", "candidates")
        self.root = self.repo / "evolution" / "gauntlet-2026-10-r2"
        shutil.copytree(HARNESS, self.root / "harness", ignore=shutil.ignore_patterns("__pycache__"))
        (self.root / "harness" / "skills.json").write_text(json.dumps([
            {"order": 1, "skill": "demo-skill", "arms": ["new", "old", "none"], "gates": ["validation", "rewrite"],
             "key_type": "x", "new_ref": "HEAD", "old_ref": "v1.2.0", "adopt": "rewrite"},
            {"order": 2, "skill": "demo-two", "arms": ["new", "none"], "gates": ["validation"],
             "key_type": "y", "new_ref": "HEAD", "old_ref": "v1.2.0", "adopt": "validated"}]))
        (self.root / "LEDGER.md").write_text(
            "| # | skill | state | validation | rewrite | commit | subagent tokens |\n|---|---|---|---|---|---|---|\n"
            "| 1 | demo-skill | pending | | | | |\n| 2 | demo-two | pending | | | | |\n")
        for s in ("demo-skill", "demo-two"):
            p = self.root / s / "pack"
            p.mkdir(parents=True)
            for f in ("brief-1", "brief-2", "brief-3", "framing-hype", "framing-skeptical", "negative", "notes"):
                (p / f"{f}.md").write_text(f"# {f}\n\nA fictional task for {f}.\n")
            (p / "keys.json").write_text(json.dumps(KEYS))
        (self.repo / "README.md").write_text(
            "| Skill | Version | The move | Validation |\n|---|---|---|---|\n"
            "| [demo-skill](skills/demo-skill/) | 2.2.1 | does a thing | old status |\n"
            "| [demo-two](skills/demo-two/) | 2.2.1 | does another | old status |\n")
        os.environ["GAUNTLET_ROOT"], os.environ["GAUNTLET_REPO"] = str(self.root), str(self.repo)

    def tearDown(self):
        os.environ.pop("GAUNTLET_ROOT", None)
        os.environ.pop("GAUNTLET_REPO", None)
        self._tmp.cleanup()

    def staged(self, skill="demo-skill", text="A short direct answer with the key points.\n"):
        gr.build(skill, seed=5)
        rd = gr.round_dir(skill)
        (rd / "raw").mkdir(exist_ok=True)
        for c in json.loads((rd / "cells.json").read_text()):
            (rd / "raw" / f"{c['cell']}.md").write_text(text)
        gr.blind(skill, seed=6)
        gr.render(skill, "judge")
        return rd

    def fake_instruments(self, rd, ceremony=None):
        sealed = json.loads((rd / "SEALED.json").read_text())
        cells = {c["cell"]: c for c in json.loads((rd / "cells.json").read_text())}
        arm_of = {code: sealed["arms"][cells[f[:-3]]["arm"]] for f, code in sealed["blind"].items()}
        plan = json.loads((rd / "jobs" / "judge-plan.json").read_text())
        score = {"new": 6, "old": 5, "none": 4}
        for jid in ("J-A", "J-B"):
            for b, codes in plan["main"].items():
                rows = [f"{jid},{c}," + ",".join([str(score[arm_of[c]])] * 4 + ["6"] * 3) + ",42" for c in codes]
                order = sorted(codes, key=lambda c: -score[arm_of[c]])
                (rd / "scores" / f"{jid}-{b}.md").write_text(
                    "```scores\njudge,code,V1,V2,V3,V4,G1,G2,G3,total\n" + "\n".join(rows) + "\n```\n\n"
                    f"```ranking\njudge,brief,order\n{jid},{b},{' '.join(order)}\n```\n")
        audit = {"reports": {c: {"ceremony": [], "leaks": []} for c in sum(plan["main"].values(), []) + plan["negative"]},
                 "framing": {p["pair"]: {"invariant": True, "why": "same"} for p in plan["framing_pairs"]},
                 "negative": {c: {"ceremony": False} for c in plan["negative"]}}
        for code, quotes in (ceremony or {}).items():
            audit["reports"][code]["ceremony"] = quotes
        (rd / "audit" / "audit.json").write_text(json.dumps(audit))
        for b, codes in plan["main"].items():
            ids = [k["id"] for k in KEYS[b]]
            (rd / "keys" / f"{b}.json").write_text(json.dumps({c: {i: "✓" for i in ids} for c in codes}))
        return plan, arm_of

    def verdict(self, skill, validation, rewrite=None):
        (gr.round_dir(skill) / "verdict.json").write_text(json.dumps({
            "skill": skill, "validation": {"verdict": validation, "conditions": {}},
            "rewrite": None if rewrite is None else {"verdict": rewrite, "conditions": {}},
            "agreement": 0.9, "freeze_ok": True, "extended": False, "arms": {}}))


class BuildBlindTest(R2Fixture):
    def test_build_runs_framing_on_every_arm(self):
        self.assertEqual(gr.build("demo-skill", seed=1)["cells"], 27)
        self.assertEqual(gr.build("demo-two", seed=1)["cells"], 18)
        cells = json.loads((gr.round_dir("demo-two") / "cells.json").read_text())
        sealed = json.loads((gr.round_dir("demo-two") / "SEALED.json").read_text())
        none_code = {a: c for c, a in sealed["arms"].items()}["none"]
        self.assertTrue(any(c["kind"] == "framing" and c["arm"] == none_code for c in cells))

    def test_build_takes_arms_from_the_configured_refs(self):
        gr.build("demo-skill", seed=1)
        rd = gr.round_dir("demo-skill")
        arms = {a: c for c, a in json.loads((rd / "SEALED.json").read_text())["arms"].items()}
        self.assertIn("CANDIDATE BODY", (rd / "arms" / arms["new"] / "SKILL.md").read_text())
        self.assertIn("SHIPPED BODY", (rd / "arms" / arms["old"] / "SKILL.md").read_text())
        prereg = (rd / "PRE-REGISTRATION.md").read_text()
        self.assertIn("v1.2.0", prereg)
        self.assertNotRegex(prereg, r"\{[a-z_]+\}")

    def test_blind_pairs_framing_for_every_arm(self):
        rd = self.staged()
        plan = json.loads((rd / "jobs" / "judge-plan.json").read_text())
        self.assertEqual(len(plan["framing_pairs"]), 3)


class ScoreR2Test(R2Fixture):
    def test_score_validates_and_records_baseline_framing(self):
        rd = self.staged()
        self.fake_instruments(rd)
        v = gr.score("demo-skill")
        self.assertEqual(v["validation"]["verdict"], "VALIDATED", v["validation"])
        self.assertIs(v["arms"]["none"]["framing_ok"], True)

    def test_score_rejects_a_quote_not_in_the_credited_reply(self):
        rd = self.staged()
        plan, _ = self.fake_instruments(rd)
        code = plan["main"]["brief-1"][0]
        audit = json.loads((rd / "audit" / "audit.json").read_text())
        audit["reports"][code]["ceremony"] = ["words that appear in no reply at all"]
        (rd / "audit" / "audit.json").write_text(json.dumps(audit))
        with self.assertRaises(SystemExit) as cm:
            gr.score("demo-skill")
        self.assertIn(code, str(cm.exception))
        self.assertIn("quote", str(cm.exception))

    def test_score_accepts_a_verbatim_quote_with_a_trailing_annotation(self):
        rd = self.staged()
        plan, _ = self.fake_instruments(rd)
        code = plan["main"]["brief-1"][0]
        self.fake_instruments(rd, ceremony={code: ["**A short direct answer** (opening line)"]})
        self.assertIn(gr.score("demo-skill")["validation"]["verdict"], ("VALIDATED", "NOT VALIDATED", "INCONCLUSIVE"))

    def test_score_ignores_framing_codes_in_reports(self):
        rd = self.staged()
        plan, _ = self.fake_instruments(rd)
        audit = json.loads((rd / "audit" / "audit.json").read_text())
        for p in plan["framing_pairs"]:
            for c in p["codes"]:
                audit["reports"][c] = {"ceremony": ["A short direct answer"], "leaks": []}
        (rd / "audit" / "audit.json").write_text(json.dumps(audit))
        self.assertEqual(gr.score("demo-skill")["validation"]["verdict"], "VALIDATED")

    def test_score_never_regresses_an_applied_round(self):
        rd = self.staged("demo-two")
        self.fake_instruments(rd)
        gr.score("demo-two")
        gr.set_state("demo-two", "applied")
        gr.score("demo-two")
        self.assertEqual(gr.get_state("demo-two"), "applied")


class ApplyR2Test(R2Fixture):
    def setUp(self):
        super().setUp()
        for s in ("demo-skill", "demo-two"):
            gr.round_dir(s).mkdir(parents=True, exist_ok=True)

    def row(self, skill):
        return [l for l in (self.repo / "README.md").read_text().splitlines() if f"[{skill}]" in l][0]

    def test_unvalidated_two_arm_candidate_is_not_adopted(self):
        self.verdict("demo-two", "NOT VALIDATED")
        r = gr.apply("demo-two")
        self.assertTrue(r["reverted"])
        sd = self.repo / "skills" / "demo-two"
        self.assertEqual((sd / "SKILL.md").read_text(), git(self.repo, "show", "v1.2.0:skills/demo-two/SKILL.md"))
        self.assertFalse((sd / "added.md").exists())
        self.assertIn("not adopted", self.row("demo-two"))

    def test_validated_two_arm_candidate_is_adopted(self):
        self.verdict("demo-two", "VALIDATED")
        r = gr.apply("demo-two")
        self.assertFalse(r["reverted"])
        self.assertIn("CANDIDATE BODY", (self.repo / "skills" / "demo-two" / "SKILL.md").read_text())
        row = self.row("demo-two")
        self.assertIn("Gauntlet 2026-10-r2: validated", row)
        self.assertIn("evolution/gauntlet-2026-10-r2/demo-two/scorecard.md", row)

    def test_reverted_rewrite_restores_the_shipped_files_exactly(self):
        self.verdict("demo-skill", "NOT VALIDATED", rewrite="REVERT")
        gr.apply("demo-skill")
        self.assertEqual((self.repo / "skills" / "demo-skill" / "SKILL.md").read_text(),
                         git(self.repo, "show", "v1.2.0:skills/demo-skill/SKILL.md"))
        self.assertIn("edit reverted", self.row("demo-skill"))

    def test_kept_rewrite_keeps_the_candidate(self):
        self.verdict("demo-skill", "NOT VALIDATED", rewrite="KEEP")
        gr.apply("demo-skill")
        self.assertIn("CANDIDATE BODY", (self.repo / "skills" / "demo-skill" / "SKILL.md").read_text())
        self.assertIn("edit kept", self.row("demo-skill"))


class PromptR2Test(R2Fixture):
    def test_designer_avoids_briefs_from_other_programs(self):
        other = self.repo / "evolution" / "gauntlet-2026-10" / "old-skill" / "pack"
        other.mkdir(parents=True)
        (other / "brief-2.md").write_text("an October brief\n")
        (other / "notes.md").write_text("sealed notes\n")
        text = gr.render_designer("demo-skill").read_text()
        self.assertIn(str(other / "brief-2.md"), text)
        self.assertNotIn(str(other / "notes.md"), text)

    def test_designer_forbids_new_facts_in_framing_variants(self):
        text = (HARNESS / "prompts" / "designer.md").read_text()
        self.assertIn("must not add", text)

    def test_auditor_prompt_requires_verbatim_quotes(self):
        text = (HARNESS / "prompts" / "auditor.md").read_text()
        self.assertIn("verbatim", text)
        self.assertIn("Do not list framing replies under \"reports\"", text)


if __name__ == "__main__":
    unittest.main()
