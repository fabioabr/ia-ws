---
title: "Delivery Report — FinTrack Pro"
description: "Relatório consolidado de Discovery para o projeto FinTrack Pro — plataforma SaaS de consolidação financeira para PMEs"
project-name: fintrack-pro
author: consolidator
category: delivery
version: "01.00.000"
status: ativo
area: tecnologia
tags:
  - delivery
  - fintrack-pro
  - discovery
  - consolidado
created: "2026-04-11 14:00"
iteration: 1
---

# 📦 Delivery Report — FinTrack Pro

## 📝 Executive Summary

FinTrack Pro is a SaaS platform that automates multi-bank financial consolidation and generates AI-powered cash flow projections for small and medium enterprises (SMEs). The Discovery phase confirmed a clear market opportunity driven by Brazil's Open Finance regulation, validated the product vision across three distinct personas, and established a modular monolith architecture that fits the 5-person team. The estimated 3-year TCO is R$3.86M with a break-even point at ~220 Pro-plan subscribers. One critical compliance risk was identified — the absence of a nominated DPO — which must be resolved before launch.

---

## 📊 Project Overview

| Field | Value |
|-------|-------|
| **Project** | FinTrack Pro |
| **Client** | Confidential (startup, fintech segment) |
| **Context-Template** | SaaS |
| **Discovery Duration** | 2h10min (single joint session) |
| **Iteration** | 1 |
| **Data Source Breakdown** | Briefing 65% · Inference 25% · RAG 10% |
| **Overall Confidence** | High (no conflicts detected) |

---

## 🎯 Product Vision

### Problem

Financial managers at SMEs spend an average of **12 hours per week** manually consolidating data from multiple banks, spreadsheets, and ERPs into reports. Existing tools (Conta Azul, Nibo) lack multi-bank consolidation and intelligent projections.

### Target Audience

| Persona | Role | Frequency | Key Need |
|---------|------|-----------|----------|
| CFO / Controller | Decision-maker | 2-3x/week | Dashboards, executive reports |
| Financial Analyst | Operator | Daily (2-3h) | Reconciliation, categorization |
| CEO | Consumer | Monthly | Executive summary |

### Value Proposition

Three differentiators that no competitor currently combines:

1. **Automatic multi-bank consolidation** via Open Finance APIs (OFX/CSV)
2. **AI-powered cash flow projections** using external LLM APIs
3. **Anomaly detection alerts** for expense monitoring

### OKRs (MVP)

| # | Objective | Key Result |
|---|-----------|------------|
| 1 | Reduce consolidation time | 12h/week → 2h/week (83% reduction) |
| 2 | Achieve product-market fit | 100 paying companies in 6 months |
| 3 | Deliver excellent UX | NPS > 50 |

### Business Model

SaaS subscription with three tiers:

| Plan | Price | Includes |
|------|-------|----------|
| **Starter** | R$199/month | Up to 2 banks |
| **Pro** | R$499/month | Up to 5 banks + AI projections |
| **Enterprise** | R$999/month | Unlimited banks + API + SSO (SAML) |

> [!note] ROI for the customer
> An analyst earning R$6,000/month who saves 10h/week recovers ~R$3,750/month in productivity — the Pro plan pays for itself **7x over**.

---

## 🏢 Organization

### Team

| Role | Seniority | Count |
|------|-----------|-------|
| CTO (full-stack) | Senior | 1 |
| Backend Developer | Mid-level | 2 |
| Frontend Developer | Mid-level | 1 |
| UX Designer | Mid-level | 1 |
| **Total** | | **5** |

### Methodology

- **Framework:** Scrum — 2-week sprints
- **CI/CD:** GitHub Actions (already operational)
- **Repository:** GitHub

### Stakeholders

| Stakeholder | Authority | Involvement |
|-------------|-----------|-------------|
| CEO | Veto power on scope and prioritization | Strategic decisions |
| CTO | Operational leadership | Day-to-day execution |

---

## 🏗️ Technical Architecture

### Technology Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Node.js (TypeScript) | Team has existing expertise |
| Frontend | React | SPA approach |
| Database | PostgreSQL | AES-256 encryption at rest |
| Queue | BullMQ | Async worker for bank data ingestion |
| Cloud | AWS | Startup credits available |
| AI | External LLM API (OpenAI / Claude) | No proprietary model in MVP |

### Architecture Decision

**Modular Monolith** with 4 internal domains:

1. **Ingestion** — Bank data import via Open Finance APIs
2. **Categorization** — Intelligent transaction classification and reconciliation
3. **Projections & Alerts** — AI-powered cash flow forecasting and anomaly detection
4. **Dashboard & Reports** — Executive views and exportable reports

> [!info] Architecture rationale
> Microservices were explicitly deferred to Phase 2. With a 5-person team, a modular monolith minimizes operational overhead while maintaining clean domain boundaries.

### Integrations

| Integration | Provider | Status |
|-------------|----------|--------|
| Open Finance APIs | Belvo or Pluggy | ⚠️ Provider not yet selected |
| LLM for projections | OpenAI / Claude API | Confirmed for MVP |
| Authentication | MFA (all plans) + SSO SAML (Enterprise) | Confirmed |

### Data Refresh Strategy

- **MVP:** Batch processing every 4 hours via async worker
- **Future:** Real-time considered for Phase 2

---

## 🔐 Privacy & Security

### Data Classification

