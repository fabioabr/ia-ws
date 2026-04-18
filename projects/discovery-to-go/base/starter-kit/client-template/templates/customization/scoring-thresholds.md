---
title: "Scoring Thresholds — pisos de nota do auditor e 10th-man"
description: "Pisos por dimensão e threshold global do auditor convergente (Fase 2) e do 10th-man divergente"
version: "01.00.000"
status: "default"
origin: "base/starter-kit/client-template/templates/customization/scoring-thresholds.md"
---

# Scoring Thresholds

Define os **pisos de nota** do `auditor` (gate convergente) e do `10th-man` (gate divergente) usados na Fase 2 (Challenge) do Discovery Pipeline v0.5. Os valores aqui são **defaults** — cada cliente pode sobrescrever copiando este arquivo para `{project}/setup/customization/rules/scoring-thresholds.md` e editando.

## Auditor — Gate Convergente

### Pesos e pisos por dimensão

| Dimensão | Peso | Piso mínimo | Observação |
|---|---|---|---|
| Completude | 25% | 80% | Cobertura do checklist do context-template + briefing |
| Fundamentação | 25% | 70% | `[INFERENCE]` em áreas críticas sem validação prévia |
| Coerência interna | 20% | 70% | Contradições silenciosas entre drafts |
| Profundidade | 15% | 60% | ≥ 3 parágrafos ou estrutura com sub-seções |
| Neutralidade | 15% | 70% | Perguntas indutivas dos especialistas |

### Regra de aprovação

```
aprovado = (todos_os_pisos_atendidos) AND (media_ponderada >= threshold_global)
```

### Threshold global

| Parâmetro | Default |
|---|---|
| `threshold-global-approval` | **90%** |

### Modificadores condicionais às flags do briefing

Estes ajustes neutralizam penalizações indevidas quando o briefing declara explicitamente que um tópico é opcional (ver [discovery.md](../../../../behavior/rules/discovery/discovery.md) — seção "Flags de configuração"):

| Condição | Efeito no auditor |
|---|---|
| `require_roi=false` | Remover do checklist de Completude: ROI, payback, break-even, receita projetada. Omitir validação automática Receita × TCO. |
| `financial_model=fundo-global` | Substituir critério "TCO completo" por "estimativa de consumo cloud sem free tier" no bloco 1.8. Omitir validação Receita × TCO. |
| `financial_model=fundo-global` AND falta estimativa de consumo | -10 pontos em Completude |
| `deliverables_scope` contém apenas `["DR"]` | Nenhum ajuste — DR é piso do pipeline, sempre auditado completo |

### Penalidades específicas

| Situação | Penalidade |
|---|---|
| Receita < TCO em 20%+ (modo projeto-paga + require_roi) | -15 pts em Completude + `[VIABILIDADE-NEGATIVA]` |
| Risco com mitigação genérica (severidade Alta) | -10 pts em Profundidade por risco |
| Risco com mitigação genérica (severidade Média) | -5 pts em Profundidade por risco |
| Resposta do customer sem tag (`[BRIEFING]`/`[RAG]`/`[INFERENCE]`) | Reprova automática |

## 10th-man — Gate Divergente

### Dimensões

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Criticalidade das questões | 40% | 60% — questões precisam desafiar hipóteses reais, não cosméticas |
| Cruzamento com fontes | 40% | 60% — questões ancoradas em gaps/contradições observáveis nos drafts |
| Cobertura cross-eixo | 20% | 50% — perguntas tocam múltiplos eixos (produto, técnico, privacidade, risco) |

### Threshold global

| Parâmetro | Default |
|---|---|
| `threshold-10th-man-approval` | **70%** |

Nota: o 10th-man tem threshold **mais baixo** que o auditor porque sua função é **provocar**, não validar — é esperado que suas notas sejam mais variáveis.

## Customização por perfil

Perfis predefinidos (o orchestrator pode aplicar via `config.md` da run):

| Perfil | Auditor global | 10th-man global | Uso |
|---|---|---|---|
| `conservador` | 92% | 75% | Projetos regulados (LGPD/SOX) com alto custo de erro |
| `default` | 90% | 70% | Projetos típicos |
| `rapido` | 85% | 65% | PoCs, hackathons, projetos experimentais |

Aplicação: `scoring-profile: conservador` no frontmatter do `config.md`.

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 01.00.000 | 2026-04-17 | Criação — origem task #9 do TODO. Pisos e pesos originais da rule `discovery.md`. Modificadores condicionais novos (ADR-001 + tasks #3 e #4). |
