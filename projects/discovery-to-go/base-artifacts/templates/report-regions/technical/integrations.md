---
region-id: REG-TECH-02
title: "Integrações"
group: technical
description: "Mapa de integrações externas com protocolo, direção e SLA"
source: "Bloco #5 (arch) → 1.5"
schema: "Tabela (sistema, protocolo, direção, volume, SLA)"
template-visual: "Table ou diagram"
default: true
---

# Integrações

Documenta todas as integrações com sistemas externos, detalhando protocolo, direção do fluxo de dados e SLAs esperados. Essa visão é essencial para dimensionar a complexidade técnica, mapear dependências e planejar estratégias de resiliência.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| sistema | string | Nome do sistema externo |
| protocolo | string | REST, gRPC, mensageria, SFTP, etc. |
| direção | enum | Inbound, Outbound, Bidirecional |
| volume | string | Volume estimado de transações |
| SLA | string | Disponibilidade e latência esperadas |

## Exemplo

| Sistema | Protocolo | Direção | Volume | SLA |
|---------|-----------|---------|--------|-----|
| Core Bancário (Temenos) | REST API v2 | Bidirecional | ~50k req/dia | 99.9%, p95 < 200ms |
| Gateway de Pagamentos (Stripe) | REST + Webhooks | Outbound / Inbound (callbacks) | ~10k transações/dia | 99.95%, p95 < 500ms |
| ERP Financeiro (SAP) | SFTP (batch) | Outbound | 1 arquivo/dia (~5k registros) | Entrega até 06h00 |
| Serviço de E-mail (SendGrid) | REST API | Outbound | ~2k emails/dia | 99.9%, best-effort delivery |
| Identity Provider (Okta) | SAML 2.0 / OIDC | Inbound | ~500 logins/dia | 99.99% |

## Representação Visual

### Dados de amostra

| Sistema | Protocolo | Direção | Volume | SLA |
|---------|-----------|---------|--------|-----|
| Core Bancário (Temenos) | REST API v2 | Bidirecional | ~50k req/dia | 99.9%, p95 < 200ms |
| Gateway de Pagamentos (Stripe) | REST + Webhooks | Outbound / Inbound (callbacks) | ~10k transações/dia | 99.95%, p95 < 500ms |
| ERP Financeiro (SAP) | SFTP (batch) | Outbound | 1 arquivo/dia (~5k registros) | Entrega até 06h00 |
| Serviço de E-mail (SendGrid) | REST API | Outbound | ~2k emails/dia | 99.9%, best-effort delivery |
| Identity Provider (Okta) | SAML 2.0 / OIDC | Inbound | ~500 logins/dia | 99.99% |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva detalhando cada integração, seu protocolo, direção de fluxo e SLAs acordados | Sempre — serve como base textual acessível para qualquer público |
| Tabela | Tabela estruturada com colunas Sistema, Protocolo, Direção, Volume e SLA | Sempre — permite comparação rápida e consulta pontual |
| Diagrama de rede | Diagrama com o sistema central no meio e os sistemas externos ao redor, conectados por setas indicando direção (inbound/outbound/bidirecional), protocolo e volume | Quando é necessário visualizar o ecossistema de integrações de forma holística, mostrando dependências, protocolos e fluxos de dados entre sistemas |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
