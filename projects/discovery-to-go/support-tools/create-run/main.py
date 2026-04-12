#!/usr/bin/env python3
"""
create-run — Discovery Pipeline run scaffold generator.

Creates the full folder structure for a new Discovery Pipeline run,
copying context-templates, customization files, and generating
config.md and pipeline-state.md from briefing frontmatter.

Requires: Python 3.10+, PyYAML
Usage:    python main.py --briefing <path> --client <name> [--project-root <path>]
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(briefing_path: Path) -> dict:
    """Return the YAML frontmatter dict from a markdown file."""
    text = briefing_path.read_text(encoding="utf-8")
    match = _FM_RE.search(text)
    if not match:
        print(f"ERROR: No YAML frontmatter found in {briefing_path}")
        sys.exit(1)
    return yaml.safe_load(match.group(1)) or {}


# ---------------------------------------------------------------------------
# Auto-detect context-templates from briefing content
# ---------------------------------------------------------------------------

def auto_detect_templates(briefing_path: Path, templates_dir: Path) -> list[str]:
    """Scan briefing text for keywords that match available template pack names."""
    text = briefing_path.read_text(encoding="utf-8").lower()
    available = [d.name for d in templates_dir.iterdir() if d.is_dir()]
    detected: list[str] = []
    # Map pack names to search keywords (pack name with hyphens replaced by spaces)
    for pack in available:
        keywords = pack.replace("-", " ").split()
        if all(kw in text for kw in keywords):
            detected.append(pack)
    if not detected:
        print("WARNING: Auto-detect found no matching context-templates. "
              "Falling back to project-type from frontmatter.")
    return detected


# ---------------------------------------------------------------------------
# Run number discovery
# ---------------------------------------------------------------------------

def next_run_number(runs_dir: Path) -> int:
    """Return the next available run number inside runs_dir."""
    if not runs_dir.exists():
        return 1
    existing = [
        int(d.name.removeprefix("run-"))
        for d in runs_dir.iterdir()
        if d.is_dir() and d.name.startswith("run-") and d.name.removeprefix("run-").isdigit()
    ]
    return max(existing, default=0) + 1


# ---------------------------------------------------------------------------
# Folder / file creation helpers
# ---------------------------------------------------------------------------

def ensure_dir(path: Path) -> Path:
    """Create directory (and parents) if it does not exist, then return it."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def copy_file(src: Path, dst: Path) -> None:
    """Copy a single file, creating parent dirs as needed."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def generate_config_md(
    run_dir: Path,
    *,
    project_name: str,
    client: str,
    context_templates: list[str],
    report_setup: str,
    scoring_threshold: str,
    client_simulation: str,
    run_number: int,
    now: datetime,
) -> Path:
    """Generate setup/config.md and return its path."""
    templates_csv = ", ".join(context_templates)
    scoring_label = {
        "padrão": "padrão (>=90%)",
        "alto-risco": "alto-risco (>=95%)",
        "poc": "poc (>=80%)",
    }.get(scoring_threshold, scoring_threshold)

    content = f"""\
---
title: "Run Config — {project_name}"
project-name: {project_name}
version: 01.00.000
status: pendente
author: create-run
category: config
created: {now.strftime('%Y-%m-%d')}
context-templates: [{templates_csv}]
report-setup: {report_setup}
scoring-threshold: {scoring_threshold}
client-simulation: {client_simulation}
iteration: 1
---

# Run Config — {project_name}

| Campo | Valor |
|-------|-------|
| Projeto | {project_name} |
| Cliente | {client} |
| Context-Templates | {templates_csv} |
| Report Setup | {report_setup} |
| Scoring | {scoring_label} |
| Simulacao do cliente | {client_simulation} |
| Iteracao | 1 |
| Inicio | {now.strftime('%Y-%m-%d %H:%M')} |
"""
    path = run_dir / "setup" / "config.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def generate_pipeline_state_md(
    run_dir: Path,
    *,
    project_name: str,
    client: str,
    context_templates: list[str],
    client_simulation: str,
    run_number: int,
    now: datetime,
) -> Path:
    """Generate pipeline-state.md at the run root and return its path."""
    templates_csv = ", ".join(context_templates)
    content = f"""\
