---
region-id: REG-PRIV-01
title: "Inventário de Dados Pessoais"
group: privacy
description: "Mapeamento de dados pessoais com localização, acesso e base legal"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (dado, local, acesso, base legal)"
template-visual: "Table detalhada"
default: "quando há PII"
---

# Inventário de Dados Pessoais

Cataloga todos os dados pessoais tratados pelo sistema, identificando onde são armazenados, quem tem acesso e qual base legal ampara o tratamento. Esse inventário é obrigatório pela LGPD e serve como referência para auditorias e solicitações de titulares.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| dado | string | Tipo de dado pessoal |
| local | string | Onde o dado é armazenado |
| acesso | string | Quem/quais sistemas acessam |
| base_legal | string | Base legal LGPD para o tratamento |

## Exemplo

| Dado Pessoal | Local de Armazenamento | Acesso | Base Legal |
|--------------|----------------------|--------|------------|
| Nome completo | PostgreSQL (tabela `users`) | API Core, Painel Admin | Execução de contrato (Art. 7, V) |
| CPF | PostgreSQL (tabela `users`, campo criptografado) | API Core (tokenizado em integrações) | Obrigação legal/regulatória (Art. 7, II) |
| E-mail | PostgreSQL (tabela `users`) + SendGrid | API Core, Notification Service | Execução de contrato (Art. 7, V) |
| Endereço IP | Logs Datadog (retenção 30 dias) | Time de SRE | Legítimo interesse (Art. 7, IX) — segurança |
| Dados de transação financeira | PostgreSQL (tabela `transactions`) | API Core, Relatórios | Obrigação legal/regulatória (Art. 7, II) |
| Cookies de sessão | Redis (TTL 15min) + navegador | API Gateway | Consentimento (Art. 7, I) — via banner de cookies |
