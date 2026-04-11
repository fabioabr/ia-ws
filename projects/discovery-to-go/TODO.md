---
title: TODO
description: Lista de pendências do projeto Discovery To Go
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: todo
area: tecnologia
tags:
  - todo
  - pendencia
created: 2026-04-11
---

# TODO — Discovery To Go

## ~~1. Consolidar os 3 packs antigos no formato único~~ DONE

Os packs `saas`, `process-documentation` e `web-microservices` foram consolidados em `discovery-blueprint.md` único. Arquivos antigos removidos.

| Pack | Arquivos atuais | Ação |
|------|----------------|------|
| `saas` | 3 separados | Consolidar em `discovery-blueprint.md` |
| `process-documentation` | 3 separados | Consolidar em `discovery-blueprint.md` |
| `web-microservices` | 3 separados | Consolidar em `discovery-blueprint.md` |

**Impacto:** `context-templates/` (global) + `base-artifacts/context-templates/` (cópia local)

---

## ~~2. Atualizar sample run para novo formato~~ DONE

Sample run atualizado — `current-context/` agora tem apenas `saas-discovery-blueprint.md`.

---

## ~~3. Terminologia "knowledge pack" → "context-template"~~ DONE

Terminologia atualizada em todos os arquivos do projeto (exceto base-artifacts/). 46 ocorrências substituídas.

---

## ~~4. Seção "Knowledge" no CLAUDE.md do workspace~~ DONE

Heading atualizado para `## Context-Templates` com descrição refletindo o formato `discovery-blueprint.md`.

---

## ~~5. Arquivo temporário do draw.io no git~~ DONE

Adicionado `.$*.bkp` e `.$*.dtmp` ao `.gitignore`.

---

## ~~6. Arquivo `product-discovery-deliverables.md`~~ DONE

Mantido em `docs/` como referência teórica para o catálogo de information regions (item 8).

---

## ~~7. README.md — seção Context-Templates desatualizada~~ DONE

Atualizado: 10 packs listados, formato documento único, multi-template, scaffold corrigido, dependências atualizadas.

---

## 8. ~~Catálogo de information regions para o delivery report~~ PARCIAL

Criar um catálogo completo de **todos os tipos de informação** que podem ser gerados num processo de discovery — independente do tipo de projeto. Cada tipo de informação será uma **region** reutilizável que aparece tanto no `.md` final quanto no `.html` visual.

### Conceito

O delivery report (`.md`) é **completo** — contém todas as informações do discovery em texto puro. O report HTML (`.html`) renderiza essas informações como **regions visuais** (cards, tabelas, diagramas, KPIs, checklists) configuráveis por projeto.

```
discovery-blueprint.md          delivery-report.md           delivery-report.html
(define quais regions)    →     (conteúdo completo)     →   (regions visuais)
       ↑                                                          ↑
custom-artifacts/                                         html-layout.md
(override por cliente)                                    (quais regions, ordem, layout)
```

### Camadas

| Camada | O que define | Quem configura |
|--------|-------------|----------------|
| **Catálogo de regions** | Todas as regions possíveis com nome, schema, template visual | Global (dtg-artifacts) |
| **Discovery blueprint** | Quais regions são relevantes para aquele tipo de projeto | Por context-template |
| **HTML layout** | Quais regions aparecem no HTML, em que ordem e com que layout | Por projeto (custom-artifacts) |
| **Delivery report (.md)** | Conteúdo completo — todas as regions com dados reais | Gerado pelo consolidator |
| **Delivery report (.html)** | Renderização visual das regions selecionadas | Gerado pelo html-writer |

### Exemplos de regions

| Categoria | Regions |
|-----------|---------|
| Executivo | Overview one-pager, Product brief, Decisão de continuidade, Próximos passos |
| Produto | Problema e contexto, Personas (JTBD), Jornadas de usuário, Proposta de valor (elevator pitch), Visão do produto, OKRs/ROI, Modelo de negócio, MVP scope (dentro/fora), Roadmap (faseamento) |
| Pesquisa | Relatório de entrevistas, Mapa de oportunidades (OST), Dados quantitativos, Citações representativas, Hipóteses não validadas |
| Organização | Mapa de stakeholders, Estrutura de equipe, RACI, Metodologia, Composição de equipe necessária, On-call, Change management |
| Técnico | Stack tecnológica, Arquitetura macro (diagrama C4 L1), Arquitetura de containers (C4 L2), Integrações, ADRs (Architecture Decision Records), Build vs Buy |
| Segurança | Classificação de dados, Criptografia (at-rest/in-transit), Autenticação/autorização, Compliance/regulação |
| Privacidade | Dados pessoais mapeados, Base legal LGPD, DPO, Política de retenção, Direito ao esquecimento, Sub-operadores |
| Financeiro | TCO 3 anos (por componente), Break-even analysis, Custo por componente/camada, Projeção de receita, Estimativa de esforço (T-shirt) |
| Riscos | Matriz de riscos (impacto x probabilidade), Risk register (score + dono + mitigação), Riscos técnicos, Hipóteses críticas em aberto |
| Qualidade | Score do auditor (5 dimensões), Questões do 10th-man, Gaps identificados, Checklist de conclusão |
| Backlog | Épicos priorizados (MoSCoW/RICE), User stories de alto nível, Dependências entre épicos, Critérios de Go/No-Go |
| Métricas | KPIs de negócio, KPIs técnicos, SLAs/SLOs, Targets por fase, DORA metrics (se platform) |
| Narrativa | Como chegamos aqui (história das iterações), Condições para prosseguir, Assinaturas de aprovação |
| Domain-specific | Modelo comercial e pricing (SaaS), Medallion architecture (datalake), Mapa de serviços (microservices), Mapa de integrações (integration), Roadmap de migração (migration), Pipeline ML (AI/ML), Estratégia mobile (mobile), Roadmap de automação (RPA/BPM), Arquitetura da plataforma (platform) |

### Referência

O documento `docs/product-discovery-deliverables.md` serve como base teórica para a definição das regions — baseado em frameworks de Marty Cagan, Teresa Torres, JTBD, C4, ADRs.

### Entregáveis

1. ~~**Catálogo de regions** (`base-artifacts/templates/report-regions/information-regions.md`) — 85 regions em 14 grupos~~ DONE
2. ~~**85 arquivos .md individuais** em `base-artifacts/templates/report-regions/{grupo}/{region}.md` — cada um com frontmatter, schema e exemplo~~ DONE
3. **Atualizar cada discovery-blueprint** para referenciar quais regions são obrigatórias/opcionais para aquele tipo de projeto
4. **`dtg-artifacts/templates/customization/html-layout.md`** — template default de layout do HTML (quais regions, ordem, grid) — customizável por projeto em `custom-artifacts/{client}/config/html-layout.md`
5. **Templates HTML por region** — componentes visuais reutilizáveis que o `html-writer` usa para renderizar cada region (card, table, KPI, diagram, checklist, etc.)
