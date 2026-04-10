---
title: Document Management
description: Ciclo de vida dos documentos — criação, atualização, arquivamento e obsolescência
project-name: global
version: 01.04.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - documentacao
  - gestao
  - ciclo-de-vida
created: 2026-04-03 09:00
---

# Gestão de Documentação

Regra comportamental que define o **ciclo de vida** de todo documento no workspace — desde a criação até a obsolescência. Garante que a base de conhecimento se mantenha **organizada, viva e confiável**.

---

## 📋 Convenções aplicáveis

| Convenção | Referência |
| --------- | ---------- |
| Valores de status e estrutura de seções do documento | `conventions/file-structure/document-sections.md` |
| Critério de versionamento semântico | `conventions/versioning/semantic-version.md` |

A IA deve aplicar as convenções acima ao criar, atualizar ou transicionar documentos.

---

## 🔄 Transições de Status

> [!danger] Regra fundamental
> **Documentos nunca são excluídos.** O histórico é sempre preservado. Documentos que não são mais úteis devem ter seu status alterado para `arquivado` ou `obsoleto`.

### Transições permitidas

| De | Para | Condição |
| -- | ---- | -------- |
| `rascunho` | `ativo` | Documento validado e pronto para uso |
| `ativo` | `rascunho` | Documento precisa de reescrita significativa |
| `ativo` | `arquivado` | Documento não é mais necessário no momento |
| `arquivado` | `ativo` | Documento volta a ser relevante |
| `arquivado` | `obsoleto` | Documento foi substituído ou definitivamente invalidado |
| `rascunho` | `obsoleto` | Rascunho abandonado que nunca será finalizado |
| `obsoleto` | `rascunho` | Reativação — requer aprovação de um administrador da base de conhecimento |

> [!warning] Restrição
> De `obsoleto` **não é permitido** ir direto para `ativo` ou `arquivado` — deve passar por `rascunho` primeiro.

> [!warning] Atenção
> Toda transição de status **deve ser registrada** no Histórico de Alterações do documento com justificativa.

---

## 📄 Quando Criar um Novo Documento

Criar um **novo** documento quando:

- O assunto **não existe** na base de conhecimento
- O escopo é **diferente o suficiente** para justificar separação
- Misturar com um documento existente **prejudicaria** a clareza

> [!tip] Dica
> Antes de criar, **busque na base** se já existe algo sobre o tema. Prefira enriquecer um documento existente a criar duplicatas.

---

## 🔍 Detecção de Conteúdo Duplicado

> [!danger] Regra fundamental
> A IA **nunca deve criar um documento novo** sem antes verificar se já existe conteúdo semelhante na base de conhecimento.

### Fluxo obrigatório

**1. Buscar na base de conhecimento**

- Pesquisar por documentos com **tags**, **títulos** ou **conteúdo** semelhantes
- Verificar o `index.md` e backlinks para identificar sobreposições

**2. Se encontrar documento(s) similar(es) — Investigar**

A IA deve apresentar o(s) documento(s) encontrado(s) e conduzir um questionário para entender a demanda:

- Qual o objetivo principal do novo documento?
- O documento existente não cobre esse assunto?
- Seria o caso de adicionar uma nova seção ao documento existente?
- O que diferencia esta demanda do conteúdo que já existe?

**3. Após análise — Sugerir uma das ações**

- **Atualizar o existente** — o conteúdo novo se encaixa como seção ou complemento
- **Dividir o existente** — o documento existente ficou grande demais e a nova demanda justifica separação
- **Criar novo documento** — o escopo é genuinamente diferente
- **Criar e referenciar** — o assunto é relacionado mas independente, criar novo com backlinks cruzados

> [!warning] Atenção
> A IA **apresenta a sugestão com justificativa**, mas a decisão final é **sempre do usuário**. Se o usuário insistir em criar novo documento mesmo com sobreposição, a IA deve acatar e garantir que os backlinks entre os documentos sejam criados.

