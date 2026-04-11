---
title: Header & Footer
description: Estilização padrão para header e footer de página com gradiente e temas.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - header
  - footer
  - layout
created: 2026-04-10 12:00
---

# Header & Footer

Standard styling for page header and footer.

## Standard

### Header

| Property | Value |
|---|---|
| Background | Gradient: `#2E2D32` → `#252428` → `#1A1923` |
| Theme | Identical in both dark and light modes |
| Text | `#FFFFFF` |
| Badges | `background: rgba(255,255,255,0.15)` with `backdrop-filter: blur()` |

### Footer

- Company logo with automatic dark/light swap
- Back-to-top button: `color: var(--info)`
- Background: same gradient as header
- Text: `#FFFFFF`
