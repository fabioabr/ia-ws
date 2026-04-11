"""Markdown validator CLI.

Validates .md files against workspace conventions.

Usage:
    python main.py <path> [--rule RULE] [--severity SEVERITY] [--format {text,json}] [--skip RULES]

Examples:
    python main.py ./my-document.md
    python main.py ./docs/ --severity error
    python main.py ./docs/ --rule frontmatter --format json
    python main.py ./docs/ --skip emoji,naming
"""

import argparse
import io
import json
import sys
from pathlib import Path
from typing import List

# Ensure UTF-8 output on Windows consoles that default to cp1252 / other codepages.
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )

# Ensure the package root is on sys.path so that `from models import ...`
# works inside rule modules regardless of how the script is invoked.
_PACKAGE_ROOT = Path(__file__).resolve().parent
if str(_PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_PACKAGE_ROOT))

from models import Issue, Severity, ValidationResult  # noqa: E402
from rules import ALL_VALIDATORS  # noqa: E402
from utils import parse_frontmatter  # noqa: E402

# ---------------------------------------------------------------------------
# ANSI color helpers
# ---------------------------------------------------------------------------

_COLORS_ENABLED = sys.stdout.isatty()

_ANSI_RESET = "\033[0m"
_ANSI_RED = "\033[91m"
_ANSI_YELLOW = "\033[93m"
_ANSI_CYAN = "\033[96m"
_ANSI_GREEN = "\033[92m"
_ANSI_BOLD = "\033[1m"
_ANSI_DIM = "\033[2m"


def _color(text: str, code: str) -> str:
    if _COLORS_ENABLED:
        return f"{code}{text}{_ANSI_RESET}"
    return text


def _severity_color(severity: Severity) -> str:
    return {
        Severity.ERROR: _ANSI_RED,
        Severity.WARNING: _ANSI_YELLOW,
        Severity.INFO: _ANSI_CYAN,
    }[severity]


def _severity_label(severity: Severity) -> str:
    return _color(severity.value.upper(), _severity_color(severity))


# ---------------------------------------------------------------------------
# Severity ordering for filtering
# ---------------------------------------------------------------------------

_SEVERITY_ORDER = {
    Severity.ERROR: 0,
    Severity.WARNING: 1,
    Severity.INFO: 2,
}


def _severity_from_str(value: str) -> Severity:
    value = value.strip().lower()
    for s in Severity:
        if s.value == value:
            return s
    raise argparse.ArgumentTypeError(
        f"Invalid severity '{value}'. Choose from: error, warning, info"
    )


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------


def _collect_md_files(target: Path) -> List[Path]:
    """Recursively collect .md files from *target* (file or directory)."""
    if target.is_file():
        if target.suffix.lower() == ".md":
            return [target]
        return []
    if target.is_dir():
        return sorted(target.rglob("*.md"))
    return []


# ---------------------------------------------------------------------------
# Validation pipeline
# ---------------------------------------------------------------------------


def _validate_file(
    file_path: Path,
    validators: list[tuple[str, object]],
) -> ValidationResult:
    """Run all validators on a single file and return the result."""
    content = file_path.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = parse_frontmatter(content)

    all_issues: List[Issue] = []
    for _rule_name, validate_fn in validators:
        try:
            issues = validate_fn(
                file_path=str(file_path),
                content=content,
                frontmatter=frontmatter,
                body=body,
            )
            all_issues.extend(issues)
        except Exception as exc:  # noqa: BLE001
            all_issues.append(Issue(
                rule=_rule_name,
                severity=Severity.ERROR,
                message=f"Validator crashed: {exc}",
            ))

    return ValidationResult(file_path=str(file_path), issues=all_issues)


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------


