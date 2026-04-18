# report-composer

Skill que materializa relatorios a partir de **report-templates**. Le o `setup.md` do projeto para descobrir quais templates rodar, invoca o parser Python `support-tools/template-parser/` para obter a AST de cada template, resolve placeholders contra os resultados do run e gera o `.md` composto. No final, delega ao `md-writer` para polir.

## Quando usar

- Na Fase 3 (Delivery), **antes** do `report-planner` e do `html-writer`, para cada relatorio declarado no `setup.md`
- Sempre que um template de `report-templates/` precisar ser instanciado

## O que consome

- `setup.md` do run (lista de reports + cenarios)
- `standards/conventions/report-templates/{id}/template.md` (o template)
- `custom-artifacts/{client}/templates/report-templates/{id}/template.md` (override, se existir)
- `iterations/iteration-N/results/` (conteudo consolidado para resolver REG-IDs)
- `standards/conventions/report-regions/schemas/` (schema de cada region)
- `standards/conventions/report-templates/schemas/TODO.md` (quais filtros estao implementados)

## O que produz

- `delivery/composed-{template-id}.md` — relatorio composto pronto para o md-writer

## Dependencias

- Python 3.10+ com `pyyaml` instalado (ver `support-tools/template-parser/requirements.txt`)
- `md-writer` skill (chamado ao final)
- `html-writer` skill (proximo passo do pipeline apos md-writer)

Spec completa: `SKILL.md`.
