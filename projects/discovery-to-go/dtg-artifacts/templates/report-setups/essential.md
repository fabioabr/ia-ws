---
title: "Report Setup — Essencial"
description: "Setup de estimativa de tempo: gera o One-Pager HTML com descritivo do projeto, qualidade, escopo, atividades com esforço em horas, planejamento relativo e totais. Sem valores monetários — apenas horas e semanas."
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - essential
  - one-pager
  - time-estimate
created: 2026-04-11
updated: 2026-04-11
---

# Report Setup — Essencial

Setup focado em **estimativa de tempo** que gera um único HTML (`one-pager.html`) com as informações necessárias para dimensionar esforço e planejamento do projeto. Sem valores monetários — apenas horas e semanas. Pensado para apresentações a gestores de projeto, tech leads e sponsors que precisam entender escopo, esforço e cronograma relativo em 2 minutos.

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única com descritivo, qualidade, escopo, atividades/esforço, planejamento e totais |

## Regions incluídas

### One-Pager

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 1 | REG-EXEC-01 | full-width | Descritivo do projeto — descrição, objetivo, premissas, responsáveis (simplificado, sem TCO/riscos/Build vs Buy) |
| 2 | REG-QUAL-01 + REG-QUAL-02 | grid-2 | Qualidade e confiança — stat cards compactos com score do auditor e questões do 10th-man (sem radar chart) |
| 3 | REG-PROD-07 | full-width | Escopo — split card dentro/fora (sem hipótese central nem critérios go/no-go) |
| 4 | REG-BACK-01 | full-width | Atividades e esforço — tabela com papéis, horas estimadas e coluna valor/hora vazia (preenchida pelo cliente) |
| 5 | REG-PLAN-01 | full-width | Planejamento — Gantt relativo (Semana 1, 2, ..., N) sem datas fixas, HTML/CSS |
| 6 | REG-FIN-06 | grid-3 | Totais — stat cards com total de horas por papel e total geral |

**Total: 6 blocos (7 regions)**

## Notas de renderização

### Bloco 1 — Descritivo do Projeto (REG-EXEC-01 simplificado)

Renderizar apenas os campos:
- **Descrição:** O que é o projeto
- **Objetivo:** O que se pretende alcançar
- **Premissas:** Condições assumidas para as estimativas
- **Responsáveis:** Product Owner, Tech Lead, Sponsor

Omitir: TCO, top 3 riscos, recomendação Build vs Buy.

### Bloco 2 — Qualidade e Confiança (REG-QUAL-01 + REG-QUAL-02)

Renderizar como stat cards compactos lado a lado:
- REG-QUAL-01: Score geral do auditor + status (aprovado/reprovado)
- REG-QUAL-02: Quantidade de questões residuais do 10th-man + severidade máxima

Omitir: radar chart, detalhamento por dimensão.

### Bloco 3 — Escopo (REG-PROD-07)

Renderizar apenas:
- Lista "dentro do escopo" (check verde)
- Lista "fora do escopo" (X vermelho)

Omitir: hipótese central, critérios go/no-go.

### Bloco 4 — Atividades e Esforço (REG-BACK-01 adaptado)

Renderizar como tabela com colunas:
| Atividade | Papel | Horas estimadas | Valor/hora |
A coluna **Valor/hora** fica vazia — é preenchida manualmente pelo cliente ou comercial.

### Bloco 5 — Planejamento (REG-PLAN-01)

Gantt relativo com barras horizontais por atividade. Eixo X em semanas (Semana 1, 2, ..., N). Sem datas fixas. HTML/CSS puro.

### Bloco 6 — Totais (REG-FIN-06)

Stat cards em grid:
- Um card por papel (ex: "Backend: 320h", "Frontend: 240h", "QA: 120h")
- Um card destacado com o total geral (ex: "Total: 680h")

## Quando usar

- Apresentação de estimativa de esforço para sponsor ou cliente
- Proposta comercial onde o cliente define os valores/hora
- Dimensionamento de time e prazo para planejamento de capacity
- Kick-off de projeto quando já se sabe o escopo mas precisa alinhar esforço
