# Discovery

Core rule defining the mandatory 3-phase discovery process that precedes any project work. The pipeline runs sequentially through Discovery, Challenge, and Delivery, with a Human Review gate after each phase.

## 3 Phases

| Phase | Name | Purpose |
|-------|------|---------|
| 1 | **Discovery** | Joint thematic meeting with 8 blocks -- produces 8 result files + interview log |
| 2 | **Challenge** | Parallel convergent (auditor) + divergent (10th-man) validation of Phase 1 drafts |
| 3 | **Delivery** | Document polishing, consolidation, and HTML report generation |

## 8 Thematic Blocks (Phase 1)

| Block | Theme | Owner |
|-------|-------|-------|
| #1 | Vision and Purpose | po |
| #2 | Personas and Journey | po |
| #3 | Expected Value / OKRs | po |
| #4 | Process, Business and Team | po |
| #5 | Technology and Security | solution-architect |
| #6 | LGPD and Privacy | cyber-security-architect |
| #7 | Macro Architecture | solution-architect |
| #8 | TCO and Build vs Buy | solution-architect |

## Key Concepts

- **Human Review after each phase** -- 4 options: re-run from Phase 1 (default), re-run last phase, advance, or abort
- **Budget is output, not input** -- the process calculates TCO as a result; it does not start from a pre-defined budget
- **Context-templates** -- domain packs (SaaS, datalake, web-microservices, etc.) provide specialized questions and checklists
- **Fixed timeline** -- 1 month planning + 6 months MVP development

## File

- [discovery.md](discovery.md) -- Full rule definition (v04.00.000)
