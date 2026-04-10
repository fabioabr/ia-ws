# Skill Schema

Frontmatter schema for skill definition files.

## Standard

### Mandatory Fields

| Field | Type | Description |
|-------------|--------|--------------------------|
| name | string | Skill name (kebab-case) |
| description | string | One-line summary |
| version | string | `XX.YY.ZZZ` format |
| author | string | Creator or maintainer |

### Optional Fields

| Field | Type | Description |
|----------|--------|-------------------------------|
| license | string | License identifier |
| status | enum | `rascunho`, `ativo`, `arquivado`, `obsoleto` |
| category | string | Primary classification |
| tags | list | 2-5 taxonomy tags |
| inputs | list | Input parameter definitions |
| outputs | list | Output definitions |
| metadata | object | Additional key-value pairs |

### Input Fields

| Field | Type | Required | Description |
|-------------|--------|----------|-------------------------------|
| name | string | yes | Parameter name |
| type | enum | yes | See input types below |
| required | boolean| yes | Whether the input is mandatory|
| description | string | yes | What the input represents |
| default | any | no | Default value if not provided |

**Input types:** `string`, `file-path`, `number`, `boolean`, `object`, `list`

### Output Fields

| Field | Type | Required | Description |
|-------------|--------|----------|-------------------------------|
| name | string | yes | Output name |
| type | enum | yes | See output types below |
| format | string | no | Specific format details |
| description | string | yes | What the output represents |

**Output types:** `file`, `text`, `json`, `markdown`, `html`

## Example

```yaml
---
name: "validate-doc"
description: "Validates document against schema"
version: "01.00.000"
author: "team"
status: "ativo"
inputs:
  - name: "file"
    type: "file-path"
    required: true
    description: "Path to the document"
outputs:
  - name: "report"
    type: "json"
    description: "Validation results"
---
```
