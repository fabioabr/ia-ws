---
region-id: REG-FIN-03
title: "Cost per Component"
group: financial
description: "Detailed cost breakdown by architectural component"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (componente, custo/mês, custo/ano)"
template-visual: "Table ou bar chart"
default: false
---

# Cost per Component

Detalha o custo operacional de cada componente da arquitetura, permitindo identificar os maiores centros de custo e oportunidades de otimizacao. Essa visao granular e essencial para decisoes de trade-off arquitetural e para planejamento de capacity.

## Schema de dados

```yaml
cost_per_component:
  components:
    - name: string             # Nome do componente
      type: string             # Tipo (compute, storage, network, service, license)
      monthly_cost: number     # Custo mensal (BRL)
      annual_cost: number      # Custo anual (BRL)
      notes: string            # Observacoes (ex: custo variavel)
  total_monthly: number
  total_annual: number
```

## Exemplo

| Componente | Tipo | Custo/Mes | Custo/Ano | Notas |
|-----------|------|-----------|-----------|-------|
| EKS Cluster (3 nodes) | Compute | R$ 2.800 | R$ 33.600 | Auto-scaling ate 6 nodes |
| RDS PostgreSQL (Multi-AZ) | Storage | R$ 1.200 | R$ 14.400 | db.r6g.large |
| Redis ElastiCache | Storage | R$ 480 | R$ 5.760 | Cache de sessao |
| CloudFront + S3 | Network | R$ 350 | R$ 4.200 | CDN para SPA |
| Auth0 (Business plan) | License | R$ 1.500 | R$ 18.000 | Ate 10k MAU |
| Datadog (Pro) | License | R$ 900 | R$ 10.800 | 5 hosts |
| **Total** | | **R$ 7.230** | **R$ 86.760** | |

## Representação Visual

### Dados de amostra

| Componente | Tipo | Custo/Mês | Custo/Ano |
|-----------|------|-----------|-----------|
| EKS Cluster (3 nodes) | Compute | R$ 2.800 | R$ 33.600 |
| RDS PostgreSQL (Multi-AZ) | Storage | R$ 1.200 | R$ 14.400 |
| Redis ElastiCache | Storage | R$ 480 | R$ 5.760 |
| CloudFront + S3 | Network | R$ 350 | R$ 4.200 |
| Auth0 (Business plan) | License | R$ 1.500 | R$ 18.000 |
| Datadog (Pro) | License | R$ 900 | R$ 10.800 |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo os principais centros de custo, proporções e oportunidades de otimização | Relatórios onde o contexto de cada componente é mais relevante que a comparação visual |
| Tabela | Matriz componente x custo com tipo e notas, como no exemplo acima | Quando o leitor precisa de valores exatos e detalhes por componente |
| Pie chart | Gráfico de pizza mostrando a proporção de cada componente no custo total mensal/anual | Visualizar rapidamente a distribuição percentual dos custos — ideal para até 6-8 componentes |
| Treemap | Retângulos proporcionais ao custo de cada componente, agrupados por tipo (compute, storage, license) | Quando há muitos componentes e se deseja mostrar hierarquia por tipo + proporção de custo |
| Stacked bar chart | Barras empilhadas agrupadas por tipo de componente (compute, storage, network, license) | Comparar custos entre tipos de componente e identificar a categoria dominante |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
