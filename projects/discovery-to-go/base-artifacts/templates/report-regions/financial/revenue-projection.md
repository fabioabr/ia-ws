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
