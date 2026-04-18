---
title: "SaaS Público B2C — Blueprint"
description: "Produto digital para consumidor final. Multi-tenant, planos de assinatura, trial gratuito, billing self-service, onboarding automatizado e suporte em escala."
category: project-blueprint
type: saas-b2c
status: rascunho
created: 2026-04-13
---

# SaaS Público B2C

## Descrição

Produto digital para consumidor final. Multi-tenant, planos de assinatura, trial gratuito, billing self-service, onboarding automatizado e suporte em escala. O modelo B2C se diferencia do B2B pelo volume de usuários (milhares a milhões), pelo processo de aquisição self-service (sem vendedor humano), pela sensibilidade a preço (disposição a pagar é baixa — $5–50/mês), e pela necessidade de growth loops virais (referral, social sharing, freemium) para escalar aquisição sem custo proporcional de vendas.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo SaaS B2C é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — SaaS B2C Freemium / Product-Led

Produto com plano gratuito robusto que atrai volume e converte uma fração para plano pago. O growth engine é o produto em si — quanto mais o usuário usa, mais valor recebe e mais provável é a conversão. O gratuito não é trial com prazo — é plano permanente com limitações (volume, features, ou ambos). O foco é minimizar friction no sign-up, maximizar o "aha moment" nos primeiros minutos, e criar triggers naturais de upgrade (limites atingidos). Exemplos: Spotify (free com ads), Canva (free com limitações), Notion (free para individual), Duolingo (free com ads e vidas).

### V2 — SaaS B2C por Assinatura Pura

Produto pago desde o primeiro acesso — com trial gratuito de 7-30 dias como único incentivo. Sem plano gratuito permanente. O valor percebido precisa ser alto o suficiente para justificar o pagamento recorrente desde o início. Retenção é o KPI central — churn acima de 5% mensal inviabiliza o modelo. O foco é demonstrar valor no trial (onboarding que leva ao "aha moment" antes do trial expirar), e-mails de nurturing durante o trial, e paywall suave no fim do período. Exemplos: Netflix, Disney+, Headspace, Strava Premium.

### V3 — SaaS B2C com Marketplace / Plataforma

Produto que conecta consumidores a criadores, prestadores ou vendedores — o consumidor é um lado da plataforma. Monetização pode ser por assinatura do consumidor, comissão por transação, ou ambos. A complexidade está na dinâmica de dois lados (chicken-and-egg problem no lançamento), na governança de conteúdo/ofertas (moderação, qualidade), e nos fluxos de pagamento entre partes (split payment). O foco é balancear aquisição de ambos os lados e criar network effects. Exemplos: Airbnb, Uber, iFood, Udemy, Etsy.

### V4 — SaaS B2C de Conteúdo / Mídia

Produto cujo valor principal é conteúdo produzido ou curado — vídeos, artigos, cursos, podcasts, newsletters. Monetização por assinatura (paywall), ads, ou modelo híbrido (free com ads, premium sem ads). O foco é produção contínua de conteúdo, descoberta e recomendação personalizada, e experiência de consumo fluida (streaming, leitura, áudio). A retenção depende da qualidade e frequência do conteúdo — não do produto em si. Exemplos: Medium, Substack, Crunchyroll, Masterclass.

### V5 — SaaS B2C Mobile-First / App

Produto projetado primariamente para consumo mobile — o web é secundário ou inexistente. Distribuição via App Store e Google Play, com todas as implicações: review process, comissão de 15-30% nas compras in-app, restrições de pagamento (Apple/Google obrigam uso de seu sistema de billing para digital goods), e ciclo de atualização controlado pelo app store (usuários em versões diferentes simultaneamente). O foco é performance mobile, notificações push como canal de reengagement, e experiência nativa ou near-native. Exemplos: Calm, Noom, Flo, Photoroom.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend | Banco de Dados | Infra | Observações |
|---|---|---|---|---|---|
| V1 — Freemium | Next.js ou Remix | Node.js (NestJS) | PostgreSQL + Redis | Vercel + Railway ou Render | Auth via Clerk ou Supabase Auth. Billing Stripe. Feature flags para gating. |
| V2 — Assinatura Pura | Next.js | Node.js (NestJS) ou Rails | PostgreSQL + Redis | Vercel + AWS (RDS, SQS) | Foco em onboarding e trial. Analytics (Mixpanel/Amplitude) obrigatório. |
| V3 — Marketplace | Next.js | Node.js (NestJS) | PostgreSQL + Redis + ElasticSearch | AWS (ECS) | Stripe Connect para split payment. Algolia/Meilisearch para busca. Filas para matching. |
| V4 — Conteúdo/Mídia | Next.js | Node.js ou Go | PostgreSQL + Redis | AWS (CloudFront + S3 + ECS) | CDN para streaming/conteúdo. Recomendação via ML ou heurísticas. CMS headless para editorial. |
| V5 — Mobile-First | React Native ou Flutter | Node.js (NestJS) | PostgreSQL + Redis | AWS ou GCP | RevenueCat para in-app purchases. Push via Firebase/OneSignal. API versionada obrigatória. |

---

## Etapa 01 — Inception

- **Product-market fit como premissa**: Antes de construir um SaaS B2C, a hipótese de valor precisa estar validada — não necessariamente com produto, mas com evidência de demanda (lista de espera, landing page com conversão, protótipo testado com usuários reais, ou dados de mercado que demonstrem o problema). Construir um SaaS B2C sem evidência de demanda é a forma mais cara de descobrir que ninguém quer o que está sendo construído. O Inception deve avaliar honestamente se há sinais de product-market fit ou se o projeto está sendo movido por intuição do fundador sem validação.

- **Modelo de monetização e unit economics**: SaaS B2C opera com margens apertadas — o custo de aquisição (CAC) precisa ser recuperado pelo lifetime value (LTV) do usuário com margem suficiente. Na Inception, estimar: preço médio por assinatura, taxa de conversão esperada (free-to-paid ou trial-to-paid), churn mensal projetado, e custo variável por usuário (infraestrutura, suporte, transação de pagamento). Se o LTV/CAC projetado é menor que 3:1, o modelo não é sustentável e precisa ser ajustado antes de investir em desenvolvimento. O modelo de monetização (freemium, trial, ads, marketplace commission) define a arquitetura e deve ser decidido aqui.

- **Escala como premissa arquitetural**: SaaS B2C precisa ser projetado para escalar de 100 para 100.000+ usuários sem refatoração arquitetural. Diferente de B2B (onde centenas de organizações é sucesso), B2C só funciona com volume — e volume chega de repente (viral loop, campanha de marketing, menção de influenciador). A arquitetura precisa suportar picos de tráfego (10x o tráfego normal em horas), auto-scaling de infraestrutura, e operações de banco de dados que não degradam com milhões de registros. Essas decisões são tomadas na Architecture, mas a premissa precisa ser estabelecida na Inception.

- **Canais de aquisição e growth strategy**: Em B2C, o produto não se vende sozinho — precisa de canais de aquisição: SEO (conteúdo que atrai tráfego orgânico), social media (presença e ads em Instagram, TikTok, YouTube), referral (usuários convidando usuários com incentivo), app store (ASO para mobile), parcerias, e mídia paga (Meta Ads, Google Ads). A estratégia de growth impacta o produto diretamente — referral exige sistema de convites com tracking, SEO exige páginas públicas indexáveis, app store exige app nativo. Definir os canais primários de aquisição na Inception orienta decisões de produto e arquitetura.

- **Competição e diferenciação**: O mercado B2C é brutalmente competitivo — para cada problema, há dezenas de soluções (incluindo "não fazer nada" e "usar planilha"). O produto precisa de diferenciação clara que o usuário perceba em segundos — não em semanas de uso. Na Inception, mapear os 3-5 concorrentes diretos, identificar o que eles fazem bem e mal, e definir o posicionamento do produto: o que ele faz que os concorrentes não fazem (ou fazem pior), e para quem especificamente. Um SaaS B2C sem diferenciação clara é um SaaS B2C morto.

- **Time e capacidade de iteração rápida**: SaaS B2C exige iteração rápida — o mercado se move, os usuários dão feedback, os concorrentes lançam features, e o produto precisa evoluir semanalmente. O time deve ser capaz de deployar múltiplas vezes por dia, rodar experimentos A/B, e pivotar features baseado em dados. Se o time é pequeno (2-5 pessoas), as escolhas tecnológicas devem otimizar para velocidade de iteração acima de tudo — frameworks opinados, managed services, e deploy automático. Over-engineering na Inception é o inimigo da velocidade em B2C.

### Perguntas

1. Existe evidência de product-market fit (lista de espera, protótipo validado, dados de mercado) ou o projeto é baseado em hipótese não validada? [fonte: Produto, Diretoria, Marketing] [impacto: PM, Produto]
2. Qual é o modelo de monetização — freemium, trial + assinatura, ads, marketplace commission, ou híbrido? [fonte: Produto, Financeiro, Diretoria] [impacto: Arquiteto, Dev, PM]
3. Os unit economics foram estimados (CAC, LTV, churn projetado, custo por usuário) e o modelo é sustentável? [fonte: Financeiro, Produto, Marketing] [impacto: PM, Diretoria]
4. Quais são os canais primários de aquisição de usuários (SEO, social, referral, app store, mídia paga)? [fonte: Marketing, Growth, Diretoria] [impacto: Dev, PM, Marketing]
5. Quem são os 3-5 concorrentes diretos e qual é a diferenciação clara do produto? [fonte: Produto, Diretoria, Marketing] [impacto: PM, Produto, Designer]
6. Qual é o tamanho e a senioridade do time técnico, e qual a capacidade de iteração esperada (deploys por semana)? [fonte: CTO, Diretoria] [impacto: Arquiteto, PM]
7. Qual é o volume esperado de usuários nos primeiros 12 meses (1.000, 10.000, 100.000+)? [fonte: Marketing, Produto, Diretoria] [impacto: Arquiteto, DevOps]
8. O produto é primariamente web, mobile (app nativo) ou ambos? [fonte: Produto, Diretoria] [impacto: Arquiteto, Dev]
9. Qual é o prazo esperado para o MVP e existe um evento de negócio que justifica (rodada de investimento, sazonalidade, parceria)? [fonte: Diretoria, Investidores] [impacto: PM, Dev]
10. O produto envolve conteúdo gerado por usuários (UGC) que exige moderação? [fonte: Produto, Jurídico] [impacto: Dev, PM, Operações]
11. Há requisitos de LGPD/GDPR que impactam coleta de dados, cookies e consentimento? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, Arquiteto]
12. O produto precisará suportar múltiplos idiomas ou operar em múltiplos países? [fonte: Produto, Diretoria, Comercial] [impacto: Dev, Arquiteto, PM]
13. Existe orçamento definido separando desenvolvimento, infraestrutura mensal e marketing de aquisição? [fonte: Financeiro, Diretoria] [impacto: PM, Marketing]
14. O produto terá componente social (perfis públicos, seguir, feed, compartilhamento)? [fonte: Produto] [impacto: Arquiteto, Dev, Designer]
15. O produto lidará com dados sensíveis (saúde, financeiro, localização) que exigem proteção especial? [fonte: Jurídico, Compliance, Produto] [impacto: Arquiteto, Dev, Security]

