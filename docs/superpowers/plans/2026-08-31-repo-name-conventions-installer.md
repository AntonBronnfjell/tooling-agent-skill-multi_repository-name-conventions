# Repository Name Conventions Installer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make this repository globally installable as the `repo-name-conventions` skill and command across supported hosts.

**Architecture:** A single Bash installer copies the existing repository content into each native Agent Skill location, omitting only `.git`. It writes lightweight Cursor and Gemini command adapters that point at the canonical `~/.agents/skills/repo-name-conventions` installation, which is installed automatically whenever either adapter is selected.

**Tech Stack:** Bash, Markdown, TOML, Python standard-library `unittest`.

## Global Constraints

- Do not alter the existing naming rules, validator, or suggester.
- Do not add dependencies.
- The installed skill name is exactly `repo-name-conventions`.
- Default installation targets are `--agents`, `--copilot`, `--claude`, `--cursor`, and `--gemini`.
- `--cursor` and `--gemini` must install their canonical `--agents` dependency.
- Refuse every selected existing destination unless `--force` is supplied.
- Do not claim universal slash-command support for generic Agent Skills readers.

---

## File Structure

| File | Responsibility |
|---|---|
| `scripts/install_skill.sh` | Install this repository and native host command adapters safely. |
| `tests/test_install_skill.py` | Verify isolated-home installation behavior. |
| `README.md` | Document global installation and host-specific invocation. |
| `tests/test_readme.py` | Assert the new README section stays present. |

### Task 1: Add the Installer and Its Isolated-Home Tests

**Files:**
- Create: `scripts/install_skill.sh`
- Create: `tests/test_install_skill.py`

**Interfaces:**
- CLI: `bash scripts/install_skill.sh [--agents] [--copilot] [--claude] [--cursor] [--gemini] [--force]`.
- Produces: copies at `"$HOME/.agents/skills/repo-name-conventions"`, `"$HOME/.copilot/skills/repo-name-conventions"`, and `"$HOME/.claude/skills/repo-name-conventions"`.
- Produces: `"$HOME/.cursor/commands/repo-name-conventions.md"` and `"$HOME/.gemini/commands/repo-name-conventions.toml"`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_install_skill.py`:

```python
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTALLER = ROOT / "scripts" / "install_skill.sh"
NAME = "repo-name-conventions"


class TestInstallSkill(unittest.TestCase):
    def run_installer(self, home, *args):
        return subprocess.run(
            ["bash", str(INSTALLER), *args],
            cwd=ROOT,
            env={**os.environ, "HOME": str(home)},
            text=True,
            capture_output=True,
        )

    def test_default_install_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home"
            result = self.run_installer(home)
            self.assertEqual(result.returncode, 0, result.stderr)
            for path in (
                home / ".agents" / "skills" / NAME / "SKILL.md",
                home / ".copilot" / "skills" / NAME / "SKILL.md",
                home / ".claude" / "skills" / NAME / "SKILL.md",
                home / ".cursor" / "commands" / f"{NAME}.md",
                home / ".gemini" / "commands" / f"{NAME}.toml",
            ):
                self.assertTrue(path.is_file(), path)
            self.assertNotEqual(self.run_installer(home).returncode, 0)
            self.assertEqual(self.run_installer(home, "--force").returncode, 0)

    def test_cursor_installs_its_canonical_dependency_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "home"
            result = self.run_installer(home, "--cursor")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(
                (home / ".agents" / "skills" / NAME / "SKILL.md").is_file()
            )
            self.assertTrue(
                (home / ".cursor" / "commands" / f"{NAME}.md").is_file()
            )
            self.assertFalse((home / ".copilot").exists())
            self.assertFalse((home / ".claude").exists())
            self.assertFalse((home / ".gemini").exists())
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_install_skill -v`

Expected: `ERROR` because `scripts/install_skill.sh` does not exist.

- [ ] **Step 3: Implement the installer**

Create `scripts/install_skill.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="repo-name-conventions"
force=false
selected=false
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
    --agents) agents=true ;;
    --copilot) copilot=true ;;
    --claude) claude=true ;;
    --cursor) cursor=true ;;
    --gemini) gemini=true ;;
    --force) force=true ;;
    *) usage; exit 2 ;;
  esac
  selected=true
  shift
