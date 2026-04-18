"""Wikilinks validation rule.

Checks:
- Count of wikilinks found
- Wikilinks should not contain backslashes (use forward slashes)
- Wikilink paths should not contain spaces (use kebab-case paths)
"""

import re
from typing import List

from models import Issue, Severity

# Matches [[...]] wikilinks, capturing the inner content
WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def _strip_code_blocks(body: str) -> str:
    """Remove fenced code blocks from text to avoid false positives."""
    return re.sub(r"```[^\n]*\n.*?```", "", body, flags=re.DOTALL)


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    clean_body = _strip_code_blocks(body)

    wikilinks = WIKILINK_PATTERN.findall(clean_body)
    total = len(wikilinks)

    if total > 0:
        issues.append(Issue(
            rule="wikilink",
            severity=Severity.INFO,
            message=f"Found {total} wikilink(s)",
        ))

    # Check each wikilink for path issues
    # Map cleaned body lines back to original body lines for line numbers
    clean_lines = clean_body.splitlines()
    for line_idx, line in enumerate(clean_lines, start=1):
        for match in WIKILINK_PATTERN.finditer(line):
            link = match.group(1)
            # Split alias part if present: [[path|alias]]
            path_part = link.split("|")[0]

            if "\\" in path_part:
                issues.append(Issue(
                    rule="wikilink",
                    severity=Severity.WARNING,
                    message=f"Wikilink '[[{link}]]' contains backslashes (use forward slashes)",
                ))

            if " " in path_part:
                issues.append(Issue(
                    rule="wikilink",
                    severity=Severity.WARNING,
                    message=f"Wikilink '[[{link}]]' contains spaces in path (use kebab-case)",
                ))

    return issues
