import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from validate_skills import check_privacy, check_skill  # noqa: E402

FRONTMATTER = 'name: demo-skill\ndescription: Does a thing.\nmetadata:\n  version: "1.0.0"\n'


def make_skill(root: Path, dirname: str = "demo-skill", frontmatter: str = FRONTMATTER,
               body: str = "# Demo\n", files: dict | None = None) -> Path:
    d = root / dirname
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(f"---\n{frontmatter}---\n\n{body}")
    for rel, text in (files or {}).items():
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        (d / rel).write_text(text)
    return d


class CheckSkillTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_valid_skill_passes(self):
        self.assertEqual(check_skill(make_skill(self.root)), [])

    def test_name_must_match_dir(self):
        d = make_skill(self.root, frontmatter=FRONTMATTER.replace("demo-skill", "other-skill"))
        errors = check_skill(d)
        self.assertEqual(len(errors), 1)
        self.assertIn("does not match directory", errors[0])

    def test_name_charset(self):
        d = make_skill(self.root, dirname="Bad_Name", frontmatter=FRONTMATTER.replace("demo-skill", "Bad_Name"))
        self.assertTrue(any("invalid name" in e for e in check_skill(d)))

    def test_description_too_long(self):
        d = make_skill(self.root, frontmatter=FRONTMATTER.replace("Does a thing.", "x" * 1025))
        self.assertTrue(any("description" in e for e in check_skill(d)))

    def test_metadata_version_required_and_semver(self):
        missing = make_skill(self.root, dirname="a", frontmatter='name: a\ndescription: d\nmetadata:\n  owner: me\n')
        self.assertTrue(any("metadata.version" in e for e in check_skill(missing)))
        loose = make_skill(self.root, dirname="b", frontmatter='name: b\ndescription: d\nmetadata:\n  version: "2.2"\n')
        self.assertTrue(any("metadata.version" in e for e in check_skill(loose)))

    def test_metadata_values_must_be_strings(self):
        d = make_skill(self.root, frontmatter=FRONTMATTER + "  n: 3\n")
        self.assertTrue(any("metadata" in e for e in check_skill(d)))

    def test_broken_reference_link(self):
        d = make_skill(self.root, body="See [x](references/missing.md).\n")
        self.assertTrue(any("references/missing.md" in e for e in check_skill(d)))

    def test_link_with_anchor_resolves(self):
        d = make_skill(self.root, body="See [x](references/a.md#sec).\n", files={"references/a.md": "# A\n"})
        self.assertEqual(check_skill(d), [])

    def test_install_path_reference_flagged(self):
        d = make_skill(self.root, body="**Templates**: `~/.claude/skills/demo-skill/references/a.md`\n",
                       files={"references/a.md": "# A\n"})
        self.assertTrue(any("install path" in e for e in check_skill(d)))

    def test_prose_path_not_checked(self):
        d = make_skill(self.root, body="see `scripts/other.py` in another skill\n")
        self.assertEqual(check_skill(d), [])


class CheckPrivacyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def scan(self, text: str, denylist=()):
        (self.repo / "f.md").write_text(text)
        return check_privacy(self.repo, ["f.md"], list(denylist))

    def test_privacy_home_path(self):
        hits = self.scan("path " + "/" + "home/alice/x" + "\n")
        self.assertEqual(len(hits), 1)
        self.assertIn("home path", hits[0])

    def test_privacy_email(self):
        hits = self.scan("bob" + "@" + "corp.io and noreply@anthropic.com\n")
        self.assertEqual(len(hits), 1)
        self.assertIn("bob", hits[0])

    def test_privacy_denylist_case_insensitive(self):
        self.assertEqual(len(self.scan("about secretco plans\n", ["SecretCo"])), 1)


if __name__ == "__main__":
    unittest.main()
