---
title: Badge Component
description: Estilização para pills e badges inline com todas as variantes de cor extraídas do HTML.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - badge
  - pill
  - estilo
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Badge Component

## Pill (`.pill`)

| Property | Value |
|----------|-------|
| Display | `inline-block` |
| Padding | `2px 10px` |
| Border radius | `12px` |
| Font size | `0.7rem` |
| Font weight | `600` |

### Pill Variants

| Class | Background | Text | Border |
|-------|-----------|------|--------|
| `.pill-success` | `var(--success-light)` | `var(--pill-success-text)` | `1px solid var(--success-border)` |
| `.pill-info` | `var(--info-light)` | `var(--pill-info-text)` | `1px solid var(--info-border)` |
| `.pill-warning` | `var(--warning-light)` | `var(--pill-warning-text)` | `1px solid var(--warning-border)` |
| `.pill-danger` | `var(--danger-light)` | `var(--alert-danger-text)` | `1px solid var(--danger-border)` |
| `.pill-purple` | `var(--purple-light)` | `var(--purple)` | `1px solid rgba(155,150,255,0.3)` |

## Card Badge (`.card-badge`)

| Property | Value |
|----------|-------|
| Padding | `2px 10px` |
| Border radius | `12px` |
| Font size | `0.7rem` |
| Font weight | `600` |
| White space | `nowrap` |

## Tab Count (`.tab-count`)

| Property | Dark | Light |
|----------|------|-------|
| Background | `rgba(255,255,255,0.2)` | `rgba(0,0,0,0.08)` |
| Padding | `1px 8px` | — |
| Border radius | `10px` | — |
| Font size | `0.68rem` | — |
| Font weight | `600` | — |
| Color | `inherit` | — |

## Header Badge (`.header-badge`)

| Property | Value |
|----------|-------|
| Background | `rgba(255,255,255,0.15)` |
| Padding | `6px 14px` |
| Border radius | `8px` |
| Font size | `0.78rem` |
| Backdrop filter | `blur(10px)` |
| Color | `white` |
