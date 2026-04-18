---
region-id: REG-EXEC-01
title: "Overview One-Pager"
group: executive
description: "Resumo executivo de 1 página: problema, proposta, stakeholders, decisões técnicas, esforço/custo/escopo, top 3 riscos, Build vs Buy, próximo passo"
source: "Consolidator"
schema: "text"
template-visual: "Hero card full-width"
default: true
deliverable-scope: ["OP", "EX", "DR"]
---

# Overview One-Pager

Resumo executivo condensado em uma única página, projetado para decisores que precisam de visão completa em poucos minutos. Apresenta o problema, a solução proposta, os principais stakeholders, as decisões técnicas estruturantes, o esforço/custo/escopo projetado, os três maiores riscos e a recomendação final de Build vs Buy. Serve como documento de referência rápida para reuniões de comitê e aprovações executivas.

> [!info] Relação com o entregável One-Pager (ADR-001)
> Esta region **não é** o entregável **One-Pager (OP)** por si só — é **um dos componentes** do layout do OP (ver [one-pager-layout.md](../../../../../../standards/conventions/layouts/one-pager-layout.md) quando criado na task #17). O OP completo é produzido pelo `deliverable-distiller` (task #16) a partir do Delivery Report. A classificação `deliverable-scope: ["OP", "EX", "DR"]` indica que esta region está presente em todos os três entregáveis.

> [!warning] Campos condicionais às flags do briefing
> - `tco_resumo` é substituído por `estimativa_consumo` quando `financial_model=fundo-global` no briefing (ver [start-briefing.md](../../../../../../starter-kit/client-template/projects/project-n/setup/start-briefing.md)).
> - `roi_resumo` só aparece quando `require_roi=true`. Por padrão (`require_roi=false`), **não inclua** justificativa de ROI/payback neste resumo — o OP do Discovery-to-Go foca em **esforço/custo/escopo**, não em justificativa de retorno.

## Schema de dados

| Campo | Tipo | Formato | Condicional |
|-------|------|---------|-------------|
| problema | string | 1-2 parágrafos narrativos descrevendo o problema e seu impacto | sempre |
| proposta | string | 1 parágrafo com a solução recomendada | sempre |
| stakeholders | list | Nomes e papéis dos stakeholders-chave (sponsor, PM, tech lead) | sempre |
| decisoes_tecnicas | list | 3-5 bullets com decisões arquiteturais estruturantes | sempre |
| tco_resumo | object | `{ total_3_anos: string, faixa: string, confianca: string }` | `financial_model=projeto-paga` |
| estimativa_consumo | object | `{ opex_cloud_anual: string, premissas: list, confianca: string }` | `financial_model=fundo-global` |
| roi_resumo | object | `{ payback_meses: string, vpl: string, premissas: list }` | `require_roi=true` |
| top_3_riscos | list | Cada item: `{ risco: string, severidade: string, mitigacao: string }` | sempre |
| build_vs_buy | object | `{ veredicto: string, justificativa: string }` | sempre |
| proximo_passo | string | Ação imediata recomendada com responsável e prazo | sempre |

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

<!-- Substituir por "Estimativa de consumo" quando financial_model=fundo-global:

### Estimativa de consumo cloud (anual)

**~R$ 380k/ano** OPEX cloud sem free tier. Premissas: 12 filiais, 500 usuários ativos, retenção 7 anos (regulatória). Confiança: média — depende de validação de volumetria real.
-->

<!-- Adicionar bloco "ROI resumido" apenas quando require_roi=true:

### ROI resumido

Payback estimado em 18 meses; VPL positivo de R$ 1,4M em 3 anos. Premissas: ganho de 12h/semana por analista × 8 analistas × R$ 120/h; evitação de 2 reapresentações/ano.
-->


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
