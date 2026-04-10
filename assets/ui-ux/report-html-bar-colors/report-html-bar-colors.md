---
title: Report HTML — Sequential Color Palette
description: Paleta fixa de 4 cores para elementos sequenciais (barras, fases, cards) em reports HTML
project-name: global
version: 01.01.000
status: ativo
author: claude-code
category: document-creation
area: design
tags:
  - report
  - html
  - design-system
  - cores
  - graficos
created: 2026-04-09 12:00
---

# Report HTML — Sequential Color Palette

Paleta obrigatória de 4 cores para todos os elementos sequenciais em reports HTML gerados pelo Design System: barras, fases, cards de métricas e phase-flows.

---

## Paleta Fixa (4 cores, ordem obrigatória)

| Posição | Classe CSS        | Variável CSS       | Uso semântico            |
| ------- | ----------------- | ------------------ | ------------------------ |
| 1ª      | `bg-primary`      | `var(--primary)`   | Primeiro item da série   |
| 2ª      | `bg-success`      | `var(--success)`   | Segundo item da série    |
| 3ª      | `bg-warning`      | `var(--warning)`   | Terceiro item da série   |
| 4ª      | `bg-danger`       | `var(--danger)`    | Quarto item da série     |

## Regras de Aplicação

1. **Barras horizontais** (`.dash-bar-seg`) — cada barra recebe a cor correspondente à sua posição na sequência
2. **Fases / Phase Flow** (`.phase-box`) — cada fase recebe a cor da sua posição (Fase 1 = primary, Fase 2 = success, Fase 3 = warning, Fase 4 = danger)
3. **Section headers de fase** (`.section-icon`) — seguem a mesma cor da fase correspondente
4. **KPIs de fase** (`border-left-color` e valor) — seguem a cor da fase a que pertencem
5. **Cards de header** (`card-header-icon`) dentro de uma fase (entregas, esforço, equipe) — seguem a cor da fase
6. **Badges** (`card-badge`) — usam a variante `light` da mesma cor (ex: `var(--primary-light)` com texto `var(--primary)`)
7. **Ciclo** — se houver mais de 4 itens, as cores reiniciam a partir da 1ª posição

## Exemplo — Barras de Esforço

```html
<!-- 1ª barra: primary -->
<div class="dash-bar-seg bg-primary" style="width:15%">15%</div>

<!-- 2ª barra: success -->
<div class="dash-bar-seg bg-success" style="width:62%">62%</div>

<!-- 3ª barra: warning -->
<div class="dash-bar-seg bg-warning" style="width:15%">15%</div>

<!-- 4ª barra: danger -->
<div class="dash-bar-seg bg-danger" style="width:8%">8%</div>
```

## Exemplo — Phase Flow (3 fases)

```html
<div class="phase-box bg-primary">Fase 1 — MVP</div>
<div class="phase-arrow">&rarr;</div>
<div class="phase-box bg-success">Fase 2 — Expansão</div>
<div class="phase-arrow">&rarr;</div>
<div class="phase-box bg-warning">Fase 3 — Escala</div>
```

## Exemplo — Phase Flow (4 fases, playground)

```html
<div class="phase-box" style="background:var(--primary-light);color:var(--primary);border:1px solid var(--primary)">Fase 1</div>
<div class="phase-box" style="background:var(--success-light);color:var(--success);border:1px solid var(--success)">Fase 2</div>
<div class="phase-box" style="background:var(--warning-light);color:var(--warning);border:1px solid var(--warning)">Fase 3</div>
<div class="phase-box" style="background:var(--danger-light);color:var(--danger);border:1px solid var(--danger)">Fase 4</div>
```

## Escopo

- Aplica-se a todos os reports HTML gerados pela skill `report-maker`
- Aplica-se a exemplos do playground (`playground.html`)
- NÃO se aplica a gráficos Chart.js (doughnut, bar charts comparativos), que possuem paleta própria

---

## 🔗 Documentos Relacionados

- [[behavior/rules/writing/acronym-glossary/acronym-glossary]] — Tratamento de siglas nos mesmos reports

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição          |
| --------- | ---------------- | ------------------ |
| 01.00.000 | 2026-04-09 12:00 | Criação da regra   |
| 01.01.000 | 2026-04-09 12:30 | Expansão: paleta agora cobre fases, phase-flow, section-icons e KPIs de fase |
