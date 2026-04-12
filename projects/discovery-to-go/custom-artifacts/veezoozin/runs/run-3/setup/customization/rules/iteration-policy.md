---
title: Iteration Policy — Default
description: Política de iteração padrão do Discovery Pipeline. Define max iterações, threshold de estagnação, comportamento default do HR Loop e regras de Abort. Projetos podem customizar localmente.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: customization
area: tecnologia
tags:
  - customization
  - iteration
  - hr-loop
  - orchestrator
  - pipeline-v05
created: 2026-04-10
---

# Iteration Policy — Default

> [!info] Como este arquivo é usado
> O `orchestrator` lê este arquivo (ou a cópia local em `{projeto}/setup/customization/rules/`) para determinar **limites de iteração, comportamento do HR Loop e regras de estagnação**. Se o arquivo não existir, usa os defaults hardcoded no SKILL.md.

---

## 1. Limites de iteração

| Parâmetro | Valor padrão | Descrição |
|---|---|---|
| `max-iterations` | `0` (sem limite) | Número máximo de iterações completas (Round 1 → Round 3). `0` = sem cap numérico. |
| `stagnation-threshold` | `10%` | Se o crescimento de contexto entre iterações for < este valor, orchestrator emite alerta de estagnação. |
| `stagnation-consecutive` | `2` | Quantas iterações consecutivas abaixo do threshold antes de forçar pausa para decisão humana. |

---

## 2. HR Loop (Iteration Control)

| Parâmetro | Valor padrão | Descrição |
|---|---|---|
| `hr-loop-default-answer` | `Re-executar desde a 1ª fase` | Resposta padrão quando nenhuma opção é marcada. "Re-executar desde a 1ª fase" = mais conservador, "Avançar para a próxima fase" = mais rápido. |
| `hr-loop-max-passes` | `0` (sem limite) | Max passagens do HR Loop dentro de um mesmo round. `0` = sem limite, humano decide quando parar. |
| `hr-loop-log-each-pass` | `true` | Registrar cada passagem do loop em `logs/hr-loop-{round}-{pass}.md`. |

---

## 3. Abortar

| Parâmetro | Valor padrão | Descrição |
|---|---|---|
| `abort-requires-justification` | `true` | Humano deve justificar por que está abortando (vs re-executar). |
| `abort-generates-change-request` | `true` | Orchestrator gera change request formal + Update State na Pipeline Memory. |
| `abort-requires-confirmation` | `true` | Humano deve usar `@` ao invés de `X` para confirmar o abort. |

---

## 4. Comportamento entre iterações (pós Abortar)

| Parâmetro | Valor padrão | Descrição |
|---|---|---|
| `partial-rework` | `true` | Iteração seguinte herda drafts intactos e revisita apenas pontos marcados. Se `false`, recomeça do zero. |
| `mandatory-awareness` | `true` | Todos os agentes recebem ciência do change request no início da nova iteração (D3 do blueprint). |
| `auto-restart` | `false` | Se `true`, orchestrator inicia a nova iteração automaticamente após abort (sem esperar comando humano). Padrão = espera. |

---

## 5. Combinações típicas

### Projeto conservador (cliente exigente, stakeholders múltiplos)
```
hr-loop-default-answer: Re-executar desde a 1ª fase
hr-loop-max-passes: 0
abort-requires-justification: true
partial-rework: true
auto-restart: false
```
*O humano revisa múltiplas vezes por round, abort é formal (requer `@` + justificativa), e o pipeline nunca avança sem comando explícito.*

### POC/spike (velocidade > rigor)
```
hr-loop-default-answer: Avançar para a próxima fase
hr-loop-max-passes: 2
abort-requires-justification: false
partial-rework: true
auto-restart: true
```
*O HR Loop passa rápido (default "Avançar para a próxima fase", máx 2 passes), abort é informal, e o pipeline reinicia automaticamente.*

---

## Changelog

| Versão | Data | Descrição |
|---|---|---|
| 01.00.000 | 2026-04-10 | Versão inicial. Parâmetros de iteração, HR Loop e Hard Rejection. 2 combinações típicas. |
| 02.00.000 | 2026-04-10 | Novas opções de decisão do HR Loop: Re-executar desde a 1ª fase (padrão), Re-executar a última fase, Avançar para a próxima fase, Abortar (com @). "Hard Rejection" renomeado para "Abortar". |
