---
title: Chart.js Configuration
description: Configuração padrão de gráficos Chart.js — tooltip, grid, legenda e tipos de gráfico.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - chartjs
  - grafico
  - visualizacao
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Chart.js Configuration

## Library

| Property | Value |
|----------|-------|
| Version | Chart.js **v4.4.7** |
| Source | CDN |
| Colors | `--chart-1` a `--chart-5`, lidas via `getComputedStyle()` |
| Theme toggle | Rebuild completo dos charts no toggle |

## Tooltip

| Property | Value |
|----------|-------|
| Background | `var(--card-bg)` |
| Border | `var(--border)` |
| Border radius | `8px` |
| Font family | `Poppins` |

## Grid & Ticks

| Property | Value |
|----------|-------|
| Grid color | `var(--border)` |
| Tick color | `var(--text-muted)` |
| Tick font | `Poppins, 11px` |

## Legend

| Property | Value |
|----------|-------|
| Use point style | `true` |
| Point style | `'circle'` |
| Font family | `Poppins` |

## Chart Types

| Type | Key Settings |
|------|-------------|
| Bar | `borderRadius: 6`, `borderSkipped: false` |
| Doughnut | `cutout: '55%'`, height `180px`, legend position `right` |
| Line | `fill: true`, `tension: 0.4`, area opacity `0x22` |
| Radar | Grid `var(--border)`, `backdropColor: 'transparent'` |
