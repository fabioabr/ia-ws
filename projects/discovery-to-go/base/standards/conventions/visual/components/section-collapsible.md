---
title: Section Collapsible Component
description: Padrão de sessão recolhível com header clicável, chevron rotativo e borda tracejada no estado recolhido — aplicável a toda region do relatório.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: design
tags:
  - componente
  - section
  - collapse
  - interatividade
created: 2026-04-17
updated: 2026-04-17
---

# Section Collapsible Component

Toda `.section` do relatório deve permitir que o leitor recolha/expanda seu conteúdo clicando no header. O botão é injetado via JS — não é necessário alterar o HTML de cada seção.

## Container (`.section-header`)

| Property | Value |
|----------|-------|
| Display | `flex` |
| Align items | `center` |
| Gap | `12px` |
| Margin bottom | `20px` |
| Padding bottom | `12px` |
| Border bottom | `2px solid var(--border)` |
| Cursor | `pointer` |
| User select | `none` |

### Hover

| Property | Value |
|----------|-------|
| `.section-toggle` color | `var(--primary)` |

## Botão (`.section-toggle`)

| Property | Value |
|----------|-------|
| Margin left | `auto` (empurra para direita) |
| Background | `none` |
| Border | `none` |
| Color | `var(--text-muted)` |
| Cursor | `pointer` |
| Font size | `1.25rem` |
| Padding | `4px 8px` |
| Border radius | `6px` |
| Transition | `transform 0.2s, color 0.2s` |
| Display | `inline-flex`, centered |
| Icon | `ri-arrow-down-s-line` (Remix Icon) |

## Estado recolhido (`.section.collapsed`)

| Seletor | Regra |
|---------|-------|
| `.section.collapsed .section-toggle` | `transform: rotate(-90deg)` — chevron aponta para esquerda |
| `.section.collapsed > *:not(.section-header)` | `display: none` — oculta todo conteúdo exceto header |
| `.section.collapsed .section-header` | `margin-bottom: 0; padding-bottom: 12px; border-bottom: 1px dashed var(--border)` — borda tracejada sinaliza estado recolhido |

## Injeção via JS

O botão é adicionado dinamicamente em `DOMContentLoaded`:

```javascript
document.querySelectorAll('.section').forEach(section => {
  const header = section.querySelector('.section-header');
  if (!header) return;
  const toggle = document.createElement('button');
  toggle.className = 'section-toggle';
  toggle.type = 'button';
  toggle.setAttribute('aria-label', 'Expandir/Recolher seção');
  toggle.innerHTML = '<i class="ri-arrow-down-s-line"></i>';
  header.appendChild(toggle);
  header.addEventListener('click', (e) => {
    e.stopPropagation();
    section.classList.toggle('collapsed');
  });
});
```

## Quando aplicar

- **Todas as regions** do relatório (`<div class="section">`).
- Exceção: seções que contêm o conteúdo principal/descritivo da primeira tela podem iniciar expandidas e não ganhar o botão apenas se o usuário solicitar explicitamente.

## Acessibilidade

- Botão tem `aria-label="Expandir/Recolher seção"`.
- Header inteiro é clicável (cursor pointer + user-select none).
- Estado visual do chevron (rotação) sinaliza expandido/recolhido sem depender só de cor.
