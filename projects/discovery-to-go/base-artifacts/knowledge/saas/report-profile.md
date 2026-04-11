---
title: Report Profile — SaaS
pack-id: saas
description: Perfil de relatório para projetos SaaS multi-tenant — define seções extras, métricas obrigatórias, diagramas e ênfases que o consolidator aplica ao delivery report
version: 01.00.000
status: ativo
author: claude-code
category: report-profile
area: tecnologia
tags:
  - report-profile
  - saas
  - delivery
  - consolidator
created: 2026-04-11
---

# Report Profile — SaaS

Perfil de relatório específico para projetos SaaS multi-tenant. O `consolidator` lê este arquivo durante a Fase 3 (Delivery) e faz merge com o template base (`final-report-template.md`) para montar a estrutura final do `delivery-report.md`.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este report-profile **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este profile é ignorado.

---

## Seções extras

Seções que o consolidator deve **adicionar** ao relatório base para projetos SaaS:

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Modelo Comercial e Pricing** | Entre Overview e Visão de Produto | Modelo de monetização (free trial / freemium / pago / tiered), planos e diferenciação entre tiers, estratégia de pricing, projeção de MRR/ARR por tier, break-even analysis |

---

## Métricas obrigatórias

O consolidator deve garantir que estas métricas apareçam no delivery report (na seção "Métricas-chave" ou distribuídas nas seções relevantes):

| Métrica | Onde incluir | Descrição |
|---------|-------------|-----------|
| MRR / ARR | Métricas-chave + Modelo Comercial | Receita recorrente mensal/anual projetada por tier |
| Churn rate | Métricas-chave | Taxa de cancelamento aceitável |
| LTV / CAC | Métricas-chave + Análise Estratégica | Lifetime value / custo de aquisição mínimo viável |
| Time-to-value | Métricas-chave + Visão de Produto | Tempo entre signup e primeiro valor percebido |
| Disponibilidade alvo | Métricas-chave + Tech | SLA de uptime (3 9s, 4 9s, 5 9s) |
| Custo por tenant | Métricas-chave + Análise Estratégica | Custo de infra variável por tenant (compute, storage, bandwidth) |
| Ativação | Métricas-chave | % de usuários que completam onboarding com sucesso |
| Retenção | Métricas-chave | % de usuários ativos após 30/60/90 dias |

---

## Diagramas

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| Fluxo de onboarding | Opcional | Visão de Produto | Jornada do signup ao primeiro valor — útil quando onboarding é self-service |

---

## Ênfases por seção base

Ajustes de ênfase que o consolidator deve aplicar nas seções do template base:

| Seção base | Ênfase SaaS |
|------------|-------------|
| **Visão de Produto** | Destacar modelo de onboarding (self-service vs assistido vs white-glove), time-to-value, diferenciação competitiva por tier |
| **Backlog Priorizado** | Priorização por tier: MVP → Growth → Enterprise. Identificar features que diferenciam planos |
| **Tecnologia e Segurança** | Destacar estratégia de tenancy (database-per-tenant vs schema vs row-level), rate limiting por tenant, SSO corporativo (SAML) para Enterprise |
| **Privacidade e Compliance** | Destacar isolamento de dados entre tenants, sub-operadores (Stripe, SendGrid) com DPA, direito ao esquecimento em banco multi-tenant |
| **Análise Estratégica** | Incluir análise Build vs Buy para billing (Stripe/Chargebee/custom), auth (Auth0/Cognito/custom), search (Algolia/Elasticsearch) |
| **Matriz de Riscos** | Incluir riscos específicos: vendor lock-in do gateway de pagamento, tenant abusando rate limit, DDoS em um tenant afetando outros |

---

## Documentos Relacionados

- [[context|knowledge/saas/context.md]] — Concerns e perguntas recomendadas para a Fase 1
- [[specialists|knowledge/saas/specialists.md]] — Catálogo de custom-specialists para SaaS
- `dtg-artifacts/templates/customization/final-report-template.md` — Template base (11 seções obrigatórias)
