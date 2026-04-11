---
region-id: REG-SEC-04
title: "Compliance"
group: security
description: "Status de conformidade regulatória com gaps identificados e ações corretivas"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (regulação, status, gap, ação)"
template-visual: "Table com status badges"
default: true
---

# Compliance

Mapeia as regulamentações aplicáveis ao projeto, avaliando o status atual de conformidade, gaps identificados e ações corretivas planejadas. Permite acompanhar a evolução da adequação regulatória e priorizar remediações antes do go-live.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| regulação | string | Nome da regulamentação ou norma |
| status | enum | Conforme, Parcial, Não conforme, N/A |
| gap | string | Descrição do gap identificado |
| ação | string | Ação corretiva planejada |

## Exemplo

| Regulação | Status | Gap | Ação |
|-----------|--------|-----|------|
| LGPD (Lei 13.709/2018) | Parcial | Falta mecanismo automatizado de exclusão de dados pessoais | Implementar endpoint de right-to-erasure na Sprint 8 |
| PCI-DSS v4.0 | Conforme | — | Conformidade via Stripe (não armazenamos dados de cartão) |
| SOC 2 Type II | Parcial | Logs de auditoria não cobrem 100% das operações administrativas | Expandir cobertura de audit trail até Sprint 6 |
| Resolução BCB 85/2021 | Conforme | — | Políticas de segurança cibernética já documentadas e aprovadas |
| ISO 27001 | Não conforme | Empresa não possui certificação; controles parcialmente implementados | Roadmap de certificação em paralelo (Q3 2026) |
