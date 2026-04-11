---
region-id: REG-QUAL-03
title: "Identified Gaps"
group: quality
description: "Gaps found during audit that need attention before proceeding"
source: "Fase 2 (auditor) → 2.1"
schema: "Lista (área, gap, impacto, recomendação)"
template-visual: "Table com alert style"
default: false
---

# Identified Gaps

Lista as lacunas identificadas pelo auditor durante a revisao dos artefatos de discovery. Cada gap indica a area afetada, o impacto potencial e uma recomendacao de como resolve-lo. Gaps criticos devem ser enderecados antes da aprovacao final.

## Schema de dados

```yaml
identified_gaps:
  gaps:
    - id: string                 # Identificador (ex: GAP-01)
      area: string               # Area afetada (requisitos, arquitetura, financeiro, seguranca, etc.)
      description: string        # Descricao do gap
      impact: string             # Critico / Alto / Medio / Baixo
      recommendation: string     # Recomendacao para resolver
      status: string             # Aberto / Em resolucao / Resolvido
```

## Exemplo

| ID | Area | Gap | Impacto | Recomendacao | Status |
|----|------|-----|---------|-------------|--------|
| GAP-01 | Financeiro | Custos de customer success e suporte nao contemplados no TCO | Alto | Incluir pelo menos 1 CS part-time a partir do mes 3 | Aberto |
| GAP-02 | Seguranca | Nenhuma mencao a politica de backup e disaster recovery | Critico | Definir RPO/RTO e estrategia de backup antes da sprint 1 | Aberto |
| GAP-03 | Requisitos | Requisitos de acessibilidade (WCAG) nao especificados | Medio | Adicionar criterios WCAG 2.1 AA nos criterios de aceite | Em resolucao |
| GAP-04 | Arquitetura | Estrategia de observabilidade mencionada mas nao detalhada | Medio | Detalhar stack de monitoring, logging e tracing | Aberto |
