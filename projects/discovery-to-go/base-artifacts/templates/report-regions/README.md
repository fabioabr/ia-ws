---
title: Information Regions Catalog
description: Catálogo completo de todas as regions de informação que um delivery report pode conter. Cada region é um bloco de conteúdo reutilizável com identidade, schema e template visual próprios.
project-name: discovery-to-go
version: 01.00.000
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
---

# Information Regions Catalog

Catálogo de todas as regions de informação disponíveis para o delivery report. Cada region é um **bloco de conteúdo independente** que pode aparecer tanto no `.md` (texto) quanto no `.html` (componente visual).

> [!info] Como usar este catálogo
> - O **consolidator** usa para saber quais regions gerar no `delivery-report.md` (sempre completo)
> - O **discovery-blueprint** referencia quais regions são obrigatórias/opcionais por tipo de projeto
> - O **html-layout** referencia quais regions renderizar no HTML, em que ordem e com que template visual
> - O **html-writer** usa os templates visuais para renderizar cada region selecionada

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
| Riscos | `REG-RISK` | Matriz, mitigações, hipóteses |
| Qualidade | `REG-QUAL` | Auditor, 10th-man, gaps |
| Backlog | `REG-BACK` | Épicos, stories, dependências |
| Métricas | `REG-METR` | KPIs, SLAs, targets |
| Narrativa | `REG-NARR` | História, decisões, próximos passos |
| Domínio | `REG-DOM` | Regions específicas por tipo de projeto |

### Campos de cada region

| Campo | Descrição |
|-------|-----------|
| **ID** | Identificador único (REG-GRUPO-NN) |
| **Path** | Caminho relativo ao arquivo .md da region (a partir de `report-regions/`) |
| **Nome** | Nome curto e descritivo |
| **Descrição** | O que esta region contém |
| **Fonte no pipeline** | Qual bloco/arquivo do discovery gera esta informação |
| **Schema** | Tipo de conteúdo esperado (texto, tabela, diagrama, KPI, checklist) |
| **Template visual** | Tipo de componente HTML recomendado |
| **Default** | Se aparece por default em todos os projetos ou é domain-specific |

---

## Executivo

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-EXEC-01 | `executive/overview-one-pager.md` | Overview one-pager | Resumo executivo de 1 página: problema, proposta, TCO, riscos top 3, recomendação, próximo passo | Consolidator | Texto narrativo + bullets | Hero card full-width | Todos |
| REG-EXEC-02 | `executive/product-brief.md` | Product brief | Documento de 1-2 páginas para alinhamento executivo — problema, solução, usuário-alvo, resultado esperado, MVP, investimento, recomendação | Consolidator | Texto estruturado | Card com seções | Todos |
| REG-EXEC-03 | `executive/go-no-go-decision.md` | Decisão de continuidade | Veredicto final: prosseguir / pivotar / cancelar — com evidências por risco (value, usability, feasibility, viability) e condições para prosseguir | Consolidator | Tabela de riscos + veredicto | Card com status badges | Todos |
| REG-EXEC-04 | `executive/next-steps.md` | Próximos passos | Ações imediatas pós-discovery com responsável e prazo | Consolidator | Tabela (ação, responsável, prazo) | Table com checkboxes | Todos |

---

