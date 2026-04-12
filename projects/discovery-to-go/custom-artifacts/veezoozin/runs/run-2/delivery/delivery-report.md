---
title: "Delivery Report — Veezoozin"
description: "Relatorio consolidado de Discovery para o projeto Veezoozin — plataforma SaaS de consulta em linguagem natural sobre bancos de dados corporativos"
project-name: "veezoozin"
client: "mAInd Tech"
author: "consolidator"
category: delivery
version: "02.00.000"
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
run: run-2
flags:
  - BELOW-THRESHOLD
  - VIABILIDADE-NEGATIVA
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

> Relatorio consolidado do Discovery Pipeline — Run 2, Iteracao 1
> Projeto: **Veezoozin** | Cliente: **mAInd Tech** | Data: 2026-04-12

> [!danger] BELOW-THRESHOLD + VIABILIDADE-NEGATIVA
> **Scores abaixo do threshold configurado.** Auditor: 71,4% | 10th-man: 57,8% | Threshold: >=90% (poc).
> **Viabilidade financeira negativa.** Receita projetada (R$ 2,4M) cobre apenas 23,3% do TCO (R$ 10,5M) em 3 anos no cenario base. Nenhum cenario alternativo fecha o deficit acumulado em 3 anos sem captacao de investimento externo. O cenario mais viavel (D — pricing + crescimento) atinge break-even mensal apenas no mes ~24, com cobertura de 59% do TCO e deficit acumulado de R$ 4,8M.
> **Em modo real, o pipeline teria pausado para revisao humana obrigatoria.** Este relatorio avancou em modo simulacao com os flags registrados.

---

<!-- region: REG-EXEC-01 -->
## Resumo Executivo

O Veezoozin e uma plataforma SaaS conversational-first que converte perguntas em linguagem natural (PT-BR, EN-US, ES) em queries SQL contextualizadas pelo dominio de negocio de cada tenant, retornando graficos, insights e analises em segundos. Utiliza stack GCP-first (Cloud Run, BigQuery, Vertex AI) com LLMs externos (Claude + Gemini) e integracao MCP para fontes de conhecimento externas.

**Metricas-chave do Discovery:**

| Metrica | Valor |
|---------|-------|
| TCO 3 anos (cenario base) | R$ 10.510.000 |
| Receita projetada 3 anos | R$ 2.447.000 (base) a R$ 7.016.000 (cenario D) |
| Deficit acumulado 3 anos | R$ -8.063.000 (base) a R$ -4.844.000 (cenario D) |
| Break-even mensal | Nunca (base) / Mes ~24 (cenario D) |
| Investimento MVP | R$ 346.000 (4 meses) |
| Score Auditor | 71,4% |
| Score 10th-man | 57,8% |
| Threshold | >=90% (poc) |
| Recomendacao Go/No-Go | **GO CONDICIONAL — exige resolucao de viabilidade financeira, captacao de investimento, e validacao de mercado** |

**Destaques positivos:** Pipeline NL-to-SQL com 8 etapas e privacy guard (excelencia tecnica), LGPD em modo profundo completo, Build vs Buy disciplinado (6 componentes), arquitetura modular monolith adequada ao time enxuto, cadeia de 56 decisoes rastreadas (D1-D56).

**Alertas criticos:** Viabilidade financeira negativa no cenario base, mercado enderecavel nao dimensionado (TAM/SAM/SOM ausente), ausencia de go-to-market tatico, moat competitivo fragil (replicavel em 6-12 meses), dependencia de premissas otimistas simultaneas no cenario D.
<!-- /region: REG-EXEC-01 -->

---

<!-- region: REG-EXEC-02 -->
## Visao Geral do Projeto

| Campo | Valor |
|-------|-------|
| **Projeto** | Veezoozin |
| **Cliente** | mAInd Tech (startup de tecnologia) |
| **Tipo de projeto** | Novo produto (greenfield) |
| **Context-Templates** | SaaS + AI/ML + Datalake-Ingestion |
| **Duracao do Discovery** | Run 2, Iteracao 1 — 8 blocos discovery + 2 blocos challenge |
| **Setup do Relatorio** | Executive |
| **Data Source Breakdown** | Briefing ~60% / Inference ~35% / RAG ~5% |
| **Confianca Geral** | Media — inconsistencias detectadas (pricing 1.3 vs 1.8, breakeven 1.3 vs 1.8) |
| **Flags** | [BELOW-THRESHOLD] [VIABILIDADE-NEGATIVA] |
<!-- /region: REG-EXEC-02 -->

---

<!-- region: REG-EXEC-03 -->
## Go/No-Go

> [!warning] GO CONDICIONAL
> Este discovery nao recomenda um GO simples. A excelencia tecnica (pipeline NL-to-SQL, LGPD, arquitetura) e contrastada por fragilidade financeira significativa. Avancar para desenvolvimento **exige** resolucao das condicoes abaixo.

**Scores de validacao:**

| Validador | Score | Threshold | Status |
|-----------|:-----:|:---------:|--------|
| Auditor (convergente) | 71,4% | >=90% | BELOW-THRESHOLD |
| 10th-man (divergente) | 57,8% | >=90% | BELOW-THRESHOLD |
| Veredicto auditor | APROVADO COM RESSALVAS | — | — |
| Veredicto 10th-man | APROVADO COM RESSALVAS GRAVES | — | — |

**Condicoes obrigatorias para GO:**

