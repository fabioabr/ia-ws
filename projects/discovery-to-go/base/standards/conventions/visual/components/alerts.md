---
title: Alerts Component
description: Estilização completa para mensagens de alerta com CSS properties extraídos do HTML.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - alerta
  - estilo
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Alerts Component

## Layout

| Property | Value |
|----------|-------|
| Padding | `12px 16px` |
| Border radius | `8px` |
| Font size | `0.82rem` |
| Display | `flex` |
| Align items | `center` |
| Gap | `10px` |
| Margin bottom | `10px` |
| Border | `1px solid` |
| Icon size | `1.1rem`, `flex-shrink: 0` |

## Variants

| Variant | Background | Border | Text |
|---------|-----------|--------|------|
| `.alert-success` | `var(--success-light)` | `var(--success-border)` | `var(--alert-success-text)` |
| `.alert-warning` | `var(--warning-light)` | `var(--warning-border)` | `var(--alert-warning-text)` |
| `.alert-danger` | `var(--danger-light)` | `var(--danger-border)` | `var(--alert-danger-text)` |
| `.alert-info` | `var(--info-light)` | `var(--info-border)` | `var(--alert-info-text)` |
