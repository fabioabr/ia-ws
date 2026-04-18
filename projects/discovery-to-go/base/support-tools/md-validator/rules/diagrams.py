"""Diagrams validation rule.

Checks:
- Count of mermaid code blocks
- Warning if mermaid block seems empty (< 2 lines of content)
- Warning for ASCII art diagrams outside code blocks
"""

import re
from typing import List

from models import Issue, Severity

# Patterns for detecting ASCII art diagrams (heuristic)
ASCII_BOX_PATTERN = re.compile(r"\+[-=]{3,}\+")
ASCII_PIPE_PATTERN = re.compile(r"\|[\s]{3,}\|")


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    lines = body.splitlines()

    in_code_block = False
    code_block_lang = ""
    code_block_start = 0
    code_block_content_lines = 0

    mermaid_count = 0
    empty_mermaid_lines: list[int] = []

    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Detect code fence boundaries
        if stripped.startswith("```"):
            if not in_code_block:
                # Opening fence
                in_code_block = True
                code_block_lang = stripped[3:].strip().lower()
                code_block_start = line_idx
                code_block_content_lines = 0
            else:
                # Closing fence
                if code_block_lang == "mermaid":
                    mermaid_count += 1
                    if code_block_content_lines < 2:
                        empty_mermaid_lines.append(code_block_start)
                in_code_block = False
                code_block_lang = ""
            continue

        if in_code_block:
            # Count non-empty lines inside mermaid blocks
            if code_block_lang == "mermaid" and stripped:
                code_block_content_lines += 1
            continue

        # Outside code blocks — check for ASCII art
        if ASCII_BOX_PATTERN.search(line) or ASCII_PIPE_PATTERN.search(line):
            issues.append(Issue(
                rule="diagram",
                severity=Severity.WARNING,
                message="Possible ASCII art diagram detected (use Mermaid instead)",
                line=line_idx,
            ))

    # Report mermaid block count
    if mermaid_count > 0:
        issues.append(Issue(
            rule="diagram",
            severity=Severity.INFO,
            message=f"Found {mermaid_count} mermaid diagram(s)",
        ))

    # Warn about empty mermaid blocks
    for start_line in empty_mermaid_lines:
        issues.append(Issue(
            rule="diagram",
            severity=Severity.WARNING,
            message="Mermaid block appears empty (less than 2 lines of content)",
            line=start_line,
        ))

    return issues
