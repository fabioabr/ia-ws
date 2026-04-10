---
title: Index and Navigation
description: Regras para manutenção de índices e navegabilidade entre documentos do workspace
project-name: global
version: 01.01.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - navegacao
  - indice
  - organizacao
created: 2026-04-02 09:00
---

# Índice e Navegação

Regra comportamental para garantir que **todo conteúdo do workspace seja localizável e navegável**. Aplica-se a qualquer área: regras, documentação, projetos, notas, etc.

---

## 📋 Convenções aplicáveis

| Convenção | Referência |
| --------- | ---------- |
| Sintaxe e regras de wikilinks | `conventions/markdown/wikilinks.md` |
| Estrutura e formato do index.md | `conventions/file-structure/index-structure.md` |

A IA deve aplicar as convenções acima ao criar ou manter índices e links entre documentos.

---

## 📚 Índices

> [!danger] Obrigatório
> Toda área que agrupe documentos **deve ter um `index.md`** como ponto de entrada.

### Regras de organização

- Listar documentos **agrupados por categoria/seção** quando houver mais de 5 itens
- Manter a lista em **ordem lógica** (não necessariamente alfabética — priorizar relevância)
- Nunca deixar um documento fora do índice da sua área

---

## 🔗 Backlinks

> [!warning] Obrigatório
> Todo documento deve referenciar **documentos relacionados** via wikilinks, criando uma rede de navegação entre conteúdos.

### Regras de backlinks

- Incluir descrição explicando **por que** o documento está relacionado
- Mínimo 1 backlink por documento
- Não referenciar a si mesmo
- Sem links órfãos — não referenciar documentos que não existem

---

## 🤖 Manutenção pela IA

> [!danger] Obrigatório
> Ao **criar, renomear ou remover** um documento, a IA **deve obrigatoriamente** atualizar todos os índices e backlinks afetados.

### Checklist de manutenção

Sempre que um documento for **criado**:

- [ ] Adicionar entrada no `index.md` da área correspondente
- [ ] Adicionar seção de backlinks no novo documento
- [ ] Verificar se documentos existentes devem referenciar o novo documento

Sempre que um documento for **removido**:

- [ ] Remover entrada do `index.md`
- [ ] Remover backlinks para o documento em todos os outros documentos
- [ ] Verificar se algum índice ficou vazio

Sempre que um documento for **renomeado**:

- [ ] Atualizar entrada no `index.md`
- [ ] Atualizar todos os wikilinks que referenciam o documento

> [!warning] Atenção
> A IA **nunca deve deixar links quebrados** na base de conhecimento. Toda operação que altere a estrutura de documentos exige verificação de integridade dos links.

---

## 🔗 Documentos Relacionados

- [[foundations/behavior-principles/behavior-principles]] — Princípios fundamentais que governam o behavior e o registro de desvios
- [[writing/markdown-writing/markdown-writing]] — Regras de formatação e estrutura que os índices devem seguir
- [[organization/taxonomy-and-tags/taxonomy-and-tags]] — Tags de categorização que complementam a navegação por índice
- [[organization/document-management/document-management]] — Regras de ciclo de vida que afetam a manutenção dos índices

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição                                                        |
| --------- | ---------------- | ---------------------------------------------------------------- |
| 01.00.000 | 2026-04-02 09:00 | Criação do documento                                             |
| 01.00.001 | 2026-04-03 10:00 | Padronização de campos de data para Timestamp (yyyy-MM-DD HH:mm) |
| 01.00.002 | 2026-04-04 09:30 | Renomeação de indice-e-navegacao para index-and-navigation (naming-convention) |
| 01.01.000 | 2026-04-10 12:00 | Refatoração: conteúdo de convenção extraído para conventions/; regra mantém apenas instruções comportamentais |
