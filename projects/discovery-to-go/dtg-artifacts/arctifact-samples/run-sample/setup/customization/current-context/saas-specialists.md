---
title: "SaaS Specialists Catalog"
description: Catálogo de especialistas disponíveis para o knowledge pack SaaS
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: knowledge
area: tecnologia
tags:
  - knowledge-pack
  - saas
  - specialists
created: 2026-04-11 09:00
---

# SaaS Specialists Catalog

> Cópia local do catálogo global de especialistas para o pack `saas`.

## Especialistas Disponíveis

| Agente | Domínio | Quando Ativar |
|--------|---------|---------------|
| po | Produto e negócio | Sempre (core) |
| solution-architect | Arquitetura e TCO | Sempre (core) |
| cyber-security-architect | Segurança e LGPD | Quando há dados sensíveis |
| ux-researcher | Experiência do usuário | Quando há B2C ou onboarding complexo |
| data-engineer | Dados e integrações | Quando há ETL ou integrações pesadas |
| devops-engineer | Infra e CI/CD | Quando há requisitos de SLA rigorosos |

## Seleção para FinTrack Pro

**Ativados neste run:**
- po — core
- solution-architect — core
- cyber-security-architect — dados financeiros sensíveis (LGPD)
- customer — simulação do cliente (sempre presente)

**Não ativados (justificativa):**
- ux-researcher — onboarding simples no MVP, equipe já tem designer UX
- data-engineer — integrações cobertas pelo solution-architect nesta escala
- devops-engineer — CI/CD existente, sem requisitos de SLA definidos no MVP

## Regras de Ativação

1. Agentes `core` participam de todas as fases
2. Agentes condicionais entram quando o pack detecta triggers no briefing
3. O orchestrator pode adicionar agentes durante o run se surgirem temas inesperados
4. Máximo recomendado: 5 agentes simultâneos na entrevista
