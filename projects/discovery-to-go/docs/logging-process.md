---
title: Logging Process
description: Guia detalhado sobre como a IA deve gerar e manter logs e anotações em todos os processos de trabalho
project-name: global
version: 01.03.000
status: ativo
author: claude-code
category: how-to
area: tecnologia
tags:
  - how-to
  - registro
  - processo
  - rastreabilidade
created: 2026-04-04 10:30
---

# 📝 Logging Process

Guia prático que explica **como, quando e o que** a IA deve registrar durante qualquer processo de trabalho. O log é a **memória viva** do processo — sem ele, decisões se perdem, contexto desaparece e a continuidade fica comprometida.

> [!danger] Princípio fundamental
> **Se não foi registrado, não aconteceu.** Todo processo relevante deve ter um log. O log não é burocracia — é a garantia de rastreabilidade, continuidade e aprendizado.

---

## 🧠 Por que Logar?

```
SEM LOG                              COM LOG
────────                             ────────
😕 "Por que decidimos X?"            📋 "Decisão X tomada porque..."
😕 "Quem respondeu isso?"            📋 "Usuário respondeu em 10:30..."
😕 "Onde paramos?"                   📋 "Último ponto: Fase 2, categoria Segurança"
😕 "Havia algum conflito?"           📋 "Conflito identificado entre A e B, resolvido com C"
😕 "Outra IA pode continuar?"        📋 "Sim — log tem todo o contexto"
```

| Benefício | Descrição |
| --------- | --------- |
| 🔍 **Rastreabilidade** | Saber o que foi perguntado, respondido e decidido |
| 🧠 **Contexto** | Entender o *porquê* por trás de cada decisão |
| 🔄 **Continuidade** | Outra sessão de IA pode retomar sem perder contexto |
| 📊 **Aprendizado** | Identificar padrões (dúvidas recorrentes, conflitos frequentes) |
| ⚠️ **Proteção** | Registrar desvios e decisões controversas |
| 👥 **Transparência** | Qualquer pessoa pode auditar o processo |

---

## 📋 Tipos de Log

### 🔄 Discovery Log

O log principal do processo de discovery de um novo projeto.

| Aspecto | Detalhe |
| ------- | ------- |
| 📂 **Localização** | `dtg-artifacts/rules/analyst-discovery-log/` |
| 📏 **Regra** | `dtg-artifacts/rules/analyst-discovery-log/` |
| 🔄 **Quando** | Durante todo o processo de discovery (Fases 1-3) |
| 📄 **Quantidade** | 1 arquivo único por projeto |
| 🤖 **Quem mantém** | A IA, em tempo real |

### 🎛️ Orchestration Log

Log de orquestração quando múltiplos agentes/processos rodam em paralelo.

| Aspecto | Detalhe |
| ------- | ------- |
| 📂 **Localização** | Junto aos artefatos sendo orquestrados |
| 🔄 **Quando** | Quando há coordenação entre múltiplos agentes ou processos |
| 📄 **Conteúdo** | Status dos agentes, decisões de coordenação, métricas |

### 📄 Document Log

Registro embutido em cada documento via seção de Histórico de Alterações.

| Aspecto | Detalhe |
| ------- | ------- |
| 📂 **Localização** | Última seção de cada `.md` |
| 📏 **Regra** | Convenção global de markdown-writing |
| 🔄 **Quando** | A cada alteração no documento |
| 📄 **Formato** | Tabela Versão / Timestamp / Descrição |

---

## 🏷️ Tipos de Entrada

Cada entrada no log deve ser classificada com um tipo. A classificação permite **filtrar, buscar e analisar** o log depois.

| Tipo | Emoji | Quando usar | Exemplo |
| ---- | ----- | ----------- | ------- |
| **Início** | 🎯 | Começo de uma sub-etapa ou processo | `🎯 Início da Fase 1 — Visão do Produto` |
| **Pergunta** | ❓ | IA faz uma pergunta ao usuário | `❓ Qual stack tecnológica será utilizada?` |
| **Resposta** | 💬 | Usuário responde uma pergunta | `💬 Python FastAPI para backend, Vue.js para frontend` |
| **Observação** | 💡 | IA identifica insight, risco ou ponto de atenção | `💡 Prazo de 3 meses é agressivo para equipe de 3 devs` |
| **Decisão** | ⚠️ | Usuário toma uma decisão que impacta o processo | `⚠️ MVP terá apenas CRUD + dashboard, sem relatórios` |
| **Conflito** | 🚫 | Conflito entre respostas, fronteiras ou documentos | `🚫 Orçamento de R$2k/mês incompatível com 10 microsserviços` |
| **Resolução** | ✅ | Um conflito ou dúvida foi resolvido | `✅ Arquitetura alterada para monolito modular` |
| **Conclusão** | 🏁 | Término de uma sub-etapa ou processo | `🏁 Fase 2 concluída — fronteiras aprovadas` |
| **Pausa** | ⏸️ | Processo interrompido temporariamente | `⏸️ Usuário precisa consultar CTO sobre stack` |
| **Retomada** | ▶️ | Processo retomado após pausa | `▶️ Retomado após alinhamento com CTO` |
| **Iteração** | 🔄 | Início de uma nova iteração do pipeline | `🔄 Iteração 2 iniciada — respostas do cliente recebidas` |
| **Perguntas enviadas** | 📤 | Perguntas do challenger enviadas ao cliente | `📤 5 perguntas enviadas ao cliente (NLP, custo, equipe)` |
| **Respostas recebidas** | 📥 | Respostas do cliente coletadas | `📥 Respostas recebidas — NLP é mandatório, custo validado` |
| **Convergência** | 🎯 | Critério de convergência atingido | `🎯 Convergência atingida — nota 92%, pipeline concluído` |

