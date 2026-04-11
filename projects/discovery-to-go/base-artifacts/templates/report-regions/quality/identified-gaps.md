---
region-id: REG-QUAL-03
title: "Identified Gaps"
group: quality
description: "Gaps found during audit that need attention before proceeding"
source: "Fase 2 (auditor) → 2.1"
schema: "Lista (área, gap, impacto, recomendação)"
template-visual: "Table com alert style"
default: false
---

# Identified Gaps

Lista as lacunas identificadas pelo auditor durante a revisao dos artefatos de discovery. Cada gap indica a area afetada, o impacto potencial e uma recomendacao de como resolve-lo. Gaps criticos devem ser enderecados antes da aprovacao final.

## Schema de dados

```yaml
identified_gaps:
  gaps:
    - id: string                 # Identificador (ex: GAP-01)
      area: string               # Area afetada (requisitos, arquitetura, financeiro, seguranca, etc.)
      description: string        # Descricao do gap
      impact: string             # Critico / Alto / Medio / Baixo
      recommendation: string     # Recomendacao para resolver
      status: string             # Aberto / Em resolucao / Resolvido
```

## Exemplo

| ID | Area | Gap | Impacto | Recomendacao | Status |
|----|------|-----|---------|-------------|--------|
| GAP-01 | Financeiro | Custos de customer success e suporte nao contemplados no TCO | Alto | Incluir pelo menos 1 CS part-time a partir do mes 3 | Aberto |
| GAP-02 | Seguranca | Nenhuma mencao a politica de backup e disaster recovery | Critico | Definir RPO/RTO e estrategia de backup antes da sprint 1 | Aberto |
| GAP-03 | Requisitos | Requisitos de acessibilidade (WCAG) nao especificados | Medio | Adicionar criterios WCAG 2.1 AA nos criterios de aceite | Em resolucao |
| GAP-04 | Arquitetura | Estrategia de observabilidade mencionada mas nao detalhada | Medio | Detalhar stack de monitoring, logging e tracing | Aberto |

## Representacao Visual

### Dados de amostra

```yaml
identified_gaps:
  gaps:
    - id: "GAP-01"
      area: "Financeiro"
      description: "Custos de customer success e suporte nao contemplados no TCO"
      impact: "Alto"
      status: "Aberto"
    - id: "GAP-02"
      area: "Seguranca"
      description: "Nenhuma mencao a politica de backup e disaster recovery"
      impact: "Critico"
      status: "Aberto"
    - id: "GAP-03"
      area: "Requisitos"
      description: "Requisitos de acessibilidade (WCAG) nao especificados"
      impact: "Medio"
      status: "Em resolucao"
    - id: "GAP-04"
      area: "Arquitetura"
      description: "Estrategia de observabilidade mencionada mas nao detalhada"
      impact: "Medio"
      status: "Aberto"
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo descritivo listando os gaps por area, destacando impactos criticos e altos com recomendacoes | Relatorios narrativos, comunicacao executiva, emails de status |
| Tabela | Tabela com colunas ID, Area, Gap, Impacto, Recomendacao e Status (formato atual do Exemplo) | Revisao detalhada, rastreamento de resolucao, documentacao tecnica |
| Barras horizontais por impacto | Grafico de barras horizontais agrupando gaps por nivel de impacto (Critico, Alto, Medio, Baixo) com contagem | Visao rapida da distribuicao de severidade, priorizacao de resolucao |
| Heatmap por area vs impacto | Matriz com areas nas linhas e niveis de impacto nas colunas, cor indicando quantidade de gaps | Identificar areas com maior concentracao de gaps criticos |
| Lista com alert style | Cards com borda colorida por impacto (vermelho=Critico, laranja=Alto, amarelo=Medio) e barra de progresso de resolucao | Dashboards de qualidade, acompanhamento visual de gaps abertos |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
