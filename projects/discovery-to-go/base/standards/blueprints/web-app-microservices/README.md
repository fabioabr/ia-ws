---
title: "Web App com Microserviços — Blueprint"
description: "Frontend desacoplado de múltiplos serviços independentes. API Gateway ou BFF. Comunicação síncrona (REST/gRPC) e assíncrona (mensageria/EDA)."
category: project-blueprint
type: web-app-microservices
status: rascunho
created: 2026-04-13
---

# Web App com Microserviços

## Descrição

Frontend desacoplado de múltiplos serviços independentes. API Gateway ou BFF. Comunicação síncrona (REST/gRPC) e assíncrona (mensageria/EDA). Cada serviço tem seu próprio banco de dados, ciclo de deploy independente e ownership por squad. A complexidade operacional é significativamente maior que em monolitos, mas a escalabilidade independente e a autonomia de times justificam quando a organização e o domínio atingem determinado tamanho.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda arquitetura de microserviços é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — SaaS B2B Multi-tenant

Plataforma multi-tenant onde cada cliente (tenant) compartilha a mesma infraestrutura, com isolamento lógico por tenant em cada serviço. Requisitos pesados de isolamento de dados, controle de acesso por tenant, billing por uso, e configuração por cliente (feature flags, branding). O domínio de negócio é tipicamente complexo (ERP, CRM, HRM, Supply Chain) e evolui por squad autônomo. A fronteira entre serviços geralmente segue os bounded contexts do domínio. Exemplos: plataforma de gestão de projetos (Jira-like), plataforma de RH (Gupy-like), sistema de gestão escolar.

### V2 — Marketplace / Plataforma de Dois Lados

Plataforma que conecta dois grupos distintos (vendedores e compradores, motoristas e passageiros, prestadores e consumidores) com fluxos assimétricos para cada lado. Serviços de catálogo, busca, matching, pagamento, avaliação e notificação são tipicamente independentes. Comunicação assíncrona é dominante (pedidos, pagamentos, entregas geram eventos consumidos por múltiplos serviços). Requisitos pesados de consistência eventual, saga patterns para transações distribuídas, e busca avançada (Elasticsearch/Algolia). Exemplos: marketplace de serviços, plataforma de delivery, marketplace de produtos com múltiplos sellers.

### V3 — Plataforma de Dados / IoT

Sistema que ingere, processa e disponibiliza dados de múltiplas fontes — sensores IoT, integrações com APIs externas, uploads de arquivos, streams em tempo real. O foco é pipeline de dados (ingestão → processamento → armazenamento → visualização), com serviços especializados para cada etapa. A comunicação é predominantemente assíncrona via mensageria (Kafka, RabbitMQ). O frontend é tipicamente um dashboard com gráficos, mapas e alertas em tempo real (WebSocket/SSE). Exemplos: plataforma de telemetria de frota, monitoramento industrial, plataforma de analytics de marketing.

### V4 — Super App / Aplicação Composta

Aplicação que agrega múltiplos domínios de negócio sob uma mesma interface — financeiro, comunicação, produtividade, marketplace — cada domínio sendo um microserviço ou conjunto de microserviços. O BFF (Backend for Frontend) é obrigatório para orquestrar chamadas a múltiplos serviços por tela. Micro-frontends são frequentemente adotados para que cada squad controle seu domínio de UI. Requisitos pesados de performance de agregação, cache distribuído e experiência unificada apesar de backends fragmentados. Exemplos: super app de banco digital, app de ecossistema corporativo, plataforma de produtividade integrada.

### V5 — API Platform / Backend Headless

Plataforma que expõe APIs como produto — consumidas por clientes externos (parceiros, desenvolvedores terceiros) ou por múltiplos frontends internos (web, mobile, TV, chatbot). Não há um frontend único — o produto é a API. API Gateway com rate limiting, versionamento, documentação interativa (OpenAPI/Swagger), developer portal e billing por consumo são componentes centrais. Cada microserviço atende um recurso ou domínio da API. Exemplos: plataforma de pagamentos (Stripe-like), plataforma de comunicação (Twilio-like), plataforma de dados geográficos.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend / Services | API Gateway | Mensageria | Infra / Deploy | Observações |
|---|---|---|---|---|---|---|
| V1 — SaaS B2B | Next.js ou React SPA | Node.js (NestJS) ou Go | Kong ou AWS API Gateway | RabbitMQ ou SQS | Kubernetes (EKS/GKE) ou ECS | Tenant isolation por header/JWT. Feature flags por tenant. |
| V2 — Marketplace | Next.js (SSR) | Node.js + Python (ML matching) | Kong ou Envoy | Kafka ou RabbitMQ | Kubernetes + Helm | Saga pattern para transações distribuídas. Elasticsearch para busca. |
| V3 — Dados/IoT | React + Grafana embeds | Go ou Rust (ingestão) + Python (processamento) | Envoy ou NGINX | Kafka obrigatório | Kubernetes + Flink/Spark | Time-series DB (TimescaleDB, InfluxDB). Volume de dados define stack. |
| V4 — Super App | Micro-frontends (Module Federation) | NestJS ou Spring Boot | BFF customizado + API Gateway | Kafka ou NATS | Kubernetes com service mesh (Istio/Linkerd) | BFF obrigatório. Cache distribuído (Redis) crítico. |
| V5 — API Platform | Developer Portal (Docusaurus/Redoc) | Go ou Node.js | Kong ou Apigee | SQS ou Kafka | ECS ou Kubernetes | Rate limiting, versionamento de API e billing são features core. |

---

## Etapa 01 — Inception

- **Origem da demanda e maturidade organizacional**: A decisão de adotar microserviços frequentemente nasce de dor real com um monolito existente (deploys arriscados, times pisando no código um do outro, impossibilidade de escalar componentes individualmente) ou de um requisito de negócio que exige autonomia de times desde o início (múltiplas squads trabalhando em paralelo com ciclos de release independentes). Entender o gatilho é crucial porque microserviços adotados prematuramente — antes que a complexidade do domínio e o tamanho do time justifiquem — geram overhead operacional que consome mais recursos do que o monolito que pretendiam substituir.

- **Estrutura organizacional como pré-requisito**: A Lei de Conway é especialmente relevante aqui — a arquitetura de microserviços só funciona quando a organização tem times independentes com ownership claro sobre domínios de negócio. Se a organização tem um time de backend, um time de frontend e um time de QA (organização funcional), microserviços vão gerar mais fricção entre times do que resolver. A organização precisa ter ou estar migrando para squads cross-funcionais (dev + QA + product) com ownership de domínio. Mapear a estrutura organizacional é tão importante quanto mapear a arquitetura técnica.

- **Custo operacional como decisão consciente**: Microserviços multiplicam o custo de infraestrutura e operação — cada serviço precisa de CI/CD, monitoramento, logging, alertas, banco de dados, e possivelmente sua própria instância de cache. O custo de uma plataforma com 10 microserviços em Kubernetes pode facilmente ultrapassar $5.000-15.000/mês em cloud, comparado a $500-2.000/mês para um monolito equivalente. Esse custo precisa ser apresentado ao stakeholder de negócio na Inception para que a decisão seja informada, não uma surpresa pós-go-live.

- **Domínio de negócio mapeado e bounded contexts identificados**: Microserviços sem Domain-Driven Design são distribuição aleatória de código em containers. Os bounded contexts do domínio (áreas de negócio com linguagem ubíqua própria e fronteiras claras) devem estar pelo menos rascunhados antes de definir a fronteira dos serviços. Se o domínio de negócio ainda não está claro — se o cliente não consegue descrever os principais processos e suas interdependências — a adoção de microserviços é prematura e perigosa.

- **Expectativa de escala e performance**: Entender se a motivação inclui escalabilidade horizontal (mais instâncias do mesmo serviço para absorver carga) ou se é puramente organizacional (autonomia de deploys). Se a motivação é escala, quais componentes específicos precisam escalar independentemente — o serviço de busca recebe 100x mais tráfego que o serviço de billing? O serviço de ingestão de dados precisa absorver picos de 10.000 eventos/segundo? Sem requisitos de escala concretos, a justificativa "precisa escalar" é vaga e não sustenta a complexidade adicional.

- **Experiência do time com sistemas distribuídos**: Microserviços exigem maturidade técnica significativa — debugging distribuído, tracing, eventual consistency, circuit breakers, retry policies, idempotência. Um time que nunca trabalhou com comunicação assíncrona, sagas ou distributed tracing vai enfrentar uma curva de aprendizado íngreme que impacta diretamente o prazo e a qualidade das primeiras entregas. Se o time é junior, considerar seriamente começar com monolito modular e migrar para microserviços quando a maturidade permitir.

### Perguntas

1. Qual é o gatilho real para adotar microserviços — dor com monolito existente, requisito de escala, autonomia de times, ou decisão top-down? [fonte: CTO, Tech Lead, Diretoria] [impacto: Arquiteto, PM, Dev]
2. A organização tem ou planeja ter squads cross-funcionais com ownership de domínio, ou a estrutura é funcional (backend/frontend/QA separados)? [fonte: CTO, VP Engineering, RH] [impacto: Arquiteto, PM]
3. Qual é o orçamento mensal disponível para infraestrutura cloud, considerando que microserviços multiplicam custos de operação? [fonte: Financeiro, CTO, Diretoria] [impacto: DevOps, Arquiteto, PM]
4. Os bounded contexts do domínio de negócio foram identificados — o cliente consegue descrever os processos principais e suas fronteiras? [fonte: Product Owner, Especialista de domínio, Diretoria] [impacto: Arquiteto, Dev]
5. Quantos serviços são previstos para o MVP e qual é a projeção para 12 meses após o go-live? [fonte: CTO, Tech Lead] [impacto: Arquiteto, DevOps, PM]
6. Existe um monolito legado que será decomposto ou o sistema será construído do zero como microserviços? [fonte: CTO, TI] [impacto: Arquiteto, Dev, PM]
7. Qual é o nível de experiência do time com sistemas distribuídos (tracing, sagas, mensageria, eventual consistency)? [fonte: Tech Lead, CTO] [impacto: Arquiteto, Dev, PM]
8. Quais são os requisitos concretos de escala — picos de tráfego esperados, volume de dados, concorrência de usuários simultâneos? [fonte: Produto, Comercial, TI] [impacto: Arquiteto, DevOps]
9. Quem é o patrocinador executivo do projeto e quem tem poder de decisão sobre trade-offs técnicos vs. prazos? [fonte: Diretoria, CTO] [impacto: PM, Arquiteto]
10. Existe prazo de go-live vinculado a evento de negócio (lançamento comercial, migração de contrato, deadline regulatório)? [fonte: Comercial, Diretoria] [impacto: PM, Dev]
11. O cliente tem preferência ou restrição por cloud provider (AWS, GCP, Azure) ou existe vendor lock-in com contratos vigentes? [fonte: TI, Financeiro, Compras] [impacto: DevOps, Arquiteto]
12. Há requisitos regulatórios ou de compliance que impactam a localização de dados, criptografia ou auditoria (LGPD, SOC2, PCI-DSS)? [fonte: Jurídico, DPO, Compliance] [impacto: Arquiteto, DevOps, Dev]
13. Quantos times/squads vão trabalhar em paralelo no sistema e qual o modelo de coordenação entre eles? [fonte: CTO, VP Engineering] [impacto: Arquiteto, PM]
14. O domínio DNS, certificados SSL e ambientes cloud já estão provisionados e acessíveis ao time de desenvolvimento? [fonte: TI, DevOps] [impacto: DevOps, Dev]
15. Existem sistemas legados com os quais os microserviços precisarão se integrar desde o MVP (ERPs, CRMs, gateways de pagamento)? [fonte: TI, Produto, Comercial] [impacto: Arquiteto, Dev]

