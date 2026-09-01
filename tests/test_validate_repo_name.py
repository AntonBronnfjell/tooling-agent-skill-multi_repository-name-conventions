import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_repo_name import validate  # noqa: E402

VALID_NAMES = [
    "project-nextjs-web-typescript_portfolio",
    "docs-astro-web-markdown_portfolio-docs",
    "sandbox-linux-shell-bash_dotfile-scripts",
    "challenge-nodejs-cli-typescript_advent-of-code-2025",
    "client-acme-project-nextjs-web-typescript_storefront",
    "client-northwind-2025-project-flutter-mobile-dart_loyalty-app",
    "acme-fin-payments-service-go-microservice-go_ledger-tier1",
    "acme-fin-payments-service-go-microservice-go_ledger-tier1-eu",
    "acme-fin-payments-service-go-microservice-go_ledger.posting-tier1",
    "acme-ml-platform-service-vllm-service-python_inference-gateway-tier1",
    "tooling-claude-skill-markdown_invoice-parser",
    "tooling-agent-skill-markdown_invoice-parser",
    "tooling-mcp-mcpserver-typescript_github-issues",
    "acme-eng-platform-project-typescript-monorepo-typescript_design-system.tokens",
    "tooling-agent-skill-multi_repository-name-conventions",
]

STRUCTURALLY_INVALID_NAMES = [
    "MyAwesomeRepo",
    "project_react_web",
    "2024-portfolio",
    "my-awesome-thing",
]


class TestValidateRepoName(unittest.TestCase):
    def test_known_valid_names_pass_with_no_errors(self):
        for name in VALID_NAMES:
            with self.subTest(name=name):
                errors, warnings = validate(name)
                self.assertEqual(errors, [], msg=f"{name}: {errors}")

    def test_known_invalid_names_fail_structurally(self):
        for name in STRUCTURALLY_INVALID_NAMES:
            with self.subTest(name=name):
                errors, warnings = validate(name)
                self.assertTrue(errors, msg=f"{name} should have failed")

    def test_unknown_vocab_is_warning_not_error_by_default(self):
        errors, warnings = validate("prj-rx-w-js_pf")
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 4)

    def test_unknown_vocab_is_error_in_strict_mode(self):
        errors, warnings = validate("prj-rx-w-js_pf", strict=True)
        self.assertEqual(len(errors), 4)


if __name__ == "__main__":
    unittest.main()
