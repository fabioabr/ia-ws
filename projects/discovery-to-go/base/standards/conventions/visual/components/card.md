---
title: Card Component
description: Estilização completa para cards com header, body e estados hover extraídos do HTML.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - card
  - layout
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Card Component

## Container (`.card`)

| Property | Value |
|----------|-------|
| Background | `var(--card-bg)` |
| Border radius | `12px` |
| Border | `1px solid var(--border)` |
| Box shadow | `0 2px 8px rgba(0,0,0,0.03)` |
| Overflow | `hidden` |
| Margin bottom | `20px` |
| Transition | `box-shadow 0.2s, border-color 0.2s` |

### Hover

| Property | Value |
|----------|-------|
| Box shadow | `var(--card-shadow)` |
| Border color | `var(--primary)` |
| Card header bg | `var(--th-bg-hover)` |

### Light Theme Hover

| Property | Value |
|----------|-------|
| Border color | `var(--hover-border)` — `#4DA8DA` |

## Header (`.card-header`)

| Property | Value |
|----------|-------|
| Display | `flex` |
| Align items | `center` |
| Gap | `10px` |
| Padding | `14px 18px` |
| Border bottom | `1px solid var(--border)` |
| Background | `var(--card-header-bg)` |

### Header Icon (`.card-header-icon`)

| Property | Value |
|----------|-------|
| Width / Height | `32px` |
| Border radius | `8px` |
| Display | `flex`, centered |
| Font size | `1rem` |

### Header Title (`.card-title`)

| Property | Value |
|----------|-------|
| Font weight | `600` |
| Font size | `0.95rem` |
| Flex | `1` |
| Color | `var(--text)` |

## Body (`.card-body`)

| Property | Value |
|----------|-------|
| Padding | `18px` |
| Color | `var(--text)` |
| Opacity | `0.85` |

### Collapsed State

`.card-body.collapsed` — `display: none` (toggle via JS)
