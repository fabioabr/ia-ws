---
title: TODO
description: Lista de pendências do projeto Discovery To Go
project-name: discovery-to-go
version: 04.00.000
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
<summary>Todos os itens concluídos (clique para expandir)</summary>

- ~~1. Consolidar os 3 packs antigos no formato único~~ DONE
- ~~2. Atualizar sample run para novo formato~~ DONE
- ~~3. Terminologia "knowledge pack" → "context-template"~~ DONE
- ~~4. Seção "Knowledge" no CLAUDE.md do workspace~~ DONE
- ~~5. Arquivo temporário do draw.io no git~~ DONE
- ~~6. Arquivo product-discovery-deliverables.md~~ DONE
- ~~7. README.md desatualizado~~ DONE
- ~~8. Information Regions (catálogo, 85 arquivos, blueprints, html-layout, previews)~~ DONE
- ~~9. Consolidator atualizado (delivery-report.md com marcadores de region)~~ DONE
- ~~10. HTML Writer atualizado (modo regions, grid responsivo, Chart.js)~~ DONE
- ~~11. Atualizar Sample Run (delivery-report.md, report-plan.md, HTML com regions)~~ DONE
- ~~12. CLAUDE.md — Adicionar novas skills (chart-specialist, html-writer v02)~~ DONE
- ~~13. Sync base-artifacts (chart-specialist, html-writer v02, blueprints, regions)~~ DONE
- ~~Report Planner skill (Fase 3.2.5)~~ DONE
- ~~READMEs em todas as subpastas (base-artifacts, docs, dtg-artifacts + index.md)~~ DONE
- ~~Report setups (essential, executive, complete) com region presets~~ DONE
- ~~Setup selector skill para escolha interativa de setup~~ DONE

</details>

---

## Pendências

### 14. Teste end-to-end do pipeline

Nunca foi executado o pipeline completo de ponta a ponta. Necessário:

- [ ] Criar um briefing de teste (projeto simples — CRUD ou landing page)
- [ ] Executar orchestrator → Fase 1 (Discovery) → HR Review
- [ ] Executar Fase 2 (Challenge) → HR Review
- [ ] Executar Fase 3 (Delivery): md-writer → consolidator → report-planner → html-writer
- [ ] Validar que os marcadores de region (`<!-- region: REG-XXXX-NN -->`) são gerados corretamente
- [ ] Validar que report-plan.md é gerado pelo report-planner
- [ ] Validar que o HTML final renderiza as regions conforme o plano
- [ ] Documentar problemas encontrados e corrigir

---

### 15. Validação de report setups

Testar os 3 presets gerando HTMLs reais a partir do sample run (FinTrack Pro):

- [ ] `essential.md` → gerar `one-pager.html` (8 regions)
- [ ] `executive.md` → gerar `one-pager.html` + `executive-report.html` (28 regions)
- [ ] `complete.md` → gerar `one-pager.html` + `executive-report.html` + `full-report.html` (90 regions)
- [ ] Comparar visualmente os 3 níveis de detalhe
- [ ] Validar que regions domain-specific (SaaS) aparecem apenas no setup complete

---

### 16. Processo de sync periódico de base-artifacts

Estabelecer processo recorrente para manter base-artifacts sincronizado:

- [ ] Criar script ou skill de sincronização automática
- [ ] Definir quando sincronizar (antes de cada run? após cada commit?)
- [ ] Documentar no `docs/reference/dependency-manifest.md`

---

### 17. Atualizar quick-start.md com report setups

O quick-start.md não menciona os 3 report setups (essential/executive/complete). Precisa:

- [ ] Adicionar passo sobre escolha do report-setup na Fase 3
- [ ] Explicar que o config.md define `report-setup: essential|executive|complete`
- [ ] Mencionar que o cliente pode sobrescrever com html-layout.md customizado

---

### 18. README.md do projeto — seções desatualizadas

O README.md principal ainda não documenta:

- [ ] Os 3 report setups (essential/executive/complete)
- [ ] O fluxo completo da Fase 3 com 4 sub-fases (md-writer → consolidator → report-planner → html-writer)
- [ ] A pasta `templates/draft-templates/` (reorganização)
- [ ] O client template scaffold (`custom-artifacts/_client-template/`)
