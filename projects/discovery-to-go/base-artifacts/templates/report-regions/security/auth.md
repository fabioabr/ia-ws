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

## Representação Visual

### Dados de amostra

O modelo de autenticação e autorização pode ser representado como texto corrido descrevendo o fluxo, complementado por uma tabela RBAC e um diagrama de fluxo de autenticação.

**Texto corrido:** "O acesso ao FinTrack Pro é controlado por autenticação SAML 2.0 via Okta com MFA obrigatório (TOTP ou push notification). O provisionamento de contas é automatizado via SCIM, e o modelo RBAC define 4 papéis com permissões progressivas — do Analista (somente visualização e relatórios) ao Administrador (acesso total). Um perfil de Auditor read-only garante segregação para processos de compliance."

**Diagrama de fluxo de autenticação:**

```
Usuário → Login Page → Okta (SAML 2.0)
                           ├─ Autenticação primária (credenciais)
                           ├─ MFA (TOTP / Push Okta Verify)
                           ├─ Token SAML assertion
                           └─ Retorno ao app → Sessão criada
                                                  └─ RBAC aplicado por papel
```

**Tabela RBAC:**

| Papel | Visualizar Dashboards | Criar Relatórios | Aprovar Transações | Gerenciar Usuários | Configurar Regras |
|-------|:---------------------:|:-----------------:|:------------------:|:------------------:|:-----------------:|
| Analista | Sim | Sim | Nao | Nao | Nao |
| Gerente Financeiro | Sim | Sim | Sim | Nao | Nao |
| Administrador | Sim | Sim | Sim | Sim | Sim |
| Auditor (read-only) | Sim | Sim | Nao | Nao | Nao |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo descrevendo o modelo de autenticação, MFA e estratégia de autorização | Para contextualizar a abordagem de segurança de acesso em documentos executivos |
| Tabela RBAC | Matriz de papéis vs. permissões com marcadores visuais (Sim/Não) | Para referência técnica de controle de acesso e auditorias |
| Diagrama de fluxo | Fluxograma mostrando as etapas desde o login até a sessão autenticada com RBAC | Para documentação técnica e onboarding de desenvolvedores |
| Swimlane diagram | Raias separando Usuário, IdP (Okta), Aplicação e RBAC Engine | Para visualizar responsabilidades de cada componente no fluxo de autenticação |
| Checklist card | Card com ícones de status para cada mecanismo (SSO, MFA, SCIM, RBAC) | Para dashboards de postura de segurança e relatórios de compliance |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
