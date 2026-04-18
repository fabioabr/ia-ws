---
region-id: REG-FIN-01
title: "TCO 3 Years"
group: financial
description: "Total Cost of Ownership projection across three years with sensitivity ranges (modo projeto-paga) OR consumption estimate without free tier (modo fundo-global)"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (categoria, ano 1, ano 2, ano 3, total) + faixa de sensibilidade"
template-visual: "Table + stat card (total)"
default: true
deliverable-scope: ["EX", "DR"]
conditional-on: "always (forma muda conforme financial_model)"
---

# TCO 3 Years

Apresenta o custo total de propriedade projetado em três anos, segmentado por categoria de custo. Inclui faixas de sensibilidade (otimista, esperado, pessimista) para refletir incertezas nas premissas. Esta visão permite ao decisor entender o compromisso financeiro completo antes de aprovar o investimento.

> [!info] Dois modos de operação (flag `financial_model` do briefing)
> Esta region opera em **dois modos distintos** conforme a flag `financial_model` do briefing:
>
> **Modo `projeto-paga` (default):** TCO 3 anos completo — projeto arca com todos os custos (infra, licenças, equipe, operação). Estrutura original descrita abaixo.
>
> **Modo `fundo-global`:** transforma-se em **"Estimativa de consumo cloud sem free tier"** — projeto não paga os custos (vêm de um fundo corporativo global), mas **precisa estimar o consumo previsto** para dimensionamento do fundo e alertas de overrun. Exclui equipe e licenças corporativas já contratadas centralmente. Ver seção "Variante fundo-global" abaixo.

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

## Variante fundo-global (quando `financial_model=fundo-global`)

Quando o projeto opera sob fundo corporativo global de OPEX cloud, o TCO completo **não é aplicável** — mas o projeto ainda precisa entregar uma **estimativa de consumo sem free tier** para dimensionamento do fundo.

### Schema alternativo

```yaml
estimativa_consumo:
  cloud_provider: string            # AWS, Azure, GCP, etc.
  categories:
    - service: string               # Nome do serviço (ex: S3, RDS, Lambda)
      unit: string                  # Unidade (GB, req/mes, hora de CPU)
      year_1: number
      year_2: number
      year_3: number
      cost_year_1_brl: number       # Custo estimado sem free tier
      cost_year_2_brl: number
      cost_year_3_brl: number
  totals:
    cost_year_1_brl: number
    cost_year_2_brl: number
    cost_year_3_brl: number
  alertas_overrun:
    - metric: string
      threshold: string
  escopo_excluido: string[]         # Equipe, licenças corporativas, etc.
  premissas: string[]
```

### Exemplo (modo fundo-global)

**Cloud provider:** AWS (conta corporativa sob fundo global)

| Serviço | Unidade | Ano 1 | Ano 2 | Ano 3 | Custo Ano 1 | Custo Ano 2 | Custo Ano 3 |
|---|---|---|---|---|---|---|---|
| S3 Storage | GB-mês | 2.400 | 4.800 | 7.200 | R$ 1.800 | R$ 3.600 | R$ 5.400 |
| RDS Postgres | instância-mês | 12 | 12 | 24 | R$ 36.000 | R$ 38.000 | R$ 78.000 |
| Lambda | 1M req | 20 | 60 | 120 | R$ 4.000 | R$ 12.000 | R$ 24.000 |
| **Total estimado** |  |  |  |  | **R$ 41.800** | **R$ 53.600** | **R$ 107.400** |

**Escopo excluído (vem do fundo global / já contratado):** Equipe (não se aplica — desenvolvimento interno); licenças SaaS corporativas (Datadog, Sentry); conta AWS (free tier não aplicável pois já ultrapassado na conta-mãe).

**Alertas de overrun:** RDS > R$ 80K/ano dispara revisão de rightsizing; Lambda > 200M req/mes requer migração para fargate.

**Premissas:** dobro de usuários ativos a cada ano; retenção de logs 7 anos (obrigatoriedade regulatória); sem free tier disponível.

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

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO + CARD
**Tipo:** Stacked bar chart + stat card total
**Tecnologia:** Chart.js (stacked bar) + HTML/CSS (stat card com faixa de sensibilidade)
**Justificativa:** 4 categorias de custo cruzadas com 3 anos formam um dataset ideal para barras empilhadas — cada barra (ano) mostra a composição do custo e permite comparar tanto o total quanto a participação de cada categoria ao longo do tempo. O stat card complementa com o grand total e a faixa de sensibilidade em destaque.
**Alternativa:** Tabela (HTML/CSS) — quando o leitor precisa dos valores exatos por célula para auditoria ou re-cálculo próprio
