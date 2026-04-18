---
region-id: REG-PROD-05A
title: "OKRs"
group: product
description: "Objetivos mensuráveis (OKRs) e critérios de sucesso do MVP"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Progress bars + stat cards"
default: true
deliverable-scope: ["OP", "EX", "DR"]
---

# OKRs

Objetivos e resultados-chave (OKRs) que definem o sucesso do produto em termos mensuráveis. Esta region traduz a visão do produto em metas concretas com prazos e métricas, permitindo que stakeholders avaliem progresso e que o time de produto tome decisões de priorização baseadas em impacto. Acompanhada dos critérios de sucesso do MVP.

> [!info] Separação OKRs vs ROI (ADR-001)
> OKRs estão **sempre** presentes em todos os entregáveis (OP, EX, DR) — são a base de avaliação de sucesso do produto. A justificativa de **ROI/payback** foi separada em region própria ([roi.md](roi.md)), condicional à flag `require_roi=true` do briefing. Por padrão (`require_roi=false`), o OP do Discovery-to-Go foca em esforço/custo/escopo, não em justificativa de retorno.

## Schema de dados

| Campo | Tipo | Formato | Condicional |
|-------|------|---------|-------------|
| okrs | list | Cada item: `{ objetivo: string, key_results: list }` | sempre |
| key_results[n] | object | `{ kr: string, baseline: string, target: string, prazo: string }` | sempre |
| criterio_mvp | list | Condições mensuráveis para considerar o MVP bem-sucedido | sempre |

## Exemplo

```markdown
## OKRs

### OKRs — Fase MVP

**Objetivo 1: Eliminar erros na consolidação financeira**

| Key Result | Baseline | Target | Prazo |
|-----------|----------|--------|-------|
| Reduzir erros materiais em relatórios ao conselho | 3 por semestre | 0 por semestre | Q4 2026 |
| Atingir 100% de rastreabilidade em cálculos de eliminação | 0% (manual) | 100% (auditável) | Q4 2026 |

**Objetivo 2: Acelerar o fechamento mensal**

| Key Result | Baseline | Target | Prazo |
|-----------|----------|--------|-------|
| Reduzir tempo de fechamento consolidado | D+8 | D+2 | Q4 2026 |
| Reduzir horas semanais de consolidação por analista | 12h | 2h | Q4 2026 |

**Objetivo 3: Viabilizar escala operacional**

| Key Result | Baseline | Target | Prazo |
|-----------|----------|--------|-------|
| Consolidar filiais sem aumento de headcount | 12 filiais / 4 analistas | 20 filiais / 4 analistas | Q2 2027 |
| Tempo de onboarding de nova filial | 4 semanas (manual) | 2 dias (configuração) | Q2 2027 |

### Critérios de sucesso do MVP

- [ ] Consolidação de 3 filiais executada sem intervenção manual
- [ ] Zero erros materiais em 3 ciclos de fechamento consecutivos
- [ ] Fechamento mensal em D+3 ou menos
- [ ] NPS dos analistas ≥ 40
```

## Representação Visual

### Dados de amostra

| Métrica | Baseline | Target |
|---------|----------|--------|
| Erros materiais/semestre | 3 | 0 |
| Rastreabilidade | 0% | 100% |
| Tempo de fechamento | D+8 | D+2 |
| Horas semanais/analista | 12h | 2h |

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Progress bars baseline-to-target, um por KR
**Tecnologia:** HTML/CSS
**Justificativa:** Com 4 OKRs e baseline/target claros, barras de progresso comunicam visualmente a magnitude do gap por KR. Com menos de 5 OKRs, barras HTML/CSS são mais leves e legíveis que um gráfico Chart.js.
**Alternativa:** Gráfico de barras agrupadas (Chart.js) — quando houver 5+ OKRs ou múltiplos cenários lado a lado.
