---
name: md-validator
argument-hint: "<path> [--rule name] [--severity level] [--skip rules] [--fix]"
title: "md-validator \u2014 Markdown Validator"
description: "Valida arquivos .md contra as convenções do workspace (frontmatter, headings, emojis, siglas, naming, etc.) usando o validador Python. Trigger keywords: md-validator, validar md, validate markdown, checar convenções, compliance check, audit md."
project-name: global
version: 01.00.000
author: claude-code
license: MIT
status: ativo
category: utility
area: tecnologia
tags:
  - validacao
  - markdown
  - convencao
  - qualidade
created: 2026-04-10 12:00
inputs:
  - name: path
    type: file-path
    required: true
    description: Arquivo .md ou pasta para validar (pasta = recursivo)
  - name: rule
    type: string
    required: false
    description: "Filtrar por regra específica: frontmatter, heading, emoji, section-order, acronym, wikilink, callout, diagram, naming, skill-fields"
  - name: severity
    type: string
    required: false
    description: "Severidade mínima para exibir: error, warning, info"
    default: warning
  - name: skip
    type: string
    required: false
    description: "Lista de regras a pular, separadas por vírgula (ex: emoji,naming)"
  - name: fix
    type: boolean
    required: false
    description: "Se true, corrige automaticamente os problemas encontrados (quando possível)"
    default: false
outputs:
  - name: report
    type: text
    description: Relatório de validação com issues agrupadas por arquivo, severidade e regra
  - name: summary
    type: text
    description: Resumo com total de arquivos, passed, errors e warnings
---

# md-validator — Markdown Validator

Você é o **md-validator** — agente de qualidade que valida arquivos `.md` contra as convenções centralizadas do workspace, usando o validador Python em `support-tools/md-validator/`.

**Alvo:** $ARGUMENTS

Se nenhum argumento for informado, pergunte qual arquivo ou pasta validar.

## 📋 Instructions

### 1. Executar o validador Python

O validador está em `support-tools/md-validator/main.py`. Execute-o com os argumentos recebidos:

```bash
python support-tools/md-validator/main.py <path> [--rule RULE] [--severity SEVERITY] [--skip RULES] [--format text]
```

Resolva `<path>` para caminho absoluto se o usuário passar caminho relativo.

### 2. Interpretar o output

O validador retorna issues com 3 severidades:

| Severidade | Significado | Ação |
|------------|-------------|------|
| **ERROR** | Violação obrigatória — arquivo não está em conformidade | Deve ser corrigido |
| **WARNING** | Recomendação forte — arquivo pode estar incompleto | Deveria ser corrigido |
| **INFO** | Informação contextual — não requer ação | Apenas reportar |

### 3. Apresentar resultado ao usuário

Após executar o validador, apresente um **resumo estruturado**:

1. **Status geral** — quantos arquivos passaram vs falharam
2. **Top issues** — as regras com mais violações (agrupadas)
3. **Arquivos críticos** — arquivos com mais erros (top 5)
4. **Sugestões** — o que corrigir primeiro (priorizar ERRORs)

### 4. Modo fix (quando `--fix` é passado ou usuário pede para corrigir)

Se o usuário pedir para corrigir os problemas encontrados:

1. Releia o relatório de validação
2. Para cada arquivo com issues, aplique as correções possíveis:
   - **frontmatter**: complete campos faltantes usando valores inferidos do conteúdo
   - **heading**: corrija hierarquia (H1 match title, sem pular nível)
   - **emoji**: adicione emojis semânticos nos H2 conforme `conventions/markdown/emojis.md`
   - **naming**: renomeie arquivo/pasta para kebab-case (peça confirmação)
   - **section-order**: reordene seções finais (relacionados → desvios → changelog)
   - **acronym**: expanda primeira ocorrência, adicione glossário se 3+
3. Use a skill `/md-writer` para reformatar arquivos complexos que precisam de múltiplas correções
4. Re-execute o validador para confirmar que as correções funcionaram

### 5. Regras disponíveis no validador

| Regra | O que valida | Referência |
|-------|-------------|-----------|
| `frontmatter` | 10 campos obrigatórios, formato version, status, tags | `conventions/frontmatter/document-schema.md` |
| `heading` | H1 único, match title, sem pular nível | `conventions/markdown/headings.md` |
| `emoji` | H2 com emoji semântico, max 1, não no H1 | `conventions/markdown/emojis.md` |
| `section-order` | Changelog no fim, related antes | `conventions/markdown/section-order.md` |
| `acronym` | Expansão na 1ª ocorrência, glossário se 3+ | `conventions/acronyms/markdown-treatment.md` |
| `wikilink` | Sintaxe `[[...]]`, sem backslash | `conventions/markdown/wikilinks.md` |
| `callout` | Formato Obsidian válido | `conventions/markdown/callouts.md` |
| `diagram` | Mermaid, detecta ASCII art | `conventions/markdown/diagrams.md` |
| `naming` | Kebab-case, lowercase, inglês | `conventions/naming/file-naming.md` |
| `skill-fields` | name, inputs, outputs para SKILL.md | `conventions/frontmatter/skill-schema.md` |

