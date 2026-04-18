---
title: "Executive Layout — estrutura mínima do entregável EX"
description: "Piso determinístico que o deliverable-distiller deve respeitar ao produzir o Executive Report (EX) a partir do Delivery Report"
target-deliverable: "EX"
version: "01.00.000"
status: "draft"
origin: "ADR-001 — Entregáveis hierárquicos OP ⊂ EX ⊂ DR"
extends: "one-pager-layout.md"
---

# Executive Layout

Define a **estrutura mínima** que o entregável **Executive Report (EX)** deve ter. O EX é o **superconjunto do OP** — inclui todas as regions do OP mais contexto técnico e de negócio suficiente para suportar uma decisão de comitê executivo.

## Propósito

O EX é um relatório de **5-15 páginas** voltado para comitês executivos que precisam de contexto suficiente para aprovar (ou não) o avanço do projeto. Inclui contexto de negócio, proposta de valor, arquitetura macro, análise de viabilidade e critérios de Go/No-Go.

## Extensão alvo

- **Páginas:** 5-15 páginas (impressão A4) ou navegação com seções em HTML
- **Tom:** executivo com contexto técnico; evitar detalhes de implementação
- **Foco:** escopo, viabilidade, trade-offs, decisão de comitê

## Regions obrigatórias

Herda **todas as regions obrigatórias** de [one-pager-layout.md](one-pager-layout.md), e adiciona:

| Ordem (extra) | Region | Grupo | Observação |
|---|---|---|---|
| 6 | `product/problem-and-context` | product | Contexto de negócio e problema em profundidade |
| 7 | `product/value-proposition` | product | Proposta de valor e diferencial competitivo |
| 8 | `product/okrs` | product | OKRs e critérios de sucesso do MVP |
| 9 | `technical/macro-architecture` | technical | Arquitetura macro (diagrama + narrativa) |
| 10 | `risk/feasibility-analysis` | risk | Análise de viabilidade (técnica, organizacional, financeira) |
| 11 | `backlog/go-no-go-criteria` | backlog | Critérios de Go/No-Go para avançar para build |

## Regions opcionais (ativar conforme contexto)

| Region | Quando ativar |
|---|---|
| `financial/tco-3-years` | sempre que `financial_model=projeto-paga` OR estimativa de consumo fundo-global for relevante |
| `metrics/business-kpis` | quando o briefing define KPIs de negócio mensuráveis pós-launch |
| `product/roi` | **só quando `require_roi=true`** — por padrão, omitir |
| `financial/break-even` | só quando `require_roi=true` |
| `organization/stakeholder-map` | quando o projeto tem >5 stakeholders críticos |

## Regions explicitamente proibidas no EX

- Logs de entrevista (`interview.md`, `hr-loop-*.md`) — vão no DR, não no EX
- Detalhes de implementação de cada épico — vão no DR
- Qualquer region com `deliverable-scope` restrito a `["DR"]`

## Comportamento do distiller

Ao produzir o EX, o distiller deve:

1. **Herdar** a lista de regions do `one-pager-layout.md` + adicionar as 6 obrigatórias extras
2. **Avaliar flags** do briefing para incluir regions opcionais (`financial_model`, `require_roi`, etc.)
3. **Destilar cada region** para uma extensão adequada (narrativa mais rica que no OP, mas sem descer em detalhes de implementação)
4. **Preservar rastreabilidade** — cada afirmação do EX deve ser rastreável a uma region do DR (metadado `source-region` no output)
5. **Emitir warning** se alguma region obrigatória herdada do OP estiver marcada como "gap" no DR

## Comparativo OP × EX × DR

| Aspecto | OP | EX | DR |
|---------|-----|-----|-----|
| Extensão | 1 página | 5-15 páginas | 30-100+ páginas |
| Audiência | Decisor rápido | Comitê executivo | Time técnico + auditor |
| Regions | 5 obrigatórias | 11 obrigatórias + opcionais | todas do Discovery |
| ROI/Break-even | nunca | quando `require_roi=true` | quando `require_roi=true` |
| Logs de entrevista | não | não | sim |
| Produzido por | distiller (task #16) | distiller (task #16) | pipeline completo (Fases 1-3) |

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 01.00.000 | 2026-04-17 | Criação — origem ADR-001 (task #17 do TODO) |
