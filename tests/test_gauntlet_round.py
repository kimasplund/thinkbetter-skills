import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REAL = Path(__file__).resolve().parent.parent
HARNESS = REAL / "evolution" / "gauntlet-2026-10" / "harness"
sys.path.insert(0, str(HARNESS))

gr = importlib.import_module("round")

KEYS = {f"brief-{i}": [{"id": f"k{i}a", "text": f"secret key alpha {i}", "split": "held-out"},
                       {"id": f"k{i}b", "text": f"secret key beta {i}", "split": "held-out"}] for i in (1, 2, 3)}


def git(repo, *a):
    return subprocess.run(["git", *a], cwd=repo, check=True, capture_output=True, text=True).stdout


class RoundFixture(unittest.TestCase):
    """A temp repo with tag v1.0.0, two demo skills, the real harness and a valid pack."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        for s in ("demo-skill", "demo-two"):
            d = self.repo / "skills" / s
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text(f"---\nname: {s}\ndescription: d\nmetadata:\n  version: \"1.0.0\"\n---\n\nOLD BODY\n")
        git(self.repo, "init", "-q")
        git(self.repo, "add", ".")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-qm", "v1")
        git(self.repo, "tag", "v1.0.0")
        for s in ("demo-skill", "demo-two"):
            (self.repo / "skills" / s / "SKILL.md").write_text(
                f"---\nname: {s}\ndescription: d2\nmetadata:\n  version: \"1.1.0\"\n---\n\nNEW BODY\n")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t.test", "commit", "-qam", "v2")
        self.root = self.repo / "evolution" / "gauntlet-2026-10"
        shutil.copytree(HARNESS, self.root / "harness", ignore=shutil.ignore_patterns("__pycache__"))
        (self.root / "harness" / "skills.json").write_text(json.dumps([
            {"order": 1, "skill": "demo-skill", "arms": ["new", "old", "none"], "gates": ["validation", "rewrite"], "key_type": "x"},
            {"order": 2, "skill": "demo-two", "arms": ["new", "none"], "gates": ["validation"], "key_type": "y"}]))
        (self.root / "LEDGER.md").write_text(
            "| # | skill | state | validation | rewrite | commit | subagent tokens |\n|---|---|---|---|---|---|---|\n"
            "| 1 | demo-skill | pending | | | | |\n| 2 | demo-two | pending | | | | |\n")
        for s in ("demo-skill", "demo-two"):
            self.write_pack(s)
        os.environ["GAUNTLET_ROOT"], os.environ["GAUNTLET_REPO"] = str(self.root), str(self.repo)

    def tearDown(self):
        os.environ.pop("GAUNTLET_ROOT", None)
        os.environ.pop("GAUNTLET_REPO", None)
        self._tmp.cleanup()

    def write_pack(self, skill, keys=KEYS, skip=()):
        p = self.root / skill / "pack"
        p.mkdir(parents=True, exist_ok=True)
        for f in ("brief-1", "brief-2", "brief-3", "framing-hype", "framing-skeptical", "negative", "notes"):
            if f not in skip:
                (p / f"{f}.md").write_text(f"# {f}\n\nA fictional task for {f}.\n")
        (p / "keys.json").write_text(json.dumps(keys))


class BuildTest(RoundFixture):
    def test_validate_pack_reports_missing_and_bad_keys(self):
        bad = json.loads(json.dumps(KEYS))
        del bad["brief-2"][0]["split"]
        self.write_pack("demo-two", keys=bad)
        (self.root / "demo-two" / "pack" / "negative.md").unlink()
        problems = gr.validate_pack(gr.round_dir("demo-two"))
        self.assertTrue(any("negative.md" in p for p in problems), problems)
        self.assertTrue(any("split" in p for p in problems), problems)

    def test_build_three_arm_cell_counts(self):
        self.assertEqual(gr.build("demo-skill", seed=1)["cells"], 25)

    def test_build_two_arm_cell_counts(self):
        self.assertEqual(gr.build("demo-two", seed=1)["cells"], 16)

    def test_build_seals_arms_and_uses_opaque_codes(self):
        gr.build("demo-skill", seed=2)
        rd = gr.round_dir("demo-skill")
        sealed = json.loads((rd / "SEALED.json").read_text())["arms"]
        self.assertEqual(sorted(sealed.values()), ["new", "none", "old"])
        cells = json.loads((rd / "cells.json").read_text())
        for c in cells:
            for word in ("new", "old", "none"):
                self.assertNotIn(word, c["cell"])
                self.assertNotIn(word, c["arm"])
        self.assertEqual({c["arm"] for c in cells}, set(sealed))

    def test_build_old_arm_comes_from_tag(self):
        gr.build("demo-skill", seed=3)
        rd = gr.round_dir("demo-skill")
        sealed = json.loads((rd / "SEALED.json").read_text())["arms"]
        code = {v: k for k, v in sealed.items()}
        self.assertIn("OLD BODY", (rd / "arms" / code["old"] / "SKILL.md").read_text())
        self.assertIn("NEW BODY", (rd / "arms" / code["new"] / "SKILL.md").read_text())
        self.assertFalse((rd / "arms" / code["none"]).exists())

    def test_build_refuses_rebuild(self):
        gr.build("demo-two", seed=4)
        with self.assertRaises(SystemExit):
            gr.build("demo-two", seed=4)


class RenderBlindTest(RoundFixture):
    def built(self, skill="demo-skill", seed=5):
        gr.build(skill, seed=seed)
        return gr.round_dir(skill)

    def write_raw(self, rd, text="# Answer\n\n## 1. First point\n\nContent.\n", skip=()):
        (rd / "raw").mkdir(exist_ok=True)
        for c in json.loads((rd / "cells.json").read_text()):
            if c["cell"] not in skip:
                (rd / "raw" / f"{c['cell']}.md").write_text(text)

    def test_render_exec_prompts_hide_arms_and_keys(self):
        rd = self.built()
        jobs = gr.render("demo-skill", "exec")
        self.assertEqual(len(jobs), 25)
        none_code = {v: k for k, v in json.loads((rd / "SEALED.json").read_text())["arms"].items()}["none"]
        for j in jobs:
            text = (rd / j["prompt"]).read_text()
            for word in (" new ", " old ", " none ", "v1.0.0", "1.1.0"):
                self.assertNotIn(word, text, j["id"])
            for b in KEYS.values():
                for k in b:
                    self.assertNotIn(k["text"], text)
            self.assertNotIn("pack/", text)
            if f"--{none_code}--" in j["id"]:
                self.assertNotIn("SKILL.md", text)
            else:
                self.assertIn("SKILL.md", text)
        self.assertTrue(all(j["model"] == "sonnet" for j in jobs))

    def test_render_judge_embeds_keys_only_in_verifier_prompts(self):
        rd = self.built()
        self.write_raw(rd)
        gr.blind("demo-skill", seed=6)
        jobs = gr.render("demo-skill", "judge")
        kinds = {j["id"].split("-")[0] for j in jobs}
        self.assertEqual(kinds, {"J", "auditor", "verifier"})
        self.assertEqual(len(jobs), 2 * 3 + 1 + 3)
        for j in jobs:
            text = (rd / j["prompt"]).read_text()
            has_key = any(k["text"] in text for b in KEYS.values() for k in b)
            self.assertEqual(has_key, j["id"].startswith("verifier"), j["id"])
            self.assertNotIn("SEALED", text)
        self.assertTrue(all(j["model"] == "opus" for j in jobs if j["id"].startswith("J-")))

    def test_blind_refuses_missing_raw(self):
        rd = self.built()
        first = json.loads((rd / "cells.json").read_text())[0]["cell"]
        self.write_raw(rd, skip=(first,))
        with self.assertRaises(SystemExit) as cm:
            gr.blind("demo-skill", seed=6)
        self.assertIn(first, str(cm.exception))

    def test_blind_strips_ordinals_and_writes_plan(self):
        rd = self.built()
        self.write_raw(rd)
        r = gr.blind("demo-skill", seed=6)
        self.assertEqual(r["blind"], 25)
        plan = json.loads((rd / "jobs" / "judge-plan.json").read_text())
        mapping = json.loads((rd / "SEALED.json").read_text())["blind"]
        mains = [c for c in json.loads((rd / "cells.json").read_text()) if c["kind"] == "main"]
        self.assertEqual(sorted(sum(plan["main"].values(), [])), sorted(mapping[f"{c['cell']}.md"] for c in mains))
        self.assertEqual(len(plan["framing_pairs"]), 2)
        some = rd / "blind" / f"{plan['main']['brief-1'][0]}.md"
        self.assertIn("## First point", some.read_text())
        self.assertNotIn("## 1.", some.read_text())


class ScoreTest(RenderBlindTest):
    VALUES = {"new": 6, "old": 5, "none": 4}
    GUARDS = {"new": 6, "old": 6, "none": 5}
    KEYS_OK = {"new": "✓", "old": "~", "none": "✗"}

    def staged(self, skill="demo-skill"):
        rd = self.built(skill)
        self.write_raw(rd, text="A short direct answer with the key points.\n")
        gr.blind(skill, seed=6)
        gr.render(skill, "judge")
        return rd

    def fake_instruments(self, rd, rank_order=("new", "old", "none")):
        sealed = json.loads((rd / "SEALED.json").read_text())
        cells = {c["cell"]: c for c in json.loads((rd / "cells.json").read_text())}
        arm_of = {code: sealed["arms"][cells[f[:-3]]["arm"]] for f, code in sealed["blind"].items()}
        plan = json.loads((rd / "jobs" / "judge-plan.json").read_text())
        for jid in ("J-A", "J-B"):
            for b, codes in plan["main"].items():
                rows = []
                for c in codes:
                    a = arm_of[c]
                    dims = [self.VALUES[a]] * 4 + [self.GUARDS[a]] * 3
                    rows.append(f"{jid},{c}," + ",".join(map(str, dims)) + f",{sum(dims)}")
                order = sorted(codes, key=lambda c: rank_order.index(arm_of[c]))
                (rd / "scores" / f"{jid}-{b}.md").write_text(
                    "```scores\njudge,code,V1,V2,V3,V4,G1,G2,G3,total\n" + "\n".join(rows) + "\n```\n\n"
                    f"```ranking\njudge,brief,order\n{jid},{b},{' '.join(order)}\n```\n")
        audit = {"reports": {c: {"ceremony": [], "leaks": []} for c in sum(plan["main"].values(), []) + plan["negative"]},
                 "framing": {p["pair"]: {"invariant": True, "why": "same"} for p in plan["framing_pairs"]},
                 "negative": {c: {"ceremony": False} for c in plan["negative"]}}
        (rd / "audit" / "audit.json").write_text(json.dumps(audit))
        for b, codes in plan["main"].items():
            ids = [k["id"] for k in KEYS[b]]
            (rd / "keys" / f"{b}.json").write_text(json.dumps(
                {c: {**{i: self.KEYS_OK[arm_of[c]] for i in ids}, "evidence": {i: "q" for i in ids}} for c in codes}))

    def test_score_validated_case(self):
        rd = self.staged()
        self.fake_instruments(rd)
        v = gr.score("demo-skill")
        self.assertEqual(v["validation"]["verdict"], "VALIDATED", v["validation"])
        self.assertEqual(v["rewrite"]["verdict"], "KEEP", v["rewrite"])
        self.assertTrue((rd / "scorecard.md").is_file())
        self.assertLessEqual(len((rd / "scorecard.md").read_text().splitlines()), 40)

    def test_score_refuses_missing_judge_file(self):
        rd = self.staged()
        self.fake_instruments(rd)
        (rd / "scores" / "J-B-brief-2.md").unlink()
        with self.assertRaises(SystemExit) as cm:
            gr.score("demo-skill")
        self.assertIn("J-B-brief-2", str(cm.exception))

    def test_score_unseals_correct_arm(self):
        rd = self.staged()
        self.fake_instruments(rd)
        sealed = json.loads((rd / "SEALED.json").read_text())
        swap = {"new": "none", "none": "new", "old": "old"}
        sealed["arms"] = {c: swap[a] for c, a in sealed["arms"].items()}
        (rd / "SEALED.json").write_text(json.dumps(sealed))
        self.assertEqual(gr.score("demo-skill")["validation"]["verdict"], "NOT VALIDATED")

    def test_score_rewrite_gate_present_only_for_three_arm(self):
        rd = self.staged("demo-two")
        self.fake_instruments(rd, rank_order=("new", "none"))
        self.assertIsNone(gr.score("demo-two")["rewrite"])

    def test_agreement_computation(self):
        rows = [{"judge": "J-A", "code": "A1B", **{d: 5.0 for d in ("V1", "V2", "V3", "V4", "G1", "G2", "G3")}},
                {"judge": "J-B", "code": "A1B", **{d: 5.0 for d in ("V1", "V2", "V3", "V4", "G1", "G2")}, "G3": 3.0}]
        self.assertAlmostEqual(gr.agreement(rows), 6 / 7)


if __name__ == "__main__":
    unittest.main()
