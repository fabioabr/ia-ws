---
title: "Briefing — Veezoozin"
project-name: "veezoozin"
project-type: "saas"
client: "mAInd Tech"
author: "Fabio"
created: "2026-04-11"
report-setup: "executive"
status: rascunho
context-templates: [saas, ai-ml, datalake-ingestion]
---

# Briefing — Veezoozin

> Plataforma SaaS de consulta em linguagem natural que converte perguntas humanas em queries de banco de dados (transacional e analítico), gerando gráficos, insights, relatórios e análises — tudo contextualizado pelo domínio de negócio do tenant.

---

## 1. Problema

**Qual problema queremos resolver?**

Empresas possuem dados valiosos distribuídos em bancos de dados transacionais (ERPs, CRMs, sistemas próprios) e analíticos (data warehouses, datalakes, BI), mas o acesso a esses dados é limitado a profissionais técnicos que sabem escrever SQL ou operar ferramentas de BI.

Os problemas concretos:

1. **Barreira técnica** — Gestores, analistas de negócio e executivos dependem de times de dados para obter respostas. Uma pergunta simples como "qual foi o faturamento por região no último trimestre?" vira um ticket que leva dias para ser atendido.

2. **Falta de contexto** — Ferramentas de BI genéricas não entendem o vocabulário do negócio do cliente. "Churn" para uma empresa de telecom é diferente de "churn" para um SaaS. As queries precisam ser contextualizadas pelo domínio.

3. **Dados sem ação** — Mesmo quando os dados são acessados, falta a camada de insight. O usuário recebe uma tabela, mas não sabe o que ela significa. Precisa de gráficos, comparações, tendências e recomendações automatizadas.

4. **Multi-idioma** — Empresas latinas operam em PT-BR, EN-US e Espanhol. O sistema precisa entender perguntas em qualquer idioma e consultar dados independentemente do idioma dos metadados.

O Veezoozin resolve isso com uma camada de inteligência que:
- Recebe perguntas em linguagem natural (PT-BR, EN-US, ES)
- Converte em queries SQL/analíticas contextualizadas pelo domínio do tenant. (Sempre usaremos o BigQuery como banco)
- Retorna resultados visuais: gráficos, insights, relatórios e análises
- Aprende continuamente sobre o contexto de cada tenant

**Impacto mensurável:**
- Tempo de resposta: De dias (ticket para time de dados) para segundos (pergunta → resposta visual)
- Democratização: 100% dos colaboradores podem consultar dados, não apenas os técnicos
- Qualidade: Respostas contextualizadas com gráficos e insights, não tabelas brutas
- Custo: Redução de 60-80% no volume de tickets para o time de dados/BI

**IMPORTANTE:**
- Devemos pensar em possibilidades de controlar o acesso aos dados em nivel de registro/campo.
- Precisamos pensar em como monetizar a plataforma. Com planos por exemplo. (incluindo uma opção free com recursos bem limitados)

---

## 2. Contexto e Domínio

| Item | Resposta |
|------|----------|
| Setor / indústria | Tecnologia — produto SaaS B2B |
| Área da empresa | Produto (mAInd Tech — desenvolve o Veezoozin como produto próprio) |
| Tipo de projeto | Novo produto (greenfield) |
| Maturidade | Greenfield — primeira versão do produto |
| Contexto organizacional | Startup de tecnologia, time enxuto, foco em speed-to-market |

---

## 3. Público-alvo

| Perfil | Descrição | Frequência de uso |
|--------|-----------|-------------------|
| Gestor / Executivo | Faz perguntas de negócio em linguagem natural, recebe dashboards e insights | Diário |
| Analista de negócio | Consultas mais profundas, cruzamento de dados, análises comparativas | Diário (intensivo) |
| Administrador do tenant | Configura o contexto do tenant, ensina o sistema sobre o domínio, gerencia integrações | Semanal |
| Administrador de TI do cliente | Configura conexões com bancos de dados, MCPs, gerencia acessos e segurança | Mensal |

---

## 4. Stakeholders

| Nome / Papel | Função no projeto | Poder de decisão | Disponível? |
|-------------|-------------------|-------------------|-------------|
| Fabio, Arquiteto de Software Sênior Full-Stack | Único desenvolvedor. Usa Claude Code como par de programação para acelerar desenvolvimento. Responsável por arquitetura, backend, frontend, infra e operação. | Total | Sim, dedicado full-time |

---

## 5. Escopo esperado

### Dentro do escopo (o que SIM será feito)

**Core — Consulta em linguagem natural:**
- Interface conversacional web para perguntas em PT-BR, EN-US, ES
- Engine de conversão: linguagem natural → SQL/query contextualizada
- Suporte a bancos transacionais (PostgreSQL, MySQL, SQL Server, Oracle) e analíticos (BigQuery, Snowflake, Redshift)
- Execução segura de queries (read-only, com sandbox e limites)

