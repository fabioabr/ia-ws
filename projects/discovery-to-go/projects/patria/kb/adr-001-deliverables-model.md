---
title: "ADR-001 — Modelo de entregáveis do Discovery-to-Go (OP / EX / DR)"
description: "Decisão arquitetural sobre como produzir e entregar os 3 artefatos hierárquicos do Discovery"
category: adr
type: architecture-decision
status: accepted
company: "Patria"
decided-by: "fabio.rodrigues.consult@patria.com"
decided-date: "2026-04-17"
supersedes: —
related-todo: "E:/Workspace/projects/discovery-to-go/TODO.md — task #2"
related-docs:
  - "projects/patria/kb/diagnosis-discovery-rule.md"
  - "projects/patria/kb/question-priority.md"
  - "docs/guides/discovery-pipeline.md"
  - "base/behavior/rules/discovery/discovery.md"
---

# ADR-001 — Modelo de entregáveis do Discovery-to-Go (OP / EX / DR)

## Status

**Accepted** — 2026-04-17.

## Contexto

O Discovery da Patria (Abr/2026) revelou que o pipeline atual do Discovery-to-Go produz **um único entregável** (`delivery-report.md + .html`), enquanto organizações com governança corporativa precisam de **3 artefatos hierárquicos** para diferentes públicos:

- **One-Pager (OP)** — 1 página, foco em escopo/custo/esforço + top riscos. Para patrocinador, C-Level.
- **Executive Report (EX)** — 5-15 páginas, foco em confiança/viabilidade. Para comitê de investimento, diretoria.
- **Delivery Report (DR)** — relatório completo, foco em execução. Para times de execução.

Com relação **OP ⊂ EX ⊂ DR** — cada nível é superconjunto semântico do anterior.

O diagnóstico da task #1 (ver `diagnosis-discovery-rule.md`) identificou este ponto como uma das 4 omissões principais da rule formal (`rules/discovery/discovery.md`): ela não prevê hierarquia, apenas um output monolítico.

## Decisão

