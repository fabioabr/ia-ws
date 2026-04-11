---
region-id: REG-DOM-SAAS-01
title: "SaaS Pricing Model"
group: domain
description: "Pricing tiers, plans, and revenue model for SaaS products"
source: "Bloco #3/#8"
schema: "Planos/tiers/pricing/MRR/ARR"
template-visual: "Pricing table"
when: saas
default: false
---

# SaaS Pricing Model

Detalha o modelo de precificacao do produto SaaS, incluindo planos, tiers, features por plano e projecao de receita. Esta regiao e ativada automaticamente quando o contexto do projeto e SaaS.

## Schema de dados

```yaml
saas_pricing:
  model: string                  # Flat / Tiered / Usage-based / Hybrid
  plans:
    - name: string
      price_monthly: number
      price_annual: number
      features: string[]
      target_segment: string
  projections:
    mrr_month_12: number
    arr_year_1: number
```

## Exemplo

| Plano | Mensal | Anual | Segmento | Features Principais |
|-------|--------|-------|----------|-------------------|
| Starter | R$ 49/mes | R$ 470/ano | MEI e micro | Dashboard basico, 1 conta bancaria, relatorios PDF |
| Professional | R$ 149/mes | R$ 1.430/ano | Pequena empresa | Multi-conta, Open Finance, relatorios avancados, API |
| Enterprise | Sob consulta | Sob consulta | Media empresa | Multi-tenancy, SSO, SLA dedicado, suporte prioritario |

## Representacao Visual

### Dados de amostra

| Plano | Mensal (R$) | Anual (R$) | Features |
|-------|-------------|------------|----------|
| Starter | 49 | 470 | 3 |
| Professional | 149 | 1.430 | 7 |
| Enterprise | Sob consulta | Sob consulta | 12+ |

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Pricing table
**Tecnologia:** HTML/CSS
**Justificativa:** Tiers de pricing com features, precos e segmentos sao melhor comunicados em uma tabela estilizada com colunas por plano e destaque visual no plano recomendado. Pricing tables sao o padrao da industria SaaS e permitem comparacao direta.
**Alternativa:** Pricing cards lado-a-lado (HTML/CSS) — quando o formato for para landing page ou material de marketing com menos de 4 planos.
