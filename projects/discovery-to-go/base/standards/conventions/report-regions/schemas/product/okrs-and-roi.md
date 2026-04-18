---
region-id: REG-PROD-05
title: "OKRs and ROI (DEPRECATED)"
group: product
description: "DEPRECATED — substituído por okrs.md + roi.md a partir de 2026-04-17"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Progress bars + stat cards"
default: false
deprecated: true
superseded-by: ["okrs.md", "roi.md"]
---

# OKRs and ROI (DEPRECATED)

> [!danger] Region descontinuada
> Esta region foi **substituída** por duas regions separadas a partir de 2026-04-17 (decisão: ADR-001 / task #7 do TODO):
>
> - **[okrs.md](okrs.md)** — OKRs e critérios de sucesso do MVP (sempre presente, `deliverable-scope: ["OP","EX","DR"]`)
> - **[roi.md](roi.md)** — Análise de ROI (condicional a `require_roi=true`)
>
> **Motivação:** o Discovery-to-Go roda **depois** da aprovação global do investimento, então ROI/payback não é obrigatório no One-Pager. Ativar apenas quando o briefing explicitamente pedir `require_roi=true`.

## Migração

Se você tem templates ou configurações que referenciam `okrs-and-roi.md`:

| Antes | Depois |
|-------|--------|
| `product/okrs-and-roi.md` | Sempre: `product/okrs.md` + (quando `require_roi=true`) `product/roi.md` |

## Conteúdo histórico

O conteúdo original desta region foi dividido integralmente entre as duas novas regions — nenhum dado é perdido, apenas separado por condicionalidade.
