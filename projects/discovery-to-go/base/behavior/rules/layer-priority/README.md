# Layer Priority

Rule defining the priority chain for loading configurations, knowledge base, assets, and rules. Client project overrides always take precedence over base defaults.

## Priority Chain

```
1. projects/{client}/    <-- highest (client customizations)
2. base/starter-kit/     <-- fallback (project templates)
3. base/                 <-- fallback (standards, behavior, assets)
```

## Key Concepts

- **Configs** -- client `scoring-thresholds.md`, `iteration-policy.md`, report and HR templates override base defaults
- **Knowledge base** -- client KB complements (not replaces) base blueprints; conflicts resolved in favor of the client
- **Assets** -- client logo and visual templates take precedence over base assets
- **Rules** -- client rules are additive (they add restrictions on top of base rules), unless explicitly declared as overrides via `overrides:` frontmatter
- **Orchestrator applies at setup** -- reads `client` from briefing frontmatter, checks for `projects/{client}/`, loads in priority order

## File

- [layer-priority.md](layer-priority.md) -- Full rule definition
