# Orchestrator Workspace

Workspace and evaluation data for the orchestrator skill.

Contains `trigger-eval.json` — a set of 20 test queries (10 positive, 10 negative) used to validate whether a user prompt should trigger the orchestrator. Positive cases cover pipeline start, HR loop processing, resume, phase transitions, abort, stagnation, and state generation. Negative cases cover tasks that belong to other skills (po, auditor, 10th-man, html-writer, md-writer, etc.).
