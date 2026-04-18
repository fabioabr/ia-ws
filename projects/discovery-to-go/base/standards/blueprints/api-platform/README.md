---
title: "API Platform / Developer Portal — Blueprint"
description: "APIs públicas consumidas por desenvolvedores externos. Developer portal, documentação (OpenAPI), rate limiting, autenticação (OAuth2/API key) e billing por uso."
category: project-blueprint
type: api-platform
status: rascunho
created: 2026-04-13
---

# API Platform / Developer Portal

## Descrição

APIs públicas consumidas por desenvolvedores externos. Developer portal, documentação (OpenAPI), rate limiting, autenticação (OAuth2/API key) e billing por uso. O escopo vai desde APIs internas expostas para parceiros até plataformas de API economy com marketplace de desenvolvedores, monetização por chamada e SDKs em múltiplas linguagens.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda API platform é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — API Interna para Parceiros

API privada exposta a um número controlado de parceiros de negócio (5-50 consumidores). Autenticação por API key ou OAuth2 client credentials. Documentação básica em Swagger/OpenAPI. Sem developer portal público, sem self-service — onboarding de novos consumidores é manual com contrato. O foco é estabilidade, versionamento e SLA contratual. Exemplos: API de preços para distribuidores, API de estoque para marketplace, API de consulta de dados para parceiro estratégico.

### V2 — API Pública com Developer Portal

API aberta para qualquer desenvolvedor se cadastrar e consumir. Developer portal com self-service (signup, geração de API key, documentação interativa, sandbox). Onboarding automatizado sem interação humana. O foco é developer experience (DX) — tempo do primeiro "Hello World" deve ser <5 minutos, documentação deve ser excelente, e erros devem ser autoexplicativos. Exemplos: API de pagamentos, API de geolocalização, API de dados climáticos, API de tradução.

### V3 — API Monetizada (API-as-a-Product)

API como produto comercial com billing por uso (pay-per-call, subscription tiers, freemium). Tudo da V2 mais: billing engine, usage metering, planos e pricing, portal de billing para o consumidor, e analytics de uso por cliente. O foco é monetização confiável — metering preciso, cobrança correta, e visibilidade de uso para o cliente. Exemplos: Twilio (comunicação), Stripe (pagamentos), Algolia (busca), Mapbox (mapas).

### V4 — API Gateway / Aggregation Layer

Camada intermediária que unifica múltiplas APIs internas (microserviços, sistemas legados, SaaS de terceiros) em uma interface coesa para consumidores externos. Não implementa lógica de negócio — orquestra, transforma e roteia. O foco é composição de APIs, transformação de payloads, caching intermediário e resiliência (circuit breaker, retry, timeout). Exemplos: BFF (Backend for Frontend) exposto como API pública, API gateway de Open Banking, camada de abstração sobre sistemas legados.

### V5 — API de Dados / Open Data

API que expõe datasets para consumo — governamentais, financeiros, geográficos, científicos. Volume alto de dados com paginação, filtros e formatos de export (JSON, CSV, Parquet). Frequentemente read-only. O foco é queryability (filtros flexíveis, full-text search, geo queries), cache agressivo, e performance para queries pesadas em datasets grandes. Exemplos: API de dados abertos governamentais, API de dados de mercado financeiro, API de dados geoespaciais, API de censo/pesquisa.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | API Framework | API Gateway | Autenticação | Documentação | Observações |
|---|---|---|---|---|---|
| V1 — Parceiros | FastAPI, Express, Spring Boot | Kong ou AWS API Gateway | API Key ou OAuth2 Client Credentials | Swagger UI + Redoc | Simplicidade é prioridade. Gateway para rate limiting e logging. |
| V2 — Pública + Portal | FastAPI, NestJS, Go (Gin/Echo) | Kong, Tyk ou AWS API Gateway | OAuth2 + API Key com self-service | Developer portal custom ou Backstage, Stoplight | DX é diferencial competitivo. Sandbox obrigatório para testes. |
| V3 — Monetizada | FastAPI, NestJS, Spring Boot | Kong Enterprise, Tyk, Apigee | OAuth2 + API Key + Billing token | Portal custom com billing dashboard | Metering preciso com Stripe Billing ou usage-based billing engine. |
| V4 — Gateway/Aggregation | Apollo Gateway (GraphQL), Kong, AWS API Gateway | Kong, Envoy, AWS API Gateway | Pass-through ou token exchange | OpenAPI ou GraphQL schema | Foco em resiliência — circuit breaker, retry, timeout configuráveis. |
| V5 — Dados/Open Data | FastAPI, PostgREST, Hasura | Cloudflare, AWS CloudFront | API Key (rate limiting) ou aberto | Swagger + exemplos de query | Cache agressivo no CDN. Paginação cursor-based para datasets grandes. |

---

## Etapa 01 — Inception

- **Origem da demanda e modelo de negócio**: APIs públicas surgem de diferentes motivações — monetização direta (API como produto), expansão de ecossistema (parceiros e integradores), compliance regulatório (Open Banking, Open Health), ou necessidade técnica de desacoplamento (múltiplos frontends consumindo a mesma lógica). O modelo de negócio da API define quase todas as decisões subsequentes: uma API monetizada precisa de billing e metering; uma API de compliance precisa de certificação e auditoria; uma API de ecossistema precisa de developer experience excepcional. Identificar o modelo de negócio real na Inception evita construir features caras que não geram valor.

- **Consumidores da API**: Identificar quem vai consumir a API — desenvolvedores externos (startups, agências, freelancers), parceiros estratégicos (empresas com contrato), times internos de outros produtos, ou qualquer desenvolvedor no mundo (público aberto). O perfil do consumidor define o nível de documentação necessário, o modelo de suporte, a complexidade do onboarding e a tolerância a breaking changes. Desenvolvedores de startups toleram APIs imperfeitas mas querem velocidade. Parceiros enterprise exigem SLA formal, versionamento rigoroso e suporte técnico dedicado.

- **Escopo da API vs. sistema existente**: A API pode ser: exposição direta de um sistema existente (wrapping do banco de dados ou microserviço), camada de abstração sobre múltiplos sistemas (aggregation/BFF), ou sistema construído do zero para ser consumido como API. Cada cenário tem implicações radicalmente diferentes de esforço — expor um sistema existente parece simples mas frequentemente esbarra em limitações de performance, segurança e modelagem que não foram projetadas para exposição externa. Definir claramente se a API é "facade sobre o que existe" ou "coisa nova" evita subestimação de escopo.

- **Compromissos de estabilidade e compatibilidade**: APIs públicas criam contratos com consumidores externos. Diferente de código interno que pode ser refatorado a qualquer momento, uma API pública com 100 consumidores não pode mudar o formato de resposta sem quebrar 100 integrações. O custo de manutenção de retrocompatibilidade cresce exponencialmente com o número de consumidores e versões mantidas. O cliente precisa entender que uma API pública é um compromisso de longo prazo — e que decisões de design tomadas agora serão mantidas por anos.

- **Requisitos regulatórios e de compliance**: Alguns domínios têm regulamentação específica para APIs — Open Banking (BACEN), Open Health (ANS), PSD2 (Europa). Essas regulamentações definem não apenas o que a API deve expor, mas como (formato, autenticação, certificação, SLA mínimo). APIs que processam dados pessoais (LGPD/GDPR) precisam de consent management, data minimization e direito de exclusão implementados como endpoints. Compliance regulatório não é feature — é pré-requisito que impacta a arquitetura desde a Inception.

- **Orçamento de operação contínua**: APIs públicas têm custo de operação proporcional ao sucesso — quanto mais consumidores, mais tráfego, mais custo de infra, mais suporte. O custo não é apenas servidor — inclui API gateway (pricing por request em planos gerenciados), monitoramento, CDN para assets de documentação, suporte técnico a desenvolvedores, e manutenção de múltiplas versões. Um API gateway como Apigee pode custar $50k+/ano em plano enterprise. O cliente precisa entender o TCO antes de decidir o escopo.

### Perguntas

1. Qual é o modelo de negócio da API — monetização direta, expansão de ecossistema, compliance regulatório ou necessidade técnica? [fonte: Diretoria, Produto, Comercial] [impacto: PM, Arquiteto]
2. Quem são os consumidores da API — desenvolvedores externos, parceiros com contrato, times internos ou público aberto? [fonte: Comercial, Produto, TI] [impacto: PM, Dev, Arquiteto]
3. A API expõe um sistema existente, abstrai múltiplos sistemas ou será construída do zero? [fonte: TI, Arquiteto, Produto] [impacto: Dev, Arquiteto, PM]
4. O cliente entende que uma API pública cria compromisso de retrocompatibilidade de longo prazo? [fonte: Diretoria, Produto, TI] [impacto: Arquiteto, Dev, PM]
5. Existem requisitos regulatórios específicos (Open Banking, Open Health, PSD2, LGPD) que impactam design e certificação? [fonte: Jurídico, Compliance, Regulatório] [impacto: Arquiteto, Dev, Segurança]
6. Qual é o orçamento total separando desenvolvimento, operação mensal (infra, gateway, monitoramento) e suporte a desenvolvedores? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
7. Quantos consumidores são esperados no primeiro ano e qual é a projeção de crescimento? [fonte: Comercial, Produto, Diretoria] [impacto: Arquiteto, DevOps, PM]
8. Qual é o SLA esperado (disponibilidade, latência) e existe consequência contratual por descumprimento? [fonte: Comercial, Jurídico, Diretoria] [impacto: DevOps, Arquiteto]
9. A API terá pricing por uso (pay-per-call, tiers) ou será gratuita com rate limiting? [fonte: Financeiro, Produto, Diretoria] [impacto: Dev, Arquiteto, PM]
10. Existe API existente (legado) que será substituída e consumidores que precisam migrar? [fonte: TI, Comercial, Produto] [impacto: Dev, PM, Arquiteto]
11. O cliente tem time interno com experiência em API design e operação de plataforma ou será construído do zero? [fonte: TI, RH, Diretoria] [impacto: PM, Arquiteto]
12. Qual é o prazo esperado para o primeiro release público e existe compromisso contratual com parceiros? [fonte: Comercial, Diretoria] [impacto: PM, Dev]
13. A API precisa suportar múltiplas regiões geográficas com dados residentes em cada região (data residency)? [fonte: Jurídico, Compliance, TI] [impacto: Arquiteto, DevOps]
14. Há expectativa de fornecer SDKs em múltiplas linguagens (Python, JavaScript, Java, Go) ou apenas documentação OpenAPI? [fonte: Produto, Comercial, TI] [impacto: Dev, PM]
15. Quem será o product owner da API após o lançamento — time de produto, TI ou comercial? [fonte: Diretoria] [impacto: PM, Produto]

