# Iteration Loop

Rule governing the iteration cycle between phases of the Discovery Pipeline v0.5. Iterations are created through Human Review decisions, with persistent memory and append-only document updates.

## 4 Human Review Decisions

| # | Decision | Effect |
|---|----------|--------|
| 1 | Re-run from Phase 1 (default) | Creates `iteration-{i+1}`, restarts pipeline from Phase 1 |
| 2 | Re-run last phase | Repeats the current phase within the same iteration |
| 3 | Advance to next phase | Moves to Phase N+1 (or final delivery if Phase 3) |
| 4 | Abort | Requires `@` confirmation, terminates pipeline |

## Key Concepts

- **Memory persists across all scenarios** -- regardless of the decision, accumulated context is preserved
- **Unaffected results are inherited** -- when a new iteration is created, unchanged results are copied from the previous iteration
- **Append-only documents** -- from iteration 2 onward, affected documents receive an iteration section (context, changes, new analyses, direction changes) without replacing original content
- **Stagnation detection** -- alerts when context growth falls below threshold (default 10%) for consecutive iterations (default 2)
- **Configurable limits** -- `max-iterations`, `stagnation-threshold`, `hr-loop-default-answer`, and other parameters are set in `iteration-policy.md`
- **Cost awareness** -- re-running from Phase 1 is a full pipeline re-execution; re-running last phase costs only one phase

## File

- [iteration-loop.md](iteration-loop.md) -- Full rule definition (v03.00.000)
