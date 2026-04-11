---
title: Discovery Blueprint — Web + Microservices
pack-id: web-microservices
description: Blueprint completo de discovery para projetos web baseados em microsserviços — guia de componentes, concerns, perguntas, antipatterns, especialistas disponíveis e perfil do delivery report. Documento único e auto-contido que o orchestrator carrega na Fase 1.
version: 02.00.000
status: ativo
author: claude-code
category: discovery-blueprint
area: tecnologia
tags:
  - discovery-blueprint
  - web-microservices
  - distributed-systems
  - context-pack
  - spec-pack
  - report-profile
created: 2026-04-11
---

# Discovery Blueprint — Web + Microservices

Documento completo e auto-contido para conduzir o discovery de um projeto web baseado em microsserviços. Organizado em **4 componentes** que representam as partes concretas da solução, seguido de antipatterns, edge cases, especialistas disponíveis e perfil do delivery report.

Serve como guia tanto para os agentes de IA (carregado pelo orchestrator na Fase 1) quanto para o humano que acompanha o processo.

---

## Quando usar este blueprint

O orchestrator deve carregar este blueprint quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Menção a microsserviços, micro-frontends, distributed systems
- Termos: API gateway, service mesh, event-driven, CQRS, saga, circuit breaker
- Sistema com múltiplos serviços interconectados (não SaaS multi-tenant puro)
- Stack mencionada: Kubernetes, Docker, Istio, Kafka, RabbitMQ, gRPC
- Necessidade de escalabilidade independente por componente
- Times distintos donos de partes diferentes do sistema (Conway's Law)
- Frontend web (SPA, PWA) consumindo backend distribuído

---

## Visão geral dos componentes

```mermaid
flowchart LR
    U["Usuários\n(Web, Mobile)"] --> A["1. Service Design\ne Boundaries"]
    A --> B["2. Comunicação\ne Resiliência"]
    B --> C["3. Infraestrutura\ne Deploy"]
    C --> D["4. Observabilidade\ne Operação"]
    D --> U

    style A fill:#2EB5F5,color:#1A1923
    style B fill:#F4AC00,color:#1A1923
    style C fill:#9B96FF,color:#1A1923
    style D fill:#0ED145,color:#1A1923
```

| # | Componente | O que define | Blocos do discovery |
|---|-----------|-------------|-------------------|
| 1 | Service Design e Boundaries | Bounded contexts, domain decomposition, ownership por squad | #5, #7 |
| 2 | Comunicação e Resiliência | Sync/async, API gateway, circuit breaker, retry, saga | #5, #7 |
| 3 | Infraestrutura e Deploy | Containers, orchestration, CI/CD, service mesh | #5, #7, #8 |
| 4 | Observabilidade e Operação | Distributed tracing, SLO/SLI, incident management | #5, #7, #8 |

---

## Componente 1 — Service Design e Boundaries

O design de serviços é o alicerce de uma arquitetura de microsserviços. Define **quais** serviços existem, **por que** cada um é um serviço separado e **quem** é dono de cada um. Boundaries mal definidos geram o temido "distributed monolith" — a complexidade de microsserviços com o acoplamento de um monolito.

### Concerns

- **Bounded contexts** — Quais são os domínios de negócio? Como mapear DDD para serviços concretos? Cada bounded context = um serviço?
- **Domain decomposition** — Critério para criar um novo serviço: capacidade de negócio, ownership de time, escalabilidade independente ou tudo junto?
- **Ownership** — Cada serviço tem um time dono claro? Conway's Law: a estrutura dos times define a estrutura dos serviços
- **Tamanho do serviço** — Micro demais (nano-serviços) ou macro demais (mini-monolitos)? Qual o critério de granularidade?
- **Database per service** — Cada serviço tem seu próprio banco? Ou há banco compartilhado (acoplamento de schema)?
- **API contracts** — Versionamento de API, backward compatibility, breaking changes — como gerenciar entre serviços?
- **Quantos serviços no MVP** — Qual o número mínimo absoluto para entregar valor? (recomendação: começar com menos)
- **Frontend** — SPA monolítica, micro-frontends, BFF (Backend for Frontend)?

### Perguntas-chave

1. Quais são os domínios de negócio? Como se agrupam as funcionalidades?
2. Como definir os boundaries de cada serviço? (DDD, capacidades de negócio, ownership de time)
3. Quantos serviços no MVP? (recomendação: o mínimo absoluto)
4. Cada serviço tem seu próprio banco ou há banco compartilhado?
5. Quem é dono de cada serviço? (time, squad, ownership claro)
6. Versionamento de API + backward compatibility — como gerenciar?
7. Como propagar mudanças breaking entre serviços?
8. Frontend: SPA monolítica, micro-frontends, BFF?
9. Testes de contrato (Pact) entre serviços?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Critério de decomposição | DDD bounded contexts / Capacidades de negócio / Ownership de time | Maturidade do time, clareza dos domínios |
| Database strategy | Database per service / Shared database / Hybrid | Nível de acoplamento aceitável, complexidade operacional |
| Granularidade | Nano-serviços / Microsserviços / Mini-monolitos modulares | Tamanho do time vs número de serviços |
| Versionamento de API | URL versioning / Header versioning / Schema evolution | Tipo de consumidor (interno vs externo) |
| Frontend architecture | SPA monolítica / Micro-frontends / BFF | Tamanho do time frontend, complexidade da UI |

### Critérios de completude

- [ ] Bounded contexts identificados e mapeados para serviços
- [ ] Critério de criação de novo serviço documentado
- [ ] Ownership de cada serviço definido (time/squad)
- [ ] Estratégia de database (per service vs shared) definida
- [ ] Estratégia de versionamento de API definida
- [ ] Número de serviços no MVP justificado (ratio time/serviços >= 2 pessoas por serviço)
- [ ] Testes de contrato planejados (Pact ou equivalente)

---

## Componente 2 — Comunicação e Resiliência

A comunicação entre serviços é o sistema nervoso da arquitetura. Define **como** os serviços se falam, **o que acontece quando falham** e **como manter consistência** em um sistema distribuído. Comunicação mal desenhada é a principal causa de cascading failures e inconsistência de dados.

### Concerns

- **Protocolo de comunicação** — REST, gRPC, GraphQL para sync? Kafka, RabbitMQ, SQS para async? Quando usar cada um?
- **Sync vs Async** — Comunicação default: síncrona ou assíncrona? Quando um, quando outro?
- **API Gateway** — Kong, Envoy, AWS API Gateway, Apigee? Rate limiting, auth edge, routing, versionamento
- **Circuit breaker** — Hystrix, Resilience4j, Istio? Thresholds, fallback, half-open
- **Retry policies** — Retry com backoff exponencial? Idempotency keys? Jitter?
- **Consistência** — Eventual consistency, saga, 2PC? Como comunicar inconsistência temporária ao usuário?
- **Saga e compensação** — Workflows que atravessam múltiplos serviços — mecanismo de compensação em caso de falha parcial
- **Backpressure** — O que acontece quando um serviço consumidor não acompanha o produtor?
- **Comunicação síncrona em cascata** — A→B→C→D, latência soma, qualquer serviço derruba todos

### Perguntas-chave

1. Comunicação default: síncrona ou assíncrona?
2. Quais protocolos de comunicação? REST, gRPC, GraphQL, eventos?
3. Precisa de API gateway? Qual? (Kong, Envoy, AWS API Gateway)
4. Como garantir consistência? (eventual consistency, saga, 2PC)
5. Tem circuit breaker? Qual é o fallback quando serviço downstream falha?
6. Retry policies com backoff exponencial + idempotency keys?
7. O que acontece quando um serviço crítico fica fora por 30 minutos?
8. RPO / RTO por serviço?
9. Como tratar race condition entre eventos chegando fora de ordem?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Comunicação default | Sync (REST/gRPC) / Async (eventos) / Híbrido | Latência requerida vs consistência |
| API Gateway | Kong / Envoy / AWS API Gateway / Apigee / Custom | Cloud provider, features, custo |
| Circuit breaker | Resilience4j / Istio / Custom | Stack, complexidade, service mesh |
| Consistência | Eventual + saga / 2PC / Sem transação distribuída | Criticidade da operação |
| Event streaming | Kafka / RabbitMQ / SQS / Pulsar | Volume, ordering, exactly-once |

### Critérios de completude

- [ ] Protocolo de comunicação definido por tipo de interação (sync vs async)
- [ ] API gateway selecionado (ou justificativa para não usar)
- [ ] Circuit breaker e retry policies definidos
- [ ] Estratégia de consistência documentada (saga, eventual, 2PC)
- [ ] Fallback definido para indisponibilidade de serviços críticos
- [ ] Backpressure strategy documentada
- [ ] RPO / RTO por serviço definidos

---

## Componente 3 — Infraestrutura e Deploy

A infraestrutura sustenta toda a operação dos microsserviços. Define **onde** rodam, **como** são deployados e **com que frequência**. Decisões erradas aqui geram overhead operacional insustentável — containers sem orquestração, deploys manuais, service mesh sem necessidade.

### Concerns

- **Containerização** — Docker? Buildpacks? Imagem base padronizada?
- **Orquestração** — Kubernetes (EKS/GKE/AKS), ECS, Nomad? Managed vs self-hosted?
- **CI/CD** — Pipeline por serviço? Monorepo vs polyrepo? Canary deploy, blue-green, rolling update?
- **Service mesh** — Istio, Linkerd, Consul Connect? Necessário agora ou v2?
- **Runtime** — Linguagens permitidas (poliglota vs restrita): Node, JVM, .NET, Go?
- **Autenticação inter-serviço** — mTLS, JWT propagation, OAuth2?
- **Secrets management** — Vault, AWS Secrets Manager, K8s Secrets?
- **Network policies** — Zero-trust? Microsegmentação? Whitelist entre serviços?
- **Escalabilidade** — HPA, VPA, KEDA? Critérios de autoscaling por serviço?

### Perguntas-chave

1. Onde rodam os serviços? (Kubernetes managed, ECS, Nomad, VMs)
2. CI/CD: monorepo ou polyrepo? Pipeline independente por serviço?
3. Canary deploy, blue-green ou rolling update?
4. Service mesh: necessário agora ou v2?
5. Linguagens permitidas: poliglota ou stack restrita?
6. Como autenticar entre serviços? (mTLS, JWT, OAuth2)
7. Secrets management: como e onde?
8. Escalabilidade: autoscaling por serviço? Critérios?
9. Como propagar uma mudança de infra para todos os serviços?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Orquestrador | EKS / GKE / AKS / ECS / Nomad | Cloud provider, skills do time, custo |
| CI/CD strategy | Monorepo + pipeline por path / Polyrepo + pipeline por repo | Tamanho do time, dependências entre serviços |
| Deploy strategy | Canary / Blue-green / Rolling update | Criticidade, rollback speed |
| Service mesh | Istio / Linkerd / Consul / None (v2) | Complexidade atual vs benefício |
| Auth inter-serviço | mTLS / JWT propagation / OAuth2 M2M | Política de segurança, service mesh |

### Critérios de completude

- [ ] Plataforma de orquestração definida (managed vs self-hosted)
- [ ] Estratégia de CI/CD documentada (monorepo vs polyrepo, pipeline por serviço)
- [ ] Deploy strategy definida (canary, blue-green, rolling)
- [ ] Service mesh: decisão de usar ou postergar documentada
- [ ] Autenticação inter-serviço definida
- [ ] Secrets management definido
- [ ] Network policies e zero-trust documentados

---

## Componente 4 — Observabilidade e Operação

A observabilidade é o que permite **entender** e **operar** um sistema distribuído em produção. Sem distributed tracing, debugar latência entre serviços é impossível. Sem SLO/SLI, não há como medir se o sistema está saudável. Sem incident management, falhas viram crises.

### Concerns

- **Distributed tracing** — OpenTelemetry, Jaeger, Zipkin? Propagação de trace ID entre serviços (inclusive async)?
- **Métricas** — Prometheus, Datadog, CloudWatch? RED metrics (Rate, Errors, Duration) por serviço?
- **Logs estruturados** — Formato (JSON), correlação com trace ID, agregação centralizada (ELK, Loki, CloudWatch)?
- **SLO/SLI** — Definidos por serviço? Error budgets? Alertas baseados em burn rate?
- **Alertas** — Quem é notificado? PagerDuty, OpsGenie? Escalonamento?
- **Incident management** — Runbooks por serviço? Post-mortem obrigatório? Blameless culture?
- **Chaos engineering** — Chaos Monkey, game days? Teste proativo de resiliência?
- **Observabilidade de custos** — Custo por serviço? Custo de observabilidade (Datadog/NewRelic/Grafana Cloud)?
- **On-call** — Rotação de on-call: 24x7? Business hours? Por serviço ou por squad?

### Perguntas-chave

1. Tem distributed tracing? (OpenTelemetry, Jaeger, Zipkin)
2. Como correlacionar logs entre serviços? (trace ID propagation)
3. SLO/SLI definidos por serviço? Error budgets?
4. Quem é o on-call? 24x7 ou business hours? Por serviço ou por squad?
5. Tem runbooks por serviço para incident management?
6. Chaos engineering: faz game days? Chaos Monkey?
7. Como detectar problemas de latência entre serviços?
8. Custo mensal estimado de observabilidade? (Datadog, NewRelic, Grafana Cloud)
9. Post-mortem obrigatório após incidentes? Blameless culture?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Stack de observabilidade | Datadog / Honeycomb / Grafana stack (self-hosted) | Custo, features, managed vs self-hosted |
| Distributed tracing | OpenTelemetry + Jaeger / Datadog APM / X-Ray | Integração com stack, sampling strategy |
| SLO/SLI | Por serviço / Por jornada de usuário / Global | Maturidade, número de serviços |
| Alerting | PagerDuty / OpsGenie / Custom | On-call process, integração |
| Chaos engineering | Chaos Monkey / Litmus / Game days manuais / Nenhum (v2) | Maturidade operacional |

### Critérios de completude

- [ ] Stack de observabilidade definida (métricas, logs, traces)
- [ ] Distributed tracing implementado com propagação de trace ID
- [ ] SLO/SLI definidos por serviço ou jornada de usuário
- [ ] On-call rotation definida (quem, quando, escalonamento)
- [ ] Runbooks por serviço crítico planejados
- [ ] Custo de observabilidade estimado
- [ ] Chaos engineering: decisão de adotar ou postergar documentada

---

## Concerns transversais — Produto e Organização

Além dos 4 componentes técnicos, o discovery precisa cobrir aspectos de produto e organização que atravessam todos os componentes. Estes são endereçados principalmente nos blocos #1 a #4 pelo **po**.

### Personas e jornadas

- Personas e jornadas críticas
- Volumetria esperada (RPS, concurrent users, picos)
- Dependências externas (parceiros, APIs de terceiros)

### Valor e métricas

- OKRs mensuráveis: disponibilidade (SLA/SLO/SLI), latência alvo, throughput
- ROI esperado
- Roadmap de funcionalidades por capability
- Sinais de resposta incompleta:
  - "Pode ser microsserviços" sem volumetria
  - Sem dono claro por serviço / capability
  - Sem definição de SLA/SLO
  - Time muito pequeno para número de serviços proposto

### Organização e Conway's Law

- **Estrutura organizacional** — Conway's Law: times definem boundaries de serviço. A estrutura dos squads deve espelhar a arquitetura desejada
- Tamanho, senioridade e experiência prévia do time com distribuído
- Critério de criação de novo serviço (quando vale o overhead)
- On-call pós-MVP (24x7? business hours?)
- Ownership por squad e on-call rotation

---

## Concerns transversais — Privacidade (bloco #6)

O **cyber-security-architect** sempre roda este bloco. Em sistemas web-microservices, o **modo profundo é o caso comum** — sistemas distribuídos costumam manipular dados pessoais de usuários/clientes em múltiplos serviços, o que amplifica a complexidade de compliance (rastrear PII distribuída, direito ao esquecimento cross-service, propagação de consentimento). Modo magro é raro e só se aplica a serviços puramente técnicos sem contato com dados de pessoa.

### Concerns específicos de distributed systems

- Dados pessoais distribuídos entre serviços — como rastrear linhagem
- LGPD com múltiplos controladores / operadores entre serviços
- Direito ao esquecimento: como apagar um titular quando seus dados estão em 8 serviços diferentes?
- Propagação de consentimento entre serviços
- Audit trail distribuído (quem acessou qual dado em qual serviço)
- Criptografia inter-serviço vs no storage
- mTLS para autenticação inter-serviço (defesa em profundidade)
- Propagação de contexto de segurança entre serviços (JWT, mTLS)
- Auditoria de chamadas inter-serviço
- Dados pessoais em logs distribuídos

---

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|---|---|
| 1 | **Microsserviços antes de validar produto** | Overhead operacional sem benefício; monolito modular cobre o MVP |
| 2 | **Distributed monolith** | Microsserviços que precisam ser deployados juntos = pior dos dois mundos |
| 3 | **Banco compartilhado entre serviços** | Acoplamento de schema, deploy coupling, contenção |
| 4 | **Sem testes de contrato (Pact)** | Mudança em A quebra B em produção |
| 5 | **Comunicação síncrona em cascata** | A→B→C→D, latência soma, qualquer serviço derruba todos |
| 6 | **Sem circuit breaker** | Falha em cascata trava o sistema inteiro |
| 7 | **Sem distributed tracing** | Impossível debugar latência entre serviços |
| 8 | **Time menor que serviço** | 10 serviços com 4 pessoas = ninguém mantém nada bem |
| 9 | **Versionamento de API ad-hoc** | Quebras silenciosas para clientes |
| 10 | **Service mesh sem necessidade** | Complexidade alta para problema que não existe |
| 11 | **Eventual consistency sem comunicar ao usuário** | Usuário vê inconsistência, perde confiança |
| 12 | **Saga sem mecanismo de compensação** | Falha parcial deixa dados em estado inconsistente |

---

## Edge cases para o 10th-man verificar

- O que acontece quando um serviço crítico fica fora por 30 minutos?
- Como propagar uma mudança breaking de API para 10 serviços consumidores?
- Saga falha no passo 5 de 7 — como rollback?
- Database de um serviço corrompe — como restaurar sem afetar os outros?
- Time dono de serviço inteiro sai da empresa — quem mantém?
- Volume cresce 10x em um dia — qual é o gargalo primeiro?
- Ataque DDoS no API gateway — como mitigar?
- Bug em service mesh derruba toda a comunicação — fallback?
- Deploy de versão nova quebra contrato com mobile que não atualizou — quem paga o pato?
- Race condition entre eventos chegando fora de ordem em consumidor?
- Migração de monolito legado para microsserviços — strangler fig ou big bang?
- LGPD pede exclusão de pessoa — como remover dados de 8 serviços diferentes?
- Latência inter-AZ explode em horário de pico — como detectar e mitigar?

---

## Custom-specialists disponíveis

Quando po, solution-architect ou cyber-security-architect precisarem de profundidade em subtópico específico durante a reunião, o orchestrator pode invocar um dos specialists abaixo:

| Specialist | Domínio | Quando invocar |
|---|---|---|
| `monolith-to-microservices` | Estratégia de migração legada | Briefing menciona monolito existente que precisa ser decomposto (strangler fig, bounded contexts) |
| `event-streaming-architecture` | Event-driven com Kafka em escala | Comunicação assíncrona via eventos em volume alto, exactly-once, saga via eventos |
| `service-mesh-architect` | Service mesh complexo (Istio, Linkerd, Consul) | Observabilidade, mTLS, traffic management, canary em escala |
| `multi-cloud-architecture` | Multi-cloud ou hybrid cloud | Requisito de não-lock-in, BCP entre clouds, data gravity entre regiões |
| `performance-engineering` | Performance crítica, baixa latência | SLA < 50ms p99 inter-serviço, otimização de hot path distribuído |
| `observability-architect` | Observabilidade distribuída avançada | Distributed tracing, logs correlacionados, SLO/SLI por serviço, error budgets |
| `api-gateway-architect` | API gateway e edge services | Kong, Apigee, AWS API Gateway, rate limit, auth edge, versionamento de API pública |
| `saga-architect` | Transações distribuídas (saga, outbox) | Workflows que atravessam múltiplos serviços com compensação |
| `regulated-distributed-systems-finance` | Compliance financeiro distribuído | Sistemas distribuídos com compliance Bacen/PCI-DSS |
| `regulated-distributed-systems-health` | Compliance saúde distribuído | Sistemas distribuídos com dados clínicos |
| `contract-testing-specialist` | Testes de contrato entre serviços | Pact, Spring Cloud Contract, consumer-driven contracts |
| `chaos-engineering-specialist` | Chaos engineering e resiliência | Chaos Monkey, game days, teste de resiliência proativo |
| `frontend-architecture` | Frontend complexo (micro-frontends, BFF) | Micro-frontends, BFF, module federation |

> [!info] Fallback genérico
> Se o subtópico não casa com nenhum specialist acima, o orchestrator gera um specialist genérico e registra `[CUSTOM-SPECIALIST-GENERIC]` no log.

### Prompt base de invocação

```
Você é o specialist `{specialist-id}` do blueprint web-microservices no Discovery Pipeline v0.5.

Domínio: {domínio da tabela}

Contexto da reunião até aqui:
{log dos blocos já cobertos}

Subtópico que pediram sua ajuda:
{descrição do ponto}

Sua missão:
1. Aprofunda o subtópico com vocabulário real do domínio (bounded context, saga, outbox, circuit breaker, backpressure, etc.)
2. Sinaliza antipatterns conhecidos (distributed monolith, banco compartilhado, comunicação síncrona em cascata, etc.)
3. Se o customer marcar [INFERENCE] em ponto crítico (tamanho do time vs nº de serviços, testes de contrato, observabilidade), force aprofundamento
4. Se o domínio exige especialista humano de verdade, marque [NEEDS-HUMAN-SPECIALIST]
5. Devolve controle ao especialista fixo que te invocou
```

---

## Perfil do Delivery Report

Configurações específicas que o `consolidator` aplica ao delivery report na Fase 3 para projetos deste tipo.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este report-profile **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este profile é ignorado.

### Seções extras no relatório

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Mapa de Serviços e Boundaries** | Entre Tecnologia e Segurança e Privacidade e Compliance | Diagrama de serviços com boundaries claros (bounded contexts), responsabilidades de cada serviço, protocolo de comunicação (sync/async), dependências entre serviços, ownership por squad |

### Métricas obrigatórias no relatório

| Métrica | Onde incluir | Descrição |
|---------|-------------|-----------|
| Latência P95 / P99 | Métricas-chave + Mapa de Serviços | Latência por jornada crítica do usuário |
| Disponibilidade alvo | Métricas-chave | SLA de uptime (3 9s, 4 9s) por serviço crítico |
| Throughput máximo testado | Métricas-chave | Requisições/segundo sustentáveis por serviço |
| MTTR | Métricas-chave | Mean time to recovery — tempo médio para restaurar serviço após falha |
| MTBF | Métricas-chave | Mean time between failures — tempo médio entre falhas |
| Cobertura de testes de contrato | Métricas-chave | % de contratos entre serviços com testes automatizados |
| Custo de infra mensal | Métricas-chave + Análise Estratégica | Custo de infraestrutura por serviço/cluster |
| Custo de observabilidade | Métricas-chave | Custo mensal de Datadog/NewRelic/Grafana Cloud por volume |
| Ratio time/serviços | Métricas-chave + Organização | Número de pessoas por serviço (recomendação: >= 2 por serviço) |

### Diagramas obrigatórios no relatório

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| Service map | Sim | Mapa de Serviços e Boundaries | Diagrama com serviços, boundaries, protocolos de comunicação e dependências |

### Ênfases por seção base

| Seção base | Ênfase Microservices |
|------------|----------------------|
| **Tecnologia e Segurança** | Destacar comunicação inter-serviço (REST/gRPC/eventos), service mesh, circuit breaker, retry policies, API gateway, distributed tracing |
| **Organização** | Aplicar Lei de Conway: estrutura de squads deve espelhar boundaries de serviços. Destacar ownership por squad e on-call rotation |
| **Análise Estratégica** | Incluir análise Build vs Buy para API gateway (Kong/Envoy/custom), observabilidade (Datadog/Grafana/custom), service mesh (Istio/Linkerd/none) |
| **Backlog Priorizado** | Priorizar por dependência: serviços fundacionais primeiro (auth, gateway, observabilidade), depois serviços de domínio, depois integrações |
| **Privacidade e Compliance** | Destacar propagação de contexto de segurança entre serviços (JWT, mTLS), auditoria de chamadas inter-serviço, dados pessoais em logs distribuídos |
| **Matriz de Riscos** | Incluir riscos específicos: cascading failures, chatty services, distributed monolith, observability blind spots, deployment ordering |

---

## Mapeamento para os 8 Blocos do Discovery

| Componente | Bloco(s) principal(is) | Agente responsável |
|------------|----------------------|-------------------|
| **1. Service Design e Boundaries** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro) | solution-architect |
| **2. Comunicação e Resiliência** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro) | solution-architect |
| **3. Infraestrutura e Deploy** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro), #8 (TCO) | solution-architect |
| **4. Observabilidade e Operação** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro), #8 (TCO) | solution-architect |

