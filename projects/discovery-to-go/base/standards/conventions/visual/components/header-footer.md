---
title: Header & Footer
description: Estilização completa para header e footer de página com gradiente, badges e back-to-top.
project-name: global
version: 02.00.000
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
updated: 2026-04-15
---

# Header & Footer

## Header (`.header`)

Container principal com gradiente, título, badges e tabs integradas.

| Property | Value |
|----------|-------|
| Background | `linear-gradient(135deg, #2E2D32 0%, #252428 50%, #1A1923 100%)` |
| Color | `white` |
| Position | `relative` |
| Overflow | `hidden` |
| Decorative circle | `::before` com `rgba(255,255,255,0.03)` |
| Theme | Idêntico em dark e light |

As tabs (`.tabs-nav`) ficam dentro do header — ver `tabs.md`.

### Title

| Property | Value |
|----------|-------|
| Color | `#fff` |
| Font size | `22px` |
| Font weight | `600` |
| Icon color | `var(--primary)`, `margin-right: 10px` |

### Subtitle

| Property | Value |
|----------|-------|
| Color | `rgba(255,255,255,0.5)` |
| Font size | `13px` |
| Margin top | `4px` |

### Badge Version

| Property | Value |
|----------|-------|
| Background | `rgba(77,168,218,0.2)` |
| Color | `var(--primary)` |
| Padding | `4px 12px` |
| Border radius | `20px` |
| Font size | `12px` |
| Font weight | `500` |

### Theme Toggle

| Property | Value |
|----------|-------|
| Background | `rgba(255,255,255,0.1)` |
| Border | `1px solid rgba(255,255,255,0.2)` |
| Color | `#fff` |
| Border radius | `6px` |
| Padding | `6px 12px` |
| Hover bg | `rgba(255,255,255,0.2)` |

## Footer (`.footer`)

| Property | Value |
|----------|-------|
| Background | Mesmo gradiente do header |
| Color | `white` |
| Padding | `36px 0` |
| Overflow | `hidden` |

### Footer Content

| Property | Value |
|----------|-------|
| Display | `flex`, `justify-content: space-between`, `align-items: center`, `flex-wrap: wrap` |
| Gap | `24px` |

### Author Section

| Element | Size | Weight |
|---------|------|--------|
| Avatar | `48x48px`, `border-radius: 12px` |
| Name | `0.95rem` | `600` |
| Role | `0.78rem` | `opacity: 0.7` |
| Date | `0.72rem` | `opacity: 0.55` |

### Document Info (right)

| Element | Size | Opacity |
|---------|------|---------|
| Title | `0.85rem`, weight `500` | `0.9` |
| Detail | `0.72rem` | `0.6` |

### Seal

| Property | Value |
|----------|-------|
| Border top | `1px solid rgba(255,255,255,0.12)` |
| Font size | `0.7rem` |
| Opacity | `0.5` |
| Icon size | `1rem` |

## Back-to-Top (`.back-to-top`)

| Property | Value |
|----------|-------|
| Position | `fixed`, `bottom: 32px`, `right: 32px` |
| Size | `44x44px` |
| Border radius | `12px` |
| Background | `var(--info)` |
| Color | `white` |
| Font size | `1.3rem` |
| Shadow | `0 4px 16px rgba(46,181,245,0.35)` |
| Hover bg | `#1E95CC` |
| Hover shadow | `0 6px 20px rgba(46,181,245,0.5)` |
| Transition | `opacity 0.3s, visibility 0.3s, transform 0.3s` |
| z-index | `999` |

## Floating Menu (`.floating-menu-btn`)

| Property | Value |
|----------|-------|
| Position | `fixed`, `bottom: 32px`, `right: 84px` |
| Size | `44x44px` |
| Border radius | `12px` |
| Background | `var(--primary)` |
| Color | `#1A1923` |
| Hover bg | `var(--primary-dark)` |
| z-index | `999` |
| Display | `none` (visible in compact mode) |

## Offcanvas Menu (`.offcanvas-menu`)

Menu lateral que substitui as tabs em compact mode. Inclui toggle switch de tema no rodapé.

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

### Theme Toggle (offcanvas rodapé)

Toggle switch com sol/lua e dot animado.

| Property | Value |
|----------|-------|
| Track | `40x22px`, `border-radius: 11px`, `background: var(--border)` |
| Dot | `18x18px`, circle, `background: var(--primary)` |
| Dark state | dot `left: 20px` (lua) |
| Light state | dot `left: 2px` (sol) |
| Transition | `left 0.2s` |
