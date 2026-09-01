import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "suggest_repo_name.py"


class TestSuggestRepoName(unittest.TestCase):
    def test_flag_driven_produces_expected_name(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT),
             "--purpose", "tooling", "--platform", "agent",
             "--repo-type", "skill", "--language", "markdown",
             "--name", "invoice-parser"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            result.stdout.strip().splitlines()[-1],
            "tooling-agent-skill-markdown_invoice-parser",
        )

    def test_flag_driven_rejects_invalid_assembled_name(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT),
             "--purpose", "tooling", "--platform", "agent",
             "--repo-type", "skill", "--language", "markdown",
             "--name", "InvoiceParser"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)

    def test_interactive_mode_builds_name_from_prompts(self):
        stdin = "tooling\nagent\nskill\nmarkdown\ninvoice-parser\n\n\n"
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=stdin, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue(
            result.stdout.rstrip().endswith("tooling-agent-skill-markdown_invoice-parser"),
            msg=result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