def _print_text_results(
    results: List[ValidationResult],
    min_severity: Severity,
) -> None:
    """Print human-readable, colorized output."""
    for result in results:
        filtered = [
            i for i in result.issues
            if _SEVERITY_ORDER[i.severity] <= _SEVERITY_ORDER[min_severity]
        ]
        if not filtered:
            continue

        print(f"\n{_color(_ANSI_BOLD + result.file_path, _ANSI_BOLD)}")
        for issue in filtered:
            loc = f":{issue.line}" if issue.line else ""
            label = _severity_label(issue.severity)
            rule_tag = _color(f"[{issue.rule}]", _ANSI_DIM)
            print(f"  {label} {rule_tag} {issue.message}{_color(loc, _ANSI_DIM)}")


def _print_json_results(
    results: List[ValidationResult],
    min_severity: Severity,
) -> None:
    """Print machine-readable JSON output."""
    output = []
    for result in results:
        filtered = [
            i for i in result.issues
            if _SEVERITY_ORDER[i.severity] <= _SEVERITY_ORDER[min_severity]
        ]
        output.append({
            "file": result.file_path,
            "passed": result.passed,
            "issues": [
                {
                    "rule": i.rule,
                    "severity": i.severity.value,
                    "message": i.message,
                    "line": i.line,
                }
                for i in filtered
            ],
        })
    print(json.dumps(output, indent=2, ensure_ascii=False))


def _print_summary(results: List[ValidationResult], min_severity: Severity) -> None:
    """Print a one-line summary."""
    total = len(results)
    passed = sum(1 for r in results if r.passed)

    error_count = sum(
        1 for r in results for i in r.issues if i.severity == Severity.ERROR
    )
    warning_count = sum(
        1 for r in results for i in r.issues if i.severity == Severity.WARNING
    )

    parts = [
        f"{total} file(s) checked",
        _color(f"{passed} passed", _ANSI_GREEN),
    ]
    if error_count:
        parts.append(_color(f"{error_count} error(s)", _ANSI_RED))
    if warning_count and _SEVERITY_ORDER[min_severity] >= _SEVERITY_ORDER[Severity.WARNING]:
        parts.append(_color(f"{warning_count} warning(s)", _ANSI_YELLOW))

    print(f"\n{', '.join(parts)}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="md-validator",
        description="Validate Markdown files against workspace conventions.",
    )
    parser.add_argument(
        "path",
        type=str,
        help="File or directory to validate (directories are searched recursively for *.md)",
    )
    parser.add_argument(
        "--rule",
        type=str,
        default=None,
        help="Only run a specific rule (e.g. frontmatter, heading, emoji)",
    )
    parser.add_argument(
        "--severity",
        type=_severity_from_str,
        default=Severity.WARNING,
        help="Minimum severity to display: error, warning (default), info",
    )
    parser.add_argument(
        "--format",
        dest="output_format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--skip",
        type=str,
        default="",
        help="Comma-separated list of rule names to skip (e.g. emoji,naming)",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print(f"Error: path '{args.path}' does not exist", file=sys.stderr)
        return 1

    md_files = _collect_md_files(target)
    if not md_files:
        print(f"No .md files found in '{args.path}'", file=sys.stderr)
        return 0

    # Build validator list, applying --rule and --skip filters
    skip_set = {s.strip() for s in args.skip.split(",") if s.strip()}
    validators = [
        (name, fn)
        for name, fn in ALL_VALIDATORS
        if (args.rule is None or name == args.rule) and name not in skip_set
    ]

    if not validators:
        print(f"No validators matched (rule={args.rule}, skip={args.skip})", file=sys.stderr)
        return 0

    # Run validation
    results: List[ValidationResult] = []
    for md_file in md_files:
        result = _validate_file(md_file, validators)
        results.append(result)

    # Output
    if args.output_format == "json":
        _print_json_results(results, args.severity)
    else:
        _print_text_results(results, args.severity)
        _print_summary(results, args.severity)

    # Exit code: 1 if any errors found
    has_errors = any(
        i.severity == Severity.ERROR
        for r in results
        for i in r.issues
    )
    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
