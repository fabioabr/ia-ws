# Client Template

Template de scaffold para customizações de um cliente. Para criar uma pasta de cliente, copie este template:

```bash
cp -r _client-template/ {client-name}/
```

Depois preencha as pastas com os artefatos específicos do cliente.

## Estrutura

```
{client-name}/
├── kb/                        ← Knowledge base do cliente
├── assets/                    ← Assets visuais
│   └── logos/                 ← Logos do cliente (dark.png, light.png)
├── rules/                     ← Regras adicionais
├── templates/                 ← Overrides de templates
│   └── customization/         ← Scoring, iteration, report, layout
└── config/                    ← Overrides de configuração
```

## Prioridade

Esta é a **camada 3** (maior prioridade). Conteúdo aqui sobrescreve:
- `dtg-artifacts/` (camada 2 — Pipeline)
- `base-artifacts/` (camada 1 — Base)