> [!warning] Atenção
> **Não inventar tipos.** Usar exclusivamente os tipos da tabela acima. Se uma situação não se encaixa, usar 💡 **Observação** como fallback.

---

## 📐 Formato de Cada Entrada

Toda entrada no log segue o formato de tabela:

```markdown
| Timestamp        | Tipo           | Descrição                                    |
| ---------------- | -------------- | -------------------------------------------- |
| 2026-04-04 10:30 | 🎯 Início      | Início do discovery da Fase 1            |
| 2026-04-04 10:31 | ❓ Pergunta    | Qual problema o produto resolve?             |
| 2026-04-04 10:32 | 💬 Resposta    | Resolve X para público Y                     |
| 2026-04-04 10:33 | 💡 Observação  | Usuário tem clareza sobre o problema         |
```

### 📏 Regras de formato

| Regra | Detalhe |
| ----- | ------- |
| ⏱️ **Timestamp** | Formato `yyyy-MM-DD HH:mm` — sempre |
| 🏷️ **Tipo** | Emoji + nome do tipo — sempre |
| 📝 **Descrição** | Frase objetiva e concisa — sem texto longo |
| 📏 **Uma linha** | Cada entrada ocupa uma linha na tabela |

> [!tip] Dica para descrições longas
> Se uma resposta do usuário for muito longa, registre um **resumo objetivo** no log. O detalhamento completo estará no documento gerado.

---

## 🔄 Quando Logar — O Pipeline de Logging

### 📍 Em cada interação

```
👤 Usuário diz algo
        │
        ▼
🤖 IA avalia: é relevante para o processo?
        │
   ✅ Sim ──► Registra no log
   ❌ Não ──► Não registra (ex: "ok", "entendi", small talk)
        │
        ▼
🤖 IA responde/pergunta
        │
        ▼
🤖 A resposta/pergunta da IA é relevante?
        │
   ✅ Sim ──► Registra no log
   ❌ Não ──► Não registra
```

### ✅ O que DEVE ser logado

| Situação | Tipo | Por quê |
| -------- | ---- | ------- |
| IA faz pergunta ao usuário | ❓ Pergunta | Rastreabilidade do questionário |
| Usuário responde com informação nova | 💬 Resposta | Registro da decisão/informação |
| IA identifica risco ou ponto de atenção | 💡 Observação | Transparência do raciocínio da IA |
| Usuário toma decisão que impacta o projeto | ⚠️ Decisão | Rastreabilidade de decisões |
| Conflito entre informações | 🚫 Conflito | Registro do problema |
| Conflito resolvido | ✅ Resolução | Registro da solução |
| Início/fim de sub-etapa | 🎯/🏁 | Marcos do processo |
| Usuário não sabe responder | 💡 Observação | Registro de lacuna |
| Usuário muda de ideia | ⚠️ Decisão | Registro da mudança e motivo |
| Processo pausado/retomado | ⏸️/▶️ | Continuidade |

### ❌ O que NÃO deve ser logado

| Situação | Por quê |
| -------- | ------- |
| "Ok", "entendi", "pode continuar" | Não agrega informação |
| Formatação ou ajuste visual de documento | Registro já existe no changelog do doc |
| Erros de digitação corrigidos | Irrelevante para o processo |
| Perguntas sobre como usar a ferramenta | Não é sobre o projeto |

---

## 💡 Como Escrever Boas Observações

As **observações** (💡) são o tipo mais valioso do log — é onde a IA registra seu **raciocínio e análise**. Uma boa observação ajuda qualquer pessoa a entender o contexto.

### ✅ Boas observações

| Observação | Por que é boa |
| ---------- | ------------- |
| `💡 Prazo de 3 meses com equipe de 3 devs exige escopo muito enxuto no MVP` | Conecta dados (prazo + equipe) com uma conclusão (risco) |
| `💡 Usuário não definiu métricas para o OKR — precisa detalhar antes de avançar` | Identifica lacuna específica com ação necessária |
| `💡 Stack React escolhida mas equipe tem experiência em Angular — risco de curva de aprendizado` | Identifica conflito entre decisões |
| `💡 Integração com gov.br requer credenciais — adicionar como dependência externa no plano` | Identifica ação necessária que pode ser esquecida |

### ❌ Observações ruins

| Observação | Por que é ruim |
| ---------- | -------------- |
| `💡 Boa resposta do usuário` | Não agrega nada — o que era bom? |
| `💡 Tudo certo` | Vazio — sem contexto |
| `💡 Precisa pensar melhor sobre isso` | Sobre o quê? Qual aspecto? |
| `💡 O usuário está engajado` | Irrelevante para o processo técnico |