> [!tip] Concerns transversais
> Alguns temas atravessam todos os componentes:
> - **Privacidade (bloco #6)** — PII aparece em múltiplos serviços, precisa de rastreamento de linhagem, propagação de consentimento e mecanismo de exclusão cross-service
> - **Custo (bloco #8)** — Cada componente tem custo próprio (compute, networking/egress, observabilidade, licenças, on-call rotation)
> - **Organização (blocos #1-#4)** — Conway's Law, ownership por squad, on-call rotation, experiência prévia com distribuído

---

## Regions do Delivery Report

Regions de informação que o `consolidator` deve gerar no delivery report para projetos web-microservices. Referência completa no [Information Regions Catalog](../../projects/discovery-to-go/base-artifacts/templates/report-regions/information-regions.md).

### Obrigatórias

Regions com `Default: Todos` no catálogo, mais as de privacidade (web apps tipicamente manipulam PII).

#### Executivo

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-EXEC-01 | Overview one-pager | Texto narrativo + bullets | Hero card full-width |
| REG-EXEC-02 | Product brief | Texto estruturado | Card com seções |
| REG-EXEC-03 | Decisão de continuidade | Tabela de riscos + veredicto | Card com status badges |
| REG-EXEC-04 | Próximos passos | Tabela (ação, responsável, prazo) | Table com checkboxes |

#### Produto

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-PROD-01 | Problema e contexto | Texto + métricas | Card com callout de métrica |
| REG-PROD-02 | Personas | Lista de personas (nome, perfil, jobs, dores) | Grid de persona cards |
| REG-PROD-04 | Proposta de valor | Texto estruturado (para/que/é um/que) | Card com highlight |
| REG-PROD-05 | OKRs e ROI | Tabela (objetivo, key result, target, prazo) | Table com progress indicators |
| REG-PROD-07 | Escopo | Objetivo + duas listas (dentro/fora) + hipótese | Card com objetivo + split list (in/out) |

#### Organização

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-ORG-01 | Mapa de stakeholders | Tabela (nome, papel, influência, interesse) | Table com badges |
| REG-ORG-02 | Estrutura de equipe | Tabela (papel, dedicação, fase) | Table ou org chart |

#### Técnico

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-TECH-01 | Stack tecnológica | Tabela (tecnologia, camada, justificativa) | Table com badges |
| REG-TECH-02 | Integrações | Tabela (sistema, protocolo, direção, volume) | Table ou diagram |
| REG-TECH-03 | Arquitetura macro | Diagrama Mermaid | Diagram full-width |
| REG-TECH-06 | Build vs Buy | Tabela (componente, opções, veredicto, justificativa) | Table com verdict badges |

#### Segurança

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-SEC-01 | Classificação de dados | Tabela (dado, classificação, tratamento) | Table com color-coded badges |
| REG-SEC-02 | Autenticação e autorização | Texto + tabela | Card com checklist |
| REG-SEC-04 | Compliance e regulação | Tabela (regulação, status, gap, ação) | Table com status badges |

#### Privacidade

Web apps baseadas em microsserviços tipicamente manipulam PII de usuários/clientes em múltiplos serviços — todas as regions `Quando há PII` são obrigatórias neste blueprint.

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-PRIV-01 | Dados pessoais mapeados | Tabela (dado, local, acesso, base legal) | Table detalhada |
| REG-PRIV-02 | Base legal LGPD | Tabela (tratamento, base legal, justificativa) | Table com badges |
| REG-PRIV-03 | DPO e responsabilidades | Texto + contato | Card simples |
| REG-PRIV-04 | Política de retenção | Tabela (dado, retenção, processo) | Table simples |

#### Financeiro

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-FIN-01 | TCO 3 anos | Tabela (categoria, ano 1, ano 2, ano 3, total) + faixa de sensibilidade | Table + stat card (total) |
| REG-FIN-05 | Estimativa de esforço | Tabela (épico, complexidade, estimativa, premissas) | Table com badges |

#### Riscos

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-RISK-01 | Matriz de riscos | Tabela (risco, probabilidade, impacto, score, mitigação, dono) | Table com heatmap badges |
| REG-RISK-02 | Riscos técnicos | Tabela | Table com severity |
| REG-RISK-03 | Hipóteses críticas não validadas | Tabela (hipótese, risco se falsa, como validar, prazo) | Table com alert style |

#### Qualidade

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-QUAL-01 | Score do auditor | Tabela (dimensão, nota, piso, status) | Stat cards ou radar chart |
| REG-QUAL-02 | Questões do 10th-man | Lista de questões com severidade | Card list com severity badges |

#### Backlog

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-BACK-01 | Épicos priorizados | Tabela (épico, narrativa, prioridade, estimativa) | Table com priority badges |

#### Métricas

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-METR-01 | KPIs de negócio | Tabela (KPI, valor atual, target, prazo) | Stat cards ou table |

#### Narrativa

| ID | Nome | Schema | Template visual |
|----|------|--------|-----------------|
| REG-NARR-01 | Como chegamos aqui | Texto narrativo + timeline | Timeline vertical |

### Domain-specific

Regions exclusivas do context-template `web-microservices`.

| ID | Nome | Descrição | Template visual |
|----|------|-----------|-----------------|
| REG-DOM-MICRO-01 | Mapa de serviços | Diagrama de serviços com boundaries, protocolos, ownership | Diagram full-width |
| REG-DOM-MICRO-02 | Resiliência inter-serviço | Circuit breaker, retry, saga, DLQ, timeout policies | Table com patterns |

### Opcionais

Regions que o consolidator pode incluir quando o discovery produzir informação suficiente.

| ID | Nome | Quando incluir |
|----|------|----------------|
| REG-PROD-03 | Jornadas de usuário | Jornadas mapeadas em detalhe |
| REG-PROD-06 | Modelo de negócio | Projeto com monetização/pricing |
| REG-PROD-08 | Roadmap | Faseamento definido além do MVP |
| REG-PROD-09 | Visão do produto | Visão de longo prazo articulada |
| REG-ORG-03 | RACI | Matriz de responsabilidades definida |
| REG-ORG-04 | Metodologia | Metodologia de desenvolvimento definida |
| REG-ORG-05 | On-call e sustentação | Modelo de sustentação pós-MVP definido |
| REG-TECH-04 | Arquitetura de containers | C4 L2 — containers internos detalhados |
| REG-TECH-05 | ADRs | Architecture Decision Records documentados |
| REG-TECH-07 | Requisitos não-funcionais | NFRs explícitos com SLAs |
| REG-SEC-03 | Criptografia | Detalhamento de criptografia at-rest/in-transit |
| REG-PRIV-05 | Direito ao esquecimento | Processo de exclusão cross-service detalhado |
| REG-PRIV-06 | Sub-operadores | Terceiros que processam dados pessoais |
| REG-FIN-02 | Break-even analysis | Análise de ponto de equilíbrio |
| REG-FIN-03 | Custo por componente | Breakdown de custo por serviço/cluster |
| REG-RISK-04 | Análise de viabilidade | Viabilidade por dimensão |
| REG-QUAL-03 | Gaps identificados | Lacunas no discovery |
| REG-QUAL-04 | Checklist de conclusão | Status de critérios de completude |
| REG-BACK-02 | User stories de alto nível | Stories por épico |
| REG-BACK-03 | Dependências | Dependências entre épicos |
| REG-BACK-04 | Critérios de Go/No-Go | Métricas de go/no-go |
| REG-METR-02 | KPIs técnicos | Métricas de saúde técnica |
| REG-METR-03 | SLAs e SLOs | SLO/SLI por serviço |
| REG-METR-04 | Targets por fase | Metas por fase do roadmap |
| REG-METR-05 | DORA metrics | Deploy frequency, lead time, MTTR, change failure rate |
| REG-NARR-02 | Condições para prosseguir | Pré-requisitos antes de iniciar desenvolvimento |
| REG-NARR-03 | Assinaturas de aprovação | Sign-off formal |
| REG-PESQ-01 | Relatório de entrevistas | Entrevistas realizadas durante o discovery |
| REG-PESQ-02 | Citações representativas | Quotes de alta relevância |
| REG-PESQ-03 | Mapa de oportunidades | Opportunity Solution Tree |
| REG-PESQ-04 | Dados quantitativos | Métricas quantitativas identificadas |
| REG-PESQ-05 | Source tag summary | Distribuição por fonte (BRIEFING, RAG, INFERENCE) |

### Resumo quantitativo

| Classificação | Quantidade |
|---------------|------------|
| Obrigatórias | 32 |
| Domain-specific | 2 |
| Opcionais | 31 |
| **Total** | **65** |
