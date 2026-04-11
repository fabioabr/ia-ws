---
region-id: REG-TECH-01
title: "Stack Tecnológica"
group: technical
description: "Tecnologias selecionadas com camada, versão e justificativa"
source: "Bloco #5 (arch) → 1.5"
schema: "Tabela (tecnologia, camada, versão, justificativa)"
template-visual: "Table com badges"
default: true
---

# Stack Tecnológica

Lista todas as tecnologias escolhidas para o projeto, organizadas por camada arquitetural. Cada escolha inclui a versão alvo e a justificativa, permitindo rastreabilidade das decisões técnicas e facilitando onboarding de novos membros.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| tecnologia | string | Nome da tecnologia ou ferramenta |
| camada | enum | Frontend, Backend, Dados, Infra, Observabilidade, etc. |
| versão | string | Versão alvo ou range |
| justificativa | string | Motivo da escolha |

## Exemplo

| Tecnologia | Camada | Versão | Justificativa |
|------------|--------|--------|---------------|
| React | Frontend | 18.x | Ecossistema maduro, equipe experiente |
| TypeScript | Frontend / Backend | 5.x | Type-safety reduz bugs em runtime |
| Node.js | Backend | 20 LTS | Unificação de linguagem front/back |
| PostgreSQL | Dados | 16 | ACID compliance, suporte a JSON, extensibilidade |
| Redis | Dados (cache) | 7.x | Cache de sessão e rate limiting |
| AWS ECS Fargate | Infra | — | Serverless containers, sem gestão de EC2 |
| Terraform | Infra (IaC) | 1.7+ | Infra versionada, módulos reutilizáveis |
| Datadog | Observabilidade | — | APM + logs + métricas unificados |

## Representação Visual

### Dados de amostra

| Tecnologia | Camada | Versão | Justificativa |
|------------|--------|--------|---------------|
| React | Frontend | 18.x | Ecossistema maduro, equipe experiente |
| TypeScript | Frontend / Backend | 5.x | Type-safety reduz bugs em runtime |
| Node.js | Backend | 20 LTS | Unificação de linguagem front/back |
| PostgreSQL | Dados | 16 | ACID compliance, suporte a JSON, extensibilidade |
| Redis | Dados (cache) | 7.x | Cache de sessão e rate limiting |
| AWS ECS Fargate | Infra | — | Serverless containers, sem gestão de EC2 |
| Terraform | Infra (IaC) | 1.7+ | Infra versionada, módulos reutilizáveis |
| Datadog | Observabilidade | — | APM + logs + métricas unificados |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva organizando as tecnologias por camada, explicando escolhas e relações entre elas | Sempre — serve como base textual acessível para qualquer público |
| Tabela | Tabela estruturada com colunas Tecnologia, Camada, Versão e Justificativa | Sempre — permite comparação rápida e consulta pontual |
| Badge grid | Grade visual com badges/ícones agrupados por camada (Frontend, Backend, Dados, Infra, Observabilidade), cada badge contendo nome e versão da tecnologia | Quando a stack precisa ser comunicada de forma visual e rápida, ideal para apresentações executivas e dashboards |
| Diagrama em camadas | Diagrama empilhado mostrando as camadas arquiteturais como blocos horizontais com as tecnologias posicionadas em cada camada | Quando é importante visualizar a relação hierárquica entre camadas e como as tecnologias se distribuem verticalmente na arquitetura |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
