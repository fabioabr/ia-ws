---
title: "Delivery Report — Veezoozin"
description: "Relatório consolidado de Discovery para o projeto Veezoozin — plataforma SaaS de consulta em linguagem natural sobre bancos de dados corporativos"
project-name: "veezoozin"
client: "mAInd Tech"
author: "consolidator"
category: delivery
version: "03.00.000"
status: ativo
area: tecnologia
tags:
  - delivery
  - veezoozin
  - discovery
  - consolidado
  - saas
  - ai-ml
  - datalake-ingestion
created: "2026-04-12"
report-setup: "executive"
iteration: 1
run: run-3
flags: []
regions:
  - REG-EXEC-01
  - REG-EXEC-02
  - REG-EXEC-03
  - REG-EXEC-04
  - REG-PROD-01
  - REG-PROD-02
  - REG-PROD-04
  - REG-PROD-05
  - REG-PROD-06
  - REG-PROD-07
  - REG-ORG-01
  - REG-ORG-02
  - REG-TECH-01
  - REG-TECH-02
  - REG-TECH-03
  - REG-SEC-01
  - REG-PRIV-01
  - REG-FIN-01
  - REG-FIN-05
  - REG-FIN-07
  - REG-RISK-01
  - REG-QUAL-01
  - REG-QUAL-02
  - REG-BACK-01
  - REG-EXEC-05
  - REG-GLOSS-01
---

# Delivery Report — Veezoozin

> Relatório consolidado do Discovery Pipeline — Run 3, Iteração 1
> Projeto: **Veezoozin** | Cliente: **mAInd Tech** | Data: 2026-04-12

---

<!-- region: REG-EXEC-01 -->
## Resumo Executivo

O Veezoozin é uma plataforma SaaS conversational-first que converte perguntas em linguagem natural (PT-BR, EN-US, ES) em queries SQL contextualizadas pelo domínio de negócio de cada tenant, retornando gráficos, insights e análises em segundos. Utiliza stack GCP-first (Cloud Run, BigQuery, Vertex AI) com LLMs externos via BYOK (Bring Your Own Key) e integração MCP para fontes de conhecimento externas.

**Mudança estrutural do Run-3:** Equipe de 1 desenvolvedor sênior + Claude Code (em vez de time convencional), modelo BYOK (custo de LLM 100% do tenant), infraestrutura 100% serverless/pay-per-use. Isso reduz o custo fixo de ~R$ 75K para ~R$ 17K/mês e torna o projeto financeiramente viável com bootstrapping.

**Métricas-chave do Discovery:**

| Métrica | Valor |
|---------|-------|
| TCO 3 anos | R$ 1.204.800 |
| Receita projetada 3 anos | R$ 1.360.214 |
| Resultado 3 anos | **+R$ 155.414** |
| Break-even operacional | Mês 19 (realista, com 1a contratação) |
| Break-even solo | Mês 16 (sem contratação) |
| Investimento até break-even | ~R$ 184K |
| Margem bruta Pro | 86% |
| Margem bruta Enterprise | 94% |
| Score Auditor | 88,8% |
| Score 10th-man | 75,8% |
| Threshold | >=80% (poc) |
| Recomendação Go/No-Go | **GO — projeto viável** |

**Destaques positivos:** Pipeline NL-to-SQL com 6 etapas e privacy guard, LGPD em modo profundo completo, Build vs Buy disciplinado (12 componentes, 840h economizadas), arquitetura Modular Monolith com 15 módulos e 12 ADRs, 78 decisões rastreadas (D1.1-D8.8), modelo financeiro viável com margem bruta 86-94% (BYOK), beta program estruturado, kill criteria definidos.

**Pontos de atenção:** Bus factor = 1 (risco existencial mitigado com docs + auto-healing + freelancer standby), TAM/SAM/SOM não dimensionado (volume necessário é baixo: ~30 clientes), precisão NL-to-SQL meta 85% pode ser otimista para MVP (10th-man recomenda >75% escalonado), sustentabilidade operacional solo por 10-14 meses até 1a contratação.
<!-- /region: REG-EXEC-01 -->

---

<!-- region: REG-EXEC-02 -->
## Visão Geral do Projeto

| Campo | Valor |
|-------|-------|
| **Projeto** | Veezoozin |
| **Cliente** | mAInd Tech (startup de tecnologia) |
| **Tipo de projeto** | Novo produto (greenfield) |
| **Context-Templates** | SaaS + AI/ML + Datalake-Ingestion |
| **Duração do Discovery** | Run 3, Iteração 1 — 8 blocos discovery + 2 blocos challenge |
| **Setup do Relatório** | Executive |
| **Data Source Breakdown** | Briefing ~69% / Inference ~31% / Recomendações ~89% aceitas |
| **Confiança Geral** | Alta — sem inconsistências inter-blocos, modelo financeiro viável |
| **Flags** | Nenhuma |
| **Equipe** | 1 arquiteto sênior full-stack + Claude Code |
| **Modelo de LLM** | BYOK — tenant cadastra sua própria API key |
| **Infraestrutura** | 100% serverless/pay-per-use (GCP) |
<!-- /region: REG-EXEC-02 -->

