# Repository Name Conventions Skill Installer

## Goal

Package this repository as the globally installable `repo-name-conventions`
skill. It must be usable as `/repo-name-conventions` in hosts with a
file-backed command or skill mechanism and as an Agent Skill in generic
compatible hosts.

## Scope

- Add `scripts/install_skill.sh`.
- Copy the complete repository, excluding `.git`, into
  `~/.agents/skills/repo-name-conventions`.
- Copy the complete repository to native Agent Skill locations for GitHub
  Copilot CLI (`~/.copilot/skills/repo-name-conventions`) and Claude Code
  (`~/.claude/skills/repo-name-conventions`).
- Write a Cursor command at `~/.cursor/commands/repo-name-conventions.md`.
- Write a Gemini CLI command at `~/.gemini/commands/repo-name-conventions.toml`.
- Have command adapters direct the host to the canonical
  `~/.agents/skills/repo-name-conventions/SKILL.md`, including the repository
  validator and suggester scripts.
- Refuse to overwrite any selected destination without `--force`.
- Document installation and host behavior in `README.md`.

## Installer Behavior

`bash scripts/install_skill.sh` installs all supported user-scoped targets.
`--copilot`, `--claude`, `--cursor`, `--gemini`, and `--agents` select
individual targets. `--force` replaces only selected targets. The installer
uses Bash and standard macOS/Linux command-line utilities only.

Copilot CLI and Claude Code expose the installed skill as
`/repo-name-conventions`. Cursor and Gemini CLI expose native commands with
that same name. Generic Agent Skills-compatible hosts load the canonical
`~/.agents/skills/repo-name-conventions` package when their own discovery
mechanism supports that standard location; no universal slash syntax is
claimed for generic readers.

## Error Handling and Validation

The installer fails for unknown flags, no selected hosts, a missing source
file, or an existing selected destination without `--force`. It must leave
unselected destinations unchanged. A standard-library `unittest` suite runs
with an isolated `HOME` and verifies default installation, selected-host
installation, and overwrite protection without touching real user files.

## Non-goals

- New skill personas, prompts, or naming rules.
- Dependency management or package publishing.
- Project-scoped installation.
