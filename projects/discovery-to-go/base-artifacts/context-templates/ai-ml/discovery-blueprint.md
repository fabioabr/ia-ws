---
title: Discovery Blueprint — AI and Machine Learning
pack-id: ai-ml
description: Blueprint completo de discovery para projetos de IA e Machine Learning — modelos preditivos, NLP, computer vision, LLM apps, MLOps. Documento único e auto-contido.
version: 01.00.000
status: ativo
author: claude-code
category: discovery-blueprint
area: tecnologia
tags:
  - discovery-blueprint
  - ai-ml
  - machine-learning
  - mlops
  - llm
created: 2026-04-11
---

# Discovery Blueprint — AI and Machine Learning

Documento completo para conduzir o discovery de projetos envolvendo IA e Machine Learning. Cobre desde modelos preditivos clássicos até aplicações com LLMs, incluindo MLOps e governança de modelos. Organizado em **4 componentes**.

---

## Quando usar este blueprint

- Menção a "inteligência artificial", "machine learning", "modelo preditivo", "deep learning"
- Termos: NLP, computer vision, LLM, RAG, fine-tuning, embeddings, GPT, Claude
- Stack: TensorFlow, PyTorch, scikit-learn, Hugging Face, LangChain, MLflow, SageMaker
- Termos: feature engineering, training, inference, serving, model drift
- Necessidade de previsão, classificação, recomendação, geração de conteúdo, extração de informações

---

## Visão geral dos componentes

```mermaid
flowchart LR
    S["Dados\nBrutos"] --> A["1. Dados\ne Features"]
    A --> B["2. Desenvolvimento\nde Modelos"]
    B --> C["3. MLOps\ne Serving"]
    C --> D["4. Monitoring\ne Governança"]
    D --> U["Decisões\nde Negócio"]

    style A fill:#2EB5F5,color:#1A1923
    style B fill:#F4AC00,color:#1A1923
    style C fill:#9B96FF,color:#1A1923
    style D fill:#0ED145,color:#1A1923
```

| # | Componente | O que define | Blocos do discovery |
|---|-----------|-------------|-------------------|
| 1 | Dados e Features | De onde vêm os dados, feature engineering, feature store | #4, #5 |
| 2 | Desenvolvimento de Modelos | Tipo de modelo, treinamento, experimentação, avaliação | #5, #7 |
| 3 | MLOps e Serving | Deploy, pipeline de treino, inferência, escalabilidade | #5, #7, #8 |
| 4 | Monitoring e Governança | Drift, bias, explicabilidade, compliance, ciclo de vida | #4, #6, #7, #8 |

---

## Componente 1 — Dados e Features

ML é data-centric: a qualidade do modelo é limitada pela qualidade dos dados. Este componente mapeia origens de dados, define features e avalia se há dados suficientes para treinar.

### Concerns

- **Dados disponíveis** — Quais dados existem? Estruturados (tabelas) ou não-estruturados (texto, imagem, áudio)?
- **Volume e qualidade** — Há dados suficientes para treinar? Quão limpos estão? % de missing values, outliers?
- **Labeling** — Os dados precisam ser rotulados? Quem rotula? Qual o custo? Crowdsourcing, especialistas, semi-supervised?
- **Feature engineering** — Quais features são relevantes? Derivadas de quais dados? Janela temporal?
- **Feature store** — Precisa de feature store para reutilização? Online (real-time serving) vs offline (batch training)?
- **Data freshness** — Frequência de atualização dos dados de treinamento vs dados de inferência?
- **Bias nos dados** — Dados representam adequadamente todas as classes/grupos? Viés histórico?
- **PII nos dados de treinamento** — Dados pessoais usados no treino? Anonimização? Consentimento?

### Perguntas-chave