---

## Etapa 02 — Discovery

- **Pesquisa de usuários e validação de personas**: Em B2C, a persona não é "empresa" — é um indivíduo com motivações emocionais, hábitos, restrições de tempo e sensibilidade a preço. Pesquisa qualitativa (entrevistas com 15-20 usuários potenciais) e quantitativa (survey com 200+ respostas) devem validar: o problema é real e frequente, o usuário está disposto a pagar para resolvê-lo, as alternativas atuais (incluindo "não fazer nada") são insatisfatórias, e o preço projetado está dentro do que o público aceita. Personas baseadas em achismo ("mulheres de 25-35 anos") não substituem pesquisa — personas B2C precisam de dados demográficos, comportamentais e psicográficos reais.

- **Jornada do usuário e "aha moment"**: Mapear a jornada completa do usuário — desde o primeiro contato (ad, busca orgânica, indicação) até a conversão em pagante e a retenção a longo prazo. Identificar o "aha moment" — o instante em que o usuário percebe o valor do produto pela primeira vez. Em B2C, o aha moment precisa acontecer nos primeiros minutos (não dias ou semanas como em B2B). Exemplos: no Canva é criar o primeiro design, no Spotify é ouvir a primeira playlist personalizada, no Notion é organizar a primeira nota. Todo o onboarding deve ser projetado para conduzir o usuário ao aha moment com o mínimo de friction possível.

- **Requisitos de onboarding e ativação**: O onboarding em B2C é a diferença entre retenção e abandono. Levantar: quantas etapas o usuário precisa completar antes de usar o produto (cada etapa é ponto de abandono), quais informações são obrigatórias no sign-up (quanto menos, melhor — nome e e-mail, ou social login), se há configuração inicial obrigatória (preferências, perfil, dados pessoais), e se o produto oferece valor antes mesmo de completar o cadastro (ex.: Canva permite criar design antes de fazer login). A taxa de abandono do onboarding é a métrica mais importante a monitorar no MVP.

- **Modelo de billing e paywall**: Detalhar o mecanismo de conversão — onde o paywall aparece na jornada do usuário e como é apresentado. Freemium: quais features são gratuitas e quais são pagas? O limite é por uso (5 projetos grátis) ou por feature (export em alta resolução é pago)? Trial: duração, com ou sem cartão de crédito obrigatório no cadastro (trial sem cartão tem mais ativações mas menos conversão), e-mails de nurturing durante o trial. Assinatura: mensal vs. anual (desconto típico de 20-40% para anual), métodos de pagamento por região (PIX e boleto no Brasil, cartão internacionalmente).

- **Requisitos de performance e experiência mobile**: B2C é mobile-first por natureza — 60-80% do tráfego vem de mobile. O Discovery deve levantar expectativas de performance: tempo de carregamento aceitável (sub-3 segundos no 4G é o mínimo), funcionamento em conexões lentas (3G em áreas rurais), e comportamento em dispositivos de baixo custo (Android com 2-3GB de RAM, telas de 5-6 polegadas). Se o produto é app nativo, levantar requisitos de versão mínima de OS (iOS 15+, Android 10+), tamanho do app bundle (usuários com armazenamento limitado desinstalam apps grandes), e funcionamento offline (se aplicável).

- **Requisitos de growth e viralidade**: Mapear os mecanismos de growth que o produto vai explorar — referral (sistema de convites com recompensa para quem convida e quem é convidado), sharing (conteúdo ou resultado do produto compartilhável em redes sociais com branding do produto), SEO (páginas públicas que atraem tráfego orgânico — perfis, conteúdo, resultados), e community (fórum, grupos, features sociais que aumentam retenção via network effects). Cada mecanismo de growth impacta a arquitetura — referral exige tracking de convites, sharing exige Open Graph e deep links, SEO exige SSR/SSG para páginas públicas.

### Perguntas

1. Pesquisa de usuários foi realizada (qualitativa + quantitativa) validando que o problema é real e há disposição a pagar? [fonte: Produto, UX Research, Marketing] [impacto: Produto, PM, Designer]
2. O "aha moment" do produto foi identificado e o onboarding está projetado para conduzir o usuário até ele? [fonte: Produto, UX Research] [impacto: Designer, Dev, PM]
3. Quantas etapas o sign-up exige e foi minimizado ao essencial (social login, mínimo de campos)? [fonte: Produto, Designer] [impacto: Dev, Designer]
4. O modelo de paywall foi definido — onde aparece na jornada, quais limites disparam, e como é apresentado? [fonte: Produto, Marketing, Financeiro] [impacto: Dev, Designer, PM]
5. Os planos de assinatura foram definidos com preços, periodicidade (mensal/anual) e métodos de pagamento por região? [fonte: Produto, Financeiro, Marketing] [impacto: Dev, Arquiteto]
6. Os requisitos de performance mobile foram levantados (tempo de carga, funcionamento em 3G, dispositivos de baixo custo)? [fonte: Produto, UX Research] [impacto: Dev, Arquiteto]
7. Os mecanismos de growth foram mapeados (referral, sharing, SEO, community) com impacto na arquitetura? [fonte: Growth, Marketing, Produto] [impacto: Dev, Arquiteto]
8. O produto terá social login (Google, Apple, Facebook) e quais provedores são obrigatórios no MVP? [fonte: Produto, Marketing] [impacto: Dev]
9. Existe necessidade de notificações push (mobile) e/ou e-mail marketing para reengagement? [fonte: Marketing, Produto] [impacto: Dev, Marketing]
10. O produto terá conteúdo gerado por usuário (UGC) e qual a estratégia de moderação? [fonte: Produto, Jurídico, Operações] [impacto: Dev, PM, Operações]
11. Quais métricas de produto são prioritárias (activation rate, D1/D7/D30 retention, conversion rate, churn)? [fonte: Produto, Growth] [impacto: Dev, Arquiteto, PM]
12. O produto precisa funcionar offline ou com sincronização para quando a conexão retornar? [fonte: Produto, UX Research] [impacto: Arquiteto, Dev]
13. Quais integrações com redes sociais são necessárias (compartilhamento, login, importação de contatos)? [fonte: Marketing, Produto] [impacto: Dev]
14. Existe necessidade de personalização algorítmica (recomendações, feed personalizado, conteúdo adaptativo)? [fonte: Produto] [impacto: Arquiteto, Dev, Data]
15. Há requisitos de acessibilidade (WCAG 2.1 AA) obrigatórios por legislação ou por público-alvo? [fonte: Jurídico, Produto] [impacto: Dev, Designer]

---

## Etapa 03 — Alignment

- **Priorização do MVP por impacto em ativação e retenção**: Em B2C, o MVP não é a lista de features que o fundador acha importante — é o conjunto mínimo de funcionalidades que permite ao usuário atingir o "aha moment" e retornar no dia seguinte. A priorização deve ser baseada em dados (quais features contribuem para ativação e retenção) ou, na ausência de dados, em hipóteses que serão testadas rapidamente. Features que não impactam ativação ou retenção diretamente são pós-MVP. O alignment deve produzir uma lista ordenada, não uma lista de "tudo é prioridade 1" — que é o mesmo que nada é prioridade.

- **Estratégia de experimentação e feature flags**: B2C vive de experimentação — A/B tests de onboarding, paywall, pricing, copy, e layout. O alignment deve definir a infraestrutura de experimentação: ferramenta de A/B testing (LaunchDarkly, Statsig, Growthbook, ou custom), como variantes são alocadas (por usuário, por sessão, por cohort), quanto tempo cada experimento roda (significance estatística), e quem tem autoridade para promover ou matar uma variante. Sem infraestrutura de experimentação, decisões de produto são baseadas em opinião — e em B2C, opinião perde para dados.

- **Design system e velocidade de iteração**: Definir o design system antes do build — não como documento extenso, mas como conjunto pragmático de componentes, cores, tipografia e espaçamento que permite ao time construir novas telas rapidamente sem redesenhar do zero. Em B2C, a velocidade de iteração da UI é diretamente proporcional à maturidade do design system. Usar sistema existente (Tailwind + shadcn/ui, Chakra UI, ou similar) como base e customizar — build from scratch de design system é luxo que startups B2C não podem pagar no MVP.

- **Estratégia de suporte em escala**: B2C com milhares de usuários não pode ter suporte 1-on-1 como B2B. A estratégia de suporte precisa ser escalonável: base de conhecimento self-service (FAQ, tutoriais, vídeos), chatbot para perguntas comuns, suporte humano apenas para escalações. O custo de suporte por ticket precisa ser baixo o suficiente para ser sustentável com o revenue por usuário ($5-50/mês). Se cada ticket custa $5 para resolver e o plano é $10/mês, dois tickets por mês e o suporte come 100% da receita do usuário.

- **Métricas e instrumentação de analytics**: Definir quais métricas o time vai monitorar e como serão coletadas — antes do build, não depois. Métricas de aquisição (CAC, conversion rate por canal), ativação (sign-up completion rate, aha moment rate), retenção (D1/D7/D30, cohort analysis), receita (MRR, ARPU, churn rate), e referral (viral coefficient, invite acceptance rate). A instrumentação (eventos no Mixpanel, Amplitude, ou PostHog) deve ser especificada no alignment para que o dev implemente tracking junto com as features — adicionar tracking retroativamente resulta em dados incompletos e lacunas históricas irrecuperáveis.

### Perguntas

