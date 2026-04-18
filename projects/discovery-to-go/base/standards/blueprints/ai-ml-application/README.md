---
title: "Aplicação de IA / ML — Blueprint"
description: "Sistema que treina, serve ou consome modelos de machine learning. Pode incluir fine-tuning, RAG, inference API, feature store ou integração de IA em produto existente."
category: project-blueprint
type: ai-ml-application
status: rascunho
created: 2026-04-13
---

# Aplicação de IA / ML

## Descrição

Sistema que treina, serve ou consome modelos de machine learning. Pode incluir fine-tuning, RAG, inference API, feature store ou integração de IA em produto existente. O escopo vai desde chatbots com LLM até pipelines de treinamento de modelos custom com MLOps completo, passando por integrações de IA generativa em produtos existentes.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda aplicação de IA/ML é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Chatbot / Assistente Conversacional

Agente baseado em LLM (GPT, Claude, Gemini, Llama) integrado a um produto ou canal de atendimento. Pode usar RAG (Retrieval-Augmented Generation) para responder com base em documentação proprietária. O foco é qualidade das respostas, latência percebida pelo usuário, guardrails contra alucinações e custo por requisição. Não envolve treinamento de modelo — consome APIs de providers ou modelos open-source servidos via inference endpoint. Exemplos: chatbot de suporte ao cliente, assistente de vendas, copilot para documentação interna, assistente jurídico.

### V2 — RAG Pipeline / Knowledge Base

Pipeline de ingestão, chunking, embedding e retrieval de documentos para alimentar um sistema de perguntas e respostas ou busca semântica. O foco é qualidade do retrieval (precision e recall dos chunks recuperados), estratégia de chunking, escolha do vector store e manutenção do índice quando documentos são atualizados ou removidos. Pode ou não ter um LLM na ponta — alguns sistemas usam RAG apenas para busca semântica sem geração. Exemplos: base de conhecimento corporativa, busca em contratos, análise de documentos regulatórios, FAQ inteligente.

### V3 — Inference API / Model Serving

API que serve predições de um modelo treinado (classificação, regressão, detecção, recomendação) para consumo por outros sistemas. O foco é latência de inferência, throughput, versionamento de modelos, estratégia de rollback e monitoramento de drift. Pode servir modelos proprietários treinados internamente ou modelos open-source fine-tunados. Exemplos: API de scoring de crédito, classificador de imagens para controle de qualidade, sistema de recomendação de produtos, detector de fraude em tempo real.

### V4 — ML Pipeline / Treinamento Custom

Pipeline completo de treinamento: coleta de dados, feature engineering, treinamento, avaliação, registro de modelo e promoção para produção. Envolve MLOps — versionamento de dados, experimentos rastreados, reprodutibilidade de treinos, e CI/CD de modelos. O foco é governança do ciclo de vida do modelo, reprodutibilidade e automação do re-treino. Exemplos: modelo de churn prediction, forecasting de demanda, detecção de anomalias em séries temporais, NLP custom para domínio específico.

### V5 — IA Embarcada em Produto Existente

Integração de capacidades de IA (geração de texto, classificação, extração de entidades, sumarização, tradução) em um produto já existente como feature incremental. O foco é design da experiência do usuário com IA (como apresentar resultados probabilísticos, como tratar falhas do modelo, fallback para fluxo sem IA), latência aceitável dentro do fluxo existente, e custo incremental por uso. Exemplos: autocompletar inteligente em editor de texto, classificação automática de tickets, sugestão de respostas em helpdesk, extração de dados de documentos uploadados.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | LLM / Modelo | Orquestração | Vector Store | Infra | Observações |
|---|---|---|---|---|---|
| V1 — Chatbot | OpenAI GPT-4o, Claude, Llama 3 | LangChain, LlamaIndex, Semantic Kernel | Pinecone, Qdrant, pgvector | Vercel AI SDK, AWS Lambda, Cloud Run | Custo por token é o fator dominante em escala. Cache de respostas frequentes reduz 30-50% do custo. |
| V2 — RAG Pipeline | Embedding: text-embedding-3-small, Cohere Embed | LangChain, LlamaIndex | Pinecone, Weaviate, Qdrant, pgvector | AWS (S3 + Lambda), GCP (Cloud Storage + Cloud Run) | Qualidade depende mais do chunking/retrieval do que do modelo de geração. |
| V3 — Inference API | PyTorch, TensorFlow, ONNX Runtime, vLLM | MLflow, BentoML, Seldon Core | Não se aplica | AWS SageMaker, GCP Vertex AI, Modal, Replicate | GPU on-demand para modelos pesados. CPU suficiente para modelos tabulares leves. |
| V4 — ML Pipeline | Scikit-learn, XGBoost, PyTorch, HuggingFace | MLflow, Kubeflow, Metaflow, ZenML | Não se aplica | AWS SageMaker, GCP Vertex AI, Databricks | Versionamento de dados (DVC) é tão importante quanto versionamento de código. |
| V5 — IA Embarcada | OpenAI API, Claude API, HuggingFace Inference | SDK do provider ou wrapper custom | Opcional (se usar RAG) | Mesma infra do produto existente + API gateway | Latência máxima aceitável definida pelo UX do produto host. Fallback sem IA é obrigatório. |

---

## Etapa 01 — Inception

- **Origem da demanda e expectativa real**: Demandas de IA frequentemente surgem de pressão competitiva ("o concorrente tem IA"), hype executivo ("precisamos usar IA generativa") ou dor operacional real (volume de atendimento insustentável, classificação manual de milhares de documentos). Distinguir o gatilho real é crítico porque define o critério de sucesso: se a motivação é hype, o risco de abandono pós-MVP é alto; se é dor operacional quantificada, existe um baseline mensurável contra o qual o sucesso será medido. Projetos de IA sem problema de negócio claro tendem a virar provas de conceito que nunca chegam a produção.

- **Maturidade de dados do cliente**: IA depende de dados. A pergunta mais importante da Inception não é "que modelo vamos usar" mas "os dados existem, são acessíveis e têm qualidade suficiente?". Clientes frequentemente superestimam a qualidade dos seus dados — "temos tudo no banco" pode significar dados inconsistentes, sem schema, com 40% de campos nulos, ou em formatos heterogêneos (PDFs escaneados, e-mails, planilhas). Sem dados minimamente estruturados e acessíveis, o projeto não é de IA — é de engenharia de dados com IA como objetivo futuro.

- **Expectativas sobre precisão e comportamento do modelo**: Clientes não-técnicos frequentemente esperam que IA funcione como software determinístico — "se eu perguntar X, a resposta é sempre Y". Modelos probabilísticos cometem erros, alucinam, e têm desempenho variável conforme o input. Alinhar na Inception que IA terá taxa de erro, que a taxa será monitorada e melhorada iterativamente, e que haverá casos onde o modelo não responde ou responde incorretamente, é essencial para evitar frustração e desconfiança quando os primeiros erros aparecerem.

- **Compliance e sensibilidade dos dados**: Dados usados para treinar, embedar ou enviar para APIs externas (OpenAI, Anthropic, Google) podem conter informações pessoais (PII), dados financeiros, dados médicos ou segredos comerciais. A conformidade com LGPD/GDPR não é opcional — enviar dados pessoais para uma API de LLM sem base legal configurada é violação. Se os dados são sensíveis, a arquitetura precisa considerar modelos self-hosted, anonimização no pipeline, ou contratos de DPA com os providers. Essa decisão impacta custo e complexidade em ordens de magnitude.

- **Orçamento de operação contínua (custo por inferência)**: Diferente de software tradicional onde o custo de operação é relativamente fixo (servidor + banco), IA tem custo variável proporcional ao uso. Uma chamada GPT-4o com contexto grande pode custar $0.03-0.10 por requisição. Em escala de 10.000 requisições/dia, o custo mensal de API pode ultrapassar $10.000. O cliente precisa entender que o custo de IA em produção não é comparável ao custo de um servidor — é mais parecido com um serviço metered como telefonia. Projeções de custo por volume são obrigatórias antes de aprovar a arquitetura.

- **Diferença entre PoC e produção**: Muitos projetos de IA são apresentados como "vamos fazer um piloto" sem definição clara de critérios de sucesso e caminho para produção. Um PoC de chatbot que funciona em demo com 5 perguntas pré-definidas é radicalmente diferente de um sistema em produção que atende 1.000 usuários/dia com monitoramento, fallback, logging, rate limiting e SLA. Se o objetivo é PoC, o escopo e orçamento devem refletir isso. Se o objetivo é produção, todas as etapas são necessárias.

### Perguntas

1. Qual é o problema de negócio que a IA vai resolver — existe uma métrica atual que será melhorada (tempo de resposta, custo por atendimento, taxa de erro manual)? [fonte: Diretoria, Operações] [impacto: PM, Data Science]
2. Os dados necessários existem, estão acessíveis e têm qualidade documentada, ou será necessário construir o pipeline de dados primeiro? [fonte: TI, Engenharia de Dados, BI] [impacto: Data Engineer, Data Science, PM]
3. Qual é o volume de dados disponível para treinamento ou para compor a base de conhecimento (RAG) — centenas, milhares ou milhões de registros/documentos? [fonte: TI, Operações, BI] [impacto: Data Science, Data Engineer]
4. Os dados contêm informações pessoais (PII), financeiras, médicas ou segredos comerciais que limitam o envio para APIs externas? [fonte: Jurídico, DPO, Compliance, TI] [impacto: Arquiteto, Data Science, DevOps]
5. Existe orçamento separado para custo de inferência em produção (APIs de LLM, GPU, vector store) além do custo de desenvolvimento? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
6. O objetivo é uma prova de conceito com critérios de sucesso definidos ou um sistema de produção com SLA desde o dia 1? [fonte: Diretoria, Produto] [impacto: PM, Dev, Data Science]
7. Quem é o usuário final da solução de IA — equipe interna (backoffice), cliente externo (self-service) ou outro sistema (API-to-API)? [fonte: Produto, Operações, Diretoria] [impacto: Designer, Dev, Data Science]
8. Qual é a tolerância a erros do modelo — respostas incorretas geram inconveniência, perda financeira ou risco legal? [fonte: Diretoria, Jurídico, Operações] [impacto: Data Science, QA, PM]
9. Existe um time interno com competência em ML/IA ou será necessário construir ou contratar essa capacidade? [fonte: RH, TI, Diretoria] [impacto: PM, Data Science, Dev]
10. O cliente tem preferência ou restrição por provider de IA (OpenAI, Google, AWS, open-source, ou proibição de cloud pública)? [fonte: TI, Diretoria, Compliance] [impacto: Arquiteto, Data Science, DevOps]
11. Existe um sistema existente no qual a IA será integrada ou será um produto standalone? [fonte: TI, Produto] [impacto: Dev, Arquiteto]
12. Qual é o prazo esperado para o primeiro resultado demonstrável e para a entrada em produção? [fonte: Diretoria, Produto] [impacto: PM, Data Science]
13. A solução de IA substituirá um processo manual existente ou criará uma capacidade nova que não existia? [fonte: Operações, Diretoria] [impacto: PM, Data Science, Operações]
14. Existe expectativa de que o modelo melhore continuamente com feedback dos usuários (human-in-the-loop) ou será estático após o deploy? [fonte: Produto, Diretoria] [impacto: Data Science, Dev, PM]
15. Há restrições regulatórias específicas do setor (saúde, financeiro, jurídico) que limitam o uso de IA ou exigem explicabilidade das decisões? [fonte: Jurídico, Compliance, Regulatório] [impacto: Data Science, Arquiteto, PM]

