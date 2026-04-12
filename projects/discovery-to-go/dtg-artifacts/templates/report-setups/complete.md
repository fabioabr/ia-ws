---
title: "Report Setup — Completo"
description: "Setup completo: gera One-Pager + Relatório Executivo + Relatório Técnico com todas as regions incluindo cenários, custos por persona, arquitetura, segurança, privacidade e domain-specific."
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - complete
  - full
  - technical
created: 2026-04-11
---

# Report Setup — Completo

Setup completo que gera **três HTMLs**: One-Pager + Relatório Executivo + Relatório Técnico Completo. Inclui **todas** as regions disponíveis — produto, organização, tecnologia, segurança, privacidade, financeiro, riscos, qualidade, backlog, métricas, pesquisa, narrativa e domain-specific.

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única executiva |
| `executive-report.html` | Relatório corporativo (produto, org, financeiro, riscos) |
| `full-report.html` | Relatório técnico completo com todas as regions |

## Regions incluídas

### One-Pager (8 regions — mesmo do setup essencial)

| # | Region | Layout |
|---|--------|--------|
| 1 | REG-EXEC-01 | full-width |
| 2 | REG-PROD-07 | full-width |
| 3 | REG-PROD-01 | full-width |
| 4 | REG-FIN-01 | grid-3 |
| 5 | REG-RISK-01 | grid-3 |
| 6 | REG-EXEC-03 | grid-3 |
| 7 | REG-FIN-05 | full-width |
| 8 | REG-EXEC-04 | full-width |

### Executive Report (20 regions �� mesmo do setup executivo)

| # | Region | Layout |
|---|--------|--------|
| 9 | REG-EXEC-02 | full-width |
| 10 | REG-PROD-04 | full-width |
| 11 | REG-PROD-02 | grid-2 |
| 12 | REG-PROD-05 | full-width |
| 13 | REG-PROD-06 | full-width |
| 14 | REG-ORG-01 | full-width |
| 15 | REG-ORG-02 | full-width |
| 16 | REG-ORG-04 | full-width |
| 17 | REG-FIN-01 | full-width |
| 18 | REG-FIN-02 | full-width |
| 19 | REG-FIN-05 | full-width |
| 20 | REG-PROD-08 | full-width |
| 21 | REG-RISK-01 | full-width |
| 22 | REG-RISK-03 | full-width |
| 23 | REG-BACK-01 | full-width |
| 24 | REG-QUAL-01 | sidebar |
| 25 | REG-QUAL-02 | full-width |
| 26 | REG-NARR-01 | full-width |
| 27 | REG-EXEC-03 | full-width |
| 28 | REG-EXEC-04 | full-width |

### Full Report — Seções adicionais

#### Seção A — Produto Detalhado

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 29 | REG-PROD-03 | full-width | Jornadas de usuário (timeline por persona) |
| 30 | REG-PROD-09 | full-width | Visão do produto (horizonte 3 anos) |

#### Seção B — Pesquisa e Evidências

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 31 | REG-PESQ-01 | full-width | Relatório de entrevistas (accordion por tema) |
| 32 | REG-PESQ-02 | full-width | Citações representativas (blockquotes) |
| 33 | REG-PESQ-03 | full-width | Mapa de oportunidades (tree) |
| 34 | REG-PESQ-04 | full-width | Dados quantitativos (tabela + KPI cards) |
| 35 | REG-PESQ-05 | full-width | Source tag summary (donut chart — Chart.js) |

#### Seção C — Organização Detalhada

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 36 | REG-ORG-03 | full-width | RACI (heatmap) |
| 37 | REG-ORG-05 | full-width | On-call e sustentação |

#### Seção D — Tecnologia e Arquitetura

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 38 | REG-TECH-01 | full-width | Stack tecnológica (tabela com badges) |
| 39 | REG-TECH-03 | full-width | Arquitetura macro (diagrama C4 L1) |
| 40 | REG-TECH-04 | full-width | Arquitetura de containers (C4 L2) |
| 41 | REG-TECH-02 | full-width | Integrações (tabela com protocolos) |
| 42 | REG-TECH-06 | full-width | Build vs Buy (tabela com verdicts) |
| 43 | REG-TECH-05 | full-width | ADRs (accordion) |
| 44 | REG-TECH-07 | full-width | Requisitos não-funcionais |

#### Seção E — Segurança

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 45 | REG-SEC-01 | full-width | Classificação de dados (badges por nível) |
| 46 | REG-SEC-02 | full-width | Autenticação e autorização (checklist) |
| 47 | REG-SEC-03 | full-width | Criptografia (tabela) |
| 48 | REG-SEC-04 | full-width | Compliance (tabela com status) |