---

<!-- region: REG-EXEC-03 -->
## Go/No-Go

> **GO — Projeto Viável**

O discovery demonstra viabilidade financeira, excelência técnica e consistência inter-blocos. O modelo econômico do run-3 (1 dev + BYOK + pay-per-use) transforma fundamentalmente a equação de viabilidade em relação ao run-2.

**Scores de validação:**

| Validador | Score | Threshold | Status |
|-----------|:-----:|:---------:|--------|
| Auditor (convergente) | 88,8% | >=80% | ACIMA DO THRESHOLD |
| 10th-man (divergente) | 75,8% | >=80% | ABAIXO DO THRESHOLD |
| Veredicto auditor | APROVADO | — | — |
| Veredicto 10th-man | APROVADO COM RESSALVAS | — | — |

**Radar de avaliação (Auditor — 5 eixos):**

| Eixo | Score |
|------|:-----:|
| Cobertura | 92% |
| Profundidade | 88% |
| Consistência | 93% |
| Fundamentação | 85% |
| Completude | 85% |

**Radar de avaliação (10th-man — 3 eixos):**

| Eixo | Score |
|------|:-----:|
| Divergência | 70% |
| Robustez | 78% |
| Completude Crítica | 80% |

**Recomendações para fortalecimento (não bloqueantes):**

1. Dimensionar mercado (TAM/SAM/SOM) — validar volume de empresas com BigQuery no Brasil
2. Confirmar 3-5 candidatos para beta program antes do desenvolvimento
3. Definir meta de precisão escalonada: >75% (MVP), >80% (mês 6), >85% (mês 8)
4. Formalizar acordo com 1-2 freelancers para contingência do bus factor
5. Criar fundo de emergência de 3 meses (R$ 51K) antes do launch
<!-- /region: REG-EXEC-03 -->

---

## Produto e Valor

<!-- region: REG-PROD-01 -->
### Problema Central

O Veezoozin resolve um problema estrutural: **dados valiosos existem nas empresas, mas estão presos atrás de barreiras técnicas**.

| Dimensão | Descrição | Impacto |
|----------|-----------|---------|
| **Barreira técnica** | Gestores dependem de times de dados. Uma pergunta vira ticket de 2-3 dias. | Decisões atrasadas, custo operacional alto |
| **Falta de contexto** | Ferramentas de BI genéricas não entendem o vocabulário do cliente. | Respostas imprecisas, retrabalho |
| **Dados sem ação** | Usuário recebe tabelas brutas sem insights, gráficos ou tendências. | Dados acessados mas não utilizados |
| **Multi-idioma** | Empresas latinas operam em PT-BR, EN-US e ES. | Exclusão de usuários, adoção limitada |

**Impacto mensurável esperado:**

| Métrica | Antes | Depois | Ganho |
|---------|-------|--------|:-----:|
| Tempo de resposta | Dias (ticket) | Segundos (pergunta) | ~99% |
| Colaboradores com acesso a dados | 5-10% (técnicos) | 100% | Democratização total |
| Volume de tickets para time de dados | Baseline | -60% a -80% | Liberação para tarefas estratégicas |
| Qualidade da resposta | Tabela bruta | Gráfico + insight + análise | Salto qualitativo |
<!-- /region: REG-PROD-01 -->

<!-- region: REG-PROD-02 -->
### Personas

| Persona | Arquétipo | Perfil | JTBD | Frequência | Tier provável |
|---------|-----------|--------|------|:----------:|:------------:|
| **P0 — Gestora** | Marina, Diretora Comercial | 38 anos, MBA, não sabe SQL | Perguntar sobre KPIs e receber gráficos em segundos | Diário (2-5/dia) | Pro/Enterprise |
| **P0 — Analista** | Rafael, Analista de BI | 29 anos, SQL básico, 70% em queries repetitivas | Cruzar dados sem escrever SQL | Diário (10-20/dia) | Pro |
| **P1 — Admin Tenant** | Lucas, Líder de Dados | 34 anos, engenheiro de dados | Ensinar o sistema sobre o domínio de negócio | Semanal | Todos |
| **P1 — Admin TI** | Carla, Coord. de Infra | 41 anos, foco em segurança | Garantir read-only, LGPD, logs — **poder de veto** | Mensal | Enterprise |

**Relação com BYOK:**
- Marina: transparente — não sabe que LLM existe
- Rafael: pode se preocupar com "custo por query"
- Lucas: monitora consumo no dashboard
- Carla: gerencia API key como secret corporativo (rotação, vault, auditoria)

**Jornada de primeiro valor:** ~45 minutos (signup 2 min → API key 3 min → BigQuery 10 min → schema mapping 15-20 min → glossário 10 min → primeira query 5 seg → "aha! moment")
<!-- /region: REG-PROD-02 -->

