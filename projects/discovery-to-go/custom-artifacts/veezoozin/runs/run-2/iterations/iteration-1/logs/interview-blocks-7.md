---
title: "Interview Log — Bloco #7"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [7]
simulation: true
depends-on: [5, 6]
roles:
  solution-architect: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-12
---

# Interview Log — Bloco #7

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto). Nenhuma resposta `[RAG]` nesta sessão.]
>
> **Nota:** Bloco #7 depende dos blocos #5 (Tecnologia e Segurança — D24–D31) e #6 (Privacidade e Compliance — D32–D39). Consolida todas as decisões D1–D39 em uma arquitetura macro coerente. O Solution Architect conduz.

---

## Bloco #7 — Arquitetura Macro

> Usando outputs dos Blocos #1-#6 como base. Todas as 39 decisões anteriores como input. Blueprints carregados: SaaS (Componentes 2 e 3), AI/ML (Componentes 2 e 3), Datalake (Componentes 1 e 4).

| Quem | Diálogo |
|------|---------|
| 🏗️ SA | Vamos definir o padrão arquitetural. Temos 39 decisões acumuladas. A pergunta central: monolith, modular monolith ou microservices? |
| 👤 Customer | [INFERENCE] Modular monolith. O time tem 6 pessoas (D17), monorepo no GitHub (D22), row-level tenancy num banco só (D24), sprints de 1 semana (D18). Microservices seria over-engineering absurdo — não temos nem SRE dedicado até a Fase 2. Mas monolith clássico sem separação de concerns vai virar big ball of mud em 3 meses. Modular monolith: deploy único, boundaries claros entre módulos, comunicação via interfaces e eventos internos. |
| 🏗️ SA | Concordo. Blueprint SaaS é explícito: "microservices prematuros são antipattern #1 para times < 10 pessoas". A pergunta de follow-up: como garantir que os boundaries do monolith não degenerem? |
| 👤 Customer | [INFERENCE] Três mecanismos: (1) Cada módulo tem suas próprias tabelas no Cloud SQL com prefixo — sem JOINs cross-módulo. Dados compartilhados via eventos ou API interna. (2) Dependency inversion — módulos dependem de abstrações (interfaces Python), não de implementações concretas. O NL-to-SQL Engine depende de `LLMProvider`, não de `ClaudeClient`. (3) Linter no CI que detecta imports proibidos cross-módulo. Se o módulo Billing importar algo do NL-to-SQL Engine, o CI falha. |
| 🏗️ SA | 💡 *Observação: abordagem disciplinada. O linter de imports é crucial — sem enforcement automático, boundaries são apenas intenção. Dependency inversion facilita testes (mocks) e futura extração de microservices. Registrar como D40.* |
| 🏗️ SA | Quantos módulos e quais? |
| 👤 Customer | [INFERENCE] Seis módulos de negócio + um Shared Kernel. (1) **NL-to-SQL Engine** — o coração, pipeline de 8 etapas do Bloco #5. (2) **Tenant Context** — schema discovery, glossário, embeddings, histórico, permissões. É o módulo do contexto de negócio, nosso moat. (3) **Visualization & Output** — gráficos, insights, export PDF/HTML, sugestões de prompts (D10). (4) **Admin Panel** — users, roles, RBAC, audit logs, feature flags. (5) **Billing Module** — integração Stripe (D27), usage metering, limites por plano. (6) **MCP Gateway** — integração com fontes externas via Model Context Protocol, mas ativado só na Fase 2. Preparamos a interface no MVP. |
| 🏗️ SA | E o Shared Kernel? |
| 👤 Customer | [INFERENCE] Middleware transversal que todos os módulos usam: Auth (Firebase JWT — D28), Tenant middleware (injection do tenant_id — D24), RBAC engine (D9 — campo/registro), Rate limiter (D14 — por plano), Event bus (in-process), Observability (OpenTelemetry — D20), e um **Privacy Guard** novo — implementa a minimização de PII do D35 antes de qualquer envio ao LLM. |
| 🏗️ SA | 💡 *Observação: o Privacy Guard como componente do Shared Kernel é elegante. Garante que D35 (minimização) é aplicado uniformemente — não depende de cada módulo lembrar de filtrar PII. É uma decisão de arquitetura, não de implementação. Registrar D42 (Shared Kernel) e D45 (Privacy Guard).* |
| 🏗️ SA | Vamos detalhar o pipeline NL-to-SQL na perspectiva arquitetural. O Bloco #5 definiu 8 etapas. Como elas se materializam nos módulos? |
| 👤 Customer | [INFERENCE] As 8 etapas não são todas do mesmo módulo. A etapa 2 (Context Assembly) chama o módulo **Tenant Context** para montar schema + glossário + permissões. O Tenant Context faz semantic search nos embeddings de schema via Vertex AI — seleciona apenas as top-K tabelas relevantes para a pergunta, não envia o schema inteiro. Isso é fundamental: schemas com 50+ tabelas no MVP e 500+ em Enterprise. Enviar tudo ao LLM é desperdício de tokens e dinheiro. |
| 🏗️ SA | Como funciona esse Context Assembly na prática? |
| 👤 Customer | [INFERENCE] Quatro componentes montados em paralelo: (1) Schema relevante — embedding da pergunta → busca nas embeddings de schema do tenant → top-K tabelas e colunas mais relevantes. (2) Glossário — termos que matcham com tokens da pergunta + termos frequentes. (3) Histórico — últimas 5 interações da sessão + 3 exemplos few-shot do tenant. (4) Permissões — tabelas e campos permitidos para o role do usuário, filtros RLS que serão aplicados na etapa 4. Tudo montado em um prompt template estruturado com seções claras: SYSTEM, SCHEMA, GLOSSÁRIO, EXEMPLOS, HISTÓRICO, PERGUNTA. |
| 🏗️ SA | 💡 *Observação: o ponto crucial é a seleção semântica de schema. Sem isso, query cost explode com schemas grandes. A separação em seções no prompt é boa prática — evita que o LLM confunda instrução com dado. Registrar como D43 (Context Assembly via embedding search).* |
| 🏗️ SA | Etapa 4 — Validate + Guard. O Bloco #5 definiu sqlglot e RLS injection. Na arquitetura, onde mora o RLS? |
| 👤 Customer | [INFERENCE] O RLS é injetado como etapa determinística DEPOIS do LLM gerar o SQL. O LLM nunca sabe sobre permissões — ele gera SQL "puro" sem considerar quem está perguntando. O Validate + Guard consulta as permissões do usuário (do módulo Admin/Tenant Context), e injeta WHERE clauses no AST da query via sqlglot. Exemplo: Marina é gestora da região Sul → sqlglot adiciona `WHERE region = 'Sul'` no AST. Isso é crítico: segurança nunca pode ser probabilística. O LLM é probabilístico por natureza. Permissão é determinística. |
| 🏗️ SA | 💡 *Observação: princípio fundamental — "segurança é determinística, não probabilística". Nunca pedir ao LLM para aplicar RLS. O pipeline separa concerns: LLM gera SQL (probabilístico, pode errar), Guard valida e injeta segurança (determinístico, não pode falhar). Registrar como D44.* |
| 🏗️ SA | Agora o multi-tenant na perspectiva de arquitetura. D24 definiu row-level. Como são as camadas de isolamento? |
| 👤 Customer | [INFERENCE] Seis camadas, da rede ao dado: (1) **Rede** — Cloud Armor (D31), WAF, DDoS. (2) **Autenticação** — Firebase Auth (D28), JWT com tenant_id claim. (3) **API Gateway** — Shared Kernel: auth middleware extrai tenant_id, rate limiter aplica limites do plano, tenant middleware injeta no contexto do request. (4) **Aplicação** — SQLAlchemy com filter automático por tenant_id, RBAC engine, RLS injector. (5) **Banco** — RLS policies nativas do PostgreSQL como segunda camada, auditoria de queries sem tenant_id, testes automatizados no CI. (6) **Dados do tenant** — service account dedicada por tenant para BigQuery, credenciais no Secret Manager. |
| 🏗️ SA | 💡 *Observação: defense-in-depth com 6 camadas. Mesmo se uma camada falhar, as outras pegam. A camada 5 (RLS no PostgreSQL) é especialmente importante — é a última barreira antes do dado. A camada 6 (service account por tenant) garante que mesmo no BigQuery, o acesso é isolado. Isso é consistente com D24 e satisfaz a persona Carla (Admin TI — poder de veto).* |
| 🏗️ SA | Cache — o Bloco #5 definiu 4 camadas (D30). Como se materializam na arquitetura? |
| 👤 Customer | [INFERENCE] Quatro camadas com fluxo de lookup ordenado: (1) **Schema cache** — in-memory na instância Cloud Run. Schema do BigQuery do tenant. Refresh quando schema muda ou TTL de 1h. (2) **Exact match** — Firestore no MVP, Redis na Fase 2. Hash da pergunta normalizada + tenant_id. TTL 24h. Hit rate ~15%. Economia: evita ambas chamadas LLM + query BigQuery. (3) **Semantic match** — Vertex AI Vector Search. Embedding da pergunta → nearest neighbor. Threshold > 0.92 para evitar falsos positivos. TTL 24h. Hit rate ~20-25%. Economia: evita chamada LLM de SQL gen, mas re-executa BigQuery (dados podem ter mudado). (4) **Result cache** — Firestore/Redis. Hash do SQL + tenant_id → resultado BigQuery. TTL 1h. Economia: evita BigQuery execution quando semantic cache retorna SQL similar. |
| 🏗️ SA | E a invalidação? |
| 👤 Customer | [INFERENCE] Quatro triggers de invalidação: (1) Schema do BigQuery alterado → invalida camadas 1, 2, 3, 4. (2) Glossário atualizado → invalida camada 3 (embeddings mudaram). (3) Permissões alteradas → invalida camadas 2 e 4 do usuário afetado (RLS pode mudar resultado). (4) TTL expirado → automático via Firestore TTL policy ou Redis EXPIRE. O tenant pode configurar refresh interval do result cache (default 1h). |
| 🏗️ SA | 💡 *Observação: invalidação por evento é a abordagem correta. O threshold de 0.92 no semantic match é conservador — preferimos miss a falso positivo. Economia projetada: de R$ 0,15/query (sem cache) para R$ 0,07/query em 12 meses — atinge meta KR5.2. Registrar como D46.* |
| 🏗️ SA | MCP Gateway — está no roadmap para Fase 2, mas como a arquitetura se prepara no MVP? |
| 👤 Customer | [INFERENCE] O módulo Tenant Context já tem um componente chamado Context Merger que combina schema + glossário + histórico em um contexto unificado para o LLM. No MVP, ele tem duas fontes: BigQuery schema e Cloud SQL glossário. Na Fase 2, adicionamos uma terceira: MCP sources. A interface `ContextSource` é abstrata — qualquer fonte que implementar `get_context(tenant_id, question)` pode ser plugada. As tabelas `mcp_sources` e `mcp_context_cache` já existem no schema do Cloud SQL, mas a feature flag está desabilitada. O módulo MCP Gateway é um "stub" no MVP — código existe, tabelas existem, mas a funcionalidade está off. |
| 🏗️ SA | 💡 *Observação: interface `ContextSource` é o ponto-chave. Abstrair desde o MVP reduz custo de integração na Fase 2 de semanas para dias. As tabelas já migradas evitam migration surpresa. Feature flag (D19) controla ativação. MCP como diferencial competitivo (Bloco #1) — preparar a base é investimento justificado. Registrar como D47.* |
| 🏗️ SA | Escalabilidade — qual o roadmap de evolução da arquitetura? Quando o modular monolith deixa de ser suficiente? |
| 👤 Customer | [INFERENCE] Quatro fases: (1) **MVP (mês 1-4):** monolith single Cloud Run + Cloud SQL single. 12 tenants, 300 queries/dia. Foco em correctness. (2) **Fase 2 (mês 5-7):** monolith com auto-scale (5-10 instâncias), Cloud SQL + read replica, Redis para cache. ~100 tenants, 3.000 queries/dia. (3) **Fase 3 (mês 8-10):** separo o async worker em deploy próprio (Cloud Run Jobs) — exports, batch, cache warmup não devem competir por CPU com queries interativas. ~200 tenants. (4) **Escala (mês 12+):** se a carga justificar, extraio o NL-to-SQL Engine como primeiro microservice. É o único módulo CPU-intensive com necessidade de scaling independente e filas por tier. Comunicação via Pub/Sub. Só faço isso se tiver SRE dedicado. |
| 🏗️ SA | Critério de extração? Como evitar a tentação de extrair cedo demais? |
| 👤 Customer | [INFERENCE] Três critérios simultâneos: (1) O módulo precisa escalar independentemente — não basta ser "grande", precisa ter padrão de carga diferente. O NL-to-SQL Engine é CPU-bound (LLM calls), enquanto o Admin é I/O-bound (CRUD). (2) O time tem SRE dedicado — sem ops capacity, microservice é suicídio operacional. (3) A latência de comunicação inter-serviço via Pub/Sub/gRPC é aceitável para o caso de uso. Se os três não são verdade, mantém no monolith. |
| 🏗️ SA | 💡 *Observação: critérios pragmáticos. "Sem SRE, sem microservice" é uma regra sólida. O NL-to-SQL Engine é o candidato natural ao primeiro microservice — único módulo com chamadas LLM que podem ter latência variável e carga imprevisível (hot tenant com 60 queries/min). Registrar D48 (planejado para Fase 3, não antes).* |
| 🏗️ SA | Última questão: como as decisões de privacidade do Bloco #6 (D32–D39) se materializam na arquitetura? |
| 👤 Customer | [INFERENCE] Quatro pontos de materialização: (1) **Privacy Guard no Shared Kernel** (D45) — implementa D35 (minimização). Intercepta envio de dados ao LLM, verifica classificação de campos no glossário (PII/sensível), trunca resultados individuais, envia apenas agregações. (2) **Feature flag de residência BR** (D38) — Admin Panel por tenant. Se ativo, o `LLMProvider` usa apenas Gemini via Vertex AI BR, desabilita Claude (que processa nos EUA). (3) **Exclusão em 3 fases** (D37) — módulo Admin implementa soft-delete → anonimização (D+30) → hard-delete (D+60). Job diário de limpeza. (4) **Audit logs** — módulo Admin registra toda operação. Event bus propaga `QueryExecuted`, `DataAccessed`, `PermissionChanged`. Logs estruturados com tenant_id, user_id, ação (D20). Persona Carla pode exportar logs para compliance. |
| 🏗️ SA | 💡 *Observação: a privacidade não é um módulo separado — é concern transversal implementado no Shared Kernel + Admin. Abordagem correta: privacy by design, não privacy as afterthought. O feature flag de residência BR (D38) é implementação elegante — mesmo código, comportamento diferente por tenant. Isso permite oferecer "dados 100% no Brasil" como upsell Enterprise sem fork de código.* |
| 🏗️ SA | Vou consolidar. O bloco #7 define a arquitetura macro com as seguintes decisões novas: D40 (modular monolith), D41 (6 módulos), D42 (Shared Kernel), D43 (Context Assembly via embedding), D44 (RLS determinístico), D45 (Privacy Guard), D46 (cache 4 camadas com invalidação), D47 (MCP Gateway preparado no MVP), D48 (primeiro microservice Fase 3), D49 (async worker Fase 2). Total de decisões acumuladas: 49. |
| 👤 Customer | [INFERENCE] Correto. A arquitetura é serverless-first (Cloud Run), modular (6 módulos com boundaries claros), privacy by design (Privacy Guard transversal), e evolucionável (seams para futura extração). As 39 decisões anteriores estão todas mapeadas para componentes concretos. O diagrama C4 L1 mostra o contexto, L2 os containers, L3 os componentes internos do API Server. |

---

## Resumo de Decisões do Bloco #7

| # | Decisão | Fonte |
|---|---------|-------|
| D40 | Modular monolith como padrão arquitetural no MVP | [INFERENCE] — justificado por D17, D22, D24 |
| D41 | 6 módulos de negócio: NL-to-SQL Engine, Tenant Context, Visualization, Admin, Billing, MCP Gateway | [INFERENCE] — decomposição por bounded context |
| D42 | Shared Kernel: auth, tenant, RBAC, rate limit, events, observability, privacy guard | [INFERENCE] — concerns cross-cutting |
| D43 | Context Assembly via semantic search em embeddings de schema (não envia schema inteiro) | [INFERENCE] — otimização de tokens e custo |
| D44 | RLS injection determinística na etapa 4 do pipeline, nunca delegada ao LLM | [INFERENCE] — "segurança é determinística, não probabilística" |
| D45 | Privacy Guard como componente do Shared Kernel | [INFERENCE] — implementa D35 uniformemente |
| D46 | Cache em 4 camadas com invalidação por evento | [INFERENCE] — materializa D30 |
| D47 | MCP Gateway preparado no MVP (interface + tabelas + feature flag off) | [INFERENCE] — reduz custo de integração na Fase 2 |
| D48 | NL-to-SQL Engine como primeiro microservice extraído (mês 12+, se necessário) | [INFERENCE] — único módulo com necessidade de scaling independente |
| D49 | Async Worker como deploy separado a partir da Fase 2 | [INFERENCE] — separação de compute interativo vs batch |

---

> **Decisões acumuladas na Discovery:** D1–D49 (49 decisões em 7 blocos)
> **Próximo bloco:** #8 — Backlog e Épicos
