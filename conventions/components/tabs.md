---
title: "Tabs Component"
description: "Padrao de estilizacao para navegacao por abas em componentes UI"
project-name: "global"
version: "01.00.000"
status: "ativo"
author: "claude-code"
category: "convention"
area: "tecnologia"
tags: [componente, aba, navegacao, ui]
created: "2026-04-10 12:00"
---

# Tabs Component

Standard styling for tab navigation.

## Standard

| State | Background | Text |
|---|---|---|
| Inactive | `rgba(255,255,255,0.1)` | `rgba(255,255,255,0.7)` |
| Hover | `rgba(255,255,255,0.18)` | `#FFFFFF` |
| Active | `var(--bg)` | `var(--text)` |

### Tab Count Badge

- Inherits parent text color

### Scrollbar

- Style: `thin`, width `4px`
- Color: translucent
- Direction: horizontal
