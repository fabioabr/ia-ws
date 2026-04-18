# Config

Configurações gerais do cliente que não se encaixam em rules ou templates.

## Exemplos

| Arquivo | O que contém |
|---------|-------------|
| `client-info.md` | Nome do cliente, contato, setor, restrições gerais |
| `confidentiality.md` | Nível de confidencialidade, NDAs, restrições de distribuição |
| `delivery-preferences.md` | Preferências de formato, idioma, nível de detalhe |

## Flags do run (`runs/run-{n}/setup/config.md`)

Além dos arquivos acima (nível cliente), cada run tem um `config.md` próprio gerado pelo Setup a partir do `briefing.md`. Esse `config.md` materializa os flags declarados pelo humano na seção 9 do briefing em frontmatter legível por máquina:

```yaml
---
financial_model: "projeto-paga"    # ou "fundo-global"
require_roi: false                 # ou true
deliverables_scope: ["DR"]         # ou ["DR","OP"] / ["DR","EX"] / ["DR","OP","EX"]
threshold: "padrao"                # "alto-risco" | "padrao" | "poc"
simulacao-cliente: true
---
```

Skills do pipeline (po, solution-architect, auditor, pipeline-md-writer, deliverable-distiller) leem **sempre do config.md**, nunca diretamente do briefing — isso garante que mudanças pontuais no run não exijam editar o briefing original.

Ver [[rules/discovery]] seção "Flags de configuração" para semântica completa.

## Como é usado

O orchestrator lê esses arquivos durante o Setup e os disponibiliza para todos os agentes ao longo do pipeline.
