# Custom Artifacts Priority

Rule defining the priority chain for loading configurations, knowledge base, assets, and rules. Client custom-artifacts always override pipeline defaults and workspace globals.

## Priority Chain

```
1. custom-artifacts/{client}/    <-- highest (client)
2. templates/                    <-- fallback (pipeline/project)
3. E:\Workspace/                 <-- fallback (global workspace)
```

## Key Concepts

- **Configs** -- client `scoring-thresholds.md`, `iteration-policy.md`, report and HR templates override pipeline defaults
- **Knowledge base** -- client KB complements (not replaces) global context-templates; conflicts resolved in favor of the client
- **Assets** -- client logo and visual templates take precedence over pipeline and workspace assets
- **Rules** -- client rules are additive (they add restrictions on top of pipeline rules), unless explicitly declared as overrides via `overrides:` frontmatter
- **Orchestrator applies at setup** -- reads `client` from briefing frontmatter, checks for `custom-artifacts/{client}/`, loads in priority order

## File

- [custom-artifacts-priority.md](custom-artifacts-priority.md) -- Full rule definition (v01.00.000)
