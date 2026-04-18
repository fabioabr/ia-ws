---
title: Report Templates Catalog
description: Catalogo de templates de relatorio disponiveis. Cada template define a estrutura (tabs, sections, cards) de um tipo de relatorio que pode ser gerado no delivery. O usuario escolhe no setup.md quais templates rodar, e o report-composer materializa cada um usando regions do catalogo report-regions e custom regions declaradas no proprio template.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: catalog
area: tecnologia
tags:
  - catalog
  - report-templates
  - delivery-report
  - report-composer
  - customization
created: 2026-04-17
updated: 2026-04-17
---

# Report Templates Catalog

Catalogo de templates de relatorio. Cada template e uma **receita de composicao** que descreve, em um arquivo `.md`, a estrutura do relatorio final — quais tabs existem, quais sections tem cada tab, e quais cards (regions do catalogo ou customizados) aparecem em cada linha.

> [!info] Relacao com `report-regions`
> - `report-regions/` define **o qu cada card individual e** (schema, dados, visual)
> - `report-templates/` define **como os cards se combinam** em um relatorio final
> - Um template referencia regions pelo seu REG-ID (ex: `[REG-FIN-01]`)

## Estrutura do catalogo

```
report-templates/
  README.md                   # este arquivo
  schemas/
    README.md
    template-syntax.md        # spec formal da sintaxe do template
    TODO.md                   # controle de filtros :variant implementados
  basic/
    README.md                 # descreve o template basic
    template.md               # o template em si
```

Cada subpasta nomeada (ex: `basic/`) contem **um template completo**.

## Templates disponiveis

| Template | Proposito | Audiencia | Status |
|----------|-----------|-----------|--------|
| `basic` | Relatorio compacto com descritivo, problemas, metricas, stakeholders, 4 cards de indicadores, cenario recomendado com escopo detalhado, planejamento, gantt, riscos, pre-requisitos e proximos passos | Decisores + time de projeto | Em construcao |

## Como o usuario escolhe um template

No `setup.md` do projeto, o usuario declara quais relatorios gerar:

```markdown
## Reports to generate

- template: basic
  scenarios: [recomendado]
```

O `report-composer` le essa lista, carrega o template correspondente, resolve os placeholders contra os dados do run, chama o `md-writer` para polir, e o `html-writer` converte em HTML final.

## Override por cliente

Para sobrescrever um template para um cliente especifico, coloque o arquivo em:

```
custom-artifacts/{client}/templates/report-templates/{template-id}/template.md
```

O `report-composer` detecta o override e usa no lugar do default.

## Proximos templates

Outros templates (executive, technical, full-discovery) serao adicionados conforme a necessidade. Para um novo template:

1. Criar subpasta `report-templates/{nome}/`
2. Escrever `README.md` e `template.md` seguindo a spec em [schemas/template-syntax.md](schemas/template-syntax.md)
3. Registrar na tabela "Templates disponiveis" acima
