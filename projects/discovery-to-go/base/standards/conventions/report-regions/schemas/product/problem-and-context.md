---
region-id: REG-PROD-01
title: "Problem and Context"
group: product
description: "Descrição do problema, quem sofre, impacto mensurável, tamanho do problema"
source: "Bloco #1 (po) → 1.1"
schema: "text"
template-visual: "Card com callout de métrica"
default: true
---

# Problem and Context

Descrição detalhada do problema que o projeto resolve, incluindo quem é afetado, qual o impacto mensurável no negócio e qual o tamanho da oportunidade. Esta region estabelece o "porquê" do projeto e serve como âncora para todas as decisões de produto e arquitetura. Um problema bem definido com métricas de impacto claras é o fundamento para justificar investimento e priorizar escopo.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| contexto | string | 1-2 parágrafos sobre o cenário atual e como o problema surgiu |
| problema | string | 1-2 parágrafos descrevendo a dor específica |
| quem_sofre | list | Perfis afetados e como são impactados |
| impacto | object | `{ metrica: string, valor_atual: string, valor_desejado: string, unidade: string }` |
| tamanho_problema | string | Dimensionamento do problema (horas perdidas, receita em risco, etc.) |

## Exemplo

```markdown
## Problema e Contexto

### Contexto

A Acme Corp opera com 12 filiais em 4 países da América Latina. Cada filial utiliza uma instância local do SAP R/3 para contabilidade, gerando dados financeiros em moedas e planos de contas diferentes. A consolidação financeira é realizada mensalmente pela equipe do controller para produzir o balanço consolidado do grupo.

### Problema

O processo de consolidação é inteiramente manual: analistas financeiros exportam dados de cada instância SAP via planilhas, aplicam regras de conversão cambial e eliminação intercompany manualmente, e consolidam em uma planilha-mestre. O processo é lento, propenso a erros e não oferece rastreabilidade para auditoria.

### Quem sofre

- **Analistas financeiros (4 pessoas):** gastam 12h/semana cada em trabalho manual repetitivo e de baixo valor
- **Controller:** não consegue fechar o mês antes de D+8, impactando a tomada de decisão do C-level
- **CFO:** já precisou reapresentar relatórios ao conselho 3 vezes por erros na consolidação
- **Auditores:** não têm trilha de auditoria — cada revisão exige reconstrução manual do cálculo

### Impacto mensurável

> **2.500 horas/ano** desperdiçadas em trabalho manual de consolidação
> **3 reapresentações** ao conselho nos últimos 6 meses por erros materiais
> **D+8** para fechamento mensal (mercado pratica D+2 a D+3)

### Tamanho do problema

Considerando o custo médio por hora dos analistas (R$ 120/h), o desperdício direto é de ~R$ 300K/ano. Somando o risco reputacional das reapresentações e o custo de oportunidade do fechamento tardio, o impacto total estimado é de R$ 500K-700K/ano.
```

## Representação Visual

### Dados de amostra

- **Horas desperdiçadas:** 2.500 horas/ano em consolidação manual
- **Reapresentações ao conselho:** 3 nos últimos 6 meses
- **Tempo de fechamento:** D+8 (benchmark de mercado: D+2 a D+3)
- **Impacto financeiro:** R$ 500K-700K/ano (direto + risco + custo de oportunidade)
- **Perfis afetados:** 4 analistas (12h/semana cada), 1 controller, 1 CFO, auditores

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com métrica destacada
**Tecnologia:** HTML/CSS
**Justificativa:** Os dados são narrativos com 3-4 KPIs de impacto isolados (horas, reapresentações, D+N, custo). Um card com métricas em destaque (stat callout) comunica a gravidade do problema de forma imediata e impactante, sem necessidade de eixos ou comparações gráficas.
**Alternativa:** Gráfico de barras horizontais (Chart.js) — quando houver 4+ métricas com baseline vs. target numérico comparável e o público precisar visualizar a magnitude do gap.
