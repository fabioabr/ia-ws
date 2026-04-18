---
title: Gantt Hierárquico (Épico → Estória) Component
description: Gantt HTML/CSS puro com 2 níveis (épico + estórias), 1 coluna por semana, linha-guia de Marco/Quick Win, estrela emoji em entregas e coluna destacada — sem libs externas.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - gantt
  - cronograma
  - quick-win
  - milestone
created: 2026-04-17
updated: 2026-04-17
---

# Gantt Hierárquico (Épico → Estória)

Gantt construído em HTML + CSS puro (sem Mermaid, sem libs) para representar cronogramas com:

- **Nível 1** — Épico (linha agrupadora, fundo escurecido)
- **Nível 2** — Estórias filhas (linhas normais)
- **Linha-guia de Marco** (ex: Quick Win) — fundo verde uniforme com emoji de estrela ⭐ na semana-alvo
- **Coluna destacada** — a semana do marco fica em verde claro translúcido em todas as linhas
- **Estrela sobreposta** na estória-chave que representa a entrega do marco

## Tabela raiz (`.gantt-table`)

| Property | Value |
|----------|-------|
| Width | `100%` |
| Border collapse | `collapse` |
| Min-width | `1180px` (scroll horizontal quando faltar espaço) |

### Células base

```css
.gantt-table th, .gantt-table td {
  padding: 3px 1px;
  font-size: 0.68rem;
  border: none;
  vertical-align: middle;
}
.gantt-table thead th {
  background: var(--th-bg);
  font-weight: 600;
  text-align: center;
  border-bottom: 1px solid var(--border);
}
.gantt-table th.label-col {
  text-align: left;
  width: 340px;
  padding: 4px 8px;
}
.gantt-table th:not(.label-col) { width: 32px; }
.gantt-table td.week {
  text-align: center;
  background: transparent;
  border-right: 1px solid var(--border);
  vertical-align: middle;
  padding: 4px 2px;
  position: relative;
}
```

- **1 coluna por semana** — cada `<th>` contém o número da semana (1..N).
- Label column (primeira td de cada linha) tem largura fixa de `340px`.
- `position: relative` em `td.week` habilita sobreposição absoluta (estrelas, marcadores).

## Barras (`.gantt-bar`)

| Seletor | Propriedades |
|---------|--------------|
| `.gantt-bar` | `height: 16px; border-radius: 4px; display: inline-block; width: 100%; vertical-align: middle` |
| `.gantt-bar.epic` | `background: var(--primary)` |
| `.gantt-bar.story` | `background: rgba(77,168,218,0.45)` |
| `.gantt-bar.qw` | `background: var(--success)` (opcional — entrega pontual) |

`vertical-align: middle` é **obrigatório** para barras alinharem corretamente com emojis/estrelas na mesma célula.

## Linhas de épico (`.gantt-epic`)

Toda a linha fica escurecida para agrupar visualmente suas estórias.

```css
.gantt-epic td, tr.gantt-epic td.week {
  background: rgba(0,0,0,0.14);
  font-weight: 700;
}
```

> **Especificidade:** use `tr.gantt-epic td.week` (0,2,2) para vencer `.gantt-table td.week` (0,2,1) e garantir que **todas** as 24 células (mesmo as vazias) recebam o escurecimento.

## Linha de marco (`.gantt-milestone`)

Linha-guia no topo do tbody indicando um marco contratual (ex: Release do Quick Win).

```css
.gantt-milestone td, tr.gantt-milestone td.week {
  background: rgba(14,209,69,0.18);
  font-weight: 700;
  color: var(--alert-success-text);
}
.gantt-milestone td:first-child { font-size: 0.82rem; }
```

- **NÃO** usar `border-left` azul/verde no primeiro td — visualmente poluído.
- Deve ser a **primeira linha do `<tbody>`** para ancorar o leitor no marco antes de ver os épicos.

## Estrela em entregas (`.gantt-star`)

Emoji ⭐ sobreposto à célula indica "aqui acontece a entrega". Posicionada absolute no centro da célula.

```css
.gantt-star {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.9rem;
  z-index: 2;
  pointer-events: none;
  line-height: 1;
}
```

Uso em HTML:

