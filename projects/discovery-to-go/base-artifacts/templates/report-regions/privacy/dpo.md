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
