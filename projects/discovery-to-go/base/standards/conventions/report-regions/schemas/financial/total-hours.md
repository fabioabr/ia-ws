---
region-id: REG-FIN-06
title: "Total Hours"
group: financial
description: "Summary of total hours per role and grand total"
source: "Consolidator"
schema: "Stat cards with hours per role + grand total"
template-visual: "Stat cards grid (HTML/CSS)"
default: false
---

# Total Hours

Resumo consolidado de horas estimadas por papel e total geral do projeto. Apresenta em stat cards a distribuicao de esforco entre os papeis envolvidos, permitindo dimensionamento de time e calculo de custo pelo cliente (que aplica seus proprios valores/hora). Nao inclui valores monetarios — apenas horas.

## Schema de dados

```yaml
total_hours:
  roles:
    - role: string                 # Nome do papel (ex: Backend Developer)
      hours: number                # Total de horas estimadas para este papel
      percentage: number           # Percentual do total geral
  grand_total: number              # Soma de todas as horas
  total_weeks: number              # Duracao estimada em semanas
  observations: string[]           # Premissas ou observacoes (opcional)
```

## Exemplo

```markdown
## Totais

### Horas por papel

| Papel | Horas | % do total |
|-------|------:|:----------:|
| Backend Developer | 320h | 37% |
| Frontend Developer | 240h | 28% |
| QA Engineer | 120h | 14% |
| DevOps Engineer | 80h | 9% |
| Tech Lead | 60h | 7% |
| Product Owner | 40h | 5% |

### Total geral

**860 horas** | 10 semanas

### Observacoes

- Horas baseadas em jornada de 8h/dia, 5 dias/semana
- Nao inclui reunioes de cerimonia (dailies, retros) — adicionar ~10% de overhead
- Valores/hora a serem definidos pelo cliente
```

## Representacao Visual

### Dados de amostra

```yaml
total_hours:
  roles:
    - role: "Backend Developer"
      hours: 320
      percentage: 37
    - role: "Frontend Developer"
      hours: 240
      percentage: 28
    - role: "QA Engineer"
      hours: 120
      percentage: 14
    - role: "DevOps Engineer"
      hours: 80
      percentage: 9
    - role: "Tech Lead"
      hours: 60
      percentage: 7
    - role: "Product Owner"
      hours: 40
      percentage: 5
  grand_total: 860
  total_weeks: 10
```

### Recomendacao do Chart Specialist

**Veredicto:** STAT CARDS
**Tipo:** Grid de stat cards com card destacado para total geral
**Tecnologia:** HTML/CSS
**Justificativa:** 6 papeis + 1 total geral cabem perfeitamente num grid 3x2 + 1 card full-width. Cada card mostra papel, horas e percentual com barra de progresso proporcional. O card de total geral fica destacado (cor primaria, fonte maior) na parte inferior. Stat cards comunicam numeros-chave de forma instantanea sem exigir leitura de tabela. HTML/CSS puro permite controle total sobre cores por papel e responsividade.
**Alternativa:** Donut chart + stat card central — quando a audiencia preferir visualizacao proporcional (fatias por papel) com o total geral no centro do donut. Requer SVG ou Chart.js.
