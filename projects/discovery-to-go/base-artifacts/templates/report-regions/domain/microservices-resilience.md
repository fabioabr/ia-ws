---
region-id: REG-DOM-MICRO-02
title: "Microservices Resilience"
group: domain
description: "Resilience patterns including circuit breaker, retry, saga, and DLQ strategies"
source: "Bloco #5/#7 (arch)"
schema: "Circuit breaker + retry + saga + DLQ"
template-visual: "Table com patterns"
when: web-microservices
default: false
---

# Microservices Resilience

Define os padroes de resiliencia adotados na arquitetura de microservicos, incluindo circuit breaker, retry, saga e dead letter queues. Esses padroes sao essenciais para garantir que falhas em um servico nao se propaguem para todo o sistema.

## Schema de dados

```yaml
resilience_patterns:
  patterns:
    - pattern: string            # Circuit Breaker, Retry, Saga, DLQ, Bulkhead, etc.
      where_applied: string      # Onde e aplicado
      tool: string               # Biblioteca/ferramenta
      configuration: string      # Configuracao principal
      fallback: string           # Comportamento em caso de falha
```

## Exemplo

| Pattern | Onde Aplicado | Ferramenta | Configuracao | Fallback |
|---------|-------------|-----------|-------------|----------|
| Circuit Breaker | Chamadas ao Open Finance API | Resilience4j | Threshold: 50% falhas em 10 requests; timeout: 60s | Retornar dados cached (ate 15min) |
| Retry | Chamadas entre microservicos (gRPC) | gRPC built-in | 3 tentativas com exponential backoff (1s, 2s, 4s) | Circuit breaker assume |
| Saga (Coreografia) | Criacao de conta + primeira sincronizacao | Kafka events | Eventos compensatorios para rollback | Conta criada em estado "pendente" |
| DLQ | Eventos Kafka que falharam processamento | AWS SQS DLQ | Max 3 retries; mensagens vao para DLQ | Alerta no Slack + reprocessamento manual |
| Bulkhead | Thread pools por servico externo | Resilience4j | Max 10 threads para Open Finance; 5 para Stripe | Rejeitar request com 503 |
| Timeout | Todas as chamadas HTTP externas | Axios/gRPC config | 5s para APIs internas; 10s para APIs externas | Erro retornado ao cliente com retry sugerido |

## Representacao Visual

### Dados de amostra

| Pattern | Aplicacao | Config Principal | Fallback |
|---------|----------|-----------------|----------|
| Circuit Breaker | Open Finance API | 50% falhas / 10 req | Cache 15min |
| Retry | gRPC inter-service | 3x exp. backoff | Circuit breaker |
| Saga | Criacao de conta | Eventos compensatorios | Estado "pendente" |
| DLQ | Kafka consumer | Max 3 retries | Alerta + manual |
| Bulkhead | Pools por servico | 10 threads (OF), 5 (Stripe) | 503 |
| Timeout | HTTP externas | 5s interno, 10s externo | Erro + retry hint |

```
Request --> [Timeout] --> [Retry] --> [Circuit Breaker] --> Servico Externo
                                          |
                                     (aberto?)
                                          |
                                     [Fallback/Cache]

Kafka Event --> [Consumer] --> [Retry 3x] --> [DLQ] --> [Alerta Slack]
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada pattern com contexto de aplicacao e justificativa | ADRs, documentacao de arquitetura |
| Tabela | Tabela com patterns, onde aplicado, configuracao e fallback | Referencia tecnica, checklists de resiliencia |
| Matriz de patterns | Grid mostrando quais patterns estao aplicados em quais servicos/integracoes | Analise de cobertura de resiliencia, revisoes de arquitetura |
| Diagrama de fluxo | Fluxo mostrando a cadeia de patterns (timeout, retry, circuit breaker, fallback) e como interagem | Onboarding tecnico, troubleshooting, documentacao de comportamento em falha |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
