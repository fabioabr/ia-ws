---
title: "Report Setup — Essencial"
description: "Setup de orçamento: gera o One-Pager HTML com descritivo, escopo, premissas, riscos, equipe, estimativa de esforço, planejamento e confiança. Sem valores monetários — apenas horas e semanas. Página única sem tabs."
project-name: discovery-to-go
version: 03.00.000
status: ativo
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - essential
  - one-pager
  - time-estimate
  - budget
created: 2026-04-11
updated: 2026-04-12
---

# Report Setup — Essencial

Setup focado em **orçamento de projeto** que gera um único HTML (`one-pager.html`) — página contínua sem tabs. Apresenta o que será feito, sob quais condições, quem faz, quanto tempo leva e quão confiável é a estimativa. Sem valores monetários — apenas horas e semanas.

Lógica da ordem: **o quê** (1-2) → **sob quais condições e riscos** (3-4) → **quem e quanto** (5-6) → **quando** (7) → **quão confiável** (8).

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única contínua (SEM tabs) com 8 seções |

## Regions incluídas

### One-Pager (8 seções)

| # | Seção | Region | Layout | O que mostra |
|---|-------|--------|--------|-------------|
| 1 | Descritivo | REG-EXEC-01 | full-width | Nome do projeto, objetivo (1 frase), contexto (2-3 frases), cliente |
| 2 | Escopo | REG-PROD-07 | full-width | IN (o que será feito) vs OUT (o que NÃO será feito) — split card verde/vermelho |
| 3 | Premissas | REG-EXEC-07 (novo) | full-width | Condições assumidas para as estimativas (BYOK, pay-per-use, 1 dev, etc.) |
| 4 | Riscos principais | REG-RISK-01 | full-width | Top 3-5 riscos com impacto no prazo/custo — tabela compacta com severity badges |
| 5 | Equipe e Papéis | REG-ORG-02 | full-width | Quem faz o quê, dedicação, horas/semana por papel |
| 6 | Estimativa de esforço | REG-FIN-06 | grid-3 | Stat cards: total de horas por papel + total geral + duração em semanas |
| 7 | Planejamento | REG-PLAN-01 | full-width | Gantt relativo (Semana 1, 2, ..., N) com fases e marcos — HTML/CSS barras horizontais |
| 8 | Confiança dos Auditores IA | REG-QUAL-01 + REG-QUAL-02 | grid-2 | Scores compactos: auditor (nota + status) e 10th-man (questões + severidade) |

**Total: 8 seções (9 regions)**

## Notas de renderização

### Seção 1 — Descritivo (REG-EXEC-01 simplificado)

Card informativo com:
- **Projeto:** Nome do projeto
- **Cliente:** Nome do cliente
- **Objetivo:** 1 frase clara do que se pretende alcançar
- **Contexto:** 2-3 frases sobre o problema e a solução proposta

Omitir: TCO, top 3 riscos, recomendação Build vs Buy, próximo passo (esses vão em seções próprias).

### Seção 2 — Escopo (REG-PROD-07)

Split card com duas colunas:
- **DENTRO** (check verde) — lista do que será feito
- **FORA** (X vermelho) — lista explícita do que NÃO será feito

Omitir: hipótese central, critérios go/no-go.

### Seção 3 — Premissas (REG-EXEC-07 — novo)

Lista de premissas que sustentam as estimativas. Formato: bullets com ícone de atenção.

Exemplos:
- "LLM é BYOK — custo de chamadas é do tenant, não do Veezoozin"
- "Infraestrutura GCP pay-per-use — custo escala com uso"
- "Equipe de 1 pessoa usando Claude Code como assistente"
- "MVP em 3-4 meses com escopo reduzido"
- "Sem contratação adicional no MVP"

> [!warning] Se qualquer premissa mudar, as estimativas precisam ser recalculadas.

### Seção 4 — Riscos principais (REG-RISK-01 compacto)

Tabela compacta com top 3-5 riscos:

| Risco | Impacto no prazo | Severidade |
|-------|-----------------|------------|

Omitir: mitigação detalhada, probabilidade numérica. Foco em: o que pode dar errado e como afeta o prazo/custo.

### Seção 5 — Equipe e Papéis (REG-ORG-02 adaptado)

Tabela com:

| Papel | Quem | Dedicação | Horas/semana |
|-------|------|-----------|-------------|

Incluir: todos os papéis necessários (dev, design, PO, QA, etc.) mesmo que sejam a mesma pessoa.

### Seção 6 — Estimativa de esforço (REG-FIN-06)

Stat cards em grid:
- Um card por papel (ex: "Arquitetura: 120h", "Backend: 320h", "Frontend: 160h")
- Um card destacado com o **total geral** (ex: "Total: 680h")
- Um card com **duração total** (ex: "16 semanas")

### Seção 7 — Planejamento (REG-PLAN-01)

Gantt relativo com barras horizontais HTML/CSS:
- Eixo X em semanas (Semana 1, 2, ..., N) — sem datas fixas
- Barras por fase/atividade macro
- Marcos (milestones) destacados
- Cores por tipo de atividade

### Seção 8 — Confiança dos Auditores IA (REG-QUAL-01 + REG-QUAL-02 compacto)

Dois stat cards lado a lado:
- **Auditor:** Score geral + status (aprovado/reprovado/ressalvas)
- **10th-man:** Nº de questões residuais + severidade máxima

Nota de rodapé: "Material gerado com X% de dados do briefing, Y% inferidos pelo especialista"

Omitir: radar chart, detalhamento por dimensão (esses vão no report executive).

## Quando usar

- Proposta comercial rápida (sponsor quer saber "quanto tempo e quem")
- Dimensionamento de equipe e prazo para capacity planning
- Kick-off de projeto quando escopo está definido mas precisa alinhar esforço
- Comparação de projetos em portfólio (formato padronizado)
