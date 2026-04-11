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

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada dimensao de qualidade com regras, thresholds e estrategia de teste | Documentacao de governanca, politicas de dados |
| Tabela | Tabela com dimensoes, regras e thresholds por camada | Referencia operacional, checklists de qualidade |
| Heatmap de cobertura | Mapa de calor com dimensoes de qualidade (linhas) vs camadas (colunas), cores indicando nivel de conformidade | Dashboards de monitoramento, reports de qualidade para stakeholders |
| Indicadores de status | Cards ou badges com status (verde/amarelo/vermelho) por dimensao e camada | Dashboards operacionais, alertas visuais em tempo real |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
