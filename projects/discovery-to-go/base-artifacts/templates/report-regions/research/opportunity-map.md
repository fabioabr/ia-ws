---
region-id: REG-PESQ-03
title: "Opportunity Map"
group: research
description: "Diagrama hierárquico (objetivo → oportunidades → soluções → experimentos)"
source: "Consolidator"
schema: "diagram"
template-visual: "Tree diagram (mermaid)"
default: false
---

# Opportunity Map

Mapa de oportunidades seguindo o framework Opportunity Solution Tree (OST) de Teresa Torres. Organiza hierarquicamente o objetivo desejado, as oportunidades identificadas para alcançá-lo, as soluções possíveis para cada oportunidade e os experimentos para validar cada solução. Permite visualizar o espaço de solução completo e tomar decisões informadas sobre onde investir esforço.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| objetivo | string | Resultado desejado de alto nível |
| oportunidades | list | Cada item: `{ oportunidade: string, evidencia: string, solucoes: list }` |
| solucoes[n] | object | `{ solucao: string, esforco: string, impacto: string, experimentos: list }` |
| experimentos[n] | object | `{ experimento: string, tipo: string, prazo: string }` |

## Exemplo

```markdown
## Mapa de Oportunidades (OST)

### Objetivo

Reduzir o tempo de fechamento financeiro consolidado de D+8 para D+2.

```mermaid
graph TD
    O["🎯 Fechamento em D+2"] --> OP1["Automatizar coleta de dados"]
    O --> OP2["Eliminar erros de consolidação"]
    O --> OP3["Acelerar revisão e aprovação"]

    OP1 --> S1A["API direta com SAP R/3"]
    OP1 --> S1B["Middleware de integração (MuleSoft)"]
    OP1 --> S1C["RPA para extração de telas"]

    OP2 --> S2A["Engine de eliminação com regras"]
    OP2 --> S2B["Validação cruzada automática"]

    OP3 --> S3A["Dashboard com drill-down"]
    OP3 --> S3B["Workflow de aprovação digital"]

    S1A --> E1["PoC: API SAP filial SP"]
    S1B --> E2["PoC: MuleSoft connector"]
    S2A --> E3["Protótipo: 3 regras de eliminação"]
    S3A --> E4["Wireframe + teste com controller"]
```

### Detalhamento

#### Oportunidade 1: Automatizar coleta de dados

**Evidência:** Analistas gastam 60% do tempo coletando e normalizando dados manualmente (entrevistas com 4/4 analistas).

| Solução | Esforço | Impacto | Experimento |
|---------|---------|---------|-------------|
| API direta com SAP R/3 | Alto | Alto | PoC com filial SP — 2 semanas |
| Middleware MuleSoft | Médio | Médio | PoC com connector existente — 1 semana |
| RPA (extração de telas) | Baixo | Baixo | Descartada — frágil e não escalável |

#### Oportunidade 2: Eliminar erros de consolidação

**Evidência:** 3 reapresentações ao conselho por erros de eliminação intercompany (CFO + Controller).

| Solução | Esforço | Impacto | Experimento |
|---------|---------|---------|-------------|
| Engine de eliminação com regras configuráveis | Alto | Alto | Protótipo com 3 regras mais frequentes — 3 semanas |
| Validação cruzada automática | Médio | Médio | Script de validação com dados reais — 1 semana |

#### Oportunidade 3: Acelerar revisão e aprovação

**Evidência:** Controller gasta 40% do tempo revisando cálculos manualmente (entrevista com controller).

| Solução | Esforço | Impacto | Experimento |
|---------|---------|---------|-------------|
| Dashboard com drill-down | Médio | Alto | Wireframe + teste de usabilidade com controller — 1 semana |
| Workflow de aprovação digital | Baixo | Médio | Protótipo em Figma — 3 dias |
```
