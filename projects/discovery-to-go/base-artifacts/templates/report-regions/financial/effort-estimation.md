---
region-id: REG-FIN-05
title: "Effort Estimation"
group: financial
description: "T-shirt sized effort estimates per epic with complexity and assumptions"
source: "Bloco #8 (arch) → 1.8"
schema: "Tabela (épico, complexidade, estimativa T-shirt, premissas)"
template-visual: "Table com badges"
default: true
---

# Effort Estimation

Apresenta a estimativa de esforco por epico usando sizing T-shirt (XS a XL), acompanhada da complexidade tecnica e premissas relevantes. Essa abordagem de alto nivel e adequada para a fase de discovery, onde estimativas detalhadas nao sao viaveis nem desejadas.

## Schema de dados

```yaml
effort_estimation:
  epics:
    - id: string                 # Identificador do epico (ex: EP-01)
      name: string               # Nome do epico
      complexity: string         # Baixa / Media / Alta / Muito Alta
      tshirt_size: string        # XS / S / M / L / XL
      estimated_sprints: string  # Faixa (ex: "2-3 sprints")
      assumptions: string[]      # Premissas para esta estimativa
  total_sprints_range: string    # Faixa total estimada
  team_composition: string       # Composicao de time assumida
```

## Exemplo

| Epico | Complexidade | T-Shirt | Sprints | Premissas |
|-------|-------------|---------|---------|-----------|
| EP-01: Onboarding e Auth | Media | M | 2-3 | Auth0 como IdP; fluxo social login |
| EP-02: Dashboard Financeiro | Alta | L | 3-4 | Integracao com Open Finance; cache agressivo |
| EP-03: Gestao de Assinaturas | Media | M | 2-3 | Stripe como gateway; 3 planos fixos |
| EP-04: Relatorios e Exportacao | Baixa | S | 1-2 | PDF server-side; templates pre-definidos |
| EP-05: Admin e Multi-tenancy | Muito Alta | XL | 4-6 | Isolamento por schema; RBAC granular |

**Total estimado:** 12-18 sprints (6-9 meses com sprints de 2 semanas)

**Time assumido:** 2 devs backend, 1 dev frontend, 1 QA, 1 PO (parcial)
