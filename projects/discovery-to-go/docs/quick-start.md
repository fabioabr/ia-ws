---
title: Quick Start
description: Guia passo a passo para iniciar um novo projeto no Discovery Pipeline v0.5 — do briefing ao delivery report
project-name: discovery-to-go
version: 03.00.000
status: ativo
author: claude-code
category: how-to
area: tecnologia
tags:
  - how-to
  - onboarding
  - guia
  - pipeline
created: 2026-04-10 12:00
---

# Quick Start

Como iniciar e conduzir um novo projeto no Discovery Pipeline v0.5, de ponta a ponta.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- [ ] Acesso ao workspace (`E:\Workspace`)
- [ ] O briefing do projeto pronto (pode ser rascunho — será refinado durante o processo)
- [ ] Definição de qual client/projeto será executado (nome, contexto)

---

## 🚀 Passo 1 — Criar o briefing

Crie um arquivo `briefing.md` com as informações iniciais do projeto. Use o template em `dtg-artifacts/templates/briefing-template.md` como base.

O briefing deve conter no mínimo:
- Nome do projeto
- Contexto / problema que resolve
- Público-alvo
- Expectativas de escopo (MVP, fases futuras)
- Restrições conhecidas (tecnologia, prazo, equipe)

> [!tip] O briefing não precisa ser perfeito
> O pipeline foi desenhado para extrair informações durante a Fase 1 (Discovery). O briefing é o ponto de partida, não o resultado final.

---

## 🚀 Passo 2 — Iniciar a run

Invoque o orchestrator passando o caminho do briefing:

```
/orchestrator briefing.md
```

O orchestrator vai:

1. **Criar a run** em `runs/run-{n}/` (número auto-incrementado)
2. **Copiar o briefing** para `setup/briefing.md`
3. **Detectar o knowledge pack** (saas, datalake, web-microservices, process-documentation ou genérico)
4. **Copiar customization defaults** de `dtg-artifacts/templates/customization/` para `setup/customization/`
5. **Criar o config.md** em `setup/` com plano de execução

Ao final do setup você verá:

```
runs/run-{n}/
├── pipeline-state.md
├── setup/
│   ├── briefing.md
│   ├── config.md
│   └── customization/
│       ├── current-context/
│       ├── report-templates/
│       └── rules/
├── iterations/
│   └── iteration-1/
│       ├── logs/
│       └── results/
└── delivery/
```

---

## 🔵 Passo 3 — Fase 1: Discovery

O orchestrator inicia a **reunião conjunta temática** com 8 blocos:

| Bloco | Tema | Quem conduz |
|-------|------|-------------|
| #1 | Visão e Propósito | po |
| #2 | Personas e Jornada | po |
| #3 | Valor Esperado / OKRs | po |
| #4 | Processo, Negócio e Equipe | po |
| #5 | Tecnologia e Segurança | solution-architect |
| #6 | LGPD e Privacidade | cyber-security-architect |
| #7 | Arquitetura Macro | solution-architect |
| #8 | TCO e Build vs Buy | solution-architect |

O **customer** (simulado) responde as perguntas de todos os especialistas, baseado no briefing + knowledge pack.

**Ao final da Fase 1 você terá:**
- 8 result files em `iterations/iteration-1/results/1-discovery/` (1.1 a 1.8)
- Log da entrevista em `iterations/iteration-1/logs/interview.md`
- State snapshot appendado em `pipeline-state.md`

---

## 👤 Passo 4 — Human Review (1ª pausa)

O pipeline **pausa** e apresenta o material para sua revisão. Você recebe um documento com:

1. **Observações gerais** — espaço para suas anotações
2. **Perguntas em aberto** — formato:
   ```
   ❓ 1) O projeto terá integração com SAP?
      R. {sua resposta aqui}
   ```
3. **Correções pontuais** — erros que você identificou
4. **Decisão** — marque uma opção:

```
- [ ] Re-executar desde a 1ª fase.
- [ ] Re-executar a última fase.
- [ ] Avançar para a próxima fase.
- [ ] Abortar — use '@' ao invés de 'X' para confirmar.
```

> [!info] Em todos os cenários a memória persiste o que foi feito até agora. Se nenhuma opção for marcada, o orchestrator assume **re-executar desde a 1ª fase**.

### O que acontece em cada decisão

| Decisão | O que acontece |
|---------|----------------|
| **Re-executar desde a 1ª fase** | Cria `iteration-2/`, incorpora seus comentários, roda tudo de novo desde o bloco #1 |
| **Re-executar a última fase** | Refaz apenas a Fase 1 com seus comentários, dentro da mesma iteração |
| **Avançar** | Material OK — segue para a Fase 2 (Challenge) |
| **Abortar** | Encerra o pipeline (requer `@` para confirmar) |

---

## 🟡 Passo 5 — Fase 2: Challenge

Se você avançou, o orchestrator dispara **em paralelo**:

- **auditor** — Validação convergente: verifica qualidade dos drafts contra 5 dimensões com pisos mínimos
- **10th-man** — Validação divergente: desafia premissas, busca pontos cegos, questiona o que NÃO foi feito

