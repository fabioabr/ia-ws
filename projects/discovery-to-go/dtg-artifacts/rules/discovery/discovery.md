---
title: Discovery
description: Processo obrigatório de discovery em 3 fases sequenciais (Discovery, Challenge, Delivery) com Human Review entre cada fase
project-name: discovery-to-go
version: 04.00.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - discovery
  - pipeline-v05
  - human-review
  - reuniao-tematica
created: 2026-04-03 13:00
---

# Discovery

Processo obrigatório e sequencial de discovery que **antecede qualquer trabalho** em um novo projeto. O pipeline conduz o levantamento por **3 fases** (Discovery, Challenge, Delivery), cada uma seguida de um **Human Review** onde o humano decide se avança, repete ou aborta.

> [!danger] Regra fundamental
> **Nenhum projeto inicia sem completar as 3 fases com aprovação humana em cada uma.** Este processo é obrigatório e sequencial.

> [!info] Para o guia detalhado passo a passo, consulte [[docs/discovery-pipeline]]

---

## 🎯 Visão Geral das 3 Fases

```mermaid
flowchart LR
    S[Setup] --> R1[Fase 1\nDiscovery]
    R1 --> HR1[Human\nReview]
    HR1 --> R2[Fase 2\nChallenge]
    R2 --> HR2[Human\nReview]
    HR2 --> R3[Fase 3\nDelivery]
    R3 --> HR3[Human\nReview]
    HR3 --> END[Entrega]
```

