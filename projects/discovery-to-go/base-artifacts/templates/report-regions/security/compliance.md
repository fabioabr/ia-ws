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

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo com resumo do status de conformidade e próximos passos | Para visão executiva e contexto em relatórios de governança |
| Tabela com badges de status | Tabela com badges coloridos (verde = Conforme, amarelo = Parcial, vermelho = Não conforme) | Para documentação detalhada e acompanhamento de remediações |
| Dashboard de compliance | Painel com indicadores visuais de status por regulação e percentual geral de conformidade | Para apresentações a stakeholders e comitês de compliance |
| Gráfico de rosca | Gráfico circular mostrando proporção de Conforme/Parcial/Não conforme | Para visão rápida do nível geral de conformidade |
| Timeline de remediação | Linha do tempo com marcos de ações corretivas por regulação | Para acompanhamento de progresso e planejamento de sprints |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
