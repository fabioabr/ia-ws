"""Template parser CLI.

Parses a report-template `template.md` file and emits the AST as JSON (default)
or a human-readable text dump.

Usage:
    python main.py <template.md> [--format json|text] [--validate]

Examples:
    python main.py ../../standards/conventions/report-templates/basic/template.md
    python main.py ./template.md --format text
    python main.py ./template.md --validate
"""

import argparse
import io
import json
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )

_PACKAGE_ROOT = Path(__file__).resolve().parent
if str(_PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_PACKAGE_ROOT))

from models import ParseError, Template  # noqa: E402
from parser import parse  # noqa: E402


def _format_text(t: Template) -> str:
    out = []
    out.append(f"Template: {t.frontmatter.get('template-id', '?')}")
    out.append(f"Title:    {t.frontmatter.get('title', '?')}")
    out.append(f"Version:  {t.frontmatter.get('version', '?')}")
    out.append("")

    out.append(f"Custom Regions ({len(t.custom_regions)}):")
    for c in t.custom_regions:
        preview = c.prompt[:60].replace("\n", " ") + ("..." if len(c.prompt) > 60 else "")
        out.append(f"  {c.id} — {c.title}")
        out.append(f"    prompt: {preview}")
    out.append("")

    out.append(f"Sub-Templates ({len(t.sub_templates)}):")
    for s in t.sub_templates:
        out.append(f"  {s.id} — {s.title_template} ({len(s.sections)} sections)")
        for sec in s.sections:
            out.append(f"    > {sec.name} ({len(sec.rows)} rows)")
    out.append("")

    out.append(f"Tabs ({len(t.tabs)}):")
    for tab in t.tabs:
        out.append(f"  # Tab: {tab.name}")
        for sec in tab.sections:
            out.append(f"    > {sec.name}")
            for row in sec.rows:
                cards = " | ".join(
                    f"{c.id}:{c.variant}" if c.variant else c.id for c in row.cards
                )
                out.append(f"      [{cards}]")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse a report-template .md file")
    ap.add_argument("path", help="Path to template.md")
    ap.add_argument(
        "--format", choices=["json", "text"], default="json", help="Output format"
    )
    ap.add_argument(
        "--validate",
        action="store_true",
        help="Validate syntax only — no output, exit code signals result",
    )
    args = ap.parse_args()

    path = Path(args.path)
    if not path.is_file():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2

    try:
        text = path.read_text(encoding="utf-8")
        t = parse(text)
    except ParseError as e:
        print(f"parse error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"unexpected error: {e}", file=sys.stderr)
        return 3

    if args.validate:
        print("ok", file=sys.stderr)
        return 0

    if args.format == "json":
        print(
            json.dumps(
                t.to_dict(),
                ensure_ascii=False,
                indent=2,
                default=str,
            )
        )
    else:
        print(_format_text(t))
    return 0


if __name__ == "__main__":
    sys.exit(main())
