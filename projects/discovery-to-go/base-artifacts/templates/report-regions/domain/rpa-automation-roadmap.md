---
region-id: REG-DOM-RPA-01
title: "RPA Automation Roadmap"
group: domain
description: "Prioritized processes for automation with ROI and timeline"
source: "Bloco #5/#7 (arch)"
schema: "Processos priorizados + ROI + timeline"
template-visual: "Timeline com ROI"
when: process-automation
default: false
---

# RPA Automation Roadmap

Lista os processos priorizados para automacao, com estimativa de ROI e timeline de implementacao. A priorizacao considera volume de execucoes, custo manual atual e complexidade de automacao.

## Schema de dados

```yaml
rpa_roadmap:
  processes:
    - name: string
      current_volume: string     # Execucoes/mes
      manual_cost: number        # Custo mensal manual (BRL)
      complexity: string         # Baixa / Media / Alta
      roi_months: number         # Meses para ROI
      phase: number              # Fase de implementacao
```

## Exemplo

| Processo | Volume/Mes | Custo Manual | Complexidade | ROI em | Fase |
|----------|-----------|-------------|-------------|--------|------|
| Conciliacao bancaria | 800 | R$ 8.000 | Media | 3 meses | 1 |
| Emissao de NF-e | 500 | R$ 5.000 | Baixa | 2 meses | 1 |
| Cobranca de inadimplentes | 200 | R$ 3.000 | Alta | 6 meses | 2 |
| Relatorio fiscal mensal | 12 | R$ 2.000 | Media | 4 meses | 2 |
