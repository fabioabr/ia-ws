---
region-id: REG-BACK-02
title: "High-Level Stories"
group: backlog
description: "User stories grouped by epic with acceptance criteria"
source: "Consolidator"
schema: "Lista agrupada por épico (US-NN: título + critérios)"
template-visual: "Accordion por épico"
default: false
---

# High-Level Stories

Detalha as user stories de alto nivel agrupadas por epico, cada uma com titulo e criterios de aceite. Este nivel de detalhe e suficiente para o time iniciar o refinamento sem ser prescritivo demais para a fase de discovery.

## Schema de dados

```yaml
high_level_stories:
  epics:
    - epic_id: string            # Referencia ao epico (ex: EP-01)
      epic_name: string
      stories:
        - id: string             # Identificador (ex: US-01)
          title: string          # Titulo da story no formato "Como... quero... para..."
          acceptance_criteria:
            - string             # Criterio de aceite
```

## Exemplo

### EP-01: Onboarding e Auth

- **US-01:** Como novo usuario, quero me cadastrar usando meu email ou conta Google para acessar o FinTrack Pro rapidamente
  - Cadastro com email + senha com validacao de forca
  - Login social com Google OAuth 2.0
  - Email de verificacao enviado em ate 30 segundos

- **US-02:** Como usuario cadastrado, quero configurar minha empresa no primeiro acesso para personalizar minha experiencia
  - Wizard de 3 passos: dados da empresa, regime tributario, integracao bancaria
  - Possibilidade de pular e completar depois
  - Dados salvos a cada passo (nao perde progresso)

### EP-02: Dashboard Financeiro

- **US-03:** Como gestor financeiro, quero ver meu fluxo de caixa dos ultimos 30 dias para entender minha situacao atual
  - Grafico de linha com entradas e saidas diarias
  - Saldo projetado para os proximos 7 dias
  - Filtro por conta bancaria

- **US-04:** Como gestor financeiro, quero ver contas a pagar e receber para planejar meu caixa
  - Lista com vencimento, valor e status (pago, pendente, atrasado)
  - Ordenacao por data de vencimento
  - Alerta visual para contas atrasadas

## Representacao Visual

### Dados de amostra

```yaml
high_level_stories:
  epics:
    - epic_id: "EP-01"
      epic_name: "Onboarding e Auth"
      stories:
        - id: "US-01"
          title: "Como novo usuario, quero me cadastrar usando meu email ou conta Google"
          acceptance_criteria_count: 3
        - id: "US-02"
          title: "Como usuario cadastrado, quero configurar minha empresa no primeiro acesso"
          acceptance_criteria_count: 3
    - epic_id: "EP-02"
      epic_name: "Dashboard Financeiro"
      stories:
        - id: "US-03"
          title: "Como gestor financeiro, quero ver meu fluxo de caixa dos ultimos 30 dias"
          acceptance_criteria_count: 3
        - id: "US-04"
          title: "Como gestor financeiro, quero ver contas a pagar e receber"
          acceptance_criteria_count: 3
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo narrativo descrevendo as stories por epico, com resumo dos criterios de aceite mais relevantes | Documentos de visao, comunicacao com stakeholders nao tecnicos |
| Tabela | Tabela com colunas Epico, ID, Story, Criterios de Aceite | Revisao tecnica, refinamento de backlog |
| Lista agrupada / accordion por epico | Stories organizadas sob cabecalhos de epico, com criterios de aceite expansiveis em cada story | Documentacao de backlog, wikis de projeto, consulta durante refinamento |
| Treemap | Blocos por epico (area proporcional ao numero de stories), subdivididos por story | Visao de distribuicao de escopo entre epicos, identificar epicos com muitas stories |
| Story map | Eixo horizontal com epicos, eixo vertical com stories ordenadas por prioridade dentro de cada epico | Planejamento de releases, workshops de story mapping |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
