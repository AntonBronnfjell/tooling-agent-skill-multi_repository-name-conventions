# Repository naming conventions

When this repository (or a new one) needs a name, follow the convention
in `reference/conventions.md`:

    <purpose>-<platform>-<repo-type>-<language>_<project-name>[.<project-module>]

All lowercase, ASCII, hyphen-separated segments, `_` before the project
name, `.` for sub-modules. Validate a candidate name with:

    python3 scripts/validate_repo_name.py <candidate-name>

Or build one from parts with `python3 scripts/suggest_repo_name.py --help`.
