---
title: Template Syntax Specification
description: Especificacao formal da sintaxe usada nos arquivos template.md de report-templates. Define frontmatter, area de custom regions, area de sub-templates, area de layout, gramatica de cards, filtros de variante e interpolacao de variaveis de setup.
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: specification
area: tecnologia
tags:
  - spec
  - syntax
  - report-templates
  - parser
  - grammar
created: 2026-04-17
updated: 2026-04-17
---

# Template Syntax Specification

Especificacao formal da sintaxe do arquivo `template.md` de qualquer report-template. Esta spec e a referencia canonica para:

- Autores de template (o que podem escrever)
- Parser Python em `support-tools/template-parser/` (o que precisa interpretar)
- Report-composer (como materializar o template)

## Estrutura geral do arquivo

Todo `template.md` tem 4 partes, nessa ordem:

1. **Frontmatter** — metadados do template
2. **`## Custom Regions`** — declaracao de regions especificas do template
3. **`## Sub-Templates`** — blocos reusaveis parametrizados (opcional)
4. **`## Layout`** — estrutura final: tabs, sections, cards

```markdown
---
template-id: basic
title: Relatorio Basic
...
---

## Custom Regions

### CUSTOM-1 — Nome
Prompt: ...

## Sub-Templates

### SUB-SCENARIO — Cenario ({scenario})
> Section A
[REG-X:{scenario}]

## Layout

# Tab: Nome da Tab

> Section
[REG-ID | CUSTOM-1]
```

## 1. Frontmatter

Campos obrigatorios:

| Campo | Tipo | Exemplo |
|-------|------|---------|
| `template-id` | string (kebab) | `basic` |
| `title` | string | `Relatorio Basic de Discovery` |
| `audience` | string | `decisores + time de projeto` |
| `version` | string semver | `01.00.000` |
| `description` | string | narrativa curta do proposito |
| `created` | date | `2026-04-17` |
| `updated` | date | `2026-04-17` |

## 2. Area `## Custom Regions`

Declara regions exclusivas deste template — cards cujo conteudo nao existe no catalogo `report-regions/`. Cada custom region tem um **codigo** e um **prompt**.

Sintaxe:

```markdown
## Custom Regions

### CUSTOM-1 — Titulo curto
Prompt: Texto que descreve o que o report-composer deve gerar quando este card
for requisitado no layout. Pode ser multilinha. Deve especificar formato
esperado (tabela, stat cards, bullets, etc.) e o conteudo semantico.

### CUSTOM-2 — Outro titulo
Prompt: ...
```

**Regras:**

- Codigo: `CUSTOM-N` onde N e inteiro sequencial a partir de 1
- Titulo: curto, separado do codigo por ` — ` (em-dash com espacos)
- Prompt: bloco de texto logo apos `Prompt:`, pode ter multiplas linhas ate a proxima `### CUSTOM-` ou ate o fim da secao
- Um template pode ter 0 ou mais custom regions
- O escopo do codigo `CUSTOM-N` e **local ao template** — dois templates diferentes podem ter `CUSTOM-1` cada, sem conflito

## 3. Area `## Sub-Templates`

Declara blocos reusaveis de layout parametrizados por variavel. Sao usados quando o mesmo conjunto de sections/cards precisa aparecer multiplas vezes com pequenas diferencas (ex: um bloco por cenario).

Sintaxe:

```markdown
## Sub-Templates

### SUB-SCENARIO — Cenario ({scenario})

> Descritivo
[REG-FIN-07:{scenario}]

> Escopo
[CUSTOM-1:{scenario}]
```

**Regras:**

- Codigo: `SUB-{NOME}` (maiusculo, kebab opcional)
- Titulo pode conter placeholders `{variavel}` que sao substituidos na materializacao
- Corpo do sub-template segue a mesma gramatica do `## Layout`: sections (`>`) e rows de cards (`[...]`)
- Variaveis `{nome}` podem aparecer dentro de filtros `:variant` e sao substituidas pelo valor concreto no momento da renderizacao
- Sub-templates sao invocados no `## Layout` via `[SUB-NOME:valor]`

## 4. Area `## Layout`

Estrutura do relatorio final. Organiza tabs, sections e cards.

### 4.1 Tab

Uma tab e delimitada por `# Tab: Nome`. Tabs sao separadas por `---` (horizontal rule).

```markdown
# Tab: Visao do Projeto

...conteudo da tab...

---

# Tab: Cenario Recomendado

...conteudo da tab...
```

**Regras:**

- Nome da tab aparece no botao/aba do HTML final
- Ordem das tabs no `template.md` = ordem de exibicao
- Template tem no minimo 1 tab

### 4.2 Section

Uma section e um agrupador dentro de uma tab, delimitado por `> Nome da Section`.

```markdown
# Tab: Visao do Projeto

> Descritivo
[REG-EXEC-02]

> Problemas Atuais
[REG-PROD-01]
```

**Regras:**

