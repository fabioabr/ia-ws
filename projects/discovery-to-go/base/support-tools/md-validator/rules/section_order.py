"""Section order validation rule.

Checks the standard section ordering:
  Content -> Documentos Relacionados -> Desvios de Behavior -> Historico de Alteracoes

Rules:
- WARNING if changelog section exists but is NOT the last H2
- WARNING if related docs section appears AFTER changelog
- WARNING if deviations section appears AFTER changelog
- INFO if no changelog section found
"""

import re
import unicodedata
from typing import List

from models import Issue, Severity
from utils import get_lines


HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$")

# Key phrases for matching special sections (case-insensitive, emoji-stripped)
CHANGELOG_KEYWORDS = [
    "histórico de alterações",
    "historico de alteracoes",
    "changelog",
]
RELATED_DOCS_KEYWORDS = [
    "documentos relacionados",
    "related documents",
    "related",
]
DEVIATIONS_KEYWORDS = [
    "desvios de behavior",
    "desvios",
    "behavior deviations",
]


def _normalize(text: str) -> str:
    """Strip emojis, variation selectors, ZWJ, and extra whitespace; lowercase."""
    result = []
    for ch in text:
        cat = unicodedata.category(ch)
        cp = ord(ch)
        # Skip emoji characters
        if cat == "So":
            continue
        if 0x1F000 <= cp <= 0x1FAFF:
            continue
        if 0x2600 <= cp <= 0x27BF:
            continue
        # Skip variation selectors and ZWJ
        if 0xFE00 <= cp <= 0xFE0F or cp == 0x200D:
            continue
        result.append(ch)
    return "".join(result).strip().lower()


def _classify_section(text: str) -> str | None:
    """Classify an H2 heading as a known section type or None."""
    norm = _normalize(text)
    for kw in CHANGELOG_KEYWORDS:
        if kw in norm:
            return "changelog"
    for kw in DEVIATIONS_KEYWORDS:
        if kw in norm:
            return "deviations"
    for kw in RELATED_DOCS_KEYWORDS:
        if kw in norm:
            return "related-docs"
    return None


def validate(file_path: str, content: str, frontmatter: dict, body: str) -> List[Issue]:
    issues: List[Issue] = []
    lines = get_lines(content)
    in_code_block = False

    # Collect all H2 sections with classification
    h2_sections: list[tuple[int, str | None, str]] = []  # (line, type, raw_text)

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

        if level == 2:
            stype = _classify_section(text)
            h2_sections.append((i, stype, text))

    if not h2_sections:
        return issues

    # Find changelog, related-docs, and deviations entries
    changelog_entries = [(idx, ln, txt) for idx, (ln, st, txt) in enumerate(h2_sections) if st == "changelog"]
    related_entries = [(idx, ln, txt) for idx, (ln, st, txt) in enumerate(h2_sections) if st == "related-docs"]
    deviations_entries = [(idx, ln, txt) for idx, (ln, st, txt) in enumerate(h2_sections) if st == "deviations"]

    last_h2_index = len(h2_sections) - 1

    # WARNING: changelog exists but is not the last H2
    for idx, ln, txt in changelog_entries:
        if idx != last_h2_index:
            issues.append(Issue(
                rule="section-order",
                severity=Severity.WARNING,
                message=(
                    f"Changelog section '## {txt}' (line {ln}) must be the last H2 section, "
                    f"but there are H2 sections after it"
                ),
                line=ln,
            ))

    # WARNING: related-docs appears after changelog
    if changelog_entries:
        changelog_idx = changelog_entries[0][0]
        for idx, ln, txt in related_entries:
            if idx > changelog_idx:
                issues.append(Issue(
                    rule="section-order",
                    severity=Severity.WARNING,
                    message=(
                        f"Related documents section '## {txt}' (line {ln}) "
                        f"must appear before the changelog section"
                    ),
                    line=ln,
                ))

        # WARNING: deviations appears after changelog
        for idx, ln, txt in deviations_entries:
            if idx > changelog_idx:
                issues.append(Issue(
                    rule="section-order",
                    severity=Severity.WARNING,
                    message=(
                        f"Deviations section '## {txt}' (line {ln}) "
                        f"must appear before the changelog section"
                    ),
                    line=ln,
                ))

    # INFO: no changelog found
    if not changelog_entries:
        issues.append(Issue(
            rule="section-order",
            severity=Severity.INFO,
            message="No changelog section found (recommended: add '## 📜 Histórico de Alterações' as the last H2)",
        ))

    return issues
