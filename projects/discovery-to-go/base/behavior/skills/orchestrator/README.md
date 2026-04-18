# Orchestrator

Pipeline coordinator skill that manages all phases of the Discovery Pipeline.

Responsibilities include:

- Starting a new discovery pipeline (with or without an existing briefing)
- Processing Human Review returns (re-execute, redo, advance, abort)
- Resuming paused pipelines from `pipeline-state.md`
- Transitioning between phases (Discovery, Challenge, Delivery)
- Invoking custom-specialists during the interview
- Tracking token usage and detecting iteration stagnation

This skill coordinates the other skills but does not perform their work.

This folder contains `SKILL.md` with the full skill specification.
