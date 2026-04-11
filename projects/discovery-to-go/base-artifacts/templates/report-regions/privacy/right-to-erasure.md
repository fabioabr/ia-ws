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

## Representação Visual

### Dados de amostra

O direito à exclusão pode ser representado como texto corrido descrevendo o processo, complementado por um diagrama de fluxo detalhado e uma tabela de exceções.

**Texto corrido:** "O FinTrack Pro atende ao direito de eliminação (Art. 18, VI da LGPD) com SLA de 15 dias úteis. O fluxo envolve 6 etapas: solicitação pelo titular, verificação de identidade via MFA, análise de viabilidade pelo DPO, execução via API de erasure (anonimização irreversível), propagação para sub-processadores e confirmação ao titular. Dados financeiros e logs de auditoria são exceções por obrigação legal, sendo mantidos de forma anonimizada."

**Diagrama de fluxo:**

```
[Titular] → Solicitação (formulário/e-mail)
     ↓
[Sistema] → Verificação de identidade (e-mail + MFA)
     ↓
[DPO] → Análise de viabilidade (obrigações legais?)
     ↓                              ↓
  Aprovado                      Negado (parcial)
     ↓                              ↓
[API Erasure] → Anonimização    Dados regulatórios
  (PII → ERASED-{hash})        mantidos anonimizados
     ↓
[Propagação] → SendGrid, Datadog (evento de exclusão)
     ↓
[Confirmação] → E-mail ao titular com protocolo
```

**Tabela de exceções:**

| Dado | Motivo da Retenção | Tratamento |
|------|--------------------|------------|
| Transações financeiras | Obrigação legal — Resolução BCB (5 anos) | Dados anonimizados, registros mantidos |
| Logs de auditoria | Compliance SOC 2 | Dados pessoais mascarados |
| Dados em backups | Limitação técnica | Excluídos pela rotação (30 dias) |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo descrevendo o fluxo de exclusão, SLA e exceções | Para contextualizar o processo em documentos de governança e relatórios à ANPD |
| Tabela de exceções | Tabela listando dados não excluídos, motivo legal e tratamento aplicado | Para documentação de compliance e referência em auditorias |
| Diagrama de fluxo | Fluxograma detalhando cada etapa desde a solicitação até a confirmação | Para documentação técnica e treinamento de equipes de suporte |
| Swimlane diagram | Raias separando Titular, Sistema, DPO e Sub-processadores com etapas cronológicas | Para visualizar responsabilidades de cada ator no processo |
| BPMN diagram | Processo modelado em notação BPMN com gateways de decisão (viabilidade) | Para documentação formal de processos e integração com ferramentas de BPM |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