---

## Etapa 02 — Discovery

- **Mapeamento de domínios e subdomínios**: Levantar todos os domínios de negócio envolvidos e decompor em subdomínios — core (diferencial competitivo, justifica investimento custom), supporting (necessário mas não diferencial), e generic (commodity, pode usar soluções prontas como auth, billing, notificações). Essa classificação é fundamental porque define onde investir esforço de desenvolvimento interno versus onde adotar serviços gerenciados. Um marketplace que constrói seu próprio sistema de autenticação do zero está desperdiçando esforço que deveria ir para o core domain (matching, busca, transações).

- **Fluxos de negócio end-to-end**: Mapear os processos de negócio completos — do gatilho inicial à conclusão — identificando quais serviços participam de cada fluxo e como se comunicam. Exemplo em marketplace: "Comprador busca produto → Serviço de Busca → Comprador adiciona ao carrinho → Serviço de Carrinho → Comprador finaliza pedido → Serviço de Pedidos → Notifica Vendedor → Serviço de Notificações → Vendedor aceita → Serviço de Fulfillment → Pagamento capturado → Serviço de Pagamento". Cada transição entre serviços é um ponto de falha que precisa de tratamento (retry, compensação, dead letter queue).

- **Requisitos de consistência de dados**: Identificar quais fluxos exigem consistência forte (transações financeiras onde débito e crédito devem ser atômicos) versus consistência eventual (atualização de feed de atividades, recálculo de ranking). Em microserviços, transações distribuídas são o desafio número um — cada serviço tem seu próprio banco e não há transação ACID cross-service. Fluxos que exigem consistência forte precisam de padrões como Saga (orquestrada ou coreografada) ou Outbox Pattern. A decisão de consistência por fluxo impacta diretamente a complexidade de implementação.

- **Requisitos não-funcionais por serviço**: Levantar RNFs específicos por serviço — não genéricos para o sistema todo. O serviço de busca pode precisar de latência <100ms com 99th percentile, enquanto o serviço de relatórios pode tolerar 5s. O serviço de ingestão de IoT pode precisar absorver 50.000 eventos/segundo, enquanto o serviço de configuração recebe 10 requests/minuto. RNFs genéricos ("o sistema deve ser rápido") são inúteis — RNFs por serviço permitem dimensionar infraestrutura e escolher tecnologias adequadas para cada um.

- **Integrações com sistemas externos**: Mapear todas as integrações externas — gateways de pagamento (Stripe, PagSeguro, Mercado Pago), provedores de e-mail (SendGrid, SES), serviços de SMS (Twilio, Zenvia), ERPs (SAP, TOTVS), CRMs (Salesforce, HubSpot), e APIs de parceiros. Cada integração é candidata a um serviço dedicado (anti-corruption layer) ou a ser encapsulada dentro do serviço de domínio correspondente. Integrações com sistemas legados que não oferecem API moderna (apenas SOAP, FTP, banco compartilhado) exigem adaptadores e são fontes frequentes de atraso.

- **Requisitos de observabilidade e auditoria**: Em sistemas distribuídos, a ausência de observabilidade centralizada torna o debugging impossível na prática. Levantar se há requisitos explícitos de distributed tracing (acompanhar uma request do frontend até o último microserviço), logging centralizado com correlação por request-id, métricas de negócio em real-time (pedidos/minuto, receita/hora), e trilha de auditoria para compliance (quem fez o quê, quando, em qual serviço). Requisitos de auditoria regulatória (PCI-DSS, SOC2, LGPD) podem exigir retenção de logs por período específico e imutabilidade.

### Perguntas

1. Quais são os domínios core do negócio (diferencial competitivo) versus os supporting e generic (commodity)? [fonte: Product Owner, Diretoria, Especialista de domínio] [impacto: Arquiteto, Dev]
2. Os fluxos de negócio end-to-end foram mapeados com os serviços participantes e os eventos trocados entre eles? [fonte: Product Owner, Analista de negócio] [impacto: Arquiteto, Dev]
3. Quais fluxos exigem consistência forte (transações atômicas) e quais toleram consistência eventual? [fonte: Product Owner, Financeiro] [impacto: Arquiteto, Dev]
4. Os requisitos não-funcionais foram definidos por serviço (latência, throughput, disponibilidade) ou apenas de forma genérica? [fonte: TI, Produto, SRE] [impacto: Arquiteto, DevOps]
5. Quais integrações externas são obrigatórias no MVP (pagamento, e-mail, SMS, ERP, CRM, APIs de parceiros)? [fonte: TI, Comercial, Produto] [impacto: Dev, Arquiteto]
6. Existe requisito de auditoria ou compliance que exija rastreabilidade de ações por usuário em cada serviço (LGPD, SOC2, PCI-DSS)? [fonte: Jurídico, DPO, Compliance] [impacto: Arquiteto, Dev, DevOps]
7. Quantos tipos de usuário existem no sistema e quais são os fluxos críticos de cada um? [fonte: Produto, UX] [impacto: Dev, Arquiteto]
8. Há requisitos de multi-tenancy — cada cliente vê apenas seus dados e pode ter configurações customizadas? [fonte: Produto, Comercial] [impacto: Arquiteto, Dev]
9. Qual é o volume esperado de dados por serviço no primeiro ano (registros, tamanho de storage, crescimento mensal)? [fonte: Produto, TI] [impacto: Arquiteto, DevOps]
10. Existem requisitos de processamento em tempo real (streaming, eventos, WebSocket) ou batch (relatórios, ETL) é suficiente? [fonte: Produto, Analista de dados] [impacto: Arquiteto, Dev]
11. O sistema precisa funcionar em múltiplas regiões geográficas com replicação de dados entre regiões? [fonte: Comercial, Jurídico, TI] [impacto: Arquiteto, DevOps]
12. Quais métricas de negócio precisam ser monitoradas em real-time (pedidos/minuto, receita, erros de transação)? [fonte: Produto, Diretoria] [impacto: DevOps, Dev]
13. Há requisitos de internacionalização (múltiplos idiomas, moedas, fusos horários) no MVP ou futuro próximo? [fonte: Comercial, Produto] [impacto: Dev, Arquiteto]
14. Quais dados são sensíveis e precisam de criptografia at-rest e in-transit separada do restante? [fonte: DPO, Jurídico, TI] [impacto: Arquiteto, DevOps]
15. Existe equipe de SRE/DevOps dedicada ou o time de desenvolvimento será responsável por operar os serviços em produção? [fonte: CTO, VP Engineering] [impacto: DevOps, PM, Dev]

---

## Etapa 03 — Alignment

- **Ownership de serviços por squad**: Definir formalmente qual squad é responsável por qual serviço ou conjunto de serviços. O modelo ideal é que cada squad tenha ownership completo (desenvolvimento, deploy, monitoramento, incidentes) dos serviços no seu bounded context. Se uma squad precisa alterar código em serviço de outra squad para implementar uma feature, a fronteira dos serviços está errada — ou o modelo de ownership precisa prever inner-source com code review obrigatório. Documentar a matriz de ownership e os canais de comunicação entre squads.

- **Contratos de API entre serviços**: Alinhar o formato dos contratos de API (REST com OpenAPI spec, gRPC com Protobuf, GraphQL com schema) e o processo de versionamento. Mudanças breaking em APIs internas são a causa número um de incidentes em arquiteturas de microserviços — um serviço muda seu contrato e os consumidores quebram silenciosamente. O padrão recomendado é consumer-driven contracts testados em CI (Pact ou similar), versionamento semântico de APIs, e período de deprecação documentado para mudanças breaking.

- **Modelo de comunicação: síncrona vs. assíncrona**: Alinhar quais fluxos usam comunicação síncrona (REST/gRPC — request-response, acoplamento temporal) e quais usam assíncrona (mensageria — fire-and-forget ou pub/sub, desacoplamento temporal). A regra geral é: consultas e operações que precisam de resposta imediata para o frontend usam síncrona; operações que iniciam processos de negócio com múltiplas etapas (pedidos, pagamentos, workflows) usam assíncrona. O alinhamento deve ser feito por fluxo, não como decisão global.

- **Estratégia de dados: database per service**: Alinhar e obter buy-in do time e do cliente sobre o princípio de database-per-service — cada microserviço tem seu próprio banco de dados, inacessível diretamente por outros serviços. Dados compartilhados entre serviços são obtidos via API ou eventos, nunca por acesso direto ao banco alheio. Esse princípio é frequentemente o mais difícil de aceitar para times vindos de monolitos com banco compartilhado, e violá-lo destrói os benefícios de deploy independente. Decisões sobre tipo de banco por serviço (PostgreSQL, MongoDB, Redis, DynamoDB) devem considerar o padrão de acesso de cada domínio.

- **Padrão de autenticação e autorização distribuída**: Alinhar como a identidade do usuário flui entre serviços — tipicamente JWT propagado via header, validado em cada serviço (ou no API Gateway centralmente). Definir se a autorização é centralizada (gateway decide quem acessa o quê) ou descentralizada (cada serviço valida suas próprias permissões com base nas claims do JWT). O modelo de permissões deve ser desenhado antes do build — adicionar RBAC ou ABAC depois que os serviços já estão implementados é custoso e propenso a falhas de segurança.

- **SLA de disponibilidade e modelo de on-call**: Alinhar o SLA de disponibilidade esperado (99.9% = ~8.7h downtime/ano, 99.95% = ~4.4h/ano, 99.99% = ~52min/ano) e o modelo de resposta a incidentes. Em microserviços, a disponibilidade composta do sistema é o produto das disponibilidades individuais — 10 serviços com 99.9% cada resultam em disponibilidade composta de ~99%. Isso significa que o SLA por serviço precisa ser mais alto que o SLA desejado do sistema. Definir quem responde a incidentes (on-call rotation por squad ou SRE centralizado), escalation paths, e runbooks para os cenários mais prováveis.

### Perguntas