---

## Etapa 02 — Discovery

- **Inventário e qualidade dos dados**: Levantar com precisão o que existe: quais fontes de dados (banco relacional, data lake, APIs, documentos PDF/Word, e-mails, planilhas), volume por fonte, schema ou falta dele, taxa de preenchimento dos campos relevantes, e frequência de atualização. A qualidade dos dados é o fator número um de sucesso ou fracasso de projetos de ML — dados sujos, inconsistentes ou insuficientes invalidam qualquer modelo, independentemente da sofisticação do algoritmo. Um assessment de dados de 2-3 dias no início pode poupar meses de retrabalho.

- **Definição do problema como tarefa de ML**: Traduzir o problema de negócio em uma tarefa técnica de ML com precisão. "Quero prever churn" se traduz em: classificação binária (churn/não-churn) com janela de predição de X dias, usando features de comportamento dos últimos Y dias, com threshold de probabilidade definido pelo trade-off entre recall (pegar todos os churners) e precision (não incomodar quem não vai churnar). Sem essa tradução, o time de data science trabalha sem target claro, e o cliente não consegue avaliar se o resultado é bom ou ruim.

- **Baseline de performance humana ou sistema atual**: Antes de treinar qualquer modelo, estabelecer o baseline: como a tarefa é feita hoje? Se é manual, qual é a taxa de acerto? Qual é o tempo médio? Qual é o custo por operação? Se é automatizada com regras simples (if/else), qual é a acurácia atual? O modelo de ML só faz sentido se superar o baseline com margem suficiente para justificar o investimento. Um modelo com 85% de acurácia pode ser revolucionário se o baseline é 60%, ou inútil se o baseline com regras simples já é 83%.

- **Requisitos de latência e throughput**: A performance do modelo em produção tem duas dimensões: latência (tempo para uma predição individual) e throughput (volume de predições por segundo/minuto). Um chatbot precisa de latência <2s para não irritar o usuário. Um batch de scoring de crédito pode tolerar minutos por lote. Uma API de detecção de fraude em tempo real precisa de <100ms. Esses requisitos definem diretamente a arquitetura — modelo em GPU vs. CPU, inference API síncrona vs. batch, edge deployment vs. cloud central.

- **Requisitos de explicabilidade**: Alguns domínios exigem que a decisão do modelo seja explicável — não basta dizer "o modelo prevê churn com 87% de probabilidade", é necessário dizer "os fatores principais foram: 3 reclamações no último mês, queda de 60% no uso, e ticket aberto sem resolução". Regulamentação de crédito (BACEN), saúde e direito frequentemente exigem explicabilidade. Mesmo fora de regulamentação, stakeholders de negócio frequentemente pedem "por que o modelo decidiu isso?" — se a resposta for "porque a rede neural disse", a confiança no sistema erode rapidamente.

- **Mapeamento de integrações e dependências de dados**: Identificar todos os sistemas que alimentarão o modelo (fontes de features, documentos para RAG, streams de eventos) e todos os sistemas que consumirão os resultados (UI, APIs downstream, filas de processamento, dashboards). Cada integração é um ponto de falha potencial e uma dependência de latência. Se a feature X vem de uma API que tem SLA de 200ms e o modelo precisa de latência total <500ms, sobraram 300ms para inferência — e isso pode não ser suficiente para um modelo grande.

### Perguntas

1. Quais são as fontes de dados disponíveis e em que formato estão (SQL, CSV, JSON, PDFs, APIs, data lake)? [fonte: TI, Engenharia de Dados, BI] [impacto: Data Engineer, Data Science]
2. Qual é o volume de dados disponível para treinar/alimentar o modelo e com que frequência os dados são atualizados? [fonte: TI, Engenharia de Dados] [impacto: Data Science, Data Engineer]
3. Foi realizado um assessment de qualidade dos dados (completude, consistência, duplicatas, outliers)? [fonte: Engenharia de Dados, BI] [impacto: Data Science, Data Engineer]
4. O problema de negócio foi traduzido em uma tarefa de ML específica (classificação, regressão, geração, retrieval, ranking)? [fonte: Data Science, Produto] [impacto: Data Science, PM]
5. Qual é o baseline atual — como a tarefa é feita hoje (manual, regras, modelo existente) e qual é a performance? [fonte: Operações, TI, BI] [impacto: Data Science, PM]
6. Qual é a latência máxima aceitável para uma predição/resposta no fluxo do usuário (real-time <1s, near-real-time <10s, batch)? [fonte: Produto, TI, Operações] [impacto: Arquiteto, Data Science, Dev]
7. Existe requisito de explicabilidade das decisões do modelo (regulatório, compliance ou confiança do usuário)? [fonte: Jurídico, Compliance, Regulatório, Produto] [impacto: Data Science, Arquiteto]
8. Quais sistemas consumirão os resultados do modelo (UI, API, fila, dashboard, notificação)? [fonte: TI, Produto] [impacto: Dev, Arquiteto]
9. O modelo precisa funcionar com dados de múltiplos idiomas ou regiões com características diferentes? [fonte: Operações, Produto, Comercial] [impacto: Data Science, Data Engineer]
10. Existem labels/anotações disponíveis para treino supervisionado ou será necessário criar um processo de anotação? [fonte: Operações, Data Science, TI] [impacto: Data Science, PM]
11. Qual é o impacto financeiro de um falso positivo vs. falso negativo — onde é mais caro errar? [fonte: Operações, Financeiro, Produto] [impacto: Data Science, PM]
12. Existe sazonalidade ou drift temporal nos dados que exija re-treino periódico do modelo? [fonte: BI, Operações, Data Science] [impacto: Data Science, MLOps]
13. A solução precisa funcionar offline ou em ambientes com conectividade limitada? [fonte: Produto, TI, Operações] [impacto: Arquiteto, Dev]
14. Quais métricas de ML serão usadas para avaliar o modelo (accuracy, F1, AUC-ROC, BLEU, ROUGE, perplexity) e quem define o threshold aceitável? [fonte: Data Science, Produto, Diretoria] [impacto: Data Science, PM]
15. Existe algum viés conhecido nos dados históricos que poderia resultar em decisões discriminatórias do modelo? [fonte: Data Science, Jurídico, Compliance, RH] [impacto: Data Science, Jurídico, PM]

---

## Etapa 03 — Alignment

- **Alinhamento sobre limitações de IA**: O stakeholder de negócio precisa entender formalmente que modelos de IA são probabilísticos e vão errar. A taxa de erro precisa ser acordada como aceitável antes do build começar — não após o primeiro erro em produção gerar uma crise. Documentar cenários de falha esperados (alucinação em chatbot, falso positivo em detector de fraude, recomendação inadequada) e como o sistema vai tratar cada um (fallback para humano, mensagem de incerteza, bloqueio da ação). Esse alinhamento formal protege o time técnico de expectativas irreais e o cliente de surpresas.

- **Definição de métricas de sucesso de negócio vs. métricas de ML**: O data scientist otimiza F1-score, AUC-ROC ou perplexity. O stakeholder de negócio quer "menos reclamações", "mais vendas" ou "atendimento mais rápido". Essas métricas nem sempre são correlacionadas — um modelo com F1 de 0.92 pode não mover a métrica de negócio se a causa raiz do problema é operacional, não preditiva. Alinhar na Etapa 03 a relação explícita entre a métrica de ML e o KPI de negócio, com os pressupostos documentados, evita a situação de "o modelo funciona mas o resultado não melhorou".

- **Estratégia de human-in-the-loop**: Definir se e como humanos participam do fluxo de decisão. Opções: modelo decide sozinho (full automation), modelo sugere e humano confirma (augmentation), modelo escala para humano em casos de baixa confiança (hybrid). A escolha impacta design, UX, custo operacional e responsabilidade legal. Full automation é mais barato em escala mas tem risco alto se o modelo errar em caso crítico. Augmentation mantém humano no loop mas pode criar bottleneck operacional se o volume for alto. A decisão deve ser tomada por domínio de aplicação, não genericamente.

- **Governança de dados e modelo**: Definir quem é responsável pela qualidade dos dados de treino, quem aprova novos modelos para produção, quem monitora performance em produção e quem decide quando re-treinar. Em empresas maiores, isso pode envolver comitê de IA, DPO, e compliance. A ausência de governança definida resulta em modelos em produção que ninguém monitora, que degradam silenciosamente, e que só são notados quando causam dano mensurável — meses depois do deploy.

- **Formato de entrega e integração**: Alinhar como a solução de IA será entregue ao usuário final. Opções: API REST/gRPC consumida por sistema existente, widget embarcado em interface existente, interface standalone (webapp ou mobile), dashboard de resultados, ou processamento batch com resultados em planilha/banco. O formato de entrega define o esforço de frontend, a necessidade de autenticação, e a experiência do usuário. Um modelo de ML sem interface de consumo adequada é um artefato técnico, não um produto.

### Perguntas