<!-- region: REG-PROD-04 -->
### Proposta de Valor e Diferenciação

| Concorrente | Limitação principal | Vantagem Veezoozin |
|-------------|--------------------|--------------------|
| Tableau Ask Data | Apenas dentro do Tableau, idiomas limitados | Standalone, multi-idioma nativo |
| ThoughtSpot | Pricing enterprise elevado (US$ 1.250+/mês), schema rígido | Acessível para PMEs (R$ 497), schema flexível por tenant |
| ChatGPT + SQL | Sem contexto de negócio, sem multi-tenancy, sem persistência | Glossário por tenant, histórico, aprendizado contínuo |
| Metabase | Dashboard-first, não conversacional | Conversational-first com output visual rico |

**Moat principal:** Contexto de negócio acumulado por tenant + multi-idioma nativo + integração MCP. O moat real é o **efeito de rede de contexto** — quanto mais o tenant usa, melhor o sistema fica (few-shot examples, glossário refinado, histórico).

**Posicionamento:** "Pergunte para seus dados" — democratização do acesso a dados via linguagem natural.
<!-- /region: REG-PROD-04 -->

<!-- region: REG-PROD-05 -->
### OKRs do MVP e Métricas

**O1: Validar que o produto resolve o problema**

| KR | Métrica | Meta |
|----|---------|:----:|
| KR1.1 | Precisão NL-to-SQL (1a tentativa) | >85% |
| KR1.2 | Latência para queries simples | <5 seg |
| KR1.3 | % tenants com "aha! moment" em <45 min | >70% |
| KR1.4 | Taxa de aceitação de sugestões de prompt | >40% |

**O2: Conseguir primeiros clientes pagantes**

| KR | Métrica | Meta |
|----|---------|:----:|
| KR2.1 | Tenants ativos (Free + Pro) | 5+ (mês 4) |
| KR2.2 | Tenants pagantes (Pro) | 3+ (m��s 6) |
| KR2.3 | MRR | R$ 1.500+ (mês 6) |

**O3: Manter operação sustentável com 1 dev**

| KR | Métrica | Meta |
|----|---------|:----:|
| KR3.1 | Custo de infra com até 50 tenants | <R$ 5K/mês |
| KR3.2 | Uptime | >99.5% |
| KR3.3 | Deploy sem downtime | 100% |

**Métricas norte por estágio:**

| Estágio | Métrica norte | Por quê |
|---------|:------------:|---------|
| MVP (meses 1-4) | Precisão NL-to-SQL | Se a query errar, nada mais importa |
| Early (meses 4-8) | Ativação (% aha! moment) | Validar onboarding |
| Growth (meses 8-14) | MRR | Caminho para break-even |
| Scale (meses 14+) | Net Revenue Retention | Expansão > churn |
<!-- /region: REG-PROD-05 -->

<!-- region: REG-PROD-06 -->
### Modelo Comercial e Pricing

**Modelo:** SaaS freemium + tiered. BYOK a partir do Pro.

| Aspecto | Free | Pro | Enterprise |
|---------|------|-----|------------|
| **Preço/mês** | R$ 0 | R$ 497 | R$ 2.497+ |
| **Preço anual** | R$ 0 | R$ 4.970 (2 meses grátis) | Negociável |
| **LLM** | Pool compartilhado (50 queries/mês, Gemini Flash) | BYOK obrigatório | BYOK obrigatório |
| **Usuários** | 2 | 10 | Ilimitado |
| **Fontes de dados** | 1 dataset, 5 tabelas | 10 datasets, 50 tabelas | Ilimitado |
| **Queries/mês** | 50 | Ilimitado | Ilimitado |
| **Glossário** | Templates prontos | Customizável (100 termos) | Ilimitado + consultoria |
| **MCP** | Não | Sim (até 3 fontes) | Sim (ilimitado) |
| **Export** | Não | PDF/HTML | PDF/HTML + API |
| **Histórico** | 7 dias | 90 dias | Ilimitado (configurável) |
| **RBAC** | Viewer/Admin | Viewer/Analyst/Admin | Custom + column-level |
| **SSO** | Não | Não | Sim (SAML/OAuth2) |
| **SLA** | Best effort | 99.5% | 99.9% |
| **Suporte** | Docs apenas | Chat + email (NBD) | Dedicado (4h SLA) |

**Trial Pro:** 14 dias sem exigir API key (pool compartilhado, 200 queries). Custo: R$ 2-6/tenant trial.

**Enterprise variável:** Base R$ 2.497/mês (até 50 usuários) + R$ 29/usuário adicional. Empresa com 200 usuários = R$ 6.847/mês.
<!-- /region: REG-PROD-06 -->

<!-- region: REG-PROD-07 -->
### Escopo do MVP e Roadmap

