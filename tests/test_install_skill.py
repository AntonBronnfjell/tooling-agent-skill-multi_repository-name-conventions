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


if __name__ == "__main__":
    unittest.main()
