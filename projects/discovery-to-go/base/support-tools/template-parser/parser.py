"""Line-based parser for report-template `template.md` files.

Grammar (informal EBNF — see schemas/template-syntax.md for full spec):

    template        = frontmatter custom-block? sub-block? layout-block
    frontmatter     = "---\n" yaml "\n---"
    custom-block    = "## Custom Regions\n" custom-region+
    custom-region   = "### CUSTOM-" digit+ " --- " title "\nPrompt: " text
    sub-block       = "## Sub-Templates\n" sub-template+
    sub-template    = "### SUB-" name " --- " title "\n" section+
    layout-block    = "## Layout\n" tab+
    tab             = "# Tab: " name "\n" section+
    section         = "> " name "\n" row+
    row             = "[" card ("|" card)* "]\n"
    card            = reg-card | custom-card | sub-card
"""

import re
from typing import List, Optional, Tuple

import yaml

from models import (
    Card,
    CardType,
    CustomRegion,
    ParseError,
    Row,
    Section,
    SubTemplate,
    Tab,
    Template,
)


# Regex for card identification
_RE_REG = re.compile(r"^REG-[A-Z]+-\d+(?::[A-Za-z0-9_\-{}]+)?$")
_RE_CUSTOM = re.compile(r"^CUSTOM-\d+(?::[A-Za-z0-9_\-{}]+)?$")
_RE_SUB = re.compile(r"^SUB-[A-Z][A-Z0-9_\-]*(?::[A-Za-z0-9_\-{}]+)?$")

# Regex for structural lines
_RE_CUSTOM_HEADER = re.compile(r"^###\s+(CUSTOM-\d+)\s+[-—]\s+(.+?)\s*$")
_RE_SUB_HEADER = re.compile(r"^###\s+(SUB-[A-Z][A-Z0-9_\-]*)\s+[-—]\s+(.+?)\s*$")
_RE_TAB_HEADER = re.compile(r"^#\s+Tab:\s+(.+?)\s*$")
_RE_SECTION = re.compile(r"^>\s+(.+?)\s*$")
_RE_ROW = re.compile(r"^\[(.+)\]\s*$")
_RE_H2 = re.compile(r"^##\s+(.+?)\s*$")
_RE_HR = re.compile(r"^---+\s*$")


def parse(text: str) -> Template:
    """Parse the full template file content into a Template AST."""
    template = Template()
    lines = text.splitlines()
    idx = 0

    # 1) Frontmatter
    idx, template.frontmatter = _parse_frontmatter(lines, idx)

    # 2/3/4) Main sections, in fixed order
    # Skip blank lines
    idx = _skip_blank(lines, idx)

    # Detect section headers and dispatch
    while idx < len(lines):
        line = lines[idx]
        m = _RE_H2.match(line)
        if m:
            name = m.group(1).strip().lower()
            if name == "custom regions":
                idx = _parse_custom_regions(lines, idx + 1, template)
            elif name == "sub-templates":
                idx = _parse_sub_templates(lines, idx + 1, template)
            elif name == "layout":
                idx = _parse_layout(lines, idx + 1, template)
            else:
                raise ParseError(
                    f"unknown top-level section '## {m.group(1)}'", idx + 1
                )
        elif line.strip() == "":
            idx += 1
        else:
            raise ParseError(f"unexpected content outside a section: {line!r}", idx + 1)

    # Layout is mandatory
    if not template.tabs:
        raise ParseError("template has no tabs — '## Layout' block is missing or empty")

    return template


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def _parse_frontmatter(lines: List[str], idx: int) -> Tuple[int, dict]:
    if idx >= len(lines) or lines[idx].strip() != "---":
        raise ParseError("missing frontmatter opening '---'", idx + 1)
    idx += 1
    start = idx
    while idx < len(lines) and lines[idx].strip() != "---":
        idx += 1
    if idx >= len(lines):
        raise ParseError("missing frontmatter closing '---'", start)
    fm_text = "\n".join(lines[start:idx])
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        raise ParseError(f"invalid frontmatter YAML: {e}", start + 1)
    if not isinstance(fm, dict):
        raise ParseError("frontmatter must be a YAML mapping", start + 1)
    return idx + 1, fm


# ---------------------------------------------------------------------------
# Custom Regions
# ---------------------------------------------------------------------------

def _parse_custom_regions(lines: List[str], idx: int, t: Template) -> int:
    while idx < len(lines):
        line = lines[idx]
        if _is_next_top_section(line):
            return idx
        stripped = line.strip()
        if stripped == "":
            idx += 1
            continue
        m = _RE_CUSTOM_HEADER.match(line)
        if not m:
            raise ParseError(
                f"expected '### CUSTOM-N — Title' inside Custom Regions, got {line!r}",
                idx + 1,
            )
        cid, title = m.group(1), m.group(2)
        idx += 1
        prompt, idx = _collect_prompt(lines, idx)
        t.custom_regions.append(
            CustomRegion(id=cid, title=title, prompt=prompt, line=idx)
        )
    return idx