1. A matriz de ownership de serviços por squad foi definida formalmente e cada squad concorda com sua responsabilidade? [fonte: CTO, Tech Lead, VP Engineering] [impacto: Arquiteto, PM]
2. O formato dos contratos de API entre serviços foi padronizado (REST+OpenAPI, gRPC+Protobuf, GraphQL) com versionamento? [fonte: Tech Lead, Arquiteto] [impacto: Dev]
3. Há estratégia definida de consumer-driven contract testing entre serviços (Pact ou similar)? [fonte: Tech Lead, QA] [impacto: Dev, QA]
4. O modelo de comunicação (síncrona vs. assíncrona) foi decidido por fluxo de negócio, não de forma genérica? [fonte: Arquiteto, Product Owner] [impacto: Dev, Arquiteto]
5. O princípio de database-per-service foi aceito e entendido por todo o time, incluindo as implicações de consistência eventual? [fonte: CTO, Tech Lead] [impacto: Dev, Arquiteto]
6. A estratégia de autenticação e autorização distribuída foi desenhada (JWT, propagação de identidade, RBAC/ABAC por serviço)? [fonte: Arquiteto, Security] [impacto: Dev, Arquiteto]
7. O SLA de disponibilidade do sistema foi definido e decomposto em SLA por serviço considerando a disponibilidade composta? [fonte: Produto, Diretoria, SRE] [impacto: DevOps, Arquiteto]
8. O modelo de resposta a incidentes foi definido (on-call rotation, escalation path, runbooks)? [fonte: CTO, SRE, VP Engineering] [impacto: DevOps, Dev]
9. Os ambientes (dev, staging, produção) foram definidos e isolados, com estratégia de paridade entre eles? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
10. O processo de code review e merge entre squads foi definido (inner-source, PR obrigatório, ownership boundaries)? [fonte: Tech Lead, CTO] [impacto: Dev, PM]
11. As dependências externas críticas (cloud provider, SaaS, APIs de parceiros) foram mapeadas com SLAs documentados? [fonte: TI, Compras, Fornecedores] [impacto: Arquiteto, DevOps]
12. O modelo de branching e release por serviço foi alinhado (trunk-based, GitFlow, release trains)? [fonte: Tech Lead, DevOps] [impacto: Dev, DevOps]
13. A estratégia de feature flags foi definida para deploys independentes sem breaking changes visíveis ao usuário? [fonte: Produto, Tech Lead] [impacto: Dev, PM]
14. O orçamento de infraestrutura cloud foi aprovado com projeção de 12 meses e cenários de pico? [fonte: Financeiro, CTO, Diretoria] [impacto: DevOps, PM]
15. O cliente entende que mudanças arquiteturais após o Build (adicionar/remover serviços, mudar fronteiras) têm impacto significativo em prazo e custo? [fonte: Diretoria, CTO] [impacto: PM, Arquiteto]

---

## Etapa 04 — Definition

- **Mapa de serviços e fronteiras**: Produzir o diagrama de arquitetura com todos os serviços do MVP, suas responsabilidades, os bancos de dados de cada um, e as interfaces de comunicação (APIs síncronas, tópicos/filas assíncronas). Cada serviço deve ter nome, ownership (squad), responsabilidade em uma frase, API pública documentada, e eventos que produz/consome. Esse mapa é o artefato central do projeto — todas as decisões de implementação, deploy e monitoramento derivam dele. Um serviço sem fronteira clara de responsabilidade vai acumular lógica e virar um mini-monolito.

- **Modelagem de dados por serviço**: Para cada serviço, definir o schema do banco de dados com entidades, relacionamentos e índices necessários. A escolha do tipo de banco (relacional, documento, time-series, grafo, key-value) deve ser justificada pelo padrão de acesso predominante — não por preferência do dev. Serviço de catálogo com busca full-text → Elasticsearch. Serviço de sessão com acesso key-value de altíssima performance → Redis. Serviço financeiro com transações ACID → PostgreSQL. Definir também a estratégia de migração de schema (Flyway, Prisma Migrate, Atlas) para cada serviço.

- **Contratos de API detalhados**: Para cada API pública de cada serviço, documentar: endpoints (verbo HTTP + path + path params + query params), request body (schema JSON com tipos, obrigatórios, validações), response body (schema JSON para 200 e para cada erro possível), headers obrigatórios (Authorization, X-Tenant-ID, X-Request-ID), e códigos HTTP esperados com semântica. Se gRPC, os arquivos .proto devem ser escritos nesta fase. Se mensageria, documentar o schema de cada evento (nome do evento, payload, metadata). Contratos documentados antes do build permitem desenvolvimento paralelo de serviços — cada squad implementa contra o contrato, não contra a implementação do outro.

- **Definição de sagas e fluxos distribuídos**: Para cada fluxo de negócio que envolve mais de um serviço com consistência transacional, documentar a saga: sequência de passos, serviço responsável por cada passo, ação de compensação em caso de falha em cada passo, e estado final esperado (sucesso e cada cenário de falha). Decidir entre saga orquestrada (um orchestrator coordena os passos) e saga coreografada (cada serviço reage a eventos e emite o próximo). Sagas mal documentadas são a principal causa de bugs em microserviços — estados inconsistentes que só aparecem em cenários de falha parcial.

- **Modelo de permissões e multi-tenancy**: Definir o modelo de autorização: quais roles existem, quais permissões cada role tem, como as permissões são avaliadas por serviço (middleware de autorização, policy engine como OPA/Casbin). Para sistemas multi-tenant, definir a estratégia de isolamento: shared database com tenant_id em cada tabela (mais barato, menos isolamento), schema-per-tenant (isolamento médio, complexidade de migration), database-per-tenant (isolamento máximo, custo maior). A decisão de isolamento impacta diretamente a complexidade de queries, backups e operações.

- **Especificação de observabilidade**: Definir os padrões de observabilidade antes do build — não como adição posterior. Distributed tracing: header de correlação (trace-id) propagado entre todos os serviços via middleware automático. Logging: formato estruturado (JSON), campos obrigatórios por log entry (timestamp, service, trace-id, level, message), destino centralizado (ELK, Grafana Loki, Datadog). Métricas: métricas de infraestrutura (CPU, memória, network) + métricas de negócio (pedidos/minuto, latência P99 por endpoint) + alertas com thresholds definidos. Dashboards por serviço e dashboard de sistema.

### Perguntas

1. O mapa de serviços do MVP foi produzido com nome, ownership, responsabilidade, API e eventos de cada serviço? [fonte: Arquiteto, Tech Lead] [impacto: Dev, PM]
2. O schema de banco de dados de cada serviço foi modelado com justificativa para o tipo de banco escolhido? [fonte: Arquiteto, Dev] [impacto: Dev]
3. Os contratos de API de cada serviço foram documentados com request/response schemas, headers e códigos de erro? [fonte: Arquiteto, Dev] [impacto: Dev]
4. Cada saga/fluxo distribuído foi documentado com passos, serviços envolvidos, compensações e cenários de falha? [fonte: Arquiteto, Product Owner] [impacto: Dev, QA]
5. O modelo de permissões (RBAC/ABAC) foi especificado com roles, permissões e mecanismo de avaliação por serviço? [fonte: Produto, Security, Arquiteto] [impacto: Dev]
6. A estratégia de multi-tenancy foi definida com nível de isolamento e justificativa de custo/segurança? [fonte: Arquiteto, Produto, Financeiro] [impacto: Dev, DevOps]
7. Os padrões de observabilidade foram especificados (tracing, logging estruturado, métricas, alertas) antes do início do build? [fonte: SRE, Arquiteto] [impacto: Dev, DevOps]
8. A estratégia de migração de schema por serviço foi definida (ferramenta, processo de versionamento, rollback)? [fonte: Tech Lead, Dev] [impacto: Dev]
9. Os eventos assíncronos foram documentados com schema, metadata e política de retry/dead-letter? [fonte: Arquiteto, Dev] [impacto: Dev]
10. A estratégia de versionamento de API foi definida (URL path, header, query param) com política de deprecação? [fonte: Arquiteto, Tech Lead] [impacto: Dev]
11. Os critérios de split de serviços foram documentados para evitar micro-serviços granulares demais ou macro-serviços vagos? [fonte: Arquiteto] [impacto: Dev, Arquiteto]
12. O capacity planning inicial foi feito por serviço (instâncias, CPU, memória, storage) baseado nos RNFs da Discovery? [fonte: SRE, Arquiteto, DevOps] [impacto: DevOps]
13. Os endpoints de health check, readiness e liveness foram especificados para cada serviço? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
14. O modelo de rate limiting e throttling foi definido por endpoint ou por serviço com thresholds documentados? [fonte: Arquiteto, Security] [impacto: Dev, DevOps]
15. A documentação de Definition foi revisada e aprovada por todos os tech leads de squad antes de iniciar o Setup? [fonte: CTO, Tech Leads] [impacto: PM, Dev, Arquiteto]

---

## Etapa 05 — Architecture

- **API Gateway e BFF**: O API Gateway é o ponto de entrada único para todos os requests externos. Ele gerencia roteamento, autenticação, rate limiting, e transformação de protocolos. Kong (open-source, extensível via plugins Lua), AWS API Gateway (serverless, integração nativa com AWS), e Envoy (alto desempenho, base do Istio) são as opções mais maduras. Se o frontend precisa agregar dados de múltiplos serviços em uma única chamada, um BFF (Backend for Frontend) é necessário — ele orquestra chamadas paralelas aos microserviços e compõe a resposta para o frontend, evitando que o frontend faça N chamadas sequenciais.

- **Service mesh e comunicação inter-serviços**: Para comunicação entre serviços, a decisão é entre comunicação direta (serviço A chama serviço B via DNS interno + load balancer) e service mesh (Istio, Linkerd, Consul Connect — proxy sidecar em cada pod que gerencia mTLS, retries, circuit breaking, observabilidade automaticamente). Service mesh adiciona overhead de latência (~1-5ms por hop) e complexidade operacional, mas elimina a necessidade de implementar retry, circuit breaker e mTLS no código de cada serviço. Recomendado quando há mais de 10 serviços em produção ou quando os requisitos de segurança exigem mTLS universal.

- **Mensageria e event streaming**: A escolha entre message broker (RabbitMQ, SQS) e event streaming (Kafka, Redpanda, Pulsar) depende do padrão de uso. RabbitMQ é ideal para job queues e request-response assíncrono — mensagem consumida e removida. Kafka é ideal para event sourcing, event-driven architecture e cenários onde múltiplos consumidores precisam ler o mesmo stream de eventos independentemente (cada consumer group mantém seu offset). Se o projeto usa Saga coreografada, Kafka é geralmente a melhor escolha por permitir replay de eventos. O custo de operar Kafka (cluster de 3+ brokers, ZooKeeper/KRaft, monitoramento) é significativamente maior que RabbitMQ — considerar serviços gerenciados (Amazon MSK, Confluent Cloud) para reduzir overhead operacional.

- **Orquestração de containers**: Kubernetes é o padrão de facto para orquestrar microserviços em produção — gerencia deploy, scaling, healing, networking e service discovery. Opções gerenciadas (EKS, GKE, AKS) eliminam o overhead de manter o control plane. Para projetos menores (3-5 serviços), ECS (AWS) ou Cloud Run (GCP) oferecem orquestração mais simples com menor curva de aprendizado e custo operacional. Docker Compose é aceitável apenas para desenvolvimento local — nunca para produção de microserviços. A escolha deve considerar o tamanho do time de DevOps — Kubernetes sem engenheiro dedicado é receita para incidentes.