1. Quais dados estão disponíveis? (listar fontes, tipo, volume, qualidade)
2. Os dados precisam ser rotulados? Se sim, quem faz e com que custo?
3. Há dados suficientes para treinar um modelo? (order of magnitude: centenas, milhares, milhões)
4. Quais features são candidatas? Já existe feature engineering ou começa do zero?
5. Precisa de feature store para reutilização entre modelos?
6. Os dados de treino contêm PII? Como anonimizar?
7. Há risco de viés nos dados? (sub-representação de grupos, viés histórico)
8. Com que frequência os dados de treinamento são atualizados?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Abordagem de labeling | Manual / Semi-supervised / Self-supervised / Pre-labeled | Volume, custo, qualidade necessária |
| Feature store | Online+Offline (Feast/Tecton) / Apenas offline / Sem feature store | Número de modelos, reuso, latência |
| Tratamento de PII | Anonimização / Pseudonimização / Dados sintéticos / Consentimento | Regulação, tipo de modelo |
| Tratamento de bias | Re-sampling / Re-weighting / Data augmentation / Auditoria | Impacto do viés na decisão |

### Critérios de completude

- [ ] Fontes de dados listadas com volume, tipo e qualidade
- [ ] Estratégia de labeling definida (se aplicável)
- [ ] Features candidatas identificadas
- [ ] Riscos de bias avaliados
- [ ] PII em dados de treinamento mapeada com estratégia de tratamento
- [ ] Frequência de atualização definida

---

## Componente 2 — Desenvolvimento de Modelos

Define o tipo de modelo, abordagem de treinamento, framework de experimentação e critérios de avaliação. O discovery não treina modelos — define os requisitos para que o time possa.

### Concerns

- **Tipo de problema** — Classificação, regressão, clustering, NLP, computer vision, geração (LLM), recomendação?
- **Abordagem** — ML clássico (XGBoost, Random Forest), deep learning (PyTorch, TF), LLM (API ou fine-tune), regras heurísticas como baseline?
- **LLM vs modelo custom** — Para NLP/geração: usar LLM via API (Claude, GPT) ou treinar modelo próprio? RAG vs fine-tuning?
- **Framework** — scikit-learn, PyTorch, TensorFlow, Hugging Face, LangChain?
- **Experimentação** — Como rastrear experimentos? MLflow, Weights & Biases, Neptune?
- **Métricas de avaliação** — Accuracy, precision, recall, F1, AUC, BLEU, perplexity? Qual métrica importa para o negócio?
- **Baseline** — Qual é o baseline? Regra simples? Modelo existente? Random?
- **Computação para treino** — GPU necessária? Quanto? Cloud (SageMaker, Vertex AI) ou on-prem?

### Perguntas-chave

1. Qual problema o modelo resolve? (classificação, previsão, geração, extração, recomendação)
2. Existe baseline hoje? (regra manual, modelo existente, nenhum)
3. Para NLP/geração: LLM via API basta ou precisa de modelo próprio? RAG vs fine-tuning?
4. Qual métrica define "sucesso" do modelo? (accuracy, latência, custo por inferência)
5. Qual framework? Já existe expertise no time?
6. Precisa de GPU para treinamento? Quanto compute?
7. Como rastrear experimentos? (MLflow, W&B, custom)
8. Qual a frequência de re-treinamento esperada? (diária, semanal, mensal, ad-hoc)

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Abordagem | ML clássico / Deep learning / LLM API / LLM fine-tuned / Híbrido | Complexidade, dados disponíveis, latência |
| LLM strategy | API (Claude/GPT) / RAG / Fine-tuning / Self-hosted | Custo, privacidade, customização |
| Framework | scikit-learn / PyTorch / TensorFlow / Hugging Face | Skills do time, tipo de modelo |
| Experiment tracking | MLflow / W&B / Neptune / Custom | Maturidade, budget |
| Compute | CPU / GPU cloud (SageMaker/Vertex) / GPU on-prem | Volume de treino, custo |

### Critérios de completude

