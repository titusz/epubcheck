"""Release gate that checks a version tag against the package and the changelog.

Run as ``python .github/scripts/release_guard.py <version> [--notes PATH]``. It exits
non-zero with an explanation when anything disagrees, so a release aborts before it
builds or uploads. With ``--notes`` it also writes the changelog entry to a file for
use as GitHub Release notes.
"""

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def package_version(root):
    """Read ``__version__`` from the package without importing it.

    :param Path root: Repository root
    :return str: The declared version
    """

    source = (root / "epubcheck" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r'^__version__ = "([^"]+)"', source, re.MULTILINE)
    if match is None:
        raise SystemExit("epubcheck/__init__.py declares no __version__")
    return match.group(1)


def changelog_notes(root, version):
    """Extract the released changelog entry for a version from the README.

    :param Path root: Repository root
    :param str version: Version being released
    :return str: The entry body, without its heading
    """

    readme = (root / "README.md").read_text(encoding="utf-8")
    heading = rf"^### {re.escape(version)} - (?P<date>[^\n]+)\n"
    match = re.search(heading + r"(?P<body>.*?)(?=^### |\Z)", readme, re.MULTILINE | re.DOTALL)
    if match is None:
        raise SystemExit(f"README.md has no changelog section '### {version} - <date>'")
    date = match.group("date").strip()
    if "unreleased" in date.lower():
        raise SystemExit(f"README.md still marks {version} as '{date}' - set a release date")
    body = match.group("body").strip()
    if not body:
        raise SystemExit(f"README.md changelog section for {version} is empty")
    return body


def main(argv=None):
    """Check the tag against the package version and the changelog.

    :param list | None argv: Overrides command options (for testing)
    :return int: 0 when every check passes
    """

    parser = argparse.ArgumentParser(description="Verify a release is ready to publish")
    parser.add_argument("version", help="Version being released, without the leading 'v'")
    parser.add_argument("--notes", help="Write the changelog entry to this file")
    args = parser.parse_args(argv)

    declared = package_version(ROOT)
    if declared != args.version:
        raise SystemExit(
            f"version mismatch: releasing {args.version} but epubcheck/__init__.py says {declared}"
        )

    notes = changelog_notes(ROOT, args.version)
    if args.notes:
        Path(args.notes).write_text(notes + "\n", encoding="utf-8")

    print(f"release guard passed for {args.version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
