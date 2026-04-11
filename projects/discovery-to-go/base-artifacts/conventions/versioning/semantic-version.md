---
title: Semantic Version
description: Formato de versionamento para documentos e artefatos.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - versionamento
  - padrao
  - documentacao
created: 2026-04-10 12:00
---

# Semantic Version

Versioning format for documents and artifacts.

## Standard

**Format:** `XX.YY.ZZZ`

| Segment | Range | Increment When |
|---------|-------|------------------------------------------------|
| XX | 00-99 | Rewrite of 50%+ of the content |
| YY | 00-99 | Section added, removed, or meaning changed |
| ZZZ | 000-999 | Minimal corrections (typos, formatting, links) |

## Examples

| Version | Meaning |
|-----------|----------------------------------------|
| `01.00.000` | First stable release |
| `01.01.000` | New section added |
| `01.01.001` | Typo fix |
| `02.00.000` | Major rewrite (50%+ changed) |
