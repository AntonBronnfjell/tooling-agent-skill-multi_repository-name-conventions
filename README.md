<div align="center">

# Repository Name Conventions

<p>
  <strong>A Git repository naming convention you can actually enforce.</strong><br>
  Packaged as an agent skill, with scripts that validate and generate names and hooks that block bad names before the repo exists.
</p>

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://github.com/AntonBronnfjell/tooling-agent-skill-multi_repository-name-conventions/actions/workflows/validate-repo-name.yml"><img alt="Validate repository name" src="https://github.com/AntonBronnfjell/tooling-agent-skill-multi_repository-name-conventions/actions/workflows/validate-repo-name.yml/badge.svg"></a>
  <img alt="Python 3" src="https://img.shields.io/badge/python-3.x-3776AB.svg?logo=python&logoColor=white">
  <img alt="Dependencies: none" src="https://img.shields.io/badge/dependencies-none-brightgreen.svg">
</p>

<p>
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-supported-D97757.svg">
  <img alt="Cursor" src="https://img.shields.io/badge/Cursor-supported-000000.svg">
  <img alt="GitHub Copilot" src="https://img.shields.io/badge/GitHub_Copilot-supported-181717.svg?logo=githubcopilot&logoColor=white">
  <img alt="Gemini CLI" src="https://img.shields.io/badge/Gemini_CLI-supported-4285F4.svg?logo=googlegemini&logoColor=white">
  <img alt="AGENTS.md" src="https://img.shields.io/badge/AGENTS.md-supported-6E40C9.svg">
</p>

<p>
  <a href="#quick-start">Quick start</a> ·
  <a href="#the-pattern-at-a-glance">The pattern</a> ·
  <a href="#validating-and-suggesting-names">Validate &amp; suggest</a> ·
  <a href="#enforcing-the-convention">Enforce</a> ·
  <a href="reference/conventions.md">Full guide</a> ·
  <a href="#faq">FAQ</a>
</p>

</div>

<br>

## What this is

Most naming conventions live in someone's head, a wiki page nobody reads,
or a Slack thread from two years ago. This repo turns one into something
executable: a machine-checkable pattern, a script that tells you exactly
why a candidate name fails, and hooks that stop a bad name before the
repo even exists — while staying readable enough that a human can also
just read [`reference/conventions.md`](reference/conventions.md) and follow it by hand.

It ships as a skill that **Claude Code, Cursor, GitHub Copilot, Gemini CLI**,
and any other `AGENTS.md`-reading tool (Codex, Grok, etc.) can load.

<table>
  <tr>
    <th align="left">Piece</th>
    <th align="left">What it gives you</th>
  </tr>
  <tr>
    <td><a href="reference/conventions.md"><code>reference/conventions.md</code></a></td>
    <td>The full human-readable guide: every segment, its vocabulary, examples, and anti-patterns.</td>
  </tr>
  <tr>
    <td><a href="reference/vocabulary.json"><code>reference/vocabulary.json</code></a></td>
    <td>The same vocabulary in machine-readable form, used by the scripts.</td>
  </tr>
  <tr>
    <td><a href="scripts/"><code>scripts/</code></a></td>
    <td>A validator, a name builder, and installers for the skill and hooks.</td>
  </tr>
  <tr>
    <td><a href="hooks/"><code>hooks/</code></a></td>
    <td>A <code>gh repo create</code> shell guard and a Claude Code <code>PreToolUse</code> guard.</td>
  </tr>
  <tr>
    <td><a href="SKILL.md"><code>SKILL.md</code></a>, <a href="AGENTS.md"><code>AGENTS.md</code></a>, <a href="GEMINI.md"><code>GEMINI.md</code></a>, …</td>
    <td>Per-host entry points so each agent picks the convention up natively.</td>
  </tr>
</table>

## Why repository naming conventions matter

