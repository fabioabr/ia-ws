---
title: Information Regions Catalog
description: Catálogo completo de todas as regions de informação que um delivery report pode conter. Cada region é um bloco de conteúdo reutilizável com identidade, schema e template visual próprios.
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: catalog
area: tecnologia
tags:
  - catalog
  - regions
  - delivery-report
  - html-writer
  - customization
created: 2026-04-11
updated: 2026-04-12
---

# Information Regions Catalog

Catálogo de todas as regions de informação disponíveis para o delivery report. Cada region é um **bloco de conteúdo independente** que pode aparecer tanto no `.md` (texto) quanto no `.html` (componente visual).

> [!info] Estrutura do catálogo
> - **Seção** = grupo de regions (Executivo, Produto, Financeiro, etc.)
> - **Card** = region individual dentro de um grupo, com ID, schema e template visual
> - Cada seção é separada visualmente no HTML (header + divisor)
> - Cada card é um componente independente renderizado pelo html-writer

> [!info] Como usar este catálogo
> - O **consolidator** usa para saber quais regions gerar no `delivery-report.md`
> - O **report-planner** usa para mapear regions → visualizações no `report-plan.md`
> - O **html-writer** usa os templates visuais para renderizar cada card
> - O **discovery-blueprint** referencia quais regions são obrigatórias/opcionais por tipo de projeto

---

## Convenções

### ID de region

Formato: `REG-{GRUPO}-{NN}`

| Grupo | Prefixo | Escopo |
|-------|---------|--------|
| Executivo | `REG-EXEC` | Visão de alto nível para decisores |
| Produto | `REG-PROD` | Problema, personas, valor, MVP |
| Pesquisa | `REG-PESQ` | Entrevistas, evidências, oportunidades |
| Organização | `REG-ORG` | Equipe, stakeholders, processos |
| Técnico | `REG-TECH` | Stack, arquitetura, integrações |
| Segurança | `REG-SEC` | Criptografia, autenticação, compliance |
| Privacidade | `REG-PRIV` | LGPD, dados pessoais, DPO |
| Financeiro | `REG-FIN` | TCO, break-even, custos |
| Planejamento | `REG-PLAN` | Gantt, timeline, faseamento |
| Riscos | `REG-RISK` | Matriz, mitigações, hipóteses |
| Qualidade | `REG-QUAL` | Auditor, 10th-man, gaps |
| Backlog | `REG-BACK` | Épicos, stories, dependências |
| Métricas | `REG-METR` | KPIs, SLAs, targets |
| Narrativa | `REG-NARR` | História, decisões, glossário |
| Domínio | `REG-DOM` | Regions específicas por context-template |

### Regra de renderização

```
Seção (grupo) = Section header com ícone + divisor
  └── Card 1 (region) = card-header com título + badge REG-ID + card-body com conteúdo
  └── Card 2 (region) = ...
  └── Card N (region) = ...
```

Cada card exibe o **REG-ID** como badge alinhado à direita no header.

---

## Seção 1 — Executivo (REG-EXEC)

4 cards · 4 default em todos os projetos

### Card REG-EXEC-01 — Overview One-Pager

| Campo | Valor |
|-------|-------|
| **ID** | REG-EXEC-01 |
| **Path** | `executive/overview-one-pager.md` |
| **Fonte** | Consolidator (extrai de todos os blocos) |
| **Schema** | Texto narrativo + bullets |
| **Template visual** | Hero card full-width |
| **Default** | Todos |
| **Conteúdo** | Resumo executivo de 1 página: problema, proposta, TCO, riscos top 3, recomendação, próximo passo |

### Card REG-EXEC-02 — Product Brief

| Campo | Valor |
|-------|-------|
| **ID** | REG-EXEC-02 |
| **Path** | `executive/product-brief.md` |
| **Fonte** | Consolidator |
| **Schema** | Texto estruturado |
| **Template visual** | Card com seções |
| **Default** | Todos |
| **Conteúdo** | Documento de 1-2 páginas para alinhamento executivo — problema, solução, usuário-alvo, resultado esperado, MVP, investimento, recomendação |

### Card REG-EXEC-03 — Decisão de Continuidade (Go/No-Go)

| Campo | Valor |
|-------|-------|
| **ID** | REG-EXEC-03 |
| **Path** | `executive/go-no-go-decision.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela de riscos + veredicto |
| **Template visual** | Card com status badges |
| **Default** | Todos |
| **Conteúdo** | Veredicto final: prosseguir / pivotar / cancelar — com evidências por risco (value, usability, feasibility, viability) e condições para prosseguir |

### Card REG-EXEC-04 — Próximos Passos

| Campo | Valor |
|-------|-------|
| **ID** | REG-EXEC-04 |
| **Path** | `executive/next-steps.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (ação, responsável, prazo) |
| **Template visual** | Table com checkboxes |
| **Default** | Todos |
| **Conteúdo** | Ações imediatas pós-discovery com responsável e prazo |

### Card REG-EXEC-07 — Premissas