- **CI/CD por serviço**: Cada microserviço deve ter seu próprio pipeline de CI/CD independente — push no repositório do serviço A dispara build, testes e deploy apenas do serviço A, sem afetar os demais. Monorepo com pipelines filtrados (build apenas o que mudou) ou polyrepo (cada serviço em seu repositório) são as duas abordagens principais. Monorepo simplifica compartilhamento de código e contratos mas complica o CI (precisa de build path detection). Polyrepo garante isolamento total mas complica sincronização de breaking changes entre serviços. A decisão deve considerar o número de squads e o grau de acoplamento entre serviços.

- **Estratégia de banco de dados e persistência**: Definir por serviço qual engine de banco de dados será usada e como será provisionada. Bancos gerenciados (RDS, Cloud SQL, DocumentDB, ElastiCache) são recomendados para produção — eliminam backup, patching e failover manual. Para Kubernetes, bancos dentro do cluster (StatefulSets) são aceitáveis em desenvolvimento mas arriscados em produção sem operadores dedicados (CloudNativePG, Percona Operator). Estratégia de backup, retenção, point-in-time recovery e disaster recovery deve ser definida aqui — não após o primeiro incidente de perda de dados.

- **Segurança inter-serviços**: Em microserviços, a superfície de ataque é multiplicada — cada serviço expõe endpoints, e a rede interna não pode ser considerada segura (zero-trust). Definir: mTLS entre todos os serviços (automático via service mesh ou manual via certificados), validação de JWT em cada serviço (não apenas no gateway), secrets management (HashiCorp Vault, AWS Secrets Manager, Kubernetes Secrets com encryption at rest), e network policies no Kubernetes (restringir quais pods podem se comunicar). Vulnerabilidades em um serviço não devem permitir lateral movement para outros serviços.

### Perguntas

1. O API Gateway foi escolhido considerando os requisitos de roteamento, autenticação, rate limiting e transformação de protocolos? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
2. Foi decidido se o projeto precisa de BFF — e se sim, qual serviço o implementa e quais agregações ele faz? [fonte: Arquiteto, Frontend Lead] [impacto: Dev]
3. A decisão entre comunicação direta e service mesh foi tomada com base no número de serviços e requisitos de segurança? [fonte: Arquiteto, DevOps] [impacto: DevOps, Dev]
4. O broker de mensageria foi escolhido (RabbitMQ vs. Kafka vs. gerenciado) com justificativa baseada nos padrões de consumo? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
5. A plataforma de orquestração de containers foi definida (Kubernetes gerenciado, ECS, Cloud Run) considerando o tamanho do time de DevOps? [fonte: CTO, DevOps] [impacto: DevOps, Dev]
6. A estratégia de CI/CD por serviço foi desenhada — monorepo com path filtering ou polyrepo com pipelines independentes? [fonte: Tech Lead, DevOps] [impacto: Dev, DevOps]
7. O tipo de banco de dados por serviço foi definido e justificado pelo padrão de acesso do domínio? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
8. A estratégia de backup, retenção e disaster recovery foi definida por serviço com RPO e RTO documentados? [fonte: SRE, Arquiteto, DevOps] [impacto: DevOps]
9. A segurança inter-serviços foi desenhada (mTLS, validação JWT distribuída, network policies, secrets management)? [fonte: Security, Arquiteto] [impacto: Dev, DevOps]
10. O modelo de deploy (rolling update, blue-green, canary) foi definido por serviço ou padronizado para todos? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
11. Os custos mensais de infraestrutura foram calculados por serviço em cenário normal e pior caso (pico de Black Friday)? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
12. A estratégia de cache distribuído (Redis, Memcached) foi definida por serviço com TTL, invalidação e fallback documentados? [fonte: Arquiteto, Dev] [impacto: Dev]
13. O modelo de logging centralizado e distributed tracing foi escolhido (ELK, Grafana Stack, Datadog) com custo projetado? [fonte: SRE, DevOps, Financeiro] [impacto: DevOps, Dev]
14. A estratégia de auto-scaling por serviço foi definida com métricas de trigger (CPU, requests/s, queue depth)? [fonte: DevOps, Arquiteto] [impacto: DevOps]
15. A arquitetura foi documentada em ADRs (Architecture Decision Records) e aprovada por todos os tech leads? [fonte: CTO, Tech Leads, Arquiteto] [impacto: Dev, Arquiteto]

---

## Etapa 06 — Setup

- **Provisionamento de infraestrutura como código**: Toda a infraestrutura deve ser provisionada via IaC (Terraform, Pulumi, AWS CDK) — nunca por click-ops no console do cloud provider. Isso inclui: VPC e subnets, cluster Kubernetes ou ECS, bancos de dados gerenciados, brokers de mensageria, load balancers, registros DNS, certificados SSL, e políticas de IAM. IaC garante que os ambientes (dev, staging, prod) são idênticos e reproduzíveis, e que mudanças de infraestrutura passam por code review e versionamento. O primeiro setup é mais lento que click-ops, mas elimina o "funciona no meu ambiente" e permite disaster recovery em horas ao invés de dias.

- **Pipeline de CI/CD configurado por serviço**: Para cada microserviço, configurar: build (compilação, testes unitários, lint, security scan), containerização (Dockerfile otimizado com multi-stage build, imagem base slim), push para container registry (ECR, GCR, Docker Hub), e deploy automatizado para staging (a cada merge na branch principal). GitHub Actions, GitLab CI ou CircleCI são as opções mais comuns. Cada pipeline deve rodar em menos de 10 minutos — pipelines lentos incentivam o time a skipar CI, que é o caminho para bugs em produção.

- **Repositório e monorepo vs. polyrepo**: Se monorepo, configurar a detecção de mudanças por path (Nx, Turborepo, ou filtros no CI) para que mudanças no serviço A não disparem build do serviço B. Configurar workspaces (npm/pnpm/yarn) para compartilhamento de código (contratos, types, utils) sem publicação em registry. Se polyrepo, criar repositórios separados, configurar links entre eles para shared libraries (submodules, packages publicados em registry privado), e documentar o processo de sincronização de contratos. A decisão de mono vs. poly deve estar tomada na Etapa 05.

- **Ambientes isolados e variáveis de configuração**: Configurar no mínimo 3 ambientes: dev (para experimentação, pode ser instável), staging (réplica de produção para QA e validação final), e production. Cada ambiente deve ter suas próprias instâncias de banco, broker, e configurações — nunca compartilhar recursos entre ambientes. Variáveis de ambiente gerenciadas via Kubernetes Secrets (com encryption at rest), AWS Systems Manager Parameter Store, ou HashiCorp Vault. Documentar todas as variáveis necessárias para cada serviço em um template .env.example no repositório.

- **Observabilidade configurada desde o primeiro deploy**: Configurar a stack de observabilidade antes de escrever código de negócio. Distributed tracing (Jaeger, Zipkin ou OTEL Collector → Grafana Tempo), logging centralizado (Fluent Bit → Grafana Loki ou Elasticsearch), e métricas (Prometheus → Grafana ou Datadog). Instrumentar o primeiro endpoint de health check de cada serviço com trace, log e métrica para validar que o pipeline de observabilidade funciona end-to-end. Dashboards com métricas RED (Rate, Errors, Duration) por serviço devem estar prontos antes do Build.

- **Developer experience local**: Configurar o ambiente de desenvolvimento local para que cada dev consiga rodar pelo menos o serviço no qual está trabalhando + suas dependências diretas (banco, broker, serviços upstream) com um único comando. Docker Compose para dependências de infra (Postgres, Redis, RabbitMQ, Kafka), e scripts de seed para popular bancos com dados de teste. Se o número de serviços torna impossível rodar tudo localmente, configurar Telepresence ou similar para conectar o dev local ao cluster de staging.

### Perguntas

1. Toda a infraestrutura foi provisionada via IaC (Terraform, Pulumi, CDK) e o código está versionado em repositório? [fonte: DevOps, Arquiteto] [impacto: DevOps]
2. Os pipelines de CI/CD de cada serviço estão configurados e rodando em menos de 10 minutos (build + test + push)? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
3. A decisão mono vs. polyrepo foi implementada com detecção de mudanças por path (se mono) ou sincronização de contratos (se poly)? [fonte: Tech Lead, DevOps] [impacto: Dev]
4. Os ambientes dev, staging e production estão isolados com recursos independentes (banco, broker, secrets)? [fonte: DevOps] [impacto: DevOps, Dev]
5. As variáveis de configuração de cada serviço estão documentadas em .env.example e gerenciadas por secrets manager em cada ambiente? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
6. A stack de observabilidade (tracing, logging, métricas) está configurada e validada end-to-end com o primeiro health check? [fonte: SRE, DevOps] [impacto: DevOps, Dev]
7. Os dashboards de monitoramento com métricas RED por serviço estão prontos antes do início do Build? [fonte: SRE, DevOps] [impacto: DevOps]
8. O ambiente de desenvolvimento local está documentado e cada dev consegue rodar seu serviço com dependências em menos de 5 minutos? [fonte: Dev, Tech Lead] [impacto: Dev]
9. Os bancos de dados de cada serviço foram criados com schema inicial e scripts de seed para dados de teste? [fonte: Dev] [impacto: Dev]
10. O container registry está configurado com políticas de retenção de imagens e scan de vulnerabilidades automático? [fonte: DevOps, Security] [impacto: DevOps]
11. Os endpoints de health check (/health, /ready, /live) de cada serviço estão implementados e conectados ao orquestrador? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
12. O broker de mensageria está configurado com tópicos/filas do MVP, dead-letter queues e políticas de retry? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
13. As network policies do Kubernetes restringem comunicação apenas entre serviços que devem se comunicar? [fonte: Security, DevOps] [impacto: DevOps]
14. O processo de onboarding de novos desenvolvedores foi documentado com instruções de setup local passo a passo? [fonte: Tech Lead, Dev] [impacto: Dev]
15. Um deploy automatizado end-to-end (push → build → test → deploy em staging) foi testado com sucesso para pelo menos um serviço? [fonte: DevOps, Dev] [impacto: DevOps, Dev]

---

## Etapa 07 — Build

- **Implementação service-by-service, não layer-by-layer**: Implementar cada microserviço como unidade completa (API + lógica de negócio + persistência + testes + observabilidade) antes de avançar para o próximo. A abordagem de implementar "toda a camada de API de todos os serviços" e depois "toda a camada de persistência" gera integração tardia e bugs de contrato que só aparecem no final. O ideal é implementar o serviço mais central do domínio (geralmente o core domain) primeiro, porque ele é dependência de vários outros e seus contratos precisam ser validados cedo.

- **Contract testing entre serviços**: Implementar testes de contrato (Pact, Spring Cloud Contract) entre serviços que se comunicam. O serviço consumidor define suas expectativas (consumer contract), e o pipeline do serviço provedor valida que sua implementação satisfaz todos os consumer contracts. Isso permite que cada serviço seja deployado independentemente — se o pipeline passa, o contrato está preservado. Sem contract testing, deploys independentes são uma ilusão — qualquer mudança de API pode quebrar consumidores silenciosamente, e o bug só aparece em staging ou produção.