**Dentro do escopo:**
- Interface conversacional web (PT-BR, EN-US, ES)
- Engine NL-to-SQL com RAG contextual (BigQuery apenas no MVP)
- Gráficos automáticos (Chart.js), insights via LLM, sugestões de próxima query
- Multi-tenant com isolamento por design (BigQuery do tenant é externo)
- Billing via Stripe (Free/Pro/Enterprise)
- BYOK multi-provider (Claude, Gemini, OpenAI) via adapter pattern
- LGPD: read-only, schema abstrato nos prompts, audit log, retenção por tier
- RBAC básico (roles por dataset)
- Guided First Query no onboarding

**Fora do escopo:**
- Escrita/modificação de dados
- Fine-tuning de LLM próprio
- ETL/ingestão de dados
- App mobile nativo
- Multi-banco (PostgreSQL, MySQL) — Fase 2
- SSO/SAML — Fase 2

**Roadmap:**

| Fase | Prazo | Escopo principal |
|------|-------|------------------|
| MVP | 4 meses (12 semanas) | NL→SQL→Viz. BigQuery. 3 idiomas. Free/Pro. BYOK. |
| Fase 2 | +3 meses | Multi-banco + MCPs + RAG + SSO + Enterprise |
| Fase 3 | +3 meses | Análises preditivas + alertas + agentes autônomos |
<!-- /region: REG-PROD-07 -->

---

## Organização

<!-- region: REG-ORG-01 -->
### Time e Stakeholders

**Time MVP:**

| Papel | Pessoa | Dedicação | Custo/mês | Status |
|-------|--------|:---------:|----------:|--------|
| Arquiteto Sênior Full-Stack | Fabio | Full-time | R$ 15.000 | Existente |
| Assistente de desenvolvimento (IA) | Claude Code | Full-time | R$ 1.500 | Existente |
| **Total** | **1 pessoa + IA** | — | **R$ 16.500** | — |

**Modelo de trabalho:** Fabio é arquiteto, desenvolvedor, DevOps, PM, suporte e operação. Claude Code é par de programação, revisor de código, gerador de testes, documentador e assistente de design. Output equivalente a ~3 devs full-stack.

**Milestones de contratação (baseados em receita):**

| MRR | Contratação | Custo adicional |
|:----|------------|:---------------:|
| R$ 25K | DevOps/SRE junior | +R$ 8K/mês |
| R$ 40K | Customer Success | +R$ 7K/mês |
| R$ 60K | Dev backend pleno | +R$ 12K/mês |
| R$ 100K | Dev frontend + Designer + PM | +R$ 30K/mês |

**Bus factor mitigation:** Auto-healing (Cloud Run restart, circuit breakers) + documentação excepcional (ADRs, runbooks) + freelancer em standby.
<!-- /region: REG-ORG-01 -->

<!-- region: REG-ORG-02 -->
### Metodologia e SLOs

| Aspecto | Abordagem |
|---------|-----------|
| Framework | Kanban pessoal (não Scrum) |
| Ciclos | Sprints de 1 semana com meta única |
| Código | Trunk-based development |
| Code review | Claude Code como reviewer |
| Testes | Automatizados desde o dia 1 |
| Deploy | CI/CD com GitHub Actions → Cloud Run |
| Monitoramento | Cloud Monitoring + Sentry + alertas Telegram |

**SLOs por tier:**

| Métrica | Free | Pro | Enterprise |
|---------|:----:|:---:|:----------:|
| Uptime | Best effort | 99.5% | 99.9% |
| Latência p95 | <10s | <5s | <3s |
| Suporte | Docs | NBD | 4h SLA |

**Rituais anti-burnout:** No-deploy Friday, review mensal 2h, semana de debt mensal, férias trimestrais.
<!-- /region: REG-ORG-02 -->

---

## Arquitetura Técnica

<!-- region: REG-TECH-01 -->
### Stack Tecnológica

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Compute | Cloud Run (serverless) | Pay-per-use, auto-scaling |
| API | Python + FastAPI | Ecossistema AI/ML, tipagem, async |
| Banco metadata | Cloud SQL (PostgreSQL) HA | Tenants, configs, glossários |
| Sessões/cache | Firestore | Pay-per-operation, 99.999% |
| Data Warehouse | BigQuery | Banco analítico dos tenants (read-only) |
| Embeddings | Vertex AI (text-embedding-004) | Schema + glossário vetorial |
| LLM | APIs externas via BYOK | Claude, Gemini, OpenAI |
| Auth | Firebase Auth | OAuth2, SSO (SAML Enterprise) |
| Frontend | Next.js + Shadcn/Radix | SSR, component library |
| Gráficos | Chart.js | Lightweight, customizável |
| Billing | Stripe | Planos, trials, dunning |
| CI/CD | GitHub Actions | Deploy contínuo |
| Secrets | Google Secret Manager | API keys BYOK criptografadas |
| Monitoramento | Cloud Monitoring + Sentry | Nativo GCP + error tracking |
<!-- /region: REG-TECH-01 -->