1. Todos os stakeholders entendem e aceitaram formalmente que o modelo terá taxa de erro e que essa taxa será monitorada e melhorada iterativamente? [fonte: Diretoria, Produto, Operações] [impacto: PM, Data Science]
2. As métricas de sucesso de negócio (KPIs) foram mapeadas explicitamente para as métricas de ML correspondentes? [fonte: Produto, Data Science, Diretoria] [impacto: Data Science, PM]
3. A estratégia de human-in-the-loop foi definida (full automation, augmentation ou hybrid) com justificativa documentada? [fonte: Operações, Produto, Diretoria] [impacto: Data Science, Dev, Designer]
4. Os cenários de falha do modelo foram documentados com ações de mitigação para cada um (fallback, escalação, bloqueio)? [fonte: Produto, Data Science, Operações] [impacto: Dev, Data Science, PM]
5. A governança do modelo foi definida — quem aprova modelos para produção, quem monitora e quem decide re-treino? [fonte: Diretoria, TI, Data Science] [impacto: Data Science, MLOps, PM]
6. A responsabilidade legal por decisões do modelo foi endereçada com o jurídico (especialmente para decisões de crédito, saúde, RH)? [fonte: Jurídico, Compliance, DPO] [impacto: Data Science, PM, Diretoria]
7. O formato de entrega da solução foi alinhado (API, widget, interface standalone, dashboard, batch)? [fonte: Produto, TI, Diretoria] [impacto: Dev, Designer, Arquiteto]
8. O SLA de disponibilidade da solução de IA foi definido (99.9%, 99.5%, best-effort) e é compatível com o SLA do sistema que consome? [fonte: TI, Produto, Operações] [impacto: DevOps, Arquiteto]
9. O custo projetado de operação em produção foi apresentado ao financeiro com cenários de volume baixo, esperado e pico? [fonte: Data Science, Financeiro, Diretoria] [impacto: PM, Arquiteto]
10. A estratégia de feedback loop foi definida — como os erros do modelo serão capturados e usados para melhorar o sistema? [fonte: Produto, Data Science] [impacto: Data Science, Dev, MLOps]
11. O time de operações foi envolvido para validar que o fluxo proposto é viável no dia a dia (não apenas tecnicamente correto)? [fonte: Operações] [impacto: PM, Data Science, Designer]
12. Se a solução é um chatbot/assistente, o tom de voz, limites de escopo e política de escalação para humano foram definidos? [fonte: Produto, Marketing, Operações] [impacto: Data Science, Dev, Conteúdo]
13. As dependências externas críticas (APIs de LLM, acesso a dados, infraestrutura GPU) foram listadas com prazos de aprovação? [fonte: TI, Compras, Financeiro] [impacto: PM, DevOps, Arquiteto]
14. O escopo de dados sensíveis foi validado com DPO/jurídico e a base legal para processamento está documentada (LGPD Art. 7)? [fonte: DPO, Jurídico, Compliance] [impacto: Data Science, Arquiteto]
15. O plano de rollout foi alinhado — big bang para todos os usuários ou rollout gradual (canary, A/B, shadow mode)? [fonte: Produto, Diretoria, Operações] [impacto: Dev, DevOps, PM]

---

## Etapa 04 — Definition

- **Especificação de features e dados de entrada**: Para cada modelo ou pipeline, definir formalmente as features de entrada (nome, tipo, fonte, transformação necessária, valor quando ausente). Para RAG, definir as fontes de documentos, formatos aceitos, estratégia de chunking (tamanho, overlap, delimitadores), e metadados associados a cada chunk (fonte, data, categoria). Essa especificação é o "contrato" entre engenharia de dados e data science — sem ela, o data scientist trabalha com dados exploratory que podem não estar disponíveis em produção com a mesma latência e qualidade.

- **Definição de prompts e guardrails (para LLM)**: Se a solução usa LLM, definir formalmente o system prompt, os guardrails (tópicos proibidos, formato de resposta esperado, comportamento quando não sabe a resposta), e as regras de grounding (quando o modelo deve citar a fonte, quando deve recusar a resposta). Prompts devem ser versionados como código — cada mudança de prompt é um deploy que pode alterar o comportamento do sistema. Definir o processo de revisão e aprovação de mudanças de prompt antes do build é tão importante quanto definir o schema de dados.

- **Schema de input/output da API de inferência**: Definir o contrato da API que servirá o modelo — formato de request (JSON, protobuf), campos obrigatórios e opcionais, formato de response (predição + confidence score + metadata), códigos de erro, timeout, e rate limiting. O schema deve incluir campos de rastreabilidade (request_id, model_version, timestamp) que serão essenciais para debugging e auditoria em produção. Se há múltiplos consumidores, definir versioning da API (v1, v2) desde o início para permitir evolução sem quebrar integrações.

- **Plano de avaliação (evaluation framework)**: Definir antes do build como o modelo será avaliado — dataset de teste (hold-out, cross-validation, dataset curado por especialistas de domínio), métricas primárias e secundárias, thresholds de aprovação para produção, e processo de comparação com modelo anterior (A/B test, shadow mode, backtesting). Sem evaluation framework formalizado, a decisão de "o modelo está bom o suficiente" é subjetiva e politizada — data scientist diz que sim, stakeholder diz que não, e ninguém tem dados para argumentar.

- **Estratégia de versionamento**: Definir como modelos, dados, prompts e configurações serão versionados. Para ML clássico: versionamento de modelo (MLflow Model Registry, Weights & Biases), versionamento de dados de treino (DVC, Delta Lake), e versionamento de features (Feature Store). Para LLM: versionamento de prompts (Git, LangSmith), versionamento de índice RAG (snapshots de embedding), e versionamento de configuração (temperatura, max_tokens, top_p). Cada versão em produção deve ser reproduzível — dado o mesmo input e a mesma versão, o output deve ser consistente.

- **Definição de monitoramento em produção**: Especificar antes do build o que será monitorado: métricas de modelo (accuracy degradation, drift, latência de inferência), métricas operacionais (error rate, throughput, custo por request), e métricas de negócio (taxa de aceitação das sugestões, escalações para humano, NPS). Definir alertas com thresholds e escalação — se a latência P95 ultrapassar 3s ou a accuracy cair 5% em relação ao baseline, quem é notificado e o que acontece.

### Perguntas

1. As features de entrada do modelo foram especificadas com nome, tipo, fonte, transformação e tratamento de ausência? [fonte: Data Science, Engenharia de Dados] [impacto: Data Engineer, Data Science]
2. Para LLM: o system prompt, guardrails e regras de grounding foram documentados e versionados? [fonte: Data Science, Produto] [impacto: Data Science, Dev]
3. O schema da API de inferência foi definido com campos de request, response, erros, timeout e rate limiting? [fonte: Arquiteto, Dev, Data Science] [impacto: Dev, Data Science]
4. O dataset de avaliação foi definido — origem, tamanho, representatividade, e quem valida que é adequado? [fonte: Data Science, Operações, Produto] [impacto: Data Science]
5. Os thresholds de aprovação para produção foram definidos (métricas + valores mínimos aceitáveis)? [fonte: Data Science, Produto, Diretoria] [impacto: Data Science, PM]
6. A estratégia de versionamento de modelo, dados e prompts foi documentada com ferramentas e processos? [fonte: Data Science, DevOps] [impacto: MLOps, Data Science, Dev]
7. O plano de monitoramento em produção foi especificado (métricas, alertas, thresholds, escalação)? [fonte: Data Science, DevOps, Operações] [impacto: MLOps, DevOps, Data Science]
8. Para RAG: a estratégia de chunking, embedding e retrieval foi definida com parâmetros documentados? [fonte: Data Science] [impacto: Data Science, Data Engineer]
9. O pipeline de dados para features em produção foi mapeado com fontes, latências e pontos de falha? [fonte: Engenharia de Dados, TI] [impacto: Data Engineer, Arquiteto]
10. Os critérios de re-treino foram definidos (periodicidade fixa, trigger por drift, manual por demanda)? [fonte: Data Science, Produto] [impacto: MLOps, Data Science]
11. A política de rollback de modelo foi documentada (como reverter para versão anterior se o novo modelo performar pior)? [fonte: Data Science, DevOps] [impacto: MLOps, DevOps]
12. As limitações conhecidas do modelo foram documentadas (tipos de input que falham, edge cases, viés identificado)? [fonte: Data Science] [impacto: Data Science, Produto, QA]
13. Para chatbot/assistente: os cenários de teste de conversação foram escritos com respostas esperadas para cada cenário? [fonte: Produto, Operações, Data Science] [impacto: QA, Data Science]
14. O processo de anotação/labeling (se necessário) foi definido — ferramenta, anotadores, guidelines, inter-annotator agreement? [fonte: Data Science, Operações] [impacto: Data Science, PM]
15. A documentação de definição foi revisada por data science, engenharia, produto e compliance antes de avançar para Architecture? [fonte: Diretoria, Data Science, Dev, Compliance] [impacto: PM]

---

## Etapa 05 — Architecture

- **Escolha do modelo base**: A decisão entre modelo proprietário via API (GPT-4o, Claude, Gemini), modelo open-source hospedado (Llama 3, Mistral, Phi) ou modelo treinado do zero depende de múltiplos fatores: sensibilidade dos dados (API externa vs. self-hosted), custo por inferência em escala, necessidade de customização (fine-tuning vs. prompt engineering), latência requerida, e capacidade operacional do time para manter infraestrutura de serving. Para a maioria dos casos de uso, começar com modelo via API e migrar para self-hosted apenas se custo ou privacidade justificarem é a estratégia mais pragmática.

- **Arquitetura de serving (inference)**: Definir como o modelo será servido em produção. Opções: serverless (AWS Lambda, GCP Cloud Functions) para volume baixo e latência tolerante; container gerenciado (Cloud Run, ECS Fargate) para volume médio com auto-scaling; GPU dedicada (SageMaker, Vertex AI, Modal) para modelos pesados que precisam de aceleração; edge/on-device para cenários offline ou de ultra-baixa latência. Para LLMs self-hosted, vLLM é o padrão de mercado para serving eficiente com batching contínuo e quantização. O custo de GPU idle pode facilmente ultrapassar $1000/mês — autoscaling e spot instances são essenciais.

- **Arquitetura de dados e feature store**: Para ML clássico, definir se features serão computadas on-the-fly (no momento da inferência, a partir de queries ao banco) ou pré-computadas (feature store com materialização periódica). Feature store (Feast, Tecton, SageMaker Feature Store) é justificado quando há múltiplos modelos compartilhando features, quando features têm janelas temporais complexas (média móvel de 30 dias), ou quando a consistência entre treino e serving é crítica (training-serving skew). Para RAG, definir a arquitetura do vector store, strategy de indexação, e pipeline de re-indexação quando documentos mudam.

- **Pipeline de treinamento e MLOps**: Para variantes V3 e V4, definir o pipeline de treinamento automatizado: orquestração (Kubeflow, Metaflow, ZenML, Airflow), experiment tracking (MLflow, Weights & Biases), versionamento de dados (DVC, Delta Lake), model registry (MLflow Model Registry, Vertex AI Model Registry), e CI/CD de modelo (testes automatizados de performance antes de promover para produção). O pipeline deve ser reproduzível — dado o mesmo código e os mesmos dados, o mesmo modelo é produzido. Sem reprodutibilidade, debugging de regressão de performance é impossível.