1. Definir estrategia de captacao de investimento (Pre-seed ~R$ 1,5M) com timeline, investidores-alvo, e plano B
2. Dimensionar mercado (TAM/SAM/SOM) — validar se 300 tenants pagantes no mes 36 e alcancavel
3. Confirmar pelo menos 3 LOIs (Letters of Intent) de early adopters antes de iniciar desenvolvimento
4. Resolver conflito de pricing: D11 (R$ 497) vs D51 (R$ 697) — definir e atualizar ambos os blocos
5. Contratar DPO terceirizado antes do lancamento (nao na Fase 2)
6. Reduzir meta de precisao NL-to-SQL do MVP para >75% (nao 85%), com plano de evolucao para 85% no mes 6
<!-- /region: REG-EXEC-03 -->

---

## Produto e Valor

<!-- region: REG-PROD-01 -->
### Problema Central

O Veezoozin resolve um problema estrutural: **dados valiosos existem nas empresas, mas estao presos atras de barreiras tecnicas**.

| Dimensao | Descricao | Impacto |
|----------|-----------|---------|
| **Barreira tecnica** | Gestores e executivos dependem de times de dados para obter respostas. Uma pergunta simples vira um ticket que leva dias. | Decisoes atrasadas, custo operacional alto |
| **Falta de contexto de negocio** | Ferramentas de BI genericas nao entendem o vocabulario do cliente. "Churn" significa coisas diferentes em cada empresa. | Respostas imprecisas, retrabalho |
| **Dados sem acao** | O usuario recebe tabelas brutas sem insights. Falta a camada de interpretacao. | Dados acessados mas nao utilizados |
| **Multi-idioma** | Empresas latinas operam em PT-BR, EN-US e Espanhol. | Exclusao de usuarios, adocao limitada |

**Impacto mensuravel esperado:** Tempo de resposta de dias para segundos, democratizacao de 5-10% para 100% dos colaboradores, reducao de 60-80% no volume de tickets para o time de dados.
<!-- /region: REG-PROD-01 -->

<!-- region: REG-PROD-02 -->
### Personas

| Persona | Arquetipo | Perfil | JTBD | Frequencia | Tier |
|---------|-----------|--------|------|:----------:|------|
| **P0 — Gestora** | Marina, Diretora Comercial | 38 anos, MBA, nao sabe SQL | Perguntar sobre KPIs e receber graficos prontos em segundos | Diario (2-5/dia) | Pro/Enterprise |
| **P0 — Analista** | Rafael, Analista de BI | 29 anos, sabe SQL basico, gasta 70% em queries repetitivas | Cruzar dados sem escrever SQL, foco em analise | Diario (10-20/dia) | Pro |
| **P1 — Admin Tenant** | Lucas, Lider de Dados | 34 anos, engenheiro de dados | Ensinar o sistema sobre o dominio de negocio | Semanal | Todos |
| **P1 — Admin TI** | Carla, Coord. de Infra | 41 anos, 15 anos de exp. | Garantir read-only, LGPD, auditoria — **poder de veto** | Mensal | Enterprise |

**Matriz de influencia:**
- Marina (Gestora): influenciadora principal — "Funciona? E rapido?"
- Rafael (Analista): validador tecnico — "As queries estao corretas?"
- Lucas (Admin Tenant): viabilizador — "Consigo ensinar o sistema em < 1 dia?"
- Carla (Admin TI): poder de veto — "E read-only? Tem LGPD? Tem log?"
<!-- /region: REG-PROD-02 -->

<!-- region: REG-PROD-04 -->
### Proposta de Valor e Diferenciacao

| Concorrente | Limitacao principal | Vantagem Veezoozin |
|-------------|--------------------|--------------------|
| Tableau Ask Data | Funciona apenas dentro do Tableau, suporte limitado a idiomas | Standalone, multi-idioma nativo |
| ThoughtSpot | Pricing enterprise elevado, schema rigido | Acessivel para PMEs, schema flexivel por tenant |
| ChatGPT + SQL | Sem contexto de negocio, sem multi-tenancy | Glossario por tenant, historico, aprendizado |
| Metabase | Dashboard-first, nao conversacional | Conversational-first com output visual rico |

**Moat declarado:** Contexto de negocio por tenant + multi-idioma nativo + integracao MCP.

> [!warning] Alerta 10th-man
> Multi-idioma nao e moat sustentavel (LLMs ja entendem 100+ idiomas). Glossario e replicavel em 3-6 meses. MCP e Fase 2, nao MVP. O moat real (nao articulado) seria o **efeito de rede de contexto acumulado** — quanto mais o tenant usa, melhor o sistema fica. Mas depende de retencao alta.
<!-- /region: REG-PROD-04 -->

<!-- region: REG-PROD-05 -->
### OKRs do MVP e ROI

**O1: Validar product-market fit com early adopters**

| KR | Metrica | Alvo |
|----|---------|:----:|
| KR1.1 | Tenants ativos (Free + Pro) | >= 12 |
| KR1.2 | Queries corretas na 1a tentativa | > 85% (10th-man recomenda > 75%) |
| KR1.3 | NPS dos primeiros 20 usuarios | > 40 |

**O2: Demonstrar valor real no dia a dia**

| KR | Metrica | Alvo |
|----|---------|:----:|
| KR2.1 | Consultas por usuario ativo/dia | > 3 |
| KR2.2 | Taxa de aceitacao de sugestoes de prompt | > 40% |
| KR2.3 | Tempo medio de resposta (queries simples) | < 5 seg |

**O3: Onboarding eficiente e escalavel**