```html
<!-- Linha de marco: estrela sem barra -->
<td class="week qw-col"><span class="gantt-star">⭐</span></td>

<!-- Estória-chave do marco: estrela sobre a barra -->
<td class="week qw-col"><span class="gantt-bar story"></span><span class="gantt-star">⭐</span></td>
```

> A estrela vai **na estória** que representa a entrega concreta do marco — **não no épico**. O épico apenas agrupa; a entrega é feita pela estória.

## Coluna destacada do Marco (Quick Win)

Ex: se o marco é na semana 10, use `:nth-child(11)` (coluna 1 = label, coluna 11 = semana 10).

```css
/* Fundo verde claro na coluna inteira */
.gantt-table th:nth-child(11),
.gantt-table td:nth-child(11) { background: var(--success-light); }

/* Indicador ⚡ no cabeçalho */
.gantt-table thead th:nth-child(11) {
  color: var(--alert-success-text);
  font-weight: 800;
  position: relative;
}
.gantt-table thead th:nth-child(11)::after {
  content: '⚡';
  position: absolute;
  top: 0px;
  right: 1px;
  font-size: 0.58rem;
}

/* Intersecção épico × coluna QW: verde mais escuro (layered) */
.gantt-epic td:nth-child(11),
tr.gantt-epic td.week:nth-child(11) {
  background-color: rgba(0,0,0,0.14);
  background-image: linear-gradient(var(--success-light), var(--success-light));
}
```

> **Técnica layered:** `background-color` (escurecimento) + `background-image: linear-gradient()` com a cor translúcida verde empilha as camadas. Como `--success-light` tem alpha 0.12, o verde passa a mostrar o escurecimento por baixo, criando um verde-escuro integrado à estética da linha de épico.

## Classe `qw-col` nas células

Toda célula da coluna do marco (semana-alvo) deve receber `class="week qw-col"`. Isso serve como âncora semântica e permite sobrescritas futuras sem depender só de `:nth-child`.

```html
<td class="week qw-col"></td>
<td class="week qw-col"><span class="gantt-bar story"></span></td>
```

## Tipografia

- Label (primeira td) herda `font-size: 0.68rem` da célula base.
- Marco (primeira td) tem `font-size: 0.82rem` — um pouco maior para destaque.
- A escala global (`html { font-size: 15px }`) reduz tudo proporcionalmente.

## Estrutura HTML esperada

```html
<table class="gantt-table">
  <thead>
    <tr>
      <th class="label-col">Épico / Estória</th>
      <th>1</th><th>2</th>...<th class="qw-col">10</th>...<th>24</th>
    </tr>
  </thead>
  <tbody>
    <!-- 1. Marco primeiro (linha-guia) -->
    <tr class="gantt-milestone">
      <td>⚡ Marco 1 · Release do Quick Win (Semana 10)</td>
      <td class="week"></td>...
      <td class="week qw-col"><span class="gantt-star">⭐</span></td>
      ...
    </tr>

    <!-- 2. Épico 1 -->
    <tr class="gantt-epic">
      <td>Épico 1 — ...</td>
      <td class="week"><span class="gantt-bar epic"></span></td>...
    </tr>
    <!-- 2.1 Estórias -->
    <tr class="gantt-story">
      <td>Estória ...</td>
      <td class="week"><span class="gantt-bar story"></span></td>...
    </tr>

    <!-- 3. Épico 2 (contém a entrega do marco) -->
    <tr class="gantt-epic">...</tr>
    <tr class="gantt-story">
      <td>Estória-chave da entrega</td>
      ...
      <td class="week qw-col">
        <span class="gantt-bar story"></span>
        <span class="gantt-star">⭐</span>
      </td>
    </tr>
  </tbody>
</table>
```

## Checklist de implementação

- [ ] 1 coluna por semana (`<th>` numerado 1..N)
- [ ] Linha do marco é a **primeira** do tbody
- [ ] Linha do marco **NÃO** tem `border-left` colorido no primeiro td
- [ ] `vertical-align: middle` nas barras
- [ ] `tr.gantt-epic td.week` (não apenas `.gantt-epic td.week`) para especificidade
- [ ] Estrela ⭐ na estória-chave, **não** no épico
- [ ] `background-color + background-image` na intersecção épico × coluna QW
- [ ] `position: relative` em `.gantt-table td.week` para ancorar a `.gantt-star`
- [ ] Cabeçalho da coluna QW com `::after` contendo ⚡
