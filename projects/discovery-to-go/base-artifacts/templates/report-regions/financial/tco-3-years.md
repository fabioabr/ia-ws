---
region-id: REG-FIN-01
title: "TCO 3 Years"
group: financial
description: "Total Cost of Ownership projection across three years with sensitivity ranges"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (categoria, ano 1, ano 2, ano 3, total) + faixa de sensibilidade"
template-visual: "Table + stat card (total)"
default: true
---

# TCO 3 Years

Apresenta o custo total de propriedade projetado em três anos, segmentado por categoria de custo. Inclui faixas de sensibilidade (otimista, esperado, pessimista) para refletir incertezas nas premissas. Esta visao permite ao decisor entender o compromisso financeiro completo antes de aprovar o investimento.

## Schema de dados

```yaml
tco:
  categories:
    - name: string           # Nome da categoria (ex: infraestrutura, licenças, equipe)
      year_1: number         # Custo estimado ano 1 (BRL)
      year_2: number         # Custo estimado ano 2 (BRL)
      year_3: number         # Custo estimado ano 3 (BRL)
      total: number          # Soma dos 3 anos
  totals:
    year_1: number
    year_2: number
    year_3: number
    grand_total: number
  sensitivity:
    optimistic: number       # -20% do esperado
    expected: number         # Valor base
    pessimistic: number      # +30% do esperado
  assumptions: string[]      # Lista de premissas usadas
```

## Exemplo

| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Infraestrutura Cloud (AWS) | R$ 48.000 | R$ 62.000 | R$ 74.000 | R$ 184.000 |
| Licenças e SaaS | R$ 36.000 | R$ 36.000 | R$ 42.000 | R$ 114.000 |
| Equipe (4 devs + 1 PO) | R$ 480.000 | R$ 520.000 | R$ 540.000 | R$ 1.540.000 |
| Operação e suporte | R$ 0 | R$ 24.000 | R$ 36.000 | R$ 60.000 |
| **Total** | **R$ 564.000** | **R$ 642.000** | **R$ 692.000** | **R$ 1.898.000** |

**Faixa de sensibilidade:** R$ 1.518.400 (otimista) — R$ 1.898.000 (esperado) — R$ 2.467.400 (pessimista)

**Premissas:** crescimento de 15% a.a. na base de usuários; reajuste salarial de 8% a.a.; sem migração de cloud provider.

## Representação Visual

### Dados de amostra

| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Infraestrutura Cloud (AWS) | R$ 48.000 | R$ 62.000 | R$ 74.000 | R$ 184.000 |
| Licenças e SaaS | R$ 36.000 | R$ 36.000 | R$ 42.000 | R$ 114.000 |
| Equipe (4 devs + 1 PO) | R$ 480.000 | R$ 520.000 | R$ 540.000 | R$ 1.540.000 |
| Operação e suporte | R$ 0 | R$ 24.000 | R$ 36.000 | R$ 60.000 |
| **Total** | **R$ 564.000** | **R$ 642.000** | **R$ 692.000** | **R$ 1.898.000** |

Faixa de sensibilidade: R$ 1.518.400 (otimista) — R$ 1.898.000 (esperado) — R$ 2.467.400 (pessimista)

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo a evolução do TCO ao longo dos 3 anos, destacando os maiores centros de custo e a faixa de sensibilidade | Relatórios executivos onde o contexto qualitativo importa mais que a precisão numérica |
| Tabela | Matriz categoria x ano com totais e faixa de sensibilidade, como no exemplo acima | Quando o leitor precisa comparar valores exatos entre categorias e períodos |
| Stacked bar chart | Barras empilhadas por ano, cada segmento representando uma categoria de custo, com cores distintas | Visualizar a composição do custo por ano e identificar quais categorias dominam o TCO |
| Waterfall chart | Cascata mostrando como cada categoria contribui para o total acumulado em cada ano | Destacar o impacto incremental de cada categoria no custo total |
| Line trend chart | Linhas por categoria ao longo dos 3 anos, com área sombreada para a faixa de sensibilidade | Enfatizar tendências de crescimento e a incerteza associada às projeções |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
