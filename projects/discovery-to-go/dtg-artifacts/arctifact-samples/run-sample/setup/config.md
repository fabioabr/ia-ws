---
title: "Iteration Setup — FinTrack Pro"
description: Configuração da iteração 1 do pipeline de discovery para o projeto FinTrack Pro
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: setup
area: tecnologia
tags:
  - setup
  - iteracao
  - pipeline
  - fintrack-pro
  - saas
created: 2026-04-11 09:00
iteration: 1
---

# Iteration Setup — FinTrack Pro

## Iteração

| Campo | Valor |
|-------|-------|
| Iteração | 1 |
| Run | run-2 |
| Knowledge Pack | saas |
| Origem | Briefing do cliente (briefing.md) |
| Objetivo | Discovery completo do MVP FinTrack Pro |

---

## Objetivos da Iteração

1. Extrair requisitos completos do projeto a partir do briefing
2. Validar viabilidade técnica e arquitetura macro
3. Mapear riscos de segurança e LGPD (dados financeiros sensíveis)
4. Produzir relatório de discovery consolidado

---

## Plano de Execução

### Fase 1 — Discovery

Reunião conjunta temática com blocos sequenciais. O **po** conduz os blocos de negócio, o **solution-architect** conduz tecnologia e TCO, o **cyber-security-architect** conduz LGPD e segurança.

**Blocos planejados:**
1. Visão e Propósito
2. Personas e Jornada
3. Valor Esperado / OKRs
4. Processo, Negócio e Equipe
5. Tecnologia e Segurança
6. LGPD e Privacidade
7. Arquitetura Macro
8. TCO e Build vs Buy

**Output:** `iteration-1/logs/interview.md`

### Fase 2 — Analysis

Scoring dos dados coletados, validação de completude, classificação de riscos, verificação de dados inferidos vs. confirmados.

**Output:** `iteration-1/memory/analysis.md`

### Fase 3 — Delivery

Geração do relatório final de discovery consolidado a partir dos dados validados.

**Output:** `delivery/report.md`

---

## Agentes Envolvidos

| Agente | Fases | Papel |
|--------|-------|-------|
| orchestrator | 1, 2, 3 | Mediação, controle de estado, HR loop |
| po | 1, 2 | Visão de produto, personas, valor, OKRs |
| solution-architect | 1, 2 | Arquitetura, stack, TCO, build vs buy |
| cyber-security-architect | 1, 2 | LGPD, segurança, compliance |
| customer | 1 | Cliente simulado (responde com base no briefing) |
| report-writer | 3 | Geração do relatório final |

---

## Customização

| Arquivo | Caminho |
|---------|---------|
| Estrutura do relatório | `customization/delivery-report-structure.md` |
| Thresholds de scoring | `customization/scoring-thresholds.md` |
| Política de iteração | `customization/iteration-policy.md` |
| Template de HR loop | `customization/hr-loop-template.md` |

Todos usando configuração padrão (sem overrides para este run).

---

## Knowledge Pack

| Arquivo | Caminho |
|---------|---------|
| Contexto SaaS | `kb/context/saas.md` |
| Especialistas SaaS | `kb/context/saas-specialists.md` |
