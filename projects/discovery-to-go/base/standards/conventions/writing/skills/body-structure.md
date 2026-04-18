---
title: Skill Body Structure
description: Ordem padrao de secoes para arquivos de definicao de skills.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - skill
  - estrutura
  - padrao
created: 2026-04-10 12:00
---

# Skill Body Structure

Standard section order for skill definition files.

## Standard

### Required Order

1. **Frontmatter** — metadata block
2. **Title + Identity** — skill name and role definition
3. **Instructions** — core behavioral instructions
4. **Examples** — minimum 2 examples
5. **Constraints** — limitations and guardrails
6. **antigravity** — Antigravity-specific section
7. **claude-code** — Claude Code-specific section
8. **open-code** — Open Code-specific section

### Notes

- Platform sections (antigravity, claude-code, open-code) are **optional**
- All other sections are required
