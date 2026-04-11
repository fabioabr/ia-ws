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
