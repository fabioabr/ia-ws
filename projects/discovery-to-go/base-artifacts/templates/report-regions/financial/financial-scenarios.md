---
region-id: REG-FIN-07
title: "Financial Scenarios"
group: financial
description: "Cenários financeiros alternativos quando o cenário base é inviável — comparativo de TCO, receita, break-even"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela comparativa + bar chart"
template-visual: "Table + Chart.js grouped bar"
default: false
---

# Financial Scenarios

Cenarios financeiros alternativos gerados quando a receita projetada nao cobre o TCO em 3 anos. O solution-architect deve produzir pelo menos 3 cenarios que tornem o projeto viavel, cada um com TCO revisado, receita projetada, break-even e veredicto. A tabela comparativa permite ao decisor avaliar trade-offs entre cenarios.

## Schema de dados

```yaml
financial_scenarios:
  base_scenario:
    name: string                    # Nome do cenário base
    tco_3y: number                  # TCO 3 anos (BRL)
    revenue_3y: number              # Receita projetada 3 anos (BRL)
    break_even_months: number|null  # Meses até break-even (null se inviável)
    verdict: string                 # viável / viável com ressalvas / inviável
  alternative_scenarios:
    - name: string                  # Nome do cenário alternativo
      description: string           # Descrição em 1 frase
      what_changes: string          # O que muda em relação ao cenário base
      tco_3y: number                # Novo TCO 3 anos (BRL)
      revenue_3y: number            # Nova receita projetada 3 anos (BRL)
      break_even_months: number     # Novo break-even (meses)
      risks: string                 # Riscos introduzidos pela mudança
      verdict: string               # viável / viável com ressalvas / inviável
```

## Exemplo

Projeto **FinTrack Pro** — cenario base inviavel (receita R$ 1.8M < TCO R$ 2.4M em 3 anos). Tres cenarios alternativos gerados pelo solution-architect:

| Cenário | TCO 3 anos | Receita 3 anos | Break-even | Veredicto |
|---------|-----------|----------------|------------|-----------|
| **Base** — stack completa, time de 4, pricing atual | R$ 2.400.000 | R$ 1.800.000 | — (não atinge) | Inviável |
| **A — Ajuste de pricing** — Professional de R$ 149 para R$ 199/mês | R$ 2.400.000 | R$ 2.520.000 | 28 meses | Viável com ressalvas |
| **B — Redução de escopo MVP** — cortar módulo de relatórios avançados | R$ 1.750.000 | R$ 1.620.000 | 30 meses | Viável com ressalvas |
| **C — Pricing + escopo reduzido** — combina A e B | R$ 1.750.000 | R$ 2.268.000 | 19 meses | Viável |

**Detalhes por cenário:**

### Cenário A — Ajuste de pricing
- **O que muda:** Ticket médio Professional sobe de R$ 149 para R$ 199/mês (+33%)
- **Riscos:** Possível queda de conversão de 12% para 9%; competidores com pricing inferior
- **Veredicto:** Viável com ressalvas — depende de elasticidade de preço não validada

### Cenário B — Redução de escopo MVP
- **O que muda:** Remove módulo de relatórios avançados (2 devs x 4 meses economizados); feature volta na Fase 2
- **Riscos:** Churn maior sem relatórios; diferencial competitivo enfraquecido
- **Veredicto:** Viável com ressalvas — time-to-market mais rápido mas proposta de valor diluída

### Cenário C — Pricing + escopo reduzido (recomendado)
- **O que muda:** Combina ajuste de pricing (R$ 199) com MVP reduzido
- **Riscos:** Cumulativos de A e B, porém break-even 11 meses antes do cenário A isolado
- **Veredicto:** Viável — melhor relação risco/retorno entre os cenários

## Representação Visual

### Dados de amostra

| Cenário | TCO 3 anos | Receita 3 anos |
|---------|-----------|----------------|
| Base | 2400000 | 1800000 |
| A — Ajuste pricing | 2400000 | 2520000 |
| B — Escopo reduzido | 1750000 | 1620000 |
| C — Pricing + escopo | 1750000 | 2268000 |

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Grouped bar chart (receita vs custo por cenário)
**Tecnologia:** Chart.js
**Justificativa:** Barras agrupadas lado a lado (TCO em vermelho, receita em verde) para cada cenário permitem comparação instantânea de viabilidade — quando a barra verde supera a vermelha, o cenário é viável. Uma linha horizontal de referência no valor do TCO base reforça o benchmark. Labels com break-even em meses sobre cada grupo completam a informação sem poluir.
**Alternativa:** Tabela (HTML/CSS) — quando o público precisa dos valores exatos e premissas detalhadas para cada cenário
