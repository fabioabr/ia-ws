---
region-id: REG-METR-04
title: "Targets per Phase"
group: metrics
description: "Measurable targets mapped to each project phase or milestone"
source: "Consolidator"
schema: "Tabela (fase, métrica, target)"
template-visual: "Timeline com targets"
default: false
---

# Targets per Phase

Mapeia metas mensuráveis para cada fase do projeto, criando checkpoints claros de progresso. Permite acompanhar se o projeto está no caminho certo e tomar decisoes corretivas antes que desvios se acumulem.

## Schema de dados

```yaml
targets_per_phase:
  phases:
    - phase: string              # Nome da fase (ex: MVP, v1.1, Scale)
      duration: string           # Duracao estimada
      metrics:
        - name: string           # Nome da metrica
          target: string         # Valor alvo
          type: string           # business / technical / quality
```

## Exemplo

| Fase | Duracao | Metrica | Target | Tipo |
|------|---------|---------|--------|------|
| MVP | 4 meses | Epicos entregues | 3 de 3 (Must) | quality |
| MVP | 4 meses | Cobertura de testes | >= 80% | technical |
| MVP | 4 meses | Usuarios beta ativos | >= 50 | business |
| v1.1 | 2 meses | Clientes pagantes | >= 100 | business |
| v1.1 | 2 meses | Uptime | >= 99.5% | technical |
| v1.1 | 2 meses | NPS beta | >= 40 | business |
| Scale | 6 meses | MRR | >= R$ 50.000 | business |
| Scale | 6 meses | Latencia P95 | < 200ms | technical |
| Scale | 6 meses | Churn | < 3% | business |