| Category | Details |
|----------|---------|
| **Classification** | Personal sensitive data (financial) |
| **Data collected** | Name, CPF/CNPJ, bank details (branch, account, balance, transactions), email, phone |
| **Legal basis** | Explicit consent via Open Finance flow (managed by banks) |
| **Retention** | Active while subscriber + 90 days post-cancellation + full anonymization |

### Encryption

| Layer | Standard |
|-------|----------|
| At rest | AES-256 (PostgreSQL) |
| In transit | TLS 1.3 |

### DPO Status

> [!danger] Critical compliance risk
> **No DPO has been nominated.** LGPD requires a Data Protection Officer for organizations processing sensitive personal data at scale. Nomination is planned for Q3 but **must occur before product launch**.

---

## 💰 Financial Analysis

### Build vs Buy Decision

| Alternative | Verdict | Rationale |
|-------------|---------|-----------|
| **Buy** (Conta Azul Enterprise) | ❌ Rejected | No native Open Finance, no AI projections |
| **Adapt** (Metabase + Open Finance API) | ❌ Rejected | Manual categorization remains; no competitive edge |
| **Build** (FinTrack Pro custom) | ✅ Selected | Core differentiator (AI + Open Finance) cannot be outsourced |

### TCO — 3-Year Projection

| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| Team (5 people) | R$900,000 | R$990,000 | R$1,089,000 | R$2,979,000 |
| AWS Infrastructure | R$36,000 | R$60,000 | R$84,000 | R$180,000 |
| Open Finance API | R$24,000 | R$36,000 | R$48,000 | R$108,000 |
| LLM API (projections) | R$12,000 | R$24,000 | R$36,000 | R$72,000 |
| Licenses (misc) | R$6,000 | R$6,000 | R$6,000 | R$18,000 |
| Contingency (15%) | R$146,700 | R$167,400 | R$189,450 | R$503,550 |
| **Total** | **R$1,124,700** | **R$1,283,400** | **R$1,452,450** | **R$3,860,550** |

### Break-Even Analysis

- **Largest cost driver:** Team salaries (77% of TCO)
- **Break-even point:** ~220 clients on the Pro plan (R$499/month)
- **Assumption:** 10% annual salary increase; infrastructure costs scale with client growth

---

## ✅ Quality Gates

### Audit Score

| Dimension | Score | Notes |
|-----------|-------|-------|
| Completeness | ⭐⭐⭐⭐ | All 8 interview blocks completed |
| Data sourcing | ⭐⭐⭐ | 25% inference-based — requires human validation |
| Conflicts | ⭐⭐⭐⭐⭐ | Zero conflicts detected |
| Risk coverage | ⭐⭐⭐⭐ | 1 critical risk identified (DPO) |

### 10th-Man Challenge

| Challenge Area | Finding |
|----------------|---------|
| Open Finance dependency | If Belvo/Pluggy APIs change pricing or terms, the entire ingestion module is at risk. Recommend dual-provider strategy. |
| LLM cost projection | R$12K→R$36K assumes linear growth, but token costs may spike with complex projections. Budget a 30% buffer. |
| Team size | 5 people for a fintech MVP with compliance requirements is tight. Any attrition delays the timeline significantly. |

---

## ⚠️ Risks & Recommendations

| # | Risk | Severity | Recommendation |
|---|------|----------|----------------|
| 1 | No DPO nominated | 🔴 Critical | Nominate before launch (LGPD requirement) |
| 2 | Open Finance provider undecided | 🟡 Medium | Evaluate Belvo vs Pluggy by Sprint 2; design adapter pattern for portability |
| 3 | Minimum bank count undefined | 🟡 Medium | Clarify with stakeholder: is 2 banks the MVP floor or 5? |
| 4 | Single-point-of-failure (CTO) | 🟡 Medium | Document architectural decisions; cross-train at least one backend dev |
| 5 | LLM API cost variance | 🟢 Low | Monitor token usage monthly; set billing alerts at 120% of budget |

---

## 📋 MVP Scope

| Module | Feature | Priority | Sprint |
|--------|---------|----------|--------|
| Ingestion | OFX/CSV file upload | P0 | 1-2 |
| Ingestion | Open Finance API integration (1 provider) | P0 | 2-4 |
| Categorization | Auto-categorization of transactions | P0 | 3-5 |
| Dashboard | Executive dashboard (CFO view) | P0 | 4-6 |
| Projections | AI cash flow forecast (30/60/90 days) | P1 | 5-7 |
| Alerts | Anomaly detection on expenses | P1 | 6-8 |
| Reports | Monthly PDF export | P1 | 7-8 |
| Auth | MFA for all plans | P0 | 1-2 |
| Auth | SSO (SAML) for Enterprise | P2 | 8+ |

---

## 🚀 Next Steps

1. **Nominate DPO** — Critical path for LGPD compliance before launch
2. **Select Open Finance provider** — Belvo vs Pluggy technical evaluation (Sprint 1-2)
3. **Define minimum bank count** — Clarify MVP floor with CEO (Human Review pending)
4. **Begin Sprint 1** — Focus on auth (MFA) + ingestion module foundation
5. **Schedule Human Review** — Validate all inference-based data points (25% of dataset)
6. **Set up monitoring** — AWS cost alerts + LLM API usage tracking from day one

---

> **Document generated by:** consolidator agent
> **Pipeline:** Discovery-to-Go v01 | **Pack:** SaaS | **Iteration:** 1
> **Timestamp:** 2026-04-11 14:00
