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

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo a trajetória de receita, premissas de crescimento e marcos de ARR por ano | Comunicação com stakeholders não-técnicos onde o storytelling financeiro é prioritário |
| Tabela | Matriz mês a mês com novos clientes, base total, MRR e churn, como no exemplo acima | Quando o leitor precisa dos números exatos para cada período e quer fazer suas próprias análises |
| Line chart | Linha mostrando a evolução do MRR ao longo dos meses, com marcadores nos marcos principais | Visualizar a curva de crescimento da receita e identificar pontos de inflexão |
| Area chart | Área preenchida sob a curva de MRR, opcionalmente segmentada por plano (Professional vs Starter) | Enfatizar o volume acumulado de receita e a composição por plano ao longo do tempo |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