#### Seção F — Privacidade (quando há PII)

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 49 | REG-PRIV-01 | full-width | Dados pessoais mapeados |
| 50 | REG-PRIV-02 | full-width | Base legal LGPD |
| 51 | REG-PRIV-03 | full-width | DPO e responsabilidades |
| 52 | REG-PRIV-04 | full-width | Política de retenção |
| 53 | REG-PRIV-05 | full-width | Direito ao esquecimento |
| 54 | REG-PRIV-06 | full-width | Sub-operadores |

#### Seção G — Financeiro Detalhado

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 55 | REG-FIN-03 | full-width | Custo por componente (horizontal bars) |
| 56 | REG-FIN-04 | full-width | Projeção de receita (line chart — quando SaaS) |
| 57 | REG-FIN-07 | full-width | Financial Scenarios (grouped bar — quando cenários alternativos existirem) |

#### Seção H — Riscos e Qualidade Detalhados

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 58 | REG-RISK-02 | full-width | Riscos técnicos (tabela com severity) |
| 59 | REG-RISK-04 | full-width | Análise de viabilidade (radar 4 dimensões — Chart.js) |
| 60 | REG-QUAL-03 | full-width | Gaps identificados |
| 61 | REG-QUAL-04 | full-width | Checklist de conclusão (progress bar) |

#### Seção I — Backlog Detalhado

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 62 | REG-BACK-02 | full-width | User stories de alto nível (accordion) |
| 63 | REG-BACK-03 | full-width | Dependências entre épicos |
| 64 | REG-BACK-04 | full-width | Critérios de Go/No-Go (traffic light) |

#### Seção J — Métricas Completas

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 65 | REG-METR-01 | grid-3 | KPIs de negócio (stat cards) |
| 66 | REG-METR-02 | grid-3 | KPIs técnicos (stat cards) |
| 67 | REG-METR-03 | full-width | SLAs e SLOs (tabela com gauges) |
| 68 | REG-METR-04 | full-width | Targets por fase (timeline) |
| 69 | REG-METR-05 | grid-4 | DORA metrics (4 stat cards — quando platform) |

#### Seção K — Narrativa Completa

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 70 | REG-NARR-02 | full-width | Condições para prosseguir (checklist) |
| 71 | REG-NARR-03 | full-width | Assinaturas de aprovação (tabela formal) |

#### Seção L — Domain-Specific (condicional por context-template)

| # | Region | Layout | Quando |
|---|--------|--------|--------|
| 72 | REG-DOM-SAAS-01 | full-width | `saas` — Pricing model |
| 73 | REG-DOM-SAAS-02 | full-width | `saas` — Tenancy strategy |
| 74 | REG-DOM-DATA-01 | full-width | `datalake-ingestion` — Medallion |
| 75 | REG-DOM-DATA-02 | full-width | `datalake-ingestion` — Data quality |
| 76 | REG-DOM-INTEG-01 | full-width | `system-integration` — Mapa de integrações |
| 77 | REG-DOM-INTEG-02 | full-width | `system-integration` — Data contracts |
| 78 | REG-DOM-MIGR-01 | full-width | `migration-modernization` — Roadmap |
| 79 | REG-DOM-MIGR-02 | full-width | `migration-modernization` — AS-IS vs TO-BE |
| 80 | REG-DOM-AIML-01 | full-width | `ai-ml` — ML strategy |
| 81 | REG-DOM-AIML-02 | full-width | `ai-ml` — Model governance |
| 82 | REG-DOM-MOB-01 | full-width | `mobile-app` — Mobile strategy |
| 83 | REG-DOM-MOB-02 | full-width | `mobile-app` — Distribution |
| 84 | REG-DOM-RPA-01 | full-width | `process-automation` — Automation roadmap |
| 85 | REG-DOM-RPA-02 | full-width | `process-automation` — CoE governance |
| 86 | REG-DOM-PLAT-01 | full-width | `platform-engineering` — Platform architecture |
| 87 | REG-DOM-PLAT-02 | grid-4 | `platform-engineering` — DX metrics |
| 88 | REG-DOM-PROC-01 | full-width | `process-documentation` — Taxonomy |
| 89 | REG-DOM-PROC-02 | full-width | `process-documentation` — Governance |
| 90 | REG-DOM-MICRO-01 | full-width | `web-microservices` — Service map |
| 91 | REG-DOM-MICRO-02 | full-width | `web-microservices` — Resilience |

**Total: até 91 regions** (71 universais + até 20 domain-specific dependendo do context-template)

## Resumo por arquivo

| HTML | Regions | Chart.js? | Público |
|------|---------|-----------|---------|
| `one-pager.html` | 8 | Não | C-level, sponsor |
| `executive-report.html` | 28 | Sim (radar auditor) | Diretoria, gestão, PMO |
| `full-report.html` | 71-91 | Sim (radar, bubble, line, donut, stacked bar, grouped bar) | Time técnico, arquiteto, PO |

## Quando usar

- Entrega final do discovery para o cliente
- Documentação completa para o time que vai implementar
- Referência para sprint planning e arquitetura
- Auditoria e compliance (trilha completa do que foi decidido e por quê)
