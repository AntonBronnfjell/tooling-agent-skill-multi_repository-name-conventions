import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK = ROOT / "hooks" / "gh-repo-create.sh"


class TestGhRepoCreateHook(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        fake_gh = Path(self.tmp.name) / "gh"
        fake_gh.write_text('#!/bin/bash\necho FAKE_GH_CALLED "$@"\n')
        fake_gh.chmod(0o755)
        self.env = dict(os.environ)
        self.env["PATH"] = f"{self.tmp.name}:{self.env['PATH']}"

    def run_gh(self, args):
        script = f'source "{HOOK}"\ngh {args}\n'
        return subprocess.run(
            ["bash", "-c", script], capture_output=True, text=True, env=self.env,
        )

    def test_valid_name_passes_through_to_real_gh(self):
        result = self.run_gh(
            "repo create tooling-agent-skill-markdown_demo --public"
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "FAKE_GH_CALLED repo create tooling-agent-skill-markdown_demo --public",
            result.stdout,
        )

    def test_invalid_name_is_blocked(self):
        result = self.run_gh("repo create MyBadRepoName --public")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("FAKE_GH_CALLED", result.stdout)
        self.assertIn("does not comply", result.stderr)

    def test_owner_prefixed_name_is_validated_by_basename(self):
        result = self.run_gh("repo create AntonBronnfjell/BadName --public")
        self.assertNotEqual(result.returncode, 0)

    def test_non_create_gh_command_passes_through_untouched(self):
        result = self.run_gh("repo list")
        self.assertEqual(result.returncode, 0)
        self.assertIn("FAKE_GH_CALLED repo list", result.stdout)


if __name__ == "__main__":
    unittest.main()