## Produto

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-PROD-01 | `product/problem-and-context.md` | Problema e contexto | Descrição do problema, quem sofre, impacto mensurável, tamanho do problema | Bloco #1 (po) → 1.1 | Texto + métricas | Card com callout de métrica | Todos |
| REG-PROD-02 | `product/personas.md` | Personas | Perfis de usuário com JTBD, dores, ganhos esperados, comportamentos | Bloco #2 (po) → 1.2 | Lista de personas (nome, perfil, jobs, dores) | Grid de persona cards | Todos |
| REG-PROD-03 | `product/user-journeys.md` | Jornadas de usuário | Mapa de jornada por persona — passos, touchpoints, dores, oportunidades | Bloco #2 (po) → 1.2 | Diagrama de jornada ou tabela | Diagram ou stepped timeline | Opcional |
| REG-PROD-04 | `product/value-proposition.md` | Proposta de valor | Elevator pitch + diferenciação competitiva + princípios de produto | Bloco #1 (po) → 1.1 | Texto estruturado (para/que/é um/que) | Card com highlight | Todos |
| REG-PROD-05 | `product/okrs-and-roi.md` | OKRs e ROI | Objetivos mensuráveis, métricas norte, ROI esperado, critério de sucesso do MVP | Bloco #3 (po) → 1.3 | Tabela (objetivo, key result, target, prazo) | Table com progress indicators | Todos |
| REG-PROD-06 | `product/business-model.md` | Modelo de negócio | Monetização, pricing, planos, canais de distribuição | Bloco #3 (po) → 1.3 | Texto + tabela de planos | Card ou pricing table | Opcional |
| REG-PROD-07 | `product/scope.md` | Escopo | Objetivo do projeto, o que será feito (dentro), o que NÃO será feito (fora, explícito), hipótese central, critério de go/no-go | Bloco #1/#3 (po) → 1.1/1.3 | Objetivo + duas listas (dentro/fora) + hipótese | Card com objetivo + split list (in/out) | Todos |
| REG-PROD-08 | `product/roadmap.md` | Roadmap | Faseamento: MVP → Fase 2 → Fase N com épicos por fase | Bloco #3 (po) → 1.3 | Timeline de fases com épicos | Timeline horizontal | Opcional |
| REG-PROD-09 | `product/product-vision.md` | Visão do produto | Elevator pitch + horizonte de 3 anos + princípios de produto | Bloco #1 (po) → 1.1 | Texto narrativo | Card com quote style | Opcional |

---

## Pesquisa

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-PESQ-01 | `research/interview-report.md` | Relatório de entrevistas | Metodologia, perfis, achados por tema, padrões, surpresas | Interview log + Bloco #1-#4 | Texto estruturado + citações | Accordion por tema | Opcional |
| REG-PESQ-02 | `research/key-quotes.md` | Citações representativas | Quotes literais de entrevistados de alta relevância | Interview log | Lista de citações com atribuição | Blockquote cards | Opcional |
| REG-PESQ-03 | `research/opportunity-map.md` | Mapa de oportunidades | Opportunity Solution Tree: objetivo → oportunidades → soluções → experimentos | Consolidator | Diagrama hierárquico | Tree diagram (mermaid) | Opcional |
| REG-PESQ-04 | `research/quantitative-data.md` | Dados quantitativos | Fontes utilizadas, métricas-chave identificadas, tamanho do problema | Bloco #3 (po) → 1.3 | Tabela (métrica, valor, fonte) | Table com KPI highlights | Opcional |
| REG-PESQ-05 | `research/source-tag-summary.md` | Source tag summary | Distribuição das respostas por fonte: % BRIEFING, % RAG, % INFERENCE | Interview log | Tabela ou gráfico | Pie chart ou stat cards | Opcional |

---

## Organização

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-ORG-01 | `organization/stakeholder-map.md` | Mapa de stakeholders | Stakeholders com papel, influência, interesse, estratégia de engajamento | Bloco #4 (po) → 1.4 | Tabela (nome, papel, influência, interesse) | Table com badges | Todos |
| REG-ORG-02 | `organization/team-structure.md` | Estrutura de equipe | Composição do time: papéis, dedicação, fase, observações | Bloco #4 (po) → 1.4 | Tabela (papel, dedicação, fase) | Table ou org chart | Todos |
| REG-ORG-03 | `organization/raci.md` | RACI | Matriz de responsabilidades: quem é Responsible, Accountable, Consulted, Informed | Bloco #4 (po) → 1.4 | Tabela RACI | Table com color-coded cells | Opcional |
| REG-ORG-04 | `organization/methodology.md` | Metodologia | Scrum, Kanban, SAFe, Shape Up — cadência, cerimônias, ferramentas | Bloco #4 (po) → 1.4 | Texto + lista | Card simples | Opcional |
| REG-ORG-05 | `organization/oncall-and-support.md` | On-call e sustentação | Quem mantém pós-MVP, rotação, escalation, runbooks | Bloco #4 (po) → 1.4 | Texto + tabela | Card com alert style | Opcional |

---

