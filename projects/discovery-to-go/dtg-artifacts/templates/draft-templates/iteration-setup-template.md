---
title: Iteration Setup Template
description: Template do setup.md criado pelo orchestrator no início de cada iteração. Define o plano da iteração, objetivos, contexto carregado (context-template + spec-pack) e foco. Referencia o Setup pré-iteração que rodou uma única vez no início do projeto.
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - iteration
  - setup
  - orchestrator
  - pipeline-v05
created: 2026-04-07
---

# Iteration Setup Template

> [!info] Quando é gerado
> Este template é preenchido pelo `orchestrator` **antes de qualquer agente atuar** em uma iteração. É o "mapinha" da iteração — quem precisa fazer o quê, com qual contexto, com qual objetivo. Sem `setup.md` não há iteração.
>
> Salvo em `{project}/iteration-{i}/setup.md`.

---

## Frontmatter

```markdown
---
title: Setup — Iteration {i}
project-name: {slug}
iteration: {i}
generated-at: YYYY-MM-DD HH:mm
generated-by: orchestrator
context-template: {nome ou "generic"}
spec-pack: {nome ou "generic"}
mode: {first | partial-rework | resume}
previous-iteration: {i-1 ou "none"}
authorized-by: {humano ou "automatic-first"}
---
```

---

## 1. Identificação

**Iteração:** {i}
**Tipo:**
- `first` — primeira iteração do projeto, sem histórico
- `partial-rework` — iteração de retrabalho após reprova; herda drafts intactos da anterior
- `resume` — retomada após pausa longa (>7 dias)

**Autorizada por:** {nome do humano que comandou o restart, ou "automatic" se for a iteração 1}

**Iniciada em:** {timestamp}

---

## 2. Objetivo desta iteração

### 2.1 Objetivo geral

{1-2 parágrafos descrevendo o propósito da iteração}

### 2.2 Critérios de sucesso

Esta iteração será considerada bem-sucedida se:

- [ ] {critério 1 — ex: "todos os itens críticos do change request endereçados"}
- [ ] {critério 2 — ex: "auditor passa com nota ≥ 90% e pisos OK"}
- [ ] {critério 3 — ex: "10th-man passa com nota ≥ 90%"}
- [ ] {critério 4 — ex: "humano aprova no Human Review das 3 fases macro"}

### 2.3 O que NÃO é objetivo desta iteração

(Para evitar scope creep)

- {ex: "Não vamos rediscutir personas — já fechadas na iteração 1"}
- {ex: "Não vamos abrir novos tópicos não relacionados ao change request"}

---

## 3. Contexto carregado

### 3.1 Briefing

- **Arquivo:** `briefing.md`
- **Versão lida:** {timestamp}
- **Atualizações desde a iteração anterior:** {sim/não}
- **Resumo do briefing:** {3-5 bullets do conteúdo principal}

### 3.2 Context-template + Spec pack

> [!info] Carregados no Setup pré-iteração
> Os packs foram carregados **uma única vez** no Setup, antes da iteração 1. Esta seção referencia os packs em uso — o carregamento não é repetido a cada iteração na v0.5.

- **Context-template:** `{nome do pack}.md` (ou "modo genérico")
  - Carregado de: `{project}/kb/context/{pack}.md` (cópia local)
  - Auto-detectado no Setup: {sim/não — se sim, qual sinal do briefing disparou}
- **Spec pack:** `{nome do pack}.md` (ou "modo genérico")
  - Carregado de: `{project}/kb/context/{spec-pack}.md` (cópia local)
  - Catálogo de custom-specialists disponíveis para invocação sob demanda durante a reunião

### 3.3 Change request (apenas se mode = partial-rework)

- **Arquivo:** `iteration-{i-1}/memory/after-phase-{N}.md`
- **Itens críticos:** {N}
- **Itens importantes:** {M}
- **Análise de impacto cross-eixo:** {presente/ausente}

### 3.4 Drafts herdados (apenas se mode = partial-rework)

- `iteration-{i}/draft/product-vision.md` ← copiado de `iteration-{i-1}` (intacto)
- `iteration-{i}/draft/organization.md` ← copiado de `iteration-{i-1}` (intacto)
- `iteration-{i}/draft/tech-and-security.md` ← copiado de `iteration-{i-1}` (intacto)
- `iteration-{i}/draft/strategic-analysis.md` ← copiado de `iteration-{i-1}` (intacto)
- `iteration-{i}/draft/privacy.md` ← copiado de `iteration-{i-1}` (intacto, se existe)

### 3.5 Memory acumulada

Arquivos relevantes de iterações anteriores que serão consultados:

- `iteration-1/memory/after-phase-1.md` — Discovery + decisão do HR
- `iteration-1/memory/after-phase-2.md` — Challenge + decisão do HR
- `iteration-1/memory/after-phase-3.md` — Delivery + decisão do cliente no HR (se chegou)
- ...

### 3.6 Enterprise RAG

- **Disponível:** {sim/não}
- **Base apontada:** {caminho ou "n/a"}

---

## 4. Plano de execução

