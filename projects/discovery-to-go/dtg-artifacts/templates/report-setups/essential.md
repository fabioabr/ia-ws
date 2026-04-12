---
title: "Report Setup — Essencial"
description: "Setup minimalista: gera apenas o One-Pager HTML com escopo, decisão e próximos passos. Para apresentações rápidas a C-level e comitês de investimento."
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: report-setup
area: tecnologia
tags:
  - report-setup
  - essential
  - one-pager
created: 2026-04-11
---

# Report Setup — Essencial

Setup minimalista que gera **um único HTML** (`one-pager.html`) com as informações mais executivas do discovery. Pensado para apresentações rápidas a C-level, comitês de investimento e stakeholders que precisam de visão completa em 2 minutos.

## Outputs

| Arquivo | Conteúdo |
|---------|----------|
| `one-pager.html` | Página única com escopo, decisão, custos e próximos passos |

## Regions incluídas

### One-Pager

| # | Region | Layout | O que mostra |
|---|--------|--------|-------------|
| 1 | REG-EXEC-01 | full-width | Overview executivo — problema, proposta, TCO resumido, top 3 riscos, recomendação Build vs Buy |
| 2 | REG-PROD-07 | full-width | Escopo — objetivo, o que será feito (dentro), o que NÃO será feito (fora) |
| 3 | REG-PROD-01 | full-width | Problema e contexto — descrição da dor com métrica de impacto |
| 4 | REG-FIN-01 | grid-3 | TCO 3 anos — stat card com valor total + faixa de sensibilidade |
| 5 | REG-RISK-01 | grid-3 | Top 3 riscos — badges com severidade |
| 6 | REG-EXEC-03 | grid-3 | Go/No-Go — badge de veredicto (prosseguir/pivotar/cancelar) |
| 7 | REG-FIN-05 | full-width | Estimativa de esforço — T-shirt sizing resumido |
| 8 | REG-EXEC-04 | full-width | Próximos passos — ações imediatas com responsável e prazo |

**Total: 8 regions**

## Quando usar

- Reunião de comitê de investimento (15 minutos)
- Primeiro contato com sponsor que não participou do discovery
- Apresentação em slide deck (abrir HTML no navegador)
- Resumo para enviar por email ao board
