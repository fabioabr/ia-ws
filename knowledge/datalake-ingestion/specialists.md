---
title: Spec Pack — Datalake Ingestion
pack-id: datalake-ingestion
description: Catálogo de custom-specialists disponíveis para projetos de ingestão de dados em datalake/warehouse (medallion architecture, streaming, batch, governance). Define quando o orchestrator deve invocar cada specialist durante a reunião da Fase 1.
version: 01.00.000
status: ativo
author: claude-code
category: spec-pack
project-name: global
area: tecnologia
tags:
  - spec-pack
  - datalake-ingestion
  - custom-specialists
created: 2026-04-08 12:00
---

# Spec Pack — Datalake Ingestion

> [!info] Relação com o context-pack
> Este spec-pack é carregado em conjunto com o `knowledge/datalake-ingestion/context.md` durante o **Setup** do pipeline. Enquanto o context define **concerns** e **perguntas recomendadas**, este specialists define **quais custom-specialists estão disponíveis** para serem invocados dinamicamente pelo orchestrator.

## Catálogo

| Specialist | Domínio | Quando invocar |
|---|---|---|
| `streaming-architect` | Streaming real-time com Kafka/Kinesis/PubSub | SLA de frescor < 1 minuto, CDC, eventos em alto volume |
| `cloud-data-platform-comparison` | Databricks vs Snowflake vs BigQuery vs Redshift | Decisão de plataforma não fechada no briefing, ou reavaliação por custo/performance |
| `feature-store-architect` | Feature store para ML downstream | Gold consumida por modelos de ML, feature reuse, online/offline serving |
| `data-governance` | Catálogo e governança formal | DataHub, Unity Catalog, Collibra; linhagem automatizada; data contracts |
| `data-cost-optimization` | Otimização de custo em cloud data warehouse | Custo de warehouse/compute explodindo, consultas caras, storage ineficiente |
| `cdc-architect` | Change data capture de origens transacionais | Ingestão near-real-time a partir de Postgres/MySQL/Oracle com Debezium ou similar |
| `data-quality-engineer` | Testes e monitoramento de qualidade | Great Expectations, Soda, dbt tests; SLA de qualidade em Gold |
| `lakehouse-table-format` | Delta Lake vs Iceberg vs Hudi | Decisão de formato de tabela para data lakehouse |
| `regulated-data-finance` | Compliance de dados financeiros (Bacen, CVM) | Ingestão de dados transacionais financeiros sensíveis |
| `regulated-data-health` | Compliance de dados de saúde | Dados clínicos, prontuários, compliance ANS/LGPD-saúde |

## Prompt base por specialist

Cada specialist é invocado com o template:

```
Você é o specialist `{specialist-id}` do context-pack datalake-ingestion no Discovery Pipeline v0.5.

Domínio: {domínio da tabela}

Contexto da reunião até aqui:
{log dos blocos já cobertos}

Subtópico que pediram sua ajuda:
{descrição do ponto}

Sua missão:
1. Aprofunda o subtópico com vocabulário real do domínio (medallion, data contracts, schema evolution, idempotência, late data, etc.)
2. Sinaliza antipatterns conhecidos (overwrite de Bronze, falta de idempotência, Gold sem testes, etc.)
3. Se o customer marcar [INFERENCE] em ponto crítico (retenção, política de reprocessamento), force aprofundamento
4. Se o domínio exige especialista humano de verdade (ex: compliance setorial profundo), marque [NEEDS-HUMAN-SPECIALIST]
5. Devolve controle ao especialista fixo que te invocou
```

## Fallback genérico

Mesma regra do spec-pack `saas` — se não houver match, gera genérico e registra `[CUSTOM-SPECIALIST-GENERIC]` no log.