### 4.1 Fases macro a executar

```
Fase 1 (Discovery)           → estimativa: ~{X} mil tokens
  ├── Reunião conjunta temática (8 blocos)
  ├── Apartes cross-eixo permitidos
  └── Ao fim: 5 drafts gerados pelos especialistas
       │
       ▼
Human Review (gate compartilhado) → ⏸️ pausa para humano
       │
       ▼
Fase 2 (Challenge)           → estimativa: ~{X} mil tokens
  ├── Auditor ‖ 10th-man (PARALELO)
  └── Relatórios consolidados pelo orchestrator
       │
       ▼
Human Review (gate compartilhado) → ⏸️ pausa para humano
       │
       ▼
Fase 3 (Delivery)            → só se aprovado nas anteriores
  ├── md-writer → consolidator → report-planner → html-writer
  └── Delivery Report = pacote de Handoff
       │
       ▼
Human Review (gate compartilhado, cliente final) → ⏸️ pausa para cliente
       │
       ▼
FIM do loop de discovery
```

### 4.2 Blocos temáticos planejados para a Fase 1

| Ordem | Bloco | Dono | Tópicos a cobrir | Prioridade |
|---|---|---|---|---|
| 1 | {ex: "Visão e propósito do produto"} | po | {tópicos do checklist + briefing} | alta |
| 2 | {ex: "Valor esperado (OKRs/ROI)"} | po | {tópicos} | alta |
| 3 | {ex: "Processo, negócio e equipe"} | po | {tópicos} | alta |
| 4 | {ex: "Tecnologia e segurança"} | solution-architect | {tópicos} | alta |
| 5 | {ex: "LGPD e privacidade"} | cyber-security-architect | {tópicos} | obrigatório (modo profundo ou magro) |
| 6 | {ex: "Arquitetura macro"} | solution-architect | {tópicos} | alta |
| 7 | {ex: "TCO e Build vs Buy"} | solution-architect | {tópicos} | alta |
| ... | | | | |

> [!info] Blocos vêm do context-template
> Os blocos temáticos são derivados do `context-template` carregado no Setup + tópicos específicos do briefing. Em iteração de partial-rework, blocos focam no change request.

### 4.3 Custom-specialists antecipados

(Lista opcional — se o orchestrator antecipa que algum domínio do **spec-pack** vai precisar de aprofundamento durante a reunião)

- {ex: "`cloud-architecture-aws` durante o bloco 5 (Tecnologia e Segurança) — briefing menciona AWS"}
- {ex: "`payments-compliance` durante o bloco 8 (TCO e Build vs Buy) — briefing menciona pagamentos internacionais"}

> Lembrete: LGPD/privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect` (agente fixo, bloco 6).

---

## 5. Fatos confirmados (carry-over de iterações anteriores)

> [!danger] Imutáveis
> Os itens abaixo foram confirmados pelo humano em iterações anteriores. O `customer` **não pode** marcá-los como `[INFERENCE]` — são `[BRIEFING]` obrigatório.

| # | Fato | Confirmado em | Origem |
|---|---|---|---|
| 1 | {ex: "Stack permitida: .NET 8 + Azure"} | iteração 1, HR da Fase 1 (Discovery) | humano |
| 2 | {ex: "Público-alvo: analistas júnior, não sênior"} | iteração 1, HR da Fase 2 (Challenge) | humano |

---

## 6. Conflitos pendentes (`[CONFLICT]`)

(Lista opcional — conflitos cross-eixo marcados em iterações anteriores que ainda não foram resolvidos pelo humano)

| # | Conflito | Eixos | Status |
|---|---|---|---|
| 1 | {descrição} | {eixo A × eixo B} | {pendente / resolvido por humano em fase X} |

---

## 7. Configurações desta iteração

| Configuração | Valor |
|---|---|
| Threshold de aprovação dos gates | ≥ 90% |
| Pisos por dimensão (auditor) | C 80 / F 70 / Co 70 / P 60 / N 70 |
| Pisos por dimensão (10th-man) | CD 70 / FAS 70 / AEC 50 |
| Modo de participação do cliente | observador passivo |
| Cap de iterações | sem cap (alerta de estagnação ativo) |
| Estagnação threshold | crescimento < 10% |

---

## 8. Estimativa de custo

| Fase macro | Tokens estimados |
|---|---|
| 1 (Discovery) | {N} |
| 2 (Challenge, paralelo) | {N} |
| 3 (Delivery) | {N — só se chegar} |
| Human Review (x3, compartilhado) | 0 |
| **Total estimado** | **{N}** |

> Estimativa baseada em iterações anteriores deste projeto + média da plataforma. Real será reportado no `process-map.md` ao fim de cada fase.

---

## 9. Próxima ação

▶️ **Iniciar Fase 1 — Discovery.**

O orchestrator passa este `setup.md` aos agentes da Fase 1 (customer + po + solution-architect + cyber-security-architect) como briefing inicial da iteração. Todos os 4 especialistas estarão presentes na reunião; o cyber-security-architect decide internamente o modo (profundo ou magro) com base no briefing + contexto.