- **Segurança e isolamento de dados**: Definir a arquitetura de segurança: dados em trânsito cifrados (TLS), dados em repouso cifrados (AES-256), anonimização ou pseudonimização no pipeline antes de chegar ao modelo, controle de acesso por role (quem vê os dados de treino, quem acessa os logs de inferência), e audit trail de todas as predições (request_id, input, output, model_version, timestamp). Para cenários de alta sensibilidade, considerar Trusted Execution Environments (TEE) ou federated learning para treinar sem expor os dados brutos.

- **Estratégia de cache e otimização de custo**: Para LLMs via API, cache de respostas para inputs idênticos ou semanticamente similares pode reduzir custos em 30-60%. Ferramentas como GPTCache ou semantic caching no Redis permitem reutilizar respostas anteriores para perguntas parecidas. Definir TTL do cache (respostas de FAQ podem ser cacheadas por dias; respostas sobre dados em tempo real não podem). Para inference APIs internas, definir batching strategy (acumular múltiplas requisições e processar em lote na GPU é significativamente mais eficiente que processamento individual).

### Perguntas

1. A decisão entre modelo via API, modelo self-hosted e modelo treinado do zero foi tomada com justificativa documentada (custo, privacidade, performance)? [fonte: Data Science, TI, Financeiro, Compliance] [impacto: Arquiteto, Data Science, DevOps]
2. A arquitetura de serving foi definida com estratégia de autoscaling, GPU vs. CPU, e estimativa de custo por volume? [fonte: Arquiteto, DevOps, Financeiro] [impacto: DevOps, Data Science]
3. O vector store (se RAG) foi escolhido considerando volume, latência de query, custo e estratégia de re-indexação? [fonte: Data Science, TI] [impacto: Data Engineer, Data Science, DevOps]
4. O pipeline de treinamento (se aplicável) foi desenhado com experiment tracking, versionamento de dados e model registry? [fonte: Data Science, DevOps] [impacto: MLOps, Data Science]
5. A estratégia de feature store vs. features on-the-fly foi decidida com base na complexidade e número de modelos? [fonte: Data Science, Engenharia de Dados] [impacto: Data Engineer, Data Science]
6. A arquitetura de segurança foi definida — criptografia, anonimização, controle de acesso e audit trail? [fonte: Segurança, DPO, TI] [impacto: DevOps, Arquiteto, Data Science]
7. A estratégia de cache de inferência foi definida com TTL por tipo de query e estimativa de economia? [fonte: Data Science, Arquiteto] [impacto: Dev, DevOps]
8. O fallback quando o modelo ou a API de LLM estiver indisponível foi desenhado (cache, modelo menor, regras, escalação)? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps, Data Science]
9. Os custos mensais de operação foram calculados para volume esperado, pico e pior caso (incluindo GPU, API, storage, egress)? [fonte: Financeiro, DevOps, Arquiteto] [impacto: PM, Diretoria]
10. A latência end-to-end do fluxo de inferência foi estimada (rede + preprocessing + inferência + postprocessing) e está dentro do SLA? [fonte: Arquiteto, Data Science] [impacto: Dev, Data Science]
11. O pipeline de CI/CD para modelo (testes automatizados, gates de performance, promoção staged) foi desenhado? [fonte: MLOps, Data Science, DevOps] [impacto: MLOps, DevOps]
12. A estratégia de monitoramento de drift (data drift, concept drift, prediction drift) foi definida com ferramentas e alertas? [fonte: Data Science, MLOps] [impacto: Data Science, MLOps]
13. A arquitetura suporta A/B testing ou shadow mode para comparar modelos antes de promover para 100% do tráfego? [fonte: Arquiteto, Data Science] [impacto: Dev, Data Science, MLOps]
14. O modelo de observabilidade foi definido — traces de inferência, logs estruturados, métricas customizadas (LangSmith, Weights & Biases, Arize)? [fonte: Data Science, DevOps] [impacto: MLOps, DevOps, Data Science]
15. O modelo de branches, ambientes (dev, staging, prod) e processo de promoção de modelo foi documentado e aprovado? [fonte: DevOps, Data Science, TI] [impacto: MLOps, DevOps, PM]

---

## Etapa 06 — Setup

- **Ambiente de desenvolvimento para data science**: Configurar o ambiente de experimentação — notebooks (JupyterHub, SageMaker Studio, Vertex AI Workbench, VS Code com extensões), acesso aos dados de treino em ambiente seguro (nunca dados de produção em laptop local sem criptografia), GPU para experimentação (cloud notebooks com GPU on-demand, não GPU dedicada 24/7 que custa $2000/mês idle). Configurar experiment tracking (MLflow server, Weights & Biases workspace) desde o primeiro experimento — reconstruir o histórico de experimentos depois é impossível.

- **Infraestrutura de dados e pipeline**: Configurar o pipeline de dados: extração das fontes (connectors, APIs, CDC), transformação (cleaning, feature engineering), carregamento no formato consumido pelo modelo (parquet, delta, vector store). Para RAG, configurar o pipeline de ingestão: loader de documentos (LangChain document loaders, Unstructured.io), chunking, embedding, e indexação no vector store. Testar o pipeline end-to-end com dados reais (não mock) para validar latência, volume e qualidade — problemas de encoding, Unicode, formatos inesperados e documentos corrompidos só aparecem com dados reais.

- **Infraestrutura de serving**: Configurar o ambiente de produção para inferência — container registry, orquestração (ECS, GKE, Cloud Run), API gateway (rate limiting, autenticação, logging), health checks, e autoscaling rules. Para LLMs self-hosted, configurar o serving framework (vLLM, TGI, Ollama) com quantização apropriada (GPTQ, AWQ, GGUF) e testar throughput/latência com benchmark realista. Para APIs externas (OpenAI, Anthropic), configurar wrappers com retry, circuit breaker, e fallback para garantir resiliência.

- **Monitoramento e observabilidade**: Configurar a stack de monitoramento desde o setup — não deixar para depois do build. Métricas de infraestrutura (CPU, memória, GPU utilization, latência de rede), métricas de aplicação (request rate, error rate, latência de inferência P50/P95/P99), e métricas de modelo (distribuição de outputs, confidence scores, taxas de fallback). Para LLMs, configurar tracing de conversas (LangSmith, Langfuse, Phoenix) para debugging de qualidade de respostas. Definir dashboards com visualizações claras e alertas com thresholds não-ambíguos.

- **Configuração de segurança e acesso**: Configurar IAM roles com princípio de menor privilégio — data scientists acessam dados de treino mas não de produção, o modelo em produção acessa apenas as features que precisa, logs de inferência são acessíveis apenas pelo time de MLOps. Configurar secrets management (AWS Secrets Manager, Vault, GCP Secret Manager) para API keys de LLM, credenciais de banco, e tokens de integração. Configurar VPC/rede com isolamento entre ambientes (dev, staging, prod) e sem acesso direto à internet a partir do modelo em produção (egress controlado).

- **Ambiente de avaliação (eval)**: Configurar o ambiente para rodar avaliações automáticas do modelo — dataset de teste carregado, scripts de avaliação versionados, pipeline de eval que roda automaticamente antes de cada promoção de modelo. Para LLMs, configurar eval frameworks (RAGAS para RAG, DeepEval, ou custom eval com LLM-as-judge). O eval deve ser determinístico na medida do possível — mesmo dataset, mesmas métricas, mesmo processo — para que comparações entre versões sejam válidas.

### Perguntas

1. O ambiente de experimentação (notebooks, GPU, experiment tracking) está configurado e acessível pelo time de data science? [fonte: Data Science, TI] [impacto: Data Science]
2. O acesso aos dados de treino está configurado em ambiente seguro, sem dados de produção em máquinas locais não-criptografadas? [fonte: Segurança, TI, Data Science] [impacto: Data Science, Segurança]
3. O pipeline de dados (extração, transformação, carregamento) foi configurado e testado end-to-end com dados reais? [fonte: Engenharia de Dados, Data Science] [impacto: Data Engineer, Data Science]
4. Para RAG: o pipeline de ingestão (loader, chunking, embedding, indexação) foi testado com documentos reais e a qualidade do retrieval foi validada? [fonte: Data Science] [impacto: Data Science, Data Engineer]
5. A infraestrutura de serving está configurada com API gateway, autoscaling, health checks e rate limiting? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
6. O monitoramento e observabilidade estão configurados com métricas de infra, aplicação e modelo, incluindo dashboards e alertas? [fonte: DevOps, Data Science] [impacto: MLOps, DevOps]
7. As variáveis de ambiente e secrets (API keys, credenciais) estão em secrets manager e nunca hardcoded no código? [fonte: DevOps, Segurança] [impacto: Dev, DevOps, Segurança]
8. Os ambientes (dev, staging, prod) estão isolados com IAM roles separados e sem acesso cruzado? [fonte: DevOps, Segurança] [impacto: DevOps, Segurança]
9. O experiment tracking (MLflow, W&B) está configurado e o primeiro experimento baseline foi registrado? [fonte: Data Science] [impacto: Data Science, MLOps]
10. O ambiente de avaliação automática está configurado com dataset de teste, scripts de eval e pipeline de comparação? [fonte: Data Science, MLOps] [impacto: Data Science, MLOps]
11. O model registry está configurado e o processo de registro e promoção de modelo foi testado? [fonte: Data Science, MLOps, DevOps] [impacto: MLOps, Data Science]
12. O versionamento de dados (DVC, Delta Lake) está configurado e o primeiro snapshot de dados de treino foi registrado? [fonte: Data Science, Engenharia de Dados] [impacto: Data Science, Data Engineer]
13. O pipeline de CI/CD do código de inferência (não do modelo, mas da API) está configurado com lint, testes e deploy automático? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
14. O ambiente de staging reproduz fielmente o ambiente de produção (mesma infra, mesmas integrações, dados representativos)? [fonte: DevOps] [impacto: DevOps, Data Science, QA]
15. A documentação de setup (como rodar localmente, como acessar dados, como treinar, como avaliar) está atualizada e testada por alguém fora do time original? [fonte: Dev, Data Science] [impacto: Dev, Data Science]

---

## Etapa 07 — Build

- **Experimentação e treinamento do modelo**: Executar o ciclo de experimentação — feature engineering, seleção de modelo, tuning de hiperparâmetros, treino, avaliação. Cada experimento deve ser registrado no experiment tracking (MLflow, W&B) com parâmetros, métricas, artifacts e código associado. O objetivo não é encontrar o modelo perfeito, mas o modelo que supera o baseline definido na Discovery com margem suficiente para justificar o investimento operacional. Evitar over-engineering no primeiro release — um modelo simples (XGBoost, logistic regression, fine-tune leve) que resolve 80% dos casos é melhor que um ensemble complexo que resolve 85% mas é impossível de manter.

