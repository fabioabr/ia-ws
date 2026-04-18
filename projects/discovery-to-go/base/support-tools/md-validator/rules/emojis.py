"""Emoji validation rule.

Checks:
- WARNING for each H2 that does NOT have a semantic emoji at the start
- ERROR if any heading has more than 1 emoji
- INFO listing the expected emoji mapping
"""

import re
import unicodedata
from typing import List

from models import Issue, Severity
from utils import get_lines


HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$")

# Expected semantic emoji mapping
EMOJI_MAPPING = {
    "\U0001F3AF": "objective",         # 🎯
    "\U0001F4CB": "overview/rules",    # 📋
    "\u26A0\uFE0F": "warning/deviations",  # ⚠️
    "\u26A0": "warning/deviations",    # ⚠ (without variation selector)
    "\U0001F517": "related",           # 🔗
    "\U0001F4DC": "changelog",         # 📜
    "\U0001F9E9": "components",        # 🧩
    "\U0001F527": "tools/config",      # 🔧
    "\U0001F4CA": "data/metrics",      # 📊
    "\U0001F4A1": "tips",              # 💡
    "\U0001F3D7\uFE0F": "architecture",  # 🏗️
    "\U0001F3D7": "architecture",      # 🏗 (without variation selector)
    "\U0001F4E6": "packages/assets",   # 📦
    "\U0001F680": "actions/deployment", # 🚀
    "\u2705": "validation/checklist",  # ✅
}


def _is_emoji_char(ch: str) -> bool:
    """Return True if the character is an emoji."""
    cat = unicodedata.category(ch)
    if cat == "So":
        return True
    cp = ord(ch)
    if 0x1F1E0 <= cp <= 0x1F1FF:
        return True
    if 0x1F3FB <= cp <= 0x1F3FF:
        return True
    if 0x1F900 <= cp <= 0x1F9FF:
        return True
    if 0x2600 <= cp <= 0x27BF:
        return True
    if 0x1FA00 <= cp <= 0x1FAFF:
        return True
    if 0x1F300 <= cp <= 0x1F5FF:
        return True
    if 0x1F600 <= cp <= 0x1F64F:
        return True
    if 0x1F680 <= cp <= 0x1F6FF:
        return True
    return False


def _count_emojis(text: str) -> int:
    """Count the number of distinct emoji characters in text.

    Compound emojis (e.g., 🏗️ which is 🏗 + variation selector) count as 1.
    """
    count = 0
    prev_was_emoji = False
    for ch in text:
        cp = ord(ch)
        # Skip variation selectors and ZWJ (part of compound emojis)
        if 0xFE00 <= cp <= 0xFE0F or cp == 0x200D:
            continue
        if _is_emoji_char(ch):
            if not prev_was_emoji:
                count += 1
            prev_was_emoji = True
        else:
            prev_was_emoji = False
    return count


def _has_leading_emoji(text: str) -> bool:
    """Check if the heading text starts with an emoji (ignoring whitespace)."""
    stripped = text.lstrip()
    if not stripped:
        return False
    return _is_emoji_char(stripped[0])


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    lines = get_lines(content)
    in_code_block = False
    h2_found = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        match = HEADING_PATTERN.match(stripped)
        if not match:
            continue

        level = len(match.group(1))
        text = match.group(2).strip()
        emoji_count = _count_emojis(text)

        # H2 should have a semantic emoji at the start
        if level == 2:
            h2_found = True
            if not _has_leading_emoji(text):
                issues.append(Issue(
                    rule="emojis",
                    severity=Severity.WARNING,
                    message=f"H2 heading missing semantic emoji: '## {text}'",
                    line=i,
                ))

        # No heading should have more than 1 emoji
        if emoji_count > 1:
            issues.append(Issue(
                rule="emojis",
                severity=Severity.ERROR,
                message=(
                    f"Heading has {emoji_count} emojis (maximum 1 allowed): "
                    f"'{'#' * level} {text}'"
                ),
                line=i,
            ))

    # Info: list expected emoji mapping
    mapping_lines = ", ".join(
        f"{emoji}={meaning}" for emoji, meaning in {
            "\U0001F3AF": "objective",
            "\U0001F4CB": "overview/rules",
            "\u26A0\uFE0F": "warning/deviations",
            "\U0001F517": "related",
            "\U0001F4DC": "changelog",
            "\U0001F9E9": "components",
            "\U0001F527": "tools/config",
            "\U0001F4CA": "data/metrics",
            "\U0001F4A1": "tips",
            "\U0001F3D7\uFE0F": "architecture",
            "\U0001F4E6": "packages/assets",
            "\U0001F680": "actions/deployment",
            "\u2705": "validation/checklist",
        }.items()
    )
    issues.append(Issue(
        rule="emojis",
        severity=Severity.INFO,
        message=f"Expected emoji mapping: {mapping_lines}",
    ))

    return issues
