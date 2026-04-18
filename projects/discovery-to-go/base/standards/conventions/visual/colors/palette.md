---
title: Color Palette
description: Todos os CSS custom properties de cor para componentes de interface, com variantes dark e light.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - cor
  - paleta
  - token
  - tema
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Color Palette

CSS custom properties definidos em `:root` (dark, default) e `[data-theme-mode=light]`.

## Semantic Colors

| Token | Dark | Light |
|-------|------|-------|
| `--primary` | `#4DA8DA` | `#4DA8DA` |
| `--primary-dark` | `#3A8BB8` | `#3A8BB8` |
| `--primary-light` | `rgba(77,168,218,0.12)` | `rgba(77,168,218,0.1)` |
| `--secondary` | `#B9B7BD` | `#88878C` |
| `--success` | `#0ED145` | `#0A9E35` |
| `--success-light` | `rgba(14,209,69,0.12)` | `rgba(10,158,53,0.08)` |
| `--success-border` | `rgba(14,209,69,0.3)` | `rgba(10,158,53,0.25)` |
| `--warning` | `#F4AC00` | `#E67E22` |
| `--warning-light` | `rgba(244,172,0,0.12)` | `rgba(230,126,34,0.12)` |
| `--warning-border` | `rgba(244,172,0,0.3)` | `rgba(230,126,34,0.35)` |
| `--danger` | `#8B1A1A` | `#E74C3C` |
| `--danger-light` | `rgba(139,26,26,0.15)` | `rgba(231,76,60,0.10)` |
| `--danger-border` | `rgba(139,26,26,0.35)` | `rgba(231,76,60,0.30)` |
| `--info` | `#2EB5F5` | `#1E95CC` |
| `--info-light` | `rgba(46,181,245,0.12)` | `rgba(30,149,204,0.08)` |
| `--info-border` | `rgba(46,181,245,0.3)` | `rgba(30,149,204,0.25)` |

## Accent Colors

| Token | Dark | Light |
|-------|------|-------|
| `--purple` | `#9B96FF` | `#7B76FE` |
| `--purple-light` | `rgba(155,150,255,0.12)` | `rgba(123,118,254,0.08)` |
| `--orange` | `#FF9473` | `#FE7C58` |
| `--teal` | `#2DD4BF` | `#00D8D8` |

## Surface & Text

| Token | Dark | Light |
|-------|------|-------|
| `--bg` | `#141414` | `#F3F3F6` |
| `--card-bg` | `#2E2D32` | `#ffffff` |
| `--text` | `#E0DFE3` | `#1A1923` |
| `--text-muted` | `#88878C` | `#88878C` |
| `--border` | `#3E3D44` | `#B9B7BD` |

## Component Backgrounds

| Token | Dark | Light |
|-------|------|-------|
| `--header-bg` | `linear-gradient(135deg, #2E2D32 0%, #252428 50%, #1A1923 100%)` | (mesmo) |
| `--card-header-bg` | `#252428` | `rgba(77,168,218,0.12)` |
| `--th-bg` | `#252428` | `rgba(77,168,218,0.12)` |
| `--th-bg-hover` | `#36353B` | `rgba(77,168,218,0.22)` |
| `--card-shadow` | `0 2px 12px rgba(46,181,245,0.06), 0 1px 4px rgba(0,0,0,0.4)` | `0 2px 8px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.06)` |
| `--progress-track` | `#3E3D44` | `#B9B7BD` |

## Alert & Pill Text

| Token | Dark | Light |
|-------|------|-------|
| `--danger-text` | `#E85D54` | — |
| `--alert-warning-text` | `#f0c040` | `#C0392B` |
| `--alert-danger-text` | `#E85D54` | `#C0392B` |
| `--alert-info-text` | `#5FC8F8` | `#1670A0` |
| `--alert-success-text` | `#3DE06A` | `#087A28` |
| `--pill-success-text` | `#3DE06A` | `#087A28` |
| `--pill-info-text` | `#5FC8F8` | `#1670A0` |
| `--pill-warning-text` | `#f0c040` | `#C0392B` |

## Light-Only Tokens

| Token | Value |
|-------|-------|
| `--hover-border` | `#4DA8DA` |
