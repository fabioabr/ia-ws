---
title: TODO
description: Lista de pendências do projeto Discovery To Go
project-name: discovery-to-go
version: 05.00.000
status: ativo
author: claude-code
category: todo
area: tecnologia
tags:
  - todo
  - pendencia
created: 2026-04-11
updated: 2026-04-11
---

# TODO — Discovery To Go

---

## Concluídos

<details>
<summary>Todos os itens concluídos (clique para expandir)</summary>

- ~~1. Consolidar packs no formato único~~ DONE
- ~~2. Sample run atualizado~~ DONE
- ~~3. Terminologia "context-template"~~ DONE
- ~~4. CLAUDE.md atualizado~~ DONE
- ~~5. .gitignore (draw.io temps)~~ DONE
- ~~6. product-discovery-deliverables.md~~ DONE
- ~~7. README.md atualizado~~ DONE
- ~~8. Information Regions (85 regions, previews, chart specialist)~~ DONE
- ~~9. Consolidator com regions~~ DONE
- ~~10. HTML Writer com regions~~ DONE
- ~~11. Sample run com regions~~ DONE
- ~~12. CLAUDE.md + chart-specialist~~ DONE
- ~~13. Sync base-artifacts~~ DONE
- ~~14. Teste end-to-end (Veezoozin)~~ DONE — com 11 problemas documentados
- ~~15. Report setups (essential/executive/complete)~~ DONE
- ~~16. Report Planner skill~~ DONE
- ~~17. quick-start.md com report setups~~ DONE
- ~~18. README.md seções atualizadas~~ DONE
- ~~READMEs em todas as subpastas (117)~~ DONE
- ~~Client template scaffold~~ DONE
- ~~Starter-kit com briefing template~~ DONE
- ~~Docs organizados (guides/ + reference/ + diagrams/)~~ DONE
- ~~Auditoria de consistência (10 issues corrigidas)~~ DONE
- ~~discovery-pipeline.md v02 (regions, 10 packs, report-planner)~~ DONE
- ~~Orchestrator: auto-detect + simulação de cliente~~ DONE

</details>

---

## Problemas do teste end-to-end (Veezoozin run-1)

Issues identificadas durante o primeiro pipeline completo. Organizadas por prioridade.

---

### P1. Orchestrator não é executável — scaffold manual

**Severidade:** Alta
**Fase:** Setup

O orchestrator é uma skill (instrução em SKILL.md), não código executável. O scaffold da run (pastas, cópias de templates, config.md, pipeline-state.md) foi criado manualmente via bash.

**Ação:**
- [ ] Criar um script Python ou bash (`scripts/create-run.sh`) que materializa o scaffold automaticamente
- [ ] Recebe: path do briefing + client name
- [ ] Cria: `custom-artifacts/{client}/runs/run-{n}/` com toda a estrutura
- [ ] Detecta context-templates do briefing e copia os blueprints
- [ ] Gera config.md e pipeline-state.md iniciais
- [ ] Documentar no quick-start.md

---

### P2. Interview.md não gerado

**Severidade:** Alta
**Fase:** Fase 1

O pipeline exige um log cronológico da entrevista (`interview.md`) com formato de tabela e emojis conforme a regra `analyst-discovery-log`. O teste pulou isso — os agentes geraram os results diretamente sem registrar o diálogo.

**Ação:**
- [ ] Cada agente da Fase 1 deve gerar um trecho de interview log
- [ ] Consolidar num único `iterations/iteration-{i}/logs/interview.md`
- [ ] Formato: tabela com colunas `Quem | Diálogo` e source tags

---

### P3. Scores abaixo do threshold — pipeline seguiu mesmo assim

**Severidade:** Alta
**Fase:** Fase 2 → Fase 3

O auditor deu 82% e o 10th-man deu 62%. O threshold padrão é ≥90%. O pipeline deveria ter parado para HR Review, mas seguiu direto para Fase 3 (porque o teste roda sem pausas).

**Ação:**
- [ ] Documentar no orchestrator que em modo simulação (`client-simulation: sim`), o pipeline registra o score mas avança com flag `[BELOW-THRESHOLD]`
- [ ] Em modo real (`client-simulation: não`), o pipeline DEVE pausar para HR Review quando score < threshold
- [ ] Gerar hr-loop-round{N}-pass{M}.md mesmo em modo simulação (com decisão automática "AVANÇAR — simulação")

---

### P4. Inconsistência financeira entre blocos 1.3 e 1.8

**Severidade:** Alta
**Fase:** Fase 1

ARR projetado diverge 2.6x entre blocos 1.3 (R$ 460K) e 1.8 ($32K USD). Break-even diverge de mês 3 para mês 14-18. Isso foi detectado pelo auditor mas não corrigido.

