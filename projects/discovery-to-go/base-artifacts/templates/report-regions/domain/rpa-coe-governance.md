---
region-id: REG-DOM-RPA-02
title: "RPA CoE Governance"
group: domain
description: "Center of Excellence structure, monitoring, and maintenance for RPA"
source: "Bloco #5/#7 (arch)"
schema: "CoE + monitoring + manutenção"
template-visual: "Card"
when: process-automation
default: false
---

# RPA CoE Governance

Define a estrutura do Centro de Excelencia (CoE) para governanca de automacoes, incluindo modelo operacional, monitoramento e manutencao. Um CoE bem estruturado e a diferenca entre automacoes pontuais e uma estrategia escalavel.

## Schema de dados

```yaml
rpa_coe:
  structure:
    team: string[]               # Papeis no CoE
    governance_model: string     # Centralizado / Federado / Hibrido
  monitoring:
    tool: string
    metrics: string[]
  maintenance:
    review_frequency: string
    update_policy: string
```

## Exemplo

| Aspecto | Definicao |
|---------|-----------|
| Modelo | Hibrido — CoE central define padroes; times de negocio desenvolvem automacoes simples |
| Time CoE | 1 RPA Lead, 2 RPA Developers, 1 Business Analyst |
| Monitoramento | Dashboard com taxa de sucesso, tempo de execucao, filas pendentes |
| Manutencao | Revisao mensal de automacoes; re-teste apos mudancas nos sistemas-fonte |
| Metricas | Taxa de sucesso >= 98%, FTE liberados, ROI acumulado |

## Representacao Visual

### Dados de amostra

| KPI | Meta | Atual | Tendencia |
|-----|------|-------|-----------|
| Taxa de sucesso | >= 98% | 99.2% | Estavel |
| FTE liberados | 4 | 3.5 | Subindo |
| ROI acumulado (12m) | R$ 180.000 | R$ 156.000 | No ritmo |
| Automacoes ativas | 6 | 4 | Crescendo |
| Tempo medio execucao | < 5 min | 3.2 min | Estavel |
| Incidentes/mes | < 2 | 1 | Melhorando |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa da estrutura do CoE com modelo, time, monitoramento e metricas | Documentos de governanca, propostas de CoE |
| Tabela | Tabela com aspectos do CoE e suas definicoes | Referencia operacional, onboarding |
| Dashboard de KPIs | Painel com gauges, trend lines e semaforos para cada KPI do CoE | Reunioes de acompanhamento, relatorios mensais para gestao |
| Scorecard | Card com metricas-chave, meta vs realizado e indicadores de tendencia | Relatorios executivos, apresentacoes de resultado |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
