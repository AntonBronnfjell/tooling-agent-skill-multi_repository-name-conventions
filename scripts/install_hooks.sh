#!/bin/bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK_LINE="source \"$REPO_ROOT/hooks/gh-repo-create.sh\""

echo "This installs a shell function that validates repo names before 'gh repo create' runs."
echo
echo "Add this line to your shell rc file (~/.zshrc or ~/.bashrc), then restart your shell:"
echo
echo "  $HOOK_LINE"
echo
echo "This script does not edit your rc file automatically -- copy the line above yourself."
