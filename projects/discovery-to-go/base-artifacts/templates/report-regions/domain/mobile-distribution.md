---
region-id: REG-DOM-MOB-02
title: "Mobile Distribution"
group: domain
description: "App store distribution, CI/CD pipeline, OTA updates, and analytics"
source: "Bloco #5/#7 (arch)"
schema: "Stores + CI/CD + OTA + analytics"
template-visual: "Table"
when: mobile-app
default: false
---

# Mobile Distribution

Detalha a estrategia de distribuicao do app mobile, incluindo presenca em stores, pipeline de CI/CD, atualizacoes OTA e analytics. A distribuicao mobile tem particularidades (review de stores, rollout gradual) que impactam o ciclo de release.

## Schema de dados

```yaml
mobile_distribution:
  stores:
    - name: string               # App Store, Google Play
      account_type: string
      review_time: string
  cicd:
    tool: string                 # Fastlane, Bitrise, etc.
    pipeline_stages: string[]
  ota_updates:
    enabled: boolean
    tool: string                 # CodePush, Expo Updates
    scope: string
  analytics:
    tool: string
    events_tracked: string[]
```

## Exemplo

| Aspecto | iOS | Android |
|---------|-----|---------|
| Store | App Store (conta Organization) | Google Play (conta Organization) |
| Tempo de review | 24-48h (media) | 2-7 dias (media) |
| CI/CD | Fastlane + GitHub Actions | Fastlane + GitHub Actions |
| Beta distribution | TestFlight | Firebase App Distribution |
| OTA updates | CodePush (JS bundle only) | CodePush (JS bundle only) |
| Analytics | Firebase Analytics + Mixpanel | Firebase Analytics + Mixpanel |
| Crash reporting | Sentry | Sentry |

## Representacao Visual

### Dados de amostra

| Etapa do Funil | iOS | Android | Total |
|---------------|-----|---------|-------|
| Impressoes na store | 50.000 | 80.000 | 130.000 |
| Downloads | 5.000 | 12.000 | 17.000 |
| Instalacoes completas | 4.800 | 11.000 | 15.800 |
| Primeiro acesso | 3.500 | 8.000 | 11.500 |
| Ativacao (cadastro) | 2.000 | 5.000 | 7.000 |
| Retencao D7 | 1.200 | 2.800 | 4.000 |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa da estrategia de distribuicao por plataforma | Documentos de estrategia, planejamento de lancamento |
| Tabela | Tabela comparativa iOS vs Android com ferramentas e metricas por plataforma | Documentacao tecnica, referencia operacional |
| Grafico de funil | Funil mostrando conversao de download ate ativacao, por plataforma | Dashboards de growth, relatorios de marketing, analise de conversao |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