**Contexto do Tenant — Aprendizado do domínio:**
- Onboarding de tenant: processo de "ensinar" o sistema sobre o domínio de negócio
- Mapeamento automático de schema (tabelas, colunas, relações) com enriquecimento semântico
- Glossário de negócio por tenant (ex: "churn" = cancelamento nos últimos 30 dias para este tenant)
- Histórico de perguntas e feedbacks para aprendizado contínuo
- Sugestão de prompts baseada no contexto e nos dados disponíveis

**Integração com fontes externas de conhecimento:**
- Suporte a MCPs (Model Context Protocols) para conectar RAGs de IA externos
- O tenant pode plugar fontes adicionais de contexto (documentos, wikis, APIs de conhecimento)
- Merge de contexto: dados do banco + RAG externo + glossário do tenant = resposta completa

**Output visual — Resultados ricos:**
- Gráficos automáticos baseados no tipo de dado retornado (barras, linhas, pizza, scatter)
- Insights gerados por IA sobre os dados (tendências, anomalias, comparações)
- Relatórios formatados (exportáveis em PDF/HTML)
- Análises sugeridas pelo sistema ("Você perguntou X, mas talvez queira ver também Y")

**Plataforma SaaS multi-tenant:**
- Isolamento completo de dados entre tenants
- Billing por consumo (queries, storage, tenants)
- Painel administrativo por tenant
- **BYOK (Bring Your Own Key):** Tenant cadastra suas próprias API keys de LLM (Claude, Gemini, etc.) no painel. O custo de chamadas LLM é 100% do tenant — o Veezoozin não paga pelas chamadas.

### Fora do escopo (o que NÃO será feito)

- Escrita/modificação de dados nos bancos do cliente (apenas leitura)
- Treinamento/fine-tuning de LLM próprio (usar APIs: Claude, Gemini)
- ETL/ingestão de dados (o Veezoozin consulta os bancos existentes do cliente)
- App mobile nativo (web responsivo no MVP)
- Integração com ERPs/CRMs diretamente (apenas via banco de dados ou MCP)

### Resultado esperado

- MVP funcional com consulta NL → SQL → visualização em 3 idiomas
- Latência de resposta < 5 segundos para queries simples
- Suporte a pelo menos 5 tenants com 50+ tabelas cada no MVP
- Precisão de query gerada > 85% (query correta na primeira tentativa)
- Custo de infraestrutura < R$ 5K/mês para até 50 tenants no MVP
- Sugestão de prompts com taxa de aceitação > 40%

---

## 6. Restrições conhecidas

| Tipo | Restrição |
|------|-----------|
| **Prazo** | MVP em 4 meses (12 semanas) |
| **Orçamento** | Calcular como output — TCO para operação em GCP |
| **Stack obrigatória** | GCP (Cloud Run, Vertex AI, Cloud SQL, BigQuery, Firestore), Python |
| **Stack proibida** | Nenhuma explicitamente, mas preferência forte por GCP over AWS/Azure |
| **Equipe disponível** | 1 arquiteto de software sênior full-stack (Fabio) + Claude Code como assistente de desenvolvimento. Sem plano de contratação no MVP — o objetivo é validar o produto com equipe mínima antes de investir em time. |
| **Compliance** | LGPD obrigatória — dados dos clientes são sensíveis. Queries não podem expor dados de um tenant para outro |
| **LLM** | Usar APIs externas (Claude API, Gemini API) — não hospedar LLM próprio. **O custo de LLM é do tenant** — cada tenant cadastra sua própria API key no painel do SaaS. O Veezoozin NÃO paga pelas chamadas LLM. |
| **Bancos suportados no MVP** | BigQuery (expandir depois) |
| **MCP** | Suportar protocolo MCP para integração com RAGs externos |
| **Segurança de queries** | Read-only obrigatório. Sandbox com timeout e limite de linhas. Sem acesso a DDL/DML |
| **Outros** | Cliente GCP já tem créditos e incentivos — maximizar uso dos serviços nativos |

---

## 7. Fontes de informação disponíveis

- [x] Conhecimento do time sobre NL-to-SQL, RAG pipelines e arquitetura em GCP
- [ ] Benchmarks de concorrentes: Tableau Ask Data, ThoughtSpot, Dremio, Lightdash AI
- [x] Documentação do GCP (Vertex AI, Cloud Run, Firestore, BigQuery)
- [x] Experiência prévia do time com embeddings, LLM APIs e MCP
- [x] Documentação do protocolo MCP (Model Context Protocol)
- [ ] Nenhum documento formal adicional — apenas este briefing

---

## 8. Expectativa de entrega