<dl>
  <dt>🔎 Discoverability</dt>
  <dd>
    <code>acme-fin-payments-service-go-microservice-go_ledger-tier1</code>
    tells you the owning domain, the criticality, the language, and the
    shape of the thing before you've opened it. A hundred repos named after
    inside jokes do not.
  </dd>
  <dt>⚙️ Automation</dt>
  <dd>
    CODEOWNERS routing, branch-protection tiers, security scanning policy,
    and cost allocation can all be driven mechanically off a structured name
    (<em>every <code>*-tier1</code> repo needs two reviewers</em>) instead of
    a spreadsheet someone forgets to update.
  </dd>
  <dt>🧭 Onboarding cost</dt>
  <dd>
    A new engineer (or a new AI agent) can guess what a repo does, and what
    convention a new one should follow, without reading a README first.
  </dd>
  <dt>📈 Grep-ability at scale</dt>
  <dd>
    Once you have dozens or hundreds of repos — which happens fast with
    AI-agent tooling (skills, MCP servers, hooks, commands are all small,
    numerous, and fast-moving) — an inconsistent namespace stops being a
    style nitpick and starts being an actual cost.
  </dd>
</dl>

## The pattern, at a glance

**Core** (always required):

```text
<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]
```

**Full** (adds optional enterprise/freelance/lifecycle segments):

```text
[<org>-][<scope>-][<client>-]<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>][-<env>][-<region>][-<lifecycle>]
```

| Rule | Detail |
|---|---|
| Case | All lowercase, ASCII only |
| <kbd>-</kbd> hyphen | Separates segments |
| <kbd>_</kbd> underscore | Separates the technical prefix from the project name — used nowhere else |
| <kbd>.</kbd> dot | Separates sub-modules |
| Missing segments | Omit them; no placeholders like `none` or `xx` |
| Length | Aim for ≤ 64 characters; hard cap at 100 |

The full controlled vocabulary for every segment — including a dedicated
section for AI agent skills, MCP servers, hooks, commands, and agent
definitions — lives in [`reference/conventions.md`](reference/conventions.md).

<details>
<summary><strong>Example names</strong></summary>
<br>

| What it is | Name |
|---|---|
| Personal Next.js portfolio | `project-nextjs-web-typescript_portfolio` |
| MCP server for GitHub issues | `tooling-mcp-mcpserver-typescript_github-issues` |
| Claude Code `PreToolUse` hook | `tooling-claude-hook-python_pretooluse-audit` |
| Multi-host agent skill | `tooling-agent-skill-markdown_invoice-parser` |
| Client storefront API | `client-acme-project-nodejs-api-typescript_storefront-api` |
| Tier-1 enterprise service, EU | `acme-fin-payments-service-go-microservice-go_ledger-tier1-eu` |

