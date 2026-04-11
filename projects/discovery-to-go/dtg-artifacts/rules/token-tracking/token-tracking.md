---
title: Token Tracking
description: Regra obrigatória de registro de consumo de tokens em todo processo executado por agentes de IA
project-name: global
version: 01.03.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - token
  - custo
  - rastreabilidade
created: 2026-04-04 18:00
---

# 📊 Token Tracking

Regra obrigatória que define o **registro de consumo de tokens** em todo processo executado por agentes de IA. O consumo de tokens é um indicador direto de **custo operacional** e deve ser rastreado para análise de eficiência e orçamento.

> [!danger] Regra inviolável
> **Todo log de processo DEVE registrar o consumo aproximado de tokens.** Sem este registro, não é possível avaliar o custo real de operar o pipeline.

---

## 📏 O que Registrar

| Métrica | Descrição | Formato |
| ------- | --------- | ------- |
| 🔢 **Total tokens** | Total de tokens consumidos pelo agente (input + output) | Número inteiro |
| 🔧 **Tool uses** | Quantidade de chamadas de ferramentas (reads, writes, edits, etc.) | Número inteiro |
| ⏱️ **Duração** | Tempo total de execução do agente | `Xmin Ys` ou `X.Xmin` |

---

## 📋 Onde Registrar

### Em logs de processo (discovery, auditoria, challenger, arquiteto)

Adicionar uma seção **📊 Consumo de Recursos** antes do Histórico de Alterações:

```markdown
## 📊 Consumo de Recursos

| Métrica | Valor |
| ------- | ----- |
| 🔢 **Total tokens** | ~XX.XXX |
| 🔧 **Tool uses** | XX |
| ⏱️ **Duração** | XX min |
| 📄 **Documentos gerados** | XX |
```

### Em relatórios consolidados (audit report, challenger report)

Adicionar na seção de execução/log:

```markdown
| Agente | Tokens | Tools | Duração | Docs |
| ------ | ------ | ----- | ------- | ---- |
| customer | ~XX.XXX | XX | XX min | XX |
| po | ~XX.XXX | XX | XX min | XX |
| solution-architect | ~XX.XXX | XX | XX min | XX |
| cyber-security-architect | ~XX.XXX | XX | XX min | XX |
| custom-specialist | ~XX.XXX | XX | XX min | XX |
| auditor | ~XX.XXX | XX | XX min | XX |
| 10th-man | ~XX.XXX | XX | XX min | XX |
| pipeline-md-writer | ~XX.XXX | XX | XX min | XX |
| consolidator | ~XX.XXX | XX | XX min | XX |
| html-writer | ~XX.XXX | XX | XX min | XX |
| **TOTAL** | **~XXX.XXX** | **XX** | **XX min** | **XX** |
```

### No discovery pipeline completo (Pipeline v0.5)

O `pipeline-state.md` deve conter o **consumo acumulado de todo o pipeline**, organizado por fase:

```markdown
## 📊 Consumo Total do Pipeline

| Fase | Agente(s) | Tokens | Duração |
| ---- | --------- | ------ | ------- |
| 1️⃣ Reunião conjunta (blocos #1-#4) | customer + po + solution-architect + cyber-security-architect + custom-specialist | ~XX.XXX | XX min |
| 2️⃣ Auditoria | auditor | ~XX.XXX | XX min |
| 3️⃣ 10th-man | 10th-man | ~XX.XXX | XX min |
| 4️⃣ Consolidação | consolidator + pipeline-md-writer + html-writer | ~XX.XXX | XX min |
| **TOTAL PIPELINE** | | **~XXX.XXX** | **XX min** |

> [!info] Custo estimado
> Com base no modelo [nome do modelo] a ~$X.XX/1M tokens:
> Input: ~XXX.XXX tokens × $X.XX = $X.XX
> Output: ~XXX.XXX tokens × $X.XX = $X.XX
> **Custo total estimado: $X.XX (~R$X.XX)**
```

---

## 💡 Por que Rastrear

| Motivo | Benefício |
| ------ | --------- |
| 💰 **Custo** | Saber quanto custa rodar o pipeline completo por projeto |
| 📊 **Eficiência** | Comparar consumo entre projetos — identificar desperdício |
| 📈 **Tendência** | Acompanhar se o consumo cresce ou diminui com melhorias no behavior |
| 🔍 **Debugging** | Identificar agentes que consomem tokens demais (possível loop ou ineficiência) |
| 💼 **Business case** | Justificar investimento em IA com dados reais de custo por discovery |

---

## 📏 Regras

- ✅ Todo log de agente **deve** ter a seção "Consumo de Recursos"
- ✅ O challenger report **deve** ter o consumo acumulado do pipeline
- ✅ Valores aproximados são aceitáveis (prefixar com `~`)
- ✅ Se o valor exato não estiver disponível, registrar como "não disponível" — nunca omitir a seção
- ❌ Não inventar números — se não sabe, diga que não sabe

---

## 📊 Dados Coletados

Dados reais de consumo de tokens coletados durante testes do pipeline:

| Processo | Projeto | Tokens | Tools | Duração |
|----------|---------|--------|-------|---------|
| Discovery (Fases 1-3) | natural-analytics | ~128k | 40 | ~16 min |
| Discovery (Fases 1-3) | consulting-erp | ~77k | 31 | ~8 min |
| Audit + Challenger | data-insights | ~145k | 35 | ~10 min |
| Pipeline completo (3 fases) | natural-analytics | ~128k + ~80k + ~145k = ~353k | ~115 | ~42 min |
| Challenger do behavior | global | ~131k | 45 | ~7 min |
| Report Maker (HTML) | natural-analytics | ~127k | 40 | ~19 min |

> [!info] Custo estimado
> Um pipeline completo consome aproximadamente 300-400k tokens. Com modelo Opus a ~$15/1M tokens input + $75/1M tokens output, o custo estimado por discovery completo é de $5-15.

---

## 🔗 Documentos Relacionados

- [[core/analyst-discovery-log/analyst-discovery-log]] — Log de discovery onde o consumo é registrado
- [[core/audit-log/audit-log]] — Log de auditoria onde o consumo é registrado
- [[core/behavior-principles/behavior-principles]] — Princípios de rastreabilidade

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-04 18:00 | Criação do documento |
| 01.01.000 | 2026-04-05 10:00 | Adição de seção "Dados Coletados" com consumo real de tokens dos testes do pipeline |
| 01.02.000 | 2026-04-05 | Pipeline v2: consumo agora por sub-etapa (não por fase). Tabela de pipeline reorganizada para 3 sub-etapas com mini-iterações |
| 01.03.000 | 2026-04-11 | Pipeline v0.5: agentes atualizados (customer, po, solution-architect, cyber-security-architect, custom-specialist, auditor, 10th-man, pipeline-md-writer, consolidator, html-writer). Tracker agora é process-map.md. Terminologia "sub-etapa" → "fase" |