- **Implementação de sagas e compensações**: Implementar as sagas definidas na Etapa 04 com atenção especial às ações de compensação. Cada passo da saga deve ser idempotente (executar duas vezes produz o mesmo resultado) porque retries são inevitáveis em sistemas distribuídos. Testar cada cenário de falha documentado — não apenas o happy path. Em saga orquestrada, o orchestrator deve persistir o estado de cada execução para permitir retry manual de sagas que falharam em estado intermediário. Dead-letter queues devem ter alertas configurados para que falhas não passem despercebidas.

- **Tratamento de falhas distribuídas**: Implementar padrões de resiliência em cada serviço: circuit breaker (parar de chamar serviço downstream quando ele está falhando, evitando cascata), retry com backoff exponencial e jitter (para chamadas idempotentes), timeout configurado por dependência (não usar timeout padrão infinito do HTTP client), e fallback/degradação graciosa (se o serviço de recomendações está fora, mostrar lista genérica, não erro 500). Bibliotecas como resilience4j (Java), Polly (.NET) ou cockatiel (Node.js) facilitam a implementação desses padrões sem código boilerplate.

- **Testes automatizados em múltiplos níveis**: Além de testes unitários por serviço (lógica de negócio isolada, sem I/O), implementar testes de integração (serviço + banco real via testcontainers, serviço + broker real), contract tests (validação de contratos inter-serviços), e testes de componente (serviço completo rodando em container com dependências mockadas). Testes end-to-end (múltiplos serviços reais em ambiente integrado) são os mais custosos de manter e devem ser limitados aos fluxos críticos de negócio. A pirâmide de testes deve ser respeitada: muitos unitários, médios de integração, poucos e2e.

- **Migração e seed de dados**: Se há migração de dados de sistema legado, implementar o pipeline de migração como um serviço ou job dedicado. A migração geralmente envolve transformação de dados (schema legado → schema novo), validação de integridade (contagem de registros, checksums, validação de foreign keys cross-service), e reconciliação (comparar dados no sistema legado e no novo para garantir que nada se perdeu). Migrar em batches com checkpoints para permitir retry parcial — nunca "tudo de uma vez" em uma janela de manutenção apertada.

### Perguntas

1. Os serviços estão sendo implementados como unidades completas (API + negócio + persistência + testes) e não em camadas horizontais? [fonte: Tech Lead] [impacto: Dev, QA]
2. Os contract tests entre serviços estão implementados e rodando no CI de ambos os lados (consumer e provider)? [fonte: Tech Lead, QA] [impacto: Dev, QA]
3. As sagas foram implementadas com ações de compensação testadas para cada cenário de falha documentado? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
4. Cada passo de saga é idempotente e o orchestrator persiste estado para permitir retry manual de sagas falhadas? [fonte: Dev, Arquiteto] [impacto: Dev]
5. Os padrões de resiliência (circuit breaker, retry, timeout, fallback) estão implementados em todas as chamadas inter-serviço? [fonte: Dev, Arquiteto] [impacto: Dev, QA]
6. Os testes unitários, de integração e de componente estão cobrindo os fluxos críticos com cobertura >80% no core domain? [fonte: Tech Lead, QA] [impacto: Dev, QA]
7. Os testes end-to-end estão limitados aos fluxos críticos de negócio e não estão duplicando cobertura dos contract tests? [fonte: QA, Tech Lead] [impacto: QA, Dev]
8. As dead-letter queues estão configuradas com alertas e existe processo documentado para tratar mensagens falhadas? [fonte: Dev, SRE] [impacto: Dev, DevOps]
9. O pipeline de migração de dados (se aplicável) foi implementado com batches, checkpoints e validação de integridade? [fonte: Dev, Analista de dados] [impacto: Dev, PM]
10. Os endpoints de cada serviço estão implementados conforme os contratos definidos na Etapa 04, sem desvios não-documentados? [fonte: Tech Lead, QA] [impacto: Dev]
11. A autenticação e autorização estão implementadas e testadas em cada serviço, não apenas no API Gateway? [fonte: Security, Dev] [impacto: Dev, Security]
12. O rate limiting está implementado no API Gateway com thresholds definidos e response adequado (429 + Retry-After)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
13. Os logs estruturados com trace-id estão sendo emitidos por todos os serviços e chegando ao sistema centralizado? [fonte: Dev, SRE] [impacto: Dev, DevOps]
14. As métricas de negócio (pedidos/minuto, latência por endpoint, taxa de erro) estão sendo coletadas e exibidas nos dashboards? [fonte: SRE, Produto] [impacto: DevOps, PM]
15. O frontend está integrado com os serviços via API Gateway/BFF e os fluxos principais funcionam end-to-end em staging? [fonte: Frontend Lead, QA] [impacto: Dev, QA]

---

## Etapa 08 — QA

- **Testes de carga por serviço e do sistema**: Executar testes de carga (k6, Gatling, Locust) em dois níveis: isolado por serviço (para identificar gargalos individuais de CPU, memória, banco, pool de conexões) e integrado no sistema completo (para identificar gargalos de comunicação inter-serviço, contenção de recursos compartilhados como banco, e cascatas de timeout). Os testes devem simular o padrão de tráfego esperado em produção (distribuição de endpoints, tamanho de payload, frequência de operações de escrita vs. leitura) com ramp-up gradual até 2x a carga esperada de pico.

- **Testes de resiliência (chaos engineering)**: Simular falhas controladas para validar que o sistema se comporta conforme projetado quando componentes falham: matar uma instância de serviço (Kubernetes deve recriar automaticamente, requests devem ser roteados para instâncias saudáveis), introduzir latência artificial em chamadas inter-serviço (circuit breaker deve abrir e fallback deve ativar), desconectar o broker de mensageria (mensagens devem ser retidas e processadas após reconexão), e simular indisponibilidade de banco (serviço deve retornar erro gracioso, não stack trace). Ferramentas: Chaos Monkey, Litmus Chaos, ou scripts customizados com toxiproxy.

- **Validação de sagas e consistência eventual**: Testar cada saga em cenários de falha parcial — não apenas o happy path. Exemplo: em um fluxo de pagamento, simular falha no serviço de notificação após pagamento capturado — a compensação deve garantir que o usuário é notificado posteriormente (retry) e que o estado do pedido reflete corretamente que o pagamento foi processado. Verificar que após a resolução de falhas, os dados em todos os serviços envolvidos estão consistentes (reconciliação). Dead-letter queues devem ser verificadas — mensagens na DLQ indicam fluxos que falharam silenciosamente.

- **Testes de segurança e penetração**: Executar SAST (análise estática de código — SonarQube, Snyk Code), DAST (análise dinâmica — OWASP ZAP, Burp Suite) e SCA (análise de dependências — Snyk, Dependabot) em cada serviço. Validar especificamente: injeção SQL/NoSQL em endpoints que aceitam input do usuário, IDOR (Insecure Direct Object Reference — um tenant acessando dados de outro), SSRF (Server-Side Request Forgery em serviços que fazem requests a URLs fornecidas pelo usuário), e broken authentication (tokens expirados, JWT forjados, escalação de privilégio). Para sistemas com dados sensíveis, considerar pentest externo por empresa especializada.

- **Testes de contrato e compatibilidade de deploy**: Validar que cada serviço pode ser deployado independentemente sem quebrar os consumidores. Simular o cenário de deploy parcial: serviço A na versão nova, serviço B na versão antiga — os contratos devem ser backwards compatible. Consumer-driven contract tests (Pact) devem estar passando para todas as combinações de versão que coexistirão em produção durante um rolling update. Se algum contrato foi alterado de forma breaking, o plano de migração coordenada deve ser documentado e testado.

- **Validação de observabilidade em cenário real**: Simular um incidente realista (latência alta em um serviço, erro 500 intermitente, mensagem presa na DLQ) e validar que a equipe consegue diagnosticar a causa raiz usando apenas as ferramentas de observabilidade — sem acessar diretamente os logs dos pods ou bancos de dados. O trace distribuído deve permitir seguir uma request do frontend até o serviço que falhou. Os alertas devem ter disparado. Os dashboards devem mostrar a anomalia. Se a equipe não consegue diagnosticar com as ferramentas disponíveis, a stack de observabilidade precisa ser melhorada antes do go-live.

### Perguntas

1. Os testes de carga foram executados por serviço e no sistema integrado com carga de até 2x o pico esperado? [fonte: QA, SRE] [impacto: Dev, DevOps]
2. Os gargalos identificados nos testes de carga (CPU, memória, pool de conexões, throughput de banco) foram resolvidos? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
3. Os testes de resiliência simularam falha de instância, latência alta, broker indisponível e banco fora do ar? [fonte: SRE, QA] [impacto: Dev, DevOps]
4. O circuit breaker abriu corretamente e o fallback foi ativado em cada cenário de falha testado? [fonte: Dev, QA] [impacto: Dev]
5. Cada saga foi testada em cenários de falha parcial e os dados ficaram consistentes após compensação? [fonte: QA, Dev] [impacto: Dev, QA]
6. A dead-letter queue foi verificada e não há mensagens presas de fluxos críticos que falharam silenciosamente? [fonte: Dev, SRE] [impacto: Dev, DevOps]
7. Os testes de segurança (SAST, DAST, SCA) foram executados e todas as vulnerabilidades críticas/altas foram corrigidas? [fonte: Security, QA] [impacto: Dev, Security]
8. Os testes de IDOR validaram que um tenant não consegue acessar dados de outro tenant em nenhum endpoint? [fonte: Security, QA] [impacto: Dev, Security]
9. O deploy independente de cada serviço foi testado sem quebrar consumidores (backwards compatibility validada)? [fonte: QA, DevOps] [impacto: Dev, DevOps]
10. Um incidente simulado foi diagnosticado com sucesso usando apenas distributed tracing, dashboards e alertas? [fonte: SRE] [impacto: DevOps, Dev]
11. Os testes end-to-end dos fluxos críticos de negócio passaram em ambiente de staging com dados realistas? [fonte: QA, Produto] [impacto: QA, Dev]
12. A validação de input em cada endpoint foi testada com payloads maliciosos (injection, XSS, overflow)? [fonte: Security, QA] [impacto: Dev, Security]
13. O auto-scaling foi testado — serviços escalaram corretamente sob carga e reduziram após o pico? [fonte: DevOps, SRE] [impacto: DevOps]
14. O backup e restore de banco de dados foi testado end-to-end com validação de integridade dos dados restaurados? [fonte: DevOps, SRE] [impacto: DevOps]
15. O time de produto validou os fluxos críticos de negócio em staging e aprovou para avançar ao launch prep? [fonte: Produto, QA] [impacto: PM, QA]

---

## Etapa 09 — Launch Prep

