---
title: Requirement Priority
description: Regra de classificação e priorização de requisitos baseada na intenção e ênfase do solicitante
project-name: global
version: 01.00.002
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - requisito
  - priorizacao
  - discovery
created: 2026-04-04 17:00
---

# 🎯 Requirement Priority

Regra que define como a IA deve **identificar, classificar e priorizar** requisitos durante o processo de discovery, garantindo que o **requisito principal do solicitante nunca seja ignorado ou rebaixado**.

> [!danger] Regra fundamental
> A IA **nunca pode reclassificar** um requisito que o solicitante expressa como essencial para uma feature futura ou secundária. Se a solução proposta não atende o requisito principal, a solução está **errada** — não o requisito.

---

## 🔍 Como Identificar o Requisito Principal

O solicitante nem sempre diz "este é o requisito mais importante". Ele comunica prioridade de formas indiretas:

### 📋 Sinais de requisito mandatório

| Sinal | Exemplo | Classificação |
| ----- | ------- | ------------- |
| 🔥 **Ênfase emocional** | "Seria um sonho", "O mais importante é...", "Se pudesse..." | 🔴 **Mandatório** |
| 😤 **Dor explícita** | "Leva 3 dias", "Perdi dinheiro com isso", "Estou cansado de..." | 🔴 **Mandatório** |
| 🔄 **Repetição** | Solicitante menciona o mesmo ponto mais de uma vez durante o discovery | 🔴 **Mandatório** |
| ☝️ **Priorização direta** | "O mais importante é X", "Sem isso não faz sentido" | 🔴 **Mandatório** |
| 💡 **Descrição do resultado ideal** | "Quero que qualquer pessoa consiga...", "Imagino um sistema que..." | 🟡 **Importante** — validar se é mandatório |
| 🤔 **Menção casual** | "Seria legal se...", "Talvez no futuro..." | 🟢 **Desejável** |

> [!warning] Atenção
> Quando o solicitante descreve o **problema principal** usando termos emocionais ou de frustração, a solução para aquele problema específico é **mandatória por definição**. Não é negociável, não é "fase futura".

---

## ❌ O Anti-Padrão: Traduzir o Pedido para o Que Você Conhece

> [!danger] Proibido
> A IA **não pode** traduzir o pedido do solicitante para uma solução diferente que ela conhece melhor.

| O solicitante pediu | IA traduziu como | Problema |
| ------------------- | ---------------- | -------- |
| "Perguntar em linguagem natural e receber resposta visual" | "Dashboards com filtros" | ❌ **Solução diferente do pedido** — dashboard com filtro NÃO é linguagem natural |
| "Sistema que avisa antes do contrato vencer" | "Relatório mensal de contratos" | ❌ **Solução passiva** — o pedido era por alerta ativo |
| "Qualquer pessoa consiga usar sem treinamento" | "Interface técnica com manual de 50 páginas" | ❌ **Ignora o requisito de simplicidade** |

### ✅ O que a IA deve fazer

```
Solicitante: "Se pudesse mandar uma pergunta em texto
             normal e receber a resposta visual, seria um sonho"
        │
        ▼
🤖 IA identifica:
   - Sinal: ênfase emocional ("seria um sonho") = 🔴 MANDATÓRIO
   - Requisito: input em linguagem natural → output visual
   - Classificação: REQUISITO PRINCIPAL
        │
        ▼
🤖 IA avalia soluções CONTRA o requisito principal:
   - Power BI + filtros → ❌ NÃO atende (não é linguagem natural)
   - Power BI Q&A → ⚠️ Parcial (funciona mal em pt-BR)
   - Solução com NLP customizado → ✅ Atende
   - Metabase + plugin NLP → ⚠️ Parcial
        │
        ▼
🤖 Se nenhuma solução atende 100%:
   INFORMAR o solicitante ANTES de propor a solução:
   "Seu requisito principal é X. A solução Y atende Z%.
    Quer aceitar essa limitação ou explorar alternativas?"
```

---

## 📋 Classificação Obrigatória

Durante a Fase 1 do discovery (reunião conjunta temática, blocos #1-#4 conduzidos pelo po), a IA **deve** classificar explicitamente os requisitos:

```markdown
## 🎯 Classificação de Requisitos

| # | Requisito | Sinal | Classificação | A solução atende? |
| - | --------- | ----- | ------------- | ------------------ |
| 1 | Linguagem natural para consultas | 🔥 "seria um sonho" | 🔴 Mandatório | ✅/⚠️/❌ |
| 2 | Resposta visual (gráficos) | ☝️ "receber resposta visual" | 🔴 Mandatório | ✅/⚠️/❌ |
| 3 | Sem depender de TI | 😤 "leva 3 dias" | 🔴 Mandatório | ✅/⚠️/❌ |
| 4 | Dashboards para gerentes | 💡 "seria incrível" | 🟡 Importante | ✅/⚠️/❌ |
| 5 | Mobile | 🤔 "seria legal" | 🟢 Desejável | ✅/⚠️/❌ |
```

> [!danger] Regra de validação
> Se a solução proposta marca ❌ em **qualquer** requisito 🔴 Mandatório, a solução **deve ser revista**. Não é aceitável propor uma solução que não atende o requisito principal e empurrar para "fase futura".

---

## 🔄 Quando o Mandatório é Inviável

Se o requisito mandatório é **tecnicamente inviável** ou **financeiramente proibitivo**:

1. **Informar** o solicitante com transparência total
2. **Explicar** por que é inviável (com dados, não opinião)
3. **Apresentar alternativas** com % de atendimento
4. **Registrar** a decisão no log como ⚠️ Decisão
5. **O solicitante decide** — a IA não rebaixa o requisito sozinha

```
🤖 "Seu requisito principal é linguagem natural em português.
    A tecnologia atual atende isso parcialmente:
    - Opção A: 70% (funciona bem para perguntas simples)
    - Opção B: 90% (requer investimento adicional de R$X)
    - Opção C: 40% (dashboard com filtros — não é linguagem natural)

    Qual caminho prefere?"
```

> [!danger] Proibido
> A IA **nunca** rebaixa um requisito mandatório sem o consentimento **explícito** do solicitante. "Vamos colocar na Fase 3" sem o solicitante concordar é violação desta regra.

---

## 🔗 Documentos Relacionados

- [[core/discovery/discovery]] — Processo de discovery onde os requisitos são identificados
- [[core/behavior-principles/behavior-principles]] — Princípios fundamentais (não inferir, perguntar)
- [[core/project-boundaries/project-boundaries]] — Fronteiras que podem impactar viabilidade de requisitos

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-04 17:00 | Criação do documento |
| 01.00.001 | 2026-04-05 | Atualização terminologia v1 para v2: "Nível 1" substituído por "Sub-etapa 1" |
| 01.00.002 | 2026-04-11 | Pipeline v0.5: "Sub-etapa 1 do discovery (Visão do Produto)" → "Fase 1 do discovery (reunião conjunta temática, blocos #1-#4 conduzidos pelo po)" |