| Campo | Valor |
|-------|-------|
| **ID** | REG-EXEC-07 |
| **Path** | `executive/premises.md` |
| **Fonte** | Consolidator (extrai de todos os blocos) |
| **Schema** | Lista de premissas com ícone de atenção |
| **Template visual** | Card com lista de bullets (HTML/CSS) |
| **Default** | Opcional |
| **Conteúdo** | Condições assumidas para as estimativas do projeto. Se qualquer premissa mudar, estimativas precisam ser recalculadas |

---

## Seção 2 — Produto (REG-PROD)

10 cards · 5 default em todos os projetos

### Card REG-PROD-01 — Problema e Contexto

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-01 |
| **Path** | `product/problem-and-context.md` |
| **Fonte** | Bloco #1 (PO) → 1.1 |
| **Schema** | Texto + métricas |
| **Template visual** | Card com callout de métrica |
| **Default** | Todos |
| **Conteúdo** | Descrição do problema, quem sofre, impacto mensurável, tamanho do problema |

### Card REG-PROD-02 — Personas

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-02 |
| **Path** | `product/personas.md` |
| **Fonte** | Bloco #2 (PO) → 1.2 |
| **Schema** | Lista de personas (nome, perfil, jobs, dores, ganhos) |
| **Template visual** | Grid de persona cards (grid-2) |
| **Default** | Todos |
| **Conteúdo** | Perfis de usuário com JTBD, dores, ganhos esperados, comportamentos. Font-size dos itens deve ser consistente com cards de escopo (`.82rem`) |

### Card REG-PROD-03 — Jornadas de Usuário

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-03 |
| **Path** | `product/user-journeys.md` |
| **Fonte** | Bloco #2 (PO) → 1.2 |
| **Schema** | Diagrama de jornada ou tabela |
| **Template visual** | Diagram ou stepped timeline |
| **Default** | Opcional |
| **Conteúdo** | Mapa de jornada por persona — passos, touchpoints, dores, oportunidades |

### Card REG-PROD-04 — Proposta de Valor

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-04 |
| **Path** | `product/value-proposition.md` |
| **Fonte** | Bloco #1 (PO) → 1.1 |
| **Schema** | Texto estruturado (para/que/é um/que) |
| **Template visual** | Card com highlight |
| **Default** | Todos |
| **Conteúdo** | Elevator pitch + diferenciação competitiva + princípios de produto |

### Card REG-PROD-05 — OKRs e ROI

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-05 |
| **Path** | `product/okrs-and-roi.md` |
| **Fonte** | Bloco #3 (PO) → 1.3 |
| **Schema** | Tabela (objetivo, key result, target, prazo) |
| **Template visual** | Table com progress indicators |
| **Default** | Todos |
| **Conteúdo** | Objetivos mensuráveis, métricas norte, ROI esperado, critério de sucesso do MVP |

### Card REG-PROD-06 — Modelo de Negócio

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-06 |
| **Path** | `product/business-model.md` |
| **Fonte** | Bloco #3 (PO) → 1.3 |
| **Schema** | Texto + tabela de planos |
| **Template visual** | Card ou pricing table (grid-3) |
| **Default** | Opcional |
| **Conteúdo** | Monetização, pricing, planos, canais de distribuição |

### Card REG-PROD-07 — Escopo (IN/OUT)

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-07 |
| **Path** | `product/scope.md` |
| **Fonte** | Bloco #1/#3 (PO) → 1.1/1.3 |
| **Schema** | Objetivo + duas listas (dentro/fora) |
| **Template visual** | Split card com duas colunas: IN (check verde) / OUT (X vermelho) |
| **Default** | Todos |
| **Conteúdo** | Objetivo do projeto, o que será feito (dentro), o que NÃO será feito (fora, explícito) |

### Card REG-PROD-08 — Roadmap

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-08 |
| **Path** | `product/roadmap.md` |
| **Fonte** | Bloco #3 (PO) → 1.3 |
| **Schema** | Timeline de fases com épicos |
| **Template visual** | Timeline horizontal (HTML/CSS) |
| **Default** | Opcional |
| **Conteúdo** | Faseamento: MVP → Fase 2 → Fase N com épicos por fase |

### Card REG-PROD-09 — Visão do Produto

| Campo | Valor |
|-------|-------|
| **ID** | REG-PROD-09 |
| **Path** | `product/product-vision.md` |
| **Fonte** | Bloco #1 (PO) → 1.1 |
| **Schema** | Texto narrativo |
| **Template visual** | Card com quote style |
| **Default** | Opcional |
| **Conteúdo** | Elevator pitch + horizonte de 3 anos + princípios de produto |

### Card REG-PLAN-01 — Gantt Relativo

| Campo | Valor |
|-------|-------|
| **ID** | REG-PLAN-01 |
| **Path** | `product/gantt-relative.md` |
| **Fonte** | Consolidator + Backlog |
| **Schema** | Barras horizontais com grid de semanas |
| **Template visual** | Gantt horizontal (HTML/CSS puro) + tabela de detalhamento (Épico, Descrição, Semanas, Horas, Dependências) |
| **Default** | Opcional |
| **Conteúdo** | Gantt chart com timeline relativa (Semana 1, 2, ..., N) — sem datas fixas. Obrigatório: tabela abaixo do grid com detalhamento de cada linha |

---

## Seção 3 — Pesquisa (REG-PESQ)

5 cards · 0 default (todos opcionais)

### Card REG-PESQ-01 — Relatório de Entrevistas

