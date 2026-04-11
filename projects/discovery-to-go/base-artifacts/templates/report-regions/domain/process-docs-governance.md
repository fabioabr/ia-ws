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

## Representacao Visual

### Dados de amostra

**RACI Heatmap:**

| Atividade | Analista Proc. | Gestor Area | Diretor | Compliance | Qualidade |
|-----------|:-------------:|:-----------:|:-------:|:----------:|:---------:|
| Criar documento | R | A | - | - | C |
| Revisar documento | C | R | A | - | I |
| Aprovar publicacao | - | C | R | C | I |
| Monitorar adocao | I | A | I | - | R |

Legenda: R = Responsible, A = Accountable, C = Consulted, I = Informed

**Metricas:**

| Metrica | Target | Atual |
|---------|--------|-------|
| Processos documentados | >= 90% | 78% |
| Documentos dentro da validade | >= 95% | 91% |
| Acessos unicos/mes | >= 5 | 6.2 |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa do modelo de governanca com papeis, ciclos e metricas | Politicas internas, documentos de qualidade |
| Tabela | Tabela RACI com atividades e papeis | Definicao de responsabilidades, onboarding de times |
| RACI heatmap | Matriz RACI com cores indicando nivel de envolvimento por papel e atividade | Workshops de governanca, apresentacoes para gestao, definicao de processos |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
