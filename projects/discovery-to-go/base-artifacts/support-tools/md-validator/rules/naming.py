"""Naming validation rule.

Checks:
- Filename must be lowercase (except conventional names: SKILL.md, README.md, CLAUDE.md, MEMORY.md, TODO.md)
- Filename must not contain spaces
- Filename must not contain underscores (use hyphens)
- Parent folder names should not contain uppercase or underscores
"""

import re
from pathlib import PurePosixPath, PureWindowsPath
from typing import List

from models import Issue, Severity

# Conventional uppercase filenames that are allowed
CONVENTIONAL_UPPERCASE = {"SKILL.md", "README.md", "CLAUDE.md", "MEMORY.md", "TODO.md", "AGENTS.md", "LICENSE.md", "CHANGELOG.md", "CONTRIBUTING.md"}

# Known dot-prefixed folders that are exempt from naming checks
KNOWN_DOT_FOLDERS = {".claude", ".git", ".gitnexus", ".github", ".vscode", ".idea", ".obsidian"}

# Folders that are user/system-level and should not be flagged
IGNORED_FOLDERS = {"Users", "Workspace", "Program Files", "Program Files (x86)", "AppData", "Documents"}


def _parse_path(file_path: str) -> tuple[list[str], str]:
    """Parse file path into (folder_parts, filename).

    Handles both Windows and POSIX paths.
    """
    # Try Windows-style first if it has backslashes or drive letters
    if "\\" in file_path or (len(file_path) >= 2 and file_path[1] == ":"):
        path = PureWindowsPath(file_path)
    else:
        path = PurePosixPath(file_path)

    filename = path.name
    folder_parts = list(path.parent.parts)
    return folder_parts, filename


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    folder_parts, filename = _parse_path(file_path)

    # --- Filename checks ---

    if filename not in CONVENTIONAL_UPPERCASE:
        # Check for uppercase letters in filename
        if any(c.isupper() for c in filename):
            issues.append(Issue(
                rule="naming",
                severity=Severity.ERROR,
                message=f"Filename '{filename}' contains uppercase letters (use kebab-case)",
            ))

    # Check for spaces in filename
    if " " in filename:
        issues.append(Issue(
            rule="naming",
            severity=Severity.ERROR,
            message=f"Filename '{filename}' contains spaces (use hyphens instead)",
        ))

    # Check for underscores in filename
    if "_" in filename:
        issues.append(Issue(
            rule="naming",
            severity=Severity.ERROR,
            message=f"Filename '{filename}' contains underscores (use hyphens instead)",
        ))

    # --- Folder checks ---

    for folder in folder_parts:
        # Skip drive letters (e.g. "C:\"), root markers, and known dot-folders
        if len(folder) <= 3 and folder.endswith((":\\", ":", "/", "\\")):
            continue
        if folder in ("/", "\\"):
            continue
        if folder.startswith(".") and folder in KNOWN_DOT_FOLDERS:
            continue
        # Skip dot-prefixed folders in general (hidden folders)
        if folder.startswith("."):
            continue

        if folder in IGNORED_FOLDERS:
            continue

        if any(c.isupper() for c in folder):
            issues.append(Issue(
                rule="naming",
                severity=Severity.WARNING,
                message=f"Folder '{folder}' contains uppercase letters (prefer kebab-case)",
            ))

        if "_" in folder:
            issues.append(Issue(
                rule="naming",
                severity=Severity.WARNING,
                message=f"Folder '{folder}' contains underscores (use hyphens instead)",
            ))

    return issues
