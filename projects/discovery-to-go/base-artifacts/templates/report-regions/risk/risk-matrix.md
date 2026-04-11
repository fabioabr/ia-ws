---
region-id: REG-RISK-01
title: "Risk Matrix"
group: risk
description: "Consolidated risk matrix with probability, impact, score, and mitigation actions"
source: "Fase 2 (auditor + 10th-man)"
schema: "Tabela (risco, probabilidade 1-5, impacto 1-5, score, mitigação, dono)"
template-visual: "Table com heatmap badges"
default: true
---

# Risk Matrix

Consolida todos os riscos identificados durante o discovery em uma matriz unica, com scores calculados (probabilidade x impacto). Cada risco inclui acao de mitigacao e responsavel. Os badges de heatmap permitem identificacao visual rapida dos riscos criticos.

## Schema de dados

```yaml
risk_matrix:
  risks:
    - id: string                 # Identificador (ex: RISK-01)
      description: string        # Descricao do risco
      category: string           # Tecnico / Negocio / Operacional / Regulatorio
      probability: number        # 1 (muito baixa) a 5 (muito alta)
      impact: number             # 1 (insignificante) a 5 (catastrofico)
      score: number              # probability * impact
      severity: string           # Critico (>=20) / Alto (>=12) / Medio (>=6) / Baixo (<6)
      mitigation: string         # Acao de mitigacao
      owner: string              # Responsavel pela mitigacao
```

## Exemplo

| ID | Risco | Prob | Impacto | Score | Severidade | Mitigacao | Dono |
|----|-------|------|---------|-------|------------|-----------|------|
| RISK-01 | Integracao Open Finance instavel | 4 | 5 | 20 | Critico | Circuit breaker + fallback com dados cached | Tech Lead |
| RISK-02 | Churn acima de 5% no primeiro trimestre | 3 | 4 | 12 | Alto | Onboarding guiado + health score do cliente | PO |
| RISK-03 | Vazamento de dados financeiros | 2 | 5 | 10 | Medio | Criptografia at-rest/in-transit + pentest trimestral | Security |
| RISK-04 | Atraso na aprovacao da App Store | 2 | 3 | 6 | Medio | Submissao antecipada + PWA como fallback | Mobile Lead |
| RISK-05 | Turnover de desenvolvedor-chave | 2 | 2 | 4 | Baixo | Documentacao de decisoes + pair programming | Engineering Manager |

## Representação Visual

### Dados de amostra

| ID | Risco | Probabilidade | Impacto | Score | Severidade |
|----|-------|--------------|---------|-------|------------|
| RISK-01 | Integração Open Finance instável | 4 | 5 | 20 | Crítico |
| RISK-02 | Churn acima de 5% no primeiro trimestre | 3 | 4 | 12 | Alto |
| RISK-03 | Vazamento de dados financeiros | 2 | 5 | 10 | Médio |
| RISK-04 | Atraso na aprovação da App Store | 2 | 3 | 6 | Médio |
| RISK-05 | Turnover de desenvolvedor-chave | 2 | 2 | 4 | Baixo |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo os riscos mais críticos, suas inter-relações e as estratégias de mitigação priorizadas | Comunicação executiva onde o contexto qualitativo dos riscos é mais importante que a classificação numérica |
| Tabela | Matriz completa com probabilidade, impacto, score, severidade, mitigação e dono, como no exemplo acima | Quando o leitor precisa de todos os detalhes para acompanhamento e gestão dos riscos |
| Bubble chart (probabilidade x impacto) | Gráfico de bolhas com eixo X = probabilidade, eixo Y = impacto, tamanho da bolha = score, cor = severidade | Visualizar a distribuição dos riscos no espaço probabilidade-impacto e identificar clusters de risco |
| 5x5 heatmap grid | Grid 5x5 com probabilidade nas colunas e impacto nas linhas, cada célula colorida por severidade, riscos posicionados na célula correspondente | Representação clássica de risk matrix — permite identificação visual imediata das zonas críticas |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