done

if ! "$selected"; then
  agents=true
  copilot=true
  claude=true
  cursor=true
  gemini=true
fi

if "$cursor" || "$gemini"; then
  agents=true
fi

copy_tree() {
  local destination="$1"
  if [[ -e "$destination" && "$force" != true ]]; then
    echo "Refusing to overwrite $destination; pass --force." >&2
    exit 1
  fi
  rm -rf "$destination"
  mkdir -p "$destination"
  for source in "$ROOT"/.[!.]* "$ROOT"/*; do
    [[ -e "$source" ]] || continue
    [[ "$(basename "$source")" == ".git" ]] && continue
    cp -R "$source" "$destination/"
  done
}

copy_file() {
  local source="$1" destination="$2"
  [[ -f "$source" ]] || { echo "Missing source: $source" >&2; exit 1; }
  if [[ -e "$destination" && "$force" != true ]]; then
    echo "Refusing to overwrite $destination; pass --force." >&2
    exit 1
  fi
  mkdir -p "$(dirname "$destination")"
  cp "$source" "$destination"
}
```

Finish the script by calling `copy_tree` for enabled `agents`, `copilot`, and
`claude` destinations. Generate the Cursor command with:

```markdown
Read and follow `~/.agents/skills/repo-name-conventions/SKILL.md`. Use its
bundled validator and suggester scripts instead of guessing repository names.
```

Generate the Gemini command with:

```toml
description = "Apply the repository name conventions skill."
prompt = "Read and follow ~/.agents/skills/repo-name-conventions/SKILL.md. Use its bundled validator and suggester scripts instead of guessing repository names."
```

Write generated commands through temporary files in `mktemp` and `copy_file`,
then remove the temporary files with a shell `trap`.

- [ ] **Step 4: Run focused tests**

Run: `python3 -m unittest tests.test_install_skill -v`

Expected: `OK`.

- [ ] **Step 5: Commit**

```bash
git add scripts/install_skill.sh tests/test_install_skill.py
git commit -m "feat: install repository naming skill"
```

### Task 2: Document Global Installation

**Files:**
- Modify: `README.md`
- Modify: `tests/test_readme.py`

**Interfaces:**
- Documents the Task 1 CLI and `/repo-name-conventions` host command name.

- [ ] **Step 1: Write the failing README test**

Add `"## Install as a global skill"` to `REQUIRED_SECTIONS` in
`tests/test_readme.py`.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_readme.TestReadme.test_required_sections_present -v`

Expected: `FAIL` because the required heading is absent.

- [ ] **Step 3: Document the installer**

Add this section before `## Validating and suggesting names`:

```markdown
## Install as a global skill

Install for every supported host:

    bash scripts/install_skill.sh

Use `/repo-name-conventions` in GitHub Copilot CLI, Claude Code, Cursor, and
Gemini CLI. Target one host with `--copilot`, `--claude`, `--cursor`, or
`--gemini`; `--cursor` and `--gemini` also install the shared generic Agent
Skill they require. Existing destinations are protected unless `--force` is
given.

Generic Agent Skills-compatible tools can load the installed package from
`~/.agents/skills/repo-name-conventions`; their command syntax is host-specific.
```

- [ ] **Step 4: Run all repository tests**

Run: `python3 -m unittest discover -s tests -v`

Expected: `OK`.

- [ ] **Step 5: Commit**

```bash
git add README.md tests/test_readme.py
git commit -m "docs: document global skill installation"
```

## Plan Self-Review

- Spec coverage: Task 1 implements every required destination, default and
  selected-host behavior, dependency installation, overwrite safety, and
  isolated-home validation. Task 2 documents all host behavior.
- Placeholder scan: no deferred implementation markers are present.
- Interface consistency: all command names, flags, and target paths are
  identical across the tasks and global constraints.
