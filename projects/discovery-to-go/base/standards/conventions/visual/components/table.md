---
title: Table Component
description: Estilização completa para tabelas de dados com header, rows, hover e code inline.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - tabela
  - estilizacao
  - ui
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Table Component

## Wrapper (`.table-wrapper`)

| Property | Value |
|----------|-------|
| Overflow x | `auto` |

## Table

| Property | Value |
|----------|-------|
| Width | `100%` |
| Border collapse | `collapse` |
| Font size | `0.82rem` |

## Header (`th`)

| Property | Value |
|----------|-------|
| Text align | `left` |
| Padding | `10px 14px` |
| Background | `var(--th-bg)` |
| Font weight | `600` |
| Border bottom | `2px solid var(--border)` |
| Font size | `0.75rem` |
| Text transform | `uppercase` |
| Letter spacing | `0.3px` |
| Color | `var(--text-muted)` |
| Transition | `background 0.2s` |

### Header Corners

| Position | Border radius |
|----------|--------------|
| First th | `8px 0 0 0` |
| Last th | `0 8px 0 0` |

## Rows

| Property | Value |
|----------|-------|
| Cell padding | `10px 14px` |
| Border bottom | `1px solid var(--border)` |
| Hover bg | `var(--primary-light)` |

## Inline Code

| Property | Value |
|----------|-------|
| Background | `var(--bg)` |
| Padding | `2px 6px` |
| Border radius | `4px` |
| Font size | `0.78rem` |
| Border | `1px solid var(--border)` |
| Font family | `'Consolas', 'Courier New', monospace` |