| KR | Metrica | Alvo |
|----|---------|:----:|
| KR3.1 | Tempo de onboarding (Free) | < 30 min |
| KR3.2 | Tempo de onboarding (Pro) | < 2 horas |
| KR3.3 | % de signups que completam onboarding | > 60% |

**ROI para o cliente:**

| Cenario | Custo Veezoozin | Economia estimada | ROI |
|---------|:---------------:|:-----------------:|:---:|
| PME (20 func.) | R$ 497/mes (Pro) | ~R$ 5.000/mes | ~900% |
| Media empresa (100 func.) | R$ 1.997/mes (Ent) | ~R$ 14.000/mes | ~600% |
<!-- /region: REG-PROD-05 -->

<!-- region: REG-PROD-06 -->
### Modelo Comercial e Pricing

**Modelo:** SaaS freemium + tiered + usage-based.

| Aspecto | Free | Pro | Enterprise |
|---------|------|-----|------------|
| **Preco mensal** | R$ 0 | R$ 497/mes (D11) | R$ 1.997/mes base (D11) |
| **Queries/dia** | 10 | Ilimitadas (fair use 5.000/mes) | Ilimitadas |
| **Fontes de dados** | 1 (BigQuery) | 3 | Ilimitadas |
| **Tabelas** | 5 | 50 | Ilimitadas |
| **Usuarios** | 2 | 10 (+ R$ 29/extra) | Ilimitados |
| **Glossario** | Templates genericos | Customizacao completa | Custom + consultoria |
| **MCP / RAG** | Nao | 1 fonte | Ilimitado |
| **Controle de acesso** | Por tabela | + por campo | + por registro (RLS) |
| **SSO** | Nao | Nao | Sim |
| **SLA** | Best-effort | 99,5% | 99,9% |

> [!warning] Conflito de pricing em aberto
> D11 (Bloco 1.3) define Pro a R$ 497 como "Confirmada". D51 (Bloco 1.8) recomenda Pro a R$ 697 (+40%) para viabilidade financeira. **Ambas coexistem como validas — deve ser resolvido antes do lancamento.** O cenario D (mais viavel) depende do pricing D51.

**Estrategia de trial:** 14 dias Pro completo, sem cartao de credito. Conversao esperada ~25% dos trials, ~10% total signup-to-paid.
<!-- /region: REG-PROD-06 -->

<!-- region: REG-PROD-07 -->
### Escopo do MVP

**Dentro do escopo:**
- Interface conversacional web (PT-BR, EN-US, ES)
- Engine NL-to-SQL com glossario por tenant (BigQuery apenas no MVP)
- Graficos automaticos, insights textuais, sugestoes de proximas perguntas
- Controle de acesso por tabela (Free), campo (Pro), registro/RLS (Enterprise)
- Billing via Stripe (assinatura + usage), planos Free/Pro/Enterprise
- Multi-tenant row-level (tenant_id)
- LGPD: read-only, privacy guard, auditoria

**Fora do escopo:**
- Escrita/modificacao de dados nos bancos do cliente
- Fine-tuning de LLM proprio
- ETL/ingestao de dados
- App mobile nativo
- Multi-banco (PostgreSQL, MySQL, SQL Server) — Fase 2
- MCP/RAG externo — Fase 2
- SSO/SAML — Fase 2

**Roadmap:**

| Fase | Prazo | Escopo principal |
|------|-------|------------------|
| MVP | 4 meses (16 semanas) | NL-to-SQL + BigQuery + 3 idiomas + 5 tenants + Free/Pro |
| Fase 2 | +3 meses | Multi-banco + MCPs + RAG + SSO + Enterprise |
| Fase 3 | +3 meses | Preditivo + alertas + agentes autonomos + marketplace |
<!-- /region: REG-PROD-07 -->

---

## Organizacao

<!-- region: REG-ORG-01 -->
### Time e Stakeholders

**Time MVP (6 pessoas):**

| Papel | Qtd | Senioridade | Custo/mes | Status |
|-------|:---:|:-----------:|:---------:|--------|
| CTO / Arquiteto (Fabio) | 1 | Senior+ | Socio (nao contabilizado) | Existente |
| Product Owner | 1 | Pleno-Senior | R$ 15.000 | A contratar |
| Backend NL-to-SQL | 1 | Senior | R$ 22.000 | A contratar |
| Backend Platform | 1 | Pleno-Senior | R$ 18.000 | A contratar |
| Frontend | 1 | Pleno | R$ 14.000 | A contratar |
| Designer UX/UI | 1 | Pleno | R$ 6.000 | Freelancer |
| **Total** | **6** | — | **R$ 75.000/mes** | 4 contratacoes + 1 freelancer |

**Custo total MVP (4 meses):** R$ 346.000 (time R$ 300K + infra R$ 16K + marketing R$ 30K)

**Stakeholders:**
- Fabio (CTO): Sponsor + Arquiteto — aprova arquitetura e budget
- PO (a contratar): Backlog + validacao com early adopters
- Tech Lead (a contratar): Decisoes de implementacao

> [!warning] Alerta 10th-man
> Bus factor critico. Se o Backend Senior NL-to-SQL nao for encontrado em 30 dias, nao ha plano B realista. Fabio (CTO) ja acumula: arquitetura, code review, mentoria, PO interino, DPO interino.
<!-- /region: REG-ORG-01 -->

<!-- region: REG-ORG-02 -->
### Metodologia e Operacao

