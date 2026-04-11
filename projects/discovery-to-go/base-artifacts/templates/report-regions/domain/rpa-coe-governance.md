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
