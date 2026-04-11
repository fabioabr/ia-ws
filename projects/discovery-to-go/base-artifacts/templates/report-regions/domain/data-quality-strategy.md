---
region-id: REG-DOM-DATA-02
title: "Data Quality Strategy"
group: domain
description: "Data quality framework, validation rules, and testing approach"
source: "Bloco #5/#7 (arch)"
schema: "Framework qualidade + testes"
template-visual: "Table com status"
when: datalake-ingestion
default: false
---

# Data Quality Strategy

Define o framework de qualidade de dados adotado, incluindo dimensoes de qualidade, regras de validacao e estrategia de testes. Dados de baixa qualidade invalidam decisoes de negocio, tornando esta regiao critica para projetos de dados.

## Schema de dados

```yaml
data_quality:
  framework: string              # Great Expectations, dbt tests, custom
  dimensions:
    - name: string               # Completude, Unicidade, Validade, etc.
      rules: string[]
      threshold: string
  testing:
    - layer: string              # Bronze / Silver / Gold
      test_type: string
      frequency: string
```

## Exemplo

| Dimensao | Regras | Threshold |
|----------|--------|-----------|
| Completude | Campos obrigatorios nao-nulos | >= 99.5% |
| Unicidade | Chaves primarias sem duplicatas | 100% |
| Validade | Valores dentro de ranges esperados | >= 99% |
| Consistencia | Totais batem entre camadas | 100% |
| Freshness | Dados atualizados dentro do SLA | < 1h de atraso |
