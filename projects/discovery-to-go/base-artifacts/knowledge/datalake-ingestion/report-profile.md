---
title: Report Profile — Datalake Ingestion
pack-id: datalake-ingestion
description: Perfil de relatório para projetos de ingestão de dados e datalake — define seções extras, métricas obrigatórias, diagramas e ênfases que o consolidator aplica ao delivery report
version: 01.00.000
status: ativo
author: claude-code
category: report-profile
area: tecnologia
tags:
  - report-profile
  - datalake-ingestion
  - delivery
  - consolidator
created: 2026-04-11
---

# Report Profile — Datalake Ingestion

Perfil de relatório específico para projetos de ingestão de dados e datalake. O `consolidator` lê este arquivo durante a Fase 3 (Delivery) e faz merge com o template base (`final-report-template.md`) para montar a estrutura final do `delivery-report.md`.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este report-profile **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este profile é ignorado.

---

## Seções extras

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Arquitetura de Dados (Medallion)** | Entre Tecnologia e Segurança e Privacidade e Compliance | Diagrama Bronze → Silver → Gold com descrição de cada camada, transformações aplicadas, políticas de retenção por camada, estratégia de particionamento |

---

## Métricas obrigatórias

| Métrica | Onde incluir | Descrição |
|---------|-------------|-----------|
| Volume estimado por camada | Métricas-chave + Arquitetura de Dados | GB/TB por dia esperados em cada camada (Bronze, Silver, Gold) |
| Freshness SLA | Métricas-chave | Tempo máximo entre dado chegar no source e estar disponível na Gold |
| Custo mensal estimado | Métricas-chave + Análise Estratégica | Compute + storage por camada |
| Tempo de reprocessamento | Métricas-chave | Tempo para reprocessar todo o histórico de uma tabela/pipeline |
| Cobertura de testes de qualidade | Métricas-chave | % de tabelas Gold com testes de qualidade automatizados |
| Cobertura de linhagem | Métricas-chave | % de tabelas com lineage rastreável end-to-end |

---

## Diagramas

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| Medallion architecture | Sim | Arquitetura de Dados | Fluxo Bronze → Silver → Gold com fontes, transformações e consumidores |

---

## Ênfases por seção base

| Seção base | Ênfase Datalake |
|------------|-----------------|
| **Tecnologia e Segurança** | Destacar stack de ingestão (Spark, Airflow, dbt, Kafka), estratégia de particionamento, formato de armazenamento (Parquet, Delta, Iceberg) |
| **Privacidade e Compliance** | Destacar mascaramento de PII por camada (Bronze raw → Silver mascarado), linhagem de dados pessoais, políticas de retenção por camada |
| **Análise Estratégica** | Incluir análise Build vs Buy para orquestração (Airflow/Prefect/Dagster), storage (S3/GCS/ADLS), processamento (Spark/dbt/Flink) |
| **Backlog Priorizado** | Priorizar por pipeline: pipelines críticos primeiro (receita/compliance), depois analíticos, depois exploratórios |
| **Matriz de Riscos** | Incluir riscos específicos: schema drift, dados duplicados, falha silenciosa de ingestão, custo de reprocessamento não orçado |

---

## Documentos Relacionados

- [[context|knowledge/datalake-ingestion/context.md]] — Concerns e perguntas recomendadas para a Fase 1
- [[specialists|knowledge/datalake-ingestion/specialists.md]] — Catálogo de custom-specialists para datalake
- `dtg-artifacts/templates/customization/final-report-template.md` — Template base (11 seções obrigatórias)
