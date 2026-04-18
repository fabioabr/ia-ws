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

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela estilizada com ícones de direção e protocolo
**Tecnologia:** HTML/CSS
**Justificativa:** Integrações possuem múltiplos atributos textuais (protocolo, direção, volume, SLA) que exigem leitura detalhada; uma tabela estilizada com ícones de direção (setas) e badges de protocolo oferece clareza máxima e permite comparação linha a linha.
**Alternativa:** Diagrama de rede (via diagram-drawio) — quando o objetivo é comunicar visualmente o ecossistema de dependências para stakeholders não técnicos, gerando o diagrama como artefato separado.
