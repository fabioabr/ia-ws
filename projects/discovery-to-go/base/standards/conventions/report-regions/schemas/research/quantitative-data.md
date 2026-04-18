---
region-id: REG-PESQ-04
title: "Quantitative Data"
group: research
description: "Fontes utilizadas, métricas-chave identificadas, tamanho do problema"
source: "Bloco #3 (po) → 1.3"
schema: "table"
template-visual: "Table com KPI highlights"
default: false
---

# Quantitative Data

Dados quantitativos coletados durante o discovery que dimensionam o problema e fundamentam a decisão de investimento. Inclui métricas de mercado, dados operacionais atuais, benchmarks do setor e dimensionamento da oportunidade. Cada métrica é acompanhada da fonte para garantir rastreabilidade e permitir que stakeholders avaliem a confiabilidade dos números.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| metricas | list | Cada item: `{ metrica: string, valor_atual: string, fonte: string, relevancia: string }` |
| tamanho_problema | object | `{ descricao: string, valor: string, composicao: list }` |
| benchmarks | list | Dados de mercado ou concorrentes para comparação |

## Exemplo

```markdown
## Dados Quantitativos

### Métricas-chave identificadas

| Métrica | Valor atual | Fonte | Relevância |
|---------|-------------|-------|------------|
| Tempo de fechamento consolidado | D+8 (média) | Controller — dados de 12 meses | Indicador primário de eficiência do processo |
| Horas semanais em consolidação por analista | 12h | Entrevistas com 4 analistas | Dimensiona custo operacional direto |
| Erros materiais em relatórios ao conselho | 3 em 6 meses | CFO — atas de conselho | Quantifica risco reputacional e regulatório |
| Custo médio hora/analista (carregado) | R$ 120 | RH — tabela salarial 2026 | Base para cálculo de ROI |
| Filiais no escopo | 12 (10 SAP + 2 TOTVS) | TI — inventário de sistemas | Define complexidade de integração |
| Tempo de auditoria para reconstruir trilha | 2 semanas por ciclo | Auditor interno | Custo oculto de falta de rastreabilidade |
| Best practice de mercado para fechamento | D+2 a D+3 | Gartner — FP&A Benchmark 2025 | Referência de target |

### Tamanho do problema

**Impacto anual estimado: R$ 500K — R$ 700K**

| Componente | Valor anual | Cálculo |
|-----------|-------------|---------|
| Horas desperdiçadas em trabalho manual | R$ 230K | 4 analistas × 10h/semana × 48 semanas × R$ 120/h |
| Custo de retrabalho por erros | R$ 80K | 6 ciclos de retrabalho/ano × 40h × R$ 120/h + custo de auditoria |
| Custo de oportunidade do fechamento tardio | R$ 150K | Estimativa conservadora: decisões atrasadas em 6 dias |
| Risco regulatório (multa potencial) | R$ 40K — R$ 240K | Faixa de penalidades CVM por erros em demonstrações |

### Benchmarks de mercado

| Referência | Valor | Fonte |
|-----------|-------|-------|
| Empresas mid-market com consolidação automatizada — fechamento médio | D+2 | Gartner FP&A Benchmark 2025 |
| Custo de Oracle HFM (licença + implantação) para 12 filiais | R$ 4,2M / 3 anos | Cotação Oracle via parceiro |
| Custo de SAP BPC para escopo similar | R$ 3,8M / 3 anos | Cotação SAP via Deloitte |
| Adoção de ferramentas de consolidação automatizada no Brasil (mid-market) | 23% | KPMG — Pesquisa CFO 2025 |
```

## Representação Visual

### Dados de amostra

- **7 métricas-chave:** Tempo de fechamento (D+8), Horas semanais (12h/analista), Erros materiais (3 em 6 meses), Custo hora/analista (R$ 120), Filiais (12), Tempo de auditoria (2 semanas), Best practice (D+2 a D+3)
- **Impacto anual estimado:** R$ 500K -- R$ 700K em 4 componentes (horas desperdiçadas R$ 230K, retrabalho R$ 80K, oportunidade R$ 150K, risco regulatório R$ 40K--R$ 240K)
- **3 benchmarks de mercado:** fechamento automatizado (D+2), Oracle HFM (R$ 4,2M/3 anos), SAP BPC (R$ 3,8M/3 anos)

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela + stat cards
**Tecnologia:** HTML/CSS
**Justificativa:** Com 7 métricas-chave, tabelas estruturadas preservam a rastreabilidade fonte-valor, enquanto stat cards destacam os KPIs principais (D+8, R$ 500K-700K) para leitura executiva rápida. Se houver 5+ métricas com comparação atual vs. benchmark, complementar com bar chart (Chart.js).
**Alternativa:** Bar chart (Chart.js) — quando a prioridade é evidenciar visualmente a magnitude das diferenças entre componentes de custo ou métricas atuais vs. benchmark
