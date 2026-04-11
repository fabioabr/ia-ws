---
region-id: REG-PESQ-05
title: "Source Tag Summary"
group: research
description: "Distribuição % BRIEFING / % RAG / % INFERENCE"
source: "Interview log"
schema: "kpi"
template-visual: "Stat cards ou pie chart"
default: false
---

# Source Tag Summary

Resumo da distribuição das fontes de informação utilizadas no discovery, classificadas por source tag: BRIEFING (informação fornecida diretamente pelo cliente), RAG (informação recuperada de documentos e bases de conhecimento) e INFERENCE (informação inferida pelo especialista quando não havia dados diretos). Esta transparência permite que stakeholders avaliem a confiabilidade das recomendações e identifiquem áreas onde validação adicional pode ser necessária.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| distribuicao | object | `{ briefing_pct: number, rag_pct: number, inference_pct: number }` |
| total_respostas | number | Número total de respostas/data points classificados |
| detalhamento_por_bloco | list | Cada item: `{ bloco: string, briefing_pct: number, rag_pct: number, inference_pct: number }` |
| observacoes | list | Notas sobre áreas com alta inferência ou baixa cobertura |

## Exemplo

```markdown
## Source Tag Summary

### Distribuição geral

| Source Tag | % | Descrição |
|-----------|---|-----------|
| **BRIEFING** | 65% | Informação fornecida diretamente pelo cliente em entrevistas ou documentos |
| **INFERENCE** | 25% | Informação inferida pelo especialista com base em padrões de mercado |
| **RAG** | 10% | Informação recuperada de bases de conhecimento e documentação técnica |

**Total de data points classificados:** 142

### Distribuição por bloco do discovery

| Bloco | BRIEFING | RAG | INFERENCE |
|-------|----------|-----|-----------|
| 1. Produto (problema, valor, escopo) | 80% | 5% | 15% |
| 2. Personas e jornadas | 75% | 0% | 25% |
| 3. Negócio (OKRs, ROI, pricing) | 50% | 15% | 35% |
| 4. Organização (equipe, stakeholders) | 90% | 0% | 10% |
| 5. Arquitetura (stack, integrações) | 60% | 20% | 20% |
| 6. Segurança e privacidade | 30% | 25% | 45% |
| 7. Diagramas (C4) | 40% | 10% | 50% |
| 8. Financeiro (TCO, Build vs Buy) | 55% | 20% | 25% |

### Observações

- **Segurança e privacidade (45% INFERENCE):** cliente não tinha políticas formais de segurança — recomendações foram baseadas em boas práticas de mercado. Validação com equipe de segurança do cliente é recomendada.
- **Diagramas C4 (50% INFERENCE):** arquitetura inferida a partir de descrições verbais e documentação parcial do SAP. Revisão técnica com equipe de TI é necessária antes de implementação.
- **Produto (80% BRIEFING):** alto nível de confiança — problema e contexto foram amplamente detalhados pelo cliente em entrevistas diretas.
```

## Representação Visual

### Dados de amostra

- **Distribuição geral:** BRIEFING 65%, INFERENCE 25%, RAG 10% (142 data points)
- **8 blocos do discovery** com distribuição variando de 30% a 90% BRIEFING
- **Blocos com maior inferência:** Diagramas C4 (50%), Segurança e privacidade (45%), Negócio (35%)
- **Blocos com maior confiança:** Organização (90% BRIEFING), Produto (80% BRIEFING)

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa explicando a distribuição geral e destacando áreas de alta inferência que requerem validação | Quando o contexto e as implicações de cada percentual precisam ser comunicados em detalhe |
| Tabela | Tabela com colunas por source tag e linhas por bloco, incluindo total geral e destaques condicionais | Quando stakeholders precisam consultar a distribuição exata por bloco rapidamente |
| Pie chart / Donut | Gráfico de pizza ou donut mostrando a proporção BRIEFING/RAG/INFERENCE na visão geral e por bloco | Quando o objetivo é comunicar visualmente a composição das fontes e evidenciar a proporção de inferência |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
