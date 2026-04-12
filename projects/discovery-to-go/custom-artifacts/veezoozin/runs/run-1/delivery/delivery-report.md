---
title: "Delivery Report — Veezoozin"
project-name: "veezoozin"
client: "mAInd Tech"
author: "consolidator"
created: "2026-04-11"
report-setup: "executive"
status: "entregue"
iteration: 1
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
  - REG-PROD-08
  - REG-ORG-01
  - REG-ORG-02
  - REG-FIN-01
  - REG-FIN-05
  - REG-RISK-01
  - REG-RISK-03
  - REG-QUAL-01
  - REG-QUAL-02
  - REG-BACK-01
  - REG-METR-01
  - REG-NARR-01
  - REG-DOM-SAAS-01
  - REG-DOM-AIML-01
---

# Delivery Report — Veezoozin

> Relatorio consolidado do Discovery Pipeline — Iteracao 1
> Projeto: **Veezoozin** | Cliente: **mAInd Tech** | Data: 2026-04-11

---

<!-- region: REG-EXEC-01 -->
## One-Pager Executivo

**Problema:** Empresas acumulam dados valiosos em bancos transacionais e analiticos, mas apenas 5-10% dos colaboradores (os que dominam SQL/BI) conseguem acessa-los; uma pergunta simples de negocio vira um ticket que leva dias para ser respondido. **A barreira tecnica, a falta de contexto de dominio e a ausencia de insights visuais impedem a democratizacao do acesso a dados corporativos.**

**Solucao:** O Veezoozin e uma plataforma SaaS conversational-first que converte perguntas em linguagem natural (PT-BR, EN-US, ES) em queries SQL contextualizadas pelo dominio de negocio de cada tenant, retornando graficos, insights e analises em segundos. Utiliza stack GCP-first (Cloud Run, BigQuery, Vertex AI) com LLMs externos (Claude + Gemini) e integracao MCP para fontes de conhecimento externas.

**TCO 3 anos:** **US$ 1,63M** (fonte de verdade: bloco 1.8). Equipe representa ~90% do custo. Break-even total estimado no mes 36-42.

> **Nota de consistencia:** Os blocos 1.3 e 1.8 apresentam divergencias financeiras significativas (pricing, ARR, break-even). Este relatorio adota o bloco 1.8 como fonte de verdade por ser mais conservador e detalhado. As projecoes do bloco 1.3 sao excessivamente otimistas (break-even no mes 3 vs mes 36-42 no bloco 1.8).

**Top 3 Riscos:**

1. **Precisao do NL-to-SQL** — Meta de 85% sem lastro empirico. Benchmarks de mercado indicam 60-75% em schemas desconhecidos. Se ficar em 60%, o produto e inviavel (personas abandonam na 2a falha).
2. **Bloqueantes LGPD** — DPO nao nomeado, DPA com sub-processadores nao assinado, RIPD nao elaborada. Lancar sem resolver e ilegal.
3. **Modelo financeiro fragil** — Cenario esperado acumula -US$ 901K em 3 anos. Premissas de conversao (35% Free para Pago) e churn (4%) sao otimistas vs benchmarks de mercado.

**Recomendacao: BUILD** — com condicoes obrigatorias (resolver 6 itens de monitoramento antes/durante primeiras sprints).

**Proximo passo:** Sessao de Human Review com CTO para validar todos os itens [INFERENCE] de alta relevancia (pricing, time, salarios, churn, OKRs) antes de iniciar Sprint 1.
<!-- /region: REG-EXEC-01 -->

---

<!-- region: REG-EXEC-02 -->
## Product Brief

**Nome do produto:** Veezoozin
**Empresa:** mAInd Tech (startup de tecnologia)
**Tipo:** SaaS B2B multi-tenant
**Maturidade:** Greenfield — primeiro produto, primeira versao
**Posicionamento:** "Pergunte para seus dados" — democratizacao do acesso a dados via linguagem natural, com contexto de negocio por tenant, multi-idioma nativo (PT-BR/EN/ES) e integracao com fontes de conhecimento externas via MCP.

**Visao:** Plataforma SaaS de consulta em linguagem natural que converte perguntas humanas em queries de banco de dados (transacional e analitico), gerando graficos, insights, relatorios e analises — tudo contextualizado pelo dominio de negocio do tenant.

**Diferencial competitivo:**

| Criterio | Veezoozin vs Mercado |
|----------|---------------------|
| Abordagem | Conversational-first (vs dashboard-first do Metabase, Tableau) |
| Multi-idioma | PT-BR, EN-US, ES nativos (vs EN-only da maioria) |
| Contexto por tenant | Glossario + schema + MCP por tenant (vs generico) |
| Preco | PME-friendly com plano Free (vs enterprise caro do ThoughtSpot) |
| Integracao MCP/RAG | Nativo (vs inexistente nos concorrentes) |

**Stack obrigatoria:** GCP (Cloud Run, Vertex AI, BigQuery, Cloud SQL, Firestore), Python (FastAPI), React, LLM APIs (Claude + Gemini).

**Restricoes:** MVP em 12-16 semanas. LGPD obrigatoria. Read-only. BigQuery como unico banco no MVP.
<!-- /region: REG-EXEC-02 -->

---

<!-- region: REG-PROD-01 -->
## Problema e Contexto

### O Problema

Empresas possuem dados valiosos distribuidos em bancos transacionais e analiticos, mas o acesso e restrito a profissionais tecnicos. O problema se manifesta em quatro dimensoes:

| Dimensao | Descricao | Impacto |
|----------|-----------|---------|
| **Barreira tecnica** | Apenas quem domina SQL/BI acessa dados (5-10% da empresa) | Gestores dependem de tickets que levam 2-5 dias |
| **Falta de contexto de dominio** | Ferramentas genericas nao compreendem vocabulario especifico (ex: "churn" tem significado diferente por empresa) | Respostas imprecisas ou inuteis |
| **Dados sem insight** | Resultados entregues como tabelas brutas, sem visualizacao ou interpretacao | Usuario nao sabe o que fazer com os dados |
| **Barreira linguistica** | Empresas latinas operam em PT-BR, EN-US e ES; ferramentas sao majoritariamente em ingles | Atrito e erros de interpretacao |

### O Contexto

| Item | Detalhe |
|------|---------|
| Setor | Tecnologia — produto SaaS B2B |
| Empresa | mAInd Tech — startup, time enxuto, foco em speed-to-market |
| Tipo | Novo produto (greenfield) |
| Mercado-alvo | PMEs latino-americanas com dados em BigQuery |
| Creditos GCP | Contrato enterprise com incentivos significativos |

### Impacto Mensuravel Esperado

| Metrica | Antes (sem Veezoozin) | Depois (com Veezoozin) |
|---------|----------------------|----------------------|
| Tempo de resposta | 2-5 dias (ticket) | < 5 segundos |
| Colaboradores com acesso a dados | 5-10% (tecnicos) | 100% |
| Qualidade do output | Tabela bruta CSV | Grafico + insight + analise + sugestao |
| Volume de tickets para time de dados | 100% (referencia) | Reducao de 60-80% |
<!-- /region: REG-PROD-01 -->

---

<!-- region: REG-PROD-02 -->
## Personas

### Persona Primaria — Renata, Gestora de Operacoes (P0)

