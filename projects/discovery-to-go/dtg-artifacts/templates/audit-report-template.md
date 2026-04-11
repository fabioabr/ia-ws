---
title: Audit Report Template
description: Template do relatório do auditor (gate convergente da Fase 2 — Challenge) do Discovery Pipeline v0.5. Implementa a fórmula de nota com 5 dimensões ponderadas + pisos por dimensão. Auditor roda em paralelo com o 10th-man.
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - audit
  - challenge
  - pipeline-v05
created: 2026-04-07
---

# Audit Report Template

> [!info] Como usar
> Este template é preenchido pelo agente `auditor` ao fim de cada execução da Fase 2 — Challenge (gate convergente). Auditor roda em paralelo com o 10th-man; o orchestrator dispara ambos ao mesmo tempo e consolida os relatórios quando os dois terminam. É salvo em `{project}/iteration-{i}/draft/audit-report.md`. O orchestrator usa este relatório (junto com o do 10th-man) para compilar o change request quando há reprova e fazer Update State na Pipeline Memory.

---

## Frontmatter

```markdown
---
title: Audit Report — Iteration {i}
project-name: {slug}
iteration: {i}
phase: 3
gate: 1-auditor
auditor-version: 00.01.000
generated-at: YYYY-MM-DD HH:mm
verdict: {APPROVED | REJECTED}
final-score: {0-100}
average-score: {0-100}
floor-violations: {lista de dimensões abaixo do piso, ou "none"}
---
```

---

## 1. Veredicto

```
┌─────────────────────────────────────────────┐
│                                             │
│  Verdict:   {APPROVED ✅ | REJECTED ❌}     │
│  Score:     {XX,XX%}                        │
│  Floor OK:  {Yes ✅ | No ❌}                │
│                                             │
└─────────────────────────────────────────────┘
```

**Resumo executivo:** {1-3 parágrafos explicando o motivo do veredicto e os pontos mais críticos}

**Lógica de aprovação:**
- Aprovação requer: **todos os pisos por dimensão** atendidos **E** média ponderada **≥ 90%**
- Reprovação ocorre se: qualquer dimensão abaixo do piso **OU** média < 90%

---

## 2. Notas por dimensão

### 2.1 Completude — peso 25% — piso 80%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,25 = XX,XX}

**Cálculo:**
```
Tópicos esperados (do checklist da Fase 1, alimentado pelo context pack + briefing): {N}
Tópicos cobertos pelos drafts (product-vision.md + organization.md + tech-and-security.md + strategic-analysis.md + privacy.md): {M}
Score = M/N × 100 = {XX,XX%}
```

**Tópicos cobertos:**
- {tópico 1}
- {tópico 2}
- ...

**Tópicos ausentes:**
- {tópico ausente 1} — sugestão: {o que falta}
- {tópico ausente 2} — sugestão: {o que falta}

---

### 2.2 Fundamentação — peso 25% — piso 70%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,25 = XX,XX}

**Cálculo:**
```
Total de respostas do customer: {T}
[INFERENCE] em áreas críticas (requisitos mandatórios + fronteiras duras) NÃO validadas: {C}
Score = 100% − (5% × C) = {XX,XX%}
```

**INFERENCE críticas detectadas:**

| # | Linha do log | Tópico | Justificativa do customer | Por que é crítica |
|---|---|---|---|---|
| 1 | {ref} | {tópico} | {1 linha} | {motivo} |

**Recomendação:** {pontos que precisam validação humana antes da próxima iteração}

---

### 2.3 Coerência interna — peso 20% — piso 70%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,20 = XX,XX}

**Cálculo:**
```
Contradições silenciosas detectadas (não marcadas como [CONFLICT] na entrevista): {K}
Score = 100% − (5% × K) = {XX,XX%}
```

**Contradições encontradas:**

| # | Drafts envolvidos | Descrição | Sugestão |
|---|---|---|---|
| 1 | product-vision.md × tech-and-security.md | {ex: produto exige offline mas tech-and-security.md assume cloud-only} | {qual lado prevalece ou criar [CONFLICT] explícito} |

