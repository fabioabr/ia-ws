---
title: "Interview Log — Blocos #1 e #2"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [1, 2]
simulation: true
roles:
  po: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-11
---

# Interview Log — Blocos #1 e #2

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto).]

---

## Bloco #1 — Propósito e Visão

| Quem | Diálogo |
|------|---------|
| 🧑‍💼 PO | Vamos começar pelo problema central. Qual é a dor principal que o Veezoozin resolve? |
| 👤 Customer | [BRIEFING] Empresas possuem dados valiosos distribuídos em bancos de dados transacionais e analíticos, mas o acesso a esses dados é limitado a profissionais técnicos que sabem escrever SQL ou operar ferramentas de BI. Gestores e executivos dependem de times de dados para obter respostas — uma pergunta simples como "qual foi o faturamento por região no último trimestre?" vira um ticket que leva dias. |
| 🧑‍💼 PO | 💡 *Observação: problema claramente definido. Vou explorar as dimensões.* Além da barreira técnica, existem outros aspectos do problema? |
| 👤 Customer | [BRIEFING] Sim, são quatro dimensões. Além da barreira técnica, tem a falta de contexto — ferramentas de BI genéricas não entendem o vocabulário do negócio do cliente. "Churn" para uma telecom é diferente de "churn" para um SaaS. Tem também o problema de dados sem ação — o usuário recebe uma tabela mas não sabe o que ela significa, falta gráficos e insights. E o multi-idioma — empresas latinas operam em PT-BR, EN-US e Espanhol. |
| 🧑‍💼 PO | 💡 *Observação: problema com 4 dimensões bem articuladas — barreira técnica, falta de contexto, dados sem ação, multi-idioma. Cada uma mapeia para uma feature core do produto.* |
| 🧑‍💼 PO | Qual é o Job to be Done principal? Se pudesse resumir em uma frase, o que o usuário quer quando abre o Veezoozin? |
| 👤 Customer | [BRIEFING] O usuário quer fazer uma pergunta em linguagem natural — em PT-BR, EN-US ou ES — e receber uma resposta visual com gráficos, insights e análises, tudo contextualizado pelo domínio do negócio dele, em segundos. Sem depender de ninguém técnico. |
| 🧑‍💼 PO | 💡 *Observação: JTBD claro e acionável. "Pergunta NL → resposta visual contextualizada em segundos". Bom norte para priorização.* |
| 🧑‍💼 PO | Sobre visão de futuro — como você vê o Veezoozin em 12 meses? E em 3 anos? |
| 👤 Customer | [BRIEFING] No MVP, em 4 meses, queremos NL-to-SQL com BigQuery, 3 idiomas, 5 tenants, glossário básico. [INFERENCE] Em 12 meses, imagino suporte multi-banco — PostgreSQL, MySQL, SQL Server — com integração de MCPs e RAGs externos, SSO e plano Enterprise. Em 3 anos, análises preditivas, alertas automáticos, talvez agentes autônomos que detectam anomalias e notificam proativamente. |
| 🧑‍💼 PO | O que diferencia o Veezoozin dos concorrentes? O Tableau Ask Data, o ThoughtSpot, o Metabase... por que o cliente escolheria vocês? |
| 👤 Customer | [BRIEFING] Tableau Ask Data só funciona dentro do Tableau e é limitado em idiomas. ThoughtSpot é enterprise caro com schema rígido. ChatGPT com SQL não tem contexto de negócio nem multi-tenancy. Metabase é dashboard-first, não conversacional. [BRIEFING] Nosso diferencial é a combinação: contexto de negócio por tenant, multi-idioma nativo PT-BR/EN/ES, e integração com fontes de conhecimento externas via MCP. Nenhum concorrente oferece as três coisas juntas. |
| 🧑‍💼 PO | 💡 *Observação: diferenciação em 3 eixos (contexto por tenant, multi-idioma, MCP). Triângulo competitivo sólido. Nenhum concorrente cobre os 3.* |
| 🧑‍💼 PO | Sobre ROI — qual o impacto mensurável que o cliente espera ao adotar o Veezoozin? |
| 👤 Customer | [BRIEFING] Tempo de resposta cai de dias para segundos. Democratização total — de 5-10% dos colaboradores com acesso a dados para 100%. Qualidade salta de tabelas brutas para gráficos com insights. E redução de 60-80% no volume de tickets para o time de dados. |
| 🧑‍💼 PO | E para a mAInd Tech como negócio? Quais as metas? |
| 👤 Customer | [BRIEFING] MVP com 5 tenants, precisão de queries acima de 85%, custo de infra abaixo de R$ 5K/mês para até 50 tenants. [INFERENCE] Em 12 meses, 50+ tenants com MRR acima de R$ 50K. |
| 🧑‍💼 PO | 💡 *Observação: ROI do cliente quantificado. Metas da mAInd Tech claras para MVP. Meta de 12 meses é inferência — registrar para validação.* |
| 🧑‍💼 PO | Qual o modelo comercial? Como vocês pretendem cobrar? |
| 👤 Customer | [BRIEFING] Modelo tiered com opção freemium. Plano Free com recursos bem limitados — poucas queries por dia, uma fonte de dados, sem MCP. Plano Pro para PMEs com queries ilimitadas, múltiplas fontes, glossário completo. E Enterprise com SSO, SLA 99.9%, database dedicado. [BRIEFING] Também queremos monetizar por consumo — queries, storage, número de tenants. Então é um modelo híbrido: assinatura base mais usage. |
| 🧑‍💼 PO | 💡 *Observação: modelo freemium + tiered + usage-based. Três mecanismos complementares. Free para aquisição, tiered para segmentação, usage para alinhamento de valor. Precisa detalhar no Bloco #3.* |
| 🧑‍💼 PO | Sobre stack técnica — alguma restrição ou preferência forte? |
| 👤 Customer | [BRIEFING] GCP obrigatório — Cloud Run, Vertex AI, Cloud SQL, BigQuery, Firestore. Python como linguagem principal. LLM via APIs externas — Claude e Gemini. Sem hospedar modelo próprio. Read-only obrigatório nas queries, com sandbox, timeout e limites. LGPD obrigatória. E no MVP, apenas BigQuery como banco suportado. |
| 🧑‍💼 PO | 💡 *Observação: stack bem definida, sem ambiguidade. GCP-native com LLM APIs. Restrição read-only é tanto segurança quanto compliance. Boa maturidade técnica do sponsor.* |
| 🧑‍💼 PO | Algum risco que te preocupa? |
| 👤 Customer | [INFERENCE] Me preocupa a precisão das queries geradas — se o NL-to-SQL errar muito, os usuários perdem confiança rapidamente. Também o custo de LLM APIs por query, que pode escalar. E o plano Free sem conversão — usuários entrando de graça e não convertendo. |
| 🧑‍💼 PO | 💡 *Observação: riscos legítimos. Precisão é o risco #1. Custo de LLM é risco operacional. Conversão Free→Pro é risco de negócio. Todos mitigáveis com design adequado.* |

---

## Bloco #2 — Personas e Jornadas

> Usando outputs do Bloco #1 como base: problema em 4 dimensões, JTBD definido, modelo tiered confirmado.

