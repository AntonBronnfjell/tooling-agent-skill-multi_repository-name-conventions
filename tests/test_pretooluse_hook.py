import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK = ROOT / "hooks" / "claude-code" / "pretooluse_repo_name_guard.py"


class TestPreToolUseHook(unittest.TestCase):
    def run_hook(self, command):
        stdin = json.dumps({
            "hook_event_name": "PreToolUse",
            "tool_name": "Bash",
            "tool_input": {"command": command},
        })
        return subprocess.run(
            [sys.executable, str(HOOK)],
            input=stdin, capture_output=True, text=True,
        )

    def test_valid_repo_name_is_allowed_silently(self):
        result = self.run_hook(
            "gh repo create tooling-agent-skill-markdown_demo --public"
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_invalid_repo_name_is_denied_with_reason(self):
        result = self.run_hook("gh repo create MyBadName --public")
        self.assertEqual(result.returncode, 0)
        output = json.loads(result.stdout)
        self.assertEqual(
            output["hookSpecificOutput"]["permissionDecision"], "deny"
        )
        self.assertIn(
            "ERROR", output["hookSpecificOutput"]["permissionDecisionReason"]
        )

    def test_unrelated_command_is_allowed_silently(self):
        result = self.run_hook("ls -la")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_interactive_create_with_no_name_is_allowed(self):
        result = self.run_hook("gh repo create")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_plain_git_init_with_dot_is_allowed(self):
        result = self.run_hook("git init .")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_plain_git_init_with_no_args_is_allowed(self):
        result = self.run_hook("git init")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_chained_git_init_command_is_allowed(self):
        result = self.run_hook("mkdir foo && cd foo && git init && npm init -y")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_quoted_string_mentioning_gh_repo_create_is_not_matched(self):
        result = self.run_hook('echo "gh repo create MyBadName"')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_flag_before_name_is_still_caught(self):
        result = self.run_hook("gh repo create --public MyBadName")
        self.assertEqual(result.returncode, 0)
        output = json.loads(result.stdout)
        self.assertEqual(
            output["hookSpecificOutput"]["permissionDecision"], "deny"
        )

    def test_git_init_with_a_real_bad_name_is_caught(self):
        result = self.run_hook("git init my-Really-Bad-Name")
        self.assertEqual(result.returncode, 0)
        output = json.loads(result.stdout)
        self.assertEqual(
            output["hookSpecificOutput"]["permissionDecision"], "deny"
        )


if __name__ == "__main__":
    unittest.main()