- [ ] Tipo de problema definido (classificação, geração, etc.)
- [ ] Abordagem de modelagem escolhida (ML clássico, DL, LLM, híbrido)
- [ ] Métrica de sucesso do modelo definida e alinhada com negócio
- [ ] Baseline definido para comparação
- [ ] Framework e infra de treino definidos
- [ ] Frequência de re-treinamento estimada

---

## Componente 3 — MLOps e Serving

Como o modelo sai do notebook e vai para produção. Define pipeline de treino automatizado, deploy, inferência e escalabilidade.

### Concerns

- **Pipeline de treino** — Automatizado (Kubeflow, SageMaker Pipelines, Vertex Pipelines) ou manual?
- **Model registry** — Onde versionam modelos? MLflow, SageMaker Model Registry, custom?
- **Deploy** — REST API, batch prediction, streaming, edge? Canary/blue-green?
- **Inferência** — Online (real-time, < 100ms) ou offline (batch, D+1)?
- **Latência** — Qual a latência máxima aceitável por inferência?
- **Escalabilidade** — Auto-scaling de endpoints? Quantas req/s no pico?
- **Custo de inferência** — Para LLM: custo por token. Para custom: custo de GPU/CPU por req
- **A/B testing** — Como testar novo modelo vs atual em produção?
- **Rollback** — Se modelo novo é pior, como reverter rapidamente?

### Perguntas-chave

1. O modelo serve predições em real-time ou batch?
2. Qual a latência máxima aceitável? (< 50ms, < 500ms, < 5s, não importa)
3. Quantas inferências por segundo no pico?
4. Como deployar? REST API, gRPC, batch job, embedded no app?
5. Pipeline de treino automatizado ou manual (notebook)?
6. Como versionar modelos? Existe model registry?
7. Como testar modelo novo vs atual em produção? (A/B, shadow, canary)
8. Para LLMs: qual o custo estimado por chamada? Budget mensal?
9. Como fazer rollback se modelo novo degradar?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Tipo de serving | Online REST / Batch / Streaming / Edge | Latência, volume, caso de uso |
| Pipeline de treino | Kubeflow / SageMaker / Vertex / Airflow + custom | Maturidade, cloud provider |
| Model registry | MLflow / SageMaker / Vertex / Custom | Integração com pipeline |
| Deploy strategy | Canary / Blue-green / Shadow / Direct | Risco, tráfego |
| LLM hosting | API externa (Claude/GPT) / Self-hosted (vLLM/TGI) | Custo, privacidade, latência |

### Critérios de completude

- [ ] Tipo de serving definido (online/batch/streaming)
- [ ] Latência e throughput requirements documentados
- [ ] Pipeline de treino automatizado ou roadmap para automatizar
- [ ] Model registry definido
- [ ] Estratégia de deploy e rollback documentada
- [ ] Custo de inferência estimado

---

## Componente 4 — Monitoring e Governança

Modelo em produção degrada silenciosamente. Monitoring de drift, bias, performance e governança (explicabilidade, compliance) garantem que o modelo continue útil e seguro.

### Concerns

- **Model drift** — Data drift (distribuição dos inputs muda) e concept drift (relação input→output muda). Como detectar?
- **Performance monitoring** — Métricas do modelo em produção vs treino. Degradação gradual?
- **Bias monitoring** — Modelo discrimina grupos protegidos? Métricas de fairness?
- **Explicabilidade** — Modelo precisa explicar suas decisões? SHAP, LIME, attention weights?
- **Compliance** — Regulação exige explicabilidade? (ex: crédito, saúde, seguros). AI Act?
- **Ciclo de vida** — Quando re-treinar? Quando aposentar um modelo? Governança de versões?
- **Human-in-the-loop** — Decisões críticas precisam de validação humana? Threshold de confiança?
- **Custo contínuo** — Custo mensal de inferência, monitoring, re-treinamento, storage de dados

### Perguntas-chave

