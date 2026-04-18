---
region-id: REG-PLAN-01
title: "Relative Gantt"
group: product
description: "Gantt chart with relative timeline (Week 1, 2, ..., N) — no fixed dates"
source: "Consolidator + Backlog"
schema: "Horizontal bars per activity with week grid"
template-visual: "Timeline horizontal (HTML/CSS)"
default: false
---

# Relative Gantt

Diagrama de Gantt com timeline relativa (Semana 1, Semana 2, ..., Semana N) sem datas fixas. Cada atividade aparece como barra horizontal posicionada no grid de semanas, mostrando inicio relativo, duracao e paralelismo entre atividades. Ideal para estimativas de discovery onde datas absolutas ainda nao foram definidas.

## Schema de dados

```yaml
gantt_relative:
  total_weeks: number              # Duracao total em semanas
  activities:
    - id: string                   # Identificador (ex: AT-01)
      name: string                 # Nome da atividade ou epico
      role: string                 # Papel principal responsavel
      week_start: number           # Semana de inicio (1-based)
      week_end: number             # Semana de fim (inclusive)
      depends_on: string[]         # IDs de atividades predecessoras (opcional)
      color: string                # Cor da barra (opcional, default por papel)
```

## Exemplo

```markdown
## Planejamento

### Gantt Relativo

| Atividade | Papel | Sem 1 | Sem 2 | Sem 3 | Sem 4 | Sem 5 | Sem 6 | Sem 7 | Sem 8 | Sem 9 | Sem 10 |
|-----------|-------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
| AT-01: Setup e Infra | DevOps | ██ | ██ | | | | | | | | |
| AT-02: Onboarding e Auth | Backend | | ██ | ██ | ██ | | | | | | |
| AT-03: UI Kit e Layout | Frontend | ██ | ██ | ██ | | | | | | | |
| AT-04: Dashboard Financeiro | Backend | | | | ██ | ██ | ██ | ██ | | | |
| AT-05: Dashboard — Telas | Frontend | | | | | ██ | ██ | ██ | | | |
| AT-06: Gestao de Assinaturas | Backend | | | | | | | ██ | ██ | ██ | |
| AT-07: Testes integrados | QA | | | | | | | | ██ | ██ | ██ |

**Duracao total estimada:** 10 semanas
**Paralelismo maximo:** 2 atividades simultaneas
```

## Representacao Visual

### Dados de amostra

```yaml
gantt_relative:
  total_weeks: 10
  activities:
    - id: "AT-01"
      name: "Setup e Infra"
      role: "DevOps"
      week_start: 1
      week_end: 2
      depends_on: []
    - id: "AT-02"
      name: "Onboarding e Auth"
      role: "Backend"
      week_start: 2
      week_end: 4
      depends_on: ["AT-01"]
    - id: "AT-03"
      name: "UI Kit e Layout"
      role: "Frontend"
      week_start: 1
      week_end: 3
      depends_on: []
    - id: "AT-04"
      name: "Dashboard Financeiro"
      role: "Backend"
      week_start: 4
      week_end: 7
      depends_on: ["AT-02"]
    - id: "AT-05"
      name: "Dashboard — Telas"
      role: "Frontend"
      week_start: 5
      week_end: 7
      depends_on: ["AT-03", "AT-04"]
    - id: "AT-06"
      name: "Gestao de Assinaturas"
      role: "Backend"
      week_start: 7
      week_end: 9
      depends_on: ["AT-04"]
    - id: "AT-07"
      name: "Testes integrados"
      role: "QA"
      week_start: 8
      week_end: 10
      depends_on: ["AT-05", "AT-06"]
```

### Recomendacao do Chart Specialist

**Veredicto:** GRAFICO
**Tipo:** Horizontal bar chart com grid de semanas
**Tecnologia:** HTML/CSS
**Justificativa:** Atividades com inicio/fim relativos mapeiam naturalmente para barras horizontais posicionadas num grid de semanas. CSS Grid permite alinhar barras precisamente nas colunas de semana sem JavaScript. Cores por papel (Backend=azul, Frontend=verde, QA=laranja, DevOps=roxo) tornam o paralelismo e a distribuicao de trabalho visiveis instantaneamente. Timeline relativa (Semana 1..N) elimina a necessidade de datas reais, adequado para estimativas de discovery.
**Alternativa:** Tabela com blocos coloridos (HTML/CSS) — quando o numero de semanas for muito grande (>20) e barras ficarem comprimidas, uma tabela scrollavel horizontalmente com celulas coloridas pode ser mais legivel.