<!-- region: REG-TECH-02 -->
### Pipeline NL-to-SQL

| Etapa | Processo | Latência alvo |
|:-----:|---------|:-------------:|
| 1 | Input NL + detecção de idioma | <100ms |
| 2 | Contexto enriquecido (RAG: schema + glossário + histórico) | <500ms |
| 3 | Geração de SQL via LLM BYOK | <2.000ms |
| 4 | Validação (read-only, dry-run) + execução BigQuery sandbox | <1.500ms |
| 5 | Output visual (Chart.js, tipo auto-selecionado) | <300ms |
| 6 | Insight generation via LLM BYOK | <1.000ms |
| **Total** | — | **<5.050ms** |

**Estratégias de otimização:**
- Cache de queries: mesma pergunta normalizada + mesmo schema → reutiliza SQL (TTL 1h). Economia estimada 30-50%
- SQL dry-run antes de execução: valida SQL e estima custo (BigQuery cobra por TB processado)
- Schema abstrato nos prompts: sem sample data (minimização PII/LGPD)
- Adapter pattern para multi-provider LLM: interface unificada `LLMProvider`

**Arquitetura: Modular Monolith** — 1 container Cloud Run com 15 módulos bem separados (preparado para split futuro).
<!-- /region: REG-TECH-02 -->

<!-- region: REG-TECH-03 -->
### Módulos do Sistema

| Módulo | Responsabilidade | Referência |
|--------|-----------------|-----------|
| auth | Firebase Auth, sessões, JWT | D5.5 |
| tenant | CRUD tenants, isolamento row-level | D5.1 |
| rbac | Roles e permissões por dataset | D2.5 |
| connection | Conexões BigQuery, service accounts | Bloco 5 |
| byok | API keys LLM, adapter multi-provider | D5.6, D1.3 |
| schema | Mapeamento automático, embeddings | Bloco 5 |
| glossary | Glossário de negócio por tenant | Bloco 1 |
| nl-to-sql | Pipeline completo NL→SQL→resultado | Bloco 5 |
| visualization | Chart.js, export PDF/HTML | Bloco 1 |
| insight | Insights via LLM, sugestões | Bloco 5 |
| billing | Stripe, planos, trial, dunning | D3.8 |
| audit | Logging LGPD, compliance | D6.1 |
| mcp | Integração fontes externas via MCP | Bloco 1 |
| admin | Painel admin do tenant | Bloco 2 |
| onboarding | Wizard setup, guided first query | D2.3 |

**12 ADRs documentados:** Modular Monolith, row-level tenancy, RAG sem fine-tuning, BYOK adapter, Firebase Auth, Stripe, schema abstrato, SQL dry-run, monitoring GCP-nativo, cache Firestore, retenção por tier, DPA obrigatório.
<!-- /region: REG-TECH-03 -->

---

## Segurança e Privacidade

<!-- region: REG-SEC-01 -->
### Segurança

| Controle | Implementação |
|----------|---------------|
| Read-only enforcement | Service account com `roles/bigquery.dataViewer` |
| SQL injection prevention | Parser whitelist (SELECT apenas) |
| Query sandbox | Timeout 30s, limit 10K rows, scan limit 1TB, dry-run |
| Audit log | Toda query: tenant_id, user_id, SQL, resultado, timestamp |
| Criptografia at-rest | GCP default (AES-256) |
| Criptografia in-transit | TLS 1.3 obrigatório |
| BYOK keys | Secret Manager, AES-256-GCM, nunca plaintext, nunca logada |
| Rate limiting | Por tier: Free 2/min, Pro 10/min, Enterprise 30/min |
| DDoS | Cloud Armor + middleware FastAPI |
| Monitoramento | 3 camadas: auto-healing, alertas inteligentes, status page |
<!-- /region: REG-SEC-01 -->

<!-- region: REG-PRIV-01 -->
### Privacidade e LGPD

**Modo:** Profundo (deep) — processa dados de terceiros que podem conter PII.

**Papéis LGPD:**
- mAInd Tech: controlador (dados SaaS) + operador (dados do tenant)
- Tenant: controlador dos dados analíticos
- Anthropic/Google/OpenAI: sub-processadores (LLM)
- Stripe: sub-processador (billing)

**Bases legais:** Execução de contrato (conta, auth, billing) + Consentimento do controlador-tenant (dados analíticos via LLM) + Legítimo interesse (histórico) + Obrigação legal (auditoria).

**Retenção:**

| Dado | Retenção |
|------|----------|
| Histórico de queries | Free 7d / Pro 90d / Enterprise configurável |
| Resultados de queries | Não persistidos (cache TTL 15 min) |
| Logs de auditoria | 2 anos |
| API keys BYOK | Delete imediato ao revogar |
| Dados de billing | 5 anos (legislação fiscal) |

