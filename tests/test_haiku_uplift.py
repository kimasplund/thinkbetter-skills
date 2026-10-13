"""Tests for the Haiku uplift program harness (evolution/haiku-uplift-2026-10/harness).

The question: does Haiku with a skill reach Sonnet without one? Each round judges four arms in one
blind panel (hs = Haiku+skill, hn = Haiku alone, ss = Sonnet+skill, sn = Sonnet alone). Sonnet replies
are reused from an earlier round on the same sealed pack where the skill text is unchanged.
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
HARNESS = REAL / "evolution" / "haiku-uplift-2026-10" / "harness"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


gu = _load("gates_uplift", HARNESS / "gates.py")
ur = _load("round_uplift", HARNESS / "round.py")

BRIEFS = ("brief-1", "brief-2", "brief-3")
KEYS = {f"brief-{i}": [{"id": f"k{i}a", "text": f"secret key alpha {i}", "split": "held-out"},
                       {"id": f"k{i}b", "text": f"secret key beta {i}", "split": "held-out"}] for i in (1, 2, 3)}
ARMS = {"hs": {"model": "haiku", "skill_ref": "HEAD"}, "hn": {"model": "haiku"},
        "ss": {"model": "sonnet", "skill_ref": "HEAD", "reuse": "new"}, "sn": {"model": "sonnet", "reuse": "none"}}


def stats(value=5.0, guards=(5.0, 5.0, 5.0), key=0.5, per_brief=None, ceremony=0.0, ratio=1.0):
    flat = {**{d: value for d in ("V1", "V2", "V3", "V4")}, **dict(zip(("G1", "G2", "G3"), guards))}
    briefs = {}
    for i, b in enumerate(BRIEFS):
        dims = {d: (per_brief[d][i] if per_brief and d in per_brief else v) for d, v in flat.items()}
        dims["value"] = sum(dims[d] for d in ("V1", "V2", "V3", "V4")) / 4
        dims["key"] = key
        briefs[b] = dims
    judge = {d: sum(briefs[b][d] for b in BRIEFS) / 3 for d in flat}
    return gu.ArmStats(judge=judge, briefs=briefs, audit_ceremony=ceremony, audit_leaks=0.0, n_replies=6,
                       word_ratio=ratio, key_rate=key, negative_ok=True, framing_ok=True)


class ReachesGateTest(unittest.TestCase):
    def test_small_deficit_reaches(self):
        r = gu.reaches_gate(stats(value=5.8), stats(value=6.0), 3, 3, 0.95, True)
        self.assertEqual(r["verdict"], "REACHES", r)

    def test_clear_deficit_does_not_reach(self):
        r = gu.reaches_gate(stats(value=5.0), stats(value=6.0), 1, 5, 0.95, True)
        self.assertEqual(r["verdict"], "DOES NOT REACH", r)
        self.assertEqual(r["conditions"]["value"], "FAIL")

    def test_guard_and_key_margins_are_non_inferiority(self):
        ok = gu.reaches_gate(stats(value=6, guards=(4.8, 5, 5), key=0.45), stats(value=6, key=0.5), 3, 3, 0.95, True)
        self.assertEqual(ok["conditions"]["guard_judge_G1"], "PASS", ok)
        self.assertEqual(ok["conditions"]["keys"], "PASS", ok)
        bad = gu.reaches_gate(stats(value=6, guards=(4.0, 5, 5)), stats(value=6), 3, 3, 0.95, True)
        self.assertEqual(bad["conditions"]["guard_judge_G1"], "FAIL", bad)

    def test_ranking_fails_only_on_a_significant_loss(self):
        self.assertEqual(gu.reaches_gate(stats(value=6), stats(value=6), 2, 4, 0.95, True)["conditions"]["ranking"], "PASS")
        self.assertEqual(gu.reaches_gate(stats(value=6), stats(value=6), 0, 6, 0.95, True)["conditions"]["ranking"], "FAIL")

    def test_finalize_after_extension_is_conservative(self):
        self.assertEqual(gu.finalize("reaches", "INCONCLUSIVE", True), "DOES NOT REACH")


def git(repo, *a):
    return subprocess.run(["git", *a], cwd=repo, check=True, capture_output=True, text=True).stdout


class UpliftFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        d = self.repo / "skills" / "demo-skill"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text("---\nname: demo-skill\ndescription: d\nmetadata:\n  version: \"2.2.1\"\n---\n\nBODY\n")
        git(self.repo, "init", "-q")
        git(self.repo, "add", ".")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-qm", "v")
        # an earlier round on the same pack, with Sonnet replies for arms "new" and "none"
        self.src = self.repo / "evolution" / "old-program" / "demo-skill"
        (self.src / "pack").mkdir(parents=True)
        for f in ("brief-1", "brief-2", "brief-3", "framing-hype", "framing-skeptical", "negative", "notes"):
            (self.src / "pack" / f"{f}.md").write_text(f"# {f}\n\nA fictional task for {f}.\n")
        (self.src / "pack" / "keys.json").write_text(json.dumps(KEYS))
        (self.src / "SEALED.json").write_text(json.dumps({"arms": {"q1": "new", "z9": "none"}}))
        (self.src / "raw").mkdir()
        for b in BRIEFS:
            for code, label in (("q1", "SONNET SKILL"), ("z9", "SONNET ALONE")):
                for run in (1, 2, 3):
                    (self.src / "raw" / f"{b}--{code}--r{run}.md").write_text(f"{label} reply {b} run {run}\n")
        self.root = self.repo / "evolution" / "haiku-uplift-2026-10"
        shutil.copytree(HARNESS, self.root / "harness", ignore=shutil.ignore_patterns("__pycache__"))
        (self.root / "harness" / "skills.json").write_text(json.dumps([
            {"order": 1, "skill": "demo-skill", "key_type": "x", "source": "evolution/old-program/demo-skill",
             "arms": ARMS}]))
        (self.root / "LEDGER.md").write_text(
            "| # | skill | state | reaches sonnet | haiku uplift | commit | subagent tokens |\n|---|---|---|---|---|---|---|\n"
            "| 1 | demo-skill | pending | | | | |\n")
        (self.repo / "README.md").write_text("| [demo-skill](skills/demo-skill/) | 2.2.1 | x | old status |\n")
        os.environ["GAUNTLET_ROOT"], os.environ["GAUNTLET_REPO"] = str(self.root), str(self.repo)

    def tearDown(self):
        os.environ.pop("GAUNTLET_ROOT", None)
        os.environ.pop("GAUNTLET_REPO", None)
        self._tmp.cleanup()

    def arm_codes(self, rd):
        return {name: code for code, name in json.loads((rd / "SEALED.json").read_text())["arms"].items()}


class BuildTest(UpliftFixture):
    def test_build_copies_pack_and_reuses_sonnet_replies(self):
        r = ur.build("demo-skill", seed=1)
        self.assertEqual(r["cells"], 24)
        rd = ur.round_dir("demo-skill")
        self.assertEqual((rd / "pack" / "keys.json").read_text(), (self.src / "pack" / "keys.json").read_text())
        codes = self.arm_codes(rd)
        self.assertEqual((rd / "raw" / f"brief-2--{codes['ss']}--r1.md").read_text(), "SONNET SKILL reply brief-2 run 1\n")
        self.assertEqual((rd / "raw" / f"brief-3--{codes['sn']}--r2.md").read_text(), "SONNET ALONE reply brief-3 run 2\n")
        self.assertFalse((rd / "raw" / f"brief-1--{codes['ss']}--r3.md").exists())
        self.assertTrue((rd / "arms" / codes["hs"] / "SKILL.md").is_file())
        self.assertTrue((rd / "arms" / codes["ss"] / "SKILL.md").is_file())
        self.assertFalse((rd / "arms" / codes["hn"]).exists())
        cells = json.loads((rd / "cells.json").read_text())
        self.assertTrue(all(c["kind"] == "main" for c in cells))
        self.assertNotRegex((rd / "PRE-REGISTRATION.md").read_text(), r"\{[a-z_]+\}")
        self.assertIn("raw", (rd / "FREEZE.md").read_text())

    def test_render_exec_runs_only_missing_cells_on_each_arms_model(self):
        ur.build("demo-skill", seed=1)
        rd = ur.round_dir("demo-skill")
        codes = self.arm_codes(rd)
        jobs = ur.render("demo-skill", "exec")
        self.assertEqual(len(jobs), 12)
        for j in jobs:
            arm = next(a for a, c in codes.items() if f"--{c}--" in j["id"])
            self.assertIn(arm, ("hs", "hn"))
            self.assertEqual(j["model"], "haiku")
            text = (rd / j["prompt"]).read_text()
            self.assertEqual("SKILL.md" in text, arm == "hs")

    def test_extend_reuses_source_runs_where_they_exist(self):
        ur.build("demo-skill", seed=1)
        rd = ur.round_dir("demo-skill")
        codes = self.arm_codes(rd)
        ur.extend("demo-skill")
        self.assertTrue((rd / "raw" / f"brief-1--{codes['ss']}--r3.md").is_file())
        jobs = {j["id"] for j in ur.render("demo-skill", "exec")}
        self.assertIn(f"brief-1--{codes['ss']}--r4", jobs)        # source has no run 4: run it fresh
        self.assertNotIn(f"brief-1--{codes['ss']}--r3", jobs)     # run 3 was reused
        sonnet = [j for j in ur.render("demo-skill", "exec") if f"--{codes['ss']}--" in j["id"]]
        self.assertTrue(all(j["model"] == "sonnet" for j in sonnet))


class ScoreApplyTest(UpliftFixture):
    def staged(self):
        ur.build("demo-skill", seed=1)
        rd = ur.round_dir("demo-skill")
        for c in json.loads((rd / "cells.json").read_text()):
            p = rd / "raw" / f"{c['cell']}.md"
            if not p.exists():
                p.write_text("A short direct answer with the key points.\n")
        ur.blind("demo-skill", seed=6)
        ur.render("demo-skill", "judge")
        return rd

    def fake_instruments(self, rd, value):
        sealed = json.loads((rd / "SEALED.json").read_text())
        cells = {c["cell"]: c for c in json.loads((rd / "cells.json").read_text())}
        arm_of = {code: sealed["arms"][cells[f[:-3]]["arm"]] for f, code in sealed["blind"].items()}
        plan = json.loads((rd / "jobs" / "judge-plan.json").read_text())
        for jid in ("J-A", "J-B"):
            for b, codes in plan["main"].items():
                rows = [f"{jid},{c}," + ",".join([str(value[arm_of[c]])] * 4 + ["6"] * 3) + ",42" for c in codes]
                order = sorted(codes, key=lambda c: -value[arm_of[c]])
                (rd / "scores" / f"{jid}-{b}.md").write_text(
                    "```scores\njudge,code,V1,V2,V3,V4,G1,G2,G3,total\n" + "\n".join(rows) + "\n```\n\n"
                    f"```ranking\njudge,brief,order\n{jid},{b},{' '.join(order)}\n```\n")
        audit = {"reports": {c: {"ceremony": [], "leaks": []} for c in sum(plan["main"].values(), [])}}
        (rd / "audit" / "audit.json").write_text(json.dumps(audit))
        for b, codes in plan["main"].items():
            ids = [k["id"] for k in KEYS[b]]
            (rd / "keys" / f"{b}.json").write_text(json.dumps({c: {i: "✓" for i in ids} for c in codes}))

    def test_score_reports_all_three_comparisons(self):
        rd = self.staged()
        self.fake_instruments(rd, {"hs": 6, "hn": 4, "ss": 6, "sn": 6})
        v = ur.score("demo-skill")
        self.assertEqual(v["reaches"]["verdict"], "REACHES", v["reaches"])
        self.assertEqual(v["haiku_uplift"]["verdict"], "VALIDATED", v["haiku_uplift"])
        self.assertIn("sonnet_uplift", v)
        self.assertEqual(set(v["arms"]), {"hs", "hn", "ss", "sn"})
        self.assertEqual(ur.get_state("demo-skill"), "scored")

    def test_score_reports_a_clear_shortfall(self):
        rd = self.staged()
        self.fake_instruments(rd, {"hs": 4, "hn": 4, "ss": 6, "sn": 6})
        self.assertEqual(ur.score("demo-skill")["reaches"]["verdict"], "DOES NOT REACH")

    def test_apply_changes_no_skill_and_no_readme(self):
        rd = self.staged()
        self.fake_instruments(rd, {"hs": 6, "hn": 4, "ss": 6, "sn": 6})
        ur.score("demo-skill")
        before = ((self.repo / "README.md").read_text(), (self.repo / "skills" / "demo-skill" / "SKILL.md").read_text())
        ur.apply("demo-skill")
        after = ((self.repo / "README.md").read_text(), (self.repo / "skills" / "demo-skill" / "SKILL.md").read_text())
        self.assertEqual(before, after)
        self.assertEqual(ur.get_state("demo-skill"), "applied")
        self.assertIn("Haiku", (rd / "research-note.md").read_text())


if __name__ == "__main__":
    unittest.main()
