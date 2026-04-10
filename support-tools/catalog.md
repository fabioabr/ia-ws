---
title: Support Tools Catalog
description: Catálogo de ferramentas de suporte para workflows com IA, com resumo, uso e dependências
project-name: global
version: 01.01.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - ferramenta
  - catalogo
  - ia
created: 2026-04-10 12:00
---

# Support Tools Catalog

Catálogo de ferramentas de suporte disponíveis no workspace para workflows com IA.

## 📋 Resumo

| Tool | Type | Language | Skill? | Description |
|------|------|----------|--------|-------------|
| GitNexus | External (MCP) | Node.js | — | Knowledge graph para consciência arquitetural de codebase |
| md-validator | Internal | Python | `/md-validator` | Validador de .md contra convenções do workspace |

---

## 🔧 GitNexus

**Tipo:** Ferramenta externa instalada via npm, expõe ferramentas ao agente via Model Context Protocol.

**O que faz:** Analisa repositórios com Tree-sitter, constrói knowledge graph de dependências, detecta clusters funcionais e traça fluxos de execução. Dá ao agente consciência arquitetural antes de editar código.

**Dependências:** Node.js, npm

**Instalação:**
```bash
npm install -g gitnexus
```

**Comandos principais:**
| Comando | O que faz |
|---------|-----------|
| `npx gitnexus analyze` | Indexar repositório atual |
| `npx gitnexus analyze --force` | Forçar re-indexação completa |
| `npx gitnexus mcp` | Iniciar servidor MCP |
| `npx gitnexus wiki` | Gerar documentação do repositório |

**Ferramentas expostas ao agente (via MCP):**
| Ferramenta | Quando usar |
|------------|-------------|
| `query` | Buscar código/conceito por texto |
| `context` | Visão 360° de um símbolo (callers, callees, processos) |
| `impact` | Raio de impacto antes de editar |
| `detect_changes` | Verificar escopo antes de commitar |
| `rename` | Rename coordenado multi-arquivo |
| `cypher` | Queries raw no grafo |

**Documentação completa:** [git-nexus/instructions.md](git-nexus/instructions.md)

---

## 🔧 md-validator

**Tipo:** Ferramenta interna (Python), executada via CLI ou skill `/md-validator`.

**O que faz:** Valida arquivos `.md` contra as 10 regras do Compliance Checklist definido em `conventions/index.md`. Detecta frontmatter incompleto, headings quebrados, siglas não tratadas, naming incorreto e mais.

**Dependências:** Python 3.10+, pyyaml

**Instalação:**
```bash
pip install pyyaml
```

**Uso direto (CLI):**
```bash
# Arquivo único
python support-tools/md-validator/main.py arquivo.md

# Pasta recursiva
python support-tools/md-validator/main.py conventions/

# Só erros
python support-tools/md-validator/main.py E:\Workspace --severity error

# Regra específica
python support-tools/md-validator/main.py E:\Workspace --rule frontmatter

# Pular regras
python support-tools/md-validator/main.py E:\Workspace --skip emoji,naming

# Output JSON
python support-tools/md-validator/main.py E:\Workspace --format json
```

**Uso via skill:**
```
/md-validator conventions/
/md-validator SKILL.md --fix
```

**Regras implementadas:**
| Regra | O que valida | Convenção |
|-------|-------------|-----------|
| `frontmatter` | 10 campos obrigatórios, version, status, tags | `conventions/frontmatter/document-schema.md` |
| `heading` | H1 único, match title, sem pular nível | `conventions/markdown/headings.md` |
| `emoji` | H2 com emoji semântico, max 1, não no H1 | `conventions/markdown/emojis.md` |
| `section-order` | Changelog no fim, related antes | `conventions/markdown/section-order.md` |
| `acronym` | Expansão na 1ª ocorrência, glossário se 3+ | `conventions/acronyms/markdown-treatment.md` |
| `wikilink` | Sintaxe `[[...]]`, sem backslash | `conventions/markdown/wikilinks.md` |
| `callout` | Formato Obsidian válido | `conventions/markdown/callouts.md` |
| `diagram` | Mermaid, detecta ASCII art | `conventions/markdown/diagrams.md` |
| `naming` | Kebab-case, lowercase, inglês | `conventions/naming/file-naming.md` |
| `skill-fields` | name, inputs, outputs para SKILL.md | `conventions/frontmatter/skill-schema.md` |

**Estrutura:**
```
md-validator/
├── main.py              # CLI entry point
├── models.py            # Issue, Severity, ValidationResult
├── utils.py             # parse_frontmatter, get_lines
├── requirements.txt     # pyyaml
└── rules/
    ├── __init__.py      # Registry de validadores
    ├── frontmatter.py
    ├── headings.py
    ├── emojis.py
    ├── section_order.py
    ├── acronyms.py
    ├── wikilinks.py
    ├── callouts.py
    ├── diagrams.py
    ├── naming.py
    └── skill_fields.py
```

**Documentação:** [md-validator/](md-validator/)

---

## 🔗 Documentos Relacionados

- [[conventions/index]] — Compliance Checklist (referência para o md-validator)
- [[setup/dependency]] — Template de projeto com seção de ferramentas externas

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 01.00.000 | 2026-04-10 | Criação com GitNexus e md-validator |
| 01.01.000 | 2026-04-10 | Renomeado de index.md para catalog.md; enriquecido com detalhes de uso, dependências e estrutura |