1. O MVP foi priorizado com base em impacto em ativação e retenção, não em lista de features do fundador? [fonte: Produto, Growth] [impacto: PM, Dev, Designer]
2. A estratégia de experimentação (A/B testing) foi definida com ferramenta, processo e critérios de decisão? [fonte: Produto, Growth, Dev] [impacto: Dev, Arquiteto]
3. O design system foi definido (componentes base, cores, tipografia) permitindo iteração rápida de UI? [fonte: Designer, Dev] [impacto: Dev, Designer]
4. A estratégia de suporte em escala foi definida (self-service, chatbot, suporte humano apenas para escalação)? [fonte: Produto, Operações, Financeiro] [impacto: PM, Dev, Operações]
5. As métricas de produto (aquisição, ativação, retenção, receita, referral) foram definidas com fonte de dados? [fonte: Produto, Growth, Data] [impacto: Dev, Arquiteto]
6. A instrumentação de analytics (eventos, propriedades, funis) foi especificada para implementar junto com o código? [fonte: Produto, Data, Growth] [impacto: Dev]
7. O fluxo de onboarding foi prototipado e testado com 5-10 usuários reais antes do build? [fonte: Produto, Designer, UX Research] [impacto: Designer, Dev]
8. A estratégia de notificação (push, e-mail, in-app) foi definida com triggers, frequência e opt-out? [fonte: Produto, Marketing] [impacto: Dev, Marketing]
9. Os breakpoints e a experiência mobile foram priorizados no design (mobile-first)? [fonte: Designer, Produto] [impacto: Dev, Designer]
10. O processo de iteração pós-MVP foi definido (cadência de releases, priorização de backlog, métricas de decisão)? [fonte: Produto, Dev] [impacto: PM, Dev]
11. O modelo de billing foi validado tecnicamente — Stripe suporta os cenários de pricing (freemium + upgrade, trial, annual)? [fonte: Dev, Financeiro, Fornecedor de pagamento] [impacto: Dev, Arquiteto]
12. O escopo de integrações sociais (login, sharing, import) foi definido com APIs e limitações mapeadas? [fonte: Dev, Marketing] [impacto: Dev]
13. O cliente entende que mudanças de escopo no MVP impactam prazo e custo? [fonte: Diretoria] [impacto: PM]
14. Os critérios de sucesso do MVP foram definidos com métricas mensuráveis (não "os usuários gostarem")? [fonte: Produto, Diretoria] [impacto: PM, Produto]
15. A estratégia de lançamento foi definida (beta fechado, beta aberto, lançamento público com marketing) com timeline? [fonte: Marketing, Produto, Diretoria] [impacto: PM, Marketing, Dev]

---

## Etapa 04 — Definition

- **Modelo de dados orientado a escala**: Especificar o schema do banco de dados considerando que B2C cresce em volume de registros — não em número de tenants como B2B. Cada tabela deve ter: índices otimizados para queries frequentes (listagem paginada, busca, filtros), particionamento para tabelas que crescem rapidamente (eventos de analytics, logs de atividade, histórico de notificações), e soft delete para dados regulados (LGPD — o usuário pode pedir exclusão, mas registros financeiros precisam ser retidos). O modelo de dados em B2C é mais simples que B2B em termos de entidades, mas mais complexo em termos de volume e performance.

- **Especificação do fluxo de onboarding step-by-step**: Documentar cada tela do onboarding — campo por campo, botão por botão, com regras de validação, mensagens de erro, e caminhos alternativos (social login, skip, voltar). Definir: o que acontece se o usuário fecha o app no meio do onboarding (salva progresso? recomeça?), o que aparece se o usuário volta dias depois sem completar (nudge por e-mail ou push), e qual é o estado "mínimo viável" de setup que permite usar o produto (pode usar sem completar tudo?). O fluxo de onboarding é o funnel mais crítico do produto — cada tela com alta taxa de abandono precisa ser identificada e otimizada.

- **Especificação do paywall e upgrade flow**: Detalhar como e onde o paywall aparece — quando o usuário atinge limite (banner inline com CTA de upgrade), quando tenta acessar feature premium (modal explicando o que ganha com upgrade), e na página de pricing (comparação de planos lado a lado). Definir: o upgrade é imediato (cartão cadastrado, upgrade com 1 clique) ou requer checkout completo? O downgrade é imediato ou no final do ciclo? O cancelamento oferece oferta de retenção (desconto, pause, downgrade)? Cada micro-decisão neste fluxo impacta diretamente a conversion rate e o churn — especificar em detalhe antes do build.

- **Mapa de eventos de analytics**: Definir todos os eventos que o sistema vai rastrear — com nome padronizado (snake_case), propriedades obrigatórias, e contexto (de qual tela, qual variante de A/B test). Eventos mínimos: sign_up_started, sign_up_completed, onboarding_step_completed (com step_name), feature_used (com feature_name), paywall_shown, upgrade_started, upgrade_completed, subscription_cancelled. A especificação deve ser suficiente para que o dev implemente tracking sem precisar perguntar "quais propriedades envio neste evento?" — cada pergunta é uma ida e volta que atrasa o build.

- **Especificação de notificações e reengagement**: Definir o mapa completo de comunicações — e-mails de ciclo de vida (welcome, onboarding incompleto, trial expirando, payment failed, churn prevention), notificações push (mobile — conteúdo novo, ação pendente, streak reminder), e notificações in-app (banner, modal, badge). Para cada comunicação: trigger (evento ou condição temporal), delay (imediato, 24h após, 3 dias após), conteúdo (template com variáveis), e regras de supressão (não enviar se usuário já converteu, não enviar mais que X por semana). Comunicações mal especificadas resultam em spam — que é a causa número um de desinstalação em mobile e unsubscribe em e-mail.

- **Especificação de conteúdo e moderação (se UGC)**: Se o produto envolve conteúdo gerado por usuários, definir: regras de conteúdo (o que é permitido e proibido — community guidelines), fluxo de moderação (pré-publicação, pós-publicação com flag, ou híbrido), ferramentas de moderação (queue para review, auto-moderation com AI, report por usuários), e consequências (warning, remoção de conteúdo, suspensão de conta, ban permanente). UGC sem moderação definida resulta em conteúdo tóxico que afasta usuários legítimos e pode gerar responsabilidade legal (Marco Civil da Internet, DSA na Europa).

### Perguntas

1. O modelo de dados foi especificado com índices, particionamento e estratégia de soft delete para tabelas de alto volume? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
2. O fluxo de onboarding foi documentado tela por tela, com validações, caminhos alternativos e estado de interrupção? [fonte: Produto, Designer] [impacto: Dev, Designer]
3. O paywall e o upgrade flow foram especificados em detalhe (trigger, apresentação, checkout, downgrade, cancelamento)? [fonte: Produto, Designer, Financeiro] [impacto: Dev, Designer]
4. O mapa de eventos de analytics foi definido com nomes padronizados, propriedades e contexto por evento? [fonte: Produto, Data, Growth] [impacto: Dev]
5. O mapa de notificações (e-mail, push, in-app) foi especificado com trigger, delay, conteúdo e regras de supressão? [fonte: Produto, Marketing] [impacto: Dev, Marketing]
6. As community guidelines e o fluxo de moderação foram definidos (se o produto tem UGC)? [fonte: Produto, Jurídico, Operações] [impacto: Dev, Operações]
7. Os wireframes do fluxo completo (sign-up → onboarding → uso → upgrade → gerenciamento de conta) foram validados? [fonte: Designer, Produto] [impacto: Dev, Designer]
8. As regras de validação de campos de cadastro foram especificadas (formato, unicidade, limites)? [fonte: Produto, Dev] [impacto: Dev]
9. O fluxo de social login foi mapeado com edge cases (conta já existente com mesmo e-mail, link/unlink de provedor)? [fonte: Dev, Produto] [impacto: Dev]
10. O sistema de referral foi especificado (mecânica, recompensa, tracking, prevenção de fraude)? [fonte: Growth, Produto] [impacto: Dev, Growth]
11. As páginas públicas para SEO foram especificadas (URLs, meta tags, dados estruturados, sitemap)? [fonte: Marketing, SEO, Produto] [impacto: Dev, SEO]
12. Os breakpoints e comportamento responsivo foram documentados para cada tela crítica? [fonte: Designer] [impacto: Dev]
13. Os estados de erro, loading, vazio e offline foram especificados para cada componente? [fonte: Designer, Produto] [impacto: Dev]
14. As regras de rate limiting para usuários (anti-abuse) foram definidas por ação e por endpoint? [fonte: Produto, Arquiteto] [impacto: Dev, DevOps]
15. A documentação de definição foi revisada e aprovada por Produto, Design e Dev antes do Setup? [fonte: Produto, Designer, Dev] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Arquitetura para escala horizontal**: B2C precisa escalar horizontalmente — mais instâncias da aplicação atrás de um load balancer, não uma máquina maior. Isso exige: aplicação stateless (sessão no Redis, não em memória local), banco de dados com read replicas para queries pesadas (dashboards, relatórios, feeds), CDN para assets estáticos e conteúdo (imagens, vídeos, arquivos de usuário), e auto-scaling configurado com métricas (CPU, request count, latência) para responder a picos. O design stateless é decisão arquitetural que afeta todo o código — mudar de stateful para stateless em produção é refatoração completa.

- **Autenticação otimizada para conversão**: O fluxo de auth em B2C deve minimizar friction — cada campo adicional no sign-up reduz a taxa de conversão. Suporte a social login (Google, Apple, Facebook) como opção principal, e-mail + senha como fallback, e magic link como alternativa sem senha. Autenticação deve ser rápida — JWT com refresh token para evitar re-autenticação frequente, sessão persistente por 30+ dias em mobile. Para app nativo, suporte a biometria (Face ID, fingerprint). Soluções como Clerk, Supabase Auth ou Firebase Auth abstraem a complexidade — build custom de auth em B2C é risco desnecessário.

- **Pipeline de analytics e dados**: Definir a arquitetura de coleta e processamento de dados de uso — eventos coletados no frontend (Mixpanel SDK, Amplitude, ou PostHog self-hosted), enviados em batch assíncrono para não impactar performance, e armazenados para análise. Para análises complexas (cohort, funnel, retention curves), ferramentas especializadas (Mixpanel, Amplitude) são preferíveis a build custom. Se há necessidade de data warehouse (análise cross-platform, ML para recomendação), definir o pipeline ETL (eventos → data warehouse como BigQuery ou Snowflake → ferramenta de BI como Metabase ou Looker). A arquitetura de dados em B2C é investimento — sem dados, decisões de produto são baseadas em achismo.

- **CDN e otimização de entrega de conteúdo**: B2C com conteúdo (imagens, vídeos, áudio) precisa de CDN edge — Cloudflare, CloudFront, ou Fastly. Definir: política de cache por tipo de asset (estáticos imutáveis com cache longo, conteúdo de usuário com cache curto e invalidação), otimização de imagens (resize on-the-fly via Cloudinary/imgix, formatos WebP/AVIF, responsive images), e streaming de vídeo/áudio se aplicável (HLS com adaptive bitrate, CDN com edge caching). Para apps mobile, definir estratégia de cache local (offline-first para conteúdo já carregado, cache em disco com TTL). Performance de carregamento impacta diretamente retenção em B2C — cada segundo adicional aumenta bounce rate.

- **Infraestrutura de notificações**: Definir a stack de notificações considerando os múltiplos canais — e-mail transacional (SendGrid, Resend, ou AWS SES), push notifications para mobile (Firebase Cloud Messaging para Android, APNs para iOS, ou serviço unificado como OneSignal), push notifications para web (Service Worker + Web Push API), e notificações in-app (WebSocket ou Server-Sent Events para tempo real, polling para simplificidade). Cada canal tem suas particularidades: e-mail precisa de domínio autenticado (SPF, DKIM, DMARC) para não cair em spam, push mobile precisa de permissão do usuário (iOS pergunta uma vez — se negar, precisa ir em Settings), e WebSocket precisa de infraestrutura para conexões persistentes.

