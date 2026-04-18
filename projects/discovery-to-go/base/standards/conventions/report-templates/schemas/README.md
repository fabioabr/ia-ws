---
title: Report Template Schemas
description: Documentacao da sintaxe formal dos templates de relatorio e controle de filtros de variante implementados.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: documentation
area: tecnologia
tags:
  - schema
  - report-templates
  - syntax
  - parser
created: 2026-04-17
updated: 2026-04-17
---

# Report Template Schemas

Pasta de documentacao da sintaxe dos templates de relatorio e controle do que ja foi implementado.

## Contents

- [template-syntax.md](template-syntax.md) — spec formal da sintaxe do arquivo `template.md` (frontmatter, custom regions, sub-templates, layout, filtros `:variant`)
- [TODO.md](TODO.md) — lista de filtros `:variant` implementados vs pendentes, organizada por REG-ID. Atualizar sempre que um filtro novo for usado em algum template.

## Como usar

- Autor de template novo: ler `template-syntax.md` e seguir a gramatica
- Implementador do parser/composer: `template-syntax.md` e a referencia canonica da sintaxe
- Quem adiciona um filtro novo: registrar em `TODO.md` antes de usar em template
