#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="repo-name-conventions"

force=false
host_selected=false
agents=false
copilot=false
claude=false
cursor=false
gemini=false

usage() {
  echo "Usage: $0 [--agents] [--copilot] [--claude] [--cursor] [--gemini] [--force]" >&2
}

while (($#)); do
  case "$1" in
    --agents)
      agents=true
      host_selected=true
      ;;
    --copilot)
      copilot=true
      host_selected=true
      ;;
    --claude)
      claude=true
      host_selected=true
      ;;
    --cursor)
      cursor=true
      host_selected=true
      ;;
    --gemini)
      gemini=true
      host_selected=true
      ;;
    --force)
      force=true
      ;;
    *)
      usage
      exit 2
      ;;
  esac
  shift
done

if ! "$host_selected"; then
  agents=true
  copilot=true
  claude=true
  cursor=true
  gemini=true
fi

if "$cursor" || "$gemini"; then
  agents=true
fi

preflight_destination() {
  local destination="$1"
  if [[ -e "$destination" && "$force" != true ]]; then
    echo "Refusing to overwrite $destination; pass --force." >&2
    exit 1
  fi
}

copy_tree() {
  local destination="$1"

  rm -rf "$destination"
  mkdir -p "$(dirname "$destination")"

  python3 - "$ROOT" "$destination" <<'PY'
import shutil
import sys
from pathlib import Path

source = Path(sys.argv[1])
destination = Path(sys.argv[2])
excluded_names = {
    ".git",
    ".pytest_cache",
    ".superpowers",
    ".test-workspaces",
    ".worktrees",
    ".DS_Store",
    ".venv",
    "__pycache__",
    "venv",
}
excluded_suffixes = (".egg-info", ".pyc")


def ignore(_directory, names):
    ignored = []
    for name in names:
        if name in excluded_names or name.endswith(excluded_suffixes):
            ignored.append(name)
    return ignored


shutil.copytree(source, destination, ignore=ignore, copy_function=shutil.copy2)
PY
}

copy_file() {
  local source="$1"
  local destination="$2"

  if [[ ! -f "$source" ]]; then
    echo "Missing source: $source" >&2
    exit 1
  fi

  mkdir -p "$(dirname "$destination")"
  rm -f "$destination"
  cp "$source" "$destination"
}

staging_dir="$HOME/.${NAME}-install-staging.$$"
cleanup() {
  rm -rf "$staging_dir"
}
trap cleanup EXIT
mkdir -p "$staging_dir"

if "$agents"; then
  preflight_destination "$HOME/.agents/skills/$NAME"
fi
if "$copilot"; then
  preflight_destination "$HOME/.copilot/skills/$NAME"
fi
if "$claude"; then
  preflight_destination "$HOME/.claude/skills/$NAME"
fi
if "$cursor"; then
  preflight_destination "$HOME/.cursor/commands/$NAME.md"
fi
if "$gemini"; then
  preflight_destination "$HOME/.gemini/commands/$NAME.toml"
fi

if "$agents"; then
  copy_tree "$HOME/.agents/skills/$NAME"
fi
if "$copilot"; then
  copy_tree "$HOME/.copilot/skills/$NAME"
fi
if "$claude"; then
  copy_tree "$HOME/.claude/skills/$NAME"
fi

if "$cursor"; then
  cursor_source="$staging_dir/$NAME.md"
  cat >"$cursor_source" <<'EOF'
Read and follow `~/.agents/skills/repo-name-conventions/SKILL.md`. Use its
bundled validator and suggester scripts instead of guessing repository names.
EOF
  copy_file "$cursor_source" "$HOME/.cursor/commands/$NAME.md"
fi

if "$gemini"; then
  gemini_source="$staging_dir/$NAME.toml"
  cat >"$gemini_source" <<'EOF'
description = "Apply the repository name conventions skill."
prompt = "Read and follow ~/.agents/skills/repo-name-conventions/SKILL.md. Use its bundled validator and suggester scripts instead of guessing repository names."
EOF
  copy_file "$gemini_source" "$HOME/.gemini/commands/$NAME.toml"
fi
