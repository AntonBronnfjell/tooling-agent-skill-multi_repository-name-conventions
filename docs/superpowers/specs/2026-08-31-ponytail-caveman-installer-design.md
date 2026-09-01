# Ponytail and Caveman Skill Installer

## Goal

Ship `/ponytail` and `/caveman` for GitHub Copilot CLI, Claude Code, Cursor,
and Gemini CLI, plus automatic Ponytail and Caveman guidance for generic
`AGENTS.md` readers.

## Scope

- Add portable `SKILL.md` files for GitHub Copilot CLI and Claude Code.
- Add `scripts/install_skills.sh`.
- Install each skill into `~/.copilot/skills/<skill>` and
  `~/.claude/skills/<skill>`.
- Install Cursor Markdown command files and Gemini TOML command files.
- Install a generic `AGENTS.md` adapter only into an explicit project
  directory.
- Refuse to overwrite an existing destination unless `--force` is given.
- Document invocation and installation in the README.

## Installer behavior

The Bash installer defaults to the four user-scoped command hosts: Copilot
CLI, Claude Code, Cursor, and Gemini CLI. Individual targets are selected
with `--copilot`, `--claude`, `--cursor`, and `--gemini`. The Cursor commands
are copied to `~/.cursor/commands/`; the Gemini commands are copied to
`~/.gemini/commands/`. `--agents <directory>` adds a generic adapter to that
specific project. `--force` replaces only the selected target's generated
files. It copies from the repository's bundled files, preserving a usable
installation if the source checkout is later moved or deleted. Invalid flags,
a missing `--agents` directory, and missing source skill files fail clearly.

## Skill behavior

`ponytail` contains the supplied minimalism guidance and accepts optional
intensity arguments. `caveman` is a separate terse-communication skill.
Copilot CLI and Claude Code discover the Agent Skills as `/ponytail` and
`/caveman`; Cursor and Gemini CLI discover their native command files under
the same names.

Generic `AGENTS.md` readers load a compact adapter automatically. They do not
share a slash-command protocol, so the installer does not claim that slash
invocation works there.

## Error handling and validation

The installer exits nonzero for invalid options, missing bundled skills, an
invalid generic target, and pre-existing destinations without `--force`. A
focused test runs it with an isolated `HOME` and a temporary project, verifies
all adapters and overwrite protection, and does not modify real user files.

## Non-goals

- Dependency management or a package manager.
