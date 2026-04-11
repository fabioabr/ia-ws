---
region-id: REG-METR-01
title: "Business KPIs"
group: metrics
description: "Key business performance indicators with current values, targets, and deadlines"
source: "Bloco #3 (po) → 1.3"
schema: "Tabela (KPI, valor atual, target, prazo)"
template-visual: "Stat cards ou table"
default: true
---

# Business KPIs

Define os indicadores-chave de performance de negocio que o projeto deve impactar. Cada KPI inclui o valor atual (baseline), o target desejado e o prazo. Estes indicadores sao a principal forma de medir se o projeto esta entregando valor de negocio.

## Schema de dados

```yaml
business_kpis:
  kpis:
    - id: string                 # Identificador (ex: BK-01)
      name: string               # Nome do KPI
      current_value: string      # Valor atual (baseline)
      target: string             # Valor alvo
      deadline: string           # Prazo para atingir o target
      unit: string               # Unidade de medida
      direction: string          # up (quanto maior melhor) / down (quanto menor melhor)
```

## Exemplo

| ID | KPI | Valor Atual | Target | Prazo | Direcao |
|----|-----|------------|--------|-------|---------|
| BK-01 | MRR (Monthly Recurring Revenue) | R$ 0 | R$ 50.000 | Mes 12 | up |
| BK-02 | Numero de clientes pagantes | 0 | 300 | Mes 12 | up |
| BK-03 | Churn mensal | N/A | < 3% | Mes 6 pos-lancamento | down |
| BK-04 | NPS (Net Promoter Score) | N/A | >= 50 | Mes 6 pos-lancamento | up |
| BK-05 | CAC (Custo de Aquisicao de Cliente) | N/A | < R$ 200 | Mes 9 | down |
| BK-06 | LTV/CAC ratio | N/A | >= 3:1 | Mes 12 | up |

## Representacao Visual

### Dados de amostra

```
MRR:        R$ 0 → R$ 50.000 (Mes 12)         ████░░░░░░ 0%
Clientes:   0 → 300 (Mes 12)                   ████░░░░░░ 0%
Churn:      N/A → < 3% (Mes 6 pos-lancamento)  ░░░░░░░░░░ N/A
NPS:        N/A → >= 50 (Mes 6 pos-lancamento)  ░░░░░░░░░░ N/A
CAC:        N/A → < R$ 200 (Mes 9)             ░░░░░░░░░░ N/A
LTV/CAC:    N/A → >= 3:1 (Mes 12)              ░░░░░░░░░░ N/A
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo descritivo com os KPIs destacados em negrito | Relatorios textuais simples, contexto narrativo |
| Tabela | Tabela estruturada com colunas ID, KPI, Valor Atual, Target, Prazo, Direcao | Visao completa e comparativa de todos os KPIs |
| Stat cards com sparklines | Cards individuais por KPI mostrando valor atual, target e tendencia ao longo do tempo | Dashboards executivos, acompanhamento periodico |
| Gauge (velocimetro) | Indicador circular mostrando progresso percentual em direcao ao target | Apresentacoes de status, visao rapida de progresso individual |
| Stat cards + gauge combinado | Cards com valor numerico e gauge embutido para cada KPI | Relatorios visuais ricos, paineis de acompanhamento |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
