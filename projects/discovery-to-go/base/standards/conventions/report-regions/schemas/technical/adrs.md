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

## Representação Visual

### Dados de amostra

| ID | Título | Status | Data | Decisão (resumo) |
|----|--------|--------|------|-------------------|
| ADR-001 | Adotar PostgreSQL como banco principal | Aceita | 2025-01 | PostgreSQL 16 em AWS RDS Multi-AZ para garantias ACID e suporte a JSONB |
| ADR-002 | Autenticação via Okta (SSO) | Aceita | 2025-01 | Uso da licença corporativa existente, SAML 2.0 / OIDC |
| ADR-003 | SQS como fila de mensagens | Aceita | 2025-02 | Serverless, volume atual não justifica Kafka |
| ADR-004 | Puppeteer para geração de PDF | Aceita | 2025-02 | Flexibilidade de layout, custo zero de licença |

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Cards em accordion (expansíveis/colapsáveis)
**Tecnologia:** HTML/CSS
**Justificativa:** ADRs contêm blocos de texto estruturado (contexto, decisão, alternativas, consequências) que não cabem em células de tabela nem se traduzem em gráficos. Accordions com badges de status permitem navegação limpa entre múltiplas decisões sem poluição visual.
**Alternativa:** Tabela resumo (HTML/CSS) — quando se precisa apenas de uma visão consolidada (ID, título, status, data) sem o conteúdo completo de cada ADR.
