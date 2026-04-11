---
region-id: REG-ORG-03
title: "Matriz RACI"
group: organization
description: "Matriz de responsabilidades por atividade e papel"
source: "Bloco #4 (po) → 1.4"
schema: "Matriz RACI"
template-visual: "Table com color-coded cells"
default: false
---

# Matriz RACI

Distribui responsabilidades claras para cada atividade-chave do projeto, eliminando ambiguidades sobre quem decide, quem executa e quem precisa ser informado. Fundamental para projetos com múltiplos stakeholders e equipes compartilhadas.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| atividade | string | Nome da atividade ou entrega |
| papéis | map | Para cada papel: R (Responsible), A (Accountable), C (Consulted), I (Informed) |

## Exemplo

| Atividade | PO | Tech Lead | Dev | QA | DevOps | Sponsor |
|-----------|:--:|:---------:|:---:|:--:|:------:|:-------:|
| Definição de requisitos | R | C | I | I | — | A |
| Decisão de arquitetura | C | R | C | — | C | A |
| Desenvolvimento de features | I | A | R | I | — | I |
| Code review | — | A | R | — | — | — |
| Testes de aceitação | A | I | C | R | — | I |
| Deploy em produção | I | A | C | C | R | I |
| Aprovação de go-live | C | C | — | C | I | R/A |