- **Estratégia de billing e gestão de assinaturas**: Stripe é o padrão para SaaS B2C — suporta subscriptions, trials, coupons, proration, e portal do cliente (customer portal para gerenciar assinatura sem código custom). Para mobile (V5), RevenueCat ou Adapty abstraem a complexidade de in-app purchases (Apple e Google têm APIs diferentes com regras diferentes). Definir: quem é o merchant of record (a empresa ou serviço como Paddle/Lemon Squeezy que cuida de VAT global), como é tratado o dunning (cobrança que falha — retry automático, e-mail de aviso, grace period), e como é tratado o churn involuntário (cartão expirado — notificar antes da expiração para atualizar).

### Perguntas

1. A aplicação é stateless com sessão em Redis e pronta para escala horizontal atrás de load balancer? [fonte: Arquiteto] [impacto: Dev, DevOps]
2. A autenticação suporta social login (Google, Apple), magic link e biometria com sessão persistente? [fonte: Arquiteto, Dev] [impacto: Dev]
3. A pipeline de analytics foi definida com ferramenta, coleta assíncrona e capacidade de análise de cohort/funnel? [fonte: Arquiteto, Produto, Data] [impacto: Dev, Data]
4. A CDN está configurada com política de cache por tipo de asset e otimização de imagens? [fonte: Arquiteto, DevOps] [impacto: DevOps, Dev]
5. A infraestrutura de notificações (e-mail, push mobile, push web, in-app) foi definida com stack por canal? [fonte: Arquiteto] [impacto: Dev, DevOps]
6. A estratégia de billing com Stripe (ou equivalente) suporta trial, upgrade, downgrade, dunning e portal do cliente? [fonte: Arquiteto, Dev, Financeiro] [impacto: Dev]
7. A arquitetura suporta auto-scaling com métricas definidas (CPU, requests, latência) e thresholds configurados? [fonte: DevOps, Arquiteto] [impacto: DevOps]
8. A estratégia de feature flags e A/B testing foi definida com ferramenta e integração na pipeline de deploy? [fonte: Arquiteto, Produto] [impacto: Dev, Produto]
9. A arquitetura de busca (se aplicável) foi definida — ElasticSearch, Algolia, Meilisearch ou full-text do PostgreSQL? [fonte: Arquiteto] [impacto: Dev]
10. A estratégia de armazenamento de arquivos de usuário foi definida (S3 + CDN, limites por plano, política de retenção)? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps]
11. O modelo de branches, ambientes e processo de deploy foi documentado (main → staging → prod com feature flags)? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
12. A estratégia de versionamento de API mobile (se app nativo) foi definida para suportar versões antigas em produção? [fonte: Arquiteto, Dev] [impacto: Dev]
13. Os custos mensais de infraestrutura foram projetados para cenários de 1k, 10k e 100k usuários ativos? [fonte: DevOps, Financeiro] [impacto: PM, Arquiteto]
14. A estratégia de proteção contra abuso (rate limiting, anti-bot, anti-fraud) foi definida? [fonte: Arquiteto, Security] [impacto: Dev, DevOps]
15. A arquitetura de recomendação/personalização foi definida (se aplicável) — heurísticas, collaborative filtering, ou ML? [fonte: Arquiteto, Data, Produto] [impacto: Dev, Data]

---

## Etapa 06 — Setup

- **Infraestrutura com auto-scaling**: Configurar a infraestrutura com capacidade de auto-scaling desde o setup — não esperar o primeiro pico de tráfego para descobrir que a infraestrutura não escala. Usar serviços managed (RDS, ElastiCache, ECS/Cloud Run) que permitem scaling automático por métricas. Configurar health checks, load balancer, e targets de scaling (scale out quando CPU >70% por 3 minutos, scale in quando <30% por 10 minutos). Mesmo no MVP com poucos usuários, a infraestrutura deve suportar um pico de 10x o tráfego normal — que é o cenário de "post viral no TikTok sobre o produto".

- **Pipeline de CI/CD com deploy contínuo**: B2C exige deploys frequentes (múltiplos por dia) — o pipeline deve ser rápido (<10 minutos do push ao deploy em produção), confiável (não quebra intermitentemente), e seguro (lint, testes, scan de vulnerabilidades). Configurar: lint + type check → testes unitários → build → deploy para staging (automático em merge para main) → testes e2e em staging → deploy para produção (automático ou manual com approval). Para mobile (V5), configurar pipeline de build para iOS e Android (Fastlane + EAS Build) com submissão automática para TestFlight e Google Play Internal Testing.

- **Setup de analytics e instrumentação**: Configurar a ferramenta de analytics (Mixpanel, Amplitude, PostHog) com: projeto separado para staging e produção, SDK integrado no frontend com inicialização correta, e os primeiros eventos de teste disparando e aparecendo no dashboard. Configurar as propriedades de usuário que serão enviadas em todo evento (user_id, plan_type, sign_up_date, referral_source). O setup de analytics no início do projeto — não no final — garante que o time terá dados desde o primeiro usuário beta.

- **Setup de billing e planos**: Criar a conta no Stripe (ou equivalente), configurar os produtos e planos definidos na Definition (free tier como plano sem cobrança, planos pagos com billing cycle mensal e anual), criar os coupons e promotion codes se aplicável, configurar o customer portal para self-service, e configurar os webhooks (subscription.created, invoice.paid, invoice.payment_failed, customer.subscription.deleted). Para mobile (V5), configurar RevenueCat com produtos no App Store Connect e Google Play Console. Testar o fluxo completo em sandbox — sign-up gratuito → uso do produto → hit do limite → upgrade → cobrança → portal do cliente.

- **Setup de e-mail e notificações**: Configurar o serviço de e-mail transacional (SendGrid, Resend, SES) com: domínio autenticado (SPF, DKIM, DMARC configurados no DNS), templates base criados (welcome, reset password, trial expiring), e envio de teste confirmado em caixa de entrada real (não apenas em logs). Para push mobile, configurar Firebase Cloud Messaging e APNs com certificados, criar os primeiros push de teste, e validar recebimento em dispositivos reais. A configuração de e-mail com domínio autenticado leva 24-48h para propagação de DNS — não deixar para a última hora.

- **Seed data e ambientes de teste**: Criar scripts que populam o banco com dados realistas — usuários em diferentes estados (trial, ativo, churned, gratuito), com diferentes volumes de uso, e dados de produto suficientes para testar performance de listagens. Para mobile (V5), criar builds de teste distribuídos via TestFlight (iOS) e Internal Testing (Android) para testers e stakeholders. Garantir que o ambiente de staging é acessível para beta testers se o plano é beta fechado.

### Perguntas

1. A infraestrutura está configurada com auto-scaling e suporta pico de 10x o tráfego normal esperado? [fonte: DevOps] [impacto: DevOps, Dev]
2. O pipeline de CI/CD completa em menos de 10 minutos e inclui lint, testes, build e deploy automático? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
3. A ferramenta de analytics está configurada com projetos separados por ambiente e primeiros eventos de teste disparando? [fonte: Dev, Produto] [impacto: Dev, Produto]
4. O Stripe (ou equivalente) está configurado com planos, webhooks e customer portal funcionando em sandbox? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
5. O serviço de e-mail está configurado com domínio autenticado (SPF, DKIM, DMARC) e templates base testados? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
6. O serviço de push notifications está configurado e testado com recebimento confirmado em dispositivos reais? [fonte: Dev] [impacto: Dev]
7. Os scripts de seed data populam ambientes de dev com dados realistas em diferentes estados de usuário? [fonte: Dev] [impacto: Dev, QA]
8. O .gitignore exclui secrets, arquivos de build e dados de teste, e o .env.example está documentado? [fonte: Dev] [impacto: Dev]
9. O domínio está configurado com SSL e subdomínios (app, api, cdn) resolvendo corretamente? [fonte: DevOps, TI] [impacto: DevOps, Dev]
10. A feature flag tool está configurada e integrada no código com pelo menos uma flag de teste funcional? [fonte: Dev, Produto] [impacto: Dev, Produto]
11. Os ambientes de staging e produção estão completamente isolados (banco, variáveis, serviços externos)? [fonte: DevOps] [impacto: DevOps, Dev]
12. O processo de onboarding de novos desenvolvedores está documentado com instruções de setup local? [fonte: Dev] [impacto: Dev]
13. Para mobile: o pipeline de build iOS/Android está configurado com distribuição para testers (TestFlight, Internal Testing)? [fonte: Dev] [impacto: Dev]
14. O monitoramento (Sentry para errors, Datadog/Grafana para métricas) está configurado com alertas básicos? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
15. O pipeline foi testado end-to-end com um PR real — lint, testes, build, deploy para staging? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Onboarding como primeiro módulo**: Implementar o fluxo de onboarding antes de qualquer outra funcionalidade — sign-up (social login + e-mail), tela de boas-vindas, coleta mínima de informações (se necessário), e condução ao "aha moment". Testar o onboarding com 5-10 usuários reais (não do time) durante o build para identificar pontos de friction que só aparecem com pessoas que não conhecem o produto. Em B2C, se o onboarding não funciona, nenhuma outra feature importa — o usuário nunca chega a ver o resto.

- **Core loop do produto**: Implementar o loop central de uso — a ação repetitiva que traz o usuário de volta ao produto diariamente. Em um app de fitness é registrar treino e ver progresso, em uma ferramenta de design é criar projeto e exportar, em um app de notas é capturar e organizar informações. O core loop deve ser fluido, rápido e satisfatório — cada milissegundo de latência e cada clique desnecessário reduz a probabilidade de o usuário retornar amanhã. Implementar com foco obsessivo em performance percebida — optimistic UI (mostrar resultado antes do servidor confirmar), skeleton loading, e transições suaves.

- **Paywall e billing integration**: Implementar o paywall nos pontos definidos na Definition — exibição do upsell quando o limite é atingido ou feature premium é acessada, página de pricing com comparação de planos, checkout com Stripe (Checkout Sessions ou Payment Element), e portal do cliente para gerenciamento de assinatura. Implementar também a lógica de gating — verificar se o usuário tem acesso a determinada feature com base no plano ativo, cota de uso restante, e estado da assinatura. O gating deve funcionar tanto no frontend (esconder/mostrar elementos) quanto no backend (rejeitar requests que excedem o plano) — gating apenas no frontend é bypass trivial.

- **Sistema de notificações e reengagement**: Implementar as notificações conforme o mapa da Definition — e-mails de ciclo de vida (welcome series, trial expiring, payment failed), push notifications (conteúdo novo, ação pendente, streak reminder), e notificações in-app (banners, modals, badges). Usar queue assíncrona para todos os envios — nunca enviar e-mail ou push síncronamente no fluxo de request. Implementar opt-out granular por canal e por tipo de notificação — legislação (LGPD, CAN-SPAM) e experiência do usuário exigem que o usuário possa escolher o que receber. Implementar tracking de abertura (e-mail) e entrega (push) para medir efetividade.