| Campo | Valor |
|-------|-------|
| **ID** | REG-PESQ-01 |
| **Path** | `research/interview-report.md` |
| **Fonte** | Interview log + Bloco #1-#4 |
| **Schema** | Texto estruturado + citações |
| **Template visual** | Accordion por tema |
| **Default** | Opcional |
| **Conteúdo** | Metodologia, perfis, achados por tema, padrões, surpresas |

### Card REG-PESQ-02 — Citações Representativas

| Campo | Valor |
|-------|-------|
| **ID** | REG-PESQ-02 |
| **Path** | `research/key-quotes.md` |
| **Fonte** | Interview log |
| **Schema** | Lista de citações com atribuição |
| **Template visual** | Blockquote cards |
| **Default** | Opcional |
| **Conteúdo** | Quotes literais de entrevistados de alta relevância |

### Card REG-PESQ-03 — Mapa de Oportunidades

| Campo | Valor |
|-------|-------|
| **ID** | REG-PESQ-03 |
| **Path** | `research/opportunity-map.md` |
| **Fonte** | Consolidator |
| **Schema** | Diagrama hierárquico |
| **Template visual** | Tree diagram |
| **Default** | Opcional |
| **Conteúdo** | Opportunity Solution Tree: objetivo → oportunidades → soluções → experimentos |

### Card REG-PESQ-04 — Dados Quantitativos

| Campo | Valor |
|-------|-------|
| **ID** | REG-PESQ-04 |
| **Path** | `research/quantitative-data.md` |
| **Fonte** | Bloco #3 (PO) → 1.3 |
| **Schema** | Tabela (métrica, valor, fonte) |
| **Template visual** | Table com KPI highlights |
| **Default** | Opcional |
| **Conteúdo** | Fontes utilizadas, métricas-chave identificadas, tamanho do problema |

### Card REG-PESQ-05 — Source Tag Summary

| Campo | Valor |
|-------|-------|
| **ID** | REG-PESQ-05 |
| **Path** | `research/source-tag-summary.md` |
| **Fonte** | Interview log |
| **Schema** | Tabela ou gráfico |
| **Template visual** | Pie chart (Chart.js) ou stat cards |
| **Default** | Opcional |
| **Conteúdo** | Distribuição das respostas por fonte: % BRIEFING, % RAG, % INFERENCE |

---

## Seção 4 — Organização (REG-ORG)

5 cards · 2 default em todos os projetos

### Card REG-ORG-01 — Mapa de Stakeholders

| Campo | Valor |
|-------|-------|
| **ID** | REG-ORG-01 |
| **Path** | `organization/stakeholder-map.md` |
| **Fonte** | Bloco #4 (PO) → 1.4 |
| **Schema** | Tabela (nome, papel, influência, interesse) |
| **Template visual** | Table com badges |
| **Default** | Todos |
| **Conteúdo** | Stakeholders com papel, influência, interesse, estratégia de engajamento |

### Card REG-ORG-02 — Estrutura de Equipe

| Campo | Valor |
|-------|-------|
| **ID** | REG-ORG-02 |
| **Path** | `organization/team-structure.md` |
| **Fonte** | Bloco #4 (PO) → 1.4 |
| **Schema** | Tabela (papel, dedicação, fase) |
| **Template visual** | Table ou org chart |
| **Default** | Todos |
| **Conteúdo** | Composição do time: papéis, dedicação, fase, horas/semana |

### Card REG-ORG-03 — RACI

| Campo | Valor |
|-------|-------|
| **ID** | REG-ORG-03 |
| **Path** | `organization/raci.md` |
| **Fonte** | Bloco #4 (PO) → 1.4 |
| **Schema** | Tabela RACI |
| **Template visual** | Table com color-coded cells (heatmap) |
| **Default** | Opcional |
| **Conteúdo** | Matriz de responsabilidades: quem é Responsible, Accountable, Consulted, Informed |

### Card REG-ORG-04 — Metodologia

| Campo | Valor |
|-------|-------|
| **ID** | REG-ORG-04 |
| **Path** | `organization/methodology.md` |
| **Fonte** | Bloco #4 (PO) → 1.4 |
| **Schema** | Texto + lista |
| **Template visual** | Card simples |
| **Default** | Opcional |
| **Conteúdo** | Scrum, Kanban, SAFe, Shape Up — cadência, cerimônias, ferramentas |

### Card REG-ORG-05 — On-call e Sustentação

| Campo | Valor |
|-------|-------|
| **ID** | REG-ORG-05 |
| **Path** | `organization/oncall-and-support.md` |
| **Fonte** | Bloco #4 (PO) → 1.4 |
| **Schema** | Texto + tabela |
| **Template visual** | Card com alert style |
| **Default** | Opcional |
| **Conteúdo** | Quem mantém pós-MVP, rotação, escalation, runbooks |

---

## Seção 5 — Técnico (REG-TECH)

7 cards · 4 default em todos os projetos

### Card REG-TECH-01 — Stack Tecnológica

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-01 |
| **Path** | `technical/tech-stack.md` |
| **Fonte** | Bloco #5 (Solution Architect) → 1.5 |
| **Schema** | Tabela (tecnologia, camada, justificativa) |
| **Template visual** | Table com badges |
| **Default** | Todos |
| **Conteúdo** | Linguagens, frameworks, bancos, infra — com justificativa para cada escolha |

