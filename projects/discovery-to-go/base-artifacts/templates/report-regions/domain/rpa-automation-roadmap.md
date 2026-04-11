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

## Representacao Visual

### Dados de amostra

```
Fase 1 (Mes 1-3)                    Fase 2 (Mes 4-8)
|================================|  |================================|
| Conciliacao bancaria           |  | Cobranca inadimplentes         |
| ROI: 3 meses | R$ 8.000/mes   |  | ROI: 6 meses | R$ 3.000/mes   |
|--------------------------------|  |--------------------------------|
| Emissao NF-e                   |  | Relatorio fiscal               |
| ROI: 2 meses | R$ 5.000/mes   |  | ROI: 4 meses | R$ 2.000/mes   |
|================================|  |================================|

ROI acumulado Fase 1: R$ 13.000/mes
ROI acumulado Fase 2: R$ 18.000/mes
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada processo com priorizacao, custo e ROI esperado | Business cases, aprovacao de investimento |
| Tabela | Tabela com processos, volumes, custos e ROI ordenados por fase | Documentacao de planejamento, acompanhamento de progresso |
| Gantt com anotacoes de ROI | Grafico de Gantt mostrando fases e processos no tempo, com anotacoes de ROI acumulado e economia mensal | Apresentacoes para stakeholders, gestao de programa, dashboards de acompanhamento |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