- **Analytics e tracking de eventos**: Implementar o tracking de eventos em paralelo com as features — cada botão, cada tela, cada ação significativa deve disparar o evento correspondente com as propriedades definidas no mapa de analytics. Validar que os eventos estão chegando corretamente na ferramenta (Mixpanel Debugger, Amplitude Event Debugger, PostHog Live Events). Implementar funis de conversão (sign-up → onboarding → aha moment → retention → upgrade) e verificar que não há quebra na cadeia de eventos. Analytics implementados corretamente desde o Build permitem decisões de produto baseadas em dados desde o lançamento.

- **Referral e sharing (se aplicável)**: Implementar o sistema de referral — geração de link/código único por usuário, tracking de convites enviados e aceitos, atribuição de recompensa (crédito, período grátis, feature unlock), e prevenção de fraude (mesmo IP, múltiplas contas, auto-referral). Implementar sharing de conteúdo/resultado do produto com Open Graph tags corretas para preview rico em redes sociais. Para mobile, implementar deep links (Universal Links para iOS, App Links para Android) que direcionam o usuário diretamente para o conteúdo compartilhado dentro do app — se o app está instalado — ou para a store se não está.

- **Performance e otimização mobile**: Otimizar a performance ao longo do build — não como tarefa final. Métricas target: LCP <2.5s, CLS <0.1, INP <200ms no web; cold start <2s e smooth 60fps scrolling no mobile. Técnicas: code splitting e lazy loading de módulos não-críticos, image optimization (WebP/AVIF, responsive images, lazy loading), bundle size monitoring (next/bundle-analyzer, size-limit), e cache de dados no frontend (React Query/SWR com stale-while-revalidate). Para mobile: lista virtualized (FlashList no React Native), cache de imagens (FastImage), e minimização de re-renders.

### Perguntas

1. O onboarding foi implementado primeiro e testado com 5-10 usuários reais fora do time? [fonte: Produto, Designer] [impacto: Dev, Designer, PM]
2. O core loop do produto é fluido, rápido e usa optimistic UI para performance percebida? [fonte: Dev, Designer] [impacto: Dev, Designer]
3. O paywall está implementado com gating no backend (não apenas frontend) e checkout funcional? [fonte: Dev, Produto] [impacto: Dev, Financeiro]
4. O sistema de notificações (e-mail, push, in-app) está implementado com queue assíncrona e opt-out granular? [fonte: Dev] [impacto: Dev, Marketing]
5. O tracking de analytics está implementado em paralelo com as features e os eventos estão chegando na ferramenta? [fonte: Dev, Produto] [impacto: Dev, Produto, Data]
6. O sistema de referral (se aplicável) está implementado com tracking, recompensa e prevenção de fraude? [fonte: Dev, Growth] [impacto: Dev, Growth]
7. A performance mobile está dentro dos targets (LCP <2.5s, cold start <2s, 60fps scroll)? [fonte: Dev] [impacto: Dev, QA]
8. O social login funciona corretamente com todos os provedores definidos (Google, Apple, Facebook)? [fonte: Dev] [impacto: Dev]
9. Os estados de erro, loading, vazio e offline estão implementados em todas as telas? [fonte: Designer, Dev] [impacto: Dev, Designer]
10. O fluxo de social sharing gera preview rico (Open Graph) e deep links funcionam em mobile? [fonte: Dev, Marketing] [impacto: Dev, Marketing]
11. O opt-out de notificações e a gestão de preferências de privacidade (LGPD) estão implementados? [fonte: Dev, Jurídico] [impacto: Dev]
12. O bundle size está monitorado e não excede limites definidos (web: <200KB initial JS, mobile: <50MB app bundle)? [fonte: Dev] [impacto: Dev, QA]
13. Os funis de conversão no analytics mostram dados consistentes sem quebra na cadeia de eventos? [fonte: Dev, Produto] [impacto: Dev, Produto]
14. A página 404 e os fluxos de erro oferecem caminhos de recuperação claros para o usuário? [fonte: Designer, Dev] [impacto: Dev, Designer]
15. O fluxo completo (sign-up → onboarding → uso → upgrade → gerenciamento) funciona end-to-end sem bugs bloqueadores? [fonte: QA, Produto] [impacto: Dev, QA, PM]

---

## Etapa 08 — QA

- **Teste de onboarding e ativação**: O teste mais importante em B2C — validar que um novo usuário consegue completar o sign-up, o onboarding e atingir o "aha moment" sem ajuda, sem confusão e sem desistir. Recrutar 10-15 testers que nunca viram o produto (não amigos do fundador, não colegas do time), pedir que completem o fluxo em voz alta (think-aloud protocol), e medir: tempo para completar o sign-up, taxa de completude do onboarding (quantos completaram vs. quantos abandonaram), tempo para atingir o aha moment, e NPS ou satisfação imediata. Cada ponto de friction identificado deve ser corrigido antes do lançamento.

- **Teste de billing e subscription lifecycle**: Validar o ciclo completo em sandbox — sign-up gratuito, uso até atingir limite, paywall exibido, upgrade com cartão de teste, uso com plano pago, renovação automática (Stripe test clock), falha de pagamento (cartão de falha), grace period, downgrade, cancelamento com oferta de retenção, e reativação. Testar edge cases: upgrade no último dia do ciclo (proration mínima), cancelamento seguido de reativação no mesmo dia, e uso de coupon com validade expirada. Para mobile: testar in-app purchase flow com sandbox da Apple e Google.

- **Teste de performance e carga**: Rodar testes de carga simulando crescimento projetado — se o plano é 10.000 usuários em 12 meses, testar com 10.000 usuários virtuais concorrentes. Focar em: tempo de resposta de endpoints críticos (feed, busca, listagem), throughput de operações de escrita concorrentes (criação de conteúdo por múltiplos usuários), e comportamento sob pico (10x tráfego normal por 30 minutos). Medir custo de infraestrutura sob carga — se o auto-scaling responde ao pico mas o custo de infra dobra, é informação relevante para o planejamento financeiro. Teste de carga deve ser executado em staging com configuração similar à produção.

- **Teste de responsividade e experiência mobile**: Validar o produto nos 5-10 dispositivos mais comuns do público-alvo — não apenas no iPhone mais recente. Testar em: iPhone SE (tela pequena), iPhone 14/15 (tela média), Android de gama média (Samsung Galaxy A, Xiaomi Redmi — 60% do mercado Android no Brasil), iPad (se tablet é suportado), e desktop (1366x768 e 1920x1080). Focar em: textos que transbordam, botões com área de toque <44px, inputs que ficam escondidos pelo teclado virtual, e scroll que não funciona corretamente em webviews. Para app nativo: testar em iOS e Android com versões mínimas suportadas.

- **Teste de notificações e reengagement**: Validar que cada notificação é entregue no canal correto, com conteúdo correto, no momento correto. E-mail: verificar recebimento em Gmail, Outlook e Yahoo (não apenas em logs), verificar que não vai para spam (check SPF/DKIM), verificar renderização em desktop e mobile. Push: verificar recebimento em foreground e background, verificar que deep link abre a tela correta, verificar opt-out funciona. In-app: verificar que notificação aparece no momento correto e some quando ação é executada. Testar regras de supressão — enviar 5 notificações em 1 hora para verificar que o rate limit funciona.

- **Teste de privacidade e LGPD**: Validar que o produto cumpre os requisitos de privacidade — banner de cookies com opção real de recusar (não apenas "aceitar"), política de privacidade acessível, opt-out de tracking funcional (desabilitar analytics quando usuário recusa cookies), e fluxo de exclusão de conta (LGPD exige que o usuário possa solicitar exclusão de seus dados — o fluxo deve ser funcional, não apenas "envie e-mail para..."). Testar que dados são realmente deletados após exclusão de conta (ou anonimizados se há obrigação de retenção de dados financeiros).

### Perguntas

1. O teste de onboarding com 10-15 testers externos foi realizado e a taxa de completude é aceitável? [fonte: Produto, UX Research] [impacto: Dev, Designer, PM]
2. O ciclo completo de billing foi testado em sandbox com todos os cenários (upgrade, falha, downgrade, cancelamento)? [fonte: QA, Dev] [impacto: Dev, Financeiro]
3. O teste de carga simulou o volume projetado com métricas de resposta e custo de infra documentados? [fonte: QA, DevOps] [impacto: Dev, DevOps, PM]
4. O produto foi testado nos 5-10 dispositivos mais comuns do público-alvo (incluindo Android de gama média)? [fonte: QA, Dev] [impacto: Dev, Designer]
5. Todas as notificações (e-mail, push, in-app) foram testadas end-to-end com verificação de entrega real? [fonte: QA, Dev] [impacto: Dev, Marketing]
6. O teste de privacidade/LGPD validou cookie banner, opt-out real de tracking e exclusão funcional de conta? [fonte: QA, Jurídico] [impacto: Dev, Jurídico]
7. O social login foi testado com contas reais em todos os provedores e edge cases (mesmo e-mail, link/unlink)? [fonte: QA, Dev] [impacto: Dev]
8. Os deep links (mobile) foram testados em iOS e Android com app instalado e sem app (redirect para store)? [fonte: QA, Dev] [impacto: Dev]
9. Os funis de analytics foram validados — cada etapa tem dados consistentes e não há quebra na cadeia? [fonte: QA, Produto] [impacto: Dev, Produto]
10. O referral system (se aplicável) foi testado com cenários de sucesso, fraude (auto-referral, mesmo IP) e recompensa? [fonte: QA, Growth] [impacto: Dev, Growth]
11. A performance mobile está dentro dos targets em dispositivos reais (não emulador)? [fonte: QA, Dev] [impacto: Dev]
12. Os e-mails não estão caindo em spam em Gmail, Outlook e Yahoo e a renderização é correta em mobile? [fonte: QA, Marketing] [impacto: Dev, Marketing]
13. O fluxo de exclusão de conta funciona end-to-end e os dados são realmente deletados/anonimizados? [fonte: QA, Jurídico] [impacto: Dev, Jurídico]
14. A revisão de conteúdo (textos, copy, UX writing) foi concluída com consistência de tom e voz? [fonte: Marketing, Produto] [impacto: Designer, Marketing]
15. O teste de acessibilidade (WCAG 2.1 AA) foi executado nos fluxos críticos? [fonte: QA, Designer] [impacto: Dev, Designer]

---

## Etapa 09 — Launch Prep

- **Estratégia de lançamento e ramp-up**: Definir a abordagem de lançamento — beta fechado (convite restrito para validação final com grupo controlado), beta aberto (sign-up público mas sem marketing ativo), ou lançamento público (sign-up público com campanha de marketing ativa). Para a maioria dos SaaS B2C, a sequência recomendada é: beta fechado (2-4 semanas com 50-200 usuários) → beta aberto (2-4 semanas com crescimento orgânico) → lançamento público (marketing ativo). Cada fase serve para identificar e corrigir problemas em escala crescente — lançar direto para o público com marketing pago é descobrir bugs com dinheiro.

