# Templates

Templates de artefatos e configurações do Discovery Pipeline.

## Estrutura

```
templates/
├── draft-templates/          ← templates de artefatos do pipeline
│   ├── briefing-template.md
│   ├── audit-report-template.md
│   ├── challenge-report-template.md
│   ├── change-request-template.md
│   └── iteration-setup-template.md
├── customization/            ← defaults customizáveis por run
│   ├── final-report-template.md
│   ├── human-review-template.md
│   ├── html-layout.md
│   ├── iteration-policy.md
│   └── scoring-thresholds.md
└── report-setups/            ← presets de nível de detalhe do HTML
    ├── essential.md          ← One-Pager (8 regions)
    ├── executive.md          ← One-Pager + Executive Report (28 regions)
    └── complete.md           ← One-Pager + Executive + Full Report (90 regions)
```

## Draft Templates

Templates usados pelo orchestrator ao criar o scaffold da run e pelos agentes ao gerar artefatos.

| Template | Usado por | Quando |
|----------|-----------|--------|
| `briefing-template.md` | Humano | Criar o briefing inicial |
| `audit-report-template.md` | Auditor | Gerar relatório de validação convergente |
| `challenge-report-template.md` | 10th-man | Gerar relatório de validação divergente |
| `change-request-template.md` | Orchestrator | Registrar change requests entre iterações |
| `iteration-setup-template.md` | Orchestrator | Configurar cada nova iteração |

## Customization

Defaults que podem ser sobrescritos por `custom-artifacts/{client}/templates/customization/`.

| Arquivo | O que controla |
|---------|----------------|
| `scoring-thresholds.md` | Pisos de nota do auditor e 10th-man |
| `iteration-policy.md` | Limites de iteração, threshold de estagnação |
| `final-report-template.md` | Estrutura base do delivery report (11 seções) |
| `human-review-template.md` | Formato do formulário de Human Review |
| `html-layout.md` | Quais regions aparecem no HTML, ordem e layout |

## Report Setups

Presets que definem o nível de detalhe dos HTMLs gerados.

| Setup | HTMLs gerados | Regions | Público |
|-------|--------------|---------|---------|
| **essential** | `one-pager.html` | 8 | C-level, sponsor |
| **executive** | `one-pager.html` + `executive-report.html` | 28 | Diretoria, gestão |
| **complete** | `one-pager.html` + `executive-report.html` + `full-report.html` | 90 | Time técnico, PO |