### Card REG-TECH-02 — Integrações

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-02 |
| **Path** | `technical/integrations.md` |
| **Fonte** | Bloco #5 (Solution Architect) → 1.5 |
| **Schema** | Tabela (sistema, protocolo, direção, volume) |
| **Template visual** | Table ou diagram |
| **Default** | Todos |
| **Conteúdo** | Sistemas integrados, protocolo, direção, volume, SLA |

### Card REG-TECH-03 — Arquitetura Macro (C4 L1)

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-03 |
| **Path** | `technical/macro-architecture.md` |
| **Fonte** | Bloco #7 (Solution Architect) → 1.7 |
| **Schema** | Diagrama de contexto |
| **Template visual** | Diagram full-width |
| **Default** | Todos |
| **Conteúdo** | Diagrama C4 Level 1 — sistema e seus vizinhos |

### Card REG-TECH-04 — Arquitetura de Containers (C4 L2)

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-04 |
| **Path** | `technical/container-architecture.md` |
| **Fonte** | Bloco #7 (Solution Architect) → 1.7 |
| **Schema** | Diagrama de containers |
| **Template visual** | Diagram full-width |
| **Default** | Opcional |
| **Conteúdo** | C4 Level 2 — containers internos: app, API, banco, filas |

### Card REG-TECH-05 — ADRs (Architecture Decision Records)

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-05 |
| **Path** | `technical/adrs.md` |
| **Fonte** | Bloco #5/#7 (Solution Architect) → 1.5/1.7 |
| **Schema** | Lista de ADRs (contexto, decisão, trade-offs) |
| **Template visual** | Accordion por ADR |
| **Default** | Opcional |
| **Conteúdo** | Architecture Decision Records — decisões com contexto, alternativas, consequências |

### Card REG-TECH-06 — Build vs Buy

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-06 |
| **Path** | `technical/build-vs-buy.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Tabela (capacidade, decisão, solução, justificativa) |
| **Template visual** | Table com coluna "Decisão" separada: badges BUILD (green), BUY (blue), HYBRID (yellow) |
| **Default** | Todos |
| **Conteúdo** | Análise comparativa para componentes-chave: build custom vs comprar/adotar |

### Card REG-TECH-07 — Requisitos Não-Funcionais

| Campo | Valor |
|-------|-------|
| **ID** | REG-TECH-07 |
| **Path** | `technical/non-functional-requirements.md` |
| **Fonte** | Bloco #5 (Solution Architect) → 1.5 |
| **Schema** | Tabela (categoria, requisito, valor, SLA) |
| **Template visual** | Table com severity badges |
| **Default** | Opcional |
| **Conteúdo** | Performance, disponibilidade, segurança, escalabilidade, compatibilidade |

---

## Seção 6 — Segurança (REG-SEC)

4 cards · 3 default em todos os projetos

### Card REG-SEC-01 — Classificação de Dados

| Campo | Valor |
|-------|-------|
| **ID** | REG-SEC-01 |
| **Path** | `security/data-classification.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (dado, classificação, tratamento) |
| **Template visual** | Table com color-coded badges |
| **Default** | Todos |
| **Conteúdo** | Tipos de dados com classificação: público, interno, confidencial, restrito |

### Card REG-SEC-02 — Autenticação e Autorização

| Campo | Valor |
|-------|-------|
| **ID** | REG-SEC-02 |
| **Path** | `security/auth.md` |
| **Fonte** | Bloco #5/#6 → 1.5/1.6 |
| **Schema** | Texto + tabela |
| **Template visual** | Card com checklist |
| **Default** | Todos |
| **Conteúdo** | Método de autenticação, MFA, SSO, RBAC, políticas de acesso |

### Card REG-SEC-03 — Criptografia

| Campo | Valor |
|-------|-------|
| **ID** | REG-SEC-03 |
| **Path** | `security/encryption.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (camada, método, chave) |
| **Template visual** | Table simples |
| **Default** | Opcional |
| **Conteúdo** | At-rest, in-transit, key management, BYOK |

### Card REG-SEC-04 — Compliance e Regulação

| Campo | Valor |
|-------|-------|
| **ID** | REG-SEC-04 |
| **Path** | `security/compliance.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (regulação, status, gap, ação) |
| **Template visual** | Table com status badges |
| **Default** | Todos |
| **Conteúdo** | Regulamentações aplicáveis, gaps, ações necessárias |

---

## Seção 7 — Privacidade (REG-PRIV)

6 cards · 0 default (4 quando há PII)

### Card REG-PRIV-01 — Dados Pessoais Mapeados

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-01 |
| **Path** | `privacy/personal-data-inventory.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (dado, local, acesso, base legal) |
| **Template visual** | Table detalhada |
| **Default** | Quando há PII |
| **Conteúdo** | Inventário de PII: quais dados, onde armazenados, quem acessa, base legal |

### Card REG-PRIV-02 — Base Legal LGPD

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-02 |
| **Path** | `privacy/legal-basis.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (tratamento, base legal, justificativa) |
| **Template visual** | Table com badges |
| **Default** | Quando há PII |
| **Conteúdo** | Base legal para cada tratamento de dados pessoais |

