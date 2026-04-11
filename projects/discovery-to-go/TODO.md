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

## 6. Arquivo `product-discovery-deliverables.md`

`docs/product-discovery-deliverables.md` — arquivo untracked. Precisa ser commitado ou descartado.

---

## 7. README.md — seção Context-Templates desatualizada

Menciona "até 4 arquivos" por pack e lista apenas 4 packs. Agora são 10 packs e o formato é documento único. Atualizar.

---

## 8. Catálogo de information cards para o delivery report

Criar um catálogo completo de **todos os tipos de informação** que podem ser gerados num processo de discovery — independente do tipo de projeto. Cada tipo de informação será um **card** reutilizável (como componentes de um dashboard).

**Objetivo:** permitir que os report-profiles dos blueprints referenciem quais cards incluir no delivery report, e que o `html-writer` renderize cada card com um template visual próprio (layout, ícones, cores, formatação).

**Exemplos de cards:**

| Categoria | Cards |
|-----------|-------|
| Produto | Problema e contexto, Personas, Jornadas de usuário, Proposta de valor, OKRs/ROI, Modelo de negócio, MVP scope, Roadmap |
| Organização | Stakeholders, Estrutura de equipe, RACI, Metodologia, On-call, Change management |
| Técnico | Stack tecnológica, Arquitetura macro (diagrama), Integrações, Decisões arquiteturais (ADRs), Build vs Buy |
| Segurança | Classificação de dados, Criptografia, Autenticação/autorização, Compliance/regulação |
| Privacidade | Dados pessoais mapeados, Base legal LGPD, DPO, Retenção, Direito ao esquecimento |
| Financeiro | TCO 3 anos, Break-even, Custo por componente, Projeção de receita |
| Riscos | Matriz de riscos (impacto x probabilidade), Mitigações, Riscos residuais |
| Qualidade | Score do auditor (5 dimensões), Questões do 10th-man, Gaps identificados |
| Backlog | Épicos priorizados (MoSCoW/RICE), User stories MVP, Dependências |
| Métricas | KPIs de negócio, KPIs técnicos, SLAs, Targets |
| Narrativa | Overview executivo (one-pager), Como chegamos aqui, Próximos passos |

**Entregáveis:**
1. `catalog/information-cards.md` — catálogo completo de cards com nome, descrição, schema de dados, exemplo
2. Cada blueprint referencia quais cards são relevantes para aquele tipo de projeto
3. No futuro: templates HTML por card (componentes visuais reutilizáveis para o `html-writer`)
