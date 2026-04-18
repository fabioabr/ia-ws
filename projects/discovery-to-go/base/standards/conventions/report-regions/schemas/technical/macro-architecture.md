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

## Representação Visual

### Dados de amostra

- **Atores:** Usuário Final (gerente financeiro/analista), Administrador (configura regras e permissões)
- **Sistema central:** FinTrack Pro — Plataforma SaaS de gestão financeira
- **Sistemas externos:** Core Bancário (Temenos), Gateway de Pagamentos (Stripe), ERP Financeiro (SAP), Identity Provider (Okta), Serviço de E-mail (SendGrid)
- **Relacionamentos:** Usuário consulta dashboards e cria relatórios; Admin gerencia usuários e regras; FinTrack consulta saldos, processa cobranças, envia lançamentos, autentica via SSO, dispara notificações

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com placeholder para diagrama
**Tecnologia:** HTML/CSS
**Justificativa:** Diagramas de arquitetura C4 são inerentemente visuais e espaciais, não redutíveis a tabelas ou gráficos de dados. O card exibe os metadados (atores, sistemas, relacionamentos) em formato estruturado e reserva um placeholder para o diagrama renderizado separadamente via diagram-drawio.
**Alternativa:** Tabela de elementos (HTML/CSS) — quando o diagrama ainda não foi gerado e é necessário listar atores, sistemas e relacionamentos de forma consultável.
