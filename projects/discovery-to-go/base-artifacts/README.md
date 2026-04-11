---
title: Base Artifacts
description: Cópia local do workspace global — assets, convenções, context-templates, skills globais e support-tools. Sincronizável com o workspace central.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - base-artifacts
  - workspace
  - sincronizacao
created: 2026-04-11
---

# Base Artifacts

Cópia local dos recursos do workspace global (`E:\Workspace`). Permite que o projeto opere standalone sem depender do workspace central. Sincronizável via `docs/dependency-manifest.md`.

## Estrutura

```
base-artifacts/
├── assets/                     ← logos, design system, playground, variáveis
│   ├── logos/                  ← dark.png, light.png + versões base64
│   ├── ui-ux/                  ← design-system.md, playground.html
│   └── variables/              ← report-variables.md
├── behavior/rules/             ← regras globais (skill-structure, etc.)
├── conventions/                ← 30+ convenções (frontmatter, markdown, naming, etc.)
├── context-templates/          ← 10 blueprints de discovery por domínio
├── skills/                     ← 8 skills globais (po, solution-architect, etc.)
├── support-tools/              ← ferramentas (md-validator Python)
├── templates/                  ← templates de reports e regions
│   └── report-regions/         ← 85 regions visuais + previews HTML
├── CLAUDE.md                   ← entry point do workspace global
└── dependency.md               ← template de herança
```

## Sincronização

A fonte de verdade é o workspace global. Para sincronizar:

1. Verificar `docs/dependency-manifest.md` para a lista de dependências
2. Comparar versões (frontmatter `version`) entre local e global
3. Copiar arquivos desatualizados do workspace global para cá

## Prioridade

Esta é a **camada 1** (menor prioridade). Conteúdo aqui é sobrescrito por:
- `dtg-artifacts/` (camada 2 — Pipeline)
- `custom-artifacts/` (camada 3 — Custom)
