---
region-id: REG-ORG-02
title: "Estrutura do Time"
group: organization
description: "Composição do time com papéis, dedicação e fases de atuação"
source: "Bloco #4 (po) → 1.4"
schema: "Tabela (papel, dedicação, fase, observação)"
template-visual: "Table ou org chart"
default: true
---

# Estrutura do Time

Define a composição do time necessário para o projeto, incluindo percentual de dedicação e fase de atuação. Permite ao cliente e à equipe de delivery dimensionar recursos e planejar alocações com antecedência, evitando gargalos e ociosidade.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| papel | string | Função no time (Tech Lead, Dev, QA, etc.) |
| dedicação | string | Percentual ou horas/semana |
| fase | string | Em quais fases do projeto atua |
| observação | string | Notas relevantes sobre a alocação |

## Exemplo

| Papel | Dedicação | Fase | Observação |
|-------|-----------|------|------------|
| Product Owner | 50% | Discovery → Go-live | Ponto focal com o cliente |
| Tech Lead | 100% | Discovery → Go-live | Responsável por decisões de arquitetura |
| Desenvolvedor Backend (2x) | 100% | Construção → Go-live | Foco em API e integrações bancárias |
| Desenvolvedor Frontend | 100% | Construção → Go-live | React + Design System interno |
| QA Engineer | 50% | Construção → Go-live | Automação de testes + testes exploratórios |
| DevOps/SRE | 25% | Construção → Sustentação | Infra, CI/CD e observabilidade |