| Aspecto | Decisao |
|---------|---------|
| **Metodologia** | Scrum adaptado, sprints de 1 semana |
| **Repositorio** | Monorepo (GitHub) |
| **Branching** | Trunk-based + feature flags |
| **Deploy** | Diario (Cloud Run rolling update) |
| **CI/CD** | Cloud Build + GitHub Actions |
| **On-call** | Rotacao semanal, horario comercial no MVP |

**SLOs por tier:**

| SLO | Free | Pro | Enterprise |
|-----|:----:|:---:|:----------:|
| Disponibilidade | Best-effort | >= 99,5% | >= 99,9% |
| Latencia p50 | < 8s | < 5s | < 3s |
| Precisao de query | > 80% | > 85% | > 90% |
<!-- /region: REG-ORG-02 -->

---

## Arquitetura Tecnica

<!-- region: REG-TECH-01 -->
### Stack Tecnologica

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| **Cloud** | GCP (obrigatorio) | Cliente com creditos e incentivos |
| **Compute** | Cloud Run (serverless) | Custo proporcional, auto-scaling |
| **Backend API** | Python (FastAPI) | Briefing: Python obrigatorio. Async, tipagem, docs OpenAPI |
| **NL-to-SQL Engine** | LangChain + custom | Orquestracao de prompts + camada custom (glossario, RLS, validacao) |
| **Frontend** | TypeScript + React + Next.js | SSR, ecossistema rico para graficos (Recharts/Nivo) |
| **Metadata** | Cloud SQL (PostgreSQL) | Tenants, users, glossario, roles, permissoes |
| **Cache/Sessoes** | Firestore | Historico, cache de queries, sessoes |
| **Analytics** | BigQuery (read-only) | Unico banco suportado no MVP |
| **LLM Primario** | Claude API (Anthropic) | Melhor SQL generation, contexto longo 200K tokens |
| **LLM Secundario** | Gemini API (Vertex AI) | Fallback, A/B testing, creditos GCP |
| **Embeddings** | Vertex AI Text Embeddings | Semantic search no schema/glossario |
| **Billing** | Stripe | Buy, nao Build. Assinatura + usage nativo |
| **Auth** | Firebase Auth | GCP-native, suporte SAML/OIDC na Fase 2 |
| **WAF** | Cloud Armor | DDoS, rate limit global |
<!-- /region: REG-TECH-01 -->

<!-- region: REG-TECH-02 -->
### Pipeline NL-to-SQL (8 Etapas)

| Etapa | Responsabilidade | Latencia alvo |
|-------|-----------------|:-------------:|
| 1. Input | Detectar idioma, normalizar texto | < 100ms |
| 2. Context Assembly | Schema + glossario + historico + permissoes via embeddings | < 500ms |
| 3. SQL Generation | LLM gera SQL (Claude primario, Gemini fallback) | < 2s |
| 4. Validate + Guard | sqlglot parse, AST validation, RLS injection, read-only check | < 200ms |
| 5. Execute | BigQuery read-only via service account do tenant | < 2s (p50) |
| 6. Result Process | Detectar tipo grafico, formatar dados, paginar | < 300ms |
| 7. Insight Generation | LLM interpreta resultados com privacy guard (D35) | < 1,5s |
| 8. Output | JSON: dados + grafico + insight + sugestao | — |

**Latencia total alvo:** < 5 segundos (p50)

**Cache de 4 camadas:** exact match (15%), semantic match (25%), schema cache, result cache. Economia projetada de 30-40% em chamadas LLM.

> [!warning] Alerta 10th-man
> Cache hit rate projetado de 35-50% pode ser otimista. Cache e por-tenant (isola volume), TTL de 24h em dados transacionais serve dados desatualizados, e normalizacao para exact match precisa ser muito agressiva. Projecao conservadora: 15-20%.
<!-- /region: REG-TECH-02 -->

<!-- region: REG-TECH-03 -->
### Arquitetura — Modular Monolith

**Padrao:** Modular Monolith com 6 modulos + Shared Kernel. Deploy unico em Cloud Run (single container).

| Modulo | Responsabilidade | Fase |
|--------|-----------------|:----:|
| **NL-to-SQL Engine** | Pipeline completo de 8 etapas | MVP |
| **Tenant Context** | Schema discovery, glossario, embeddings, historico, permissoes | MVP |
| **Visualization & Output** | Graficos, insights, export PDF/HTML, sugestoes | MVP |
| **Admin Panel** | Users, roles (RBAC), feature flags, audit logs | MVP |
| **MCP Gateway** | Integracao com fontes externas via MCP | Fase 2 |
| **Billing Module** | Stripe webhooks, usage metering, limites por plano | MVP |
| **Shared Kernel** | Auth middleware, tenant middleware, RBAC engine, rate limiter, event bus, observability, privacy guard | MVP |

**Justificativa:** Time de 6 pessoas (D17) nao consegue operar microservices. Deploy unico, um pipeline CI/CD, refactoring global. Boundaries claros permitem extrair microservices quando o time crescer (Fase 2/3).

**Multi-tenant:** Row-level (tenant_id) no MVP com 6 camadas de isolamento (rede, auth, API gateway, aplicacao, banco, dados do tenant). Database dedicado para Enterprise na Fase 2.
<!-- /region: REG-TECH-03 -->

---

## Privacidade e Seguranca

<!-- region: REG-SEC-01 -->
### Seguranca

**Seguranca em camadas:**

