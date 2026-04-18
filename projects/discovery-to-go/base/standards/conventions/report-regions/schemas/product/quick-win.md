---
region-id: REG-PROD-10
title: "Quick Win"
group: product
description: "Entrega intermediária de um MVP funcional durante a execução do projeto completo — valida hipóteses, gera valor cedo e reduz risco de ROI tardio"
source: "Bloco #3 (po) + Solution Architect → 1.3/1.8"
schema: "object"
template-visual: "Card destacado com pilula 'Quick Win' + timeline interna (semana-alvo) + escopo enxuto IN/OUT + valor gerado + critério de aceite"
default: false
---

# Quick Win

Uma entrega intermediária de MVP executada **durante** o projeto principal, posicionada em um marco que gera valor tangível antes do go-live completo. O Quick Win NÃO substitui o escopo completo — ele é um sub-conjunto cuidadosamente escolhido para:

- **Validar hipóteses críticas** cedo (evita investimento pesado em algo inviável)
- **Gerar ROI parcial** antes do fim do projeto (o patrocinador vê retorno em 2-3 meses)
- **Reduzir risco** de perda de momentum em projetos longos (6+ meses)
- **Construir credibilidade** do time entregando algo funcional cedo

A seção responde: o que será entregue cedo, quando, para quem, qual é o valor incremental comprovável, e qual o critério objetivo de aceitação.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| marco | string | Semana/fase-alvo de entrega (ex: "Semana 12 — fim da Fase 2") |
| duracao_ate_marco | string | Tempo decorrido até o Quick Win (ex: "12 semanas / 3 meses") |
| % do_projeto | number | Percentual do escopo total representado pelo Quick Win (ex: 35) |
| escopo_quick_win | list | Subconjunto de entregas que compõe o MVP intermediário |
| fora_quick_win | list | Itens do projeto completo que NÃO entram no Quick Win (explicitamente adiados) |
| valor_entregue | string | Valor concreto e mensurável gerado ao liberar o Quick Win |
| beneficiarios | list | Quem já colhe benefício no momento do Quick Win (grupos/áreas) |
| hipotese_validada | string | Premissa que o Quick Win prova ou refuta |
| criterio_aceite | list | Condições objetivas que marcam o Quick Win como bem-sucedido |
| investimento_ate_marco | string | Custo acumulado até a entrega do Quick Win (R$ e horas) |
| riscos_mitigados | list | Riscos do projeto completo que o Quick Win reduz ou elimina |

## Exemplo

```markdown
## Quick Win — MVP Intermediário

**Marco:** Semana 12 — fim da Fase 2 (Sensedia + GCS)
**Investimento acumulado:** R$ 310K · 800h · 35% do escopo total

### O que será entregue cedo

- ✅ Extração automatizada das 5 fontes críticas (ERPs SAP, TOTVS, Oracle EBS)
- ✅ Armazenamento raw no GCS com particionamento e CMEK
- ✅ Dashboard operacional mínimo (volumetria por fonte + qualidade de ingestão)

### Fora do Quick Win (segue para o projeto completo)

- Camada Silver consolidada (Fase 3)
- Camada Gold e modelagem dimensional (Fase 4)
- Dashboard Analítico com drill-down (Fase 4)
- 10 fontes restantes (Blocos 2 e 3 da Fase 2)

### Valor entregue

> Controladoria passa a enxergar o status de ingestão das 5 fontes mais
> críticas em tempo quase real — antes dependiam de planilhas manuais
> semanais. Ganho imediato: 6 dias úteis/mês liberados por analista.

### Beneficiários imediatos

- Controladoria (3 analistas) — visibilidade operacional
- Head de Dados — evidência de maturidade técnica para a Diretoria
- Time de TI — debug de integrações com ferramenta visual

### Hipótese validada

> O Sensedia + GCS suportam as 5 fontes críticas dentro do SLA projetado,
> sem intervenção manual, por 4 semanas consecutivas.

### Critério de aceite

| Critério | Alvo |
|----------|------|
| Cobertura automatizada | 5 de 5 fontes críticas |
| Frequência de extração | Diária sem intervenção manual |
| Taxa de sucesso | ≥ 98% dos jobs no período de avaliação |
| Dashboard disponível | Publicado e acessado por ≥ 3 usuários |

### Riscos do projeto que esta entrega reduz

- **Dependência de Sensedia como ponto único** — validada em produção antes de ampliar
- **Baixa adoção dos dashboards** — uso real precoce confirma valor para o usuário final
- **Custo BigQuery acima do estimado** — primeiros sinais de consumo aparecem cedo
```

## Representação Visual

### Dados de amostra

- **Marco:** Semana 12 (no meio de um projeto de 24 semanas)
- **% do projeto:** 35% do escopo total liberado cedo
- **Escopo Quick Win:** 3 itens funcionais
- **Fora Quick Win:** 4 itens adiados para o projeto completo
- **Critérios de aceite:** 4 condições objetivas mensuráveis
- **Riscos mitigados:** 3 de 5 riscos do top list

### Recomendação do Chart Specialist

**Veredicto:** CARD DESTACADO
**Tipo:** Card com pílula "⚡ Quick Win" no topo + mini-timeline interna marcando o ponto de entrega na régua do projeto + split IN/OUT + bloco lateral com valor e beneficiários + tabela compacta de critérios de aceite.
**Tecnologia:** HTML/CSS puro
**Justificativa:** Quick Win é um ponto narrativo forte — precisa se destacar visualmente do restante do cenário. A pílula e o destaque da borda chamam atenção para a entrega antecipada; a mini-timeline comunica "quando" instantaneamente; o IN/OUT deixa claro que é um sub-escopo e não o projeto inteiro. A tabela de critérios encerra a seção ancorando em métricas objetivas.
**Alternativa:** Quando houver múltiplos Quick Wins no mesmo cenário, usar uma trilha horizontal (milestones) com cards menores em sequência sobre uma timeline unificada.
