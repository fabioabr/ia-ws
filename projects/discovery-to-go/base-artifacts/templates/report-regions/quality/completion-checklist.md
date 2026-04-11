---
region-id: REG-QUAL-04
title: "Completion Checklist"
group: quality
description: "Checklist of all required deliverables and their completion status"
source: "Consolidator"
schema: "Checklist (item, status)"
template-visual: "Checklist com checkmarks"
default: false
---

# Completion Checklist

Lista todos os entregaveis esperados do discovery e seu status de conclusao. Permite uma visao rapida do que foi produzido e do que ainda esta pendente. Itens incompletos podem indicar necessidade de iteracao adicional antes da aprovacao.

## Schema de dados

```yaml
completion_checklist:
  items:
    - category: string           # Categoria do item
      item: string               # Descricao do entregavel
      status: string             # Completo / Parcial / Pendente / N/A
      notes: string              # Observacoes
  completion_rate: number        # % de itens completos
```

## Exemplo

| Categoria | Item | Status | Notas |
|-----------|------|--------|-------|
| Produto | Visao e proposta de valor | Completo | |
| Produto | Personas e jornadas | Completo | |
| Produto | Backlog priorizado (epicos) | Completo | 5 epicos com MoSCoW |
| Arquitetura | Diagrama de arquitetura | Completo | C4 nivel 2 |
| Arquitetura | Definicao de stack | Completo | |
| Arquitetura | NFRs e SLAs | Parcial | SLAs definidos, SLOs pendentes |
| Financeiro | TCO 3 anos | Completo | Revisado apos reprovacao do auditor |
| Financeiro | Estimativa de esforco | Completo | |
| Seguranca | Analise LGPD | Pendente | Aguardando DPO |
| Seguranca | Threat modeling | Pendente | |
| Riscos | Matriz de riscos | Completo | |
| Qualidade | Revisao do auditor | Completo | 2 iteracoes |
| Qualidade | Revisao do 10th-man | Completo | |

**Taxa de conclusao:** 77% (10/13 completos)

## Representacao Visual

### Dados de amostra

```yaml
completion_checklist:
  items:
    - category: "Produto"
      item: "Visao e proposta de valor"
      status: "Completo"
    - category: "Produto"
      item: "Personas e jornadas"
      status: "Completo"
    - category: "Produto"
      item: "Backlog priorizado (epicos)"
      status: "Completo"
    - category: "Arquitetura"
      item: "Diagrama de arquitetura"
      status: "Completo"
    - category: "Arquitetura"
      item: "Definicao de stack"
      status: "Completo"
    - category: "Arquitetura"
      item: "NFRs e SLAs"
      status: "Parcial"
    - category: "Financeiro"
      item: "TCO 3 anos"
      status: "Completo"
    - category: "Financeiro"
      item: "Estimativa de esforco"
      status: "Completo"
    - category: "Seguranca"
      item: "Analise LGPD"
      status: "Pendente"
    - category: "Seguranca"
      item: "Threat modeling"
      status: "Pendente"
    - category: "Riscos"
      item: "Matriz de riscos"
      status: "Completo"
    - category: "Qualidade"
      item: "Revisao do auditor"
      status: "Completo"
    - category: "Qualidade"
      item: "Revisao do 10th-man"
      status: "Completo"
  completion_rate: 77
```

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Checklist com progress bar
**Tecnologia:** HTML/CSS
**Justificativa:** Itens de checklist com status (Completo/Parcial/Pendente) agrupados por categoria mapeiam naturalmente em uma lista com checkmarks, alertas e indicadores visuais, complementada por uma barra de progresso geral mostrando a taxa de conclusao — formato compacto e acionavel.
**Alternativa:** Barras de progresso por categoria (HTML/CSS) — quando a identificacao de categorias com maior lacuna for mais importante que o detalhe item a item.
