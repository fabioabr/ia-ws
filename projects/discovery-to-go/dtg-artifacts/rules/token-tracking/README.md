# Token Tracking

Mandatory rule for recording token consumption across all AI agent processes. Token usage is a direct indicator of operational cost and must be tracked for efficiency analysis and budgeting.

## Metrics Tracked

| Metric | Description |
|--------|-------------|
| Total tokens | Input + output tokens consumed by the agent |
| Tool uses | Number of tool calls (reads, writes, edits, etc.) |
| Duration | Total execution time |
| Documents generated | Number of output files produced |

## Where to Record

- **Agent logs** -- "Resource Consumption" section before changelog in every process log
- **Consolidated reports** -- per-agent breakdown table (tokens, tools, duration, docs) with totals
- **Pipeline state** -- cumulative consumption across all phases and iterations in `pipeline-state.md`

## Key Concepts

- **Approximate values are acceptable** -- prefix with `~`; never fabricate numbers
- **Never omit the section** -- if exact data is unavailable, record "not available"
- **Cost estimation** -- the pipeline state includes estimated cost based on model pricing (input/output token rates)
- **Real-world benchmarks** -- a full pipeline run (3 phases) typically consumes 300-400k tokens, estimated at $5-15 per discovery

## File

- [token-tracking.md](token-tracking.md) -- Full rule definition (v01.03.000)