| Atributo | Detalhe |
|----------|---------|
| Cargo | Diretora de Operacoes |
| Nivel tecnico | Baixo — sabe usar Excel e dashboards, nao escreve SQL |
| Frequencia | Diario |
| JTBD principal | Obter respostas de negocio em tempo real para decisoes em reunioes |
| Dor critica | Dependencia do time de dados (ticket de 2-5 dias para respostas simples) |
| Ganho principal | Autonomia total para consultar dados com resposta visual em < 30 segundos |
| Tolerancia a erros | **Baixa** — se a resposta estiver errada 2x, abandona a ferramenta |

### Persona Secundaria — Lucas, Analista de Negocio (P0)

| Atributo | Detalhe |
|----------|---------|
| Cargo | Analista de Inteligencia de Negocio |
| Nivel tecnico | Medio — entende SQL basico, usa BI e planilhas avancadas |
| Frequencia | Diario (intensivo) — 10-30 consultas/dia |
| JTBD principal | Analises comparativas complexas e exploracao de dados em sequencia |
| Dor critica | Tempo gasto montando queries SQL para perguntas recorrentes |
| Ganho principal | Velocidade 10x na exploracao com conversacao encadeada e memoria de contexto |

### Persona de Configuracao — Diego, Administrador do Tenant (P1)

| Atributo | Detalhe |
|----------|---------|
| Cargo | Coordenador de Dados / Lider Tecnico de BI |
| Nivel tecnico | Medio-Alto |
| Frequencia | Semanal |
| JTBD principal | Configurar contexto do tenant (glossario, schema, MCPs) |
| Meta de onboarding | < 4 horas (banco conectado ate primeiro usuario) |

### Persona Tecnica — Camila, Administradora de TI (P1)

| Atributo | Detalhe |
|----------|---------|
| Cargo | Analista de Infraestrutura / DBA |
| Nivel tecnico | Alto |
| Frequencia | Mensal |
| JTBD principal | Configurar conexoes seguras, RBAC, row-level security |
| Preocupacao critica | Isolamento multi-tenant e zero vazamento de dados |
<!-- /region: REG-PROD-02 -->

---

<!-- region: REG-PROD-04 -->
## Proposta de Valor

**"Pergunte para seus dados."** Qualquer pessoa da empresa, em qualquer idioma, faz uma pergunta e recebe um grafico com insight em segundos. Sem SQL, sem ticket, sem espera.

### Value Proposition Canvas

| Dimensao | Estado Atual | Estado Futuro (Veezoozin) | Metrica-alvo |
|----------|-------------|--------------------------|-------------|
| Tempo de resposta | Dias (ticket para time de dados) | Segundos (pergunta para resposta visual) | < 5s queries simples |
| Acessibilidade | 5-10% da empresa | 100% dos colaboradores | Cobertura total |
| Qualidade do output | Tabela bruta CSV/Excel | Graficos + insights + analises + sugestoes | Precisao > 85% na 1a tentativa |
| Custo operacional | Alto volume de tickets ad-hoc | Autoatendimento por linguagem natural | Reducao de 60-80% tickets |
| Contexto do dominio | Generico ou inexistente | Glossario + schema + MCP por tenant | Cobertura semantica por tenant |
| Idioma | Ingles predominante | PT-BR, EN-US, ES nativos | 3 idiomas no MVP |

### Diferenciais Competitivos

| Concorrente | Limitacao | Veezoozin |
|-------------|-----------|-----------|
| Tableau Ask Data | Preso ao ecossistema Tableau, apenas ingles | Standalone, multi-idioma |
| ThoughtSpot | Enterprise caro, schema rigido | PME-friendly, schema flexivel |
| ChatGPT + SQL | Sem contexto de negocio, sem multi-tenant | Contexto por tenant, glossario |
| Metabase | Dashboard-first, nao conversacional | Conversational-first com output visual |
<!-- /region: REG-PROD-04 -->

---

<!-- region: REG-PROD-05 -->
## OKRs e ROI

### OKR 1 — Produto funcional e validado

| Key Result | Meta |
|-----------|------|
| KR1.1 | Precisao de query gerada >= 85% na 1a tentativa |
| KR1.2 | Latencia < 5s para queries simples (ate 3 JOINs) |
| KR1.3 | Suporte a 3 idiomas (PT-BR, EN-US, ES) com >= 80% interpretacao correta |
| KR1.4 | Sugestao de prompts com taxa de aceitacao >= 40% |

### OKR 2 — Plataforma multi-tenant operacional

| Key Result | Meta |
|-----------|------|
| KR2.1 | Suporte a >= 5 tenants simultaneos com 50+ tabelas cada |
| KR2.2 | Onboarding de novo tenant <= 2 horas |
| KR2.3 | Zero incidentes de vazamento cross-tenant |
| KR2.4 | Controle de acesso registro/campo para >= 1 tenant piloto |

### OKR 3 — Viabilidade economica validada

| Key Result | Meta |
|-----------|------|
| KR3.1 | Custo de infra <= R$ 5K/mes para ate 50 tenants |
| KR3.2 | >= 2 tenants pagantes ate o final do MVP |
| KR3.3 | Custo medio por query <= R$ 0,05 |
| KR3.4 | Unit economics positivo no plano Pro (margem bruta >= 60%) |

### ROI (fonte de verdade: bloco 1.8)

| Indicador | Valor |
|-----------|-------|
| TCO 3 anos | US$ 1,63M |
| Break-even operacional (infra + LLM) | Mes 14-18 (~35 tenants pagantes) |
| Break-even total (inclui equipe) | Mes 36-42 (~200 tenants pagantes) |
| Payback do investimento acumulado | Mes 42-48 |
| Deficit acumulado cenario esperado (3 anos) | -US$ 901K |

> **Atencao:** As projecoes do bloco 1.3 (break-even mes 3, payback mes 8-10) divergem significativamente das do bloco 1.8. O auditor (2.1) e o 10th-man (2.2) concordam que o bloco 1.3 e excessivamente otimista. Este relatorio adota o bloco 1.8 como referencia.
<!-- /region: REG-PROD-05 -->

---

<!-- region: REG-PROD-06 -->
## Modelo de Negocio — SaaS Pricing Tiers

**Modelo:** SaaS Subscription + Usage-based hybrid (assinatura mensal por plano com componente de consumo).

### Planos (fonte de verdade: bloco 1.8, em USD)

| Plano | Preco/mes | Tenants | Queries/mes | Tabelas | Usuarios | Custo variavel/tenant/mes |
|-------|-----------|---------|-------------|---------|----------|--------------------------|
| **Free** | $0 | 1 | 100 | 10 | 2 | $0,50 |
| **Starter** | $99 | 1 | 1.000 | 50 | 10 | $54,70 |
| **Business** | $299 | 3 | 5.000 | 200 | 50 | $122,50 |
| **Enterprise** | $799+ | Ilimitado | 20.000+ | Ilimitado | Ilimitado | $285+ |

> **Nota de consistencia:** O bloco 1.3 utiliza nomenclatura diferente (Free/Starter/Pro/Enterprise) e valores em R$ (R$0/R$297/R$897/R$2.997). O bloco 1.8 usa Free/Starter/Business/Enterprise em USD. Este relatorio adota a nomenclatura e valores do bloco 1.8. A padronizacao final requer decisao do CTO/PO.

