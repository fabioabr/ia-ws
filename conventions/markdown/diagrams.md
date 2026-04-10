# Diagrams

Standard for diagrams in Markdown documents.

## Standard

- **Engine:** Mermaid only (no ASCII art)
- **Labels:** max 3 words; emojis when useful for clarity
- **Styling:** use `style` or `classDef` for colors

### Diagram Types

| Type | Use Case |
|---------------------|-------------------------------|
| `flowchart TD/LR` | Processes, workflows |
| `sequenceDiagram` | Interactions between actors |
| `stateDiagram-v2` | Lifecycle, state transitions |
| `gantt` | Timelines, schedules |

## Examples

```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[End]
    style A fill:#4CAF50,color:#fff
```

```mermaid
sequenceDiagram
    User->>System: Request
    System-->>User: Response
```

```mermaid
stateDiagram-v2
    [*] --> Rascunho
    Rascunho --> Ativo
    Ativo --> Arquivado
    Arquivado --> Obsoleto
```

```mermaid
gantt
    title Timeline
    section Phase 1
    Task A :a1, 2026-01-01, 30d
    Task B :after a1, 20d
```