- **Desenvolvimento da API de inferência**: Implementar o serviço que expõe o modelo para consumo — recebe request, preprocessa o input, executa inferência, postprocessa o output, retorna response. A API deve incluir: validação de input (schema, tipos, limites), tratamento de erros (modelo falha, timeout, input inválido), logging estruturado de cada request (para debugging e auditoria), e headers de metadata (model_version, latency_ms, confidence_score). Para LLMs, implementar streaming de resposta (SSE) para melhorar a percepção de latência do usuário.

- **Implementação de guardrails e safety**: Para LLMs e chatbots, implementar as camadas de proteção definidas na Etapa 04: input filtering (rejeitar prompts maliciosos, injection attempts), output filtering (detectar e bloquear conteúdo tóxico, PII vazado, alucinações flagrantes), grounding verification (conferir se a resposta é suportada pelos documentos recuperados), e confidence-based routing (respostas com confidence abaixo do threshold são escaladas para humano ou retornam "não sei"). Guardrails devem ser testáveis — cada regra deve ter test case associado.

- **Pipeline de dados em produção**: Implementar a versão de produção do pipeline de dados — não é o mesmo notebook do data scientist. O pipeline de produção precisa ser resiliente (retry em caso de falha de fonte), idempotente (reprocessar os mesmos dados não gera duplicatas), monitorado (alerta se volume de dados cai abaixo do esperado ou se distribuição muda significativamente), e performático (processar no tempo exigido pelo SLA de freshness). Para features em real-time, implementar com streaming (Kafka, Kinesis) ou cache com TTL curto.

- **Interface de consumo (se aplicável)**: Implementar a interface que o usuário final vai interagir. Para chatbots: área de conversa com streaming, indicador de digitação, botões de feedback (thumbs up/down), opção de escalação para humano. Para dashboards de resultado: visualizações claras com intervalos de confiança, filtros por período/segmento, export de dados. Para integrações em produto existente: componente encapsulado que pode ser ativado/desativado via feature flag sem impactar o fluxo principal. O design deve tratar explicitamente o estado de erro e de loading do modelo.

- **Testes automatizados**: Implementar testes em múltiplas camadas: unit tests para preprocessing e postprocessing, integration tests para o pipeline de dados (dados entram no formato correto, features computadas corretamente), contract tests para a API de inferência (schema de input/output respeitado), e evaluation tests para o modelo (rodar eval dataset e verificar que métricas estão acima do threshold). Para LLMs, implementar testes de regressão de prompt — conjunto de inputs/outputs esperados que são verificados automaticamente quando o prompt muda.

### Perguntas

1. Os experimentos de modelagem estão registrados no experiment tracking com parâmetros, métricas e artifacts reproduzíveis? [fonte: Data Science] [impacto: Data Science, MLOps]
2. O modelo selecionado supera o baseline definido na Discovery com margem documentada e estatisticamente significativa? [fonte: Data Science, Produto] [impacto: Data Science, PM]
3. A API de inferência está implementada com validação de input, tratamento de erros, logging estruturado e headers de metadata? [fonte: Dev, Data Science] [impacto: Dev, QA]
4. Os guardrails de segurança (input/output filtering, grounding, confidence routing) estão implementados e testáveis? [fonte: Data Science, Dev, Segurança] [impacto: Dev, Data Science, QA]
5. O pipeline de dados em produção é resiliente, idempotente e monitorado — diferente do notebook de experimentação? [fonte: Engenharia de Dados, Data Science] [impacto: Data Engineer, MLOps]
6. O streaming de resposta (SSE) está implementado para LLMs para melhorar a percepção de latência do usuário? [fonte: Dev] [impacto: Dev, Designer]
7. Os testes automatizados cobrem preprocessing, pipeline de dados, contrato de API e avaliação de modelo? [fonte: Dev, Data Science, QA] [impacto: Dev, Data Science, QA]
8. A interface de consumo trata explicitamente os estados de loading, erro e incerteza do modelo? [fonte: Designer, Dev] [impacto: Dev, Designer]
9. O mecanismo de feedback do usuário (thumbs up/down, correção, escalação) está implementado e os dados são coletados? [fonte: Dev, Produto] [impacto: Dev, Data Science]
10. O feature flag para ativar/desativar a funcionalidade de IA sem deploy está implementado? [fonte: Dev, Produto] [impacto: Dev, DevOps]
11. O modelo versionado foi registrado no model registry com metadata (data de treino, métricas, dataset, código)? [fonte: Data Science, MLOps] [impacto: MLOps, Data Science]
12. Para RAG: a qualidade do retrieval foi avaliada com métricas formais (precision@k, recall@k, MRR) no dataset de teste? [fonte: Data Science] [impacto: Data Science]
13. O custo por request em produção foi medido em benchmark realista e está dentro do orçamento aprovado? [fonte: Data Science, DevOps, Financeiro] [impacto: PM, Arquiteto]
14. Os testes de regressão de prompt (para LLM) estão implementados e rodam automaticamente quando o prompt muda? [fonte: Data Science, Dev] [impacto: Data Science, QA]
15. O pipeline de re-treino automatizado (se aplicável) foi implementado e testado end-to-end? [fonte: Data Science, MLOps] [impacto: MLOps, Data Science]

---

## Etapa 08 — QA

- **Avaliação de qualidade do modelo com dados de teste**: Executar a avaliação formal do modelo com o dataset de teste definido na Etapa 04 — não com os dados de treino ou validação usados durante a experimentação. As métricas devem ser comparadas contra o baseline e contra os thresholds de aprovação definidos. Para classificação, analisar a confusion matrix por classe — accuracy global pode mascarar performance terrível em classes minoritárias. Para LLMs, avaliar com métricas de qualidade de resposta (faithfulness, relevance, correctness) usando eval frameworks como RAGAS ou DeepEval.

- **Teste de carga e latência**: Executar load tests com volume realista (ferramentas como Locust, k6, Artillery) para validar que a inferência mantém latência aceitável sob carga. Testar especificamente: latência P50/P95/P99, throughput máximo antes de degradação, comportamento do autoscaling (tempo de scale-up de novas instâncias), e comportamento sob carga extrema (o sistema degrada gracefully com respostas mais lentas ou falha catastroficamente com timeout em cascata). Para LLMs, testar com prompts de tamanho variável — latência de LLM é diretamente proporcional ao tamanho do input+output.

- **Teste de adversarial e edge cases**: Para LLMs e chatbots, testar com inputs adversariais: prompt injection ("ignore as instruções anteriores e..."), jailbreak attempts, inputs com PII (o sistema redacta ou vaza?), perguntas fora do escopo definido, inputs em idioma diferente do esperado, e inputs malformados (extremamente longos, com caracteres especiais, com encoding inválido). Para modelos de ML clássico, testar com edge cases: features com valores extremos, features ausentes, combinações incomuns que não existiam no treino.

- **Teste de integração end-to-end**: Validar o fluxo completo desde o trigger do usuário até o resultado final — não apenas a API de inferência isolada. Para chatbot: usuário digita pergunta → API recebe → preprocessing → retrieval (se RAG) → inferência → postprocessing → guardrails → resposta exibida → feedback coletado. Para batch: dados chegam → pipeline processa → modelo prediz → resultados são escritos no destino → consumidor lê corretamente. Cada ponto de integração é um ponto de falha que só aparece no teste end-to-end.

- **Teste de fallback e resiliência**: Simular falhas dos componentes críticos e verificar que os fallbacks definidos na Etapa 03 funcionam: API do LLM indisponível → fallback para modelo menor ou mensagem de indisponibilidade? Vector store down → retrieval retorna vazio e modelo gera sem contexto? Feature store com dados stale → modelo usa valor default ou recusa a predição? Cada cenário de falha deve ter um comportamento definido, implementado e testado. "Testar o caminho feliz" não é QA — testar os caminhos de falha é o que protege a produção.

- **Revisão de segurança e compliance**: Antes de promover para produção, verificar: dados pessoais estão sendo logados? (não deveriam) Respostas do modelo podem vazar informações de treino? (prompt extraction attack) API está acessível apenas por consumidores autorizados? (autenticação e rate limiting) Audit trail está completo e inalterado? (compliance) Para sistemas que tomam decisões com impacto legal (crédito, RH, saúde), verificar que a explicabilidade funciona corretamente e que os documentos de compliance estão prontos.

### Perguntas

1. A avaliação formal do modelo foi executada no dataset de teste com métricas acima dos thresholds de aprovação definidos? [fonte: Data Science, Produto] [impacto: Data Science, PM]
2. A confusion matrix (para classificação) foi analisada por classe, não apenas accuracy global? [fonte: Data Science] [impacto: Data Science]
3. O load test foi executado com volume realista e a latência P95/P99 está dentro do SLA sob carga? [fonte: DevOps, QA] [impacto: DevOps, Dev]
4. O comportamento de autoscaling foi validado — tempo de scale-up e degradação graceful sob carga extrema? [fonte: DevOps] [impacto: DevOps]
5. Os testes adversariais foram executados para LLM (prompt injection, jailbreak, PII, fora de escopo)? [fonte: QA, Segurança, Data Science] [impacto: Data Science, Segurança]
6. O teste end-to-end do fluxo completo foi executado (trigger → preprocessing → inferência → resultado → feedback)? [fonte: QA, Dev] [impacto: Dev, QA]
7. Os fallbacks foram testados com simulação de falha de cada componente crítico (LLM, vector store, feature store)? [fonte: QA, DevOps] [impacto: DevOps, Dev]
8. A API está protegida com autenticação, rate limiting e sem exposição de informações internas em mensagens de erro? [fonte: Segurança, Dev] [impacto: Dev, Segurança]
9. Os logs de inferência não contêm dados pessoais (PII) e o audit trail está completo e inalterado? [fonte: DPO, Segurança, QA] [impacto: Segurança, Compliance]
10. Para chatbot: o teste de conversação multi-turno foi executado com cenários realistas, não apenas perguntas isoladas? [fonte: QA, Produto] [impacto: QA, Data Science]
11. O custo real por request sob carga foi medido e está dentro do orçamento projetado? [fonte: DevOps, Financeiro] [impacto: PM, Arquiteto]
12. A explicabilidade do modelo (se aplicável) foi validada — as explicações fazem sentido para humanos do domínio? [fonte: Operações, Produto, Compliance] [impacto: Data Science, Produto]
13. O monitoramento de drift está ativo em staging e detectou corretamente drift artificial injetado para teste? [fonte: Data Science, MLOps] [impacto: MLOps, Data Science]
14. A documentação de limitações conhecidas do modelo foi revisada e está acessível ao time de operações? [fonte: Data Science, Produto] [impacto: Operações, PM]
15. O eval pipeline automatizado está integrado no CI/CD e bloqueia promoção se métricas caírem abaixo do threshold? [fonte: Data Science, MLOps, DevOps] [impacto: MLOps, Data Science]

