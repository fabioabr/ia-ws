---
title: Acronym Treatment in Markdown
description: Regras de uso e expansão de siglas em documentos Markdown.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - sigla
  - markdown
  - glossario
created: 2026-04-10 12:00
---

# Acronym Treatment in Markdown

How to handle acronyms in Markdown documents.

## Standard

1. **First occurrence:** write full form followed by acronym in parentheses.
2. **Subsequent occurrences:** acronym only.
3. **Glossary:** add a glossary section if 3 or more acronyms are used.

### Glossary Table Format

| Sigla | Significado | Contexto |
|-------|-------------|----------|
| API | Application Programming Interface | Integração de sistemas |
| CLI | Command-Line Interface | Ferramentas de terminal |

### Exempt Acronyms

These are universally known and never need expansion:

`HTTP` | `HTTPS` | `URL` | `HTML` | `CSS` | `JS` | `PDF` | `PNG` | `JPG` | `CSV` | `JSON` | `XML` | `BR` | `US` | `EU`

## Example

> O sistema utiliza uma Interface de Programação de Aplicações (API) para comunicação. A API expõe endpoints REST.
