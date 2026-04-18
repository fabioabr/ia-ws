# Customer

Client simulator skill for Phase 1 (Discovery) of the Discovery Pipeline.

Acts as the project client whenever specialists (po, solution-architect, cyber-security-architect) need answers during the discovery interview. Responds based on the briefing and context-template, tagging every answer with a traceability label:

- `[BRIEFING]` — sourced directly from the briefing
- `[RAG]` — sourced from the context-template
- `[INFERENCE]` — deduced by the skill

Cannot operate without a briefing.

This folder contains `SKILL.md` with the full skill specification.
