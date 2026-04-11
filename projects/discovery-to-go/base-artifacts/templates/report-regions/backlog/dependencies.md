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

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo descrevendo a sequencia de execucao, dependencias criticas e oportunidades de paralelismo | Relatorios executivos, comunicacao textual de planejamento |
| Tabela | Tabela com colunas De, Para, Tipo e Descricao (formato atual do Exemplo) | Documentacao tecnica, rastreamento formal de dependencias |
| Grafo direcionado / network diagram | Nos representando epicos, arestas direcionadas mostrando dependencias com cor por tipo (blocks=vermelho, enables=azul, recommends=cinza) | Visao principal de dependencias, planejamento de releases, identificacao de caminho critico |
| Diagrama de faixas (swimlane) por grupo | Faixas horizontais representando grupos de execucao paralela, com epicos posicionados em suas respectivas faixas | Planejamento de timeline, comunicacao de sequenciamento com o time |
| Gantt simplificado | Barras horizontais por epico com setas de dependencia, agrupadas por fase de execucao | Planejamento de cronograma, visao de sequenciamento temporal |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
