---
region-id: REG-METR-05
title: "DORA Metrics"
group: metrics
description: "DevOps Research and Assessment metrics for engineering performance"
source: "Bloco #5/#7 (arch)"
schema: "4 stat cards (deploy frequency, lead time, MTTR, change failure rate)"
template-visual: "Stat card grid"
default: false
---

# DORA Metrics

Define os targets para as quatro metricas DORA que medem a performance de engenharia: frequencia de deploy, lead time para mudancas, tempo de recuperacao (MTTR) e taxa de falha em mudancas. Essas metricas sao o padrao da industria para avaliar a maturidade DevOps.

## Schema de dados

```yaml
dora_metrics:
  metrics:
    - name: string               # Nome da metrica DORA
      current: string            # Valor atual (ou N/A se greenfield)
      target: string             # Target para 6 meses
      elite_benchmark: string    # Benchmark "Elite" do DORA report
      measurement: string        # Como medir
```

## Exemplo

| Metrica | Atual | Target (6 meses) | Benchmark Elite | Como Medir |
|---------|-------|------------------|----------------|-----------|
| Deploy Frequency | N/A (greenfield) | Diario | On-demand (multiplos/dia) | Contagem de deploys em producao por dia |
| Lead Time for Changes | N/A | < 1 dia | < 1 hora | Tempo entre commit e deploy em producao |
| Mean Time to Recovery (MTTR) | N/A | < 1 hora | < 1 hora | Tempo entre deteccao do incidente e restauracao |
| Change Failure Rate | N/A | < 10% | < 5% | % de deploys que causam incidente ou rollback |

**Nota:** Por ser um projeto greenfield, os targets iniciais sao conservadores. A meta e atingir o nivel "High" do DORA em 6 meses e "Elite" em 12 meses.
