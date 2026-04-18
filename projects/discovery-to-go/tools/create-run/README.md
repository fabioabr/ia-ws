# create-run

Automates the creation of a Discovery Pipeline run scaffold under `custom-artifacts/{client}/runs/run-{N}/`.

## Requirements

- Python 3.10+
- PyYAML (`pip install pyyaml`)

## Usage

```bash
python main.py --briefing <path-to-briefing.md> --client <client-name> [--project-root <path>]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--briefing` | Yes | Path to the briefing `.md` file. Must contain YAML frontmatter between `---` markers. |
| `--client` | Yes | Client name. Used as the folder slug under `custom-artifacts/` (lowercased, spaces replaced with hyphens). |
| `--project-root` | No | Path to the `discovery-to-go` project root. If omitted, the script walks up from its own location to find it. |

### Examples

```bash
# From the create-run directory (auto-discovers project root)
python main.py --briefing ../../custom-artifacts/acme/start/briefing.md --client "Acme Corp"

# Explicit project root (useful from any working directory)
python main.py --briefing C:\docs\briefing.md --client acme --project-root E:\Workspace\projects\discovery-to-go
```

## What it does

1. **Parses briefing frontmatter** to extract configuration:
   - `context-templates` — list of template packs, or `"auto-detect"`
   - `deliverables_scope` — **canonical** — list containing any of `DR`, `OP`, `EX` (default derived from `report-setup`)
   - `report-setup` — **legacy alias** — `essential` / `executive` / `complete` (default: `complete`). Mapping:
     - `essential` → `["DR", "OP"]`
     - `executive` → `["DR", "OP", "EX"]`
     - `complete` → `["DR", "OP", "EX"]`
   - `client-simulation` — `sim` / `nao` (default: `sim`)
   - `scoring-threshold` — `padrao` / `alto-risco` / `poc` (default: `padrao`)
   - `project-name`, `client`

   > If `deliverables_scope` is present, it wins. `report-setup` is used only as fallback.

2. **Auto-increments the run number** by scanning existing `run-*` folders.

3. **Creates the full folder structure:**

```
custom-artifacts/{client}/runs/run-{N}/
├── setup/
│   ├── briefing.md              (copy of original)
│   ├── config.md                (generated from frontmatter)
│   └── customization/
│       ├── current-context/     (discovery blueprints copied here)
│       ├── report-templates/    (final-report-template, human-review-template)
│       ├── rules/               (iteration-policy, scoring-thresholds)
│       └── html-layout.md
├── iterations/
│   └── iteration-1/
│       ├── logs/
│       └── results/
│           ├── 1-discovery/
│           ├── 2-challenge/
│           └── 3-delivery/
├── delivery/
└── pipeline-state.md            (generated with initial metadata)
```

4. **Copies context-template blueprints** for each listed pack (e.g., `saas`, `ai-ml`) from `base-artifacts/context-templates/{pack}/discovery-blueprint.md` into `current-context/{pack}-discovery-blueprint.md`.

5. **Generates `config.md`** with all run parameters in frontmatter and a summary table.

6. **Generates `pipeline-state.md`** with run metadata and an empty snapshots section.

## Helper functions

The script also exposes two helper functions for use by other tooling or pipeline orchestration:

### `append_snapshot()`

Appends a phase-completion snapshot to `pipeline-state.md`.

```python
from main import append_snapshot
append_snapshot(
    pipeline_state_path,
    phase="1-discovery",
    iteration=1,
    status="concluido",
    notes="All 8 blocks completed successfully.",
)
```

### `generate_hr_log()`

Generates an HR loop log file (`hr-loop-round{N}-pass{M}.md`) from the human-review-template, substituting `{N}` and `{P}` placeholders.

```python
from main import generate_hr_log
generate_hr_log(
    logs_dir=Path("iterations/iteration-1/logs"),
    round_number=1,
    pass_number=1,
    hr_template_path=Path("setup/customization/report-templates/human-review-template.md"),
)
```
