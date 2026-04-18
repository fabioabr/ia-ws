---
title: "One-Pager Layout — estrutura mínima do entregável OP"
description: "Piso determinístico que o deliverable-distiller deve respeitar ao produzir o One-Pager (OP) a partir do Delivery Report"
target-deliverable: "OP"
version: "01.00.000"
status: "draft"
origin: "ADR-001 — Entregáveis hierárquicos OP ⊂ EX ⊂ DR"
extends: "—"
---

# One-Pager Layout

Define a **estrutura mínima** que o entregável **One-Pager (OP)** deve ter, independente do contexto do cliente. O [deliverable-distiller](../../../../behavior/skills/deliverable-distiller/SKILL.md) (task #16) é obrigado a produzir pelo menos estas regions; pode omitir somente quando uma region for explicitamente **condicional** a uma flag do briefing e a flag estiver desligada.

## Propósito

O OP é um **resumo de 1 página** para decisores que precisam entender **escopo, esforço, custo e top riscos** em poucos minutos. Por decisão formal (ADR-001 + `feedback_one_pager_scope.md`), o OP do Discovery-to-Go **não dimensiona time real** nem **justifica ROI** por padrão — assume que aprovação global aconteceu upstream.

## Extensão alvo

- **Páginas:** 1 página (impressão A4) ou 1 scroll de tela em HTML
- **Tom:** executivo, direto, sem jargão técnico desnecessário
- **Foco:** escopo, custo, esforço, top riscos, recomendação

## Regions obrigatórias

| Ordem | Region | Grupo | Observação |
|---|---|---|---|
| 1 | `executive/overview-one-pager` | executive | Hero card com problema, proposta, decisões técnicas, próximo passo |
| 2 | `executive/premises` | executive | Premissas que sustentam esforço/custo/escopo |
| 3 | `risk/risk-matrix` | risk | Top-3 riscos (severidade × probabilidade) |
| 4 | `financial/cost-per-component` | financial | Estimativa de custo/consumo por componente |
| 5 | `backlog/prioritized-epics` | backlog | Top-3 épicos priorizados |

> [!info] Region condicionalmente substituída
> Em `executive/overview-one-pager`, o campo `tco_resumo` é substituído por `estimativa_consumo` quando `financial_model=fundo-global`. O distiller aplica a substituição automaticamente.

## Regions opcionais

Nenhuma. O OP é um piso — se o cliente quiser mais que isto, o entregável apropriado é o **Executive Report (EX)**, não o OP.

## Regions explicitamente proibidas no OP

- `product/roi` — mesmo quando `require_roi=true`, ROI vai no EX/DR, não no OP do DTG
- `organization/team-structure`, `organization/raci` — não dimensionamos time no OP
- `financial/break-even`, `financial/financial-scenarios` — análises de cenário vão no EX/DR
- Qualquer region com `deliverable-scope` que não inclua `"OP"`

## Comportamento do distiller

Ao produzir o OP, o distiller deve:

1. **Ler** este layout e extrair a lista de regions obrigatórias
2. **Para cada region obrigatória**:
   - Ler o schema da region
   - Verificar `conditional-on` no frontmatter da region
   - Avaliar a condição contra as flags do briefing
   - Se a condição passar, **destilar** o conteúdo do DR para caber na extensão alvo (1 página)
   - Se a condição falhar, pular (log em `hr-loop-*.md`)
3. **Nunca adicionar** regions fora da lista obrigatória, mesmo que existam no DR
4. **Emitir warning** se alguma region obrigatória **não existir** no DR de origem — indica gap no Discovery, não é resolvido pelo distiller

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 01.00.000 | 2026-04-17 | Criação — origem ADR-001 (task #17 do TODO) |
