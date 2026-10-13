import os
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "link_local.sh"
SKILLS = sorted(p.name for p in (REPO / "skills").iterdir() if p.is_dir())


class LinkLocalTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.target = self.tmp / "target"
        self.backup = self.tmp / "backup"
        (self.target / "tree-of-thoughts").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def run_script(self, *args: str) -> list[str]:
        env = {**os.environ, "LINK_BACKUP_DIR": str(self.backup)}
        out = subprocess.run(["bash", str(SCRIPT), *args], env=env, capture_output=True, text=True, check=True)
        return out.stdout.splitlines()

    def test_backs_up_existing_and_links_all(self):
        lines = self.run_script(str(self.target))
        self.assertIn("backup tree-of-thoughts", lines)
        self.assertEqual(sum(l.startswith("link ") for l in lines), len(SKILLS))
        for name in SKILLS:
            self.assertEqual((self.target / name).resolve(), REPO / "skills" / name)
        self.assertTrue((self.backup / "tree-of-thoughts").is_dir())

    def test_second_run_is_noop(self):
        self.run_script(str(self.target))
        lines = self.run_script(str(self.target))
        self.assertEqual(lines, [f"ok {name}" for name in SKILLS])
        self.assertEqual([p.name for p in self.backup.iterdir()], ["tree-of-thoughts"])

    def test_named_skill_only(self):
        lines = self.run_script(str(self.tmp / "t2"), "premortem-evolved")
        self.assertEqual(lines, ["link premortem-evolved"])
        self.assertEqual([p.name for p in (self.tmp / "t2").iterdir()], ["premortem-evolved"])


if __name__ == "__main__":
    unittest.main()