- [x] Resumo executivo (one-pager para apresentação rápida)
- [x] Relatório corporativo (visão de negócio, custos, prazos, riscos)
- [ ] Relatório técnico completo (arquitetura, stack, integrações, privacidade)
- [x] Backlog priorizado (épicos para o time de implementação)
- [x] Relatório HTML visual (para apresentar ao sponsor/comitê)

**Público da entrega final:**

```
Time mAInd Tech (execução) + CTO (decisão de arquitetura e investimento)
```

---

## 9. Configurações

| Configuração | Valor | Opções |
|-------------|-------|--------|
| **Nível de detalhe do report** | executive | `essential` / `executive` / `complete` |
| **Rigor da validação** | poc | `padrão` (≥90%) / `alto-risco` (≥95%) / `poc` (≥80%) |
| **Tipo de projeto** | saas + ai-ml + datalake-ingestion | Multi-template: SaaS (multi-tenant, billing) + AI/ML (NL-to-SQL, LLM, embeddings) + Datalake (consulta a bancos analíticos) |
| **Simulação do cliente** | sim | `sim` (IA simula o cliente usando o briefing como base) / `não` (cliente humano real responde durante a Fase 1) |

> [!info] Simulação do cliente
> Quando `sim`, o agente **customer** simula as respostas do cliente durante a entrevista da Fase 1, baseando-se neste briefing + knowledge base + RAG. Útil para testes, dry runs e quando o cliente humano não está disponível. Toda resposta simulada é marcada com `[BRIEFING]`, `[RAG]` ou `[INFERENCE]` para rastreabilidade.
>
> Quando `não`, o pipeline pausa nas perguntas da Fase 1 e espera que o cliente humano real responda.

---

## 10. Notas livres

### Modelo de equipe — 1 dev + Claude Code

O projeto será desenvolvido por **uma única pessoa** (Fabio, arquiteto sênior full-stack) usando **Claude Code** como assistente de desenvolvimento. Não há plano de contratação para o MVP.

**Premissas:**
- Claude Code acelera desenvolvimento em 3-5x para um dev sênior
- 1 pessoa full-stack pode entregar MVP de um SaaS em 3-4 meses com Claude Code
- Sem overhead de gestão, comunicação, onboarding de equipe
- Custo de equipe cai de R$ 6.99M (12 pessoas em 3 anos) para custo de 1 pessoa + licença Claude
- Se o produto validar, contratações futuras são feitas com receita (não com investimento)
- Design: usar templates/componentes prontos + Claude Code para UI (sem designer dedicado)

### Modelo BYOK — LLM por conta do tenant

O custo de chamadas LLM (Claude API, Gemini API) é **100% do tenant**. O Veezoozin não paga pelas chamadas — cada tenant cadastra sua própria API key no painel administrativo. Suportar múltiplos provedores (Claude, Gemini, OpenAI, etc.).

### Modelo de infra — Pay-per-use (custo proporcional à receita)

A infraestrutura GCP é **100% serverless/pay-per-use**. Sem clientes = custo quase zero. Com clientes = custo cresce proporcional ao uso (e portanto à receita).

- **Cloud Run:** cobra por vCPU-second — sem requests, custo zero
- **BigQuery:** cobra por TB processado — sem queries, custo zero
- **Firestore:** cobra por operação — sem uso, custo zero
- **Cloud SQL:** único custo fixo (~R$ 250/mês instância mínima), mas pode usar Firestore para eliminar
- **Vertex AI Embeddings:** cobra por volume de texto processado — custo de onboarding do tenant

O custo de infra **nunca será um problema** porque escala junto com a receita. Quanto mais clientes, mais custo de infra, mas também mais receita.

### Projeção de custos — Custo fixo + variável por cliente

**Custos fixos mensais (independem de quantidade de clientes):**

| Item | Custo/mês |
|------|-----------|
| Fabio (arquiteto sênior) | R$ 15.000 |
| Claude Code (Pro + API) | R$ 1.500 |
| Cloud SQL (instância mínima) | R$ 250 |
| Domínio + DNS + certificados | R$ 50 |
| Ferramentas (GitHub, monitoring) | R$ 200 |
| **Total fixo** | **R$ 17.000/mês** |

**Custo variável por cliente (pay-per-use):**

| Item | Custo estimado/tenant/mês | Premissa |
|------|--------------------------|----------|
| Cloud Run (compute) | R$ 15-50 | ~500-2.000 queries/mês |
| BigQuery (queries) | R$ 10-30 | ~5-20 GB processados/mês |
| Firestore (sessões, cache) | R$ 5-15 | ~10K-50K operações/mês |
| Vertex AI (embeddings onboarding) | R$ 5 (amortizado) | Onboarding único, ~R$ 50 |
| Cloud Storage (logs, exports) | R$ 2-5 | ~1-5 GB/mês |
| Stripe (billing) | 2,9% + R$ 0,30/transação | Sobre receita do plano |
| **Total variável/tenant** | **~R$ 40-100/mês** | Depende do uso |

