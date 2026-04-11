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

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva da composição do time, dedicação e fases de cada membro | Relatórios executivos ou documentos onde diagramas não são viáveis |
| Tabela | Tabela com papel, dedicação, fase e observações por membro | Planejamento detalhado de alocação e dimensionamento de recursos |
| Organograma (org chart) | Diagrama hierárquico mostrando a estrutura de reporte e os papéis do time | Apresentações para stakeholders que precisam entender a cadeia de liderança e composição |
| Diagrama de timeline | Barras horizontais por papel mostrando dedicação ao longo das fases do projeto | Quando é importante visualizar a variação de alocação ao longo do tempo |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