## Técnico

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-TECH-01 | `technical/tech-stack.md` | Stack tecnológica | Linguagens, frameworks, bancos, infra — com justificativa | Bloco #5 (arch) → 1.5 | Tabela (tecnologia, camada, justificativa) | Table com badges | Todos |
| REG-TECH-02 | `technical/integrations.md` | Integrações | Sistemas integrados, protocolo, direção, volume, SLA | Bloco #5 (arch) → 1.5 | Tabela (sistema, protocolo, direção, volume) | Table ou diagram | Todos |
| REG-TECH-03 | `technical/macro-architecture.md` | Arquitetura macro | Diagrama de contexto (C4 L1) — sistema e seus vizinhos | Bloco #7 (arch) → 1.7 | Diagrama Mermaid | Diagram full-width | Todos |
| REG-TECH-04 | `technical/container-architecture.md` | Arquitetura de containers | C4 L2 — containers internos: app, API, banco, filas | Bloco #7 (arch) → 1.7 | Diagrama Mermaid | Diagram full-width | Opcional |
| REG-TECH-05 | `technical/adrs.md` | ADRs | Architecture Decision Records — decisões com contexto, alternativas, consequências | Bloco #5/#7 (arch) → 1.5/1.7 | Lista de ADRs (contexto, decisão, trade-offs) | Accordion por ADR | Opcional |
| REG-TECH-06 | `technical/build-vs-buy.md` | Build vs Buy | Análise comparativa para componentes-chave: build custom vs comprar/adotar | Bloco #8 (arch) → 1.8 | Tabela (componente, opções, veredicto, justificativa) | Table com verdict badges | Todos |
| REG-TECH-07 | `technical/non-functional-requirements.md` | Requisitos não-funcionais | Performance, disponibilidade, segurança, escalabilidade, compatibilidade | Bloco #5 (arch) → 1.5 | Tabela (categoria, requisito, valor, SLA) | Table com severity badges | Opcional |

---

## Segurança

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-SEC-01 | `security/data-classification.md` | Classificação de dados | Tipos de dados com classificação: público, interno, confidencial, restrito | Bloco #6 (cyber) → 1.6 | Tabela (dado, classificação, tratamento) | Table com color-coded badges | Todos |
| REG-SEC-02 | `security/auth.md` | Autenticação e autorização | Método de autenticação, MFA, SSO, RBAC, políticas de acesso | Bloco #5/#6 → 1.5/1.6 | Texto + tabela | Card com checklist | Todos |
| REG-SEC-03 | `security/encryption.md` | Criptografia | At-rest, in-transit, key management, BYOK | Bloco #6 (cyber) → 1.6 | Tabela (camada, método, chave) | Table simples | Opcional |
| REG-SEC-04 | `security/compliance.md` | Compliance e regulação | Regulamentações aplicáveis, gaps, ações necessárias | Bloco #6 (cyber) → 1.6 | Tabela (regulação, status, gap, ação) | Table com status badges | Todos |

---

## Privacidade

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-PRIV-01 | `privacy/personal-data-inventory.md` | Dados pessoais mapeados | Inventário de PII: quais dados, onde armazenados, quem acessa, base legal | Bloco #6 (cyber) → 1.6 | Tabela (dado, local, acesso, base legal) | Table detalhada | Quando há PII |
| REG-PRIV-02 | `privacy/legal-basis.md` | Base legal LGPD | Base legal para cada tratamento de dados pessoais (consentimento, legítimo interesse, etc.) | Bloco #6 (cyber) → 1.6 | Tabela (tratamento, base legal, justificativa) | Table com badges | Quando há PII |
| REG-PRIV-03 | `privacy/dpo.md` | DPO e responsabilidades | DPO nomeado, canal de comunicação, responsabilidades | Bloco #6 (cyber) → 1.6 | Texto + contato | Card simples | Quando há PII |
| REG-PRIV-04 | `privacy/retention-policy.md` | Política de retenção | Tempo de retenção por tipo de dado, processo de expurgo | Bloco #6 (cyber) → 1.6 | Tabela (dado, retenção, processo) | Table simples | Quando há PII |
| REG-PRIV-05 | `privacy/right-to-erasure.md` | Direito ao esquecimento | Como atender pedidos de exclusão sem quebrar referências históricas | Bloco #6 (cyber) → 1.6 | Texto + fluxo | Card com callout | Opcional |
| REG-PRIV-06 | `privacy/sub-processors.md` | Sub-operadores | Terceiros que processam dados pessoais, contratos DPA | Bloco #6 (cyber) → 1.6 | Tabela (sub-operador, dados, DPA status) | Table com status | Opcional |

