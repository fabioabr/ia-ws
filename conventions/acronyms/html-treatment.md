---
title: Acronym Treatment in HTML
description: Regras de marcação e estilização de siglas em relatórios e interfaces HTML.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - sigla
  - html
  - acessibilidade
created: 2026-04-10 12:00
---

# Acronym Treatment in HTML

How to handle acronyms in HTML reports and interfaces.

## Standard

### Markup

```html
<abbr class="acronym" title="Application Programming Interface">API</abbr>
```

### CSS

```css
.acronym {
  color: var(--primary);
  cursor: help;
}

.acronym:hover {
  color: var(--info);
}
```

### Glossary in Reports

- Render as the **last tab** in report interfaces.
- Tab button includes an icon and a count of unique acronyms.

```html
<button class="tab-button">
  <span class="icon">glossary</span>
  <span class="count">5</span>
</button>
```
