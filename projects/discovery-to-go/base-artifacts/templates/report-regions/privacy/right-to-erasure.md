---
region-id: REG-PRIV-05
title: "Direito à Exclusão"
group: privacy
description: "Fluxo e mecanismos para atendimento ao direito de eliminação de dados"
source: "Bloco #6 (cyber) → 1.6"
schema: "Texto + fluxo"
template-visual: "Card com callout"
default: false
---

# Direito à Exclusão

Descreve como o sistema atende ao direito de eliminação de dados pessoais previsto na LGPD (Art. 18, VI). Inclui o fluxo de solicitação, os mecanismos técnicos implementados e as exceções aplicáveis onde a exclusão não é possível por obrigação legal.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| fluxo | texto/diagrama | Passos desde a solicitação até a confirmação |
| mecanismo | texto | Como a exclusão é implementada tecnicamente |
| exceções | lista | Dados que não podem ser excluídos e motivo legal |
| SLA | string | Prazo para atendimento da solicitação |

## Exemplo

**SLA de atendimento:** Até 15 dias úteis após a confirmação de identidade do titular

**Fluxo de exclusão:**

1. **Solicitação** — Titular envia pedido via formulário no app ou e-mail para dpo@fintrackpro.com.br
2. **Verificação de identidade** — Sistema solicita confirmação via e-mail cadastrado + código MFA
3. **Análise de viabilidade** — DPO verifica se há obrigação legal que impeça a exclusão
4. **Execução** — API de erasure anonimiza dados pessoais (substitui por hash irreversível)
5. **Propagação** — Evento de exclusão é disparado para todos os sub-processadores (SendGrid, Datadog)
6. **Confirmação** — Titular recebe e-mail confirmando a exclusão com protocolo de atendimento

**Mecanismo técnico:** Soft-delete seguido de anonimização irreversível. Campos PII substituídos por `ERASED-{hash}`. Registros financeiros mantidos com dados anonimizados para conformidade regulatória.

**Exceções (dados não excluídos):**
- **Transações financeiras** — Obrigação legal de retenção por 5 anos (Resolução BCB); dados anonimizados mas registros mantidos
- **Logs de auditoria** — Mantidos por exigência de compliance SOC 2; dados pessoais mascarados
- **Dados em backups** — Excluídos naturalmente pela rotação de backups (30 dias)
