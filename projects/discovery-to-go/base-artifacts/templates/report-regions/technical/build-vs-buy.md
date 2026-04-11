---
region-id: REG-TECH-06
title: "Build vs Buy"
group: technical
description: "Análise de construir vs comprar para cada componente-chave"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (componente, opções, veredicto, justificativa)"
template-visual: "Table com verdict badges"
default: true
---

# Build vs Buy

Avalia para cada componente-chave se é mais vantajoso construir internamente ou adquirir uma solução pronta. Considera custo total de propriedade, time-to-market, diferenciação competitiva e risco técnico para fundamentar cada decisão.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| componente | string | Nome do componente ou capacidade |
| opções | lista | Alternativas avaliadas (build, SaaS, open-source) |
| veredicto | enum | Build, Buy, Open-Source |
| justificativa | string | Motivo da escolha |

## Exemplo

| Componente | Opções Avaliadas | Veredicto | Justificativa |
|------------|-----------------|-----------|---------------|
| Motor de regras financeiras | Build custom vs Drools vs AWS Step Functions | **Build** | Core do negócio, regras muito específicas do domínio financeiro brasileiro |
| Autenticação/SSO | Build custom vs Okta vs Keycloak | **Buy (Okta)** | Cliente já possui licença corporativa, reduz 3 sprints de desenvolvimento |
| Gateway de pagamentos | Build custom vs Stripe vs PagSeguro | **Buy (Stripe)** | Certificação PCI-DSS inclusa, API madura, suporte a boleto e Pix |
| Monitoramento/APM | ELK stack vs Datadog vs Grafana Cloud | **Buy (Datadog)** | Unifica logs, métricas e traces; menor custo operacional que self-hosted |
| Fila de mensagens | RabbitMQ vs AWS SQS vs Kafka | **Buy (SQS)** | Volume atual não justifica Kafka; SQS é serverless e integrado ao ecossistema AWS |
| Relatórios PDF | Build custom vs Jasper vs Puppeteer | **Open-Source (Puppeteer)** | Flexibilidade total no layout, custo zero de licença, equipe já domina |

## Representação Visual

### Dados de amostra

| Componente | Opções Avaliadas | Veredicto | Justificativa |
|------------|-----------------|-----------|---------------|
| Motor de regras financeiras | Build custom vs Drools vs AWS Step Functions | Build | Core do negócio, regras específicas do domínio |
| Autenticação/SSO | Build custom vs Okta vs Keycloak | Buy (Okta) | Licença corporativa existente, reduz 3 sprints |
| Gateway de pagamentos | Build custom vs Stripe vs PagSeguro | Buy (Stripe) | PCI-DSS incluso, API madura |
| Monitoramento/APM | ELK stack vs Datadog vs Grafana Cloud | Buy (Datadog) | Unifica logs, métricas e traces |
| Fila de mensagens | RabbitMQ vs AWS SQS vs Kafka | Buy (SQS) | Serverless, volume não justifica Kafka |
| Relatórios PDF | Build custom vs Jasper vs Puppeteer | Open-Source (Puppeteer) | Flexibilidade total, custo zero |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva analisando cada componente com suas opções, veredicto e justificativa detalhada | Sempre — serve como base textual acessível para qualquer público |
| Tabela | Tabela estruturada com colunas Componente, Opções Avaliadas, Veredicto e Justificativa, com badges visuais para o veredicto (Build, Buy, Open-Source) | Sempre — permite comparação rápida entre componentes e decisões |
| Gráfico de barras comparativo | Barras horizontais agrupadas por componente mostrando critérios de avaliação (custo, time-to-market, diferenciação, risco) para cada opção considerada | Quando é necessário justificar visualmente a escolha com base em múltiplos critérios de avaliação |
| Matriz de decisão | Grid com componentes nas linhas e critérios nas colunas (custo, controle, time-to-market, risco, maturidade), com scores visuais (cores/ícones) para cada combinação | Quando stakeholders precisam entender o racional completo por trás de cada decisão Build vs Buy vs Open-Source |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
