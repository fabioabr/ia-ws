---
title: "Table Component"
description: "Padrao de estilizacao para tabelas de dados em componentes UI"
project-name: "global"
version: "01.00.000"
status: "ativo"
author: "claude-code"
category: "convention"
area: "tecnologia"
tags: [componente, tabela, estilizacao, ui]
created: "2026-04-10 12:00"
---

# Table Component

Standard styling for data tables.

## Standard

### Header

| Property | Value |
|---|---|
| Background | `var(--th-bg)` |
| Text color | `var(--text-muted)` |
| Transform | `uppercase` |
| Font size | `0.75rem` |

### Rows

- Hover: `background: var(--primary-light)`

### Content

- Highlighted text: `var(--info)` or `var(--primary)`
- Numeric values: `font-family: Consolas, monospace`, `text-align: right`
