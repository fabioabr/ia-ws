# template-parser

Python CLI que faz parse de um arquivo `template.md` de `report-templates/` e produz uma **AST em JSON** que o `report-composer` skill consome.

O parser **nao resolve** placeholders — apenas transforma a sintaxe do template em uma estrutura de dados navegavel. A resolucao (buscar conteudo de REG-IDs, executar prompts de CUSTOM regions, expandir sub-templates por cenario) e responsabilidade do `report-composer`.

## Usage

```
python main.py <template.md> [--format json|text] [--validate]
```

## Examples

```
python main.py ../../standards/conventions/report-templates/basic/template.md
python main.py ./template.md --format text
python main.py ./template.md --validate
```

## Output

### `--format json` (default)

Estrutura JSON com:

- `frontmatter` — dict com os metadados
- `custom_regions` — lista de `{id, title, prompt}`
- `sub_templates` — lista de `{id, title_template, sections}`
- `tabs` — lista de `{name, sections}` onde cada section tem `{name, rows}` e cada row tem `cards: [{type, id, variant}]`

### `--format text`

Dump legivel em colunas para inspecao manual.

### `--validate`

Nao emite parse. Apenas valida a sintaxe e retorna codigo 0 (ok) ou 1 (erros). Erros vao para stderr.

## Structure

- `main.py` — CLI entry point
- `models.py` — dataclasses (Template, Tab, Section, Row, Card, CustomRegion, SubTemplate)
- `parser.py` — o parser em si (line-based, stateful)
- `requirements.txt` — pyyaml

## Referencia

Sintaxe completa do template: `standards/conventions/report-templates/schemas/template-syntax.md`