def _collect_prompt(lines: List[str], idx: int) -> Tuple[str, int]:
    # Collect everything until the next '### CUSTOM-' or top-level section
    buf: List[str] = []
    seen_prompt_marker = False
    while idx < len(lines):
        line = lines[idx]
        if _is_next_top_section(line):
            break
        if _RE_CUSTOM_HEADER.match(line) or _RE_SUB_HEADER.match(line):
            break
        # Strip leading "Prompt:" from first non-empty line
        if not seen_prompt_marker and line.strip().startswith("Prompt:"):
            content = line.split("Prompt:", 1)[1].lstrip()
            if content:
                buf.append(content)
            seen_prompt_marker = True
        else:
            buf.append(line)
        idx += 1
    text = "\n".join(buf).strip()
    return text, idx


# ---------------------------------------------------------------------------
# Sub-Templates
# ---------------------------------------------------------------------------

def _parse_sub_templates(lines: List[str], idx: int, t: Template) -> int:
    while idx < len(lines):
        line = lines[idx]
        if _is_next_top_section(line):
            return idx
        stripped = line.strip()
        if stripped == "":
            idx += 1
            continue
        m = _RE_SUB_HEADER.match(line)
        if not m:
            raise ParseError(
                f"expected '### SUB-NAME — Title' inside Sub-Templates, got {line!r}",
                idx + 1,
            )
        sid, title = m.group(1), m.group(2)
        sub = SubTemplate(id=sid, title_template=title, line=idx + 1)
        idx += 1
        idx = _parse_sections_until(lines, idx, sub.sections, stop_on_sub=True)
        t.sub_templates.append(sub)
    return idx


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

def _parse_layout(lines: List[str], idx: int, t: Template) -> int:
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()
        if stripped == "":
            idx += 1
            continue
        if _RE_HR.match(stripped):
            idx += 1
            continue
        m = _RE_TAB_HEADER.match(line)
        if not m:
            if _RE_H2.match(line):
                return idx  # hand back to main loop (shouldn't happen)
            raise ParseError(
                f"expected '# Tab: Name' in Layout, got {line!r}", idx + 1
            )
        tab = Tab(name=m.group(1), line=idx + 1)
        idx += 1
        idx = _parse_sections_until(lines, idx, tab.sections, stop_on_tab=True)
        t.tabs.append(tab)
    return idx


# ---------------------------------------------------------------------------
# Sections + Rows (shared by layout tabs and sub-templates)
# ---------------------------------------------------------------------------

def _parse_sections_until(
    lines: List[str],
    idx: int,
    sections: List[Section],
    stop_on_tab: bool = False,
    stop_on_sub: bool = False,
) -> int:
    current: Optional[Section] = None
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()
        if stripped == "":
            idx += 1
            continue
        if _RE_HR.match(stripped):
            # end-of-tab marker; do not consume — parent handles it
            return idx
        if stop_on_tab and _RE_TAB_HEADER.match(line):
            return idx
        if stop_on_sub and _RE_SUB_HEADER.match(line):
            return idx
        if _is_next_top_section(line):
            return idx
        m_sec = _RE_SECTION.match(line)
        if m_sec:
            current = Section(name=m_sec.group(1), line=idx + 1)
            sections.append(current)
            idx += 1
            continue
        m_row = _RE_ROW.match(line)
        if m_row:
            if current is None:
                # Anonymous section — allowed e.g. when a tab contains only
                # a SUB-* invocation with no explicit section header.
                current = Section(name="", line=idx + 1)
                sections.append(current)
            current.rows.append(_parse_row(m_row.group(1), idx + 1))
            idx += 1
            continue
        raise ParseError(
            f"unexpected line inside section: {line!r}", idx + 1
        )
    return idx


def _parse_row(inner: str, line_no: int) -> Row:
    parts = [p.strip() for p in inner.split("|")]
    if not parts or any(p == "" for p in parts):
        raise ParseError(
            "row has empty card slot (check '|' separators)", line_no
        )
    cards: List[Card] = []
    for token in parts:
        cards.append(_classify_card(token, line_no))
    return Row(cards=cards, line=line_no)


def _classify_card(token: str, line_no: int) -> Card:
    cid, variant = _split_variant(token)
    if _RE_REG.match(token):
        return Card(type=CardType.REG, id=cid, variant=variant)
    if _RE_CUSTOM.match(token):
        return Card(type=CardType.CUSTOM, id=cid, variant=variant)
    if _RE_SUB.match(token):
        return Card(type=CardType.SUB, id=cid, variant=variant)
    raise ParseError(
        f"unrecognized card token {token!r} — must match REG-*, CUSTOM-* or SUB-*",
        line_no,
    )


def _split_variant(token: str) -> Tuple[str, Optional[str]]:
    if ":" in token:
        cid, variant = token.split(":", 1)
        return cid, variant
    return token, None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _skip_blank(lines: List[str], idx: int) -> int:
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    return idx


def _is_next_top_section(line: str) -> bool:
    """True when `line` starts a new '## Name' top-level section."""
    m = _RE_H2.match(line)
    if not m:
        return False
    name = m.group(1).strip().lower()
    return name in ("custom regions", "sub-templates", "layout")
