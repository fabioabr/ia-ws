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

## Representacao Visual

### Dados de amostra

| Metrica DORA / DX | Target | Atual | Status |
|-------------------|--------|-------|--------|
| Deployment Frequency | Diario | 3.2/dia | OK |
| Lead Time for Changes | < 15 min | 12 min | OK |
| Change Failure Rate | < 5% | 3.8% | OK |
| MTTR | < 30 min | 22 min | OK |
| Onboarding time | < 2 dias | 1.5 dias | OK |
| Dev Satisfaction | >= 4.0/5.0 | 4.2/5.0 | OK |

| Golden Path | Tempo ate Producao |
|------------|-------------------|
| Novo microservico | 28 min |
| Novo banco de dados | 12 min |
| Novo ambiente staging | 45 min |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa dos golden paths, capacidades self-service e metricas DX | Documentos de estrategia de plataforma, relatorios executivos |
| Tabela | Tabela com golden paths, metricas e targets | Referencia operacional, acompanhamento de metas |
| Stat cards (DORA + DX) | Cards individuais com metricas DORA e DX, mostrando valor atual, target e trend | Dashboards de platform engineering, reunioes de acompanhamento, relatorios de performance |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
