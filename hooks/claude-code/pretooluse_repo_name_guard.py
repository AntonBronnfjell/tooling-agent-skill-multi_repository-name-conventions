#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

HOOK_DIR = Path(__file__).resolve().parent
VALIDATOR = HOOK_DIR.parent.parent / "scripts" / "validate_repo_name.py"

COMMAND_PATTERN = re.compile(r"(?:gh repo create|git init)\s+(\S+)")


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def main():
    hook_input = json.load(sys.stdin)
    command = hook_input.get("tool_input", {}).get("command", "")

    match = COMMAND_PATTERN.search(command)
    if not match:
        sys.exit(0)

    candidate = match.group(1)
    if candidate.startswith("-"):
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
        deny(reason)

    sys.exit(0)


if __name__ == "__main__":
    main()
