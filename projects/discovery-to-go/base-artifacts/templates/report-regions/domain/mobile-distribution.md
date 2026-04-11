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
