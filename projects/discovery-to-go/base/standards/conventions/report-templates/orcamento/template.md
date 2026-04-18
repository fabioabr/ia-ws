---
template-id: orcamento
title: Relatorio de Orcamento
audience: decisores financeiros + patrocinador + time de projeto
version: 01.00.000
description: Template de orcamento em duas tabs — Visao do Projeto (contexto + 4 indicadores financeiros) e Cenario Recomendado (escopo detalhado IN/OUT, planejamento por fase com horas por papel, gantt expandido epico-estoria, top 5 riscos, pre-requisitos e proximos passos). Tabs adicionais sao geradas automaticamente quando o setup declara cenarios alternativos (enxuto, expandido).
created: 2026-04-17
updated: 2026-04-17
---

## Custom Regions

### CUSTOM-1 — Escopo Detalhado
Prompt:
Gere o escopo do cenario em **duas colunas** (DENTRO DO ESCOPO / FORA DO ESCOPO) com
**detalhamento explicito** de cada item. Quando um item tiver sub-entregas, liste-as em
bullets aninhados identificados por letras minusculas (a, b, c, ...).

Regras de detalhamento:
- Itens com quantidade ou enumeracao devem declarar o numero ("3 dashboards", "10 tabelas")
  e enumerar as sub-entregas em nivel aninhado.
- Evitar generalidades do tipo "varios relatorios". Ser concreto.
- Cada item em uma unica linha, sub-itens em bullets abaixo.

Exemplo de estrutura esperada:
```
DENTRO DO ESCOPO
* 3 dashboards em Power BI sendo:
    a) visao operacional por fonte
    b) visao analitica com drill-down
    c) listagem para filtros customizados
* extracao de 10 tabelas do sistema XPTO via conector gerenciado
* processo de ETL das 10 tabelas para ingestao na camada Gold

FORA DO ESCOPO
* integracao com sistema Y (avaliada para wave 2)
* dashboards em PDF estatico
* modelos de Machine Learning
```

Formato visual: split card com duas colunas. Coluna IN com check verde, coluna OUT com X vermelho.

### CUSTOM-2 — Planejamento Macro por Fase
Prompt:
Liste as **fases do projeto** no cenario. Para cada fase, informe:

- Nome da fase (ex: "Setup & Arquitetura")
- Duracao em semanas
- Papeis que atuam na fase
- Para cada papel, quantas horas sao consumidas NESTA fase

Render como **cards horizontais lado a lado** (um por fase) contendo numero, nome,
duracao em semanas e horas totais da fase — seguido de uma **tabela detalhada**
com as linhas sendo os papeis e as colunas sendo as fases, com total por papel
e total geral do cenario.

Exemplo de estrutura esperada:
```
Fase 1 — Setup & Arquitetura (3 semanas, 180h)
Fase 2 — Ingestao & Consolidacao (6 semanas, 640h)
Fase 3 — Modelagem & Dashboards (4 semanas, 420h)
...

Tabela Papeis × Fases:
  Arquiteto ......... F1:60 F2:120 F3:80 ... Total:360
  Dev Sr ............ F1:40 F2:200 F3:180 .. Total:580
  ...
  TOTAL GERAL ...................... 1.860h
```

### CUSTOM-3 — Gantt Expandido (Epico → Estoria)
Prompt:
Renderize um **Gantt em HTML+CSS puro** com **2 niveis hierarquicos**:

- **Nivel 1 — Epico** (linha agrupadora, negrito, cor mais forte)
- **Nivel 2 — Estorias** filhas do epico (linhas indentadas abaixo, cor mais suave)

Eixo X: semanas relativas (Semana 1, 2, ..., N) — sem datas fixas.
Eixo Y: lista hierarquica de epicos com suas estorias expandidas.

Cada linha (epico ou estoria) tem uma barra horizontal indicando em quais semanas ocorre.
A barra do epico deve cobrir a uniao das barras de suas estorias. Use as fases do
CUSTOM-2 como contexto — os epicos devem se enquadrar nas fases correspondentes.

Abaixo do gantt, incluir tabela de detalhamento com colunas: Epico/Estoria, Fase, Semanas,
Horas estimadas, Papel responsavel, Dependencias.

Nao usar Mermaid nem libs externas — apenas HTML/CSS puro, conforme o design system do
workspace.

## Sub-Templates

### SUB-SCENARIO — Cenario ({scenario})

> Descritivo do Cenario
[REG-FIN-07:{scenario}]

> Escopo
[CUSTOM-1]

> Planejamento Macro
[CUSTOM-2]

> Quick Win
[REG-PROD-10]

> Cronograma Detalhado
[CUSTOM-3]

> Top 5 Riscos Criticos
[REG-RISK-01:top5]

> Pre-requisitos
[REG-NARR-02]

> Proximos Passos
[REG-EXEC-04]

## Layout

# Tab: Visao do Projeto

> Descritivo
[REG-EXEC-02]

> Problemas Atuais
[REG-PROD-01]

> O Que Queremos Resolver
[REG-PROD-04]

> Metricas de Sucesso
[REG-PROD-05]

> Stakeholders
[REG-ORG-01]

> Indicadores do Projeto
[REG-FIN-06 | REG-FIN-01:total | REG-ORG-02:count | REG-QUAL-01:score]

---

# Tab: Cenario Recomendado

[SUB-SCENARIO:recomendado]
