---
region-id: REG-SEC-01
title: "Classificação de Dados"
group: security
description: "Inventário de dados com classificação de sensibilidade e tratamento requerido"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (dado, classificação, tratamento)"
template-visual: "Table com color-coded badges"
default: true
---

# Classificação de Dados

Categoriza todos os dados manipulados pelo sistema segundo seu nível de sensibilidade, definindo o tratamento de segurança adequado para cada categoria. Essa classificação é a base para decisões de criptografia, controle de acesso e conformidade regulatória.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| dado | string | Nome ou tipo do dado |
| classificação | enum | Público, Interno, Confidencial, Restrito |
| tratamento | string | Medidas de proteção requeridas |

## Exemplo

| Dado | Classificação | Tratamento |
|------|---------------|------------|
| Nome completo do usuário | Confidencial | Criptografia em repouso, acesso via RBAC, mascaramento em logs |
| CPF | Restrito | Criptografia AES-256, acesso restrito a perfis autorizados, tokenização em integrações |
| Saldo de conta | Restrito | Criptografia em trânsito e repouso, audit trail obrigatório |
| Histórico de transações | Confidencial | Criptografia em repouso, retenção de 5 anos, acesso auditado |
| Preferências de dashboard | Interno | Controle de acesso padrão, sem criptografia adicional |
| Documentação pública da API | Público | Sem restrições de acesso |