| Camada | Controle |
|--------|----------|
| Transporte | TLS 1.3 obrigatorio |
| Autenticacao | JWT + 2FA (TOTP), Firebase Auth |
| Autorizacao | RBAC + RLS (controle por tabela/campo/registro) |
| SQL Injection | sqlglot parser, AST validation, whitelist de funcoes |
| Query sandboxing | Read-only, timeout 30s, LIMIT por plano |
| Secrets | Secret Manager (GCP), rotacao automatica |
| Criptografia at-rest | AES-256 (Google-managed) |
| WAF | Cloud Armor (DDoS, rate limit) |
| Scanning | Container scanning (Artifact Registry) + Dependabot |

**Seguranca especifica NL-to-SQL:**
- Prompt injection: separacao de prompt do sistema vs input do usuario, validacao SQL independente
- SQL injection via LLM: sqlglot parse, whitelist, AST validation, nenhum DML/DDL
- Data exfiltration: RLS injection, LIMIT obrigatorio, log de toda query
<!-- /region: REG-SEC-01 -->

<!-- region: REG-PRIV-01 -->
### Privacidade e LGPD

**Modo:** Profundo (obrigatorio — SaaS multi-tenant com PII em queries e chamadas LLM externas).

**Papeis LGPD:**
- mAInd Tech como **Controladora** dos dados de conta/uso dos usuarios
- mAInd Tech como **Operadora** dos dados do banco do tenant (PII dos clientes do tenant)
- DPA obrigatorio com cada tenant e sub-processador

**Sub-processadores:**

| Sub-processador | Dados que recebe | Residencia |
|-----------------|-----------------|:----------:|
| Anthropic (Claude) | Perguntas NL + contexto do tenant | EUA |
| Google (Gemini/Vertex AI) | Perguntas NL + contexto (fallback) | BR/EUA |
| Stripe | Dados de pagamento | EUA |
| SendGrid/Resend | Email + nome | EUA |
| GCP (infra) | Todos os dados | BR (southamerica-east1) |

**Classificacao de dados:**
- Critico: dados do banco do tenant (PII transitando, nao armazenado)
- Sensivel: auth + billing
- Pessoal: conta + uso + logs
- Nao pessoal: glossario, schema, embeddings

**Retencao:** Historico de 7 dias (Free) / 90 dias (Pro) / 365 dias (Enterprise). Resultados de queries nao persistidos. Exclusao em 3 fases: soft-delete (D+0) → anonimizacao (D+30) → hard-delete (D+60).

**Pendencias criticas antes do lancamento:**
- DPAs com todos os sub-processadores (Anthropic, Google, Stripe, email provider)
- RIPD elaborado (semana 13-14)
- Politica de privacidade publicada
- Cookie consent banner implementado

> [!danger] DPO — Risco regulatorio
> D34 define Fabio (CTO) como DPO interino no MVP. 10th-man alerta: conflito de interesse estrutural (juiz e parte na mesma pessoa). ANPD pode questionar. **Recomendacao: contratar DPO terceirizado (~R$ 2.000/mes) antes do lancamento, nao na Fase 2.**
<!-- /region: REG-PRIV-01 -->

---

## Analise Financeira

<!-- region: REG-FIN-01 -->
### TCO — 3 Anos (Fonte de verdade: Bloco 1.8)

| Categoria | Ano 1 (R$) | Ano 2 (R$) | Ano 3 (R$) | Total 3a (R$) | % |
|-----------|:----------:|:----------:|:----------:|:-------------:|:---:|
| **Equipe** | 1.350.000 | 2.520.000 | 3.120.000 | **6.990.000** | 66,5% |
| **LLM APIs** | 180.000 | 504.000 | 780.000 | **1.464.000** | 13,9% |
| **Marketing** | 190.000 | 480.000 | 720.000 | **1.390.000** | 13,2% |
| **Infra GCP** | 83.000 | 310.000 | 580.000 | **973.000** | 9,3% |
| **SaaS terceiros** | 42.000 | 113.000 | 208.000 | **363.000** | 3,5% |
| **TOTAL** | **1.845.000** | **3.927.000** | **5.408.000** | **10.510.000** | 100% |

> Creditos GCP podem reduzir ~30% da infra. TCO ajustado: ~R$ 9.778.000.

**Receita projetada (cenario base conservador):**

| Periodo | Tenants Pro | Tenants Ent | MRR fim (R$) | Receita periodo (R$) |
|---------|:-----------:|:-----------:|:------------:|:--------------------:|
| Mes 1-4 (MVP) | 0 | 0 | 0 | 0 |
| Mes 5-12 | 2 → 40 | 0 → 6 | 994 → 31.862 | 148.000 |
| Ano 2 | 40 → 80 | 6 → 15 | 31.862 → 89.400 | 726.000 |
| Ano 3 | 80 → 150 | 15 → 30 | 89.400 → 173.250 | 1.573.000 |
| **Total** | — | — | — | **2.447.000** |

**Break-even:**
- Cenario base: **Nunca** em 3 anos. Receita cobre 23,3% do TCO.
- Deficit: R$ -8.063.000

> [!danger] Inconsistencia detectada pelo Auditor (F2)
> O Bloco 1.3 projetava breakeven em "mes 10-12 pos-lancamento" (D15). O Bloco 1.8 com TCO completo mostra que isso era apenas margem bruta (infra vs MRR), nao TCO total incluindo equipe, marketing e LLM APIs. O breakeven real no cenario base **nao e atingido em 3 anos.**
<!-- /region: REG-FIN-01 -->

<!-- region: REG-FIN-05 -->
### Build vs Buy