### Card REG-PRIV-03 — DPO e Responsabilidades

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-03 |
| **Path** | `privacy/dpo.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Texto + contato |
| **Template visual** | Card simples |
| **Default** | Quando há PII |
| **Conteúdo** | DPO nomeado, canal de comunicação, responsabilidades |

### Card REG-PRIV-04 — Política de Retenção

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-04 |
| **Path** | `privacy/retention-policy.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (dado, retenção, processo) |
| **Template visual** | Table simples |
| **Default** | Quando há PII |
| **Conteúdo** | Tempo de retenção por tipo de dado, processo de expurgo |

### Card REG-PRIV-05 — Direito ao Esquecimento

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-05 |
| **Path** | `privacy/right-to-erasure.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Texto + fluxo |
| **Template visual** | Card com callout |
| **Default** | Opcional |
| **Conteúdo** | Como atender pedidos de exclusão sem quebrar referências históricas |

### Card REG-PRIV-06 — Sub-operadores

| Campo | Valor |
|-------|-------|
| **ID** | REG-PRIV-06 |
| **Path** | `privacy/sub-processors.md` |
| **Fonte** | Bloco #6 (Cyber-Security Architect) → 1.6 |
| **Schema** | Tabela (sub-operador, dados, DPA status) |
| **Template visual** | Table com status |
| **Default** | Opcional |
| **Conteúdo** | Terceiros que processam dados pessoais, contratos DPA |

---

## Seção 8 — Financeiro (REG-FIN)

7 cards · 2 default em todos os projetos

### Card REG-FIN-01 — TCO 3 Anos

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-01 |
| **Path** | `financial/tco-3-years.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Tabela (categoria, ano 1, ano 2, ano 3, total) + faixa de sensibilidade |
| **Template visual** | Table + stat card (total) |
| **Default** | Todos |
| **Conteúdo** | Custo total de ownership projetado em 3 anos — por categoria (equipe, infra, licenças, contingência) |

### Card REG-FIN-02 — Break-even Analysis

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-02 |
| **Path** | `financial/break-even.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Texto + número + premissas |
| **Template visual** | KPI card + callout |
| **Default** | Opcional |
| **Conteúdo** | Ponto de equilíbrio: quando o investimento se paga — volume, prazo, premissas |

### Card REG-FIN-03 — Custo por Componente

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-03 |
| **Path** | `financial/cost-per-component.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Tabela (componente, custo/mês, custo/ano) |
| **Template visual** | Table ou horizontal bar chart (HTML/CSS) |
| **Default** | Opcional |
| **Conteúdo** | Breakdown de custo por componente técnico (compute, storage, licenças, APIs) |

### Card REG-FIN-04 — Projeção de Receita

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-04 |
| **Path** | `financial/revenue-projection.md` |
| **Fonte** | Bloco #3/#8 → 1.3/1.8 |
| **Schema** | Tabela de projeção mensal/anual |
| **Template visual** | Table ou line chart (Chart.js) |
| **Default** | Quando SaaS |
| **Conteúdo** | Receita projetada — MRR/ARR, crescimento, churn |

### Card REG-FIN-05 — Estimativa de Esforço

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-05 |
| **Path** | `financial/effort-estimation.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Tabela (épico, complexidade, estimativa, premissas) |
| **Template visual** | Table com badges |
| **Default** | Todos |
| **Conteúdo** | T-shirt sizing por épico, esforço total para MVP em sprints |

### Card REG-FIN-06 — Total Hours (Stat Cards)

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-06 |
| **Path** | `financial/total-hours.md` |
| **Fonte** | Consolidator |
| **Schema** | Stat cards com horas por papel + total geral |
| **Template visual** | Stat cards grid-3 (HTML/CSS) |
| **Default** | Opcional |
| **Conteúdo** | Resumo de horas totais por papel e total geral — usado no essential/one-pager |

### Card REG-FIN-07 — Cenários Financeiros

| Campo | Valor |
|-------|-------|
| **ID** | REG-FIN-07 |
| **Path** | `financial/financial-scenarios.md` |
| **Fonte** | Bloco #8 (Solution Architect) → 1.8 |
| **Schema** | Tabela comparativa + horizontal bars |
| **Template visual** | Table + horizontal bars (HTML/CSS) |
| **Default** | Opcional |
| **Conteúdo** | Cenários financeiros alternativos quando o cenário base é inviável — comparativo de TCO, receita, break-even |

---

## Seção 9 — Riscos (REG-RISK)

4 cards · 3 default em todos os projetos

### Card REG-RISK-01 — Matriz de Riscos

| Campo | Valor |
|-------|-------|
| **ID** | REG-RISK-01 |
| **Path** | `risk/risk-matrix.md` |
| **Fonte** | Fase 2 (Auditor + 10th-man) |
| **Schema** | Tabela (risco, probabilidade, impacto, score, mitigação, dono) |
| **Template visual** | Table com heatmap badges de severidade |
| **Default** | Todos |
| **Conteúdo** | Top riscos com impacto × probabilidade, classificação, mitigação detalhada (5 campos), dono |

### Card REG-RISK-02 — Riscos Técnicos

| Campo | Valor |
|-------|-------|
| **ID** | REG-RISK-02 |
| **Path** | `risk/technical-risks.md` |
| **Fonte** | Bloco #5/#7 (Solution Architect) |
| **Schema** | Tabela |
| **Template visual** | Table com severity badges |
| **Default** | Todos |
| **Conteúdo** | Riscos específicos de tecnologia com probabilidade, impacto e mitigação |

### Card REG-RISK-03 — Hipóteses Não Validadas

| Campo | Valor |
|-------|-------|
| **ID** | REG-RISK-03 |
| **Path** | `risk/unvalidated-hypotheses.md` |
| **Fonte** | Fase 2 (10th-man) |
| **Schema** | Tabela (hipótese, risco se falsa, como validar, prazo) |
| **Template visual** | Table com alert style |
| **Default** | Todos |
| **Conteúdo** | Premissas que ainda não foram testadas — risco se forem falsas, como validar |

### Card REG-RISK-04 — Análise de Viabilidade

| Campo | Valor |
|-------|-------|
| **ID** | REG-RISK-04 |
| **Path** | `risk/feasibility-analysis.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (dimensão, veredicto, justificativa) |
| **Template visual** | Card com status badges |
| **Default** | Opcional |
| **Conteúdo** | Veredicto por dimensão: técnica, financeira, operacional, regulatória |