> [!tip] Regra de ouro
> Uma boa observação responde: **"O que eu notei?"** + **"Por que isso importa?"**

---

## 🚨 Situações Críticas de Logging

### 😕 Usuário não sabe responder

```markdown
| 2026-04-04 10:30 | ❓ Pergunta    | Qual banco de dados será utilizado?                        |
| 2026-04-04 10:31 | 💬 Resposta    | Usuário não tem preferência definida                       |
| 2026-04-04 10:31 | 💡 Observação  | Lacuna: banco de dados indefinido. Apresentadas opções:    |
|                  |                | PostgreSQL (relacional), MongoDB (documento), MySQL.       |
|                  |                | Usuário pediu tempo para consultar o tech lead.            |
| 2026-04-04 10:32 | ⏸️ Pausa       | Aguardando definição de banco de dados com tech lead       |
```

### 🔄 Usuário muda de ideia

```markdown
| 2026-04-04 10:30 | ⚠️ Decisão     | Usuário inicialmente definiu PostgreSQL como banco         |
| 2026-04-04 11:00 | ⚠️ Decisão     | Usuário altera decisão: MySQL ao invés de PostgreSQL.      |
|                  |                | Motivo: equipe tem mais experiência com MySQL.             |
| 2026-04-04 11:01 | 💡 Observação  | Impacto: fronteira de tecnologia precisa ser atualizada.   |
|                  |                | Verificar se visão do projeto referencia banco específico. |
```

### 🚫 Conflito identificado

```markdown
| 2026-04-04 10:30 | 🚫 Conflito    | Orçamento de R$2k/mês incompatível com                     |
|                  |                | arquitetura de 10 microsserviços (decisão da Fase 3). |
|                  |                | Estimativa mínima: R$8k/mês para essa arquitetura na AWS. |
| 2026-04-04 10:35 | 💬 Resposta    | Usuário opta por monolito modular para caber no orçamento |
| 2026-04-04 10:36 | ✅ Resolução   | Conflito resolvido: arquitetura alterada para monolito     |
|                  |                | modular. Fronteira de orçamento mantida. Visão do projeto  |
|                  |                | será ajustada.                                              |
```

---

## 📏 Regra de Imutabilidade

> [!danger] Append-only
> O log é **append-only** — nunca editar ou remover entradas anteriores.

| Situação | O que fazer |
| -------- | ----------- |
| Informação estava errada | Adicionar nova entrada com a correção — não apagar a original |
| Decisão foi revertida | Adicionar nova entrada registrando a reversão e o motivo |
| Erro de digitação no log | Ignorar — o log não é documento formal, é registro operacional |

```markdown
❌ ERRADO — apagar entrada antiga:
(linha removida)

✅ CORRETO — adicionar correção:
| 2026-04-04 11:00 | ✅ Resolução | Correção: banco será PostgreSQL (não MySQL como     |
|                  |              | registrado em 10:30). Motivo: requisito de JSONB.   |
```

---

## 📊 Métricas do Log

Ao final de um processo, o log pode ser analisado para extrair métricas:

| Métrica | Como calcular | O que indica |
| ------- | ------------- | ------------ |
| ❓ Total de perguntas | Contar entradas tipo `❓` | Profundidade do questionário |
| 🚫 Total de conflitos | Contar entradas tipo `🚫` | Complexidade/incerteza do projeto |
| ⏸️ Total de pausas | Contar entradas tipo `⏸️` | Dependências externas, lacunas de conhecimento |
| ⚠️ Decisões alteradas | Contar mudanças de decisão | Maturidade do planejamento |
| ⏱️ Tempo por sub-etapa | Diferença entre `🎯 Início` e `🏁 Conclusão` | Onde o processo demora mais |
| 💡 Ratio observações/perguntas | Observações ÷ perguntas | Nível de análise da IA |

---

## 🔗 Documentos Relacionados

- [[docs/discovery-pipeline]] — Pipeline completo do discovery onde o logging se aplica
- `dtg-artifacts/rules/analyst-discovery-log/` — Regra formal do log de discovery
- `dtg-artifacts/rules/discovery/` — Processo de discovery em 3 fases
- Behavior principles — Princípios fundamentais (regra global do workspace)
- Markdown writing — Formato do changelog em cada documento (convenção global do workspace)

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-04 10:30 | Criação do documento |
| 01.01.000 | 2026-04-04 | Adição de 4 tipos de entrada para iterações do pipeline: Iteração, Perguntas enviadas, Respostas recebidas, Convergência |
| 01.02.000 | 2026-04-05 18:30 | Atualização terminologia v1 para v2: "Nível" e "Fase" substituídos por "Sub-etapa" em todo o documento |
| 01.03.000 | 2026-04-11 | Atualização de paths para nova estrutura de 3 camadas (base-artifacts, dtg-artifacts, custom-artifacts). Terminologia "Sub-etapa" substituída por "Fase" (v0.5). Wikilinks core/ atualizados para dtg-artifacts/rules/ |
