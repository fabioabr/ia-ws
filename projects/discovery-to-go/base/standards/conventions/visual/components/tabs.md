---
title: Tabs Component
description: Estilização completa para navegação por abas integrada ao header, tab content, offcanvas menu, compact mode, print e responsive.
project-name: global
version: 03.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - aba
  - navegacao
  - ui
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Tabs Component

As tabs ficam **dentro do header** (sobre o gradiente), não no body da página.

## Tabs Nav (`.tabs-nav`)

| Property | Value |
|----------|-------|
| Display | `flex` |
| Gap | `4px` |
| Margin top | `36px` |
| Overflow x | `auto` |
| Scrollbar width | `thin` |
| Scrollbar color | `rgba(255,255,255,0.25) transparent` |

### Scrollbar (webkit)

| Property | Value |
|----------|-------|
| Height | `4px` |
| Track | `transparent` |
| Thumb | `rgba(255,255,255,0.2)`, `border-radius: 4px` |
| Thumb hover | `rgba(255,255,255,0.35)` |

## Tab Button (`.tab-btn`)

| Property | Value |
|----------|-------|
| Padding | `10px 24px` |
| Background | `rgba(255,255,255,0.1)` |
| Border | `none` |
| Border radius | `10px 10px 0 0` |
| Color | `rgba(255,255,255,0.7)` |
| Font family | `'Poppins', sans-serif` |
| Font size | `0.85rem` |
| Font weight | `500` |
| Display | `flex` |
| Align items | `center` |
| Gap | `8px` |
| White space | `nowrap` |
| Cursor | `pointer` |
| Transition | `all 0.2s` |

### Icon

| Property | Value |
|----------|-------|
| Font size | `1.1rem` |

### States

| State | Background | Color | Font weight |
|-------|-----------|-------|-------------|
| Default | `rgba(255,255,255,0.1)` | `rgba(255,255,255,0.7)` | `500` |
| Hover | `rgba(255,255,255,0.18)` | `#FFFFFF` | `500` |
| Active | `var(--bg)` | `var(--text)` | `600` |

### Light Theme

| State | Override |
|-------|---------|
| Active | `color: #2E2D32` |

## Tab Count (`.tab-count`)

| Property | Value |
|----------|-------|
| Background | `rgba(255,255,255,0.2)` |
| Padding | `1px 8px` |
| Border radius | `10px` |
| Font size | `0.68rem` |
| Font weight | `600` |
| Color | `inherit` |

### Active State

| Property | Value |
|----------|-------|
| Background | `rgba(255,255,255,0.2)` |
| Color | `inherit` |

## Tab Content (`.tab-content`)

| Property | Value |
|----------|-------|
| Display | `none` (default) |
| Display active | `block` |
| Padding top | `24px` |
| Padding bottom | `32px` |

## Responsive (max-width: 768px)

| Property | Value |
|----------|-------|
| `.tabs-nav` | `flex-wrap: wrap` |
| `.tab-btn` | `padding: 8px 14px`, `font-size: 0.78rem` |

## Print

| Element | Value |
|---------|-------|
| `.tab-btn` | `display: none` |
| `.tab-content` | `display: block !important`, `page-break-inside: avoid` |

## Offcanvas Menu (`.offcanvas-menu`)

Navegação alternativa para mobile/compact mode.

| Property | Value |
|----------|-------|
| Position | `fixed`, `top: 0`, `right: -300px` |
| Width | `280px` |
| Height | `100vh` |
| Background | `var(--card-bg)` |
| Border left | `1px solid var(--border)` |
| z-index | `1050` |
| Transition | `right 0.3s ease` |
| Shadow | `-4px 0 24px rgba(0,0,0,0.3)` |
| Open state | `right: 0` |

### Menu Header

| Property | Value |
|----------|-------|
| Padding | `16px 20px` |
| Border bottom | `1px solid var(--border)` |
| Background | `var(--card-header-bg)` |
| Title color | `var(--primary)`, weight `600`, `14px` |

### Menu Item (`.nav-menu-item`)

| State | Background | Color |
|-------|-----------|-------|
| Default | `none` | `var(--text-muted)` |
| Hover | `rgba(77,168,218,0.08)` | `var(--text)` |
| Active | `rgba(77,168,218,0.15)` | `var(--primary)`, weight `600` |

| Property | Value |
|----------|-------|
| Padding | `10px 14px` |
| Border radius | `8px` |
| Font size | `13px` |
| Font weight | `500` |

### Backdrop (`.offcanvas-backdrop`)

| Property | Value |
|----------|-------|
| Background | `rgba(0,0,0,0.5)` |
| z-index | `1049` |
| Transition | `opacity 0.3s, visibility 0.3s` |
