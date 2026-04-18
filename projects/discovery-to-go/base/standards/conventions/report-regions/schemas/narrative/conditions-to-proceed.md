---
region-id: REG-NARR-02
title: "Conditions to Proceed"
group: narrative
description: "Mandatory prerequisites that must be met before project kickoff"
source: "Consolidator"
schema: "Lista de pré-requisitos obrigatórios"
template-visual: "Checklist card"
default: false
---

# Conditions to Proceed

Lista os pre-requisitos obrigatorios que devem ser atendidos antes de iniciar a execucao do projeto. Diferente dos criterios de go/no-go (que sao mensuráveis ao longo do tempo), estas sao condicoes binarias que devem estar resolvidas antes do kickoff.

## Schema de dados

```yaml
conditions_to_proceed:
  conditions:
    - id: string                 # Identificador (ex: CTP-01)
      condition: string          # Descricao da condicao
      category: string           # Organizacional / Tecnica / Financeira / Legal
      status: string             # Atendida / Pendente / Em andamento
      owner: string              # Responsavel
      deadline: string           # Prazo
```

## Exemplo

| ID | Condicao | Categoria | Status | Responsavel | Prazo |
|----|----------|-----------|--------|------------|-------|
| CTP-01 | Budget de R$ 564.000 aprovado para o ano 1 | Financeira | Pendente | CFO | Antes do kickoff |
| CTP-02 | Contratacao de 2 devs backend concluida | Organizacional | Em andamento | Engineering Manager | 2 semanas |
| CTP-03 | Conta AWS dedicada provisionada com guardrails | Tecnica | Atendida | DevOps Lead | - |
| CTP-04 | Contrato com Auth0 (Business plan) assinado | Financeira | Pendente | Procurement | 1 semana |
| CTP-05 | DPO designado para acompanhar requisitos LGPD | Legal | Pendente | Juridico | Antes do kickoff |
| CTP-06 | Acesso as APIs Open Finance (sandbox) obtido | Tecnica | Atendida | Tech Lead | - |

## Representacao Visual

### Dados de amostra

```
Condicoes para Prosseguir (2/6 atendidas)

[x] CTP-03  Conta AWS dedicada provisionada          Tecnica        Atendida
[x] CTP-06  Acesso APIs Open Finance (sandbox)       Tecnica        Atendida
[~] CTP-02  Contratacao 2 devs backend                Organizacional Em andamento
[ ] CTP-01  Budget R$ 564.000 aprovado                Financeira     Pendente
[ ] CTP-04  Contrato Auth0 (Business plan)            Financeira     Pendente
[ ] CTP-05  DPO designado para LGPD                   Legal          Pendente
```

### Recomendacao do Chart Specialist

**Veredicto:** CARD
**Tipo:** Checklist com progress bar
**Tecnologia:** HTML/CSS
**Justificativa:** Condicoes para prosseguir sao binarias (atendida/pendente/em andamento) e exigem visao de completude. Um checklist com indicadores visuais por item e barra de progresso geral (X de Y atendidas) comunica instantaneamente o grau de prontidao do projeto para o kickoff.
**Alternativa:** Checklist agrupado por categoria — quando ha muitas condicoes (>10) e a organizacao por area (Tecnica, Financeira, Legal) facilita a delegacao.
