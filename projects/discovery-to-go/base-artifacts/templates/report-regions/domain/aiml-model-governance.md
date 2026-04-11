---
region-id: REG-DOM-AIML-02
title: "AI/ML Model Governance"
group: domain
description: "Model governance covering drift, bias, explainability, and compliance"
source: "Bloco #5/#7 (arch)"
schema: "Drift/bias/explicabilidade/compliance"
template-visual: "Card com checklist"
when: ai-ml
default: false
---

# AI/ML Model Governance

Define as politicas de governanca de modelos de IA/ML, cobrindo deteccao de drift, mitigacao de bias, explicabilidade e compliance regulatorio. Modelos em producao sem governanca representam risco operacional e regulatorio significativo.

## Schema de dados

```yaml
model_governance:
  drift_detection:
    method: string
    frequency: string
    threshold: string
    action: string
  bias_mitigation:
    approach: string
    protected_attributes: string[]
    testing_frequency: string
  explainability:
    method: string               # SHAP, LIME, feature importance
    audience: string             # Tecnico / Negocio / Regulador
  compliance:
    regulations: string[]
    audit_frequency: string
```

## Exemplo

| Aspecto | Politica | Frequencia |
|---------|----------|-----------|
| Deteccao de drift | PSI (Population Stability Index) > 0.2 dispara alerta | Diaria |
| Mitigacao de bias | Auditoria de fairness por segmento (porte empresa, regiao) | Mensal |
| Explicabilidade | SHAP values disponiveis para cada previsao; dashboard para PO | Continuo |
| Compliance LGPD | Consentimento explicito para uso de dados em treinamento; direito ao esquecimento implementado | Auditoria trimestral |
| Model registry | Todas as versoes versionadas no MLflow com metricas e artefatos | A cada deploy |
