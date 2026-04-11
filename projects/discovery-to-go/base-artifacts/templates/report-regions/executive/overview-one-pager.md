---
region-id: REG-EXEC-01
title: "Overview One-Pager"
group: executive
description: "Resumo executivo de 1 página: problema, proposta, stakeholders, decisões técnicas, TCO, top 3 riscos, recomendação Build vs Buy, próximo passo"
source: "Consolidator"
schema: "text"
template-visual: "Hero card full-width"
default: true
---

# Overview One-Pager

Resumo executivo condensado em uma única página, projetado para decisores que precisam de visão completa em poucos minutos. Apresenta o problema, a solução proposta, os principais stakeholders, as decisões técnicas estruturantes, o custo total projetado, os três maiores riscos e a recomendação final de Build vs Buy. Serve como documento de referência rápida para reuniões de comitê e aprovações executivas.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| problema | string | 1-2 parágrafos narrativos descrevendo o problema e seu impacto |
| proposta | string | 1 parágrafo com a solução recomendada |
| stakeholders | list | Nomes e papéis dos stakeholders-chave (sponsor, PM, tech lead) |
| decisoes_tecnicas | list | 3-5 bullets com decisões arquiteturais estruturantes |
| tco_resumo | object | `{ total_3_anos: string, faixa: string, confianca: string }` |
| top_3_riscos | list | Cada item: `{ risco: string, severidade: string, mitigacao: string }` |
| build_vs_buy | object | `{ veredicto: string, justificativa: string }` |
| proximo_passo | string | Ação imediata recomendada com responsável e prazo |

## Exemplo

```markdown
## Overview One-Pager

### Problema

A área de consolidação financeira da Acme Corp opera com planilhas manuais distribuídas entre 12 filiais. Analistas financeiros gastam em média 12h/semana coletando, validando e consolidando dados — processo sujeito a erros que já causou 3 reapresentações ao conselho nos últimos 2 trimestres.

### Proposta

Plataforma SaaS de consolidação financeira automatizada (FinTrack Pro) que centraliza dados de todas as filiais, aplica regras de eliminação intercompany e gera relatórios consolidados em tempo real.

### Stakeholders-chave

- **Sponsor:** Maria Silva (CFO)
- **Product Owner:** João Santos (Controller)
- **Tech Lead:** Ana Costa (Head de Engenharia)

### Decisões técnicas estruturantes

- Arquitetura multi-tenant com isolamento por schema (PostgreSQL)
- API-first com integrações via REST + webhooks para ERPs existentes
- Deploy em AWS com IaC (Terraform) e CI/CD automatizado
- Autenticação via SSO corporativo (SAML 2.0)

### TCO projetado (3 anos)

**R$ 2,1M — R$ 2,8M** (confiança média-alta)

### Top 3 riscos

| Risco | Severidade | Mitigação |
|-------|-----------|-----------|
| Integração com ERP legado (SAP R/3) pode exigir middleware customizado | Alta | PoC de integração na Sprint 0 |
| Regulação contábil (IFRS 16) pode mudar regras de consolidação | Média | Módulo de regras configurável |
| Adoção pelos analistas — resistência a mudança de processo | Média | Programa de change management com champions por filial |

### Recomendação Build vs Buy

**Build customizado.** Soluções de mercado (Oracle HFM, SAP BPC) atendem parcialmente, mas o custo de licenciamento supera R$ 4M/3 anos e não cobre as regras específicas de eliminação intercompany da Acme.

### Próximo passo

Aprovar orçamento da Fase 1 (MVP) e iniciar Sprint 0 com PoC de integração SAP — responsável: Ana Costa, prazo: 15/05/2026.
```

## Representação Visual

### Dados de amostra

**Problema:** Consolidação manual de 12 filiais, 12h/semana, 3 erros em 2 trimestres
**Proposta:** FinTrack Pro — consolidação financeira automatizada (SaaS)
**Stakeholders:** 3 (CFO, Controller, Head de Engenharia)
**Decisões técnicas:** 4 (multi-tenant, API-first, AWS/IaC, SSO)
**TCO 3 anos:** R$ 2,1M — R$ 2,8M (confiança média-alta)
**Top riscos:** Integração SAP (Alta), Regulação IFRS (Média), Adoção (Média)
**Build vs Buy:** Build customizado
**Próximo passo:** Aprovar Fase 1 + Sprint 0 (PoC SAP)

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card layout com callout sections (hero card full-width com seções internas)
**Tecnologia:** HTML/CSS
**Justificativa:** O conteúdo é predominantemente narrativo e qualitativo — parágrafos, listas de stakeholders, bullets de decisões técnicas e recomendação textual. Não há série numérica que justifique gráfico; a melhor representação é um layout de cards com seções visuais (problema, proposta, TCO highlight, riscos, veredicto) usando tipografia hierárquica, bordas e ícones CSS.
**Alternativa:** Tabela comparativa (HTML/CSS) — quando o one-pager for comparado lado a lado com outros projetos em reunião de portfólio
