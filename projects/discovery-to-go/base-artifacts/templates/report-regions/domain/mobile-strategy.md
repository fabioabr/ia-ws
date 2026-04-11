---
region-id: REG-DOM-MOB-01
title: "Mobile Strategy"
group: domain
description: "Mobile platform approach, features, and offline capabilities"
source: "Bloco #5/#7 (arch)"
schema: "Plataformas + abordagem + features + offline"
template-visual: "Card com badges"
when: mobile-app
default: false
---

# Mobile Strategy

Define a estrategia mobile do projeto, incluindo plataformas-alvo, abordagem de desenvolvimento (nativo, hibrido, cross-platform), features criticas e capacidades offline. A escolha de abordagem impacta custo, performance e time-to-market.

## Schema de dados

```yaml
mobile_strategy:
  platforms: string[]            # iOS, Android
  approach: string               # Native, React Native, Flutter, PWA
  min_os_versions:
    ios: string
    android: string
  key_features: string[]
  offline_strategy: string
  push_notifications: boolean
```

## Exemplo

| Aspecto | Decisao |
|---------|---------|
| Plataformas | iOS 15+ e Android 12+ |
| Abordagem | React Native (reuso de skills do time web React) |
| Features criticas | Dashboard financeiro, notificacoes de vencimento, leitura de QR code para boletos |
| Estrategia offline | Cache local (SQLite) dos ultimos 30 dias; sincronizacao ao reconectar |
| Push notifications | Sim — alertas de vencimento, transacoes suspeitas, metas atingidas |
| Biometria | Face ID / fingerprint para acesso ao app |

## Representacao Visual

### Dados de amostra

| Criterio | React Native | Flutter | Nativo | PWA |
|----------|-------------|---------|--------|-----|
| Performance | 4/5 | 4/5 | 5/5 | 3/5 |
| Time-to-market | 5/5 | 4/5 | 2/5 | 5/5 |
| Reuso de skills | 5/5 (React) | 2/5 | 1/5 | 5/5 |
| Acesso HW | 4/5 | 4/5 | 5/5 | 2/5 |
| Offline | 4/5 | 4/5 | 5/5 | 3/5 |
| Custo | Medio | Medio | Alto | Baixo |

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela comparativa com badges
**Tecnologia:** HTML/CSS
**Justificativa:** A comparacao de plataformas mobile envolve 4 abordagens vs 6 criterios com scores e valores qualitativos. Uma tabela comparativa com badges coloridos para scores (4/5, 5/5) e custo permite comparacao direta e justifica a decisao tomada de forma objetiva.
**Alternativa:** Radar chart (Chart.js) — quando os criterios tiverem todos scores numericos uniformes e a comparacao visual de perfil entre abordagens for mais relevante que os valores individuais.
