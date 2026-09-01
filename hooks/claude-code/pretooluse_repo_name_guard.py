#!/usr/bin/env python3
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

HOOK_DIR = Path(__file__).resolve().parent
VALIDATOR = HOOK_DIR.parent.parent / "scripts" / "validate_repo_name.py"

CONTROL_OPERATORS = re.compile(r"(&&|\|\||[;|])")

# Flags known to take no value -- everything else starting with "-" is
# treated as consuming the next token as its value (skip both), unless it's
# in "--flag=value" form. This errs toward skipping too much rather than
# misidentifying a flag's value as the repo name (a false denial of a valid
# name is worse than occasionally missing a bad one -- CI is the real gate).
BOOLEAN_FLAGS = {
    "--public", "--private", "--internal", "--clone", "--push",
    "--add-readme", "--disable-issues", "--disable-wiki",
    "--bare", "--quiet", "-q", "--shared",
}


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def find_candidate_name(tokens_after_command):
    skip_next = False
    for token in tokens_after_command:
        if skip_next:
            skip_next = False
            continue
        if token.startswith("-"):
            if "=" not in token and token not in BOOLEAN_FLAGS:
                skip_next = True
            continue
        return token
    return None


def looks_like_non_name(token):
    return token in (".", "..") or token.startswith("/") or token.startswith(".")


def extract_repo_name_candidate(command):
    segments_raw = CONTROL_OPERATORS.split(command)
    for segment in segments_raw:
        segment = segment.strip()
        if not segment or CONTROL_OPERATORS.fullmatch(segment):
            continue
        try:
            tokens = shlex.split(segment)
        except ValueError:
            continue
        if len(tokens) >= 3 and tokens[0] == "gh" and tokens[1] == "repo" and tokens[2] == "create":
            candidate = find_candidate_name(tokens[3:])
            if candidate:
                return candidate
        elif len(tokens) >= 2 and tokens[0] == "git" and tokens[1] == "init":
            candidate = find_candidate_name(tokens[2:])
            if candidate and not looks_like_non_name(candidate):
                return candidate
    return None


def main():
    hook_input = json.load(sys.stdin)
    command = hook_input.get("tool_input", {}).get("command", "")

    candidate = extract_repo_name_candidate(command)
    if not candidate:
        sys.exit(0)

    repo_name = candidate.rsplit("/", 1)[-1]

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), repo_name],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        reason_lines = [
            line for line in result.stdout.splitlines() if line.startswith("ERROR:")
        ]
        reason = "; ".join(reason_lines) or f"'{repo_name}' failed repository naming validation"
        deny(f"{reason} (from command token '{candidate}')")

    sys.exit(0)


if __name__ == "__main__":
    main()
