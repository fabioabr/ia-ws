---
title: Badge Component
description: Estilização padrão para badges inline com variantes de cor.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - badge
  - estilo
created: 2026-04-10 12:00
---

# Badge Component

Standard styling for inline badges.

## Standard

| Property | Value |
|---|---|
| Display | Inline |
| Border radius | `12px` |
| Font size | `0.7rem` |
| Sizing | Compact (minimal padding) |

### Color Variants

Same logic as alerts:

| Variant | Uses |
|---|---|
| Success | `var(--success-light)` bg, `var(--success-border)` border, `var(--alert-success-text)` text |
| Warning | `var(--warning-light)` bg, `var(--warning-border)` border, `var(--alert-warning-text)` text |
| Danger | `var(--danger-light)` bg, `var(--danger-border)` border, `var(--alert-danger-text)` text |
| Info | `var(--info-light)` bg, `var(--info-border)` border, `var(--alert-info-text)` text |
