---
region-id: REG-METR-03
title: "SLAs and SLOs"
group: metrics
description: "Service Level Agreements and Objectives per service component"
source: "Bloco #5 (arch) → 1.5"
schema: "Tabela (serviço, SLI, SLO, SLA)"
template-visual: "Table com status"
default: false
---

# SLAs and SLOs

Define os indicadores de nivel de servico (SLI), objetivos (SLO) e acordos (SLA) para cada componente critico da plataforma. A distincao entre SLO (objetivo interno) e SLA (compromisso externo) permite margem operacional para correcao antes de impactar o cliente.

## Schema de dados

```yaml
slas_and_slos:
  services:
    - service: string            # Nome do servico
      sli: string                # Service Level Indicator (o que e medido)
      slo: string                # Service Level Objective (objetivo interno)
      sla: string                # Service Level Agreement (compromisso externo)
      error_budget: string       # Budget de erro permitido
```

## Exemplo

| Servico | SLI | SLO | SLA | Error Budget |
|---------|-----|-----|-----|-------------|
| API Gateway | % de requests com status 2xx | 99.9% | 99.5% | 43 min/mes de downtime |
| Dashboard Web | First Contentful Paint P95 | < 1.5s | < 3s | 5% das sessoes acima |
| Integracao Open Finance | % de sincronizacoes bem-sucedidas | 99.0% | 97.0% | 7.2h/mes de falha |
| Servico de Relatorios | Tempo de geracao P95 | < 30s | < 60s | 5% acima do SLO |
| Banco de Dados | Latencia de query P99 | < 100ms | N/A (interno) | 1% acima do SLO |

## Representacao Visual

### Dados de amostra

```
API Gateway          SLO 99.9% | SLA 99.5%  [██████████░] error budget: 43 min/mes
Dashboard Web        SLO <1.5s | SLA <3s    [████████░░░] error budget: 5% sessoes
Open Finance         SLO 99.0% | SLA 97.0%  [█████████░░] error budget: 7.2h/mes
Servico Relatorios   SLO <30s  | SLA <60s   [████████░░░] error budget: 5% acima
Banco de Dados       SLO <100ms| SLA N/A    [█████████░░] error budget: 1% acima
```

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com gauge indicators
**Tecnologia:** HTML/CSS
**Justificativa:** SLAs/SLOs envolvem multiplas dimensoes por servico (SLI, SLO, SLA, error budget) que exigem comparacao lado a lado. Uma tabela com mini-gauges inline (barras de consumo do error budget) em cada linha combina a densidade da tabela com a leitura visual imediata dos indicadores.
**Alternativa:** Stat cards por servico — quando ha poucos servicos (<=3) e o foco e no error budget individual de cada um.
