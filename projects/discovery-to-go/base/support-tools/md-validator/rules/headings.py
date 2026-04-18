"""Heading validation rule.

Checks:
- Exactly one H1 per file
- ERROR if more than one H1 (report line numbers of extras)
- WARNING if H1 text doesn't match frontmatter title (strip emojis/whitespace)
- ERROR for skipped heading levels (e.g., H1 -> H3 without H2)
- WARNING if H1 has an emoji
"""

import re
import unicodedata
from typing import List

from models import Issue, Severity
from utils import get_lines


HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$")


def _is_emoji_char(ch: str) -> bool:
    """Return True if the character is an emoji or emoji component."""
    cat = unicodedata.category(ch)
    if cat == "So":
        return True
    cp = ord(ch)
    # Regional indicators
    if 0x1F1E0 <= cp <= 0x1F1FF:
        return True
    # Skin tone modifiers
    if 0x1F3FB <= cp <= 0x1F3FF:
        return True
    # Supplemental symbols and pictographs
    if 0x1F900 <= cp <= 0x1F9FF:
        return True
    # Misc symbols and dingbats range
    if 0x2600 <= cp <= 0x27BF:
        return True
    # Extended-A symbols
    if 0x1FA00 <= cp <= 0x1FAFF:
        return True
    # Misc symbols and pictographs
    if 0x1F300 <= cp <= 0x1F5FF:
        return True
    # Emoticons
    if 0x1F600 <= cp <= 0x1F64F:
        return True
    # Transport and map symbols
    if 0x1F680 <= cp <= 0x1F6FF:
        return True
    return False


def _strip_emojis(text: str) -> str:
    """Remove emoji characters, variation selectors, and ZWJ from text."""
    result = []
    for ch in text:
        if _is_emoji_char(ch):
            continue
        cp = ord(ch)
        # Skip variation selectors and ZWJ
        if 0xFE00 <= cp <= 0xFE0F or cp == 0x200D:
            continue
        result.append(ch)
    return "".join(result).strip()


def _has_emoji(text: str) -> bool:
    """Return True if text contains any emoji character."""
    return any(_is_emoji_char(ch) for ch in text)


def _parse_headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """Parse headings from lines, skipping fenced code blocks.

    Returns list of (line_number_1based, level, heading_text).
    """
    headings: list[tuple[int, int, str]] = []
    in_code_block = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        match = HEADING_PATTERN.match(stripped)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headings.append((i, level, text))

    return headings


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    lines = get_lines(content)
    headings = _parse_headings(lines)

    # --- Collect H1 headings ---
    h1_headings = [(ln, lvl, txt) for ln, lvl, txt in headings if lvl == 1]

    # Check: exactly one H1
    if len(h1_headings) == 0:
        issues.append(Issue(
            rule="headings",
            severity=Severity.ERROR,
            message="No H1 heading found. Every document must have exactly one H1.",
        ))
    elif len(h1_headings) > 1:
        extra_lines = [str(ln) for ln, _, _ in h1_headings[1:]]
        issues.append(Issue(
            rule="headings",
            severity=Severity.ERROR,
            message=(
                f"Multiple H1 headings found ({len(h1_headings)} total). "
                f"Extra H1 at line(s): {', '.join(extra_lines)}"
            ),
            line=h1_headings[1][0],
        ))

    # Check: H1 text matches frontmatter title (strip emojis and whitespace)
    if len(h1_headings) >= 1 and frontmatter.get("title"):
        h1_clean = _strip_emojis(h1_headings[0][2]).strip()
        fm_clean = _strip_emojis(str(frontmatter["title"])).strip()
        if h1_clean.lower() != fm_clean.lower():
            issues.append(Issue(
                rule="headings",
                severity=Severity.WARNING,
                message=(
                    f"H1 text '{h1_headings[0][2]}' does not match "
                    f"frontmatter title '{frontmatter['title']}'"
                ),
                line=h1_headings[0][0],
            ))

    # Check: H1 should not have emojis
    if len(h1_headings) >= 1 and _has_emoji(h1_headings[0][2]):
        issues.append(Issue(
            rule="headings",
            severity=Severity.WARNING,
            message="H1 should not contain emojis",
            line=h1_headings[0][0],
        ))

    # Check: no skipped heading levels
    if headings:
        prev_level = headings[0][1]
        for line_num, level, text in headings[1:]:
            if level > prev_level + 1:
                skipped = [f"H{lv}" for lv in range(prev_level + 1, level)]
                issues.append(Issue(
                    rule="headings",
                    severity=Severity.ERROR,
                    message=(
                        f"Skipped heading level(s): {', '.join(skipped)} "
                        f"(went from H{prev_level} to H{level} at '{text}')"
                    ),
                    line=line_num,
                ))
            prev_level = level

    return issues
