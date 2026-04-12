# min-rag

Minimal RAG (Retrieval-Augmented Generation) configuration for client customization.

This folder holds the smallest viable knowledge base a client needs to provide so the Discovery Pipeline can retrieve relevant context during a run. It serves as a lightweight alternative to a full `custom-artifacts/{client}/kb/` setup when the client has limited documentation available.

## Usage

Copy this folder into `custom-artifacts/{client-name}/` and populate the files with client-specific content. The orchestrator loads them as additional context for agents during Phase 1.

## Related

- `custom-artifacts/README.md` — Full guide on client customization structure
- `docs/guides/quick-start.md` — How to start a pipeline run
