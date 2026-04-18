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

## Representação Visual

### Dados de amostra

O inventário de dados pessoais pode ser representado como texto corrido contextualizando o mapeamento, complementado por uma tabela detalhada com status color-coded.

**Texto corrido:** "O FinTrack Pro trata 6 categorias de dados pessoais, distribuídos em 4 sistemas de armazenamento (PostgreSQL, Redis, SendGrid e Datadog). Cada dado possui base legal definida conforme a LGPD, sendo as mais frequentes Execução de contrato (Art. 7, V) e Obrigação legal (Art. 7, II). O acesso é restrito por serviço, com a API Core sendo o principal consumidor."

**Tabela com status color-coded:**

| Dado Pessoal | Local de Armazenamento | Acesso | Base Legal | Proteção |
|--------------|----------------------|--------|------------|----------|
| Nome completo | PostgreSQL (`users`) | API Core, Painel Admin | Execução de contrato (Art. 7, V) | Criptografia em repouso |
| CPF | PostgreSQL (`users`, criptografado) | API Core (tokenizado) | Obrigação legal (Art. 7, II) | Criptografia AES-256 + tokenização |
| E-mail | PostgreSQL (`users`) + SendGrid | API Core, Notification Service | Execução de contrato (Art. 7, V) | Criptografia em trânsito |
| Endereço IP | Logs Datadog (30 dias) | Time de SRE | Legítimo interesse (Art. 7, IX) | Retenção limitada |
| Dados de transação | PostgreSQL (`transactions`) | API Core, Relatórios | Obrigação legal (Art. 7, II) | Criptografia em repouso e trânsito |
| Cookies de sessão | Redis (TTL 15min) | API Gateway | Consentimento (Art. 7, I) | TTL automático |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com badges coloridos por classificação de proteção
**Tecnologia:** HTML/CSS
**Justificativa:** Inventário de dados pessoais é um registro estruturado com múltiplas colunas textuais (dado, local, acesso, base legal). Badges coloridos na coluna de proteção indicam visualmente o nível de criticidade, mantendo a completude necessária para auditorias LGPD.
**Alternativa:** Matriz dado x sistema (HTML/CSS) — quando o objetivo for analisar concentração de acesso e segregação entre sistemas, em vez do inventário completo.
