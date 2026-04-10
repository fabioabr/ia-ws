---
title: Conventions Index
description: Referencia rapida para todas as convencoes do workspace.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - indice
  - convencao
  - organizacao
created: 2026-04-10 12:00
---

# Conventions Index

Quick reference to all conventions in this workspace.

## Categories

### acronyms
- `acronym-bank.md` — Centralized bank of known acronyms with meanings and tooltips
- `html-treatment.md` — How to handle acronyms in HTML reports
- `markdown-treatment.md` — How to handle acronyms in Markdown documents

### charts
- `chartjs-config.md` — Standard configuration for Chart.js charts

### colors
- `chart-palette.md` — Color sequence for data visualizations and charts
- `contrast.md` — Text color pairing rules for accessible contrast
- `palette.md` — Core color tokens for all UI components
- `sequential-palette.md` — Sequential color palette for ordered data

### components
- `alerts.md` — Standard styling for alert messages
- `badge.md` — Standard styling for inline badges
- `card.md` — Standard styling for card components
- `header-footer.md` — Standard styling for header and footer
- `stat-card.md` — Standard styling for stat card components
- `table.md` — Standard styling for tables
- `tabs.md` — Standard styling for tab components

### file-structure
- `boundary-structure.md` — Standard file structure for project boundaries documentation
- `document-sections.md` — Standard sections and lifecycle for documents
- `index-structure.md` — Standard format for index.md files

### frontmatter
- `document-schema.md` — Mandatory frontmatter fields for all documents
- `skill-schema.md` — Frontmatter schema for skill definition files

### icons
- `remix-icon.md` — Icon library standard for all UI components

### markdown
- `callouts.md` — Obsidian callout types and syntax
- `diagrams.md` — Standard for diagrams in Markdown documents
- `emojis.md` — Semantic emojis for headings and highlights
- `headings.md` — Heading hierarchy and formatting rules
- `section-order.md` — Standard section ordering in documents
- `wikilinks.md` — Wikilink syntax and usage rules

### naming
- `file-naming.md` — Standard naming convention for files, folders, skills, and agents

### responsive
- `breakpoints.md` — Breakpoint definitions and layout behavior

### skills
- `body-structure.md` — Standard section order for skill definition files

### spacing
- `border-radius.md` — Radius tokens for rounded corners
- `shadows.md` — Elevation shadow tokens per theme
- `tokens.md` — Spacing scale based on a 4px base unit

### tags
- `taxonomy.md` — Standard for creating and applying tags to documents

### typography
- `scale.md` — Type scale tokens for all text elements

### versioning
- `semantic-version.md` — Versioning format for documents and artifacts

---

## Compliance Checklist

Passos obrigatórios para tornar qualquer arquivo `.md` em conformidade com as convenções deste workspace. Executar na ordem.

### 1. Frontmatter

- [ ] Arquivo começa com bloco `---` contendo frontmatter YAML
- [ ] Campos obrigatórios presentes: `title`, `description`, `project-name`, `version`, `status`, `author`, `category`, `area`, `tags`, `created`
- [ ] `version` no formato `XX.YY.ZZZ` (ver `versioning/semantic-version.md`)
- [ ] `status` é um dos valores válidos: `rascunho`, `ativo`, `arquivado`, `obsoleto` (ver `file-structure/document-sections.md`)
- [ ] `created` no formato `YYYY-MM-DD HH:mm`
- [ ] `tags` entre 2 e 5, pt-BR sem acentos, kebab-case, singular (ver `tags/taxonomy.md`)
- [ ] Referência: `frontmatter/document-schema.md`

### 2. Heading (título)

- [ ] Exatamente 1 H1 (`#`) por arquivo
- [ ] H1 = mesmo texto do campo `title` do frontmatter
- [ ] H2 para seções principais, H3 para sub-seções, H4 raramente
- [ ] Nenhum nível pulado (H1 → H3 sem H2 = erro)
- [ ] Referência: `markdown/headings.md`

### 3. Emojis semânticos

- [ ] Headings H2 usam emojis com função semântica (não decorativos)
- [ ] Máximo 1 emoji por heading
- [ ] Emojis seguem o mapeamento padrão (🎯 = objetivo, ⚠️ = atenção, 🔗 = relacionados, 📜 = changelog, etc.)
- [ ] Não usar emojis no H1
- [ ] Referência: `markdown/emojis.md`

### 4. Ordem de seções

- [ ] Sequência: Frontmatter → Conteúdo → 🔗 Documentos Relacionados → ⚠️ Desvios de Behavior (se houver) → 📜 Histórico de Alterações
- [ ] Changelog é **sempre** a última seção
- [ ] Referência: `markdown/section-order.md`

### 5. Siglas

- [ ] Primeira ocorrência de cada sigla escrita por extenso + (SIGLA)
- [ ] Ocorrências seguintes usam apenas a sigla
- [ ] Se 3+ siglas no documento, seção de glossário antes do changelog
- [ ] Siglas isentas (não precisam expandir): HTTP, HTTPS, URL, HTML, CSS, JS, PDF, PNG, JPG, CSV, JSON, XML, BR, US, EU
- [ ] Consultar banco de siglas para significados corretos: `acronyms/acronym-bank.md`
- [ ] Referência: `acronyms/markdown-treatment.md`

### 6. Wikilinks

- [ ] Referências a documentos usam `[[caminho/do/documento]]`
- [ ] Referências a skills usam inline code: `/skill-name`
- [ ] Referências a caminhos de arquivo usam inline code: `` `path/to/file.md` ``
- [ ] Paths absolutos a partir da raiz do vault
- [ ] Referência: `markdown/wikilinks.md`

### 7. Callouts

- [ ] Destaques usam callouts Obsidian: `> [!info]`, `> [!warning]`, `> [!danger]`, `> [!tip]`
- [ ] Tipo correto para o contexto (danger = proibição, warning = atenção, info = contexto, tip = sugestão)
- [ ] Referência: `markdown/callouts.md`

### 8. Diagramas

- [ ] Diagramas em Mermaid (não ASCII)
- [ ] Tipo correto: flowchart para processos, sequenceDiagram para interações, stateDiagram para ciclo de vida, gantt para cronogramas
- [ ] Labels curtos (max 3 palavras)
- [ ] Referência: `markdown/diagrams.md`

### 9. Naming

- [ ] Nome do arquivo em inglês, kebab-case, lowercase
- [ ] Nome da pasta em inglês, kebab-case, lowercase
- [ ] Referência: `naming/file-naming.md`

### 10. Texto em português

- [ ] Acentos corretos (á, é, í, ó, ú, ã, õ, ç, ê, â)
- [ ] Exceção: tags no frontmatter são sem acento (por convenção)

### 11. Campos extras para SKILL.md (apenas se o arquivo for uma skill)

- [ ] Campo `name` presente (kebab-case, inglês, = nome da pasta)
- [ ] Campo `inputs` presente (lista de parâmetros com name, type, required, description)
- [ ] Campo `outputs` presente (lista de saídas com name, type, description)
- [ ] Corpo segue estrutura: Instructions → Examples (min 2) → Constraints → seções de plataforma
- [ ] Seção `## 🔧 claude-code` com Trigger, Arguments, Permissions
- [ ] Referência: `frontmatter/skill-schema.md` + `skills/body-structure.md`