### Estrategia de Pricing

| Principio | Aplicacao |
|-----------|-----------|
| Value-based pricing | Precificacao baseada em horas economizadas e tickets eliminados |
| Land and expand | Free (trial) para Starter, Starter para Business, Business para Enterprise |
| Transparent metering | Dashboard de consumo em tempo real para o admin |
| Annual discount | 20% para contratos anuais |

### Alertas do 10th-man sobre o plano Free

O plano Free pode canibalizar o Starter: 50 queries/mes com 10 tabelas atende muitas PMEs. O gatilho de upgrade mais natural (multi-idioma) nao se aplica ao publico primario (PT-BR). Recomendacao: limitar Free a trial de 7 dias ou remover graficos/insights do Free.
<!-- /region: REG-PROD-06 -->

---

<!-- region: REG-PROD-07 -->
## Escopo — In/Out

### Dentro do Escopo (MVP)

| Area | Funcionalidade |
|------|---------------|
| **Core NL-to-SQL** | Interface conversacional web, engine NL para SQL, execucao read-only com sandbox |
| **Contexto do tenant** | Onboarding, mapeamento automatico de schema, glossario por tenant, historico de perguntas |
| **Output visual** | Graficos automaticos (Chart.js), insights por IA, relatorios PDF/HTML, sugestao de proxima pergunta |
| **Multi-tenant** | Isolamento completo de dados, billing por consumo, painel admin por tenant |
| **Multi-idioma** | PT-BR, EN-US, ES |
| **Seguranca** | RBAC, row/column-level security, criptografia em repouso (AES-256) e transito (TLS 1.3) |
| **Integracao MCP** | Suporte a MCP para fontes externas de conhecimento (RAGs, wikis) |

### Fora do Escopo

- Escrita/modificacao de dados nos bancos do cliente (apenas leitura)
- Treinamento/fine-tuning de LLM proprio
- ETL/ingestao de dados
- App mobile nativo (web responsivo no MVP)
- Integracao direta com ERPs/CRMs (apenas via banco ou MCP)
- Bancos alem do BigQuery no MVP

### Recomendacao do 10th-man: Reducao de Escopo

Para um time de 6.5 pessoas em 12 semanas, o escopo e excessivo. Recomendacao de corte:

| Corte sugerido | Economia | Quando retorna |
|----------------|----------|----------------|
| Remover MCP do MVP | 2-3 sprints | Q2 pos-launch |
| Apenas PT-BR no MVP | 1 sprint | Q1 pos-launch |
| Billing simplificado (tudo free no MVP) | 1-2 sprints | Q2 pos-launch |
| Timeline realista: 16-20 semanas | Buffer de qualidade | — |
<!-- /region: REG-PROD-07 -->

---

<!-- region: REG-PROD-08 -->
## Roadmap

### MVP — 12 Semanas (6 Sprints de 2 Semanas)

| Sprint | Semanas | Foco | Entregaveis-chave |
|--------|---------|------|-------------------|
| **S1** | 1-2 | Fundacao | Infra GCP provisionada, CI/CD, auth basica, schema de banco, design system |
| **S2** | 3-4 | Core Engine | NL para SQL engine (v1), conexao BigQuery, mapeamento automatico de schema |
| **S3** | 5-6 | Visualizacao + Multi-tenant | Interface conversacional, graficos automaticos, isolamento de tenants, onboarding |
| **S4** | 7-8 | Contexto + Inteligencia | Glossario por tenant, sugestao de prompts, multi-idioma (PT-BR, EN, ES) |
| **S5** | 9-10 | Billing + Seguranca | Planos e billing, controle de acesso por campo, LGPD compliance, MCP (v1) |
| **S6** | 11-12 | Polimento + Launch | Testes E2E, performance tuning, exportacao PDF/HTML, tenants piloto, go-live |

### Pos-MVP — Roadmap de Evolucao

| Fase | Timeline | Foco |
|------|----------|------|
| **Fase 2** | Q1-Q2 pos-launch | MCP completo, suporte PostgreSQL/MySQL, cache semantico agressivo, SOC2 prep |
| **Fase 3** | Q3-Q4 pos-launch | Microservicos (extrair NL-to-SQL engine), multi-region, WCAG 2.1, Enterprise features |
| **Escalabilidade** | >50 tenants | Extrair NL-to-SQL como servico, auto-scaling agressivo (R$ 8-15K/mes) |
| **Enterprise** | >500 tenants | Microservicos completos, BigQuery reservations, SLAs dedicados (R$ 30-50K/mes) |
<!-- /region: REG-PROD-08 -->

---

<!-- region: REG-ORG-01 -->
## Stakeholders

### Matriz Poder x Interesse

| Stakeholder | Poder | Interesse | Estrategia | Comunicacao |
|-------------|-------|-----------|------------|-------------|
| **Fabio (CTO/Sponsor)** | Alto | Alto | Gerenciar de perto | Daily sync + Sprint Review |
| **Time mAInd Tech** | Medio | Alto | Manter informado | Slack + Cerimonias Scrum |
| **Tenants piloto** | Baixo | Alto | Manter informado | E-mail + Slack quinzenal |
| **GCP Account Manager** | Baixo | Baixo | Monitorar | Google Meet mensal |
| **Investidores futuros** | Alto | Baixo (por ora) | Manter satisfeito | Metricas e pitch deck pos-MVP |

### Governanca (RACI Simplificado)

| Decisao | CTO | PO | Tech Lead |
|---------|-----|----|-----------|
| Priorizacao de backlog | A | R | C |
| Arquitetura tecnica | A | I | R |
| Orcamento / custos | R | C | C |
| Mudanca de escopo MVP | A | R | C |
| Deploy em producao | I | A | R |
<!-- /region: REG-ORG-01 -->

---

<!-- region: REG-ORG-02 -->
## Estrutura do Time

### Composicao MVP

| Papel | Qtd | Dedicacao | Responsabilidades | Salario CLT+encargos/mes |
|-------|-----|-----------|-------------------|--------------------------|
| CTO / Sponsor | 1 | Parcial | Arquitetura, orcamento, priorizacao estrategica | — |
| Product Owner | 1 | Integral | Backlog, priorizacao, metricas de produto | R$ 22.000 |
| Tech Lead / Senior Backend | 1 | Integral | Arquitetura de codigo, code reviews, NL-to-SQL engine | R$ 28.000 |
| Backend Dev (AI/ML) | 1 | Integral | Engine NL-SQL, embeddings, LLM APIs, MCP | R$ 25.000 |
| Backend Dev (Plataforma) | 1 | Integral | Multi-tenancy, billing, auth, APIs REST | R$ 22.000 |
| Frontend Dev | 1 | Integral | Interface conversacional, graficos, dashboard admin | R$ 20.000 |
| UX/UI Designer | 1 | Parcial (50%) | Design system, UX conversacional, onboarding | R$ 18.000 |

**Total: 7 pessoas (6.5 FTE)** | **Custo mensal estimado: R$ 148.000/mes** (Ano 1)

### Estrategia de Contratacao

