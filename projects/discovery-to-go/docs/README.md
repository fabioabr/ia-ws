---
title: Documentação
description: Guias operacionais, documentos de referência e diagramas do Discovery Pipeline
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - documentacao
  - guia
  - how-to
created: 2026-04-11
---

# Documentação

```
docs/
├── guides/                              ← guias operacionais (how-to)
│   ├── discovery-pipeline.md            ← guia completo do pipeline
│   ├── quick-start.md                   ← como iniciar uma run
│   └── logging-process.md               ← como funciona o logging
├── reference/                           ← documentos de referência
│   ├── dependency-manifest.md           ← mapeamento de dependências
│   └── product-discovery-deliverables.md ← teoria de entregáveis
└── diagrams/                            ← diagramas visuais
    ├── pipeline.drawio                  ← editável no draw.io
    └── pipeline.png                     ← versão exportada
```

## Guides

| Guia | Descrição |
|------|-----------|
| `guides/discovery-pipeline.md` | Guia completo do pipeline — fases, blocos, agentes, regions, outputs |
| `guides/quick-start.md` | Como iniciar e conduzir uma run (8 passos) |
| `guides/logging-process.md` | Tipos de log, formato de entradas, regras de imutabilidade |

## Reference

| Documento | Descrição |
|-----------|-----------|
| `reference/dependency-manifest.md` | Mapeamento de todas as dependências do workspace global |
| `reference/product-discovery-deliverables.md` | Referência teórica — entregáveis de um Product Discovery (Cagan, Torres, JTBD, C4, ADRs) |

## Diagrams

| Arquivo | Descrição |
|---------|-----------|
| `diagrams/pipeline.drawio` | Diagrama completo do pipeline (editável no draw.io) |
| `diagrams/pipeline.png` | Versão PNG exportada |