**Minimização de PII:** Schema abstrato nos prompts desde o MVP. Column tagging de PII na Fase 2. "Right to be Forgotten" automatizado (botão + cascade delete).

**DPO:** Fabio até R$ 25K MRR, depois terceirizado (~R$ 2K/mês). Canal: privacidade@veezoozin.com.

**DPAs obrigatórios:** mAInd Tech ↔ Tenant (Pro/Enterprise), mAInd Tech ↔ Google, mAInd Tech ↔ Stripe. Termos de Uso com cláusula explícita sobre LLM e BYOK.
<!-- /region: REG-PRIV-01 -->

---

## Financeiro

<!-- region: REG-FIN-01 -->
### TCO — 3 Anos

**Custos fixos mensais (evolução por período):**

| Item | Mês 1-12 | Mês 13-18 | Mês 19-24 | Mês 25-36 |
|------|----------:|----------:|----------:|----------:|
| Fabio (arquiteto sênior) | R$ 15.000 | R$ 15.000 | R$ 15.000 | R$ 15.000 |
| Claude Code | R$ 1.500 | R$ 1.500 | R$ 1.500 | R$ 1.500 |
| Cloud SQL HA | R$ 400 | R$ 400 | R$ 600 | R$ 600 |
| Ferramentas | R$ 250 | R$ 250 | R$ 350 | R$ 350 |
| SRE junior | — | R$ 8.000 | R$ 8.000 | R$ 8.000 |
| CS | — | — | R$ 7.000 | R$ 7.000 |
| Dev backend | — | — | — | R$ 12.000 |
| DPO terceirizado | — | — | R$ 2.000 | R$ 2.000 |
| **Total fixo/mês** | **R$ 17.150** | **R$ 25.650** | **R$ 34.950** | **R$ 47.450** |

**Custo variável:** ~R$ 70/tenant/mês (Cloud Run + BigQuery + Firestore + Vertex AI + Storage + Stripe). Com cache: ~R$ 55/tenant. LLM é BYOK = R$ 0 para mAInd Tech.

**Projeção consolidada:**

| Período | Receita | Custo total | Resultado |
|---------|:-------:|:-----------:|:---------:|
| Ano 1 | R$ 50.834 | R$ 211.800 | -R$ 160.966 |
| Ano 2 | R$ 329.244 | R$ 353.400 | -R$ 24.156 |
| Ano 3 | R$ 980.136 | R$ 639.600 | **+R$ 340.536** |
| **Total 3 anos** | **R$ 1.360.214** | **R$ 1.204.800** | **+R$ 155.414** |

**Investimento até break-even: ~R$ 184K** (mês 19).

Comparativo vs Run-2: investimento até break-even reduziu de ~R$ 900K-1.2M para R$ 184K (-80%). TCO 3 anos reduziu de R$ 10.5M para R$ 1.2M (-88%).
<!-- /region: REG-FIN-01 -->

<!-- region: REG-FIN-05 -->
### Build vs Buy

| Componente | Decisão | Custo Buy | Economia de tempo |
|-----------|:-------:|-----------|:-----------------:|
| Autenticação | BUY — Firebase Auth | R$ 0 | 80h |
| Billing | BUY — Stripe | ~3% receita | 200h |
| NL-to-SQL engine | BUILD — Custom pipeline | N/A | Core do produto |
| LLM | BUY — APIs externas BYOK | R$ 0 (tenant paga) | Inviável hospedar |
| Embeddings | BUY — Vertex AI | ~R$ 5/tenant | 100h |
| Bancos | BUY — Cloud SQL + Firestore + BQ | Pay-per-use | Managed = zero ops |
| Monitoramento | BUY — GCP + Sentry free | R$ 0 | 60h |
| CI/CD | BUY — GitHub Actions | R$ 0 | 40h |
| Gráficos | BUY — Chart.js | R$ 0 | 120h |
| Frontend UI | BUY — Shadcn/Radix | R$ 0 | 200h |
| Feature flags | BUILD — Custom (Cloud SQL) | R$ 0 | 8h |
| Secrets | BUY — Secret Manager | Incluído GCP | 40h |

**Total economizado: ~840h (21 semanas).** Sem Buy, MVP levaria 33 semanas em vez de 12. Regra aplicada: "Build apenas o que é diferencial competitivo. Buy todo o resto."
<!-- /region: REG-FIN-05 -->

<!-- region: REG-FIN-07 -->
### Cenários de Viabilidade

| Cenário | Break-even | Investimento | Viabilidade |
|---------|:----------:|:-----------:|:-----------:|
| **Base (gradual)** | Mês 19 | R$ 184K | Viável — bootstrapping |
| **A (crescimento lento, 50%)** | Mês 28 | R$ 330K | Viável, apertado |
| **B (acelerado, 200%)** | Mês 10-12 | R$ 85K | Muito viável |
| **C (preço R$ 297/Pro)** | Mês 22 | R$ 260K | Viável, exige mais volume |
| **D (Enterprise-first)** | Mês 12-14 | R$ 140K | Viável financeiramente, risco operacional |

