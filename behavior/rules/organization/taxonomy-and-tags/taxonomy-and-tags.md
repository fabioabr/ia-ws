---
title: Taxonomy and Tags
description: Convenções de tags e categorização para toda a base de conhecimento do workspace
project-name: global
version: 01.02.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - taxonomia
  - organizacao
created: 2026-04-02 09:00
---

# Taxonomia e Tags

Regra comportamental que garante que **toda a base de conhecimento seja pesquisável, consistente e navegável** por meio de tags padronizadas.

---

## 📋 Convenções aplicáveis

| Convenção | Referência |
| --------- | ---------- |
| Idioma, formato, estrutura e categorias de tags | `conventions/tags/taxonomy.md` |

A IA deve aplicar a convenção acima ao criar ou editar tags em qualquer documento.

---

## 📏 Comportamento obrigatório

> [!danger] Obrigatório
> Tags são **obrigatórias** em todo documento da base de conhecimento. Nenhum documento pode existir sem tags no frontmatter.

### Quando adicionar tags

- Na **criação** de qualquer documento
- Na **atualização** quando o escopo do documento mudar
- Na **revisão periódica** para eliminar sinônimos e manter consistência

### Regras de quantidade e qualidade

- Usar entre **2 e 5 tags** por documento — nem de menos (difícil encontrar), nem demais (poluição)
- Todo documento deve ter **pelo menos uma tag de categoria e uma de tema**
- Reutilizar tags existentes antes de criar novas — manter a consistência
- Tags devem ser **descritivas e específicas** — evitar tags genéricas como `geral` ou `outro`
- Revisar tags periodicamente para eliminar sinônimos e manter a base limpa

> [!danger] Proibido
> Nunca criar tags descartáveis ou temporárias. Toda tag deve ter valor permanente para a base de conhecimento.

---

## 🔗 Documentos Relacionados

- [[foundations/behavior-principles/behavior-principles]] — Princípios fundamentais que governam todas as regras incluindo taxonomia
- [[writing/markdown-writing/markdown-writing]] — Regras de formatação que definem o uso de tags no frontmatter
- [[organization/index-and-navigation/index-and-navigation]] — Regras de navegabilidade que complementam a categorização por tags
- [[organization/document-management/document-management]] — Ciclo de vida dos documentos onde as tags ajudam a identificar o estado

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição                                                        |
| --------- | ---------------- | ---------------------------------------------------------------- |
| 01.00.000 | 2026-04-02 09:00 | Criação do documento                                             |
| 01.00.001 | 2026-04-02 09:30 | Correção de contradição na seção de Idioma (acentos)             |
| 01.00.002 | 2026-04-02 10:00 | Adição de seção de documentos relacionados (backlinks)           |
| 01.00.003 | 2026-04-03 10:00 | Padronização de campos de data para Timestamp (yyyy-MM-DD HH:mm) |
| 01.00.004 | 2026-04-04 09:30 | Renomeação de taxonomia-e-tags para taxonomy-and-tags (naming-convention) |
| 01.01.000 | 2026-04-04 12:00 | Exceção ampliada: palavras em inglês absorvidas pelo uso cotidiano em pt-BR são permitidas como tags |
| 01.02.000 | 2026-04-10 12:00 | Refatoração: conteúdo de convenção extraído para conventions/tags/taxonomy.md; regra mantém apenas instruções comportamentais |
