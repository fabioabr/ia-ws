---
title: "Priorização de Perguntas por Entregável"
description: "Classifica cada pergunta do environment.md por entregável (One-Pager, Executive, Delivery) e mapeia para as regions do report correspondente."
category: knowledge-base
type: question-priority
status: ativo
company: "Patria"
last-updated: "2026-04-17"
source: "Derivado de environment.md (10 domínios, 564 checkboxes) + base/standards/conventions/report-regions/schemas/ (15 regions)"
---

# Priorização de Perguntas por Entregável — Patria

> Este documento responde: **"Para gerar o One-Pager, preciso responder tudo?"** Não. Cada entregável tem um subconjunto mínimo de perguntas do `environment.md` que precisa estar respondido para ser útil. Este arquivo mapeia quais perguntas alimentam quais entregáveis.

---

## Legenda

Cada pergunta é marcada com um **bitmap** `[OP][EX][DR]` que indica em quais entregáveis ela é necessária.

| Tag | Entregável | Quando gerar | Audiência |
|-----|-----------|--------------|-----------|
| `[OP]` | **One-Pager** (1 página) | Aprovação executiva inicial — vai/não vai | C-Level, patrocinador |
| `[EX]` | **Executive Report** (5-15 páginas) | Comitê de investimento, decisão Go/No-Go formal | Diretoria, Legal, Compliance |
| `[DR]` | **Delivery Report** (relatório completo) | Handoff para time de execução | PMs, arquitetos, devs, ops |

### Regra de herança

**OP ⊂ EX ⊂ DR** — tudo que está no One-Pager também está no Executive e no Delivery. Tudo que está no Executive também está no Delivery. O Delivery é superconjunto.

Notação:
- `[X][X][X]` — necessário em todos os três
- `[ ][X][X]` — necessário em Executive e Delivery, opcional em One-Pager
- `[ ][ ][X]` — necessário apenas em Delivery
- `[ ][ ][ ]` — pergunta informativa, útil como RAG mas não bloqueia nenhum entregável

### Princípios de classificação

1. **One-Pager foca em ESFORÇO, CUSTO e ESCOPO.** Responde: *o que vai ser feito, quanto custa (estimativa), quanto esforço/duração*. Top 1-2 riscos e premissas-chave.
   - **NÃO entra no One-Pager:** FTE/disponibilidade real do time (assumir "todos contratados" para simplificar cálculo de esforço). ROI/payback (Discovery acontece após aprovação global do investimento; exceção: se o briefing do projeto exigir).
2. **Executive foca em CONFIANÇA.** Entra o que o comitê precisa para assinar: modelo de negócio, personas, value proposition, stakeholders, TCO resumido, matriz de riscos, compliance aplicável, metodologia, time.
3. **Delivery foca em EXECUÇÃO.** Tudo o mais: ADRs, secrets, integrações com volumes/SLA, runbooks, RACI, CI/CD, observabilidade, débito técnico detalhado.

---

## Resumo agregado

| Entregável | Regions alimentadas | Perguntas mínimas do `environment.md` | Status atual Patria |
|-----------|---------------------|--------------------------------------|---------------------|
| **One-Pager** | executive (overview-one-pager, go-no-go-decision, next-steps, premises, product-brief) | **~8 perguntas** (escopo/custo/esforço) | **100% respondido** (Abr/2026) |
| **Executive** | + product, financial, risk, organization, security (alto nível), privacy (alto nível) | **~120 perguntas** | ~30% respondido |
| **Delivery** | + technical, domain, metrics, narrative, research, backlog, quality, security (detalhe), privacy (detalhe) | **~564 perguntas (todas)** | ~11% respondido |

> **Leitura:** One-Pager da Patria está pronto para ser gerado. O One-Pager do framework Discovery-to-Go **não inclui** FTE disponível (assume-se contratação integral) nem ROI/payback (Discovery acontece após aprovação global do investimento).

---

## Mapeamento regions → arquivos-fonte