---

## Seção 10 — Qualidade (REG-QUAL)

4 cards · 2 default em todos os projetos

### Card REG-QUAL-01 — Score do Auditor

| Campo | Valor |
|-------|-------|
| **ID** | REG-QUAL-01 |
| **Path** | `quality/auditor-score.md` |
| **Fonte** | Fase 2 (Auditor) → 2.1 |
| **Schema** | Tabela (dimensão, nota, piso, status) |
| **Template visual** | Radar chart (Chart.js) com zones coloridas + stat card de score geral |
| **Default** | Todos |
| **Conteúdo** | Nota por dimensão (Cobertura, Profundidade, Consistência, Fundamentação, Completude) com pisos mínimos. Radar com faixas verde/amarelo/vermelho |

### Card REG-QUAL-02 — Ressalvas do 10th-man

| Campo | Valor |
|-------|-------|
| **ID** | REG-QUAL-02 |
| **Path** | `quality/tenth-man-questions.md` |
| **Fonte** | Fase 2 (10th-man) → 2.2 |
| **Schema** | Lista de questões com severidade |
| **Template visual** | Radar chart 3 eixos (Chart.js) + caveat cards com 5 campos (title, dimension, description, why_important, recommendation) |
| **Default** | Todos |
| **Conteúdo** | Questões residuais que o 10th-man levantou. Cada ressalva tem badge CRITICAL/IMPORTANT e 5 campos obrigatórios |

### Card REG-QUAL-03 — Gaps Identificados

| Campo | Valor |
|-------|-------|
| **ID** | REG-QUAL-03 |
| **Path** | `quality/identified-gaps.md` |
| **Fonte** | Fase 2 (Auditor) → 2.1 |
| **Schema** | Lista (área, gap, impacto, recomendação) |
| **Template visual** | Table com alert style |
| **Default** | Opcional |
| **Conteúdo** | Lacunas no discovery — áreas com informação insuficiente ou inferida |

### Card REG-QUAL-04 — Checklist de Conclusão

| Campo | Valor |
|-------|-------|
| **ID** | REG-QUAL-04 |
| **Path** | `quality/completion-checklist.md` |
| **Fonte** | Consolidator |
| **Schema** | Checklist (item, status) |
| **Template visual** | Checklist com checkmarks |
| **Default** | Opcional |
| **Conteúdo** | Status de cada critério de completude do discovery |

---

## Seção 11 — Backlog (REG-BACK)

4 cards · 1 default em todos os projetos

### Card REG-BACK-01 — Épicos Priorizados

| Campo | Valor |
|-------|-------|
| **ID** | REG-BACK-01 |
| **Path** | `backlog/prioritized-epics.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (épico, narrativa, prioridade, estimativa) |
| **Template visual** | Table com priority badges (MoSCoW) |
| **Default** | Todos |
| **Conteúdo** | Lista de épicos com priorização MoSCoW, RICE ou WSJF |

### Card REG-BACK-02 — User Stories de Alto Nível

| Campo | Valor |
|-------|-------|
| **ID** | REG-BACK-02 |
| **Path** | `backlog/high-level-stories.md` |
| **Fonte** | Consolidator |
| **Schema** | Lista agrupada por épico |
| **Template visual** | Accordion por épico |
| **Default** | Opcional |
| **Conteúdo** | Stories por épico — sem refinamento para sprint, apenas escopo e intenção |

### Card REG-BACK-03 — Dependências

| Campo | Valor |
|-------|-------|
| **ID** | REG-BACK-03 |
| **Path** | `backlog/dependencies.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela ou diagrama |
| **Template visual** | Diagram ou table |
| **Default** | Opcional |
| **Conteúdo** | Dependências entre épicos e com sistemas externos |

### Card REG-BACK-04 — Critérios de Go/No-Go

