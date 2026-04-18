---
title: Stat Card Component
description: Estilização completa para cards de estatísticas com ícone, valor e label.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - stat-card
  - metrica
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Stat Card Component

## Grid (`.stats-grid`)

| Property | Value |
|----------|-------|
| Display | `grid` |
| Columns | `repeat(auto-fit, minmax(200px, 1fr))` |
| Gap | `16px` |
| Margin bottom | `28px` |

## Card (`.stat-card`)

| Property | Value |
|----------|-------|
| Background | `var(--card-bg)` |
| Border radius | `12px` |
| Padding | `18px 20px` |
| Box shadow | `var(--card-shadow)` |
| Border | `1px solid var(--border)` |
| Display | `flex`, `align-items: center` |
| Gap | `14px` |
| Transition | `box-shadow 0.2s, border-color 0.2s, background 0.2s` |

### Hover

| Property | Value |
|----------|-------|
| Border color | `var(--primary)` |
| Background | `var(--th-bg-hover)` |

### Light Theme

| Property | Value |
|----------|-------|
| Hover border | `var(--hover-border)` |
| Background | `var(--card-bg)` |

## Icon (`.stat-card-icon`)

| Property | Value |
|----------|-------|
| Width / Height | `44px` |
| Border radius | `10px` |
| Display | `flex`, centered |
| Font size | `1.3rem` |
| Flex shrink | `0` |

## Value (`.stat-card-number`)

| Property | Value |
|----------|-------|
| Font size | `1.12rem` |
| Font weight | `700` |
| Line height | `1.1` |
| Color | Token semântico do contexto |

## Label (`.stat-card-label`)

| Property | Value |
|----------|-------|
| Font size | `0.72rem` |
| Color | `var(--text-muted)` |
| Font weight | `500` |
| Text transform | `uppercase` |
| Letter spacing | `0.3px` |