| Componente | Decisao | Custo 3a (R$) | TTM | Justificativa |
|-----------|:-------:|:-------------:|:---:|---------------|
| **NL-to-SQL Engine** | BUILD | ~0 (dev na equipe) | 4-6 sem | Core product, moat competitivo |
| **Vector Store** | BUY (Vertex AI) | ~180.000 | < 1 sem | Infra, nao diferencial |
| **LLM** | BUY (Claude + Gemini) | ~1.464.000 | 1 dia | D3, qualidade + TTM |
| **Auth** | BUY (Firebase) | ~10.000 | < 1 sem | Seguranca critica |
| **Visualizacao** | BUY (Recharts/Nivo) | 0 (OSS) | 1-2 sem | Nao e moat |
| **Billing** | BUY (Stripe) | ~340.000 | < 1 sem | Antipattern #2 do blueprint SaaS |

**Padrao:** Build apenas o que e diferencial competitivo (NL-to-SQL Engine). Buy tudo que e commodity.
<!-- /region: REG-FIN-05 -->

<!-- region: REG-FIN-07 -->
### Cenarios Alternativos de Viabilidade

> Cenarios gerados pelo Bloco 1.8 (P22) porque receita < TCO no cenario base.

| Metrica | Base | A (Pricing) | B (Escopo) | C (Crescimento) | D (A+C) |
|---------|:----:|:-----------:|:----------:|:----------------:|:-------:|
| Pricing Pro | R$ 497 | R$ 697 | R$ 497 | R$ 497 | R$ 697 |
| Pricing Enterprise | R$ 1.997 | R$ 2.997 | R$ 1.997 | R$ 1.997 | R$ 2.997 |
| Tenants pagantes mes 12 | 46 | 46 | 46 | 60 | 60 |
| Tenants pagantes mes 36 | 180 | 180 | 180 | 300 | 300 |
| **Receita 3 anos** | R$ 2,4M | R$ 3,4M | R$ 2,2M | R$ 4,9M | **R$ 7,0M** |
| **TCO 3 anos** | R$ 10,5M | R$ 10,5M | R$ 6,6M | R$ 11,9M | **R$ 11,9M** |
| **Deficit** | -R$ 8,1M | -R$ 7,1M | -R$ 4,4M | -R$ 6,9M | **-R$ 4,8M** |
| **Cobertura** | 23% | 33% | 33% | 42% | **59%** |
| **Break-even mensal** | Nunca | Nunca | Mes ~32 | Mes ~30 | **Mes ~24** |

**Cenario D (mais viavel):** Exige pricing 40% acima + crescimento 5x em 2 anos + cache efetivo + ticket Enterprise alto. O 10th-man estima probabilidade conjunta como **baixa** — se 2 das 5 premissas falharem, cobertura cai para ~34%.

**Recomendacao estrategica do Bloco 1.8:**
1. Lancar com pricing Pro R$ 697, Enterprise R$ 2.997
2. Foco em Enterprise desde o mes 6 (contratar SDR)
3. Cache agressivo desde o MVP
4. Migrar 40% do trafego LLM para Gemini ate mes 12
5. Negociar creditos GCP agressivamente
6. Revisar headcount trimestralmente

**Gatilhos Go/No-Go:**

| Marco | Metrica | Minimo aceitavel | Acao se nao atingir |
|-------|---------|:-----------------:|---------------------|
| Mes 8 | Tenants pagantes | >= 8 Pro + 1 Enterprise | Rever pricing/posicionamento, considerar pivot |
| Mes 12 | MRR | >= R$ 30.000 | Rever equipe, considerar cenario B |
| Mes 18 | MRR | >= R$ 80.000 | Se < R$ 50K: cenario B agressivo |
| Mes 24 | Break-even mensal | MRR >= custos mensais | Avaliar captacao ou reducao para equipe minima |

**Investimento necessario:**

| Fase | Investimento acumulado | Fonte sugerida |
|------|:----------------------:|----------------|
| MVP (4 meses) | R$ 338.000 | Bootstrap (socios) |
| Ano 1 | R$ 1.845.000 | Bootstrap + Angel/Pre-seed (~R$ 1,5M) |
| Ano 2 | R$ 3.927.000 | Seed round (~R$ 3-5M) |
| Ano 3 | R$ 5.408.000 | Series A |
<!-- /region: REG-FIN-07 -->

---

## Riscos e Recomendacoes

<!-- region: REG-RISK-01 -->
### Riscos Consolidados

| # | Risco | Prob. | Impacto | Fonte | Mitigacao |
|---|-------|:-----:|:-------:|:-----:|-----------|
| 1 | **Viabilidade financeira negativa** — receita cobre 23% do TCO em 3 anos | Alta | Critico | 1.8, 2.1, 2.2 | Cenario D (pricing + crescimento), captacao de investimento, gatilhos Go/No-Go trimestrais |
| 2 | **Mercado enderecavel nao dimensionado** — "BigQuery no Brasil" pode ser nicho insuficiente | Alta | Critico | 2.2 | Dimensionar TAM/SAM/SOM antes de iniciar. Validar LOIs. |
| 3 | **Precisao NL-to-SQL < 85% no MVP** — realista e 65-75% com schemas desconhecidos | Media | Alto | 1.1, 2.2 | Meta MVP > 75% (nao 85%), feedback loop agressivo, evolucao para 85% no mes 6 |
| 4 | **Cross-tenant data leak** via bug no row-level filtering | Baixa | Critico | 1.5, 1.7 | 6 camadas de isolamento, RLS no PostgreSQL, testes automatizados de isolamento |
| 5 | **DPO acumulado pelo CTO** — conflito de interesse, risco regulatorio | Alta | Alto | 1.6, 2.2 | Contratar DPO terceirizado antes do lancamento (~R$ 2.000/mes) |
| 6 | **Custo de LLM APIs explode com escala** | Media | Alto | 1.5, 1.8 | Cache 4 camadas, migracao gradual para Gemini, otimizacao de prompts |
| 7 | **Ausencia de go-to-market** — sem equipe de vendas, sem early adopters confirmados | Alta | Alto | 2.2 | Confirmar LOIs, contratar SDR no mes 6, partnership com consultores de dados |
| 8 | **PII transitando em chamadas LLM** sem controle adequado | Alta | Alto | 1.6 | Privacy guard (D35), minimizacao de dados, DPA com Anthropic/Google |
| 9 | **Dificuldade de contratar Backend Senior NL-to-SQL** | Alta | Alto | 1.4 | Iniciar busca imediatamente, fallback CTO + junior com mentoria |
| 10 | **Enterprise adocao mais lenta** — sem SSO no MVP, ciclo de venda longo | Alta | Alto | 2.2 | Projetar 2-3 Enterprise no mes 12 (nao 6-10), focar em Pro/PLG inicialmente |
<!-- /region: REG-RISK-01 -->