1. Como detectar que o modelo está degradando em produção? (drift, performance)
2. O modelo toma decisões sobre pessoas? (crédito, saúde, contratação — compliance)
3. Precisa de explicabilidade? Para quem? (regulador, cliente, analista)
4. Com que frequência o modelo será re-treinado?
5. Existe threshold de confiança abaixo do qual um humano revisa a decisão?
6. Quem é responsável pelo modelo em produção? (ML engineer, data scientist, SRE)
7. Qual o budget mensal contínuo? (inferência + monitoring + re-treino + storage)
8. Como auditar decisões do modelo? Logs de predições são armazenados?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Drift detection | Evidently / NannyML / Custom / SageMaker Monitor | Volume, maturidade |
| Explicabilidade | SHAP / LIME / Attention / Nenhum | Regulação, audiência |
| Human-in-the-loop | Threshold de confiança / Sampling / Sempre / Nunca | Risco da decisão |
| Re-treinamento | Scheduled / Triggered by drift / Manual | Custo, velocidade de drift |
| Logging | Todas as predições / Sampling / Apenas erros | Volume, compliance |

### Critérios de completude

- [ ] Estratégia de monitoring de drift definida
- [ ] Requisitos de explicabilidade e compliance mapeados
- [ ] Ciclo de re-treinamento definido (gatilho e frequência)
- [ ] Human-in-the-loop definido para decisões críticas
- [ ] Budget mensal contínuo estimado
- [ ] Responsável pelo modelo em produção identificado

---

## Concerns transversais — Produto e Organização

- Qual problema de negócio o ML resolve? (não é "usar IA" — é "prever X para decidir Y")
- Qual o impacto de uma predição errada? (inconveniente vs perda financeira vs risco de vida)
- OKRs: accuracy do modelo, tempo economizado, receita incrementada, custo evitado
- Time: data scientist, ML engineer, data engineer — quem faz o quê?
- Sinais de resposta incompleta:
  - "Queremos usar IA" (sem problema definido)
  - "O modelo vai decidir tudo" (sem human-in-the-loop)
  - "Dados? Temos bastante" (sem validar qualidade e representatividade)

---

## Concerns transversais — Privacidade (bloco #6)

- Dados pessoais nos dados de treinamento? Consentimento para uso em ML?
- Modelo reproduz ou amplifica viés contra grupos protegidos?
- Decisões automatizadas sobre pessoas? (art. 20 LGPD — direito a revisão humana)
- Dados de produção (inferência) logados com PII?
- LLMs: dados do prompt são enviados para API externa? Data residency?
- Dados sintéticos como alternativa para treinamento sem PII real

---

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|-------------|----------------|
| 1 | **Começar pelo modelo, não pelo dado** | Modelo sofisticado com dados ruins = resultado ruim |
| 2 | **ML quando regra simples basta** | Over-engineering — 80% dos casos são resolvidos com heurísticas |
| 3 | **Treinar e esquecer** | Modelo degrada com data drift — precisa de monitoring contínuo |
| 4 | **Notebook em produção** | Sem pipeline, sem versionamento, sem reproducibilidade |
| 5 | **Métricas offline ≠ métricas de negócio** | F1 de 95% mas sem impacto no KPI de negócio |
| 6 | **LLM para tudo** | Custo alto, latência alta, quando retrieval ou classificador simples bastaria |
| 7 | **Sem baseline** | Não sabe se o modelo é melhor que random ou regra manual |
| 8 | **Ignorar bias** | Modelo discriminatório em produção — risco legal e reputacional |
| 9 | **Fine-tuning sem necessidade** | RAG com prompt engineering resolve a maioria dos casos de LLM |
| 10 | **Sem human-in-the-loop em decisões críticas** | Modelo errado toma decisão irreversível |

---

## Edge cases para o 10th-man verificar

