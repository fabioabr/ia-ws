---
title: "Diagnóstico — rules/discovery/discovery.md"
description: "Análise do que a rule formal do Discovery prescreve hoje e onde conflita com as correções capturadas no Discovery da Patria (Abr/2026)"
category: diagnosis
type: rule-analysis
status: concluido
company: "Patria"
analyzed-by: "fabio.rodrigues.consult@patria.com (via Claude)"
analyzed-date: "2026-04-17"
source-file: "base/behavior/rules/discovery/discovery.md (v04.00.000, 287 linhas)"
related-todo: "E:/Workspace/projects/discovery-to-go/TODO.md — task #1"
---

# Diagnóstico — rules/discovery/discovery.md

Produto da task #1 do [TODO.md](../../../TODO.md). Documenta o que a rule formal do processo de Discovery prescreve hoje, onde isso conflita com as correções estruturais capturadas no Discovery da Patria (Abr/2026) e quais tasks derivadas devem ser priorizadas.

---

## Sumário executivo

A rule `discovery.md` (v04.00.000, 287L) é **coerente internamente** mas **filosoficamente incompatível** com três aspectos que a Patria revelou:

1. **"Orçamento como output, não input"** (linha 220-229) é o **conflito raiz**. A rule diz que o Discovery CALCULA o custo total. Na Patria, o custo já foi aprovado globalmente antes do Discovery começar — o processo está invertido do ponto de vista da rule.
2. **Fase 3 produz 1 entregável monolítico** (`delivery-report.md` + `.html`). Não prevê a hierarquia OP ⊂ EX ⊂ DR que estabelecemos.
3. **Blocos #3, #4 e #8 tratam ROI, FTE e TCO como sempre-obrigatórios.** Não há condicionalidade baseada em tipo de projeto ou modelo de governança.

**Top 3 recomendações prioritárias:**

1. **Reescrever seção "Orçamento e Output, não Input"** para contemplar dois modos: `projeto-paga` (atual) e `fundo-global` (novo). Decisão de escopo vem da task #3 (flags no briefing).
2. **Desacoplar a Fase 3** — o `delivery-report.md` continua sendo o consolidado completo, mas precisa gerar os 3 entregáveis (OP/EX/DR) como outputs distintos ou views filtradas. Depende da task #2.
3. **Tornar o bloco #3 condicional** ao flag `require_roi_justification`. O bloco continua existindo para OKRs, mas ROI só é levantado quando pedido explicitamente.

---

## Tabela de obrigatoriedades prescritas

Classificação:
- 🔴 **Conflito duro** — contradiz o que o usuário estabeleceu
- 🟡 **Conflito por omissão** — a rule não prevê o caso novo
- 🟢 **Alinhado** — já compatível, não precisa mexer

