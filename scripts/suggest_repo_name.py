import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_repo_name import validate, load_vocab, flatten  # noqa: E402


def build_name(purpose, platform, repo_type, language, project_name,
               modules=None, leading=None, trailing=None):
    prefix_parts = list(leading or []) + [purpose, platform, repo_type, language]
    name = "-".join(prefix_parts) + "_" + project_name
    for module in (modules or []):
        name += "." + module
    for suffix in (trailing or []):
        name += "-" + suffix
    return name


def prompt_choice(label, options):
    print(f"\n{label} -- pick one, or type a value not listed:")
    for opt in sorted(options)[:20]:
        print(f"  {opt}")
    if len(options) > 20:
        print(f"  ... and {len(options) - 20} more (type any known value)")
    return input(f"{label}: ").strip().lower()


def interactive():
    vocab = load_vocab()
    purpose = prompt_choice("purpose", flatten(vocab["purpose"]))
    platform = prompt_choice("platform", flatten(vocab["platform"]))
    repo_type = prompt_choice("repo-type", flatten(vocab["repo_type"]))
    language = prompt_choice("language", flatten(vocab["language"]))
    project_name = input("project-name (kebab-case): ").strip().lower()
    modules_raw = input("project-module(s), dot-separated, optional: ").strip().lower()
    modules = [m for m in modules_raw.split(".") if m] if modules_raw else []
    trailing_raw = input(
        "trailing suffixes (tier/env/region/lifecycle), hyphen-separated, optional: "
    ).strip().lower()
    trailing = [t for t in trailing_raw.split("-") if t] if trailing_raw else []
    return build_name(purpose, platform, repo_type, language, project_name, modules, [], trailing)


def main():
    parser = argparse.ArgumentParser(description="Suggest a compliant repository name.")
    parser.add_argument("--purpose")
    parser.add_argument("--platform")
    parser.add_argument("--repo-type")
    parser.add_argument("--language")
    parser.add_argument("--name", help="project name")
    parser.add_argument("--modules", help="dot-separated project modules")
    parser.add_argument("--trailing", help="hyphen-separated trailing suffixes")
    args = parser.parse_args()

    if args.purpose and args.platform and args.repo_type and args.language and args.name:
        modules = args.modules.split(".") if args.modules else []
        trailing = args.trailing.split("-") if args.trailing else []
        name = build_name(
            args.purpose, args.platform, args.repo_type, args.language,
            args.name, modules, [], trailing,
        )
    else:
        name = interactive()

    errors, warnings = validate(name)
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"Assembled name failed validation: {name}")
        sys.exit(1)

    print(name)
    sys.exit(0)


if __name__ == "__main__":
    main()
