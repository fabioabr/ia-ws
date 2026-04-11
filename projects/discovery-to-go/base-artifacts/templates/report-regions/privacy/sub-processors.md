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

## Representação Visual

### Dados de amostra

Os sub-operadores podem ser representados como texto corrido resumindo o cenário de terceiros, complementado por uma tabela detalhada com status de DPA.

**Texto corrido:** "O FinTrack Pro compartilha dados pessoais com 6 sub-operadores. Cinco possuem DPA assinado e vigente (AWS, Okta, SendGrid, Stripe e Datadog), enquanto o Zendesk está em fase de negociação com previsão de assinatura até a Sprint 4. Os dados compartilhados variam de identificadores básicos (nome, e-mail) até dados de transação, sempre respeitando o princípio da minimização."

**Tabela com status de DPA:**

| Sub-operador | Dados Compartilhados | DPA Status | Risco |
|--------------|---------------------|------------|-------|
| AWS (hospedagem) | Todos os dados (criptografados) | Assinado | Baixo |
| Okta (autenticação) | Nome, e-mail, identificador | Assinado | Baixo |
| SendGrid (e-mail) | Nome, e-mail | Assinado | Baixo |
| Stripe (pagamentos) | Nome, e-mail, dados de transação | Assinado | Baixo |
| Datadog (observabilidade) | IP, user-agent (em logs) | Assinado | Baixo |
| Zendesk (suporte) | Nome, e-mail, conteúdo de tickets | Em negociação | Médio |

**Resumo de status:**

| DPA Status | Quantidade | Proporção |
|------------|:----------:|-----------|
| Assinado | 5 | 83% |
| Em negociação | 1 | 17% |
| Pendente | 0 | 0% |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com status badges verde/amarelo/vermelho para DPA
**Tecnologia:** HTML/CSS
**Justificativa:** Sub-operadores com status de DPA tricolor (Assinado, Em negociacao, Pendente) seguem o mesmo padrao eficaz de compliance com badges. Cada linha mostra fornecedor, dados compartilhados e status com badge colorido, permitindo identificar rapidamente riscos contratuais.
**Alternativa:** Risk matrix (HTML/CSS) — quando houver muitos sub-operadores (10+) e o objetivo for priorizar acoes cruzando volume de dados com status do DPA.