---

## Etapa 09 — Launch Prep

- **Plano de rollout gradual**: IA não deve ser lançada para 100% dos usuários no dia 1. Definir a estratégia: shadow mode (modelo roda em paralelo ao processo atual, resultados são comparados mas não expostos ao usuário), canary release (5% dos usuários, monitorar por 48h, expandir para 20%, 50%, 100%), ou A/B test (metade com IA, metade sem, comparar métricas de negócio). O plano deve definir critérios de expansão (métricas acima do threshold por X horas) e critérios de rollback (métrica abaixo do threshold ou incidentes de segurança).

- **Documentação operacional**: Produzir o runbook para o time de operações que vai operar o sistema em produção. Incluir: como monitorar a saúde do sistema (quais dashboards, quais métricas, quais alertas), como interpretar alertas (o que significa "drift detected", "latency P99 > 3s", "confidence score baixo"), como escalar um problema (quem acionar quando o modelo está respondendo errado), como executar rollback de modelo (passo a passo com comandos), e como forçar re-treino se necessário. Runbook sem clareza gera pânico operacional no primeiro incidente.

- **Preparação do feedback loop**: Configurar e testar o mecanismo que vai coletar feedback dos usuários em produção e alimentar o ciclo de melhoria. Para chatbots: botões de thumbs up/down, formulário de correção, logging de escalações para humano. Para classificadores: revisão manual de amostra de predições por especialistas. Os dados de feedback devem fluir para um dataset rotulado que será usado no próximo ciclo de treino. Sem feedback loop configurado antes do go-live, o modelo fica congelado em produção e degrada silenciosamente.

- **Treinamento dos times de operação e suporte**: Treinar o time que vai interagir com o sistema pós-lançamento — operadores que monitoram, suporte que recebe reclamações, e gestores que consomem métricas. O treinamento deve cobrir: o que o modelo faz e o que não faz (gestão de expectativas), como identificar problemas (quais sintomas indicam degradação), quando escalar para o time técnico, e como usar os dashboards de monitoramento. Entregar documentação em formato prático (não paper acadêmico) com exemplos reais e cenários de troubleshooting.

- **Plano de contingência e rollback**: Documentar o plano de rollback completo: se o modelo em produção apresentar comportamento inaceitável (alucinações graves, vazamento de dados, latência insustentável), qual é a sequência de ações? Opções: reverter para versão anterior do modelo (model registry), desativar a feature de IA via feature flag e manter o fluxo sem IA, ou escalar 100% do tráfego para atendimento humano. Definir quem tem autoridade para acionar o rollback e o tempo máximo para decisão (SLA de incidente). Testar o rollback em staging antes do go-live — não no dia do incidente.

### Perguntas

1. A estratégia de rollout gradual foi definida (shadow mode, canary, A/B) com critérios de expansão e rollback? [fonte: Produto, Data Science, Diretoria] [impacto: DevOps, PM, Data Science]
2. O runbook operacional foi produzido com instruções de monitoramento, interpretação de alertas e procedimento de escalação? [fonte: Data Science, DevOps] [impacto: Operações, MLOps]
3. O mecanismo de feedback loop está configurado e testado (coleta de feedback → dataset → pipeline de re-treino)? [fonte: Dev, Data Science] [impacto: Data Science, Dev]
4. O time de operações e suporte foi treinado sobre o que o modelo faz, suas limitações e como identificar problemas? [fonte: Data Science, PM] [impacto: Operações, Suporte]
5. O plano de rollback está documentado com sequência de ações, responsáveis e tempo máximo para decisão? [fonte: DevOps, Data Science, Diretoria] [impacto: DevOps, PM]
6. O feature flag para desativar a IA sem deploy está testado e funcional em produção? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
7. O modelo final foi registrado no model registry com todas as métricas e pronto para promoção para produção? [fonte: Data Science, MLOps] [impacto: MLOps, Data Science]
8. Os dashboards de monitoramento de produção estão configurados e acessíveis ao time de operações? [fonte: DevOps, Data Science] [impacto: Operações, MLOps]
9. Os alertas de produção foram testados — disparam corretamente quando thresholds são ultrapassados? [fonte: DevOps] [impacto: DevOps, MLOps]
10. O custo projetado para o primeiro mês de operação foi revisado e aprovado pelo financeiro? [fonte: Financeiro, DevOps] [impacto: PM, Diretoria]
11. A comunicação de lançamento foi preparada para os usuários finais (o que é, como usar, limitações, como dar feedback)? [fonte: Produto, Marketing] [impacto: PM, Produto]
12. Os termos de uso e política de privacidade foram atualizados para refletir o uso de IA (se aplicável à regulamentação)? [fonte: Jurídico, DPO] [impacto: Jurídico, PM]
13. O teste de rollback foi executado em staging — reversão para modelo anterior e desativação via feature flag funcionaram corretamente? [fonte: DevOps, Data Science] [impacto: DevOps, MLOps]
14. O processo de promoção de modelo (staging → prod) foi testado e está documentado com checklist de verificação? [fonte: MLOps, DevOps] [impacto: MLOps, DevOps]
15. A janela de lançamento foi escolhida em dia útil, horário comercial, com time técnico disponível por pelo menos 4h após o go-live? [fonte: PM, DevOps] [impacto: PM, DevOps, Data Science]

---

## Etapa 10 — Go-Live

- **Ativação do modelo em produção**: Executar a promoção do modelo para produção conforme o plano definido — shadow mode, canary ou ativação com feature flag. Monitorar em tempo real nos primeiros 30 minutos: latência de inferência, taxa de erro, distribuição de confidence scores, e primeiras respostas/predições para validação manual. Para chatbots, revisar manualmente as primeiras 20-50 conversas para identificar alucinações, respostas fora do escopo, ou formatação quebrada que não foram capturadas no QA.

- **Monitoramento intensivo na primeira semana**: Os primeiros 7 dias são críticos. Monitorar diariamente: métricas de modelo (accuracy, confidence distribution, taxa de fallback), métricas operacionais (latência, error rate, custo diário), métricas de negócio (taxa de adoção, taxa de feedback positivo/negativo, volume de escalações para humano), e métricas de segurança (tentativas de prompt injection, dados sensíveis nos logs). Comparar todas as métricas com os baselines definidos no QA. Drift significativo nos primeiros dias geralmente indica diferença entre dados de teste e dados reais de produção, não degradação do modelo.

- **Coleta e análise de feedback inicial**: Nos primeiros dias, o feedback dos usuários é ouro. Analisar sistematicamente: quais perguntas/inputs geram respostas ruins? Quais cenários não foram cobertos no QA? Quais expectativas dos usuários não foram atendidas? Esse feedback é o input para o primeiro ciclo de melhoria. Para chatbots, revisar as conversas com thumbs down e as escalações para humano — são os casos mais ricos para ajuste de prompt e adição de documentos no RAG.

- **Expansão gradual e decisão de rollout completo**: Se o plano é canary ou A/B, monitorar as métricas de cada grupo por pelo menos 48-72h antes de expandir. A decisão de expandir deve ser baseada em dados, não em pressão de prazo. Critérios mínimos para expansão: métricas de modelo acima do threshold, custo por request dentro do orçamento, zero incidentes de segurança, e feedback qualitativo predominantemente positivo. Documentar a decisão de expansão com os dados que a justificaram — se precisar de rollback depois, o histórico de decisão é valioso.

- **Handoff e operação contínua**: Transferir a operação do sistema para o time permanente (MLOps, operações) com documentação completa: runbook atualizado com os aprendizados do go-live, dashboards finais, alertas calibrados (remover falsos positivos que apareceram na primeira semana), pipeline de feedback loop operacional, e cronograma do primeiro ciclo de re-treino. O handoff não é "jogar por cima do muro" — é um período de shadowing onde o time de build acompanha o time de operações por 1-2 semanas para transferência efetiva de conhecimento.

### Perguntas

1. O modelo foi ativado em produção conforme o plano (shadow, canary ou feature flag) e monitorado em tempo real nos primeiros 30 minutos? [fonte: DevOps, Data Science] [impacto: DevOps, MLOps, Data Science]
2. As primeiras predições/respostas foram revisadas manualmente para validar qualidade em dados reais de produção? [fonte: Data Science, Operações] [impacto: Data Science, QA]
3. A latência P95/P99 em produção está dentro do SLA com tráfego real? [fonte: DevOps] [impacto: DevOps, Dev]
4. O custo diário de inferência real está dentro da projeção aprovada? [fonte: DevOps, Financeiro] [impacto: PM, Diretoria]
5. O monitoramento de drift está ativo e não detectou divergência significativa entre dados de teste e dados de produção? [fonte: Data Science, MLOps] [impacto: Data Science, MLOps]
6. O feedback dos primeiros usuários foi coletado e os casos negativos foram analisados para identificar padrões? [fonte: Produto, Data Science] [impacto: Data Science, Produto]
7. Para canary/A/B: os critérios de expansão foram atingidos com dados e a decisão de expansão está documentada? [fonte: Data Science, Produto, DevOps] [impacto: PM, Data Science]
8. Zero incidentes de segurança (prompt injection, vazamento de dados, conteúdo tóxico) foram detectados nas primeiras 48h? [fonte: Segurança, Data Science] [impacto: Segurança, Data Science]
9. As escalações para humano (se aplicável) estão sendo tratadas e os motivos estão sendo registrados para melhoria? [fonte: Operações, Data Science] [impacto: Operações, Data Science]
10. Os alertas de produção estão calibrados — sem excesso de falsos positivos e sem alertas críticos silenciados? [fonte: DevOps, MLOps] [impacto: DevOps, MLOps]
11. O runbook foi atualizado com os aprendizados do go-live (alertas novos, cenários não previstos, ajustes de threshold)? [fonte: DevOps, Data Science] [impacto: Operações, MLOps]
12. O pipeline de feedback loop está operacional — dados de feedback estão fluindo para o dataset de treino futuro? [fonte: Data Science, Dev] [impacto: Data Science, MLOps]
13. O handoff para o time de operações permanente foi iniciado com período de shadowing definido? [fonte: PM, Data Science] [impacto: Operações, MLOps]
14. O cronograma do primeiro ciclo de re-treino foi definido com base nos dados do go-live? [fonte: Data Science, MLOps] [impacto: Data Science, MLOps]
15. O aceite formal de entrega foi obtido com métricas de performance documentadas e contrato de SLA ativado? [fonte: Diretoria, Produto] [impacto: PM]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos usar IA generativa porque todo mundo está usando"** — Motivação por hype, não por problema de negócio. Se não existe métrica atual a melhorar ou processo manual a automatizar, não existe critério de sucesso. Resultado: PoC que impressiona em demo, nunca vai para produção, e gera frustração executiva com IA.
- **"Nossos dados são muito bons, estão todos no banco"** — Superestimação da qualidade dos dados sem assessment formal. "Tudo no banco" pode significar 40% de campos nulos, dados de 5 anos sem limpeza, schemas inconsistentes entre tabelas, e ausência de labels para treino supervisionado. Validar antes de prometer resultado.
- **"Queremos 99% de acurácia"** — Expectativa de software determinístico aplicada a sistema probabilístico. A precisão alcançável depende da qualidade dos dados, da complexidade do problema e do domínio. Se a taxa de erro humano na tarefa é 15%, esperar 1% de erro do modelo é ilusão.

