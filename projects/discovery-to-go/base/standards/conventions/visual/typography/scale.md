---
title: Typography Scale
description: Escala tipográfica, font families e estilos de texto extraídos do HTML de referência.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - tipografia
  - token
  - escala
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Typography Scale

## Font Families

| Usage | Font | Fallback |
|-------|------|----------|
| Interface | `Poppins` (Google Fonts, weights 300-700) | `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` |
| Code | `Consolas` | `'Courier New', monospace` |

## Base

| Property | Value |
|----------|-------|
| Font size | `14px` |
| Line height | `1.6` |

## Scale

| Token | Size | Weight | Line Height | Uso |
|-------|------|--------|-------------|-----|
| Display | `22px` | 600 | 1.2 | Header h1 |
| H1 | `1.15rem` | 600 | 1.3 | Section titles |
| H2 | `0.95rem` | 600 | 1.3 | Card titles |
| Body | `0.88rem` | 400 | 1.6 | Intro text, parágrafos |
| Body Small | `0.82rem` | 400 | 1.5 | Tabelas, alertas |
| Caption | `0.72rem` | 600 | 1.4 | Labels, stat-card labels, timestamps |
| Code | `0.78rem` | 400 | 1.6 | Code blocks, inline code |
| Micro | `0.7rem` | 600 | 1.2 | Pills, badges, card badges |
| Badge Version | `12px` | 500 | — | Header version badge |

## Text Transforms

| Context | Transform | Letter Spacing |
|---------|-----------|---------------|
| Table headers (`th`) | `uppercase` | `0.3px` |
| Stat card labels | `uppercase` | `0.3px` |
| Section count badges | — | — |
