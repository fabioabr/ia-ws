---
region-id: REG-PROD-05
title: "OKRs and ROI"
group: product
description: "Objetivos mensuráveis, métricas norte, ROI esperado, critério de sucesso do MVP"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Table com progress indicators"
default: true
---

# OKRs and ROI

Objetivos e resultados-chave (OKRs) que definem o sucesso do produto em termos mensuráveis, acompanhados da análise de retorno sobre investimento (ROI). Esta region traduz a visão do produto em metas concretas com prazos e métricas, permitindo que stakeholders avaliem progresso e que o time de produto tome decisões de priorização baseadas em impacto.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| okrs | list | Cada item: `{ objetivo: string, key_results: list }` |
| key_results[n] | object | `{ kr: string, baseline: string, target: string, prazo: string }` |
| roi | object | `{ investimento: string, retorno_anual: string, payback: string, premissas: list }` |
| criterio_mvp | list | Condições mensuráveis para considerar o MVP bem-sucedido |

## Exemplo

```markdown
## OKRs e ROI

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

### ROI

| Métrica | Valor |
|---------|-------|
| **Investimento total (3 anos)** | R$ 2,1M — R$ 2,8M |
| **Economia anual estimada** | R$ 500K — R$ 700K (horas + retrabalho + risco) |
| **Payback** | 14 meses |
| **ROI em 3 anos** | 75% — 100% |

**Premissas:**
- Custo médio hora/analista: R$ 120
- 4 analistas × 10h economizadas/semana × 48 semanas
- Redução de custo de retrabalho de auditoria: R$ 80K/ano
- Sem considerar benefícios intangíveis (reputação, velocidade de decisão)

### Critérios de sucesso do MVP

- [ ] Consolidação de 3 filiais executada sem intervenção manual
- [ ] Zero erros materiais em 3 ciclos de fechamento consecutivos
- [ ] Fechamento mensal em D+3 ou menos
- [ ] NPS dos analistas ≥ 40
```
