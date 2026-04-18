---
title: Base
description: Fundação do discovery-to-go — assets, comportamento (rules + skills), padrões (conventions + blueprints), starter-kit e ferramentas.
project-name: discovery-to-go
version: 05.00.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - base
  - fundacao
created: 2026-04-11
updated: 2026-04-15
---

# Base

Fundação reutilizável para todos os projetos do discovery-to-go.

## Estrutura

```
base/
├── assets/                          ← apoio ao processo (logos, variáveis)
│   ├── logos/
│   └── variables/
├── behavior/                        ← o que os agentes FAZEM
│   ├── rules/                       ← 7 regras de comportamento do pipeline
│   └── skills/                      ← 23 skills (globais + pipeline, unificadas)
├── standards/                       ← como as coisas DEVEM SER
│   ├── conventions/                 ← convenções globais
│   │   ├── organization/            ← tags, versioning
│   │   ├── report-regions/          ← catálogo de regions (schemas + samples)
│   │   ├── visual/                  ← design tokens, componentes, charts, playground
│   │   └── writing/                 ← markdown, naming, frontmatter, acronyms
│   └── blueprints/                  ← guias de entrevista por tipo de projeto (22 tipos)
├── starter-kit/                     ← scaffold para novos projetos
│   ├── client-template/             ← template de cliente + projeto
│   └── report-setups/               ← catálogo legacy de regions por HTML (ver `deliverables_scope`)
└── support-tools/                   ← ferramentas independentes do modelo
    └── md-validator/
```

## Prioridade

Esta é a camada base (menor prioridade). Conteúdo aqui é sobrescrito por customizações do cliente em `projects/{client}/`.
