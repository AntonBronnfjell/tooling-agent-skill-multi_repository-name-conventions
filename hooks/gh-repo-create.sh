if [ -n "${BASH_SOURCE:-}" ]; then
  _rnc_src="${BASH_SOURCE[0]}"
elif [ -n "${ZSH_VERSION:-}" ]; then
  _rnc_src="${(%):-%x}"
else
  _rnc_src="$0"
fi
_RNC_HOOK_ROOT="$(cd "$(dirname "$_rnc_src")/.." && pwd)"
unset _rnc_src

gh() {
  if [ "$1" = "repo" ] && [ "$2" = "create" ]; then
    # gh repo create's canonical usage is `gh repo create [<name>] [flags]`;
    # if flags come before the name, this hook doesn't see it and lets the
    # call through unchecked (fail-open rather than misidentifying a flag's
    # value as the name).
    local name="$3"
    case "$name" in
      -*|"") name="" ;;
    esac
    if [ -n "$name" ]; then
      local repo_name
      repo_name="$(basename "$name")"
      local validator="$_RNC_HOOK_ROOT/scripts/validate_repo_name.py"
      if [ ! -f "$validator" ]; then
        echo "Warning: repo-name-conventions validator not found at $validator -- skipping name check." >&2
      else
        local validator_output
        if ! validator_output="$(python3 "$validator" "$repo_name" 2>&1)"; then
          echo "$validator_output" >&2
          echo "Blocked: '$repo_name' does not comply with the repository naming convention. See reference/conventions.md, or run scripts/suggest_repo_name.py." >&2
          return 1
        fi
      fi
    fi
  fi
  command gh "$@"
}
