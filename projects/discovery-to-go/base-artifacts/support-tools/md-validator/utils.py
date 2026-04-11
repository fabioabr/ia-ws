import re
from pathlib import Path

import yaml


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body.

    Returns (frontmatter_dict, body_text).
    If no frontmatter block is found, returns ({}, full_content).
    """
    pattern = re.compile(r"\A---\s*\n(.*?\n)---\s*\n?", re.DOTALL)
    match = pattern.match(content)
    if not match:
        return {}, content

    yaml_text = match.group(1)
    body = content[match.end():]

    try:
        frontmatter = yaml.safe_load(yaml_text)
        if not isinstance(frontmatter, dict):
            frontmatter = {}
    except yaml.YAMLError:
        frontmatter = {}

    return frontmatter, body


def get_lines(content: str) -> list[str]:
    """Split content into a list of lines (preserving line content, no trailing newline chars)."""
    return content.splitlines()


def is_skill_file(file_path: str) -> bool:
    """Return True if the filename is SKILL.md."""
    return Path(file_path).name == "SKILL.md"
