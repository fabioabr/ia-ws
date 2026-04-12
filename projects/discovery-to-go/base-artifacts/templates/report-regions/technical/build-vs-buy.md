---
region-id: REG-TECH-06
title: "Build vs Buy"
group: technical
description: "Análise de construir vs comprar para cada componente-chave"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (capacidade, decisão, solução, justificativa)"
template-visual: "Table com verdict badges"
default: true
---

# Build vs Buy

Avalia para cada componente-chave se é mais vantajoso construir internamente ou adquirir uma solução pronta. Considera custo total de propriedade, time-to-market, diferenciação competitiva e risco técnico para fundamentar cada decisão.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| capacidade | string | Nome do componente ou capacidade |
| decisão | enum | BUILD, BUY, HYBRID (badge separado da solução) |
| solução | string | Nome da solução escolhida ou descrição da abordagem |
| justificativa | string | Motivo da escolha |

## Exemplo

| Capacidade | Decisão | Solução | Justificativa |
|------------|---------|---------|---------------|
| Motor de regras financeiras | **BUILD** | Desenvolvimento custom | Core do negócio, regras muito específicas do domínio financeiro brasileiro |
| Autenticação/SSO | **BUY** | Okta | Cliente já possui licença corporativa, reduz 3 sprints de desenvolvimento |
| Gateway de pagamentos | **BUY** | Stripe | Certificação PCI-DSS inclusa, API madura, suporte a boleto e Pix |
| Monitoramento/APM | **BUY** | Datadog | Unifica logs, métricas e traces; menor custo operacional que self-hosted |
| Fila de mensagens | **BUY** | AWS SQS | Volume atual não justifica Kafka; SQS é serverless e integrado ao ecossistema AWS |
| Relatórios PDF | **BUILD** | Puppeteer (open-source) | Flexibilidade total no layout, custo zero de licença, equipe já domina |

## Representação Visual

### Dados de amostra

| Capacidade | Decisão | Solução | Justificativa |
|------------|---------|---------|---------------|
| Motor de regras financeiras | BUILD | Desenvolvimento custom | Core do negócio, regras específicas do domínio |
| Autenticação/SSO | BUY | Okta | Licença corporativa existente, reduz 3 sprints |
| Gateway de pagamentos | BUY | Stripe | PCI-DSS incluso, API madura |
| Monitoramento/APM | BUY | Datadog | Unifica logs, métricas e traces |
| Fila de mensagens | BUY | AWS SQS | Serverless, volume não justifica Kafka |
| Relatórios PDF | BUILD | Puppeteer (open-source) | Flexibilidade total, custo zero |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com coluna "Decisão" renderizada como badges coloridos (BUILD = success/green, BUY = info/blue, HYBRID = warning/yellow)
**Tecnologia:** HTML/CSS
**Justificativa:** Com 6 componentes e atributos textuais (solução, justificativa), a tabela com badges coloridos na coluna "Decisão" permite scanning rápido das decisões e leitura detalhada da justificativa. A coluna de decisão é separada da solução para clareza visual. A amostra não inclui scores numéricos que justifiquem gráfico.
**Alternativa:** Gráfico de barras horizontais (Chart.js) — quando houver 4+ componentes com scores numéricos por critério (custo, risco, time-to-market), permitindo comparação visual entre opções.