Cada region abaixo consome respostas de um ou mais domínios do `environment.md`.

| Region | Schema-base | Domínios do environment.md que alimentam |
|--------|-------------|------------------------------------------|
| `executive/overview-one-pager` | Sumário de 1 página | D01 (cloud), D09 (budget), D08 (time), D05 (compliance) |
| `executive/product-brief` | Visão do produto | D02 (sistemas), D06 (dados) |
| `executive/premises` | Premissas | D01 (regiões), D05 (compliance), D10 (arquitetura ref) |
| `executive/go-no-go-decision` | Decisão | D09 (aprovação), D08 (gaps), D03 (débito) |
| `executive/next-steps` | Próximos passos | D07 (metodologia), D08 (disponibilidade) |
| `product/*` | Negócio, personas, valor | D02 (contratos), D07 (stakeholders) |
| `financial/*` | TCO, break-even, custo | D09 (todos) |
| `risk/*` | Matriz de riscos, viabilidade | D02 (legados), D03 (débito), D08 (riscos de equipe) |
| `organization/*` | RACI, stakeholders, metodologia | D07, D08 |
| `security/*` | Auth, criptografia, compliance | D05 |
| `privacy/*` | LGPD, dados pessoais, retenção | D05 (privacidade) |
| `technical/*` | Stack, arquitetura, ADRs, build-vs-buy | D01, D03, D04, D10 |
| `domain/*` | Integrações, dados, AI/ML, datalake | D02, D06 |
| `metrics/*` | KPIs, DORA, SLAs | D04 (observabilidade), D10 (SLOs) |
| `narrative/*` | Como chegamos aqui, condições | D07 (aprovações), D10 (change mgmt) |
| `research/*` | Entrevistas, quotes, oportunidades | Todos (evidência transversal) |
| `backlog/*` | Épicos, stories, dependências, Go/No-Go | D02 (legados), D03 (débito), D06 (integrações) |
| `quality/*` | Auditor score, checklist, gaps | Meta — gerada a partir de tudo |

---

## D01 — Infraestrutura & Cloud

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Tipo de infraestrutura (cloud/on-prem/híbrido) | X | X | X | executive/premises |
| 2 | Cloud provider principal | X | X | X | executive/premises, technical/tech-stack |
| 3 | Modelo de conta (single/multi-account) |  | X | X | technical/tech-stack |
| 4 | Billing (pay-as-you-go/reservado) |  | X | X | financial/tco-3-years |
| 5 | Budget alerts e cost tags |  | X | X | financial/cost-per-component |
| 6 | VPN site-to-site |  |  | X | technical/integrations |
| 7 | Direct Connect / ExpressRoute |  |  | X | technical/integrations |
| 8 | Restrições de firewall |  |  | X | technical/integrations |
| 9 | Topologia de VPCs |  |  | X | technical/container-architecture |
| 10 | Regiões em uso | X | X | X | executive/premises |
| 11 | Residência de dados obrigatória Brasil | X | X | X | security/compliance, privacy/legal-basis |
| 12 | Disaster recovery (multi-AZ/region) |  | X | X | risk/technical-risks, metrics/slas-and-slos |
| 13 | RPO/RTO alvo |  | X | X | metrics/slas-and-slos |
| 14 | Ambientes existentes (dev/hml/prd) |  |  | X | technical/macro-architecture |
| 15 | Provisionamento (IaC/manual) |  | X | X | technical/tech-stack, domain/platform-developer-experience |
| 16 | IaC cobertura (total/parcial) |  | X | X | risk/technical-risks |
| 17 | Ferramenta de observabilidade |  | X | X | technical/tech-stack, metrics/dora-metrics |
| 18 | Alertas configurados |  |  | X | metrics/slas-and-slos |
| 19 | Dashboards operacionais |  |  | X | metrics/slas-and-slos |
| 20 | Usa containers (Docker) |  |  | X | technical/container-architecture |
| 21 | Orquestrador (K8s/ECS/Compose) |  |  | X | technical/container-architecture |

