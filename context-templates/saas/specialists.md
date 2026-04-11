---
title: Spec Pack — SaaS
pack-id: saas
description: Catálogo de custom-specialists disponíveis para projetos SaaS multi-tenant. Define quando o orchestrator deve invocar cada specialist durante a reunião da Fase 1, qual subtópico ele cobre e qual o prompt base.
version: 01.00.000
status: ativo
author: claude-code
category: spec-pack
project-name: global
area: tecnologia
tags:
  - spec-pack
  - saas
  - custom-specialists
created: 2026-04-08 12:00
---

# Spec Pack — SaaS

> [!info] Relação com o context-pack
> Este spec-pack é carregado em conjunto com o `context-templates/saas/context.md` durante o **Setup** do pipeline. Enquanto o context define **concerns** e **perguntas recomendadas**, este specialists define **quais custom-specialists estão disponíveis** para serem invocados dinamicamente pelo orchestrator quando po, solution-architect ou cyber-security-architect pedirem `help` em subtópicos específicos.

## Como o orchestrator consulta este pack

Durante a reunião da Fase 1, quando um especialista fixo pede `help` em domínio específico:

1. Orchestrator identifica o subtópico pedido
2. Consulta a tabela "Catálogo" abaixo
3. Se houver match → invoca o specialist declarado com o prompt base correspondente
4. Se não houver match → gera um custom-specialist **on-the-fly** em modo genérico e registra no log

LGPD/Privacidade NÃO está aqui — é coberta obrigatoriamente pelo `cyber-security-architect` (agente fixo, bloco 6).

## Catálogo

| Specialist | Domínio | Quando invocar |
|---|---|---|
| `cloud-architecture-aws` | Arquitetura AWS avançada | Stack definida como AWS com requisitos de multi-region, EKS, serverless, ou custo-otimização |
| `cloud-architecture-gcp` | Arquitetura GCP avançada | Stack definida como GCP com Cloud Run, GKE, BigQuery, ou integração com Workspace |
| `cloud-architecture-azure` | Arquitetura Azure avançada | Stack definida como Azure com AKS, Cosmos DB, ou integração com M365/Entra ID |
| `payments-compliance` | Compliance de pagamentos e billing | Pagamentos internacionais, múltiplas moedas, PCI-DSS, anti-fraude, chargebacks, compliance Bacen |
| `enterprise-identity` | SSO corporativo, SAML, federação | Vendas enterprise exigem SAML/SCIM, federação com AD/Okta, ou certificações SOC 2 |
| `ml-engineering` | ML/IA como feature do produto | Produto tem componente de ML (recomendação, classificação, scoring, LLM wrapper) |
| `performance-engineering` | Performance crítica, baixa latência | SLA < 100ms p99, volumes altos, otimização de hot path |
| `multi-tenancy-architect` | Isolamento multi-tenant avançado | Decisão entre database-per-tenant, schema-per-tenant, row-level; isolamento regulatório |
| `billing-platform-advisor` | Escolha e design de billing | Decisão Stripe vs Chargebee vs custom; modelo de cobrança complexo; dunning; revenue recognition |
| `regulated-industry-health` | Compliance em saúde (HIPAA, ANS) | SaaS em saúde com dados clínicos |
| `regulated-industry-finance` | Compliance financeiro (Bacen, CVM) | SaaS financeiro, fintech, crédito |

## Prompt base por specialist

Cada specialist é invocado com o template:

```
Você é o specialist `{specialist-id}` do context-pack saas no Discovery Pipeline v0.5.

Domínio: {domínio da tabela}

Contexto da reunião até aqui:
{log dos blocos já cobertos}

Subtópico que pediram sua ajuda:
{descrição do ponto}

Sua missão:
1. Aprofunda o subtópico com vocabulário real do domínio
2. Sinaliza antipatterns conhecidos
3. Se o customer marcar [INFERENCE] em ponto crítico, force aprofundamento
4. Se o domínio exige especialista humano de verdade, marque [NEEDS-HUMAN-SPECIALIST] e justifique
5. Devolve controle ao especialista fixo que te invocou

Seja honesto sobre suas limitações: você é o mesmo modelo de linguagem assumindo um papel. Não invente profundidade que não tem.
```

## Fallback genérico

Se o orchestrator não encontrar um specialist neste catálogo para o subtópico pedido, ele gera um custom-specialist **on-the-fly** em modo genérico com o prompt:

```
Você é um specialist genérico em {domínio inferido} do Discovery Pipeline v0.5.
Não há prompt curado para este domínio neste spec-pack — você opera em modo genérico.
Priorize clareza sobre profundidade. Marque [NEEDS-HUMAN-SPECIALIST] facilmente.
```

E registra no log: `[CUSTOM-SPECIALIST-GENERIC] invocado para {domínio}`.
