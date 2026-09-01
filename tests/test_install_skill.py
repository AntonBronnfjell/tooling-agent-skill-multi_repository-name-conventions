import os
import shutil
import subprocess
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTALLER = ROOT / "scripts" / "install_skill.sh"
NAME = "repo-name-conventions"
WORKSPACES = ROOT / ".test-workspaces"
SKILL_SOURCE = ROOT / "SKILL.md"
CURSOR_COMMAND = (
    "Read and follow `~/.agents/skills/repo-name-conventions/SKILL.md`. Use its\n"
    "bundled validator and suggester scripts instead of guessing repository names.\n"
)
GEMINI_COMMAND = (
    'description = "Apply the repository name conventions skill."\n'
    'prompt = "Read and follow ~/.agents/skills/repo-name-conventions/SKILL.md. Use its bundled validator and suggester scripts instead of guessing repository names."\n'
)


@contextmanager
def isolated_home():
    WORKSPACES.mkdir(exist_ok=True)
    home = WORKSPACES / f"install-skill-{uuid.uuid4().hex}" / "home"
    home.mkdir(parents=True, exist_ok=True)
    try:
        yield home
    finally:
        shutil.rmtree(home.parent, ignore_errors=True)


class TestInstallSkill(unittest.TestCase):
    def run_installer(self, home, *args):
        return subprocess.run(
            ["bash", str(INSTALLER), *args],
            cwd=ROOT,
            env={**os.environ, "HOME": str(home)},
            text=True,
            capture_output=True,
        )

    def run_copy_staged_tree(self, source, destination):
        return subprocess.run(
            [
                "bash",
                "-lc",
                'set -euo pipefail; '
                'INSTALLER="$1"; SOURCE="$2"; DESTINATION="$3"; '
                'set --; '
                'INSTALL_SKILL_SOURCE_ONLY=1 source "$INSTALLER"; '
                'copy_staged_tree "$SOURCE" "$DESTINATION"',
                "_",
                str(INSTALLER),
                str(source),
                str(destination),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

    def start_destination_racer(self, wait_for, destination, *, directory=False):
        script = """
from pathlib import Path
import sys
import time

wait_for = Path(sys.argv[1])
destination = Path(sys.argv[2])
mode = sys.argv[3]
deadline = time.time() + 10

while time.time() < deadline:
    if wait_for.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
        if mode == "directory":
            destination.mkdir(parents=True, exist_ok=True)
            (destination / "concurrent.txt").write_text("concurrent\\n")
        else:
            destination.write_text("concurrent\\n")
        raise SystemExit(0)
    time.sleep(0.01)

raise SystemExit(1)
"""
        return subprocess.Popen(
            [
                "python3",
                "-c",
                script,
                str(wait_for),
                str(destination),
                "directory" if directory else "file",
            ],
            cwd=ROOT,
            env=os.environ.copy(),
        )

    def test_default_install_and_overwrite_protection(self):
        with isolated_home() as home:
            result = self.run_installer(home)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed_paths = (
                home / ".agents" / "skills" / NAME / "SKILL.md",
                home / ".copilot" / "skills" / NAME / "SKILL.md",
                home / ".claude" / "skills" / NAME / "SKILL.md",
                home / ".cursor" / "commands" / f"{NAME}.md",
                home / ".gemini" / "commands" / f"{NAME}.toml",
            )
            for path in installed_paths:
                self.assertTrue(path.is_file(), path)

            self.assertEqual(
                list((home / ".agents" / "skills" / NAME).glob(".install-skill-staging*")),
                [],
            )
            self.assertFalse(
                (home / ".agents" / "skills" / NAME / ".test-workspaces").exists()
            )
            self.assertEqual(
                (home / ".cursor" / "commands" / f"{NAME}.md").read_text(),
                CURSOR_COMMAND,
            )
            self.assertEqual(
                (home / ".gemini" / "commands" / f"{NAME}.toml").read_text(),
                GEMINI_COMMAND,
            )

            second_result = self.run_installer(home)
            self.assertNotEqual(second_result.returncode, 0)

            gemini_command = home / ".gemini" / "commands" / f"{NAME}.toml"
            gemini_command.unlink()

            force_result = self.run_installer(home, "--force")
            self.assertEqual(force_result.returncode, 0, force_result.stderr)
            self.assertEqual(gemini_command.read_text(), GEMINI_COMMAND)

    def test_cursor_installs_its_canonical_dependency_only(self):
        with isolated_home() as home:
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

    def test_installed_agents_copy_can_install_copilot_without_git_metadata(self):
        with isolated_home() as home:
            agents_result = self.run_installer(home, "--agents")
            self.assertEqual(agents_result.returncode, 0, agents_result.stderr)

            installed_root = home / ".agents" / "skills" / NAME
            installed_installer = installed_root / "scripts" / "install_skill.sh"
            self.assertTrue(installed_installer.is_file())

            copilot_result = subprocess.run(
                ["bash", str(installed_installer), "--copilot"],
                cwd=installed_root,
                env={**os.environ, "HOME": str(home)},
                text=True,
                capture_output=True,
            )

            self.assertEqual(copilot_result.returncode, 0, copilot_result.stderr)
            self.assertEqual(
                (home / ".copilot" / "skills" / NAME / "SKILL.md").read_text(),
                SKILL_SOURCE.read_text(),
            )

    def test_installed_agents_force_is_a_successful_no_op(self):
        with isolated_home() as home:
            agents_result = self.run_installer(home, "--agents")
            self.assertEqual(agents_result.returncode, 0, agents_result.stderr)

            installed_root = home / ".agents" / "skills" / NAME
            installed_installer = installed_root / "scripts" / "install_skill.sh"
            installed_skill = installed_root / "SKILL.md"
            original_skill = installed_skill.read_text()

            forced_result = subprocess.run(
                ["bash", str(installed_installer), "--agents", "--force"],
                cwd=installed_root,
                env={**os.environ, "HOME": str(home)},
                text=True,
                capture_output=True,
            )

            self.assertEqual(forced_result.returncode, 0, forced_result.stderr)
            self.assertTrue(installed_skill.is_file())
            self.assertEqual(installed_skill.read_text(), original_skill)

    def test_installed_agents_copy_can_install_cursor_without_force(self):
        with isolated_home() as home:
            agents_result = self.run_installer(home, "--agents")
            self.assertEqual(agents_result.returncode, 0, agents_result.stderr)

            installed_root = home / ".agents" / "skills" / NAME
            installed_installer = installed_root / "scripts" / "install_skill.sh"
            installed_skill = installed_root / "SKILL.md"
            original_skill = installed_skill.read_text()

            cursor_result = subprocess.run(
                ["bash", str(installed_installer), "--cursor"],
                cwd=installed_root,
                env={**os.environ, "HOME": str(home)},
                text=True,
                capture_output=True,
            )

            self.assertEqual(cursor_result.returncode, 0, cursor_result.stderr)
            self.assertTrue(
                (home / ".cursor" / "commands" / f"{NAME}.md").is_file()
            )
            self.assertEqual(installed_skill.read_text(), original_skill)

    def test_concurrently_created_tree_destination_is_preserved_without_force(self):
        with isolated_home() as home:
            concurrent_destination = home / ".claude" / "skills" / NAME
            racer = self.start_destination_racer(
                home / ".agents" / "skills" / NAME / "SKILL.md",
                concurrent_destination,
                directory=True,
            )
            try:
                result = self.run_installer(home)
            finally:
                racer.wait(timeout=15)

            self.assertEqual(racer.returncode, 0)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Refusing to overwrite", result.stderr)
            self.assertTrue((home / ".agents" / "skills" / NAME / "SKILL.md").is_file())
            self.assertTrue((home / ".copilot" / "skills" / NAME / "SKILL.md").is_file())
            self.assertTrue(concurrent_destination.is_dir())
            self.assertEqual(
                (concurrent_destination / "concurrent.txt").read_text(),
                "concurrent\n",
            )
            self.assertFalse((concurrent_destination / "SKILL.md").exists())
            self.assertFalse((home / ".cursor").exists())
            self.assertFalse((home / ".gemini").exists())

    def test_concurrently_created_command_destination_is_preserved_without_force(self):
        with isolated_home() as home:
            concurrent_destination = home / ".gemini" / "commands" / f"{NAME}.toml"
            racer = self.start_destination_racer(
                home / ".cursor" / "commands" / f"{NAME}.md",
                concurrent_destination,
            )
            try:
                result = self.run_installer(home)
            finally:
                racer.wait(timeout=15)

            self.assertEqual(racer.returncode, 0)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Refusing to overwrite", result.stderr)
            self.assertEqual(concurrent_destination.read_text(), "concurrent\n")
            self.assertTrue(
                (home / ".cursor" / "commands" / f"{NAME}.md").is_file()
            )

    def test_existing_selected_destination_aborts_without_partial_install(self):
        with isolated_home() as home:
            existing = home / ".copilot" / "skills" / NAME / "SKILL.md"
            existing.parent.mkdir(parents=True, exist_ok=True)
            existing.write_text("already here\n")

            result = self.run_installer(home)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Refusing to overwrite", result.stderr)
            self.assertFalse((home / ".agents").exists())
            self.assertFalse((home / ".claude").exists())
            self.assertFalse((home / ".cursor").exists())
            self.assertFalse((home / ".gemini").exists())

    def test_force_replaces_existing_command_destinations_across_types(self):
        variants = ("file", "directory", "symlink")

        for variant in variants:
            with self.subTest(variant=variant), isolated_home() as home:
                cursor_command = home / ".cursor" / "commands" / f"{NAME}.md"
                cursor_command.parent.mkdir(parents=True, exist_ok=True)
                preserved_target = None

                if variant == "file":
                    cursor_command.write_text("old contents\n")
                elif variant == "directory":
                    cursor_command.mkdir()
                    (cursor_command / "stale.md").write_text("old contents\n")
                else:
                    preserved_target = home / "preserved-target.md"
                    preserved_target.write_text("keep me\n")
                    cursor_command.symlink_to(preserved_target)

                result = self.run_installer(home, "--cursor", "--force")

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(cursor_command.is_file())
                self.assertFalse(cursor_command.is_symlink())
                self.assertEqual(cursor_command.read_text(), CURSOR_COMMAND)
                self.assertTrue(
                    (home / ".agents" / "skills" / NAME / "SKILL.md").is_file()
                )
                if preserved_target is not None:
                    self.assertEqual(preserved_target.read_text(), "keep me\n")

    def test_dangling_symlink_destination_requires_force(self):
        with isolated_home() as home:
            cursor_command = home / ".cursor" / "commands" / f"{NAME}.md"
            cursor_command.parent.mkdir(parents=True, exist_ok=True)
            cursor_command.symlink_to(home / "missing-target.md")

            result = self.run_installer(home, "--cursor")

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Refusing to overwrite", result.stderr)
            self.assertTrue(cursor_command.is_symlink())
            self.assertFalse(cursor_command.exists())
            self.assertFalse((home / ".agents").exists())

            forced_result = self.run_installer(home, "--cursor", "--force")

            self.assertEqual(forced_result.returncode, 0, forced_result.stderr)
            self.assertTrue(cursor_command.is_file())
            self.assertFalse(cursor_command.is_symlink())
            self.assertEqual(cursor_command.read_text(), CURSOR_COMMAND)

    def test_copy_staged_tree_refuses_preexisting_entries_inside_claimed_destination(self):
        fixtures = (
            ("file", "SKILL.md"),
            ("directory", "scripts"),
            ("symlink", "SKILL.md"),
        )

        for fixture, relative_path in fixtures:
            with self.subTest(fixture=fixture), isolated_home() as home:
                source = home.parent / f"source-{fixture}"
                source.mkdir()
                (source / "SKILL.md").write_text("skill source\n")
                (source / "scripts").mkdir()
                (source / "scripts" / "install_skill.sh").write_text("#!/usr/bin/env bash\n")

                destination = home.parent / f"destination-{fixture}"
                destination.mkdir()
                conflict = destination / relative_path
                preserved_target = None

                if fixture == "file":
                    conflict.write_text("concurrent\n")
                elif fixture == "directory":
                    conflict.mkdir()
                    (conflict / "concurrent.txt").write_text("concurrent\n")
                else:
                    preserved_target = home.parent / "preserved-symlink-target"
                    preserved_target.write_text("keep me\n")
                    conflict.symlink_to(preserved_target)

                result = self.run_copy_staged_tree(source, destination)

                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Refusing to overwrite", result.stderr)
                if fixture == "directory":
                    self.assertTrue(conflict.is_dir())
                    self.assertEqual(
                        (conflict / "concurrent.txt").read_text(),
                        "concurrent\n",
                    )
                    self.assertFalse((conflict / "install_skill.sh").exists())
                elif fixture == "symlink":
                    self.assertTrue(conflict.is_symlink())
                    self.assertEqual(preserved_target.read_text(), "keep me\n")
                else:
                    self.assertEqual(conflict.read_text(), "concurrent\n")


if __name__ == "__main__":
    unittest.main()