**Mínimo D01 para One-Pager:** 1, 2, 10, 11.

---

## D02 — Sistemas Contratados & SaaS

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Inventário de sistemas ativos |  | X | X | product/business-model, technical/integrations |
| 2 | Custo mensal por sistema |  | X | X | financial/cost-per-component |
| 3 | API disponível por sistema |  |  | X | technical/integrations, domain/integration-map |
| 4 | SSO integrado por sistema |  |  | X | security/auth |
| 5 | Provedor de identidade (SSO) |  | X | X | security/auth |
| 6 | Sistemas legados sem substituição | X | X | X | risk/technical-risks, backlog/prioritized-epics |
| 7 | Shadow IT identificado |  | X | X | risk/technical-risks |
| 8 | Contratos/renovação |  | X | X | financial/cost-per-component, risk/risk-matrix |

**Mínimo D02 para One-Pager:** 6 (legados são potenciais bloqueadores críticos).

---

## D03 — Stack de Desenvolvimento

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Linguagens e frameworks |  | X | X | technical/tech-stack |
| 2 | Versionamento (Git provider, estratégia de branch) |  |  | X | domain/platform-developer-experience |
| 3 | Padrões e convenções (linter, formatter, code review) |  |  | X | domain/platform-developer-experience |
| 4 | Packages internos |  |  | X | technical/tech-stack |
| 5 | Bancos de dados |  | X | X | technical/tech-stack, domain/data-medallion-architecture |
| 6 | Mensageria e filas |  |  | X | technical/tech-stack, domain/microservices-service-map |
| 7 | Débito técnico conhecido | X | X | X | risk/technical-risks, backlog/prioritized-epics |

**Mínimo D03 para One-Pager:** 7 (débito crítico muda o orçamento e prazo).

---

## D04 — DevOps & Entrega Contínua

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | CI/CD (ferramenta, gates, cobertura) |  |  | X | domain/platform-developer-experience, metrics/dora-metrics |
| 2 | Deploy (estratégia, frequência, rollback) |  |  | X | metrics/dora-metrics |
| 3 | Gestão de secrets |  | X | X | security/encryption |
| 4 | Observabilidade de aplicação |  |  | X | metrics/dora-metrics |
| 5 | Gestão de incidentes |  |  | X | organization/oncall-and-support |

**Mínimo D04 para One-Pager:** nenhum obrigatório.

---

## D05 — Segurança & Compliance

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Políticas de segurança formais |  | X | X | security/compliance |
| 2 | Compliance regulatório aplicável (LGPD/GDPR/SOX/etc) | X | X | X | security/compliance, privacy/legal-basis, executive/premises |
| 3 | Classificação de dados |  | X | X | security/data-classification |
| 4 | Tratamento de dados pessoais (PII) |  | X | X | privacy/personal-data-inventory |
| 5 | DPO nomeado |  | X | X | privacy/dpo |
| 6 | Base legal LGPD |  | X | X | privacy/legal-basis |
| 7 | Retenção de dados |  |  | X | privacy/retention-policy |
| 8 | Direito ao esquecimento |  |  | X | privacy/right-to-erasure |
| 9 | Sub-processadores |  |  | X | privacy/sub-processors |
| 10 | Controle de acesso (IAM, RBAC, PAM) |  | X | X | security/auth |
| 11 | MFA obrigatório |  | X | X | security/auth |
| 12 | Vulnerabilidades (SAST/DAST/SCA) |  |  | X | security/compliance |
| 13 | Criptografia em trânsito/repouso |  | X | X | security/encryption |
| 14 | KMS / gestão de chaves |  |  | X | security/encryption |

**Mínimo D05 para One-Pager:** 2 (compliance define jurisdição e restrições duras).

---

