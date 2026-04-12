# Customization

Overrides de configuração que substituem os defaults de `dtg-artifacts/templates/customization/`.

## Arquivos disponíveis para override

| Arquivo | O que controla | Default em |
|---------|----------------|-----------|
| `scoring-thresholds.md` | Pisos de nota do auditor e 10th-man por perfil | `dtg-artifacts/templates/customization/` |
| `iteration-policy.md` | Limites de iteração, threshold de estagnação | `dtg-artifacts/templates/customization/` |
| `final-report-template.md` | Estrutura/seções do delivery report (override total) | `dtg-artifacts/templates/customization/` |
| `human-review-template.md` | Formato do formulário de Human Review | `dtg-artifacts/templates/customization/` |
| `html-layout.md` | Quais regions aparecem no HTML, ordem e layout | `dtg-artifacts/templates/customization/` |

## Como funciona

Copie o arquivo default, modifique o que precisa. O orchestrator detecta que o arquivo existe aqui e usa no lugar do default.

Exemplo: para mudar os pisos de nota do auditor:
```bash
cp ../../dtg-artifacts/templates/customization/scoring-thresholds.md .
# edite scoring-thresholds.md com os valores do cliente
```