- **Runbooks de operação**: Documentar procedimentos operacionais para os cenários mais prováveis de incidente: serviço fora do ar (como diagnosticar, como reiniciar, como escalar), banco de dados lento (como identificar queries lentas, como fazer kill de sessions, como escalar read replicas), broker de mensageria com lag crescente (como identificar consumers lentos, como escalar consumer group, como fazer purge de mensagens antigas), e deploys que precisam de rollback (como reverter para versão anterior, como verificar que o rollback foi bem-sucedido). Cada runbook deve poder ser executado por qualquer membro do time de on-call, não apenas pelo dev que escreveu o serviço.

- **Plano de deploy para produção**: Documentar a sequência exata de deploy dos serviços — a ordem importa quando há dependências (o serviço de autenticação deve estar no ar antes dos serviços que dependem dele). Definir a estratégia de rollout: rolling update (instâncias substituídas gradualmente, zero downtime), blue-green (dois ambientes completos, troca de tráfego instantânea), ou canary (nova versão recebe 5% do tráfego inicialmente, percentual aumenta conforme métricas de sucesso). Canary é recomendado para o primeiro deploy em produção de microserviços — permite detectar problemas com impacto limitado.

- **Configuração de alertas de produção**: Configurar alertas para cada serviço com thresholds calibrados — alertas demais geram fadiga e são ignorados, alertas de menos deixam incidentes passarem. Alertas recomendados por serviço: taxa de erro >1% (5xx responses), latência P99 acima do SLO definido, CPU >80% sustentado por 5 minutos, memória >90%, fila de mensagens com lag >1000 mensagens por 5 minutos, health check falhando por >30 segundos. Alertas de negócio: zero pedidos processados por 10 minutos (se normalmente há fluxo constante), taxa de falha em pagamentos acima de 5%, zero logins por 15 minutos.

- **Estratégia de rollback por serviço**: Para cada serviço, documentar o procedimento de rollback: reverter para a imagem anterior no container registry (tag específica), verificar que o schema do banco é compatível com a versão anterior (migrations devem ser backwards compatible), e validar que os consumer contracts continuam satisfeitos. Se uma migration de banco não é backwards compatible (coluna removida, tipo alterado), o rollback exige restore de backup — esse cenário deve ser testado antes do go-live. Feature flags permitem desabilitar funcionalidades novas sem rollback de código.

- **War room e comunicação durante o go-live**: Definir o modelo de comunicação durante o go-live: canal dedicado (Slack, Teams) onde todas as atualizações são postadas em tempo real, roles definidos (quem executa o deploy, quem monitora dashboards, quem comunica status para stakeholders, quem tem poder de decisão de rollback), e checklist de validação pós-deploy (cada item com responsável e status). O go-live de microserviços é mais complexo que de monolitos porque envolve múltiplos deploys coordenados — a war room garante que todos sabem o estado atual de cada serviço.

- **Data migration e cutover de dados**: Se o novo sistema substitui um sistema legado, planejar a migração de dados com estratégia de cutover — período de dual-write (ambos os sistemas recebem dados), período de validação (comparação de dados entre sistemas), e cutover final (sistema legado para de receber dados). O cutover deve ter rollback possível — manter o sistema legado funcional por período de contingência. Dados financeiros e regulatórios exigem atenção especial — a perda de um registro de transação pode ter implicações legais.

### Perguntas

1. Os runbooks de operação foram documentados para os cenários mais prováveis de incidente e podem ser executados por qualquer membro do on-call? [fonte: SRE, DevOps] [impacto: DevOps, Dev]
2. O plano de deploy para produção documenta a ordem de deploy dos serviços considerando dependências entre eles? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
3. A estratégia de rollout (rolling, blue-green, canary) foi definida e testada em staging com sucesso? [fonte: DevOps] [impacto: DevOps, Dev]
4. Os alertas de produção foram configurados com thresholds calibrados e testados (alerta disparou quando threshold foi violado)? [fonte: SRE, DevOps] [impacto: DevOps]
5. O procedimento de rollback por serviço foi documentado e testado, incluindo backwards compatibility de migrations? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
6. A war room para o go-live foi planejada com canal dedicado, roles definidos e checklist de validação? [fonte: PM, DevOps] [impacto: PM, DevOps, Dev]
7. A data migration (se aplicável) foi testada com dados reais em staging e a reconciliação confirmou integridade? [fonte: Dev, Analista de dados] [impacto: Dev, PM]
8. Os feature flags para funcionalidades de risco estão configurados para permitir desabilitação sem rollback de código? [fonte: Dev, Produto] [impacto: Dev, PM]
9. Os stakeholders foram notificados sobre data, horário, impactos esperados e janela de indisponibilidade (se houver)? [fonte: Diretoria, PM] [impacto: PM]
10. O SLA de resposta a incidentes nas primeiras 72h pós-go-live foi definido (quem está de on-call, como escalar)? [fonte: CTO, SRE] [impacto: DevOps, Dev]
11. Os certificados SSL e tokens de integração de produção foram provisionados e testados (não expiram nos próximos 30 dias)? [fonte: DevOps, Security] [impacto: DevOps]
12. O DNS de produção foi configurado e o TTL reduzido com antecedência para facilitar cutover? [fonte: DevOps, TI] [impacto: DevOps]
13. Os secrets de produção (API keys, tokens de pagamento, credentials de banco) foram configurados e validados? [fonte: DevOps, Security] [impacto: DevOps, Dev]
14. O monitoramento de disponibilidade externo (UptimeRobot, Better Uptime, PagerDuty) está configurado e testado? [fonte: SRE, DevOps] [impacto: DevOps]
15. A janela de go-live foi escolhida estrategicamente (dia útil, horário de baixo tráfego, time completo disponível, sem conflito com eventos de negócio)? [fonte: PM, Diretoria] [impacto: PM, DevOps]

---

## Etapa 10 — Go-Live

- **Deploy sequencial com validação entre etapas**: Executar o deploy dos serviços na ordem planejada, validando cada serviço antes de avançar para o próximo. Para cada serviço deployado: verificar health check (endpoint /health retorna 200), verificar métricas no dashboard (taxa de erro, latência), executar smoke test automatizado (request de validação para endpoints críticos), e confirmar no canal da war room antes de prosseguir. Se qualquer serviço falhar na validação, pausar o deploy, diagnosticar, e decidir entre fix forward (corrigir e re-deployar) ou rollback (reverter para versão anterior e abortar o go-live).

- **Cutover de tráfego e monitoramento intensivo**: Após todos os serviços estarem no ar e validados, direcionar o tráfego real para o novo sistema. Se o cutover é via DNS, monitorar propagação. Se é via load balancer (switch de backend), a troca é instantânea. Nas primeiras horas, monitorar intensivamente: latência P99 de cada serviço (comparar com baseline de staging), taxa de erro 5xx (deve ser <0.1%), utilização de recursos (CPU, memória — confirmar que auto-scaling está funcionando se necessário), e métricas de negócio (pedidos processados, logins realizados, transações completadas). Qualquer anomalia deve ser reportada imediatamente no canal da war room.

- **Validação de integrações em produção**: Testar cada integração externa com dados reais de produção. Gateway de pagamento: processar uma transação real de valor mínimo. Serviço de e-mail: enviar notificação real para endereço de teste. Webhook de parceiros: verificar que callbacks estão chegando e sendo processados. APIs de terceiros: confirmar que rate limits de produção são suficientes para a carga esperada. Integrações que funcionavam perfeitamente em staging podem falhar em produção por diferenças de configuração, rate limits mais restritivos, ou firewalls que bloqueiam IPs do novo ambiente.

- **Monitoramento da primeira semana**: Manter monitoramento intensivo nos primeiros 7 dias. Os problemas mais comuns em microserviços pós-go-live são: memory leaks que só aparecem após horas/dias de operação contínua (GC pressure, connection pool exhaustion), mensagens acumulando na DLQ por edge cases não testados, degradação gradual de performance conforme o volume de dados cresce, e inconsistências de dados entre serviços que só aparecem com tráfego real (race conditions, timeout em sagas). Revisar dashboards e DLQs diariamente. Realizar um post-mortem ao final da primeira semana documentando incidentes, lições aprendidas e ações de melhoria.

- **Estabilização e handoff operacional**: Após a primeira semana sem incidentes críticos, formalizar o handoff operacional. Entregar ao time de operações (ou ao cliente, se aplicável): documentação de arquitetura atualizada com o que foi realmente implementado (não o planejado), runbooks testados e atualizados com base nos incidentes da primeira semana, acessos a todos os sistemas (cloud console, monitoramento, CI/CD, repositórios), dashboards de monitoramento com alertas calibrados, e contatos de suporte para cada serviço (ownership por squad). O projeto não está encerrado até que o time de operações consiga resolver incidentes de severidade média sem escalar para os desenvolvedores originais.

- **Documentação de decisões arquiteturais**: Consolidar todos os ADRs (Architecture Decision Records) produzidos durante o projeto em um local acessível. Cada ADR documenta: contexto (por que a decisão precisou ser tomada), decisão tomada (o que foi escolhido), alternativas consideradas (o que foi descartado e por quê), e consequências (trade-offs aceitos). Esta documentação é crucial para quem herdar o sistema — evita que futuras equipes revisitem decisões já tomadas sem entender o contexto original, ou pior, revertam decisões que tinham justificativa sólida.

### Perguntas

1. O deploy dos serviços foi executado na ordem planejada com validação de health check e smoke test entre cada serviço? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
2. O cutover de tráfego foi executado e a latência P99, taxa de erro e métricas de negócio estão dentro dos limites esperados? [fonte: SRE, DevOps] [impacto: DevOps, Dev]
3. Cada integração externa (pagamento, e-mail, SMS, APIs de parceiros) foi validada com dados reais de produção? [fonte: Dev, QA] [impacto: Dev]
4. O auto-scaling respondeu corretamente ao tráfego real de produção (scale-up e scale-down funcionaram)? [fonte: DevOps, SRE] [impacto: DevOps]
5. A DLQ foi verificada nas primeiras horas e não há mensagens falhadas de fluxos críticos? [fonte: Dev, SRE] [impacto: Dev, DevOps]
6. O monitoramento de disponibilidade externo confirmou uptime desde o go-live sem alertas falsos? [fonte: SRE, DevOps] [impacto: DevOps]
7. Os dashboards de monitoramento estão mostrando métricas de negócio em real-time e as primeiras transações foram validadas? [fonte: SRE, Produto] [impacto: DevOps, PM]
8. O plano de on-call para a primeira semana está ativo com responsáveis designados e escalation paths testados? [fonte: SRE, CTO] [impacto: DevOps, Dev]
9. O sistema legado (se aplicável) está mantido como fallback pelo período de contingência acordado? [fonte: TI, DevOps] [impacto: DevOps, PM]
10. Os logs e traces das primeiras horas foram revisados para identificar warnings ou erros não-críticos que merecem atenção? [fonte: Dev, SRE] [impacto: Dev, DevOps]
11. O post-mortem da primeira semana foi agendado com todos os participantes relevantes? [fonte: PM, CTO] [impacto: PM, Dev, DevOps]
12. A documentação de arquitetura foi atualizada para refletir o que foi realmente implementado (não o planejado)? [fonte: Arquiteto, Dev] [impacto: Dev, Arquiteto]
13. Os runbooks foram atualizados com base nos incidentes e aprendizados da primeira semana? [fonte: SRE, DevOps] [impacto: DevOps]
14. Todos os acessos foram entregues formalmente ao time de operações/cliente e cada pessoa confirmou acesso? [fonte: DevOps, PM] [impacto: PM]
15. O aceite formal de entrega foi obtido e o plano de suporte pós-lançamento foi ativado com SLA comunicado? [fonte: Diretoria, PM] [impacto: PM]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Precisamos de microserviços porque todo mundo usa"** — Decisão arquitetural por hype, não por necessidade. Microserviços só se justificam quando há complexidade de domínio que exige bounded contexts independentes, times grandes que precisam de autonomia de deploy, ou requisitos de escala diferenciados por componente. Para um time de 3-5 devs com domínio simples, um monolito modular entrega o mesmo valor com um décimo da complexidade operacional.
- **"O time nunca trabalhou com sistemas distribuídos mas vai aprender"** — Curva de aprendizado subestimada. Debugging distribuído, eventual consistency, sagas, circuit breakers e observabilidade são habilidades que levam meses para dominar. Um time inexperiente vai gastar mais tempo lutando contra a infraestrutura do que entregando valor de negócio. Considerar monolito modular como primeiro passo, com migração planejada para microserviços quando a maturidade permitir.
- **"O orçamento de infra é o mesmo do monolito atual"** — Custo operacional subestimado. Microserviços multiplicam custos: Kubernetes, múltiplos bancos, broker de mensageria, observabilidade, container registry. Um sistema com 10 serviços pode custar 5-10x mais em infraestrutura do que o monolito equivalente. Se o orçamento não acompanha, o projeto vai cortar corners em observabilidade e resiliência — exatamente onde não se pode cortar.

