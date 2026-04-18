# Customization

Overrides de configuração que substituem os defaults de `starter-kit/client-template/templates/customization/`.

## Arquivos disponíveis para override

| Arquivo | O que controla | Default em |
|---------|----------------|-----------|
| `scoring-thresholds.md` | Pisos de nota do auditor e 10th-man por perfil | `starter-kit/client-template/templates/customization/` |
| `iteration-policy.md` | Limites de iteração, threshold de estagnação | `starter-kit/client-template/templates/customization/` |
| `final-report-template.md` | Estrutura/seções do delivery report (override total) | `starter-kit/client-template/templates/customization/` |
| `human-review-template.md` | Formato do formulário de Human Review | `starter-kit/client-template/templates/customization/` |
| `html-layout.md` | Quais regions aparecem no HTML, ordem e layout | `starter-kit/client-template/templates/customization/` |

## Como funciona

Copie o arquivo default, modifique o que precisa. O orchestrator detecta que o arquivo existe aqui e usa no lugar do default.

Exemplo: para mudar os pisos de nota do auditor:
```bash
cp ../../starter-kit/client-template/templates/customization/scoring-thresholds.md .
# edite scoring-thresholds.md com os valores do cliente
```