**Projeção por cenário de crescimento:**

| Cenário | Tenants pagantes | Receita/mês | Custo fixo | Custo variável | Custo total | Margem |
|---------|-----------------|-------------|------------|---------------|-------------|--------|
| MVP (mês 1-3) | 0 | R$ 0 | R$ 17K | R$ 0 | R$ 17K | -R$ 17K |
| Early (mês 4-6) | 3 Pro | R$ 1.5K | R$ 17K | R$ 200 | R$ 17.2K | -R$ 15.7K |
| Tração (mês 7-12) | 10 Pro + 1 Ent | R$ 7K | R$ 17K | R$ 700 | R$ 17.7K | -R$ 10.7K |
| **Break-even** | **~25 Pro + 2 Ent** | **~R$ 17K** | **R$ 17K** | **R$ 2K** | **R$ 19K** | **~R$ 0** |
| Crescimento (mês 18+) | 40 Pro + 5 Ent | R$ 30K | R$ 17K | R$ 3.5K | R$ 20.5K | +R$ 9.5K |
| Escala (mês 24+) | 80 Pro + 10 Ent | R$ 60K | R$ 17K* | R$ 7K | R$ 24K | +R$ 36K |

> *No cenário de escala, pode ser necessário contratar 1 pessoa adicional (SRE/suporte), elevando o fixo para ~R$ 30K.

**Break-even estimado: ~25 tenants Pro + 2 Enterprise** (receita ~R$ 17K/mês cobre os custos fixos + variáveis).

**Premissas importantes:**
- Custo variável/tenant é baixo (~R$ 40-100) porque LLM é BYOK (tenant paga)
- O maior custo é FIXO (pessoa) e não escala com clientes
- A margem bruta por tenant é alta (~80-90%) porque o custo variável é quase só infra GCP
- Contratação adicional só quando receita justificar (não antes)

### Fluxo principal do produto

```
1. SETUP DO TENANT
   Admin cria tenant → conecta banco(s) de dados → sistema mapeia schema automaticamente
   → Admin enriquece com glossário de negócio → sistema aprende o contexto

2. INTEGRAÇÃO DE CONHECIMENTO EXTERNO (opcional)
   Admin configura MCPs → conecta RAGs de IA externos (docs, wikis, APIs)
   → Sistema merge: dados do banco + conhecimento externo + glossário

3. CONSULTA DO USUÁRIO
   Usuário faz pergunta em linguagem natural (PT-BR/EN/ES)
   → Sistema analisa o contexto do tenant
   → Converte em SQL/query contextualizada
   → Executa query (read-only, sandbox)
   → Gera visualização: gráfico + insight + análise

4. SUGESTÃO DE PROMPTS
   Sistema sugere perguntas relevantes baseado em:
   → Schema do banco (tabelas/colunas disponíveis)
   → Histórico de perguntas do tenant
   → Contexto do MCP/RAG
   → Tendências detectadas nos dados

5. OUTPUT RICO
   → Gráfico automático (tipo escolhido por IA baseado nos dados)
   → Insight textual ("Faturamento caiu 12% vs trimestre anterior")
   → Análise comparativa ("Top 5 regiões por receita")
   → Relatório exportável (PDF/HTML)
   → Sugestão de próxima pergunta ("Quer ver o breakdown por produto?")
```

### Contexto GCP

O cliente (que usará o Veezoozin) já tem contrato enterprise com a Google Cloud e recebe incentivos significativos para uso de serviços GCP. Priorizar:
- **Vertex AI** — embeddings de texto e schema, NL-to-SQL com Gemini
- **Cloud Run** — compute serverless para API e workers
- **BigQuery** — como banco analítico suportado nativamente + para analytics internos
- **Cloud SQL** — para metadata e configuração dos tenants
- **Firestore** — para sessões, cache e histórico de conversas
- **Cloud Storage** — para documentos e exports

### Diferencial competitivo

| Concorrente | Limitação | Veezoozin |
|------------|-----------|-----------|
| Tableau Ask Data | Só funciona dentro do Tableau, inglês apenas | Standalone, multi-idioma |
| ThoughtSpot | Enterprise caro, schema rígido | PME-friendly, schema flexível |
| ChatGPT + SQL | Sem contexto de negócio, sem multi-tenant | Contexto por tenant, glossário de negócio |
| Metabase | Dashboard-first, não conversacional | Conversational-first com output visual |

**Posicionamento:** "Pergunte para seus dados" — democratização do acesso a dados via linguagem natural, com contexto de negócio por tenant, multi-idioma nativo (PT-BR/EN/ES), e integração com fontes de conhecimento externas via MCP.

### Nome do produto

"Veezoozin" — nome lúdico e memorável para o mercado latino-americano. Remete a "visualização" de forma informal e acessível.
