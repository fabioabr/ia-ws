---
region-id: REG-DOM-MIGR-02
title: "Migration As-Is vs To-Be"
group: domain
description: "Side-by-side comparison of current and target state across stack, cost, and performance"
source: "Bloco #5/#7 (arch)"
schema: "Comparativo stack/custo/performance"
template-visual: "Split comparison card"
when: migration-modernization
default: false
---

# Migration As-Is vs To-Be

Comparativo lado a lado entre o estado atual (as-is) e o estado futuro (to-be) em termos de stack tecnologica, custos operacionais e performance. Permite visualizar claramente os ganhos esperados com a migracao.

## Schema de dados

```yaml
as_is_vs_to_be:
  dimensions:
    - dimension: string
      as_is: string
      to_be: string
      improvement: string
```

## Exemplo

| Dimensao | As-Is | To-Be | Melhoria Esperada |
|----------|-------|-------|-------------------|
| Infraestrutura | Servidores on-premise (3 VMs) | AWS EKS (containers) | Elasticidade + redução de 40% no custo |
| Banco de dados | SQL Server 2014 (licenciado) | PostgreSQL 16 (open source) | Economia de R$ 48.000/ano em licencas |
| Deploy | Manual (1x/mes) | CI/CD automatizado (diario) | Lead time de 30 dias para < 1 dia |
| Monitoramento | Logs em arquivo + Nagios | Datadog (APM + logs + metrics) | MTTR de 4h para < 30min |
| Performance | P95 latencia: 1.2s | P95 latencia: < 200ms | 6x mais rapido |
| Custo mensal | R$ 12.000 | R$ 7.230 | Economia de R$ 4.770/mes |

## Representacao Visual

### Dados de amostra

| Dimensao | As-Is (score 1-5) | To-Be (score 1-5) |
|----------|-------------------|-------------------|
| Elasticidade | 1 | 5 |
| Custo | 2 | 4 |
| Automacao deploy | 1 | 5 |
| Observabilidade | 2 | 5 |
| Performance | 2 | 5 |
| Agilidade | 1 | 4 |

### Recomendacao do Chart Specialist

**Veredicto:** CARD
**Tipo:** Comparison cards lado-a-lado
**Tecnologia:** HTML/CSS
**Justificativa:** A comparacao as-is vs to-be tem 6 dimensoes com descricoes qualitativas e quantitativas. Cards lado-a-lado (As-Is a esquerda, To-Be a direita) com destaque visual nas melhorias comunicam o contraste de forma imediata e impactante para decisores.
**Alternativa:** Radar chart (Chart.js) — quando houver 5+ dimensoes com scores numericos (como os scores 1-5 dos dados de amostra) e o objetivo for comparar maturidade geral entre estados.
