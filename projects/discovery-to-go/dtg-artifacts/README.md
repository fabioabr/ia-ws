---
title: DTG Artifacts
description: Artefatos específicos do Discovery Pipeline — regras, skills, templates, samples de execução
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - dtg-artifacts
  - pipeline
  - discovery
created: 2026-04-11
---

# DTG Artifacts

Artefatos específicos do Discovery Pipeline v0.5. É o "motor" do discovery — contém as regras, skills, templates e samples que definem o comportamento do pipeline.

## Estrutura

```
dtg-artifacts/
├── rules/                          ← 7 regras do pipeline
│   ├── discovery/                  ← 3 fases, 8 blocos temáticos
│   ├── iteration-loop/             ← iterações, limites, convergência
│   ├── analyst-discovery-log/      ← formato da entrevista
│   ├── audit-log/                  ← log de auditoria
│   ├── requirement-priority/       ← classificação de requisitos
│   ├── token-tracking/             ← rastreamento de tokens
│   └── custom-artifacts-priority/  ← prioridade Custom > Pipeline > Base
├── skills/                         ← 6 skills locais do pipeline
│   ├── orchestrator/               ← coordenador central (transversal)
│   ├── customer/                   ← simulador do cliente (Fase 1)
│   ├── auditor/                    ← validação convergente (Fase 2)
│   ├── consolidator/               ← consolidador de conteúdo (Fase 3)
│   ├── report-planner/             ← planejador visual de relatórios (Fase 3)
│   └── pipeline-md-writer/         ← formatador de markdown (Fase 3)
├── templates/                      ← templates de artefatos
│   ├── briefing-template.md
│   ├── audit-report-template.md
│   ├── challenge-report-template.md
│   ├── change-request-template.md
│   ├── iteration-setup-template.md
│   └── customization/              ← defaults customizáveis por run
│       ├── final-report-template.md
│       ├── human-review-template.md
│       ├── html-layout.md
│       ├── iteration-policy.md
│       └── scoring-thresholds.md
├── assets/                         ← assets do pipeline (diagramas)
└── arctifact-samples/              ← sample de uma run completa (FinTrack Pro)
    └── run-sample/
```

## Skills do Pipeline

| Skill | Fase | Papel |
|-------|------|-------|
| orchestrator | Todas | Coordena, cria scaffold, gerencia estado |
| customer | 1 | Simula o cliente na entrevista |
| auditor | 2 | Validação convergente (5 dimensões) |
| consolidator | 3 | Consolida conteúdo no delivery-report.md |
| report-planner | 3 | Planeja a visualização do HTML por regions |
| pipeline-md-writer | 3 | Formata drafts em markdown polido |

## Regras

| Regra | O que governa |
|-------|---------------|
| `discovery/` | 3 fases, 8 blocos, critérios de conclusão |
| `iteration-loop/` | Iterações, limites, convergência |
| `analyst-discovery-log/` | Formato da entrevista (tabela com emojis) |
| `audit-log/` | Log de auditoria |
| `requirement-priority/` | Classificação de requisitos (MoSCoW/RICE) |
| `token-tracking/` | Rastreamento de consumo de tokens |
| `custom-artifacts-priority/` | Cadeia de prioridade Custom > Pipeline > Base |

## Prioridade

Esta é a **camada 2** (prioridade média). Conteúdo aqui sobrescreve `base-artifacts/` mas é sobrescrito por `custom-artifacts/`.
