---
title: TODO
description: Lista de pendências do projeto Discovery To Go
project-name: discovery-to-go
version: 03.00.000
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
<summary>Itens 1-10 + extras (clique para expandir)</summary>

### ~~1. Consolidar os 3 packs antigos no formato único~~ DONE
### ~~2. Atualizar sample run para novo formato~~ DONE
### ~~3. Terminologia "knowledge pack" → "context-template"~~ DONE
### ~~4. Seção "Knowledge" no CLAUDE.md do workspace~~ DONE
### ~~5. Arquivo temporário do draw.io no git~~ DONE
### ~~6. Arquivo product-discovery-deliverables.md~~ DONE
### ~~7. README.md desatualizado~~ DONE
### ~~8. Information Regions~~ DONE
- 8.1 Catálogo (README.md) — 85 regions em 14 grupos
- 8.2 85 arquivos individuais com schema, exemplo, chart specialist
- 8.3 10 blueprints com seção "Regions do Delivery Report"
- 8.4 html-layout.md (template default de layout)
- 8.5 15 HTMLs de preview por grupo
### ~~9. Consolidator atualizado~~ DONE
Gera delivery-report.md com marcadores de region.
### ~~10. HTML Writer atualizado~~ DONE
Modo regions: lê marcadores, aplica html-layout, grid responsivo, Chart.js condicional.
### ~~Report Planner skill~~ DONE
Nova skill (Fase 3.2.5) entre consolidator e html-writer.
### ~~READMEs em todas as subpastas~~ DONE
base-artifacts, docs, dtg-artifacts + index.md consolidado no README.md raiz.

</details>

---

## 11. Atualizar Sample Run

O sample run (`dtg-artifacts/arctifact-samples/run-sample/`) precisa refletir o novo fluxo:

- [ ] `delivery/delivery-report.md` no formato de regions (com marcadores `<!-- region: REG-XXXX-NN -->`)
- [ ] `delivery/report-plan.md` — plano visual gerado pelo report-planner
- [ ] `delivery/delivery-report.html` — HTML gerado pelo html-writer com regions visuais

**Arquivos:** `dtg-artifacts/arctifact-samples/run-sample/delivery/`

---

## 12. CLAUDE.md — Adicionar novas skills

Adicionar ao `CLAUDE.md` do workspace:
- [ ] `chart-specialist` na lista de skills globais
- [ ] Atualizar descrição do `html-writer` (v02, modo regions)

**Arquivo:** `E:\Workspace\CLAUDE.md`

---

## 13. Sync base-artifacts

Verificar e sincronizar drift entre workspace global e `base-artifacts/`:

- [ ] `chart-specialist` skill (nova, não está em base-artifacts)
- [ ] `html-writer` skill (atualizada para v02)
- [ ] Context-templates atualizados (10 blueprints com regions)
- [ ] Report-regions (85 arquivos + previews + README)
- [ ] Verificação geral de versões