---

## Quality Gates

<!-- region: REG-QUAL-01 -->
### Auditoria (Validacao Convergente)

**Score global: 71,4%** | Veredicto: APROVADO COM RESSALVAS

| Dimensao | Score | Peso | Ponderado |
|----------|:-----:|:----:|:---------:|
| Cobertura | 85% | 20% | 17,0 |
| Profundidade | 68% | 25% | 17,0 |
| Consistencia | 78% | 20% | 15,6 |
| Fundamentacao | 72% | 15% | 10,8 |
| Completude | 55% | 20% | 11,0 |

**Findings criticos (Auditor):**
- F1: Viabilidade financeira negativa — cenario base cobre 23% do TCO. Nenhum cenario fecha deficit sem investimento externo
- F2: Inconsistencia breakeven — Bloco 1.3 (mes 10-12) vs Bloco 1.8 (nunca no cenario base)
- F3: Pricing contraditorio — D11 (R$ 497 Confirmada) vs D51 (R$ 697 Recomendacao)

**Findings importantes:**
- F4: Mitigacoes de risco genericas nos blocos 1.1-1.4
- F5: Tags [BRIEFING]/[INFERENCE] nao preservadas nos blocos 1.1-1.4
- F6: Falta TAM/SAM/SOM
<!-- /region: REG-QUAL-01 -->

<!-- region: REG-QUAL-02 -->
### 10th-man (Validacao Divergente)

**Score global: 57,8%** | Veredicto: APROVADO COM RESSALVAS GRAVES

| Dimensao | Score | Peso | Ponderado |
|----------|:-----:|:----:|:---------:|
| Divergencia | 45% | 35% | 15,8 |
| Robustez | 60% | 35% | 21,0 |
| Completude Critica | 70% | 30% | 21,0 |

**Premissas desafiadas:**
- P1: Precisao NL-to-SQL > 85% no MVP — realista e 65-75%, recomenda > 75% como meta
- P2: Custos GCP subestimados — Vertex AI Vector Search cobra por hora (fixo), BigQuery on-demand pode ser 3-5x maior sem particionar
- P3: Moat competitivo replicavel — multi-idioma e table stakes, glossario copiavel em 3-6 meses, MCP e Fase 2
- P4: Enterprise adocao otimista — ciclo de venda 6-12 meses, sem SSO no MVP, sem certificacoes
- P5: DPO acumulado CTO — conflito de interesse, ANPD pode questionar
- P6: Cache 35-50% otimista — projecao conservadora e 15-20%

**Pontos cegos identificados:**
- B1: Ausencia de go-to-market (quem vende? quem sao os 5 early adopters?)
- B2: Resposta competitiva nao modelada (Google BigQuery NL nativo?)
- B3: Clientes sem BigQuery nao podem usar o MVP (mercado muito pequeno?)
- B4: Qualidade de schema dos tenants nao avaliada
- B5: Dependencia critica de Claude API
- B6: Budget juridico ausente no MVP para LGPD

**Modelo de negocio alternativo sugerido:** Open-core (engine NL-to-SQL open-source com monetizacao via cloud hosting + enterprise features) ou exit via aquisicao.

**Stress-test do cenario D:** Se 2 das 5 premissas falharem (30 tenants no mes 12 + cache 20%), cobertura cai de 59% para ~34%.
<!-- /region: REG-QUAL-02 -->

---

<!-- region: REG-BACK-01 -->
## Backlog MVP (Priorizado)

| Sprint | Semanas | Foco | Entregaveis |
|:------:|:-------:|------|-------------|
| S1-S2 | 1-4 | Setup | Infra GCP, monorepo, CI/CD, auth basica (Firebase) |
| S3-S4 | 5-8 | Core | Engine NL-to-SQL basico (BigQuery), schema discovery |
| S5-S6 | 9-12 | Core | Glossario por tenant, contexto de negocio |
| S7-S8 | 13-16 | UX | Interface conversacional, graficos automaticos |
| S9-S10 | 17-20 | Features | Sugestao de prompts, export, historico |
| S11-S12 | 21-24 | Polish | Onboarding wizard, billing (Stripe), planos |
| S13-S14 | 25-28 | QA | Testes e2e, load testing, security review, RIPD |
| S15-S16 | 29-32 | Launch | Early adopters (5 tenants), monitoramento, ajustes |
<!-- /region: REG-BACK-01 -->

