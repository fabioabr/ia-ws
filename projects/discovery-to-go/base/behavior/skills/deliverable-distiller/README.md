# Deliverable Distiller

Skill que destila o **Delivery Report (DR)** em **One-Pager (OP)** e/ou **Executive Report (EX)**.

## Quando é invocada

- **Automaticamente** pelo `orchestrator` na Fase 3 (Delivery), após o `consolidator` produzir o DR
- **Somente** quando o briefing declara `deliverables_scope` com `"OP"` e/ou `"EX"`
- **Nunca** se o briefing pede apenas `["DR"]`

## Inputs

| Input | Origem |
|-------|--------|
| delivery-report | `{project}/delivery/delivery-report.md` |
| briefing | `{project}/setup/briefing.md` |
| layout | `one-pager-layout.md` ou `executive-layout.md` (customização ou default) |
| target | `OP` ou `EX` |

## Outputs

| Target | Path ativo | Path archive |
|--------|-----------|--------------|
| OP | `{project}/delivery/one-pager.md` | `{project}/iterations/iteration-{N}/results/3-delivery/one-pager.md` |
| EX | `{project}/delivery/executive-report.md` | `{project}/iterations/iteration-{N}/results/3-delivery/executive-report.md` |

## Garantias

- Rastreabilidade: cada region destilada cita a region-fonte do DR
- Sem hallucination: se o DR não tem o dado, emite warning (`[GAP — ausente no DR]`)
- Respeita flags condicionais (`financial_model`, `require_roi`)
- Respeita piso do layout (regions obrigatórias) e teto (regions proibidas)

## Documento completo

Ver [SKILL.md](SKILL.md).

## Contexto de origem

- [ADR-001 — Entregáveis hierárquicos OP ⊂ EX ⊂ DR](../../../../projects/patria/kb/adr-001-deliverable-hierarchy.md)
- Task #16 e #17 do [TODO.md](../../../../TODO.md) do Discovery-to-Go
