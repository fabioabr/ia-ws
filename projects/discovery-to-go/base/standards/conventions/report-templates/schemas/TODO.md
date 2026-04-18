---
title: Template Filters TODO
description: Controle de filtros :variant implementados vs pendentes por REG-ID. Atualizar sempre que um filtro novo for introduzido em algum template, antes de usar efetivamente.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: tracking
area: tecnologia
tags:
  - todo
  - filters
  - variants
  - report-templates
  - parser
created: 2026-04-17
updated: 2026-04-17
---

# Template Filters TODO

Controle dos filtros `:variant` que os templates usam sobre regions do catalogo. O report-composer precisa saber como aplicar cada filtro. Esta lista e o **source of truth** do que ja tem suporte e do que falta.

> [!info] Fluxo de trabalho
> 1. Autor de template quer usar um novo filtro `REG-X:novofiltro`
> 2. Registra aqui com status `pendente` e descricao do que o filtro deve fazer
> 3. Implementa a logica no report-composer (ou no schema da region)
> 4. Move o status para `implementado` e atualiza a data

## Legenda de status

- `implementado` — filtro funciona no composer
- `pendente` — filtro declarado mas ainda nao implementado
- `usado-por` — templates que consomem este filtro

## Filtros por REG-ID

### REG-EXEC-02 (Product Brief)

_Nenhum filtro registrado._

### REG-EXEC-04 (Proximos Passos)

_Nenhum filtro registrado._

### REG-FIN-01 (TCO 3 Anos)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:total` | pendente | Renderizar apenas o valor total do TCO como stat card unico (sem breakdown por ano/categoria) | `basic` |

### REG-FIN-06 (Total Hours)

_Sem filtro — a region ja e um stat-cards grid por natureza. Usada direta._

### REG-FIN-07 (Cenarios Financeiros)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:principal` | pendente | Renderizar apenas o cenario recomendado (nao o comparativo completo) | `basic` (via SUB-SCENARIO) |
| `:enxuto` | pendente | Renderizar apenas o cenario enxuto | `basic` (via SUB-SCENARIO) |
| `:expandido` | pendente | Renderizar apenas o cenario expandido | `basic` (via SUB-SCENARIO) |

> Nota: na spec o valor e `recomendado`, mas o nome original da region usa `principal`. Padronizar para `recomendado` no momento da implementacao.

### REG-NARR-02 (Condicoes para Prosseguir)

_Nenhum filtro registrado._

### REG-ORG-01 (Mapa de Stakeholders)

_Nenhum filtro registrado._

### REG-ORG-02 (Estrutura de Equipe)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:count` | pendente | Renderizar apenas o numero total de pessoas da equipe como stat card | `basic` |

### REG-PROD-01 (Problema e Contexto)

_Nenhum filtro registrado._

### REG-PROD-04 (Proposta de Valor)

_Nenhum filtro registrado._

### REG-PROD-05 (OKRs e ROI)

_Nenhum filtro registrado._

### REG-PROD-07 (Escopo)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:in` | pendente | Renderizar apenas a coluna "DENTRO DO ESCOPO" | — (reservado) |
| `:out` | pendente | Renderizar apenas a coluna "FORA DO ESCOPO" | — (reservado) |

### REG-QUAL-01 (Score do Auditor)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:score` | pendente | Renderizar apenas o score geral como stat card (sem radar chart) | `basic` |

### REG-RISK-01 (Matriz de Riscos)

| Filtro | Status | Descricao | Usado-por |
|--------|--------|-----------|-----------|
| `:top5` | pendente | Renderizar apenas os 5 riscos de maior severidade | `basic` |

## Variantes de Sub-Templates

### SUB-SCENARIO (template basic)

| Variante | Status | Descricao |
|----------|--------|-----------|
| `recomendado` | pendente | Cenario base recomendado (sempre inline) |
| `enxuto` | pendente | Cenario com escopo reduzido |
| `expandido` | pendente | Cenario com escopo ampliado |

## Variaveis globais de setup

| Variavel | Status | Descricao |
|----------|--------|-----------|
| `scenarios: all` | pendente | Expande para `[recomendado, enxuto, expandido]` |
| `scenarios: [list]` | pendente | Lista explicita de cenarios a gerar como tabs |

## Resumo

- Total de filtros declarados: **11**
- Implementados: **0**
- Pendentes: **11**

Atualizar este resumo a cada mudanca de status.
