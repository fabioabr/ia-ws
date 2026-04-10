---
title: Skill Schema
description: Esquema de frontmatter para arquivos SKILL.md — herda todos os campos do document-schema e adiciona campos específicos de skills
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: convention
area: tecnologia
tags:
  - frontmatter
  - esquema
  - skill
  - metadado
created: 2026-04-10 12:00
---

# Skill Schema

Esquema de frontmatter para arquivos `SKILL.md`. **Herda todos os campos do document-schema** e adiciona campos específicos de skills.

## Base herdada

Todo SKILL.md é um `.md` — portanto herda **todos os campos obrigatórios** de `frontmatter/document-schema.md`:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `title` | string | sim | Título da skill (= H1) |
| `description` | string | sim | O que a skill faz + trigger keywords |
| `project-name` | string | sim | Projeto a que pertence (`global` para skills globais) |
| `version` | string | sim | Formato `XX.YY.ZZZ` |
| `status` | enum | sim | `rascunho`, `ativo`, `arquivado`, `obsoleto` |
| `author` | string | sim | Quem criou/mantém |
| `category` | string | sim | Agrupamento funcional (ex: `utility`, `pipeline`) |
| `area` | string | sim | Área de conhecimento (ex: `tecnologia`, `design`) |
| `tags` | list | sim | 2-5 tags pt-BR sem acentos, kebab-case, singular |
| `created` | string | sim | Timestamp `yyyy-MM-DD HH:mm` |

## Campos adicionais de skill

Além da base herdada, SKILL.md tem campos específicos:

### Obrigatórios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | string | Identificador único da skill (kebab-case, inglês, = nome da pasta) |
| `inputs` | list | Parâmetros que a skill aceita |
| `outputs` | list | Formatos de resposta que a skill retorna |

### Opcionais

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `license` | string | Licença (ex: `MIT`, `proprietary`) |
| `metadata` | object | Campos livres específicos do projeto |

## Input fields

Cada item de `inputs` é um objeto com:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `name` | string | sim | Nome do parâmetro |
| `type` | enum | sim | `string`, `file-path`, `number`, `boolean`, `object`, `list` |
| `required` | boolean | sim | Se o input é obrigatório |
| `description` | string | sim | O que o parâmetro representa |
| `default` | any | não | Valor padrão quando não informado |

## Output fields

Cada item de `outputs` é um objeto com:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `name` | string | sim | Nome da saída |
| `type` | enum | sim | `file`, `text`, `json`, `markdown`, `html` |
| `format` | string | não | Formato específico (ex: `html`, `csv`, `drawio`) |
| `description` | string | sim | O que é retornado |

## Example

```yaml
---
name: validate-doc
title: Validate Doc
description: "Valida documento contra o schema de frontmatter. Trigger: validate, validar, schema, frontmatter."
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: utility
area: tecnologia
tags:
  - validacao
  - frontmatter
  - qualidade
created: 2026-04-10 12:00
license: MIT
inputs:
  - name: file
    type: file-path
    required: true
    description: Caminho do documento a validar
outputs:
  - name: report
    type: json
    description: Resultado da validação com status por campo
---
```
