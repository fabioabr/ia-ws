---
title: Dependency Manifest
description: Mapeamento completo de tudo que o Discovery Pipeline herda do workspace global — usado pelo agente sincronizador para manter o projeto atualizado
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: manifesto
area: tecnologia
tags:
  - dependencia
  - sincronizacao
  - manifesto
  - workspace
created: 2026-04-11 12:00
workspace-base: E:\Workspace
---

# Dependency Manifest

Mapeamento de todos os recursos que o Discovery Pipeline herda do workspace global. O agente sincronizador usa este arquivo para detectar atualizações e propagar mudanças.

> [!danger] Regra
> Este arquivo é a **fonte de verdade** para dependências. Se um recurso não está listado aqui, ele não é sincronizado. Ao adicionar uma nova dependência do workspace, registre aqui.

> [!info] Camada base-artifacts
> `base-artifacts/` é a cópia local dos recursos globais do workspace (`E:\Workspace`). Os caminhos no workspace (coluna "Caminho no workspace") são a **fonte original**; os caminhos locais em `base-artifacts/` são cópias sincronizadas pelo agente.

---

## 📋 Como funciona a sincronização

1. O agente lê este manifesto
2. Para cada dependência, compara `version` do arquivo local vs arquivo no workspace
3. Se o workspace tem versão mais recente → atualiza o local
4. Registra o que foi atualizado no changelog deste manifesto

---

## 🔧 Global Skills

Skills globais em `base-artifacts/skills/` (local copy of `base-artifacts/skills/`) que o pipeline usa diretamente.