- **Configuração de billing em produção**: Migrar de sandbox para produção no Stripe — criar conta verified, configurar chaves de API de produção, ativar webhooks de produção, e testar com transação real de valor mínimo. Para mobile, submeter a primeira versão com in-app purchase para review (Apple pode levar 3-5 dias para aprovar a primeira submissão com IAP — planejar com antecedência). Verificar que a lógica de feature gating funciona corretamente em produção — plano gratuito tem acesso limitado, plano pago tem acesso completo, trial expira na data correta.

- **ASO e App Store listing (se mobile)**: Preparar as listagens na App Store e Google Play — título (30 chars iOS, 50 chars Android), subtítulo/short description, descrição longa com keywords, screenshots (6-10 por tamanho de tela, mostrando as features core), app preview video (opcional mas recomendado), ícone (1024×1024px), e categorias. O ASO (App Store Optimization) é o SEO do mobile — keywords no título e descrição impactam diretamente a visibilidade em buscas na store. Preparar as listagens com antecedência e não no último dia antes da submissão.

- **Campanhas de aquisição pré-lançamento**: Se há orçamento de marketing, preparar as campanhas antes do go-live — Meta Ads (Instagram, Facebook), Google Ads (Search, Display), e/ou TikTok Ads com criativos testados. Configurar os pixels de conversão (Meta Pixel, Google Ads tag) no produto e validar que os eventos de conversão (sign-up, trial start, purchase) estão sendo registrados corretamente. Preparar landing page de pré-lançamento com lista de espera se o lançamento for faseado. As campanhas devem estar prontas para ativar no momento do go-live — tempo entre lançamento e primeira campanha ativa é receita perdida.

- **Plano de suporte para os primeiros dias**: Dimensionar suporte para o volume esperado nos primeiros dias — que pode ser 5-10x o volume normal se houver campanha de marketing ativa no lançamento. Preparar FAQ com os problemas mais prováveis (baseado nos bugs do QA e nos feedbacks do beta), configurar chatbot com respostas automáticas para perguntas comuns, e ter time humano disponível para escalações rápidas. O tempo de resposta nos primeiros dias impacta reviews na App Store — uma review de 1 estrela por "suporte não responde" é difícil de reverter.

- **Plano de rollback e critérios de go/no-go**: Definir critérios objetivos para decidir se o lançamento prossegue ou é adiado — error rate aceitável (<1%), latência aceitável (P95 <2s), billing funcionando (primeira cobrança processada com sucesso), onboarding funcional (taxa de completude >80% no teste final). Definir plano de rollback: se algo crítico falhar nas primeiras horas, qual a sequência (reverter deploy, desativar sign-up, comunicar usuários). Para mobile: rollback é mais complexo (app publicado não pode ser revertido instantaneamente) — ter kill switch via feature flag para desativar funcionalidades problemáticas remotamente.

### Perguntas

1. A estratégia de lançamento foi definida (beta fechado → beta aberto → público) com timeline e critérios de transição? [fonte: Produto, Marketing, Diretoria] [impacto: PM, Marketing]
2. O billing está configurado em modo produção com conta verified, webhooks ativos e transação real testada? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
3. Para mobile: a App Store listing está preparada com screenshots, descrição, keywords e ícone aprovados? [fonte: Marketing, Designer, Produto] [impacto: Marketing, Dev]
4. As campanhas de aquisição estão prontas com pixels de conversão validados e criativos aprovados? [fonte: Marketing, Dev] [impacto: Marketing]
5. O FAQ e o chatbot estão configurados com respostas para os problemas mais prováveis? [fonte: Produto, CS, Dev] [impacto: CS, Operações]
6. O time de suporte está dimensionado para o volume esperado nos primeiros dias de lançamento? [fonte: CS, PM, Diretoria] [impacto: CS]
7. Os critérios de go/no-go foram definidos com métricas objetivas (error rate, latência, billing, onboarding)? [fonte: Produto, Dev, PM] [impacto: PM, Dev]
8. O plano de rollback está documentado com sequência de ações e, para mobile, kill switch via feature flag? [fonte: DevOps, Dev, PM] [impacto: DevOps, Dev]
9. O monitoramento de disponibilidade e alertas estão ativos e testados? [fonte: DevOps] [impacto: DevOps]
10. Os termos de uso, política de privacidade e consentimento de cookies estão publicados e validados pelo jurídico? [fonte: Jurídico] [impacto: Jurídico, Dev]
11. Os beta testers (se lançamento faseado) foram selecionados e convidados com instruções claras? [fonte: Produto, Marketing] [impacto: PM]
12. A landing page / site de marketing está pronta com links para sign-up ou download na store? [fonte: Marketing, Designer] [impacto: Marketing]
13. Todos os stakeholders foram notificados sobre data, horário e procedimentos do lançamento? [fonte: PM, Diretoria] [impacto: PM]
14. Os processos de revisão da App Store (se mobile) foram submetidos com antecedência suficiente (5+ dias úteis)? [fonte: Dev] [impacto: Dev, PM]
15. A documentação de suporte (help center, tutoriais, vídeos) está publicada e acessível no produto? [fonte: Produto, CS] [impacto: CS, Produto]

---

## Etapa 10 — Go-Live

- **Ativação do lançamento e monitoramento em tempo real**: Executar o plano de lançamento — ativar sign-up público (ou enviar convites do beta fechado), ativar billing em produção, publicar app na store (se mobile), e ativar campanhas de marketing (se lançamento público). Monitorar em tempo real: sign-up rate (quantos novos por hora), onboarding completion rate (quantos completam vs. abandonam), error rate (5xx devem ser <0.1%), latência de endpoints críticos, e canais de suporte (volume de tickets). O time deve estar em war room por pelo menos 4 horas após a ativação — problemas que aparecem nos primeiros minutos de tráfego real são os mais urgentes.

- **Validação de billing com transações reais**: Acompanhar as primeiras transações reais — sign-up de plano pago, upgrade de free para paid, cobrança de trial convertido. Verificar no Stripe Dashboard que os pagamentos estão sendo processados, os webhooks estão sendo entregues, e o status da assinatura no sistema reflete corretamente o Stripe. Para mobile, verificar que in-app purchases estão sendo processadas corretamente pela Apple/Google e que o RevenueCat (ou equivalente) está sincronizando o status. Uma falha de billing nas primeiras horas é perda direta de receita — verificar manualmente as primeiras 10-20 transações.

- **Monitoramento de métricas de produto**: Acompanhar os dashboards de analytics nas primeiras 24-72 horas — sign-up rate, onboarding completion, aha moment rate, e primeiras indicações de retention (D1). Comparar com as projeções e os benchmarks do beta. Se o onboarding completion está abaixo de 60%, há friction que precisa ser identificada e corrigida urgentemente. Se a D1 retention está abaixo de 30%, o produto não está entregando valor suficiente no primeiro dia — problema de produto, não de marketing. Esses dados definem as prioridades da primeira sprint pós-lançamento.

- **Gestão de reviews e feedback público**: Em B2C, os usuários expressam opinião publicamente — reviews na App Store/Google Play, posts em redes sociais, threads em Reddit/Twitter. Monitorar ativamente essas fontes nas primeiras 48 horas. Responder a reviews negativas com empatia e solução (reviews respondidas têm probabilidade maior de serem atualizadas para nota mais alta). Coletar feedback estruturado — NPS in-app após 3 dias de uso, survey de satisfação após completar onboarding. O feedback dos primeiros dias é o mais valioso e o mais acionável — bugs que só aparecem com diversidade de dispositivos e cenários reais.

- **Ajustes de emergência e hotfixes**: Estar preparado para deployar hotfixes nas primeiras horas — bugs críticos em B2C impactam centenas ou milhares de usuários simultaneamente. O pipeline de CI/CD deve permitir deploy de emergência em menos de 15 minutos (do push ao produção). Para mobile, ter mecanismo de hotfix sem submissão à store — CodePush (React Native), ou feature flags para desativar funcionalidades problemáticas. Priorizar ruthlessly: bugs que impedem sign-up, onboarding ou pagamento são P0 e devem ser corrigidos em horas, não dias.

- **Retrospectiva e transição para operação contínua**: Após a primeira semana estável, conduzir retrospectiva — o que funcionou, o que deu errado, quais métricas estão acima/abaixo do esperado. Definir as prioridades do primeiro mês pós-lançamento baseadas em dados reais (não mais em hipóteses). Ativar os processos operacionais contínuos: monitoramento 24/7, backup validado, scan de vulnerabilidades, atualização de dependências, e suporte com SLA. Transicionar do modo "projeto" para o modo "produto" — com roadmap de evolução, sprints regulares, e métricas de saúde do produto monitoradas semanalmente.

### Perguntas

1. O lançamento foi ativado conforme o plano e o time está em war room monitorando em tempo real? [fonte: PM, DevOps] [impacto: PM, DevOps, Dev]
2. As primeiras transações reais de billing foram verificadas manualmente no dashboard do Stripe/gateway? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
3. Os dashboards de analytics mostram sign-up rate, onboarding completion e D1 retention dentro do esperado? [fonte: Produto, Growth] [impacto: Produto, PM]
4. Os canais de suporte estão operacionais e os primeiros tickets foram respondidos dentro do prazo? [fonte: CS] [impacto: CS]
5. As reviews na App Store/Google Play (se mobile) estão sendo monitoradas e respondidas? [fonte: Marketing, CS, Produto] [impacto: Marketing, Produto]
6. O error rate em produção está abaixo de 0.1% e a latência P95 está abaixo de 2s? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
7. O auto-scaling respondeu corretamente ao tráfego real (scale out e scale in sem intervenção manual)? [fonte: DevOps] [impacto: DevOps]
8. Os pixels de conversão (Meta, Google) estão registrando eventos reais de sign-up e purchase? [fonte: Marketing, Dev] [impacto: Marketing]
9. O pipeline de hotfix está pronto para deploy de emergência em menos de 15 minutos se necessário? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
10. Para mobile: in-app purchases estão sendo processadas corretamente na Apple e Google com status sincronizado? [fonte: Dev] [impacto: Dev, Financeiro]
11. O feedback dos primeiros usuários está sendo coletado, categorizado e alimentando o backlog de produto? [fonte: Produto, CS] [impacto: Produto, PM]
12. A retrospectiva de lançamento foi agendada para a primeira semana e as prioridades pós-launch estão sendo definidas? [fonte: PM, Produto] [impacto: PM, Produto, Dev]
13. Os processos operacionais contínuos (monitoramento, backup, scan de vulnerabilidades) foram ativados? [fonte: DevOps] [impacto: DevOps]
14. O aceite formal de lançamento foi registrado (se projeto com cliente) ou o marco de "produto live" foi documentado? [fonte: PM, Diretoria] [impacto: PM]
15. As métricas de saúde do produto (uptime, error rate, support volume, churn) estão sendo monitoradas semanalmente? [fonte: Produto, DevOps, CS] [impacto: Produto, PM, DevOps]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"O produto é para todo mundo"** — Produto B2C sem persona definida é produto para ninguém. "Todo mundo de 18-65 anos" não é persona — é a população inteira. Sem foco, o produto tenta agradar todos e não encanta ninguém. Definir um nicho específico (mesmo que pareça pequeno) e dominar antes de expandir.
- **"Não precisamos validar, a ideia é óbvia"** — A maioria das ideias "óbvias" falha. Sem evidência de demanda (lista de espera, protótipo validado, dados de mercado), o projeto é aposta pura. Investir em validação antes de investir em desenvolvimento — o custo de um protótipo testado com 20 usuários é uma fração do custo de um MVP completo que ninguém usa.
- **"Vamos ser o Uber/Airbnb de X"** — Comparação com plataformas de dois lados sem reconhecer a complexidade do chicken-and-egg problem. Marketplace precisa de supply e demand simultaneamente — construir apenas um lado e esperar que o outro apareça não funciona. Se o modelo é marketplace, o plano de aquisição de ambos os lados precisa existir antes do build.

