---
region-id: REG-PROD-06
title: "Business Model"
group: product
description: "Monetização, pricing, planos, canais de distribuição"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Pricing table ou card"
default: false
---

# Business Model

Modelo de negócio e estratégia de monetização do produto, incluindo estrutura de planos, pricing, canais de distribuição e projeções de receita. Esta region é especialmente relevante para projetos SaaS ou produtos que serão comercializados, fornecendo clareza sobre como o investimento será recuperado e como o produto se sustenta financeiramente a longo prazo.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| modelo | string | Tipo de modelo (SaaS, licença, marketplace, freemium, etc.) |
| planos | list | Cada item: `{ nome: string, preco: string, ciclo: string, inclui: list, limite: string }` |
| canais | list | Canais de distribuição e aquisição |
| metricas | object | `{ mrr_projetado: string, arr_projetado: string, ltv: string, cac: string, churn_target: string }` |

## Exemplo

```markdown
## Modelo de Negócio

### Modelo

SaaS B2B com pricing por filial consolidada. Receita recorrente mensal (MRR) com contratos anuais e desconto para compromisso de 3 anos.

### Planos

| Plano | Preço/mês | Filiais | Inclui | Limite |
|-------|-----------|---------|--------|--------|
| **Starter** | R$ 2.500 | Até 5 | Consolidação básica, 1 moeda, relatório P&L, suporte email | 3 usuários |
| **Pro** | R$ 6.500 | Até 20 | Tudo do Starter + multi-moeda, eliminação intercompany, API, trilha de auditoria | 10 usuários |
| **Enterprise** | Sob consulta | Ilimitado | Tudo do Pro + SSO, SLA 99.9%, suporte dedicado, customização de regras | Ilimitado |

### Canais de distribuição

- **Venda direta:** equipe de vendas para Enterprise (ACV > R$ 200K)
- **Inside sales:** demonstrações online para Starter e Pro
- **Parceiros:** Big Four (Deloitte, PwC, EY, KPMG) como canais de indicação
- **Conteúdo:** webinars sobre IFRS e consolidação financeira como geração de leads

### Métricas projetadas (12 meses pós-lançamento)

| Métrica | Target |
|---------|--------|
| MRR | R$ 120K |
| ARR | R$ 1,44M |
| LTV médio | R$ 234K |
| CAC médio | R$ 18K |
| Churn mensal | < 2% |
| LTV/CAC | 13x |
```

## Representação Visual

### Dados de amostra

| Plano | Preço/mês | Filiais | Usuários |
|-------|-----------|---------|----------|
| Starter | R$ 2.500 | Até 5 | 3 |
| Pro | R$ 6.500 | Até 20 | 10 |
| Enterprise | Sob consulta | Ilimitado | Ilimitado |

| Métrica SaaS | Target 12 meses |
|-------------- |-----------------|
| MRR | R$ 120K |
| ARR | R$ 1,44M |
| LTV médio | R$ 234K |
| CAC médio | R$ 18K |
| Churn mensal | < 2% |
| LTV/CAC | 13x |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa do modelo de negócio com detalhamento de canais e estratégia de pricing | Quando o leitor precisa entender a lógica por trás do modelo |
| Tabela | Matrizes separadas para planos (features por tier) e métricas SaaS | Para comparação direta entre planos e consulta de métricas |
| Pricing table | Cards lado a lado por plano com preço, features incluídas e CTA, estilo página de pricing | Para apresentações comerciais e validação de posicionamento |
| Gráfico de barras | Barras comparando métricas SaaS (LTV vs CAC, MRR projetado) | Para comunicação visual de unit economics |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