> [!danger] Desvio de Behavior
> Se o usuário optar por **não seguir a sugestão da IA**, o desvio **deve ser registrado** no documento criado, conforme definido em [[foundations/behavior-principles/behavior-principles|Princípio #2 — Desvios São Registrados]]. A IA deve perguntar o motivo para registrar a justificativa.

> [!info] Profundidade da análise
> A IA deve ir além de uma busca superficial — analisar o **conteúdo real** dos documentos encontrados, comparar seções, e apresentar uma visão clara de onde há sobreposição e onde há diferença.

---

## ✏️ Quando Atualizar um Documento Existente

Atualizar o documento quando:

- Corrigir erros de texto, formatação ou links
- Adicionar novas seções ou detalhamento
- Ajustar regras ou comportamentos descritos
- Atualizar tags, frontmatter ou backlinks

> [!info] Lembrete
> Toda atualização deve:
> - Incrementar a versão conforme a convenção em `conventions/versioning/semantic-version.md`
> - Atualizar o campo `version` no frontmatter
> - Registrar a alteração no Histórico de Alterações

---

## 📦 Quando Arquivar

Mover para `arquivado` quando:

- O documento **não é mais relevante** para o contexto atual
- Foi **substituído parcialmente** por outro documento, mas ainda tem valor histórico
- O assunto está **temporariamente fora de escopo**

> [!tip] Dica
> Documentos arquivados podem ser **reativados** a qualquer momento. Arquivar não é perder — é organizar.

---

## ❌ Quando Marcar como Obsoleto

Mover para `obsoleto` quando:

- O documento foi **completamente substituído** por outro
- O conteúdo é **factualmente incorreto** e não vale a correção
- A regra ou processo descrito **não se aplica mais** em nenhum contexto

> [!danger] Atenção
> Ao marcar como obsoleto, o documento deve incluir uma nota indicando:
> - **Por que** foi obsoletado
> - **O que substitui** (se aplicável), com wikilink para o novo documento

> [!tip] Reativação
> Um documento obsoleto **pode voltar para `rascunho`** mediante aprovação de um administrador da base de conhecimento. A partir de `rascunho`, segue o fluxo normal de validação até `ativo`.

---

## 🤖 Papel da IA

A IA deve **sugerir proativamente** mudanças de status quando identificar:

- Documentos `rascunho` que parecem completos — sugerir `ativo`
- Documentos `ativo` sem referências ou backlinks — sugerir revisão
- Documentos `ativo` com conteúdo potencialmente desatualizado — sugerir revisão ou `arquivado`
- Documentos `ativo` cujo assunto foi coberto por outro documento — sugerir `arquivado` ou `obsoleto`

> [!warning] Atenção
> A IA **sugere**, mas **não altera** o status sem confirmação do usuário.

---

## 🔗 Documentos Relacionados

- [[foundations/behavior-principles/behavior-principles]] — Princípios fundamentais que regem o behavior, incluindo registro de desvios
- [[writing/markdown-writing/markdown-writing]] — Regras de formatação, frontmatter e versionamento que todo documento deve seguir
- [[organization/taxonomy-and-tags/taxonomy-and-tags]] — Convenções de tags usadas para categorizar documentos
- [[organization/index-and-navigation/index-and-navigation]] — Regras de índice e backlinks afetados por transições de status

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição                                                                      |
| --------- | ---------------- | ------------------------------------------------------------------------------ |
| 01.00.000 | 2026-04-03 09:00 | Criação do documento                                                           |
| 01.01.000 | 2026-04-03 09:15 | Obsoleto deixa de ser terminal — permite transição para rascunho com aprovação |
| 01.02.000 | 2026-04-03 09:30 | Adição da seção de detecção de conteúdo duplicado com fluxo de questionário    |
| 01.03.000 | 2026-04-03 09:45 | Referência ao registro de desvios conforme principios-do-behavior              |
| 01.03.001 | 2026-04-03 10:00 | Padronização de campos de data para Timestamp (yyyy-MM-DD HH:mm)              |
| 01.03.002 | 2026-04-03 10:30 | Correção da descrição de obsoleto (não é mais terminal)                        |
| 01.03.003 | 2026-04-04 09:30 | Renomeação de gestao-de-documentacao para document-management (naming-convention) |
| 01.04.000 | 2026-04-10 12:00 | Refatoração: valores de status e formato de seções extraídos para conventions/; regra mantém apenas instruções comportamentais |
