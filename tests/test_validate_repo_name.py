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
    "client-acme-docs-astro-web-markdown_storefront-docs",
    "project-unity-game-csharp_puzzle-prototype",
    "project-chrome-browserext-typescript_tab-manager",
    "project-ethereum-contract-solidity_escrow-vault",
    "tooling-opentelemetry-observability-yaml_service-slos",
    "tooling-playwright-e2e-typescript_checkout-flows",
    "data-dbt-pipeline-sql_warehouse-models",
]

STRUCTURALLY_INVALID_NAMES = [
    "MyAwesomeRepo",
    "project_react_web",
    "2024-portfolio",
    "my-awesome-thing",
]

KNOWN_STRICT_MODE_VOCAB_GAPS = [
    "project-aws-cloud-terraform_portfolio-infra",
    "acme-data-platform-pipeline-python-etl-python_warehouse-loaders",
    "acme-eng-platform-project-typescript-cli-typescript_internal-cli-tier2",
    "acme-ops-infra-cloud-terraform-hcl_kubernetes-baseline-tier1",
    "config-nix-infra-nix_workstation-baseline",
    "acme-eng-platform-project-typescript-monorepo-typescript_design-system",
    "acme-eng-platform-project-typescript-monorepo-typescript_design-system.tokens",
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

    def test_known_strict_mode_vocabulary_gaps_are_documented(self):
        # These are real examples from reference/conventions.md's own Examples
        # section that use keywords not present in reference/vocabulary.json's
        # tables (e.g. "terraform"/"typescript"/"nix" used as a core segment
        # value where the tables list "hcl" or a web-frontend category
        # instead). This is a known inconsistency between the source guide's
        # prose and its own tables -- not a bug in the validator or in
        # vocabulary.json's transcription. They still pass default (non-strict)
        # validation; only --strict elevates the unknown-vocabulary warnings
        # to errors.
        for name in KNOWN_STRICT_MODE_VOCAB_GAPS:
            with self.subTest(name=name):
                errors, warnings = validate(name)
                self.assertEqual(errors, [])
                self.assertTrue(warnings)
                strict_errors, _ = validate(name, strict=True)
                self.assertTrue(strict_errors)


if __name__ == "__main__":
    unittest.main()
