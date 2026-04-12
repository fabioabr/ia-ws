# Report Setups

Presets de layout para os relatórios HTML do delivery report. Cada setup define um nível de detalhe e quais regions aparecem.

## Setups disponíveis

| Setup | Arquivo | Output | Público-alvo | Regions |
|-------|---------|--------|-------------|---------|
| **Essencial** | `essential.md` | `one-pager.html` | C-level, sponsor, comitê de investimento | ~8 regions |
| **Executivo** | `executive.md` | `one-pager.html` + `executive-report.html` | Diretoria, gestão, PMO | ~20 regions |
| **Completo** | `complete.md` | `one-pager.html` + `executive-report.html` + `full-report.html` | Time técnico, arquiteto, PO, stakeholders | Todas (~85 regions) |

## Como usar

O orchestrator (ou o humano) seleciona o setup durante a Fase 3. O report-planner lê o setup escolhido e gera o report-plan.md adequado.

```yaml
# No config.md da run:
report-setup: executive  # essential | executive | complete
```

O setup pode ser sobrescrito por `custom-artifacts/{client}/templates/customization/html-layout.md` (override total do cliente).
