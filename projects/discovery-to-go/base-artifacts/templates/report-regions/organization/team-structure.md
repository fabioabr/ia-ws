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

## Representação Visual

### Dados de amostra

```
Product Owner (50%)
├── Tech Lead (100%)
│   ├── Desenvolvedor Backend 1 (100%)
│   ├── Desenvolvedor Backend 2 (100%)
│   ├── Desenvolvedor Frontend (100%)
│   └── DevOps/SRE (25%)
└── QA Engineer (50%)
```

**Fases de atuação:**
- **Discovery → Go-live:** Product Owner, Tech Lead
- **Construção → Go-live:** Desenvolvedores Backend (2x), Desenvolvedor Frontend, QA Engineer
- **Construção → Sustentação:** DevOps/SRE

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela estilizada com colunas de papel, dedicação, fase e observação
**Tecnologia:** HTML/CSS
**Justificativa:** Dados tabulares de papéis com dedicação percentual e fases são melhor representados em tabela estilizada, permitindo leitura rápida e comparação direta entre membros do time.
**Alternativa:** Diagrama de timeline (barras horizontais) via Chart.js — usar quando a variação de alocação ao longo das fases for o foco principal da análise.
