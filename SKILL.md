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
`reference/conventions.md`. The machine-readable vocabulary the scripts
check against is `reference/vocabulary.json`.

## Workflow

1. **Work out what the repo is.** From the request, the working
   directory (`package.json`, `pyproject.toml`, `go.mod`, `SKILL.md`,
   `Dockerfile`, …), and the existing name if renaming, determine: why
   it exists (purpose), what it runs on (platform), what kind of
   artifact it is (repo-type), its primary language, and a short
   project name. Ask only about what you genuinely can't infer — usually
   whether it's personal, client, or enterprise work.
2. **Pick each core segment** using the quick guide below; look up
   anything unfamiliar in `reference/conventions.md` rather than
   inventing a keyword.
3. **Add extensions only when they apply.** Org/business-unit/team
   prefixes for enterprise repos, `client-<slug>` for client work,
   `-tier1`/`-prod`/`-eu`/`-pii`/`-deprecated` style suffixes only when
   they carry real meaning. Personal repos normally use the core pattern
   alone.
4. **Build and validate with the scripts** (next section) — never hand
   a name to the user, or to `gh repo create`, without a passing
   validation run.
5. **Present the result**: the name, a one-line breakdown of each
   segment, and any validator warnings. Offer one alternative only when
   a segment is a genuine judgment call (e.g. `markdown` vs `multi`).

## Quick segment guide

- **purpose** — `project` (a thing you build), `product` (you sell it),
  `tooling` (dev/agent tooling), `service`, `config`, `docs`, `guide` /
  `example` (exists to teach), `template` / `starter` (a scaffold),
  `sandbox` / `poc` / `spike` (throwaway), `research`, `fork`, `archive`.
- **platform** — the framework, runtime, cloud, or host that defines
  the repo: `nextjs`, `nodejs`, `aws`, `flutter`, `github`, `claude`…
  Use `agent` for agent tooling that targets 2+ AI hosts, `mcp` for MCP
  servers/clients.
- **repo-type** — the shape of the deliverable: `web`, `api`, `service`,
  `cli`, `lib`, `infra`, `pipeline`, `plugin`, `skill`, `mcpserver`,
  `hook`, `monorepo`…
- **language** — the primary language: `typescript`, `python`, `go`,
  `hcl`, `yaml`… Use `markdown` for prose-only repos and `multi` when
  several languages carry real weight.
- **project-name** — kebab-case, descriptive, ≤30 characters; don't
  repeat words already present in the prefix.

## When naming an AI-agent-tooling repo

| Repo shape | repo-type | platform |
|---|---|---|
| Instructions + optional scripts loaded into an agent's context | `skill` | the agent, or `agent` if it targets 2+ hosts |
| A server exposing tools over MCP to any compliant client | `mcpserver` | `mcp` |
| A script another system triggers on an event | `hook` | the triggering system |
| A reusable prompt or slash command | `command` / `prompt` | the agent, or `agent` |
| The agent itself — persona, tool wiring, orchestration | `agentdef` | the agent, or `agent` |

Never stack host names (`tooling-claude-cursor-skill-…`); use `agent`
and list supported hosts in the repo description and topics. Per-host
adapters inside a multi-agent repo use the module segment
(`…_invoice-parser.cursor`). Full detail:
`reference/conventions.md` § AI & Agent Repositories.

## Validating or suggesting a name

Run the bundled scripts rather than eyeballing the tables:

    python3 scripts/validate_repo_name.py <candidate-name>            # structural + vocab check
    python3 scripts/validate_repo_name.py <candidate-name> --strict   # unknown vocab = error
    python3 scripts/suggest_repo_name.py --purpose ... --platform ... --repo-type ... --language ... --name ...
    python3 scripts/suggest_repo_name.py                              # interactive prompts

`suggest_repo_name.py` also accepts `--modules` (dot-separated) and
`--trailing` (hyphen-separated suffixes), and validates what it builds.

These paths are relative to this skill's directory. When the user's
working directory is a different project, call the scripts by absolute
path (e.g. `~/.claude/skills/repo-name-conventions/scripts/validate_repo_name.py`).

`scripts/validate_repo_name.py` treats structural violations (wrong
separators, uppercase, missing segment) as hard errors always, but an
unrecognized-but-well-formed keyword only as a warning by default — the
vocabulary can never be fully exhaustive. Use `--strict` when the check
needs to be unambiguous (e.g. in CI). If a warning names a keyword,
prefer a known synonym from `reference/vocabulary.json`; keep the
unknown word only when no listed keyword fits, and say so.

## Examples

| Request | Name |
|---|---|
| Personal Next.js portfolio site | `project-nextjs-web-typescript_portfolio` |
| MCP server for GitHub issues, TypeScript | `tooling-mcp-mcpserver-typescript_github-issues` |
| Claude Code PreToolUse hook in Python | `tooling-claude-hook-python_pretooluse-audit` |
| Skill for Claude, Cursor and Copilot with scripts | `tooling-agent-skill-multi_invoice-parser` |
| Client storefront API for Acme | `client-acme-project-nodejs-api-typescript_storefront-api` |
| Tier-1 payments ledger at Acme, EU | `acme-fin-payments-service-go-microservice-go_ledger-tier1-eu` |

## Common mistakes

- Underscores between segments (`project_react_web`) — `_` marks only
  the project-name boundary.
- Status or version in the name (`-v2`, `-new`, `-final`) — use tags and
  the `<lifecycle>` suffix instead.
- Placeholder segments (`-none-`, `-xx-`) — omit the segment.
- Customer names in client repos under NDA — use an alias such as
  `client-c14`.

## Renaming an existing repo

Validate the current name first and explain what fails. After proposing
a new name, remind the user that GitHub/GitLab keep a redirect from the
old name, but local remotes (`git remote set-url`), CI config, and
anything else pinned to the old URL still need updating. Don't rename
the remote repo yourself unless asked.

## Enforcing this automatically

See `README.md` for installing the `gh repo create` guard hook, the
Claude Code `PreToolUse` hook, and the CI check.
