# Audit Log

Mandatory rule for chronological logging of every audit process. Each specialized auditor generates its own log, and the orchestrator consolidates all logs into a final audit report.

## Key Concepts

- **Per-auditor logs** -- each agent produces an independent `auditor-log.md` in `logs/`
- **Consolidated report** -- the `auditor` agent generates `2.1-convergent-validation.md` in `results/2-challenge/`
- **9 entry types** -- Start, Verification, Approved, Failure, Observation, Recommendation, Conflict, Calculation, Conclusion
- **Scoring scale** -- 0-100% per audit dimension, weighted average for the final score
- **Severity thresholds** -- 90-100% approved, 70-89% with caveats, 50-69% rejected, 0-49% critical rejection
- **Append-only** -- entries are never edited; every check is logged with explicit pass/fail and justification
- **Evidence required** -- an audit that says "all OK" without evidence is invalid

## File

- [audit-log.md](audit-log.md) -- Full rule definition (v01.03.000)
