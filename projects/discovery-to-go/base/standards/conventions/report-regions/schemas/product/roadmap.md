---
region-id: REG-PROD-08
title: "Roadmap"
group: product
description: "Faseamento: MVP → Fase 2 → Fase N com épicos por fase"
source: "Bloco #3 (po) → 1.3"
schema: "text"
template-visual: "Timeline horizontal"
default: false
---

# Roadmap

Visão de faseamento do produto ao longo do tempo, mostrando a progressão do MVP até as fases subsequentes. Cada fase contém os épicos planejados, o prazo estimado e o marco de decisão (go/no-go) para avançar. O roadmap comunica a estratégia de entrega incremental e permite que stakeholders entendam quando cada capacidade estará disponível.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| fases | list | Cada item: `{ nome: string, periodo: string, objetivo: string, epicos: list, marco_decisao: string }` |

## Exemplo

```markdown
## Roadmap

### Fase 0 — Sprint 0 (2 semanas)

**Período:** Mai/2026
**Objetivo:** Validar viabilidade técnica da integração SAP

- PoC de integração com SAP R/3 (filial SP)
- Setup de infraestrutura (AWS + CI/CD)
- Definição de arquitetura e ADRs

**Marco:** PoC aprovada → Go para Fase 1

---

### Fase 1 — MVP (16 semanas)

**Período:** Jun — Set/2026
**Objetivo:** Consolidação automatizada de 3 filiais com P&L

- Épico 1: Ingestão de dados via API SAP (3 filiais)
- Épico 2: Engine de eliminação intercompany
- Épico 3: Geração de P&L consolidado
- Épico 4: Dashboard executivo
- Épico 5: Trilha de auditoria

**Marco:** 3 fechamentos consecutivos sem erro → Go para Fase 2

---

### Fase 2 — Escala (12 semanas)

**Período:** Out — Dez/2026
**Objetivo:** Expandir para 12 filiais + multi-moeda + balanço patrimonial

- Épico 6: Integração com 9 filiais restantes
- Épico 7: Motor de conversão cambial multi-moeda
- Épico 8: Consolidação de balanço patrimonial
- Épico 9: Relatórios customizáveis

**Marco:** 12 filiais operacionais + auditoria OK → Go para Fase 3

---

### Fase 3 — Maturidade (8 semanas)

**Período:** Q1/2027
**Objetivo:** Filiais internacionais + compliance avançado

- Épico 10: Filiais internacionais (4 países)
- Épico 11: Compliance IFRS 16 automatizado
- Épico 12: Alertas e anomaly detection
- Épico 13: API para integração com BI externo
```

## Representação Visual

### Dados de amostra

| Fase | Período | Duração | Épicos | Marco de decisão |
|------|---------|---------|--------|-----------------|
| Fase 0 — Sprint 0 | Mai/2026 | 2 semanas | 3 atividades | PoC aprovada |
| Fase 1 — MVP | Jun-Set/2026 | 16 semanas | 5 épicos | 3 fechamentos sem erro |
| Fase 2 — Escala | Out-Dez/2026 | 12 semanas | 4 épicos | 12 filiais + auditoria OK |
| Fase 3 — Maturidade | Q1/2027 | 8 semanas | 4 épicos | — |

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Timeline horizontal com fases como blocos coloridos e marcos como diamantes
**Tecnologia:** HTML/CSS
**Justificativa:** São 4 fases sequenciais com duração, épicos e marcos de decisão. Uma timeline horizontal com blocos proporcionais à duração, sub-itens de épicos e ícones de marco comunica a progressão temporal e o faseamento de forma imediatamente compreensível para stakeholders executivos.
**Alternativa:** Tabela estilizada (HTML/CSS) — quando o público for técnico e preferir ver todos os detalhes (épicos, datas, marcos) em formato denso e exportável.
