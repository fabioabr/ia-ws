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

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo descrevendo a estratégia de retenção e os princípios aplicados | Para contexto em documentos de governança e relatórios ao DPO |
| Tabela detalhada | Tabela com dado, prazo de retenção, processo de descarte e tipo de automação | Para documentação de compliance e referência operacional |
| Timeline horizontal | Linha do tempo mostrando os diferentes prazos de retenção em escala (minutos → anos) | Para visualização comparativa dos prazos e identificação de outliers |
| Gantt chart | Barras horizontais representando o ciclo de vida de cada tipo de dado | Para apresentações que precisam mostrar sobreposição de prazos e janelas de descarte |
| Diagrama de ciclo de vida | Fluxo mostrando criação → armazenamento → retenção → descarte para cada tipo de dado | Para documentação técnica e treinamento de equipes |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