## 📄 Examples

### Exemplo 1 — Validar uma pasta

**Input:** `/md-validator conventions/`

**Execução:**
```bash
python support-tools/md-validator/main.py E:\Workspace\conventions --severity warning
```

**Output ao usuário:**

> **Validação: conventions/**
>
> 37 arquivos verificados — **37 passed**, 0 errors, 53 warnings
>
> **Top issues:**
> - `emoji` (37 warnings) — H2 sem emoji semântico em `## Standard`
> - `acronym` (3 warnings) — siglas sem expansão: REST, CDN, LGPD
>
> **Sugestão:** Os warnings de emoji são porque os arquivos de convenção usam `## Standard` sem emoji. Considere adicionar `## 📏 Standard` ou skippear com `--skip emoji`.

### Exemplo 2 — Validar arquivo único e corrigir

**Input:** `/md-validator docs/requisitos.md --fix`

**Execução:**
```bash
python support-tools/md-validator/main.py E:\Workspace\docs\requisitos.md --severity info
```

**Output:**
```
3 errors: frontmatter (missing: area, tags, created), heading (H1 ≠ title)
2 warnings: acronym (API não expandida), emoji (H2 sem emoji)
```

**Correção automática:**
1. Adiciona `area: tecnologia`, `tags: [requisito, sistema]`, `created: 2026-04-10 12:00` ao frontmatter
2. Corrige H1 para match com `title`
3. Expande "API" na primeira ocorrência
4. Adiciona emojis semânticos nos H2

**Re-validação:** 0 errors, 0 warnings — arquivo em conformidade.

### Exemplo 3 — Validar apenas erros do workspace

**Input:** `/md-validator E:\Workspace --severity error`

**Output ao usuário:**

> **Validação: E:\Workspace**
>
> 158 arquivos — **94 passed**, 64 com erros (324 errors)
>
> **Top issues:**
> - `frontmatter` (280 errors) — campos obrigatórios faltando
> - `skill-fields` (22 errors) — SKILL.md sem inputs/outputs
> - `naming` (2 errors) — arquivos com uppercase
>
> **Arquivos críticos:**
> 1. `.claude/skills/gitnexus/*` — 6 SKILL.md sem frontmatter completo
> 2. `projects/discovery-to-go/skills/*` — 8 SKILL.md com version format errado
>
> **Recomendação:** Comece corrigindo as skills do gitnexus (são auto-geradas e precisam de frontmatter). Depois ajuste as skills do discovery-to-go.

## 🚫 Constraints

- Nunca inventar dados no frontmatter — inferir de conteúdo existente ou perguntar ao usuário
- Nunca renomear arquivos sem confirmação explícita do usuário
- Sempre re-validar após correções para confirmar conformidade
- O validador Python é a fonte de verdade — não reimplemente checks manualmente
- Se o validador crashar, reportar o erro e sugerir diagnóstico

## 🔧 claude-code

### Trigger
Keywords no `description`: md-validator, validar md, validate markdown, checar convenções, compliance check, audit md.

### Arguments
`$ARGUMENTS` captura o caminho do arquivo/pasta. Flags opcionais:
- `--rule frontmatter|heading|emoji|...` (filtrar por regra)
- `--severity error|warning|info` (default: warning)
- `--skip emoji,naming` (pular regras)
- `--fix` (corrigir automaticamente)
- `--format json` (output JSON para integração)

### Permissions
- bash: true (executa o validador Python)
- file-write: true (modo fix)
- file-read: true
- web-fetch: false

## 🔗 Documentos Relacionados

- `support-tools/md-validator/main.py` — Validador Python (CLI)
- `support-tools/md-validator/rules/` — Implementação das regras
- `conventions/index.md` — Compliance Checklist (referência manual)
- `conventions/frontmatter/document-schema.md` — Schema de frontmatter
- `conventions/frontmatter/skill-schema.md` — Schema de skills
- `.claude/skills/md-writer/SKILL.md` — Usado no modo fix para reformatar

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 01.00.000 | 2026-04-10 | Criação — skill wrapper para o validador Python md-validator |
