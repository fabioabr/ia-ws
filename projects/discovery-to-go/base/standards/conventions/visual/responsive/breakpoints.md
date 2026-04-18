---
title: Responsive Breakpoints
description: Breakpoints, comportamento responsivo e compact mode extraídos do HTML de referência.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - responsivo
  - layout
  - breakpoint
created: 2026-04-10 12:00
updated: 2026-04-15
---

# Responsive Breakpoints

## Container

| Property | Value |
|----------|-------|
| Max width | `1400px` |
| Margin | `0 auto` |
| Padding | `24px 32px` (desktop) / `16px` (mobile) |

## Breakpoints

| Breakpoint | Value | Mudanças |
|------------|-------|----------|
| Mobile | `max-width: 768px` | Container: `padding: 16px` |
| | | `.tabs-nav`: `flex-wrap: wrap` |
| | | `.tab-btn`: `padding: 8px 14px`, `font-size: 0.78rem` |
| | | Stats grid: `grid-template-columns: 1fr` |
| | | Phase flow: `flex-direction: column` |
| | | `.pg-two-col`: `grid-template-columns: 1fr` |

## Compact Mode

Ativado via `body.compact-mode` quando a janela fica com 50% ou menos da largura da tela (`window.innerWidth <= screen.width * 0.5`).

| Elemento | Comportamento |
|----------|---------------|
| `.floating-menu-btn` | `display: flex` (visível) |
| `.tabs-nav` | `display: none` (escondido) |
| `.theme-toggle` (header) | `display: none` (escondido) |
| `.badge-version` (header) | `display: none` (escondido) |

Navegação passa para o **offcanvas menu** (`.offcanvas-menu`) com toggle switch de tema no rodapé.

## Print

| Elemento | Comportamento |
|----------|---------------|
| `body` | `background: white`, `color: #212B37` |
| `.header` | `background: #2E2D32` |
| `.tab-btn` | `display: none` |
| `.tab-content` | `display: block !important`, `page-break-inside: avoid` |
| `.card` | `break-inside: avoid` |
| `.card-body.collapsed` | `display: block` |
| `.search-container` | `display: none` |

## Scrollbar

| Property | Value |
|----------|-------|
| Width | `6px` |
| Height | `6px` |
| Track | `transparent` |
| Thumb | `rgba(77,168,218,0.3)`, `border-radius: 3px` |
