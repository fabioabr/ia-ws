# Document Schema

Mandatory frontmatter fields for all documents.

## Standard

All fields are **mandatory**.

| Field | Type | Description |
|--------------|--------|--------------------------------------|
| title | string | Document title (= H1) |
| description | string | One-line summary |
| project-name | string | Owning project identifier |
| version | string | `XX.YY.ZZZ` format |
| status | enum | Current lifecycle state |
| author | string | Creator or maintainer |
| category | string | Primary classification |
| area | string | Knowledge area |
| tags | list | 2-5 taxonomy tags |
| created | string | Creation timestamp |

### Status Values

`rascunho` | `ativo` | `arquivado` | `obsoleto`

### Timestamp Format

`yyyy-MM-DD HH:mm`

## Example

```yaml
---
title: "Document Management"
description: "Standards for managing project documents"
project-name: "workspace"
version: "01.00.000"
status: "ativo"
author: "team"
category: "documentacao"
area: "governanca"
tags: [documentacao, organizacao]
created: "2026-04-10 09:00"
---
```
