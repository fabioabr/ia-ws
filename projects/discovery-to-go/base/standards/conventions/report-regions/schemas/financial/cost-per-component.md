---
region-id: REG-FIN-03
title: "Cost per Component"
group: financial
description: "Detailed cost breakdown by architectural component — modo custo-real (projeto-paga) OU consumo-estimado (fundo-global)"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (componente, custo/mês, custo/ano)"
template-visual: "Table ou bar chart"
default: false
deliverable-scope: ["DR"]
conditional-on: "always (rótulo muda conforme financial_model)"
---

# Cost per Component

Detalha o custo operacional de cada componente da arquitetura, permitindo identificar os maiores centros de custo e oportunidades de otimização. Essa visão granular é essencial para decisões de trade-off arquitetural e para planejamento de capacity.

> [!info] Dois rótulos conforme `financial_model`
> - Modo `projeto-paga`: valores representam **custo real** que o projeto pagará por componente.
> - Modo `fundo-global`: valores representam **estimativa de consumo sem free tier** — o projeto não paga, mas precisa estimar para dimensionamento do fundo. A tabela deve explicitar isso no cabeçalho ("Estimativa de consumo por componente — cobrança central via fundo global").

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

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Horizontal bar chart
**Tecnologia:** HTML/CSS (barras proporcionais com largura percentual)
**Justificativa:** 6 componentes com custos absolutos são perfeitamente representados por barras horizontais ordenadas do maior para o menor — o label do componente fica legível à esquerda e a barra comunica a magnitude relativa sem necessidade de biblioteca JS. HTML/CSS puro é mais leve e mantém controle total do layout.
**Alternativa:** Pie chart (Chart.js) — quando o foco da análise for a proporção percentual de cada componente no custo total em vez da comparação absoluta entre valores