### Etapa 02 — Discovery

- **"Os bounded contexts vão emergir durante o build"** — Fronteiras de serviço definidas por conveniência técnica em vez de domínio de negócio. Resultado: serviços que precisam se chamar constantemente (chatty services), dados duplicados inconsistentes entre serviços, e refatoração custosa de fronteiras 6 meses depois. Bounded contexts devem ser mapeados antes de escrever a primeira linha de código.
- **"Todos os serviços precisam de 99.99% de disponibilidade"** — RNFs genéricos que inflam custo sem justificativa. O serviço de billing que roda uma vez por mês não precisa da mesma disponibilidade que o serviço de checkout. RNFs devem ser definidos por serviço com base no impacto de negócio da indisponibilidade de cada um.
- **"Não temos integração com legado, é tudo novo"** — Raramente é verdade. Frequentemente há ERP, CRM, gateway de pagamento, ou sistemas internos que precisam trocar dados. Integrações com legado são as fontes mais comuns de atraso em projetos de microserviços e precisam ser mapeadas explicitamente.

### Etapa 03 — Alignment

- **"Cada dev pode trabalhar em qualquer serviço"** — Ausência de ownership. Se todos são responsáveis por todos os serviços, ninguém tem profundidade de contexto para diagnosticar problemas rapidamente. Resultado: incidentes que levam horas para resolver porque ninguém conhece o serviço em profundidade. Ownership clara por squad é pré-requisito operacional.
- **"Usamos banco compartilhado para simplificar"** — Violação do princípio fundamental de microserviços. Banco compartilhado destrói a independência de deploy — schema change em uma tabela pode quebrar todos os serviços que acessam o mesmo banco. Se o time não aceita database-per-service, não está pronto para microserviços.
- **"A gente define os contratos de API durante o build"** — Sem contratos definidos antes do build, cada squad implementa suas APIs no formato que preferir. Integração entre serviços vira um exercício de negociação constante. Contratos devem ser definidos, documentados e versionados antes do build começar.

### Etapa 04 — Definition

- **Serviços definidos por camada técnica** — "Serviço de banco de dados", "serviço de autenticação", "serviço de API". Microserviços devem ser organizados por domínio de negócio (pedidos, pagamentos, catálogo), não por camada técnica. Serviços por camada criam acoplamento forte e perdem a vantagem de deploy independente.
- **"As sagas são simples, não precisa documentar"** — Toda saga parece simples no happy path. A complexidade está nos cenários de falha e compensação — que só são descobertos em produção se não forem documentados antes. Cada saga precisa de diagrama com passos, compensações e estados finais.
- **Contratos de API sem versionamento** — APIs que mudam sem aviso quebram consumidores silenciosamente. Em microserviços, breaking changes em APIs internas causam incidentes em cascata. Versionamento semântico com período de deprecação documentado é obrigatório.

### Etapa 05 — Architecture

- **"Kubernetes porque é enterprise"** — Kubernetes sem engenheiro de DevOps/SRE dedicado é fonte de incidentes. Para 3-5 serviços, ECS ou Cloud Run resolve com menos complexidade e custo. Kubernetes se justifica acima de 8-10 serviços com requisitos de auto-scaling, service mesh e multi-tenancy de infraestrutura.
- **"Kafka para tudo"** — Kafka é poderoso mas caro de operar e over-engineering para cenários simples de job queue. RabbitMQ ou SQS resolve 80% dos casos de comunicação assíncrona com fração do custo e complexidade operacional. Kafka se justifica quando há necessidade de event replay, múltiplos consumer groups, ou volume >10.000 msg/segundo.
- **"Monorepo porque é mais simples"** — Monorepo sem tooling adequado (Nx, Turborepo, Bazel) se torna gargalo — CI roda todos os testes de todos os serviços a cada push. Com 10+ serviços, o pipeline leva 30+ minutos e developers perdem produtividade. Monorepo exige investimento em build tooling desde o dia 1.

### Etapa 06 — Setup

- **Infraestrutura provisionada via console (click-ops)** — Ambientes criados manualmente no console do AWS/GCP/Azure. Resultado: staging e produção com diferenças invisíveis, impossibilidade de recriar ambiente em caso de disaster, e knowledge concentrado em quem clicou. IaC (Terraform, Pulumi) é obrigatório desde o primeiro ambiente.
- **"Observabilidade a gente configura depois do MVP"** — Em microserviços sem observabilidade, o primeiro bug em produção é irresolvível. Sem distributed tracing, sem logging centralizado e sem métricas, o time vai fazer SSH em pods e grep em logs — atividade que leva horas e não escala. Observabilidade é pré-requisito do build, não adição posterior.
- **Pipeline de CI que leva 30+ minutos** — Pipelines lentos incentivam devs a fazer merge sem esperar CI, acumular commits sem push, ou skipar testes. O resultado é bugs em produção que custam 10x mais que os minutos economizados. Pipeline deve rodar em menos de 10 minutos por serviço.

### Etapa 07 — Build

- **"Todos os serviços precisam estar prontos para testar"** — Integração big-bang. Cada serviço deve ser testável independentemente com suas dependências mockadas (contract tests, stubs de serviços downstream). Esperar todos os serviços prontos para testar qualquer um é voltar ao mindset de monolito.
- **Happy path only nas sagas** — Sagas testadas apenas no cenário de sucesso. Compensações de falha nunca testadas até o primeiro incidente em produção — quando se descobre que a compensação também falha, criando estado inconsistente. Cada cenário de falha documentado na Definition deve ter teste correspondente.
- **Logs como println/console.log** — Logging não-estruturado em microserviços torna o debugging impossível quando há 10 serviços emitindo logs simultaneamente. Logs devem ser JSON estruturado com trace-id, service name, timestamp e severity desde o primeiro endpoint.

### Etapa 08 — QA

- **"Testamos em staging, está funcionando"** — Staging com 10 registros no banco não revela problemas que aparecem com 1 milhão. Testes de carga com volume realista de dados são obrigatórios — banco com seed de volume produtivo, tráfego simulado com padrão realista, e execução por tempo suficiente para revelar memory leaks.
- **Apenas testes manuais nos fluxos distribuídos** — Tester manual não consegue simular falha parcial de serviço, latência de rede ou race condition. Testes de resiliência (chaos engineering) devem ser automatizados e reproduzíveis. Se o circuit breaker nunca foi ativado em teste, não há garantia de que funciona.
- **Security scan apenas no frontend** — Microserviços expõem múltiplos endpoints, cada um com seu próprio modelo de validação. SAST e DAST devem cobrir cada serviço. Vulnerabilidade em um serviço interno é tão grave quanto no frontend — um atacante que passa do gateway acessa a rede interna.

### Etapa 09 — Launch Prep

- **"Deploy de todos os serviços de uma vez"** — Deploy big-bang de 10 serviços simultaneamente torna impossível identificar qual serviço causou um problema. Deploy sequencial com validação entre etapas é obrigatório — se o serviço 3 falhar, os serviços 1 e 2 já estão validados e o impacto é controlado.
- **Alertas com thresholds padrão do template** — Alertas genéricos ("CPU > 80%") sem calibração para o padrão real de cada serviço. Um serviço CPU-intensive pode ter CPU normal em 70% enquanto outro pode ter problema real em 30%. Thresholds devem ser calibrados com base nos testes de carga.
- **Sem runbooks para on-call** — "A gente resolve na hora". Na hora, às 3h da manhã, com pressão, o engenheiro de on-call precisa de um passo a passo — não de criatividade. Runbooks com diagnóstico e ações para cada cenário são obrigatórios antes do go-live.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde** — Se algo der errado, o time não está disponível no fim de semana. Go-live de microserviços é mais arriscado que de monolito — há mais componentes que podem falhar. Dia útil, início da manhã, com dia inteiro de buffer é obrigatório.
- **"Está no ar, projeto encerrado"** — Sem monitoramento intensivo na primeira semana, memory leaks, mensagens na DLQ, inconsistências de dados entre serviços e degradação gradual de performance passam despercebidos. A primeira semana pós-go-live é a fase mais crítica do projeto.
- **Sistema legado desligado no mesmo dia** — Se algo der errado e o rollback for necessário, o sistema legado precisa estar funcional. Manter em paralelo por pelo menos 1-2 semanas é seguro e necessário. Custos de operação em paralelo são insignificantes comparados ao custo de um rollback impossível.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não precisa de microserviços** e deveria ser reclassificado.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "O time tem 3 desenvolvedores" | Time pequeno demais para ownership de múltiplos serviços | Reclassificar para web-app-monolith |
| "É um CRUD simples com poucas entidades" | Domínio simples que não justifica bounded contexts separados | Reclassificar para web-app-monolith |
| "Não temos DevOps/SRE no time" | Incapacidade de operar infraestrutura distribuída | Reclassificar para web-app-monolith ou alocar DevOps |
| "É uma landing page com formulário e dashboard" | Site estático + backend simples | Reclassificar para static-site + api ou web-app-monolith |
| "Tudo pode rodar no mesmo servidor" | Sem requisito de escala independente por componente | Reclassificar para web-app-monolith |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Os bounded contexts ainda não estão definidos" | 02 | Fronteiras de serviço arbitrárias, refatoração custosa | Investir em event storming/DDD antes de prosseguir |
| "Não temos orçamento para Kubernetes gerenciado" | 01 | Orquestração manual = incidentes operacionais | Aprovar orçamento ou simplificar para monolito |
| "O time nunca usou mensageria assíncrona" | 01 | Sagas e event-driven vão falhar em produção | Treinamento antes do build ou simplificar comunicação para síncrona |
| "Não temos stack de observabilidade" | 06 | Primeiro bug em produção será irresolvível | Setup de tracing/logging/métricas é pré-requisito do build |
| "O esquema de permissões ainda não foi definido" | 04 | Brechas de segurança, acessos não-autorizados | Definir RBAC/ABAC antes do build |
| "Não sabemos quem vai operar em produção" | 01 | Sem on-call, incidentes ficam sem resposta | Definir modelo operacional antes de avançar |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Vamos começar com 15 microserviços no MVP" | 04 | Over-engineering, complexidade desnecessária | Questionar necessidade de cada serviço, sugerir começar com 3-5 |
| "Cada squad escolhe sua stack" | 03 | Polyglot extremo, impossível fazer code review cross-squad | Definir stack padrão com exceções justificadas por ADR |
| "Não precisamos de contract testing, confiamos nas squads" | 03 | Breaking changes silenciosas entre serviços | Implementar Pact ou similar como obrigatório no CI |
| "O deploy vai ser manual inicialmente" | 06 | Deploy manual de 10 serviços = erro humano garantido | CI/CD automatizado é pré-requisito, não nice-to-have |
| "Performance a gente otimiza depois" | 02 | Gargalos arquiteturais descobertos em produção são caros de resolver | Definir RNFs por serviço e testar carga antes do go-live |
| "Vamos usar o mesmo banco para todos os serviços inicialmente" | 03 | Acoplamento que impede deploy independente e escala individual | Alertar que migrar para database-per-service com dados em produção é custoso |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Gatilho para microserviços identificado e validado como legítimo (pergunta 1)
- Estrutura organizacional compatível com ownership de serviços (pergunta 2)
- Orçamento de infraestrutura cloud aprovado com projeção de 12 meses (pergunta 3)
- Nível de experiência do time avaliado e gaps de capacitação identificados (pergunta 7)
- Prazo de go-live com justificativa de negócio (pergunta 10)