### Etapa 02 — Discovery

- **"A gente tem milhões de registros"** — Volume não garante qualidade. Um milhão de registros com 30% de duplicatas, 20% de dados incorretos e 10% de campos nulos pode ser inferior a 10 mil registros limpos e bem rotulados. O assessment de qualidade é mais importante que a contagem de registros.
- **"O modelo vai aprender sozinho com o tempo"** — Confusão entre supervised learning e aprendizado contínuo automático. A maioria dos modelos precisa ser re-treinada explicitamente com dados novos e labels. "Aprender sozinho" exige feedback loop formal, pipeline de anotação e ciclo de re-treino — nada disso é automático.
- **"Não precisa de baseline, sabemos que precisa melhorar"** — Sem baseline quantificado, não há como medir melhoria. Se o processo atual não foi mensurado, o modelo pode ter performance inferior ao status quo sem que ninguém perceba.

### Etapa 03 — Alignment

- **"O modelo não pode errar nunca"** — Exigência de infalibilidade é incompatível com ML. O alinhamento correto é definir taxa de erro aceitável, impacto de cada tipo de erro, e mecanismo de mitigação. Se a tolerância a erro é zero, a solução não é IA — é sistema de regras determinísticas ou processo humano.
- **"Vamos lançar para todo mundo de uma vez"** — Rollout big bang de IA é aposta desnecessária. Shadow mode, canary release e A/B test existem para reduzir risco. Se o stakeholder insiste em lançamento total no dia 1, documentar o risco formalmente.
- **"O jurídico vê depois"** — Postergar compliance para o final em projetos de IA é especialmente perigoso. LGPD, regulamentação setorial e requisitos de explicabilidade impactam a arquitetura (self-hosted vs. API, logging vs. anonimização), não apenas o texto da política de privacidade.

### Etapa 04 — Definition

- **"O prompt a gente vai ajustando em produção"** — Prompt sem versão, sem testes e sem processo de aprovação é código sem CI/CD. Cada mudança de prompt pode alterar fundamentalmente o comportamento do sistema. Definir processo de versionamento e avaliação antes do build.
- **"Não precisa de dataset de teste formal"** — Sem eval dataset, a decisão de "o modelo está bom" é subjetiva. O dataset de teste deve ser curado, representativo e validado por especialistas do domínio. Criá-lo depois do build gera viés de confirmação.
- **"Monitoramento a gente implementa depois do lançamento"** — Definir monitoramento depois do go-live significa operar às cegas durante o período mais crítico. As métricas, thresholds e alertas devem ser especificados antes do setup e configurados antes do build.

### Etapa 05 — Architecture

- **"Vamos fine-tunar o GPT-4 com nossos dados"** — Fine-tuning de modelo proprietário raramente é a primeira escolha correta. Para a maioria dos casos, RAG + prompt engineering resolve. Fine-tuning é caro, lento, requer dataset de alta qualidade, e trava a versão do modelo base. Justificar com evidência de que RAG não resolve antes de fine-tunar.
- **"GPU dedicada 24/7 para servir o modelo"** — GPU idle custa $1000-5000/mês. Para a maioria das cargas de trabalho, serverless GPU (Modal, Replicate, RunPod serverless) ou autoscaling com scale-to-zero é significativamente mais econômico. GPU fixa só se justifica com tráfego constante e previsível.
- **"Não precisa de cache, cada pergunta é diferente"** — Em chatbots corporativos, 30-40% das perguntas são repetidas ou semanticamente similares. Cache semântico pode reduzir custo e latência dramaticamente. Negar a necessidade de cache sem analisar a distribuição real de queries é otimização prematuramente recusada.

### Etapa 06 — Setup

- **"Cada um usa seu notebook local para treinar"** — Sem experiment tracking centralizado, experimentos não são reproduzíveis, não são comparáveis, e o conhecimento é perdido quando o data scientist sai do time. MLflow ou W&B devem ser configurados antes do primeiro experimento.
- **"Os dados de produção estão no meu laptop"** — Dados sensíveis em máquinas locais sem criptografia violam LGPD e políticas de segurança. Dados devem ser acessados em ambiente controlado, auditado e criptografado.
- **"Staging é igual a produção, só sem dados reais"** — Staging sem dados representativos não testa o que importa. Distribuições de dados diferentes entre staging e produção são a principal causa de degradação pós-deploy. Usar dados anonimizados ou sintéticos que preservem a distribuição estatística.

### Etapa 07 — Build

- **"O modelo no notebook já funciona, é só colocar em API"** — O gap entre notebook e produção é enorme. Código de notebook não tem tratamento de erros, não é testável, não lida com concorrência, e não monitora nada. A "produtivização" do modelo frequentemente leva mais tempo que o desenvolvimento do modelo em si.
- **"Vamos otimizar a acurácia ao máximo antes de lançar"** — Perseguir o último 1% de acurácia tem rendimentos decrescentes exponenciais. Um modelo com 85% que está em produção gerando valor é infinitamente melhor que um modelo com 87% que está no notebook há 3 meses. Lançar cedo, coletar feedback, iterar.
- **"Guardrails a gente adiciona se der problema"** — Reativo, não proativo. O primeiro incidente de alucinação grave, vazamento de dados ou conteúdo tóxico em produção terá impacto reputacional antes de qualquer fix ser deployado. Guardrails são parte do MVP.

### Etapa 08 — QA

- **"A acurácia no teste é 92%, está ótimo"** — Acurácia global pode mascarar performance terrível em segmentos críticos. Um classificador de fraude com 92% de acurácia pode estar errando 80% das fraudes reais (recall baixo) enquanto acerta todos os legítimos. Métricas por classe e métricas de custo assimétrico são obrigatórias.
- **"Testamos com 10 perguntas e funcionou bem"** — Teste manual com poucos exemplos cherry-picked não é QA. Avaliação formal requer dataset representativo com centenas ou milhares de exemplos, métricas automatizadas, e cobertura de edge cases e cenários adversariais.
- **"Não precisa de load test, vai ter pouco tráfego no início"** — O "pouco tráfego" pode ser pouco de forma imprevisível. Um pico causado por campanha de marketing, notícia viral ou batch processing simultâneo pode derrubar um sistema que nunca foi testado sob carga. Load test revela problemas de arquitetura que são caros de corrigir depois.

### Etapa 09 — Launch Prep

- **"Vamos lançar para 100% na segunda-feira"** — Big bang de IA é aposta desnecessária. Canary com 5% do tráfego por 48h é trivial de implementar e reduz dramaticamente o blast radius de qualquer problema. A urgência raramente justifica o risco.
- **"O time de suporte já sabe o que é IA"** — "Saber o que é IA" e "saber operar este sistema específico de IA com seus limites, dashboards e procedimentos de escalação" são coisas completamente diferentes. Treinamento específico com cenários do sistema real é insubstituível.
- **"Se der problema a gente desliga"** — "Desligar" sem plano documentado pode significar indisponibilidade do serviço, estado inconsistente, ou perda de dados de feedback. O rollback precisa ser testado, não improvisado.

### Etapa 10 — Go-Live

- **"O modelo está no ar, trabalho do data science acabou"** — Data science sem monitoramento e re-treino é como lançar e abandonar. O modelo vai degradar conforme os dados mudam (concept drift), e sem monitoramento ativo, a degradação só é percebida quando o impacto de negócio é mensurável — meses depois.
- **"Go-live na sexta porque o sprint acaba sexta"** — Se o modelo aluinar ou degradar no fim de semana, não há time disponível. Go-live deve ser em dia útil, horário comercial, com buffer de pelo menos 4h e time técnico de sobreaviso por 48h.
- **"Não precisa de período de shadow/canary, já testamos tudo"** — Dados reais de produção são sempre diferentes dos dados de teste. Distribuições mudam, inputs inesperados aparecem, e integrações se comportam diferente sob carga real. Shadow mode de 24-48h é seguro e barato.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é aplicação de IA/ML** como descrito e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Queremos um dashboard com gráficos dos nossos dados" | BI / Analytics, não IA | Reclassificar para data-platform ou web-app |
| "Precisa automatizar o envio de e-mails com regras" | Automação de workflow, não ML | Reclassificar para workflow-automation ou integração |
| "Queremos um chatbot com respostas fixas, sem IA" | Chatbot baseado em regras / decision tree | Reclassificar para web-app ou usar ferramenta no-code |
| "É só uma API que consulta o banco e retorna dados" | API REST tradicional, sem modelo | Reclassificar para api-platform |
| "Queremos integrar o ChatGPT no nosso site" | Widget de chat genérico, não solução custom | Avaliar se wrapper simples resolve ou se precisa de solução custom |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos onde estão nossos dados" | 01 | Sem dados, não há projeto de IA | Resolver acesso e inventário de dados antes de iniciar |
| "Os dados são confidenciais, não podemos compartilhar" | 01 | Time de data science não consegue trabalhar | Definir ambiente seguro, NDA, anonimização — ou cancelar |
| "Não temos orçamento para GPU ou APIs pagas" | 01 | Operação em produção inviável | Apresentar custo realista e obter aprovação antes de continuar |
| "O jurídico ainda não validou o uso de IA com dados de clientes" | 03 | Violação de LGPD pode gerar multa e dano reputacional | Obter parecer jurídico antes de processar qualquer dado pessoal |
| "Não temos labels/anotações para treinar o modelo" | 02 | Sem labels, ML supervisionado é impossível | Incluir processo de anotação no escopo ou pivotar para abordagem não-supervisionada |
| "O modelo não pode errar em nenhum caso" | 03 | Expectativa incompatível com IA | Alinhar que IA é probabilística antes de continuar |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Os dados estão em planilhas Excel espalhadas" | 02 | Esforço de engenharia de dados pode dominar o projeto | Estimar esforço de ETL separadamente e incluir no cronograma |
| "O time de data science é uma pessoa só" | 01 | Risco de pessoa — se sair, o projeto para | Documentar tudo, pair programming, e plano de contingência |
| "Precisamos de resultado em 2 semanas" | 01 | PoC é possível, produção não | Alinhar que o resultado em 2 semanas é PoC, não sistema final |
| "O modelo precisa funcionar em tempo real" | 02 | Latência <100ms requer arquitetura específica e possivelmente GPU | Validar que o modelo escolhido é compatível com o SLA de latência |
| "Queremos que a IA tome decisões automaticamente" | 03 | Full automation sem human-in-the-loop em domínio crítico | Documentar risco legal e operacional; recomendar hybrid approach |
| "Não sabemos quantos requests teremos por dia" | 05 | Impossível dimensionar infra e custo | Estimar com base em dados do processo atual e projetar cenários |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Problema de negócio quantificado com métrica baseline (pergunta 1)
- Dados existem e são acessíveis (pergunta 2)
- Sensibilidade dos dados avaliada e compliance endereçado (pergunta 4)
- Orçamento de operação (inferência) apresentado e aprovado (pergunta 5)
- Objetivo definido — PoC ou produção (pergunta 6)