| Campo | Valor |
|-------|-------|
| **ID** | REG-BACK-04 |
| **Path** | `backlog/go-no-go-criteria.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (critério, valor-alvo, prazo) |
| **Template visual** | Table com target indicators |
| **Default** | Opcional |
| **Conteúdo** | Métricas e condições que definem se o MVP avança ou pivota |

---

## Seção 12 — Métricas (REG-METR)

5 cards · 1 default em todos os projetos

### Card REG-METR-01 — KPIs de Negócio

| Campo | Valor |
|-------|-------|
| **ID** | REG-METR-01 |
| **Path** | `metrics/business-kpis.md` |
| **Fonte** | Bloco #3 (PO) → 1.3 |
| **Schema** | Tabela (KPI, valor atual, target, prazo) |
| **Template visual** | Stat cards ou table |
| **Default** | Todos |
| **Conteúdo** | Métricas de sucesso do produto — ativação, retenção, NPS, receita |

### Card REG-METR-02 — KPIs Técnicos

| Campo | Valor |
|-------|-------|
| **ID** | REG-METR-02 |
| **Path** | `metrics/technical-kpis.md` |
| **Fonte** | Bloco #5/#7 (Solution Architect) |
| **Schema** | Tabela (KPI, valor, SLA) |
| **Template visual** | Stat cards |
| **Default** | Opcional |
| **Conteúdo** | Métricas de saúde técnica — latência, uptime, MTTR, deploy frequency |

### Card REG-METR-03 — SLAs e SLOs

| Campo | Valor |
|-------|-------|
| **ID** | REG-METR-03 |
| **Path** | `metrics/slas-and-slos.md` |
| **Fonte** | Bloco #5 (Solution Architect) → 1.5 |
| **Schema** | Tabela (serviço, SLI, SLO, SLA) |
| **Template visual** | Table com status |
| **Default** | Opcional |
| **Conteúdo** | Service Level Agreements/Objectives por serviço ou componente |

### Card REG-METR-04 — Targets por Fase

| Campo | Valor |
|-------|-------|
| **ID** | REG-METR-04 |
| **Path** | `metrics/targets-per-phase.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (fase, métrica, target) |
| **Template visual** | Timeline com targets |
| **Default** | Opcional |
| **Conteúdo** | Metas por fase do roadmap (MVP, Fase 2, etc.) |

### Card REG-METR-05 — DORA Metrics

| Campo | Valor |
|-------|-------|
| **ID** | REG-METR-05 |
| **Path** | `metrics/dora-metrics.md` |
| **Fonte** | Bloco #5/#7 (Solution Architect) |
| **Schema** | 4 stat cards |
| **Template visual** | Stat card grid |
| **Default** | Quando platform |
| **Conteúdo** | Deploy frequency, lead time, MTTR, change failure rate |

---

## Seção 13 — Narrativa (REG-NARR)

4 cards · 1 default em todos os projetos

### Card REG-NARR-01 — Como Chegamos Aqui

| Campo | Valor |
|-------|-------|
| **ID** | REG-NARR-01 |
| **Path** | `narrative/how-we-got-here.md` |
| **Fonte** | Pipeline-state + Consolidator |
| **Schema** | Texto narrativo + timeline |
| **Template visual** | Timeline vertical ou card com tabela comparativa (Briefing Original vs Após Discovery) |
| **Default** | Todos |
| **Conteúdo** | História das iterações: quantas, onde reprovou, o que mudou, como convergiu |

### Card REG-NARR-02 — Condições para Prosseguir

| Campo | Valor |
|-------|-------|
| **ID** | REG-NARR-02 |
| **Path** | `narrative/conditions-to-proceed.md` |
| **Fonte** | Consolidator |
| **Schema** | Lista de condições |
| **Template visual** | Checklist card |
| **Default** | Opcional |
| **Conteúdo** | Pré-requisitos obrigatórios antes de iniciar desenvolvimento |

### Card REG-NARR-03 — Assinaturas de Aprovação

| Campo | Valor |
|-------|-------|
| **ID** | REG-NARR-03 |
| **Path** | `narrative/approval-signatures.md` |
| **Fonte** | Consolidator |
| **Schema** | Tabela (papel, nome, data) |
| **Template visual** | Table formal |
| **Default** | Opcional |
| **Conteúdo** | Tabela de sign-off: papel, nome, assinatura, data |

### Card REG-NARR-04 — Glossário

| Campo | Valor |
|-------|-------|
| **ID** | REG-NARR-04 |
| **Path** | `narrative/glossary.md` |
| **Fonte** | Consolidator + acronym-bank.md |
| **Schema** | Tabela alfabética (sigla, expansão, contexto) |
| **Template visual** | Table com filtro de busca inline |
| **Default** | Todos (quando há `<abbr>` tooltips) |
| **Conteúdo** | Glossário completo de siglas e termos técnicos usados no relatório |

---

## Seção 14 — Domain-specific (REG-DOM)

20 cards · 0 default (ativados por context-template)

### Card REG-DOM-SAAS-01 — Modelo Comercial e Pricing
- **Context-template:** `saas`
- **Template visual:** Pricing table (grid-3)
- **Conteúdo:** Planos, tiers, pricing strategy, MRR/ARR, trial/freemium

