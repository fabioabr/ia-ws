---
region-id: REG-NARR-01
title: "How We Got Here"
group: narrative
description: "Narrative timeline of the discovery process including iterations and convergence"
source: "Pipeline-state + Consolidator"
schema: "Texto narrativo + timeline (iterações, reprovas, convergência)"
template-visual: "Timeline vertical"
default: true
---

# How We Got Here

Conta a historia do processo de discovery: quantas iteracoes foram necessarias, quais blocos foram reprovados e re-executados, e como o time convergiu para a solucao final. Esta narrativa da contexto ao leitor sobre a maturidade e robustez dos artefatos entregues.

## Schema de dados

```yaml
how_we_got_here:
  total_iterations: number       # Total de iteracoes do pipeline
  total_duration: string         # Duracao total do discovery
  timeline:
    - step: number               # Numero do passo
      date: string               # Data
      event: string              # Descricao do evento
      type: string               # execution / rejection / approval / convergence
      details: string            # Detalhes adicionais
  convergence_summary: string    # Resumo de como se chegou ao resultado final
```

## Exemplo

**Duracao total do discovery:** 3 dias (pipeline automatizado)

1. **Dia 1 — Execucao inicial (Fase 1)**
   - Blocos #1 a #8 executados sequencialmente
   - Briefing processado, personas definidas, arquitetura desenhada, TCO calculado
   - *Tipo: execution*

2. **Dia 2 — Auditoria e 10th-man (Fase 2)**
   - Auditor atribuiu nota 6.5/10 para analise financeira (abaixo do piso de 7.0)
   - 10th-man levantou 5 questoes, 2 criticas em aberto
   - Bloco #8 (financeiro) reprovado e re-executado com inclusao de custos de suporte
   - *Tipo: rejection + re-execution*

3. **Dia 2 — Segunda iteracao**
   - TCO revisado com custos de CS e suporte incluidos
   - Nova nota do auditor: 7.8/10 — aprovado
   - *Tipo: approval*

4. **Dia 3 — Consolidacao e convergencia**
   - Consolidator gerou relatorio final
   - 2 questoes do 10th-man permanecem em aberto (aceitas como riscos conhecidos)
   - *Tipo: convergence*

**Resumo:** O discovery convergiu em 2 iteracoes. A principal correcao foi a inclusao de custos operacionais no TCO, identificada pelo auditor. As questoes abertas do 10th-man foram documentadas como hipoteses a validar.

## Representacao Visual

### Dados de amostra

```
  Dia 1  ●  Execucao inicial (Fase 1)
         │  Blocos #1 a #8 executados
         │
  Dia 2  ●  Auditoria e 10th-man (Fase 2)
         │  Bloco #8 reprovado (nota 6.5/10)
         │
  Dia 2  ●  Segunda iteracao
         │  TCO revisado — aprovado (nota 7.8/10)
         │
  Dia 3  ●  Consolidacao e convergencia
            Relatorio final gerado
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa cronologica com marcos destacados em negrito | Relatorios executivos, contexto detalhado do processo |
| Tabela | Tabela com colunas Data, Evento, Tipo, Detalhes | Referencia rapida, rastreabilidade de decisoes |
| Timeline vertical | Linha do tempo vertical com nos coloridos por tipo (execucao, rejeicao, aprovacao, convergencia) | Apresentacoes de processo, visao geral do discovery |
| Timeline vertical com detalhes expandiveis | Timeline com cards laterais contendo detalhes de cada etapa | Relatorios detalhados, retrospectivas de processo |
| Timeline vertical com status icons | Timeline com icones indicando tipo de evento (check, alerta, reprocesso) | Dashboards de acompanhamento de pipeline |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
