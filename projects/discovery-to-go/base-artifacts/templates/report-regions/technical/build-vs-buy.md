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

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com verdict badges (Build / Buy / Open-Source)
**Tecnologia:** HTML/CSS
**Justificativa:** Com 6 componentes e atributos textuais (opções, justificativa), a tabela com badges coloridos por veredicto permite scanning rápido das decisões e leitura detalhada da justificativa. A amostra não inclui scores numéricos que justifiquem gráfico.
**Alternativa:** Gráfico de barras horizontais (Chart.js) — quando houver 4+ componentes com scores numéricos por critério (custo, risco, time-to-market), permitindo comparação visual entre opções.
