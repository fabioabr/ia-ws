# Assets

Assets visuais do cliente usados na geração de reports HTML.

## Logos

Coloque os logos do cliente em `logos/`:

| Arquivo | Uso |
|---------|-----|
| `logos/dark.png` | Logo para tema escuro (header/footer do report) |
| `logos/light.png` | Logo para tema claro |

O html-writer embute os logos como base64 no HTML. Se não houver logos do cliente, usa os logos globais do workspace.
