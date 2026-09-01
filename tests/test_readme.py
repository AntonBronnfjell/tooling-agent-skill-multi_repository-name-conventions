import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

REQUIRED_SECTIONS = [
    "## What this is",
    "## Why repository naming conventions matter",
    "## The pattern, at a glance",
    "## Quick start",
    "## Install as a global skill",
    "## Validating and suggesting names",
    "## Enforcing the convention",
    "## Extending the vocabulary",
    "## FAQ",
]


class TestReadme(unittest.TestCase):
    def test_required_sections_present(self):
        content = README.read_text()
        for section in REQUIRED_SECTIONS:
            self.assertIn(section, content)


if __name__ == "__main__":
    unittest.main()