---
title: "Pipeline State — {project_name}"
project-name: {project_name}
version: 01.00.000
status: pendente
author: create-run
category: pipeline-state
created: {now.strftime('%Y-%m-%d')}
iteration: 1
pack: {templates_csv}
---

# Pipeline State — {project_name}

## Run Metadata

| Campo | Valor |
|-------|-------|
| Run | run-{run_number} |
| Cliente | {client} |
| Context-Templates | {templates_csv} |
| Inicio | {now.strftime('%Y-%m-%d %H:%M')} |
| Status | Pendente |
| Iteracao | 1 |
| Simulacao do cliente | {client_simulation} |

---

## Estado Atual

- **Fase:** Aguardando inicio
- **Iteracao:** 1
- **Proxima acao:** Executar pipeline

---

## Snapshots

_Nenhum snapshot registrado ainda._
"""
    path = run_dir / "pipeline-state.md"
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Helper functions (append_snapshot / generate_hr_log)
# ---------------------------------------------------------------------------

def append_snapshot(
    pipeline_state_path: Path,
    *,
    phase: str,
    iteration: int,
    status: str,
    notes: str = "",
) -> None:
    """Append a snapshot section to pipeline-state.md.

    Called after each pipeline phase completes to maintain an audit trail.

    Args:
        pipeline_state_path: Absolute path to pipeline-state.md.
        phase: Phase identifier (e.g. "1-discovery", "2-challenge", "3-delivery").
        iteration: Current iteration number.
        status: Outcome status (e.g. "concluido", "reprovado", "aprovado").
        notes: Optional free-text notes about the phase outcome.
    """
    now = datetime.now()
    snapshot = f"""
### Snapshot — {phase} (iteracao {iteration})

| Campo | Valor |
|-------|-------|
| Fase | {phase} |
| Iteracao | {iteration} |
| Status | {status} |
| Timestamp | {now.strftime('%Y-%m-%d %H:%M')} |

{f'**Notas:** {notes}' if notes else ''}
"""
    # Replace the placeholder line if present, otherwise append
    text = pipeline_state_path.read_text(encoding="utf-8")
    placeholder = "_Nenhum snapshot registrado ainda._"
    if placeholder in text:
        text = text.replace(placeholder, snapshot.strip())
        pipeline_state_path.write_text(text, encoding="utf-8")
    else:
        with pipeline_state_path.open("a", encoding="utf-8") as f:
            f.write(snapshot)


def generate_hr_log(
    logs_dir: Path,
    *,
    round_number: int,
    pass_number: int,
    hr_template_path: Path | None = None,
) -> Path:
    """Generate an HR loop log file from the human-review-template.

    Creates ``hr-loop-round{N}-pass{M}.md`` inside the given logs directory,
    substituting ``{N}`` and ``{P}`` placeholders in the template.

    Args:
        logs_dir: Directory where log files are written (e.g. iterations/iteration-1/logs/).
        round_number: Current round (1, 2, or 3).
        pass_number: Pass number within the HR loop (starts at 1).
        hr_template_path: Path to human-review-template.md. If None, looks in the
            standard customization location relative to the run.

    Returns:
        Path to the generated log file.
    """
    ensure_dir(logs_dir)
    filename = f"hr-loop-round{round_number}-pass{pass_number}.md"
    output_path = logs_dir / filename

    if hr_template_path and hr_template_path.exists():
        text = hr_template_path.read_text(encoding="utf-8")
    else:
        # Minimal fallback template
        text = (
            "## Human Review — Round {N} (passagem {P})\n\n"
            "### Observacoes gerais\n\n```\n{suas observacoes aqui}\n```\n\n"
            "### Decisao\n\n- [ ] Re-executar desde a 1a fase.\n"
            "- [ ] Re-executar a ultima fase.\n"
            "- [ ] Avancar para a proxima fase.\n"
            "- [ ] Abortar\n"
        )

    # Extract the HR-LOOP section if markers are present
    loop_start = "<!-- HR-LOOP-START -->"
    loop_end = "<!-- HR-LOOP-END -->"
    if loop_start in text and loop_end in text:
        start_idx = text.index(loop_start) + len(loop_start)
        end_idx = text.index(loop_end)
        text = text[start_idx:end_idx].strip()

    # Substitute placeholders
    text = text.replace("{N}", str(round_number))
    text = text.replace("{P}", str(pass_number))

    now = datetime.now()
    header = f"""\
