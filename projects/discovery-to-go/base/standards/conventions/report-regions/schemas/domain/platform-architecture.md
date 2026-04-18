---
region-id: REG-DOM-PLAT-01
title: "Platform Architecture"
group: domain
description: "Cloud infrastructure, CI/CD, observability, and Internal Developer Platform design"
source: "Bloco #5/#7 (arch)"
schema: "Cloud + CI/CD + observability + IDP"
template-visual: "Diagram full-width"
when: platform-engineering
default: false
---

# Platform Architecture

Descreve a arquitetura da plataforma de engenharia, incluindo infraestrutura cloud, pipelines de CI/CD, stack de observabilidade e Internal Developer Platform (IDP). Esta visao holistica e essencial para projetos de platform engineering.

## Schema de dados

```yaml
platform_architecture:
  cloud:
    provider: string
    regions: string[]
    iac_tool: string             # Terraform, Pulumi, CDK
  cicd:
    tool: string
    stages: string[]
    environments: string[]
  observability:
    metrics: string
    logs: string
    traces: string
    alerting: string
  idp:
    tool: string                 # Backstage, Port, custom
    capabilities: string[]
```

## Exemplo

| Camada | Tecnologia | Detalhes |
|--------|-----------|---------|
| Cloud | AWS (sa-east-1) | EKS, RDS, S3, CloudFront, Route53 |
| IaC | Terraform + Atlantis | Modulos compartilhados; PR-based workflow |
| CI/CD | GitHub Actions | Build → Test → Security Scan → Deploy (staging → prod) |
| Observabilidade | Datadog (metrics + logs + APM) | Dashboards por servico; alertas no Slack |
| IDP | Backstage | Catalogo de servicos, templates, golden paths, docs |

## Representacao Visual

### Dados de amostra

```
+----------------------------------------------------------+
|                    Developer Portal                       |
|                    (Backstage IDP)                        |
+----------------------------------------------------------+
|             CI/CD (GitHub Actions)                        |
|  Build -> Test -> Security Scan -> Deploy (stg -> prod)  |
+----------------------------------------------------------+
|          Observabilidade (Datadog)                        |
|  Metrics | Logs | APM | Alerting (Slack)                 |
+----------------------------------------------------------+
|              Infraestrutura (AWS sa-east-1)               |
|  EKS | RDS | S3 | CloudFront | Route53                   |
+----------------------------------------------------------+
|              IaC (Terraform + Atlantis)                   |
|  Modulos compartilhados | PR-based workflow               |
+----------------------------------------------------------+
```

### Recomendacao do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com layers
**Tecnologia:** HTML/CSS
**Justificativa:** A arquitetura de plataforma e um stack de camadas empilhadas (IaC, Cloud, Observabilidade, CI/CD, IDP) com componentes por camada. Cards empilhados verticalmente com fundo colorido por camada e badges de tecnologia comunicam a hierarquia e os componentes de forma visual e compacta.
**Alternativa:** Tabela com camadas e tecnologias (HTML/CSS) — quando o formato for documentacao de referencia e a visualizacao de stack nao for necessaria.
