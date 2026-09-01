---
name: repo-name-conventions
description: Comprehensive repository naming convention for Git repos — personal, freelance/agency, and tiered-enterprise contexts — including dedicated patterns for AI agent skills, MCP servers, hooks, commands, and other agent-tooling repos. Use this skill whenever the user is naming, renaming, or scaffolding a new Git repository; asking what to call a repo; choosing a purpose/platform/repo-type/language prefix; or asking to validate an existing repo name against a convention. Also trigger when the user is creating a skill, MCP server, hook, agent definition, or other AI-agent-tooling repo and needs the right platform/repo-type keywords (e.g. claude vs agent vs mcp, skill vs mcpserver vs hook).
---

# Repository Name Conventions

## Pattern

Core (always required):

    <purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]

Full (enterprise/freelance/lifecycle extensions):

    [<org>-][<scope>-][<client>-]<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>][-<env>][-<region>][-<lifecycle>]

Rules: all lowercase, ASCII only; segments separated by `-`; project name
separated from the technical prefix by `_`; sub-modules use `.`; omit
segments that don't apply rather than inserting placeholders; aim for
≤64 characters, hard-cap at 100.

For the full guide (every segment's controlled vocabulary, AI/agent repo
shapes, enterprise/freelance extensions, examples, anti-patterns), read
`reference/conventions.md`.

## When naming an AI-agent-tooling repo

| Repo shape | repo-type | platform |
|---|---|---|
| Instructions + optional scripts loaded into an agent's context | `skill` | the agent, or `agent` if it targets 2+ hosts |
| A server exposing tools over MCP to any compliant client | `mcpserver` | `mcp` |
| A script another system triggers on an event | `hook` | the triggering system |
| A reusable prompt or slash command | `command` / `prompt` | the agent, or `agent` |
| The agent itself — persona, tool wiring, orchestration | `agentdef` | the agent, or `agent` |

Full detail: `reference/conventions.md` § AI & Agent Repositories.

## Validating or suggesting a name

Run the bundled scripts rather than eyeballing the tables:

    python3 scripts/validate_repo_name.py <candidate-name>            # structural + vocab check
    python3 scripts/validate_repo_name.py <candidate-name> --strict   # unknown vocab = error
    python3 scripts/suggest_repo_name.py --purpose ... --platform ... --repo-type ... --language ... --name ...
    python3 scripts/suggest_repo_name.py                              # interactive prompts

`scripts/validate_repo_name.py` treats structural violations (wrong
separators, uppercase, missing segment) as hard errors always, but an
unrecognized-but-well-formed keyword only as a warning by default — the
vocabulary can never be fully exhaustive. Use `--strict` when the check
needs to be unambiguous (e.g. in CI).

## Enforcing this automatically

See `README.md` for installing the `gh repo create` guard hook, the
Claude Code `PreToolUse` hook, and the CI check.
