"""Callouts validation rule.

Checks:
- Detects valid Obsidian callout blocks (> [!type])
- Warns about callout-like patterns that don't match valid format
- Reports count of callouts by type
"""

import re
from collections import Counter
from typing import List

from models import Issue, Severity

# Valid Obsidian callout types
VALID_CALLOUT_TYPES = {
    "info", "warning", "danger", "tip", "note", "abstract",
    "todo", "success", "question", "failure", "bug", "example", "quote",
}

# Matches a valid callout opening: > [!type]
VALID_CALLOUT_PATTERN = re.compile(r"^>\s*\[!([a-z]+)\]", re.IGNORECASE)

# Matches callout-like patterns that may be malformed:
# e.g. > [!WARN], > [NOTE], > [!anything]
CALLOUT_LIKE_PATTERN = re.compile(r"^>\s*\[(!?)([^\]]+)\]")


def _strip_code_blocks(body: str) -> str:
    """Remove fenced code blocks from text to avoid false positives."""
    return re.sub(r"```[^\n]*\n.*?```", "", body, flags=re.DOTALL)


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    clean_body = _strip_code_blocks(body)
    lines = clean_body.splitlines()

    type_counts: Counter = Counter()

    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Try valid callout pattern first
        valid_match = VALID_CALLOUT_PATTERN.match(stripped)
        if valid_match:
            callout_type = valid_match.group(1).lower()
            if callout_type in VALID_CALLOUT_TYPES:
                type_counts[callout_type] += 1
                continue
            else:
                # Has correct format but unknown type
                issues.append(Issue(
                    rule="callout",
                    severity=Severity.WARNING,
                    message=f"Unknown callout type '> [!{valid_match.group(1)}]' "
                            f"(valid: {', '.join(sorted(VALID_CALLOUT_TYPES))})",
                ))
                continue

        # Check for malformed callout-like patterns
        like_match = CALLOUT_LIKE_PATTERN.match(stripped)
        if like_match:
            bang = like_match.group(1)
            inner = like_match.group(2).strip()

            # Missing the ! prefix
            if not bang:
                # Check if it looks like an intended callout type
                if inner.lower() in VALID_CALLOUT_TYPES or inner.upper() in {t.upper() for t in VALID_CALLOUT_TYPES}:
                    issues.append(Issue(
                        rule="callout",
                        severity=Severity.WARNING,
                        message=f"Malformed callout '> [{inner}]' — missing '!' "
                                f"(use '> [!{inner.lower()}]')",
                    ))
            elif bang == "!":
                # Has ! but type is not lowercase or not valid
                lower_inner = inner.lower()
                if lower_inner in VALID_CALLOUT_TYPES and inner != lower_inner:
                    issues.append(Issue(
                        rule="callout",
                        severity=Severity.WARNING,
                        message=f"Callout type '> [!{inner}]' should be lowercase "
                                f"(use '> [!{lower_inner}]')",
                    ))

    # Report counts by type
    if type_counts:
        summary = ", ".join(f"{t}: {c}" for t, c in sorted(type_counts.items()))
        issues.append(Issue(
            rule="callout",
            severity=Severity.INFO,
            message=f"Callouts found — {summary}",
        ))

    return issues