### Etapa 02 — Discovery

- **"O onboarding é só um formulário de cadastro"** — Em B2C, onboarding é o momento decisivo entre retenção e abandono. Um formulário com 10 campos e nenhuma gratificação imediata perde 60%+ dos usuários. Onboarding precisa ser projetado como experiência — mínimo de friction, condução ao valor, e feedback positivo a cada etapa.
- **"Vamos cobrar $50/mês como os concorrentes americanos"** — Pricing precisa considerar o mercado local. $50/mês é viável nos EUA, mas no Brasil (onde salário médio é ~R$3.000) é preço enterprise. Pesquisar disposição a pagar do público-alvo real, não do público imaginado.
- **"Não precisamos de analytics no MVP"** — Sem analytics, decisões de produto pós-lançamento são baseadas em feeling. Cada feature adicionada sem dados é aposta. Instrumentação mínima (sign-up, aha moment, retention, churn) é obrigatória desde o MVP — é investimento, não overhead.

### Etapa 03 — Alignment

- **"Tudo é prioridade 1"** — Se tudo é prioridade, nada é prioridade. MVP com 50 features é um produto medíocre — MVP com 5 features excepcionais é um produto que retém. Forçar ranking: se pudesse lançar com apenas 3 features, quais seriam?
- **"A gente decide o pricing depois do lançamento"** — Pricing afeta toda a arquitetura de billing, feature gating, e analytics. Lançar sem pricing definido significa lançar sem billing funcional — e adicionar billing depois é refatoração significativa. Definir ao menos a estrutura (freemium vs. trial vs. pago) no alignment.
- **"Design system é overhead para um MVP"** — Sem design system (mesmo mínimo — cores, tipografia, 5 componentes base), cada tela é desenhada do zero. O tempo gasto definindo um sistema mínimo no alignment é recuperado 10x durante o build em velocidade de implementação.

### Etapa 04 — Definition

- **Eventos de analytics definidos "depois que o dev implementar"** — Tracking adicionado retroativamente resulta em: eventos com nomes inconsistentes, propriedades faltando, e lacunas históricas irrecuperáveis. O mapa de eventos é artefato da Definition, não do QA.
- **"O onboarding tem 8 etapas, todas obrigatórias"** — Cada etapa obrigatória é um ponto de abandono. 8 etapas obrigatórias antes de usar o produto = 80%+ de abandono. Minimizar obrigatórias, permitir skip, e completar perfil progressivamente durante o uso.
- **Paywall indefinido — "a gente vai sentindo"** — Sem definição clara de onde o paywall aparece, quais limites disparam, e como o upgrade é apresentado, a implementação será inconsistente e a otimização impossível. Paywall é o coração da monetização — precisa de especificação detalhada.

### Etapa 05 — Architecture

- **"Vamos usar microservices para escalar"** — Para um time de 3-5 pessoas construindo um MVP, microservices é over-engineering. A complexidade operacional (deploy independente, service mesh, distributed tracing) consome mais capacidade do que a feature development. Monolito modular escala para milhões de usuários quando bem feito (ver: Shopify, GitHub, Basecamp).
- **"Vamos buildar nosso próprio analytics"** — Construir pipeline de analytics do zero (coleta, armazenamento, agregação, visualização) é projeto de meses. Mixpanel, Amplitude ou PostHog resolvem por $0-500/mês. O tempo do dev é melhor gasto no produto, não na infraestrutura de medição.
- **"Auth custom porque social login é fácil de implementar"** — Cada provedor de social login tem peculiaridades (Apple exige suporte, Google muda APIs, Facebook tem fluxo de review complexo). Serviços como Clerk ou Supabase Auth abstraem a complexidade e mantêm compatibilidade quando os provedores mudam. Auth custom em B2C é risco permanente de segurança.

### Etapa 06 — Setup

- **Pipeline de CI/CD lento (>20 minutos)** — Em B2C, velocidade de iteração é vantagem competitiva. Pipeline lento = menos deploys por dia = menor capacidade de reagir a feedback. Otimizar para <10 minutos: cache de dependências, testes paralelos, build incremental.
- **Analytics configurado apenas em produção** — Sem analytics em staging, os primeiros eventos no lançamento podem estar errados (nomes errados, propriedades faltando) e só são descobertos quando os dados já estão poluídos. Configurar analytics em staging primeiro, validar, depois ligar em produção.
- **"Vamos configurar auto-scaling depois"** — Configurar infra fixa para o MVP e "adicionar auto-scaling quando precisar" significa que o primeiro pico de tráfego derruba o serviço. O post viral no TikTok não avisa com antecedência. Auto-scaling desde o setup.

### Etapa 07 — Build

- **Onboarding implementado por último** — "Primeiro vamos fazer as features, depois o onboarding." Resultado: features excelentes que ninguém usa porque o onboarding é friction pura. Onboarding é o primeiro módulo a ser implementado e o mais importante a ser testado.
- **Tracking de analytics implementado "na sprint de QA"** — Analytics adicionado na última sprint tem cobertura parcial — features implementadas nas primeiras sprints não têm tracking. Implementar tracking junto com cada feature — cada PR que adiciona funcionalidade deve adicionar os eventos correspondentes.
- **Optimistic UI ignorado — "funciona, só demora um pouco"** — Em B2C, percepção de velocidade é tudo. Um botão que demora 2 segundos para responder parece quebrado. Optimistic UI (mostrar resultado imediato, reverter se falhar) transforma percepção de 2s em percepção de instantâneo. Implementar desde o início, não como otimização posterior.

### Etapa 08 — QA

- **"Testamos no iPhone 15, tá perfeito"** — 60% dos usuários de Android no Brasil usam dispositivos de gama média com 3-4GB de RAM e telas de 6 polegadas. Testar apenas no dispositivo mais recente e caro é QA para 10% do público. Testar em dispositivos representativos do público real.
- **Teste de billing apenas com upgrade** — O cenário mais crítico não é o pagamento com sucesso — é a falha, o cancelamento, o trial expirado. Se o sistema não bloqueia acesso quando o trial expira, o produto é grátis para sempre (e o dev descobre meses depois olhando o MRR).
- **"O onboarding funciona, eu mesmo testei"** — O fundador que testou o onboarding conhece o produto e consegue completar qualquer fluxo. Testers externos que nunca viram o produto revelam friction que o time é cego para ver. Teste com 10+ testers externos é obrigatório.

### Etapa 09 — Launch Prep

- **Lançamento público sem beta** — Lançar direto para o público com marketing ativo é descobrir bugs com dinheiro de ads e reputação. Beta fechado com 50-200 usuários custa quase nada e revela os 80% dos problemas que o QA não pegou. Sempre fazer beta antes do lançamento público.
- **App Store submission no dia do lançamento** — Apple pode levar 1-5 dias para aprovar (ou rejeitar) a primeira versão. Submeter no dia do lançamento planejado e rezar para aprovação imediata é irresponsável. Submeter com 7+ dias de antecedência.
- **"Marketing liga quando o produto estiver pronto"** — Se marketing só começa a preparar campanhas quando o produto é lançado, há gap de semanas entre go-live e primeiro usuário pago. Campanhas, criativos e pixels devem estar prontos para ativar no momento do go-live.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde** — Se algo der errado, o time não está disponível no fim de semana. Em B2C, fim de semana é pico de uso para muitos produtos. Go-live em dia útil, manhã, com time completo disponível por 8+ horas.
- **"O app tá na store, missão cumprida"** — Sem monitoramento das primeiras 72 horas (reviews, crash reports, métricas de ativação), problemas se acumulam silenciosamente. A primeira review de 1 estrela por crash não resolvido pode definir a percepção do produto por meses.
- **Nenhum mecanismo de hotfix mobile** — Bug crítico no app publicado, e a única opção é submeter nova versão para review (3-5 dias). Sem CodePush ou feature flags para desativar funcionalidade problemática, o bug persiste por dias. Ter kill switch remoto é obrigatório para mobile.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é SaaS B2C** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "O produto é vendido para empresas, não para consumidores" | SaaS B2B, não B2C | Reclassificar para saas-b2b |
| "É um site informativo, não precisa de login" | Site estático, não SaaS | Reclassificar para static-site |
| "É uma loja com carrinho e checkout de produtos físicos" | E-commerce, não SaaS | Reclassificar para e-commerce |
| "O cliente compra uma vez e usa para sempre" | Software com licença, não SaaS | Reclassificar para software ou app nativo |
| "Cada empresa cliente terá SSO e permissões por organização" | SaaS B2B (multi-tenant organizacional) | Reclassificar para saas-b2b |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não validamos se alguém quer isso" | 01 | Construir produto sem demanda validada — risco máximo de desperdício | Validar demand antes de avançar (landing page, protótipo, survey) |
| "Não sabemos como vamos monetizar" | 01 | Sem modelo de monetização, impossível definir billing, pricing e feature gating | Definir modelo de monetização antes do Discovery |
| "O pricing a gente define depois" | 03 | Billing, feature gating e analytics dependem do pricing | Definir estrutura de planos antes do build |
| "Não temos budget para marketing de aquisição" | 01 | SaaS B2C sem aquisição = produto sem usuários | Definir estratégia de growth orgânico ou obter budget de aquisição |
| "O app precisa funcionar em iOS 12 e Android 7" | 02 | Versões antigas limitam APIs disponíveis e aumentam custo de QA exponencialmente | Negociar versão mínima razoável (iOS 15+, Android 10+) |
| "Não temos designer no time" | 03 | B2C é competição de UX — sem design profissional, perde para concorrentes | Contratar designer ou usar design system pronto adaptado |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O MVP tem 30+ features" | 03 | Scope creep — vai demorar 3x mais e entregar qualidade 3x menor | Forçar priorização: top 5-7 features que impactam ativação e retenção |
| "A gente vai competir com [big tech]" | 01 | Big tech tem recursos infinitos — competir de frente é suicídio | Encontrar nicho ou ângulo que big tech não atende e focar nele |
| "Performance não é tão importante, depois a gente otimiza" | 02 | Em B2C mobile, 1s de delay = 10% de bounce. Performance é feature, não otimização | Definir targets de performance como requisitos do MVP |
| "Vamos suportar iOS e Android e web desde o dia 1" | 01 | 3 plataformas com time pequeno = qualidade baixa em todas | Lançar na plataforma principal do público-alvo primeiro, expandir depois |
| "Os usuários vão moderar o conteúdo entre si" | 04 | Auto-moderação falha em escala — conteúdo tóxico afasta usuários legítimos | Planejar moderação profissional + ferramentas automatizadas |
| "Não precisamos de LGPD, somos startup" | 02 | LGPD se aplica a qualquer empresa que processa dados pessoais, independente do tamanho | Implementar requisitos mínimos de LGPD (consentimento, exclusão, transparência) |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Evidência de product-market fit ou plano de validação definido (pergunta 1)
- Modelo de monetização definido (pergunta 2)
- Canais primários de aquisição identificados (pergunta 4)
- Volume esperado de usuários estimado (pergunta 7)
- Orçamento separando dev, infra e marketing (pergunta 13)