More in [`reference/conventions.md` § Examples](reference/conventions.md#examples).

</details>

<details>
<summary><strong>How this repo's own name breaks down</strong></summary>
<br>

`tooling-agent-skill-multi_repository-name-conventions` follows the
multi-agent-skill sub-pattern from the guide:

| Segment | Value | Why |
|---|---|---|
| purpose | `tooling` | Developer / agent tooling |
| platform | `agent` | Platform-agnostic — it targets 5+ hosts |
| repo-type | `skill` | Instructions loaded into an agent's context |
| language | `multi` | Ships Markdown, Python, and Bash |
| project-name | `repository-name-conventions` | What it is |

</details>

## Quick start

> [!IMPORTANT]
> Claude Code discovers skills at `.claude/skills/<name>/SKILL.md`
> (project-scoped) or `~/.claude/skills/<name>/SKILL.md` (personal) — a
> root-level `SKILL.md` in an unrelated working directory is not auto-loaded.
> The fastest path is the [global installer](#install-as-a-global-skill).

<table>
  <tr>
    <th align="left">Host</th>
    <th align="left">How it picks the convention up</th>
  </tr>
  <tr>
    <td><strong>Claude Code</strong></td>
    <td>
      Clone or symlink this repo to <code>~/.claude/skills/repo-name-conventions/</code>
      (or the project-scoped path above). Once installed there,
      <code>SKILL.md</code>'s relative references (<code>reference/conventions.md</code>,
      <code>scripts/validate_repo_name.py</code>) resolve against the skill's own
      directory automatically.
    </td>
  </tr>
  <tr>
    <td><strong>Cursor</strong></td>
    <td><code>.cursor/rules/repo-name-conventions.mdc</code> is picked up as a project rule automatically.</td>
  </tr>
  <tr>
    <td><strong>GitHub Copilot</strong></td>
    <td><code>.github/copilot-instructions.md</code> is read automatically as repo-level custom instructions.</td>
  </tr>
  <tr>
    <td><strong>Gemini CLI</strong></td>
    <td><code>GEMINI.md</code> is read automatically as a context file.</td>
  </tr>
  <tr>
    <td><strong>Any other agent</strong><br><sub>Grok, Codex, generic <code>AGENTS.md</code> readers</sub></td>
    <td><code>AGENTS.md</code> follows the emerging cross-tool <code>agents.md</code> convention.</td>
  </tr>
</table>

## Install as a global skill

Install for every supported host:

```bash
bash scripts/install_skill.sh
```

Then use <kbd>/repo-name-conventions</kbd> in GitHub Copilot CLI, Claude Code,
Cursor, and Gemini CLI.

| Flag | Effect |
|---|---|
| `--copilot` | Install for GitHub Copilot CLI only |
| `--claude` | Install for Claude Code only |
| `--cursor` | Install for Cursor (plus the shared generic Agent Skill it requires) |
| `--gemini` | Install for Gemini CLI (plus the shared generic Agent Skill it requires) |
| `--force` | Overwrite existing destinations |

> [!NOTE]
> Existing destinations are protected unless `--force` is given.
> Generic Agent Skills-compatible tools can load the installed package from
> `~/.agents/skills/repo-name-conventions`; their command syntax is host-specific.

## Validating and suggesting names

```bash
python3 scripts/validate_repo_name.py <candidate-name>
python3 scripts/validate_repo_name.py <candidate-name> --strict
python3 scripts/suggest_repo_name.py --purpose tooling --platform agent --repo-type skill --language markdown --name invoice-parser
python3 scripts/suggest_repo_name.py   # interactive prompts
```

<details>
<summary><strong>Sample output</strong></summary>
<br>

```console
$ python3 scripts/validate_repo_name.py tooling-agent-skill-multi_invoice-parser
VALID: tooling-agent-skill-multi_invoice-parser

$ python3 scripts/validate_repo_name.py tooling-zzz-skill-multi_invoice-parser
WARNING: platform segment 'zzz' is not in the known vocabulary
VALID: tooling-zzz-skill-multi_invoice-parser

$ python3 scripts/validate_repo_name.py MyRepo
ERROR: does not match the repository naming pattern (...)
INVALID: MyRepo
```

</details>

`validate_repo_name.py` always hard-fails on structural problems (wrong
separators, uppercase, a missing required segment). An unrecognized but
well-formed keyword (a brand-new framework, say) is only a warning by
default, since the vocabulary in `reference/vocabulary.json` can never be
fully exhaustive — pass `--strict` when the check needs to be
unambiguous, such as in CI.

> [!TIP]
> These commands assume your current directory is this repo (or wherever
> you installed it — see [Quick start](#quick-start)). From a different
> project, use an absolute path to the script instead, e.g.
> `python3 ~/.claude/skills/repo-name-conventions/scripts/validate_repo_name.py <candidate-name>`.

## Enforcing the convention

Three layers, from earliest to latest:

<table>
  <tr>
    <th align="left">Layer</th>
    <th align="left">Catches a bad name…</th>
    <th align="left">Setup</th>
  </tr>
  <tr>
    <td>🐚 <strong>Shell</strong></td>
    <td>before <code>gh repo create</code> reaches GitHub</td>
    <td><code>bash scripts/install_hooks.sh</code></td>
  </tr>
  <tr>
    <td>🤖 <strong>Claude Code</strong></td>
    <td>before the agent's tool call runs</td>
    <td>merge <code>hooks/claude-code/settings.snippet.json</code></td>
  </tr>
  <tr>
    <td>✅ <strong>CI</strong></td>
    <td>on every push, after the fact</td>
    <td><code>.github/workflows/validate-repo-name.yml</code></td>
  </tr>
</table>

### Local — block bad names before `gh repo create` runs

```bash
bash scripts/install_hooks.sh
```

This prints a `source .../hooks/gh-repo-create.sh` line to add to your
shell rc file. It does not edit your rc file for you. Once sourced, a
`gh repo create <bad-name>` call is blocked before it reaches GitHub.

### Claude Code — block bad names before the tool call happens

Merge [`hooks/claude-code/settings.snippet.json`](hooks/claude-code/settings.snippet.json)
into your `.claude/settings.json` (project or global). It registers a
`PreToolUse` hook on the `Bash` tool that inspects `gh repo create` /
`git init` commands and denies the call — with a reason fed back to the
model — if the name doesn't comply.

> [!WARNING]
> `${CLAUDE_PROJECT_DIR}` in that snippet resolves to whatever project is
> currently open — correct only if this repo itself is the open project.
> For global use (`~/.claude/settings.json`, so the guard applies
> everywhere), replace it with the absolute path to wherever you installed
> this repo/skill, e.g.
> `~/.claude/skills/repo-name-conventions/hooks/claude-code/pretooluse_repo_name_guard.py`.

### CI — catch drift after the fact

[`.github/workflows/validate-repo-name.yml`](.github/workflows/validate-repo-name.yml)
runs on every push and fails the build if the repo's own name
(`github.event.repository.name`) doesn't pass `--strict` validation.

## Extending the vocabulary

Every controlled-vocabulary table in `reference/conventions.md` has a
matching array (or nested object, for `platform` and `enterprise`) in
`reference/vocabulary.json`. To recognize a new keyword, add it to
**both** files — the JSON array so the scripts stop warning about it, and
the markdown table so a human reading the guide sees it too.

<details>
<summary><strong>What the validator does and doesn't check</strong></summary>
<br>

Automated vocabulary checking covers the four core segments only —
purpose, platform, repo-type, language. Enterprise, freelance, and
project-name-suffix segments are structurally permitted by the naming
pattern but not vocabulary-checked, because their position relative to
the free-form project name is genuinely ambiguous to parse without
already knowing the vocabulary (see `reference/conventions.md`'s own
validation regexes, which have the same limitation by design).

A few of the guide's own worked examples (some Terraform/Nix/monorepo
names) use keywords that aren't yet in `reference/vocabulary.json`'s
tables — that's a known gap between the guide's prose and its own
tables, not a validator bug, and `--strict` enforces the tables exactly
as written, not the examples.

</details>

## FAQ

<details>
<summary><strong>Why is an unknown platform/language only a warning, not an error?</strong></summary>
<br>

Because the vocabulary can't keep up with every new framework. Structural
rules (casing, separators, segment count) are non-negotiable; the
specific words are a living list. Use `--strict` wherever unambiguous
compliance matters more than convenience (CI, for instance).

</details>

<details>
<summary><strong>Can I use this without any of the agent integrations?</strong></summary>
<br>

Yes — `reference/conventions.md` is a plain, human-readable guide, and
`scripts/validate_repo_name.py` / `scripts/suggest_repo_name.py` are
ordinary command-line tools with no dependency on any agent being present.

</details>

<details>
<summary><strong>What about GitLab, or enforcing this org-wide for repos other people create?</strong></summary>
<br>

Out of scope for now — this ships GitHub-only tooling for repos you
create yourself. The validator is host-agnostic, though, so a GitLab CI
job or a GitHub App for org-wide enforcement can reuse it unchanged.

</details>

## License

MIT — see [`LICENSE`](LICENSE).

<p align="right"><a href="#repository-name-conventions">↑ Back to top</a></p>
