---
region-id: REG-METR-02
title: "Technical KPIs"
group: metrics
description: "Technical performance indicators and their service level targets"
source: "Bloco #5/#7 (arch)"
schema: "Tabela (KPI, valor, SLA)"
template-visual: "Stat cards"
default: false
---

# Technical KPIs

Define os indicadores tecnicos que devem ser monitorados para garantir a saude da plataforma. Cada KPI inclui o valor esperado e o SLA associado. Estes indicadores orientam decisoes de arquitetura e capacidade.

## Schema de dados

```yaml
technical_kpis:
  kpis:
    - id: string                 # Identificador (ex: TK-01)
      name: string               # Nome do KPI tecnico
      target_value: string       # Valor alvo
      sla: string                # SLA associado
      measurement: string        # Como medir
```

## Exemplo

| ID | KPI | Target | SLA | Como Medir |
|----|-----|--------|-----|-----------|
| TK-01 | Latencia P95 da API | < 200ms | 99% das requests | APM (Datadog) |
| TK-02 | Disponibilidade | 99.5% | Mensal | Uptime monitor |
| TK-03 | Tempo de resposta do dashboard | < 2s (first contentful paint) | 95% dos acessos | RUM (Real User Monitoring) |
| TK-04 | Taxa de erro da API | < 0.1% | Mensal | Logs + metricas |
| TK-05 | Tempo de build + deploy | < 10 minutos | 95% dos deploys | CI/CD pipeline metrics |
