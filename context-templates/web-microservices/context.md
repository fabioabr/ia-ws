---
title: Context Pack — Web + Microservices
pack-id: web-microservices
description: Context pack para sistemas web baseados em microsserviços. Cobre boundaries de serviços, comunicação, resiliência, dados distribuídos, observabilidade, deploy e versionamento de API.
version: 00.01.000
status: ativo
author: claude-code
category: context-pack
project-name: global
area: tecnologia
tags:
  - context-pack
  - web
  - microservices
  - distributed-systems
created: 2026-04-07 12:00
---

# Context Pack — Web + Microservices

## Quando usar

O orchestrator deve carregar este pack quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Menção a microsserviços, micro-frontends, distributed systems
- Termos: API gateway, service mesh, event-driven, CQRS, saga, circuit breaker
- Sistema com múltiplos serviços interconectados (não SaaS multi-tenant puro)
- Stack mencionada: Kubernetes, Docker, Istio, Kafka, RabbitMQ, gRPC
- Necessidade de escalabilidade independente por componente
- Times distintos donos de partes diferentes do sistema (Conway's Law)
- Frontend web (SPA, PWA) consumindo backend distribuído

## Concerns por eixo

### Product + Valor + Organização (po) — blocos 1-4

**Tópicos obrigatórios do checklist:**

- Personas e jornadas críticas
- Volumetria esperada (RPS, concurrent users, picos)
- OKRs mensuráveis: disponibilidade (SLA/SLO/SLI), latência alvo, throughput
- ROI esperado
- Roadmap de funcionalidades por capability
- **Estrutura organizacional** (Conway's Law — times definem boundaries de serviço)
- Tamanho, senioridade e experiência prévia do time com distribuído
- On-call pós-MVP (24x7? business hours?)
- Dependências externas (parceiros, APIs de terceiros)
- Critério de criação de novo serviço (quando vale o overhead)

**Sinais de resposta incompleta:**
- "Pode ser microsserviços" sem volumetria
- Sem dono claro por serviço / capability
- Sem definição de SLA/SLO
- Time muito pequeno para número de serviços proposto

### Técnico (solution-architect) — blocos 5, 7, 8

**Categorias aplicáveis:**

- **Tecnologia:** linguagens permitidas (poliglota × restrita), frameworks, runtime (Node, JVM, .NET, Go), orquestrador (k8s, ECS, Nomad), service mesh, API gateway
- **Segurança:** autenticação inter-serviço (mTLS, JWT, OAuth), authorization (RBAC, ABAC), secrets management, network policies, zero-trust
- **Arquitetura:** boundaries de serviços (DDD/capacidades/ownership), comunicação (sync × async, REST/gRPC/GraphQL/eventos), padrões (CQRS, saga, BFF, strangler fig, circuit breaker, bulkhead), database per service × shared
- **Integrações:** API gateway, service mesh (Istio/Linkerd/Consul), event streaming (Kafka/Pulsar)
- **Observabilidade:** métricas, logs estruturados, traces distribuídos correlacionados, alertas, chaos engineering
- **Build vs Buy:** orquestração k8s (managed EKS/GKE/AKS vs self-hosted), service mesh (Istio managed vs self-hosted), observabilidade (Datadog/Honeycomb vs Grafana stack self-hosted)
- **TCO:** compute + storage + networking (egress entre AZs pode explodir) + observabilidade + licenças + equipe + on-call rotation

**Perguntas recomendadas:**

- Quantos serviços no MVP? (recomendação: o mínimo absoluto)
- Como definir os boundaries (DDD, capacidades de negócio, ownership)?
- Comunicação default: síncrona ou assíncrona?
- Como garantir consistência (eventual consistency, saga, 2PC)?
- Cada serviço tem seu próprio banco?
- Versionamento de API + backward compatibility?
- Service mesh: necessário agora ou v2?
- Como propagar mudanças breaking entre serviços?
- Testes de contrato (Pact) entre serviços?
- RPO / RTO por serviço?

### Privacidade (cyber-security-architect, **obrigatório**) — bloco 6

O cyber-security-architect sempre roda este bloco. Em sistemas web-microservices, o **modo profundo é o caso comum** — sistemas distribuídos costumam manipular dados pessoais de usuários/clientes em múltiplos serviços, o que amplifica a complexidade de compliance (rastrear PII distribuída, direito ao esquecimento cross-service, propagação de consentimento). Modo magro é raro e só se aplica a serviços puramente técnicos sem contato com dados de pessoa.

**Concerns específicos distributed systems:**

- Dados pessoais distribuídos entre serviços — como rastrear linhagem
- LGPD com múltiplos controladores / operadores entre serviços
- Direito ao esquecimento: como apagar um titular quando seus dados estão em 8 serviços diferentes?
- Propagação de consentimento entre serviços
- Audit trail distribuído (quem acessou qual dado em qual serviço)
- Criptografia inter-serviço vs no storage
- mTLS para autenticação inter-serviço (defesa em profundidade)

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

## Custom-specialists disponíveis

O catálogo de custom-specialists para projetos web-microservices está no **spec-pack** correspondente: [[../web-microservices/specialists|context-templates/web-microservices/specialists.md]]. O orchestrator carrega o spec-pack junto com este context-pack durante o Setup.

Lembrete: LGPD/Privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect`.
| Frontend complexo (micro-frontends, BFF) | `frontend-architecture` |

## Report Profile

Seções extras, métricas obrigatórias e diagramas específicos para o delivery report estão definidos em [[report-profile]].