## D06 — Dados & Integrações

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Fontes autoritativas de dado |  | X | X | domain/integration-map, domain/data-medallion-architecture |
| 2 | Qualidade dos dados (SLA, monitoramento) |  |  | X | domain/data-quality-strategy |
| 3 | Integrações existentes (volume, frequência, SLA) |  |  | X | domain/integration-map, domain/integration-data-contracts |
| 4 | Data warehouse / Data lake |  | X | X | domain/data-medallion-architecture |
| 5 | ETL/ELT (ferramenta, orquestração) |  |  | X | domain/data-medallion-architecture |
| 6 | Backup e recuperação |  |  | X | risk/technical-risks |

**Mínimo D06 para One-Pager:** nenhum obrigatório (entra via D05 se tiver dado pessoal).

---

## D07 — Gestão & Metodologia

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Metodologia praticada (Scrum/Kanban/XP) |  | X | X | organization/methodology |
| 2 | Ferramentas de gestão (Jira/ClickUp/Azure DevOps) |  |  | X | organization/methodology |
| 3 | Cerimônias praticadas |  |  | X | organization/methodology |
| 4 | Comunicação (Slack/Teams/email) |  |  | X | organization/stakeholder-map |
| 5 | Fluxo de aprovações |  | X | X | narrative/approval-signatures, organization/raci |
| 6 | Stakeholders mapeados |  | X | X | organization/stakeholder-map |

**Mínimo D07 para One-Pager:** nenhum obrigatório.

---

## D08 — Equipe & Capacidades

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Composição do time técnico (headcount, senioridade) |  | X | X | organization/team-structure |
| 2 | Especialistas disponíveis (cloud, dados, segurança) |  | X | X | organization/team-structure |
| 3 | Riscos de equipe (bus-factor, turnover) |  | X | X | risk/risk-matrix |
| 4 | Disponibilidade real para o projeto |  | X | X | organization/team-structure |
| 5 | Gaps de skills conhecidos |  | X | X | risk/risk-matrix, backlog/dependencies |

**Mínimo D08 para One-Pager:** nenhum obrigatório. One-Pager assume "todos contratados" para calcular esforço/custo. Dimensionamento real é tema do Executive.

---

## D09 — Financeiro (OPEX / CAPEX / TCO)

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Modelo de custo (OPEX/CAPEX/fundo global) |  | X | X | financial/tco-3-years |
| 2 | Custos de cloud (atual mensal, baseline) |  | X | X | financial/cost-per-component |
| 2b | **Estimativa de consumo cloud do projeto novo (sem free tier)** | X | X | X | financial/cost-per-component, executive/overview-one-pager |
| 3 | Custos recorrentes de fornecedores |  | X | X | financial/cost-per-component |
| 4 | Budget anual aprovado |  | X | X | financial/financial-scenarios |
| 5 | Aprovação financeira (alçadas) |  | X | X | narrative/approval-signatures |
| 6 | ROI / payback esperado |  |  | X | product/okrs-and-roi, financial/break-even |

**Mínimo D09 para One-Pager:** apenas 2b (estimativa de consumo cloud do projeto). Patria opera com fundo global corporativo — não há budget por projeto no formato convencional. ROI não entra (Discovery acontece após aprovação global, exceto se briefing exigir explicitamente).

---

## D10 — Governança, Normas & Boas Práticas

| # | Pergunta (resumo) | OP | EX | DR | Region primária |
|---|-------------------|----|----|----|-----------------|
| 1 | Catálogo de tecnologias aprovadas |  | X | X | executive/premises, technical/tech-stack |
| 2 | Change management (processo de mudança) |  |  | X | narrative/how-we-got-here |
| 3 | Auditoria (periodicidade, escopo) |  |  | X | security/compliance |
| 4 | SLAs e SLOs corporativos |  | X | X | metrics/slas-and-slos |
| 5 | Propriedade intelectual (quem é dono do código) |  | X | X | narrative/conditions-to-proceed |
| 6 | Arquitetura de referência existente |  | X | X | technical/macro-architecture, executive/premises |

**Mínimo D10 para One-Pager:** nenhum obrigatório (catálogo útil mas não bloqueia).

