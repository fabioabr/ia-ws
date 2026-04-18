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

## Representação Visual

### Dados de amostra

O status de compliance pode ser representado como texto corrido com visão geral, complementado por uma tabela detalhada e um dashboard de status com badges.

**Texto corrido:** "Das 5 regulamentações mapeadas, 2 estão em conformidade total (PCI-DSS v4.0 e Resolução BCB 85/2021), 2 em conformidade parcial (LGPD e SOC 2 Type II) e 1 não conforme (ISO 27001). As ações corretivas para LGPD e SOC 2 estão planejadas para as próximas sprints, enquanto a certificação ISO 27001 segue um roadmap separado para Q3 2026."

**Dashboard de status com badges:**

| Regulação | Status | Gap | Ação |
|-----------|--------|-----|------|
| LGPD (Lei 13.709/2018) | Parcial | Falta mecanismo automatizado de exclusão de dados pessoais | Implementar endpoint de right-to-erasure na Sprint 8 |
| PCI-DSS v4.0 | Conforme | — | Conformidade via Stripe |
| SOC 2 Type II | Parcial | Logs de auditoria incompletos | Expandir audit trail até Sprint 6 |
| Resolução BCB 85/2021 | Conforme | — | Políticas já documentadas e aprovadas |
| ISO 27001 | Não conforme | Sem certificação; controles parciais | Roadmap de certificação (Q3 2026) |

**Resumo visual:**

| Status | Quantidade | Proporção |
|--------|:----------:|-----------|
| Conforme | 2 | 40% |
| Parcial | 2 | 40% |
| Não conforme | 1 | 20% |

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com status badges verde/amarelo/vermelho
**Tecnologia:** HTML/CSS
**Justificativa:** Regulamentações com status tricolor (Conforme, Parcial, Não conforme) são ideais para tabela com badges coloridos. Cada linha mostra regulação, status com badge, gap e ação corretiva, permitindo tanto visão geral do compliance quanto drill-down nos gaps específicos.
**Alternativa:** Dashboard de compliance com indicadores (HTML/CSS) — quando houver 8+ regulamentações e o foco for o percentual geral de conformidade em vez do detalhe por regulação.