---

<!-- region: REG-EXEC-04 -->
## Proximos Passos

| # | Acao | Prioridade | Responsavel | Prazo |
|---|------|:----------:|:-----------:|:-----:|
| 1 | **Resolver viabilidade financeira** — definir estrategia de captacao (Pre-seed ~R$ 1,5M) com timeline e investidores-alvo | Critica | Fabio (CTO) | Antes de iniciar dev |
| 2 | **Dimensionar mercado** — TAM/SAM/SOM de NL-to-SQL para BigQuery no Brasil/LATAM | Critica | PO | Antes de iniciar dev |
| 3 | **Confirmar early adopters** — obter pelo menos 3 LOIs | Critica | Fabio + PO | Antes de iniciar dev |
| 4 | **Resolver pricing** — D11 (R$ 497) vs D51 (R$ 697) — testar com early adopters | Alta | PO | Mes 1-2 |
| 5 | **Contratar DPO terceirizado** (~R$ 2.000/mes) | Alta | Fabio | Antes do lancamento |
| 6 | **Iniciar contratacao** — Backend Senior NL-to-SQL (prioridade maxima) | Alta | Fabio | Imediato |
| 7 | **Iniciar Sprint 1** — setup GCP, monorepo, CI/CD, auth | Alta | Tech Lead + Fabio | Apos resolucao itens 1-3 |
| 8 | **Estabelecer metricas de gatilho** — dashboard com KPIs Go/No-Go (mes 8, 12, 18, 24) | Media | PO | Sprint 1-2 |
<!-- /region: REG-EXEC-04 -->

---

<!-- region: REG-EXEC-05 -->
## Decisoes Registradas (Consolidado)

56 decisoes registradas (D1-D56) ao longo de 8 blocos de discovery. Destaques:

| # | Decisao | Status |
|---|---------|:------:|
| D1 | BigQuery como unico banco no MVP | Confirmada |
| D3 | APIs externas (Claude, Gemini) para LLM — sem LLM proprio | Confirmada |
| D4 | Read-only obrigatorio nas queries | Confirmada |
| D9 | Controle de acesso por campo/registro como feature core | Confirmada |
| D11 | Pricing Pro = R$ 497, Enterprise = R$ 1.997 | Conflita com D51 |
| D17 | Time MVP de 6 pessoas | Confirmada |
| D24 | Row-level multi-tenancy no MVP | Confirmada |
| D27 | Stripe como billing platform (Buy) | Confirmada |
| D32 | LGPD modo profundo obrigatorio | Confirmada |
| D40 | Modular Monolith como padrao arquitetural | Confirmada |
| D50 | NL-to-SQL Engine e o unico componente BUILD | Confirmada |
| D51 | Pricing recomendado: Pro R$ 697, Enterprise R$ 2.997 | Recomendacao (conflita com D11) |
| D54 | Gatilhos Go/No-Go: mes 8, 12, 18, 24 | Confirmada |
| D55 | Pre-seed ~R$ 1,5M necessario | Recomendacao |
<!-- /region: REG-EXEC-05 -->

---

<!-- region: REG-GLOSS-01 -->
## Glossario

| Termo | Definicao |
|-------|-----------|
| **NL-to-SQL** | Natural Language to SQL — conversao de perguntas em linguagem natural para queries de banco de dados |
| **RLS** | Row-Level Security — controle de acesso em nivel de registro que restringe quais linhas um usuario pode ver |
| **Tenant** | Organizacao cliente que utiliza o Veezoozin; cada tenant tem dados isolados |
| **MCP** | Model Context Protocol — protocolo para conectar fontes externas de conhecimento (RAGs, wikis, APIs) |
| **LLM** | Large Language Model — modelo de linguagem de grande escala (Claude, Gemini) |
| **LGPD** | Lei Geral de Protecao de Dados — legislacao brasileira de privacidade de dados |
| **DPO** | Data Protection Officer — encarregado de protecao de dados pessoais |
| **DPA** | Data Processing Agreement — acordo de processamento de dados entre controlador e operador |
| **RIPD** | Relatorio de Impacto a Protecao de Dados Pessoais — documento exigido pela LGPD |
| **TCO** | Total Cost of Ownership — custo total de propriedade (infra + equipe + marketing + servicos) |
| **MRR** | Monthly Recurring Revenue — receita recorrente mensal |
| **ARR** | Annual Recurring Revenue — receita recorrente anual |
| **PLG** | Product-Led Growth — estrategia de crescimento onde o produto e o principal canal de aquisicao |
| **PME** | Pequenas e Medias Empresas |
| **SLA/SLO/SLI** | Service Level Agreement/Objective/Indicator — niveis de servico contratado/objetivo/indicador |
| **RBAC** | Role-Based Access Control — controle de acesso baseado em papeis |
| **WAF** | Web Application Firewall — firewall de aplicacao web |
| **sqlglot** | Biblioteca open-source de parsing e validacao de SQL |
| **Modular Monolith** | Padrao arquitetural com separacao logica de modulos em deploy unico |
| **Feature Flag** | Mecanismo para ativar/desativar funcionalidades sem deploy |
<!-- /region: REG-GLOSS-01 -->

---

> **Documento gerado por:** consolidator
> **Pipeline:** Discovery-to-Go v02 | **Pack:** SaaS + AI/ML + Datalake-Ingestion | **Iteracao:** 1 | **Run:** 2
> **Timestamp:** 2026-04-12
> **Flags:** [BELOW-THRESHOLD] [VIABILIDADE-NEGATIVA]
