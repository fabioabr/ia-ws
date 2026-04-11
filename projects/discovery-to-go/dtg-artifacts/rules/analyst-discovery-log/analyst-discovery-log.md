---
title: Interview Log
description: Regra obrigatoria de geracao do log de entrevista (interview.md) durante a Fase 1 (Discovery) do pipeline
project-name: discovery-to-go
version: 04.00.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - registro
  - discovery
  - entrevista
created: 2026-04-03 14:00
---

# 📋 Interview Log

Regra obrigatoria que define a geracao do **log de entrevista** (`interview.md`) durante a Fase 1 (Discovery) do pipeline. O arquivo registra a reuniao conjunta tematica entre os agentes especialistas e o customer, usando formato de dialogo em tabela com personas identificadas por emoji.

> [!danger] Regra fundamental
> **Toda Fase 1 (Discovery) DEVE gerar um interview.md.** O log e criado no inicio da fase e atualizado em append-only ate a conclusao de todos os 8 blocos tematicos.

---

## 📂 Localizacao

O log deve ficar em:

```
{run-folder}/
└── iteration-{i}/
    └── logs/
        └── interview.md
```

> [!warning] Atencao
> O arquivo de log e **unico por iteracao** — toda a Fase 1 (Discovery) e registrada no mesmo arquivo.

---

## 📋 Frontmatter

```yaml
---
title: "Interview Log — {Nome do Projeto}"
description: Log cronologico da reuniao conjunta tematica da Fase 1 (Discovery) para o projeto {Nome do Projeto}
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: pipeline
category: log
area: tecnologia
tags:
  - log
  - entrevista
  - discovery
  - fase-1
created: YYYY-MM-DD HH:mm
iteration: {i}
run: {run-id}
---
```

Campos adicionais alem do schema padrao:

| Campo | Tipo | Descricao |
|-------|------|-----------|
| iteration | number | Numero da iteracao atual |
| run | string | Identificador do run |

---

## 📰 Header

Logo apos o H1, o log deve conter:

1. **Info line** — run, iteracao, fase, horario de inicio e context-template:

```markdown
> **Run:** {run-id} | **Iteracao:** {i} | **Fase:** 1 — Discovery
> **Inicio:** YYYY-MM-DD HH:mm | **Context-Template:** {pack}
```

2. **Tabela de participantes** — todos os agentes que participam da reuniao:

```markdown
### Participantes

| Emoji | Agente | Papel |
|-------|--------|-------|
| 🎯 | po | Product Owner — visao, personas, valor, organizacao |
| 🏗️ | solution-architect | Arquitetura, tecnologia, TCO |
| 🔐 | cyber-security-architect | Privacidade, seguranca, compliance |
| 🧑‍💼 | customer | Cliente simulado |
| 🤖 | orchestrator | Orquestrador (mediacao) |
| 🧩 | custom-specialist | Especialista sob demanda (quando invocado) |
```

> [!info] custom-specialist
> O `custom-specialist` so aparece na tabela de participantes quando efetivamente invocado durante a reuniao. Se nao participar, omitir da tabela.

---

## 💬 Formato de Dialogo

Cada trecho de conversa usa uma **tabela de 2 colunas**:

```markdown
| Quem | Dialogo |
|------|---------|
| 🎯 po | Pergunta aqui... |
| 🧑‍💼 customer | [BRIEFING] Resposta aqui... |
```

### Regras da tabela de dialogo

- Cada **linha** e um turno de fala
- A coluna **Quem** usa `emoji + nome do agente`
- Respostas do customer devem conter **source tags** (ver secao abaixo)
- Quando outro agente faz um **aparte** (intervencao fora do seu bloco), prefixar com `*(aparte)*`:

```markdown
| 🏗️ solution-architect | *(aparte)* Quando diz "multi-banco", estamos falando de quantas integracoes? |
```

- **Callouts** (`> [!warning]`, `> [!danger]`, `> [!info]`) vao **ENTRE** tabelas de dialogo, nunca dentro delas
- Uma tabela de dialogo pode ser **dividida por callouts** — isso e intencional para enfase visual

---

## 🏷️ Source Tags

Toda resposta do customer deve ser prefixada com uma source tag que indica a origem da informacao:

| Tag | Significado | Quando usar |
|-----|-------------|-------------|
| `[BRIEFING]` | Informacao do briefing | Dado extraido diretamente do documento de briefing |
| `[INFERENCE]` | Inferencia do customer | Dado deduzido ou inferido, nao declarado explicitamente no briefing |
| `[RAG]` | Context-template | Informacao proveniente do contexto do context-template |

> [!warning] Inferencias
> Toda resposta com `[INFERENCE]` deve gerar um callout `> [!warning] Dado inferido` entre as tabelas, sinalizando necessidade de validacao no Human Review.

---

## 📢 Callouts entre Dialogos

Os callouts sao inseridos **entre** tabelas de dialogo para dar destaque visual a eventos importantes:

| Tipo | Uso |
|------|-----|
| `> [!warning] Dado inferido` | Resposta do customer e inferencia — precisa de validacao no Human Review |
| `> [!danger] Risco identificado` | Risco de seguranca, compliance ou critico identificado durante o dialogo |
| `> [!info] Decisao registrada` | Decisao de arquitetura ou negocio tomada durante o dialogo |

---

## 📦 Estrutura de Bloco

A entrevista e organizada em **8 blocos tematicos**. Cada bloco segue esta estrutura:

### 1. Cabecalho do bloco

```markdown
## 📋 Bloco #N — Tema

**Dono:** {emoji} {agente} | **Inicio:** HH:mm
```