| # | Item prescrito | Onde (linha) | Obrigatoriedade hoje | Conflito | Novo comportamento esperado |
|---|---------------|--------------|---------------------|----------|------------------------------|
| A | "Nenhum projeto inicia sem completar as 3 fases com aprovação humana" | L24 | Sempre obrigatório | 🟢 Alinhado | Mantido |
| B | 3 fases sequenciais (Discovery → Challenge → Delivery) | L32-47 | Sempre obrigatório | 🟡 Omissão | Manter as 3 fases, mas Fase 3 precisa produzir 3 entregáveis (OP/EX/DR) |
| C | Bloco #3 "Valor Esperado / OKRs" inclui **ROI** | L71 | Obrigatório sempre | 🔴 Duro | Condicional a `require_roi_justification` (default: false) |
| D | Bloco #4 "Processo, Negócio e Equipe" captura **equipe real** | L72 | Obrigatório sempre | 🟡 Omissão | Capturar, mas marcar que FTE real não vaza para o OP (OP assume "todos contratados") |
| E | Bloco #8 "TCO e Build vs Buy" calcula **custo total** | L76 | Obrigatório sempre | 🔴 Duro | Dois modos: (a) `projeto-paga` → TCO convencional; (b) `fundo-global` → estimativa de consumo sem free tier |
| F | "Discovery NÃO parte de orçamento pré-definido" | L222-223 | Regra dura | 🔴 Duro | Inverter para organizações com governança pré-aprovada (Patria). Orçamento pode ser input quando aprovado globalmente |
| G | "O processo CALCULA o custo total como resultado" | L223 | Regra dura | 🔴 Duro | Manter o cálculo, mas nem sempre ele é usado para decidir "vai/não vai" — às vezes é só referência (fundo global) |
| H | "NÃO perguntar 'qual o orçamento?' nos blocos #1-#4" | L225 | Regra dura | 🔴 Duro | Manter proibição de cobrar orçamento ao cliente; mas ler do briefing se já foi aprovado globalmente |
| I | "Prazo fixo: 1 mês planejamento + 6 meses MVP" | L229 | Regra dura | 🔴 Duro | Transformar em default configurável; não é universal |
| J | Fase 3 produz `delivery-report.md + .html` | L130, L47, L258 | Output único | 🟡 Omissão | Produzir também `one-pager.html` e `executive-report.html` (ou views equivalentes) |
| K | Auditor valida 5 dimensões com pisos mínimos | L105 | Sempre | 🟡 Omissão | Dimensões devem ser condicionais às flags (ver task #9) |
| L | Critério de conclusão: 8 files Fase 1 + 2 Fase 2 + 2 Fase 3 | L256-260 | Sempre | 🟡 Omissão | Critério deve acomodar produção dos 3 entregáveis |
| M | Context-templates listados (apenas 4) | L237-242 | Incompleto | 🟢 Alinhado (defasagem menor) | Atualizar para os 10 do guide (task separada menor) |
| N | Human Review após cada fase (4 opções de decisão) | L141-157 | Sempre | 🟢 Alinhado | Mantido |
| O | Iterações com herança de results não-afetados | L160-186 | Sempre | 🟢 Alinhado | Mantido |
| P | Bloco #6 LGPD/Privacidade | L74 | Obrigatório sempre | 🟢 Alinhado | Mantido |

---

## Conflitos duros — exemplos de trechos

### 🔴 Conflito F/G/H — "Orçamento como Output, não Input"

**Trecho literal (L220-229):**

```markdown
## 💰 Orcamento e Output, nao Input

> [!danger] Regra sobre orcamento
> O discovery **NAO parte de orcamento pre-definido**. O processo **CALCULA** o custo total como resultado.
>
> - Fase 1 (blocos #1 a #4): NAO perguntar "qual o orcamento?" — focar em escopo e necessidades
> - Fase 1 (blocos #5 a #7): Definir o que e NECESSARIO, nao o que cabe no orcamento
> - Fase 1 (bloco #8): Arquiteto CALCULA o TCO baseado nas decisoes anteriores
>
> **Prazo fixo:** 1 mes de planejamento + 6 meses de desenvolvimento MVP.
```

**Por que conflita:** na Patria (e em qualquer organização com governança pré-aprovada), o orçamento **É input** — foi aprovado globalmente antes do Discovery começar. O Discovery pode calcular TCO como **referência** (ex.: "o projeto consumirá ~USD X/mês em cloud") sem que isso seja a base da decisão de investimento. A decisão já foi tomada.

**Também notável:** o histórico da rule registra **v03.00.001 (2026-04-05)** — "Remocao de 'Orçamento' da lista de categorias obrigatórias de fronteira (contradicao com pipeline-master e skills)". Ou seja, **já houve ajuste anterior para reduzir conflitos com orçamento** — este diagnóstico continua esse esforço.

---

### 🔴 Conflito C — Bloco #3 inclui ROI como obrigatório

**Trecho literal (L71):**

```markdown
| #3 | Valor Esperado / OKRs | po | Metricas, ROI, criterios de sucesso |
```

**Por que conflita:** ROI só deve ser levantado quando o briefing pede explicitamente. Em organizações onde o Discovery ocorre após aprovação global do investimento, exigir ROI é redundante — o retorno já foi aceito como hipótese na fase de aprovação anterior.

**Correção sugerida:** reclassificar para "Metricas, criterios de sucesso (OKRs); ROI/payback apenas se `require_roi_justification=true`".

---

### 🔴 Conflito E — Bloco #8 assume projeto paga

**Trecho literal (L76):**

```markdown
| #8 | TCO e Build vs Buy | solution-architect | Custo total, alternativas, viabilidade |
```

**Por que conflita:** "Custo total" pressupõe que o projeto arca com o custo e precisa justificar a viabilidade financeira. No modelo fundo global (Patria), o custo de cloud é absorvido corporativamente; o Discovery precisa apenas **estimar o consumo** (sem free tier) para dimensionamento técnico, não para viabilidade.

**Correção sugerida:** descrição do bloco passa a ser "Custo total (convencional) ou estimativa de consumo sem free tier (fundo-global), Build vs Buy, alternativas, viabilidade".

---

### 🔴 Conflito I — Prazo fixo

**Trecho literal (L229):**

```markdown
> **Prazo fixo:** 1 mes de planejamento + 6 meses de desenvolvimento MVP.
```

**Por que conflita:** esse prazo foi estabelecido como default absoluto na rule. Mas é uma decisão de projeto, não de framework. Em organizações com SLAs diferentes (trimestre fiscal, ciclo de budget semestral etc.), o prazo é outro.

**Correção sugerida:** mover para `setup/customization/rules/iteration-policy.md` como `planning_duration` e `mvp_duration` configuráveis. A rule cita apenas "prazo default configurável".

---

## Conflitos por omissão — o que a rule não prevê

### 🟡 Omissão B/J/L — Hierarquia OP/EX/DR

A rule só conhece `delivery-report.md` + `.html` como output final. Não há menção a:
- One-Pager como artefato distinto
- Executive Report como artefato distinto
- Qualquer gate progressivo de aprovação (patrocinador → comitê)

A tabela da Fase 3 (L124-131) tem 3 sub-fases (pipeline-md-writer, consolidator, html-writer) — nenhuma delas produz diferenciação de entregáveis.

### 🟡 Omissão D — FTE capturado mas não classificado

Bloco #4 captura "Organizacao, stakeholders, equipe" (L72). Ok. Mas não diz **em qual entregável** cada dado deve aparecer. Sem isso:
- Equipe real vaza para o OP (incorreto)
- OP não pode assumir "todos contratados" (porque a informação conflitante está disponível)

### 🟡 Omissão K — Auditor sem condicionalidade

L105 diz apenas "Valida qualidade dos drafts contra 5 dimensoes com pisos minimos". As 5 dimensões não estão descritas aqui (estão em `skills/auditor/SKILL.md` ou em `scoring-thresholds.md`). Mas qualquer que sejam, precisam respeitar as flags da task #3.

---

## Referências cruzadas (arquivos tocados pela rule)

| Arquivo referenciado | Linha | Implicação |
|---------------------|-------|------------|
| `docs/guides/discovery-pipeline.md` | L269 | Duplicação didática — precisa ser sincronizado quando a rule mudar |
| `rules/iteration-loop/iteration-loop.md` | L270 | Provavelmente tem regras sobre gates e critérios de convergência — candidato a task separada |
| `rules/analyst-discovery-log/analyst-discovery-log.md` | L271, L93 | Formato da entrevista — provavelmente tem markers [BRIEFING]/[RAG]/[INFERENCE] |
| `rules/audit-log/audit-log.md` | L272 | Log do auditor |
| `rules/requirement-priority/requirement-priority.md` | L273 | Classificação de requisitos — pode já ter conceito compatível com OP/EX/DR |
| `rules/token-tracking/token-tracking.md` | L274 | Não deve conflitar |
| `templates/customization/human-review-template.md` | L156 | Template do HR Loop — pode precisar ajustar para 3 entregáveis |
| `setup/customization/rules/iteration-policy.md` | L186 | **Candidato direto** para receber `planning_duration`, `mvp_duration` |
| `setup/customization/rules/scoring-thresholds.md` | L207 | **Candidato direto** para as flags do auditor (task #9) |

---

## Impacto nas tasks derivadas

| Task TODO | Achado que a alimenta |
|-----------|----------------------|
| **#2** (3 entregáveis) | Conflitos B, J, L — a Fase 3 precisa ser redesenhada; o critério de conclusão precisa acomodar os 3 artefatos |
| **#3** (flags no briefing) | Conflitos F, G, H — precisam de `financial_model`. Conflito C precisa de `require_roi_justification`. Conflito I precisa de `planning_duration`/`mvp_duration` |
| **#4** (blocos #3/#4/#8 condicionais) | Conflitos C, D, E — diretamente endereçados |
| **#5** (pré-aprovação no diagrama) | Conflitos F, G, H — a seção "Orçamento como Output" precisa reconhecer que em alguns modelos ele é input |
| **#9** (auditor + scoring) | Omissão K — dimensões do auditor condicionais às flags |

### Subtasks novas identificadas

- **#13 (novo)** — atualizar context-templates listados na rule (L237-242) — só 4 de 10 estão lá. Esforço: S. Severidade: 🟢.
- **#14 (novo)** — mover `Prazo fixo` (L229) para `iteration-policy.md` como `planning_duration`/`mvp_duration` configuráveis. Esforço: S. Severidade: 🟠. Parte natural da task #3.
- **#15 (novo)** — sincronizar `docs/guides/discovery-pipeline.md` com a rule após cada edição (são duas fontes que precisam casar). Esforço: S por edição. Não é task única; é política.

---

## Conclusão

A rule é **bem estruturada**, mas sua premissa central ("orçamento como output") **é incompatível com qualquer organização onde o investimento já foi aprovado antes do Discovery começar** — cenário comum em empresas com governança corporativa (Patria, bancos, asset managers, grandes multinacionais).

O conflito não é "errado" — é **contextual**. A rule foi escrita assumindo o contexto de projeto-paga (startup ou squad que precisa justificar cada real). Patria revelou o contexto oposto: investimento já aprovado, Discovery dimensiona escopo e esforço dentro de um teto dado.

**A correção mais limpa é a da task #3** — introduzir a flag `financial_model` no briefing/config. A rule passa a dizer:

> O Discovery pode operar em dois modos:
> - **projeto-paga** (default): orçamento é output calculado. Não perguntar ao cliente o orçamento — o processo calcula.
> - **fundo-global**: orçamento é input aprovado previamente. O processo calcula TCO/consumo apenas como referência técnica, não como viabilidade.

Com essa mudança, **todos os conflitos duros ficam resolvidos sem violar a integridade filosófica da rule original**.
