---
title: Spec Pack — Web + Microservices
pack-id: web-microservices
description: Catálogo de custom-specialists disponíveis para projetos web baseados em microsserviços (boundaries, comunicação, resiliência, observabilidade). Define quando o orchestrator deve invocar cada specialist.
version: 01.00.000
status: ativo
author: claude-code
category: spec-pack
project-name: global
area: tecnologia
tags:
  - spec-pack
  - web-microservices
  - custom-specialists
created: 2026-04-08 12:00
---

# Spec Pack — Web + Microservices

> [!info] Relação com o context-pack
> Este spec-pack é carregado em conjunto com o `knowledge/web-microservices/context.md` durante o **Setup** do pipeline.

## Catálogo

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

## Prompt base por specialist

```
Você é o specialist `{specialist-id}` do context-pack web-microservices no Discovery Pipeline v0.5.

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

## Fallback genérico

Mesma regra dos outros specialists packs.
