---
title: "TO-DO — Ajustes no Pipeline Discovery-to-Go"
description: "Pendências identificadas a partir das correções estruturais capturadas no Discovery da Patria (Abr/2026)"
project-name: discovery-to-go
status: ativo
created: 2026-04-17
owner: fabio.rodrigues.consult@patria.com
---

# TO-DO — Ajustes no Pipeline Discovery-to-Go

Lista de pendências a resolver, em ordem de prioridade, derivadas das correções estruturais feitas durante o Discovery da Patria.

## Contexto — o que mudou

1. **One-Pager do Discovery-to-Go NÃO dimensiona time real** — assume "todos contratados" para simplificar esforço/custo/escopo.
2. **One-Pager NÃO justifica ROI/payback** — Discovery acontece depois da aprovação global do investimento. Exceção: se briefing exigir explicitamente.
3. **Modelo financeiro "fundo global"** existe — projetos não arcam custo cloud, só estimam consumo sem free tier. O pipeline só modela o caso "projeto paga".
4. **3 entregáveis distintos** foram formalizados: One-Pager (OP) ⊂ Executive Report (EX) ⊂ Delivery Report (DR) — mas o pipeline hoje gera só 1 delivery.
5. **Bitmap `[OP][EX][DR]`** em cada pergunta do `environment.md` — classificação criada em `projects/patria/kb/question-priority.md`.

Fonte: `projects/patria/kb/question-priority.md`, `one-pager-form.txt` respondido pelo usuário, memórias `feedback_one_pager_scope.md` e `project_patria_financial_model.md`.

---

## Legenda

| Campo | Valores |
|-------|---------|
| **Status** | `[ ]` pendente, `[~]` em andamento, `[X]` concluído, `[!]` bloqueado |
| **Severidade** | 🔴 Crítica, 🟡 Alta, 🟠 Média, 🟢 Baixa |
| **Esforço** | S (≤1h), M (1-4h), L (>4h) |

---

## #1 — Revisar regra formal `rules/discovery/discovery.md`  🔴  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** —
- **Bloqueia:** #3, #4, #5, #9
- **Resultado:** [projects/patria/kb/diagnosis-discovery-rule.md](projects/patria/kb/diagnosis-discovery-rule.md)

### 🎯 Objetivo

Diagnosticar o que a rule formal prescreve hoje como **obrigatório** e identificar onde isso conflita com o novo entendimento capturado no Discovery da Patria (One-Pager sem FTE/ROI, modelo "fundo global", 3 entregáveis OP⊂EX⊂DR).

**Importante:** essa task **não edita** a rule. Só investiga. A edição vem nas tasks derivadas, depois que a task #2 decidir o modelo de entregáveis.

### 📋 Planejamento

1. **Ler** `base/behavior/rules/discovery/discovery.md` (287L) completo.
2. **Extrair** todas as obrigatoriedades em tabela estruturada:

   | Item prescrito | Onde (linha/seção) | Obrigatoriedade hoje | Novo comportamento esperado |
   |---|---|---|---|
   | Bloco #3 inclui ROI/payback | — | Obrigatório sempre | Condicional a `require_roi_justification` |
   | Bloco #8 TCO 3 anos | — | Obrigatório sempre | Condicional a `financial_model` |
   | Bloco #4 FTE real | — | Obrigatório sempre | Capturar mas marcar como EX/DR-only |
   | ... | ... | ... | ... |

3. **Mapear referências cruzadas** — listar outros arquivos que a rule aponta (skills, regions, schemas, outras rules). Servirá de guia para tasks derivadas.
4. **Marcar conflitos** — separar o que conflita com as correções em 3 categorias:
   - **🔴 Conflito duro:** contradiz o que o usuário estabeleceu (ex: "ROI é obrigatório no OP")
   - **🟡 Conflito por omissão:** a rule não prevê o caso novo (ex: não conhece "fundo global")
   - **🟢 Alinhado:** já compatível, não precisa mexer
5. **Identificar lacunas** — coisas que o usuário estabeleceu mas que a rule nem menciona (ex: diferença entre OP/EX/DR — a rule hoje só conhece "delivery").
6. **Verificar se há rules vizinhas** potencialmente afetadas pelo mesmo conflito (por ex. `iteration-loop`, `requirement-priority`) — marcar para task futura sem entrar no mérito.

### ❓ Decisões pendentes (preciso da sua resposta)

