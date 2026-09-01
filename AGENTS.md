# Repository Naming Conventions

When naming, renaming, or scaffolding a Git repository, follow the
convention in `reference/conventions.md`.

Core pattern (always required):

    <purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]

Full pattern (adds optional org/client prefixes and env/region/lifecycle
suffixes):

    [<org>-][<scope>-][<client>-]<purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>][-<env>][-<region>][-<lifecycle>]

All lowercase, ASCII, hyphen-separated segments, `_` before the project
name, `.` for sub-modules. Omit segments that don't apply.

Before proposing a repository name, validate it:

    python3 scripts/validate_repo_name.py <candidate-name>

Or build one from parts:

    python3 scripts/suggest_repo_name.py --purpose <p> --platform <pl> --repo-type <rt> --language <l> --name <project-name>

For the full controlled vocabulary (purpose, platform, repo-type,
language, enterprise and freelance extensions) and worked examples, read
`reference/conventions.md`.
