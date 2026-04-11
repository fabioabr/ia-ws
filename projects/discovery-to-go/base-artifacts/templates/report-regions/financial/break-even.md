---
region-id: REG-FIN-02
title: "Break-Even Analysis"
group: financial
description: "Point in time where cumulative revenue exceeds cumulative investment"
source: "Bloco #8 (arch) → 1.8"
schema: "Texto + número + premissas"
template-visual: "KPI card + callout"
default: false
---

# Break-Even Analysis

Identifica o momento em que a receita acumulada (ou economia gerada) supera o investimento acumulado. Este indicador e fundamental para justificar o projeto e definir expectativas de retorno. As premissas subjacentes sao explicitadas para permitir revisao critica.

## Schema de dados

```yaml
break_even:
  months_to_break_even: number   # Meses ate o ponto de equilibrio
  cumulative_investment: number   # Investimento total ate o break-even (BRL)
  cumulative_revenue: number     # Receita acumulada no break-even (BRL)
  confidence: string             # Alta / Media / Baixa
  assumptions:
    - description: string        # Premissa
      impact: string             # Impacto se incorreta
```

## Exemplo

**Break-even estimado: 14 meses** apos o lancamento do FinTrack Pro SaaS.

- Investimento acumulado ate o break-even: R$ 780.000
- Receita acumulada no mes 14: R$ 795.000
- Confianca: Media

**Premissas:**
- Conversao de trial para pago de 12% (se cair para 8%, break-even sobe para 19 meses)
- Ticket medio de R$ 149/mes no plano Professional
- Churn mensal de 3%
