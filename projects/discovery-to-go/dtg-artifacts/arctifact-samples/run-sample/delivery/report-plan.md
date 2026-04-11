---
title: "Report Plan — FinTrack Pro"
project-name: fintrack-pro
version: 01.00.000
status: gerado
author: report-planner
category: delivery
created: 2026-04-11
source: delivery-report.md
blueprint: saas-discovery-blueprint.md
total-regions: 22
chart-js-required: true
---

# Report Plan — FinTrack Pro

## Summary

| Metric | Value |
|--------|-------|
| **Source** | delivery-report.md |
| **Total regions** | 22 |
| **Chart.js regions** | 2 (REG-FIN-01, REG-QUAL-01) |
| **HTML/CSS only regions** | 20 |
| **Layout types** | full-width (20), grid-2 (1), sidebar (1) |

---

## Per-Section Plan

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|--------------|
| 1 | REG-EXEC-01 | full-width | Hero card com callouts | HTML/CSS | Card destaque com metricas-chave: TCO R$3.86M, break-even 220 Pro-plan, 1 risco critico (DPO) |
| 2 | REG-EXEC-02 | full-width | Card com secoes | HTML/CSS | Tabela key-value estilizada com 7 campos do projeto |
| 3 | REG-PROD-01 | full-width | Card com metrica destacada | HTML/CSS | Metrica hero: 12h/semana, problema central com comparativo de ferramentas |
| 4 | REG-PROD-02 | grid-2 | Persona cards | HTML/CSS | 3 persona cards: CFO/Controller, Financial Analyst, CEO — com role, frequencia, necessidade |
| 5 | REG-PROD-05 | full-width | Progress bars + stat cards | HTML/CSS | 3 diferenciadores como stat cards + 3 OKRs com progress bars (83% reducao, 100 empresas, NPS>50) |
| 6 | REG-PROD-06 | full-width | Pricing table | HTML/CSS | 3 tiers: Starter R$199, Pro R$499, Enterprise R$999 — com callout ROI 7x |
| 7 | REG-DOM-SAAS-01 | full-width | Pricing table | HTML/CSS | Subregiao de REG-PROD-06 — mesma pricing table com destaque SaaS tiers |
| 8 | REG-ORG-01 | full-width | Tabela com badges | HTML/CSS | 5 membros do time com badges de seniority (Senior, Mid-level) |
| 9 | REG-ORG-02 | full-width | Tabela estilizada | HTML/CSS | Metodologia (Scrum 2-week) + stakeholders com authority badges |
| 10 | REG-TECH-01 | full-width | Tabela com badges | HTML/CSS | 6 camadas do stack com badges de tecnologia e notas |
| 11 | REG-TECH-02 | full-width | Tabela estilizada | HTML/CSS | 3 integracoes com status badges (confirmado/pendente) + data refresh strategy |
| 12 | REG-TECH-03 | full-width | Card placeholder diagrama | HTML/CSS | Modular monolith com 4 dominios — placeholder para diagrama de arquitetura |
| 13 | REG-TECH-06 | full-width | Tabela com verdict badges | HTML/CSS | 3 alternativas Build vs Buy com badges: Rejected (vermelho), Selected (verde) |
| 14 | REG-SEC-01 | full-width | Tabela com badges coloridos | HTML/CSS | 2 camadas de criptografia: AES-256 at rest, TLS 1.3 in transit |
| 15 | REG-SEC-02 | full-width | Card com checklist | HTML/CSS | Alerta critico DPO — card vermelho com status e acao requerida |
| 16 | REG-PRIV-01 | full-width | Tabela com badges | HTML/CSS | 4 categorias de dados: classificacao, dados coletados, base legal, retencao |
| 17 | REG-FIN-01 | full-width | Stacked bar chart + stat card | Chart.js + HTML/CSS | Chart.js stacked bar 3 anos (Team, AWS, API, LLM, Licenses, Contingency) + stat card break-even 220 clientes |
| 18 | REG-RISK-01 | full-width | Tabela com severity badges | HTML/CSS | 5 riscos com badges: Critical (vermelho), Medium (amarelo), Low (verde) |
| 19 | REG-QUAL-01 | sidebar | Radar chart 5 eixos | Chart.js | Chart.js radar com 4 dimensoes: Completeness(4), Data sourcing(3), Conflicts(5), Risk coverage(4) |
| 20 | REG-QUAL-02 | full-width | Cards com severity badges | HTML/CSS | 3 challenge cards: Open Finance dependency, LLM cost, Team size |
| 21 | REG-BACK-01 | full-width | Tabela com priority badges | HTML/CSS | 9 features com badges P0/P1/P2 e sprint timeline |
| 22 | REG-EXEC-04 | full-width | Tabela com priority badges + timeline | HTML/CSS | 6 next steps com prioridade e timeline badges |
