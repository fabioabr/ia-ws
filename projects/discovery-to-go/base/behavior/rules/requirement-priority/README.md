# Requirement Priority

Rule for classifying and prioritizing requirements based on the requester's intent and emphasis. Ensures the primary requirement is never ignored or downgraded by the AI.

## Classification Levels

| Level | Signal Examples | Meaning |
|-------|----------------|---------|
| Mandatory | Emotional emphasis, explicit pain, repetition, direct prioritization | Must be addressed -- solution is wrong if it doesn't meet this |
| Important | Description of ideal outcome | Likely mandatory -- needs validation |
| Desirable | Casual mention, "nice to have" | Can be deferred |

## Key Concepts

- **Signal-based detection** -- the AI identifies priority through indirect cues (emotion, frustration, repetition), not just explicit statements
- **Anti-pattern: translating the request** -- the AI must not replace the requester's actual need with a different solution it knows better
- **Mandatory requirements are non-negotiable** -- if the proposed solution does not meet a mandatory requirement, the solution must be revised
- **Inviability protocol** -- when a mandatory requirement is technically or financially infeasible, the AI must inform transparently with data, present alternatives with coverage percentages, and let the requester decide
- **Explicit classification table** -- during Phase 1 (blocks #1-#4), every requirement gets a row with signal, classification, and solution compliance status

## File

- [requirement-priority.md](requirement-priority.md) -- Full rule definition (v01.00.002)