- Modelo toma decisão de crédito e erra — quem é responsável legalmente?
- Data drift após evento macroeconômico (pandemia, crise) — modelo ainda serve?
- LLM hallucination gera informação falsa usada em decisão de negócio — como prevenir?
- Custo de inferência LLM explode 5x após go-live — é sustentável?
- Modelo treinado com dados enviesados nega crédito para grupo protegido — e agora?
- Pipeline de treino falha silenciosamente — modelo em produção fica desatualizado por meses?
- Concorrente lança modelo similar — diferenciação está no modelo ou nos dados?
- Regulação muda (AI Act, LGPD) — modelo precisa ser explicável retroativamente?

---

## Custom-specialists disponíveis

| Specialist | Domínio | Quando invocar |
|-----------|---------|----------------|
| `nlp-specialist` | NLP (classificação de texto, NER, sentiment, summarization) | Problema de linguagem natural |
| `computer-vision` | Computer vision (detecção, segmentação, OCR) | Problema de imagem/vídeo |
| `llm-architect` | Arquitetura de aplicações com LLM (RAG, agents, fine-tuning) | Aplicação usando LLM |
| `mlops-engineer` | MLOps (pipelines, serving, monitoring, model registry) | Necessidade de produtização de modelos |
| `recommendation-system` | Sistemas de recomendação (collaborative, content-based, hybrid) | Recomendação de produtos/conteúdo |
| `time-series-forecast` | Séries temporais e forecasting | Previsão de demanda, vendas, métricas |
| `ai-ethics-compliance` | Ética em IA, fairness, explicabilidade, regulação | Decisões sobre pessoas, compliance |
| `feature-engineering` | Feature engineering e feature store | Dados complexos, muitas features |

---

## Perfil do Delivery Report

### Seções extras no relatório

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Estratégia de ML** | Entre Visão de Produto e Organização | Tipo de problema, abordagem (ML clássico/DL/LLM), métricas de sucesso, dados necessários, ciclo de vida do modelo |

### Métricas obrigatórias no relatório

| Métrica | Onde incluir |
|---------|-------------|
| Métrica de sucesso do modelo (accuracy, F1, etc.) | Métricas-chave |
| Latência de inferência | Métricas-chave |
| Custo mensal de inferência | Análise Estratégica |
| Custo de re-treinamento | Análise Estratégica |
| Volume de dados de treinamento | Estratégia de ML |
| Frequência de re-treinamento | Estratégia de ML |

### Diagramas obrigatórios

| Diagrama | Seção destino |
|----------|---------------|
| Arquitetura macro | Tecnologia e Segurança |
| Pipeline ML (dados → treino → deploy → monitoring) | Estratégia de ML |

### Ênfases por seção base

| Seção base | Ênfase |
|------------|--------|
| **Tecnologia e Segurança** | Framework ML, infra de treino/serving, integração com apps |
| **Privacidade e Compliance** | PII em dados de treino, explicabilidade, decisão automatizada (art. 20 LGPD) |
| **Análise Estratégica** | Build vs Buy (modelo custom vs API LLM), TCO incluindo re-treino e monitoring |
| **Matriz de Riscos** | Model drift, bias, hallucination, custo de LLM, dependência de provedor |

---

## Mapeamento para os 8 Blocos do Discovery

| Componente | Bloco(s) principal(is) | Agente responsável |
|------------|----------------------|-------------------|
| **1. Dados e Features** | #4 (Processo/Equipe), #5 (Tech) | po, solution-architect |
| **2. Desenvolvimento de Modelos** | #5 (Tech), #7 (Arquitetura Macro) | solution-architect |
| **3. MLOps e Serving** | #5 (Tech), #7 (Arch), #8 (TCO) | solution-architect |
| **4. Monitoring e Governança** | #4 (Processo), #6 (Privacy), #7 (Arch), #8 (TCO) | po, cyber-security-architect, solution-architect |

---

## Regions do Delivery Report

Regions de informação que o delivery report deve conter para projetos AI/ML. Referência completa: `templates/report-regions/information-regions.md`.

