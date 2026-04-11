---
title: HTML Layout — Default
description: Define quais regions aparecem no delivery report HTML, em que ordem e com que layout. Customizável por projeto em custom-artifacts/{client}/config/html-layout.md.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: customization
area: tecnologia
tags:
  - customization
  - html-layout
  - regions
  - delivery-report
created: 2026-04-11
---

# HTML Layout — Default

Define a estrutura visual do `delivery-report.html`. O html-writer lê este arquivo para saber **quais regions** renderizar, **em que ordem** e com **que layout**.

> [!info] Customização
> O cliente pode sobrescrever este layout em `custom-artifacts/{client}/config/html-layout.md`. Se não existir override, este default é usado.

> [!info] Relação com o .md
> O `delivery-report.md` é sempre **completo** (todas as regions com dados). O HTML renderiza apenas as regions listadas aqui, na ordem e layout definidos. Regions que existem no .md mas não estão neste layout simplesmente não aparecem no HTML.

---

## Layouts disponíveis

| Layout | Descrição | Quando usar |
|--------|-----------|-------------|
| `full-width` | Ocupa toda a largura do container | Narrativas, diagramas, tabelas grandes |
| `grid-2` | Grid de 2 colunas (50/50) | Comparações lado-a-lado, pares de cards |
| `grid-3` | Grid de 3 colunas (33/33/33) | KPIs, stat cards, métricas |
| `grid-4` | Grid de 4 colunas (25/25/25/25) | DORA metrics, mini stat cards |
| `sidebar` | 70/30 — conteúdo principal + sidebar | Texto com KPI lateral |

---

## Seção 1 — Executive Summary

| Region | Layout | Notas |
|--------|--------|-------|
| REG-EXEC-01 | full-width | Hero card — primeira coisa que o leitor vê |
| REG-FIN-01 | grid-3 | Stat card com total TCO |
| REG-RISK-01 | grid-3 | Top 3 riscos com badges |
| REG-EXEC-03 | grid-3 | Badge de veredicto Go/No-Go |
| REG-EXEC-04 | full-width | Tabela de próximos passos |

---

## Seção 2 — Produto

| Region | Layout | Notas |
|--------|--------|-------|
| REG-PROD-01 | full-width | Problema e contexto com métrica destacada |
| REG-PROD-04 | full-width | Proposta de valor (elevator pitch) |
| REG-PROD-02 | grid-2 | Persona cards (2 por linha) |
| REG-PROD-07 | full-width | Escopo — split card (dentro/fora) |
| REG-PROD-05 | full-width | OKRs com progress bars |

---

## Seção 3 — Organização

| Region | Layout | Notas |
|--------|--------|-------|
| REG-ORG-01 | full-width | Mapa de stakeholders |
| REG-ORG-02 | full-width | Estrutura de equipe |

---

## Seção 4 — Tecnologia e Arquitetura

| Region | Layout | Notas |
|--------|--------|-------|
| REG-TECH-01 | full-width | Stack tecnológica (tabela com badges) |
| REG-TECH-03 | full-width | Arquitetura macro (diagrama) |
| REG-TECH-02 | full-width | Integrações |
| REG-TECH-06 | full-width | Build vs Buy (tabela com verdicts) |

---

## Seção 5 — Segurança e Privacidade

| Region | Layout | Notas |
|--------|--------|-------|
| REG-SEC-01 | full-width | Classificação de dados |
| REG-SEC-02 | full-width | Autenticação e autorização |
| REG-SEC-04 | full-width | Compliance |
| REG-PRIV-01 | full-width | Dados pessoais mapeados (se aplicável) |
| REG-PRIV-02 | full-width | Base legal LGPD (se aplicável) |

---

## Seção 6 — Financeiro

| Region | Layout | Notas |
|--------|--------|-------|
| REG-FIN-01 | full-width | TCO 3 anos (stacked bar chart + tabela) |
| REG-FIN-05 | full-width | Estimativa de esforço (horizontal bars) |

---

## Seção 7 — Riscos e Qualidade

| Region | Layout | Notas |
|--------|--------|-------|
| REG-RISK-01 | full-width | Matriz de riscos (bubble chart ou tabela) |
| REG-RISK-02 | full-width | Riscos técnicos |
| REG-RISK-03 | full-width | Hipóteses não validadas |
| REG-QUAL-01 | sidebar | Radar chart (auditor) + score cards |
| REG-QUAL-02 | full-width | Questões do 10th-man |

---

## Seção 8 — Backlog

| Region | Layout | Notas |
|--------|--------|-------|
| REG-BACK-01 | full-width | Épicos priorizados (tabela com badges) |

---

## Seção 9 — Métricas

| Region | Layout | Notas |
|--------|--------|-------|
| REG-METR-01 | grid-3 | KPIs de negócio (stat cards) |

