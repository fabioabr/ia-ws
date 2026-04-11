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

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo cada dimensão de viabilidade, seu veredicto e as condições para sustentá-lo | Relatórios executivos onde o raciocínio por trás de cada veredicto é mais importante que a comparação visual |
| Tabela | Matriz dimensão x veredicto x justificativa x condições, como no exemplo acima | Quando o leitor precisa dos detalhes completos de cada dimensão para tomada de decisão |
| Radar chart (4 dimensões) | Gráfico radar com 4 eixos (Técnica, Financeira, Operacional, Regulatória), scores de 1-5, área preenchida mostrando o perfil de viabilidade | Visualizar o equilíbrio entre as dimensões e identificar rapidamente quais áreas são mais fracas |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
