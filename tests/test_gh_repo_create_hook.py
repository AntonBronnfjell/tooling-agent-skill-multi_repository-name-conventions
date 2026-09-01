import os
import shutil
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

    def run_gh(self, args, shell="bash"):
        script = f'source "{HOOK}"\ngh {args}\n'
        return subprocess.run(
            [shell, "-c", script], capture_output=True, text=True, env=self.env,
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

    def test_flag_value_with_spaces_before_name_does_not_false_block(self):
        result = self.run_gh(
            "repo create --description 'my cool repo' tooling-agent-skill-markdown_demo"
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("FAKE_GH_CALLED", result.stdout)

    def test_flags_before_bad_name_pass_through_unvalidated(self):
        # Documented, deliberate limitation: gh repo create's canonical usage is
        # `gh repo create [<name>] [flags]`, so this hook only inspects the third
        # word. A name preceded by flags is not validated (fail-open) rather than
        # risk misidentifying a flag's value as the name.
        result = self.run_gh("repo create --description x BadName")
        self.assertEqual(result.returncode, 0)
        self.assertIn("FAKE_GH_CALLED", result.stdout)

    @unittest.skipUnless(shutil.which("zsh"), "zsh not available on this system")
    def test_valid_name_passes_through_under_zsh(self):
        result = self.run_gh(
            "repo create tooling-agent-skill-markdown_demo --public", shell="zsh"
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("FAKE_GH_CALLED", result.stdout)

    @unittest.skipUnless(shutil.which("zsh"), "zsh not available on this system")
    def test_invalid_name_is_blocked_under_zsh(self):
        result = self.run_gh("repo create MyBadRepoName --public", shell="zsh")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("FAKE_GH_CALLED", result.stdout)


if __name__ == "__main__":
    unittest.main()
