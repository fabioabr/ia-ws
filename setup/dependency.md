---
title: Project Dependency Template
description: Template para projetos que herdam regras, convenções e assets do workspace global ia-ws
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - dependencia
  - setup
created: 2026-04-10 12:00
---

# Project Dependency Template

Template para projetos que herdam regras, convenções e assets do workspace global `ia-ws`. Copie este arquivo para a raiz do seu projeto como `dependency.md` e preencha os campos marcados com `{{...}}`.

---

## Como usar

1. Copie a seção **Template** abaixo para `{seu-projeto}/dependency.md`
2. Substitua `{{project-name}}` pelo nome do projeto
3. Substitua `{{WS_BASE}}` pelo caminho absoluto do workspace `ia-ws` na máquina
4. Preencha a seção **Overrides** se o projeto customiza algo
5. Preencha a seção **Regras locais** se o projeto tem regras próprias
6. A IA deve ler este arquivo no início da sessão para saber de onde herda

---

## Template

````markdown
# Dependency — {{project-name}}

Este projeto herda regras, convenções e assets do workspace global `ia-ws`.

---

## Workspace Base

> [!danger] Localização física obrigatória
> Todos os caminhos deste documento são **relativos** à pasta base abaixo.
> A IA DEVE resolver qualquer referência a partir deste caminho.
> USUÁRIO DEVE PREENCHER ESTA PASTA NO SETUP

```
{{WS_BASE}}
```

Exemplo: se `{{WS_BASE}}` = `E:/Workspace`, então `behavior/rules/index.md` resolve para `E:/Workspace/behavior/rules/index.md`.

---

## O que é herdado

### Regras (obrigatórias)

A IA DEVE ler `behavior/rules/index.md` no início de cada sessão. As regras têm prioridade absoluta. Desvios devem ser registrados conforme o processo definido nas regras.

| Categoria | Caminho relativo | O que governa |
|-----------|-----------------|--------------|
| Foundations | `behavior/rules/foundations/` | Princípios de comportamento, fronteiras de projeto |
| Writing | `behavior/rules/writing/` | Markdown, naming, siglas, hallucination guard |
| Organization | `behavior/rules/organization/` | Tags, índices, ciclo de vida de documentos |
| Code | `behavior/rules/code/` | Estrutura de skills |

### Convenções (obrigatórias)

A IA DEVE consultar as convenções antes de gerar qualquer artefato.

| Categoria | Caminho relativo | O que define |
|-----------|-----------------|-------------|
| Naming | `conventions/naming/` | Kebab-case, inglês |
| Versioning | `conventions/versioning/` | Formato XX.YY.ZZZ |
| Frontmatter | `conventions/frontmatter/` | Schema de documentos e skills |
| Tags | `conventions/tags/` | Taxonomia pt-BR sem acentos |
| Markdown | `conventions/markdown/` | Headings, callouts, diagramas, wikilinks, emojis, seções |
| Acronyms | `conventions/acronyms/` | Tratamento MD/HTML, banco de siglas |
| Colors | `conventions/colors/` | Paleta, sequencial, charts, contraste |
| Typography | `conventions/typography/` | Escala tipográfica |
| Spacing | `conventions/spacing/` | Tokens, border-radius, shadows |
| Components | `conventions/components/` | Card, table, alerts, badges, tabs, stat-card, header-footer |
| Charts | `conventions/charts/` | Chart.js config |
| Variables | `conventions/variables/` | Variáveis de report (empresa, footer) |
| File Structure | `conventions/file-structure/` | Seções de documento, boundaries, index |
| Icons | `conventions/icons/` | Remix Icon |
| Responsive | `conventions/responsive/` | Breakpoints |
| Skills | `conventions/skills/` | Estrutura do corpo de SKILL.md |

### Assets (com override local)

| Prioridade | Caminho |
|------------|---------|
| 1. Projeto (local) | `{pasta-do-projeto}/assets/` |
| 2. Global (fallback) | `assets/` (relativo ao WS_BASE) |

Se ambos existirem, assets do projeto **sobrescrevem** os globais.

| Asset | Caminho relativo em `assets/` |
|-------|-------------------------------|
| Design System | `ui-ux/design-system.md` |
| Playground | `ui-ux/playground.html` |
| Variáveis | `variables/reports.md` |
| Logo dark | `logos/dark.png` |
| Logo light | `logos/light.png` |

### Skills (com extensão local)

| Prioridade | Caminho |
|------------|---------|
| 1. Projeto (local) | `{pasta-do-projeto}/skills/` |
| 2. Global (fallback) | `.claude/skills/` (relativo ao WS_BASE) |

Skills do projeto estendem ou substituem as globais.

### Knowledge Packs (com extensão local)

| Prioridade | Caminho |
|------------|---------|
| 1. Projeto (local) | `{pasta-do-projeto}/knowledge/` |
| 2. Global (fallback) | `knowledge/` (relativo ao WS_BASE) |

Domínios tecnológicos com `context.md` (concerns + perguntas) e `specialists.md` (catálogo de especialistas). Projetos podem criar packs locais ou customizar cópias dos globais.

| Domínio | Caminho relativo em `knowledge/` |
|---------|----------------------------------|
| SaaS | `saas/context.md` + `saas/specialists.md` |
| Datalake Ingestion | `datalake-ingestion/context.md` + `datalake-ingestion/specialists.md` |
| Process Documentation | `process-documentation/context.md` + `process-documentation/specialists.md` |
| Web Microservices | `web-microservices/context.md` + `web-microservices/specialists.md` |

### Referências rápidas

| Recurso | Caminho relativo |
|---------|-----------------|
| Índice de regras | `behavior/rules/index.md` |
| Banco de siglas | `conventions/acronyms/acronym-bank.md` |
| Design System | `assets/ui-ux/design-system.md` |
| Playground HTML | `assets/ui-ux/playground.html` |
| Paleta sequencial | `conventions/colors/sequential-palette.md` |

---

## Overrides do projeto

Listar aqui o que este projeto customiza em relação ao global:

| Item | Override | Descrição |
|------|----------|-----------|
| — | — | Nenhum override definido |

## Regras locais do projeto

Listar aqui regras adicionais que só se aplicam a este projeto:

| Regra | Caminho | Descrição |
|-------|---------|-----------|
| — | — | Nenhuma regra local definida |

---

## Ferramentas externas (opcional)

Ferramentas recomendadas para uso com agentes de IA. Instruções completas ficam em `support-tools/` (relativo ao WS_BASE).

| Ferramenta | O que faz | Instruções |
|------------|-----------|------------|
| GitNexus | Knowledge graph do codebase — dá consciência arquitetural a agentes via Model Context Protocol (MCP) | `support-tools/git-nexus/instructions.md` |

### Ferramentas disponíveis para o agente (via MCP)

| Ferramenta | Quando usar |
|------------|-------------|
| `query` | Buscar código/conceito por texto |
| `context` | Visão 360° de um símbolo (callers, callees, processos) |
| `impact` | Raio de impacto antes de editar |
| `detect_changes` | Verificar escopo antes de commitar |
| `rename` | Rename coordenado multi-arquivo |
````

