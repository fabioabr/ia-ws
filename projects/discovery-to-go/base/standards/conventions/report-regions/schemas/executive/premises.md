---
region-id: REG-EXEC-07
title: "Premises"
group: executive
description: "Premissas que sustentam as estimativas do projeto — condições assumidas que, se mudarem, impactam prazo e custo"
source: "Consolidator (extrai de todos os blocos)"
schema: "Lista de premissas com ícone de atenção"
template-visual: "Card com lista de bullets (HTML/CSS)"
default: false
---

# Premises

Lista de condições assumidas para as estimativas do projeto. Se qualquer premissa mudar, as estimativas precisam ser recalculadas. Serve como "contrato" entre quem fez o discovery e quem vai executar.

## Schema de dados

```yaml
premises:
  items:
    - text: string          # Descrição da premissa
      category: string      # Técnica / Financeira / Organizacional / Regulatória
      impact_if_changes: string  # O que acontece se mudar
```

## Exemplo

- ⚠️ **LLM é BYOK** — custo de chamadas é do tenant, não do produto. *Se mudar: +R$ 50-150K/ano de custo operacional.*
- ⚠️ **Infraestrutura GCP pay-per-use** — custo escala com uso. *Se mudar para reservado: custo fixo mensal independente de clientes.*
- ⚠️ **Equipe de 1 pessoa + Claude Code** — sem contratação no MVP. *Se mudar: +R$ 15-20K/mês por pessoa adicional.*
- ⚠️ **MVP em 16 semanas** — escopo reduzido (apenas BigQuery, 3 idiomas). *Se escopo aumentar: prazo proporcional.*
- ⚠️ **Sem design dedicado** — UI com templates + Claude Code. *Se exigir design custom: +4-6 semanas + freelancer.*

## Representação Visual

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com lista de bullets e ícones de atenção
**Tecnologia:** HTML/CSS
**Justificativa:** Dados qualitativos em lista — card informativo é o formato ideal.
**Alternativa:** Tabela (categoria, premissa, impacto) — quando há 10+ premissas.
