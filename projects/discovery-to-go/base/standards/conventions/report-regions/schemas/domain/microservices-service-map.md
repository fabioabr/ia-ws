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

## Representacao Visual

### Dados de amostra

```
[Clients] --> [api-gateway]
                  |
          +-------+--------+
          |                |
     [bff-web]        [auth-service]
      /  |  \              |
     v   v   v             v
[account] [transaction] [report]    (Auth0 externo)
  |  gRPC    |  gRPC+Kafka  | SQS
  v          v              v
 [PostgreSQL] [PostgreSQL] [S3]
              |
              v (Kafka)
       [notification-service]
              |
              v
         (SendGrid)
```

**Bounded Contexts:** Infrastructure | Identity | Financial Core | Communication | Reporting | Frontend

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela de servicos com boundaries
**Tecnologia:** HTML/CSS
**Justificativa:** O mapa de servicos tem 7 microservicos com 6 atributos cada (bounded context, tipo, protocolo, dependencias, banco, owner). Uma tabela estilizada agrupada por bounded context com badges de tipo e protocolo funciona como catalogo de servicos e permite consulta rapida sem a complexidade de um diagrama de rede em HTML estatico.
**Alternativa:** Card grid agrupado por bounded context (HTML/CSS) — quando houver poucos servicos (4-5) e o foco for visualizar as dependencias entre eles.
