# Consolidator

Content consolidation skill for Phase 3 (Delivery) of the Discovery Pipeline.

Runs after the pipeline-md-writer has polished the individual Markdown documents. Reads all approved results, pipeline state, and logs, then generates `delivery/delivery-report.md` containing an executive overview (one-pager) plus thematic sections. After consolidation, invokes the global html-writer to produce `delivery/delivery-report.html`.

This folder contains `SKILL.md` with the full skill specification.
