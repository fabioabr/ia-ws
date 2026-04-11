"""Acronym validation rule.

Checks:
- First occurrence of each non-exempt acronym must be expanded: "Full Form (ACRONYM)"
- If 3+ non-exempt acronyms are used, a glossary section must exist before changelog
- Reports all acronyms found with occurrence counts

Convention reference: conventions/acronyms/markdown-treatment.md
"""

import re
from typing import List

from models import Issue, Severity


# Acronyms that are universally known and never need expansion.
EXEMPT_ACRONYMS: set[str] = {
    "HTTP", "HTTPS", "URL", "HTML", "CSS", "JS", "PDF", "PNG", "JPG",
    "CSV", "JSON", "XML", "BR", "US", "EU", "API", "CLI", "SQL", "SSH",
    "FTP", "DNS", "TCP", "UDP", "IP", "RAM", "CPU", "GPU", "SSD", "HDD",
    "USB", "YAML", "TOML", "GIT", "NPM", "SDK", "UI", "UX", "AI", "IA",
    "ID", "OK", "MD", "ASCII", "SKILL", "README", "TODO",
    "SIGLA", "MCP", "BM", "CDN", "REST", "CRUD", "LGPD", "GDPR",
    "ERROR", "WARNING", "INFO", "DEBUG", "TRACE", "FATAL",
    "TRUE", "FALSE", "NULL", "NONE",
    "ARGUMENTS", "MUST", "SHALL", "SHOULD",
}

# Patterns that look like acronyms but aren't (hex colors, placeholders, etc.)
FALSE_POSITIVE_RE = re.compile(
    r"^("
    r"[A-F0-9]{6}"        # Hex colors like FFFFFF, 1E1E2E
    r"|[A-Z]{1,3}(?=\.\d)"  # Version placeholders XX.YY.ZZZ
    r"|XX|YY|ZZZ"         # Explicit version format placeholders
    r")$"
)

# Pattern to detect bare acronyms: 2+ uppercase letters as whole words.
ACRONYM_RE = re.compile(r"\b[A-Z]{2,}\b")

# Template for detecting an expansion like "Some Words (ACRONYM)".
EXPANSION_RE_TEMPLATE = r"(?:[A-ZÀ-Ýa-zà-ý][\w-]*\s+)+\({acronym}\)"

# Glossary section heading (H2 or H3).
GLOSSARY_HEADING_RE = re.compile(
    r"^#{2,3}\s+.*(?:Glossário|Glossary|Siglas)",
    re.IGNORECASE | re.MULTILINE,
)


def _strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks, replacing content with blank lines to
    preserve line-number alignment."""
    result: list[str] = []
    lines = text.split("\n")
    in_fence = False
    fence_char = ""
    for line in lines:
        if not in_fence:
            m = re.match(r"^(`{3,}|~{3,})", line)
            if m:
                in_fence = True
                fence_char = m.group(1)[0]
                result.append("")
                continue
        else:
            if re.match(rf"^{re.escape(fence_char)}{{3,}}\s*$", line):
                in_fence = False
                result.append("")
                continue
            result.append("")
            continue
        result.append(line)
    return "\n".join(result)


def _strip_inline_code(text: str) -> str:
    """Replace inline code spans with whitespace to avoid false matches."""
    return re.sub(r"`[^`]+`", " ", text)


def _strip_urls(text: str) -> str:
    """Remove URLs so acronyms inside them are not matched."""
    return re.sub(r"https?://\S+", " ", text)


def _clean_body(body: str) -> str:
    """Return body text with code blocks, inline code, and URLs removed."""
    text = _strip_code_blocks(body)
    text = _strip_inline_code(text)
    text = _strip_urls(text)
    return text


def _find_first_line(body: str, acronym: str) -> int | None:
    """Return the 1-based line number of the first bare occurrence of
    *acronym* in the cleaned body text."""
    cleaned = _clean_body(body)
    pattern = re.compile(rf"\b{re.escape(acronym)}\b")
    for i, line in enumerate(cleaned.split("\n"), start=1):
        if pattern.search(line):
            return i
    return None


def _has_expansion_before(clean_text: str, acronym: str) -> bool:
    """Check whether an expansion pattern like 'Some Words (ACRONYM)' appears
    in *clean_text* before or at the first bare (non-parenthesized) use."""
    expansion_pattern = re.compile(
        EXPANSION_RE_TEMPLATE.format(acronym=re.escape(acronym)),
    )
    # A bare use is one not immediately inside parentheses.
    bare_pattern = re.compile(rf"(?<!\()\b{re.escape(acronym)}\b(?!\))")

    exp_match = expansion_pattern.search(clean_text)
    bare_match = bare_pattern.search(clean_text)

    if exp_match is None:
        # No expansion found anywhere.
        return False
    if bare_match is None:
        # Only appears inside parentheses after its expansion — acceptable.
        return True
    # Expansion must come at or before the first bare use.
    return exp_match.start() <= bare_match.start()


def validate(
    file_path: str,
    content: str,
    frontmatter: dict,
    body: str,
) -> List[Issue]:
    issues: List[Issue] = []
    clean_text = _clean_body(body)

    # Skip acronym-bank files (they define acronyms, not use them)
    if "acronym-bank" in file_path.replace("\\", "/"):
        return issues

    # Collect all acronym occurrences (non-exempt).
    found: dict[str, int] = {}
    for m in ACRONYM_RE.finditer(clean_text):
        acr = m.group()
        if acr not in EXEMPT_ACRONYMS and not FALSE_POSITIVE_RE.match(acr):
            found[acr] = found.get(acr, 0) + 1

    if not found:
        return issues

    # --- Rule 1: first occurrence must be expanded --------------------------
    for acronym in sorted(found):
        if not _has_expansion_before(clean_text, acronym):
            line_no = _find_first_line(body, acronym)
            issues.append(Issue(
                rule="acronyms",
                severity=Severity.WARNING,
                message=(
                    f"Acronym '{acronym}' first appears without expansion. "
                    f"Write it as 'Full Form ({acronym})' on first use."
                ),
                line=line_no,
            ))

    # --- Rule 2: glossary required when 3+ non-exempt acronyms --------------
    if len(found) >= 3:
        if not GLOSSARY_HEADING_RE.search(body):
            issues.append(Issue(
                rule="acronyms",
                severity=Severity.WARNING,
                message=(
                    f"Document uses {len(found)} acronyms but has no glossary "
                    f"section. Add a '## Glossário' (or '## Glossary' / "
                    f"'## Siglas') section before the Changelog."
                ),
            ))

    # --- Info: list all acronyms found with counts --------------------------
    summary = ", ".join(
        f"{acr} ({count}x)" for acr, count in sorted(found.items())
    )
    issues.append(Issue(
        rule="acronyms",
        severity=Severity.INFO,
        message=f"Acronyms found: {summary}",
    ))

    return issues
