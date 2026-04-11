---
region-id: REG-TECH-05
title: "Architecture Decision Records"
group: technical
description: "Registro de decisões arquiteturais com contexto, alternativas e consequências"
source: "Bloco #5/#7 (arch)"
schema: "Lista de ADRs (contexto, decisão, alternativas, consequências)"
template-visual: "Accordion por ADR"
default: false
---

# Architecture Decision Records

Registra as decisões arquiteturais significativas do projeto no formato ADR. Cada registro documenta o contexto, a decisão tomada, as alternativas consideradas e as consequências esperadas, criando um histórico rastreável que evita re-discussões e facilita onboarding.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | string | Identificador sequencial (ADR-001, ADR-002...) |
| título | string | Nome descritivo da decisão |
| status | enum | Proposta, Aceita, Substituída, Depreciada |
| contexto | texto | Situação que motivou a decisão |
| decisão | texto | O que foi decidido |
| alternativas | lista | Opções avaliadas e motivo da rejeição |
| consequências | texto | Impactos positivos e negativos esperados |

## Exemplo

### ADR-001 — Adotar PostgreSQL como banco principal

**Status:** Aceita

**Contexto:** O FinTrack Pro precisa de um banco relacional com suporte a transações ACID para operações financeiras, capacidade de lidar com dados semi-estruturados (JSON) e ecossistema maduro de ferramentas.

**Decisão:** Utilizar PostgreSQL 16 como banco de dados principal, hospedado em AWS RDS com Multi-AZ.

**Alternativas consideradas:**
- **MySQL 8** — descartado por suporte inferior a JSON e funcionalidades analíticas
- **MongoDB** — descartado por falta de garantias ACID nativas em transações multi-documento no contexto financeiro
- **CockroachDB** — descartado por custo elevado e complexidade operacional para o volume atual

**Consequências:**
- (+) Garantias ACID robustas para operações financeiras
- (+) Suporte nativo a JSONB para dados flexíveis de configuração
- (+) Amplo ecossistema de ferramentas e profissionais
- (-) Escalabilidade horizontal limitada — sharding manual se ultrapassar 1TB
