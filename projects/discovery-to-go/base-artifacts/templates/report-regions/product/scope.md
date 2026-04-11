---
region-id: REG-PROD-07
title: "Scope"
group: product
description: "Objetivo do projeto + lista dentro + lista fora (explícito) + hipótese central + critério go/no-go"
source: "Bloco #1/#3 (po) → 1.1/1.3"
schema: "text"
template-visual: "Card com objetivo + split list (in/out)"
default: true
---

# Scope

Definição clara e explícita do escopo do projeto, dividida em: objetivo principal, o que está dentro do escopo (será feito), o que está fora do escopo (não será feito — e por quê), a hipótese central que o MVP pretende validar e os critérios de go/no-go para avançar para a próxima fase. A lista "fora do escopo" é tão importante quanto a lista "dentro" — ela previne scope creep e alinha expectativas com stakeholders.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| objetivo | string | Declaração clara do objetivo do projeto em 1-2 frases |
| dentro | list | Features/capacidades que serão entregues no MVP |
| fora | list | Cada item: `{ item: string, motivo: string }` — o que não será feito e por quê |
| hipotese_central | string | A premissa principal que o MVP precisa validar |
| criterios_go_no_go | list | Condições mensuráveis para decidir se avança |

## Exemplo

```markdown
## Escopo

### Objetivo

Construir o MVP do FinTrack Pro que automatize a consolidação financeira de 3 filiais da Acme Corp, eliminando o processo manual e reduzindo o tempo de fechamento de D+8 para D+3.

### Dentro do escopo (será feito)

- ✅ Integração via API com SAP R/3 de 3 filiais (SP, RJ, MG)
- ✅ Engine de eliminação intercompany com regras configuráveis
- ✅ Consolidação automática com geração de P&L consolidado
- ✅ Dashboard executivo com drill-down por filial
- ✅ Trilha de auditoria completa (log de todas as transformações)

### Fora do escopo (não será feito)

| Item | Motivo |
|------|--------|
| Integração com filiais internacionais (4 países) | Complexidade de multi-moeda e regulação local — planejado para Fase 2 |
| Consolidação de balanço patrimonial | MVP foca apenas em P&L — balanço na Fase 2 |
| App mobile | Baixa prioridade — analistas trabalham em desktop |
| Relatórios customizáveis pelo usuário | MVP entrega relatórios padrão — customização na Fase 2 |

### Hipótese central

> Se automatizarmos a coleta de dados e a eliminação intercompany para 3 filiais, conseguiremos reduzir o fechamento mensal de D+8 para D+3 com zero erros materiais — validando que a abordagem técnica funciona antes de escalar para 12 filiais.

### Critérios de Go/No-Go para Fase 2

| Critério | Valor-alvo |
|----------|-----------|
| Tempo de fechamento | ≤ D+3 por 3 meses consecutivos |
| Erros materiais | 0 em 3 ciclos |
| Satisfação dos analistas (NPS) | ≥ 40 |
| Integração SAP estável | Uptime ≥ 99% no período |
```

## Representação Visual

### Dados de amostra

- **Dentro do escopo:** 5 itens (integração SAP 3 filiais, engine eliminação, consolidação P&L, dashboard executivo, trilha de auditoria)
- **Fora do escopo:** 4 itens (filiais internacionais, balanço patrimonial, app mobile, relatórios customizáveis)
- **Hipótese central:** Automatizar coleta + eliminação de 3 filiais reduz fechamento de D+8 para D+3 com zero erros
- **Critérios go/no-go:** 4 condições mensuráveis

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa do objetivo, hipótese e justificativas de inclusão/exclusão | Quando o leitor precisa entender o raciocínio por trás das decisões de escopo |
| Tabela | Matrizes separadas para dentro/fora do escopo e critérios go/no-go | Para referência rápida e checklist de escopo |
| Split card (in/out) | Card dividido em duas colunas — verde (dentro) e vermelho (fora) — com ícones de check/x | Para comunicação visual imediata do que está e não está no escopo |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