---

## Financeiro

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-FIN-01 | `financial/tco-3-years.md` | TCO 3 anos | Custo total de ownership projetado em 3 anos — por categoria (equipe, infra, licenças, contingência) | Bloco #8 (arch) → 1.8 | Tabela (categoria, ano 1, ano 2, ano 3, total) + faixa de sensibilidade | Table + stat card (total) | Todos |
| REG-FIN-02 | `financial/break-even.md` | Break-even analysis | Ponto de equilíbrio: quando o investimento se paga — volume, prazo, premissas | Bloco #8 (arch) → 1.8 | Texto + número + premissas | KPI card + callout | Opcional |
| REG-FIN-03 | `financial/cost-per-component.md` | Custo por componente | Breakdown de custo por componente técnico (compute, storage, licenças, APIs) | Bloco #8 (arch) → 1.8 | Tabela (componente, custo/mês, custo/ano) | Table ou bar chart | Opcional |
| REG-FIN-04 | `financial/revenue-projection.md` | Projeção de receita | Receita projetada (se aplicável) — MRR/ARR, crescimento, churn | Bloco #3/#8 → 1.3/1.8 | Tabela de projeção mensal/anual | Table ou line chart | Quando SaaS |
| REG-FIN-05 | `financial/effort-estimation.md` | Estimativa de esforço | T-shirt sizing por épico, esforço total para MVP em sprints | Bloco #8 (arch) → 1.8 | Tabela (épico, complexidade, estimativa, premissas) | Table com badges | Todos |

---

## Riscos

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-RISK-01 | `risk/risk-matrix.md` | Matriz de riscos | Top riscos com impacto × probabilidade, classificação, mitigação, dono | Fase 2 (auditor + 10th-man) | Tabela (risco, probabilidade, impacto, score, mitigação, dono) | Table com heatmap badges | Todos |
| REG-RISK-02 | `risk/technical-risks.md` | Riscos técnicos | Riscos específicos de tecnologia com probabilidade, impacto e mitigação | Bloco #5/#7 (arch) | Tabela | Table com severity | Todos |
| REG-RISK-03 | `risk/unvalidated-hypotheses.md` | Hipóteses críticas não validadas | Premissas que ainda não foram testadas — risco se forem falsas, como validar | Fase 2 (10th-man) | Tabela (hipótese, risco se falsa, como validar, prazo) | Table com alert style | Todos |
| REG-RISK-04 | `risk/feasibility-analysis.md` | Análise de viabilidade | Veredicto por dimensão: técnica, financeira, operacional, regulatória | Consolidator | Tabela (dimensão, veredicto, justificativa) | Card com status badges | Opcional |

---

## Qualidade

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-QUAL-01 | `quality/auditor-score.md` | Score do auditor | Nota por dimensão (Cobertura, Profundidade, Consistência, Fundamentação, Completude) com pisos mínimos | Fase 2 (auditor) → 2.1 | Tabela (dimensão, nota, piso, status) | Stat cards ou radar chart | Todos |
| REG-QUAL-02 | `quality/tenth-man-questions.md` | Questões do 10th-man | Questões residuais que o 10th-man levantou mesmo com aprovação — para o cliente considerar | Fase 2 (10th-man) → 2.2 | Lista de questões com severidade | Card list com severity badges | Todos |
| REG-QUAL-03 | `quality/identified-gaps.md` | Gaps identificados | Lacunas no discovery — áreas com informação insuficiente ou inferida | Fase 2 (auditor) → 2.1 | Lista (área, gap, impacto, recomendação) | Table com alert style | Opcional |
| REG-QUAL-04 | `quality/completion-checklist.md` | Checklist de conclusão | Status de cada critério de completude do discovery | Consolidator | Checklist (item, status) | Checklist com checkmarks | Opcional |