**Análise de sensibilidade:** O modelo é extremamente sensível ao custo fixo (equipe) e pouco sensível ao custo variável (infra). Cada contratação adiciona ~R$ 8K/mês, exigindo ~16 Pro adicionais.

**Go/No-Go gates:**

| Gate | Quando | Critério GO | Critério STOP |
|------|--------|------------|---------------|
| Gate 1 | Mês 4 | Produto funcional, 3+ tenants beta | 0 tenants |
| Gate 2 | Mês 7 | 1+ pagante, NPS >30 | 0 pagantes |
| Gate 3 | Mês 12 | MRR >R$ 5K, 10+ Pro | MRR <R$ 2K |
| Gate 4 | Mês 18 | MRR >R$ 20K, trajetória de break-even | MRR <R$ 10K |
<!-- /region: REG-FIN-07 -->

---

## Riscos

<!-- region: REG-RISK-01 -->
### Mapa de Riscos

| # | Risco | Prob. | Impacto | Mitigação |
|---|-------|:-----:|:-------:|-----------|
| R1 | Bus factor = 1 (Fabio indisponível) | Alta | Crítico | Auto-healing, ADRs/runbooks, freelancer standby, fundo emergência 3 meses |
| R2 | Precisão NL-to-SQL <85% no MVP | Média | Crítico | Glossário + RAG + feedback loop 3 camadas. Kill criterion: <70% → pivotar |
| R3 | Burnout do fundador (6-12 meses) | Alta | Alto | No-deploy Friday, semana de debt, férias trimestrais, automação 34h/mês |
| R4 | BYOK key expirada/sem saldo | Média | Médio | Healthcheck diário, notificação proativa, mensagem amigável ao usuário |
| R5 | Google lança BigQuery NL nativo | Média | Alto | Moat de contexto acumulado + glossário + multi-idioma + insights |
| R6 | Conversão Free→Pro <5% | Alta | Médio | Limitar Free agressivamente, demonstrar valor claro no Pro, trial 14 dias |
| R7 | Churn >10% mensal | Média | Alto | Feedback loop, guided first query, customer success (post R$ 40K MRR) |
| R8 | BigQuery cost spike (query pesada) | Média | Médio | Dry-run + scan limit 1TB + alertas de custo |
| R9 | LLM provider muda termos/preços | Média | Médio | Multi-provider adapter, suporte a 3+ provedores |
| R10 | LGPD multa por não-compliance | Baixa | Alto | Compliance escalável por estágio de receita, DPO antes de R$ 25K MRR |
<!-- /region: REG-RISK-01 -->

---

## Qualidade

<!-- region: REG-QUAL-01 -->
### Validação Convergente (Auditor)

**Score global: 88,8%** | **Veredicto: APROVADO**

| Dimensão | Score |
|----------|:-----:|
| Cobertura | 92% |
| Profundidade | 88% |
| Consistência | 93% |
| Fundamentação | 85% |
| Completude | 85% |

**P21 — Viabilidade Financeira: APROVADO** (sem penalidade). Projeto viável com break-even mês 19, margem 86-94%, ROI positivo em 3 anos.

**Findings não bloqueantes:**
- F1: TAM/SAM/SOM ausente (volume necessário é baixo: ~30 clientes)
- F2: Churn sem benchmark externo
- F3: Competitive response estática (não modela BigQuery NL nativo)
<!-- /region: REG-QUAL-01 -->

<!-- region: REG-QUAL-02 -->
### Validação Divergente (10th Man)

**Score global: 75,8%** | **Veredicto: APROVADO COM RESSALVAS**

| Dimensão | Score |
|----------|:-----:|
| Divergência | 70% |
| Robustez | 78% |
| Completude Crítica | 80% |

**Premissas desafiadas:**
1. Bus factor = 1 — mitigações propostas são necessárias mas insuficientes para ausência prolongada
2. BYOK — financeiramente brilhante, mas cria fricção (key expirada, custo surpresa, suporte de terceiro)
3. Precisão NL-to-SQL — 85% é otimista para schemas desconhecidos; recomenda meta escalonada (75%→80%→85%)

**Pontos cegos identificados:**
- Sustentabilidade operacional solo por 10-14 meses
- Exit strategy não definida
- BigQuery NL nativo como risco competitivo existencial
- Nenhuma validação com clientes reais (beta program planejado)

**Reconhecimento:** Salto qualitativo vs run-2. Modelo financeiro transformado de inviável (23% cobertura) para viável (113%). Consistência inter-blocos excelente. Especialistas proativos.
<!-- /region: REG-QUAL-02 -->

---

## Backlog e Próximos Passos

<!-- region: REG-BACK-01 -->
### Roadmap de Execução — MVP (12 semanas)

