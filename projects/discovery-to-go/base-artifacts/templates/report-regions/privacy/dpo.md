---
region-id: REG-PRIV-03
title: "Encarregado de Dados (DPO)"
group: privacy
description: "Informações de contato e responsabilidades do DPO"
source: "Bloco #6 (cyber) → 1.6"
schema: "Texto + contato"
template-visual: "Card simples"
default: "quando há PII"
---

# Encarregado de Dados (DPO)

Identifica o Encarregado de Proteção de Dados (DPO) responsável pelo projeto, conforme exigido pela LGPD. O DPO é o ponto de contato entre a organização, os titulares dos dados e a ANPD, e deve ser facilmente acessível.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| nome | string | Nome do DPO |
| cargo | string | Cargo na organização |
| email | string | E-mail de contato público |
| telefone | string | Telefone de contato (opcional) |
| responsabilidades | lista | Principais atribuições no contexto do projeto |

## Exemplo

**Encarregado de Dados designado:**

- **Nome:** Maria Helena Rodrigues
- **Cargo:** Data Protection Officer — Diretoria de Compliance
- **E-mail:** dpo@fintrackpro.com.br
- **Telefone:** +55 (11) 3000-0000 ramal 400

**Responsabilidades no contexto do FinTrack Pro:**
- Validar a adequação do tratamento de dados pessoais antes de cada release
- Responder solicitações de titulares (acesso, correção, exclusão) em até 15 dias úteis
- Conduzir o RIPD (Relatório de Impacto à Proteção de Dados) quando aplicável
- Reportar incidentes de dados pessoais à ANPD no prazo legal
- Participar das reviews de arquitetura que envolvam novos tratamentos de dados

## Representação Visual

### Dados de amostra

As informações do DPO podem ser representadas como texto corrido de apresentação, complementado por um card simples com dados de contato e responsabilidades.

**Texto corrido:** "O Encarregado de Dados (DPO) designado para o FinTrack Pro é Maria Helena Rodrigues, da Diretoria de Compliance. Ela é responsável por validar o tratamento de dados em cada release, responder solicitações de titulares em até 15 dias úteis, conduzir o RIPD e reportar incidentes à ANPD. O canal de contato público é dpo@fintrackpro.com.br."

**Card simples:**

| Campo | Informação |
|-------|------------|
| Nome | Maria Helena Rodrigues |
| Cargo | Data Protection Officer — Diretoria de Compliance |
| E-mail | dpo@fintrackpro.com.br |
| Telefone | +55 (11) 3000-0000 ramal 400 |
| Responsabilidades | Validação de tratamentos, resposta a titulares (SLA 15 dias), RIPD, reporte à ANPD, review de arquitetura |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo apresentando o DPO, suas responsabilidades e canal de contato | Para contexto em relatórios executivos e documentos de governança |
| Tabela/Card simples | Card com campos estruturados (nome, cargo, contato, responsabilidades) | Para referência rápida em dashboards e páginas de compliance |
| Card visual com avatar | Card estilizado com foto/avatar, dados de contato e lista de responsabilidades | Para portais de privacidade voltados a titulares de dados |
| Organograma | Posição do DPO na estrutura organizacional com linhas de reporte | Para documentação de governança e apresentações ao board |
| Contact card interativo | Card clicável com links diretos para e-mail e telefone | Para versões digitais de relatórios e portais internos |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
