---
title: "Headings"
description: "Regras de hierarquia de headings para documentos Markdown"
project-name: "global"
version: "01.00.000"
status: "ativo"
author: "claude-code"
category: "convention"
area: "tecnologia"
tags: [heading, hierarquia, markdown, estrutura]
created: "2026-04-10 12:00"
---

# Headings

Heading hierarchy rules for Markdown documents.

## Standard

| Level | Usage | Rule |
|-------|----------------------|--------------------------------------|
| H1 | Document title | Exactly 1 per file, matches frontmatter `title` |
| H2 | Main sections | Primary content divisions |
| H3 | Sub-sections | Details within an H2 |
| H4 | Rare sub-sub-sections | Only when clearly justified |

- **Never skip levels** (e.g., no H2 followed directly by H4).
- H5 and H6 are not used.