---

## Etapa 02 — Discovery

- **Design da API (recursos, operações, payloads)**: Mapear todos os recursos que a API vai expor, as operações sobre cada recurso (CRUD, ações custom), os payloads de request e response, e as relações entre recursos. O design deve seguir princípios REST (recursos como substantivos, HTTP verbs corretos, status codes significativos, HATEOAS se aplicável) ou GraphQL (schema-first, tipos, queries, mutations, subscriptions). O design da API é a interface pública do sistema — errros de design são custosos de corrigir após o lançamento porque consumidores externos já dependem do formato.

- **Modelo de autenticação e autorização**: Mapear os requisitos de segurança: autenticação do consumidor (API key, OAuth2 client credentials, OAuth2 authorization code, JWT), autorização (quais endpoints cada consumidor pode acessar, quais dados pode ver), e gestão de credenciais (como API keys são geradas, rotacionadas e revogadas). OAuth2 é o padrão para APIs públicas com consumidores que agem em nome de usuários finais. API key é aceitável para APIs server-to-server onde o consumidor é o próprio sistema, não um usuário. A escolha impacta a complexidade do onboarding e a segurança da plataforma.

- **Rate limiting e quotas**: Definir os limites de uso — requests por segundo, requests por minuto, requests por dia, por consumidor e por plano. Rate limiting protege a plataforma contra abuso (acidental ou intencional) e é essencial para fair use entre consumidores. Os limites devem ser comunicados claramente na documentação, retornados nos headers de resposta (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset), e o comportamento quando o limite é atingido deve ser previsível (429 Too Many Requests com Retry-After header, não timeout silencioso).

- **Requisitos de paginação, filtros e ordenação**: Para APIs que retornam coleções, definir a estratégia de paginação (offset-based vs. cursor-based), tamanho máximo de página, filtros suportados por recurso, e opções de ordenação. Cursor-based pagination é superior para datasets grandes e mutáveis (não pula/duplica itens quando dados mudam entre páginas), mas offset-based é mais intuitivo para desenvolvedores e adequado para datasets estáveis e pequenos. A escolha deve ser consistente em toda a API — consumidores não devem aprender dois padrões de paginação.

- **Requisitos de versionamento**: Definir a estratégia de versionamento desde o Discovery — não após o primeiro breaking change. Opções: URL path versioning (/v1/users, /v2/users), header versioning (Accept: application/vnd.api.v1+json), query parameter (?version=1). URL path é o mais comum, mais intuitivo e mais fácil de rotear no API gateway — recomendado salvo restrição específica. Definir também a política de depreciação: quanto tempo uma versão antiga será mantida após o lançamento da nova, como consumidores serão notificados, e qual é o sunset date.

- **Benchmarks de performance e SLA**: Definir os targets de performance: latência P50 e P99 por endpoint, throughput máximo suportado, disponibilidade target (99.9% = ~8.7h downtime/ano, 99.99% = ~52min/ano). Definir se o SLA é contratual (com penalidades financeiras por descumprimento) ou best-effort. SLA contratual exige investimento significativo em redundância, monitoramento e incident response — a diferença de custo entre 99.9% e 99.99% pode ser 10x. O cliente precisa entender que cada "nove" adicional no SLA tem custo exponencial.

### Perguntas

1. Os recursos da API foram mapeados com operações, payloads de request/response e relações entre recursos? [fonte: Produto, TI, Arquiteto] [impacto: Dev, Arquiteto]
2. O design da API segue padrões REST ou GraphQL com justificativa documentada para a escolha? [fonte: Arquiteto, TI] [impacto: Dev, Arquiteto]
3. O modelo de autenticação foi definido (API key, OAuth2, JWT) considerando o perfil dos consumidores? [fonte: Segurança, Arquiteto, Produto] [impacto: Dev, Segurança]
4. Os limites de rate limiting e quotas por plano/consumidor foram definidos com valores justificados? [fonte: Produto, TI, Arquiteto] [impacto: Dev, DevOps]
5. A estratégia de paginação foi definida (offset vs. cursor) com tamanho máximo de página e filtros por recurso? [fonte: Arquiteto, Produto] [impacto: Dev]
6. A estratégia de versionamento foi definida (URL, header, query) com política de depreciação e sunset? [fonte: Arquiteto, Produto] [impacto: Dev, PM]
7. Os targets de latência (P50, P99) e disponibilidade foram definidos com compromisso de SLA (contratual ou best-effort)? [fonte: Comercial, TI, Produto] [impacto: DevOps, Arquiteto]
8. Os formatos de resposta suportados foram definidos (JSON, XML, CSV, Protocol Buffers)? [fonte: Produto, Arquiteto] [impacto: Dev]
9. O modelo de tratamento de erros foi definido (formato de error response, códigos HTTP, mensagens de erro developer-friendly)? [fonte: Arquiteto] [impacto: Dev]
10. A API precisa suportar webhooks para notificar consumidores de eventos assíncronos? [fonte: Produto, TI] [impacto: Dev, Arquiteto]
11. Existe necessidade de idempotência em operações de escrita (POST, PUT) para proteção contra retry duplicado? [fonte: Arquiteto, Produto] [impacto: Dev]
12. A API precisa suportar bulk operations (criação/atualização em lote) para eficiência de consumidores com alto volume? [fonte: Produto, Comercial] [impacto: Dev, Arquiteto]
13. Os dados expostos pela API contêm informações pessoais (PII) que exigem mascaramento, consent ou data minimization? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, Segurança]
14. Há requisitos de CORS para consumidores que chamarão a API diretamente do browser (SPAs)? [fonte: TI, Produto] [impacto: Dev]
15. O developer portal precisa de funcionalidades além da documentação (sandbox, API playground, code samples, community forum)? [fonte: Produto, Comercial] [impacto: Dev, Designer, PM]

---

## Etapa 03 — Alignment

- **Contrato de API como especificação formal**: Alinhar que a especificação OpenAPI (ou GraphQL schema) é o contrato formal entre provider e consumidores. Mudanças neste contrato têm impacto direto em integrações externas e devem seguir processo de revisão tão rigoroso quanto mudanças de banco de dados. O ciclo "design → review → approve → implement" deve ser acordado antes do build — não são os desenvolvedores sozinhos que decidem adicionar ou remover campos. Stakeholders de produto, parceiros estratégicos e o time jurídico (para APIs reguladas) devem ter voz no design da API.

- **Política de breaking changes e depreciação**: Definir formalmente o que constitui breaking change (remover campo, mudar tipo de campo, alterar comportamento de endpoint, remover endpoint), como consumidores serão notificados (changelog, e-mail, header de depreciação, banner no developer portal), e o prazo mínimo entre anúncio e efetivação (tipicamente 6-12 meses para APIs com muitos consumidores). A política deve ser publicada no developer portal antes do lançamento — consumidores decidem se integram com base na confiança de que o provider não vai quebrar a integração sem aviso.

- **Developer experience (DX) como prioridade**: Alinhar que a documentação e o onboarding são tão importantes quanto o código da API. Uma API tecnicamente excelente com documentação ruim não será adotada. O benchmark de DX é: "um desenvolvedor novo consegue fazer a primeira chamada bem-sucedida em menos de 5 minutos?". Se a resposta for não, o onboarding precisa de trabalho. Isso inclui: quick start guide, exemplos de código em múltiplas linguagens, API playground interativo (Swagger UI, Stoplight), e mensagens de erro claras que dizem o que está errado e como corrigir.

- **Modelo de suporte a desenvolvedores**: Definir como consumidores da API obterão suporte quando tiverem problemas — documentação self-service, FAQ, community forum, canal de suporte dedicado (e-mail, Slack, Discord), ou suporte premium pago. O modelo de suporte impacta custo operacional e satisfação dos consumidores. APIs públicas com milhares de consumidores não podem ter suporte one-on-one para todos — a documentação e os erros autoexplicativos precisam resolver 90%+ dos problemas. APIs para parceiros enterprise frequentemente incluem suporte dedicado no contrato.

- **Estratégia de sandbox e ambiente de testes**: Alinhar como consumidores testarão suas integrações. Opções: sandbox environment com dados fictícios (endpoints idênticos à produção mas com dados mock), test mode com API key de teste (mesma API mas respostas simuladas), ou apenas documentação com exemplos estáticos (sem ambiente de teste). Sandbox é o padrão para APIs públicas com onboarding self-service — sem ele, desenvolvedores não conseguem testar sem impactar dados reais, o que é inaceitável para APIs de pagamento, dados financeiros ou operações destrutivas.

### Perguntas