| Prioridade | Papeis | Timeline |
|-----------|--------|----------|
| Critica (Semana 1-2) | Tech Lead + Backend AI/ML | Sem eles o projeto nao inicia |
| Alta (Semana 2-3) | Backend Plataforma + Frontend | Infra multi-tenant e interface |
| Alta (Semana 3-4) | PO + UX/UI Designer | Backlog e design system |

> **Alerta do 10th-man:** Contratar Tech Lead e Backend AI/ML seniors em 2 semanas e irrealista (mercado leva 4-8 semanas). Se atrasarem, o MVP precisa ter escopo revisado. Contingencia: freelancers seniors ou CTO assume Tech Lead temporariamente.

### Evolucao do Time

| Ano | Headcount | Custo mensal | Custo anual |
|-----|-----------|-------------|-------------|
| Ano 1 | 6.5 FTE | R$ 148.000 | R$ 1.776.000 |
| Ano 2 | 10.5 FTE | R$ 229.000 | R$ 2.748.000 |
| Ano 3 | 13 FTE | R$ 293.000 | R$ 3.516.000 |
<!-- /region: REG-ORG-02 -->

---

<!-- region: REG-FIN-01 -->
## TCO 3 Anos

> **Fonte de verdade: bloco 1.8.** O auditor (2.1) e o 10th-man (2.2) identificaram divergencias financeiras criticas entre blocos 1.3 e 1.8. O bloco 1.8 e adotado por ser mais conservador e detalhado.

### Consolidacao TCO

| Categoria | Ano 1 | Ano 2 | Ano 3 | Total 3 Anos | % TCO |
|-----------|-------|-------|-------|-------------|-------|
| **Equipe** | $322.909 | $499.636 | $639.273 | **$1.461.818** | 89,8% |
| **LLM APIs** | $1.140 | $10.944 | $54.720 | **$66.804** | 4,1% |
| **Infra GCP** | $5.689 | $12.940 | $30.516 | **$49.145** | 3,0% |
| **Servicos Auxiliares GCP** | $1.248 | $2.484 | $6.396 | **$10.128** | 0,6% |
| **Licenciamento e Ferramentas** | $3.326 | $13.228 | $23.250 | **$39.804** | 2,4% |
| **Total anual** | **$334.312** | **$539.232** | **$754.155** | — | — |
| **Total 3 anos** | — | — | — | **$1.627.699** | 100% |

### Premissas de Crescimento

| Premissa | Ano 1 | Ano 2 | Ano 3 |
|----------|-------|-------|-------|
| Tenants | 20 | 80 | 200 |
| Usuarios ativos/tenant | 10 | 15 | 20 |
| Queries/mes | 30K | 288K | 1,44M |
| Creditos GCP | 15% desconto (cenario esperado) |

### Projecao Receita vs Custo (cenario esperado)

| Metrica | Ano 1 | Ano 2 | Ano 3 |
|---------|-------|-------|-------|
| ARR | $32.256 | $179.808 | $514.080 |
| Custo total | $334.312 | $539.232 | $754.155 |
| Resultado | -$302.056 | -$359.424 | -$240.075 |
| **Resultado acumulado** | -$302.056 | -$661.480 | **-$901.555** |

### Divergencia Documentada (blocos 1.3 vs 1.8)

| Aspecto | Bloco 1.3 | Bloco 1.8 (adotado) |
|---------|-----------|---------------------|
| Break-even operacional | Mes 3 | Mes 14-18 |
| Payback total | Mes 8-10 | Mes 42-48 |
| ARR Ano 1 | ~R$ 460K (~$84K) | $32.256 |
| Custo equipe MVP (3 meses) | R$ 180.000 | R$ 444.000 |

> O bloco 1.3 subestima gravemente o custo de equipe (diferenca de ~2,5x) e superestima receita (~2,6x). A divergencia foi classificada como **critica** pelo auditor.
<!-- /region: REG-FIN-01 -->

---

<!-- region: REG-FIN-05 -->
## Estimativa de Esforco

### Implementacao Build vs Buy

| Componente | Decisao | Custo Impl. | Custo Op./ano (Ano 1) |
|------------|---------|-------------|----------------------|
| NL-to-SQL Engine | Hibrido (Vanna.ai + Claude/Gemini) | $10K-15K | $1.140 |
| Vector Store | Buy (Firestore para Vertex AI) | $3K-5K | $60 |
| LLM Provider | Buy (Multi-provider Gemini + Claude) | $5K-8K | $1.140 |
| Autenticacao | Buy (Firebase Auth) | $5K-8K | $0 |
| Visualizacao | Build (Chart.js custom) | $8K-12K | $0 |
| **Total** | — | **$31K-48K** | **$2.340** |

### Esforco por Sprint

| Sprint | Foco | Esforco estimado |
|--------|------|-----------------|
| S1 (Sem 1-2) | Fundacao, infra, CI/CD | Alta (setup) |
| S2 (Sem 3-4) | Core NL-to-SQL | Muito alta (critico) |
| S3 (Sem 5-6) | Visualizacao + Multi-tenant | Alta |
| S4 (Sem 7-8) | Contexto + Inteligencia | Media-alta |
| S5 (Sem 9-10) | Billing + Seguranca | Alta |
| S6 (Sem 11-12) | Polimento + Launch | Media (testes + deploy) |

> **Alerta:** O 10th-man avalia que o escopo completo requer 16-20 semanas realistas, nao 12. O time de 6.5 pessoas ainda nao existe e a contratacao pode atrasar 2-4 semanas.
<!-- /region: REG-FIN-05 -->

---

<!-- region: REG-RISK-01 -->
## Matriz de Riscos

Consolidacao dos riscos identificados pelo discovery (blocos 1.1-1.8), auditor (2.1) e 10th-man (2.2).

### Riscos Criticos

| # | Risco | Probabilidade | Impacto | Fonte | Mitigacao |
|---|-------|--------------|---------|-------|-----------|
| R1 | **Precisao NL-to-SQL abaixo de 75%** — produto inviavel, personas abandonam | Alta | Critico | 2.2 (QH-1) | Benchmark com 100+ queries contra 3+ schemas reais antes da Sprint 3 |
| R2 | **DPO nao nomeado** — go-live ilegal, risco de sancao ANPD | Alta | Critico | 1.6, 2.2 (QH-6) | Contratar DPO-as-a-Service antes da Sprint 1 |
| R3 | **DPA com Anthropic/Google nao assinado** — transferencia internacional sem base legal | Alta | Critico | 1.6, 2.2 (QH-6) | Iniciar negociacao ANTES do MVP (leva 2-6 meses) |
| R4 | **Vazamento cross-tenant** — violacao LGPD grave | Media | Critico | 1.5, 1.6 | Testes automatizados de isolamento + pentest obrigatorio |
| R5 | **RIPD nao elaborada** — obrigatoria por lei para tratamento de dados sensiveis | Alta | Critico | 1.6 | Elaborar com suporte do DPO como pre-requisito Sprint 1 |

### Riscos Altos

