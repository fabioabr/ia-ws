---
title: "Política de sincronização Rule ↔ Guide"
description: "Como manter `rules/discovery/discovery.md` e `docs/guides/discovery-pipeline.md` consistentes"
project-name: discovery-to-go
version: "01.00.000"
status: "ativo"
created: 2026-04-17
---

# Política de Sincronização Rule ↔ Guide

Esta política vale para os pares de arquivos **rule-formal / guide-operacional** do Discovery-to-Go — notadamente:

- [base/behavior/rules/discovery/discovery.md](../../base/behavior/rules/discovery/discovery.md) (rule formal)
- [docs/guides/discovery-pipeline.md](discovery-pipeline.md) (guide operacional)

## Por que existem as duas

| Arquivo | Propósito | Audiência |
|---|---|---|
| **Rule** (`discovery.md`) | **Contrato prescritivo** — o que o pipeline **obrigatoriamente faz**, invariantes, flags, phase gates. Curto, denso, autoritativo. | Skills (`orchestrator`, `auditor`, `consolidator`) — leem como lei. Humanos que definem o framework. |
| **Guide** (`discovery-pipeline.md`) | **Manual operacional** — como executar o pipeline, exemplos, diagramas detalhados, fluxos, troubleshooting. Longo, didático, explicativo. | Humanos que usam o pipeline. Projetos que copiam templates. |

Os dois **sobrepõem conteúdo** (fases, skills, outputs) por design: a rule é o mínimo viável, o guide expande com contexto. Mas a informação **não pode divergir**.

## Regra principal

> **Ao editar um, atualize o outro no mesmo commit.**

Se você alterar conceitos que aparecem em ambos — lista de fases, skills, outputs, flags, context-templates, sub-fases — ambos os arquivos **devem** sair do commit consistentes. Um commit que atualiza apenas um dos dois é considerado **tecnicamente incompleto**.

## Tópicos com sobreposição (manter sincronizados)

Quando qualquer um destes for editado, verificar o outro arquivo:

| Tópico | Localização na rule | Localização no guide |
|---|---|---|
| Número e nomes das fases | início + tabela de fases | início + tabela de fases |
| Sub-fases da Fase 3 | seção "Fase 3 — Delivery" | seção "Fase 3 — Delivery" + diagrama mermaid |
| Lista de context-templates (packs) | seção "Context Templates" | seção "Context Templates" |
| Skills usadas em cada fase | tabela de fases | tabela de skills + diagramas |
| Outputs finais da Fase 3 | tabela de outputs | tabela de outputs |
| Flags do briefing (`financial_model`, `require_roi`, `deliverables_scope`) | seção "Flags de configuração" | menção operacional + exemplo |
| Human Review (opções) | seção "Human Review" | seção "Human Review" |

## Tópicos exclusivos (não sincronizar)

Nem tudo precisa existir nos dois. Cada arquivo tem exclusividades:

**Só na rule:**
- Histórico de versões da rule
- Regras invioláveis (quando falha = reprova)
- Cláusulas formais do contrato

**Só no guide:**
- Exemplos completos de briefing
- Diagramas mermaid de processo
- Troubleshooting e FAQs
- Explicações pedagógicas ("por que fazemos assim")

## Checklist antes do commit

Ao editar a rule ou o guide, percorrer mentalmente:

- [ ] O tópico editado aparece nos dois arquivos? Se sim, ambos foram atualizados?
- [ ] Se mudei a lista de fases/skills/outputs/flags, validei que os **números**, **nomes** e **ordem** batem exatamente?
- [ ] Se bumpei a versão da rule, adicionei entrada no histórico dela?
- [ ] O commit mensagem cita os dois arquivos quando houver sincronização?

## Responsabilidades por skill

| Skill | Quando deve revisitar esta política |
|---|---|
| Quem edita skills (`po`, `solution-architect`, etc.) | Se a mudança afeta sub-fases, outputs ou flags — sincronizar rule + guide |
| Quem edita regions ou templates | Se promover uma region para "obrigatória" em uma fase — sincronizar rule + guide |
| Quem edita o briefing template | Se adicionar/remover flag — sincronizar rule + guide + `starter-kit/client-template/projects/project-n/setup/start-briefing.md` |

## Em caso de divergência observada

Se você **ler** a rule e o guide e encontrar divergência:

1. Decidir qual é a verdade (geralmente a versão mais recente; em dúvida, abrir issue)
2. Atualizar o outro arquivo para refletir a verdade
3. Bumpar a versão da rule (patch) com uma nota no histórico: "sync rule ↔ guide em \<tópico\>"
4. Commit único com ambos

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 01.00.000 | 2026-04-17 | Criação — origem task #15 do TODO, após conflito de lista de context-templates descoberto na task #13 |
