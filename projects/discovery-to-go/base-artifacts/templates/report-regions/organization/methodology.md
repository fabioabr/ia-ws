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

## Representação Visual

### Dados de amostra

**Framework:** Scrum adaptado + Kanban

**Cadência do sprint (2 semanas):**

| Dia | Cerimônia | Duração | Participantes |
|-----|-----------|---------|---------------|
| Seg (Semana 1) | Sprint Planning | 1h | Time completo |
| Diário | Daily Standup | 15min | Time completo |
| Qua (Semana 1) | Refinamento | 1h | PO, Tech Lead, Dev |
| Sex (Semana 2) | Sprint Review | 1h | Time + Stakeholders |
| Sex (Semana 2) | Retrospectiva | 45min | Time interno |

**Stack de ferramentas:** Jira (gestão), Slack (comunicação), Confluence + Git (documentação), Figma (design)

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva do framework, cadência, cerimônias e ferramentas adotadas | Propostas comerciais, documentos executivos ou onboarding de novos membros |
| Tabela | Tabela de cerimônias com dia, duração e participantes | Referência rápida para o time sobre a agenda recorrente do sprint |
| Card / ficha resumo | Blocos visuais organizados por categoria (framework, cadência, cerimônias, ferramentas) | Dashboards de projeto, wikis ou painéis de onboarding visual |
| Diagrama de fluxo do sprint | Fluxo visual mostrando a sequência de cerimônias ao longo das 2 semanas | Apresentações de kickoff para alinhar o ritmo do projeto com todos os envolvidos |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
