---
title: "Knowledge Pack — SaaS"
description: Contexto do knowledge pack SaaS aplicado ao projeto FinTrack Pro
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: knowledge
area: tecnologia
tags:
  - knowledge-pack
  - saas
  - fintrack-pro
created: 2026-04-11 09:00
---

# Knowledge Pack — SaaS

> Cópia local do pack global `saas`, filtrada para o contexto FinTrack Pro.

## Preocupações-chave para SaaS

### Multi-tenancy
- Isolamento de dados entre clientes (especialmente dados financeiros)
- Estratégia de particionamento: schema por tenant vs row-level security
- Noisy neighbor: limites de uso por plano

### Billing e Planos
- Gestão de assinaturas (upgrade, downgrade, cancelamento)
- Período de trial e conversão
- Metering de uso para limites por plano (ex: número de bancos)

### Onboarding
- Time-to-value: quanto tempo até o cliente ver resultado
- Self-service vs. assistido
- Migração de dados existentes (planilhas, ERPs)

### Compliance e Dados
- LGPD: consentimento, retenção, anonimização, DPO
- Dados financeiros sensíveis: classificação especial
- Auditoria: logs de acesso e alteração

### Escalabilidade
- Arquitetura que suporte crescimento de 10x sem rewrite
- Background jobs para processamento pesado
- Cache e CDN para dashboards

### Integrações
- APIs de terceiros (Open Finance, ERPs)
- Webhooks para eventos
- Rate limiting e circuit breakers

## Perguntas que o Pack Injeta na Entrevista

1. Qual a estratégia de multi-tenancy?
2. Como será o billing e gestão de planos?
3. Qual o onboarding esperado (self-service vs. assistido)?
4. Quais dados sensíveis serão armazenados e qual a base legal?
5. Qual a meta de SLA (uptime)?
6. Existe plano de disaster recovery?
