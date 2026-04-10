---
title: Markdown Writing
description: Regras de formatação e estrutura para todos os arquivos .md do workspace
project-name: global
version: 01.06.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - markdown
  - obsidian
created: 2026-04-02 09:00
---

# 📝 Escrita Markdown

Padrão obrigatório para criação e manutenção de todos os arquivos `.md` neste workspace.

## 🌐 Idioma

- Conteúdo e documentação escritos em **português (pt-BR)**
- Termos técnicos e nomes de arquivos em **inglês** quando apropriado

## 📋 Convenções Aplicáveis

Ao criar ou editar qualquer arquivo `.md`, aplique **todas** as convenções listadas abaixo:

| Convenção | Referência | Quando aplicar |
| --------- | ---------- | -------------- |
| Frontmatter YAML | `conventions/frontmatter/document-schema.md` | Todo arquivo `.md` deve iniciar com frontmatter válido. O campo `version` deve sempre refletir a última versão no Histórico de Alterações. |
| Headings | `conventions/markdown/headings.md` | Respeitar hierarquia de headings em todo documento |
| Callouts | `conventions/markdown/callouts.md` | Usar para destacar informações importantes (avisos, dicas, perigos) |
| Diagramas Mermaid | `conventions/markdown/diagrams.md` | Todo diagrama em `.md` deve usar Mermaid. Diagramas ASCII são proibidos. |
| Ordem das seções | `conventions/markdown/section-order.md` | Todo documento deve seguir a ordem padronizada de seções |
| Wikilinks e referências | `conventions/markdown/wikilinks.md` | Vincular documentos entre si; skills usam inline code |
| Emojis semânticos | `conventions/markdown/emojis.md` | Usar em headings H2 para enriquecer navegação visual |

> [!info] Exceção: Skills
> Arquivos de skill (`.claude/skills/*.md`) são instruções para agentes de IA, não documentos do behavior. Eles NÃO seguem o formato de frontmatter — são prompts, não documentos.

---

## 🎨 Identidade Visual

> [!danger] Regra fundamental
> **Quanto mais rico o visual do `.md`, melhor.** Documentos pobres visualmente não são aceitáveis.

Todos os arquivos `.md` devem ser **visualmente ricos e atraentes**:

- 🏷️ Usar **emojis** nos títulos e seções para facilitar a leitura e navegação
- 📊 Utilizar **tabelas** para organizar dados estruturados
- 💬 Usar **callouts** para destacar informações importantes
- 📋 Usar **listas** (ordenadas e não-ordenadas) para itens sequenciais ou agrupados
- 💻 Usar **blocos de código** com syntax highlighting para exemplos técnicos
- ✅❌ Usar **indicadores visuais** para correto/incorreto, sim/não
- ➡️ Usar **separadores** (`---`) para dividir seções longas quando necessário
- 🔤 Usar **negrito**, *itálico* e `inline code` para dar ênfase e clareza
- Priorizar **clareza visual** — o documento deve ser agradável de ler no Obsidian

---

## 📊 Diagramas — Contexto de uso

> [!danger] Mermaid é exclusivo para .md
> - **Arquivos `.md`** → diagramas Mermaid
> - **Arquivos `.html`** (gerados pelo `/report-maker`) → componentes visuais do Design System (CSS bars, Chart.js, stat cards, tabelas estilizadas)
> - **Nunca misturar:** não usar Mermaid no HTML, não usar Chart.js no .md

---

## 🗂️ Estrutura de Pastas por Regra

Cada regra deve seguir a estrutura:

```
categoria/
└── nome-da-regra/
    ├── nome-da-regra.md
    └── assets/          ← somente se necessário
```

- O arquivo `.md` tem o mesmo nome da pasta
- A pasta `assets/` armazena material de apoio (imagens, exemplos, templates)
- ⚠️ A pasta `assets/` **só deve ser criada quando houver assets necessários** — não criar pastas vazias

---

## ⚙️ Compatibilidade Obsidian

Todos os arquivos devem respeitar as convenções do Obsidian:

- Títulos com `#` (sem linhas em branco entre `#` e o texto)
- Callouts com sintaxe `> [!tipo]` quando necessário
- Sem HTML inline — usar sintaxe Markdown pura
- Uma única heading `h1` (`#`) por arquivo

---

## 🕐 Regras do Histórico de Alterações

Todo arquivo `.md` deve conter uma seção de histórico como **última seção** do documento:

> [!info] Critério de versionamento — formato `XX.YY.ZZZ`
> - **XX** — Reescrita de mais de 50% do documento
> - **YY** — Criação ou correção grande de comportamento (adição/remoção de seções, mudança de significado)
> - **ZZZ** — Mudanças e ajustes mínimos (correção de texto, ajustes básicos sem adição/remoção de seções)

---

## 🔗 Documentos Relacionados

- [[core/behavior-principles/behavior-principles]] — Princípios fundamentais que regem o formato e comportamento deste documento
- [[core/taxonomy-and-tags/taxonomy-and-tags]] — Convenções de tags usadas no frontmatter
- [[core/index-and-navigation/index-and-navigation]] — Regras de índice e backlinks que todo documento deve seguir
- [[core/document-management/document-management]] — Ciclo de vida e transições de status definidos no frontmatter

## 📜 Histórico de Alterações

| Versão     | Timestamp        | Descrição                                              |
| ---------- | ---------------- | ------------------------------------------------------ |
| 01.00.000  | 2026-04-02 09:00 | Criação do documento                                   |
| 01.01.000  | 2026-04-02 09:30 | Adição de callouts padrão e seção de histórico         |
| 01.01.001  | 2026-04-02 10:00 | Reforço da identidade visual como regra fundamental    |
| 01.02.000  | 2026-04-02 10:30 | Novo critério de versionamento no formato `XX.YY.ZZZ`  |
| 01.02.001  | 2026-04-02 11:00 | Adição de seção de documentos relacionados (backlinks)  |
| 01.03.000  | 2026-04-02 11:30 | Enriquecimento do frontmatter com novos campos obrigatórios |
| 01.03.001  | 2026-04-03 10:00 | Padronização de campos de data para Timestamp (yyyy-MM-DD HH:mm) |
| 01.04.000  | 2026-04-03 10:30 | Adição de ordem obrigatória das seções e correção da posição de Documentos Relacionados |
| 01.04.001  | 2026-04-03 10:45 | Renomeação da seção descritiva do histórico para evitar heading duplicado; correção do status obsoleto |
| 01.04.002  | 2026-04-04 09:30 | Renomeação de escrita-markdown para markdown-writing (naming-convention) |
| 01.05.000  | 2026-04-05 10:00 | Adição de exceção explícita para skills (sem frontmatter), correção 10 campos no frontmatter |
| 01.05.001  | 2026-04-05 | Correção de exemplos Mermaid: remoção de `\n` nos labels dos nós, alinhando com prática do pipeline doc (labels curtos, max 3 palavras) |
| 01.06.000  | 2026-04-10 | Refatoração: conteúdo de convenções extraído para `conventions/`; regra agora referencia convenções via tabela |
