# Auditor

Convergent validation skill for Phase 2 (Challenge) of the Discovery Pipeline.

Audits the 8 discovery blocks (1.1--1.8) against 5 weighted dimensions:

1. Completude (completeness)
2. Fundamentacao (evidence grounding)
3. Coerencia (coherence)
4. Profundidade (depth)
5. Neutralidade (neutrality)

Each dimension has a minimum floor. The final output is `2.1-convergent-validation.md` with a score (0--100%) and a verdict of APPROVED or REJECTED. Runs in parallel with the 10th-man gate, with no dependency between them.

This folder contains `SKILL.md` with the full skill specification.
