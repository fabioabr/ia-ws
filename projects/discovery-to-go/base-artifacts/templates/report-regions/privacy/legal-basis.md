---
region-id: REG-PRIV-02
title: "Bases Legais"
group: privacy
description: "Base legal LGPD para cada tipo de tratamento de dados pessoais"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (tratamento, base legal, justificativa)"
template-visual: "Table com badges"
default: "quando há PII"
---

# Bases Legais

Associa cada operação de tratamento de dados pessoais à sua respectiva base legal conforme a LGPD. Essa documentação é exigida pelo princípio da responsabilização e prestação de contas, e deve ser apresentada à ANPD quando solicitado.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| tratamento | string | Descrição da operação de tratamento |
| base_legal | string | Base legal LGPD aplicável |
| justificativa | string | Fundamentação da escolha |

## Exemplo

| Tratamento | Base Legal | Justificativa |
|------------|-----------|---------------|
| Cadastro de usuário (nome, e-mail, CPF) | Execução de contrato (Art. 7, V) | Dados necessários para criação de conta e prestação do serviço contratado |
| Armazenamento de CPF para validação regulatória | Obrigação legal (Art. 7, II) | Exigido pela Resolução BCB 85/2021 e normas de prevenção à lavagem de dinheiro |
| Envio de e-mails transacionais | Execução de contrato (Art. 7, V) | Notificações essenciais ao funcionamento do serviço (confirmações, alertas) |
| Envio de e-mails de marketing | Consentimento (Art. 7, I) | Opt-in explícito no cadastro, com opção de revogação a qualquer momento |
| Registro de IP e logs de acesso | Legítimo interesse (Art. 7, IX) | Necessário para segurança da plataforma e investigação de incidentes |
| Analytics de uso do produto | Legítimo interesse (Art. 7, IX) | Melhoria do serviço; dados anonimizados quando possível |
