---
title: Behavior Principles
description: Princípios fundamentais que regem toda a base de regras e o comportamento da IA
project-name: global
version: 01.00.005
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - comportamento
  - principio
created: 2026-04-03 09:00
---

# 🏛️ Princípios do Behavior

Princípios fundamentais e invioláveis que regem toda a base de conhecimento e o comportamento da IA. Este documento tem **prioridade sobre todos os outros** — suas regras são a base sobre a qual tudo é construído.

---

## 📜 Princípio #1 — O Behavior é o Universo

> [!danger] Regra suprema
> **Nenhum documento, formato ou comportamento é criado fora do que está definido na base de regras (behavior).** As regras são a única fonte de verdade.

### 📌 O que isso significa

- ✅ Todo documento `.md` segue as regras definidas em [[writing/markdown-writing/markdown-writing]]
- ✅ Toda tag segue as convenções de [[organization/taxonomy-and-tags/taxonomy-and-tags]]
- ✅ Todo índice e backlink segue [[organization/index-and-navigation/index-and-navigation]]
- ✅ Todo ciclo de vida segue [[organization/document-management/document-management]]
- ✅ Se uma regra não existe para um cenário, **a regra deve ser criada primeiro**
- ❌ Apesar da IA poder sugerir melhorias, na prática **nunca** aplica essas melhorias sem que estejam nos padrões.
- ❌ A IA **nunca** infere regras — na dúvida, **pergunta**

> [!warning] Atenção
> Se durante o trabalho a IA identificar uma situação que não está coberta pelo behavior, ela deve **pausar e perguntar** e/ou **iniciar uma conversa** com o usuário para discutir a criação de uma nova regra.

---

## 📜 Princípio #2 — Desvios São Registrados

> [!danger] Regra suprema
> Quando o usuário opta por **seguir no desenvolvimento de uma regra, contra a sugestão da IA**, essa decisão **deve ser registrada** no documento afetado.

### 📌 Por que registrar desvios

- 🔍 **Rastreabilidade** — saber quais decisões foram tomadas fora do padrão
- 🧠 **Contexto** — entender o motivo da exceção no futuro
- 🔄 **Revisão** — permitir que administradores revisem desvios periodicamente
- 📊 **Evolução** — desvios recorrentes podem indicar que o behavior precisa ser atualizado

### 📋 Como registrar

Todo documento que contenha um desvio de behavior deve incluir uma seção **⚠️ Desvios de Behavior** posicionada **antes do Histórico de Alterações**:

```markdown
## ⚠️ Desvios de Behavior

| Timestamp        | Regra                    | Sugestão da IA           | Decisão do Usuário | Motivo            |
| ---------------- | ------------------------ | ------------------------ | ------------------ | ----------------- |
| 2026-04-03 10:00 | gestao-de-documentacao   | Atualizar doc existente  | Criar novo         | Motivo informado  |
```

| Campo               | Descrição                                                  |
| ------------------- | ---------------------------------------------------------- |
| `Timestamp`         | 📅 Data/hora em que o desvio ocorreu (formato `yyyy-MM-DD HH:mm`) |
| `Regra`             | 📏 Wikilink ou nome da regra que sugeria outro caminho      |
| `Sugestão da IA`    | 🤖 O que a IA recomendou com base no behavior               |
| `Decisão do Usuário`| 👤 O que o usuário decidiu fazer                            |
| `Motivo`            | 💬 Justificativa do usuário para o desvio                   |

> [!info] Importante
> A seção de desvios **só existe quando há desvios**. Não criar a seção preventivamente em documentos sem desvio.

> [!tip] Dica
> A IA deve **perguntar o motivo** ao usuário no momento do desvio para registrar a justificativa corretamente.

---

## 📜 Princípio #3 — O Behavior Evolui

> [!info] Melhoria contínua
> As regras não são imutáveis. Se desvios recorrentes indicam que uma regra precisa ser ajustada, a regra deve ser **revisada e atualizada** ao invés de continuamente violada.

- 🔄 Desvios frequentes na mesma regra → sugerir revisão da regra ao usuário
- 🆕 Cenários não cobertos → sugerir criação de nova regra
- 🧹 Regras que ninguém segue → sugerir arquivamento ou obsolescência

---

## 🔗 Documentos Relacionados

- [[writing/markdown-writing/markdown-writing]] — Regras de formatação que todo documento deve seguir
- [[organization/taxonomy-and-tags/taxonomy-and-tags]] — Convenções de categorização governadas por este princípio
- [[organization/index-and-navigation/index-and-navigation]] — Regras de navegação governadas por este princípio
- [[organization/document-management/document-management]] — Ciclo de vida dos documentos, incluindo registro prático de desvios
- [[foundations/project-boundaries/project-boundaries]] — Fronteiras absolutas governadas pelos princípios do behavior

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição                                                  |
| --------- | ---------------- | ---------------------------------------------------------- |
| 01.00.000 | 2026-04-03 09:00 | Criação do documento                                       |
| 01.00.001 | 2026-04-03 09:30 | Ajustes pelo usuário nos princípios #1 e #2                |
| 01.00.002 | 2026-04-03 10:00 | Padronização de campos de data para Timestamp (yyyy-MM-DD HH:mm) |
| 01.00.003 | 2026-04-03 10:30 | Correção do created no frontmatter e formato explícito no campo Timestamp |
| 01.00.004 | 2026-04-04 09:30 | Renomeação de principios-do-behavior para behavior-principles (naming-convention) |
| 01.00.005 | 2026-04-04 10:00 | Correção de tag: behavior→comportamento (padronização pt-BR sem acentos) |