| Semana | Foco | Entregável |
|:------:|------|-----------|
| 1-2 | Fundação | Projeto GCP, Cloud Run, Firestore, auth básica, CI/CD |
| 3-4 | Multi-tenant core | Tenant CRUD, isolamento row-level, RBAC básico |
| 5-6 | NL-to-SQL engine | Parser NL, conversão BigQuery SQL, sandbox |
| 7-8 | Contexto do tenant | Schema mapping, glossário, embeddings Vertex AI |
| 9-10 | Output visual | Gráficos Chart.js, insights IA, export PDF/HTML |
| 11 | Billing + BYOK | Stripe, planos Free/Pro, cadastro API key LLM |
| 12 | Polish + launch | Onboarding wizard, guided first query, landing page |
<!-- /region: REG-BACK-01 -->

<!-- region: REG-EXEC-04 -->
### Próximos Passos

**Antes do desenvolvimento (semana 0):**

1. Confirmar reserva financeira de R$ 184K (ou fonte de financiamento)
2. Mapear 20 empresas da rede pessoal com BigQuery para beta program
3. Formalizar acordo com 1-2 freelancers para contingência
4. Criar projeto GCP com créditos

**Durante o desenvolvimento:**

5. Convidar 5 empresas para beta (semana 8-10)
6. Instrumentar métricas de precisão desde a semana 5
7. Documentar ADRs continuamente

**Pós-launch:**

8. Go/No-Go Gate 1 (mês 4): produto funcional + 3 tenants beta
9. Beta program: onboarding assistido, feedback, conversão
10. Go/No-Go Gate 2 (mês 7): 1+ pagante, NPS >30
<!-- /region: REG-EXEC-04 -->

<!-- region: REG-EXEC-05 -->
### Decisões Consolidadas (78 decisões — seleção das principais)

| # | Decisão | Status |
|---|---------|--------|
| D1.3 | BYOK obrigatório a partir do Pro | Confirmada |
| D1.4 | Pool LLM subsidiado para Free (Gemini Flash, 50 queries/mês) | Recomendada → Aceita |
| D2.3 | Guided First Query no onboarding | Recomendada → Aceita |
| D3.1 | Pro a R$ 497/mês | Confirmada |
| D3.6 | Break-even real: 27 Pro + 3 Enterprise | Confirmada |
| D4.1 | Equipe = 1 arquiteto + Claude Code | Confirmada |
| D4.8 | Kill criteria definidos | Recomendada → Aceita |
| D5.1 | Row-level isolation + dataset isolation | Confirmada |
| D5.3 | Pipeline NL-to-SQL com RAG (sem fine-tuning) | Confirmada |
| D6.4 | Schema abstrato nos prompts (sem sample data) | Recomendada ��� Aceita |
| D7.1 | Modular Monolith | Confirmada |
| D8.1 | Projeto viável — break-even m��s 19 | Confirmada |
| D8.3 | Margem bruta 86-94% (BYOK) | Confirmada |
| D8.4 | Build vs Buy: 840h economizadas | Confirmada |
<!-- /region: REG-EXEC-05 -->

<!-- region: REG-GLOSS-01 -->
### Glossário

| Termo | Definição |
|-------|-----------|
| BYOK | Bring Your Own Key — modelo onde o tenant cadastra sua própria API key de LLM |
| MCP | Model Context Protocol — protocolo para integração com fontes de conhecimento externas |
| NL-to-SQL | Conversão de linguagem natural em queries SQL |
| RAG | Retrieval-Augmented Generation — enriquecimento de contexto via busca vetorial |
| Tenant | Organização-cliente que usa o Veezoozin (cada empresa é um tenant) |
| RBAC | Role-Based Access Control — controle de acesso baseado em papéis |
| PLG | Product-Led Growth — estratégia de crescimento liderada pelo produto |
| MRR | Monthly Recurring Revenue — receita recorrente mensal |
| NRR | Net Revenue Retention — retenção líquida de receita |
| TCO | Total Cost of Ownership — custo total de propriedade |
| DPA | Data Processing Agreement — acordo de processamento de dados |
| DPO | Data Protection Officer — encarregado de proteção de dados |
| LGPD | Lei Geral de Proteção de Dados — legislação brasileira de privacidade |
| ADR | Architecture Decision Record — registro de decisão arquitetural |
| SLA | Service Level Agreement — acordo de nível de serviço |
| SLO | Service Level Objective — objetivo de nível de serviço |
| CAC | Customer Acquisition Cost — custo de aquisição de cliente |
| LTV | Lifetime Value — valor do tempo de vida do cliente |
| Glossário (produto) | Dicionário de termos de negócio por tenant que contextualiza as queries NL |
| Guided First Query | Feature de onboarding que sugere a primeira query baseada no schema mapeado |
<!-- /region: REG-GLOSS-01 -->

---

> **Discovery Pipeline completo.** Run 3, Iteração 1. 8 blocos discovery + 2 blocos challenge + delivery report. Projeto Veezoozin: **VIÁVEL**.
