---
title: "Interview Log — Blocos #5 e #6"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [5, 6]
simulation: true
parallel: true
roles:
  solution-architect: claude-code
  cyber-security-architect: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-11
---

# Interview Log — Blocos #5 e #6

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto). Nenhuma resposta `[RAG]` nesta sessão.]
>
> **Nota:** Blocos #5 e #6 rodam em paralelo conforme decisão D23 (P23 — única exceção à regra de blocos sequenciais). O Solution Architect conduz o #5, o Cyber Security Architect conduz o #6. O orchestrator intercala as sessões.

---

## Bloco #5 — Tecnologia e Segurança

> Usando outputs dos Blocos #1-#4 como base. Blueprints carregados: SaaS (Componente 2 — Tenancy e Infraestrutura, Componente 3 — Billing), AI/ML (Componente 2 — Desenvolvimento de Modelos, Componente 3 — MLOps e Serving), Datalake (Componente 1 — Aquisição de Dados).

| Quem | Diálogo |
|------|---------|
| 🏗️ SA | Vamos definir a stack. O briefing é explícito sobre GCP. Quais serviços especificamente? |
| 👤 Customer | [BRIEFING] Stack obrigatória: GCP — Cloud Run, Vertex AI, Cloud SQL, BigQuery, Firestore, Python. Temos créditos e incentivos GCP. Maximizar uso de serviços nativos. [INFERENCE] Cloud Run para compute serverless — pago por uso, auto-scaling. Cloud SQL PostgreSQL para metadata. Firestore para cache e sessões. BigQuery para queries dos tenants (read-only). Vertex AI para embeddings de schema e como endpoint para Gemini. |
| 🏗️ SA | 💡 *Observação: stack 100% GCP-native. Custo controlado via créditos. Cloud Run é boa escolha para startup — sem ops overhead de Kubernetes. Consistente com D20 (observabilidade GCP-native) e time enxuto (D17).* |
| 🏗️ SA | Backend language e framework? |
| 👤 Customer | [BRIEFING] Python obrigatório. [INFERENCE] FastAPI como framework — async nativo, tipagem Pydantic para validação, documentação OpenAPI automática. É o padrão para APIs que integram com LLMs. O Backend NL-to-SQL do Bloco #4 vai usar LangChain para orquestração de prompts. |
| 🏗️ SA | E o frontend? |
| 👤 Customer | [INFERENCE] TypeScript com React e Next.js. SSR para performance e SEO. Ecossistema React tem as melhores bibliotecas de gráficos — Recharts ou Nivo para os gráficos automáticos. Next.js deploy no Cloud Run como container. |
| 🏗️ SA | 💡 *Observação: Python backend + TypeScript frontend é combinação madura. D22 (monorepo) facilita — apps/api e apps/web no mesmo repo. Next.js no Cloud Run funciona bem.* |
| 🏗️ SA | Agora o coração do produto: pipeline NL-to-SQL. Blueprint AI/ML Componente 2 pede que definamos tipo de modelo, abordagem e métricas. Como funciona? |
| 👤 Customer | [BRIEFING] D3 — APIs externas (Claude, Gemini), sem LLM próprio. [INFERENCE] O pipeline tem 8 etapas: Input (detectar idioma, normalizar) → Context Assembly (schema + glossário + histórico + permissões do usuário via embeddings) → SQL Generation (LLM gera SQL com few-shot examples do tenant) → Validate + Guard (sqlglot parse, whitelist, RLS injection — D4 read-only, D9 campo/registro) → Execute (BigQuery read-only via service account) → Result Process (detectar tipo de gráfico) → Insight Generation (LLM interpreta resultados) → Output (gráfico + insight + sugestão). |
| 🏗️ SA | Latência total? |
| 👤 Customer | [INFERENCE] Alvo: < 5 segundos p50 (KR2.3 do Bloco #2). Context Assembly < 500ms (embedding search). SQL Generation < 2s (LLM call). Validate < 200ms. Execute < 2s (BigQuery). Insight Gen < 1.5s (LLM call paralela com result processing se possível). Sobra margem. P99 vai ser mais alto — < 15s para Pro, < 10s para Enterprise. |
| 🏗️ SA | 💡 *Observação: 2 chamadas LLM por query (SQL gen + insight gen). Principal fator de latência e custo. Cache de queries é crítico — se 30-40% das queries baterem cache, reduz tanto latência quanto custo de LLM.* |
| 🏗️ SA | Sobre o cache — como funciona? |
| 👤 Customer | [INFERENCE] Dois níveis: exact match (hash da pergunta normalizada + tenant_id, TTL 24h) e semantic match (embedding da pergunta, nearest neighbor no cache, TTL 24h). O exact match pega ~15% das queries — mesma pergunta repetida. O semantic match pega mais ~25% — perguntas similares ("faturamento do mês" vs "faturamento mensal"). Junto: ~30-40% de economia de chamadas LLM. Cache de schema do BigQuery do tenant em memória (refresh quando schema muda). Cache de resultados BigQuery por 1h para queries idênticas. |
| 🏗️ SA | 💡 *Observação: cache em 4 camadas. No MVP, Firestore para exact match e schema cache. Semantic match exige embedding da pergunta + vector search — pode usar Vertex AI Matching Engine ou Firestore vector search. Na Fase 2 com Redis (Memorystore) para performance. Economia de LLM crítica para meta KR5.2 (< R$ 0,08/query em 12 meses).* |
| 🏗️ SA | Vamos ao multi-tenant. Blueprint SaaS Componente 2: database-per-tenant, schema-per-tenant ou row-level? Gap G3 do Bloco #2. |
| 👤 Customer | [INFERENCE] Row-level com tenant_id no MVP. Uma instância Cloud SQL com todas as tabelas filtradas por tenant_id. O time é enxuto (D17 — 6 pessoas), não temos ops capacity para gerenciar N databases. Row-level é simples: 1 migration, 1 backup, 1 monitoring. O risco é cross-tenant leak, mas mitigamos com middleware obrigatório, RLS no PostgreSQL, testes automatizados e auditoria. Para Enterprise na Fase 2: opção de database dedicado para quem exige isolamento total — provisioning automático. |
| 🏗️ SA | 💡 *Observação: row-level é a escolha certa para MVP com time enxuto. O risco de cross-tenant leak é real mas gerenciável com as 5 camadas de proteção (middleware, query builder, testes, auditoria, RLS nativo). Database dedicado para Enterprise é upsell natural — cobrar mais por isolamento. Registrar como D24.* |
| 🏗️ SA | Autenticação? Gap G4 do Bloco #2 — SSO para Enterprise. |
| 👤 Customer | [INFERENCE] Firebase Auth no MVP. Suporta email+senha e magic link nativamente. Para Enterprise na Fase 2: SAML 2.0 via Firebase Auth SAML provider — integra com Okta, Azure AD, Google Workspace. A persona Carla (Admin TI) exige isso. 2FA com TOTP (Google Authenticator) no MVP, opcional para Free/Pro, obrigatório para Enterprise. JWT com access token de 15 min e refresh de 7 dias. |
| 🏗️ SA | 💡 *Observação: Firebase Auth é GCP-native, custo zero para até 50K usuarios mensais, suporta SAML para upgrade posterior. Boa escolha para MVP. Carla vai aceitar se 2FA estiver disponível e SAML no roadmap.* |
| 🏗️ SA | Billing — o blueprint SaaS avisa: "billing custom no MVP é antipattern #2". Build ou buy? |
| 👤 Customer | [BRIEFING] D13 — monetização híbrida: assinatura + usage + add-ons. [INFERENCE] Stripe, sem dúvida. Stripe Billing suporta assinatura + Usage Records nativamente. Webhook para provisioning automático — quando o Stripe confirma pagamento, Cloud Run provisiona o tenant com os limites do plano. Dunning automático, invoicing, portal do cliente — tudo pronto. Custo de 2.9% + R$ 0,60 por transação é aceitável no estágio atual. Para NFe (nota fiscal brasileira): API separada na Fase 2, Stripe não faz NFe nativamente. |
| 🏗️ SA | 💡 *Observação: Stripe é o padrão de mercado. Time de 6 pessoas (D17) não tem bandwidth para billing custom. 2.9% sobre MRR de R$ 32K (mês 12) = ~R$ 928/mês — custo irrelevante versus semanas de desenvolvimento. Registrar como D27.* |
| 🏗️ SA | Segurança do pipeline NL-to-SQL — o grande concern. Prompt injection, SQL injection via LLM, data exfiltration. |
| 👤 Customer | [INFERENCE] Três camadas de defesa: (1) sqlglot como SQL parser — parse da query gerada pelo LLM, reconstrói AST, whitelist de funções permitidas, rejeita qualquer DDL/DML. Nunca executa string raw. (2) Separação de prompt do sistema vs input do usuário — o input do usuário vai em campo delimitado, nunca concatenado com instruções do sistema. (3) RLS injection na etapa Validate — injeta WHERE clauses de permissão DEPOIS do LLM gerar o SQL, nunca pede ao LLM para aplicar permissões. Permissão é lógica determinística, não probabilística. |
| 🏗️ SA | 💡 *Observação: abordagem defense-in-depth. O ponto crucial é "permissão é lógica determinística, não probabilística" — nunca confiar no LLM para aplicar controle de acesso. sqlglot é open-source, suporta BigQuery dialect, permite AST manipulation. Excelente escolha. Registrar como D29.* |
| 🏗️ SA | Rate limiting — como proteger contra abuso e hot tenants? |
| 👤 Customer | [BRIEFING] D14 — fair use 5.000 queries/mês no Pro. [INFERENCE] Rate limit em 3 dimensões: por dia (Free: 10, Pro: ilimitado, Enterprise: ilimitado), por minuto (Free: 2, Pro: 20, Enterprise: 60), e concurrent (Free: 1, Pro: 3, Enterprise: 10). Implementação: Firestore counter com TTL no MVP, Redis (Memorystore) na Fase 2. HTTP 429 com Retry-After header. Mensagem amigável no frontend sugerindo upgrade. Além disso, Cloud Armor (WAF) para rate limit global e proteção DDoS. |
| 🏗️ SA | 💡 *Observação: 3 dimensões de rate limit (dia, minuto, concurrent) protegem contra diferentes tipos de abuso. 429 com mensagem de upgrade é boa UX + driver de conversão. Cloud Armor para proteção de infra — GCP-native, custo baixo.* |
| 🏗️ SA | Integrações externas — quais no MVP e quais depois? |
| 👤 Customer | [BRIEFING] BigQuery (tenant), Claude API, Gemini API, MCP para RAG externo (Fase 2). [INFERENCE] No MVP: BigQuery (gRPC), Claude API (REST), Gemini via Vertex AI (gRPC), Stripe (REST + webhooks), Firebase Auth (SDK), e email transacional (SendGrid ou Resend — REST). Na Fase 2: multi-banco (PostgreSQL, MySQL, SQL Server), MCP, Slack/Teams para notificações, Okta/Azure AD para SSO, API NFe para notas fiscais. |
| 🏗️ SA | 💡 *Observação: 6 integrações no MVP — gerenciável. Cada uma com autenticação via Secret Manager (GCP). Service accounts por tenant para BigQuery — cada tenant fornece sua própria credential com permissão read-only. Veezoozin nunca armazena dados do BigQuery do tenant — apenas transita no pipeline.* |
| 🏗️ SA | Escalabilidade — projeção de carga para 12 meses. |
| 👤 Customer | [INFERENCE] MVP: 12 tenants, ~50 usuários, ~300 queries/dia. Cloud Run com 1-2 instâncias basta. 6 meses: ~100 tenants, ~500 usuários, ~3.000 queries/dia. Cloud Run escala automaticamente para 5-10 instâncias. 12 meses: ~300 tenants, ~2.000 usuários, ~15.000 queries/dia. Cloud Run 10-20 instâncias, Cloud SQL precisa de read replicas, Memorystore para cache. Hot tenant protection: rate limit por tenant + queue isolation para Enterprise na Fase 2 + PgBouncer para connection pooling. |
| 🏗️ SA | 💡 *Observação: Cloud Run auto-scaling cobre os 12 primeiros meses sem intervenção. O bottleneck será Cloud SQL connections — PgBouncer resolve. BigQuery é serverless, escala transparente. LLM APIs: distribuir entre Claude e Gemini para evitar rate limit de um único provider. Arquitetura serverless-first é correta para o estágio.* |

---

## Bloco #6 — Privacidade e Compliance

> Usando outputs dos Blocos #1-#4 + decisões do Bloco #5 em andamento (D24 row-level, D26 Claude/Gemini, D27 Stripe, D28 Firebase Auth). Blueprint carregado: SaaS (Concerns transversais — Privacidade).

| Quem | Diálogo |
|------|---------|
| 🔒 CSA | Antes de tudo: LGPD modo profundo ou magro? |
| 👤 Customer | [BRIEFING] LGPD obrigatória — dados dos clientes são sensíveis. Queries não podem expor dados de um tenant para outro. [INFERENCE] Modo profundo, sem dúvida. O Veezoozin processa queries que podem retornar CPF, nome, salário — qualquer PII que estiver no BigQuery do tenant. Além disso, enviamos perguntas em linguagem natural para APIs externas (Claude, Gemini) que podem conter PII. Multi-tenant com risco de cross-tenant leak. Não existe cenário de modo magro aqui. |
| 🔒 CSA | 💡 *Observação: modo profundo confirmado. O Veezoozin tem 3 vetores de risco LGPD: (1) dados de conta dos usuários (controlador), (2) dados do banco do tenant transitando no pipeline (operador), (3) dados enviados a LLMs externos (sub-operadores). Os 3 exigem tratamento distinto.* |
| 🔒 CSA | Papéis LGPD — controlador ou operador? |
| 👤 Customer | [INFERENCE] Duplo papel. mAInd Tech é controladora dos dados de conta e uso — decidimos o que coletar, por que e como. E somos operadores dos dados do banco do tenant — processamos sob instrução do tenant (controlador). O tenant é quem decide quais dados disponibiliza para o Veezoozin consultar. Precisamos de DPA com cada tenant. |
| 🔒 CSA | 💡 *Observação: duplo papel é comum em SaaS B2B. O ponto crítico é: o tenant (controlador) garante que tem base legal para os dados em seu banco. Veezoozin como operador trata sob instrução. Cláusula contratual obrigatória: "tenant declara ter base legal para os dados que disponibiliza". Registrar como D33.* |
| 🔒 CSA | Sub-processadores — quem recebe dados pessoais? O blueprint SaaS exige DPA com cada um. |
| 👤 Customer | [BRIEFING] Claude API (Anthropic), Gemini API (Google). [INFERENCE] Lista completa: Anthropic (Claude — recebe perguntas NL + contexto que pode conter PII), Google (Gemini/Vertex AI — idem, + embeddings + toda a infra GCP), Stripe (dados de billing — tokenizado, PCI compliant), email provider (SendGrid ou Resend — email + nome). Todos nos EUA exceto GCP que pode ser configurado para região BR (southamerica-east1). |
| 🔒 CSA | O concern mais grave: PII nas chamadas LLM. Quando Marina pergunta "qual o salário do João Silva?", essa pergunta vai para o Claude. E quando o resultado volta com CPFs e salários, vai para o Gemini gerar insight. Como mitigar? |
| 👤 Customer | [INFERENCE] Quatro mitigações: M1 — documentar no DPA que queries contêm PII sob instrução do controlador (tenant). M2 — Anthropic e Google não usam dados de API para treinamento, confirmar contratualmente. M3 — truncar resultados antes de enviar ao LLM para insight gen — enviar apenas agregações, nunca dados individuais com PII. M4 — campos marcados como "sensíveis" no glossário (configurados pelo Lucas, Admin Tenant) nunca têm valores individuais incluídos no prompt de insight. |
| 🔒 CSA | 💡 *Observação: M3 e M4 são as mitigações mais efetivas. M3 (truncar resultados) reduz drasticamente o volume de PII que transita para LLMs. M4 (glossário com campos sensíveis) coloca o controle nas mãos do tenant — o Lucas (Admin Tenant) decide o que é sensível. Consistente com D9 (controle de acesso por campo/registro). Registrar como D35 (minimização de dados em chamadas LLM).* |
| 🔒 CSA | DPO — LGPD art. 41 exige encarregado. Quem? |
| 👤 Customer | [INFERENCE] No MVP, Fabio (CTO) acumula a função de DPO. Time enxuto (D17), poucos tenants, risco controlado. Na Fase 2, quando entrarem os primeiros Enterprise, terceirizamos para escritório jurídico especializado — custo de R$ 2.000-5.000/mês. Com 50+ tenants, DPO interno dedicado. Canal de contato: dpo@veezoozin.com. Nome e contato publicados no site e na política de privacidade. |
| 🔒 CSA | 💡 *Observação: acumular DPO no MVP é prática comum em startups. O risco é baixo com poucos tenants. Mas o RIPD precisa estar pronto antes do lançamento — se a ANPD solicitar e não existir, a multa pode chegar a 2% do faturamento. Registrar D34 (DPO) e D36 (RIPD obrigatório antes do MVP).* |
| 🔒 CSA | Bases legais por categoria de dados — vamos mapear. |
| 👤 Customer | [INFERENCE] Dados de conta (nome, email): execução de contrato — necessário para prestar o serviço. Dados de auth: execução de contrato. Billing: obrigação legal (NFe). Dados de uso (queries, frequência): legítimo interesse — melhoria do serviço, sugestão de prompts (D10), detecção de anomalias. Histórico de conversas: execução de contrato — faz parte do serviço contratado. Dados de query do banco: instrução do controlador (tenant) via DPA. Cookies não essenciais: consentimento. |
| 🔒 CSA | Legítimo interesse para dados de uso exige LIA (Legitimate Interest Assessment). Passa no teste? |
| 👤 Customer | [INFERENCE] Finalidade legítima: sim — melhoria do serviço, sugestão de prompts, anti-fraude. Necessidade: sim — sem dados de uso, impossível melhorar precisão ou detectar churn. Balanceamento: dados de uso são expectativa razoável do titular ao usar SaaS. Não inclui PII do banco do tenant. Salvaguardas: pseudonimização em analytics, TTL por plano, opt-out de telemetria. Conclusão: passa no LIA. |
| 🔒 CSA | 💡 *Observação: LIA bem fundamentado. O ponto de atenção é o opt-out de telemetria — precisa estar nas configurações do usuário, não escondido. Sugestão de prompts (D10 do Bloco #2) depende de dados de uso — se o usuário fizer opt-out, perde a feature. Essa trade-off deve ser clara.* |
| 🔒 CSA | Direito ao esquecimento em multi-tenant — o blueprint SaaS pergunta: "como remover dados sem quebrar referências históricas?" |
| 👤 Customer | [INFERENCE] Exclusão em 3 fases: (1) Soft-delete imediato — marca deleted_at, dados somem de queries, período de recuperação de 30 dias. (2) Anonimização no D+30 — substitui PII por valores genéricos ("Usuário Anônimo #hash"), mantém métricas agregadas. (3) Hard-delete no D+60 — remove de Cloud SQL, Firestore, Vertex AI (embeddings), Cloud Logging (set retention). Exceções: NF-e retida por 5 anos (obrigação legal), logs de auditoria anonimizados retidos por 1 ano, métricas agregadas retidas indefinidamente (não são PII). |
| 🔒 CSA | 💡 *Observação: 3 fases é elegante. O período de recuperação de 30 dias evita exclusões acidentais (tenant cancela e volta). A anonimização preserva métricas sem PII. O hard-delete remove tudo. Referências históricas são mantidas via dados anonimizados — "Usuário Anônimo" em vez de buraco no banco. Registrar como D37.* |
| 🔒 CSA | Política de retenção — por tipo de dado e por plano. |
| 👤 Customer | [BRIEFING] D11 — histórico: Free 7 dias, Pro 90 dias, Enterprise 365 dias. [INFERENCE] Conversas: TTL do plano. Cache de queries: 24h (todos). Resultados de query: não persistidos — transientes no pipeline. Dados de conta: enquanto ativo + 30 dias pós-cancelamento. Logs de auditoria: Free 30 dias, Pro 90, Enterprise 365, anonimizados retidos 1 ano. Billing (NF-e): 5 anos. Métricas agregadas: indefinido (não PII). |
| 🔒 CSA | Implementação técnica da retenção? |
| 👤 Customer | [INFERENCE] Firestore TTL policies para conversas e cache — automático, sem job. Cloud Logging retention policy por bucket (30/90/365 dias). Cloud SQL: job diário de limpeza (check deleted_at + TTL, anonimiza ou remove). Vertex AI: exclusão de embeddings via API quando tenant é removido. Tudo automatizado — não pode depender de processo manual. |
| 🔒 CSA | 💡 *Observação: Firestore TTL é perfeito para conversas — deleta automaticamente sem job. Cloud Logging retention policies são nativas e confiáveis. O job de Cloud SQL é o único que precisa de engenharia custom — incluir no sprint 11-12 (QA/Polish do Bloco #4). Alerta se job falhar.* |
| 🔒 CSA | Transferência internacional de dados — perguntas NL vão para Anthropic nos EUA. |
| 👤 Customer | [INFERENCE] Fluxos internacionais: Claude API (EUA), Stripe (EUA), email provider (EUA). Gemini via Vertex AI pode ser configurado para região BR (southamerica-east1) — preferir. GCP infra na região BR. Mitigações: SCC (Cláusulas Contratuais Padrão) no DPA com cada sub-processador nos EUA. Minimização de dados. Transparência na política de privacidade. Para Enterprise com requisito de residência total no BR: usar apenas Gemini (Vertex AI BR) como LLM, desabilitar Claude. Feature flag por tenant. |
| 🔒 CSA | 💡 *Observação: opção Enterprise "BR-only" é diferencial competitivo — empresas reguladas (saúde, financeiro) vão exigir. Feature flag por tenant (D19 — feature flags do Bloco #4) permite controle granular. Registrar como D38. O custo é perder Claude como opção — Gemini precisa ter qualidade suficiente de SQL generation. Testar na Fase 2.* |
| 🔒 CSA | RIPD — precisa? |
| 👤 Customer | [INFERENCE] Sim, obrigatoriamente. Três razões: (1) tratamento de dados pessoais em larga escala (multi-tenant), (2) uso de IA/LLMs para processar dados que podem conter PII, (3) transferência internacional de dados. Se a ANPD solicitar e não existir, é infração grave. Deve estar pronto antes do lançamento — semana 13-14 do cronograma do Bloco #4. |
| 🔒 CSA | 💡 *Observação: RIPD deve ser deliverable do MVP, não pós-lançamento. Incluir no sprint de QA/Security review (semana 13-14). Conteúdo já está mapeado neste bloco — classificação de dados, bases legais, riscos, mitigações. O DPO (Fabio) assina e publica. Registrar D36.* |
| 🔒 CSA | Personas e privacidade — como cada persona interage com os concerns de LGPD? |
| 👤 Customer | [INFERENCE] Marina (Gestora) — pode fazer perguntas que revelam PII. Mitigação: RLS garante que ela só vê dados do seu escopo (D9). Campos sensíveis mascarados. Rafael (Analista) — uso intensivo, muito PII transitando. Mitigação: cache reduz re-processamento, logs auditam tudo. Lucas (Admin Tenant) — configura classificação de campos sensíveis no glossário. É a pessoa-chave para M4 (minimização). Carla (Admin TI) — poder de veto. Precisa ver logs de auditoria, DPA, RIPD. Se não estiverem disponíveis, ela barra a adoção. Este bloco inteiro é para a Carla poder dizer "sim". |
| 🔒 CSA | 💡 *Observação: "Este bloco inteiro é para a Carla poder dizer sim" — frase perfeita. Todo o trabalho de privacidade e compliance tem como output final: Carla (Admin TI) aprova o uso do Veezoozin na empresa. Sem essa aprovação, não há venda Enterprise.* |
| 🔒 CSA | Processo de notificação de incidentes à ANPD? |
| 👤 Customer | [INFERENCE] Data breach: notificar ANPD em 72 horas (best practice, LGPD não fixa prazo exato). Notificar titulares afetados no mesmo prazo. Cross-tenant leak: mesmo processo — é incidente de segurança com potencial acesso indevido. Template de notificação pré-preparado: natureza dos dados, titulares afetados, medidas adotadas. Runbook de incident response inclui checklist de LGPD. |
| 🔒 CSA | 💡 *Observação: 72 horas é referência GDPR adotada como best practice para LGPD. Template pré-preparado é essencial — no meio de um incidente, ninguém quer redigir notificação. Incluir no runbook de on-call (D21 do Bloco #4).* |
| 🔒 CSA | DPA com sub-processadores — status? |
| 👤 Customer | [INFERENCE] Anthropic tem DPA disponível no site. Google Cloud DPA é padrão no contrato enterprise. Stripe DPA é padrão. Email provider (SendGrid/Resend) tem DPA. Todos precisam ser revisados e assinados antes do lançamento. Não lançar sem DPA com todos. |
| 🔒 CSA | 💡 *Observação: DPA é pré-requisito de lançamento, não nice-to-have. Incluir no checklist de go-live (semana 15-16 do cronograma). Registrar como D39.* |

---

## Decisões consolidadas — Blocos #5 e #6

| # | Decisão | Bloco | Justificativa | Status |
|---|---------|:-----:|---------------|--------|
| D24 | Row-level multi-tenancy no MVP (tenant_id) | #5 | Custo baixo, operação simples para time enxuto (D17). Database dedicado para Enterprise na Fase 2. | ✅ |
| D25 | FastAPI (Python) + Next.js (TypeScript) | #5 | Python obrigatório. FastAPI async + tipagem. Next.js SSR + React para gráficos. | ✅ |
| D26 | Claude primário, Gemini secundário/fallback | #5 | Claude melhor SQL gen + contexto longo. Gemini com créditos GCP + fallback. | ✅ |
| D27 | Stripe para billing (Buy) | #5 | Assinatura + usage nativo. < 1 semana vs 4-8 semanas build. Antipattern #2 SaaS. | ✅ |
| D28 | Firebase Auth para autenticação | #5 | GCP-native, SAML/OIDC para Enterprise na Fase 2. Zero custo até 50K users. | ✅ |
| D29 | sqlglot como SQL parser/validator | #5 | Open-source, BigQuery dialect, AST validation, whitelist de funções. | ✅ |
| D30 | Cache de queries (exact + semantic) | #5 | ~30-40% economia LLM. Critical path para KR5.2 (< R$ 0,08/query). | ✅ |
| D31 | Cloud Armor (WAF) para DDoS + rate limit global | #5 | GCP-native, integra Cloud Run. Protege contra DDoS direcionado. | ✅ |
| D32 | LGPD modo profundo obrigatório | #6 | Multi-tenant + PII em queries + LLMs externos. Sem cenário de modo magro. | ✅ |
| D33 | mAInd Tech: controladora (conta/uso) + operadora (banco tenant) | #6 | Duplo papel LGPD. DPA com cada tenant obrigatório. | ✅ |
| D34 | DPO: Fabio acumula no MVP → terceirizar Fase 2 | #6 | Time enxuto. DPO terceirizado quando Enterprise (~R$ 2-5K/mês). | ✅ |
| D35 | Minimização de dados em chamadas LLM | #6 | Não enviar PII individual ao LLM. Truncar resultados. Schema relevante apenas. | ✅ |
| D36 | RIPD obrigatório antes do lançamento do MVP | #6 | IA + larga escala + transferência internacional. Risco de infração grave. | ✅ |
| D37 | Exclusão em 3 fases (soft-delete → anonimização → hard-delete) | #6 | Recuperação 30d + métricas preservadas + compliance LGPD. | ✅ |
| D38 | Opção Enterprise "BR-only" (apenas Gemini/Vertex BR) | #6 | Residência de dados para tenants regulados. Feature flag por tenant. | ✅ |
| D39 | DPA com todos sub-processadores antes do lançamento | #6 | Pré-requisito legal. Sem DPA = sem lançamento. | ✅ |

---

> **Sessão anterior:** Blocos #3 e #4 (interview-blocks-3-4.md)
> **Próxima sessão:** Blocos #7 e #8 (Arquitetura Macro + TCO)
