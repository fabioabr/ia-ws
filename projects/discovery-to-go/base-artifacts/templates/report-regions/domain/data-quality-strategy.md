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

## Representacao Visual

### Dados de amostra

| Dimensao | Bronze | Silver | Gold |
|----------|--------|--------|------|
| Completude | 92% | 99.2% | 99.8% |
| Unicidade | 95% | 100% | 100% |
| Validade | 88% | 99.5% | 99.9% |
| Consistencia | N/A | 98% | 100% |
| Freshness | < 5min | < 30min | < 1h |

### Recomendacao do Chart Specialist

**Veredicto:** GRAFICO
**Tipo:** Heatmap
**Tecnologia:** HTML/CSS
**Justificativa:** Os dados de amostra mostram cobertura de qualidade por dimensao (linhas) vs camada (colunas) com valores percentuais numericos. Um heatmap com cores graduadas (vermelho-amarelo-verde) permite identificar instantaneamente gaps de qualidade e areas criticas. Se os scores forem numericos puros, barras horizontais por dimensao agrupadas por camada tambem funcionam bem.
**Alternativa:** Horizontal bars agrupadas por camada (HTML/CSS) — quando houver muitas dimensoes (8+) ou quando a comparacao entre camadas for mais importante que a visao geral.