---

## Backlog

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-BACK-01 | `backlog/prioritized-epics.md` | Épicos priorizados | Lista de épicos com priorização (MoSCoW, RICE, ou WSJF) | Consolidator | Tabela (épico, narrativa, prioridade, estimativa) | Table com priority badges | Todos |
| REG-BACK-02 | `backlog/high-level-stories.md` | User stories de alto nível | Stories por épico — sem refinamento para sprint, apenas escopo e intenção | Consolidator | Lista agrupada por épico | Accordion por épico | Opcional |
| REG-BACK-03 | `backlog/dependencies.md` | Dependências | Dependências entre épicos e com sistemas externos | Consolidator | Tabela ou diagrama | Diagram ou table | Opcional |
| REG-BACK-04 | `backlog/go-no-go-criteria.md` | Critérios de Go/No-Go | Métricas e condições que definem se o MVP avança ou pivota | Consolidator | Tabela (critério, valor-alvo, prazo) | Table com target indicators | Opcional |

---

## Métricas

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-METR-01 | `metrics/business-kpis.md` | KPIs de negócio | Métricas de sucesso do produto — ativação, retenção, NPS, receita | Bloco #3 (po) → 1.3 | Tabela (KPI, valor atual, target, prazo) | Stat cards ou table | Todos |
| REG-METR-02 | `metrics/technical-kpis.md` | KPIs técnicos | Métricas de saúde técnica — latência, uptime, MTTR, deploy frequency | Bloco #5/#7 (arch) | Tabela (KPI, valor, SLA) | Stat cards | Opcional |
| REG-METR-03 | `metrics/slas-and-slos.md` | SLAs e SLOs | Service Level Agreements/Objectives por serviço ou componente | Bloco #5 (arch) → 1.5 | Tabela (serviço, SLI, SLO, SLA) | Table com status | Opcional |
| REG-METR-04 | `metrics/targets-per-phase.md` | Targets por fase | Metas por fase do roadmap (MVP, Fase 2, etc.) | Consolidator | Tabela (fase, métrica, target) | Timeline com targets | Opcional |
| REG-METR-05 | `metrics/dora-metrics.md` | DORA metrics | Deploy frequency, lead time, MTTR, change failure rate | Bloco #5/#7 (arch) | 4 stat cards | Stat card grid | Quando platform |

---

## Narrativa

| ID | Path | Nome | Descrição | Fonte | Schema | Template visual | Default |
|----|------|------|-----------|-------|--------|-----------------|---------|
| REG-NARR-01 | `narrative/how-we-got-here.md` | Como chegamos aqui | História das iterações: quantas, onde reprovou, o que mudou, como convergiu | Pipeline-state + Consolidator | Texto narrativo + timeline | Timeline vertical | Todos |
| REG-NARR-02 | `narrative/conditions-to-proceed.md` | Condições para prosseguir | Pré-requisitos obrigatórios antes de iniciar desenvolvimento | Consolidator | Lista de condições | Checklist card | Opcional |
| REG-NARR-03 | `narrative/approval-signatures.md` | Assinaturas de aprovação | Tabela de sign-off: papel, nome, assinatura, data | Consolidator | Tabela (papel, nome, data) | Table formal | Opcional |

---

## Domain-specific

Regions que só aparecem quando o context-template correspondente está carregado:

