"""Tests for the release gate that guards tag, package version and changelog."""

import importlib.util
from pathlib import Path
import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "release_guard", ROOT / ".github" / "scripts" / "release_guard.py"
)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


def write_repo(root, version="1.2.3", date="2026-08-18", entry="- Do a thing"):
    """Create a minimal repository layout the guard can read."""

    (root / "epubcheck").mkdir(parents=True)
    (root / "epubcheck" / "__init__.py").write_text(f'__version__ = "{version}"\n')
    (root / "README.md").write_text(
        f"## Changelog\n\n### {version} - {date}\n\n{entry}\n\n### 1.0.0 - 2020-01-01\n\n- Old\n"
    )
    return root


def test_package_version(tmp_path):
    """The declared __version__ is read without importing the package."""
    write_repo(tmp_path, version="9.9.9")

    assert guard.package_version(tmp_path) == "9.9.9"


def test_changelog_notes(tmp_path):
    """Only the entry for the released version is returned, not later sections."""
    write_repo(tmp_path, entry="- Do a thing\n- Do another")

    assert guard.changelog_notes(tmp_path, "1.2.3") == "- Do a thing\n- Do another"


def test_changelog_notes_missing_section(tmp_path):
    """A version with no changelog section aborts the release."""
    write_repo(tmp_path)

    with pytest.raises(SystemExit, match="no changelog section"):
        guard.changelog_notes(tmp_path, "4.5.6")


def test_changelog_notes_still_unreleased(tmp_path):
    """A changelog entry left as Unreleased aborts the release."""
    write_repo(tmp_path, date="Unreleased")

    with pytest.raises(SystemExit, match="set a release date"):
        guard.changelog_notes(tmp_path, "1.2.3")


def test_changelog_notes_empty_section(tmp_path):
    """A changelog section without any content aborts the release."""
    write_repo(tmp_path, entry="")

    with pytest.raises(SystemExit, match="is empty"):
        guard.changelog_notes(tmp_path, "1.2.3")


def test_main_rejects_mismatched_version(tmp_path, monkeypatch):
    """Releasing a version the package does not declare aborts before publishing."""
    monkeypatch.setattr(guard, "ROOT", write_repo(tmp_path, version="1.2.3"))

    with pytest.raises(SystemExit, match="version mismatch"):
        guard.main(["7.7.7"])


def test_main_writes_notes(tmp_path, monkeypatch):
    """A passing guard writes the changelog entry for the GitHub release."""
    monkeypatch.setattr(guard, "ROOT", write_repo(tmp_path / "repo", version="1.2.3"))
    notes = tmp_path / "notes.md"

    assert guard.main(["1.2.3", "--notes", str(notes)]) == 0
    assert notes.read_text() == "- Do a thing\n"


def test_repository_versions_agree():
    """The real pyproject.toml and __init__.py must not drift apart."""
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert f'version = "{guard.package_version(ROOT)}"' in pyproject
