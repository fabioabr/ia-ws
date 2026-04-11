---
region-id: REG-TECH-03
title: "Arquitetura Macro (C4 L1)"
group: technical
description: "Diagrama de contexto do sistema mostrando atores e sistemas externos"
source: "Bloco #7 (arch) → 1.7"
schema: "Diagrama Mermaid C4 L1"
template-visual: "Diagram full-width"
default: true
---

# Arquitetura Macro (C4 L1)

Apresenta o diagrama de contexto do sistema (nível 1 do modelo C4), mostrando o FinTrack Pro e suas relações com usuários e sistemas externos. Oferece a visão de mais alto nível da solução, ideal para comunicação com stakeholders não técnicos.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| diagram | mermaid | Diagrama C4 Context em sintaxe Mermaid |
| atores | lista | Pessoas/papéis que interagem com o sistema |
| sistemas_externos | lista | Sistemas fora do boundary do projeto |

## Exemplo

```mermaid
C4Context
    title Diagrama de Contexto — FinTrack Pro

    Person(usuario, "Usuário Final", "Gerente financeiro ou analista")
    Person(admin, "Administrador", "Configura regras e permissões")

    System(fintrack, "FinTrack Pro", "Plataforma SaaS de gestão financeira")

    System_Ext(core, "Core Bancário", "Temenos — saldos e extratos")
    System_Ext(pagamentos, "Gateway de Pagamentos", "Stripe — cobranças e recebimentos")
    System_Ext(erp, "ERP Financeiro", "SAP — conciliação contábil")
    System_Ext(idp, "Identity Provider", "Okta — autenticação SSO")
    System_Ext(email, "Serviço de E-mail", "SendGrid — notificações")

    Rel(usuario, fintrack, "Consulta dashboards, cria relatórios")
    Rel(admin, fintrack, "Gerencia usuários e regras")
    Rel(fintrack, core, "Consulta saldos e lança transações")
    Rel(fintrack, pagamentos, "Processa cobranças")
    Rel(fintrack, erp, "Envia lançamentos contábeis")
    Rel(fintrack, idp, "Autentica usuários via SAML/OIDC")
    Rel(fintrack, email, "Dispara notificações")
```
