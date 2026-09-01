import argparse
import json
import re
import sys
from pathlib import Path

VOCAB_PATH = Path(__file__).resolve().parent.parent / "reference" / "vocabulary.json"

CORE_PATTERN = re.compile(
    r"^[a-z]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+_[a-z0-9]+(-[a-z0-9]+)*(\.[a-z0-9]+(-[a-z0-9]+)*){0,2}$"
)
FULL_PATTERN = re.compile(
    r"^([a-z0-9]+-){0,4}[a-z]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+_[a-z0-9]+(-[a-z0-9]+)*"
    r"(\.[a-z0-9]+(-[a-z0-9]+)*){0,2}(-[a-z0-9]+){0,4}$"
)


def load_vocab():
    with open(VOCAB_PATH) as f:
        return json.load(f)


def flatten(value):
    """Flatten a vocab entry (a list, or a dict of lists) into one set of strings."""
    if isinstance(value, list):
        return set(value)
    if isinstance(value, dict):
        out = set()
        for v in value.values():
            if isinstance(v, list):
                out |= set(v)
        return out
    return set()


def extract_core_segments(name):
    """Return the four hyphen tokens immediately preceding the first
    underscore -- (purpose, platform, repo_type, language) -- or None if
    the name has no such block."""
    if "_" not in name:
        return None
    prefix = name.split("_", 1)[0]
    tokens = prefix.split("-")
    if len(tokens) < 4:
        return None
    return tuple(tokens[-4:])


def validate(name, strict=False):
    errors = []
    warnings = []

    if not (CORE_PATTERN.match(name) or FULL_PATTERN.match(name)):
        errors.append(
            "does not match the repository naming pattern "
            "(<purpose>-<platform>-<repo-type>-<language>_<project-name>, "
            "optionally with leading org/domain/team/client segments and "
            "trailing env/region/tier/lifecycle segments)"
        )
        return errors, warnings

    vocab = load_vocab()
    segments = extract_core_segments(name)
    if segments is None:
        errors.append("could not locate the four required core segments before '_'")
        return errors, warnings

    purpose, platform, repo_type, language = segments
    checks = [
        ("purpose", purpose, flatten(vocab["purpose"])),
        ("platform", platform, flatten(vocab["platform"])),
        ("repo_type", repo_type, flatten(vocab["repo_type"])),
        ("language", language, flatten(vocab["language"])),
    ]
    for label, value, allowed in checks:
        if value not in allowed:
            message = f"{label} segment '{value}' is not in the known vocabulary"
            if strict:
                errors.append(message)
            else:
                warnings.append(message)

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Validate a repository name against the naming convention."
    )
    parser.add_argument("name")
    parser.add_argument(
        "--strict", action="store_true",
        help="Treat unknown vocabulary as errors, not warnings.",
    )
    args = parser.parse_args()

    errors, warnings = validate(args.name, strict=args.strict)

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    if errors:
        print(f"INVALID: {args.name}")
        sys.exit(1)
    print(f"VALID: {args.name}")
    sys.exit(0)


if __name__ == "__main__":
    main()