| ID | Path | Nome | Quando | Descrição | Template visual |
|----|------|------|--------|-----------|-----------------|
| REG-DOM-SAAS-01 | `domain/saas-pricing-model.md` | Modelo comercial e pricing | `saas` | Planos, tiers, pricing strategy, MRR/ARR, trial/freemium | Pricing table |
| REG-DOM-SAAS-02 | `domain/saas-tenancy-strategy.md` | Estratégia de tenancy | `saas` | Multi-tenant approach: database/schema/row-level, isolamento, rate limiting | Card com diagrama |
| REG-DOM-DATA-01 | `domain/data-medallion-architecture.md` | Medallion architecture | `datalake-ingestion` | Diagrama Bronze → Silver → Gold com transformações, retenção, particionamento | Diagram full-width |
| REG-DOM-DATA-02 | `domain/data-quality-strategy.md` | Data quality strategy | `datalake-ingestion` | Framework de qualidade, testes por camada, freshness SLA | Table com status |
| REG-DOM-INTEG-01 | `domain/integration-map.md` | Mapa de integrações | `system-integration` | Diagrama de sistemas e fluxos com padrão, volume e SLA | Diagram full-width |
| REG-DOM-INTEG-02 | `domain/integration-data-contracts.md` | Data contracts | `system-integration` | Contratos entre sistemas: schema, versionamento, ownership | Table |
| REG-DOM-MIGR-01 | `domain/migration-roadmap.md` | Roadmap de migração | `migration-modernization` | Faseamento visual com marcos, critérios de go/no-go, timeline | Timeline horizontal |
| REG-DOM-MIGR-02 | `domain/migration-as-is-vs-to-be.md` | Comparativo AS-IS vs TO-BE | `migration-modernization` | Stack, custo, performance antes e depois | Split comparison card |
| REG-DOM-AIML-01 | `domain/aiml-strategy.md` | Estratégia de ML | `ai-ml` | Tipo de modelo, abordagem, métricas, dados, ciclo de vida | Card com pipeline diagram |
| REG-DOM-AIML-02 | `domain/aiml-model-governance.md` | Model governance | `ai-ml` | Drift detection, bias monitoring, explicabilidade, compliance | Card com checklist |
| REG-DOM-MOB-01 | `domain/mobile-strategy.md` | Estratégia mobile | `mobile-app` | Plataformas, abordagem (nativo/híbrido/PWA), features nativas, offline | Card com badges |
| REG-DOM-MOB-02 | `domain/mobile-distribution.md` | App distribution | `mobile-app` | Stores, CI/CD mobile, OTA updates, analytics, crash reporting | Table |
| REG-DOM-RPA-01 | `domain/rpa-automation-roadmap.md` | Roadmap de automação | `process-automation` | Processos priorizados, tipo de automação, ROI, timeline | Timeline com ROI |
| REG-DOM-RPA-02 | `domain/rpa-coe-governance.md` | CoE governance | `process-automation` | Center of Excellence, monitoring, manutenção, métricas de valor | Card |
| REG-DOM-PLAT-01 | `domain/platform-architecture.md` | Arquitetura da plataforma | `platform-engineering` | Cloud foundation + CI/CD + observabilidade + IDP | Diagram full-width |
| REG-DOM-PLAT-02 | `domain/platform-developer-experience.md` | Developer experience | `platform-engineering` | Golden paths, self-service, onboarding time, DX score | Stat cards |
| REG-DOM-PROC-01 | `domain/process-docs-taxonomy.md` | Taxonomia de documentos | `process-documentation` | Tipos de doc (SOP, runbook, playbook), categorização, lifecycle | Table com badges |
| REG-DOM-PROC-02 | `domain/process-docs-governance.md` | Governança de docs | `process-documentation` | RACI de manutenção, ciclo de revisão, aprovação, métricas de adoção | Card com RACI table |
| REG-DOM-MICRO-01 | `domain/microservices-service-map.md` | Mapa de serviços | `web-microservices` | Diagrama de serviços com boundaries, protocolos, ownership | Diagram full-width |
| REG-DOM-MICRO-02 | `domain/microservices-resilience.md` | Resiliência inter-serviço | `web-microservices` | Circuit breaker, retry, saga, DLQ, timeout policies | Table com patterns |

---

## Resumo quantitativo

| Grupo | Regions | Default em todos |
|-------|---------|-----------------|
| Executivo | 4 | 4 |
| Produto | 9 | 5 |
| Pesquisa | 5 | 0 |
| Organização | 5 | 2 |
| Técnico | 7 | 4 |
| Segurança | 4 | 3 |
| Privacidade | 6 | 0 (quando há PII: 4) |
| Financeiro | 5 | 2 |
| Riscos | 4 | 3 |
| Qualidade | 4 | 2 |
| Backlog | 4 | 1 |
| Métricas | 5 | 1 |
| Narrativa | 3 | 1 |
| Domain-specific | 20 | 0 (por context-template) |
| **Total** | **85** | **28 universais** |