### Etapa 02 → 03

- Pesquisa de usuários realizada com dados reais (pergunta 1)
- "Aha moment" identificado (pergunta 2)
- Modelo de paywall definido (pergunta 4)
- Requisitos de performance mobile levantados (pergunta 6)
- Mecanismos de growth mapeados (pergunta 7)

### Etapa 03 → 04

- MVP priorizado por impacto em ativação e retenção (pergunta 1)
- Métricas de produto definidas com fonte de dados (pergunta 5)
- Instrumentação de analytics especificada (pergunta 6)
- Fluxo de onboarding testado com usuários reais (pergunta 7)
- Critérios de sucesso do MVP mensuráveis (pergunta 14)

### Etapa 04 → 05

- Fluxo de onboarding documentado tela por tela (pergunta 2)
- Paywall e upgrade flow especificados em detalhe (pergunta 3)
- Mapa de eventos de analytics completo (pergunta 4)
- Mapa de notificações com triggers e regras (pergunta 5)
- Documentação revisada por Produto, Design e Dev (pergunta 15)

### Etapa 05 → 06

- Arquitetura stateless pronta para escala horizontal (pergunta 1)
- Stack de auth com social login definida (pergunta 2)
- Pipeline de analytics definida (pergunta 3)
- Estratégia de billing definida (pergunta 6)
- Custos projetados por cenário de crescimento (pergunta 13)

### Etapa 06 → 07

- Infraestrutura com auto-scaling configurada (pergunta 1)
- Pipeline de CI/CD rápido (<10 min) e funcional (pergunta 2)
- Analytics configurado com eventos de teste disparando (pergunta 3)
- Billing configurado em sandbox com planos e webhooks (pergunta 4)
- E-mail com domínio autenticado e templates testados (pergunta 5)

### Etapa 07 → 08

- Onboarding implementado e testado com usuários externos (pergunta 1)
- Core loop fluido com optimistic UI (pergunta 2)
- Billing funcional com gating no backend (pergunta 3)
- Analytics implementado com eventos consistentes (pergunta 5)
- Fluxo completo end-to-end funcional sem bugs bloqueadores (pergunta 15)

### Etapa 08 → 09

- Teste de onboarding com testers externos concluído (pergunta 1)
- Billing testado com todos os cenários de lifecycle (pergunta 2)
- Performance validada em dispositivos representativos (pergunta 4)
- Privacidade/LGPD validada (pergunta 6)
- Funis de analytics consistentes (pergunta 9)

### Etapa 09 → 10

- Billing em produção validado com transação real (pergunta 2)
- Campanhas de aquisição prontas com pixels validados (pergunta 4)
- Suporte dimensionado para volume esperado (pergunta 6)
- Critérios de go/no-go definidos (pergunta 7)
- Plano de rollback documentado com kill switch mobile (pergunta 8)

### Etapa 10 → Encerramento

- Billing real processado com sucesso (pergunta 2)
- Métricas de ativação e retenção dentro do esperado (pergunta 3)
- Error rate <0.1% e latência P95 <2s (pergunta 6)
- Processos operacionais contínuos ativados (pergunta 13)
- Aceite formal ou marco "produto live" documentado (pergunta 14)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de SaaS B2C. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Freemium | V2 Assinatura Pura | V3 Marketplace | V4 Conteúdo/Mídia | V5 Mobile-First |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 3 | 2 | 2 |
| 02 Discovery | 3 | 3 | 4 | 3 | 3 |
| 03 Alignment | 3 | 2 | 3 | 2 | 3 |
| 04 Definition | 3 | 3 | 5 | 4 | 4 |
| 05 Architecture | 3 | 3 | 4 | 4 | 4 |
| 06 Setup | 3 | 2 | 3 | 3 | 4 |
| 07 Build | 4 | 4 | 5 | 4 | 5 |
| 08 QA | 3 | 3 | 4 | 3 | 5 |
| 09 Launch Prep | 3 | 3 | 3 | 3 | 4 |
| 10 Go-Live | 2 | 2 | 3 | 2 | 3 |
| **Total relativo** | **29** | **27** | **37** | **30** | **37** |

**Observações por variante:**

- **V1 Freemium**: Esforço distribuído uniformemente. O diferencial está no Build (feature gating preciso, paywall nos pontos certos) e no Alignment (definir quais features são gratuitas vs. pagas — decisão de produto que impacta toda a arquitetura). A experimentação pós-launch (A/B tests de paywall) é onde a conversão é otimizada.
- **V2 Assinatura Pura**: O mais leve em total. O foco está no Build (onboarding excepcional que demonstra valor antes do trial expirar) e no QA (teste de billing com cenários de trial expiration). Sem plano gratuito, o onboarding precisa ser impecável — o usuário decide em 7-14 dias se vale pagar.
- **V3 Marketplace**: O mais pesado junto com Mobile-First. Definition é crítica (fluxos distintos para cada lado, lógica de matching, comissionamento). Build é pesado (dois conjuntos de experiências — supply e demand). O chicken-and-egg problem adiciona complexidade no Launch (como atrair ambos os lados simultaneamente).
- **V4 Conteúdo/Mídia**: Pico na Definition (modelo de conteúdo, recomendação, personalização) e Architecture (CDN para streaming, pipeline de conteúdo). Build é moderado se o conteúdo é texto — pesado se envolve vídeo/áudio com streaming adaptativo.
- **V5 Mobile-First**: Setup e QA são os mais pesados — pipeline de build iOS/Android, submissão à store, testes em dispositivos reais, in-app purchases com Apple/Google. A complexidade de duas plataformas (iOS + Android) e o ciclo de review da App Store adicionam tempo e risco em cada etapa.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Produto exclusivamente web, sem app mobile (Etapa 01, pergunta 8) | Etapa 05: perguntas 12, 15 parcial (versionamento de API mobile, notificações push nativas). Etapa 06: pergunta 13 (pipeline iOS/Android). Etapa 08: pergunta 8 (deep links). Etapa 09: perguntas 3 e 14 (ASO, App Store review). Etapa 10: pergunta 10 (in-app purchases). |
| Modelo de assinatura pura, sem freemium (Etapa 01, pergunta 2) | Perguntas sobre feature gating entre plano free e pago se simplificam. O paywall é trial expiration, não limite de uso. |
| Sem UGC — conteúdo apenas do time interno (Etapa 01, pergunta 10) | Etapa 02: pergunta 10 (moderação). Etapa 04: pergunta 6 (community guidelines). Etapa 09: moderação como processo operacional. |
| Sem referral system no MVP (Etapa 02, pergunta 7) | Etapa 04: pergunta 10 (especificação de referral). Etapa 07: pergunta 6 (implementação de referral). Etapa 08: pergunta 10 (teste de referral). |
| Mercado único (apenas Brasil) sem i18n (Etapa 01, pergunta 12) | Perguntas sobre multi-currency, multi-language e localização por região se tornam irrelevantes. Billing simplificado para BRL. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| App mobile nativo como plataforma principal (Etapa 01, pergunta 8) | Etapa 05: pergunta 12 (versionamento de API para suportar versões antigas) se torna bloqueadora. Etapa 06: pergunta 13 (pipeline iOS/Android) se torna gate. Etapa 09: perguntas 3 e 14 (ASO e submissão antecipada) se tornam obrigatórias. Etapa 10: pergunta 10 (in-app purchases) se torna gate. |
| Modelo freemium com feature gating (Etapa 01, pergunta 2) | Etapa 04: pergunta 3 (paywall e upgrade flow) se torna a definição mais crítica. Etapa 05: pergunta 8 (feature flags obrigatório para gating). Etapa 07: pergunta 3 (gating no backend) se torna gate. Etapa 08: pergunta 2 (testar todos os cenários de billing) se torna crítico. |
| Produto com UGC (Etapa 01, pergunta 10) | Etapa 04: pergunta 6 (community guidelines e moderação) se torna bloqueadora. Etapa 07: implementação de queue de moderação se torna obrigatória. Etapa 09: equipe ou ferramenta de moderação ativa se torna gate. |
| Campanhas de ads pagas ativas no lançamento (Etapa 01, pergunta 4) | Etapa 06: pixels de conversão configurados se torna obrigatório. Etapa 09: perguntas 4 e 8 (campanhas prontas e pixels validados) se tornam gate. Etapa 10: pergunta 8 (pixels registrando eventos reais) se torna gate. |
| Requisitos LGPD/GDPR com dados sensíveis (Etapa 01, pergunta 15) | Etapa 04: pergunta 14 (rate limiting e anti-abuse) se torna bloqueadora. Etapa 07: pergunta 11 (gestão de preferências de privacidade) se torna gate. Etapa 08: pergunta 6 (teste de privacidade e exclusão de conta) se torna obrigatório. Etapa 09: pergunta 10 (termos e políticas publicados) se torna gate. |
| Volume esperado >100k usuários no primeiro ano (Etapa 01, pergunta 7) | Etapa 05: pergunta 7 (auto-scaling) se torna crítica com thresholds rigorosos. Etapa 06: pergunta 1 (infra com auto-scaling testado) se torna bloqueadora. Etapa 08: pergunta 3 (teste de carga com volume projetado) se torna obrigatório. Etapa 10: pergunta 7 (auto-scaling respondendo ao tráfego real) se torna gate. |