---
title: "HR Loop — Round {round_number} Pass {pass_number}"
round: {round_number}
pass: {pass_number}
created: {now.strftime('%Y-%m-%d %H:%M')}
status: pendente
---

"""
    output_path.write_text(header + text + "\n", encoding="utf-8")
    return output_path


# ---------------------------------------------------------------------------
# Main scaffold logic
# ---------------------------------------------------------------------------

def discover_project_root(start: Path | None = None) -> Path:
    """Walk up from start (or this script's location) to find the discovery-to-go root."""
    current = start or Path(__file__).resolve().parent
    for _ in range(10):
        if (current / "dtg-artifacts").is_dir() and (current / "base-artifacts").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent
    print("ERROR: Could not locate discovery-to-go project root. "
          "Use --project-root to specify it explicitly.")
    sys.exit(1)


def create_run(
    briefing_path: Path,
    client: str,
    project_root: Path,
) -> None:
    """Create the full run scaffold."""
    now = datetime.now()

    # --- Parse briefing frontmatter ---
    fm = parse_frontmatter(briefing_path)
    project_name: str = fm.get("project-name", briefing_path.stem)
    report_setup: str = fm.get("report-setup", "complete")
    client_simulation: str = fm.get("client-simulation", "sim")
    scoring_threshold: str = fm.get("scoring-threshold", "padrão")
    fm_client: str = fm.get("client", client)
    # Use --client arg as the folder slug, fm client field for display
    client_slug = client.lower().replace(" ", "-")
    client_display = fm_client or client

    # --- Resolve context-templates ---
    templates_base = project_root / "base-artifacts" / "context-templates"
    raw_templates = fm.get("context-templates", "auto-detect")
    if isinstance(raw_templates, str) and raw_templates.strip().lower() == "auto-detect":
        context_templates = auto_detect_templates(briefing_path, templates_base)
        # Fallback to project-type if auto-detect yielded nothing
        if not context_templates:
            pt = fm.get("project-type", "")
            if pt and pt != "generic":
                context_templates = [pt]
    elif isinstance(raw_templates, list):
        context_templates = [str(t).strip() for t in raw_templates]
    elif isinstance(raw_templates, str):
        context_templates = [t.strip() for t in raw_templates.split(",")]
    else:
        context_templates = []

    # --- Determine run number ---
    runs_dir = project_root / "custom-artifacts" / client_slug / "runs"
    run_number = next_run_number(runs_dir)
    run_dir = runs_dir / f"run-{run_number}"

    print(f"Creating run-{run_number} for client '{client_display}' "
          f"(project: {project_name})")
    print(f"  Root: {run_dir}")
    print()

    # --- Create folder structure ---
    dirs_to_create = [
        run_dir / "setup" / "customization" / "current-context",
        run_dir / "setup" / "customization" / "report-templates",
        run_dir / "setup" / "customization" / "rules",
        run_dir / "iterations" / "iteration-1" / "logs",
        run_dir / "iterations" / "iteration-1" / "results" / "1-discovery",
        run_dir / "iterations" / "iteration-1" / "results" / "2-challenge",
        run_dir / "iterations" / "iteration-1" / "results" / "3-delivery",
        run_dir / "delivery",
    ]
    for d in dirs_to_create:
        ensure_dir(d)

    created_files: list[str] = []

    # --- Copy briefing ---
    copy_file(briefing_path, run_dir / "setup" / "briefing.md")
    created_files.append("setup/briefing.md (copy of original)")

    # --- Copy context-templates (blueprints) ---
    for pack in context_templates:
        src = templates_base / pack / "discovery-blueprint.md"
        dst = run_dir / "setup" / "customization" / "current-context" / f"{pack}-discovery-blueprint.md"
        if src.exists():
            copy_file(src, dst)
            created_files.append(f"setup/customization/current-context/{pack}-discovery-blueprint.md")
        else:
            print(f"  WARNING: Blueprint not found: {src}")

    # --- Copy customization files from dtg-artifacts/templates/customization ---
    cust_src = project_root / "dtg-artifacts" / "templates" / "customization"

    # report-templates: final-report-template.md, human-review-template.md
    for fname in ("final-report-template.md", "human-review-template.md"):
        src = cust_src / fname
        if src.exists():
            dst = run_dir / "setup" / "customization" / "report-templates" / fname
            copy_file(src, dst)
            created_files.append(f"setup/customization/report-templates/{fname}")

    # rules: iteration-policy.md, scoring-thresholds.md
    for fname in ("iteration-policy.md", "scoring-thresholds.md"):
        src = cust_src / fname
        if src.exists():
            dst = run_dir / "setup" / "customization" / "rules" / fname
            copy_file(src, dst)
            created_files.append(f"setup/customization/rules/{fname}")

    # html-layout.md
    src = cust_src / "html-layout.md"
    if src.exists():
        dst = run_dir / "setup" / "customization" / "html-layout.md"
        copy_file(src, dst)
        created_files.append("setup/customization/html-layout.md")

    # --- Generate config.md ---
    generate_config_md(
        run_dir,
        project_name=project_name,
        client=client_display,
        context_templates=context_templates,
        report_setup=report_setup,
        scoring_threshold=scoring_threshold,
        client_simulation=client_simulation,
        run_number=run_number,
        now=now,
    )
    created_files.append("setup/config.md (generated)")

    # --- Generate pipeline-state.md ---
    generate_pipeline_state_md(
        run_dir,
        project_name=project_name,
        client=client_display,
        context_templates=context_templates,
        client_simulation=client_simulation,
        run_number=run_number,
        now=now,
    )
    created_files.append("pipeline-state.md (generated)")

    # --- Summary ---
    print("=" * 60)
    print(f"  Run scaffold created: run-{run_number}")
    print(f"  Client:  {client_display} ({client_slug})")
    print(f"  Project: {project_name}")
    print(f"  Templates: {', '.join(context_templates) or '(none)'}")
    print(f"  Report setup: {report_setup}")
    print(f"  Scoring: {scoring_threshold}")
    print(f"  Client simulation: {client_simulation}")
    print("=" * 60)
    print()
    print("Files created:")
    for f in created_files:
        print(f"  + {f}")
    print()
    print("Directories created:")
    for d in dirs_to_create:
        rel = d.relative_to(run_dir)
        print(f"  + {rel}/")
    print()
    print(f"Next step: start the pipeline from {run_dir}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a Discovery Pipeline run scaffold.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python main.py --briefing ../briefing.md --client "Acme Corp"
  python main.py --briefing C:/docs/briefing.md --client acme --project-root E:/Workspace/projects/discovery-to-go
""",
    )
    parser.add_argument(
        "--briefing",
        type=Path,
        required=True,
        help="Path to the briefing .md file (must contain YAML frontmatter).",
    )
    parser.add_argument(
        "--client",
        type=str,
        required=True,
        help="Client name (used as folder slug under custom-artifacts/).",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Path to the discovery-to-go project root. "
             "Auto-discovered if omitted.",
    )

    args = parser.parse_args()

    # Resolve paths
    briefing_path = args.briefing.resolve()
    if not briefing_path.exists():
        print(f"ERROR: Briefing file not found: {briefing_path}")
        sys.exit(1)

    if args.project_root:
        project_root = args.project_root.resolve()
    else:
        project_root = discover_project_root()

    if not (project_root / "dtg-artifacts").is_dir():
        print(f"ERROR: Invalid project root (dtg-artifacts/ not found): {project_root}")
        sys.exit(1)

    create_run(briefing_path, args.client, project_root)


if __name__ == "__main__":
    main()
