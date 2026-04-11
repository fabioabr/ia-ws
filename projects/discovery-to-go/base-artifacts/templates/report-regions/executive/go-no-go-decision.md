---
region-id: REG-EXEC-03
title: "Go/No-Go Decision"
group: executive
description: "Veredicto final: prosseguir / pivotar / cancelar — com evidências por risco (value, usability, feasibility, viability) e condições para prosseguir"
source: "Consolidator"
schema: "table"
template-visual: "Card com status badges"
default: true
---

# Go/No-Go Decision

Avaliação estruturada de continuidade do projeto baseada nas quatro dimensões de risco de produto: valor (o mercado quer?), usabilidade (o usuário consegue usar?), viabilidade técnica (conseguimos construir?) e viabilidade de negócio (faz sentido financeiramente?). O veredicto final — prosseguir, pivotar ou cancelar — é fundamentado em evidências coletadas durante o discovery e acompanhado de condições obrigatórias para avançar.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| dimensoes | list | Cada item: `{ dimensao: string, status: "verde" | "amarelo" | "vermelho", evidencia: string, risco_residual: string }` |
| veredicto | string | `"prosseguir"`, `"pivotar"` ou `"cancelar"` |
| justificativa | string | 1-2 parágrafos fundamentando o veredicto |
| condicoes | list | Pré-requisitos obrigatórios para prosseguir (se veredicto = prosseguir) |
| ressalvas | list | Pontos de atenção que não bloqueiam mas exigem monitoramento |

## Exemplo

```markdown
## Go/No-Go Decision

### Avaliação por dimensão de risco

| Dimensão | Status | Evidência | Risco residual |
|----------|--------|-----------|----------------|
| **Value** (o mercado quer?) | 🟢 Verde | 4/4 stakeholders confirmam dor crítica; 3 erros materiais documentados em 6 meses | Baixo — problema validado com dados reais |
| **Usability** (o usuário consegue usar?) | 🟡 Amarelo | Wireframes validados com 2/4 analistas; falta teste com analistas das filiais remotas | Médio — validação parcial; planejar teste de usabilidade na Sprint 1 |
| **Feasibility** (conseguimos construir?) | 🟡 Amarelo | Stack definida e equipe capacitada; integração SAP R/3 é incerta (API legada) | Médio-alto — PoC de integração necessária antes do commit de escopo total |
| **Viability** (faz sentido financeiramente?) | 🟢 Verde | ROI positivo em 14 meses; TCO 40% menor que Oracle HFM; budget aprovado pela CFO | Baixo — números validados com equipe financeira |

### Veredicto

**PROSSEGUIR** com ressalva de viabilidade técnica.

O discovery confirma que o problema é real, urgente e mensurável. A solução proposta atende aos requisitos de negócio e o investimento é justificável. A principal incerteza é a integração com o SAP R/3 legado, que deve ser resolvida na Sprint 0 antes de comprometer o escopo completo do MVP.

### Condições obrigatórias para prosseguir

1. **PoC de integração SAP** concluída com sucesso na Sprint 0 (prazo: 30/05/2026)
2. **Validação de usabilidade** com pelo menos 1 analista de filial remota antes da Sprint 2
3. **Aprovação formal do budget** da Fase 1 pelo comitê de investimentos

### Ressalvas

- Mudanças regulatórias IFRS 16 previstas para Q1 2027 podem impactar regras de consolidação
- Equipe de sustentação pós-MVP ainda não definida — escalar discussão com RH na Fase 1
```

## Representação Visual

### Dados de amostra

| Dimensão | Status | Risco residual |
|----------|--------|----------------|
| Value | Verde | Baixo |
| Usability | Amarelo | Médio |
| Feasibility | Amarelo | Médio-alto |
| Viability | Verde | Baixo |

**Veredicto:** PROSSEGUIR
**Condições obrigatórias:** 3
**Ressalvas:** 2

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa com veredicto, justificativa e listas de condições/ressalvas | Quando o público precisa do contexto completo e da argumentação detalhada |
| Tabela | Grid de dimensões com status, evidência e risco residual | Quando o foco é a comparação rápida entre as 4 dimensões de risco |
| Semáforo (status badges) | Cards com indicador verde/amarelo/vermelho por dimensão + badge de veredicto | Quando o público é executivo e precisa de leitura instantânea do status |
| Radar chart | Gráfico radar com as 4 dimensões pontuadas (ex: verde=3, amarelo=2, vermelho=1) | Quando se deseja visualizar o equilíbrio entre dimensões de risco de forma sintética |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
