---
title: Delivery Report Structure — Default
description: Estrutura padrão do relatório consolidado gerado pelo consolidator na Fase 3 (Delivery). Define seções obrigatórias, overview one-pager e tom por seção. Seções extras por domínio estão nos report-profiles dos context-templates. Projetos podem copiar e customizar localmente em {projeto}/customization/.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: customization
area: tecnologia
tags:
  - customization
  - delivery
  - report
  - consolidator
  - pipeline-v05
created: 2026-04-10
---

# Delivery Report Structure — Default

> [!info] Como este arquivo é usado
> O `consolidator` lê este arquivo (ou a cópia local em `{projeto}/customization/`) para saber **como estruturar o `delivery-report.md` consolidado**. Se o arquivo não existir, o consolidator cai para o fallback hardcoded no próprio SKILL.md.
>
> **Prioridade:** `{projeto}/customization/delivery-report-structure.md` > `behavior/templates/customization/delivery-report-structure.md` > fallback do SKILL.md.

---

## 1. Seções obrigatórias do delivery-report.md

Toda execução do pipeline gera um `delivery-report.md` com **pelo menos** estas seções, nesta ordem:

| # | Seção | Tom | Audiência | Obrigatória? |
|---|---|---|---|---|
| 1 | **Overview (one-pager)** | Executivo — 1 página no máximo | C-level, sponsor, stakeholders | Sim |
| 2 | **Visão de Produto** | Híbrido (produto + negócio) | PO, sponsor | Sim |
| 3 | **Organização** | Processo/gestão | PO, RH, gerência | Sim |
| 4 | **Tecnologia e Segurança** | Técnico | Arquiteto, tech lead, devs | Sim |
| 5 | **Privacidade e Compliance** | Regulatório | DPO, jurídico, compliance | Sim |
| 6 | **Análise Estratégica** | Executivo-técnico | Sponsor, CTO | Sim |
| 7 | **Backlog Priorizado** | Operacional | PO, squad | Sim |
| 8 | **Matriz de Riscos** | Operacional | Todos os stakeholders | Sim |
| 9 | **Métricas-chave** | KPIs | PO, sponsor | Sim |
| 10 | **Questões residuais do Challenge** | Informativo | Sponsor, arquiteto | Sim |
| 11 | **Como chegamos aqui** | Narrativo | Todos | Sim |

---

## 2. Overview (one-pager) — elementos obrigatórios

O one-pager é a **seção mais importante** do relatório. Deve ser legível em ~1 minuto por alguém que nunca viu o projeto. Elementos obrigatórios:

- **Problema resolvido:** 1-2 frases
- **Proposta de valor:** 1-2 frases
- **Stakeholders-chave:** lista enxuta (nomes e papéis)
- **Decisões técnicas fundamentais:** 3-5 bullets (stack, arquitetura, integrações)
- **Custo estimado (TCO 3 anos):** número + faixa de sensibilidade
- **Riscos top 3:** bullets com impacto × probabilidade
- **Recomendação Build vs Buy:** frase objetiva com justificativa de 1 linha
- **Próximo passo concreto:** 1 ação com responsável

---

## 3. Tom e nível técnico por seção

| Seção | Tom | Nível técnico | Exemplo de linguagem |
|---|---|---|---|
| Overview | Executivo | Baixo | "O sistema reduzirá o tempo de onboarding em 60%" |
| Visão de Produto | Produto/negócio | Baixo-médio | "Persona primária: analista júnior que precisa de..." |
| Organização | Gestão | Baixo | "O time de 6 pessoas será estruturado em 2 squads" |
| Tech & Security | Técnico | Alto | "API Gateway com rate limiting por tenant via Kong" |
| Privacidade | Regulatório | Médio-alto | "Base legal: legítimo interesse (art. 7, IX LGPD)" |
| Análise Estratégica | Executivo-técnico | Médio | "Build: R$ 1.2M em 18 meses vs Buy: R$ 480K/ano" |
| Backlog | Operacional | Médio | "US-001: Como analista, quero filtrar por período..." |
| Riscos | Operacional | Médio | "R-001: Vendor lock-in AWS — impacto alto, probabilidade média" |
| Métricas | KPIs | Baixo | "MRR alvo: R$ 50K em 6 meses pós-launch" |
| Questões residuais | Informativo | Variável | "10th-man: Build vs Buy não avaliou alternativa X" |
| Como chegamos aqui | Narrativo | Baixo | "Em 3 iterações, o discovery convergiu após..." |

---

## 4. Report Profiles por Context-Template

Seções extras, métricas obrigatórias, diagramas e ênfases específicas de cada domínio estão definidas nos **report-profiles** dos context-templates — não mais neste template.

O consolidator faz merge na seguinte ordem de prioridade:

```
1. Template base (este arquivo) → 11 seções obrigatórias + regras de tom/formato
2. report-profile.md do pack carregado → seções extras, métricas, diagramas, ênfases
3. Override total do cliente (se existir) → substitui tudo acima
```

| Context-Template | Report Profile |
|---------------|----------------|
| saas | `context-templates/saas/report-profile.md` |
| datalake-ingestion | `context-templates/datalake-ingestion/report-profile.md` |
| process-documentation | `context-templates/process-documentation/report-profile.md` |
| web-microservices | `context-templates/web-microservices/report-profile.md` |
| genérico (sem pack) | Sem report-profile — usa apenas as 11 seções base |

> [!info] Override total pelo cliente
> Se o cliente tiver `custom-artifacts/{client}/config/final-report-template.md`, o consolidator ignora tanto este template base quanto o report-profile — usa exclusivamente o template do cliente.

---

## 5. Formato de priorização do Backlog

O consolidator escolhe o formato de priorização com base no briefing e no tipo de projeto:

| Formato | Quando usar | Estrutura |
|---|---|---|
| **MoSCoW** | Projetos com stakeholders não-técnicos que precisam entender prioridades facilmente | Must / Should / Could / Won't |
| **RICE** | Projetos com dados suficientes para quantificar Reach, Impact, Confidence, Effort | Score RICE por item |
| **Weighted Shortest Job First (WSJF)** | Projetos SAFe/ágil scaled com CoD | Business Value / Time Criticality / Risk Reduction / Job Size |
| **Simples (Alta/Média/Baixa)** | POCs, MVPs muito pequenos | 3 faixas sem fórmula |

**Default:** MoSCoW (mais universal e legível).

---

## 6. Formato da Matriz de Riscos

| Formato | Estrutura |
|---|---|
| **Tabela 5×5** | Impacto (1-5) × Probabilidade (1-5) com heatmap |
| **Top 5 + mitigação** | Lista ranqueada dos 5 maiores riscos com plano de mitigação inicial |

**Default:** Top 5 + mitigação (mais prático e acionável).

---

## 7. Diagramas

O consolidator deve incluir diagramas Mermaid quando aplicável:

- **Arquitetura macro** (extraída de tech-and-security.md) — **obrigatória em todos os projetos**
- Diagramas adicionais por domínio são definidos no `report-profile.md` do context-template carregado

---

## Changelog

| Versão | Data | Descrição |
|---|---|---|
| 02.00.000 | 2026-04-11 | Migração de overrides por tipo de projeto para report-profiles nos context-templates. Template base mantém apenas as 11 seções universais. |
| 01.00.000 | 2026-04-10 | Versão inicial. Estrutura mínima de 11 seções, overrides por tipo de projeto, formatos de backlog e riscos. |
