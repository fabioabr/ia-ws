---
title: Discovery To Go
description: Pipeline de discovery automatizado por agentes de IA para levantamento de requisitos e arquitetura de projetos
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: indice
area: tecnologia
tags:
  - pipeline
  - discovery
  - indice
created: 2026-04-10 12:00
updated: 2026-04-11 12:00
---

# Discovery To Go

Pipeline de discovery automatizado por agentes de IA. Conduz levantamento de requisitos, validação arquitetural e entrega de relatórios consolidados em 3 fases iterativas.

## 📋 Estrutura do Projeto

```
discovery-to-go/
├── index.md                          ← entry point (este arquivo)
├── docs/                             ← documentação + manifesto + diagramas
│   ├── discovery-pipeline.md
│   ├── quick-start.md
│   ├── logging-process.md
│   ├── dependency-manifest.md
│   └── diagrams/
├── base-artifacts/                   ← cópia do workspace global (sincronizável)
│   ├── assets/
│   ├── behavior/rules/
│   ├── conventions/
│   ├── knowledge/
│   ├── skills/
│   └── support-tools/
├── dtg-artifacts/                    ← artefatos do pipeline DTG
│   ├── rules/                        ← regras do pipeline
│   ├── skills/                       ← skills locais (orchestrator, customer, auditor, consolidator, pipeline-md-writer)
│   ├── templates/                    ← templates de artefatos + customization defaults
│   ├── assets/                       ← assets do pipeline (diagrams)
│   └── arctifact-samples/            ← samples de uma run completa
└── custom-rules/                     ← customização do tenant/cliente
    ├── README.md
    └── min-rag/
```

### Estrutura em 3 camadas

| Camada | Pasta | Propósito |
|--------|-------|-----------|
| Base | `base-artifacts/` | Cópia local do workspace global — assets, regras base, convenções, knowledge packs, skills globais e support-tools. Sincronizável com o workspace central. |
| Pipeline | `dtg-artifacts/` | Artefatos específicos do pipeline DTG — regras, skills, templates, assets e samples de execução. |
| Custom | `custom-rules/` | Customizações por tenant/cliente — regras e políticas que sobrescrevem as camadas anteriores. |

## 🔧 Pipeline v0.5 — Fases

| Fase | Nome | Agentes | Output |
|------|------|---------|--------|
| 1 | Discovery | customer, po, solution-architect, cyber-security-architect, custom-specialist | 5 drafts + interview log |
| 2 | Challenge | auditor, 10th-man | audit-report + challenge-report |
| 3 | Delivery | pipeline-md-writer, consolidator | final-report.md + .html |

Entre cada fase: **Human Review** loop com logs de aprovação/rejeição.

## 📦 Skills (Agentes)

| Skill | Papel |
|-------|-------|
| orchestrator | Orquestra o pipeline, cria scaffold, gerencia estado |
| customer | Simula o cliente, responde perguntas dos especialistas |
| po | Product Owner — levanta visão, personas, valor |
| solution-architect | Arquitetura, tecnologia, TCO |
| cyber-security-architect | Privacidade, segurança, compliance |
| custom-specialist | Especialista dinâmico de domínio (sob demanda) |
| auditor | Valida qualidade dos drafts (5 dimensões) |
| 10th-man | Desafia premissas, busca pontos cegos |
| pipeline-md-writer | Formata drafts em markdown polido |
| consolidator | Consolida tudo no delivery report final |

## 📚 Knowledge Packs

Domínios tecnológicos disponíveis localmente em `base-artifacts/knowledge/`:

| Domínio | Context | Specialists |
|---------|---------|-------------|
| saas | `base-artifacts/knowledge/saas/context.md` | `base-artifacts/knowledge/saas/specialists.md` |
| datalake-ingestion | `base-artifacts/knowledge/datalake-ingestion/context.md` | `base-artifacts/knowledge/datalake-ingestion/specialists.md` |
| process-documentation | `base-artifacts/knowledge/process-documentation/context.md` | `base-artifacts/knowledge/process-documentation/specialists.md` |
| web-microservices | `base-artifacts/knowledge/web-microservices/context.md` | `base-artifacts/knowledge/web-microservices/specialists.md` |

> [!info] Knowledge packs são cópias locais do workspace global (`base-artifacts/`). A fonte de verdade continua no workspace central — sincronize quando necessário.

## 🚀 Scaffold de uma Run

```
runs/run-{n}/
├── pipeline-state.md                 Estado + snapshots (append-only)
├── setup/
│   ├── briefing.md                   Input do humano
│   ├── config.md                     Configuração da run
│   └── customization/
│       ├── current-context/          Knowledge pack copiado
│       ├── report-templates/         Templates de output
│       └── rules/                    Políticas da run
├── iterations/
│   └── iteration-{i}/
│       ├── logs/                     Interview + HR loop logs
│       └── results/                  Outputs por fase
│           ├── 1-discovery/          8 blocos (1.1 to 1.8)
│           ├── 2-challenge/          2 validações
│           └── 3-delivery/           3 sub-fases
└── delivery/                         Output final (md + html)
```

## 📄 Docs

| Documento | Descrição |
|-----------|-----------|
| `docs/quick-start.md` | Como iniciar uma nova run |
| `docs/discovery-pipeline.md` | Guia completo do pipeline |
| `docs/logging-process.md` | Como funciona o logging |
| `docs/dependency-manifest.md` | Manifesto de dependências do projeto |

## 🔗 Documentos Relacionados

- `dtg-artifacts/rules/` — Regras comportamentais do pipeline (discovery, iteration-loop, audit-log, etc.)
- `dtg-artifacts/templates/` — Templates de artefatos (briefing, reports, memory, etc.)
- `dtg-artifacts/skills/` — Skills locais do pipeline (orchestrator, customer, auditor, etc.)
- `dtg-artifacts/arctifact-samples/` — Samples de uma run completa
- `custom-rules/` — Customizações por tenant/cliente (scoring, policies, etc.)
- `base-artifacts/` — Cópia local do workspace global (assets, conventions, knowledge, etc.)

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 02.00.000 | 2026-04-11 | Reestruturação em 3 camadas (base-artifacts, dtg-artifacts, custom-rules) |
| 01.00.000 | 2026-04-10 | Criação — reestruturação completa do projeto com separação definição/execução |