### Card REG-DOM-SAAS-02 — Estratégia de Tenancy
- **Context-template:** `saas`
- **Template visual:** Card com diagrama
- **Conteúdo:** Multi-tenant approach: database/schema/row-level, isolamento, rate limiting

### Card REG-DOM-DATA-01 — Medallion Architecture
- **Context-template:** `datalake-ingestion`
- **Template visual:** Diagram full-width
- **Conteúdo:** Diagrama Bronze → Silver → Gold com transformações, retenção, particionamento

### Card REG-DOM-DATA-02 — Data Quality Strategy
- **Context-template:** `datalake-ingestion`
- **Template visual:** Table com status
- **Conteúdo:** Framework de qualidade, testes por camada, freshness SLA

### Card REG-DOM-INTEG-01 — Mapa de Integrações
- **Context-template:** `system-integration`
- **Template visual:** Diagram full-width
- **Conteúdo:** Diagrama de sistemas e fluxos com padrão, volume e SLA

### Card REG-DOM-INTEG-02 — Data Contracts
- **Context-template:** `system-integration`
- **Template visual:** Table
- **Conteúdo:** Contratos entre sistemas: schema, versionamento, ownership

### Card REG-DOM-MIGR-01 — Roadmap de Migração
- **Context-template:** `migration-modernization`
- **Template visual:** Timeline horizontal
- **Conteúdo:** Faseamento visual com marcos, critérios de go/no-go, timeline

### Card REG-DOM-MIGR-02 — Comparativo AS-IS vs TO-BE
- **Context-template:** `migration-modernization`
- **Template visual:** Split comparison card
- **Conteúdo:** Stack, custo, performance antes e depois

### Card REG-DOM-AIML-01 — Estratégia de ML
- **Context-template:** `ai-ml`
- **Template visual:** Card com pipeline diagram
- **Conteúdo:** Tipo de modelo, abordagem, métricas, dados, ciclo de vida

### Card REG-DOM-AIML-02 — Model Governance
- **Context-template:** `ai-ml`
- **Template visual:** Card com checklist
- **Conteúdo:** Drift detection, bias monitoring, explicabilidade, compliance

### Card REG-DOM-MOB-01 — Estratégia Mobile
- **Context-template:** `mobile-app`
- **Template visual:** Card com badges
- **Conteúdo:** Plataformas, abordagem (nativo/híbrido/PWA), features nativas, offline

### Card REG-DOM-MOB-02 — App Distribution
- **Context-template:** `mobile-app`
- **Template visual:** Table
- **Conteúdo:** Stores, CI/CD mobile, OTA updates, analytics, crash reporting

### Card REG-DOM-RPA-01 — Roadmap de Automação
- **Context-template:** `process-automation`
- **Template visual:** Timeline com ROI
- **Conteúdo:** Processos priorizados, tipo de automação, ROI, timeline

### Card REG-DOM-RPA-02 — CoE Governance
- **Context-template:** `process-automation`
- **Template visual:** Card
- **Conteúdo:** Center of Excellence, monitoring, manutenção, métricas de valor

### Card REG-DOM-PLAT-01 — Arquitetura da Plataforma
- **Context-template:** `platform-engineering`
- **Template visual:** Diagram full-width
- **Conteúdo:** Cloud foundation + CI/CD + observabilidade + IDP

### Card REG-DOM-PLAT-02 — Developer Experience
- **Context-template:** `platform-engineering`
- **Template visual:** Stat cards
- **Conteúdo:** Golden paths, self-service, onboarding time, DX score

### Card REG-DOM-PROC-01 — Taxonomia de Documentos
- **Context-template:** `process-documentation`
- **Template visual:** Table com badges
- **Conteúdo:** Tipos de doc (SOP, runbook, playbook), categorização, lifecycle

### Card REG-DOM-PROC-02 — Governança de Docs
- **Context-template:** `process-documentation`
- **Template visual:** Card com RACI table
- **Conteúdo:** RACI de manutenção, ciclo de revisão, aprovação, métricas de adoção

### Card REG-DOM-MICRO-01 — Mapa de Serviços
- **Context-template:** `web-microservices`
- **Template visual:** Diagram full-width
- **Conteúdo:** Diagrama de serviços com boundaries, protocolos, ownership

### Card REG-DOM-MICRO-02 — Resiliência Inter-serviço
- **Context-template:** `web-microservices`
- **Template visual:** Table com patterns
- **Conteúdo:** Circuit breaker, retry, saga, DLQ, timeout policies

---

## Resumo Quantitativo

| # | Seção | Cards | Default |
|---|-------|-------|---------|
| 1 | Executivo | 5 | 4 |
| 2 | Produto | 10 | 5 |
| 3 | Pesquisa | 5 | 0 |
| 4 | Organização | 5 | 2 |
| 5 | Técnico | 7 | 4 |
| 6 | Segurança | 4 | 3 |
| 7 | Privacidade | 6 | 0 (4 com PII) |
| 8 | Financeiro | 7 | 2 |
| 9 | Riscos | 4 | 3 |
| 10 | Qualidade | 4 | 2 |
| 11 | Backlog | 4 | 1 |
| 12 | Métricas | 5 | 1 |
| 13 | Narrativa | 4 | 2 |
| 14 | Domain-specific | 20 | 0 (por template) |
| | **Total** | **90** | **29 universais** |
