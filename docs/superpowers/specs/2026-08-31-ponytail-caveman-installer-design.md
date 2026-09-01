# Ponytail and Caveman Skill Installer

## Goal

Ship the Ponytail and Caveman guidance for every host this repository supports:
GitHub Copilot CLI, Claude Code, Cursor, Gemini CLI, and generic
`AGENTS.md` readers.

## Scope

- Add portable `SKILL.md` files for the native slash-command hosts.
- Add `scripts/install_skills.sh`.
- Install each skill into `~/.copilot/skills/<skill>` and
  `~/.claude/skills/<skill>`.
- Install automatic instruction adapters for Cursor and Gemini CLI.
- Install a generic `AGENTS.md` adapter only into an explicit project
  directory.
- Refuse to overwrite an existing destination unless `--force` is given.
- Document invocation and installation in the README.

## Installer behavior

The Bash installer defaults to the four user-scoped hosts: Copilot CLI, Claude
Code, Cursor, and Gemini CLI. Individual targets are selected with
`--copilot`, `--claude`, `--cursor`, and `--gemini`. `--agents <directory>`
adds a generic adapter to that specific project. `--force` replaces only the
selected target's generated files. It copies from the repository's bundled
files, preserving a usable installation if the source checkout is later moved
or deleted. Invalid flags, a missing `--agents` directory, and missing source
skill files fail clearly.

## Skill behavior

`ponytail` contains the supplied minimalism guidance and accepts optional
intensity arguments. `caveman` is a separate terse-communication skill. Both
use standard Agent Skills metadata so Copilot CLI and Claude Code discover
them as `/ponytail` and `/caveman`.

Cursor, Gemini CLI, and generic `AGENTS.md` readers load compact adapters
automatically. These hosts do not share a slash-command protocol, so the
installer does not claim that slash invocation works there.

## Error handling and validation

The installer exits nonzero for invalid options, missing bundled skills, an
invalid generic target, and pre-existing destinations without `--force`. A
focused test runs it with an isolated `HOME` and a temporary project, verifies
all adapters and overwrite protection, and does not modify real user files.

## Non-goals

- Project-scoped installation.
- Dependency management or a package manager.