### Etapa 02 → 03

- Inventário de dados com qualidade assessment realizado (perguntas 1, 2 e 3)
- Problema traduzido em tarefa de ML específica (pergunta 4)
- Baseline de performance atual quantificado (pergunta 5)
- Requisitos de latência e throughput definidos (pergunta 6)
- Viés nos dados avaliado (pergunta 15)

### Etapa 03 → 04

- Stakeholders aceitaram formalmente a taxa de erro do modelo (pergunta 1)
- Métricas de ML mapeadas para KPIs de negócio (pergunta 2)
- Estratégia de human-in-the-loop definida (pergunta 3)
- Governança do modelo definida (pergunta 5)
- Validação jurídica do uso de dados concluída (pergunta 14)

### Etapa 04 → 05

- Features de entrada especificadas com contrato formal (pergunta 1)
- Schema de API de inferência definido (pergunta 3)
- Dataset de avaliação definido e validado (pergunta 4)
- Thresholds de aprovação para produção definidos (pergunta 5)
- Plano de monitoramento especificado (pergunta 7)

### Etapa 05 → 06

- Modelo base e arquitetura de serving escolhidos e justificados (perguntas 1 e 2)
- Segurança e isolamento de dados definidos (pergunta 6)
- Custos mensais calculados em cenários de volume (pergunta 9)
- CI/CD de modelo desenhado (pergunta 11)
- Ambientes e modelo de branches documentados (pergunta 15)

### Etapa 06 → 07

- Ambiente de experimentação configurado com experiment tracking (pergunta 1)
- Pipeline de dados testado end-to-end com dados reais (pergunta 3)
- Infraestrutura de serving configurada com autoscaling (pergunta 5)
- Monitoramento e alertas configurados (pergunta 6)
- Ambiente de avaliação automática operacional (pergunta 10)

### Etapa 07 → 08

- Modelo supera baseline com margem documentada (pergunta 2)
- API de inferência implementada com logging e tratamento de erros (pergunta 3)
- Guardrails implementados e testáveis (pergunta 4)
- Testes automatizados cobrindo preprocessing, contrato de API e eval (pergunta 7)
- Modelo registrado no model registry (pergunta 11)

### Etapa 08 → 09

- Avaliação formal no dataset de teste acima dos thresholds (pergunta 1)
- Load test executado com latência dentro do SLA (pergunta 3)
- Testes adversariais executados para LLM (pergunta 5)
- Fallbacks testados com simulação de falha (pergunta 7)
- Eval pipeline integrado no CI/CD (pergunta 15)

### Etapa 09 → 10

- Estratégia de rollout gradual definida com critérios (pergunta 1)
- Runbook operacional produzido e revisado (pergunta 2)
- Feedback loop configurado e testado (pergunta 3)
- Plano de rollback testado em staging (pergunta 13)
- Feature flag testado e funcional (pergunta 6)

### Etapa 10 → Encerramento

- Modelo ativado em produção e monitorado em tempo real (pergunta 1)
- Primeiras predições revisadas manualmente (pergunta 2)
- Custo real dentro da projeção (pergunta 4)
- Feedback coletado e analisado (pergunta 6)
- Handoff para operações iniciado com shadowing (pergunta 13)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de aplicação de IA/ML. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Chatbot | V2 RAG Pipeline | V3 Inference API | V4 ML Pipeline | V5 IA Embarcada |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 2 | 3 | 2 |
| 02 Discovery | 2 | 3 | 4 | 5 | 2 |
| 03 Alignment | 3 | 2 | 3 | 3 | 3 |
| 04 Definition | 3 | 4 | 4 | 5 | 3 |
| 05 Architecture | 3 | 4 | 4 | 5 | 3 |
| 06 Setup | 3 | 4 | 4 | 5 | 2 |
| 07 Build | 4 | 4 | 4 | 5 | 4 |
| 08 QA | 4 | 3 | 4 | 4 | 4 |
| 09 Launch Prep | 3 | 2 | 3 | 3 | 3 |
| 10 Go-Live | 3 | 2 | 3 | 3 | 3 |
| **Total relativo** | **30** | **30** | **35** | **41** | **29** |

**Observações por variante:**

- **V1 Chatbot**: Esforço concentrado no Build (prompt engineering, guardrails, UX de conversa) e QA (testes adversariais, multi-turno, edge cases). Discovery é relativamente leve porque não envolve treinamento — o desafio é qualidade de prompt e retrieval.
- **V2 RAG Pipeline**: Pico na Definition (estratégia de chunking, schema de metadados, eval framework) e Architecture (vector store, pipeline de re-indexação). Build é moderado porque o modelo de geração é consumido via API.
- **V3 Inference API**: Esforço alto e distribuído. Discovery é pesado (assessment de dados, definição de task ML) e Architecture é complexa (serving, autoscaling, versionamento). QA exige load test e testes de drift.
- **V4 ML Pipeline**: A variante mais pesada. Discovery e Definition são intensos (feature engineering, pipeline de treino, evaluation framework). Setup e Build envolvem infraestrutura de MLOps completa. É o único tipo onde o data scientist pode dominar o esforço total.
- **V5 IA Embarcada**: Esforço concentrado no Build (integração com produto existente, UX de IA, feature flags) e QA (testar IA no contexto do produto, não isolada). Discovery é leve porque o problema de negócio geralmente já está definido pelo produto existente.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Modelo via API externa, sem treinamento custom (Etapa 05, pergunta 1) | Etapa 04: perguntas 10, 14 (critérios de re-treino, processo de anotação). Etapa 05: perguntas 4 e 5 (pipeline de treinamento, feature store). Etapa 06: perguntas 9, 11, 12 (experiment tracking, model registry, versionamento de dados). Etapa 07: perguntas 1, 11, 15 (experimentação, model registry, re-treino). |
| Sem RAG — modelo direto sem retrieval (Etapa 04, pergunta 8) | Etapa 04: pergunta 8 (estratégia de chunking). Etapa 05: pergunta 3 (vector store). Etapa 06: pergunta 4 (pipeline de ingestão RAG). Etapa 07: pergunta 12 (métricas de retrieval). |
| PoC sem produção (Etapa 01, pergunta 6) | Etapa 05: perguntas 2, 7, 8, 11, 13 (serving, cache, fallback, CI/CD, A/B). Etapa 06: perguntas 5, 6, 8 (serving, monitoramento, isolamento). Etapa 08: perguntas 3, 4, 7 (load test, autoscaling, fallback). Etapa 09: todas. Etapa 10: todas. |
| Full automation sem human-in-the-loop (Etapa 03, pergunta 3) | Etapa 07: pergunta 9 (mecanismo de feedback de escalação). Etapa 09: perguntas 4 e 11 (treinamento de operações, comunicação de lançamento). Etapa 10: pergunta 9 (escalações para humano). |
| Batch processing, sem API em tempo real (Etapa 02, pergunta 6) | Etapa 05: perguntas 7 e 10 (cache de inferência, latência end-to-end). Etapa 07: pergunta 6 (streaming SSE). Etapa 08: perguntas 3 e 4 (load test, autoscaling). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Dados contêm PII ou são sensíveis (Etapa 01, pergunta 4) | Etapa 03: pergunta 14 (validação jurídica LGPD) se torna bloqueadora. Etapa 05: pergunta 6 (segurança e anonimização) se torna gate. Etapa 06: perguntas 2 e 7 (ambiente seguro, secrets management). Etapa 08: pergunta 9 (PII nos logs). |
| Domínio regulado — saúde, financeiro, jurídico (Etapa 01, pergunta 15) | Etapa 02: pergunta 7 (explicabilidade) se torna obrigatória. Etapa 03: pergunta 6 (responsabilidade legal) se torna gate. Etapa 04: pergunta 12 (limitações documentadas). Etapa 08: pergunta 12 (explicabilidade validada por humanos do domínio). |
| Modelo treinado internamente, não via API (Etapa 05, pergunta 1) | Etapa 04: perguntas 1, 10, 14 (features, re-treino, anotação) se tornam gates. Etapa 05: perguntas 4 e 5 (pipeline de treinamento, feature store). Etapa 06: perguntas 9, 11, 12 (experiment tracking, model registry, versionamento de dados). Etapa 07: perguntas 1 e 15 (experimentação e pipeline de re-treino). |
| Chatbot/assistente voltado para cliente externo (Etapa 01, pergunta 7) | Etapa 03: pergunta 12 (tom de voz, escopo, escalação) se torna gate. Etapa 04: pergunta 13 (cenários de teste de conversação). Etapa 07: pergunta 4 (guardrails) se torna gate. Etapa 08: perguntas 5 e 10 (adversarial, multi-turno). |
| Volume alto de inferência — >10.000 requests/dia (Etapa 02, pergunta 6) | Etapa 05: perguntas 2, 7 e 9 (serving, cache, custo) se tornam gates. Etapa 06: pergunta 5 (autoscaling) se torna gate. Etapa 08: perguntas 3 e 11 (load test, custo real). Etapa 10: pergunta 4 (custo diário real). |
| Rollout com A/B test ou canary (Etapa 09, pergunta 1) | Etapa 05: pergunta 13 (arquitetura suporta A/B/shadow) se torna gate. Etapa 10: pergunta 7 (critérios de expansão baseados em dados). |