- **D1.1 — Onde salvar o diagnóstico?**
  - Opções:
    - (a) Como seção nova dentro do próprio `TODO.md` (task #1 ganha "Resultado")
    - (b) Em arquivo separado `projects/patria/kb/diagnosis-discovery-rule.md`
    - (c) Em arquivo separado global `base/behavior/rules/discovery/diagnosis-2026-04.md`
  - Recomendação: **(b)** — é um produto do Discovery da Patria, fica no kb do cliente; depois é promovido para framework quando virar padrão.
  - Resposta: _____

- **D1.2 — Escopo da leitura: só `discovery.md` ou rules vizinhas também?**
  - Contexto: além de `discovery.md`, existem `iteration-loop.md` (249L), `requirement-priority.md`, `analyst-discovery-log.md`, `audit-log.md`, `token-tracking.md`, `layer-priority.md` na pasta `rules/`.
  - Opções:
    - (a) Apenas `discovery.md` — mantém task #1 no esforço S (≤1h), foco no núcleo
    - (b) `discovery.md` + `iteration-loop.md` — principais, cobre ciclo e gates (1-2h)
    - (c) Todas as rules de discovery — exaustivo (3-5h), muda esforço para M-L
  - Recomendação: **(a)** — faz a #1 enxuta; abre task nova se rules vizinhas aparecerem como bloqueadoras.
  - Resposta: _____

- **D1.3 — Formato do diagnóstico: tabela compacta ou narrativo?**
  - Opções:
    - (a) Só a tabela de obrigatoriedades (mínimo viável)
    - (b) Tabela + sumário executivo (recomendações top 3-5)
    - (c) Tabela + sumário + exemplos de trechos conflitantes (mais verbose, mais útil para a task #2)
  - Recomendação: **(c)** — o custo extra é baixo e alimenta bem a decisão da task #2.
  - Resposta: _____

### 📦 Entregáveis

- Arquivo de diagnóstico (local conforme D1.1), contendo:
  - Tabela de obrigatoriedades prescritas hoje
  - Classificação conflito duro / omissão / alinhado
  - Lista de referências cruzadas (outros arquivos tocados)
  - Top 3-5 recomendações (se formato D1.3 = b ou c)
- Atualização da task #1 no TODO.md para status `[X] concluído`
- Identificação automática de subtasks novas (se surgirem) — adicionadas ao final do TODO

### 📝 Notas / Registro

_(append-only durante execução)_

- 2026-04-17 — Task criada, aguardando decisões D1.1, D1.2, D1.3 para começar.
- 2026-04-17 — Respostas: D1.1=(b), D1.2=(a), D1.3=(c). Executando.
- 2026-04-17 — Task concluída. Diagnóstico salvo em `projects/patria/kb/diagnosis-discovery-rule.md`.

### 🎯 Resultado

**Achados principais:**

- **1 conflito filosófico raiz:** a rule estabelece "orçamento como output" (L220-229) — incompatível com organizações onde o investimento já foi aprovado globalmente antes do Discovery começar (caso Patria).
- **6 conflitos duros** — blocos #3 (ROI), #8 (TCO), seção "Orçamento Output" (3 trechos), Prazo fixo 1+6 meses.
- **4 conflitos por omissão** — hierarquia OP/EX/DR não prevista; FTE capturado mas sem classificação por entregável; auditor sem condicionalidade; critério de conclusão monolítico.
- **3 subtasks novas identificadas:** #13, #14, #15 (ver abaixo).

**Correção mais limpa identificada:** introduzir flag `financial_model` (`projeto-paga` | `fundo-global`) no briefing/config — **resolve todos os conflitos duros em uma única mudança**. Isso é exatamente o que a task #3 já prevê; o diagnóstico confirma que ela é de fato a chave.

**Impacto nas outras tasks:** todos os achados foram mapeados para as tasks #2, #3, #4, #5, #9 no diagnóstico. Não houve descobertas que invalidem a ordem sugerida no TODO.

---

## #2 — Decisão: 3 entregáveis (OP / EX / DR) — como modelar?  🔴  [esforço: L]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #1 ✓
- **Bloqueia:** #5, #6, #7, #8, #11
- **Resultado:** [projects/patria/kb/adr-001-deliverables-model.md](projects/patria/kb/adr-001-deliverables-model.md)

### 🎯 Objetivo

Decidir **como o pipeline produz e entrega** os 3 artefatos hierárquicos (One-Pager, Executive Report, Delivery Report). Essa decisão define a estrutura da Fase 3 e o contrato do `consolidator`, `report-planner` e `html-writer`.

**Não é nesta task que editamos código.** É a task que toma as decisões arquiteturais que habilitam as edições nas tasks #5 em diante.

### 🧱 Entendimento (baseado no diagnóstico da #1)

A rule hoje prevê 1 output (`delivery-report.md + .html`). Precisamos acomodar 3 artefatos sem quebrar a Fase 3. Há **3 dimensões de decisão** independentes — vale a pena tratá-las separadamente:

- **DIM-A: Estrutura de dados** — os 3 artefatos são 1 arquivo com views ou 3 arquivos distintos?
- **DIM-B: Momento de geração** — geramos os 3 em série única (uma execução da Fase 3) ou em sequência com aprovação entre eles?
- **DIM-C: Filtragem** — quem define o que entra em cada artefato? Schemas? `html-layout.md`? Flag no region? Bitmap OP/EX/DR?

Cada dimensão tem suas opções. As opções (a)(b)(c) originais cobriam misturas de A+B — vou desacoplar.

### 📋 Planejamento

1. **Consolidar decisão em DIM-A, DIM-B, DIM-C** com o usuário (ver Decisões Pendentes).
2. **Escrever ADR** (`projects/patria/kb/adr-001-deliverables-model.md`) registrando a escolha final e o porquê.
3. **Listar impacto concreto** nos arquivos afetados (deriva das escolhas):
   - `docs/guides/discovery-pipeline.md`
   - `base/behavior/rules/discovery/discovery.md`
   - `base/behavior/skills/consolidator/SKILL.md`
   - `base/behavior/skills/report-planner/SKILL.md`
   - `base/behavior/skills/html-writer/SKILL.md`
   - `base/behavior/skills/pipeline-md-writer/SKILL.md`
   - `base/standards/conventions/report-regions/schemas/**`
   - `dtg-artifacts/templates/customization/html-layout.md`
4. **Atualizar tasks #5, #6, #7, #8, #11** no TODO para refletir a estrutura escolhida.
5. **Marcar task #2 como concluída** apontando para o ADR.

### ❓ Decisões pendentes (preciso da sua resposta)

#### DIM-A — Estrutura de dados

- **D2.A — Os 3 artefatos são 1 arquivo com views ou 3 arquivos distintos?**
  - **(a.1) View única:** 1 `delivery-report.md` é o superset. OP e EX são **renderizações filtradas** via `html-layout.md`.
    - ✅ Pros: 1 fonte da verdade; impossível divergirem; menor esforço de manutenção; regions com bitmap `[OP][EX][DR]` servem como filtro natural.
    - ❌ Cons: conteúdo escrito "em modo DR" pode ficar denso demais para OP; difícil ter linguagem executiva vs. técnica no mesmo texto-fonte.
  - **(a.2) Arquivos distintos:** 3 arquivos md + 3 html. Cada um com consolidator próprio (ou modo do mesmo skill).
    - ✅ Pros: cada entregável tem densidade/linguagem própria; flexibilidade total.
    - ❌ Cons: 3x trabalho; risco de divergência; triplica complexidade no consolidator.
  - **(a.3) Híbrido — "source doc + renderizações":** 1 `delivery-report.md` (o DR completo) **+** 2 arquivos derivados (`one-pager.md`, `executive-report.md`) **gerados por skill dedicada de destilação** (não cópia mecânica — usa LLM para adaptar linguagem/densidade).
    - ✅ Pros: 1 fonte da verdade para dados; linguagem adequada em cada entregável; aderente ao princípio OP ⊂ EX ⊂ DR.
    - ❌ Cons: precisa de nova skill (`deliverable-distiller` ou equivalente); risco de hallucination se a destilação inferir o que não está no DR.
  - **Recomendação:** **(a.3)**. Equilibra integridade da fonte única com qualidade editorial por público.
  - **Resposta:** _____

#### DIM-B — Momento de geração

- **D2.B — Geramos os 3 em uma execução só ou em sequência com aprovação entre eles?**
  - **(b.1) Todos em paralelo na Fase 3 atual:** uma execução da Fase 3 produz OP + EX + DR. Human Review final valida os 3 juntos.
    - ✅ Pros: pipeline atual muda minimamente — só adiciona outputs; 1 ciclo de HR.
    - ❌ Cons: não reflete fluxo real (patrocinador → comitê → time); usuário pode ter que rejeitar OP tendo lido EX+DR que distraem.
  - **(b.2) Stage-gate com HR entre cada:** OP é gerado → HR → se aprovar, gera EX → HR → se aprovar, gera DR → HR final.
    - ✅ Pros: espelha fluxo real de aprovação corporativa; economiza tokens/esforço se OP for rejeitado; mantém foco por entregável.
    - ❌ Cons: 3 HR a mais; pipeline mais longo; exige reescrever Fase 3 como sequência; pode atrasar clientes que querem tudo junto.
  - **(b.3) Híbrido — DR é gerado sempre, OP e EX são destilações on-demand:** a Fase 3 sempre produz DR completo; OP e EX são gerados por solicitação explícita (comando/flag) **após** o DR.
    - ✅ Pros: não trava o pipeline; OP pode ser regerado quantas vezes quiser sem reprocessar tudo.
    - ❌ Cons: não força a produção dos 3; depende de disciplina para gerar OP/EX.
  - **Recomendação:** **(b.3)** — casa perfeitamente com **(a.3)**: DR vira artefato canônico, OP/EX são destilações. Quem quiser stage-gate de aprovação faz por processo humano (sem travar o pipeline).
  - **Resposta:** _____

#### DIM-C — Filtragem: como saber o que entra em cada artefato?

- **D2.C — Como o sistema decide o conteúdo de cada artefato?**
  - **(c.1) `html-layout.md` escolhe regions** — solução atual, apenas estendida com 3 layouts (`one-pager-layout.md`, `executive-layout.md`, `delivery-layout.md`).
    - ✅ Pros: reutiliza infra atual; já existe o conceito.
    - ❌ Cons: filtragem por region é grosseira; não consegue destilar **trechos** dentro de uma region.
  - **(c.2) Bitmap `[OP][EX][DR]` dentro de cada region** — cada schema de region marca quais sub-campos vão para cada entregável.
    - ✅ Pros: granularidade fina; aderente ao `question-priority.md` que criamos para a Patria.
    - ❌ Cons: exige editar todos os 85 schemas de region; mais complexidade no consolidator.
  - **(c.3) Destilação por skill** — a skill `deliverable-distiller` (da DIM-A.3) **resume e adapta** o DR completo para OP/EX usando regras do prompt.
    - ✅ Pros: máxima flexibilidade; linguagem ajustada; não precisa editar schemas.
    - ❌ Cons: depende de qualidade do prompt; precisa de eval/validação.
  - **Recomendação:** **(c.3) principal + (c.1) como fallback determinístico**. A destilação via LLM faz o trabalho editorial; o layout garante ordem e presença obrigatória de regions-chave (ex: "OP sempre tem `executive/overview-one-pager`").
  - **Resposta:** _____

#### Confirmação do conjunto

Se as 3 recomendações forem aceitas (a.3 + b.3 + c.3+c.1), o modelo final é:

> **Fase 3 produz `delivery-report.md` + `delivery-report.html` como hoje. Após isso, o usuário pode invocar a skill `deliverable-distiller` para produzir `one-pager.md`/`.html` e `executive-report.md`/`.html` — ambos destilados do DR com linguagem e densidade apropriadas, usando layouts específicos para garantir estrutura mínima.**

Isso **não quebra** o pipeline atual — adiciona capacidade sem remover nada. E é compatível com o fluxo real da Patria (DR é o produto do Discovery; OP/EX são comunicação para stakeholders).

- **D2.FINAL — Aceita o conjunto (a.3 + b.3 + c.3+c.1)?**
  - (sim) — avanço para ADR e atualizo tasks derivadas
  - (não, quero outro conjunto) — especifique
  - (quero discutir mais antes de decidir)
  - **Resposta:** _____

### 📦 Entregáveis

- ADR salvo em `projects/patria/kb/adr-001-deliverables-model.md` (decisão + justificativa + alternativas descartadas)
- TODO atualizado: tasks #5, #6, #7, #8, #11 ajustadas à estrutura escolhida
- Task #2 marcada como `[X] concluído` no TODO

### 📝 Notas / Registro

- 2026-04-17 — Task redesenhada no novo formato. Opções originais (a)(b)(c) desdobradas em 3 dimensões (DIM-A, DIM-B, DIM-C) para decisão mais granular. Recomendação consolidada: **a.3 + b.3 + c.3+c.1**.
- 2026-04-17 — Usuário aceitou o conjunto recomendado. ADR-001 criado e salvo.
- 2026-04-17 — Tasks derivadas ajustadas (#3, #5, #6, #7, #8, #11) + tasks novas adicionadas (#16, #17). Task #2 concluída.

### 🎯 Resultado

**Decisão aceita:** **a.3 + b.3 + c.3+c.1**

- **DIM-A:** `delivery-report.md` é canônico; OP e EX são destilações geradas por skill dedicada.
- **DIM-B:** DR sempre gerado pela Fase 3. OP/EX on-demand após Fase 3 (não quebra pipeline atual).
- **DIM-C:** Destilação LLM + layout mínimo obrigatório como piso determinístico.

**Novas tasks geradas:** #16 (skill `deliverable-distiller`), #17 (layouts OP/EX).

**Tasks derivadas ajustadas:** #3 (reinterpretação de `deliverables_scope`), #5 (caixa pós-Fase 3), #6 (region vira componente de layout), #7 (classificação vira sugestão), #8 (mantida), #11 (bitmap vira input de prompt).

---

## #3 — Adicionar flags no briefing/config para controlar condicionalidade  🟡  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #1 ✓, #2 ✓
- **Bloqueia:** #4, #6, #8, #9, #14
- **Resultado:** ver seção "🎯 Resultado" abaixo.

### 🎯 Objetivo

Introduzir no briefing/config do Discovery-to-Go os **3 flags que materializam as decisões dos ADRs e do diagnóstico**: modelo financeiro (projeto paga vs. fundo global), obrigatoriedade de ROI e escopo de entregáveis (OP/EX/DR). Sem esses flags, o pipeline não tem como decidir em runtime entre os dois comportamentos conflitantes identificados nas tasks #1 e #2.

**Não é nesta task que tornamos blocos/regions condicionais** — essa é a task #4. Aqui apenas **declaramos** o vocabulário de flags e onde eles vivem.

### 🧱 Entendimento

Três flags, três famílias de efeitos:

| Flag | Valores | Efeito principal | Tasks consumidoras |
|------|---------|------------------|--------------------|
| `financial_model` | `projeto-paga` (default) \| `fundo-global` | Bloco #8 (TCO) muda para "estimativa de consumo sem free tier"; regions financeiras têm variante | #4, #8 |
| `require_roi_justification` | `false` (default) \| `true` | Bloco #3 cobra ROI/payback; region `product/roi` ativa; auditor pontua dimensão ROI | #4, #6, #7, #9 |
| `deliverables_scope` | `["DR"]` (default) \| `["DR","OP"]` \| `["DR","EX"]` \| `["DR","OP","EX"]` | Após Fase 3, dispara destilação automática para OP e/ou EX (ADR-001) | #16 |

Adicionalmente, a task #14 separou dois valores de `iteration-policy.md` (prazo fixo 1+6 meses). Tecnicamente pertencem a outra família (cadência), mas vale alinhar nomenclatura para que a semântica "tudo configurável" fique consistente.

### 📋 Planejamento

1. **Decidir onde os flags vivem** (briefing? config? rule própria?) — ver D3.1.
2. **Decidir nomes finais e defaults** — ver D3.2.
3. **Atualizar `docs/starter-kit/briefing-template.md`** incluindo seção nova "Flags de configuração".
4. **Atualizar rule `base/behavior/rules/discovery/discovery.md`** com parágrafo que explica os flags e aponta para o briefing-template (não duplicar).
5. **Atualizar `dtg-artifacts/templates/customization/`** se D3.1 exigir arquivo novo de customization.
6. **Documentar impacto nas tasks consumidoras** — deixar ponteiros em #4, #6, #8, #9 (já feito parcialmente; revalidar).

### ❓ Decisões pendentes (preciso da sua resposta)

- **D3.1 — Onde os flags vivem fisicamente?**
  - (a) **Só no `briefing.md` do projeto** — 1 lugar; simples; mas briefing é conteúdo narrativo e flags podem se perder
  - (b) **Só no `config.md` do run** — lugar técnico, fácil de ler por skills; mas briefing precisaria duplicar para humano ler
  - (c) **Briefing declara, config consome** — briefing tem seção "Flags" (humano), config.md é gerado/copiado a partir do briefing. Skills leem config.md
  - **Recomendação:** **(c)** — separa intenção (briefing, humano) de estado (config, máquina). Padrão já usado na pipeline.
  - **Resposta:** _____

- **D3.2 — Nomes dos flags: manter como está ou renomear?**
  - Proposta atual: `financial_model`, `require_roi_justification`, `deliverables_scope`
  - Alternativa: padronizar prefixo (`flags.financial_model`, `flags.require_roi`, `flags.deliverables`)
  - **Recomendação:** manter **sem prefixo** (mais conciso, o contexto do arquivo já é "flags"). Renomear `require_roi_justification` → `require_roi` (mais curto, mesmo sentido).
  - **Resposta:** _____

- **D3.3 — Default de `deliverables_scope` — só `["DR"]` ou `["DR","OP"]`?**
  - (a) `["DR"]` — mínimo; quem quiser OP/EX precisa declarar. Aderente ao ADR-001 ("DR sempre, OP/EX on-demand")
  - (b) `["DR","OP"]` — OP é barato e quase sempre útil; fazer default evita esquecimento
  - **Recomendação:** **(a)** — ADR-001 diz explicitamente "on-demand". Forçar declaração é pedagógico e evita custo de tokens em projetos que só querem DR.
  - **Resposta:** _____

- **D3.4 — `require_roi` quando `financial_model=fundo-global` — proibir ou permitir?**
  - Contexto: se a organização opera com fundo global (Patria), por definição o investimento já foi aprovado antes. Faz sentido cobrar ROI no entregável?
  - (a) **Permitir combinação** — são flags independentes; alguém pode querer ROI por motivo fiscal/contábil mesmo com fundo global
  - (b) **Proibir combinação** — validator do config rejeita `financial_model=fundo-global` + `require_roi=true`
  - **Recomendação:** **(a)** — ortogonalidade é mais simples. Documenta-se "não é o caso comum" mas não bloqueia.
  - **Resposta:** _____

### 📦 Entregáveis

- `docs/starter-kit/briefing-template.md` com seção nova "Flags de configuração" (conforme D3.1)
- `base/behavior/rules/discovery/discovery.md` com parágrafo curto apontando para os flags
- (Se D3.1 = c) Arquivo/seção em `dtg-artifacts/templates/customization/` que define como config.md é gerado a partir do briefing
- Task #3 marcada como `[X] concluído`
- Tasks #4, #6, #8, #9 revalidadas com nomes finais dos flags

### 📝 Notas / Registro

- 2026-04-17 — Task estruturada no formato workbook. Aguardando D3.1, D3.2, D3.3, D3.4 para executar.
- 2026-04-17 — Respostas: D3.1=(c), D3.2=sem prefixo + renomear `require_roi`, D3.3=(a) `["DR"]`, D3.4=(a) permitir. Executando.
- 2026-04-17 — Briefing, rule e config README atualizados. Task concluída. Descoberto: `report-setup` existente ainda é lido por 12 arquivos — mantido como legacy alias, migração virou task #18.

### 🎯 Resultado

**Arquivos editados:**

- `base/starter-kit/client-template/projects/project-n/setup/start-briefing.md` — frontmatter inclui 3 novos flags; seção 9.1 reescrita para `deliverables_scope` (com nota sobre legacy `report-setup`); seções 9.5 (`financial_model`) e 9.6 (`require_roi`) adicionadas.
- `base/behavior/rules/discovery/discovery.md` — nova seção "⚙️ Flags de configuração" com tabela de efeitos; versão bumpada para 04.01.000; histórico atualizado.
- `base/starter-kit/client-template/config/README.md` — documenta como `config.md` do run materializa os flags do briefing.

**Defaults finais:**

```yaml
financial_model: "projeto-paga"
require_roi: false
deliverables_scope: ["DR"]
```

**Descoberta:** 12 arquivos do ecossistema ainda leem `report-setup: essential | executive | complete`. Mantido como legacy alias no frontmatter do briefing para não quebrar ninguém. Migração tracked na **task #18** (nova, abaixo).

---

## #4 — Tornar blocos #3, #4 e #8 condicionais ao briefing  🟡  [esforço: M]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #1 ✓, #3 ✓
- **Bloqueia:** #9
- **Resultado:** ver seção "🎯 Resultado" abaixo.

### 🎯 Objetivo

Fazer as skills `po` e `solution-architect` **consumirem os flags** declarados na task #3 e ajustarem seu comportamento em runtime. Sem esta task, os flags existem só em papel — o pipeline real ignora.

### 🧱 Entendimento

Mapeamento entre flags e pontos de mudança:

| Flag | Skill afetada | Onde no SKILL.md |
|------|--------------|------------------|
| `require_roi=false` (default) | `po` | Área 3 linha 3 ("ROI esperado") — skip; seção 3.3 do `product-vision.md` — omitir |
| `require_roi=true` | `po` | Comportamento atual (ROI obrigatório) |
| `financial_model=fundo-global` | `solution-architect` | Área 3 — TCO vira "Estimativa de consumo mensal sem free tier"; Build vs Buy foca em sustentabilidade/lock-in, não em custo total |
| `financial_model=projeto-paga` (default) | `solution-architect` | Comportamento atual (TCO 3 anos + Build vs Buy econômico) |
| FTE real (bloco #4) | — | **Não muda skill**. A filtragem FTE→EX/DR é downstream (destilador/layouts — tasks #6, #16, #17) |

**Insight:** o bloco #4 não exige edição de skill; a skill `po` continua capturando FTE sempre. Quem decide se aparece no OP é o destilador (task #16). Então task #4 edita só `po` (bloco #3) e `solution-architect` (bloco #8).

### 📋 Planejamento (decisões tomadas autonomamente)

- **D4.1** Canal de comunicação dos flags → skill: **orchestrator injeta via contexto** (padrão atual). Skills só precisam condicionar o comportamento. Documentação: incluir nota nas skills "Se `require_roi=false` no config.md...".
- **D4.2** Comportamento quando `require_roi=false`: pular área e **omitir seção 3.3** do `product-vision.md`. Consistência > completude.
- **D4.3** Comportamento quando `financial_model=fundo-global`: substituir TCO por "Estimativa de consumo mensal". Build vs Buy mantido mas refocado em sustentabilidade.
- **D4.4** Context-templates (10 packs): **não editar agora**. São guias domínio-específicos; evoluem sob demanda. Adicionar nota na skill: "ao rodar com context-template, respeitar flags acima".

Passos:

1. Editar `base/behavior/skills/po/SKILL.md` — adicionar bloco "Condicionais de flags" + ajustes no checklist Área 3 + nota na estrutura do `product-vision.md`.
2. Editar `base/behavior/skills/solution-architect/SKILL.md` — adicionar bloco "Condicionais de flags" + ajustes no checklist Área 3 + nota na estrutura do `strategic-analysis.md`.
3. Bump de versão em ambos.

### 📦 Entregáveis

- `base/behavior/skills/po/SKILL.md` atualizado (v04.00.000)
- `base/behavior/skills/solution-architect/SKILL.md` atualizado (v03.00.000)
- Task #4 marcada como `[X] concluído`

### 📝 Notas / Registro

- 2026-04-17 — Task estruturada e executada autonomamente (usuário autorizou autonomia até o próximo bloqueio real).

### 🎯 Resultado

**Arquivos editados:**

- `base/behavior/skills/po/SKILL.md` (v04.00.000) — Área 3 ganhou coluna "Condicional"; ROI (linha 3) só é cobrado quando `require_roi=true`; callout explicando o comportamento; marcador `<!-- OMITIR se require_roi=false -->` na estrutura do `product-vision.md`.
- `base/behavior/skills/solution-architect/SKILL.md` (v03.00.000) — Área 3 desdobrada em 2 modos (`projeto-paga` e `fundo-global`); seção "TCO obrigatório" bifurcada; estrutura do `strategic-analysis.md` ganhou variante "Estimativa de Consumo Cloud"; Constraints atualizadas.

**Blocos decididos:**
- #3 ROI: condicional a `require_roi`
- #4 FTE: **sem mudança na skill** — captura continua; filtragem é downstream (task #6/#16/#17)
- #8 TCO: dois modos completos (`projeto-paga` vs `fundo-global`)

**Context-templates (10 packs):** não editados. Decisão: evoluem sob demanda quando forem usados. Nota: o comportamento condicional **já funciona** independente do context-template, porque a condicionalidade está na skill.

---

## #5 — Modelar fase "pré-aprovação" + destilação no diagrama macro  🟠  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #2 ✓ (define caixa de destilação)
- **Bloqueia:** —

### 🎯 Objetivo

Tornar explícito no diagrama macro que (a) o pipeline começa **depois** da aprovação global — que acontece fora dele; e (b) existe uma caixa **opcional** de destilação pós-Fase 3 para gerar OP/EX a partir do DR (conforme ADR-001).

### 🧩 Resultado

**Arquivos editados (2):**

| Arquivo | Mudança |
|---|---|
| [docs/guides/discovery-pipeline.md](docs/guides/discovery-pipeline.md) | Diagrama mermaid ganhou nó `PRE` (Aprovação Global) antes do briefing e `DIST` (Destilação OP/EX) após `Entrega DR`. Ambos em linha pontilhada (`stroke-dasharray: 5 5`). Callout `[!info]` explica caixas pontilhadas. |
| [README.md](README.md) | Mesma atualização aplicada ao diagrama da seção "As 3 Fases do Pipeline" (L85). Callout adicionado. |

**Arquivo não afetado:**

- `docs/guides/quick-start.md` — inspecionado, não contém diagrama mermaid; apenas instruções operacionais. Nenhuma edição necessária.

**Convenção introduzida:** linhas pontilhadas no diagrama macro representam **etapas fora do escopo do pipeline** (upstream ou downstream opcional). Qualquer novo diagrama que represente o fluxo macro deve seguir o mesmo padrão.

---

## #6 — Revisar region `executive/overview-one-pager.md`  🟠  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #2 ✓, #3 ✓
- **Bloqueia:** —

### 🎯 Objetivo

Tornar a region **condicional às flags do briefing** (`financial_model`, `require_roi`) e deixar explícito que ela é **componente** do OP — não o entregável inteiro.

### 🧩 Resultado

**Arquivo editado:** [base/standards/conventions/report-regions/schemas/executive/overview-one-pager.md](base/standards/conventions/report-regions/schemas/executive/overview-one-pager.md)

Mudanças:

1. **Frontmatter** ganhou campo `deliverable-scope: ["OP", "EX", "DR"]` sinalizando que a region aparece em todos os entregáveis (distiller decide a forma).
2. **Descrição** atualizada: "TCO" → "esforço/custo/escopo" (alinhamento com escopo do OP segundo ADR-001 + `feedback_one_pager_scope.md`).
3. **Callout `[!info]`** explica a relação com o entregável OP (região = componente; OP completo vem do distiller — task #16).
4. **Callout `[!warning]`** documenta as duas condicionalidades:
   - `tco_resumo` ⇄ `estimativa_consumo` conforme `financial_model`
   - `roi_resumo` só quando `require_roi=true`
5. **Schema de dados** ganhou coluna **Condicional** e 2 campos novos:
   - `estimativa_consumo` (objeto com `opex_cloud_anual`, `premissas`, `confianca`) — para `fundo-global`
   - `roi_resumo` (objeto com `payback_meses`, `vpl`, `premissas`) — para `require_roi=true`
6. **Exemplo** ganhou comentários HTML mostrando quando substituir TCO por Estimativa de Consumo e quando adicionar o bloco ROI.

**Convenção introduzida:** campo `deliverable-scope` no frontmatter das regions — aceita `["OP"]`, `["EX"]`, `["DR"]` ou combinações. É sugestão para o distiller, não filtro mecânico (conforme ADR-001).

---

## #7 — Separar region `product/okrs-and-roi.md` em 2 regions  🟠  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #2 ✓
- **Bloqueia:** —

### 🎯 Objetivo

Separar a region única `product/okrs-and-roi.md` em **duas regions independentes** para que OKRs (sempre presente) e ROI (condicional) possam ser ativadas separadamente via flags do briefing.

### 🧩 Resultado

**Arquivos criados (2):**

| Arquivo | Propósito | Condicional |
|---|---|---|
| [base/standards/conventions/report-regions/schemas/product/okrs.md](base/standards/conventions/report-regions/schemas/product/okrs.md) | OKRs + critérios de sucesso do MVP | sempre (`deliverable-scope: ["OP","EX","DR"]`) |
| [base/standards/conventions/report-regions/schemas/product/roi.md](base/standards/conventions/report-regions/schemas/product/roi.md) | Análise de ROI (investimento, payback, VPL, premissas) | `require_roi=true` |

**Arquivo deprecado:** [base/standards/conventions/report-regions/schemas/product/okrs-and-roi.md](base/standards/conventions/report-regions/schemas/product/okrs-and-roi.md)

- Convertido em stub com `deprecated: true` e `superseded-by: ["okrs.md", "roi.md"]` no frontmatter
- Callout `[!danger]` explicando a substituição
- Tabela de migração para templates legados

**Campo novo no frontmatter:** `conditional-on: "require_roi=true"` em `roi.md` — padroniza como expressar condicionalidades derivadas das flags do briefing. Qualquer region condicional futura deve usar esse campo.

**Nota ADR-001:** a classificação `deliverable-scope` é **sugestão para o prompt do distiller** (task #16), não filtro mecânico. OKRs estão no DR sempre; distiller decide se resume/omite no OP.

---

## #8 — Criar variante "fundo global" para regions financeiras  🟠  [esforço: M]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #2 ✓, #3 ✓
- **Bloqueia:** —

### 🎯 Objetivo

Fazer as regions financeiras reconhecerem as flags `financial_model` e `require_roi` do briefing — algumas mudam **forma** (TCO vira "estimativa de consumo"), outras passam a ser **condicionais** (break-even só quando há ROI) ou **fortemente condicionais** (financial-scenarios só em combinação específica).

### 🧩 Resultado

**Arquivos editados (4):**

| Arquivo | Mudança |
|---|---|
| [financial/tco-3-years.md](base/standards/conventions/report-regions/schemas/financial/tco-3-years.md) | Frontmatter ganhou `deliverable-scope: ["EX","DR"]` + `conditional-on`. Callout `[!info]` documenta 2 modos. Nova seção **"Variante fundo-global"** com schema próprio (`estimativa_consumo`: cloud_provider, serviços com unidade/volume/custo, alertas_overrun, escopo_excluido), exemplo tabulado e premissas. |
| [financial/cost-per-component.md](base/standards/conventions/report-regions/schemas/financial/cost-per-component.md) | Ganhou `deliverable-scope: ["DR"]`. Callout `[!info]` diferencia "custo real" (projeto-paga) × "estimativa de consumo" (fundo-global). |
| [financial/financial-scenarios.md](base/standards/conventions/report-regions/schemas/financial/financial-scenarios.md) | Marcada como **fortemente condicional**: só produzir quando `financial_model=projeto-paga` AND `require_roi=true`. Callout `[!warning]`. |
| [financial/break-even.md](base/standards/conventions/report-regions/schemas/financial/break-even.md) | Condicional a `require_roi=true`. Callout `[!warning]` explicando que aprovação é upstream do pipeline. |

**Regions não afetadas:** `effort-estimation.md`, `revenue-projection.md`, `total-hours.md` — serão revisadas nas tasks #16/#17 quando o distiller definir o payload do OP/EX definitivamente.

**Convenção reforçada:** `conditional-on` no frontmatter — suporta expressões booleanas simples (`AND`, `OR`, `=`). Usada por distiller (task #16) para incluir/omitir regions por run.

---

## #9 — Revisar auditor + scoring-thresholds  🟠  [esforço: M]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #1 ✓, #4 ✓
- **Bloqueia:** —

### 🎯 Objetivo

Tornar o auditor **sensível às flags do briefing** — não penalizar ausência de ROI/TCO quando as flags declaram explicitamente que esses itens são opcionais. Criar arquivo default `scoring-thresholds.md` (nunca havia sido materializado, estava sendo apenas referenciado).

### 🧩 Resultado

**Arquivo novo criado:** [base/starter-kit/client-template/templates/customization/scoring-thresholds.md](base/starter-kit/client-template/templates/customization/scoring-thresholds.md) — default completo com:

- Pesos e pisos das 5 dimensões do auditor
- Threshold global (90% default)
- **Modificadores condicionais** às flags (`require_roi`, `financial_model`, `deliverables_scope`)
- Penalidades específicas (viabilidade negativa, mitigação genérica, tag ausente)
- Pisos do 10th-man (criticalidade, cruzamento, cross-eixo)
- **3 perfis predefinidos** (conservador 92%/75%, default 90%/70%, rapido 85%/65%)

**SKILL editada:** [base/behavior/skills/auditor/SKILL.md](base/behavior/skills/auditor/SKILL.md)

- Versão bumpada: 01.00.000 → 02.00.000
- Leitura obrigatória ganhou itens 13 (briefing com flags) e 14 (scoring-thresholds)
- Callout `[!warning]` "Critérios condicionais às flags do briefing" documenta 3 casos:
  - `require_roi=false` → remover ROI/payback/break-even do checklist
  - `financial_model=fundo-global` → substituir TCO por "estimativa de consumo sem free tier"
  - Validação automática Receita × TCO só quando `projeto-paga AND require_roi`
- Nova subseção "Validação alternativa: overrun de consumo (modo fundo-global)" — critérios específicos para fundo-global (volumes, custo anual, premissas, alertas de overrun)
- Validação de viabilidade original ganhou callout `[!info]` explicitando condicionalidade

**Convenção reforçada:** modificadores de scoring vivem em `scoring-thresholds.md` (customizável por cliente), **nunca** hardcoded na skill. SKILL descreve o *mecanismo*; `scoring-thresholds.md` descreve os *valores* e *regras condicionais*.

---

## #10 — Modificador organizacional "fundo-global / governança pré-aprovada"  🟢  [esforço: L]

- [X] **Status:** concluído (2026-04-17) — resolvido pela opção (b) via task #3
- **Depende de:** #3 ✓
- **Bloqueia:** —

### 🎯 Resultado

Resolvido **integralmente pela opção (b)** — flag no briefing — sem necessidade de arquivo transversal de "organizational modifiers".

**Como a solução (b) cobre o caso:**

- Flag `financial_model: fundo-global` (criada na task #3) captura a essência do modificador: projeto opera sob fundo corporativo centralizado, não arca custo individual
- Flag `require_roi: false` (default da task #3) captura o outro lado: aprovação foi upstream, não há obrigação de justificar retorno aqui
- Essas 2 flags juntas já modelam "governança pré-aprovada" em **todas as skills e regions** condicionais (tasks #4, #6, #7, #8, #9)

**Por que (a) não vale o esforço agora:**

- Modificador transversal exigiria: novo conceito de arquivo, logica de merge com packs, manutenção paralela — complexidade para resolver um único caso de uso real
- Se novos modificadores surgirem (ex: "time distribuído global", "compliance cross-jurisdictional"), reabrir a discussão com padrão validado em produção
- **Feedback registrado:** preferência por flags no briefing em vez de modificadores transversais — menor custo cognitivo, mesma expressividade

**Evidência de cobertura:**

| Aspecto do "fundo-global" | Materializado em |
|---|---|
| Custo vem de fundo, não do projeto | `financial_model=fundo-global` (briefing + solution-architect + regions financeiras) |
| Estimativa de consumo em vez de TCO | `tco-3-years.md` (variante fundo-global), `cost-per-component.md` |
| Sem exigência de ROI | `require_roi=false` (default) + `roi.md` condicional + `break-even.md` condicional |
| Auditor não penaliza ausência | `scoring-thresholds.md` + callout no `auditor/SKILL.md` |

Tudo isso foi feito sem criar uma camada nova de "modificadores". (a) fica arquivada como opção futura se os requisitos mudarem.

---

## #11 — Mapear questões do `environment.md` com bitmap [OP][EX][DR] no framework  🟢  [esforço: L]

- [X] **Status:** concluído (2026-04-17)
- **Problema:** o bitmap existe apenas em `projects/patria/kb/question-priority.md` (específico da Patria). Framework não tem isso.
- **O que fazer:** promover a ideia para o framework — `base/standards/.../question-priority-template.md` que qualquer projeto copia e adapta.
- **Nota (ADR-001):** o bitmap **deixa de ser filtro mecânico** e passa a ser **input para o prompt do `deliverable-distiller`** (task #16). Continua valioso: diz ao destilador "essa informação é OP-relevante" para ele priorizar na destilação.
- **Depende de:** #2 ✓
- **Bloqueia:** #16 (alimenta o prompt do destilador)

### 🎯 Resultado

**Arquivos criados/editados:**

| Arquivo | Mudança |
|---------|---------|
| [base/standards/blueprints/environment/question-priority-template.md](base/standards/blueprints/environment/question-priority-template.md) | **Criação** — template genérico com bitmap `[OP][EX][DR]` para os 10 domínios (D01–D10) do `environment.md`. Generalizado a partir de `projects/patria/kb/question-priority.md`. Inclui seção "Ajustes condicionais às flags do briefing" que dialoga com as 3 flags do ADR-001. |
| [base/standards/blueprints/environment/README.md](base/standards/blueprints/environment/README.md) | Adicionado callout `[!tip]` no topo referenciando o template e explicando a relação com o `deliverable-distiller`. |
| [base/behavior/skills/deliverable-distiller/SKILL.md](base/behavior/skills/deliverable-distiller/SKILL.md) | Versão `01.00.000 → 01.01.000`. Input opcional `question-priority` adicionado ao frontmatter. Seção "Bitmap semântico" reescrita com **regras explícitas** de hint × lei (o bitmap nunca remove region obrigatória nem inclui region ausente do layout). |

**Ponto-chave ADR-001:** o bitmap é **sugestão de densidade**, não filtro. O layout é a lei. Isso está explícito nos três arquivos acima. Projetos existentes que já tinham o bitmap como filtro (ex: Patria) permanecem válidos — o significado mudou mas a estrutura não quebrou.

**Não feito (escopo):** migração retroativa de `projects/patria/kb/question-priority.md` para o template genérico. Patria já tem o seu com dados reais preenchidos; o template é **ponto de partida para novos projetos**. Manter Patria como está.

---

## #12 — Atualizar `projects/patria/kb/environment.md` com % por entregável  🟢  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **O que fazer:** adicionar seção no cabeçalho do `environment.md` com "% respondido por entregável (OP / EX / DR)" para ficar visível o progresso.
- **Arquivo afetado:** `projects/patria/kb/environment.md`
- **Depende de:** —
- **Bloqueia:** —

### 🎯 Resultado

**Arquivo editado:** [projects/patria/kb/environment.md](projects/patria/kb/environment.md).

Mudanças:

- Frontmatter ganhou bloco `completude-por-entregavel` (OP 100% / EX ~30% / DR ~11%) — machine-readable.
- Adicionada seção "Progresso por entregável" logo após o cabeçalho com tabela explicando o status de cada entregável e callout `[!tip]` com leitura interpretativa (One-Pager pronto; EX/DR são progressivos via Discovery Pipeline).
- Referência cruzada para `question-priority.md` — sem duplicar o bitmap aqui.

---

## #13 — Atualizar lista de context-templates na rule  🟢  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** —
- **Bloqueia:** —

### 🎯 Resultado

**Arquivo editado:** [base/behavior/rules/discovery/discovery.md](base/behavior/rules/discovery/discovery.md) — versão `04.02.000 → 04.02.001`.

Mudanças:

- Tabela de context-templates **sincronizada** com `docs/guides/discovery-pipeline.md` (de 4 para 10 packs): adicionados `system-integration`, `migration-modernization`, `ai-ml`, `mobile-app`, `process-automation`, `platform-engineering`.
- Callout `[!tip] Templates múltiplos` incorporado (paridade com o guide).
- Estrutura do pack atualizada: referencia **`discovery-blueprint.md`** (arquivo atual consolidado) no lugar de `context.md` + `specialists.md` (estrutura antiga).
- Path corrigido: `context-templates/` na raiz do workspace → `base-artifacts/context-templates/` (paridade com guide).
- Histórico ganhou entrada `04.02.001`.

**Nota operacional:** os blueprints físicos dos packs não foram encontrados em `base-artifacts/context-templates/` durante esta edição (provavelmente ainda não migrados para a nova estrutura). A rule agora usa a nomenclatura correta — quando os arquivos existirem, a referência já estará consistente.

---

## #14 — Mover "Prazo fixo 1+6 meses" para `iteration-policy.md`  🟠  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #3 ✓
- **Bloqueia:** —
- **Origem:** conflito duro I identificado no diagnóstico da task #1
- **Resultado:** ver seção "🎯 Resultado" abaixo.

### 🎯 Objetivo

Remover o prazo fixo "1 mês de planejamento + 6 meses de desenvolvimento MVP" de `rules/discovery/discovery.md` (L229) — onde hoje vive como regra dura universal — e movê-lo para `iteration-policy.md` como **parâmetros configuráveis por projeto**. Um prazo de execução é uma decisão de projeto, não de framework; hardcodá-lo na rule conflita com clientes que operam com outros ciclos (OKRs trimestrais, releases mensais, etc.).

### 🧱 Entendimento

Situação atual:

- **Prazo fixo** está no callout `💰 Orcamento e Output, nao Input` da rule (L220-229), misturado com a lógica "orçamento como output". Dois conceitos acoplados no mesmo lugar.
- **`iteration-policy.md`** é referenciado em 15 arquivos mas o **arquivo default não existe fisicamente** (foi removido num restruct anterior — ver `git status`: `dtg-artifacts/templates/customization/rules/iteration-policy.md` deletado). Vou precisar **recriar o default** já incorporando os 2 novos parâmetros.
- **Parâmetros existentes** (documentados em `iteration-loop.md` L191-198): `max-iterations`, `stagnation-threshold`, `stagnation-consecutive`, `hr-loop-default-answer`, `hr-loop-max-passes`, `abort-requires-confirmation`.

Ou seja: a task tem **duas frentes** — (i) criar o arquivo default de `iteration-policy.md` que o sistema já espera; (ii) migrar o prazo fixo para lá.

### 📋 Planejamento

1. **Criar** `base/starter-kit/client-template/templates/customization/iteration-policy.md` com:
   - Parâmetros existentes (6, já documentados em `iteration-loop.md`)
   - 2 parâmetros novos: `planning_duration`, `mvp_duration`
2. **Editar** `base/behavior/rules/discovery/discovery.md`:
   - Remover a linha "Prazo fixo: 1 mês planejamento + 6 meses MVP" do callout de orçamento
   - Opcional: separar o callout em duas peças (orçamento vs. prazo) para desacoplar (ver D14.1)
   - Apontar para `iteration-policy.md` como fonte dos prazos
   - Bump de versão para `04.01.001`
3. **Editar** `base/behavior/rules/iteration-loop/iteration-loop.md` seção "Iteration Policy" para incluir os 2 parâmetros novos na tabela.
4. **Validar** que `layer-priority.md` e outros consumidores continuam consistentes.

### ❓ Decisões pendentes (preciso da sua resposta)

- **D14.1 — O callout "Orçamento e Output, nao Input" também vai ser retirado?**
  - Contexto: a rule tem o callout (L220-229) que mistura **2 princípios**: (a) "orçamento é output, não input" e (b) "prazo fixo 1+6". O princípio (a) **também já foi contestado** pelo diagnóstico da task #1 (é incompatível com `financial_model=fundo-global`, onde o budget já foi pré-aprovado).
  - Opções:
    - (a) **Minimal** — só remover a linha do prazo; deixar o princípio "orçamento como output" para revisitar na task #4 (blocos condicionais)
    - (b) **Completa** — reescrever o callout inteiro já tornando "orçamento como output" condicional a `financial_model=projeto-paga`
  - **Recomendação:** **(a) minimal**. A task #14 é cirúrgica (prazo). O princípio "orçamento como output" é da família da task #4 (blocos condicionais) — deixa lá para manter escopo das tasks enxuto.
  - **Resposta:** _____

- **D14.2 — Nomes dos novos parâmetros: `planning_duration` / `mvp_duration` ou outro?**
  - Opções:
    - (a) `planning_duration` e `mvp_duration` (proposta original)
    - (b) `planning-duration-months` e `mvp-duration-months` (hifenizado + unidade explícita, casa com o resto dos parâmetros do arquivo)
    - (c) `project-timeline.planning` e `project-timeline.mvp` (agrupado)
  - **Recomendação:** **(b)** — hifenizado casa com os 6 parâmetros existentes (`max-iterations`, `hr-loop-default-answer`, etc.); sufixo `-months` deixa a unidade inequívoca.
  - **Resposta:** _____

- **D14.3 — Defaults: manter 1 mês + 6 meses ou aproveitar para remover opinião?**
  - Opções:
    - (a) Manter defaults `1` e `6` — não muda comportamento para quem já usa a rule hoje
    - (b) Defaults `null` (sem prazo) — força o projeto a declarar explicitamente
    - (c) Defaults `1` e `6` mas marcar como `[exemplo]` — neutro em tom, ainda funcional
  - **Recomendação:** **(c)** — preserva o valor pedagógico ("esse é um ponto de partida comum") sem prescrever como lei do framework.
  - **Resposta:** _____

- **D14.4 — O que acontece no pipeline se os prazos não forem respeitados?**
  - Contexto: hoje a rule declara o prazo mas não há ação automática ligada a ele. Vale transformar em algo acionável?
  - Opções:
    - (a) **Nada** — é só um parâmetro declarativo consumido pelo `po` / `solution-architect` para calibrar escopo do MVP
    - (b) **Alerta brando** — orchestrator loga aviso se o backlog priorizado não cabe no `mvp-duration-months`
    - (c) **Bloqueio duro** — pipeline falha se não couber
  - **Recomendação:** **(a) nada**. Manter cirúrgico. Se no futuro quisermos alerta, vira task nova. `mvp-duration-months` entra no prompt das skills que dimensionam escopo; o resto é processo humano.
  - **Resposta:** _____

### 📦 Entregáveis

- `base/starter-kit/client-template/templates/customization/iteration-policy.md` (novo)
- `base/behavior/rules/discovery/discovery.md` atualizado (prazo removido do callout; versão bumpada)
- `base/behavior/rules/iteration-loop/iteration-loop.md` atualizado (tabela de parâmetros estendida)
- Task #14 marcada como `[X] concluído`

### 📝 Notas / Registro

- 2026-04-17 — Task estruturada no formato workbook. Descoberta: `iteration-policy.md` default não existe fisicamente, precisa ser criado. Aguardando D14.1, D14.2, D14.3, D14.4.
- 2026-04-17 — Respostas: D14.1=(a) minimal, D14.2=(b) hifenizado com `-months`, D14.3=(c) defaults `[exemplo]`, D14.4=(a) nenhuma ação. Executando.
- 2026-04-17 — `iteration-policy.md` default criado; prazo fixo removido de `discovery.md` (v04.01.001); tabela de parâmetros em `iteration-loop.md` estendida. Task concluída.

### 🎯 Resultado

**Arquivos criados:**

- `base/starter-kit/client-template/templates/customization/iteration-policy.md` (novo) — 8 parâmetros documentados (6 existentes + 2 novos), com exemplos de configurações conservadora e rápida.

**Arquivos editados:**

- `base/behavior/rules/discovery/discovery.md` — linha "Prazo fixo: 1 mês + 6 meses" removida; substituída por callout `[!info] Prazos de planejamento e MVP` apontando para `iteration-policy.md`. Versão `04.01.001`.
- `base/behavior/rules/iteration-loop/iteration-loop.md` — tabela de parâmetros estendida com `planning-duration-months` e `mvp-duration-months`.

**Defaults `[exemplo]` ativos:**

```yaml
planning-duration-months: 1
mvp-duration-months: 6
```

**Descoberta colateral resolvida:** o arquivo default `iteration-policy.md` não existia fisicamente apesar de ser referenciado em 15 arquivos. Agora existe e serve como ponte entre a rule e o config do run.

**Impacto residual:** nenhum. Callout "orçamento como output" permanece intacto (escopo da task #4). Princípio "orçamento como output" segue conflitante com `financial_model=fundo-global`, mas essa reconciliação é da #4.

---

## #15 — Política de sincronização rule ↔ guide  🟢  [esforço: S por edição]

- [X] **Status:** concluído (2026-04-17) — política estabelecida e cross-linkada
- **Depende de:** —
- **Bloqueia:** —

### 🎯 Resultado

**Arquivo novo criado:** [docs/guides/rule-guide-sync-policy.md](docs/guides/rule-guide-sync-policy.md) — política explícita em 1 arquivo com:

- **Regra principal:** "ao editar um, atualize o outro no mesmo commit"
- **Tabela de tópicos sincronizados** (fases, sub-fases, skills, outputs, flags, context-templates, Human Review) com apontamento de localização em cada arquivo
- **Tabela de tópicos exclusivos** (histórico/cláusulas na rule; exemplos/diagramas/FAQs no guide)
- **Checklist pré-commit** (4 itens)
- **Responsabilidades por skill/papel**
- **Procedimento em caso de divergência observada**

**Cross-links adicionados (2):**

| Arquivo | Mudança |
|---|---|
| [base/behavior/rules/discovery/discovery.md](base/behavior/rules/discovery/discovery.md) | Seção "Documentos Relacionados" ganhou wikilink para `rule-guide-sync-policy` |
| [docs/guides/discovery-pipeline.md](docs/guides/discovery-pipeline.md) | Callout `[!info]` no topo aponta para a policy como par operacional da rule |

**Por que não virou hook/CI:**

Considerado mas rejeitado nesta fase. A política é documental, curta e referenciada dos dois arquivos — qualquer contribuidor (humano ou agente) consegue ler e respeitar. Automação pode vir depois se a divergência voltar a acontecer; hoje, um arquivo explícito resolve o caso observado na task #13 (lista de context-templates divergente).

---

## #16 — Criar skill `deliverable-distiller`  🔴  [esforço: L]

- [X] **Status:** concluído (2026-04-17) — em `status: draft`
- **Depende de:** #2 ✓, #17 ✓, #11 (bitmap — opcional, pode ser integrado depois)
- **Bloqueia:** —

### 🎯 Objetivo

Criar a skill que materializa a decisão do ADR-001: **destilar** o Delivery Report consolidado em One-Pager e/ou Executive Report, respeitando layouts, flags condicionais e rastreabilidade.

### 🧩 Resultado

**Skill nova criada (2 arquivos):**

| Arquivo | Conteúdo |
|---|---|
| [base/behavior/skills/deliverable-distiller/SKILL.md](base/behavior/skills/deliverable-distiller/SKILL.md) | SKILL.md completa — frontmatter, princípios inegociáveis, 5 passos de instruction, restrições, handoff, exemplo mínimo, histórico. `status: draft` — implementação real dependerá de ajustes pós tasks #11 e #9. |
| [base/behavior/skills/deliverable-distiller/README.md](base/behavior/skills/deliverable-distiller/README.md) | README curto apontando quando é invocada, inputs, outputs, garantias. |

**5 princípios inegociáveis registrados na skill:**

1. Hierarquia OP ⊂ EX ⊂ DR (DR é fonte de verdade)
2. Rastreabilidade obrigatória (cada region destilada cita `source-region`)
3. Flags do briefing são lei (distiller não improvisa)
4. Layout é piso, não teto (obrigatórias + proibidas + opcionais condicionais)
5. Hallucination = falha crítica (gap vira placeholder explícito)

**Arquivos do ecossistema atualizados (2):**

| Arquivo | Mudança |
|---|---|
| [base/behavior/rules/discovery/discovery.md](base/behavior/rules/discovery/discovery.md) | Versão 04.01.001 → 04.02.000. Sub-fase 3.3 adicionada à tabela de Fase 3 como opcional. Tabela de outputs expandida com colunas condicionais. Callout `[!info]` explicando condicionalidade. Entrada 04.02.000 no histórico. |
| [docs/guides/discovery-pipeline.md](docs/guides/discovery-pipeline.md) | Diagrama mermaid da Fase 3 ganhou nó `DIST` (pontilhado). Tabela de sub-fases 3.1-3.5 renumerada com `Condicional`. Tabela de outputs expandida com linha OP e EX. Tabela de skills da Fase 3 ganhou `deliverable-distiller`. |

**Correção de rota (vs planejamento original):**

- Planejado: "usar bitmap `[OP][EX][DR]` como hint no prompt".
- Real: a skill menciona o bitmap como **hint opcional** para decisões ambíguas, explicitando que **layout é a lei** — bitmap nunca substitui layout. Evita ambiguidade semântica entre "sugestão" e "filtro".

---

## #18 — Migrar `report-setup` legacy para `deliverables_scope`  🟢  [esforço: M]

- [X] **Status:** concluído (2026-04-17)
- **Origem:** descoberto durante execução da task #3
- **Problema:** 12 arquivos do ecossistema ainda leem o flag antigo `report-setup: essential | executive | complete`. O novo canônico é `deliverables_scope`. Ambos coexistem no briefing atual (legacy mantido para não quebrar).
- **Mapeamento aplicado:**
  - `essential` → `["DR", "OP"]`
  - `executive` → `["DR", "OP", "EX"]`
  - `complete` → `["DR", "OP", "EX"]`
- **Depende de:** #3 ✓
- **Bloqueia:** —

### 🎯 Resultado

**Decisão central:** manter `report-setup` como **alias legacy aceito** em vez de remover. Razão: muitos artefatos/logs históricos já materializaram o valor; quebrar a leitura sem transição teria gerado `[GAP]` em runs existentes. O canônico passa a ser `deliverables_scope`; `report-setup` é derivado quando ausente, com warning explícito no tool.

**Arquivos editados:**

| Arquivo | Mudança |
|---------|---------|
| [tools/create-run/main.py](tools/create-run/main.py) | Lê `deliverables_scope` (list) como canônico; fallback para `report-setup` com warning + mapeamento. `generate_config_md` agora emite `deliverables-scope` primeiro no frontmatter gerado; `report-setup` permanece com comentário `# legacy alias`. Output do CLI mostra ambos. |
| [tools/create-run/README.md](tools/create-run/README.md) | Seção "Parses briefing frontmatter" reescrita: `deliverables_scope` canônico; `report-setup` como legacy com tabela de mapeamento. |
| [base/starter-kit/report-setups/README.md](base/starter-kit/report-setups/README.md) | Reescrito como "catálogo legacy de regions por HTML". Tabela de equivalência. Seção "Migração do briefing" com exemplo antes/depois. |
| [base/starter-kit/report-setups/essential.md](base/starter-kit/report-setups/essential.md) | Frontmatter: `status: legacy`, `deprecated-as-briefing-flag: true`, `superseded-by`, `deliverables-scope-equivalent: ["DR","OP"]`. Callout `[!warning] Legacy` no topo. |
| [base/starter-kit/report-setups/executive.md](base/starter-kit/report-setups/executive.md) | Idem, equivalente `["DR","OP","EX"]`. |
| [base/starter-kit/report-setups/complete.md](base/starter-kit/report-setups/complete.md) | Idem, equivalente `["DR","OP","EX"]`. |
| [base/starter-kit/README.md](base/starter-kit/README.md) | Árvore de diretórios: `report-setups/` marcado como **legacy** com nota sobre `deliverables_scope`. |
| [base/README.md](base/README.md) | Árvore de diretórios: idem. |
| [README.md](README.md) | Árvore de diretórios + tabela de setups substituída por **"Entregáveis (`deliverables_scope`)"** com tabela de MDs e HTMLs. Legacy mencionado como alias com link para `report-setups/README.md`. |
| [base/behavior/skills/consolidator/SKILL.md](base/behavior/skills/consolidator/SKILL.md) | Seção "Adaptação de tom por report-setup" → "Adaptação de tom por entregável (`deliverables_scope`)". Esclarece que o consolidator escreve o DR com profundidade técnica e o `deliverable-distiller` faz a adaptação de linguagem para OP/EX. |
| [docs/guides/quick-start.md](docs/guides/quick-start.md) | Callout "Report Setup" substituído por "Entregáveis (`deliverables_scope`)". Seção "Report Setup" na customização substituída por "Deliverables scope". Histórico ganhou entrada `03.03.000`. |
| [base/starter-kit/client-template/projects/project-n/setup/start-briefing.md](base/starter-kit/client-template/projects/project-n/setup/start-briefing.md) | Callout legacy suavizado de `[!warning]` para `[!info]` — task concluída; `report-setup` agora é apenas alias aceito, não "a ser migrado". |
| [projects/patria/projects/project-n/setup/start-briefing.md](projects/patria/projects/project-n/setup/start-briefing.md) | Frontmatter: adicionados `financial_model: "fundo-global"`, `require_roi: false`, `deliverables_scope: ["DR"]`. Seção 9.1 reescrita para `deliverables_scope` + 9.5/9.6 adicionadas com defaults Patria. |

**Não feito (escopo):** apagar a pasta `report-setups/`. Ela ainda contém o catálogo de regions que o `html-writer` consulta para montar o HTML. Foi **reposicionada** (legacy + catálogo), não removida. Se futuramente os layouts (`one-pager-layout.md`, `executive-layout.md`, `html-layout.md`) absorverem esse catálogo de regions, pode ser aposentada — fora do escopo desta task.

**Dor positiva:** o warning do tool ao derivar `deliverables_scope` de `report-setup` dá feedback imediato para quem continuar usando o legacy — atrito suave que empurra a migração dos briefings existentes.

---

## #17 — Criar layouts `one-pager-layout.md` e `executive-layout.md`  🟠  [esforço: S]

- [X] **Status:** concluído (2026-04-17)
- **Depende de:** #2 ✓
- **Bloqueia:** #16 (agora desbloqueada)

### 🎯 Objetivo

Criar o **piso determinístico** que o [deliverable-distiller](#16) deve respeitar ao produzir OP e EX. Cada layout lista as regions obrigatórias, opcionais e proibidas + o comportamento esperado do distiller.

### 🧩 Resultado

**Arquivos criados (2):**

| Arquivo | Escopo | Regions obrigatórias | Extensão alvo |
|---|---|---|---|
| [base/starter-kit/client-template/templates/customization/one-pager-layout.md](base/starter-kit/client-template/templates/customization/one-pager-layout.md) | OP | 5 (overview-one-pager, premises, risk-matrix, cost-per-component, prioritized-epics) | 1 página |
| [base/starter-kit/client-template/templates/customization/executive-layout.md](base/starter-kit/client-template/templates/customization/executive-layout.md) | EX | 11 (5 do OP + problem-and-context, value-proposition, okrs, macro-architecture, feasibility-analysis, go-no-go-criteria) | 5-15 páginas |

**Correção de rota (vs planejamento original):**

- Planejado: `dtg-artifacts/templates/customization/` — essa pasta **não existe** no repo atual.
- Real: `base/starter-kit/client-template/templates/customization/` — onde os outros defaults vivem (iteration-policy, scoring-thresholds, html-layout).

**Decisões estruturais documentadas nos layouts:**

1. **OP herdado pelo EX** — `executive-layout.md` declara `extends: one-pager-layout.md` no frontmatter. Distiller deve resolver a herança.
2. **Regions proibidas** listadas explicitamente (ROI no OP, logs no EX, etc.) para evitar que o distiller "vaze" conteúdo.
3. **Comportamento condicional** documentado: distiller avalia `conditional-on` de cada region contra flags do briefing.
4. **Warning obrigatório** se region de um layout estiver marcada como gap no DR — sinaliza que Discovery ficou incompleto; não é resolvido pelo distiller.
5. **Tabela comparativa OP × EX × DR** no `executive-layout.md` serve de referência visual para orchestrator/distiller.

**README atualizado:** [base/starter-kit/client-template/templates/customization/README.md](base/starter-kit/client-template/templates/customization/README.md) — adicionadas 2 linhas na tabela de overrides.

---

## Ordem de execução sugerida

```
#1 (diagnóstico) ✓ → #2 (ADR-001) ✓ → #3 (flags) ✓ → #14 (prazo) ✓ → #4 (blocos condicionais)
                                                                      ↓
                                              #5, #6, #7, #8 em paralelo
                                                                      ↓
                               #17 (layouts) → #16 (distiller) → #9 (auditor)
                                                                      ↓
                          #10, #11, #12, #13, #15, #18 (migração legacy)
```

**Próximo item a atacar:** **#4** — tornar blocos #3 (ROI), #4 (FTE) e #8 (TCO) da Fase 1 condicionais aos flags já declarados em #3. É onde as flags viram comportamento real nas skills `po` e `solution-architect`.
