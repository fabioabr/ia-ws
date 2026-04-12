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
  findings:
    - title: string              # Titulo da ressalva (ex: "TCO sem custos de treinamento")
      dimension: string          # Dimensao afetada (Completude / Fundamentacao / Coerencia / Profundidade / Neutralidade)
      score_impact: string       # Como afeta o score (ex: "Completude: 6.5 < piso 7.0")
      severity: string           # Critica / Alta / Media
      description: string        # 2-3 frases: O QUE foi identificado
      why_important: string      # 1-2 frases: impacto se nao enderecado
      recommendation: string     # O que fazer para resolver
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

### Findings detalhados

**Finding 1 — TCO Incompleto: Custos de Treinamento e Change Management Ausentes**
- **Dimensao:** Analise financeira | **Score impact:** Analise financeira: 6.5 < piso 7.0
- **Severidade:** Critica
- **Descricao:** O bloco 1.8 (TCO) nao inclui custos de treinamento da equipe e change management organizacional. Para um projeto com 3 squads e migracao de processos manuais, esses custos representam tipicamente 10-15% do investimento total no ano 1.
- **Por que e importante:** A dimensao "Analise financeira" ficou abaixo do piso (6.5 < 7.0), causando reprovacao automatica da iteracao. O TCO subestimado pode levar a aprovacao de um projeto financeiramente inviavel.
- **Recomendacao:** Adicionar ao TCO: programa de treinamento (40h por squad x 3 squads), consultoria de change management (3 meses), custos de shadow period durante transicao. Recalcular e resubmeter bloco financeiro.

**Finding 2 — Requisitos de Acessibilidade Nao Detalhados**
- **Dimensao:** Completude dos requisitos | **Score impact:** Completude: 8.5 (acima do piso, mas com gap)
- **Severidade:** Alta
- **Descricao:** Os requisitos funcionais estao bem cobertos, porem requisitos de acessibilidade (WCAG 2.1 AA) foram mencionados apenas como bullet point sem detalhamento. Nao ha especificacao de quais componentes precisam de acessibilidade nem criterios de aceite.
- **Por que e importante:** Acessibilidade pode ser requisito legal dependendo do setor. A ausencia de detalhamento gera retrabalho nas sprints de desenvolvimento quando os criterios forem descobertos tardiamente.
- **Recomendacao:** Expandir secao de acessibilidade com: niveis WCAG exigidos por tipo de interface, componentes prioritarios, ferramentas de teste automatizado (axe-core), e criterios de aceite por user story.

**Finding 3 — Risco de Dependencia de Fornecedor Nao Mitigado**
- **Dimensao:** Cobertura de riscos | **Score impact:** Cobertura de riscos: 7.5 (acima do piso, mas incompleto)
- **Severidade:** Alta
- **Descricao:** A matriz de riscos cobre riscos tecnicos e de timeline, mas nao inclui risco de vendor lock-in. A arquitetura proposta usa 3 servicos gerenciados proprietarios (AWS Lambda, DynamoDB, Cognito) sem avaliar portabilidade ou alternativas.
- **Por que e importante:** Se houver necessidade de migracao de cloud (por custo, compliance ou estrategia), o custo de reescrita pode ser 40-60% do investimento original.
- **Recomendacao:** Adicionar risco de vendor lock-in a matriz com: probabilidade, impacto financeiro estimado, estrategia de mitigacao (abstraction layers, multi-cloud readiness), e trigger de revisao (ex: custo AWS > 120% do projetado).

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
  findings:
    - title: "TCO Incompleto: Custos de Treinamento e Change Management Ausentes"
      dimension: "Analise financeira"
      score_impact: "Analise financeira: 6.5 < piso 7.0"
      severity: "Critica"
      description: "TCO nao inclui treinamento e change management — 10-15% do investimento total."
      why_important: "Dimensao abaixo do piso causa reprovacao automatica. TCO subestimado."
      recommendation: "Adicionar treinamento (40h x 3 squads), change management (3 meses), shadow period."
    - title: "Requisitos de Acessibilidade Nao Detalhados"
      dimension: "Completude dos requisitos"
      score_impact: "Completude: 8.5 (acima do piso, mas com gap)"
      severity: "Alta"
      description: "Acessibilidade WCAG 2.1 AA mencionada como bullet sem especificacao."
      why_important: "Pode ser requisito legal. Ausencia gera retrabalho tardio nas sprints."
      recommendation: "Expandir com niveis WCAG por interface, componentes prioritarios, criterios de aceite."
    - title: "Risco de Dependencia de Fornecedor Nao Mitigado"
      dimension: "Cobertura de riscos"
      score_impact: "Cobertura de riscos: 7.5 (acima do piso, mas incompleto)"
      severity: "Alta"
      description: "Vendor lock-in nao consta na matriz de riscos. 3 servicos AWS proprietarios sem avaliacao de portabilidade."
      why_important: "Migracao de cloud pode custar 40-60% do investimento original."
      recommendation: "Adicionar vendor lock-in a matriz com probabilidade, impacto, abstraction layers, trigger de revisao."
```

### Recomendacao do Chart Specialist

**Veredicto:** GRAFICO
**Tipo:** Radar chart com 5 eixos
**Tecnologia:** Chart.js
**Justificativa:** 5 dimensoes com scores numericos (0-10) e linha de piso minimo mapeiam perfeitamente em um radar chart com overlay, permitindo visao holistica do equilibrio entre dimensoes e identificacao imediata de quais estao abaixo do piso.
**Alternativa:** Stat cards com gauge (HTML/CSS) — quando o relatorio e estatico e a comparacao aprovado/reprovado por dimensao individual importa mais que o perfil geral.