**Ao final da Fase 2 você terá:**
- `iterations/iteration-1/results/2-challenge/2.1-convergent-validation.md`
- `iterations/iteration-1/results/2-challenge/2.2-divergent-validation.md`
- State snapshot appendado em `pipeline-state.md`

---

## 👤 Passo 6 — Human Review (2ª pausa)

Mesmo formato do Passo 4. Revise os relatórios de auditoria e challenge, adicione comentários e escolha sua decisão.

---

## 🟢 Passo 7 — Fase 3: Delivery

Se você avançou, o orchestrator executa em sequência:

1. **pipeline-md-writer** — Transforma os drafts aprovados em markdown polido
2. **consolidator** — Consolida tudo em um delivery report único
3. **html-writer** — Gera a versão HTML do report

**Ao final da Fase 3 você terá:**
- `delivery/final-report.md`
- `delivery/final-report.html`
- State snapshot final appendado em `pipeline-state.md`

---

## 👤 Passo 8 — Human Review (3ª pausa)

Última revisão. Se avançar, o pipeline é **concluído** com sucesso.

---

## ✅ Resultado Final

Ao final de uma run bem-sucedida, sua estrutura será:

```
runs/run-{n}/
├── pipeline-state.md                         ← estado + snapshots (append-only)
├── setup/
│   ├── briefing.md                           ← input do humano
│   ├── config.md                             ← configuração da run
│   └── customization/
│       ├── current-context/                  ← knowledge pack copiado
│       │   ├── {pack}.md
│       │   └── {pack}-specialists.md
│       ├── report-templates/                 ← templates de output
│       │   ├── final-report-template.md
│       │   └── human-review-template.md
│       └── rules/                            ← políticas da run
│           ├── iteration-policy.md
│           └── scoring-thresholds.md
├── iterations/
│   └── iteration-{i}/                        ← (ou iteration-N se houve rework)
│       ├── logs/
│       │   ├── interview.md
│       │   └── hr-loop-round{N}-pass{M}.md
│       └── results/
│           ├── 1-discovery/                  ← 8 blocos (1.1 to 1.8)
│           │   ├── 1.1-purpose-and-vision.md
│           │   ├── 1.2-personas-and-journey.md
│           │   ├── 1.3-value-and-okrs.md
│           │   ├── 1.4-process-business-and-team.md
│           │   ├── 1.5-technology-and-security.md
│           │   ├── 1.6-privacy-and-compliance.md
│           │   ├── 1.7-macro-architecture.md
│           │   └── 1.8-tco-and-build-vs-buy.md
│           ├── 2-challenge/
│           │   ├── 2.1-convergent-validation.md
│           │   └── 2.2-divergent-validation.md
│           └── 3-delivery/
│               ├── 3.1-markdown-documents.md
│               ├── 3.2-consolidated-report.md
│               └── 3.3-delivery-reports.md
└── delivery/
    ├── final-report.md               ← relatório final
    └── final-report.html             ← versão HTML
```

---

## 🔧 Customização

### Antes de iniciar

Se o projeto tem necessidades específicas, edite os arquivos em `runs/run-{n}/setup/customization/` **antes** de iniciar a Fase 1:

| Arquivo | O que controla |
|---------|----------------|
| `rules/scoring-thresholds.md` | Pisos de nota do auditor e 10th-man por perfil (standard, poc, high-risk) |
| `rules/iteration-policy.md` | Máximo de iterações, threshold de estagnação |
| `report-templates/human-review-template.md` | Formato do Human Review apresentado a você |
| `report-templates/final-report-template.md` | Estrutura do relatório final |

### Overrides por cliente

Se o cliente já tem overrides definidos em `custom-artifacts/{client}/`, o orchestrator usa esses automaticamente no lugar dos defaults.

---

## ❓ Troubleshooting

| Problema | Solução |
|----------|---------|
| Pipeline não detectou o knowledge pack | Adicione `project-type: saas` (ou outro) no frontmatter do briefing |
| Notas baixas repetidas no Challenge | Verifique se o briefing tem informações suficientes; considere enriquecer com mais contexto |
| Pipeline parou sem Human Review | Verifique o `pipeline-state.md` — pode haver um erro registrado |
| Quer mudar customization mid-run | Edite os arquivos em `runs/run-{n}/setup/customization/` e re-execute |

---

## 🔗 Documentos Relacionados

- `docs/discovery-pipeline.md` — Guia detalhado do processo completo
- `docs/logging-process.md` — Como funciona o logging
- `dtg-artifacts/templates/briefing-template.md` — Template de briefing
- `dtg-artifacts/templates/customization/human-review-template.md` — Template do Human Review

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 01.00.000 | 2026-04-05 | Criação do documento |
| 02.00.000 | 2026-04-05 | Reescrita para Pipeline v2 |
| 03.00.000 | 2026-04-10 | Reescrita completa para Pipeline v0.5 — guia passo a passo de ponta a ponta com scaffold de runs, 3 fases, Human Review com 4 opções de decisão, knowledge packs globais |
