---
region-id: REG-PRIV-06
title: "Sub-operadores"
group: privacy
description: "Terceiros que processam dados pessoais e status de seus contratos de proteção de dados"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (sub-operador, dados, DPA status)"
template-visual: "Table com status"
default: false
---

# Sub-operadores

Lista todos os terceiros (sub-operadores/sub-processadores) que tratam dados pessoais em nome do FinTrack Pro. Para cada um, documenta quais dados são compartilhados e o status do Data Processing Agreement (DPA), conforme exigido pela LGPD para transferências a terceiros.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| sub_operador | string | Nome do fornecedor/serviço |
| dados | string | Tipos de dados pessoais compartilhados |
| dpa_status | enum | Assinado, Em negociação, Pendente |

## Exemplo

| Sub-operador | Dados Compartilhados | DPA Status |
|--------------|---------------------|------------|
| AWS (hospedagem) | Todos os dados armazenados (criptografados) | Assinado — AWS Data Processing Addendum vigente |
| Okta (autenticação) | Nome, e-mail, identificador de usuário | Assinado — DPA corporativo renovado em Jan/2026 |
| SendGrid (e-mail) | Nome, e-mail | Assinado — Twilio DPA padrão |
| Stripe (pagamentos) | Nome, e-mail, dados de transação (sem dados de cartão retidos) | Assinado — Stripe DPA + certificação PCI-DSS |
| Datadog (observabilidade) | Endereço IP, user-agent (em logs) | Assinado — Datadog DPA padrão |
| Zendesk (suporte) | Nome, e-mail, conteúdo de tickets | Em negociação — previsão de assinatura até Sprint 4 |
