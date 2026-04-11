---
region-id: REG-PRIV-04
title: "Política de Retenção"
group: privacy
description: "Prazos de retenção e processos de descarte para cada tipo de dado"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (dado, retenção, processo)"
template-visual: "Table simples"
default: "quando há PII"
---

# Política de Retenção

Define por quanto tempo cada tipo de dado é mantido no sistema e qual processo é utilizado para seu descarte. A retenção mínima necessária é um princípio fundamental da LGPD, e prazos claros facilitam automação e auditoria.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| dado | string | Tipo de dado |
| retenção | string | Prazo de retenção |
| processo | string | Como o dado é descartado ao fim do prazo |

## Exemplo

| Dado | Retenção | Processo de Descarte |
|------|----------|---------------------|
| Dados cadastrais (nome, e-mail, CPF) | Enquanto a conta estiver ativa + 6 meses após cancelamento | Anonimização automática via job agendado; registros financeiros mantidos separadamente |
| Transações financeiras | 5 anos após a transação | Exigência regulatória (BCB); após o prazo, migração para cold storage anonimizado |
| Logs de acesso (IP, user-agent) | 90 dias | Exclusão automática via política de retenção do Datadog |
| Logs de auditoria | 5 anos | Armazenamento em S3 Glacier; exclusão automática após expiração |
| Cookies de sessão | 15 minutos (TTL Redis) | Expiração automática pelo Redis |
| Backups de banco de dados | 30 dias (rolling) | Exclusão automática pela política de retenção do RDS |
