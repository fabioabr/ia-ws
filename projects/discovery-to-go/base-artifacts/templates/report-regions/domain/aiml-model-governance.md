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

## Representacao Visual

### Dados de amostra

| Aspecto | Metrica | Valor Atual | Threshold | Status |
|---------|---------|-------------|-----------|--------|
| Drift (PSI) | Population Stability Index | 0.08 | < 0.2 | OK |
| Bias (porte empresa) | Disparate Impact Ratio | 0.92 | >= 0.8 | OK |
| Bias (regiao) | Disparate Impact Ratio | 0.75 | >= 0.8 | ALERTA |
| Explicabilidade | SHAP coverage | 100% | 100% | OK |
| Compliance LGPD | Consentimentos validos | 99.8% | >= 99% | OK |
| Model versions | Versoes no MLflow | 12 | N/A | INFO |

### Recomendacao do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com checklist/status
**Tecnologia:** HTML/CSS
**Justificativa:** Os itens de governanca sao aspectos independentes com metricas, thresholds e status (OK/ALERTA). Cards com indicadores semaforo (verde/amarelo/vermelho) por aspecto, mostrando valor atual vs threshold, comunicam conformidade de forma imediata e sao faceis de escanear.
**Alternativa:** Tabela com badges de status (HTML/CSS) — quando houver muitos aspectos (10+) e a densidade de informacao exigir formato mais compacto.
