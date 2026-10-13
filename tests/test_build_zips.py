import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from build_zips import build_zip, main, strip_frontmatter  # noqa: E402
from validate_skills import parse_frontmatter  # noqa: E402

SKILL_MD = """---
name: demo-skill
description: Does a thing.
model: opus
context: fork
agent: general-purpose
user-invocable: true
metadata:
  version: "1.0.0"
---

# Demo

Body stays *exactly* as written.
"""


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


class StripFrontmatterTest(unittest.TestCase):
    def test_strip_keeps_only_spec_keys(self):
        meta, body = parse_frontmatter(strip_frontmatter(SKILL_MD))
        self.assertEqual(set(meta), {"name", "description", "metadata"})
        self.assertEqual(meta["metadata"], {"version": "1.0.0"})
        self.assertEqual(body, parse_frontmatter(SKILL_MD)[1])


class BuildZipTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name) / "repo"
        skill = self.repo / "skills" / "demo-skill"
        (skill / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_text(SKILL_MD)
        (skill / "references" / "public.md").write_text("public\n")
        git(self.repo, "init", "-q")
        git(self.repo, "add", ".")
        git(self.repo, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "init")
        (self.repo / ".git" / "info" / "exclude").write_text("skills/demo-skill/references/private.md\n")
        (skill / "references" / "private.md").write_text("private\n")
        self.out = Path(self._tmp.name) / "dist"

    def tearDown(self):
        self._tmp.cleanup()

    def names(self, with_overlays: bool) -> set[str]:
        with zipfile.ZipFile(build_zip(self.repo, "demo-skill", self.out, with_overlays)) as z:
            return set(z.namelist())

    def test_zip_root_is_skill_folder(self):
        names = self.names(False)
        self.assertTrue(all(n.startswith("demo-skill/") for n in names))
        self.assertIn("demo-skill/SKILL.md", names)

    def test_overlay_excluded_by_default_included_with_flag(self):
        self.assertNotIn("demo-skill/references/private.md", self.names(False))
        self.assertIn("demo-skill/references/private.md", self.names(True))


class MainGuardTest(unittest.TestCase):
    def test_with_overlays_refuses_output_inside_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit) as cm:
                main(["--with-overlays", "--out", str(Path(__file__).resolve().parent.parent / "dist"), "premortem-evolved"])
            self.assertEqual(cm.exception.code, 2)
            out = Path(tmp) / "personal"
            self.assertEqual(main(["--with-overlays", "--out", str(out), "premortem-evolved"]), 0)
            self.assertTrue((out / "premortem-evolved.zip").is_file())


if __name__ == "__main__":
    unittest.main()
