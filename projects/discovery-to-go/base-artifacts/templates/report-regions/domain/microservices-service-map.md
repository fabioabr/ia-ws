---
region-id: REG-DOM-MICRO-01
title: "Microservices Service Map"
group: domain
description: "Service diagram with boundaries, protocols, and communication patterns"
source: "Bloco #5/#7 (arch)"
schema: "Diagram serviços + boundaries + protocolos"
template-visual: "Diagram full-width"
when: web-microservices
default: false
---

# Microservices Service Map

Mapa de servicos mostrando cada microservico, seus bounded contexts, protocolos de comunicacao e dependencias. Esta visao e fundamental para entender a topologia do sistema e planejar o desenvolvimento e deploy independente de cada servico.

## Schema de dados

```yaml
service_map:
  services:
    - name: string
      bounded_context: string
      type: string               # API, Worker, BFF, Gateway
      protocol: string           # REST, gRPC, async (Kafka/SQS)
      dependencies: string[]
      database: string           # Database-per-service
      team_owner: string
```

## Exemplo

| Servico | Bounded Context | Tipo | Protocolo | Dependencias | Banco |
|---------|----------------|------|-----------|-------------|-------|
| api-gateway | Infrastructure | Gateway | REST (externo) | auth-service, bff-web | N/A |
| auth-service | Identity | API | REST | N/A (Auth0 externo) | Redis (sessoes) |
| account-service | Financial Core | API | gRPC | auth-service | PostgreSQL (schema account) |
| transaction-service | Financial Core | API | gRPC + Kafka | account-service | PostgreSQL (schema txn) |
| notification-service | Communication | Worker | Kafka consumer | N/A (SendGrid externo) | DynamoDB |
| report-service | Reporting | Worker | Async (SQS) | transaction-service | S3 (PDFs) |
| bff-web | Frontend | BFF | REST | account-service, transaction-service, report-service | N/A |
