---
title: TODO
description: Lista de pendências do projeto Discovery To Go
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: todo
area: tecnologia
tags:
  - todo
  - pendencia
created: 2026-04-11
updated: 2026-04-11
---

# TODO — Discovery To Go

---

## Concluídos

<details>
<summary>Itens 1-7 (clique para expandir)</summary>

### ~~1. Consolidar os 3 packs antigos no formato único~~ DONE
Os packs `saas`, `process-documentation` e `web-microservices` foram consolidados em `discovery-blueprint.md` único.

### ~~2. Atualizar sample run para novo formato~~ DONE
Sample run atualizado — `current-context/` agora tem apenas `saas-discovery-blueprint.md`.

### ~~3. Terminologia "knowledge pack" → "context-template"~~ DONE
70 ocorrências substituídas em 24 arquivos.

### ~~4. Seção "Knowledge" no CLAUDE.md do workspace~~ DONE
Heading atualizado para `## Context-Templates`.

### ~~5. Arquivo temporário do draw.io no git~~ DONE
`.$*.bkp` e `.$*.dtmp` adicionados ao `.gitignore`.

### ~~6. Arquivo `product-discovery-deliverables.md`~~ DONE
Mantido em `docs/` como referência teórica.

### ~~7. README.md desatualizado~~ DONE
10 packs, formato documento único, multi-template, scaffold corrigido.

</details>

---

## 8. Information Regions — PARCIAL

Sistema de regions reutilizáveis para o delivery report (`.md` completo + `.html` configurável).

```
discovery-blueprint.md          delivery-report.md           delivery-report.html
(define quais regions)    →     (conteúdo completo)     →   (regions visuais)
       ↑                                                          ↑
custom-artifacts/                                         html-layout.md
(override por cliente)                                    (quais regions, ordem, layout)
```

| # | Entregável | Status |
|---|-----------|--------|
| 8.1 | Catálogo de regions (`base-artifacts/templates/report-regions/README.md`) — 85 regions em 14 grupos | DONE |
| 8.2 | 85 arquivos individuais com schema, exemplo, dados visuais e recomendação do chart-specialist | DONE |
| 8.3 | Blueprints → regions: cada discovery-blueprint listar quais regions são obrigatórias/opcionais | PENDENTE |
| 8.4 | `dtg-artifacts/templates/customization/html-layout.md` — template default de layout HTML | PENDENTE |
| 8.5 | Templates HTML por region — componentes visuais reutilizáveis para o html-writer | PENDENTE |

---

## 9. Atualizar Consolidator para gerar por regions

O consolidator hoje gera o `delivery-report.md` usando seções fixas (11 seções base + extras por context-template). Precisa ser atualizado para:

- Ler o catálogo de regions + blueprint do context-template carregado
- Gerar cada seção do `.md` como uma region identificada (com marcador que o html-writer reconhece)
- Respeitar a lista de regions obrigatórias/opcionais do blueprint
- Manter o `.md` completo e legível como texto puro (sem depender de HTML)

**Arquivos:** `dtg-artifacts/skills/consolidator/SKILL.md`

---

## 10. Atualizar HTML Writer para renderizar regions

O html-writer hoje converte `.md` → `.html` de forma linear. Precisa ser atualizado para:

- Ler `html-layout.md` para saber quais regions renderizar, em que ordem e com que layout
- Usar os templates visuais por region (card, table, chart, timeline, etc.)
- Renderizar gráficos Chart.js onde indicado pelo chart-specialist
- Respeitar HTML/CSS puro como prioridade (Chart.js só onde necessário)
- Manter dark/light theme, responsividade e auto-contido

**Arquivos:** `.claude/skills/html-writer/SKILL.md`, templates HTML por region

---

## 11. Atualizar Sample Run

O sample run (`dtg-artifacts/arctifact-samples/run-sample/`) precisa refletir:

- `delivery-report.md` no formato de regions (com marcadores)
- `delivery-report.html` gerado pelo novo html-writer com regions visuais
- `setup/customization/` com `html-layout.md` (se customizado)

**Arquivos:** `dtg-artifacts/arctifact-samples/run-sample/delivery/`

---

## 12. CLAUDE.md — Adicionar chart-specialist

Adicionar `chart-specialist` à lista de skills globais no `CLAUDE.md` do workspace.

**Arquivo:** `E:\Workspace\CLAUDE.md`

---

## 13. Sync base-artifacts

Vários arquivos novos/alterados no projeto que precisam ser espelhados no `base-artifacts/`:

- Context-templates consolidados (já sincronizados)
- Templates de report-regions (já estão em base-artifacts)
- Skills globais alteradas (chart-specialist é nova, não está em base-artifacts)
- Verificar se há drift entre workspace global e base-artifacts

---

## Ordem sugerida de execução

```
12. CLAUDE.md (rápido)                          ← 1 min
 ↓
8.3 Blueprints → regions (10 blueprints)        ← paralelo com 10 agentes
 ↓
8.4 html-layout.md (template default)           ← 1 arquivo
 ↓
9. Consolidator atualizado                       ← SKILL.md
 ↓
8.5 Templates HTML por region                    ← componentes visuais
 ↓
10. HTML Writer atualizado                       ← SKILL.md
 ↓
11. Sample run atualizado                        ← validação end-to-end
 ↓
13. Sync base-artifacts                          ← verificação final
```