1. A especificação OpenAPI (ou GraphQL schema) é tratada como contrato formal com processo de revisão e aprovação? [fonte: Arquiteto, Produto, Jurídico] [impacto: Dev, PM]
2. A política de breaking changes e depreciação foi definida com prazos, notificação e sunset policy? [fonte: Produto, Arquiteto, Comercial] [impacto: Dev, PM]
3. O benchmark de DX foi definido — qual é o tempo target para o primeiro "Hello World" de um desenvolvedor novo? [fonte: Produto, TI] [impacto: Dev, Designer]
4. O modelo de suporte a desenvolvedores foi definido (self-service, community, dedicado, premium)? [fonte: Produto, Comercial, Diretoria] [impacto: PM, Dev]
5. A estratégia de sandbox/ambiente de teste para consumidores foi definida? [fonte: Produto, Arquiteto] [impacto: Dev, DevOps]
6. O processo de onboarding de novos consumidores foi mapeado (signup, geração de credenciais, primeiro teste, produção)? [fonte: Produto, Comercial] [impacto: Dev, PM]
7. Os stakeholders que aprovam mudanças no design da API foram identificados (produto, parceiros, jurídico)? [fonte: Diretoria, Produto] [impacto: PM, Arquiteto]
8. O modelo de comunicação com consumidores foi definido (changelog, e-mail, developer blog, status page)? [fonte: Produto, Marketing] [impacto: PM, Dev]
9. Se API monetizada: os planos, pricing e modelo de billing foram definidos e validados com o financeiro? [fonte: Financeiro, Produto, Diretoria] [impacto: Dev, PM]
10. O SLA contratual (se aplicável) foi revisado pelo jurídico com penalidades e exclusões documentadas? [fonte: Jurídico, Comercial] [impacto: PM, DevOps]
11. O modelo de governança da API pós-lançamento foi definido — quem decide novas features, quem prioriza bugs, quem gerencia a comunidade? [fonte: Diretoria, Produto] [impacto: PM]
12. Se há API legada sendo substituída: o plano de migração de consumidores foi comunicado com timeline? [fonte: Comercial, Produto] [impacto: PM, Dev]
13. As dependências externas críticas (gateway SaaS, identity provider, billing engine) foram avaliadas com SLA e custo? [fonte: TI, Financeiro, Fornecedores] [impacto: Arquiteto, DevOps]
14. O time de desenvolvimento tem acesso às ferramentas necessárias (gateway, identity provider, billing, monitoramento)? [fonte: TI, Fornecedores SaaS] [impacto: Dev, DevOps]
15. O cliente entende que manutenção de API pública é compromisso contínuo (versionamento, suporte, monitoramento) e não projeto com fim? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Especificação OpenAPI detalhada**: Produzir a especificação OpenAPI 3.1 (ou GraphQL schema) completa com todos os endpoints, parâmetros, request bodies, response schemas, exemplos, e códigos de erro possíveis. A especificação deve ser granular o suficiente para gerar código (SDK, stubs de servidor) e documentação automaticamente. Campos devem ter description, type, format, required, enum (quando aplicável), e example. Responses devem documentar todos os status codes possíveis (200, 201, 400, 401, 403, 404, 409, 422, 429, 500) com schema de erro padronizado.

- **Schema de erros padronizado**: Definir um formato consistente de erro para toda a API — não cada endpoint com formato diferente. O padrão recomendado inclui: code (identificador único do erro, ex.: "INVALID_EMAIL"), message (descrição human-readable do erro), details (array de erros específicos por campo para validação), documentation_url (link para documentação do erro). O formato RFC 7807 (Problem Details for HTTP APIs) é um padrão maduro e recomendado. Erros padronizados permitem que consumidores implementem tratamento de erro genérico em vez de tratar cada endpoint individualmente.

- **Definição de modelos de dados e relações**: Definir os schemas de dados da API com nível de detalhe suficiente para implementação. Para cada modelo: campos com tipo, formato, validação e exemplo; relações entre modelos (embedded vs. referência por ID); formato de dados temporais (ISO 8601), monetários (centavos como inteiro, currency como código ISO 4217), e geográficos (GeoJSON). A consistência nos formatos é mais importante que a escolha individual — se datas são ISO 8601 em um endpoint e timestamp Unix em outro, a DX é degradada.

- **Webhook specifications (se aplicável)**: Se a API envia eventos via webhook, especificar formalmente: lista de eventos disponíveis, payload de cada evento, mecanismo de assinatura (registro de URL + escolha de eventos), policy de retry (exponential backoff, máximo de tentativas), assinatura de payload para verificação de autenticidade (HMAC-SHA256 com secret compartilhado), e formato de delivery report. Webhooks mal especificados são a principal fonte de frustração em APIs assíncronas — o consumidor não sabe o que esperar e não consegue implementar retry/idempotência sem documentação clara.

- **Definição de SDK e code samples**: Especificar quais linguagens terão SDK oficial (Python, JavaScript/TypeScript, Java, Go, Ruby), o nível de abstração do SDK (wrapper fino sobre HTTP ou client com objetos tipados e helpers), e se o SDK será gerado automaticamente a partir da especificação OpenAPI (openapi-generator, Speakeasy) ou desenvolvido manualmente. SDKs gerados são mais rápidos de produzir e manter em sincronia com a API, mas frequentemente têm ergonomia inferior a SDKs manuais. Para APIs públicas com >1000 consumidores, SDKs em pelo menos Python e JavaScript são expectativa mínima.

- **Métricas e analytics de uso**: Definir quais métricas serão coletadas e expostas: requests por endpoint, latência por endpoint, taxa de erro por endpoint, uso por consumidor, uso por plano, top consumers, endpoints mais populares. Essas métricas servem tanto para operação (identificar problemas) quanto para negócio (entender adoção, justificar investimento, identificar oportunidades de upsell). Para APIs monetizadas, as métricas de uso são a base do billing — precisão é obrigatória.

### Perguntas

1. A especificação OpenAPI 3.1 (ou GraphQL schema) está completa com todos os endpoints, schemas, exemplos e códigos de erro? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
2. O schema de erros padronizado foi definido e é consistente em toda a API (RFC 7807 ou formato custom)? [fonte: Arquiteto] [impacto: Dev]
3. Os modelos de dados foram definidos com tipos, formatos, validações e convenções consistentes (datas, moeda, geo)? [fonte: Arquiteto, Dev] [impacto: Dev]
4. Os webhooks (se aplicável) foram especificados com eventos, payloads, retry policy e assinatura de autenticidade? [fonte: Arquiteto, Produto] [impacto: Dev]
5. A estratégia de SDK foi definida — linguagens, nível de abstração e geração automática vs. manual? [fonte: Produto, Dev] [impacto: Dev, PM]
6. As métricas de uso e analytics foram especificadas (por endpoint, por consumidor, por plano)? [fonte: Produto, Diretoria] [impacto: Dev, PM]
7. O modelo de paginação foi especificado com formato consistente de links, metadata e tratamento de edge cases? [fonte: Arquiteto] [impacto: Dev]
8. Os limites de payload (request body size, response size, file upload) foram definidos por endpoint? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
9. A API suporta content negotiation (Accept header) ou formato fixo (apenas JSON)? [fonte: Arquiteto, Produto] [impacto: Dev]
10. O esquema de idempotência (Idempotency-Key header) foi especificado para operações de escrita? [fonte: Arquiteto] [impacto: Dev]
11. O formato de changelog e release notes foi definido com processo de publicação? [fonte: Produto, PM] [impacto: PM, Dev]
12. As regras de validação de input por endpoint foram especificadas (tipos, ranges, formatos, obrigatórios)? [fonte: Arquiteto, Produto] [impacto: Dev, QA]
13. O modelo de permissions/scopes por endpoint foi mapeado (quais planos/roles acessam quais endpoints)? [fonte: Produto, Segurança] [impacto: Dev, Segurança]
14. Os headers customizados da API foram definidos (rate limit, request ID, deprecation, pagination)? [fonte: Arquiteto] [impacto: Dev]
15. A documentação de definição foi revisada por arquiteto, produto, segurança e pelo menos um consumidor beta? [fonte: Diretoria, Produto, Parceiros] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Escolha do API Gateway**: O gateway é o componente central da plataforma — controla autenticação, rate limiting, logging, transformação e roteamento. Opções: gerenciado (AWS API Gateway, Apigee, Azure API Management) — setup rápido, custo por request, menos controle; self-hosted open-source (Kong, Tyk, KrakenD) — mais controle, requer operação, custo de infra; ou custom (middleware no próprio framework). Para APIs com >10M requests/mês, o custo do gateway gerenciado pode ser significativo — calcular antes de escolher. Kong open-source é a opção mais equilibrada para times com capacidade de operação.

- **Arquitetura de backend**: Definir se a API será monolítica (um serviço serve todos os endpoints), microserviços (cada domínio é um serviço separado atrás do gateway), ou serverless (cada endpoint é uma function). Monolítica é adequada para APIs com <20 endpoints e time pequeno — mais simples de desenvolver, testar e operar. Microserviços fazem sentido quando domínios diferentes têm requisitos de escala distintos ou são mantidos por times diferentes. Serverless é adequado para APIs com tráfego altamente variável e endpoints stateless — custo proporcional ao uso, mas cold start pode ser problema para latência P99.

- **Estratégia de banco de dados**: Definir o modelo de dados persistente e a escolha de banco. PostgreSQL é o padrão para a maioria das APIs com dados relacionais e queries complexas. Para APIs de dados com volume alto e queries de busca, considerar Elasticsearch ou OpenSearch. Para APIs com requisitos de escala horizontal massiva e schema flexível, DynamoDB ou MongoDB. Para APIs monetizadas, o metering de uso pode exigir time-series database (InfluxDB, TimescaleDB) separado do banco principal para não impactar performance das queries de negócio.

- **Infraestrutura de cache**: Cache é essencial para APIs públicas — reduz latência, custo de backend e protege contra picos de tráfego. Definir camadas: CDN cache (Cloudflare, CloudFront) para responses idempotentes com headers Cache-Control, application cache (Redis) para dados de sessão, rate limiting counters e resultados de queries frequentes, e database cache (materialized views, query cache). Definir TTL por tipo de dado — dados de referência (países, moedas) podem ser cacheados por dias; dados transacionais (saldo, pedidos) devem ser cacheados por segundos ou não cacheados.

