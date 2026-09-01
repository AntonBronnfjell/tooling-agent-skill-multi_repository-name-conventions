# Repository Name Conventions

A comprehensive Git repository naming convention, packaged as a skill
that Claude Code, Cursor, GitHub Copilot, Gemini CLI, and any other
`AGENTS.md`-reading tool (Codex, Grok, etc.) can all load — plus scripts
to validate and generate compliant names, and hooks that enforce the
convention at repo-creation time.

## What this is

Most naming conventions live in someone's head, a wiki page nobody reads,
or a Slack thread from two years ago. This repo turns one into something
executable: a machine-checkable pattern, a script that tells you exactly
why a candidate name fails, and hooks that stop a bad name before the
repo even exists — while staying readable enough that a human can also
just read `reference/conventions.md` and follow it by hand.

## Why repository naming conventions matter

- **Discoverability.** `acme-fin-payments-service-go-microservice-go_ledger-tier1`
  tells you the owning domain, the criticality, the language, and the
  shape of the thing before you've opened it. A hundred repos named after
  inside jokes do not.
- **Automation.** CODEOWNERS routing, branch-protection tiers, security
  scanning policy, and cost allocation can all be driven mechanically off
  a structured name (`every *-tier1 repo needs two reviewers`) instead of
  a spreadsheet someone forgets to update.
- **Onboarding cost.** A new engineer (or a new AI agent) can guess what
  a repo does, and what convention a new one should follow, without
  reading a README first.
- **Grep-ability at scale.** Once you have dozens or hundreds of repos —
  which happens fast with AI-agent tooling (skills, MCP servers, hooks,
  commands are all small, numerous, and fast-moving) — an inconsistent
  namespace stops being a style nitpick and starts being an actual cost.

## The pattern, at a glance

Core (always required):

    <purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]

Full (adds optional enterprise/freelance/lifecycle segments):

    [<org>-][<scope>-][<client>-]<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>][-<env>][-<region>][-<lifecycle>]

All lowercase, ASCII only, hyphen-separated segments, `_` before the
project name, `.` for sub-modules, no placeholders for segments that
don't apply. The full controlled vocabulary for every segment — including
a dedicated section for AI agent skills, MCP servers, hooks, commands,
and agent definitions — lives in [`reference/conventions.md`](reference/conventions.md).

This repo's own name, `tooling-agent-skill-multi_repository-name-conventions`,
follows the multi-agent-skill sub-pattern from that guide: `tooling`
(purpose) + `agent` (platform-agnostic, because it targets 5+ hosts) +
`skill` (repo-type) + `multi` (language, because it ships more than one
language of content) + the project name.

## Quick start

**Claude Code** — this repo ships `SKILL.md`; Claude Code picks it up
automatically as a project skill.

**Cursor** — `.cursor/rules/repo-name-conventions.mdc` is picked up as a
project rule automatically.

**GitHub Copilot** — `.github/copilot-instructions.md` is read
automatically as repo-level custom instructions.

**Gemini CLI** — `GEMINI.md` is read automatically as a context file.

**Any other agent (Grok, Codex, and generic `AGENTS.md` readers)** —
`AGENTS.md` follows the emerging cross-tool `agents.md` convention.

## Validating and suggesting names

```
python3 scripts/validate_repo_name.py <candidate-name>
python3 scripts/validate_repo_name.py <candidate-name> --strict
python3 scripts/suggest_repo_name.py --purpose tooling --platform agent --repo-type skill --language markdown --name invoice-parser
python3 scripts/suggest_repo_name.py   # interactive prompts
```

`validate_repo_name.py` always hard-fails on structural problems (wrong
separators, uppercase, a missing required segment). An unrecognized but
well-formed keyword (a brand-new framework, say) is only a warning by
default, since the vocabulary in `reference/vocabulary.json` can never be
fully exhaustive — pass `--strict` when the check needs to be
unambiguous, such as in CI.

## Enforcing the convention

**Local — block bad names before `gh repo create` runs:**

```
bash scripts/install_hooks.sh
```

This prints a `source .../hooks/gh-repo-create.sh` line to add to your
shell rc file. It does not edit your rc file for you. Once sourced, a
`gh repo create <bad-name>` call is blocked before it reaches GitHub.

**Claude Code — block bad names before the tool call happens:**

Merge `hooks/claude-code/settings.snippet.json` into your `.claude/settings.json`
(project or global). It registers a `PreToolUse` hook on the `Bash` tool
that inspects `gh repo create` / `git init` commands and denies the call
— with a reason fed back to the model — if the name doesn't comply.

**CI — catch drift after the fact:**

`.github/workflows/validate-repo-name.yml` runs on every push and fails
the build if the repo's own name (`github.event.repository.name`)
doesn't pass `--strict` validation.

## Extending the vocabulary

Every controlled-vocabulary table in `reference/conventions.md` has a
matching array (or nested object, for `platform` and `enterprise`) in
`reference/vocabulary.json`. To recognize a new keyword, add it to both
files — the JSON array so the scripts stop warning about it, and the
markdown table so a human reading the guide sees it too.

## FAQ

**Why is an unknown platform/language only a warning, not an error?**
Because the vocabulary can't keep up with every new framework. Structural
rules (casing, separators, segment count) are non-negotiable; the
specific words are a living list. Use `--strict` wherever unambiguous
compliance matters more than convenience (CI, for instance).

**Can I use this without any of the agent integrations?**
Yes — `reference/conventions.md` is a plain, human-readable guide, and
`scripts/validate_repo_name.py` / `scripts/suggest_repo_name.py` are
ordinary command-line tools with no dependency on any agent being present.

**What about GitLab, or enforcing this org-wide for repos other people create?**
Out of scope for now — this ships GitHub-only tooling for repos you
create yourself. The validator is host-agnostic, though, so a GitLab CI
job or a GitHub App for org-wide enforcement can reuse it unchanged.

## License

MIT — see [`LICENSE`](LICENSE).