---

## Seção 10 — Narrativa e Decisão

| Region | Layout | Notas |
|--------|--------|-------|
| REG-NARR-01 | full-width | Como chegamos aqui (timeline) |
| REG-EXEC-02 | full-width | Product brief |
| REG-EXEC-03 | full-width | Go/No-Go (radar chart + verdicts) |
| REG-EXEC-04 | full-width | Próximos passos |

---

## Seção 11 — Domain-specific (condicional)

Regions domain-specific são inseridas automaticamente pelo html-writer quando o context-template correspondente está ativo. A posição default é após a Seção 4 (Tecnologia).

| Region | Layout | Quando |
|--------|--------|--------|
| REG-DOM-SAAS-01 | full-width | `saas` — Pricing table |
| REG-DOM-SAAS-02 | full-width | `saas` — Tenancy strategy |
| REG-DOM-DATA-01 | full-width | `datalake-ingestion` — Medallion |
| REG-DOM-DATA-02 | full-width | `datalake-ingestion` — Data quality |
| REG-DOM-INTEG-01 | full-width | `system-integration` — Mapa de integrações |
| REG-DOM-INTEG-02 | full-width | `system-integration` — Data contracts |
| REG-DOM-MIGR-01 | full-width | `migration-modernization` — Roadmap |
| REG-DOM-MIGR-02 | full-width | `migration-modernization` — AS-IS vs TO-BE |
| REG-DOM-AIML-01 | full-width | `ai-ml` — Estratégia ML |
| REG-DOM-AIML-02 | full-width | `ai-ml` — Model governance |
| REG-DOM-MOB-01 | full-width | `mobile-app` — Mobile strategy |
| REG-DOM-MOB-02 | full-width | `mobile-app` — Distribution |
| REG-DOM-RPA-01 | full-width | `process-automation` — Automation roadmap |
| REG-DOM-RPA-02 | full-width | `process-automation` — CoE governance |
| REG-DOM-PLAT-01 | full-width | `platform-engineering` — Platform architecture |
| REG-DOM-PLAT-02 | grid-4 | `platform-engineering` — DX stat cards |
| REG-DOM-PROC-01 | full-width | `process-documentation` — Taxonomy |
| REG-DOM-PROC-02 | full-width | `process-documentation` — Governance |
| REG-DOM-MICRO-01 | full-width | `web-microservices` — Service map |
| REG-DOM-MICRO-02 | full-width | `web-microservices` — Resilience |

---

## Regions opcionais (não incluídas por default)

Estas regions existem no catálogo mas não aparecem no HTML por default. O cliente pode adicioná-las no seu override de layout.

| Region | Grupo | Para incluir |
|--------|-------|-------------|
| REG-PROD-03 | Jornadas de usuário | Adicionar após REG-PROD-02 |
| REG-PROD-06 | Modelo de negócio | Adicionar na Seção 2 |
| REG-PROD-08 | Roadmap | Adicionar no final da Seção 2 |
| REG-PROD-09 | Visão do produto | Adicionar no início da Seção 2 |
| REG-PESQ-01 a 05 | Pesquisa | Criar Seção "Pesquisa" entre 2 e 3 |
| REG-ORG-03 | RACI | Adicionar na Seção 3 |
| REG-ORG-04 | Metodologia | Adicionar na Seção 3 |
| REG-ORG-05 | On-call | Adicionar na Seção 3 |
| REG-TECH-04 | Container architecture | Adicionar após REG-TECH-03 |
| REG-TECH-05 | ADRs | Adicionar na Seção 4 |
| REG-TECH-07 | Requisitos não-funcionais | Adicionar na Seção 4 |
| REG-SEC-03 | Criptografia | Adicionar na Seção 5 |
| REG-PRIV-03 a 06 | Privacidade (extras) | Adicionar na Seção 5 |
| REG-FIN-02 | Break-even | Adicionar na Seção 6 |
| REG-FIN-03 | Custo por componente | Adicionar na Seção 6 |
| REG-FIN-04 | Projeção de receita | Adicionar na Seção 6 |
| REG-RISK-04 | Análise de viabilidade | Adicionar na Seção 7 |
| REG-QUAL-03 | Gaps identificados | Adicionar na Seção 7 |
| REG-QUAL-04 | Checklist de conclusão | Adicionar na Seção 7 |
| REG-BACK-02 a 04 | Backlog (extras) | Adicionar na Seção 8 |
| REG-METR-02 a 05 | Métricas (extras) | Adicionar na Seção 9 |
| REG-NARR-02 | Condições para prosseguir | Adicionar na Seção 10 |
| REG-NARR-03 | Assinaturas | Adicionar no final da Seção 10 |
