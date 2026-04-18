---
region-id: REG-PROD-05B
title: "ROI"
group: product
description: "Análise de retorno sobre investimento — condicional à flag require_roi=true"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Stat cards"
default: false
deliverable-scope: ["OP", "EX", "DR"]
conditional-on: "require_roi=true"
---

# ROI

Análise de retorno sobre investimento (ROI): quanto custa, quanto retorna, em quanto tempo o investimento se paga e sob quais premissas. Traduz a visão do produto em justificativa financeira para o comitê de investimento.

> [!warning] Region condicional
> Esta region **só é produzida** quando a flag `require_roi=true` estiver presente no briefing (ver [start-briefing.md](../../../../../../starter-kit/client-template/projects/project-n/setup/start-briefing.md)).
>
> Por **padrão** do Discovery-to-Go, `require_roi=false` — o Discovery acontece **depois** da aprovação global do investimento, então justificativa de ROI já foi feita upstream. O One-Pager do DTG foca em **esforço/custo/escopo**, não em justificativa de retorno.
>
> Ative `require_roi=true` apenas quando o cliente explicitamente pedir — ex: projeto é parte de um business case próprio que precisa ser vendido internamente; projeto tem budget condicional à demonstração de payback.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| investimento_total | string | Valor total ou faixa (3 anos) |
| retorno_anual | string | Economia anual estimada (valor ou faixa) |
| payback_meses | string | Tempo até o payback, em meses |
| roi_3_anos | string | ROI percentual em 3 anos (valor ou faixa) |
| vpl | string | Valor Presente Líquido (quando aplicável) |
| premissas | list | Premissas que sustentam os cálculos |
| intangiveis | list | Benefícios não monetizados (reputação, velocidade de decisão, etc.) |

## Exemplo

```markdown
## ROI

| Métrica | Valor |
|---------|-------|
| **Investimento total (3 anos)** | R$ 2,1M — R$ 2,8M |
| **Economia anual estimada** | R$ 500K — R$ 700K (horas + retrabalho + risco) |
| **Payback** | 14 meses |
| **ROI em 3 anos** | 75% — 100% |
| **VPL (taxa desconto 12%)** | R$ 1,4M |

### Premissas

- Custo médio hora/analista: R$ 120
- 4 analistas × 10h economizadas/semana × 48 semanas
- Redução de custo de retrabalho de auditoria: R$ 80K/ano
- Taxa de desconto: 12% (custo de capital corporativo)

### Benefícios intangíveis (não monetizados)

- Velocidade de decisão do conselho (dados confiáveis em D+2)
- Redução de risco regulatório (rastreabilidade total)
- Capacidade de escalar portfólio sem aumentar headcount financeiro
```

## Representação Visual

### Dados de amostra

| Métrica | Valor |
|---------|-------|
| Investimento (3 anos) | R$ 2,1M-2,8M |
| Economia anual | R$ 500K-700K |
| Payback | 14 meses |
| ROI 3 anos | 75%-100% |
| VPL | R$ 1,4M |

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Stat cards destacando 4-5 números-chave (investimento, retorno, payback, ROI, VPL)
**Tecnologia:** HTML/CSS
**Justificativa:** ROI é um conjunto de 4-5 números financeiros chave — stat cards com tipografia hierárquica comunicam imediatamente sem necessidade de gráfico. Gráficos fazem sentido apenas se houver **séries temporais** (payback curve) ou **cenários comparativos** (otimista/realista/pessimista).
**Alternativa:** Gráfico de linhas (Chart.js) da payback curve mês-a-mês — quando o cliente solicitar projeção temporal visual.
