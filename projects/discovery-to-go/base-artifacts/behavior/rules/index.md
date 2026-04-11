---
title: Rules Index
description: Índice central das regras de comportamento para AI assistants
project-name: global
version: 02.01.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - indice
  - comportamento
created: 2026-04-02 09:00
---

# 📚 Rules Index

Índice central das regras de comportamento para AI assistants. Este arquivo é o ponto de entrada para qualquer projeto que referencie o behavior global.

---

## 🏛️ Foundations

Princípios e limites que governam o comportamento da IA.

- [[foundations/behavior-principles/behavior-principles]] — Princípios fundamentais que regem toda a base de regras e o comportamento da IA
- [[foundations/project-boundaries/project-boundaries]] — Como a IA deve buscar, respeitar e reagir a fronteiras definidas por cada projeto

---

## ✍️ Writing

Padrões de escrita, formatação e qualidade dos dados gerados.

- [[writing/markdown-writing/markdown-writing]] — Regras de formatação e estrutura para todos os arquivos .md
- [[writing/naming-convention/naming-convention]] — Regra de nomenclatura em inglês para arquivos, pastas, skills e agents
- [[writing/acronym-glossary/acronym-glossary]] — Tratamento obrigatório de siglas em HTML e MD: destaque visual, tooltip, glossário como última aba/seção
- [[writing/hallucination-guard/hallucination-guard]] — Proteção contra alucinação de LLM — dados não verificáveis devem ser sinalizados

---

## 🗂️ Organization

Estrutura, navegação e ciclo de vida dos documentos.

- [[organization/taxonomy-and-tags/taxonomy-and-tags]] — Convenções de tags e categorização para toda a base de conhecimento
- [[organization/index-and-navigation/index-and-navigation]] — Regras para manutenção de índices e navegabilidade entre documentos
- [[organization/document-management/document-management]] — Ciclo de vida dos documentos: criação, atualização, arquivamento e obsolescência

---

## 💻 Code

Regras para estrutura de código, skills e agentes.

- [[code/skill-structure/skill-structure]] — Estrutura obrigatória do SKILL.md — formato universal compatível com Obsidian, Claude Code, OpenCode e Antigravity

---

## 🔮 Categorias Futuras

Categorias reservadas para expansão conforme o workspace evolui:

- **💻 Code** — Regras adicionais (linting, padrões, segurança, testes)
- **🎨 Design** — Regras de design system, paleta de cores, componentes visuais
- **🔀 Git** — Convenções de commit, branching, PR
- **💬 Communication** — Tom, idioma, formato de respostas ao usuário
- **🔒 Security** — Proteção de dados sensíveis, validação de inputs, compliance

---

> [!info] Regras do pipeline de discovery foram movidas para `projects/discovery-to-go/rules/`

## 🔗 Documentos Relacionados

- [[foundations/behavior-principles/behavior-principles]] — Princípios que governam toda a base de regras
- [[writing/markdown-writing/markdown-writing]] — Regras de formatação que este índice segue

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição                                        |
| --------- | ---------------- | ------------------------------------------------ |
| 01.00.000 | 2026-04-02 09:00 | Criação do índice                                |
| 01.01.000 | 2026-04-03 10:30 | Adição de frontmatter e padronização Obsidian    |
| 01.02.000 | 2026-04-03 11:00 | Adição da categoria Criação de Documentos        |
| 01.02.001 | 2026-04-03 11:30 | Adição de fronteiras-de-projeto ao core           |
| 01.03.000 | 2026-04-03 13:00 | Adição de levantamento-de-projeto ao core         |
| 01.04.000 | 2026-04-03 16:00 | Renomeação de levantamento-de-projeto para discovery e log-de-levantamento para log-de-discovery |
| 01.05.000 | 2026-04-04 09:30 | Renomeação de todos os wikilinks para nomes em inglês (naming-convention) |
| 01.06.000 | 2026-04-04 | Adição de [[core/iteration-loop/iteration-loop]] ao core — conceito de iterações incrementais do pipeline |
| 01.07.000 | 2026-04-05 10:00 | Adição de [[core/hallucination-guard/hallucination-guard]], correção 7 etapas no creation-flow, correções do challenger report |
| 01.08.000 | 2026-04-05 | Correção terminologia: "3 níveis" → "3 sub-etapas com mini-ciclos" na descrição de discovery |
| 01.09.000 | 2026-04-09 | Adição de report-html-bar-colors (movido para assets/ui-ux/) |
| 01.10.000 | 2026-04-09 | Remoção da categoria document-creation (creation-flow e bar-colors movidos/excluídos) |
| 01.11.000 | 2026-04-09 | Movidas 6 regras de discovery para projects/discovery-to-go/rules/ |
| 02.00.000 | 2026-04-09 | Reorganização: core/ → 3 categorias (foundations, writing, organization) + categorias futuras |
| 02.01.000 | 2026-04-09 | Primeira regra em code/: skill-structure (formato universal SKILL.md) |
