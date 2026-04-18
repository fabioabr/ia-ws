# Report Setups (legacy — superseded by `deliverables_scope` + layouts)

> [!warning]
> **Esta pasta é legacy.** Desde 2026-04-17 (ADR-001 + task #18), o framework usa `deliverables_scope` no briefing + arquivos de layout para decidir o que é produzido. Esta pasta permanece como **catálogo de referência** das regions por HTML, consumida pelo `html-writer` quando precisa montar o relatório, mas **não deve mais ser citada no briefing** — use `deliverables_scope`.

## Presets mantidos (referência de regions por HTML)

| Setup | Arquivo | Output | Equivalente `deliverables_scope` |
|-------|---------|--------|----------------------------------|
| **Essencial** | `essential.md` | `one-pager.html` | `["DR", "OP"]` |
| **Executivo** | `executive.md` | `one-pager.html` + `executive-report.html` | `["DR", "OP", "EX"]` |
| **Completo** | `complete.md` | `one-pager.html` + `executive-report.html` + `full-report.html` | `["DR", "OP", "EX"]` |

## O que é canônico hoje

1. **Briefing declara `deliverables_scope`:**

   ```yaml
   deliverables_scope: ["DR", "OP", "EX"]  # ou ["DR", "OP"] ou ["DR"]
   ```

2. **Layouts definem as regions de cada entregável:**
   - `base/starter-kit/client-template/templates/customization/one-pager-layout.md` — regions do OP
   - `base/starter-kit/client-template/templates/customization/executive-layout.md` — regions do EX
   - `base/starter-kit/client-template/templates/customization/html-layout.md` — override total por cliente (opcional)

3. **Pipeline produz sempre o DR** e, se `OP`/`EX` estiverem em `deliverables_scope`, o `deliverable-distiller` destila a partir do DR.

## O que esta pasta ainda serve para

Os arquivos `essential.md`, `executive.md` e `complete.md` **continuam úteis** como:
- Catálogo de IDs de region por tipo de HTML (`REG-EXEC-*`, `REG-PROD-*`, etc.)
- Notas de renderização (layouts `grid-3`, `full-width`, stat cards, tabs)
- Condicionais domain-specific (ex: `REG-DOM-SAAS-01` só em context-template `saas`)

O `html-writer` lê esses presets quando vai montar o HTML, cruzando com os layouts acima.

## Migração do briefing

**Antes (legacy):**

```yaml
report-setup: executive
```

**Agora (canônico):**

```yaml
deliverables_scope: ["DR", "OP", "EX"]
# report-setup: executive  # opcional, mantido como alias para tools antigas
```

O `tools/create-run/main.py` aceita os dois formatos: se só `report-setup` estiver presente, deriva `deliverables_scope` automaticamente (com warning).

## Histórico

| Data | Mudança |
|------|---------|
| 2026-04-17 | Pasta reposicionada como legacy. README reescrito com mapeamento para `deliverables_scope`. Origem: task #18 do TODO. |
