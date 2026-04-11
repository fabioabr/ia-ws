---
region-id: REG-RISK-03
title: "Unvalidated Hypotheses"
group: risk
description: "Critical assumptions that remain unvalidated and their associated risks"
source: "Fase 2 (10th-man)"
schema: "Tabela (hipótese, risco se falsa, como validar, prazo)"
template-visual: "Table com alert style"
default: true
---

# Unvalidated Hypotheses

Lista as hipoteses criticas que sustentam o projeto mas que ainda nao foram validadas com dados reais. Cada hipotese inclui o risco associado caso se prove falsa e um plano concreto de validacao. Este e um dos artefatos mais importantes do 10th-man, pois expoe os pontos cegos do discovery.

## Schema de dados

```yaml
unvalidated_hypotheses:
  hypotheses:
    - id: string                 # Identificador (ex: HYP-01)
      hypothesis: string         # Descricao da hipotese
      risk_if_false: string      # Consequencia se a hipotese for invalida
      severity: string           # Critica / Alta / Media
      validation_method: string  # Como validar
      deadline: string           # Prazo para validacao
      status: string             # Pendente / Em validacao / Validada / Invalidada
```

## Exemplo

| ID | Hipotese | Risco se Falsa | Severidade | Como Validar | Prazo |
|----|----------|----------------|------------|-------------|-------|
| HYP-01 | PMEs aceitam pagar R$ 149/mes por gestao financeira automatizada | Modelo de receita inviavel; necessidade de pivotar pricing | Critica | Landing page com pre-cadastro + entrevistas com 30 PMEs | Antes do MVP |
| HYP-02 | Open Finance tera cobertura de 80% dos bancos ate o lancamento | Funcionalidade core com cobertura parcial | Alta | Consultar roadmap BACEN + testar APIs dos 5 maiores bancos | Sprint 2 |
| HYP-03 | Um time de 5 pessoas consegue entregar o MVP em 4 meses | Atraso no lancamento e estouro de budget | Alta | Validar com spike tecnico nas primeiras 2 sprints | Sprint 2 |
| HYP-04 | Usuarios preferem dashboard visual a relatorios em PDF | Investimento em UX sem retorno se preferencia for PDF | Media | Teste A/B com 50 usuarios beta | Mes 2 pos-lancamento |

## Representação Visual

### Dados de amostra

| ID | Hipótese | Severidade | Status | Prazo |
|----|----------|------------|--------|-------|
| HYP-01 | PMEs aceitam pagar R$ 149/mês por gestão financeira automatizada | Crítica | Pendente | Antes do MVP |
| HYP-02 | Open Finance terá cobertura de 80% dos bancos até o lançamento | Alta | Pendente | Sprint 2 |
| HYP-03 | Time de 5 pessoas entrega MVP em 4 meses | Alta | Pendente | Sprint 2 |
| HYP-04 | Usuários preferem dashboard visual a relatórios PDF | Média | Pendente | Mês 2 pós-lançamento |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo cada hipótese, por que é crítica, o risco se falsa e o plano de validação | Comunicação executiva onde o storytelling sobre incertezas é mais eficaz que uma lista |
| Tabela | Matriz completa com hipótese, risco se falsa, severidade, método de validação, prazo e status | Quando o leitor precisa acompanhar o progresso de validação de cada hipótese |
| Risk cards com severidade | Cards individuais por hipótese, coloridos por severidade (Crítica = vermelho, Alta = laranja, Média = amarelo), com risco, método e prazo | Visualização de alto impacto para destacar hipóteses não validadas como itens de ação urgentes |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
