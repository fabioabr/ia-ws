---
region-id: REG-BACK-03
title: "Dependencies"
group: backlog
description: "Dependency map between epics showing blocking and enabling relationships"
source: "Consolidator"
schema: "Tabela ou diagrama de dependências entre épicos"
template-visual: "Diagram ou table"
default: false
---

# Dependencies

Mapeia as dependencias entre epicos, identificando quais bloqueiam outros e quais podem ser executados em paralelo. Esta visao e essencial para o planejamento de releases e para evitar gargalos no desenvolvimento.

## Schema de dados

```yaml
dependencies:
  edges:
    - from: string               # Epico de origem (ex: EP-01)
      to: string                 # Epico dependente (ex: EP-02)
      type: string               # blocks / enables / recommends
      description: string        # Descricao da dependencia
  parallel_groups:
    - group: number              # Grupo de execucao paralela
      epics: string[]            # Epicos que podem rodar em paralelo
```

## Exemplo

| De | Para | Tipo | Descricao |
|----|------|------|-----------|
| EP-01 (Onboarding e Auth) | EP-02 (Dashboard) | blocks | Dashboard requer usuario autenticado e empresa configurada |
| EP-01 (Onboarding e Auth) | EP-03 (Assinaturas) | blocks | Gestao de assinatura requer tenant criado |
| EP-02 (Dashboard) | EP-04 (Relatorios) | enables | Relatorios consomem dados ja exibidos no dashboard |
| EP-01 (Onboarding e Auth) | EP-05 (Admin) | blocks | Admin gerencia tenants criados pelo onboarding |

**Grupos de execucao paralela:**
1. EP-01 (obrigatorio primeiro)
2. EP-02 + EP-03 (podem rodar em paralelo apos EP-01)
3. EP-04 + EP-05 (podem rodar em paralelo apos EP-02)

## Representacao Visual

### Dados de amostra

```yaml
dependencies:
  edges:
    - from: "EP-01"
      to: "EP-02"
      type: "blocks"
    - from: "EP-01"
      to: "EP-03"
      type: "blocks"
    - from: "EP-02"
      to: "EP-04"
      type: "enables"
    - from: "EP-01"
      to: "EP-05"
      type: "blocks"
  parallel_groups:
    - group: 1
      epics: ["EP-01"]
    - group: 2
      epics: ["EP-02", "EP-03"]
    - group: 3
      epics: ["EP-04", "EP-05"]
```

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela de dependencias
**Tecnologia:** HTML/CSS
**Justificativa:** Grafos direcionados sao visualmente ideais para dependencias, porem complexos de renderizar de forma confiavel em HTML estatico. Uma tabela com colunas De, Para, Tipo (com badges coloridos: blocks=vermelho, enables=azul) e grupos de execucao paralela listados abaixo entrega a mesma informacao de forma previsivel e acessivel.
**Alternativa:** Diagrama de swimlanes por grupo — quando houver suporte a bibliotecas de renderizacao SVG no pipeline de geracao.
