---
region-id: REG-ORG-04
title: "Metodologia"
group: organization
description: "Framework de trabalho, cadência, cerimônias e ferramentas do projeto"
source: "Bloco #4 (po) → 1.4"
schema: "Texto + lista (framework, cadência, cerimônias, ferramentas)"
template-visual: "Card simples"
default: false
---

# Metodologia

Descreve o framework de trabalho adotado, a cadência de entregas e as cerimônias que garantem alinhamento e ritmo. Permite que todos os envolvidos saibam o que esperar em termos de processo, comunicação e ferramentas desde o início.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| framework | string | Nome do framework (Scrum, Kanban, Shape Up, etc.) |
| cadência | string | Duração dos ciclos (sprints, cooldowns) |
| cerimônias | lista | Cerimônias e sua frequência |
| ferramentas | lista | Ferramentas utilizadas no processo |

## Exemplo

**Framework:** Scrum adaptado com elementos de Kanban para sustentação

**Cadência:** Sprints de 2 semanas, com release a cada sprint

**Cerimônias:**
- **Sprint Planning** — segunda-feira, 1h, início de cada sprint
- **Daily Standup** — diária, 15min, 09h30
- **Refinamento** — quarta-feira da semana 1, 1h
- **Sprint Review** — sexta-feira da semana 2, 1h (aberta a stakeholders)
- **Retrospectiva** — sexta-feira da semana 2, 45min (time interno)

**Ferramentas:**
- **Gestão:** Jira (backlog, sprints, métricas)
- **Comunicação:** Slack (canal #fintrack-pro-delivery)
- **Documentação:** Confluence + repositório Git
- **Design:** Figma (protótipos e handoff)
