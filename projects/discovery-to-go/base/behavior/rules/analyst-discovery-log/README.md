# Analyst Discovery Log

Mandatory rule for generating the interview log (`interview.md`) during Phase 1 (Discovery). The log records the joint thematic meeting between specialist agents and the customer using a table-based dialogue format with emoji-identified personas.

## Key Concepts

- **One log per iteration** -- the entire Phase 1 is recorded in a single `interview.md` file
- **Table dialogue format** -- two-column tables (`Who | Dialogue`) with emoji + agent name per turn
- **Source tags** -- every customer response is prefixed with `[BRIEFING]`, `[INFERENCE]`, or `[RAG]` to indicate information origin
- **Callouts between tables** -- warnings for inferred data, danger for risks, info for decisions
- **8 thematic blocks** -- each block has a header, dialogue tables, completion marker, and summary table
- **Append-only** -- entries are never edited; corrections are logged as new entries
- **Global summary** -- block status table and metrics (duration, source distribution, conflicts, risks) at the end

## File

- [analyst-discovery-log.md](analyst-discovery-log.md) -- Full rule definition (v04.00.000)