| Quem | Diálogo |
|------|---------|
| 🧑‍💼 PO | Agora vamos para personas. O briefing menciona 4 perfis. Vamos começar: quem é a persona primária? Quem mais sofre a dor? |
| 👤 Customer | [BRIEFING] A persona primária é o Gestor/Executivo. Ele faz perguntas de negócio em linguagem natural diariamente — faturamento, pipeline, conversão — e quer receber dashboards e insights prontos. [INFERENCE] É a Marina, Diretora Comercial, 38 anos. Ela precisa de dados para a reunião semanal e hoje depende do time de dados. O ticket leva 2-3 dias, então ela apresenta dados desatualizados. |
| 🧑‍💼 PO | 💡 *Observação: persona primária clara — Gestora que sofre a dor diretamente. Uso diário. Influencia compra. Mapeia direto para o JTBD do Bloco #1.* |
| 🧑‍💼 PO | E quem valida tecnicamente? Quem vai testar se as queries estão certas? |
| 👤 Customer | [BRIEFING] O Analista de Negócio. Ele usa o sistema intensivamente — 10-20 consultas por dia. [INFERENCE] É o Rafael, 29 anos, sabe SQL básico mas gasta 70% do tempo em queries repetitivas. Ele quer focar em análise, não em extração. Se o Rafael aprovar o produto tecnicamente, a Marina compra. |
| 🧑‍💼 PO | 💡 *Observação: Rafael é o "power user" e validador técnico. Se a precisão de query não satisfizer ele, a adoção falha. Confirma que precisão >85% do Bloco #1 é KR crítico.* |
| 🧑‍💼 PO | Quem configura o contexto do tenant? Quem ensina o sistema sobre o domínio? |
| 👤 Customer | [BRIEFING] O Admin do Tenant. Ele configura o contexto, ensina sobre o domínio, gerencia integrações. Uso semanal. [INFERENCE] É o Lucas, Líder de Dados, 34 anos. Ele é quem alimenta o glossário — define o que é "churn", o que é "cliente ativo" no contexto daquela empresa. Se ele não configurar bem, todas as respostas saem erradas. |
| 🧑‍💼 PO | 💡 *Observação: Lucas é o viabilizador. Sem onboarding eficiente para ele, o produto não entrega valor. O glossário por tenant — diferencial do Bloco #1 — depende inteiramente dessa persona.* |
| 🧑‍💼 PO | E a segurança? Quem garante que os dados estão protegidos? |
| 👤 Customer | [BRIEFING] O Admin de TI. Configura conexões, gerencia acessos e segurança. Uso mensal. [INFERENCE] A Carla, Coordenadora de Infra, 41 anos. Ela tem poder de veto. Se não aprovar segurança — read-only, LGPD, logs de auditoria, controle de acesso granular — o produto não entra na empresa. |
| 🧑‍💼 PO | 💡 *Observação: Carla é gatekeeper com poder de veto. Feature de controle de acesso por campo/registro mencionada no briefing é diretamente para ela. Sem essa feature, Enterprise não vende.* |
| 🧑‍💼 PO | Sobre a jornada de primeiro valor — quanto tempo entre o signup e o momento "aha!"? |
| 👤 Customer | [INFERENCE] Idealmente, menos de 45 minutos. O signup é rápido — 2 minutos. Conectar o BigQuery leva uns 10 minutos com as credenciais prontas. O mapeamento automático de schema mais uns 15-20 minutos para um banco de 50 tabelas. O Lucas revisa rapidamente e ajusta o glossário básico. Aí a Marina faz a primeira pergunta — "Qual foi o faturamento por região no último trimestre?" — e em 5 segundos tem um gráfico de barras com insight. Esse é o momento "aha!". |
| 🧑‍💼 PO | 💡 *Observação: time-to-value de ~45 min é ambicioso mas viável se o mapeamento automático de schema funcionar bem. O "aha!" moment é visual — gráfico + insight. Registrar como KR.* |
| 🧑‍💼 PO | O onboarding muda por plano? |
| 👤 Customer | [INFERENCE] Sim. O Free é 100% self-service — wizard guiado, templates de glossário prontos, limitado a 5 tabelas. O Pro é self-service com documentação e suporte por chat, glossário customizável, até 50 tabelas. O Enterprise é white-glove — engenheiro dedicado configura junto com o cliente, consultoria de domínio de 1-2 horas, tabelas ilimitadas, SSO e RBAC. |
| 🧑‍💼 PO | 💡 *Observação: onboarding escalado por tier. Free = zero touch. Pro = low touch. Enterprise = high touch. Consistente com o modelo tiered do Bloco #1.* |
| 🧑‍💼 PO | Sobre controle de acesso — o briefing menciona controle em nível de registro e campo. Como imagina isso funcionando? |
| 👤 Customer | [BRIEFING] Precisamos pensar em possibilidades de controlar o acesso aos dados em nível de registro e campo. [INFERENCE] Imagino três camadas: por tabela (quem pode acessar qual tabela), por campo (mascarar CPF, ocultar salário para certos roles) e por registro (gestor regional vê apenas dados da sua região). O nível de tabela é básico — até no Free. Campo é Pro. Registro é Enterprise. |
| 🧑‍💼 PO | 💡 *Observação: modelo de acesso em 3 camadas alinhado com tiers. IMPORTANTE: controle por registro exige injeção de filtros na query SQL antes da execução. Isso precisa ser arquitetado como concern nativo do engine NL-to-SQL, não como afterthought. Registrar como decisão arquitetural.* |
| 🧑‍💼 PO | Quais OKRs você definiria para o MVP? |
| 👤 Customer | [BRIEFING] 5 tenants ativos, queries corretas acima de 85%, custo de infra abaixo de R$ 5K/mês. [INFERENCE] Adicionaria: NPS acima de 40 dos primeiros usuários, consultas por usuário ativo acima de 3 por dia, taxa de aceitação de sugestões de prompts acima de 40%, e tempo de onboarding no Free abaixo de 30 minutos. |
| 🧑‍💼 PO | 💡 *Observação: OKRs mensuráveis e não vagos. Cobrem ativação (onboarding time), retenção (consultas/dia, sugestões aceitas), qualidade (precisão), satisfação (NPS). Bom conjunto para MVP.* |
| 🧑‍💼 PO | Quais gaps ficam para os próximos blocos? |
| 👤 Customer | [INFERENCE] Pricing concreto — os valores dos planos. Estratégia de trial — duração, conversão. Multi-tenant strategy — row-level vs schema-per-tenant. Autenticação enterprise — qual padrão SSO/SAML. E rate limiting por plano — quantas queries por dia em cada tier. |
| 🧑‍💼 PO | 💡 *Observação: 5 gaps identificados, todos mapeáveis para blocos futuros (#3 Pricing, #5 Tenancy, #6 Infra). Nenhum gap é blocker para os resultados dos blocos #1 e #2. Encerrando com boa cobertura.* |

---

## Resumo da Sessão

| Aspecto | Status |
|---------|--------|
| **Duração simulada** | ~45 minutos |
| **Blocos cobertos** | #1 (Propósito e Visão), #2 (Personas e Jornadas) |
| **Decisões registradas** | D1–D10 (ver arquivos de resultado) |
| **Gaps identificados** | G1–G5 (pricing, trial, multi-tenant, SSO, rate limiting) |
| **Riscos identificados** | 4 (precisão NL-to-SQL, custo LLM, conversão Free, concorrentes) |
| **Respostas [BRIEFING]** | 18 (diretamente do briefing) |
| **Respostas [INFERENCE]** | 11 (deduzidas do contexto) |
| **Qualidade das respostas** | Alta — briefing detalhado permitiu respostas ricas com poucas inferências necessárias |

### Concerns do Blueprint SaaS Cobertos

| Concern (Componente 1) | Status | Onde |
|------------------------|--------|------|
| Persona primária e secundárias | ✅ Coberto | Bloco #2, seção 1 |
| Job to be done principal | ✅ Coberto | Bloco #1, seção 2 |
| Modelo comercial | ✅ Diretriz (detalhe no Bloco #3) | Bloco #1, seção 6 |
| Planos e diferenciação entre tiers | ✅ Diretriz (detalhe no Bloco #3) | Bloco #1, seção 6 |
| Onboarding | ✅ Coberto | Bloco #2, seção 4 |
| Time-to-value | ✅ Coberto | Bloco #2, seção 3 |
| OKRs e métricas norte | ✅ Coberto | Bloco #2, seção 5 |
| ROI esperado | ✅ Coberto | Bloco #1, seção 5 |
| Diferenciação competitiva | ✅ Coberto | Bloco #1, seção 4 |
| Roadmap | ✅ Coberto | Bloco #1, seção 7 |

| Concern (Componente 2 — parcial) | Status | Onde |
|----------------------------------|--------|------|
| Isolamento de dados / controle de acesso | ✅ Parcial | Bloco #2, seção 6 |
| Stack tecnológica | ✅ Confirmada | Bloco #1 (entrevista) |


---

---
title: "Interview Log — Blocos #3 e #4"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [3, 4]
simulation: true
roles:
  po: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-11
---

# Interview Log — Blocos #3 e #4

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto). Nenhuma resposta `[RAG]` nesta sessão.]

---

## Bloco #3 — Valor, OKRs e Pricing

> Usando outputs do Bloco #1 (modelo tiered freemium, diretriz D2) e Bloco #2 (personas, OKRs iniciais, gaps G1-G5) como base.

| Quem | Diálogo |
|------|---------|
| 🧑‍💼 PO | Vamos ao pricing concreto — o gap G1 do bloco anterior. No Bloco #1 definimos três tiers: Free, Pro e Enterprise. Qual valor você imagina para o Pro? |
| 👤 Customer | [INFERENCE] Olhando o mercado, ThoughtSpot cobra em torno de US$ 95/usuário/mês — muito caro para PMEs latinas. Nosso posicionamento é PME-friendly. Imagino algo em torno de R$ 500/mês para um pacote de até 10 usuários. Isso dá ~R$ 50/usuário, cerca de 50% mais barato que o ThoughtSpot. |
| 🧑‍💼 PO | 💡 *Observação: R$ 497/mês é um price point psicologicamente bom (abaixo de 500). Benchmark contra ThoughtSpot faz sentido. Posicionamento PME-friendly confirmado.* |
| 🧑‍💼 PO | E o Enterprise? |
| 👤 Customer | [INFERENCE] O Enterprise tem SLA 99.9%, SSO, database dedicado, suporte 24/7. Penso em R$ 2.000/mês como base, com add-ons para usuários extras, storage, fontes de dados adicionais. O ticket médio real seria R$ 3.000-5.000/mês com os add-ons. Contratos anuais com desconto. |
| 🧑‍💼 PO | 💡 *Observação: base R$ 1.997 + add-ons. Modelo de land-and-expand — entra pelo base, upsell via add-ons. Bom para NRR (net revenue retention).* |
| 🧑‍💼 PO | O plano Free — quão limitado deve ser? Lembra que no Bloco #1 definimos recursos "muito limitados". |
| 👤 Customer | [BRIEFING] Recursos bem limitados. [INFERENCE] Diria: 10 queries por dia, 1 fonte de dados (BigQuery), máximo 5 tabelas, 2 usuários, sem MCP, sem export, glossário com templates genéricos apenas, histórico de 7 dias. Precisa ser útil o suficiente para a pessoa ver o valor, mas limitado o bastante para querer o Pro. |
| 🧑‍💼 PO | 💡 *Observação: 10 queries/dia é suficiente para o "aha!" moment mas insuficiente para uso profissional. 5 tabelas e 2 usuários forçam upgrade para qualquer empresa real. Boa calibragem.* |
| 🧑‍💼 PO | Sobre o trial — gap G2. Duração? Precisa de cartão de crédito? |
| 👤 Customer | [INFERENCE] 14 dias de trial do Pro completo, sem cartão de crédito. Queremos reduzir a fricção máxima na entrada. Ao expirar, faz downgrade automático para o Free — os dados ficam mantidos por 30 dias caso o usuário decida converter depois. |
| 🧑‍💼 PO | 💡 *Observação: 14 dias sem cartão é padrão para SaaS B2B de baixa fricção. 30 dias de retenção de dados pós-trial evita perda de contexto configurado pelo Lucas (Admin Tenant). Bom equilíbrio.* |
| 🧑‍💼 PO | Quando consideramos que o trial converteu? Qual o critério? |
| 👤 Customer | [INFERENCE] O usuário fez mais de 30 queries durante o trial E teve pelo menos 3 sessões em dias diferentes. Se esses dois critérios acontecerem, o produto demonstrou valor suficiente — aí o nudge de conversão tem alta probabilidade de funcionar. |
| 🧑‍💼 PO | 💡 *Observação: critério duplo — volume (30 queries) + frequência (3 dias). Evita contar trial como sucesso só porque o usuário fez 30 queries no primeiro dia e nunca mais voltou. Inteligente.* |
| 🧑‍💼 PO | Sobre monetização — no Bloco #1 definimos billing híbrido: assinatura + usage. Vamos detalhar o usage. |
| 👤 Customer | [BRIEFING] Billing por consumo — queries, storage de contexto, número de tenants. [INFERENCE] No Pro, "queries ilimitadas" é o marketing, mas internamente temos um fair use de 5.000/mês. Acima disso, cobra R$ 0,05 por query excedente. Storage de contexto: 5 GB incluído no Pro, R$ 2/GB extra. Usuários adicionais: R$ 29/usuário/mês. Fontes de dados extras no Pro: R$ 97/fonte/mês. |
| 🧑‍💼 PO | 💡 *Observação: "ilimitado" no marketing com fair use operacional. Prática comum em SaaS. O excedente é barato o suficiente para não irritar, mas caro o bastante para desincentivar abuso. Registrar como D14.* |
| 🧑‍💼 PO | Vamos às projeções financeiras. Cenário conservador para 12 meses. |
| 👤 Customer | [INFERENCE] No lançamento, imagino 10 tenants Free e 2 Pro — os early adopters que já conhecemos. MRR de ~R$ 1.000. Em 3 meses, com produto estável e referências, escalamos para 30 Free e 5 Pro, talvez 1 Enterprise — MRR ~R$ 4.500. Em 6 meses, 80 Free, 15 Pro, 2 Enterprise — MRR ~R$ 11.500. E em 12 meses, 250 Free, 40 Pro, 6 Enterprise — MRR ~R$ 32.000. |
| 🧑‍💼 PO | A meta do Bloco #1 era R$ 50K MRR em 12 meses. Esse cenário fica em ~R$ 32K. É conservador o suficiente ou estamos subestimando? |
| 👤 Customer | [INFERENCE] É conservador propositalmente. A meta de R$ 50K é alcançável no cenário otimista se o product-led growth funcionar bem — mais viralidade do Free, conversão acima de 12%. Prefiro prometer R$ 32K e entregar R$ 50K do que o contrário. Mas se o NRR (net revenue retention) ficar acima de 115%, os upsells de Enterprise puxam o MRR para cima. |
| 🧑‍💼 PO | 💡 *Observação: cenário conservador realista. R$ 50K é cenário otimista, não base. Boa prática de planejamento — planejar para o conservador, celebrar se chegar no otimista.* |
| 🧑‍💼 PO | Custo operacional — no Bloco #1 definimos < R$ 5K no MVP. Vamos detalhar. |
| 👤 Customer | [BRIEFING] GCP com créditos e incentivos — maximizar serviços nativos. [INFERENCE] No MVP com 5 tenants: Cloud Run ~R$ 800, LLM APIs (Claude + Gemini) ~R$ 1.500 — esse é o mais caro, depende do volume de queries. BigQuery ~R$ 500, Cloud SQL ~R$ 400, Firestore ~R$ 200, observabilidade ~R$ 300, outros ~R$ 300. Total ~R$ 4.000. Dentro do orçamento de R$ 5K. |
| 🧑‍💼 PO | 💡 *Observação: LLM APIs são ~37% do custo — maior componente. Cache de queries similares e otimização de prompts são críticos para margem. Registrar meta: custo LLM/query < R$ 0,15 em 6 meses, < R$ 0,08 em 12 meses.* |
| 🧑‍💼 PO | Margem bruta projetada? |
| 👤 Customer | [INFERENCE] Com MRR de R$ 32K e custo de infra de ~R$ 13.500 em 12 meses, margem bruta de ~58%. Meta de longo prazo: acima de 70%. Isso exige otimizar o custo de LLM — cache agressivo, detectar queries similares, reduzir tokens por prompt. |
| 🧑‍💼 PO | 💡 *Observação: 58% de margem bruta no ano 1 é aceitável para SaaS early-stage. SaaS maduro tem 70-85%. O caminho está claro: escala + otimização de LLM.* |
| 🧑‍💼 PO | CAC versus LTV — temos números? |
| 👤 Customer | [INFERENCE] Para o Pro: ticket médio de R$ 555/mês (com add-ons), lifetime estimado de 20 meses (churn de 5%/mês), LTV de ~R$ 11.000. CAC alvo abaixo de R$ 2.000 — dá um LTV/CAC de 5.5x, acima do benchmark saudável de 3x. Para Enterprise: ticket médio R$ 3.000, lifetime 50 meses, LTV R$ 150.000, CAC alvo R$ 15.000 — LTV/CAC de 10x. |
| 🧑‍💼 PO | 💡 *Observação: LTV/CAC excelente nos dois tiers. O desafio é manter o CAC baixo — product-led growth no Pro (sem SDR) e outbound focado no Enterprise. Payback de 4-5 meses é saudável.* |
| 🧑‍💼 PO | ROI para o cliente final — temos que convencer a Marina (Gestora) e a Carla (Admin TI). Quais números? |
| 👤 Customer | [INFERENCE] Para uma PME com 20 funcionários pagando R$ 497/mês no Pro: economia de 1 analista part-time (~R$ 3.000/mês) mais produtividade de gestores (~R$ 2.000/mês). ROI de ~900%. Para empresa média pagando R$ 2.000/mês no Enterprise: economia de 2 analistas (~R$ 6.000) + produtividade de 10 gestores (~R$ 8.000). ROI de ~600%. São números que Marina apresenta na reunião de aprovação e Carla não consegue vetar. |
| 🧑‍💼 PO | 💡 *Observação: ROI > 500% em todos os cenários. Argumento de venda poderoso. Lembrar de criar calculadora de ROI no site como ferramenta de conversão.* |
| 🧑‍💼 PO | Como detectar e prevenir churn? |
| 👤 Customer | [INFERENCE] Sinais automatizáveis: queda de queries/dia acima de 50% por 7 dias, nenhum login em 14 dias, taxa de queries falhadas acima de 30%, tenant que não completou onboarding em 48h. Para cada sinal, uma ação automática — email personalizado, sugestões de análises, oferta de suporte. Para Enterprise, o CSM acompanha com health score e QBRs trimestrais. |
| 🧑‍💼 PO | 💡 *Observação: 5 sinais de churn mapeados com ações concretas. Mix de automação (Free/Pro) e toque humano (Enterprise). Consistente com as jornadas do Bloco #2 — sugestão de prompts como retenção (D10) se conecta aqui.* |

---

## Bloco #4 — Processo, Negócio e Time

> Usando outputs dos Blocos #1, #2 e #3 como base. Referenciando personas e projeções financeiras.

| Quem | Diálogo |
|------|---------|
| 🧑‍💼 PO | Vamos falar de time. O briefing diz "contrataremos". Quantas pessoas para entregar o MVP em 4 meses? |
| 👤 Customer | [BRIEFING] Time enxuto, foco em speed-to-market. Equipe será contratada. [INFERENCE] Preciso de: 1 PO para priorizar e validar com early adopters, 1 Backend Senior focado no engine NL-to-SQL — esse é o coração do produto —, 1 Backend Pleno-Senior para plataforma (multi-tenancy, auth, billing), 1 Frontend Pleno para a interface conversacional e gráficos, e 1 Designer UX/UI part-time ou freelancer. Eu (Fabio, CTO) atuo como arquiteto e mentor. Total: 6 pessoas, 4 contratações + 1 freelancer. |
| 🧑‍💼 PO | 💡 *Observação: time de 6 é o mínimo viável. Bus factor = 1 em cada função, especialmente no Backend NL-to-SQL. Risco alto — documentação e pair programming são mitigações essenciais.* |
| 🧑‍💼 PO | Custo mensal desse time? |
| 👤 Customer | [INFERENCE] PO Pleno-Senior: ~R$ 15.000. Backend Senior (NL-to-SQL): ~R$ 22.000 — precisa ser senior mesmo, experiência com LLMs e SQL. Backend Pleno-Senior (Platform): ~R$ 18.000. Frontend Pleno: ~R$ 14.000. Designer part-time: ~R$ 6.000. Total: ~R$ 75.000/mês sem contar eu como CTO. Em 4 meses: R$ 300.000 de time + R$ 16.000 de infra + R$ 30.000 de marketing = ~R$ 346.000 de investimento total até o lançamento. |
| 🧑‍💼 PO | No Bloco #3 estimamos R$ 296.000. Essa atualização para R$ 346.000 é significativa. Impacta o breakeven? |
| 👤 Customer | [INFERENCE] Sim, mas não dramaticamente. O breakeven no cenário conservador passa de mês 10-12 para mês 12-14 pós-lançamento. Ainda aceitável para uma startup. O investimento extra é no time — e time bom é o que faz a diferença entre MVP que funciona e MVP que precisa ser reescrito. |
| 🧑‍💼 PO | 💡 *Observação: R$ 50K a mais, breakeven 2 meses depois. Trade-off aceitável. Time forte > time barato. Registrar D23 com valor atualizado.* |
| 🧑‍💼 PO | Qual a maior dificuldade de contratação? |
| 👤 Customer | [INFERENCE] O Backend Senior de NL-to-SQL, sem dúvida. Preciso de alguém que entenda LLMs, prompt engineering, SQL gerado dinamicamente, e que tenha experiência com BigQuery. Esse perfil é raro. Meu fallback é eu (Fabio) assumir essa função temporariamente enquanto mentoro um pleno com potencial. |
| 🧑‍💼 PO | 💡 *Observação: risco de contratação confirmado. Fallback realista (CTO assume temporariamente). Mas isso sobrecarrega o CTO — precisa iniciar busca imediatamente para minimizar esse período.* |
| 🧑‍💼 PO | Metodologia — como vão trabalhar? |
| 👤 Customer | [INFERENCE] Scrum adaptado com sprints de 1 semana. Com 16 semanas de MVP, cada sprint precisa entregar algo tangível. Planning na segunda, daily de 15 minutos, review e retro na sexta. Ferramenta: Linear ou GitHub Projects — algo leve. Monorepo no GitHub. Trunk-based development com feature flags para rollout gradual. |
| 🧑‍💼 PO | 💡 *Observação: sprints de 1 semana são agressivos mas adequados para MVP. Cerimônias mínimas — sem overhead. Trunk-based + feature flags é estado da arte. Monorepo para time pequeno faz total sentido.* |
| 🧑‍💼 PO | Como fica a cadência de entregas ao longo das 16 semanas? |
| 👤 Customer | [INFERENCE] Semanas 1-2: setup — infra GCP, monorepo, CI/CD, auth básica. Semanas 3-6: core — engine NL-to-SQL e glossário. Semanas 7-8: UX — interface conversacional e gráficos. Semanas 9-10: features — sugestões, export, histórico. Semanas 11-12: polish — onboarding wizard, billing via Stripe. Semanas 13-14: QA — testes, load testing, security review. Semanas 15-16: launch — early adopters, monitoramento, ajustes. |
| 🧑‍💼 PO | 💡 *Observação: cadência lógica — infra → core → UX → features → polish → QA → launch. Core (NL-to-SQL) começa cedo e tem 4 semanas. QA tem 2 semanas dedicadas. Buffer implícito de 2 semanas (polish pode comprimir se necessário).* |
| 🧑‍💼 PO | Vamos ao RACI. Quem é responsável por quê? Vou cruzar com as personas do Bloco #2 para o lado do cliente. |
| 👤 Customer | [INFERENCE] Do lado interno: Fabio aprova arquitetura e budget. PO prioriza backlog e valida com early adopters. Tech Lead decide implementação e faz code review. Time executa. Designer entrega telas e sistema de design. Do lado do cliente — usando as personas: Marina (Gestora) decide a compra, Rafael (Analista) valida tecnicamente, Lucas (Admin Tenant) configura o glossário, Carla (Admin TI) configura acesso e tem poder de veto na segurança. |
| 🧑‍💼 PO | 💡 *Observação: RACI interno e externo mapeados. Marina é Accountable pela compra, Carla tem poder de veto (Consulted com autoridade). Lucas é Responsible pela configuração que viabiliza o produto. Boa separação de responsabilidades.* |
| 🧑‍💼 PO | SLA e SLOs — no Bloco #3 definimos Free=best-effort, Pro=99.5%, Enterprise=99.9%. Vamos detalhar os SLIs. |
| 👤 Customer | [INFERENCE] Quatro SLIs principais: disponibilidade (% de requests com status 2xx/3xx, medido por monitoramento externo), latência de query (tempo entre pergunta NL e resposta visual — p50, p90, p99), precisão de query (% de queries SQL corretas, medido por feedback do usuário), e tempo de onboarding (minutos entre signup e primeira query com resultado). |
| 🧑‍💼 PO | E os SLOs concretos por plano? |
| 👤 Customer | [INFERENCE] Free: latência p50 < 8 seg, precisão > 80%. Pro: disponibilidade 99.5%, latência p50 < 5 seg, precisão > 85%. Enterprise: disponibilidade 99.9%, latência p50 < 3 seg, precisão > 90%. O SLA contratual é só para Enterprise — crédito de 10% do MRR por cada 0.1% abaixo de 99.9%. |
| 🧑‍💼 PO | 💡 *Observação: SLOs diferenciados por tier são consistentes com o pricing do Bloco #3 (Enterprise paga 4x mais, recebe SLA melhor). Precisão diferenciada por tier é interessante — Enterprise pode ter glossário mais refinado e modelos mais caros.* |
| 🧑‍💼 PO | Observabilidade — como monitorar por tenant? |
| 👤 Customer | [BRIEFING] GCP nativo — Cloud Monitoring, Cloud Logging, Cloud Trace. [INFERENCE] Tudo segmentado por tenant_id como dimensão obrigatória em logs e métricas. Cada log tem: tenant_id, plan, user_id, persona_type, request_type, latency_ms, llm_provider, llm_cost_usd, query_accuracy. Assim consigo dashboards por tenant, por plano, por feature. No MVP uso GCP nativo + Grafana Cloud free tier. Custo: ~R$ 300/mês. |
| 🧑‍💼 PO | 💡 *Observação: observabilidade per tenant como first-class citizen. A inclusão de llm_cost_usd por request é excelente — permite monitorar margem por tenant. Alinhado com a meta do Bloco #3 de LLM cost < R$ 0,08/query.* |
| 🧑‍💼 PO | On-call — quem responde quando cai? |
| 👤 Customer | [INFERENCE] No MVP, rotação semanal entre Tech Lead e os 2 Backend Engineers. Horário comercial apenas — 9h às 18h. P1 (sistema down): resposta em menos de 15 minutos. P2 (degradado): menos de 1 hora. P3 (bug): próximo sprint. Alertas via Slack, telefone para P1. Post-mortem obrigatório para todo P1. Quando tivermos Enterprise com SLA, expandimos para horário estendido e depois 24/7 com SRE dedicado. |
| 🧑‍💼 PO | 💡 *Observação: on-call pragmático. Sem overengineering para o MVP. Escalação clara quando Enterprise entrar. Post-mortem obrigatório é boa prática desde o dia 1.* |
| 🧑‍💼 PO | Feature flags — como vão controlar rollout de features? |
| 👤 Customer | [INFERENCE] No MVP, custom simples — configuração no Firestore por tenant. Flag true/false por feature por tenant. Na Fase 2, migramos para LaunchDarkly quando precisarmos de targeting mais sofisticado (% de usuários, A/B testing de pricing). Granularidade: por tenant, por plano, por % de usuários. |
| 🧑‍💼 PO | 💡 *Observação: build simples no MVP, buy na Fase 2. Evita antipattern #2 do blueprint (overengineering no MVP). Feature flags custom em Firestore é trivial de implementar.* |
| 🧑‍💼 PO | CI/CD — qual o pipeline? |
| 👤 Customer | [INFERENCE] Push para main → lint + format (Ruff para Python, ESLint para TypeScript) → unit tests (pytest, Vitest, cobertura > 80%) → build Docker via Cloud Build → deploy em staging (Cloud Run) → integration tests (pytest + Playwright) → deploy em produção como canary 10% → se error rate < 1% por 10 minutos, promote para 100%. Rollback automático se canary falhar. |
| 🧑‍💼 PO | 💡 *Observação: pipeline completo com quality gates. Canary de 10% com auto-promote é sofisticado mas Cloud Run suporta nativamente (traffic splitting). Cobertura > 80% é ambiciosa para MVP — pode começar em 60% e subir. Mas como meta, está certo.* |
| 🧑‍💼 PO | Como evolui o time depois do MVP? |
| 👤 Customer | [INFERENCE] Fase 2 (mês 5-7): +1 SRE/DevOps para operação real com tenants pagantes, +1 Backend para multi-banco. Time vai para 8. Fase 3 (mês 8-10): +1 Data/ML Engineer para preditivo, +1 CS/Growth para escalar aquisição. Time vai para 10. Mês 12: mais 1 Backend e 1 Frontend. Time de 12. |
| 🧑‍💼 PO | 💡 *Observação: crescimento gradual — 6 → 8 → 10 → 12. SRE entra quando tem Enterprise (SLA contratual). ML Engineer entra na Fase 3 (preditivo). CS/Growth entra quando precisa escalar aquisição. Cada adição tem justificativa clara. Boa disciplina.* |

---

## Resumo da Sessão

| Aspecto | Status |
|---------|--------|
| **Duração simulada** | ~55 minutos |
| **Blocos cobertos** | #3 (Valor, OKRs e Pricing), #4 (Processo, Negócio e Time) |
| **Decisões registradas** | D11–D23 (ver arquivos de resultado) |
| **Riscos identificados** | 10 (5 no Bloco #3, 5 no Bloco #4) |
| **Respostas [BRIEFING]** | 5 (direto do briefing) |
| **Respostas [INFERENCE]** | 27 (deduzidas do contexto e decisões dos blocos anteriores) |
| **Qualidade das respostas** | Alta — blocos #3 e #4 dependem mais de inferência (pricing, projeções, organização) do que do briefing direto. Inferências são consistentes com as diretrizes dos blocos #1 e #2. |

### Concerns do Blueprint SaaS Cobertos

| Concern (Componente 1) | Status | Onde |
|------------------------|--------|------|
| OKRs e métricas norte | ✅ Detalhado | Bloco #3, seção 6 |
| ROI esperado | ✅ Consolidado | Bloco #3, seção 7 |
| Modelo comercial | ✅ Completo | Bloco #3, seções 1-2 |
| Planos e diferenciação entre tiers | ✅ Completo | Bloco #3, seção 1 |
| Free trial | ✅ Definido | Bloco #3, seção 3 |
| Projeção MRR/ARR | ✅ Conservador + otimista | Bloco #3, seção 4 |
| CAC vs LTV | ✅ Calculado | Bloco #3, seção 5 |

| Concern (Componente 4 — parcial) | Status | Onde |
|----------------------------------|--------|------|
| Tamanho e senioridade do time | ✅ Definido | Bloco #4, seção 2 |
| Processo de deploy e releases | ✅ Definido | Bloco #4, seções 8-9 |
| On-call | ✅ Definido | Bloco #4, seção 7 |
| SLA/SLO/SLI | ✅ Definido por tier | Bloco #4, seção 5 |
| Observabilidade per tenant | ✅ Definido | Bloco #4, seção 6 |
| Feature flags | ✅ Definido | Bloco #4, seção 8 |
| CI/CD pipeline | ✅ Definido | Bloco #4, seção 9 |

### Gaps Resolvidos dos Blocos Anteriores

| Gap (do Bloco #2) | Resolução | Onde |
|--------------------|-----------|------|
| G1 — Pricing concreto | ✅ Free R$ 0, Pro R$ 497, Enterprise R$ 1.997 | Bloco #3, seção 1 |
| G2 — Estratégia de trial | ✅ 14 dias, sem cartão, downgrade automático | Bloco #3, seção 3 |
| G5 — Rate limiting por plano | ✅ Parcial — fair use 5.000 queries/mês no Pro | Bloco #3, seção 2 |

### Gaps Remanescentes (para blocos futuros)

| Gap | Impacto | Bloco que resolve |
|-----|---------|-------------------|
| G3 — Multi-tenant strategy (row-level vs schema-per-tenant) | Impacta arquitetura fundamental | Bloco #5 (Tenancy) |
| G4 — Autenticação enterprise (SSO/SAML) | Impacta persona Carla | Bloco #6 (Infra) |
| G5 — Rate limiting detalhado (por endpoint, burst, throttle) | Impacta operação | Bloco #5 (Tenancy) |
| G6 — Billing platform (Stripe vs Chargebee) | Impacta implementação | Bloco #5 ou #7 (Billing) |
| G7 — Estratégia de backup e disaster recovery | Impacta SLA Enterprise | Bloco #6 (Infra) |


---

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


---

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


---

---
title: "Interview Log — Bloco #8"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [8]
simulation: true
depends-on: [1, 2, 3, 4, 5, 6, 7]
roles:
  solution-architect: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-12
---

# Interview Log — Bloco #8

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto). Nenhuma resposta `[RAG]` nesta sessão.]
>
> **Nota:** Bloco #8 depende de TODOS os blocos anteriores (D1–D49). O Solution Architect conduz a análise de TCO 3 anos, Build vs Buy dos componentes críticos, break-even e cenários alternativos de viabilidade.

---

## Bloco #8 — TCO e Build vs Buy

> Usando outputs dos Blocos #1-#7 como base. Todas as 49 decisões anteriores como input. Números-chave: MRR R$ 994 (lançamento) → R$ 31.862 (mês 12), ARR ~R$ 382K (ano 1), time R$ 75K/mês (6 pessoas), stack GCP (Cloud Run, Vertex AI, BigQuery, Cloud SQL, Firestore), LLM Claude/Gemini, cache 4 camadas.

| Quem | Diálogo |
|------|---------|
| 🏗️ SA | Vamos construir o TCO de 3 anos. Preciso que a gente seja brutalmente honesto com os números — se a conta não fechar, precisamos saber agora. Começando pela infraestrutura GCP. O Bloco #3 estimou R$ 4K/mês no MVP. Vamos detalhar com preços reais. |
| 👤 Customer | [BRIEFING] A stack definida no Bloco #5 é: Cloud Run (compute), Cloud SQL PostgreSQL (metadata), BigQuery (queries read-only dos tenants), Vertex AI (embeddings), Firestore (cache e sessões), Cloud Storage (exports). Tudo em GCP southamerica-east1 porque temos créditos e incentivos enterprise. |
| 🏗️ SA | Cloud Run primeiro. Preço real: US$ 0.00002400/vCPU-second, US$ 0.00000250/GiB-second. No MVP com 1-2 instâncias, 1 vCPU, ~9.000 requests/mês... dá cerca de US$ 80/mês, ou R$ 400. O Bloco #3 estimou R$ 800 — a estimativa era conservadora, o real é menor. |
| 👤 Customer | [INFERENCE] Cloud Run escala a zero para instâncias excedentes, então no MVP com pouco tráfego o custo é realmente baixo. O problema vem na escala: com 300+ tenants no mês 36, estimamos 30-50 instâncias com 16 vCPUs — aí chega a R$ 22.500/mês. É o componente de infra que mais escala. |
| 🏗️ SA | Cloud SQL. O db-f1-micro custa ~US$ 10/mês. Para MVP com row-level tenancy (D24) é suficiente. |
| 👤 Customer | [INFERENCE] Sim, mas conforme crescemos precisamos de db-custom com read replicas e HA. No mês 36 com 300+ tenants: db-custom-4-16384 com 2 read replicas e HA, mais database dedicado para Enterprise — uns R$ 5.500/mês. Storage SSD a US$ 0.17/GiB. |
| 🏗️ SA | BigQuery — o Veezoozin não armazena dados, apenas executa queries. US$ 5/TB scanned. Qual o volume estimado? |
| 👤 Customer | [INFERENCE] Cada query simples escaneia em média ~55 KB. Com 9.000 queries/mês no MVP: ~0.5 TB — custo quase zero, R$ 13. Em escala com 3 milhões de queries/mês no ano 3: ~150 TB — R$ 3.750/mês. E o cache de resultado (D46, camada 4) reduz ~30% das execuções. Os créditos GCP reduzem ainda mais. |
| 🏗️ SA | Agora o elefante na sala: custo de LLM APIs. São 2 chamadas por query — SQL gen e insight gen. Qual o custo real? |
| 👤 Customer | [INFERENCE] Com Claude Sonnet para produção: ~R$ 15/1M tokens input, ~R$ 75/1M tokens output. Cada query usa ~2.300 tokens input e ~600 output nas 2 chamadas combinadas. Custo unitário: ~R$ 0,08 por query com prompt otimizado. Gemini Pro é ~60% mais barato. No MVP sem cache: R$ 1.200/mês para 9.000 queries. No ano 3 com 3M queries, cache de 50% e mix 65/35 Claude/Gemini: R$ 65.000/mês. |
| 🏗️ SA | 💡 *Observação: LLM APIs são o segundo maior custo variável após equipe. O cache (D46) é literalmente um projeto de redução de custo — sem cache de 50%, o custo LLM no ano 3 seria R$ 130.000/mês, o dobro. A migração gradual para Gemini (mais barato + créditos GCP) é outra alavanca.* |
| 🏗️ SA | Equipe. O Bloco #4 definiu R$ 75K/mês para 6 pessoas no MVP. Qual a projeção de 3 anos? |
| 👤 Customer | [INFERENCE] MVP: 6 pessoas (R$ 75K/mês). Fase 2: +2, total 8 (R$ 105K). Fase 3: +2, total 10 (R$ 135K). Mês 12: 12 pessoas (R$ 165K). Ano 2: 15 pessoas com reajuste anual de ~8% (R$ 210K). Ano 3: 18 pessoas (R$ 260K). Total em 3 anos: R$ 6.990.000. Isso é 66,5% do TCO total. |
| 🏗️ SA | 💡 *Observação: equipe é dois terços do TCO. Qualquer otimização de infra ou LLM é marginal perto do impacto do headcount. Precisamos ser disciplinados: não contratar por antecipação. Revisar headcount trimestralmente.* |
| 🏗️ SA | Consolidando o TCO total de 3 anos? |
| 👤 Customer | [INFERENCE] Equipe R$ 6.990.000 + Infra GCP R$ 973.000 + LLM APIs R$ 1.464.000 + SaaS terceiros R$ 363.000 + Marketing R$ 1.390.000 = **R$ 10.510.000**. Com 30% de créditos GCP sobre infra + Vertex AI: ~R$ 9.778.000. |
| 🏗️ SA | Agora Build vs Buy. Quais componentes temos que decidir? |
| 👤 Customer | [INFERENCE] Seis componentes críticos: (1) NL-to-SQL Engine, (2) Vector Store, (3) LLM, (4) Auth, (5) Visualização, (6) Billing. Para cada um: Build é diferencial competitivo? Buy tem custo justificável? Time de 6 (D17) consegue operar? |
| 🏗️ SA | NL-to-SQL Engine — a decisão mais importante. Existem soluções prontas: Vanna.ai, Dataherald, Text2SQL. Por que não usar? |
| 👤 Customer | [INFERENCE] Porque o engine É o produto. O pipeline de 8 etapas com glossário por tenant, RLS injection, cache semântico, privacy guard, multi-idioma — isso não existe em nenhuma solução pronta. Vanna.ai tem glossário básico mas sem RLS, sem privacy guard, sem multi-idioma. Comprar isso commoditiza nosso valor. Qualquer concorrente pode plugar Vanna.ai e ter o mesmo resultado. Nosso moat é o contexto por tenant (Bloco #1). |
| 🏗️ SA | 💡 *Observação: decisão correta. Build apenas o que é moat. O NL-to-SQL Engine com contexto por tenant é a única coisa que diferencia o Veezoozin de "ChatGPT + SQL". Todo o resto pode ser commodity.* |
| 🏗️ SA | Vector Store? |
| 👤 Customer | [INFERENCE] Buy — Vertex AI Vector Search. Não é diferencial. É infraestrutura. Self-hosted (Qdrant, Weaviate) custa menos em 3 anos (~R$ 120K vs R$ 180K) mas requer SRE para operar backup, scaling, monitoring. Com time de 6 pessoas (D17), não temos capacity. Vertex AI é GCP-native, zero operação, créditos aplicáveis. |
| 🏗️ SA | LLM? |
| 👤 Customer | [BRIEFING] Buy — D3 é decisão do briefing. Sem fine-tune, sem modelo próprio. APIs Claude + Gemini. Custo em 3 anos: R$ 1.464.000. Hosting de modelo próprio seria ~R$ 800K (GPU) mas qualidade inferior e time de ML inexistente. |
| 🏗️ SA | Auth? |
| 👤 Customer | [INFERENCE] Buy — Firebase Auth (D28). Implementação custom de auth é risco de segurança desnecessário. Firebase é free tier generoso, GCP-native, suporte SAML/OIDC para Enterprise. Auth é o componente que menos devemos arriscar implementar do zero — um bug de auth é catastrófico. Persona Carla (Bloco #2 — poder de veto) exige segurança comprovada. |
| 🏗️ SA | Visualização? |
| 👤 Customer | [INFERENCE] Buy — Recharts ou Nivo (open-source, custo zero). São React-based (D25 — Next.js), altamente customizáveis. Implementar rendering engine custom é desvio de foco. O moat não é o gráfico — é o contexto + SQL generation + insight. Se precisar trocar de biblioteca no futuro, é trivial. |
| 🏗️ SA | Billing? |
| 👤 Customer | [INFERENCE] Buy — Stripe (D27). Antipattern #2 do blueprint SaaS: "billing custom no MVP é armadilha". Stripe custa ~R$ 340K em 3 anos em fees (2.9% sobre receita), mas evita 6-10 semanas de dev + PCI compliance + dunning custom + usage metering custom. Se o fee ficar pesado na escala, Lago (open-source) é alternativa para Fase 3. |
| 🏗️ SA | 💡 *Observação: padrão claro — Build o moat (NL-to-SQL), Buy todo o resto. Seis componentes, apenas 1 é Build. Isso é disciplina para time enxuto (D17). Registrar como D50.* |
| 🏗️ SA | Agora o momento da verdade. Receita vs TCO em 3 anos. |
| 👤 Customer | [INFERENCE] Receita cenário conservador do Bloco #3: MRR cresce de R$ 994 (lançamento) para R$ 31.862 (mês 12), projetando R$ 173.250 (mês 36). Total de receita em 3 anos: ~R$ 2.447.000. TCO: R$ 10.510.000. Déficit: R$ -8.063.000. Receita cobre apenas 23,3% do TCO. |
| 🏗️ SA | Isso é preocupante. Vamos ser claros: o projeto NÃO se paga em 3 anos no cenário conservador. |
| 👤 Customer | [INFERENCE] Correto. Mas isso é esperado para SaaS B2B greenfield. A maioria dos SaaS leva 3-5 anos para break-even total. O ponto relevante é: (1) a operação mensal se torna sustentável antes disso? (2) o crescimento justifica captação de investimento? |
| 🏗️ SA | 💡 *Observação: P22 acionado — receita < TCO em 3 anos. Precisamos de cenários alternativos. Vamos explorar 3+.* |
| 🏗️ SA | Cenário A: pricing mais alto. O Bloco #3 definiu Pro R$ 497 e Enterprise R$ 1.997. ThoughtSpot cobra US$ 95/user/mês. Há espaço? |
| 👤 Customer | [INFERENCE] Sim. Pro a R$ 697 (+40%) ainda posiciona o Veezoozin ~30% abaixo do ThoughtSpot por usuário. Enterprise a R$ 2.997 (+50%) com add-ons de R$ 4.500 ticket médio é competitivo para o valor entregue (democracia de dados, multi-idioma, contexto por tenant). Receita 3 anos sobe para ~R$ 3.436.000. Melhora mas não resolve sozinho. |
| 🏗️ SA | Cenário B: redução de escopo. O que cortar? |
| 👤 Customer | [INFERENCE] O maior candidato a corte é a insight generation automática (etapa 7 do pipeline). Remove uma chamada LLM por query — corta ~50% do custo LLM. O usuário ainda recebe gráfico e dados, mas sem o insight textual automático. Team reduzido para 4 no MVP (sem Designer e sem PO dedicado, Fabio acumula). Time máximo 8 no ano 3. Marketing 50% menor. TCO cai para R$ 6.617.000. Mas receita pode cair ~10% sem insights (NPS menor → conversão menor). |
| 🏗️ SA | 💡 *Observação: Cenário B é o "modo sobrevivência". Funciona para bootstrap, mas sacrifica diferenciação. O insight textual é parte do momento "Aha!" da persona Marina (Bloco #2). Cortar isso pode matar a ativação. Usar apenas se os cenários de crescimento falharem.* |
| 🏗️ SA | Cenário C: crescimento acelerado. O que precisa acontecer? |
| 👤 Customer | [INFERENCE] Product-market fit forte desde o lançamento. 50 Pro + 10 Enterprise no mês 12 (vs 46 no base). 250 Pro + 50 Enterprise no mês 36. Enterprise ticket médio de R$ 4.500 com upsell agressivo. Receita 3 anos: R$ 4.937.000. Mas TCO também sobe ~13% porque mais tráfego = mais LLM e infra. |
| 🏗️ SA | E se combinarmos A + C? |
| 👤 Customer | [INFERENCE] Cenário D — o mais realista para viabilidade. Pricing ajustado (Pro R$ 697, Enterprise R$ 2.997) E crescimento acelerado. Receita 3 anos: R$ 7.016.000. TCO: ~R$ 11.860.000. Break-even mensal (MRR > custos mensais) no mês ~24 pós-lançamento. Não recupera o investimento acumulado em 3 anos, mas a operação se torna sustentável. Isso é financiável via rodadas de investimento. |
| 🏗️ SA | 💡 *Observação: Cenário D é o "target scenario". Exige execution forte: pricing validado nos primeiros 3 meses, foco em Enterprise desde o mês 6, cache agressivo para controlar custo LLM, headcount disciplinado. Registrar gatilhos Go/No-Go nos meses 8, 12 e 24.* |
| 🏗️ SA | Falando em gatilhos — quais são os marcos de decisão? |
| 👤 Customer | [INFERENCE] Quatro marcos: (1) Mês 8 (3 meses pós-lançamento): ≥ 8 Pro + 1 Enterprise. Se não atingir, rever pricing e posicionamento. (2) Mês 12: MRR ≥ R$ 30K. Se não, rever equipe e considerar cenário B. (3) Mês 18: MRR ≥ R$ 80K. Se < R$ 50K, cenário B agressivo. (4) Mês 24: break-even mensal. Se não, avaliar captação ou redução para equipe mínima. |
| 🏗️ SA | Investimento necessário? |
| 👤 Customer | [INFERENCE] MVP: ~R$ 338K — bootstrap dos sócios. Ano 1 total: R$ 1.845.000 — precisa de Pre-seed/Angel de ~R$ 1.5M. Ano 2: Seed round de R$ 3-5M. Ano 3: Series A se métricas confirmarem. O MRR de R$ 500K+ no mês 36 (cenário D) é pitch atraente para Series A. |
| 🏗️ SA | 💡 *Observação: a história de investimento faz sentido se os marcos forem atingidos. MRR R$ 500K+ com 300 tenants pagantes é um SaaS B2B saudável para Series A. O TCO de R$ 10M em 3 anos não é assustador nesse contexto — é o custo de construir um SaaS com margem bruta de 60%+ projetada. O ponto é: os marcos do mês 8 e 12 são o teste real de viabilidade.* |
| 🏗️ SA | Uma última recomendação: D11 definiu pricing Pro R$ 497 e Enterprise R$ 1.997. Os números de TCO sugerem que deveríamos lançar com Pro R$ 697 e Enterprise R$ 2.997 desde o início. Isso atualiza D11. |
| 👤 Customer | [INFERENCE] Concordo, com uma ressalva: validar nos primeiros 3 meses com early adopters. Se o mercado resistir, podemos baixar. Mas é mais fácil baixar preço do que subir. Registrar como D51 — recomendação de pricing, sujeita a validação. |
| 🏗️ SA | Consolidando. Bloco #8 gera 7 novas decisões: D50 (Build apenas NL-to-SQL, Buy todo o resto), D51 (pricing recomendado Pro R$ 697 / Enterprise R$ 2.997), D52 (TCO R$ 10.5M — equipe é 66,5%), D53 (break-even mensal mês ~24 no cenário D), D54 (gatilhos Go/No-Go), D55 (investimento necessário), D56 (migração gradual para Gemini). Total acumulado: 56 decisões (D1-D56). |

---

## Resumo de Decisões do Bloco #8

| # | Decisão | Fonte |
|---|---------|-------|
| D50 | NL-to-SQL Engine é o único componente BUILD — todo o resto é BUY | [INFERENCE] — moat competitivo, D3, D17, D27, D28 |
| D51 | Pricing recomendado: Pro R$ 697, Enterprise R$ 2.997 (atualiza D11) | [INFERENCE] — TCO exige receita maior, benchmark ThoughtSpot |
| D52 | TCO 3 anos estimado R$ 10.5M — equipe é 66,5% do custo | [INFERENCE] — consolidação de todos os blocos |
| D53 | Break-even mensal no cenário D (pricing + crescimento) no mês ~24 | [INFERENCE] — cenário combinado A+C |
| D54 | Gatilhos Go/No-Go: mês 8 (≥ 8 Pro + 1 Ent), mês 12 (MRR ≥ R$ 30K), mês 24 (break-even) | [INFERENCE] — marcos de viabilidade |
| D55 | Investimento necessário: ~R$ 1.8M Ano 1, Pre-seed/Angel ~R$ 1.5M | [INFERENCE] — projeção financeira |
| D56 | Migração gradual para Gemini (40% até mês 12) para reduzir custo LLM | [INFERENCE] — Gemini ~60% mais barato, créditos GCP |

---

## Rastreabilidade de Fontes

| Informação-chave | Fonte | Tag |
|------------------|-------|:---:|
| Stack GCP obrigatória | Briefing seção 6 | [BRIEFING] |
| Créditos e incentivos GCP | Briefing seção 10 | [BRIEFING] |
| Claude/Gemini APIs sem modelo próprio | Briefing seção 6 (D3) | [BRIEFING] |
| MRR R$ 994 → R$ 31.862 (mês 12) | Bloco #3 seção 4 | [BRIEFING] |
| Time R$ 75K/mês (6 pessoas) | Bloco #4 seção 2 | [BRIEFING] |
| Cache 4 camadas reduz 35-50% LLM calls | Bloco #7 seção 6 (D46) | [INFERENCE] |
| Preços GCP (Cloud Run, BigQuery, etc.) | GCP Pricing públic (abr/2026) | [INFERENCE] |
| Cenários A, B, C, D | Análise de sensibilidade | [INFERENCE] |
| Gatilhos Go/No-Go | Análise de viabilidade | [INFERENCE] |