### Etapa 02 → 03

- Domínios core, supporting e generic classificados (pergunta 1)
- Fluxos de negócio end-to-end mapeados com serviços participantes (pergunta 2)
- Requisitos de consistência definidos por fluxo (pergunta 3)
- RNFs definidos por serviço, não genericamente (pergunta 4)
- Integrações externas obrigatórias mapeadas (pergunta 5)

### Etapa 03 → 04

- Ownership de serviços por squad definida (pergunta 1)
- Formato de contratos de API padronizado (pergunta 2)
- Modelo de comunicação decidido por fluxo (pergunta 4)
- Princípio de database-per-service aceito pelo time (pergunta 5)
- Estratégia de autenticação e autorização desenhada (pergunta 6)

### Etapa 04 → 05

- Mapa de serviços do MVP aprovado com fronteiras claras (pergunta 1)
- Contratos de API documentados com schemas de request/response (pergunta 3)
- Sagas documentadas com compensações e cenários de falha (pergunta 4)
- Modelo de permissões especificado (pergunta 5)
- Padrões de observabilidade definidos (pergunta 7)

### Etapa 05 → 06

- API Gateway e BFF definidos e justificados (perguntas 1 e 2)
- Plataforma de orquestração escolhida (pergunta 5)
- CI/CD por serviço desenhado (pergunta 6)
- Custos mensais calculados e aprovados (pergunta 11)
- Arquitetura documentada em ADRs e aprovada (pergunta 15)

### Etapa 06 → 07

- Infraestrutura provisionada via IaC e versionada (pergunta 1)
- CI/CD de cada serviço configurado e testado (pergunta 2)
- Ambientes isolados e configurados (pergunta 4)
- Observabilidade validada end-to-end (pergunta 6)
- Deploy automatizado testado com sucesso (pergunta 15)

### Etapa 07 → 08

- Serviços implementados como unidades completas com testes (pergunta 1)
- Contract tests implementados entre serviços (pergunta 2)
- Sagas implementadas com compensações testadas (pergunta 3)
- Padrões de resiliência implementados (pergunta 5)
- Frontend integrado e fluxos principais funcionando end-to-end (pergunta 15)

### Etapa 08 → 09

- Testes de carga executados em 2x pico esperado (pergunta 1)
- Testes de resiliência executados com cenários de falha (pergunta 3)
- Sagas validadas em falha parcial com dados consistentes (pergunta 5)
- Testes de segurança executados e vulnerabilidades críticas corrigidas (pergunta 7)
- Produto aprovou fluxos críticos em staging (pergunta 15)

### Etapa 09 → 10

- Runbooks documentados e executáveis por qualquer membro do on-call (pergunta 1)
- Plano de deploy sequencial documentado com ordem de serviços (pergunta 2)
- Alertas de produção configurados e testados (pergunta 4)
- Rollback testado por serviço (pergunta 5)
- War room planejada com roles e checklist (pergunta 6)

### Etapa 10 → Encerramento

- Deploy executado com validação entre etapas (pergunta 1)
- Métricas de produção dentro dos limites esperados (pergunta 2)
- Integrações externas validadas com dados reais (pergunta 3)
- Post-mortem da primeira semana agendado (pergunta 11)
- Aceite formal obtido e suporte pós-lançamento ativado (pergunta 15)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de web app com microserviços. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 SaaS B2B | V2 Marketplace | V3 Dados/IoT | V4 Super App | V5 API Platform |
|---|---|---|---|---|---|
| 01 Inception | 3 | 3 | 3 | 3 | 2 |
| 02 Discovery | 4 | 4 | 4 | 4 | 3 |
| 03 Alignment | 4 | 4 | 3 | 5 | 3 |
| 04 Definition | 5 | 5 | 4 | 5 | 5 |
| 05 Architecture | 5 | 5 | 5 | 5 | 4 |
| 06 Setup | 4 | 4 | 5 | 4 | 3 |
| 07 Build | 5 | 5 | 5 | 5 | 4 |
| 08 QA | 4 | 5 | 4 | 5 | 4 |
| 09 Launch Prep | 3 | 4 | 3 | 4 | 3 |
| 10 Go-Live | 3 | 4 | 3 | 4 | 2 |
| **Total relativo** | **40** | **43** | **39** | **44** | **33** |

**Observações por variante:**

- **V1 SaaS B2B**: Definition e Build são os mais pesados — modelo de multi-tenancy, permissões por tenant e fluxos de billing são complexos. O gargalo oculto é a governança de dados entre tenants.
- **V2 Marketplace**: Esforço consistentemente alto em todas as etapas. QA é especialmente pesado por causa das sagas de transação (pedido → pagamento → fulfillment) e dos cenários de falha parcial. Testes de carga são críticos por causa de picos sazonais (Black Friday).
- **V3 Dados/IoT**: Setup é o mais pesado — pipeline de ingestão, streaming, processamento e armazenamento exigem infraestrutura especializada (Kafka, Flink, time-series DB). Build é pesado por conta da otimização de throughput.
- **V4 Super App**: O mais pesado de todas as variantes em quase todas as etapas. Alignment é especialmente complexo por causa da coordenação entre múltiplos domínios de negócio. Micro-frontends adicionam complexidade ao Build e QA.
- **V5 API Platform**: Relativamente mais leve porque não há frontend complexo. Definition é pesada por causa da especificação detalhada de APIs, versionamento e documentação. O diferencial é que a API É o produto — a qualidade da documentação e do developer experience é tão importante quanto a funcionalidade.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sistema novo, sem legado (Etapa 01, pergunta 6) | Etapa 07: pergunta 9 (pipeline de migração de dados). Etapa 09: pergunta 7 (data migration). Etapa 10: pergunta 9 (sistema legado como fallback). |
| Comunicação apenas síncrona, sem mensageria (Etapa 03, pergunta 4) | Etapa 04: perguntas 4 e 9 (sagas coreografadas, eventos assíncronos). Etapa 05: pergunta 4 (broker de mensageria). Etapa 06: pergunta 12 (setup de broker). Etapa 07: perguntas 3, 4, 8 (sagas, idempotência, DLQ). Etapa 08: perguntas 5 e 6 (sagas e DLQ). |
| Single-tenant (Etapa 02, pergunta 8) | Etapa 04: pergunta 6 (estratégia de multi-tenancy). Etapa 08: pergunta 8 (teste de IDOR entre tenants). |
| Sem integrações externas (Etapa 02, pergunta 5) | Etapa 07: integrações com terceiros. Etapa 10: pergunta 3 (validação de integrações em produção). |
| API Platform sem frontend (variante V5) | Etapa 05: pergunta 2 (BFF). Etapa 07: pergunta 15 (integração frontend). Etapa 03: micro-frontend considerations. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Migração de monolito existente (Etapa 01, pergunta 6) | Etapa 02: pergunta 2 (fluxos end-to-end mapeados com serviços que extraem do monolito). Etapa 04: estratégia de strangler fig pattern. Etapa 07: pergunta 9 (migração de dados com coexistência). Etapa 09: pergunta 7 (data migration com dual-write). Etapa 10: pergunta 9 (monolito como fallback). |
| Multi-tenancy confirmada (Etapa 02, pergunta 8) | Etapa 04: pergunta 6 (estratégia de isolamento) se torna gate. Etapa 07: pergunta 11 (autorização por tenant). Etapa 08: pergunta 8 (teste de IDOR entre tenants) se torna obrigatório. |
| Comunicação assíncrona com sagas (Etapa 03, pergunta 4) | Etapa 04: pergunta 4 (documentação de sagas) se torna gate. Etapa 05: pergunta 4 (broker de mensageria) se torna bloqueadora. Etapa 07: perguntas 3, 4 e 8 (sagas, idempotência, DLQ) se tornam obrigatórias. Etapa 08: perguntas 5 e 6 (validação de sagas e DLQ). |
| Requisitos de PCI-DSS ou SOC2 (Etapa 01, pergunta 12) | Etapa 05: pergunta 9 (segurança inter-serviços com mTLS obrigatório). Etapa 06: pergunta 13 (network policies). Etapa 08: pergunta 7 (security scan com compliance validation). Etapa 10: pergunta 10 (audit trail verificado em produção). |
| Mais de 10 serviços no MVP (Etapa 01, pergunta 5) | Etapa 05: pergunta 3 (service mesh se torna recomendação forte). Etapa 06: pergunta 2 (pipelines devem ser <10min, monorepo exige tooling sofisticado). Etapa 09: pergunta 2 (plano de deploy sequencial se torna obrigatório com dependências mapeadas). |
| Time distribuído em múltiplos fusos horários (Etapa 01, pergunta 13) | Etapa 03: pergunta 10 (processo de code review assíncrono). Etapa 09: pergunta 6 (war room precisa considerar fusos). Etapa 10: pergunta 8 (on-call rotation precisa cobrir 24h). |