- **Infraestrutura de monitoramento e observabilidade**: APIs públicas exigem monitoramento mais robusto que sistemas internos — downtime afeta consumidores externos e impacta reputação. Definir: health check endpoint (/health com status de dependências), status page pública (statuspage.io, Instatus, ou custom), APM (Datadog, New Relic, Grafana Cloud) para tracing distribuído, alertas para latência P99, error rate por endpoint, e threshold de rate limiting atingido por consumidor. Definir o processo de incident response: quem é acionado, em quanto tempo, como a comunicação é feita para consumidores (status page + e-mail).

- **Segurança em camadas**: Definir a stack de segurança: WAF (Web Application Firewall) na borda para bloquear ataques automatizados (SQL injection, XSS — mesmo em APIs JSON), TLS 1.3 obrigatório, CORS configurado por origem (não wildcard * em produção), rate limiting por IP e por API key (dupla camada), input validation rigorosa em cada endpoint (reject early), e audit logging de todas as operações de escrita. Para APIs que processam dados financeiros ou pessoais, implementar também request signing (HMAC) para garantir integridade e non-repudiation.

### Perguntas

1. O API Gateway foi escolhido (gerenciado, self-hosted ou custom) com justificativa de custo, controle e capacidade operacional? [fonte: Arquiteto, TI, Financeiro] [impacto: DevOps, Dev]
2. A arquitetura de backend foi definida (monolítica, microserviços ou serverless) com justificativa documentada? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
3. O banco de dados foi escolhido considerando modelo de dados, volume esperado, performance de queries e custo? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
4. A estratégia de cache em múltiplas camadas (CDN, application, database) foi definida com TTL por tipo de dado? [fonte: Arquiteto] [impacto: Dev, DevOps]
5. A infraestrutura de monitoramento foi definida com health check, status page, APM, alertas e process de incident response? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
6. A stack de segurança foi definida em camadas (WAF, TLS, CORS, rate limiting, input validation, audit logging)? [fonte: Segurança, Arquiteto] [impacto: Dev, Segurança, DevOps]
7. O mecanismo de autenticação foi desenhado com flow completo (geração de credentials, validação, rotação, revogação)? [fonte: Segurança, Arquiteto] [impacto: Dev, Segurança]
8. A infraestrutura de rate limiting suporta limites por consumidor, por plano e por IP com headers padrão? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
9. Os custos mensais de operação foram calculados para volume esperado e pico (gateway, infra, banco, monitoramento)? [fonte: Financeiro, DevOps, Arquiteto] [impacto: PM, Diretoria]
10. A arquitetura suporta deploy zero-downtime (rolling update, blue-green, canary)? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
11. A estratégia de versionamento está refletida na arquitetura (routing por versão no gateway, coexistência de versões)? [fonte: Arquiteto] [impacto: Dev, DevOps]
12. Se API monetizada: a arquitetura de metering e billing foi desenhada com precisão e auditabilidade? [fonte: Arquiteto, Financeiro, Produto] [impacto: Dev, Financeiro]
13. A arquitetura suporta multi-region (se requisito de data residency) com replicação de dados e roteamento geográfico? [fonte: Arquiteto, DevOps] [impacto: DevOps, Dev]
14. O modelo de ambientes (dev, staging, sandbox, prod) foi documentado com isolamento e dados adequados? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
15. A arquitetura foi revisada por segurança, operações e pelo menos um consumidor beta para validar viabilidade de integração? [fonte: Segurança, Operações, Parceiros] [impacto: Arquiteto, PM]

---

## Etapa 06 — Setup

- **API Gateway e infraestrutura base**: Configurar o API gateway com as rotas iniciais, policies de autenticação, rate limiting por default, e logging. Configurar ambientes separados (sandbox, staging, produção) no gateway com configurações independentes. Testar o flow completo: request chega no gateway → autenticação → rate limiting → roteamento para backend → resposta formatada → logging. Para gateways gerenciados (AWS API Gateway, Apigee), configurar também os quotas/throttling por stage e os custom domain mappings.

- **Pipeline de CI/CD com testes de contrato**: Configurar o pipeline de CI/CD que inclui: lint da especificação OpenAPI (spectral, redocly cli), testes unitários do backend, testes de contrato (verificar que a implementação está em conformidade com a especificação OpenAPI usando Prism, Dredd ou Schemathesis), testes de integração com banco real, e deploy automático para staging por merge na branch principal. O teste de contrato é especialmente importante em APIs — a especificação é o contrato público e qualquer desvio é um bug, mesmo que o backend "funcione".

- **Sandbox environment**: Configurar o ambiente de sandbox para consumidores — mesmos endpoints da produção mas com dados fictícios, sem efeitos colaterais reais (sandbox de pagamento não cobra, sandbox de e-mail não envia), e com rate limits relaxados para experimentação. O sandbox deve ser acessível com as mesmas credenciais de teste geradas no developer portal. A qualidade do sandbox define a qualidade do onboarding — se o sandbox não funciona ou tem dados irrealistas, o desenvolvedor desiste antes de integrar.

- **Developer Portal**: Configurar o developer portal com: landing page explicando o que a API faz, seção de getting started com quick start guide, documentação de referência gerada da especificação OpenAPI (Swagger UI, Redoc, Stoplight Elements), API playground interativo, seção de autenticação com instruções de como gerar e usar credenciais, changelog de versões, e status page linkada. Para APIs públicas, o portal é a primeira impressão — design profissional e conteúdo claro são obrigatórios, não diferenciais.

- **Gestão de credenciais e onboarding**: Configurar o fluxo de self-service: signup (e-mail, empresa, use case), verificação de e-mail, geração de API key (ou OAuth2 client ID + secret), dashboard do consumidor (uso, credenciais, plano), e revogação de credenciais. Para APIs de parceiros (V1), o fluxo pode ser manual — admin gera credenciais e compartilha de forma segura. Para APIs públicas (V2-V5), o fluxo deve ser completamente automatizado sem interação humana. Testar o fluxo completo como um novo desenvolvedor — criar conta, gerar key, fazer primeira chamada.