- Sintaxe: linha comecando com `>` seguido de espaco e nome
- Nome aparece no header visual do grupo (com icone + divisor)
- Uma section pode ter 1 ou mais rows de cards
- Uma tab pode ter 1 ou mais sections

### 4.3 Row de cards

Uma row e uma linha entre colchetes contendo um ou mais cards separados por `|`.

```markdown
> Indicadores
[REG-FIN-06 | REG-FIN-01:total | REG-ORG-02:count | REG-QUAL-01:score]
```

**Regras:**

- Sintaxe: `[card1 | card2 | ... | cardN]` em uma unica linha
- Um card por coluna — N cards = grid responsivo de N colunas
- Uma section pode ter multiplas rows (cada row = uma linha visual nova)

```markdown
> Cenario
[REG-FIN-01 | REG-FIN-06]
[REG-PROD-07]
```

A section acima tem 2 rows: a primeira com 2 cards lado a lado, a segunda com 1 card full-width.

## 5. Tipos de card

Um card e o conteudo entre separadores `|` dentro de uma row. Quatro tipos:

### 5.1 Region do catalogo

Formato: `REG-{GRUPO}-{NN}`

```
[REG-FIN-01]
[REG-EXEC-02]
```

Resolvido contra `report-regions/schemas/{group}/{slug}.md`.

### 5.2 Region com filtro de variante

Formato: `REG-ID:variant`

```
[REG-FIN-01:total]
[REG-PROD-07:in]
[REG-QUAL-01:score]
```

O filtro `:variant` aplica projecao/recorte sobre a region base — ex: renderizar apenas o "IN" de um escopo, ou apenas a nota geral de um auditor score como stat card.

Filtros disponiveis por region: ver [TODO.md](TODO.md). Filtros novos devem ser registrados la antes de serem usados em template.

### 5.3 Custom region

Formato: `CUSTOM-N`

```
[CUSTOM-1]
[CUSTOM-2]
```

Resolvido contra o bloco `## Custom Regions` do proprio template. O report-composer usa o prompt declarado para gerar o conteudo.

### 5.4 Sub-template

Formato: `SUB-NOME:variante`

```
[SUB-SCENARIO:recomendado]
[SUB-SCENARIO:enxuto]
```

Resolvido contra o bloco `## Sub-Templates`. A variante e substituida em todos os `{scenario}` do corpo do sub-template.

## 6. Interpolacao de variaveis

Sub-templates podem receber variaveis do `setup.md` via placeholder `{nome}`.

```markdown
### SUB-SCENARIO — Cenario ({scenario})

> Descritivo
[REG-FIN-07:{scenario}]
```

Quando o layout invoca `[SUB-SCENARIO:recomendado]`, o composer substitui todos os `{scenario}` por `recomendado` antes de resolver os cards.

## 7. Regras de cenarios (scenarios)

O `setup.md` pode declarar uma variavel `scenarios` por relatorio:

```markdown
- template: basic
  scenarios: [recomendado]
```

Valores validos: `all` | qualquer subconjunto de `[enxuto, recomendado, expandido]`.

**Comportamento:**

- `recomendado` **sempre** aparece **inline** na tab onde `[SUB-SCENARIO:...]` foi colocado no template
- Demais cenarios declarados em `scenarios` viram **tabs adicionais** apos a tab inline, uma por cenario, cada uma contendo um `[SUB-SCENARIO:cenario]` no mesmo ponto
- `scenarios: all` expande para todos os tres

Exemplo:

```markdown
# Tab: Cenario Recomendado
[SUB-SCENARIO:recomendado]
```

Com `scenarios: [recomendado, enxuto]`, o composer gera:

```
Tab: Cenario Recomendado  -> SUB-SCENARIO:recomendado
Tab: Cenario Enxuto       -> SUB-SCENARIO:enxuto (gerada automaticamente)
```

## 8. Gramatica resumida (EBNF informal)

```
template        = frontmatter custom-block? sub-block? layout-block
frontmatter     = "---\n" yaml "\n---"
custom-block    = "## Custom Regions\n" custom-region+
custom-region   = "### CUSTOM-" digit+ " — " title "\nPrompt: " text
sub-block       = "## Sub-Templates\n" sub-template+
sub-template    = "### SUB-" name " — " title "\n" (section)+
layout-block    = "## Layout\n" tab+
tab             = "# Tab: " name "\n" section+ ("---\n")?
section         = "> " name "\n" row+
row             = "[" card ("|" card)* "]\n"
card            = reg-card | custom-card | sub-card
reg-card        = "REG-" group "-" digit+ (":" variant)?
custom-card     = "CUSTOM-" digit+
sub-card        = "SUB-" name ":" variant
variant         = word | "{" var-name "}"
```

## 9. Convencoes auxiliares

- **Comentarios:** linhas comecando com `<!--` e terminando com `-->` sao ignoradas pelo parser
- **Whitespace:** linhas em branco entre sections/rows sao ignoradas; dentro de row de cards nao e permitido quebrar linha
- **Encoding:** UTF-8, LF
- **Ordem rigida:** `Custom Regions` antes de `Sub-Templates` antes de `Layout`
