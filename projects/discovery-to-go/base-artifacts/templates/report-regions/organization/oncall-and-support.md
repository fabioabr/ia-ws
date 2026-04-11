---
region-id: REG-ORG-05
title: "Plantão e Suporte"
group: organization
description: "Modelo de plantão, escalation e suporte pós-go-live"
source: "Bloco #4 (po) → 1.4"
schema: "Texto + tabela (quem, quando, escalation)"
template-visual: "Card com alert style"
default: false
---

# Plantão e Suporte

Define o modelo de suporte e plantão para o período pós-go-live, incluindo responsáveis, horários de cobertura e cadeia de escalação. Garante que incidentes críticos sejam tratados dentro dos SLAs acordados e que haja clareza sobre quem acionar em cada cenário.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| quem | string | Pessoa ou equipe responsável |
| quando | string | Período de cobertura |
| escalation | string | Próximo nível de escalação |
| canal | string | Canal de acionamento |
| SLA | string | Tempo de resposta esperado |

## Exemplo

**Modelo:** Suporte N2 dedicado em horário comercial + plantão rotativo para P1/P2

| Nível | Quem | Quando | SLA Resposta | Escalation |
|-------|------|--------|--------------|------------|
| N1 | Service Desk cliente | 24/7 | 15min (P1), 1h (P2) | Escala para N2 se não resolver em 30min |
| N2 | Time FinTrack Pro | Seg-Sex 08h-20h | 30min (P1), 2h (P2) | Escala para Tech Lead |
| N3 (plantão) | Dev rotativo | Fora do horário comercial | 1h (P1 apenas) | Escala para Head de Engenharia |

**Canais de acionamento:**
- **P1 (Crítico):** Telefone + Slack #fintrack-incidents + PagerDuty
- **P2 (Alto):** Slack #fintrack-incidents + ticket Jira
- **P3/P4:** Ticket Jira via Service Desk
