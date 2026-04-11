# Rules

Pipeline behavior rules for Discovery-to-Go. These rules govern how the pipeline operates across all phases and iterations.

| Rule | Description |
|------|-------------|
| [analyst-discovery-log](analyst-discovery-log/) | Defines the interview log format (`interview.md`) for Phase 1 -- table-based dialogue with emoji personas and source tags |
| [audit-log](audit-log/) | Chronological audit trail logging -- each auditor generates a log, the orchestrator consolidates into a final report |
| [custom-artifacts-priority](custom-artifacts-priority/) | Priority chain for loading configs, KB, assets and rules: Custom (client) > Pipeline (project) > Base (workspace) |
| [discovery](discovery/) | Core discovery process with 3 sequential phases (Discovery, Challenge, Delivery), 8 thematic blocks, and Human Review gates |
| [iteration-loop](iteration-loop/) | Iteration cycle management -- limits, convergence detection, stagnation alerts, and the 4 Human Review decisions |
| [requirement-priority](requirement-priority/) | Requirement classification and prioritization using signal-based detection (emotional emphasis, pain, repetition) with mandatory/important/desirable levels |
| [token-tracking](token-tracking/) | Token consumption tracking per agent, phase, and iteration for cost analysis and efficiency monitoring |
