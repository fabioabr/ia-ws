---
region-id: REG-BACK-04
title: "Go/No-Go Criteria"
group: backlog
description: "Decision criteria with target values and deadlines for project continuation"
source: "Consolidator"
schema: "Tabela (critério, valor-alvo, prazo)"
template-visual: "Table com target indicators"
default: false
---

# Go/No-Go Criteria

Define os criterios objetivos que devem ser atingidos para que o projeto avance de fase. Cada criterio tem um valor-alvo mensuravel e um prazo. Esta regiao transforma a decisao de continuidade em algo baseado em dados, nao em opiniao.

## Schema de dados

```yaml
go_no_go_criteria:
  criteria:
    - id: string                 # Identificador (ex: GNG-01)
      criterion: string          # Descricao do criterio
      target_value: string       # Valor-alvo mensuravel
      deadline: string           # Prazo para atingir
      measurement: string        # Como medir
      status: string             # Atingido / Em risco / Nao atingido / Pendente
```

## Exemplo

| ID | Criterio | Valor-Alvo | Prazo | Como Medir | Status |
|----|----------|-----------|-------|-----------|--------|
| GNG-01 | Validacao de willingness-to-pay | >= 50 pre-cadastros pagos | Antes do MVP | Landing page com pagamento simulado | Pendente |
| GNG-02 | Spike tecnico de multi-tenancy | Isolamento comprovado com 10 tenants | Sprint 1 | Teste de carga + auditoria de dados | Pendente |
| GNG-03 | Cobertura Open Finance | >= 5 bancos com API funcional | Sprint 2 | Teste de integracao end-to-end | Pendente |
| GNG-04 | Score do auditor | >= 7.0 em todas as dimensoes | Fase 2 | Score do auditor (REG-QUAL-01) | Atingido |
| GNG-05 | Budget aprovado | Aprovacao formal do sponsor | Antes do kickoff | Documento assinado | Pendente |
