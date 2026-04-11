---
region-id: REG-SEC-02
title: "Autenticação e Autorização"
group: security
description: "Modelo de autenticação, MFA, SSO e controle de acesso"
source: "Bloco #5/#6"
schema: "Texto + tabela (método, MFA, SSO, RBAC)"
template-visual: "Card com checklist"
default: true
---

# Autenticação e Autorização

Define o modelo de autenticação e autorização adotado, incluindo mecanismos de MFA, integração com SSO corporativo e estratégia de controle de acesso baseado em papéis (RBAC). Garante que apenas usuários autorizados acessem recursos adequados ao seu perfil.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| método | string | Método de autenticação principal |
| MFA | string | Tipo de segundo fator |
| SSO | string | Protocolo e provider de SSO |
| RBAC | tabela | Papéis e permissões associadas |

## Exemplo

**Método de autenticação:** SAML 2.0 via Okta (SSO corporativo) com fallback para e-mail + senha

**MFA:** Obrigatório para todos os usuários — TOTP (Google Authenticator, Authy) ou push notification via Okta Verify

**SSO:** Integração com Okta via SAML 2.0; provisionamento automático (SCIM) para criação e desativação de contas

**Papéis e permissões (RBAC):**

| Papel | Visualizar Dashboards | Criar Relatórios | Aprovar Transações | Gerenciar Usuários | Configurar Regras |
|-------|:---------------------:|:-----------------:|:------------------:|:------------------:|:-----------------:|
| Analista | Sim | Sim | Nao | Nao | Nao |
| Gerente Financeiro | Sim | Sim | Sim | Nao | Nao |
| Administrador | Sim | Sim | Sim | Sim | Sim |
| Auditor (read-only) | Sim | Sim | Nao | Nao | Nao |
