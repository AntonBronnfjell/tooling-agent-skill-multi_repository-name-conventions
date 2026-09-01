import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_PATH = ROOT / "reference" / "vocabulary.json"
CONVENTIONS_PATH = ROOT / "reference" / "conventions.md"

EXPECTED_TOP_HEADINGS = [
    "## TL;DR — The Pattern",
    "## The Core Segments",
    "## AI & Agent Repositories",
    "## Enterprise Extensions",
    "## Freelance / Agency Extensions",
    "## Validation",
    "## Examples",
    "## Anti-Patterns",
    "## Related Conventions",
    "## Adopting This in an Existing Org",
]


class TestVocabulary(unittest.TestCase):
    def setUp(self):
        with open(VOCAB_PATH) as f:
            self.vocab = json.load(f)

    def test_top_level_keys(self):
        for key in [
            "purpose", "platform", "repo_type", "language",
            "project_name_suffixes", "enterprise", "freelance",
        ]:
            self.assertIn(key, self.vocab)

    def test_purpose_is_nonempty_list_of_lowercase_strings(self):
        self.assertIsInstance(self.vocab["purpose"], list)
        self.assertGreater(len(self.vocab["purpose"]), 20)
        for value in self.vocab["purpose"]:
            self.assertIsInstance(value, str)
            self.assertEqual(value, value.lower())

    def test_platform_is_dict_of_nonempty_lists(self):
        self.assertIsInstance(self.vocab["platform"], dict)
        self.assertGreaterEqual(len(self.vocab["platform"]), 10)
        for category, values in self.vocab["platform"].items():
            self.assertIsInstance(values, list, msg=category)
            self.assertGreater(len(values), 0, msg=category)

    def test_repo_type_and_language_are_large_lists(self):
        self.assertGreater(len(self.vocab["repo_type"]), 50)
        self.assertGreater(len(self.vocab["language"]), 50)

    def test_enterprise_tiers(self):
        self.assertEqual(
            self.vocab["enterprise"]["tier"],
            ["tier1", "tier2", "tier3", "tier4"],
        )


class TestConventionsDoc(unittest.TestCase):
    def setUp(self):
        self.content = CONVENTIONS_PATH.read_text()

    def test_no_leftover_obsidian_wikilinks(self):
        self.assertNotIn("[[", self.content)
        self.assertNotIn("]]", self.content)

    def test_expected_sections_present(self):
        for heading in EXPECTED_TOP_HEADINGS:
            self.assertIn(heading, self.content)

    def test_is_substantial(self):
        self.assertGreater(len(self.content), 40000)


if __name__ == "__main__":
    unittest.main()
