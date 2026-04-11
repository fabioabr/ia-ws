---
region-id: REG-EXEC-04
title: "Next Steps"
group: executive
description: "Ações imediatas pós-discovery com responsável e prazo"
source: "Consolidator"
schema: "table"
template-visual: "Table com checkboxes"
default: true
---

# Next Steps

Lista de ações concretas e priorizadas que devem ser executadas imediatamente após a conclusão do discovery. Cada ação tem um responsável claro e um prazo definido, permitindo que o projeto mantenha momentum e que stakeholders saibam exatamente o que acontece a seguir. É o artefato de transição entre discovery e execução.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| acoes | list | Cada item: `{ id: number, acao: string, responsavel: string, prazo: string, prioridade: "crítica" | "alta" | "média", dependencia: string | null }` |

## Exemplo

```markdown
## Next Steps

| # | Ação | Responsável | Prazo | Prioridade | Dependência |
|---|------|-------------|-------|------------|-------------|
| 1 | Aprovar budget da Fase 1 (MVP) no comitê de investimentos | Maria Silva (CFO) | 20/05/2026 | Crítica | — |
| 2 | Executar PoC de integração com SAP R/3 (Sprint 0) | Ana Costa (Tech Lead) | 30/05/2026 | Crítica | #1 aprovado |
| 3 | Contratar 2 desenvolvedores backend sênior para o time | Carlos Mendes (RH) | 15/06/2026 | Alta | #1 aprovado |
| 4 | Agendar sessão de validação de usabilidade com analistas das filiais SP e RJ | João Santos (PO) | 25/05/2026 | Alta | — |
| 5 | Definir plano de change management com champions por filial | Luciana Alves (Change Manager) | 10/06/2026 | Média | — |
```
