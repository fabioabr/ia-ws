---
template-id: one-page
title: Relatorio One-Page de Discovery
audience: decisores + time de projeto (leitura rapida, 1 pagina por aba)
version: 01.00.000
description: Template one-page de duas tabs compactas — Aba 1 com contexto + cenario recomendado condensado (descritivo, indicadores, problemas, proposta, cenario, escopo, riscos, proximos passos) e Aba 2 com detalhamento operacional (metricas, stakeholders, fases, cronograma, quick win, pre-requisitos, proximos passos). Densidade alta, uma tela por aba.
created: 2026-04-17
updated: 2026-04-17
---

## Custom Regions

### CUSTOM-1 — Escopo Detalhado
Prompt:
Gere o escopo do cenario recomendado em **duas colunas** (DENTRO DO ESCOPO / FORA DO ESCOPO) com
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
Liste as **fases do projeto** no cenario recomendado. Para cada fase, informe:

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

### CUSTOM-3 — Gantt Hierarquico (Epico → Estoria)
Prompt:
Renderize um **Gantt em HTML+CSS puro** seguindo o componente `gantt-hierarchical`
(ver `conventions/components/gantt-hierarchical.md`) com **2 niveis hierarquicos**:

- **Nivel 1 — Epico** (linha agrupadora, fundo escurecido via `.gantt-epic`)
- **Nivel 2 — Estorias** filhas do epico (linhas normais)

Eixo X: **1 coluna por semana** (Semana 1, 2, ..., N) — sem datas fixas, sem agrupar semanas.
Eixo Y: lista hierarquica de epicos com suas estorias.

Regras obrigatorias (P48):
- Quando houver Quick Win, a **linha de marco** (.gantt-milestone) deve ser a **primeira** do tbody,
  com fundo verde uniforme e emoji ⭐ na semana-alvo — sem border-left colorido.
- A estrela ⭐ tambem vai na **estoria-chave** que materializa a entrega do Quick Win (nao no epico).
- A coluna da semana do marco ganha classe `qw-col` e fundo verde claro.
- A intersecao epico × coluna QW usa tecnica layered (background-color escurecido +
  linear-gradient com --success-light).

Abaixo do gantt, incluir tabela de detalhamento com colunas: Epico/Estoria, Fase, Semanas,
Horas estimadas, Papel responsavel, Dependencias.

Nao usar Mermaid nem libs externas — apenas HTML/CSS puro.

## Layout

# Tab: Visao & Decisao

> Descritivo
[REG-EXEC-02]

> Indicadores do Projeto
[REG-FIN-06 | REG-FIN-01:total | REG-ORG-02:count | REG-QUAL-01:score]

> Problemas Atuais
[REG-PROD-01]

> O Que Queremos Resolver
[REG-PROD-04]

> Descritivo do Cenario Recomendado
[REG-FIN-07:recomendado]

> Escopo Detalhado
[CUSTOM-1]

> Top 5 Riscos Criticos
[REG-RISK-01:top5]

> Proximos Passos
[REG-EXEC-04]

---

# Tab: Execucao & Entrega

> Metricas de Sucesso
[REG-PROD-05]

> Stakeholders
[REG-ORG-01]

> Planejamento Macro por Fase
[CUSTOM-2]

> Cronograma Detalhado
[CUSTOM-3]

> Quick Win
[REG-PROD-10]

> Pre-requisitos
[REG-NARR-02]

> Proximos Passos
[REG-EXEC-04]
