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

## Representação Visual

### Dados de amostra

As bases legais podem ser representadas como texto corrido explicando a estratégia de fundamentação, complementado por uma tabela com badges por base legal.

**Texto corrido:** "O FinTrack Pro fundamenta o tratamento de dados pessoais em 3 bases legais da LGPD: Execução de contrato (Art. 7, V) para operações essenciais ao serviço, Obrigação legal (Art. 7, II) para exigências regulatórias do setor financeiro, e Legítimo interesse (Art. 7, IX) para segurança e melhoria do produto. Apenas o envio de e-mails de marketing depende de Consentimento (Art. 7, I) com opt-in explícito."

**Tabela com badges:**

| Tratamento | Base Legal | Justificativa |
|------------|-----------|---------------|
| Cadastro de usuário | Execução de contrato | Dados necessários para criação de conta |
| Armazenamento de CPF | Obrigação legal | Exigido pela Resolução BCB 85/2021 |
| E-mails transacionais | Execução de contrato | Notificações essenciais ao serviço |
| E-mails de marketing | Consentimento | Opt-in explícito com opção de revogação |
| Registro de IP e logs | Legítimo interesse | Segurança e investigação de incidentes |
| Analytics de uso | Legítimo interesse | Melhoria do serviço; dados anonimizados |

**Distribuição por base legal:**

| Base Legal | Tratamentos | Proporção |
|------------|:-----------:|-----------|
| Execução de contrato (Art. 7, V) | 2 | 33% |
| Obrigação legal (Art. 7, II) | 1 | 17% |
| Legítimo interesse (Art. 7, IX) | 2 | 33% |
| Consentimento (Art. 7, I) | 1 | 17% |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com badges coloridos por base legal
**Tecnologia:** HTML/CSS
**Justificativa:** Cada tratamento precisa mostrar sua base legal e justificativa textual. Badges com cores distintas por artigo da LGPD (ex.: azul = Execução de contrato, verde = Obrigação legal, amarelo = Legítimo interesse, roxo = Consentimento) permitem agrupamento visual imediato sem perder o detalhe da justificativa.
**Alternativa:** Cards agrupados por base legal (HTML/CSS) — quando a apresentação for para comitê de privacidade e o foco for mostrar quais tratamentos se apoiam em cada base, em vez do inventário linear.
