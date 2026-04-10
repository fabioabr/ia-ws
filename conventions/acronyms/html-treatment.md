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
