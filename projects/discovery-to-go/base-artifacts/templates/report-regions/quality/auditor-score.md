---
region-id: REG-QUAL-01
title: "Auditor Score"
group: quality
description: "Quality scores across five dimensions from the auditor phase"
source: "Fase 2 (auditor) → 2.1"
schema: "Tabela (dimensão, nota, piso, status) — 5 dimensões"
template-visual: "Stat cards ou radar chart"
default: true
---

# Auditor Score

Apresenta as notas de qualidade atribuidas pelo auditor em cinco dimensoes do discovery. Cada dimensao tem um piso minimo aceitavel; dimensoes abaixo do piso disparam reprovas e re-execucao do bloco correspondente. Este mecanismo garante um nivel minimo de qualidade no artefato final.

## Schema de dados

```yaml
auditor_score:
  dimensions:
    - name: string               # Nome da dimensao
      score: number              # Nota (0-10)
      minimum: number            # Piso minimo aceitavel
      status: string             # Aprovado / Reprovado / Marginal
      feedback: string           # Feedback do auditor
  overall_score: number          # Media ponderada
  overall_status: string         # Aprovado / Reprovado
  iteration: number              # Numero da iteracao (1 = primeira passada)
```

## Exemplo

| Dimensao | Nota | Piso | Status | Feedback |
|----------|------|------|--------|----------|
| Completude dos requisitos | 8.5 | 7.0 | Aprovado | Requisitos funcionais bem cobertos; falta detalhar requisitos de acessibilidade |
| Viabilidade tecnica | 9.0 | 7.0 | Aprovado | Arquitetura solida com tecnologias maduras |
| Analise financeira | 6.5 | 7.0 | Reprovado | TCO nao inclui custos de treinamento e change management |
| Cobertura de riscos | 7.5 | 7.0 | Aprovado | Boa cobertura; adicionar riscos de dependencia de fornecedor |
| Alinhamento estrategico | 8.0 | 7.0 | Aprovado | Alinhado com OKRs da empresa para o trimestre |

**Score geral:** 7.9 / 10 — **Status: Reprovado** (1 dimensao abaixo do piso)

**Iteracao:** 1 (bloco financeiro sera re-executado)

## Representacao Visual

### Dados de amostra

```yaml
auditor_score:
  dimensions:
    - name: "Completude dos requisitos"
      score: 8.5
      minimum: 7.0
      status: "Aprovado"
    - name: "Viabilidade tecnica"
      score: 9.0
      minimum: 7.0
      status: "Aprovado"
    - name: "Analise financeira"
      score: 6.5
      minimum: 7.0
      status: "Reprovado"
    - name: "Cobertura de riscos"
      score: 7.5
      minimum: 7.0
      status: "Aprovado"
    - name: "Alinhamento estrategico"
      score: 8.0
      minimum: 7.0
      status: "Aprovado"
  overall_score: 7.9
  overall_status: "Reprovado"
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo resumindo o score geral, dimensoes aprovadas e reprovadas, e proximos passos | Relatorios textuais, emails executivos, contextos onde grafico nao e possivel |
| Tabela | Tabela com colunas Dimensao, Nota, Piso, Status e Feedback (formato atual do Exemplo) | Visao detalhada para revisao tecnica, comparacao lado a lado das dimensoes |
| Radar chart (5 dimensoes) | Grafico radar com os 5 eixos representando as dimensoes, overlay da linha de piso minimo | Visao holistica do equilibrio entre dimensoes; destaca visualmente desequilibrios |
| Gauge por dimensao | Um medidor (gauge) individual para cada dimensao, com zona verde (acima do piso) e vermelha (abaixo) | Dashboards interativos, visualizacao rapida de aprovado/reprovado por dimensao |
| Stat cards | Cards individuais com nota grande, nome da dimensao e indicador visual de status | Resumo executivo, dashboards, apresentacoes com visao rapida |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
