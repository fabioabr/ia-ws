---
region-id: REG-DOM-PROC-02
title: "Process Docs Governance"
group: domain
description: "RACI matrix, review cycles, and adoption metrics for process documentation"
source: "Bloco #5/#7 (arch)"
schema: "RACI + revisão + métricas adoção"
template-visual: "Card com RACI table"
when: process-documentation
default: false
---

# Process Docs Governance

Define o modelo de governanca da documentacao de processos, incluindo matriz RACI, ciclos de revisao e metricas de adocao. Documentacao sem governanca tende a ficar desatualizada rapidamente, perdendo valor e confiabilidade.

## Schema de dados

```yaml
docs_governance:
  raci:
    - activity: string
      responsible: string
      accountable: string
      consulted: string
      informed: string
  review_cycle:
    frequency: string
    process: string
  adoption_metrics:
    - metric: string
      target: string
```

## Exemplo

**Matriz RACI:**

| Atividade | Responsible | Accountable | Consulted | Informed |
|-----------|-----------|-------------|-----------|----------|
| Criar documento | Analista de processos | Gestor da area | Especialistas | Equipe |
| Revisar documento | Gestor da area | Diretor | Qualidade | Equipe |
| Aprovar publicacao | Diretor | Compliance | Juridico | Toda a org |
| Monitorar adocao | Qualidade | Gestor da area | RH | Diretoria |

**Metricas de adocao:**
- % de processos documentados: target >= 90%
- % de documentos dentro da validade: target >= 95%
- Acessos unicos/mes por documento: target >= 5
