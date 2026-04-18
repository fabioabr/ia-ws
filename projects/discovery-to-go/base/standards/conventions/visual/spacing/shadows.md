---
title: Box Shadows
description: Tokens de sombra para elevação por tema, incluindo sombras específicas de componentes.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - sombra
  - token
  - tema
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Box Shadows

## Card Shadow (`--card-shadow`)

| Theme | Value |
|-------|-------|
| Dark | `0 2px 12px rgba(46,181,245,0.06), 0 1px 4px rgba(0,0,0,0.4)` |
| Light | `0 2px 8px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.06)` |

## Component Shadows

| Component | Shadow |
|-----------|--------|
| Card (default) | `0 2px 8px rgba(0,0,0,0.03)` |
| Card (hover) | `var(--card-shadow)` |
| Back-to-top | `0 4px 16px rgba(46,181,245,0.35)` |
| Back-to-top (hover) | `0 6px 20px rgba(46,181,245,0.5)` |
| Floating menu | `0 4px 16px rgba(77,168,218,0.35)` |
| Floating menu (hover) | `0 6px 20px rgba(77,168,218,0.5)` |
| Offcanvas menu | `-4px 0 24px rgba(0,0,0,0.3)` |
| Acronym tooltip | `0 4px 12px rgba(0,0,0,0.3)` |
