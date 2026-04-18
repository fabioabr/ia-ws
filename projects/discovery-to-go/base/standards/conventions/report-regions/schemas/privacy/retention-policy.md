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

## Representação Visual

### Dados de amostra

A política de retenção pode ser representada como texto corrido resumindo a estratégia, complementado por uma tabela detalhada e uma timeline de retenção.

**Texto corrido:** "O FinTrack Pro aplica prazos de retenção diferenciados por tipo de dado, variando de 15 minutos (cookies de sessão) a 5 anos (transações financeiras e logs de auditoria, por exigência regulatória). Dados cadastrais são mantidos enquanto a conta estiver ativa, com anonimização automática 6 meses após o cancelamento. Todos os processos de descarte são automatizados."

**Tabela/Timeline de retenção:**

| Dado | Retenção | Processo de Descarte | Tipo |
|------|----------|---------------------|------|
| Cookies de sessão | 15 minutos | Expiração automática (Redis TTL) | Automático |
| Logs de acesso | 90 dias | Exclusão automática (Datadog) | Automático |
| Backups de banco | 30 dias (rolling) | Exclusão automática (RDS) | Automático |
| Dados cadastrais | Conta ativa + 6 meses | Anonimização via job agendado | Automático |
| Transações financeiras | 5 anos | Migração para cold storage anonimizado | Regulatório |
| Logs de auditoria | 5 anos | S3 Glacier → exclusão automática | Regulatório |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela simples com colunas dado, retencao e processo de descarte
**Tecnologia:** HTML/CSS
**Justificativa:** Politica de retencao combina dados textuais (tipo de dado, processo de descarte) com prazos variados. Uma tabela simples e o formato mais direto para documentacao de compliance e referencia operacional, cobrindo todos os campos necessarios sem complexidade visual desnecessaria.
**Alternativa:** Grafico de barras horizontais (HTML/CSS com barras puras) — quando houver 6+ itens com faixas de tempo comparaveis e o objetivo for visualizar a escala relativa dos prazos (minutos vs. anos).