> [!info] [CONFLICT] explícito não conta
> Conflitos marcados como `[CONFLICT]` durante a reunião são tratados pelo humano em qualquer passagem pelo Human Review compartilhado — não penalizam o auditor.

---

### 2.4 Profundidade — peso 15% — piso 60%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,15 = XX,XX}

**Cálculo:**
```
Total de tópicos cobertos: {N}
Tópicos com detalhamento adequado (≥ 3 parágrafos ou estruturados): {D}
Score = D/N × 100 = {XX,XX%}
```

**Tópicos superficiais:**
- {tópico 1} — apenas {X} parágrafos sem detalhamento
- {tópico 2} — bullet points sem contexto

---

### 2.5 Neutralidade da entrevista — peso 15% — piso 70%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,15 = XX,XX}

**Cálculo:**
```
Total de perguntas feitas pelos especialistas no log: {Q}
Perguntas detectadas como indutivas (carregam a resposta): {I}
Score = 100% − (I/Q × 100%) = {XX,XX%}
```

**Perguntas indutivas detectadas:**

| # | Quem perguntou | Linha do log | Pergunta | Reformulação sugerida |
|---|---|---|---|---|
| 1 | {po/solution-architect/cyber-security-architect} | {ref} | "Você concorda que precisa de microsserviços, certo?" | "Que tipo de arquitetura faz mais sentido para o seu volume?" |

---

## 3. Resumo da fórmula

| # | Dimensão | Score | Peso | Piso | Piso OK? | Contribuição |
|---|---|---|---|---|---|---|
| 1 | Completude | {XX,XX%} | 25% | 80% | {✅/❌} | {XX,XX} |
| 2 | Fundamentação | {XX,XX%} | 25% | 70% | {✅/❌} | {XX,XX} |
| 3 | Coerência interna | {XX,XX%} | 20% | 70% | {✅/❌} | {XX,XX} |
| 4 | Profundidade | {XX,XX%} | 15% | 60% | {✅/❌} | {XX,XX} |
| 5 | Neutralidade | {XX,XX%} | 15% | 70% | {✅/❌} | {XX,XX} |
| | **Total** | | **100%** | | **{Todos OK?}** | **{XX,XX}** |

---

## 4. Pontos para o change request

> [!warning] Apenas se REJECTED
> Esta seção só é preenchida quando o veredicto é REJECTED. O orchestrator usa esta lista para compilar o change request da próxima iteração.

### 4.1 Itens críticos (precisam ser corrigidos)

- [ ] {item crítico 1 — qual draft, qual seção, o que mudar}
- [ ] {item crítico 2}

### 4.2 Itens importantes (recomendado corrigir)

- [ ] {item importante 1}

### 4.3 Itens menores (nice to have)

- [ ] {item menor 1}

---

## 5. Evidências

**Drafts auditados:**
- `iteration-{i}/draft/product-vision.md` (versão {timestamp})
- `iteration-{i}/draft/organization.md` (versão {timestamp})
- `iteration-{i}/draft/tech-and-security.md` (versão {timestamp})
- `iteration-{i}/draft/strategic-analysis.md` (versão {timestamp})
- `iteration-{i}/draft/privacy.md` (versão {timestamp}, sempre existe — modo profundo ou magro)

**Logs consultados:**
- `iteration-{i}/logs/interview.md`

**Context pack utilizado:** `{nome do pack}` ou `genérico`

**Briefing utilizado:** `briefing.md` (versão {timestamp})

---

## 6. Token consumption

- Tokens consumidos pelo auditor nesta execução: {N}
- Reportado ao orchestrator para inclusão no `process-map.md`

---

> [!info] Próximo gate
> O `10th-man` **sempre roda em seguida**, mesmo se o auditor reprovou. Os achados dos dois são consolidados pelo orchestrator no change request.
