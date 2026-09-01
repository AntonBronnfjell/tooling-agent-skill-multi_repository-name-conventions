gh() {
  if [ "$1" = "repo" ] && [ "$2" = "create" ]; then
    local name=""
    local arg
    for arg in "${@:3}"; do
      case "$arg" in
        -*) ;;
        *) name="$arg"; break ;;
      esac
    done
    if [ -n "$name" ]; then
      local repo_name
      repo_name="$(basename "$name")"
      local hook_dir
      hook_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
      if ! python3 "$hook_dir/../scripts/validate_repo_name.py" "$repo_name"; then
        echo "Blocked: '$repo_name' does not comply with the repository naming convention. See reference/conventions.md, or run scripts/suggest_repo_name.py." >&2
        return 1
      fi
    fi
  fi
  command gh "$@"
}
