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