### 2. Tabela(s) de dialogo

Uma ou mais tabelas de dialogo, opcionalmente separadas por callouts.

### 3. Marcador de conclusao

```markdown
**✅ Bloco #N concluido.**
```

### 4. Tabela de resumo do bloco

```markdown
| Item | Valor |
|------|-------|
| ... | ... |
```

A tabela de resumo captura os **achados-chave** do bloco em pares item/valor.

### Exemplo completo de bloco

```markdown
## 📋 Bloco #1 — Visao e Proposito

**Dono:** 🎯 po | **Inicio:** 09:00

| Quem | Dialogo |
|------|---------|
| 🎯 po | Qual e o problema principal que o projeto resolve? |
| 🧑‍💼 customer | [BRIEFING] Gestores gastam 12h/semana consolidando dados manualmente. |
| 🎯 po | Existe algum concorrente direto? |
| 🧑‍💼 customer | [INFERENCE] Tipicamente 3 a 5 fornecedores no mercado. |

> [!warning] Dado inferido
> O customer mencionou "3 a 5 fornecedores" mas nao especificou fonte. Registrado para validacao no Human Review.

| Quem | Dialogo |
|------|---------|
| 🎯 po | Qual e a proposta de valor unica? |
| 🧑‍💼 customer | [BRIEFING] Automacao completa com IA. |

**✅ Bloco #1 concluido.**

| Item | Valor |
|------|-------|
| Problema | Consolidacao manual (12h/semana) |
| Diferencial | Automacao com IA |
```

---

## 📊 Resumo Global

Ao final de todos os 8 blocos, o log deve conter:

### Tabela de status dos blocos

```markdown
## 📊 Resumo da Reuniao

| Bloco | Tema | Dono | Status |
|-------|------|------|--------|
| #1 | Visao e Proposito | 🎯 po | ✅ |
| #2 | Personas e Jornada | 🎯 po | ✅ |
| #3 | Valor Esperado / OKRs | 🎯 po | ✅ |
| #4 | Processo, Negocio e Equipe | 🎯 po | ✅ |
| #5 | Tecnologia e Seguranca | 🏗️ solution-architect | ✅ |
| #6 | LGPD e Privacidade | 🔐 cyber-security-architect | ✅ |
| #7 | Arquitetura Macro | 🏗️ solution-architect | ✅ |
| #8 | TCO e Build vs Buy | 🏗️ solution-architect | ✅ |
```

### Tabela de metricas

```markdown
| Metrica | Valor |
|---------|-------|
| Duracao total | HH:mm — HH:mm (Xh Ymin) |
| Dados por fonte | [BRIEFING] X% · [INFERENCE] Y% · [RAG] Z% |
| Conflitos detectados | N |
| Riscos identificados | N (descricao breve) |
| Pendencias para Human Review | N (descricao breve) |
```

---

## 📏 Regras de Registro

- ✅ O log e **append-only** — nunca editar entradas anteriores
- ✅ **Toda interacao** relevante entre agentes e customer deve ser registrada
- ✅ Cada bloco deve ter **timestamp de inicio** no formato `HH:mm`
- ✅ O log e a **unica fonte de verdade** sobre o que foi discutido na Fase 1
- ✅ **Toda informacao** compartilhada pelo customer deve ser capturada, mesmo que aparentemente menor
- ✅ Observacoes dos agentes devem ser **objetivas e concisas**
- ❌ **Nao omitir** perguntas que o customer nao soube responder — registrar como lacuna
- ❌ **Nao editar** entradas anteriores — se uma informacao foi corrigida, registrar nova entrada

> [!info] Append-only
> O log e um registro historico imutavel. Se uma informacao foi corrigida posteriormente, registre uma nova entrada com a correcao — nao altere a entrada original.

---

## 🤖 Papel do Pipeline

- 📝 **Criar o interview.md** no inicio da Fase 1
- 🕐 **Registrar cada turno de dialogo** em tempo real
- 🏷️ **Aplicar source tags** em todas as respostas do customer
- 📢 **Inserir callouts** quando detectar inferencias, riscos ou decisoes
- 📊 **Gerar resumo do bloco** ao concluir cada bloco tematico
- 🏁 **Gerar resumo global** ao concluir todos os 8 blocos

---

## 🔗 Documentos Relacionados

- [[core/discovery/discovery]] — Processo de discovery que este log documenta
- [[core/behavior-principles/behavior-principles]] — Principios fundamentais que governam o registro de informacoes
- [[core/markdown-writing/markdown-writing]] — Regras de formatacao para o arquivo de log

## 📜 Historico de Alteracoes

| Versao    | Timestamp        | Descricao            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-03 14:00 | Criacao do documento |
| 02.00.000 | 2026-04-03 16:00 | Renomeacao de log-de-levantamento para log-de-discovery |
| 02.00.001 | 2026-04-04 09:30 | Renomeacao de log-de-discovery para discovery-log (naming-convention) |
| 02.00.002 | 2026-04-04 10:00 | Correcao de tag: log para registro (padronizacao pt-BR sem acentos) |
| 03.00.000 | 2026-04-04 | Adicao de 4 tipos de entrada para iteracoes do pipeline: Iteracao, Perguntas enviadas, Respostas recebidas, Convergencia |
| 03.00.001 | 2026-04-05 | Atualizacao terminologia v1 para v2: "Nivel" substituido por "Sub-etapa" em todo o documento |
| 04.00.000 | 2026-04-11 | Rewrite for Pipeline v0.5: table-based dialogue format with emoji personas, source tags, callouts between dialogues, block-based structure with summaries |
