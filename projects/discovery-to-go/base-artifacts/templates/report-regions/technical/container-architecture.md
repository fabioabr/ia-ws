---
region-id: REG-TECH-04
title: "Arquitetura de Containers (C4 L2)"
group: technical
description: "Diagrama de containers mostrando componentes internos e suas interações"
source: "Bloco #7 (arch) → 1.7"
schema: "Diagrama Mermaid C4 L2"
template-visual: "Diagram full-width"
default: false
---

# Arquitetura de Containers (C4 L2)

Detalha os containers internos do FinTrack Pro (aplicações, serviços, bancos de dados), mostrando como se comunicam entre si e com sistemas externos. Essa visão é a referência principal para decisões de deploy, escalabilidade e ownership de componentes.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| diagram | mermaid | Diagrama C4 Container em sintaxe Mermaid |
| containers | lista | Componentes internos do sistema |
| relacionamentos | lista | Fluxos entre containers e sistemas externos |

## Exemplo

```mermaid
C4Container
    title Diagrama de Containers — FinTrack Pro

    Person(usuario, "Usuário Final")

    System_Boundary(fintrack, "FinTrack Pro") {
        Container(spa, "SPA Frontend", "React, TypeScript", "Interface do usuário")
        Container(api, "API Gateway", "Node.js, Express", "Roteamento, auth, rate limiting")
        Container(core_svc, "Core Service", "Node.js, TypeScript", "Lógica de negócio financeira")
        Container(notification_svc, "Notification Service", "Node.js", "Envio de e-mails e alertas")
        ContainerDb(db, "PostgreSQL", "Dados transacionais e configurações")
        ContainerDb(cache, "Redis", "Cache de sessão e rate limiting")
        Container(queue, "SQS", "Fila de mensagens assíncronas")
    }

    System_Ext(core, "Core Bancário")
    System_Ext(pagamentos, "Stripe")
    System_Ext(idp, "Okta")
    System_Ext(email, "SendGrid")

    Rel(usuario, spa, "HTTPS")
    Rel(spa, api, "REST/JSON")
    Rel(api, cache, "Sessão + throttle")
    Rel(api, core_svc, "gRPC")
    Rel(core_svc, db, "SQL")
    Rel(core_svc, queue, "Publica eventos")
    Rel(queue, notification_svc, "Consome eventos")
    Rel(core_svc, core, "REST API")
    Rel(core_svc, pagamentos, "REST + Webhooks")
    Rel(api, idp, "SAML/OIDC")
    Rel(notification_svc, email, "REST API")
```

## Representação Visual

### Dados de amostra

- **Ator:** Usuário Final
- **Containers internos (FinTrack Pro):** SPA Frontend (React, TypeScript), API Gateway (Node.js, Express), Core Service (Node.js, TypeScript), Notification Service (Node.js), PostgreSQL (dados transacionais), Redis (cache de sessão), SQS (fila de mensagens)
- **Sistemas externos:** Core Bancário, Stripe, Okta, SendGrid
- **Fluxos:** Usuário → SPA → API Gateway → Core Service → PostgreSQL/Core Bancário/Stripe; API Gateway → Redis/Okta; Core Service → SQS → Notification Service → SendGrid

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva detalhando cada container interno, sua responsabilidade, tecnologia e como se conecta aos demais componentes e sistemas externos | Sempre — serve como base textual acessível para qualquer público |
| Tabela | Tabela com colunas Container, Tecnologia, Responsabilidade e Conexões | Sempre — permite consulta rápida dos componentes e seus vínculos |
| Diagrama C4 Container (Mermaid) | Diagrama C4 nível 2 renderizado via Mermaid, mostrando os containers dentro do boundary do sistema com seus relacionamentos internos e conexões a sistemas externos | Quando é necessário apresentar a decomposição interna do sistema, ideal para decisões de deploy, escalabilidade e ownership de componentes |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