### Obrigatórias

Regions que **sempre** aparecem no delivery report deste tipo de projeto.

| ID | Nome | Justificativa |
|----|------|---------------|
| REG-EXEC-01 | Overview one-pager | Default: Todos |
| REG-EXEC-02 | Product brief | Default: Todos |
| REG-EXEC-03 | Decisão de continuidade | Default: Todos |
| REG-EXEC-04 | Próximos passos | Default: Todos |
| REG-PROD-01 | Problema e contexto | Default: Todos |
| REG-PROD-02 | Personas | Default: Todos |
| REG-PROD-04 | Proposta de valor | Default: Todos |
| REG-PROD-05 | OKRs e ROI | Default: Todos |
| REG-PROD-07 | Escopo | Default: Todos |
| REG-ORG-01 | Mapa de stakeholders | Default: Todos |
| REG-ORG-02 | Estrutura de equipe | Default: Todos |
| REG-TECH-01 | Stack tecnológica | Default: Todos |
| REG-TECH-02 | Integrações | Default: Todos |
| REG-TECH-03 | Arquitetura macro | Default: Todos |
| REG-TECH-06 | Build vs Buy | Default: Todos |
| REG-SEC-01 | Classificação de dados | Default: Todos |
| REG-SEC-02 | Autenticação e autorização | Default: Todos |
| REG-SEC-04 | Compliance e regulação | Default: Todos |
| REG-PRIV-01 | Dados pessoais mapeados | ML quase sempre usa dados pessoais para treinamento |
| REG-PRIV-02 | Base legal LGPD | ML quase sempre usa dados pessoais para treinamento |
| REG-PRIV-03 | DPO e responsabilidades | ML quase sempre usa dados pessoais para treinamento |
| REG-PRIV-04 | Política de retenção | ML quase sempre usa dados pessoais para treinamento |
| REG-FIN-01 | TCO 3 anos | Default: Todos |
| REG-FIN-05 | Estimativa de esforço | Default: Todos |
| REG-RISK-01 | Matriz de riscos | Default: Todos |
| REG-RISK-02 | Riscos técnicos | Default: Todos |
| REG-RISK-03 | Hipóteses críticas não validadas | Default: Todos |
| REG-QUAL-01 | Score do auditor | Default: Todos |
| REG-QUAL-02 | Questões do 10th-man | Default: Todos |
| REG-BACK-01 | Épicos priorizados | Default: Todos |
| REG-METR-01 | KPIs de negócio | Default: Todos |
| REG-NARR-01 | Como chegamos aqui | Default: Todos |

### Opcionais

Regions que podem ser incluídas conforme necessidade do projeto.

| ID | Nome | Quando incluir |
|----|------|----------------|
| REG-PESQ-01 | Relatório de entrevistas | Quando houver entrevistas com usuários ou stakeholders |
| REG-PESQ-02 | Citações representativas | Quando houver quotes relevantes de entrevistas |
| REG-PESQ-03 | Mapa de oportunidades | Quando houver Opportunity Solution Tree |
| REG-PESQ-04 | Dados quantitativos | Quando houver métricas quantitativas de pesquisa |
| REG-PESQ-05 | Source tag summary | Quando houver distribuição de fontes (briefing/RAG/inference) |
| REG-TECH-04 | Arquitetura de containers | Quando a arquitetura justificar C4 L2 (ML pipeline containers) |
| REG-METR-05 | DORA metrics | Quando houver necessidade de métricas de engenharia de plataforma |

### Domain-specific

Regions específicas do context-template `ai-ml` — sempre incluídas neste tipo de projeto.

| ID | Nome | Descrição |
|----|------|-----------|
| REG-DOM-AIML-01 | Estratégia de ML | Tipo de modelo, abordagem, métricas, dados, ciclo de vida |
| REG-DOM-AIML-02 | Model governance | Drift detection, bias monitoring, explicabilidade, compliance |
