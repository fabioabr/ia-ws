---
title: Template One-Page
description: Template one-page de discovery em duas tabs densas — Aba 1 entrega em uma tela o contexto + cenario recomendado condensado (decisao); Aba 2 entrega o detalhamento operacional (execucao). Proposta de leitura rapida, 1 pagina por aba.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - report
  - one-page
  - compacto
  - decisao
created: 2026-04-17
updated: 2026-04-17
---

# Template One-Page

Template one-page compacto. Em duas tabs densas entrega **decisao** na primeira tela e **execucao** na segunda — cada tab cabe proximo a uma pagina de leitura corrida.

## Proposito

Servir cenarios onde o patrocinador pede um material objetivo, de leitura rapida, sem perder as pecas essenciais do discovery:

- **Aba 1 — Visao & Decisao:** tudo que e preciso para decidir — contexto, numeros, dor, proposta, cenario recomendado, escopo, riscos e proximo passo imediato
- **Aba 2 — Execucao & Entrega:** como o projeto vai rodar — metricas, pessoas, fases, cronograma, quick win, pre-requisitos e proximo passo de execucao

## Audiencia

- Executivos (CFO, CEO, comite de investimento)
- Patrocinador e sponsor
- Tech Lead / Arquiteto (aba 2)
- PO / Scrum Master (aba 2)

## Estrutura do relatorio

```
Tab 1 — Visao & Decisao
  > Descritivo                          [REG-EXEC-02]
  > Indicadores do Projeto              [REG-FIN-06 | REG-FIN-01:total | REG-ORG-02:count | REG-QUAL-01:score]
  > Problemas Atuais                    [REG-PROD-01]
  > O Que Queremos Resolver             [REG-PROD-04]
  > Descritivo do Cenario Recomendado   [REG-FIN-07:recomendado]
  > Escopo Detalhado                    [CUSTOM-1]
  > Top 5 Riscos Criticos               [REG-RISK-01:top5]
  > Proximos Passos                     [REG-EXEC-04]

Tab 2 — Execucao & Entrega
  > Metricas de Sucesso                 [REG-PROD-05]
  > Stakeholders                        [REG-ORG-01]
  > Planejamento Macro por Fase         [CUSTOM-2]
  > Cronograma Detalhado                [CUSTOM-3]
  > Quick Win                           [REG-PROD-10]
  > Pre-requisitos                      [REG-NARR-02]
  > Proximos Passos                     [REG-EXEC-04]
```

> **Proximos Passos aparece nas duas tabs** — proposital. Na Aba 1 sao os proximos passos de **decisao** (ex: aprovar orcamento ate data X, assinar contrato). Na Aba 2 sao os proximos passos de **execucao** (kickoff, setup de ambientes, primeiras reunioes). O composer deve resolver REG-EXEC-04 com foco diferente em cada tab quando possivel.

## Diferencas em relacao ao template `orcamento`

| Aspecto | orcamento | one-page |
|---------|-----------|----------|
| Cenarios | Suporta multiplos cenarios (recomendado + enxuto + expandido) via SUB-SCENARIO | So cenario recomendado |
| Densidade | Baixa-media (Aba 1 = contexto, Aba 2 = detalhes) | Alta (Aba 1 ja tem o cenario condensado) |
| Propositio | Orçar e comparar cenarios | Decidir rapido sobre o cenario recomendado |
| Indicadores na primeira tela | Nao (Aba 1 foca em contexto) | Sim (4 indicadores logo apos o descritivo) |
| Quick Win | Na aba do cenario | Destacada na Aba 2 como bloco dedicado |

## Regions do catalogo utilizadas

| REG-ID | Filtro | Fonte original |
|--------|--------|----------------|
| REG-EXEC-02 | — | Product Brief |
| REG-EXEC-04 | — | Proximos Passos |
| REG-FIN-01 | `:total` | TCO 3 Anos — apenas total |
| REG-FIN-06 | — | Total Hours |
| REG-FIN-07 | `:recomendado` | Cenarios Financeiros — cenario unico |
| REG-NARR-02 | — | Condicoes para Prosseguir |
| REG-ORG-01 | — | Mapa de Stakeholders |
| REG-ORG-02 | `:count` | Estrutura de Equipe — contagem |
| REG-PROD-01 | — | Problema e Contexto |
| REG-PROD-04 | — | Proposta de Valor |
| REG-PROD-05 | — | OKRs e ROI |
| REG-PROD-10 | — | Quick Win |
| REG-QUAL-01 | `:score` | Score do Auditor — numero so |
| REG-RISK-01 | `:top5` | Matriz de Riscos — top 5 |

## Custom regions

| Codigo | Nome | Motivo de ser custom |
|--------|------|----------------------|
| CUSTOM-1 | Escopo Detalhado | REG-PROD-07 tem escopo IN/OUT simples; precisamos de bullets aninhados com sub-entregas explicitas |
| CUSTOM-2 | Planejamento Macro por Fase | Combina fase × papel × horas; nao existe region unica que cruze essas 3 dimensoes |
| CUSTOM-3 | Gantt Hierarquico (Epico → Estoria) | REG-PLAN-01 renderiza so epicos; precisamos de 2 niveis + linha de marco + estrela de Quick Win (P48) |

## Convencoes visuais aplicadas

- **Gantt** deve seguir `conventions/components/gantt-hierarchical.md` (P48) — linha de marco primeira, estrela na estoria-chave do Quick Win, 1 coluna por semana, tecnica layered na intersecao epico × coluna QW
- **Todas as sections** devem ser recolhiveis via botao injetado pelo JS (P49) — permite ao leitor focar em uma secao de cada vez
- **Font-size global reduzido** (html { font-size: 15px }) — densidade maior sem perder legibilidade

## Uso no setup.md

```markdown
## Reports to generate

- template: one-page
  scenarios: [recomendado]
```

Nao faz sentido declarar multiplos cenarios neste template — se precisar comparar alternativas, use o template `orcamento`.

## Dependencias do composer

- Filtros `:total`, `:count`, `:score`, `:top5`, `:recomendado` implementados
- Suporte aos 3 CUSTOM do template
- html-writer v02.07.000+ (para aplicar P48 e P49)
