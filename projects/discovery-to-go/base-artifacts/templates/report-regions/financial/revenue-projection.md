---
region-id: REG-FIN-04
title: "Revenue Projection"
group: financial
description: "Monthly and annual revenue forecast for SaaS or product-based projects"
source: "Bloco #3/#8"
schema: "Tabela projeção mensal/anual"
template-visual: "Table ou line chart"
default: false
---

# Revenue Projection

Projeta a receita esperada ao longo do tempo, baseada em premissas de aquisicao, conversao e ticket medio. Esta regiao e ativada principalmente em projetos SaaS ou de produto, onde existe um modelo de receita direta. Permite validar a viabilidade comercial do projeto.

## Schema de dados

```yaml
revenue_projection:
  model: string                  # Tipo (subscription, usage-based, hybrid)
  currency: string               # BRL
  monthly:
    - month: number              # Mes (1-12)
      new_customers: number
      total_customers: number
      mrr: number                # Monthly Recurring Revenue
      churn_rate: number         # % churn no mes
  annual_summary:
    - year: number
      arr: number                # Annual Recurring Revenue
      total_revenue: number
      growth_rate: number        # % crescimento YoY
  assumptions: string[]
```

## Exemplo

| Mes | Novos Clientes | Base Total | MRR | Churn |
|-----|---------------|------------|-----|-------|
| 1 | 20 | 20 | R$ 2.980 | 0% |
| 3 | 35 | 78 | R$ 11.622 | 3% |
| 6 | 50 | 185 | R$ 27.565 | 3% |
| 12 | 60 | 420 | R$ 62.580 | 2,5% |

**Resumo anual:**
- Ano 1: ARR estimado de R$ 750.960
- Ano 2: ARR estimado de R$ 1.876.000 (+150%)
- Ano 3: ARR estimado de R$ 3.500.000 (+87%)

**Premissas:** ticket medio de R$ 149/mes; churn estabiliza em 2,5% apos mes 9; 70% plano Professional, 30% plano Starter.

## Representação Visual

### Dados de amostra

| Mês | Novos Clientes | Base Total | MRR |
|-----|---------------|------------|-----|
| 1 | 20 | 20 | R$ 2.980 |
| 3 | 35 | 78 | R$ 11.622 |
| 6 | 50 | 185 | R$ 27.565 |
| 12 | 60 | 420 | R$ 62.580 |

Resumo anual: Ano 1 ARR R$ 750.960 — Ano 2 ARR R$ 1.876.000 (+150%) — Ano 3 ARR R$ 3.500.000 (+87%).

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Line chart
**Tecnologia:** Chart.js
**Justificativa:** A progressão mensal do MRR é uma série temporal contínua com tendência de crescimento — o line chart é o formato nativo para esse tipo de dado, permitindo identificar a curva de aceleração, pontos de inflexão e projetar visualmente a trajetória futura. Marcadores nos meses-chave (1, 3, 6, 12) reforçam os marcos de receita.
**Alternativa:** Area chart (Chart.js) — quando houver segmentação por plano (Professional vs Starter) e o objetivo for mostrar a composição da receita ao longo do tempo
