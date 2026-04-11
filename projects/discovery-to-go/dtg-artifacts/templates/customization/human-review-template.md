---
title: HR Loop Template — Default
description: Template da seção "Human Review" embutida ao fim de cada round do Discovery Pipeline. Define texto das perguntas, formato da pergunta objetiva, campos de observações e perguntas em aberto. Projetos podem customizar localmente.
project-name: global
version: 02.00.000
status: ativo
author: claude-code
category: customization
area: tecnologia
tags:
  - customization
  - hr-loop
  - human-review
  - iteration-control
  - pipeline-v05
created: 2026-04-10
---

# HR Loop Template — Default

> [!info] Como este arquivo é usado
> O `orchestrator` anexa esta seção ao fim do material entregue ao humano em **cada passagem do HR Loop**. O humano preenche as observações, responde perguntas em aberto e marca a decisão. Quando o documento volta, o orchestrator lê a decisão e age.
>
> O template abaixo é **a estrutura padrão**. Projetos podem editar a cópia local em `{projeto}/setup/customization/report-templates/human-review-template.md` para ajustar texto, perguntas ou formato.

---

## Template da seção Human Review

O orchestrator copia o bloco abaixo (entre as marcas `<!-- HR-LOOP-START -->` e `<!-- HR-LOOP-END -->`) para o fim de cada documento de round entregue ao humano.

<!-- HR-LOOP-START -->

---

## 🧑‍⚖️ Human Review — Round {N} (passagem {P})

> **Instruções:** preencha as seções abaixo e marque sua decisão no final. Ao devolver este documento ao orchestrator, ele vai ler sua decisão e agir.

### Observações gerais

*Espaço livre para registrar qualquer anotação sobre o material revisado. Pode ser curta ("tudo OK, sem observações") ou longa. Tudo que escrever aqui será incorporado como contexto se você pedir nova revisão.*

```
{suas observações aqui}
```

### Perguntas em aberto

*Perguntas que o material levantou e que precisam de resposta sua antes de avançar. O orchestrator preencheu as que detectou automaticamente. Você pode adicionar outras.*

❓ 1) {pergunta detectada pelo orchestrator}
   R. {sua resposta}

❓ 2) {pergunta detectada pelo orchestrator}
   R. {sua resposta}

### Correções pontuais

*Se você identificou erros específicos no material, liste aqui com referência exata (seção, parágrafo, frase).*

| # | Onde (seção/parágrafo) | O que está errado | O que deveria ser |
|---|---|---|---|
| 1 | {referência} | {erro} | {correção} |

### Decisão

> [!danger] Obrigatória — adicione seus comentários acima e marque uma opção abaixo.

- [ ] Re-executar desde a 1ª fase.
- [ ] Re-executar a última fase.
- [ ] Avançar para a próxima fase.
- [ ] Abortar — use `@` ao invés de `X` para confirmar.

> [!info] Em todos os cenários a memória persiste o que foi feito até agora. Se nenhuma opção for marcada, o orchestrator assume **re-executar desde a 1ª fase**.

**Se marcou Abortar, justifique:**

```
{justificativa}
```

<!-- HR-LOOP-END -->

---

## Notas para o orchestrator

### Como processar o retorno do humano

1. Leia a **Decisão** marcada
2. Se **Re-executar desde a 1ª fase** (ou nenhuma opção marcada — é o padrão):
   - Incorpore as observações, respostas e correções como contexto
   - Reinicie o pipeline desde a **Fase 1 (Discovery)**, mantendo todo o histórico
   - Crie nova iteração (`iteration-{i+1}`) herdando drafts da anterior
   - Registre a passagem em `logs/hr-loop-{round}-{pass}.md`
3. Se **Re-executar a última fase**:
   - Incorpore as observações, respostas e correções como contexto
   - Re-execute apenas a **última etapa executada** dentro do mesmo round
   - Mantenha o histórico — gere nova passagem (P+1)
   - Depende do round:
     - Round 1: reabre reunião parcialmente nos tópicos afetados
     - Round 2: reavalia gates com as observações como input adicional
     - Round 3: consolidator regenera `delivery-report.md` com as correções
   - Registre a passagem em `logs/hr-loop-{round}-{pass}.md`
4. Se **Avançar para a próxima fase**:
   - Finalize o round: appende snapshot em `pipeline-state.md`
   - Avance para o próximo round (ou encerre o pipeline se Round 3)
5. Se **Abortar**:
   - Verifique se o caractere marcado é `@`. Se não for `@`, **ignore a marcação** e apresente a decisão novamente ao humano, explicando que precisa usar `@` para confirmar
   - Se confirmado com `@`: compile change request formal, appende snapshot final em `pipeline-state.md`, e **encerre o pipeline**

### Campos dinâmicos

| Campo | Substituição |
|---|---|
| `{N}` | Número do round atual (1, 2 ou 3) |
| `{P}` | Número da passagem dentro do HR Loop (começa em 1, incrementa a cada re-execução) |
| Perguntas na tabela | Orchestrator auto-detecta perguntas em aberto a partir do material do round e preenche as linhas iniciais. Humano pode adicionar mais. |

---

## Changelog

| Versão | Data | Descrição |
|---|---|---|
| 01.00.000 | 2026-04-10 | Versão inicial. Template com observações, perguntas, correções e decisão (SIM/NÃO/HARD REJECT). |
| 02.00.000 | 2026-04-10 | Novas opções de decisão: REINICIAR (padrão), REFAZER, AVANÇAR, ABORTAR (com confirmação @). Substitui SIM/NÃO/HARD REJECT. |