| Skill | Caminho no workspace | Usado por | Tipo |
|-------|---------------------|-----------|------|
| po | `base-artifacts/skills/po/SKILL.md` | orchestrator (Fase 1, blocos #1-#4) | Referência direta |
| solution-architect | `base-artifacts/skills/solution-architect/SKILL.md` | orchestrator (Fase 1, blocos #5, #7, #8) | Referência direta |
| cyber-security-architect | `base-artifacts/skills/cyber-security-architect/SKILL.md` | orchestrator (Fase 1, bloco #6) | Referência direta |
| 10th-man | `base-artifacts/skills/10th-man/SKILL.md` | orchestrator (Fase 2, #2.2) | Referência direta |
| custom-specialist | `base-artifacts/skills/custom-specialist/SKILL.md` | orchestrator (Fase 1, sob demanda) | Referência direta |
| html-writer | `base-artifacts/skills/html-writer/SKILL.md` | consolidator (Fase 3, #3.3) | Referência indireta |
| md-writer | `base-artifacts/skills/md-writer/SKILL.md` | pipeline-md-writer (Fase 3, #3.1) | Referência indireta |
| md-validator | `base-artifacts/skills/md-validator/SKILL.md` | validação de artefatos | Opcional |

---

## 📚 Context-Templates

Domínios tecnológicos em `base-artifacts/context-templates/` (local copy of workspace `context-templates/`) copiados para a run durante o setup.

| Pack | Caminho no workspace | Arquivos |
|------|---------------------|----------|
| saas | `base-artifacts/context-templates/saas/` | `context.md`, `specialists.md`, `report-profile.md` |
| datalake-ingestion | `base-artifacts/context-templates/datalake-ingestion/` | `discovery-blueprint.md` (documento único e auto-contido) |
| process-documentation | `base-artifacts/context-templates/process-documentation/` | `context.md`, `specialists.md`, `report-profile.md` |
| web-microservices | `base-artifacts/context-templates/web-microservices/` | `context.md`, `specialists.md`, `report-profile.md` |

---

## 🎨 Assets

Recursos visuais em `base-artifacts/assets/` (local copy of workspace `assets/`) usados na geração de reports.

| Asset | Caminho no workspace | Usado por |
|-------|---------------------|-----------|
| Logo dark | `base-artifacts/assets/logos/dark.png` | html-writer (header/footer) |
| Logo light | `base-artifacts/assets/logos/light.png` | html-writer (header/footer) |
| Logo dark base64 | `base-artifacts/assets/logos/dark-base64.txt` | html-writer (embed) |
| Logo light base64 | `base-artifacts/assets/logos/light-base64.txt` | html-writer (embed) |
| Design System | `base-artifacts/assets/ui-ux/design-system.md` | html-writer (tokens, cores, tipografia) |
| Playground HTML | `base-artifacts/assets/ui-ux/playground.html` | html-writer (template de referência) |
| Report Variables | `base-artifacts/assets/variables/report-variables.md` | html-writer (empresa, footer, confidencialidade) |

---

## 📏 Conventions

Convenções em `base-artifacts/conventions/` (local copy of workspace `conventions/`) referenciadas pelas skills e regras para formatação de artefatos.

| Convenção | Caminho no workspace | Usado para |
|-----------|---------------------|------------|
| Document Schema | `base-artifacts/conventions/frontmatter/document-schema.md` | Frontmatter de todos os .md |
| Skill Schema | `base-artifacts/conventions/frontmatter/skill-schema.md` | Frontmatter das SKILL.md |
| Headings | `base-artifacts/conventions/markdown/headings.md` | Hierarquia H1-H4 |
| Callouts | `base-artifacts/conventions/markdown/callouts.md` | Alertas Obsidian |
| Emojis | `base-artifacts/conventions/markdown/emojis.md` | Emojis semânticos em H2 |
| Section Order | `base-artifacts/conventions/markdown/section-order.md` | Ordem de seções |
| Wikilinks | `base-artifacts/conventions/markdown/wikilinks.md` | Links entre documentos |
| Diagrams | `base-artifacts/conventions/markdown/diagrams.md` | Diagramas Mermaid |
| Acronyms (MD) | `base-artifacts/conventions/acronyms/markdown-treatment.md` | Tratamento de siglas |
| Acronym Bank | `base-artifacts/conventions/acronyms/acronym-bank.md` | Banco de siglas |
| File Naming | `base-artifacts/conventions/naming/file-naming.md` | Kebab-case, inglês |
| Tags | `base-artifacts/conventions/tags/taxonomy.md` | Tags pt-BR sem acentos |
| Versioning | `base-artifacts/conventions/versioning/semantic-version.md` | Formato XX.YY.ZZZ |
| Colors | `base-artifacts/conventions/colors/palette.md` | Paleta de cores |
| Sequential Palette | `base-artifacts/conventions/colors/sequential-palette.md` | Cores sequenciais |
| Chart Palette | `base-artifacts/conventions/colors/chart-palette.md` | Cores de gráficos |
| Typography | `base-artifacts/conventions/typography/scale.md` | Escala tipográfica |
| Components | `base-artifacts/conventions/components/*.md` | Card, table, alerts, etc. |
| Breakpoints | `base-artifacts/conventions/responsive/breakpoints.md` | Responsividade |

---

## 📜 Behavior Rules

Regras globais em `base-artifacts/behavior/rules/` (local copy of workspace `behavior/rules/`) que o pipeline herda.

| Regra | Caminho no workspace | O que governa |
|-------|---------------------|---------------|
| Index | `base-artifacts/behavior/rules/index.md` | Índice de todas as regras |
| Skill Structure | `base-artifacts/behavior/rules/code/skill-structure/skill-structure.md` | Formato obrigatório de SKILL.md |

> [!info] Regras de escrita
> As regras globais de escrita (markdown-writing, naming-convention, acronym-glossary, etc.) são aplicadas **indiretamente** via conventions. O pipeline não referencia as regras diretamente — referencia as conventions que as regras definem.

---

## 🔧 Support Tools

Ferramentas em `base-artifacts/support-tools/` (local copy of workspace `support-tools/`) disponíveis para o pipeline.

| Tool | Caminho no workspace | Uso |
|------|---------------------|-----|
| md-validator | `base-artifacts/support-tools/md-validator/` | Validação de .md contra convenções |
| GitNexus | `base-artifacts/support-tools/git-nexus/` | Knowledge graph do codebase |

---

## 📄 Outros

| Recurso | Caminho no workspace | Uso |
|---------|---------------------|-----|
| CLAUDE.md | `CLAUDE.md` | Entry point do workspace |
| Dependency Template | `setup/dependency.md` | Template de herança para projetos |

---

## 🔄 Protocolo de sincronização

### Para o agente sincronizador

```
1. Ler este manifesto
2. Para cada recurso listado:
   a. Ler o campo `version` do frontmatter do arquivo no workspace
   b. Comparar com a versão que o projeto usa (se tiver cópia local)
   c. Se workspace > local → marcar como "needs update"
   d. Para recursos sem cópia local (referência direta) → verificar se ainda existe
3. Gerar relatório:
   - Recursos atualizados
   - Recursos desatualizados (com diff de versão)
   - Recursos removidos no workspace (possível breaking change)
4. Se --apply: copiar/atualizar os recursos desatualizados
5. Registrar no changelog deste manifesto
```

### Quando sincronizar

- Antes de iniciar uma nova run
- Após atualização do workspace (pull do repositório)
- Manualmente via agente: `/sync-dependencies`

---

## 📜 Histórico de Sincronização

| Data | Recursos atualizados | Detalhes |
|------|---------------------|----------|
| 2026-04-11 | Criação do manifesto | Mapeamento inicial de todas as dependências |