**Ação:**
- [ ] Adicionar regra no orchestrator: ao fim da Fase 1, validar consistência financeira entre blocos
- [ ] Se divergência > 20%, sinalizar automaticamente antes do HR Review
- [ ] Considerar cross-validation automática entre blocos como pré-check antes da Fase 2

---

### P5. Customer não operou como agente separado

**Severidade:** Média
**Fase:** Fase 1

O customer (simulador do cliente) deveria ser um agente independente respondendo perguntas dos especialistas (PO, architect, security). No teste, cada agente fez tudo sozinho — entrevistou e respondeu.

**Ação:**
- [ ] Na implementação real, o customer deve ser invocado como agente separado
- [ ] Fluxo: PO faz pergunta → customer responde com [BRIEFING]/[INFERENCE] → PO analisa
- [ ] Em modo simulação, o customer pode rodar inline mas deve gerar respostas tagueadas

---

### P6. Agentes não consultaram discovery-blueprints

**Severidade:** Média
**Fase:** Fase 1

Os 3 blueprints (saas, ai-ml, datalake-ingestion) foram copiados para `current-context/` mas os agentes não os leram. Trabalharam apenas com o briefing.

**Ação:**
- [ ] O orchestrator deve instruir cada agente a ler os blueprints antes de iniciar o bloco
- [ ] O blueprint tem a seção de componentes específicos do domínio — deve guiar as perguntas
- [ ] Incluir path dos blueprints no prompt de cada agente

---

### P7. HR Review logs não gerados

**Severidade:** Média
**Fase:** Entre fases

Os arquivos `hr-loop-round{N}-pass{M}.md` não foram gerados. Em modo simulação, deveriam ser criados com decisão automática.

**Ação:**
- [ ] Gerar `hr-loop-round1-pass1.md` após Fase 1 (simulado: "AVANÇAR — simulação")
- [ ] Gerar `hr-loop-round2-pass1.md` após Fase 2 (simulado, com nota do flag [BELOW-THRESHOLD])
- [ ] Gerar `hr-loop-round3-pass1.md` após Fase 3

---

### P8. md-writer (Fase 3.1) foi pulado

**Severidade:** Média
**Fase:** Fase 3

O pipeline-md-writer deveria rodar antes do consolidator para polir os drafts. No teste, o consolidator leu os results brutos diretamente.

**Ação:**
- [ ] Incluir passo 3.1 (md-writer) na execução — polir os 8 drafts antes de consolidar
- [ ] Gerar arquivos intermediários em `delivery/intermediate/` ou manter em results/
- [ ] Consolidator deve ler os drafts polidos, não os brutos

---

### P9. Path das runs não documentado

**Severidade:** Baixa
**Fase:** Estrutura

As runs ficam em `custom-artifacts/{client}/runs/run-{n}/` mas isso não está documentado em nenhum lugar. O quick-start e o README referenciam `runs/run-{n}/` genérico.

**Ação:**
- [ ] Documentar no quick-start.md que runs ficam dentro da pasta do cliente
- [ ] Atualizar README.md com o path correto
- [ ] Atualizar orchestrator SKILL.md com o path

---

### P10. config.md não puxa report-setup automaticamente

**Severidade:** Baixa
**Fase:** Setup

O campo `report-setup: executive` do briefing não foi automaticamente copiado para o config.md — foi preenchido manualmente.

**Ação:**
- [ ] Script de scaffold (P1) deve ler o frontmatter do briefing e copiar `report-setup` para config.md
- [ ] Mesmo para `context-templates`, `client-simulation`, `scoring-threshold`

---

### P11. pipeline-state.md não atualizado ao longo do pipeline

**Severidade:** Baixa
**Fase:** Todas

O pipeline-state.md foi criado no setup mas não foi atualizado com snapshots após cada fase (como o pipeline exige — append-only).

**Ação:**
- [ ] Após cada fase, appendar snapshot com: status, scores, decisão do HR, tokens consumidos
- [ ] No final, appendar snapshot de conclusão com resultado final

---

## Ordem sugerida de resolução

```
P1 (scaffold script)     ← desbloqueia tudo
 ↓
P2 (interview.md)        ← Fase 1 completa
P5 (customer separado)   ← Fase 1 fiel ao pipeline
P6 (blueprints lidos)    ← Fase 1 com contexto
 ↓
P4 (cross-validation)    ← entre Fase 1 e 2
P3 (threshold + HR logs) ← Fase 2 com gates
P7 (HR loop logs)        ← entre fases
 ↓
P8 (md-writer 3.1)       ← Fase 3 completa
 ↓
P9-P11 (docs + config)   ← polish final
```