---

## Checklist — One-Pager (mínimo viável)

O One-Pager responde: **o que vai ser feito (escopo), quanto custa (estimativa), quanto esforço (duração em FTE-meses assumindo contratação integral), top riscos, premissas-chave**.

- [X] **D01.1** Tipo de infraestrutura → *cloud pública*
- [X] **D01.2** Cloud provider → *GCP*
- [X] **D01.10** Regiões em uso → *us-central1*
- [X] **D01.11** Residência de dados BR → *não obrigatória*
- [X] **D05.2** Compliance regulatório → *BACEN, CVM, CMF*
- [X] **D02.6** Legados críticos → **Incorta EOL 06/2026** (risco #1, bloqueio de ETL Oracle Fusion GL Cayman); Pentaho em declínio
- [X] **D03.7** Débito técnico crítico → *(a levantar em entrevistas; confirmado que não bloqueia One-Pager — tratar como premissa "débito existente, escopo a mapear")*
- [X] **D09.2b** Estimativa de consumo cloud do projeto → *a estimar por arquitetura proposta, desconsiderando free tier (fundo global cobre OPEX; não há budget por projeto)*

**Excluídos por design do framework Discovery-to-Go:**
- ~~D08.4~~ Disponibilidade de FTE — One-Pager assume "todos contratados" para simplificar cálculo de esforço.
- ~~D08.5~~ Gaps de skill — confirmado "sem gaps críticos" na Patria; tema do Executive de toda forma.
- ~~D09.2~~ Custo atual de cloud — baseline informativo, não bloqueante.
- ~~D09.4~~ Budget anual — Patria não aloca budget por projeto (fundo global).
- ~~D09.6~~ ROI/payback — Discovery ocorre após aprovação global, exceto se briefing pedir explicitamente.

**Status Patria (Abr/2026):** One-Pager **pronto para ser gerado**. Os itens em aberto (consumo cloud estimado, detalhamento de débito) são produzidos durante o próprio Discovery, não são pré-requisitos.

---

## Checklist — Executive Report (incremental sobre One-Pager)

Adiciona ~80 perguntas. Áreas críticas:

- [ ] D01.12–13 — DR multi-AZ/region e RPO/RTO alvo
- [ ] D02.1, D02.5 — inventário + SSO consolidado
- [ ] D02.7 — Shadow IT
- [ ] D03.1, D03.5 — linguagens e DBs
- [ ] D04.3 — gestão de secrets
- [ ] D05.1, D05.3–6, D05.10–11, D05.13 — bloco de segurança/privacidade alto nível
- [ ] D06.1, D06.4 — fontes autoritativas e DW
- [ ] D07.1, D07.5–6 — metodologia, aprovações, stakeholders
- [ ] D08.1–3 — time, especialistas, riscos de equipe
- [ ] D09.1, D09.3, D09.5 — OPEX/CAPEX, fornecedores, alçadas
- [ ] D10.1, D10.4–6 — catálogo, SLAs, IP, arquitetura ref

---

## Checklist — Delivery Report (tudo)

Todas as ~564 perguntas. Use o próprio `environment.md` como checklist. A coluna "Status atual Patria" do resumo agregado indica 11% hoje — a maior parte do trabalho de descoberta ainda está pela frente e é o que as fases seguintes do discovery (entrevistas, workshops) devem fechar.

---

## Como usar este documento

1. **Antes de gerar um entregável**, abra este arquivo e confira o checklist correspondente.
2. Se faltar resposta em qualquer item marcado `[X]` na coluna do entregável, **não gere o documento ainda** — colete a resposta primeiro (form, entrevista, workshop).
3. Para perguntas marcadas apenas `[DR]`, é aceitável gerar One-Pager/Executive sem elas; registrar como "A DESCOBRIR" no Delivery.
4. Quando o `environment.md` for atualizado, este arquivo **não** precisa mudar — ele é estrutural. O que muda é o percentual de completude por entregável.
