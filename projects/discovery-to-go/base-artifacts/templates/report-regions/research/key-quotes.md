---
region-id: REG-PESQ-02
title: "Key Quotes"
group: research
description: "Citações representativas de entrevistados com atribuição e source tag"
source: "Interview log"
schema: "text"
template-visual: "Blockquote cards"
default: false
---

# Key Quotes

Citações literais dos entrevistados que capturam de forma vívida as dores, necessidades e expectativas identificadas durante o discovery. Cada citação é atribuída ao papel do entrevistado (nunca ao nome real) e classificada com uma source tag indicando a origem da informação. Citações representativas são poderosas para comunicar insights a stakeholders e fundamentar decisões de produto.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| citacoes | list | Cada item: `{ quote: string, atribuicao: string, contexto: string, source_tag: "BRIEFING" | "INTERVIEW" | "RAG" | "INFERENCE", tema: string }` |

## Exemplo

```markdown
## Citações Representativas

> "Eu gasto mais tempo coletando dados do que analisando. Virei um operador de planilha, não um analista financeiro."
>
> — **Analista Financeiro Sênior** | Tema: Processo de consolidação | `INTERVIEW`

---

> "Toda vez que apresento o consolidado ao conselho, rezo para não ter erro. Já tive que pedir desculpas 3 vezes esse ano."
>
> — **CFO** | Tema: Qualidade e confiança | `INTERVIEW`

---

> "A gente até tentou automatizar com macro. Funcionou por 2 meses. Depois ninguém entendia o código e voltamos para o manual."
>
> — **Controller** | Tema: Tentativas anteriores | `INTERVIEW`

---

> "Quando o auditor pede a memória de cálculo, eu levo 2 semanas para reconstruir. É tudo na minha cabeça e nas minhas planilhas."
>
> — **Analista Financeiro Pleno** | Tema: Rastreabilidade | `INTERVIEW`

---

> "Eu não quero só consolidar mais rápido. Eu quero saber o resultado antes do fechamento oficial. Quero predição."
>
> — **CFO** | Tema: Visão de futuro | `INTERVIEW`

---

> "As filiais do TOTVS são um pesadelo. O formato muda toda vez que atualizam o sistema. Nem eles sabem explicar."
>
> — **Analista Financeiro Sênior** | Tema: Integração multi-ERP | `INTERVIEW`
```