| # | Risco | Probabilidade | Impacto | Fonte | Mitigacao |
|---|-------|--------------|---------|-------|-----------|
| R6 | **Modelo financeiro fragil** — cenario esperado acumula -$901K em 3 anos | Alta | Alto | 1.8, 2.2 (QH-2) | Reconciliar 1.3 e 1.8; modelar cenario com churn 7% e conversao 10%; documentar runway |
| R7 | **Atraso na contratacao** — Tech Lead e AI/ML levam 4-8 semanas | Alta | Alto | 1.4, 2.2 (QH-8) | Pipeline paralelo; contingencia com freelancers; CTO assume temporariamente |
| R8 | **Escopo excessivo para 12 semanas** — 12+ features complexas para 6.5 pessoas | Alta | Alto | 2.2 (QH-8) | Cortar MCP, simplificar billing, aceitar 16-20 semanas |
| R9 | **Latencia > 5s sem cache** — pipeline NL-to-SQL realista leva 8-12s | Media | Alto | 2.2 (QH-7) | Cache semantico na Sprint 2; streaming de resposta parcial; SLA duplo (<5s cache, <15s sem) |
| R10 | **Plano Free canibaliza Starter** — 80% ficam free forever | Media | Alto | 2.2 (QH-3) | Limitar Free a trial 7 dias ou remover graficos/insights |
| R11 | **Anthropic triplica precos** — custo LLM Ano 3 salta de $55K para $164K | Baixa | Alto | 2.2 (QH-10) | Abstraction layer para swap rapido; Gemini Flash como fallback |
| R12 | **Dados inferidos nao validados** — 40% do discovery e [INFERENCE] | Alta | Alto | 2.2 (QH-9) | Human Review com CTO antes da Sprint 1 |

### Riscos Medios

