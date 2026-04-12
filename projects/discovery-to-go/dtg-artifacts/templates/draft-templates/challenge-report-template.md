---
title: Challenge Report Template
description: Template do relatório do 10th-man (gate divergente da Fase 2 — Challenge) do Discovery Pipeline v0.5. Estrutura em 2 subfases internas (divergência pura → avaliação) com 3 dimensões ponderadas + pisos. 10th-man roda em paralelo com o auditor.
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - challenge
  - 10th-man
  - pipeline-v05
created: 2026-04-07
---

# Challenge Report Template

> [!info] Como usar
> Este template é preenchido pelo agente `10th-man` ao fim de cada execução da Fase 2 — Challenge (gate divergente). Salvo em `{project}/iteration-{i}/draft/challenge-report.md`.
>
> O 10th-man roda **em paralelo** com o auditor — ambos são disparados ao mesmo tempo pelo orchestrator, sem dependência entre si. Os achados dos dois são consolidados pelo orchestrator e entregues juntos no Human Review da Fase 2.

---

## Frontmatter

```markdown
---
title: Challenge Report — Iteration {i}
project-name: {slug}
iteration: {i}
phase: 3
gate: 2-tenth-man
challenger-version: 00.01.000
generated-at: YYYY-MM-DD HH:mm
verdict: {APPROVED | REJECTED}
final-score: {0-100}
floor-violations: {lista ou "none"}
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

**Resumo executivo:** {1-3 parágrafos. O que o décimo homem encontrou de mais sério, mesmo que tenha aprovado.}

**Filosofia do 10th-man:**
> Eu parto do princípio de que o documento está **errado ou incompleto**. Minha pergunta não é "está bom?" — é "**o que não foi considerado e deveria ter sido**?". Se eu não conseguir derrubar nada, então o documento está bom.

---

## 2. Subfase interna A — Divergência pura

> [!info] Subfases internas do 10th-man
> O 10th-man opera em **duas subfases internas**: (A) Divergência pura — gera todas as questões hostis sem pontuar; (B) Avaliação — cruza as questões com os drafts e calcula nota. Não confundir com as fases macro do pipeline (Discovery, Challenge, Delivery). Este relatório pertence à **Fase 2 macro (Challenge)** do pipeline.

> [!warning] Esta seção é registrada SEMPRE
> Mesmo que o veredicto final seja APPROVED, todas as questões geradas na Subfase A ficam registradas. Isso garante audit trail e ajuda iterações futuras.

### 2.1 Questões cruzando blocos / cross-eixo

Questões que tocam mais de um eixo (product × bounds × project):

| # | Questão | Eixos afetados |
|---|---|---|
| 1 | {ex: "O produto promete latência < 100ms mas o bounds permite Heroku — incompatível?"} | product × bounds |
| 2 | {questão} | {eixos} |

### 2.2 Antipatterns conhecidos do domínio

Cruzando os drafts com antipatterns do context-template ativo:

| # | Antipattern | Onde aparece nos drafts | Impacto |
|---|---|---|---|
| 1 | {antipattern do pack} | {ref no draft} | {alto/médio/baixo} |

### 2.3 Edge cases não cobertos

Cenários de falha/borda que o documento ignora:

| # | Cenário | Por que importa | Coberto? |
|---|---|---|---|
| 1 | {ex: "Origem de dados fica fora do ar por 24h"} | {motivo} | {Sim/Não/Parcialmente} |

### 2.4 Premissas não validadas

Coisas que o customer assumiu mas que não foram confirmadas:

| # | Premissa | Quem assumiu | Validação |
|---|---|---|---|
| 1 | {premissa} | {customer/po/solution-architect/cyber-security-architect} | {confirmada / [INFERENCE] solto / contraditada} |

### 2.5 Riscos estratégicos

Decisões que podem matar o projeto se estiverem erradas:

- {risco 1 — descrição + razão}
- {risco 2}

### 2.6 Questões livres adicionais

- {qualquer outra questão divergente que não cabe nas categorias acima}

---

## 3. Subfase interna B — Avaliação

Cruza as questões da Subfase A (divergência pura) com os drafts e calcula nota.

### 3.1 Cobertura divergente — peso 50% — piso 70%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,50 = XX,XX}

**Cálculo:**
```
Total de questões geradas na Subfase A: {Q}
Questões respondidas adequadamente pelos drafts: {R}
Score = R/Q × 100 = {XX,XX%}
```

**Questões NÃO respondidas (críticas):**

| # | Questão | Por que crítica |
|---|---|---|
| 1 | {questão da Subfase A} | {motivo} |

---

### 3.2 Fundamentação em áreas sensíveis — peso 30% — piso 70%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,30 = XX,XX}

**Cálculo:**
```
Áreas sensíveis avaliadas: requisitos mandatórios + fronteiras críticas
Concentração de [INFERENCE] em áreas sensíveis: {percentual}
Score = 100% − (penalidade) = {XX,XX%}
```

**Concentrações detectadas:**

| Área sensível | % de respostas [INFERENCE] | Justificativa |
|---|---|---|
| {ex: "Requisitos de segurança"} | 60% | {3 de 5 respostas inferidas pelo customer} |

---

### 3.3 Antipatterns e edge cases — peso 20% — piso 50%

**Score bruto:** {XX,XX%}
**Status do piso:** {✅ atende | ❌ viola}
**Contribuição na média:** {XX,XX × 0,20 = XX,XX}

**Cálculo:**
```
Antipatterns + edge cases conhecidos do domínio (via context-template): {N}
Cobertos pelos drafts: {C}
Score = C/N × 100 = {XX,XX%}
```

**Cenários conhecidos NÃO abordados:**
- {antipattern/edge case 1}
- {antipattern/edge case 2}

---

## 4. Resumo da fórmula

| # | Dimensão | Score | Peso | Piso | Piso OK? | Contribuição |
|---|---|---|---|---|---|---|
| 1 | Cobertura divergente | {XX,XX%} | 50% | 70% | {✅/❌} | {XX,XX} |
| 2 | Fundamentação áreas sensíveis | {XX,XX%} | 30% | 70% | {✅/❌} | {XX,XX} |
| 3 | Antipatterns e edge cases | {XX,XX%} | 20% | 50% | {✅/❌} | {XX,XX} |
| | **Total** | | **100%** | | **{Todos OK?}** | **{XX,XX}** |

---

## 5. Questões residuais (mesmo se aprovado)

Mesmo quando o veredicto é APPROVED, o 10th-man pode ter questões que valeriam aprofundamento. Elas vão para o Human Review da Fase 2 (Challenge) como notas para o humano considerar.

| # | Questão residual | Severidade | Recomendação |
|---|---|---|---|
| 1 | {questão} | {baixa/média} | {humano valida ou ignora} |

---

## 6. Pontos para o change request

> [!warning] Apenas se REJECTED
> Esta seção só é preenchida quando o veredicto é REJECTED. O orchestrator consolida estes pontos com os do auditor.

### 6.1 Críticos
- [ ] {item crítico}

### 6.2 Importantes
- [ ] {item importante}

### 6.3 Sugestões
- [ ] {sugestão}

---

## 7. Evidências

**Drafts desafiados:**
- `iteration-{i}/draft/product-vision.md`
- `iteration-{i}/draft/organization.md`
- `iteration-{i}/draft/tech-and-security.md`
- `iteration-{i}/draft/strategic-analysis.md`
- `iteration-{i}/draft/privacy.md` (sempre existe — modo profundo ou magro)

**Logs consultados:**
- `iteration-{i}/logs/interview.md`

**Audit report consultado (se disponível — roda em paralelo, pode não estar pronto quando 10th-man inicia):**
- `iteration-{i}/draft/audit-report.md`

**Context pack utilizado:** `{nome}` ou `genérico`

---

## 8. Token consumption

- Tokens consumidos pelo 10th-man nesta execução: {N}
- Inclui Subfase A (divergência pura) + Subfase B (avaliação)
- Reportado ao orchestrator
