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

## Representacao Visual

### Dados de amostra

```yaml
go_no_go_criteria:
  criteria:
    - id: "GNG-01"
      criterion: "Validacao de willingness-to-pay"
      target_value: ">= 50 pre-cadastros pagos"
      deadline: "Antes do MVP"
      status: "Pendente"
    - id: "GNG-02"
      criterion: "Spike tecnico de multi-tenancy"
      target_value: "Isolamento comprovado com 10 tenants"
      deadline: "Sprint 1"
      status: "Pendente"
    - id: "GNG-03"
      criterion: "Cobertura Open Finance"
      target_value: ">= 5 bancos com API funcional"
      deadline: "Sprint 2"
      status: "Pendente"
    - id: "GNG-04"
      criterion: "Score do auditor"
      target_value: ">= 7.0 em todas as dimensoes"
      deadline: "Fase 2"
      status: "Atingido"
    - id: "GNG-05"
      criterion: "Budget aprovado"
      target_value: "Aprovacao formal do sponsor"
      deadline: "Antes do kickoff"
      status: "Pendente"
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo descrevendo os criterios de decisao, quais foram atingidos e quais estao pendentes ou em risco | Relatorios executivos, atas de reuniao de go/no-go |
| Tabela | Tabela com colunas ID, Criterio, Valor-Alvo, Prazo, Como Medir e Status (formato atual do Exemplo) | Documentacao formal, rastreamento detalhado de criterios |
| Traffic light dashboard (semaforo) | Indicadores semaforo (verde=Atingido, amarelo=Em risco, vermelho=Nao atingido, cinza=Pendente) para cada criterio | Visao principal para reunioes de decisao, dashboards executivos, apresentacoes de steering committee |
| Scorecard com barras de progresso | Card por criterio com barra de progresso mostrando proximidade do valor-alvo e indicador de prazo | Acompanhamento de evolucao ao longo do tempo, dashboards operacionais |
| Timeline com marcos | Linha do tempo com marcos (deadlines) e indicadores de status em cada ponto | Visao temporal de quando cada criterio deve ser atingido, planejamento de gates |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
