---
region-id: REG-DOM-DATA-01
title: "Data Medallion Architecture"
group: domain
description: "Bronze-Silver-Gold data lake layer design and data flow"
source: "Bloco #5/#7 (arch)"
schema: "Diagram Bronze→Silver→Gold"
template-visual: "Diagram full-width"
when: datalake-ingestion
default: false
---

# Data Medallion Architecture

Descreve a arquitetura de dados em camadas (Bronze, Silver, Gold) com os fluxos de ingestao, transformacao e consumo. Cada camada tem responsabilidades claras de qualidade e governanca.

## Schema de dados

```yaml
medallion:
  layers:
    - name: string               # Bronze / Silver / Gold
      purpose: string
      storage: string            # Tecnologia de armazenamento
      format: string             # Parquet, Delta, JSON, etc.
      retention: string
      quality_checks: string[]
  pipelines:
    - source: string
      target: string
      tool: string               # Spark, dbt, Airflow, etc.
      frequency: string
```

## Exemplo

| Camada | Proposito | Storage | Formato | Retencao |
|--------|-----------|---------|---------|----------|
| Bronze | Dados brutos das fontes (APIs, CSVs, eventos) | S3 | JSON/Parquet | 90 dias |
| Silver | Dados limpos, deduplicados, tipados | S3 + Glue Catalog | Delta Lake | 1 ano |
| Gold | Agregacoes e metricas prontas para consumo | Redshift/Athena | Parquet | Indefinido |

## Representacao Visual

### Dados de amostra

```
Fontes (APIs, CSVs, Eventos)
    |
    v
[ Bronze ] -- S3/JSON/Parquet -- Dados brutos, 90 dias retencao
    |
    v (Spark/dbt - limpeza, dedup, tipagem)
[ Silver ] -- S3+Glue/Delta Lake -- Dados limpos, 1 ano retencao
    |
    v (Agregacoes, metricas)
[  Gold  ] -- Redshift/Athena/Parquet -- Consumo, retencao indefinida
    |
    v
Dashboards / APIs / ML Models
```

### Recomendacao do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com layers visuais
**Tecnologia:** HTML/CSS
**Justificativa:** A arquitetura medallion e um fluxo sequencial de 3 camadas com metadados distintos por camada (storage, formato, retencao). Cards empilhados verticalmente com setas de conexao e badges de tecnologia comunicam hierarquia e fluxo de forma clara e compacta.
**Alternativa:** Tabela com camadas em linhas (HTML/CSS) — quando o foco for referencia rapida sem necessidade de comunicar o fluxo entre camadas.
