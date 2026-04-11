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

## Representação Visual

### Dados de amostra

| Mês | Investimento Acumulado | Receita Acumulada |
|-----|----------------------|-------------------|
| 0 | R$ 0 | R$ 0 |
| 3 | R$ 195.000 | R$ 45.000 |
| 6 | R$ 390.000 | R$ 165.000 |
| 9 | R$ 585.000 | R$ 390.000 |
| 12 | R$ 720.000 | R$ 630.000 |
| 14 | R$ 780.000 | R$ 795.000 |
| 18 | R$ 850.000 | R$ 1.100.000 |

Break-even no mês 14: investimento acumulado de R$ 780.000 cruzado pela receita acumulada de R$ 795.000. Confiança: Média.

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Line chart com crossover
**Tecnologia:** Chart.js
**Justificativa:** Duas linhas (investimento acumulado vs. receita acumulada) convergindo e cruzando no mês 14 comunicam instantaneamente o ponto de equilíbrio — é o formato canônico para break-even analysis. A anotação no ponto de interseção e o preenchimento da área entre as curvas reforçam a mensagem sem poluir o gráfico.
**Alternativa:** Tabela (HTML/CSS) — quando o público precisa dos valores exatos mês a mês para validação das premissas
