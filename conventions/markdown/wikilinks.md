---
title: Wikilinks
description: Convencoes de links para documentos baseados em Obsidian.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - markdown
  - obsidian
  - link
created: 2026-04-10 12:00
---

# Wikilinks

Linking conventions for Obsidian-based documents.

## Standard

| Element | Syntax | Example |
|-----------|------------------|---------------------------------------|
| Document | Wikilink | `[[conventions/tags/taxonomy]]` |
| Skill | Inline code | `/validate-doc` |
| File path | Inline code | `conventions/naming/file-naming.md` |

- Use **absolute paths** from the vault root.
- Wikilinks resolve via Obsidian's link system.
- Skills and paths use backtick inline code for visual distinction.
