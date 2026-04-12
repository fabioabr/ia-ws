---
title: "Report Setup — Executivo"
description: "Setup intermediário: gera One-Pager + Relatório Executivo com visão corporativa, custos, prazos e organização — sem detalhes de tecnologia e sistemas."
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - executive
  - corporate
created: 2026-04-11
---

# Report Setup — Executivo

Setup intermediário que gera **dois HTMLs**: o One-Pager (do setup essencial) + um Relatório Executivo com visão corporativa. Foca em **negócio, organização, custos e prazos** — sem entrar em detalhes de tecnologia, sistemas ou arquitetura.

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única executiva (mesmo do setup essencial) |
| `executive-report.html` | Relatório corporativo: produto, organização, financeiro, riscos, backlog |

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

### Executive Report

#### Seção 1 — Produto e Valor

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 9 | REG-EXEC-02 | full-width | Product brief completo |
| 10 | REG-PROD-04 | full-width | Proposta de valor (elevator pitch) |
| 11 | REG-PROD-02 | grid-2 | Personas (cards com perfil e dores) |
| 12 | REG-PROD-05 | full-width | OKRs e ROI (métricas de sucesso) |
| 13 | REG-PROD-06 | full-width | Modelo de negócio (se aplicável) |

#### Seção 2 — Organização

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 14 | REG-ORG-01 | full-width | Mapa de stakeholders |
| 15 | REG-ORG-02 | full-width | Estrutura de equipe |
| 16 | REG-ORG-04 | full-width | Metodologia (se definida) |

#### Seção 3 — Financeiro e Prazos

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 17 | REG-FIN-01 | full-width | TCO 3 anos detalhado (tabela + chart) |
| 18 | REG-FIN-02 | full-width | Break-even analysis (se aplicável) |
| 19 | REG-FIN-05 | full-width | Estimativa de esforço detalhada |
| 20 | REG-FIN-07 | full-width | Financial Scenarios (quando cenários alternativos existirem) |
| 21 | REG-PROD-08 | full-width | Roadmap (faseamento MVP → Fase 2 → N) |

#### Seção 4 — Riscos e Decisão

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 22 | REG-RISK-01 | full-width | Matriz de riscos completa |
| 23 | REG-RISK-03 | full-width | Hipóteses não validadas |
| 24 | REG-BACK-01 | full-width | Backlog priorizado (épicos com MoSCoW) |
| 25 | REG-QUAL-01 | sidebar | Score do auditor (radar) |
| 26 | REG-QUAL-02 | full-width | Questões do 10th-man |

#### Seção 5 — Narrativa

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 27 | REG-NARR-01 | full-width | Como chegamos aqui (timeline das iterações) |
| 28 | REG-EXEC-03 | full-width | Go/No-Go detalhado (4 dimensões + condições) |
| 29 | REG-EXEC-04 | full-width | Próximos passos |

**Total: 29 regions** (8 no one-pager, 21 exclusivas do executive report)

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
