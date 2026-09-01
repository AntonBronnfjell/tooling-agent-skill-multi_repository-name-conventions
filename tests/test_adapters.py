import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestAdapterFiles(unittest.TestCase):
    def test_skill_md_frontmatter_and_pointers(self):
        content = (ROOT / "SKILL.md").read_text()
        self.assertTrue(content.startswith("---\n"))
        frontmatter = content.split("---\n")[1]
        self.assertIn("name: repo-name-conventions", frontmatter)
        self.assertIn("description:", frontmatter)
        self.assertIn("reference/conventions.md", content)
        self.assertIn("scripts/validate_repo_name.py", content)

    def test_agents_md_points_to_reference_and_scripts(self):
        content = (ROOT / "AGENTS.md").read_text()
        self.assertIn("reference/conventions.md", content)
        self.assertIn("validate_repo_name.py", content)

    def test_gemini_md_points_to_reference(self):
        content = (ROOT / "GEMINI.md").read_text()
        self.assertIn("reference/conventions.md", content)

    def test_cursor_rule_frontmatter_and_pointer(self):
        content = (ROOT / ".cursor" / "rules" / "repo-name-conventions.mdc").read_text()
        self.assertTrue(content.startswith("---\n"))
        self.assertIn("description:", content)
        self.assertIn("reference/conventions.md", content)

    def test_copilot_instructions_points_to_reference(self):
        content = (ROOT / ".github" / "copilot-instructions.md").read_text()
        self.assertIn("reference/conventions.md", content)


if __name__ == "__main__":
    unittest.main()
