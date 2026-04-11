---
region-id: REG-RISK-04
title: "Feasibility Analysis"
group: risk
description: "Multi-dimensional feasibility assessment across technical, financial, operational, and regulatory axes"
source: "Consolidator"
schema: "Tabela (dimensão: técnica/financeira/operacional/regulatória, veredicto, justificativa)"
template-visual: "Card com status badges"
default: false
---

# Feasibility Analysis

Avalia a viabilidade do projeto em quatro dimensoes fundamentais: tecnica, financeira, operacional e regulatoria. Cada dimensao recebe um veredicto claro (viavel, viavel com ressalvas, inviavel) acompanhado de justificativa. Esta visao sintetica apoia a decisao de go/no-go.

## Schema de dados

```yaml
feasibility_analysis:
  dimensions:
    - dimension: string          # Tecnica / Financeira / Operacional / Regulatoria
      verdict: string            # Viavel / Viavel com Ressalvas / Inviavel
      justification: string      # Justificativa do veredicto
      key_conditions: string[]   # Condicoes para manter o veredicto
  overall_verdict: string        # Veredicto consolidado
  recommendation: string         # Recomendacao final
```

## Exemplo

| Dimensao | Veredicto | Justificativa |
|----------|-----------|---------------|
| Tecnica | Viavel | Stack madura (React + Node + PostgreSQL); APIs Open Finance disponiveis; equipe tem experiencia |
| Financeira | Viavel com Ressalvas | TCO de R$ 1.9M em 3 anos e compativel com projecao de receita, mas break-even depende de churn <3% |
| Operacional | Viavel | Time disponivel; processos de CI/CD ja estabelecidos na empresa; suporte pode ser escalonado |
| Regulatoria | Viavel com Ressalvas | LGPD exige DPO designado e consentimento explicito; Open Finance regulado pelo BACEN com requisitos de seguranca |

**Veredicto consolidado:** Viavel com Ressalvas

**Recomendacao:** Prosseguir com o projeto, priorizando a validacao das hipoteses HYP-01 e HYP-02 antes do comprometimento total do budget.

## Representação Visual

### Dados de amostra

| Dimensão | Veredicto | Score (1-5) |
|----------|-----------|-------------|
| Técnica | Viável | 5 |
| Financeira | Viável com Ressalvas | 3 |
| Operacional | Viável | 4 |
| Regulatória | Viável com Ressalvas | 3 |

Veredicto consolidado: Viável com Ressalvas. Condições-chave: validar hipóteses HYP-01 e HYP-02, designar DPO, monitorar churn <3%.

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO
**Tipo:** Radar chart com 4 eixos
**Tecnologia:** Chart.js
**Justificativa:** 4 dimensões com scores numéricos (1-5) mapeiam perfeitamente em um radar chart que mostra o perfil de viabilidade como área preenchida, permitindo identificação imediata de desequilíbrios entre Técnica, Financeira, Operacional e Regulatória.
**Alternativa:** Status badges grid (HTML/CSS) — quando o relatório é estático e os veredictos textuais (Viável / Viável com Ressalvas / Inviável) importam mais que a comparação numérica entre dimensões.
