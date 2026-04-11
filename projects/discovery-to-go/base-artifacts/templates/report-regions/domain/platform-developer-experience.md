---
region-id: REG-DOM-PLAT-02
title: "Platform Developer Experience"
group: domain
description: "Golden paths, self-service capabilities, and developer experience metrics"
source: "Bloco #5/#7 (arch)"
schema: "Golden paths + self-service + DX"
template-visual: "Stat cards"
when: platform-engineering
default: false
---

# Platform Developer Experience

Define os golden paths, capacidades self-service e metricas de developer experience (DX) da plataforma. Uma boa DX acelera o onboarding de desenvolvedores e reduz a carga cognitiva no dia a dia.

## Schema de dados

```yaml
developer_experience:
  golden_paths:
    - name: string
      description: string
      time_to_production: string
  self_service:
    - capability: string
      tool: string
      sla: string
  dx_metrics:
    - metric: string
      target: string
```

## Exemplo

| Golden Path | Descricao | Tempo ate Producao |
|------------|-----------|-------------------|
| Novo microservico | Template Backstage com CI/CD, monitoring e docs pre-configurados | < 30 minutos |
| Novo banco de dados | Provisao de RDS via Terraform module self-service | < 15 minutos |
| Novo ambiente de staging | Clone do ambiente de prod com dados anonimizados | < 1 hora |

**Metricas de DX:**
- Tempo de onboarding de novo dev: target < 2 dias
- Tempo de deploy (commit to prod): target < 15 minutos
- Satisfacao do desenvolvedor (survey trimestral): target >= 4.0/5.0