- **Configuração de domínio e SSL**: Configurar o custom domain da API (api.empresa.com), SSL/TLS com certificado válido (Let's Encrypt ou certificado gerenciado), HSTS habilitado, e redirect de HTTP para HTTPS. Para APIs com múltiplos ambientes: api.empresa.com (produção), sandbox.api.empresa.com (sandbox), staging-api.empresa.com (staging). Configurar DNS com TTL baixo antes do go-live. Para APIs com requisito de mTLS (mutual TLS), configurar certificate pinning e CA trust chain.

### Perguntas

1. O API Gateway está configurado com rotas, autenticação, rate limiting e logging em todos os ambientes? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
2. O pipeline de CI/CD inclui lint da especificação OpenAPI, testes de contrato e testes de integração? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
3. O sandbox environment está funcional com dados fictícios, sem efeitos colaterais e acessível com credenciais de teste? [fonte: Dev, QA] [impacto: Dev, QA]
4. O developer portal está publicado com documentação, quick start, playground, autenticação e changelog? [fonte: Dev, Produto, Designer] [impacto: Dev, PM]
5. O fluxo de self-service (signup → credenciais → primeira chamada) foi testado end-to-end como novo desenvolvedor? [fonte: Dev, QA] [impacto: Dev, PM]
6. O custom domain da API está configurado com SSL válido, HSTS e redirect HTTP→HTTPS? [fonte: DevOps, TI] [impacto: DevOps, Dev]
7. As variáveis de ambiente estão configuradas nos ambientes corretos e nunca hardcoded no código? [fonte: Dev, DevOps] [impacto: Dev, DevOps, Segurança]
8. O rate limiting está configurado com headers padrão (X-RateLimit-*) e retorna 429 com Retry-After corretamente? [fonte: Dev, DevOps] [impacto: Dev]
9. Os ambientes (sandbox, staging, prod) estão isolados — dados e credenciais de sandbox não funcionam em produção? [fonte: DevOps, Segurança] [impacto: DevOps, Segurança]
10. O monitoramento e alertas estão configurados desde o setup (não apenas após o go-live)? [fonte: DevOps] [impacto: DevOps]
11. O fluxo de geração e revogação de credenciais funciona corretamente (inclusive API key rotation)? [fonte: Dev, Segurança] [impacto: Dev, Segurança]
12. A status page pública está configurada e acessível para consumidores? [fonte: DevOps, Produto] [impacto: DevOps, PM]
13. O logging estruturado está configurado com request_id, consumer_id, endpoint, latency, status code em cada request? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
14. Os primeiros consumidores beta (se aplicável) foram onboardados e conseguiram fazer a primeira chamada com sucesso? [fonte: Produto, Dev] [impacto: PM, Dev]
15. A documentação de setup (como rodar localmente, como acessar ambientes, como contribuir) está atualizada e testada? [fonte: Dev] [impacto: Dev]

---

## Etapa 07 — Build

- **Implementação de endpoints por domínio**: Implementar os endpoints seguindo a especificação OpenAPI aprovada — request validation, business logic, response formatting, error handling. Cada endpoint deve ser validado automaticamente contra a especificação (contract test) após a implementação para garantir conformidade. Implementar por domínio funcional (users, orders, products), não endpoint a endpoint isolado — isso permite testes de integração por domínio e entrega incremental com valor para consumidores beta. Cada domínio entregue deve incluir documentação atualizada no developer portal.

- **Middleware de autenticação e autorização**: Implementar a camada de autenticação como middleware reutilizável — validação de API key ou JWT, lookup de consumidor, verificação de scopes/permissions por endpoint, e injeção de consumer_id no contexto da request para logging e rate limiting. O middleware deve ser o primeiro passo no pipeline de processamento — requests não autenticados devem ser rejeitados antes de chegar ao business logic. Implementar também o endpoint de introspection (para OAuth2) e o fluxo de revogação de tokens se aplicável.

- **Rate limiting e throttling**: Implementar rate limiting com precisão — counter por consumer (API key), sliding window ou token bucket algorithm, headers de resposta padronizados (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset como Unix timestamp), e resposta 429 com Retry-After header quando o limite é atingido. Para APIs monetizadas, implementar throttling por plano — consumidores em plano free têm limite menor que premium. O rate limiting deve ser atômico (Redis com Lua script ou similar) para evitar race conditions que permitem burst acima do limite.

- **Tratamento de erros consistente**: Implementar error handling padronizado em todos os endpoints seguindo o schema definido na Etapa 04. Erros de validação (400) devem listar cada campo com problema e a razão. Erros de autenticação (401) devem indicar se o token expirou, é inválido ou está ausente. Erros de autorização (403) devem indicar qual scope está faltando. Erros internos (500) devem retornar mensagem genérica (nunca stack trace) com request_id para correlação com logs internos. Implementar um error handler global que garante que nenhum erro escapa sem formatação padronizada.

- **Logging e observabilidade**: Implementar logging estruturado em cada request com: request_id (UUID gerado no gateway ou no primeiro middleware), consumer_id, endpoint, HTTP method, status code, latency_ms, request body size, response body size, e metadata relevante ao negócio. Para tracing distribuído (se microserviços), propagar o trace_id via headers (W3C Trace Context ou B3). Os logs devem ser enviados para sistema centralizado (ELK, Datadog, Grafana Loki) e nunca conter PII (dados pessoais) dos usuários finais — consumer_id é aceitável, dados do request body não.

- **Developer portal e documentação interativa**: Implementar ou configurar o developer portal com documentação gerada automaticamente da especificação OpenAPI. Adicionar: getting started guide com exemplos copiáveis em curl e em pelo menos 3 linguagens (Python, JavaScript, Java), authentication guide com passo a passo visual, error reference com todos os códigos de erro e como resolver cada um, webhook guide (se aplicável) com exemplos de payload e instruções de verificação de assinatura, e changelog com versionamento semântico. A documentação deve ser atualizada automaticamente quando a especificação muda — nunca manter documentação manual separada da spec.

### Perguntas

1. Todos os endpoints foram implementados em conformidade com a especificação OpenAPI e validados por contract tests? [fonte: Dev, Arquiteto] [impacto: Dev, QA]
2. O middleware de autenticação e autorização está implementado como camada reutilizável com verificação de scopes por endpoint? [fonte: Dev, Segurança] [impacto: Dev, Segurança]
3. O rate limiting está implementado com precisão atômica (Redis + Lua ou similar) e headers padronizados? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
4. O tratamento de erros segue o schema padronizado em todos os endpoints sem exceção? [fonte: Dev, QA] [impacto: Dev, QA]
5. O logging estruturado está implementado com request_id, consumer_id, latency e sem PII? [fonte: Dev, DPO] [impacto: Dev, Segurança]
6. A documentação do developer portal é gerada automaticamente da especificação OpenAPI e está atualizada? [fonte: Dev, Produto] [impacto: Dev, PM]
7. O getting started guide foi testado por alguém fora do time de desenvolvimento (time de QA, parceiro beta)? [fonte: QA, Parceiros] [impacto: Dev, PM]
8. Os SDKs (se aplicável) foram gerados ou implementados e estão em sincronia com a especificação? [fonte: Dev] [impacto: Dev, PM]
9. Os webhooks (se aplicável) estão implementados com retry, assinatura HMAC e delivery report? [fonte: Dev] [impacto: Dev]
10. A paginação está implementada de forma consistente em todos os endpoints de listagem? [fonte: Dev] [impacto: Dev, QA]
11. A idempotência de operações de escrita está implementada com Idempotency-Key header (se especificado)? [fonte: Dev] [impacto: Dev]
12. O metering de uso (se API monetizada) está implementado com precisão e auditabilidade? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
13. O health check endpoint (/health) retorna status de todas as dependências (banco, cache, gateway)? [fonte: Dev, DevOps] [impacto: DevOps, Dev]
14. O CORS está configurado com origens específicas (não wildcard *) e methods/headers permitidos? [fonte: Dev, Segurança] [impacto: Dev, Segurança]
15. Os estados de depreciação (Sunset header, deprecation notices) estão implementados para endpoints já marcados? [fonte: Dev, Produto] [impacto: Dev, PM]

---

## Etapa 08 — QA

- **Testes de contrato automatizados**: Executar a suíte completa de contract tests que valida que cada endpoint da implementação está em conformidade com a especificação OpenAPI — request schemas, response schemas, status codes, headers, e content types. Ferramentas como Schemathesis fazem fuzzing automatizado baseado na spec (geram inputs aleatórios válidos e inválidos para testar edge cases). Prism funciona como proxy de validação que intercepta traffic e reporta desvios da spec. Contract tests devem ser parte do CI/CD — nenhum merge é permitido se a implementação diverge da especificação.

- **Testes de performance e carga**: Executar load tests com cenários realistas: volume esperado de requests por endpoint, mix de operações (70% reads, 20% writes, 10% searches — ou o mix real esperado), requests com payloads de tamanho variável, e simulação de múltiplos consumidores simultâneos com rate limits diferentes. Medir: latência P50/P95/P99 por endpoint, throughput máximo antes de degradação, comportamento sob overload (degradação graceful vs. cascading failure), tempo de recovery após pico, e impacto do rate limiting na experiência do consumidor.

- **Testes de segurança**: Executar security testing focado em APIs: injection attacks (SQL injection, NoSQL injection, command injection via parâmetros), broken authentication (tokens expirados aceitos, credenciais de sandbox funcionando em produção, API keys de consumidor A acessando dados de consumidor B), excessive data exposure (response retorna mais campos que o documentado, incluindo dados internos), mass assignment (consumidor envia campos extras que são aceitos e persistidos), e BOLA (Broken Object Level Authorization — acessar recurso de outro consumidor via ID sequencial).

- **Testes de integração com consumidores beta**: Antes do lançamento público, ter pelo menos 2-3 consumidores beta fazendo integração real. O feedback de consumidores beta revela problemas que testes internos não encontram: documentação confusa, erros de autenticação não autoexplicativos, edge cases de paginação, respostas com formato inconsistente entre endpoints, e onboarding friction (passos desnecessários, e-mails que não chegam, credenciais que não funcionam). O beta deve ter duração mínima de 2 semanas com uso real — não apenas "testei uma vez e funcionou".

- **Teste de rate limiting e throttling**: Validar que o rate limiting funciona corretamente sob condições reais: enviar requests acima do limite e verificar que 429 é retornado com headers corretos, verificar que o counter reseta corretamente após o window, verificar que o rate limiting é por consumidor (consumer A no limite não impacta consumer B), e verificar que burst handling funciona (token bucket permite burst curto seguido de throttling, não bloqueia imediatamente). Testar também o edge case de múltiplas API keys do mesmo consumidor — o limite é por key ou por consumidor?

- **Teste do developer portal e onboarding**: Executar o fluxo completo de onboarding como um desenvolvedor novo que nunca viu a API: encontrar a documentação, entender o que a API faz, criar conta, gerar credenciais, seguir o getting started, fazer a primeira chamada com sucesso, entender um erro e corrigi-lo, encontrar a documentação de um endpoint específico. Medir o tempo total — se ultrapassar 10 minutos, o onboarding precisa ser simplificado. Testar também o API playground — requests de exemplo devem funcionar sem modificação.

### Perguntas

1. Os contract tests automatizados validam que todos os endpoints estão em conformidade com a especificação OpenAPI? [fonte: Dev, QA] [impacto: Dev, QA]
2. O load test foi executado com cenários realistas e latência P95/P99 está dentro do SLA sob carga? [fonte: DevOps, QA] [impacto: DevOps, Dev]
3. O security testing foi executado cobrindo OWASP API Security Top 10 (injection, broken auth, excessive data, BOLA)? [fonte: Segurança, QA] [impacto: Dev, Segurança]
4. Pelo menos 2-3 consumidores beta fizeram integração real por no mínimo 2 semanas e o feedback foi incorporado? [fonte: Produto, Parceiros] [impacto: Dev, PM]
5. O rate limiting foi testado com cenários de overload e os headers 429 + Retry-After estão corretos? [fonte: QA, Dev] [impacto: Dev]
6. O fluxo completo de onboarding no developer portal foi testado por alguém externo ao time e o tempo target foi atingido? [fonte: QA, Produto] [impacto: Dev, PM]
7. Os erros retornados pela API são autoexplicativos — um desenvolvedor consegue corrigir o problema sem consultar suporte? [fonte: QA, Parceiros beta] [impacto: Dev]
8. O sandbox funciona corretamente com dados fictícios, sem efeitos colaterais e com comportamento previsível? [fonte: QA, Dev] [impacto: Dev]
9. Os webhooks (se aplicável) foram testados com failure scenarios (endpoint do consumidor offline, timeout, retry, dead letter)? [fonte: QA, Dev] [impacto: Dev]
10. A paginação funciona corretamente em edge cases (página vazia, último item, dataset mutando entre páginas)? [fonte: QA, Dev] [impacto: Dev]
11. A idempotência foi testada — reenviar a mesma request com mesmo Idempotency-Key não cria duplicata? [fonte: QA, Dev] [impacto: Dev]
12. Os SDKs (se aplicável) foram testados end-to-end e produzem os mesmos resultados que chamadas HTTP diretas? [fonte: QA, Dev] [impacto: Dev]
13. O monitoramento detecta corretamente degradação de latência e error rate elevado com alertas funcionais? [fonte: DevOps, QA] [impacto: DevOps]
14. O metering de uso (se monetizada) foi validado contra requests reais — a contagem é precisa e auditável? [fonte: QA, Financeiro] [impacto: Financeiro, Dev]
15. O test de resiliência (circuit breaker, retry, timeout) foi executado com simulação de falha de backend? [fonte: QA, DevOps] [impacto: DevOps, Dev]

---

## Etapa 09 — Launch Prep

- **Programa de beta público ou early access**: Antes do lançamento geral, abrir a API para um grupo controlado de early adopters (20-50 desenvolvedores) com comunicação clara de que é versão beta, que pode haver instabilidade, e que feedback é ativamente solicitado. O programa de beta serve para: validar o onboarding em escala, identificar gaps na documentação, detectar edge cases que o QA interno não encontrou, e construir a primeira base de consumidores que servirão como referência. Definir canal de comunicação direto com os beta testers (Slack, Discord, e-mail) e person designada para responder em <24h.

- **Comunicação e marketing do lançamento**: Preparar os materiais de comunicação: developer blog post anunciando a API, documentação de getting started otimizada para SEO, landing page do developer portal com value proposition clara, exemplos de use cases com código funcional, e se aplicável, pricing page com comparação de planos. Para APIs que substituem versão anterior, comunicar timeline de migração com pelo menos 90 dias de antecedência e guia de migração com diff entre versões.

- **Status page e comunicação de incidentes**: Configurar e publicar a status page pública antes do go-live — não após o primeiro incidente. A status page deve listar todos os componentes da plataforma (API, developer portal, sandbox, webhooks, billing) com status individual. Configurar subscribers para que consumidores recebam updates automaticamente. Definir os templates de comunicação para cada tipo de incidente (degradação, outage parcial, outage total, manutenção planejada) com responsável designado para cada.

- **Plano de suporte pós-lançamento**: Definir o processo de suporte para os primeiros 30 dias — período de maior volume de perguntas. Quem responde no developer forum? Qual é o SLA de primeira resposta (24h? 4h? 1h para premium)? Quem triage bugs reportados por consumidores? Existe canal escalation para problemas que impactam múltiplos consumidores? Os primeiros 30 dias definem a reputação da API — respostas lentas ou ausentes nesse período causam abandono permanente.

- **Plano de rollback e contingência**: Documentar o plano de rollback: se a API nova apresentar problemas graves nas primeiras horas, qual é a sequência? Para APIs novas: desativar o acesso público e comunicar manutenção. Para APIs que substituem versão anterior: reverter o routing no gateway para a versão antiga (que deve estar ativa e funcional). Definir critérios de acionamento (error rate >5%, latência P99 >5s, incidente de segurança, billing incorreto) e quem tem autoridade para decidir.

### Perguntas

1. O programa de beta/early access foi executado com pelo menos 20 desenvolvedores e feedback foi incorporado? [fonte: Produto, Dev] [impacto: PM, Dev]
2. Os materiais de comunicação de lançamento estão prontos (blog post, landing page, getting started, use cases)? [fonte: Marketing, Produto] [impacto: PM, Marketing]
3. A status page pública está configurada com todos os componentes e o mecanismo de notificação de incidentes testado? [fonte: DevOps, Produto] [impacto: DevOps, PM]
4. O plano de suporte pós-lançamento foi definido com SLA de resposta, canal de comunicação e person designada? [fonte: Produto, Diretoria] [impacto: PM, Dev]
5. O plano de rollback está documentado com critérios de acionamento, sequência de ações e responsável designado? [fonte: DevOps, Diretoria] [impacto: DevOps, PM]
6. Se API substitui versão anterior: o guia de migração está publicado e os consumidores foram notificados com >90 dias? [fonte: Produto, Comercial] [impacto: PM, Dev]
7. Se API monetizada: o billing foi testado end-to-end com cobrança real em ambiente de staging? [fonte: Financeiro, Dev] [impacto: Financeiro, Dev]
8. Os limites de rate limiting por plano estão configurados em produção e testados com credenciais reais? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
9. O monitoramento de produção está ativo com alertas testados e escalação configurada? [fonte: DevOps] [impacto: DevOps]
10. A API key de teste/sandbox não funciona em produção e vice-versa — isolamento confirmado? [fonte: Segurança, QA] [impacto: Segurança, Dev]
11. A versão anterior da API (se existente) está ativa e funcional como fallback durante o período de transição? [fonte: DevOps, TI] [impacto: DevOps, PM]
12. Os termos de uso e política de uso aceitável da API foram revisados pelo jurídico e publicados? [fonte: Jurídico] [impacto: Jurídico, PM]
13. A janela de lançamento foi escolhida estrategicamente (dia útil, horário de baixo tráfego, time de suporte disponível)? [fonte: PM, DevOps] [impacto: PM, DevOps]
14. Todos os stakeholders (produto, comercial, suporte, jurídico) foram notificados sobre data e horário do go-live? [fonte: Diretoria] [impacto: PM]
15. O processo de incident response foi ensaiado (dry run) com cenário simulado de outage? [fonte: DevOps, PM] [impacto: DevOps, PM]

---

## Etapa 10 — Go-Live

- **Ativação do acesso público e monitoramento em tempo real**: Ativar o acesso público conforme o plano — para APIs novas, publicar o developer portal e habilitar signup; para APIs que substituem versão anterior, redirecionar tráfego no gateway. Monitorar em tempo real nos primeiros 60 minutos: requests por segundo, latência P50/P95/P99, error rate por endpoint, rate limiting triggers, novos signups (se público), e primeiras chamadas de consumidores. Ter pelo menos 2 pessoas monitorando — uma olhando métricas de infra, outra olhando logs de request para detectar padrões anômalos.

- **Validação com tráfego real**: Os primeiros requests reais de consumidores revelam problemas que nunca apareceram em testes: payloads com formatos inesperados (encoding diferente, campos extras, tipos errados), padrões de uso não previstos (burst de requests em sequência rápida, polling agressivo, queries com filtros complexos), e integrações que dependem de comportamentos não documentados da API anterior (se substituição). Monitorar os logs de erro 4xx em busca de padrões — se 30% dos requests de um consumidor dão 400, o problema pode ser na documentação, não no consumidor.

- **Comunicação com primeiros consumidores**: Nos primeiros 3 dias, ser proativo na comunicação — não esperar reclamações. Entrar em contato com os primeiros consumidores que fizeram signup ou que estão enviando requests para verificar se o onboarding foi fluido, se encontraram problemas, e se a documentação é clara. Feedback direto nos primeiros dias vale mais que NPS survey meses depois. Para APIs de parceiros, agendar call de validação com cada parceiro nas primeiras 48h.

- **Calibração de rate limiting e quotas**: Com tráfego real, os limites de rate limiting definidos teoricamente podem precisar de ajuste. Se muitos consumidores estão atingindo o limite em uso normal (não abusivo), o limite está baixo demais. Se nenhum consumidor se aproxima do limite, pode ser otimizado. Monitorar o X-RateLimit-Remaining dos consumidores mais ativos e ajustar proativamente — não esperar reclamação. Para APIs monetizadas, garantir que o metering está contando corretamente comparando logs do gateway com records do billing.

- **Handoff e operação contínua**: Transferir a operação para o time permanente com: runbook atualizado com aprendizados do go-live, dashboards calibrados (remover métricas irrelevantes, adicionar as que faltavam), alertas ajustados (eliminar falsos positivos, calibrar thresholds com dados reais), processo de suporte documentado e testado, e cronograma de evolução (próximas features, próxima versão, próximo sunset). A API é um produto vivo — o go-live é o início da operação, não o fim do projeto.

### Perguntas

1. O acesso público foi ativado e o developer portal está acessível e funcional para novos consumidores? [fonte: Dev, DevOps] [impacto: DevOps, PM]
2. O monitoramento em tempo real está ativo com pelo menos 2 pessoas acompanhando nos primeiros 60 minutos? [fonte: DevOps] [impacto: DevOps, Dev]
3. A latência P95/P99 com tráfego real está dentro do SLA comprometido? [fonte: DevOps] [impacto: DevOps, Dev]
4. A error rate com tráfego real está abaixo do threshold aceitável (<1% de 5xx)? [fonte: DevOps] [impacto: DevOps, Dev]
5. Os primeiros consumidores conseguiram completar o onboarding e fazer a primeira chamada com sucesso? [fonte: Produto, Dev] [impacto: PM, Dev]
6. Os logs de erro 4xx foram analisados para identificar padrões de documentação confusa ou edge cases? [fonte: Dev] [impacto: Dev, Produto]
7. O rate limiting está funcionando corretamente com tráfego real — sem bloqueios indevidos nem falhas de enforcement? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
8. Se API monetizada: o metering está contando corretamente e o billing do primeiro ciclo está alinhado com os logs? [fonte: Financeiro, Dev] [impacto: Financeiro, Dev]
9. A comunicação proativa com primeiros consumidores foi feita e o feedback foi registrado? [fonte: Produto, PM] [impacto: PM, Dev]
10. A status page foi atualizada refletindo o status real de cada componente da plataforma? [fonte: DevOps] [impacto: DevOps, PM]
11. Se API substitui versão anterior: os consumidores da versão antiga estão migrando conforme o timeline comunicado? [fonte: Produto, Comercial] [impacto: PM]
12. O plano de suporte pós-lançamento foi ativado com canal de comunicação funcionando e SLA sendo cumprido? [fonte: PM, Produto] [impacto: PM, Dev]
13. O aceite formal de entrega foi obtido com métricas de performance, SLA e documentação entregue? [fonte: Diretoria] [impacto: PM]
14. O runbook foi atualizado com aprendizados do go-live e entregue ao time de operações permanente? [fonte: DevOps, Dev] [impacto: Operações, DevOps]
15. O cronograma de evolução (próximas features, próxima versão, próximo sunset) foi definido e comunicado? [fonte: Produto, Diretoria] [impacto: PM, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Vamos expor nosso banco de dados como API"** — Database-as-API sem camada de abstração expõe schema interno, permite queries arbitrárias, e torna impossível evoluir o banco sem quebrar consumidores. A API deve ser projetada como interface de negócio, não como proxy de banco de dados.
- **"Depois a gente vê a questão de versionamento"** — Adiar versionamento para depois do lançamento é dívida técnica garantida. A primeira breaking change sem versão deprecia a confiança de todos os consumidores de uma vez. Versioning from day one.
- **"É só uma API simples de CRUD"** — APIs expostas externamente nunca são "simples". Autenticação, rate limiting, versionamento, documentação, tratamento de erros, paginação, cache, monitoramento e suporte são obrigatórios para qualquer API pública. O CRUD é 20% do esforço.

### Etapa 02 — Discovery

- **"Não precisamos de rate limiting, confiamos nos parceiros"** — Um parceiro com bug de loop infinito pode derrubar a API para todos os consumidores em segundos. Rate limiting é proteção da plataforma, não desconfiança do consumidor.
- **"A documentação a gente faz no final"** — API-first significa documentação é o produto. Se a especificação OpenAPI não é o primeiro artefato do projeto, o design será emergente e inconsistente. Design-first, implement after.
- **"Não precisa de sandbox, podem testar em staging"** — Staging é ambiente interno com dados internos. Consumidores externos não devem ter acesso a dados de staging. Sandbox é ambiente dedicado com dados fictícios e comportamento controlado.

### Etapa 03 — Alignment

- **"O contrato da API pode mudar a qualquer momento"** — Se o contrato muda sem aviso, consumidores não integram. A confiança na estabilidade do contrato é o fundamento de qualquer API platform. Breaking changes devem seguir processo formal com meses de antecedência.
- **"Suporte a desenvolvedores é responsabilidade do time de TI"** — Suporte de API é suporte de produto, não de infraestrutura. Requer entendimento do negócio, da documentação e do contexto do consumidor. TI não tem essa visão. Produto ou developer relations deve ser o dono.
- **"Não precisamos de status page, o monitoring da empresa serve"** — Monitoring interno não é acessível por consumidores externos. Quando a API cai, consumidores precisam saber se o problema é do lado deles ou do provider. Status page pública é obrigatória para APIs com consumidores externos.

### Etapa 04 — Definition

- **Especificação OpenAPI como documentação, não como contrato** — Se a spec é escrita depois da implementação ("vou documentar o que fiz"), ela reflete o código, não o design. Spec-first garante que o design é intencional e que contract tests validam a implementação contra o design, não o contrário.
- **"Cada endpoint tem seu próprio formato de erro"** — Inconsistência de erro força consumidores a implementar tratamento diferente para cada endpoint. Schema de erro padronizado em toda a API é requisito de DX mínimo.
- **"Versionamento semântico não se aplica a APIs"** — Versioning é mais importante em APIs do que em bibliotecas. Consumidores externos não controlam quando upgradam — o provider controla. Sem versioning claro, qualquer mudança é potencialmente breaking.

### Etapa 05 — Architecture

- **"Vamos usar API Gateway X porque já temos licença"** — Gateway escolhido por inércia corporativa, não por adequação. Um gateway enterprise projetado para APIs internas pode não ter features essenciais para APIs públicas (developer portal, billing, analytics de consumidor). Avaliar antes de reusar.
- **"Microserviços porque é moderno"** — API com 5 endpoints mantida por time de 3 pessoas não precisa de microserviços. A complexidade operacional de 5 serviços, 5 bancos de dados e 5 pipelines de deploy é maior que o benefício de isolamento. Monolito primeiro, extrair quando justificado.
- **"Cache complica, vamos servir sempre do banco"** — API pública sem cache: cada request vai ao banco, latência alta, custo alto, e qualquer pico de tráfego derruba o backend. Cache em múltiplas camadas é infraestrutura obrigatória, não otimização prematura.

### Etapa 06 — Setup

- **"O sandbox usa o mesmo banco de produção"** — Consumidores testando contra dados reais é violação de privacidade e risco operacional. Sandbox deve ter banco próprio com dados fictícios e zero conexão com produção.
- **"CI/CD sem contract tests"** — Deploy de API sem verificar conformidade com a especificação é deploy sem QA. Um campo removido acidentalmente passa em todos os unit tests mas quebra todos os consumidores. Contract test no pipeline é obrigatório.
- **"Developer portal em página estática com Swagger UI embedado"** — Swagger UI sozinho não é developer portal. Faltam: getting started, authentication guide, error reference, changelog, playground com credenciais de sandbox, e search. DX requer investimento além de auto-geração.

### Etapa 07 — Build

- **"Tratamento de erro? Deixamos o framework resolver"** — Erros default do framework expõem stack trace, internals do servidor e caminhos de arquivo. Em API pública, isso é vulnerabilidade de segurança e péssima DX. Error handler global customizado é obrigatório.
- **"Rate limiting no código, sem Redis"** — Rate limiting in-memory não funciona com múltiplas instâncias — cada instância tem seu próprio counter. Com 3 instâncias, o consumidor efetivamente tem 3x o limite. Rate limiting distribuído (Redis, Memcached) é obrigatório para qualquer API com auto-scaling.
- **"Documentação depois do build"** — Se a documentação é escrita depois, ela documenta o que foi implementado, não o que foi projetado. Divergências entre spec e implementação passam despercebidas. Spec-first + contract test é o fluxo correto.

### Etapa 08 — QA

- **"Testamos com Postman, funciona"** — Testes manuais com Postman cobrem o caminho feliz de poucos endpoints. QA de API exige: contract tests automatizados, fuzzing, load test, security test (OWASP API Top 10), e teste de paginação/rate limiting em edge cases. Postman é para exploração, não para QA.
- **"Security test é responsabilidade de infosec"** — A equipe de segurança faz pentest e review, mas o time de desenvolvimento deve implementar e testar segurança durante o build (input validation, BOLA prevention, token validation). Esperar pelo pentest no final resulta em rewrite de última hora.
- **"Beta desnecessário, testamos internamente"** — Testes internos são feitos por pessoas que entendem a API porque a construíram. O beta com consumidores externos revela problemas de DX, documentação e onboarding que só aparecem para quem vê a API pela primeira vez.

### Etapa 09 — Launch Prep

- **"Lançamento soft — abrimos o portal e vemos quem aparece"** — Sem comunicação, ninguém aparece. APIs não são virais por natureza — precisam de developer marketing (blog, exemplos, comunidade). Lançamento sem comunicação é feature sem usuário.
- **"Plano de suporte? O time de dev responde"** — Desenvolvedores respondendo suporte durante o build da próxima versão gera context switching destrutivo. Suporte deve ter processo, pessoa designada e SLA — não ser absorvido pelo mesmo time que desenvolve.
- **"A versão antiga desliga no dia do lançamento da nova"** — Consumidores não migram instantaneamente. Período de coexistência de pelo menos 6 meses (para APIs públicas) é padrão de mercado. Desligar a versão antiga sem aviso destrói confiança permanentemente.

### Etapa 10 — Go-Live

- **"O developer portal está no ar, missão cumprida"** — Portal publicado sem consumidores ativos não é go-live, é deploy. O go-live real é quando consumidores estão enviando requests em produção e recebendo respostas corretas. Monitorar adoção, não apenas disponibilidade.
- **"Go-live na sexta antes de feriado"** — Se algo der errado no fim de semana prolongado, não há time disponível. Go-live deve ser em dia útil com pelo menos 4h de buffer e time de suporte ativo por 48h.
- **"Monitoramento só para 5xx"** — 5xx é o sintoma final. Monitorar também: latência crescente (indica degradação antes do colapso), 4xx rate alto (indica problema de DX ou breaking change), rate limiting triggers (indica necessidade de ajuste), e zero traffic de consumidor (indica que o onboarding quebrou).

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é API platform** como descrito e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "A API é só para nosso app mobile consumir" | Backend for Frontend (BFF), não API platform | Reclassificar para web-app ou mobile-app |
| "Só um sistema vai consumir, o nosso ERP" | Integração ponto-a-ponto, não plataforma | Reclassificar para integração/middleware |
| "Queremos um site onde desenvolvedores baixam SDKs" | Portal de downloads, não API platform | Avaliar se é site estático com links |
| "A API não vai ter consumidores externos, é só interna" | API interna / microserviço | Reclassificar para web-app ou microservices-architecture |
| "Precisa de interface para o usuário final cadastrar dados" | Web app com API, não API-first | Reclassificar para web-app ou saas |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos quem vai consumir a API" | 01 | Sem consumidor definido, não há como projetar a DX | Identificar pelo menos 3 consumidores antes de iniciar o design |
| "O sistema backend ainda não está pronto" | 01 | API sem backend é interface sem implementação | Alinhar timeline de backend com timeline de API |
| "Não temos orçamento para API gateway" | 01 | Rate limiting e autenticação feitos na mão são inseguros e frágeis | Apresentar opções open-source (Kong, Tyk) e obter aprovação |
| "Cada parceiro quer o formato de resposta diferente" | 02 | API sem padronização é integração custom para cada consumidor | Definir formato único e documentar — exceções via content negotiation |
| "Não podemos garantir SLA" | 02 | Sem SLA, consumidores não baseiam negócio na API | Definir pelo menos SLA best-effort com métricas publicadas |
| "Os dados que a API expõe mudam de schema frequentemente" | 04 | Breaking changes constantes destroem confiança | Estabilizar schema antes de expor publicamente |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Temos 5 versões da API legada rodando" | 01 | Custo de manutenção de versões legadas consome equipe | Planejar sunset agressivo das versões mais antigas |
| "O time nunca construiu API pública antes" | 01 | API design e DX são skills diferentes de backend interno | Trazer consultor de API design ou fazer assessment de DX com dev externo |
| "O pricing vai ser definido pelo comercial depois" | 03 | Billing implementado sem pricing definido gera retrabalho | Definir pricing antes de implementar billing engine |
| "Não queremos limitar nossos parceiros com rate limiting" | 02 | Um parceiro com bug derruba a plataforma para todos | Rate limiting é proteção, não restrição — implementar com limites generosos |
| "A autenticação atual é token fixo no header" | 02 | Token fixo não rotaciona, não expira, não revoga — segurança frágil | Migrar para OAuth2 ou API key com rotação |
| "Webhooks são nice-to-have" | 04 | Sem webhooks, consumidores fazem polling — custo para ambos | Avaliar se polling é aceitável para os use cases ou se webhook é necessário |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Modelo de negócio da API definido (pergunta 1)
- Consumidores identificados com perfil (pergunta 2)
- Compromisso de retrocompatibilidade entendido pelo cliente (pergunta 4)
- Orçamento de desenvolvimento e operação aprovado (pergunta 6)
- Product owner da API definido (pergunta 15)

### Etapa 02 → 03

- Recursos e operações da API mapeados (pergunta 1)
- Modelo de autenticação definido (pergunta 3)
- Estratégia de versionamento definida (pergunta 6)
- Targets de performance e SLA definidos (pergunta 7)
- Necessidades de developer portal mapeadas (pergunta 15)

### Etapa 03 → 04

- Especificação OpenAPI tratada como contrato formal (pergunta 1)
- Política de breaking changes e depreciação definida (pergunta 2)
- Estratégia de sandbox definida (pergunta 5)
- Modelo de suporte a desenvolvedores definido (pergunta 4)
- Modelo de governança da API definido (pergunta 11)

### Etapa 04 → 05

- Especificação OpenAPI completa e aprovada (pergunta 1)
- Schema de erros padronizado definido (pergunta 2)
- Modelos de dados com formatos consistentes definidos (pergunta 3)
- Métricas de uso especificadas (pergunta 6)
- Especificação revisada por consumidor beta (pergunta 15)

### Etapa 05 → 06

- API Gateway escolhido com justificativa (pergunta 1)
- Arquitetura de backend definida (pergunta 2)
- Stack de segurança definida em camadas (pergunta 6)
- Custos mensais calculados e aprovados (pergunta 9)
- Ambientes documentados com isolamento (pergunta 14)

### Etapa 06 → 07

- Gateway configurado com autenticação e rate limiting em todos os ambientes (pergunta 1)
- Pipeline de CI/CD com contract tests operacional (pergunta 2)
- Sandbox funcional com dados fictícios (pergunta 3)
- Developer portal publicado com documentação (pergunta 4)
- Fluxo de onboarding testado end-to-end (pergunta 5)

### Etapa 07 → 08

- Todos os endpoints implementados e validados por contract tests (pergunta 1)
- Rate limiting implementado com precisão atômica (pergunta 3)
- Tratamento de erros padronizado em todos os endpoints (pergunta 4)
- Documentação do developer portal atualizada e gerada da spec (pergunta 6)
- Health check endpoint funcional (pergunta 13)

### Etapa 08 → 09

- Contract tests passando para todos os endpoints (pergunta 1)
- Load test com latência dentro do SLA (pergunta 2)
- Security testing executado cobrindo OWASP API Top 10 (pergunta 3)
- Consumidores beta validaram integração por ≥2 semanas (pergunta 4)
- Onboarding testado por externo com tempo target atingido (pergunta 6)

### Etapa 09 → 10

- Beta/early access executado com feedback incorporado (pergunta 1)
- Status page publicada e notificações testadas (pergunta 3)
- Plano de suporte ativado com SLA definido (pergunta 4)
- Plano de rollback documentado e testado (pergunta 5)
- Processo de incident response ensaiado (pergunta 15)

### Etapa 10 → Encerramento

- Acesso público ativado e consumidores fazendo requests (pergunta 1)
- Latência e error rate dentro do SLA com tráfego real (perguntas 3 e 4)
- Primeiros consumidores completaram onboarding com sucesso (pergunta 5)
- Comunicação proativa com consumidores realizada (pergunta 9)
- Aceite formal obtido e runbook entregue (perguntas 13 e 14)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de API platform. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Parceiros | V2 Pública + Portal | V3 Monetizada | V4 Gateway/Aggregation | V5 Dados/Open Data |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 3 | 2 | 2 |
| 02 Discovery | 2 | 4 | 4 | 3 | 3 |
| 03 Alignment | 2 | 4 | 5 | 2 | 2 |
| 04 Definition | 3 | 4 | 5 | 3 | 4 |
| 05 Architecture | 2 | 4 | 5 | 4 | 3 |
| 06 Setup | 2 | 4 | 4 | 3 | 2 |
| 07 Build | 3 | 4 | 5 | 4 | 3 |
| 08 QA | 2 | 4 | 4 | 3 | 3 |
| 09 Launch Prep | 1 | 3 | 4 | 2 | 2 |
| 10 Go-Live | 1 | 3 | 3 | 2 | 2 |
| **Total relativo** | **20** | **37** | **42** | **28** | **26** |

**Observações por variante:**

- **V1 Parceiros**: A variante mais leve. Sem developer portal público, sem billing, sem self-service. O esforço concentra-se na Definition (contrato robusto) e Build (endpoints sólidos). O risco principal é subestimar requisitos de SLA contratual.
- **V2 Pública + Portal**: Esforço alto e distribuído. Developer portal e DX consomem tanto esforço quanto o backend. Discovery e Alignment são pesados porque o design precisa servir consumidores desconhecidos. O gargalo oculto é a qualidade da documentação.
- **V3 Monetizada**: A variante mais pesada. Billing engine, metering preciso, pricing por plano, e compliance financeiro adicionam camadas de complexidade em todas as etapas. Alignment é o mais pesado (pricing, SLA contratual, termos de uso). Erros de billing destroem confiança — precisão é existencial.
- **V4 Gateway/Aggregation**: Pico na Architecture (roteamento, transformação, resiliência) e Build (circuit breaker, retry, timeout, transformação de payload). Discovery é moderado porque a API agrega o que já existe. O risco principal é performance — cada camada de agregação adiciona latência.
- **V5 Dados/Open Data**: Pico na Definition (queryability, filtros, paginação para datasets grandes) e QA (performance de queries pesadas, cache). Build é relativamente leve porque a maioria é read-only. O risco principal é performance degradada com dataset crescente.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| API gratuita sem monetização (Etapa 01, pergunta 9) | Etapa 03: pergunta 9 (planos e pricing). Etapa 04: perguntas 6 e 13 (métricas de uso por plano, permissions por plano). Etapa 05: pergunta 12 (metering e billing). Etapa 07: pergunta 12 (metering). Etapa 08: pergunta 14 (validação de billing). Etapa 09: pergunta 7 (teste de billing). |
| Sem webhooks (Etapa 02, pergunta 10) | Etapa 04: pergunta 4 (especificação de webhooks). Etapa 07: pergunta 9 (implementação de webhooks). Etapa 08: pergunta 9 (teste de webhooks). |
| API para parceiros controlados, sem developer portal público (V1) | Etapa 03: perguntas 3, 4 e 6 (DX, suporte self-service, onboarding automatizado). Etapa 04: perguntas 5 e 15 (SDKs, revisão por consumidor público). Etapa 06: perguntas 4, 5 e 12 (developer portal, self-service, status page pública). Etapa 08: pergunta 6 (teste de onboarding público). Etapa 09: perguntas 1 e 2 (beta público, comunicação marketing). |
| API não substitui versão anterior (Etapa 01, pergunta 10) | Etapa 03: pergunta 12 (migração de consumidores). Etapa 09: perguntas 6 e 11 (guia de migração, versão anterior como fallback). Etapa 10: pergunta 11 (migração de consumidores). |
| Formato único (apenas JSON), sem content negotiation (Etapa 04, pergunta 9) | Etapa 04: pergunta 9 perde profundidade (não precisa especificar múltiplos formatos). Etapa 07: simplifica implementação de serialization. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| API monetizada com billing por uso (Etapa 01, pergunta 9) | Etapa 03: pergunta 9 (pricing validado pelo financeiro) se torna gate. Etapa 04: pergunta 6 (métricas de uso) se torna gate. Etapa 05: pergunta 12 (arquitetura de metering) se torna gate. Etapa 07: pergunta 12 (metering preciso). Etapa 08: pergunta 14 (validação de billing). Etapa 09: pergunta 7 (teste end-to-end de billing). |
| SLA contratual com penalidades (Etapa 02, pergunta 7) | Etapa 05: perguntas 5 e 10 (monitoramento, zero-downtime deploy) se tornam gates. Etapa 06: pergunta 10 (monitoramento desde o setup). Etapa 09: pergunta 15 (dry run de incident response). Etapa 10: perguntas 3 e 4 (latência e error rate em produção). |
| API substitui versão anterior com consumidores ativos (Etapa 01, pergunta 10) | Etapa 03: pergunta 12 (plano de migração) se torna gate. Etapa 05: pergunta 11 (coexistência de versões). Etapa 09: perguntas 6 e 11 (guia de migração, versão antiga ativa). Etapa 10: pergunta 11 (monitoramento de migração). |
| Requisitos regulatórios — Open Banking, PSD2, LGPD (Etapa 01, pergunta 5) | Etapa 02: pergunta 13 (PII e consent) se torna gate. Etapa 03: pergunta 10 (SLA revisado pelo jurídico). Etapa 05: pergunta 6 (segurança em camadas) se torna gate. Etapa 06: pergunta 9 (isolamento de ambientes). Etapa 09: pergunta 12 (termos de uso aprovados). |
| Developer portal público com self-service (V2, V3, V5) | Etapa 03: perguntas 3 e 5 (DX target, sandbox) se tornam gates. Etapa 04: pergunta 5 (SDK strategy). Etapa 06: perguntas 4 e 5 (portal e onboarding). Etapa 08: pergunta 6 (teste de onboarding por externo). Etapa 09: perguntas 1 e 2 (beta e comunicação). |
| Webhooks habilitados (Etapa 02, pergunta 10) | Etapa 04: pergunta 4 (especificação formal) se torna gate. Etapa 07: pergunta 9 (implementação com retry e HMAC). Etapa 08: pergunta 9 (teste de failure scenarios). |
