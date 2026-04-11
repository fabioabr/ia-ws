# Templates

Artifact templates used by the orchestrator during project scaffold and pipeline execution.

| Template | Used by | Purpose |
|----------|---------|---------|
| `briefing-template.md` | Orchestrator (setup) | Initial briefing the human client fills before Phase 1 |
| `iteration-setup-template.md` | Orchestrator (each iteration) | Iteration plan with objectives, loaded context, and focus |
| `audit-report-template.md` | Auditor (Phase 2) | Convergent validation report with 5 weighted dimensions |
| `challenge-report-template.md` | 10th-man (Phase 2) | Divergent validation report with 3 weighted dimensions |
| `change-request-template.md` | Orchestrator (HR loop) | Change request compiled when a Human Review is rejected |

The `customization/` subfolder contains tunable defaults that projects can override locally.
