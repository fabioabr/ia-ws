---
title: Stat Card Component
description: Estilização padrão para cards de estatísticas e métricas com ícone e valor.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - stat-card
  - metrica
created: 2026-04-10 12:00
---

# Stat Card Component

Standard styling for statistic/metric cards.

## Standard

### Layout

- Icon: `44x44px`, `border-radius: 10px`
- Value + Label stacked beside icon

### Value

- Color: semantic token matching context
  - `var(--primary)`, `var(--info)`, `var(--success)`, `var(--warning)`

### Label

| Property | Value |
|---|---|
| Color | `var(--text-muted)` |
| Transform | `uppercase` |
| Font size | `0.72rem` |
