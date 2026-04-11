---
title: Report Profile — Web + Microservices
pack-id: web-microservices
description: Perfil de relatório para projetos web com microserviços — define seções extras, métricas obrigatórias, diagramas e ênfases que o consolidator aplica ao delivery report
version: 01.00.000
status: ativo
author: claude-code
category: report-profile
area: tecnologia
tags:
  - report-profile
  - web-microservices
  - delivery
  - consolidator
created: 2026-04-11
---

# Report Profile — Web + Microservices

Perfil de relatório específico para projetos web com arquitetura de microserviços. O `consolidator` lê este arquivo durante a Fase 3 (Delivery) e faz merge com o template base (`final-report-template.md`) para montar a estrutura final do `delivery-report.md`.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este report-profile **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este profile é ignorado.

---

## Seções extras

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Mapa de Serviços e Boundaries** | Entre Tecnologia e Segurança e Privacidade e Compliance | Diagrama de serviços com boundaries claros (bounded contexts), responsabilidades de cada serviço, protocolo de comunicação (sync/async), dependências entre serviços, ownership por squad |

---

## Métricas obrigatórias

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

---

## Diagramas

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| Service map | Sim | Mapa de Serviços e Boundaries | Diagrama com serviços, boundaries, protocolos de comunicação e dependências |

---

## Ênfases por seção base

| Seção base | Ênfase Microservices |
|------------|----------------------|
| **Tecnologia e Segurança** | Destacar comunicação inter-serviço (REST/gRPC/eventos), service mesh, circuit breaker, retry policies, API gateway, distributed tracing |
| **Organização** | Aplicar Lei de Conway: estrutura de squads deve espelhar boundaries de serviços. Destacar ownership por squad e on-call rotation |
| **Análise Estratégica** | Incluir análise Build vs Buy para API gateway (Kong/Envoy/custom), observabilidade (Datadog/Grafana/custom), service mesh (Istio/Linkerd/none) |
| **Backlog Priorizado** | Priorizar por dependência: serviços fundacionais primeiro (auth, gateway, observabilidade), depois serviços de domínio, depois integrações |
| **Privacidade e Compliance** | Destacar propagação de contexto de segurança entre serviços (JWT, mTLS), auditoria de chamadas inter-serviço, dados pessoais em logs distribuídos |
| **Matriz de Riscos** | Incluir riscos específicos: cascading failures, chatty services, distributed monolith, observability blind spots, deployment ordering |

---

## Documentos Relacionados

- [[context|context-templates/web-microservices/context.md]] — Concerns e perguntas recomendadas para a Fase 1
- [[specialists|context-templates/web-microservices/specialists.md]] — Catálogo de custom-specialists para microserviços
- `dtg-artifacts/templates/customization/final-report-template.md` — Template base (11 seções obrigatórias)
