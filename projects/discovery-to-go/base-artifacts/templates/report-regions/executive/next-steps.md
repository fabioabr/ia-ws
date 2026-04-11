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

## Representação Visual

### Dados de amostra

| # | Ação | Responsável | Prazo | Prioridade | Dependência |
|---|------|-------------|-------|------------|-------------|
| 1 | Aprovar budget Fase 1 | Maria Silva (CFO) | 20/05/2026 | Crítica | — |
| 2 | PoC integração SAP R/3 | Ana Costa (Tech Lead) | 30/05/2026 | Crítica | #1 |
| 3 | Contratar 2 devs backend sênior | Carlos Mendes (RH) | 15/06/2026 | Alta | #1 |
| 4 | Sessão validação usabilidade | João Santos (PO) | 25/05/2026 | Alta | — |
| 5 | Plano de change management | Luciana Alves (Change) | 10/06/2026 | Média | — |

**Total de ações:** 5
**Críticas:** 2 | **Alta:** 2 | **Média:** 1
**Com dependência:** 3 | **Independentes:** 2

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com priority badges + timeline horizontal
**Tecnologia:** HTML/CSS
**Justificativa:** Com 5 ações estruturadas contendo responsável, prazo, prioridade e dependências, a representação ideal é uma tabela HTML estilizada com badges coloridos de prioridade (Critica=vermelho, Alta=laranja, Media=amarelo) e uma timeline horizontal CSS (barras proporcionais ao prazo) abaixo da tabela para visualizar o sequenciamento temporal e sobreposicoes entre ações.
**Alternativa:** Tabela simples sem timeline (HTML/CSS) — quando o foco é apenas rastreabilidade das ações sem necessidade de visualização temporal
