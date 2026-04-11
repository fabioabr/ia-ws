---
region-id: REG-DOM-AIML-01
title: "AI/ML Strategy"
group: domain
description: "Model type, approach, metrics, and lifecycle management for AI/ML projects"
source: "Bloco #5/#7 (arch)"
schema: "Tipo modelo + abordagem + métricas + ciclo vida"
template-visual: "Card com pipeline diagram"
when: ai-ml
default: false
---

# AI/ML Strategy

Define a estrategia de IA/ML do projeto, incluindo tipo de modelo, abordagem de treinamento, metricas de avaliacao e ciclo de vida. Esta regiao e essencial para projetos que incluem componentes de machine learning.

## Schema de dados

```yaml
aiml_strategy:
  models:
    - name: string
      type: string               # Classification, Regression, NLP, Computer Vision, etc.
      approach: string           # Pre-trained, Fine-tuned, Custom, AutoML
      framework: string          # PyTorch, TensorFlow, scikit-learn, etc.
      metrics: string[]          # Metricas de avaliacao
      lifecycle: string          # Batch retrain, Online learning, etc.
  infrastructure:
    training: string
    serving: string
    monitoring: string
```

## Exemplo

| Modelo | Tipo | Abordagem | Framework | Metricas |
|--------|------|-----------|-----------|----------|
| Categorizador de transacoes | Classificacao multi-label | Fine-tuned BERT | PyTorch + HuggingFace | F1-score >= 0.92, Precision >= 0.95 |
| Previsao de fluxo de caixa | Regressao temporal | Custom LSTM | TensorFlow | MAPE < 10%, R2 >= 0.85 |
| Deteccao de anomalias | Anomaly detection | Isolation Forest | scikit-learn | Recall >= 0.90, FPR < 5% |

**Ciclo de vida:** Re-treinamento semanal com dados novos; monitoramento de drift diario; rollback automatico se metricas caem abaixo do threshold.

## Representacao Visual

### Dados de amostra

```
Dados Brutos --> Pre-processamento --> Feature Engineering --> Treinamento
                                                                   |
                                                                   v
Monitoramento <-- Serving (API) <-- Validacao <-- Model Registry
    |
    v (drift detectado)
Re-treinamento automatico
```

| Modelo | F1-Score | Precision | Recall | Status |
|--------|---------|-----------|--------|--------|
| Categorizador | 0.94 | 0.96 | 0.92 | Producao |
| Previsao fluxo | MAPE 8.2% | R2 0.87 | - | Producao |
| Anomalias | - | FPR 3.1% | 0.93 | Staging |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada modelo com tipo, abordagem, metricas e ciclo de vida | Documentos de estrategia, relatorios executivos |
| Tabela | Tabela com modelos, tipos, frameworks e metricas-alvo | Referencia tecnica, catalogo de modelos |
| Diagrama de pipeline | Fluxo mostrando etapas do ciclo de vida ML (dados, treino, validacao, deploy, monitoramento) | Apresentacoes de arquitetura ML, onboarding do time de data science |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
