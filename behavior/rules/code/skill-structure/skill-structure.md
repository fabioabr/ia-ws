---
title: Skill Structure
description: Estrutura obrigatória do SKILL.md — formato universal compatível com Obsidian, Claude Code, OpenCode e Antigravity
project-name: global
version: 01.01.000
status: ativo
author: claude-code
category: code
area: tecnologia
tags:
  - skill
  - structure
  - claude-code
  - open-code
  - antigravity
  - obsidian
created: 2026-04-09
---

# Skill Structure

Regra comportamental que define a estrutura obrigatória para todo arquivo `SKILL.md`. O formato é **universal** — um único arquivo funciona no Obsidian (documentação), Claude Code, OpenCode e Antigravity.

---

## 📋 Convenções aplicáveis

| Convenção | Referência |
| --------- | ---------- |
| Campos do frontmatter (obrigatórios, opcionais, schema de inputs/outputs) | `conventions/frontmatter/skill-schema.md` |
| Ordem das seções do corpo, exemplos por plataforma | `conventions/skills/body-structure.md` |

A IA deve aplicar as convenções acima ao criar ou editar qualquer SKILL.md.

---

## 📏 Regras comportamentais

### Estrutura de arquivos

1. **Um SKILL.md por pasta** — cada skill vive em `skills/{nome}/SKILL.md`
2. **Nome da pasta = campo `name`** — `skills/report-maker/` implica `name: report-maker`

### Nomenclatura

3. **Inglês** — nome, description e seções em inglês (conforme naming-convention)
4. **Corpo em português ou inglês** — instructions podem ser no idioma do projeto

### Frontmatter

5. **Frontmatter nunca vazio** — no mínimo os campos obrigatórios definidos na convenção `conventions/frontmatter/skill-schema.md`

### Inputs e Outputs

6. **inputs/outputs são documentação** — plataformas que não suportam ignoram silenciosamente; o objetivo é documentar o contrato da skill para humanos e orquestradores

### Seções de plataforma

7. **Seções de plataforma são opcionais** — a skill funciona sem elas; cada engine lê apenas a sua

---

## 🔗 Documentos Relacionados

- [[writing/naming-convention/naming-convention]] — Nomenclatura em inglês para skills
- [[writing/acronym-glossary/acronym-glossary]] — Tratamento de siglas no corpo da skill

## 📜 Histórico de Alterações

| Versão    | Data       | Descrição |
|-----------|------------|-----------|
| 01.00.000 | 2026-04-09 | Criação — formato universal compatível com Obsidian, Claude Code, OpenCode e Antigravity |
| 01.01.000 | 2026-04-10 | Refatoração: schema do frontmatter, inputs/outputs, corpo e templates extraídos para conventions/; regra mantém apenas instruções comportamentais |