Adotar o modelo **a.3 + b.3 + c.3 + c.1** (ver task #2 do TODO):

### 1. Estrutura de dados (DIM-A) — "source canônico + destilações"

O `delivery-report.md` permanece como **fonte única da verdade**. O One-Pager e o Executive Report são **destilações** do DR, geradas por skill dedicada (não são cópias filtradas nem arquivos independentes mantidos em paralelo).

**Saídas:**

| Artefato | Arquivo | Origem |
|----------|---------|--------|
| Delivery Report | `delivery/delivery-report.md` + `.html` | Produto da Fase 3 (atual, inalterado) |
| One-Pager | `delivery/one-pager.md` + `.html` | Destilado do DR por nova skill |
| Executive Report | `delivery/executive-report.md` + `.html` | Destilado do DR por nova skill |

### 2. Momento de geração (DIM-B) — "DR sempre, OP/EX on-demand"

A Fase 3 continua produzindo o DR como hoje (`pipeline-md-writer` → `consolidator` → `report-planner` → `html-writer`). Após a conclusão da Fase 3 e do Human Review final, o usuário pode invocar explicitamente a geração do OP e do EX.

**Não** há stage-gate automatizado entre OP → EX → DR. A aprovação em sequência (patrocinador → comitê → time) é **processo humano fora do pipeline**, não estado do pipeline.

### 3. Filtragem (DIM-C) — "destilação LLM + layout como piso determinístico"

A skill nova (ver seção Consequências) destila o DR usando:

- **Prompt com regras de densidade/linguagem** — determina o tom (executivo vs. operacional) e o limite de extensão.
- **Layout mínimo obrigatório** (`dtg-artifacts/templates/customization/one-pager-layout.md` e `executive-layout.md`) — define quais regions DEVEM estar presentes, garantindo estrutura mesmo que a destilação varie.

Ordem de precedência: **layout** (piso determinístico) **< destilação** (conteúdo adaptado). O layout diz *"o OP precisa ter as regions X, Y, Z"*. A destilação decide *o que escrever em cada uma*.

## Justificativa

### Por que não (a.1) views filtradas?

Filtragem por `html-layout.md` é grosseira — escolhe regions inteiras, não destila trechos. O OP não é "o DR com menos regions"; é um documento com linguagem e densidade diferentes. Mesmo texto-fonte, renderizado de forma diferente, não produz comunicação executiva adequada.

### Por que não (a.2) arquivos distintos?

Triplicaria o esforço do consolidator, criaria risco de divergência entre documentos (um dado atualizado no DR pode não chegar ao OP) e não aproveita o fato de que OP ⊂ EX ⊂ DR semanticamente. Três arquivos independentes ignoram a hierarquia.

### Por que não (b.2) stage-gate?

Stage-gate automatizado (OP → HR → EX → HR → DR → HR) força um fluxo que nem toda organização segue. Na Patria o fluxo existe, mas é humano — vive nos comitês, não no pipeline. Automatizá-lo engessa. Manter o pipeline produzindo DR e deixar OP/EX como destilação permite qualquer fluxo de aprovação por cima.

### Por que não (c.2) bitmap nos schemas?

Exigiria editar os ~85 schemas de region para marcar sub-campos como `[OP]/[EX]/[DR]`. Esforço enorme, e ainda não resolve o problema de linguagem (um sub-campo marcado `[OP]` continua escrito em tom técnico). A destilação por LLM faz o trabalho certo no lugar certo.

## Consequências

### Positivas

- **Pipeline atual não quebra.** Fase 3 continua exatamente como está.
- **1 fonte da verdade.** DR é canônico; OP/EX são derivações. Impossível divergirem por desatualização.
- **Linguagem adequada por público.** Destilação via LLM ajusta tom, densidade e ênfase.
- **Regeneração barata.** OP pode ser regerado sem reprocessar toda a Fase 3.
- **Compatível com a Patria hoje.** Patria precisa de OP imediato; EX e DR vêm depois. Esse modelo serve.
- **Resolve a omissão B/J/L** do diagnóstico (task #1) sem reescrever a rule inteira.

### Negativas / riscos

- **Nova skill `deliverable-distiller` precisa ser escrita** (ver Impacto). Risco de hallucination: destilação pode inferir dados não presentes no DR. **Mitigação:** prompt obriga citar region-fonte para cada afirmação; validação por auditor.
- **Necessidade de 2 novos layouts** (`one-pager-layout.md`, `executive-layout.md`). Esforço S.
- **Não atende organizações que querem stage-gate automatizado.** Para estas, seria possível criar variante no futuro (b.2 ainda é implementável por cima, como ADR futuro).
- **O flag `deliverables_scope` do briefing** (task #3) precisa ser reinterpretado: não controla mais "quais fases rodam", e sim "quais destilações gerar automaticamente ao final da Fase 3".

### Impacto nas tasks do TODO

- **Task #3 (flags)** — ajustar interpretação do flag `deliverables_scope`. Default passa a ser `["DR"]`; quem quiser OP/EX automaticamente adiciona.
- **Task #5 (diagrama macro)** — adicionar caixa pós-Fase 3: "Destilação OP/EX (opcional)".
- **Task #6 (region `overview-one-pager`)** — esta region continua viva como **componente de layout** do OP, não como entregável inteiro.
- **Task #7 (separar `okrs-and-roi`)** — mantida, mas a classificação OP/EX/DR agora é **sugestão para o destilador**, não filtro duro.
- **Task #8 (regions financeiras fundo-global)** — mantida sem mudança.
- **Task #11 (bitmap no framework)** — reinterpretada: o bitmap `[OP][EX][DR]` no `question-priority.md` passa a ser **input para o prompt do destilador**, não para um filtro mecânico.
- **Nova task #16** — criar skill `deliverable-distiller`. Ver abaixo.
- **Nova task #17** — criar layouts `one-pager-layout.md` e `executive-layout.md`. Ver abaixo.

## Novas tasks geradas

### #16 — Criar skill `deliverable-distiller`  🔴  [esforço: L]

Skill nova que recebe `delivery-report.md` + um layout alvo + tipo (OP ou EX) e produz o entregável destilado em `.md`, com regras:

- Cita region-fonte do DR para cada afirmação (rastreabilidade)
- Respeita o layout (ordem, regions obrigatórias)
- Ajusta linguagem ao público (executivo para OP/EX, técnico para DR)
- Extensão máxima configurável (ex: 1 página para OP; 10 páginas para EX)
- Não inventa dados não presentes no DR (alucinação = falha)

### #17 — Criar layouts `one-pager-layout.md` e `executive-layout.md`  🟠  [esforço: S]

Em `dtg-artifacts/templates/customization/`. Cada um lista:

- Regions obrigatórias (ex: OP requer `executive/overview-one-pager`, `executive/premises`, `risk/risk-matrix` top-3, `financial/cost-per-component` estimativa)
- Regions opcionais
- Extensão alvo
- Tom/linguagem

## Alternativas consideradas e descartadas

| Alternativa | Motivo do descarte |
|-------------|-------------------|
| (a.1) Views filtradas apenas | Filtragem por region é grosseira; não destila linguagem |
| (a.2) 3 arquivos independentes | Risco de divergência; triplica esforço; ignora hierarquia semântica |
| (b.1) Todos em paralelo na Fase 3 | Força geração de OP/EX mesmo quando só se quer DR; inflige custo a projetos que não precisam |
| (b.2) Stage-gate automatizado | Engessa fluxo que é humano por natureza; aumenta número de HR a 6 (2x atual) |
| (c.1) Apenas html-layout.md | Não resolve o problema de linguagem; filtragem mecânica |
| (c.2) Bitmap nos 85 schemas | Esforço desproporcional; ainda não resolve linguagem |
| (d) Híbrido a.2 + b.2 | Combinação de piores pontos — triplica arquivos E engessa pipeline |

## Observações adicionais

- **Sobre o bitmap `[OP][EX][DR]`** do `question-priority.md`: continua útil como **sugestão semântica para o destilador** (prompt). Não é obrigatório para implementar este ADR, mas deve alimentar a task #16.
- **Sobre a rule `discovery.md`**: precisa ser atualizada para mencionar OP/EX como produtos opcionais pós-Fase 3. Ajuste pequeno, pode entrar na task #14 ou como parte da #16.
- **Compatibilidade retroativa**: runs antigos continuam válidos — eles produziram DR, que permanece sendo o artefato canônico. Regerar OP/EX de runs antigos é possível basta rodar o destilador.

## Histórico

| Data | Mudança |
|------|---------|
| 2026-04-17 | Criado. Decisão a.3+b.3+c.3+c.1 aceita. |
