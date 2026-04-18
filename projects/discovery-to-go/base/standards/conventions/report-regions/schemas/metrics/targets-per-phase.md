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

## Representacao Visual

### Dados de amostra

```
MVP (4 meses)          v1.1 (2 meses)         Scale (6 meses)
────●──────────────────────●───────────────────────●────────
  Epicos: 3/3             Clientes: >= 100        MRR: >= R$ 50k
  Testes: >= 80%          Uptime: >= 99.5%        Latencia: < 200ms
  Usuarios beta: >= 50    NPS beta: >= 40         Churn: < 3%
```

### Recomendacao do Chart Specialist

**Veredicto:** GRAFICO
**Tipo:** Timeline com markers
**Tecnologia:** HTML/CSS
**Justificativa:** Targets por fase sao inerentemente temporais e sequenciais. Uma timeline horizontal com marcadores por fase, duracao proporcional e metricas listadas abaixo de cada marcador comunica a progressao e os checkpoints de forma intuitiva para stakeholders.
**Alternativa:** Tabela agrupada por fase — quando ha muitas metricas por fase (>5) e a timeline fica visualmente sobrecarregada.