| # | Risco | Probabilidade | Impacto | Fonte | Mitigacao |
|---|-------|--------------|---------|-------|-----------|
| R13 | Adocao do plano Free sem conversao | Media | Medio | 1.1 | Limites claros, evidencia de valor |
| R14 | Concorrentes enterprise adicionam NL features | Alta | Medio | 1.1 | Diferenciacao: multi-idioma, contexto por tenant, preco PME |
| R15 | Lock-in GCP — sem portabilidade se precos subirem | Baixa | Medio | 2.2 (QH-10) | Terraform + Docker; documentar custo de migracao |
| R16 | Complexidade de dois bancos (Cloud SQL + Firestore) | Media | Medio | 2.2 (QH-4) | Reavaliar PostgreSQL unico com JSONB para MVP |
| R17 | MCP prematuro — protocolo imaturo, nenhum tenant vai usar no Ano 1 | Alta | Medio | 2.2 (QH-5) | Remover do MVP, lancar Q2 pos-launch |
| R18 | Ausencia de estrategia GTM | Alta | Medio | 2.2 (ponto cego #6) | Documentar aquisicao dos primeiros 5 tenants ate Sprint 3 |
<!-- /region: REG-RISK-01 -->

---

<!-- region: REG-RISK-03 -->
## Hipoteses Nao Validadas

Hipoteses identificadas pelo 10th-man (2.2) que carecem de evidencia empirica e devem ser validadas antes ou durante as primeiras sprints.

| # | Hipotese | Fonte | Status | Acao de Validacao |
|---|----------|-------|--------|-------------------|
| H1 | Precisao NL-to-SQL >= 85% na 1a tentativa | 1.1, 1.3 | **Nao validada** | Benchmark com 100+ queries reais contra 3+ schemas antes da Sprint 3 |
| H2 | Conversao Free para Pago de 35% | 1.8 | **Nao validada** | Benchmark de mercado e 2-5% (freemium B2B). Validar com tenants piloto |
| H3 | Churn mensal de 4% (Pro/Business) | 1.8 | **Nao validada** | SaaS B2B SMB tipico tem 5-8% nos primeiros 18 meses |
| H4 | Pricing ($99/$299/$799) adequado ao mercado | 1.8 | **Nao validada** | Nenhum estudo de willingness-to-pay realizado |
| H5 | Onboarding de tenant em < 4 horas | 1.2 | **Nao validada** | Depende da qualidade do mapeamento automatico de schema |
| H6 | Latencia < 5s para queries simples | 1.1, 1.3 | **Nao validada** | Pipeline completo (embedding + LLM + BQ) leva 8-12s sem cache |
| H7 | Custo por query <= R$ 0,05 | 1.3 | **Nao validada** | Depende do mix de modelos LLM e complexidade das queries |
| H8 | MCP como diferencial competitivo unico | 1.1 | **Nao validada** | Base instalada de MCP Servers no mercado PME latam e praticamente zero |
| H9 | TAM suficiente com apenas BigQuery no MVP | Briefing | **Nao validada** | Mercado PME latam usa mais PostgreSQL/MySQL que BigQuery |
| H10 | Time de 6.5 pessoas entrega escopo completo em 12 semanas | 1.4 | **Nao validada** | 12+ features complexas; time ainda nao existe |

### Perguntas Residuais para o CTO/Sponsor

| # | Pergunta | Impacto se nao respondida |
|---|---------|--------------------------|
| 1 | Qual e o runway disponivel (meses sem receita)? | Impossivel validar break-even no mes 36+ |
| 2 | O pricing foi validado com algum potencial cliente? | Risco de precificar fora da realidade |
| 3 | Existe cliente piloto comprometido antes do MVP? | Sem piloto, sem validacao real |
| 4 | Creditos GCP cobrem quanto tempo e qual valor? | Impacta TCO diretamente |
| 5 | DPA do contrato GCP cobre Gemini API? | Bloqueante LGPD |
| 6 | Tolerancia a atraso no MVP: 4 semanas? 8 semanas? | Define se escopo precisa ser cortado |
| 7 | Se precisao ficar em 70%, lancamento e aceitavel? | Define criterio go/no-go mais importante |
| 8 | Existe orcamento para marketing/vendas? | Sem GTM, projecao de 200 tenants e fantasia |
<!-- /region: REG-RISK-03 -->

---

<!-- region: REG-QUAL-01 -->
## Score do Auditor (Validacao Convergente)

**Veredicto: APROVADO COM RESSALVAS** — Score geral: **82%**

| Dimensao | Peso | Score | Score Ponderado |
|----------|------|-------|----------------|
| Cobertura | 20% | 90% | 18,0% |
| Profundidade | 20% | 87% | 17,4% |
| Consistencia | 25% | 72% | 18,0% |
| Fundamentacao | 15% | 80% | 12,0% |
| Completude | 20% | 83% | 16,6% |
| **Total** | **100%** | — | **82,0%** |

### Score por Bloco

| Bloco | Score | Destaque |
|-------|-------|----------|
| 1.1 — Proposito e Visao | **93%** | Exemplar: rastreabilidade impecavel |
| 1.2 — Personas e Jornada | **88%** | Personas ricas, jornadas detalhadas |
| 1.3 — Valor e OKRs | **83%** | Profundidade excelente, mas projecoes otimistas e divergentes do 1.8 |
| 1.4 — Processo e Time | **78%** | Completo, mas quase tudo e inferencia |
| 1.5 — Tecnologia | **82%** | Stack solida, falta rastreabilidade sistematica |
| 1.6 — Privacidade | **88%** | Analise LGPD profunda, bloqueantes identificados |
| 1.7 — Macro Arquitetura | **82%** | Arquitetura coerente e modularizada |
| 1.8 — TCO e Build vs Buy | **90%** | Mais detalhado e rigoroso do discovery |

### Principais Forcas

1. Rastreabilidade de fontes [BRIEFING]/[INFERENCE] nos blocos 1.1-1.3
2. Consistencia tecnica entre blocos 1.5, 1.6, 1.7
3. Analise LGPD profunda com identificacao proativa de bloqueantes
4. TCO com breakdown granular e 3 cenarios de sensibilidade
5. Decisao de monolito modular justificada com comparacao direta

### Principais Fraquezas

1. **Divergencias financeiras criticas** entre blocos 1.3 e 1.8 (ARR, break-even, payback, pricing)
2. **Nomenclatura inconsistente** dos planos (Pro vs Business) e moedas (R$ vs USD)
3. **Blocos 1.5-1.7** nao seguem padrao de rastreabilidade [BRIEFING]/[INFERENCE]
4. **Projecoes do 1.3** excessivamente otimistas sem benchmarks de mercado
5. **Ausencia** de plano de testes, disaster recovery, RIPD e ADRs
<!-- /region: REG-QUAL-01 -->

---

<!-- region: REG-QUAL-02 -->
## Questoes do 10th-man (Validacao Divergente)

**Veredicto: APROVADO COM RESSALVAS** — Score geral: **62%**

| Dimensao | Peso | Score | Status |
|----------|------|-------|--------|
| Divergencia (exploracao de alternativas) | 30% | 55% | Aprovado (marginal) |
| Robustez (resiliencia a mudanca) | 40% | 60% | Aprovado (marginal) |
| Completude critica (riscos enderecoados) | 30% | 73% | Aprovado |

### Resumo das 10 Questoes Hostis

| QH | Tema | Avaliacao |
|----|------|-----------|
| QH-1 | Precisao 85% NL-to-SQL sem evidencia | **REJEITADA** (premissa fragil) |
| QH-2 | Modelo financeiro contradiz entre 1.3 e 1.8 | Parcialmente aceita |
| QH-3 | Plano Free pode canibalizar Starter | Parcialmente aceita |
| QH-4 | Dois bancos (Cloud SQL + Firestore) desnecessarios | Aceita (fragilidade moderada) |
| QH-5 | MCP prematuro para MVP | Parcialmente aceita |
| QH-6 | 3 bloqueantes LGPD sem plano de resolucao | **ACEITA** (risco critico) |
| QH-7 | Latencia realista: 8-12s, nao < 5s | Parcialmente aceita |
| QH-8 | Escopo irreal para 6.5 pessoas em 12 semanas | **ACEITA** (risco alto) |
| QH-9 | 40% dos dados sao inferencias nao validadas | **REJEITADA** (premissa fragil) |
| QH-10 | Lock-in GCP sem quantificacao de risco | Parcialmente aceita |

### 14 Pontos Cegos Identificados

| # | Ponto Cego | Severidade |
|---|-----------|-----------|
| 1 | Estrategia de go-to-market | Critica |
| 2 | Regression testing do pipeline NL-to-SQL | Critica |
| 3 | Rate limiting definido por usuario | Alta |
| 4 | Plano de contingencia para demissoes (bus factor) | Alta |
| 5 | Testes de carga/performance | Alta |
| 6 | Versionamento de schema do tenant | Alta |
| 7 | Data export/portabilidade (LGPD Art. 18) | Alta |
| 8 | Observabilidade end-to-end do pipeline | Alta |
| 9 | Modo offline/baixa conectividade | Media |
| 10 | Multi-region/disaster recovery | Media |
| 11 | Acessibilidade (WCAG) | Media |
| 12 | Internacionalizacao real (i18n na interface) | Media |
| 13 | Suporte a bancos alem do BigQuery | Media |
| 14 | Politica de fair use para Enterprise "ilimitado" | Media |

### 6 Itens de Monitoramento Obrigatorio

| MON | Tema | Prazo | Responsavel |
|-----|------|-------|-------------|
| MON-1 | Benchmark de precisao NL-to-SQL (100+ queries, 3+ schemas) | Ate Sprint 2 | Backend AI/ML + CTO |
| MON-2 | Human Review — validar todos os [INFERENCE] criticos | Antes da Sprint 1 | PO + CTO |
| MON-3 | Resolucao bloqueantes LGPD (DPO, DPA, RIPD) | DPO antes da Sprint 1; DPA/RIPD antes da Sprint 5 | CTO + DPO |
| MON-4 | Reconciliacao financeira 1.3 vs 1.8 | Antes da Sprint 1 | PO |
| MON-5 | Definicao de escopo realista do MVP | Antes da Sprint Planning S1 | PO + CTO + Tech Lead |
| MON-6 | Estrategia de go-to-market (3+ LOIs) | Ate Sprint 3 | CTO |
<!-- /region: REG-QUAL-02 -->

---

<!-- region: REG-BACK-01 -->
## Backlog Priorizado — Epicos MVP

| # | Epico | Prioridade | Sprint | Justificativa |
|---|-------|-----------|--------|---------------|
| E1 | **Fundacao e Infraestrutura** — Provisionar GCP, CI/CD, auth, schema de banco | P0 | S1 | Pre-requisito para tudo |
| E2 | **NL-to-SQL Engine (v1)** — Pipeline completo: pergunta NL para SQL para resultados | P0 | S2 | Core do produto, sem isso nao existe Veezoozin |
| E3 | **Mapeamento Automatico de Schema** — Scan do BigQuery, enriquecimento semantico | P0 | S2 | Habilita o NL-to-SQL com contexto |
| E4 | **Interface Conversacional** — Chat web responsivo com campo de pergunta e sugestoes | P0 | S3 | Ponto de contato do usuario |
| E5 | **Visualizacao Automatica** — Graficos (Chart.js) com tipo escolhido por IA + insights | P0 | S3 | Diferencial vs tabela bruta |
| E6 | **Isolamento Multi-Tenant** — Middleware, row-level filtering, service accounts por tenant | P0 | S3 | Requisito de seguranca e LGPD |
| E7 | **Contexto do Tenant** — Glossario de negocio, historico, sugestao de prompts | P1 | S4 | Diferencial competitivo: respostas contextualizadas |
| E8 | **Multi-Idioma** — Suporte a PT-BR, EN-US, ES nas queries | P1 | S4 | Requisito do briefing |
| E9 | **Billing e Planos** — Free/Starter/Business/Enterprise com limites | P1 | S5 | Monetizacao |
| E10 | **Controle de Acesso Granular** — RBAC + row/column-level security | P1 | S5 | Requisito do briefing e LGPD |
| E11 | **Integracao MCP (v1)** — Gateway para RAGs externos | P2 | S5 | Diferencial, mas pode ser cortado se necessario |
| E12 | **Exportacao PDF/HTML** — Relatorios formatados exportaveis | P1 | S6 | Requisito de personas (Renata, Lucas) |
| E13 | **Onboarding de Tenants Piloto** — Setup dos primeiros clientes reais | P0 | S6 | Validacao real do produto |
| E14 | **Testes E2E e Performance** — Cobertura de testes, load testing | P0 | S6 | Qualidade pre-launch |

> **Nota:** Epicos P2 sao candidatos a corte se o cronograma apertar. O 10th-man recomenda remover E11 (MCP) e simplificar E9 (billing) no MVP.
<!-- /region: REG-BACK-01 -->

---

<!-- region: REG-METR-01 -->
## KPIs de Negocio

### North Star Metric

**Queries com resposta correta entregues por semana (por tenant)** — captura adocao, qualidade e frequencia simultaneamente.

### Metricas por Categoria

#### Ativacao

| Metrica | Meta MVP |
|---------|----------|
| Time-to-first-query | <= 30 min apos signup |
| Activation rate (>= 3 queries na 1a semana) | >= 60% |
| Schema mapping success (automatico) | >= 90% |

#### Engajamento

| Metrica | Meta MVP |
|---------|----------|
| DAU/MAU | >= 30% |
| Queries por usuario ativo/dia | >= 5 |
| Prompt suggestion acceptance | >= 40% |

#### Retencao

| Metrica | Meta MVP |
|---------|----------|
| D7 retention | >= 70% |
| D30 retention | >= 50% |
| Net Revenue Retention (NRR) | >= 105% |
| Churn mensal Starter | <= 8% |
| Churn mensal Pro/Business | <= 4% |

#### Qualidade

| Metrica | Meta MVP |
|---------|----------|
| Query accuracy (1a tentativa) | >= 85% |
| Latencia P95 (query simples) | <= 5s (com cache) / <= 15s (sem cache) |
| Latencia P95 (query complexa) | <= 15s |
| NPS | >= 40 |
| CSAT pos-query | >= 4.0/5.0 |

#### Financeiro

| Metrica | Meta M6 | Meta M12 |
|---------|---------|----------|
| MRR | ~$7.500 | ~$2.688 a $14.984 (range 1.3 vs 1.8) |
| Custo por query | <= $0,0032 a $0,05 | Otimizar com cache |
| Margem bruta (plano Business) | >= 60% | >= 70% |
<!-- /region: REG-METR-01 -->

---

<!-- region: REG-NARR-01 -->
## Como Chegamos Aqui

### Narrativa do Discovery

O Discovery Pipeline do Veezoozin foi executado em **1 iteracao** com 2 fases:

**Fase 1 — Discovery (8 blocos):**
Conduzida com simulacao de cliente (IA simulando respostas a partir do briefing). Produziu 8 blocos cobrindo desde proposito e visao (1.1) ate TCO e build-vs-buy (1.8). Os blocos foram escritos por agentes especializados: PO (1.1-1.4), Solution Architect (1.5, 1.7, 1.8) e Cyber Security Architect (1.6).

**Fase 2 — Challenge (2 blocos):**
- **Auditor (2.1):** Avaliacao convergente — score de 82%, APROVADO COM RESSALVAS. Identificou divergencias financeiras criticas entre blocos 1.3 e 1.8 como a principal fraqueza.
- **10th-man (2.2):** Avaliacao divergente — score de 62%, APROVADO COM RESSALVAS. Formulou 10 questoes hostis, identificou 14 pontos cegos e definiu 6 itens de monitoramento obrigatorio.

### Status dos Veredictos

| Validador | Score | Veredicto |
|-----------|-------|-----------|
| Auditor (convergente) | 82% | APROVADO COM RESSALVAS |
| 10th-man (divergente) | 62% | APROVADO COM RESSALVAS |

Ambas as validacoes aprovaram o projeto com caveats significativos. O auditor foca nas inconsistencias de negocio (financeiro divergente). O 10th-man foca nas premissas frageis (precisao NL-to-SQL, modelo financeiro) e na ausencia de validacao empirica.

### Maturidade da Informacao

| Fonte | % estimado | Confiabilidade |
|-------|-----------|----------------|
| [BRIEFING] (fornecido pelo cliente/sponsor) | ~55% | Alta |
| [INFERENCE] (inferido pela IA) | ~40% | Media-baixa (requer validacao) |
| [RAG] (documentacao tecnica) | ~5% | Alta |

> **40% do discovery e baseado em inferencias nao validadas pelo cliente.** Isso inclui pricing, composicao do time, salarios, churn, conversao e OKRs. A sessao de Human Review (MON-2) e pre-requisito para qualquer decisao irreversivel.
<!-- /region: REG-NARR-01 -->

---

<!-- region: REG-EXEC-03 -->
## Decisao Go/No-Go

### Recomendacao: **GO CONDICIONAL (Build)**

O Veezoozin tem um problema real, um mercado real e uma abordagem tecnica coerente. O discovery foi competente — melhor que a maioria dos projetos greenfield. Entretanto, o aval para iniciar o desenvolvimento esta condicionado a resolucao de 6 itens obrigatorios.

### Condicoes Obrigatorias (antes ou durante primeiras sprints)

| # | Condicao | Prazo | Owner |
|---|---------|-------|-------|
| 1 | **Human Review** — CTO valida todos os [INFERENCE] criticos (pricing, team, churn, OKRs) | Antes da Sprint 1 | PO + CTO |
| 2 | **Reconciliacao financeira** — Unificar blocos 1.3 e 1.8 em modelo unico (adotar 1.8) | Antes da Sprint 1 | PO |
| 3 | **DPO contratado** (DPO-as-a-Service) | Antes da Sprint 1 | CTO |
| 4 | **Benchmark NL-to-SQL** — 100+ queries contra 3+ schemas reais. Se < 75%, reavaliar viabilidade | Ate Sprint 2 | Backend AI/ML + CTO |
| 5 | **Escopo MVP revisado** — Definir cortes (MCP? multi-idioma? billing?) para caber em 12-16 semanas | Antes da Sprint Planning S1 | PO + CTO + Tech Lead |
| 6 | **Estrategia GTM documentada** — Como adquirir primeiros 5 tenants; 3+ LOIs de piloto | Ate Sprint 3 | CTO |

### Criterios Go/No-Go pos-Benchmark

| Resultado do benchmark | Decisao |
|----------------------|---------|
| Precisao >= 85% | GO — MVP conforme planejado |
| Precisao 75-84% | GO COM AJUSTE — Investir mais em cache/glossario/feedback loop |
| Precisao 60-74% | PIVOT — Reavaliar abordagem tecnica (fine-tuning? modelo especializado?) |
| Precisao < 60% | NO-GO — Produto inviavel com abordagem atual |
<!-- /region: REG-EXEC-03 -->

---

<!-- region: REG-EXEC-04 -->
## Proximos Passos

### Imediatos (esta semana)

| # | Acao | Responsavel | Resultado esperado |
|---|------|-------------|-------------------|
| 1 | Sessao de Human Review (2-3h) com CTO | PO + CTO | Validar/ajustar todos os [INFERENCE] criticos |
| 2 | Contratar DPO-as-a-Service | CTO | DPO nomeado e atuando |
| 3 | Verificar se DPA do contrato GCP cobre Gemini API | CTO | Clareza sobre bloqueante LGPD |
| 4 | Iniciar negociacao DPA com Anthropic | CTO + DPO | Processo em andamento |

### Proximas 2 semanas

| # | Acao | Responsavel | Resultado esperado |
|---|------|-------------|-------------------|
| 5 | Reconciliar modelos financeiros (adotar 1.8 como base) | PO | Modelo unico consolidado |
| 6 | Definir escopo final do MVP (cortes aprovados pelo CTO) | PO + CTO | Sprint backlog realista |
| 7 | Publicar vagas: Tech Lead + Backend AI/ML | CTO | Pipeline de candidatos ativo |
| 8 | Contatar 5+ potenciais tenants piloto | CTO | Pelo menos 3 LOIs |

### Antes do Go-Live

| # | Acao | Prazo |
|---|------|-------|
| 9 | Benchmark NL-to-SQL (100+ queries) | Sprint 2 |
| 10 | DPA com Anthropic e Google assinados | Sprint 5 |
| 11 | RIPD elaborada com suporte do DPO | Sprint 5 |
| 12 | Politica de privacidade publicada | Sprint 6 |
| 13 | Testes de isolamento multi-tenant (automatizados) | Sprint 6 |
| 14 | Pentest focado em bypass de tenant | Sprint 6 |
<!-- /region: REG-EXEC-04 -->

---

<!-- region: REG-DOM-SAAS-01 -->
## Modelo SaaS — Detalhamento

### Arquitetura Multi-Tenant

| Camada | Estrategia de Isolamento |
|--------|-------------------------|
| Aplicacao | Middleware obrigatorio: extrai `tenant_id` do JWT e injeta no contexto |
| Cloud SQL | Row-level filtering: `tenant_id` em todas as tabelas via ORM (SQLAlchemy) |
| Firestore | Collection isolation: `/tenants/{tenant_id}/` com security rules |
| BigQuery | Service account dedicada por tenant com acesso apenas ao seu dataset |
| Secret Manager | Prefixo por tenant: `veezoozin-{tenant_id}-{secret_name}` |
| Cloud Storage | Bucket path por tenant: `gs://veezoozin-exports/{tenant_id}/` |
| Logging | Label obrigatoria `tenant_id` em todo log estruturado |

### Billing por Consumo

| Componente | Custo unitario | Base de calculo |
|-----------|---------------|-----------------|
| LLM API (por query) | $0,0032/query | 6.500 tokens in + 1.500 tokens out (mix de modelos) |
| BigQuery (por query) | $0,00625/query | ~1MB processado por query simples |
| Embeddings (por tabela/mes) | $0,01/tabela/mes | Re-embedding mensal do schema |
| Firestore (por sessao) | $0,0001/sessao | ~10 docs read + 2 write por sessao |
| Storage (por export) | $0,005/export | ~200KB por PDF/HTML |

### Margem por Plano (Ano 1)

| Plano | Receita/mes | Custo variavel/mes | Margem bruta |
|-------|------------|--------------------|----|
| Free | $0 | $0,50 | Negativa (investimento em aquisicao) |
| Starter | $99 | $54,70 | ~45% |
| Business | $299 | $122,50 | ~59% |
| Enterprise | $799+ | $285+ | ~64%+ |
<!-- /region: REG-DOM-SAAS-01 -->

---

<!-- region: REG-DOM-AIML-01 -->
## Estrategia AI/ML — Pipeline NL-to-SQL

### Modelos e Provedores

| Modelo | Uso no Veezoozin | Custo (1M tokens in/out) |
|--------|-------------------|--------------------------|
| Gemini 2.0 Flash | Intent, insights, fallback (60% queries) | $0,10 / $0,40 |
| Claude Sonnet 4 | NL-to-SQL principal (30% queries) | $3,00 / $15,00 |
| Gemini 2.5 Pro | Queries complexas, multi-join (10% queries) | $1,25 / $10,00 |
| Vertex AI text-embedding-005 | Embeddings de schema, glossario e queries | $0,000025/1K chars |

### Pipeline NL-to-SQL (5 fases sincronas)

| Fase | Tecnologia | Latencia estimada (P95) |
|------|-----------|------------------------|
| 1. Deteccao de idioma + Embedding | Vertex AI | 200-500ms |
| 2. Schema Matching (vector search) | Firestore Vector Search | 50-200ms |
| 3. Contexto do tenant (glossario + historico) | Firestore + Cloud SQL | 100-300ms |
| 4. SQL Generation | Claude Sonnet 4 | 1.500-4.000ms |
| 5. Execucao | BigQuery (read-only, timeout 30s, limit 10K rows) | 500-5.000ms |
| 6. Insight Generation | Gemini Flash | 500-2.000ms |
| **Total P95** | — | **3.050-12.500ms** |

### Estrategia de Engine: Hibrido (Vanna.ai + LLM API)

| Decisao | Detalhe |
|---------|---------|
| Framework base | Vanna.ai (open-source NL-to-SQL com RAG integrado) |
| LLM para geracao SQL | Claude Sonnet 4 (melhor raciocinio logico) |
| LLM para insights | Gemini Flash (mais rapido e barato) |
| Fallback | Gemini Pro para queries complexas com contexto grande |
| Multi-tenant | Orquestracao custom sobre Vanna.ai com training data por tenant |
| Precisao esperada | 80-88% (benchmark 1.8). Meta: >= 85%. Risco: 60-75% em schemas desconhecidos (10th-man) |

### Cache Semantico (5 camadas)

| Camada | TTL | Conteudo | Economia |
|--------|-----|----------|----------|
| L1 — Schema Cache | 24h | Schema mapeado + embeddings | 90% latencia |
| L2 — Query Cache | 4h | Hash(pergunta NL) para resultado | 96% latencia, 100% custo LLM |
| L3 — MCP Cache | 1h | Respostas de MCP Servers | Variavel |
| L4 — Embedding Cache | Request | Embeddings computados | Overhead zero |
| L5 — LLM Response Cache | 2h | SQL gerado para perguntas identicas | 100% custo LLM |

> **Nota do 10th-man:** A meta de < 5s so e viavel com cache hit. Sem cache, o pipeline completo leva 8-12s. Recomendacao: priorizar cache semantico na Sprint 2 e implementar streaming de resposta parcial.
<!-- /region: REG-DOM-AIML-01 -->

---

## Apendices

### A. Fontes do Discovery

| Bloco | Titulo | Autor |
|-------|--------|-------|
| 1.1 | Proposito e Visao | PO Agent |
| 1.2 | Personas e Jornada | PO Agent |
| 1.3 | Valor e OKRs | PO Agent |
| 1.4 | Processo, Negocio e Time | PO Agent |
| 1.5 | Tecnologia e Seguranca | Solution Architect |
| 1.6 | Privacidade e Compliance | Cyber Security Architect |
| 1.7 | Macro Arquitetura | Solution Architect |
| 1.8 | TCO e Build vs Buy | Solution Architect |
| 2.1 | Validacao Convergente (Auditor) | Auditor Agent |
| 2.2 | Validacao Divergente (10th-man) | 10th-man |

### B. Glossario de Siglas

| Sigla | Significado |
|-------|-----------|
| NL-to-SQL | Natural Language to SQL |
| TCO | Total Cost of Ownership |
| MCP | Model Context Protocol |
| RAG | Retrieval-Augmented Generation |
| DPO | Data Protection Officer (Encarregado de Dados) |
| DPA | Data Processing Agreement |
| RIPD | Relatorio de Impacto a Protecao de Dados |
| LGPD | Lei Geral de Protecao de Dados |
| RBAC | Role-Based Access Control |
| ARR | Annual Recurring Revenue |
| MRR | Monthly Recurring Revenue |
| ARPU | Average Revenue Per User |
| GTM | Go-to-Market |
| LOI | Letter of Intent |
