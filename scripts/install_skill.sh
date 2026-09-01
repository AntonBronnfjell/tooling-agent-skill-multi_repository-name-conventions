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
  local relative_path

  rm -rf "$destination"
  mkdir -p "$destination"

  while IFS= read -r -d '' relative_path; do
    local source="$ROOT/$relative_path"
    local target="$destination/$relative_path"

    mkdir -p "$(dirname "$target")"
    cp -R "$source" "$target"
  done < <(git -C "$ROOT" ls-files --cached -z)
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
