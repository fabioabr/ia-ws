---
title: "Iteration Policy"
description: Política de iteração do pipeline de discovery
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: customization
area: tecnologia
tags:
  - customization
  - iteration
  - policy
created: 2026-04-11 09:00
---

# Iteration Policy

> Usando política padrão. Nenhum override aplicado para este run.

## Regras de Iteração

| Parâmetro | Valor |
|-----------|-------|
| Máximo de iterações | 3 |
| Critério de re-iteração | Score abaixo de 70% ou HR decide "Refazer" |
| Fases re-executáveis | 1 (Discovery) e 2 (Analysis) |
| Fase 3 (Delivery) | Executada uma única vez após aprovação |

## Fluxo de Decisão

1. Fase concluída -> HR Review
2. HR escolhe: **Avançar**, **Refazer fase**, ou **Abortar**
3. Se "Refazer": nova iteração com contexto acumulado
4. Se "Abortar": run encerrado, artefatos parciais preservados
