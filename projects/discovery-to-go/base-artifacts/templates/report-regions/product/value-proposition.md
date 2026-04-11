---
region-id: REG-PROD-04
title: "Value Proposition"
group: product
description: "Elevator pitch + diferenciação competitiva + princípios de produto"
source: "Bloco #1 (po) → 1.1"
schema: "text"
template-visual: "Card com highlight"
default: true
---

# Value Proposition

Declaração clara e concisa do valor que o produto entrega, usando o formato de elevator pitch estruturado. Complementada pela diferenciação competitiva (o que torna esta solução única frente às alternativas) e pelos princípios de produto que guiarão decisões de design e priorização ao longo do desenvolvimento. Esta region é a bússola do produto — qualquer feature ou decisão técnica deve estar alinhada com a proposta de valor aqui definida.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| elevator_pitch | object | `{ para: string, que: string, o_produto: string, e_um: string, que_faz: string, diferente_de: string, nosso_produto: string }` |
| diferenciais | list | 3-5 bullets com diferenciais competitivos |
| principios | list | 3-5 princípios de produto (ex: "Automatizar, não apenas digitalizar") |

## Exemplo

```markdown
## Proposta de Valor

### Elevator Pitch

> **Para** equipes de controladoria de empresas com múltiplas filiais
> **que** precisam consolidar dados financeiros de diferentes ERPs com rapidez e confiabilidade,
> **o FinTrack Pro** é uma **plataforma de consolidação financeira automatizada**
> **que** centraliza dados, aplica regras de eliminação intercompany e gera relatórios consolidados em tempo real.
> **Diferente de** soluções como Oracle HFM ou planilhas manuais,
> **nosso produto** é configurável sem código, custa 40% menos e se integra nativamente com SAP, TOTVS e Oracle.

### Diferenciais competitivos

- **Integração nativa multi-ERP:** conectores prontos para SAP, TOTVS e Oracle — sem middleware
- **Regras de eliminação configuráveis:** motor de regras no-code que controllers configuram sem depender de TI
- **Custo 40% menor que soluções enterprise:** pricing por filial, sem licenciamento por usuário
- **Trilha de auditoria completa:** cada número rastreável até a origem, com log de todas as transformações
- **Time-to-value de 8 semanas:** implementação rápida com templates por indústria

### Princípios de produto

1. **Automatizar, não apenas digitalizar** — eliminar etapas manuais, não apenas movê-las para tela
2. **Confiança acima de velocidade** — dados consolidados devem ser auditáveis e rastreáveis
3. **Controller no controle** — regras de negócio configuráveis pelo usuário, sem dependência de TI
4. **Transparência radical** — todo cálculo visível, toda transformação logada
5. **Escala sem complexidade** — adicionar uma filial deve levar horas, não semanas
```

## Representação Visual

### Dados de amostra

- **Elevator pitch:** Plataforma de consolidação financeira automatizada para equipes de controladoria multi-filial
- **Diferenciais:** 5 itens (integração multi-ERP, regras no-code, custo 40% menor, trilha de auditoria, time-to-value 8 semanas)
- **Princípios:** 5 itens (automatizar vs digitalizar, confiança, controller no controle, transparência, escala)
- **Comparativo implícito:** FinTrack Pro vs Oracle HFM vs planilhas manuais

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa completa com elevator pitch, diferenciais e princípios em prosa | Quando o leitor precisa absorver a proposta de valor com contexto |
| Tabela | Matriz comparativa de diferenciais vs concorrentes (FinTrack vs Oracle HFM vs manual) | Para posicionamento competitivo claro |
| Highlight card | Card visual com elevator pitch em destaque, diferenciais como ícones/badges e princípios listados | Para apresentações executivas e pitch decks |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