| Fase | Nome | O que faz | Agentes | Output principal |
|------|------|-----------|---------|------------------|
| 1 | **Discovery** | Reunião conjunta temática com 8 blocos | customer, po, solution-architect, cyber-security-architect, custom-specialist | 5 drafts + interview.md |
| 2 | **Challenge** | Validação convergente + divergente em paralelo | auditor (#2.1), 10th-man (#2.2) | audit-report.md + challenge-report.md |
| 3 | **Delivery** | Documentação, consolidação e report HTML | pipeline-md-writer (#3.1), consolidator (#3.2), html-writer (#3.3) | delivery-report.md + delivery-report.html |

---

## 🔵 Fase 1 — Discovery (Reunião Conjunta Temática)

**Objetivo:** Levantar requisitos completos do projeto através de uma reunião simulada com **8 blocos temáticos**.

### Agentes

| Agente | Papel | Blocos |
|--------|-------|--------|
| **customer** | Simula o cliente, responde perguntas | Todos (interlocutor) |
| **po** | Product Owner — visão, personas, valor, organização | #1, #2, #3, #4 |
| **solution-architect** | Arquitetura, tecnologia, TCO | #5, #7, #8 |
| **cyber-security-architect** | Privacidade, segurança, compliance | #6 |
| **custom-specialist** | Especialista de domínio sob demanda | Quando solicitado |

### 8 Blocos Temáticos

| Bloco | Tema | Dono | O que levanta |
|-------|------|------|---------------|
| #1 | Visão e Propósito | po | Problema, publico-alvo, proposta de valor |
| #2 | Personas e Jornada | po | Perfis de uso, jornadas, dores |
| #3 | Valor Esperado / OKRs | po | Metricas, ROI, criterios de sucesso |
| #4 | Processo, Negocio e Equipe | po | Organizacao, stakeholders, equipe |
| #5 | Tecnologia e Seguranca | solution-architect | Stack, integracoes, seguranca |
| #6 | LGPD e Privacidade | cyber-security-architect | Dados pessoais, compliance, DPO |
| #7 | Arquitetura Macro | solution-architect | Padroes, camadas, escalabilidade |
| #8 | TCO e Build vs Buy | solution-architect | Custo total, alternativas, viabilidade |

### Outputs

| Arquivo | Autor |
|---------|-------|
| `iterations/iteration-{i}/results/1-discovery/1.1-purpose-and-vision.md` | po |
| `iterations/iteration-{i}/results/1-discovery/1.2-personas-and-journey.md` | po |
| `iterations/iteration-{i}/results/1-discovery/1.3-value-and-okrs.md` | po |
| `iterations/iteration-{i}/results/1-discovery/1.4-process-business-and-team.md` | po |
| `iterations/iteration-{i}/results/1-discovery/1.5-technology-and-security.md` | solution-architect |
| `iterations/iteration-{i}/results/1-discovery/1.6-privacy-and-compliance.md` | cyber-security-architect |
| `iterations/iteration-{i}/results/1-discovery/1.7-macro-architecture.md` | solution-architect |
| `iterations/iteration-{i}/results/1-discovery/1.8-tco-and-build-vs-buy.md` | solution-architect |
| `iterations/iteration-{i}/logs/interview.md` | orchestrator |

> [!info] Formato da entrevista
> O log da reuniao segue o formato definido em [[rules/analyst-discovery-log/analyst-discovery-log]]. Cada bloco tematico e registrado cronologicamente com dados marcados como `[BRIEFING]`, `[RAG]` ou `[INFERENCE]` para rastreabilidade.

---

## 🟡 Fase 2 — Challenge (Validacao Convergente + Divergente)

**Objetivo:** Validar a qualidade e robustez dos drafts produzidos na Fase 1.

### Agentes (em paralelo)

| Agente | Tipo | O que faz |
|--------|------|-----------|
| **auditor** | Convergente (#2.1) | Valida qualidade dos drafts contra 5 dimensoes com pisos minimos |
| **10th-man** | Divergente (#2.2) | Desafia premissas, busca pontos cegos. Pergunta-chave: "O que NAO foi feito e aceitavel?" |

> [!warning] Paralelo e independente
> Auditor e 10th-man rodam **ao mesmo tempo**, sem dependencia entre si. Ambos recebem os mesmos drafts e produzem relatorios independentes.

### Outputs

| Arquivo | Autor |
|---------|-------|
| `iterations/iteration-{i}/results/2-challenge/2.1-convergent-validation.md` | auditor |
| `iterations/iteration-{i}/results/2-challenge/2.2-divergent-validation.md` | 10th-man |

---

## 🟢 Fase 3 — Delivery (Documentacao + Consolidacao + Reports)

**Objetivo:** Transformar os drafts aprovados em documentos finais polidos e report HTML.

### Sub-fases sequenciais

| # | Sub-fase | Agente | Input | Output |
|---|----------|--------|-------|--------|
| 3.1 | Documents creation | pipeline-md-writer | Drafts aprovados | Markdown polido |
| 3.2 | Consolidation | consolidator | Markdown documents | delivery-report.md |
| 3.3 | Reports | html-writer | delivery-report.md | delivery-report.html |

### Outputs

| Arquivo | Descricao |
|---------|-----------|
| `delivery/delivery-report.md` | Relatorio consolidado final |
| `delivery/delivery-report.html` | Versao HTML auto-contida |

---

## 👤 Human Review

Apos **cada fase**, o pipeline pausa e apresenta o material ao humano para revisao. O humano preenche observacoes, responde perguntas em aberto, registra correcoes e marca uma das 4 decisoes:

| Opcao | Comportamento |
|-------|---------------|
| **Re-executar desde a 1a fase** (padrao) | Incorpora comentarios, cria nova iteracao (`iteration-{i+1}`), reinicia desde a Fase 1 mantendo historico |
| **Re-executar a ultima fase** | Incorpora comentarios, re-executa apenas a ultima fase dentro do mesmo round |
| **Avancar para a proxima fase** | Finaliza o round, gera memory file, avanca para a proxima fase |
| **Abortar** | Exige confirmacao com `@`. Se confirmado, encerra o pipeline |

> [!info] Comportamento padrao
> Se nenhuma opcao for marcada, o orchestrator assume **re-executar desde a 1a fase**. Em todos os cenarios a memoria persiste o que foi feito ate agora.

> [!tip] Template
> O formato completo do HR Loop esta em `templates/customization/human-review-template.md`.

---

## 🔄 Iteracoes

Quando o humano escolhe **re-executar desde a 1a fase**, o orchestrator cria uma nova iteracao:

```
runs/run-{n}/
├── iterations/
│   ├── iteration-1/     ← primeira tentativa (historico preservado)
│   │   ├── logs/
│   │   └── results/
│   │       ├── 1-discovery/
│   │       ├── 2-challenge/
│   │       └── 3-delivery/
│   ├── iteration-2/     ← segunda tentativa (herda results da anterior)
│   │   ├── logs/
│   │   └── results/
│   └── iteration-3/     ← terceira tentativa
```

### Regras de iteracao

- Results **nao-afetados** sao herdados da iteracao anterior (copia direta)
- Results **afetados** pelos comentarios do humano sao regenerados
- Snapshots no `pipeline-state.md` sao **imutaveis** — append-only, nunca editados
- Cada iteracao tem seus proprios `logs/` e `results/`
- O `pipeline-state.md` e atualizado continuamente com tracking de tokens por fase/iteracao
- Limites de iteracoes configurados em `setup/customization/rules/iteration-policy.md`

---

## 🗂️ Estrutura no Projeto

```
runs/run-{n}/
├── pipeline-state.md                         ← estado + snapshots (append-only)
├── setup/
│   ├── briefing.md                           ← input do humano
│   ├── config.md                             ← configuração da run
│   └── customization/
│       ├── current-context/                  ← context-template copiado
│       │   ├── {pack}.md
│       │   └── {pack}-specialists.md
│       ├── report-templates/                 ← templates de output
│       │   ├── final-report-template.md
│       │   └── human-review-template.md
│       └── rules/                            ← políticas da run
│           ├── iteration-policy.md
│           └── scoring-thresholds.md
├── iterations/
│   └── iteration-{i}/
│       ├── logs/
│       └── results/
│           ├── 1-discovery/
│           ├── 2-challenge/
│           └── 3-delivery/
└── delivery/
```

---

## 💰 Orcamento e Output, nao Input

> [!danger] Regra sobre orcamento
> O discovery **NAO parte de orcamento pre-definido**. O processo **CALCULA** o custo total como resultado.
>
> - Fase 1 (blocos #1 a #4): NAO perguntar "qual o orcamento?" — focar em escopo e necessidades
> - Fase 1 (blocos #5 a #7): Definir o que e NECESSARIO, nao o que cabe no orcamento
> - Fase 1 (bloco #8): Arquiteto CALCULA o TCO baseado nas decisoes anteriores
>
> **Prazo fixo:** 1 mes de planejamento + 6 meses de desenvolvimento MVP.

---

## 📦 Context-Templates

O pipeline usa context-templates globais (em `context-templates/` na raiz do workspace):

| Pack | Quando usar |
|------|-------------|
| `saas` | Projetos SaaS multi-tenant |
| `datalake-ingestion` | Pipelines de dados / ETL |
| `process-documentation` | Documentacao de processos existentes |
| `web-microservices` | Aplicacoes web com microservicos |

Cada pack tem:
- `context.md` — concerns, perguntas recomendadas, checklist por bloco tematico
- `specialists.md` — catalogo de custom-specialists disponiveis para o dominio

O orchestrator auto-detecta o pack a partir de sinais no briefing. Se ambiguo, roda em modo generico.

---

## ✅ Criterio de Conclusao

O discovery so esta completo quando:

- [ ] Fase 1 — 8 result files (1.1 a 1.8) + interview.md gerados, aprovados no Human Review
- [ ] Fase 2 — 2.1-convergent-validation.md + 2.2-divergent-validation.md gerados, aprovados no Human Review
- [ ] Fase 3 — delivery-report.md + delivery-report.html gerados, aprovados no Human Review
- [ ] pipeline-state.md atualizado com tracking completo de todas as fases e iteracoes
- [ ] Todos os snapshots gerados em pipeline-state.md (após cada fase)

> [!tip] Apos o discovery
> Com as 3 fases concluidas e aprovadas pelo humano, o projeto esta apto a iniciar.

---

## 🔗 Documentos Relacionados

- [[docs/discovery-pipeline]] — Guia detalhado passo a passo do Pipeline v0.5
- [[rules/iteration-loop/iteration-loop]] — Iteracoes, limites, criterios de convergencia
- [[rules/analyst-discovery-log/analyst-discovery-log]] — Log cronologico obrigatorio da reuniao tematica
- [[rules/audit-log/audit-log]] — Log de auditoria
- [[rules/requirement-priority/requirement-priority]] — Classificacao de requisitos
- [[rules/token-tracking/token-tracking]] — Rastreamento de tokens

## 📜 Historico de Alteracoes

| Versao | Timestamp | Descricao |
| ------ | --------- | --------- |
| 01.00.000 | 2026-04-03 13:00 | Criacao do documento |
| 02.00.000 | 2026-04-03 16:00 | Renomeacao de levantamento-de-projeto para discovery |
| 02.00.001 | 2026-04-04 09:30 | Atualizacao de wikilinks para nomes em ingles (naming-convention) |
| 02.01.000 | 2026-04-04 11:00 | Adicao de auditoria automatica pos-geracao em cada nivel, nomes de pastas em ingles |
| 02.02.000 | 2026-04-05 10:00 | Refatoracao: discovery.md como regra concisa, detalhes movidos para discovery-pipeline |
| 03.00.000 | 2026-04-05 | Pipeline v2: 3 niveis substituidos por 3 sub-etapas com mini-ciclos (PO → Arquiteto → Auditor → Challenger). Criterio de conclusao: nota >= 90% por sub-etapa. Orcamento como output calculado. Auditoria por sub-etapa (nao centralizada) |
| 03.00.001 | 2026-04-05 18:30 | Remocao de "Orcamento" da lista de categorias obrigatorias de fronteira (contradicao com pipeline-master e skills) |
| 04.00.000 | 2026-04-11 | Rewrite for Pipeline v0.5: 3 phases (Discovery, Challenge, Delivery), joint thematic meeting with 8 blocks, parallel auditor + 10th-man, new HR Review options, runs/run-{n} scaffold |
