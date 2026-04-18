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

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com priority badges
**Tecnologia:** HTML/CSS
**Justificativa:** Epicos priorizados sao dados tabulares com multiplas dimensoes (prioridade, esforco, release) que se beneficiam de alinhamento em colunas. Badges coloridos por prioridade MoSCoW (Must=vermelho, Should=amarelo, Could=azul, Won't=cinza) tornam a leitura imediata sem sacrificar densidade informacional.
**Alternativa:** Kanban por release — quando a audiencia precisa de visao de roadmap agrupada por fase em vez de lista linear.
