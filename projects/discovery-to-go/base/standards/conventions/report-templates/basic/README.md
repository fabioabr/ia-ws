---
title: Template Basic
description: Template de relatorio compacto que apresenta descritivo, problemas, metricas, stakeholders, 4 cards de indicadores do projeto (horas, investimento, equipe, confianca de auditoria) e um cenario recomendado completo com escopo detalhado, planejamento por fase, gantt expandido, top 5 riscos, pre-requisitos e proximos passos. Primeiro template do catalogo.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - report
  - basic
  - budget
  - scenarios
created: 2026-04-17
updated: 2026-04-17
---

# Template Basic

Template compacto orientado a decisao. Em duas tabs entrega o contexto do projeto e o cenario recomendado com todos os detalhes operacionais necessarios para aprovar ou reprovar.

## Proposito

Dar ao patrocinador e ao time uma visao rapida de:

- **Aba 1 — Visao do Projeto:** por que o projeto existe, o que queremos resolver, quem sao os stakeholders, qual o tamanho (4 indicadores chave)
- **Aba 2 — Cenario Recomendado:** como o projeto sera executado — escopo explicito, fases, cronograma, riscos, pre-requisitos e proximos passos

## Audiencia

- Decisores (patrocinador, CFO, comite)
- Time de projeto (PO, Tech Lead, arquiteto)

## Estrutura do relatorio

```
Tab 1 — Visao do Projeto
  > Descritivo                      [REG-EXEC-02]
  > Problemas Atuais                [REG-PROD-01]
  > O Que Queremos Resolver         [REG-PROD-04]
  > Metricas de Sucesso             [REG-PROD-05]
  > Stakeholders                    [REG-ORG-01]
  > Indicadores do Projeto          [REG-FIN-06 | REG-FIN-01:total | REG-ORG-02:count | REG-QUAL-01:score]

Tab 2 — Cenario Recomendado        (sempre inline, via SUB-SCENARIO:recomendado)
  > Descritivo do Cenario           [REG-FIN-07:recomendado]
  > Escopo                          [CUSTOM-1]
  > Planejamento Macro              [CUSTOM-2]
  > Cronograma Detalhado            [CUSTOM-3]
  > Top 5 Riscos Criticos           [REG-RISK-01:top5]
  > Pre-requisitos                  [REG-NARR-02]
  > Proximos Passos                 [REG-EXEC-04]
```

Se o setup declarar `scenarios: [recomendado, enxuto]`, o composer gera **uma tab adicional** ao final (`Tab 3 — Cenario Enxuto`) com o mesmo SUB-SCENARIO aplicado a variante `enxuto`. Mesma logica para `expandido`.

## Regions do catalogo utilizadas

| REG-ID | Filtro | Fonte original |
|--------|--------|----------------|
| REG-EXEC-02 | — | Product Brief |
| REG-EXEC-04 | — | Proximos Passos |
| REG-FIN-01 | `:total` | TCO 3 Anos — apenas total |
| REG-FIN-06 | — | Total Hours |
| REG-FIN-07 | `:{scenario}` | Cenarios Financeiros — 1 cenario por vez |
| REG-NARR-02 | — | Condicoes para Prosseguir |
| REG-ORG-01 | — | Mapa de Stakeholders |
| REG-ORG-02 | `:count` | Estrutura de Equipe — contagem |
| REG-PROD-01 | — | Problema e Contexto |
| REG-PROD-04 | — | Proposta de Valor |
| REG-PROD-05 | — | OKRs e ROI |
| REG-QUAL-01 | `:score` | Score do Auditor — numero so |
| REG-RISK-01 | `:top5` | Matriz de Riscos — top 5 |

## Custom regions

Tres customs declaradas no template por nao haver region-equivalente no catalogo com o grau de detalhe necessario:

| Codigo | Nome | Motivo de ser custom |
|--------|------|----------------------|
| CUSTOM-1 | Escopo Detalhado | REG-PROD-07 tem escopo IN/OUT simples; precisamos de bullets aninhados com sub-entregas explicitas (ex: "3 dashboards sendo a) ... b) ... c) ...") |
| CUSTOM-2 | Planejamento Macro por Fase | Combina fase × papel × horas; nao existe region unica que cruze essas 3 dimensoes |
| CUSTOM-3 | Gantt Expandido (Epico → Estoria) | REG-PLAN-01 renderiza so epicos; precisamos de 2 niveis hierarquicos |

## Uso no setup.md

```markdown
## Reports to generate

- template: basic
  scenarios: [recomendado]        # padrao — so o cenario recomendado

# ou mais de um cenario:
- template: basic
  scenarios: [recomendado, enxuto, expandido]

# ou todos:
- template: basic
  scenarios: all
```

## Dependencias do composer

Para renderizar este template o report-composer precisa ter:

- Todos os 11 filtros listados em [schemas/TODO.md](../schemas/TODO.md) implementados
- Suporte a `SUB-SCENARIO` com variavel `{scenario}`
- Suporte a expansao automatica de tabs adicionais por cenario

Enquanto filtros estiverem pendentes, este template nao pode ser materializado completo.
