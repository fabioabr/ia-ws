---
region-id: REG-BACK-01
title: "Prioritized Epics"
group: backlog
description: "Epics prioritized with MoSCoW/RICE including narrative and effort estimates"
source: "Consolidator"
schema: "Tabela (épico, narrativa, prioridade MoSCoW/RICE, estimativa)"
template-visual: "Table com priority badges"
default: true
---

# Prioritized Epics

Apresenta os epicos do backlog priorizados usando MoSCoW ou RICE, com narrativa de negocio e estimativa de esforco. Esta visao e o principal entregavel para o time de desenvolvimento, definindo o que construir primeiro e por que.

## Schema de dados

```yaml
prioritized_epics:
  method: string                 # MoSCoW ou RICE
  epics:
    - id: string                 # Identificador (ex: EP-01)
      name: string               # Nome do epico
      narrative: string          # Narrativa de negocio (1-2 frases)
      priority: string           # Must / Should / Could / Won't (MoSCoW) ou score numerico (RICE)
      effort: string             # T-shirt size
      target_release: string     # Release ou fase alvo
```

## Exemplo

| ID | Epico | Narrativa | Prioridade | Esforco | Release |
|----|-------|-----------|-----------|---------|---------|
| EP-01 | Onboarding e Auth | Permitir que PMEs se cadastrem e acessem o FinTrack Pro em menos de 3 minutos | Must | M | MVP |
| EP-02 | Dashboard Financeiro | Visao consolidada de fluxo de caixa, contas a pagar/receber e saldo | Must | L | MVP |
| EP-03 | Gestao de Assinaturas | Permitir escolha de plano, pagamento e upgrade/downgrade self-service | Must | M | MVP |
| EP-04 | Relatorios e Exportacao | Gerar relatorios financeiros em PDF para contabilidade e fiscalizacao | Should | S | v1.1 |
| EP-05 | Admin e Multi-tenancy | Painel administrativo com gestao de tenants, usuarios e permissoes | Should | XL | v1.1 |

## Representacao Visual

### Dados de amostra

```yaml
prioritized_epics:
  method: "MoSCoW"
  epics:
    - id: "EP-01"
      name: "Onboarding e Auth"
      priority: "Must"
      effort: "M"
      target_release: "MVP"
    - id: "EP-02"
      name: "Dashboard Financeiro"
      priority: "Must"
      effort: "L"
      target_release: "MVP"
    - id: "EP-03"
      name: "Gestao de Assinaturas"
      priority: "Must"
      effort: "M"
      target_release: "MVP"
    - id: "EP-04"
      name: "Relatorios e Exportacao"
      priority: "Should"
      effort: "S"
      target_release: "v1.1"
    - id: "EP-05"
      name: "Admin e Multi-tenancy"
      priority: "Should"
      effort: "XL"
      target_release: "v1.1"
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo narrativo descrevendo os epicos por ordem de prioridade, agrupados por release, com justificativa de priorizacao | Relatorios executivos, documentos de visao de produto |
| Tabela | Tabela com colunas ID, Epico, Narrativa, Prioridade, Esforco e Release (formato atual do Exemplo) | Revisao detalhada, planejamento de sprint, documentacao tecnica |
| Barras horizontais por prioridade | Grafico de barras horizontais com epicos no eixo Y, tamanho proporcional ao esforco, cor por prioridade MoSCoW | Visao rapida de distribuicao de esforco vs prioridade, comunicacao com stakeholders |
| Kanban por release | Colunas por release (MVP, v1.1, v1.2) com cards dos epicos contendo badge de prioridade e esforco | Planejamento de roadmap, visao de entrega por fase |
| Bubble chart | Bolhas posicionadas por prioridade (eixo X) e esforco (eixo Y), tamanho proporcional ao valor de negocio | Analise de trade-off prioridade vs esforco, decisoes de corte de escopo |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
