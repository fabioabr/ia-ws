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

## Representação Visual

### Dados de amostra

**Distribuição de responsabilidades por papel:**

| Papel | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|-------|:---------------:|:----------------:|:--------------:|:-------------:|
| PO | 1 | 1 | 2 | 1 |
| Tech Lead | 0 | 3 | 2 | 1 |
| Dev | 2 | 0 | 2 | 1 |
| QA | 1 | 0 | 1 | 2 |
| DevOps | 1 | 0 | 1 | 1 |
| Sponsor | 1 | 2 | 0 | 3 |

**Cobertura por atividade:** Todas as 7 atividades possuem pelo menos um R e um A atribuídos.

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo as responsabilidades de cada papel por atividade | Documentos executivos ou atas de reunião onde a matriz completa seria excessiva |
| Tabela | Matriz RACI completa com atividades nas linhas e papéis nas colunas | Referência operacional do dia a dia para consulta rápida de responsabilidades |
| Heatmap (matriz de calor) | Matriz colorida onde cada célula R/A/C/I recebe uma cor distinta, destacando concentração de responsabilidades | Apresentações visuais para identificar sobrecarga de papéis ou lacunas de cobertura |
| Gráfico de barras empilhadas | Barras por papel mostrando a proporção de R, A, C e I atribuídos | Quando é preciso comparar rapidamente a carga de responsabilidade entre papéis |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
