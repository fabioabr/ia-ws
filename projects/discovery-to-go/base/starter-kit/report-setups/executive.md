---
title: "Report Setup — Executivo (legacy — catálogo de regions do executive-report.html)"
description: "Catálogo das regions que o html-writer monta para o executive-report.html (8 tabs). Legacy: não use como setting do briefing — declare `deliverables_scope: [\"DR\", \"OP\", \"EX\"]` em vez disso."
project-name: discovery-to-go
version: 02.01.000
status: legacy
deprecated-as-briefing-flag: true
superseded-by: ["deliverables_scope", "executive-layout.md"]
deliverables-scope-equivalent: ["DR", "OP", "EX"]
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - executive
  - corporate
  - legacy
created: 2026-04-11
updated: 2026-04-17
---

# Report Setup — Executivo

> [!warning] Legacy
> Este arquivo permanece como **catálogo de referência** das regions do `executive-report.html` (8 tabs). Mas **não deve mais ser citado no briefing** como `report-setup: executive`. Use `deliverables_scope: ["DR", "OP", "EX"]`. Ver [report-setups/README.md](README.md#migração-do-briefing).

Setup intermediário que gera **dois HTMLs**: o One-Pager (do setup essencial) + um Relatório Executivo com visão corporativa. Foca em **negócio, organização, custos e prazos** — sem entrar em detalhes de tecnologia, sistemas ou arquitetura.

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única executiva (mesmo do setup essencial) |
| `executive-report.html` | Relatório corporativo com 8 tabs: produto, organização, financeiro, riscos, backlog/decisão, auditoria IA, domínio, glossário |

## Regions incluídas

### One-Pager (mesmas do setup essencial)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 1 | REG-EXEC-01 | full-width | Overview executivo |
| 2 | REG-PROD-07 | full-width | Escopo (dentro/fora) |
| 3 | REG-PROD-01 | full-width | Problema e contexto |
| 4 | REG-FIN-01 | grid-3 | TCO 3 anos (stat card) |
| 5 | REG-RISK-01 | grid-3 | Top 3 riscos |
| 6 | REG-EXEC-03 | grid-3 | Go/No-Go (veredicto) |
| 7 | REG-FIN-05 | full-width | Estimativa de esforço |
| 8 | REG-EXEC-04 | full-width | Próximos passos |

### Executive Report (8 tabs)

#### Tab 1 — Produto (8 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 9 | REG-NARR-01 | full-width | Como chegamos aqui — timeline do discovery (dentro da Tab 1, não pré-tabs) |
| 10 | REG-EXEC-02 | full-width | Product brief completo |
| 11 | REG-PROD-01 | full-width | Problema e contexto |
| 12 | REG-PROD-04 | full-width | Proposta de valor (elevator pitch) |
| 13 | REG-PROD-02 | grid-2 | Personas (cards com perfil, dores e ganhos) |
| 14 | REG-PROD-07 | full-width | Escopo IN/OUT (split card verde/vermelho) |
| 15 | REG-PROD-05 | full-width | Modelo de negócio (pricing table se SaaS) |
| 16 | REG-PROD-06 | full-width | Roadmap (timeline horizontal HTML/CSS) |
| 17 | REG-PROD-08 | full-width | OKRs e métricas de sucesso |

#### Tab 2 — Organização (3 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 18 | REG-ORG-01 | full-width | Mapa de stakeholders |
| 19 | REG-ORG-02 | full-width | Estrutura de equipe (papéis, dedicação, horas) |
| 20 | REG-ORG-04 | full-width | Metodologia (Kanban, Scrum, etc.) |

#### Tab 3 — Financeiro (7 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 21 | REG-FIN-01 | full-width | TCO 3 anos detalhado (tabela + horizontal bars) |
| 22 | REG-FIN-02 | full-width | Break-even analysis |
| 23 | REG-FIN-04 | full-width | Receita vs custo (Chart.js line — único line chart) |
| 24 | REG-FIN-05 | full-width | Projeção de receita (tabela) |
| 25 | REG-FIN-06 | grid-3 | Estimativa de esforço (stat cards) |
| 26 | REG-FIN-07 | full-width | Cenários financeiros (horizontal bars HTML/CSS) |
| 27 | REG-PLAN-01 | full-width | Gantt relativo (horizontal bars + tabela de detalhamento obrigatória) |

#### Tab 4 — Riscos (5 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 28 | REG-RISK-01 | full-width | Matriz de riscos top 10 (tabela com severity badges) |
| 29 | REG-RISK-02 | full-width | Riscos técnicos |
| 30 | REG-RISK-03 | full-width | Hipóteses não validadas + perguntas residuais |
| 31 | REG-RISK-04 | full-width | Análise de viabilidade (veredicto por dimensão) |
| 32 | REG-EXEC-07 | full-width | Premissas (lista com ícones de atenção) |

#### Tab 5 — Backlog e Decisão (3 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 33 | REG-BACK-01 | full-width | Backlog MVP priorizado (tabela MoSCoW) |
| 34 | REG-EXEC-03 | full-width | Go/No-Go (4 dimensões + condições para prosseguir) |
| 35 | REG-EXEC-04 | full-width | Próximos passos (tabela com ações, responsável, prazo) |

#### Tab 6 — Auditoria IA (2 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 36 | REG-QUAL-01 | full-width | Score do Auditor — radar chart (Chart.js) com zones coloridas + tabela de scores por dimensão + ressalvas detalhadas |
| 37 | REG-QUAL-02 | full-width | Ressalvas do 10th-man — radar 3 eixos (Chart.js) + caveat cards com 5 campos (title, dimension, description, why_important, recommendation) |

> [!info] Por que tab separada?
> Auditor e 10th-man são agentes de IA da Fase 2 (Challenge). Ambos fazem validação independente do material. Agrupar numa tab "Auditoria IA" deixa claro que são avaliações automatizadas, separadas dos riscos de negócio (Tab 4) e das decisões humanas (Tab 5).

#### Tab 7 — Domínio (5 cards)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 38 | REG-TECH-06 | full-width | Build vs Buy (tabela com coluna Decisão separada: BUILD/BUY/HYBRID badges) |
| 39 | REG-SEC-01 | full-width | Classificação de dados |
| 40 | REG-SEC-02 | full-width | Autenticação e autorização |
| 41 | REG-SEC-04 | full-width | Compliance e regulação |
| 42 | REG-PRIV-01 | full-width | LGPD detalhado (quando há PII) |

#### Tab 8 — Glossário (1 card)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 43 | REG-NARR-04 | full-width | Glossário de siglas e termos (tabela alfabética com filtro de busca) |

**Total: 35 regions no executive report + 9 no one-pager = 44 cards renderizados**

## O que NÃO está incluído

- Stack tecnológica (REG-TECH-01)
- Arquitetura macro/containers (REG-TECH-03, 04)
- Integrações técnicas (REG-TECH-02)
- Build vs Buy detalhado (REG-TECH-06)
- ADRs (REG-TECH-05)
- Requisitos não-funcionais (REG-TECH-07)
- Segurança e criptografia (REG-SEC-*)
- Privacidade detalhada (REG-PRIV-*)
- KPIs técnicos (REG-METR-02)
- SLAs/SLOs (REG-METR-03)
- Regions de pesquisa (REG-PESQ-*)
- Regions domain-specific (REG-DOM-*)

## Quando usar

- Reunião de diretoria (30-60 minutos)
- Apresentação a gestores que precisam entender impacto e custo, mas não tecnologia
- PMO avaliando viabilidade e priorização de portfólio
- Sponsor aprovando budget e faseamento
