---
title: "Pipeline de Dados / ETL-ELT — Blueprint"
description: "Processo de ingestão, transformação e carga de dados. Pode ser batch (ETL) ou em tempo real (streaming). Foco em qualidade, latência e resiliência da cadeia de dados."
category: project-blueprint
type: data-pipeline
status: rascunho
created: 2026-04-13
---

# Pipeline de Dados / ETL-ELT

## Descrição

Processo de ingestão, transformação e carga de dados. Pode ser batch (ETL) ou em tempo real (streaming). Foco em qualidade, latência e resiliência da cadeia de dados.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo pipeline de dados é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — ETL Batch Simples

Pipeline que roda em schedule fixo (diário, horário, semanal) extraindo dados de uma ou poucas fontes (banco relacional, arquivo CSV/JSON, API REST), transformando com regras de negócio simples (limpeza, deduplicação, agregação) e carregando em um destino único (data warehouse, banco analítico). Volume de dados moderado (milhares a milhões de registros por execução). O foco é confiabilidade, idempotência (reprocessar sem duplicar) e observabilidade (saber se rodou, se falhou, e o que falhou). Exemplos: carga diária de vendas para BI, sincronização noturna de cadastros entre sistemas, extração semanal de relatórios para compliance.

### V2 — ELT com Data Warehouse Moderno

Pipeline que extrai dados brutos de múltiplas fontes e carrega diretamente no data warehouse (BigQuery, Snowflake, Redshift, Databricks) onde as transformações acontecem via SQL usando ferramentas como dbt. O paradigma ELT desloca a complexidade de transformação para o warehouse, que tem compute elástico para processar grandes volumes. O foco é governança de dados (lineage, catalogação, controle de acesso), qualidade de dados (testes automatizados por coluna/tabela com dbt tests), e custo de warehouse (queries mal otimizadas no Snowflake podem gerar faturas surpreendentes). Exemplos: data platform corporativa, lake house com camadas bronze/silver/gold, plataforma de dados para data science.

### V3 — Streaming / Tempo Real

Pipeline que processa eventos conforme chegam, com latência de segundos a minutos (near real-time) ou milissegundos (real-time). Usa message broker (Kafka, Kinesis, Pub/Sub) como backbone e processadores de stream (Flink, Spark Streaming, Kafka Streams) para transformação em trânsito. O foco é latência (tempo entre o evento acontecer e o dado estar disponível no destino), throughput (milhares a milhões de eventos por segundo), e exatamente-uma-vez (exactly-once semantics para evitar duplicação ou perda). Complexidade operacional significativamente maior que batch. Exemplos: detecção de fraude em tempo real, atualização de preços dinâmicos, monitoramento de IoT, feed de eventos para personalização.

### V4 — Integração de Dados entre Sistemas (iPaaS / CDC)

Pipeline focado em manter dados sincronizados entre sistemas operacionais (CRM, ERP, e-commerce, helpdesk) em near real-time usando Change Data Capture (CDC) ou APIs de webhook. Diferente de ETL analítico, o destino é outro sistema operacional (não warehouse) e a latência tolerada é baixa (minutos). O foco é consistência eventual entre sistemas (o que muda no CRM aparece no ERP em <5 minutos), tratamento de conflitos (o que acontece quando o mesmo registro é alterado nos dois sistemas simultaneamente), e resiliência (se um sistema está fora, os dados ficam em fila e são sincronizados quando voltar). Exemplos: sincronização de clientes entre Salesforce e SAP, replicação de pedidos de e-commerce para ERP, integração de tickets Zendesk com CRM.

### V5 — Pipeline de Machine Learning (Feature Store / Training Pipeline)

Pipeline especializado em preparar dados para modelos de ML: extração de features a partir de dados brutos, transformação e normalização, armazenamento em feature store (para servir online e offline), e orquestração de training pipelines (re-treinamento automático quando novos dados chegam). O foco é reprodutibilidade (mesmos dados → mesmo resultado), versionamento de datasets e features, detecção de data drift (distribuição dos dados mudou e o modelo precisa ser re-treinado), e servir features com latência baixa para inferência online. Exemplos: feature store para modelo de recomendação, pipeline de treinamento de modelo de risco de crédito, preparação de dados para NLP.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Orquestração | Transformação | Armazenamento | Ingestão | Observações |
|---|---|---|---|---|---|
| V1 — ETL Batch | Airflow ou Prefect | Python (pandas, polars) ou Spark | PostgreSQL, BigQuery ou S3+Athena | Airbyte, custom scripts | Para volumes <10M registros, pandas/polars resolve sem Spark. Airflow é padrão de mercado. |
| V2 — ELT DW | Airflow ou Dagster | dbt (SQL) | BigQuery, Snowflake ou Databricks | Fivetran, Airbyte ou Stitch | dbt é o padrão para transformação no warehouse. Fivetran para fontes SaaS (zero code). |
| V3 — Streaming | Kafka + Flink ou Spark Streaming | Flink SQL, Kafka Streams ou Spark | Kafka (buffer), BigQuery ou ClickHouse | Kafka Connect, Debezium (CDC) | Kafka é o backbone. Flink para processamento stateful complexo. ClickHouse para analytics real-time. |
| V4 — Integração CDC | n8n, Temporal ou Airflow | Python ou Node.js | Kafka (buffer), banco destino | Debezium (CDC), webhooks, APIs | CDC via Debezium captura mudanças no banco fonte sem polling. Temporal para workflows complexos com retry. |
| V5 — ML Pipeline | Kubeflow, MLflow ou Vertex AI | Spark, pandas, Feature Store (Feast/Tecton) | S3/GCS + Feature Store | Custom extractors, Spark | Feast (open-source) ou Tecton (managed) para feature store. MLflow para tracking de experimentos. |

---

## Etapa 01 — Inception

- **Origem da demanda e problema de dados**: A necessidade de um pipeline costuma surgir de: dados indisponíveis para decisão (BI sem dados atualizados, relatórios manuais em Excel), dados inconsistentes entre sistemas (CRM diz uma coisa, ERP diz outra), latência inaceitável (dados de vendas de ontem só ficam disponíveis 48h depois), ou iniciativa de data platform (centralizar dados para analytics e ML). Entender o gatilho real define o KPI de sucesso: se o problema é latência, o SLA de freshness é central; se é inconsistência, a qualidade de dados é prioridade; se é custo, a eficiência do pipeline é o foco.

- **Stakeholders e consumidores de dados**: O patrocinador formal costuma ser o CTO, CDO (Chief Data Officer) ou diretor de BI, mas os consumidores reais dos dados são analistas, cientistas de dados, ou outros sistemas. É frequente que esses dois grupos tenham expectativas diferentes — o patrocinador quer "todos os dados centralizados", enquanto os analistas querem "os dados de vendas atualizados a cada hora, limpos e confiáveis". Identificar os consumidores concretos e suas necessidades reais de dados evita construir pipeline que serve a todos em teoria e a ninguém na prática.

- **Fontes de dados e acesso**: Mapear todas as fontes de dados relevantes desde a Inception: bancos de dados operacionais (MySQL, PostgreSQL, SQL Server, Oracle), APIs de SaaS (Salesforce, HubSpot, Shopify, Google Analytics), arquivos (CSV/JSON em SFTP ou S3), sistemas legados (mainframe, FTP, flat files). Para cada fonte, identificar: quem é o dono, existe acesso disponível (credenciais, VPN, firewall rules), qual o volume de dados, e qual a qualidade percebida. Fontes sem acesso são bloqueadores que podem levar semanas para resolver — principalmente em empresas com segurança corporativa rigorosa.

- **Orçamento de infraestrutura de dados**: Custos de pipeline de dados são frequentemente subestimados. BigQuery cobra por query (USD 5/TB scanned), Snowflake cobra por compute por segundo, Kafka managed (Confluent Cloud) começa em centenas de dólares/mês, Fivetran cobra por MAR (Monthly Active Rows). Um pipeline que parece simples pode custar R$500/mês ou R$50.000/mês dependendo do volume, da frequência e das ferramentas escolhidas. Apresentar estimativa de custo operacional mensal nesta fase é obrigatório para evitar surpresa após o go-live.

- **Regulamentação e sensibilidade dos dados**: Dados de pipeline frequentemente incluem PII (dados pessoais), dados financeiros, ou dados de saúde — todos sujeitos a LGPD, GDPR, SOX ou HIPAA. A classificação dos dados impacta: onde podem ser armazenados (residência de dados), quem pode acessar (RBAC, data masking), por quanto tempo podem ser retidos (política de retenção), e se precisam ser criptografados em trânsito e repouso. Ignorar a classificação de dados na Inception resulta em refatoração custosa quando compliance descobre o pipeline 6 meses depois.

- **Expectativa de latência e freshness**: A diferença entre "dados atualizados todo dia às 6h" e "dados atualizados em tempo real" é a diferença entre um cron job simples e uma arquitetura de streaming complexa. A maioria dos casos de uso de BI funciona perfeitamente com batch diário ou horário. Streaming só se justifica quando a latência impacta decisão operacional imediata (fraude, pricing dinâmico, alertas de monitoramento). Definir o SLA de freshness com o consumidor real (não com o patrocinador) evita over-engineering.

### Perguntas

1. Qual é o problema concreto de dados que este pipeline deve resolver — dados indisponíveis, inconsistentes, atrasados, ou dispersos? [fonte: Diretoria, BI, Dados] [impacto: PM, Engenheiro de Dados]
2. Quem são os consumidores reais dos dados (analistas, cientistas de dados, outros sistemas, dashboards) e qual o uso concreto? [fonte: BI, Data Science, TI] [impacto: Engenheiro de Dados, PM]
3. Quais são todas as fontes de dados relevantes (bancos, APIs, arquivos, SaaS) e quem é o dono de cada uma? [fonte: TI, Operações, fornecedores SaaS] [impacto: Engenheiro de Dados, DevOps]
4. O acesso a todas as fontes de dados já está disponível (credenciais, VPN, firewall rules, APIs habilitadas)? [fonte: TI, Segurança, fornecedores SaaS] [impacto: Engenheiro de Dados, DevOps]
5. Qual é o volume aproximado de dados por fonte (registros/dia, GB/dia) e a taxa de crescimento esperada? [fonte: TI, BI, Operações] [impacto: Engenheiro de Dados, Arquiteto]
6. Qual é a latência aceitável entre o dado ser gerado na fonte e estar disponível no destino (real-time, minutos, horas, diário)? [fonte: BI, Operações, Diretoria] [impacto: Engenheiro de Dados, Arquiteto]
7. Qual é o orçamento total disponível, separando custo de desenvolvimento e custo de operação mensal (infra, ferramentas SaaS)? [fonte: Financeiro, Diretoria] [impacto: PM, Engenheiro de Dados, Arquiteto]
8. Os dados incluem informações pessoais (PII), financeiras ou de saúde sujeitas a LGPD, GDPR ou regulação setorial? [fonte: Jurídico, DPO, Compliance] [impacto: Engenheiro de Dados, Segurança, Arquiteto]
9. Existe pipeline de dados atual que será substituído ou complementado? Qual tecnologia usa? [fonte: TI, BI] [impacto: Engenheiro de Dados, PM]
10. O destino dos dados já existe (data warehouse, lake, banco analítico) ou precisará ser provisionado? [fonte: TI, BI] [impacto: Engenheiro de Dados, DevOps]
11. Qual é o prazo esperado para o go-live e existe dependência de negócio vinculada (migração, auditoria, novo produto)? [fonte: Diretoria, BI] [impacto: PM, Engenheiro de Dados]
12. O time interno tem experiência com engenharia de dados ou será o primeiro projeto desta natureza? [fonte: TI, RH] [impacto: PM, Engenheiro de Dados]
13. Existe expectativa de que o pipeline alimente modelos de ML ou apenas BI/reporting? [fonte: Data Science, BI, Diretoria] [impacto: Engenheiro de Dados, Arquiteto]
14. Há preferência ou restrição de cloud provider (AWS, GCP, Azure) ou ferramentas específicas? [fonte: TI, Diretoria] [impacto: Engenheiro de Dados, Arquiteto]
15. Qual é o SLA de disponibilidade esperado para o pipeline (pode ficar fora por horas, minutos, ou deve ser 24/7)? [fonte: Operações, BI, Diretoria] [impacto: Engenheiro de Dados, DevOps]

---

## Etapa 02 — Discovery

- **Profiling de fontes de dados**: Para cada fonte identificada na Inception, realizar profiling detalhado: schema (tabelas, colunas, tipos de dados), volume (registros totais, registros novos por dia, tamanho em GB), qualidade (nulos, duplicados, outliers, encoding incorreto), mecanismo de extração (full load, incremental por timestamp, CDC, API paginada), e limitações (rate limits de API, janela de manutenção do banco, restrições de acesso por horário). O profiling revela a real complexidade de cada fonte — um banco com "50 tabelas" pode ter 10 tabelas relevantes com dados limpos ou 50 tabelas com schemas inconsistentes e dados sujos.

- **Modelo de dados do destino**: Definir a estrutura do destino antes de construir o pipeline. Se o destino é um data warehouse moderno, definir o modelo dimensional (fatos, dimensões, granularidade) ou o modelo ELT em camadas (bronze/raw → silver/cleaned → gold/curated). Para cada camada, definir: quais tabelas existem, quais colunas, tipos de dados, grain (granularidade de cada fato), relações entre tabelas, e políticas de particionamento (por data é o mais comum — BigQuery e Snowflake cobram por dados escaneados, particionar reduz custo drasticamente).

- **Regras de transformação e qualidade**: Documentar todas as regras de negócio que transformam dados brutos em dados úteis. Exemplos: "pedidos com status 'cancelado' não devem aparecer no faturamento", "CPF deve ser validado com dígito verificador", "valores em USD devem ser convertidos pela cotação do dia do pedido", "clientes duplicados devem ser deduplicados pelo e-mail normalizado". Cada regra é uma unidade testável — e deve ter teste automatizado correspondente. Regras não documentadas são regras que existem na cabeça de alguém e que se perdem quando essa pessoa sai.

- **Requisitos de qualidade de dados**: Definir os controles de qualidade que o pipeline deve aplicar: testes de schema (colunas esperadas existem e têm o tipo correto), testes de freshness (dados não são mais antigos que o SLA), testes de volume (número de registros dentro do range esperado — se normalmente chega 10.000 registros e hoje chegou 100, algo está errado), testes de unicidade (chave primária realmente única), testes de not-null (colunas obrigatórias preenchidas), e testes de referência (foreign keys apontam para registros existentes). dbt tests resolve a maioria desses controles para pipelines ELT.

- **Mapa de dependências entre fontes**: Identificar dependências entre fontes de dados: "vendas" depende de "produtos" e "clientes" — se a carga de clientes falhar, a tabela de vendas terá foreign keys órfãs. "Faturamento" depende de "vendas" e "câmbio" — se câmbio não for carregado primeiro, valores em USD não são convertidos. O mapa de dependências define a ordem de execução do pipeline (DAG — Directed Acyclic Graph) e os pontos de falha que podem cascatear. Pipeline sem grafo de dependências explícito é pipeline com falhas silenciosas.

- **Requisitos de observabilidade e SLA**: Definir como o pipeline será monitorado: alertas de falha (qual etapa falhou, erro exato, dados impactados), alertas de atraso (pipeline deveria ter terminado às 6h mas ainda está rodando às 8h), dashboards de saúde (histórico de execuções, tempo de execução, volume processado), e SLA formal (dados disponíveis até 7h, taxa de erro <1%, reprocessamento em até 2h após falha). Sem observabilidade, falhas são descobertas quando o analista reclama que o dashboard está desatualizado — horas ou dias depois.

### Perguntas

1. O profiling de cada fonte de dados foi realizado (schema, volume, qualidade, mecanismo de extração, limitações)? [fonte: TI, DBA, fornecedores SaaS] [impacto: Engenheiro de Dados]
2. O modelo de dados do destino foi definido (dimensional, ELT em camadas, grain, particionamento)? [fonte: BI, Dados, Arquiteto] [impacto: Engenheiro de Dados, BI]
3. Todas as regras de transformação de negócio foram documentadas com exemplos e aprovadas pelo dono dos dados? [fonte: BI, Operações, Financeiro] [impacto: Engenheiro de Dados]
4. Os controles de qualidade de dados foram especificados por tabela/coluna (schema, freshness, volume, unicidade, null)? [fonte: BI, Dados] [impacto: Engenheiro de Dados]
5. O mapa de dependências entre fontes e entre tabelas no destino foi produzido (DAG de execução)? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
6. O mecanismo de extração por fonte foi definido (full load, incremental, CDC, API) com justificativa? [fonte: TI, DBA] [impacto: Engenheiro de Dados]
7. As janelas de extração foram alinhadas com os donos das fontes (horário permitido, impacto no sistema de origem)? [fonte: TI, DBA, Operações] [impacto: Engenheiro de Dados, DevOps]
8. O volume de dados históricos a migrar (backfill) foi quantificado e o esforço estimado? [fonte: TI, BI] [impacto: Engenheiro de Dados, PM]
9. Os requisitos de retenção de dados foram definidos (quanto tempo cada camada mantém dados, política de purge)? [fonte: Jurídico, Compliance, BI] [impacto: Engenheiro de Dados, Segurança]
10. O SLA de freshness foi acordado com os consumidores reais dos dados (não com o patrocinador)? [fonte: BI, Data Science, Operações] [impacto: Engenheiro de Dados, PM]
11. Os requisitos de data masking e anonimização foram identificados para dados sensíveis (PII, financeiro)? [fonte: Jurídico, DPO, Segurança] [impacto: Engenheiro de Dados, Segurança]
12. Existe necessidade de dados históricos versionados (SCD Type 2) para rastrear mudanças ao longo do tempo? [fonte: BI, Financeiro, Compliance] [impacto: Engenheiro de Dados]
13. Os formatos de dados nas fontes foram inventariados (encoding, delimitadores, timezone, formato de data, moeda)? [fonte: TI, DBA] [impacto: Engenheiro de Dados]
14. Se streaming (V3), os tópicos/eventos foram mapeados com schema, volume por segundo e requisito de ordering? [fonte: TI, Arquiteto] [impacto: Engenheiro de Dados, Arquiteto]
15. Existe orçamento e responsável definidos para limpeza de dados legados antes da ingestão? [fonte: BI, Financeiro, Dados] [impacto: PM, Engenheiro de Dados]

---

## Etapa 03 — Alignment

- **Ownership dos dados e governança**: Definir formalmente quem é o dono de cada fonte de dados (quem autoriza extração, quem garante qualidade na origem) e quem é o dono de cada tabela no destino (quem define regras de transformação, quem aprova mudanças de schema). Em organizações maiores, a governança de dados envolve múltiplas áreas (TI, compliance, BI, operações) com interesses divergentes. Sem ownership claro, mudanças no schema da fonte quebram o pipeline e ninguém avisa; regras de negócio mudam e o pipeline continua aplicando a regra antiga; e dados incorretos ficam semanas no dashboard sem que ninguém assuma a correção.

- **SLA entre produtor e consumidor de dados**: Formalizar o contrato de dados entre quem produz (o pipeline) e quem consome (BI, data science, outros sistemas). O contrato deve especificar: freshness (dados disponíveis até que horas), completude (100% dos registros do período), qualidade mínima (taxa de nulos aceitável, taxa de duplicação máxima), schema estável (mudanças de schema comunicadas com X dias de antecedência), e procedimento em caso de falha (quem é notificado, qual o SLA de reprocessamento). Sem contrato, o pipeline opera em best-effort e o consumidor não tem como planejar.

- **Custo operacional e modelo de billing**: Alinhar o custo mensal esperado do pipeline em operação. Ferramentas de dados têm modelos de billing complexos: BigQuery cobra por TB escaneado (uma query mal escrita pode custar centenas de dólares), Snowflake cobra por credit por segundo de compute (warehouse esquecido ligado gera conta contínua), Fivetran cobra por MAR (Monthly Active Rows — um source com 1M registros atualizados por mês tem custo diferente de 100K), Kafka managed cobra por throughput e retenção. Projetar o custo em cenário normal e em pior caso (backfill completo, reprocessamento, pico de volume).

- **Estratégia de ambientes e dados de teste**: Alinhar como os ambientes de desenvolvimento e staging vão funcionar. Pipeline de dados em staging precisa de dados para processar — mas usar dados reais de produção em staging pode violar LGPD (dados pessoais em ambiente sem controle de acesso adequado). Opções: dados sintéticos (gerados com Faker ou similar), dados anonimizados (copiados de produção com PII mascarada), ou subset de dados reais com acesso controlado. A decisão afeta a confiabilidade dos testes e a conformidade com regulação.

- **Modelo de operação e on-call**: Definir quem opera o pipeline no dia a dia e quem responde quando falha fora do horário. Pipelines batch que rodam de madrugada falham de madrugada — se ninguém está de plantão, os dados não estão prontos quando os analistas chegam às 8h. Definir: quem monitora, quem é notificado em caso de falha, qual o SLA de resposta (15 minutos, 1 hora, próximo dia útil), e se existe automação de recuperação (retry automático, re-run manual com um clique). Pipeline sem modelo de operação definido é pipeline que funciona por sorte.

### Perguntas

1. O ownership de cada fonte de dados e de cada tabela no destino foi definido formalmente? [fonte: TI, BI, Dados, Diretoria] [impacto: Engenheiro de Dados, PM]
2. O contrato de dados (SLA de freshness, completude, qualidade) foi formalizado com os consumidores? [fonte: BI, Data Science, Operações] [impacto: Engenheiro de Dados, PM]
3. O custo operacional mensal foi projetado em cenário normal e pior caso e aprovado pelo financeiro? [fonte: Financeiro, TI, Diretoria] [impacto: PM, Engenheiro de Dados]
4. A estratégia de dados em staging foi definida (sintéticos, anonimizados, subset real) com aprovação de compliance? [fonte: Segurança, Jurídico, DPO] [impacto: Engenheiro de Dados, Segurança]
5. O modelo de operação e on-call foi definido (quem monitora, quem responde, SLA de reação)? [fonte: TI, Operações, Diretoria] [impacto: Engenheiro de Dados, DevOps]
6. Os donos das fontes de dados concordam com a janela e o método de extração (impacto nos sistemas de origem)? [fonte: TI, DBA, Operações] [impacto: Engenheiro de Dados, DevOps]
7. A política de mudança de schema (tanto na fonte quanto no destino) foi acordada com processo de comunicação? [fonte: TI, BI, Dados] [impacto: Engenheiro de Dados]
8. Os acessos necessários (credenciais, VPN, service accounts) foram solicitados e estão em processo de aprovação? [fonte: Segurança, TI] [impacto: Engenheiro de Dados, DevOps]
9. O processo de resolução de problemas de qualidade de dados na origem foi definido (quem reporta, quem corrige)? [fonte: TI, Operações, BI] [impacto: Engenheiro de Dados, PM]
10. As dependências externas (aprovação de acessos, provisionamento de infra, licenças de ferramentas) foram listadas com prazos? [fonte: TI, Financeiro, Compras] [impacto: PM]
11. O time de desenvolvimento tem acesso a todas as ferramentas e ambientes necessários? [fonte: TI, Segurança] [impacto: Engenheiro de Dados, DevOps]
12. A estratégia de backup e disaster recovery do pipeline e dos dados foi alinhada? [fonte: TI, Segurança, Diretoria] [impacto: DevOps, Engenheiro de Dados]
13. O impacto nos sistemas de origem durante a extração foi avaliado e aceito pelos donos dos sistemas? [fonte: TI, DBA, Operações] [impacto: Engenheiro de Dados]
14. O processo de revisão e aprovação de entregas parciais durante o build foi definido? [fonte: BI, Diretoria, PM] [impacto: PM, Engenheiro de Dados]
15. O cliente entende que pipelines de dados exigem manutenção contínua (schemas mudam, fontes mudam, regras mudam)? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **DAG de execução completo**: Produzir o grafo acíclico dirigido (DAG) que representa a ordem de execução de todas as tarefas do pipeline: qual extração roda primeiro, quais podem rodar em paralelo, quais transformações dependem de quais extrações, e qual é o caminho crítico (a sequência mais longa que define o tempo total de execução). O DAG é o artefato que permite estimar o tempo de execução do pipeline, identificar gargalos, e planejar paralelismo. Pipeline sem DAG explícito é pipeline com ordem de execução acidental — funciona até que uma dependência não atendida cause falha silenciosa.

- **Especificação de cada tarefa (job)**: Para cada nó do DAG, documentar: nome, fonte de dados, destino, tipo de operação (extração, transformação, carga), lógica de negócio em pseudo-código ou SQL, critérios de qualidade (testes), comportamento em caso de falha (retry, skip, abort pipeline), e tempo estimado de execução. Esta especificação é o contrato entre quem definiu a regra de negócio e quem vai implementar — sem ela, o engenheiro de dados interpreta as regras e os resultados divergem da expectativa.

- **Modelo de dados detalhado por camada**: Para cada camada do modelo (raw, cleaned, curated), documentar: todas as tabelas com schema completo (nome da coluna, tipo, nullable, default, descrição), relações entre tabelas (foreign keys, mesmo que lógicas), política de particionamento (partition key, granularidade), política de clustering (colunas de clustering para otimizar queries comuns), e exemplos de queries que os consumidores vão executar. O modelo detalhado permite validar que o schema suporta os use cases dos consumidores antes de construir o pipeline.

- **Estratégia de backfill e reprocessamento**: Definir como dados históricos serão carregados (backfill) e como dados errôneos serão corrigidos (reprocessamento). Backfill pode ser simples (carregar tudo de uma vez) ou incremental (carregar mês a mês para não sobrecarregar a fonte). Reprocessamento exige idempotência — rodar o mesmo período duas vezes deve produzir o mesmo resultado, sem duplicação. Definir: qual período máximo de backfill é suportado, quanto tempo leva, e se pode rodar em paralelo com o pipeline normal ou precisa de janela exclusiva.

- **Política de data lineage e catalogação**: Definir como será rastreada a origem de cada dado (de qual fonte veio, quais transformações sofreu, quando foi carregado). Data lineage é requisito de compliance para empresas reguladas e é fundamental para debugging quando dados parecem incorretos ("por que o faturamento de março está 10% menor que o esperado?"). Ferramentas como dbt geram lineage automaticamente para transformações SQL. Para fontes externas, documentar manualmente a cadeia completa: sistema de origem → extração → raw → transformação → curated.

- **Definição de alertas e thresholds**: Especificar os alertas que o pipeline deve disparar: falha de execução (qualquer task falhou após retries), atraso (pipeline não completou dentro do SLA), anomalia de volume (registros processados fora do range esperado — ex.: <1.000 ou >100.000 quando a média é 10.000), anomalia de qualidade (taxa de nulos acima do threshold, taxa de duplicação acima do aceitável), e custo (query ou job que ultrapassou limite de custo). Cada alerta deve ter: destino (e-mail, Slack, PagerDuty), severidade (info, warning, critical), e procedimento de resposta.

### Perguntas

1. O DAG de execução completo foi produzido com todas as dependências entre tarefas e o caminho crítico identificado? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
2. Cada tarefa do pipeline foi especificada com fonte, destino, lógica, critérios de qualidade e comportamento em falha? [fonte: BI, Engenheiro de Dados] [impacto: Engenheiro de Dados]
3. O modelo de dados de cada camada foi documentado com schema completo, particionamento e exemplos de queries? [fonte: BI, Engenheiro de Dados, Data Science] [impacto: Engenheiro de Dados]
4. A estratégia de backfill foi definida (volume, prazo, método, impacto na fonte, paralelismo com pipeline normal)? [fonte: TI, BI, Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
5. A política de reprocessamento foi definida com garantia de idempotência? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
6. A estratégia de data lineage e catalogação foi definida (ferramenta, nível de detalhe, automação)? [fonte: Dados, Compliance, BI] [impacto: Engenheiro de Dados]
7. Os alertas e thresholds foram especificados por tipo (falha, atraso, volume, qualidade, custo) com destino e procedimento? [fonte: Engenheiro de Dados, Operações] [impacto: Engenheiro de Dados, DevOps]
8. As regras de transformação foram validadas com dados reais de amostra para confirmar que produzem o resultado esperado? [fonte: BI, Financeiro, Operações] [impacto: Engenheiro de Dados]
9. A granularidade de cada tabela de fato foi definida e validada contra os use cases dos consumidores? [fonte: BI, Data Science] [impacto: Engenheiro de Dados]
10. Se SCD Type 2 foi definido, as tabelas afetadas, as colunas rastreadas e o mecanismo de versionamento foram especificados? [fonte: BI, Engenheiro de Dados] [impacto: Engenheiro de Dados]
11. A política de acesso por camada foi definida (quem acessa raw, quem acessa curated, por role ou por usuário)? [fonte: Segurança, BI, Dados] [impacto: Engenheiro de Dados, Segurança]
12. Os testes de qualidade de dados foram especificados por tabela (not_null, unique, accepted_values, relationships, custom)? [fonte: BI, Engenheiro de Dados] [impacto: Engenheiro de Dados]
13. O tempo estimado de execução do pipeline end-to-end foi calculado e está dentro do SLA de freshness? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, PM]
14. Se streaming (V3), o schema dos eventos foi definido com schema registry e estratégia de evolução de schema? [fonte: Arquiteto, Engenheiro de Dados] [impacto: Engenheiro de Dados]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes do Setup? [fonte: BI, Diretoria, Dados] [impacto: PM, Engenheiro de Dados]

---

## Etapa 05 — Architecture

- **Escolha do orquestrador**: O orquestrador é o "maestro" que agenda, executa e monitora as tarefas do pipeline. Apache Airflow é o padrão de mercado para pipelines batch — maduro, extensível, com comunidade enorme, mas complexo de operar (scheduler, webserver, workers, metastore DB). Prefect e Dagster são alternativas modernas com melhor developer experience e observabilidade nativa — Dagster especialmente bom para pipelines com dbt. Para streaming, o orquestrador é geralmente o próprio framework (Kafka Streams, Flink) com gestão de offsets e checkpoints. Cloud-managed options (Cloud Composer para Airflow, Astronomer) removem a complexidade operacional em troca de custo.

- **Escolha do warehouse/lake**: A decisão entre BigQuery, Snowflake, Redshift, Databricks ou solução open-source (Trino + Iceberg + S3) define o ecossistema, o modelo de custo e as capabilities disponíveis. BigQuery é serverless (zero infra para gerenciar), cobra por query e armazenamento, e escala automaticamente — ideal para quem quer simplicidade. Snowflake separa compute de storage (múltiplos warehouses acessam os mesmos dados), tem melhor controle de custo granular, e suporta multi-cloud. Databricks é ideal quando há forte componente de ML (notebooks, MLflow integrado, Delta Lake). A escolha deve considerar: perfil do time (SQL-first vs. Python-first), volume de dados, padrão de queries (ad-hoc vs. scheduled), e orçamento.

- **Pipeline de ingestão**: Definir como os dados chegam da fonte ao destino raw. Ferramentas managed como Fivetran e Airbyte oferecem conectores prontos para centenas de fontes SaaS e bancos de dados — zero código para fontes suportadas, mas custo por MAR e menor flexibilidade. Custom scripts (Python + SQLAlchemy, Singer taps) oferecem controle total mas exigem manutenção contínua. CDC via Debezium captura mudanças em tempo real diretamente do log do banco (WAL do PostgreSQL, binlog do MySQL) — a forma mais eficiente de ingestão incremental para bancos relacionais, mas requer acesso ao log de replicação.

- **Framework de transformação**: Para pipelines ELT, dbt (data build tool) é o padrão para transformação via SQL no warehouse — traz versionamento, testes, documentação e lineage como cidadãos de primeira classe. Para transformações que exigem Python (ML features, processamento de texto, chamadas a APIs), Spark ou pandas rodam como tasks no orquestrador. A decisão SQL vs. Python deve ser por capacidade: se a transformação é expressável em SQL, dbt é mais simples, mais testável e mais documentável; se precisa de lógica imperativa ou bibliotecas externas, Python.

- **Estratégia de particionamento e custo**: Em warehouses que cobram por dados escaneados (BigQuery) ou por compute (Snowflake), a estratégia de particionamento é diretamente proporcional ao custo operacional. Particionar por data (dia, mês) é o padrão para tabelas de fato com filtro temporal frequente — uma query que filtra "último mês" escaneia 1/12 dos dados ao invés de todos. Clustering (BigQuery) ou sort key (Redshift) por colunas de filtro frequente complementa o particionamento. Queries sem filtro de partição devem ser bloqueadas ou alertadas — uma SELECT * em tabela de 10TB custa USD 50 no BigQuery.

- **Segurança e controle de acesso**: Definir o modelo de acesso por camada: raw (apenas engenheiros de dados e pipeline service account), cleaned (engenheiros de dados e analistas seniores), curated (todos os analistas e dashboards). Implementar via RBAC (roles no warehouse com grants por schema/tabela) ou via data masking (colunas com PII visíveis apenas para roles autorizados). Para ambientes multi-tenant, garantir que dados de um cliente não sejam visíveis para outro (row-level security). Para dados sensíveis, implementar criptografia column-level ou tokenização.

### Perguntas

1. O orquestrador foi escolhido com justificativa documentada considerando perfil do time, complexidade e custo operacional? [fonte: TI, Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
2. O warehouse/lake foi escolhido considerando modelo de custo, perfil do time, volume de dados e use cases? [fonte: TI, BI, Financeiro] [impacto: Engenheiro de Dados, Arquiteto]
3. A ferramenta de ingestão foi definida por fonte (managed vs. custom) com custo projetado por MAR/volume? [fonte: TI, Financeiro] [impacto: Engenheiro de Dados]
4. O framework de transformação foi definido (dbt, Spark, pandas) com critério claro de quando usar SQL vs. Python? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
5. A estratégia de particionamento e clustering foi definida por tabela com estimativa de impacto no custo? [fonte: Engenheiro de Dados, Arquiteto] [impacto: Engenheiro de Dados]
6. O modelo de segurança e controle de acesso foi desenhado por camada com RBAC e masking para PII? [fonte: Segurança, Dados, Jurídico] [impacto: Engenheiro de Dados, Segurança]
7. Se streaming (V3), o message broker (Kafka, Kinesis, Pub/Sub) e o processador (Flink, Spark Streaming) foram escolhidos? [fonte: Arquiteto, TI] [impacto: Engenheiro de Dados, DevOps]
8. O custo mensal de operação foi calculado por cenário (normal, backfill, pior caso) e está dentro do orçamento? [fonte: Financeiro, TI] [impacto: PM, Engenheiro de Dados]
9. A estratégia de ambientes (dev, staging, produção) foi definida com isolamento de dados e credenciais? [fonte: TI, Segurança] [impacto: Engenheiro de Dados, DevOps]
10. A solução de observabilidade foi escolhida (logs, métricas, alertas, lineage) com integração ao orquestrador? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
11. A estratégia de schema evolution (mudanças de schema na fonte) foi definida com detecção e tratamento automático? [fonte: Engenheiro de Dados, Arquiteto] [impacto: Engenheiro de Dados]
12. O pipeline suporta crescimento de volume (2x, 5x, 10x) sem refatoração estrutural? [fonte: Arquiteto] [impacto: Engenheiro de Dados]
13. A estratégia de disaster recovery e backup do pipeline e dos dados foi definida (RPO, RTO)? [fonte: TI, Segurança] [impacto: DevOps, Engenheiro de Dados]
14. A arquitetura foi documentada com diagrama de componentes e fluxo de dados end-to-end? [fonte: Arquiteto, Engenheiro de Dados] [impacto: Engenheiro de Dados, PM]
15. A arquitetura foi revisada por segurança e compliance antes de avançar para o Setup? [fonte: Segurança, Compliance, Arquiteto] [impacto: Engenheiro de Dados, Segurança]

---

## Etapa 06 — Setup

- **Provisionamento de infraestrutura**: Criar todos os recursos de infraestrutura via IaC (Terraform, Pulumi, CloudFormation): warehouse/lake com configurações de produção e staging, buckets S3/GCS para dados raw e intermediários, instância do orquestrador (Airflow/Dagster), clusters Kafka (se streaming), bancos de metadados, e service accounts com permissões mínimas. IaC garante reprodutibilidade (staging idêntico à produção), versionamento (mudanças de infra rastreáveis no git), e disaster recovery (recriar toda a infra a partir do código). Infraestrutura criada manualmente via console é anti-pattern que se torna dívida técnica permanente.

- **Configuração do orquestrador**: Instalar e configurar o orquestrador com: conexões para todas as fontes e destinos (connection strings, API keys, service accounts), pools de workers com limites de concorrência (evitar saturar APIs externas ou bancos de origem), variáveis de configuração por ambiente (staging vs. produção), integração com sistema de alertas (Slack, PagerDuty, e-mail), e política de retry por tipo de falha (erro de rede → retry em 5 minutos; erro de lógica → não retry, alertar). Configurar o scheduler para executar na cadência definida (diário, horário, a cada 5 minutos).

- **Setup do framework de transformação**: Se dbt, inicializar o projeto com estrutura de pastas (staging, intermediate, marts), configurar profiles.yml com credenciais do warehouse, criar os primeiros modelos com sources e testes básicos, e configurar o pipeline de CI/CD para rodar dbt test e dbt build automaticamente a cada PR. Se Spark, configurar o cluster com libs necessárias, configurar acesso a fontes e destinos, e criar o projeto com estrutura de jobs. O primeiro modelo/job deve ser end-to-end (fonte → raw → curated) como proof of concept da stack.

- **Pipeline de CI/CD para dados**: Configurar o pipeline que valida mudanças antes de ir para produção: lint de código (sqlfluff para SQL, ruff/black para Python), testes de dbt (dbt test em staging com dados de teste), testes de integridade do DAG (Airflow: dag_test, Dagster: materialize dry-run), e deploy automatizado em staging com promoção manual para produção. Para dbt, o CI ideal roda dbt build com dataset de CI (clone parcial dos dados de produção) e compara resultados com a versão atual. Pipeline sem CI/CD é pipeline que quebra em produção sem aviso.

- **Configuração de monitoramento e alertas**: Configurar as ferramentas de observabilidade: logs centralizados (CloudWatch, Stackdriver, Datadog) com retenção adequada, métricas de execução do pipeline (tempo por task, registros processados, erros), dashboards de saúde (Grafana, Looker, ou dashboard nativo do orquestrador), e alertas configurados com destino e escalação. Testar cada alerta manualmente (provocar falha, verificar que a notificação chega). Alertas não testados são alertas que não funcionam quando necessário.

- **Dados de teste e validação**: Popular o ambiente de staging com dados representativos para testes. Opções: subset de produção (últimos 30 dias, anonimizado se PII), dados sintéticos gerados com Faker ou dbt-datamocktool, ou seed files (arquivos CSV com dados de referência). Os dados de teste devem cobrir edge cases: registros com nulos, formatos inesperados, datas em timezones diferentes, caracteres especiais. Sem dados de teste realistas, os bugs são descobertos apenas em produção.

### Perguntas

1. Toda a infraestrutura foi provisionada via IaC (Terraform, Pulumi) e o código está versionado no repositório? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, Engenheiro de Dados]
2. Os ambientes de staging e produção estão provisionados com isolamento completo de dados e credenciais? [fonte: DevOps, Segurança] [impacto: Engenheiro de Dados, Segurança]
3. O orquestrador está configurado com conexões, pools, variáveis e integração com alertas? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
4. O framework de transformação (dbt, Spark) está configurado com projeto inicializado e primeiro modelo end-to-end funcionando? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
5. O pipeline de CI/CD inclui lint, testes de dados e deploy automatizado em staging? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
6. As credenciais e service accounts estão configuradas com permissão mínima (principle of least privilege) e secrets seguros? [fonte: Segurança, DevOps] [impacto: Engenheiro de Dados, Segurança]
7. Os alertas foram configurados e testados (falha provocada → notificação recebida)? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps, Engenheiro de Dados]
8. Os dados de teste em staging são representativos e cobrem edge cases (nulos, formatos inesperados, timezone)? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
9. A conectividade com todas as fontes de dados foi testada em staging (credenciais, rede, firewall)? [fonte: Engenheiro de Dados, TI] [impacto: Engenheiro de Dados]
10. O scheduling do orquestrador foi configurado na cadência definida com timezone correto? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
11. O warehouse está configurado com particionamento, clustering e políticas de acesso por camada? [fonte: Engenheiro de Dados, Segurança] [impacto: Engenheiro de Dados]
12. O processo de onboarding de novos engenheiros foi documentado (setup local, acesso a ferramentas, padrões de código)? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
13. Se streaming, o message broker está provisionado com tópicos, partições e retenção configurados? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
14. O ambiente de desenvolvimento local está funcional para cada engenheiro do time? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
15. O pipeline de CI/CD foi testado com uma mudança real — testes passaram, staging atualizado, dados gerados corretamente? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]

---

## Etapa 07 — Build

- **Implementação de ingestão por fonte**: Implementar a extração de cada fonte conforme definido na Etapa 04. Para cada fonte: configurar o conector (Fivetran, Airbyte, custom script), definir o modo de extração (full load para a primeira execução, incremental para as subsequentes), implementar tratamento de erros específicos da fonte (timeout de API, rate limiting, conexão perdida), e validar que os dados raw no destino correspondem aos dados na fonte (contagem de registros, checksum de valores-chave). Fontes com APIs instáveis ou mal documentadas são as que consomem mais tempo — priorizar o mapeamento e testes dessas fontes primeiro.

- **Implementação de transformações**: Implementar as regras de negócio como modelos dbt (SQL) ou jobs Python conforme a especificação da Etapa 04. Cada transformação deve: ter teste associado (not_null, unique, accepted_values, custom), ter documentação inline (descrição da regra de negócio no código ou no schema.yml do dbt), ser idempotente (reprocessar produz o mesmo resultado), e gerar output rastreável (data lineage via dbt ou logging explícito). Implementar na ordem do DAG — tabelas de dimensão antes de tabelas de fato, camada raw → cleaned → curated em sequência.

- **Implementação de data quality checks**: Configurar os testes de qualidade de dados que rodam automaticamente após cada execução do pipeline. Testes estruturais: schema validation (colunas esperadas existem com tipo correto), not_null em colunas obrigatórias, unique em chaves primárias, referential integrity entre tabelas. Testes de negócio: valores dentro de ranges aceitáveis (preço >0, data no passado para pedidos históricos), totalizações que batem (soma de line items = total do pedido), freshness (dados não mais antigos que o SLA). Para dbt, usar dbt tests nativos + packages como dbt-expectations para testes estatísticos.

- **Backfill de dados históricos**: Executar a carga inicial de dados históricos conforme a estratégia definida na Etapa 04. O backfill é frequentemente o processo mais longo do build — carregar 3 anos de dados pode levar dias. Planejar: execução em lotes (por mês ou por trimestre para não sobrecarregar a fonte), monitoramento de progresso (% concluído, registros processados, erros acumulados), e validação pós-backfill (contagem total confere com a fonte, valores agregados batem). Se o backfill falhar no meio, o pipeline deve ser capaz de retomar de onde parou sem reprocessar tudo.

- **Documentação e catalogação**: Documentar o pipeline de forma que outros engenheiros e analistas possam entender sem consultar o autor. Para dbt, usar schema.yml para documentar cada modelo e coluna, gerar o site de documentação com dbt docs generate, e disponibilizar o lineage graph. Para Airflow, documentar cada DAG com description e doc_md. No data catalog (se houver), registrar cada tabela com descrição, owner, SLA, e regras de acesso. Pipeline sem documentação é pipeline que só o autor consegue manter — e quando o autor sai, o pipeline vira caixa preta.

- **Implementação de observabilidade**: Instrumentar o pipeline com logs estruturados em cada etapa: registros processados, registros rejeitados, tempo de execução, erros com stack trace. Configurar métricas customizadas no orquestrador: duração por task (tendência de degradação indica problema futuro), volume processado por execução (anomalias indicam problema na fonte), e taxa de erro (>0 em pipeline batch é investigável). Integrar com sistema de alertas para que falhas, atrasos e anomalias sejam notificados automaticamente.

### Perguntas

1. A ingestão de cada fonte foi implementada com modo correto (full/incremental/CDC) e validada contra a fonte? [fonte: Engenheiro de Dados, TI] [impacto: Engenheiro de Dados]
2. As transformações foram implementadas com testes associados e documentação inline das regras de negócio? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
3. Os data quality checks rodam automaticamente após cada execução e bloqueiam a camada seguinte em caso de falha? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
4. O backfill de dados históricos foi concluído e validado com contagens e valores agregados conferindo com a fonte? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados, PM]
5. A documentação do pipeline (dbt docs, DAG docs, data catalog) está atualizada e acessível ao time? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, BI]
6. A observabilidade está implementada com logs estruturados, métricas e integração com alertas? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
7. Cada transformação é idempotente (reprocessar o mesmo período produz o mesmo resultado sem duplicação)? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
8. As fontes com APIs instáveis foram testadas com cenários de falha (timeout, rate limit, resposta incompleta)? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
9. O DAG completo foi executado end-to-end em staging com dados representativos? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
10. Os consumidores (analistas, data scientists) validaram que os dados curated atendem seus use cases? [fonte: BI, Data Science] [impacto: Engenheiro de Dados, BI]
11. O data masking e anonimização de PII foram implementados conforme a política definida? [fonte: Segurança, Engenheiro de Dados] [impacto: Engenheiro de Dados, Segurança]
12. As queries mais frequentes dos consumidores foram testadas com tempo de resposta aceitável? [fonte: BI, Engenheiro de Dados] [impacto: Engenheiro de Dados]
13. O retry e circuit breaker para fontes externas estão implementados e testados? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
14. Se streaming, o processamento de eventos está funcionando com latência dentro do SLA sob carga normal? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados]
15. O pipeline end-to-end roda dentro do tempo estimado e cumpre o SLA de freshness em staging? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, PM]

---

## Etapa 08 — QA

- **Validação de dados end-to-end**: Comparar os dados no destino curated com os dados na fonte para cada entidade principal. Para tabelas de fato: contagem total de registros confere, soma de métricas numéricas confere (faturamento, quantidade, valor), distribuição por dimensão confere (top 10 clientes por faturamento é o mesmo nas duas pontas). Para tabelas de dimensão: contagem de registros únicos confere, campos descritivos estão corretos (nome do produto, categoria), campos calculados estão consistentes. Discrepâncias revelam bugs de transformação, filtros incorretos ou problemas de deduplicação.

- **Teste de falha e recuperação**: Provocar cenários de falha controlados e validar o comportamento do pipeline. Cenários: fonte indisponível (API offline, banco fora) → pipeline deve gerar alerta e parar sem corromper dados parciais. Dados inválidos na fonte (campo obrigatório nulo, formato incorreto) → pipeline deve rejeitar registros inválidos, registrar em tabela de erros e continuar com os válidos. Falha no meio da execução (task de transformação falha) → rerun deve retomar do ponto de falha sem reprocessar tudo. Cada cenário deve ter resultado esperado documentado e testado.

- **Teste de performance e custo**: Executar o pipeline com volume realista (não subset) em staging e medir: tempo total de execução (está dentro do SLA?), custo de queries e compute no warehouse (BigQuery: bytes scanned por query; Snowflake: credits consumidos), custo de ingestão (Fivetran: MAR atingido?), e custo de armazenamento (TB armazenados por camada). Projetar o custo para 12 meses considerando crescimento de volume. Se o custo projetado excede o orçamento, otimizar antes do go-live (particionar melhor, reduzir retenção de raw, otimizar queries caras).

- **Validação de segurança e acesso**: Verificar que o modelo de acesso funciona como especificado: usuário com role "analista" acessa apenas camada curated (não raw), colunas com PII estão mascaradas para roles não autorizados, service accounts do pipeline têm apenas as permissões necessárias (não admin), e logs de acesso estão sendo capturados (quem acessou quais dados, quando). Para compliance, executar uma auditoria simulada: dado um registro de cliente, rastrear quem acessou seus dados, qual transformação foi aplicada, e onde está armazenado.

- **Teste de reprocessamento e idempotência**: Executar o pipeline para o mesmo período duas vezes consecutivas e verificar que o resultado é idêntico — sem duplicação de registros, sem mudança em valores calculados, sem efeitos colaterais. Para pipelines com MERGE/UPSERT, verificar que registros atualizados sobrescrevem corretamente e novos registros são inseridos. Para pipelines com APPEND, verificar que a partição é limpa antes da recarga (TRUNCATE+INSERT ou DELETE+INSERT com filtro de período). Idempotência é o teste mais crítico — sem ela, qualquer reprocessamento corrompe dados.

- **Validação com consumidores**: Disponibilizar os dados para os consumidores finais (analistas, data scientists, dashboards) em staging e validar que: os dados atendem os use cases definidos, as queries habituais retornam resultados consistentes com o que era esperado, a latência de queries é aceitável, e não há dados faltantes ou inconsistentes que impeçam o uso. O aceite dos consumidores é o gate mais importante do QA — pipeline tecnicamente perfeito que não atende o consumidor é pipeline inútil.

### Perguntas

1. A validação end-to-end (fonte vs. destino) foi realizada para cada entidade principal com contagens e totais conferindo? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
2. Os cenários de falha foram testados (fonte indisponível, dados inválidos, falha no meio) com resultado documentado? [fonte: Engenheiro de Dados, QA] [impacto: Engenheiro de Dados]
3. O teste de performance com volume realista foi executado e o tempo total está dentro do SLA? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
4. O custo de operação foi medido em staging e projetado para 12 meses — está dentro do orçamento? [fonte: Engenheiro de Dados, Financeiro] [impacto: PM, Engenheiro de Dados]
5. A segurança de acesso foi verificada (roles funcionam, PII mascarada, service accounts com permissão mínima)? [fonte: Segurança, Engenheiro de Dados] [impacto: Segurança, Engenheiro de Dados]
6. O teste de idempotência (reprocessamento) foi executado e confirmou ausência de duplicação? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
7. Os consumidores finais validaram os dados em staging e confirmaram que atendem seus use cases? [fonte: BI, Data Science] [impacto: Engenheiro de Dados, BI]
8. Os data quality checks detectaram problemas reais (não apenas passaram em dados perfeitos)? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
9. Os alertas foram testados com triggers reais (provocar falha, verificar notificação, verificar escalação)? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps]
10. O data lineage está completo — é possível rastrear cada dado curated de volta à fonte original? [fonte: Engenheiro de Dados, Compliance] [impacto: Engenheiro de Dados]
11. Se streaming, o teste de latência e throughput sob carga de pico foi executado e está dentro do SLA? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados]
12. O reprocessamento de backfill (re-run de um período específico) foi testado sem impactar o pipeline normal? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
13. Os dashboards de saúde do pipeline exibem métricas corretas e atualizadas? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps, Engenheiro de Dados]
14. A documentação do pipeline (dbt docs, data catalog, runbook) está completa e atualizada para handover? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
15. O time de operações foi treinado nas ferramentas de monitoramento e sabe responder a falhas comuns? [fonte: Engenheiro de Dados, Operações] [impacto: Operações]

---

## Etapa 09 — Launch Prep

- **Promoção de staging para produção**: Executar o processo de promoção da configuração de staging para produção: atualizar variáveis de ambiente (credenciais de produção, endpoints reais), configurar scheduling na cadência final (horário exato de execução, timezone correto), ativar alertas de produção (destinos finais, escalação), e fazer o último deploy de código. A promoção deve ser feita via pipeline de CI/CD (não manual) e deve ser reversível. Verificar que nenhuma credencial de staging foi deixada na configuração de produção e vice-versa.

- **Backfill em produção**: Se o backfill não foi executado diretamente em produção durante o build (cenário mais comum quando staging usa dados distintos), executar o backfill completo em produção antes de ativar o pipeline regular. Monitorar o backfill com atenção: tempo de execução (backfill em warehouse pode gerar custo significativo), impacto na fonte (queries pesadas podem degradar o sistema operacional), e validação de dados pós-backfill (contagens, totais, distribuições). Backfill em produção é a operação mais arriscada do go-live — se falhar ou corromper dados, o rollback é custoso.

- **Runbook de operações**: Produzir o runbook completo que o time de operações vai usar no dia a dia. Para cada tipo de incidente (falha de ingestão, falha de transformação, dados atrasados, qualidade degradada, custo anômalo), documentar: como identificar (alerta, dashboard), como diagnosticar (logs, queries de investigação), como resolver (re-run, fix manual, escalar para engenharia), e como validar a resolução (query de verificação). O runbook é o documento mais importante para operação — sem ele, cada incidente é uma aventura de debugging.

- **Comunicação aos consumidores**: Notificar todos os consumidores de dados sobre o go-live: quais tabelas estarão disponíveis, em qual schema, com qual SLA de freshness, quem contatar em caso de problema, e quais são as limitações conhecidas da primeira versão. Para dashboards que migram de fonte antiga para a nova, comunicar a data de migração com antecedência e oferecer período de convivência (ambas as fontes ativas) para validação.

- **Plano de rollback e contingência**: Documentar o procedimento de rollback para cada cenário: pipeline com bug de transformação (reverter para versão anterior do código, reprocessar período afetado), dados corrompidos no warehouse (restaurar de snapshot/backup, reprocessar), fonte indisponível por tempo prolongado (dados parciais disponíveis com disclaimer, ou revert para fonte anterior). Definir quem decide o rollback, quanto tempo tem para decidir, e como comunicar aos consumidores que os dados estão temporariamente indisponíveis ou parciais.

- **Validação de custos em produção**: Executar uma execução completa do pipeline em produção (sem backfill) e validar o custo real contra a projeção. Verificar especificamente: custo de compute no warehouse (credits Snowflake, on-demand BigQuery), custo de ingestão (MAR Fivetran, horas Airbyte), custo de storage (TB armazenados por camada), e custo de infraestrutura (instâncias, clusters). Se o custo real excede a projeção em mais de 20%, investigar e otimizar antes de declarar go-live.

### Perguntas

1. A promoção de staging para produção foi executada via CI/CD com credenciais de produção corretas? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
2. O backfill em produção foi concluído e validado com contagens e totais conferindo com a fonte? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados, PM]
3. O runbook de operações foi produzido com procedimentos para cada tipo de incidente? [fonte: Engenheiro de Dados] [impacto: Operações, Engenheiro de Dados]
4. Os consumidores foram notificados sobre o go-live com informações de schema, SLA e contato de suporte? [fonte: PM, BI] [impacto: BI, Data Science]
5. O plano de rollback está documentado com cenários, procedimentos e responsáveis? [fonte: Engenheiro de Dados, TI] [impacto: Engenheiro de Dados, DevOps]
6. O custo da primeira execução em produção foi medido e comparado com a projeção — está dentro do esperado? [fonte: Engenheiro de Dados, Financeiro] [impacto: PM, Engenheiro de Dados]
7. O scheduling em produção está configurado na cadência correta com timezone correto? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
8. Os alertas de produção foram testados em produção (não apenas staging)? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps]
9. O treinamento do time de operações foi realizado com o runbook e as ferramentas de monitoramento? [fonte: Engenheiro de Dados, PM] [impacto: Operações]
10. Os dashboards de consumidores foram apontados para os dados do novo pipeline e validados? [fonte: BI, Data Science] [impacto: BI]
11. Se há período de convivência (pipeline novo + antigo), o critério de desligamento do antigo foi definido? [fonte: TI, BI] [impacto: PM, Engenheiro de Dados]
12. A capacidade do time de operações de executar o runbook sem suporte de engenharia foi validada? [fonte: Operações, PM] [impacto: Operações]
13. Os acessos ao warehouse, orquestrador e ferramentas de monitoramento foram distribuídos ao time de operações? [fonte: Engenheiro de Dados, DevOps] [impacto: Operações]
14. A janela de go-live foi escolhida estrategicamente (após execução completa, dia útil, equipe disponível)? [fonte: PM, Engenheiro de Dados] [impacto: PM]
15. Existe war room ou canal de comunicação rápida definido para as primeiras 48h após o go-live? [fonte: PM, TI] [impacto: PM, Engenheiro de Dados]

---

## Etapa 10 — Go-Live

- **Ativação do pipeline em produção**: Ativar o scheduling do pipeline na cadência final. Monitorar a primeira execução completa em tempo real: cada task completou com sucesso, dados foram carregados no destino, testes de qualidade passaram, e freshness SLA foi cumprido. Se qualquer task falha na primeira execução em produção, investigar imediatamente — o contexto está fresco e o time está focado. Falha ignorada na primeira execução tende a se repetir e se tornar "normal" na cultura do time ("ah, essa task sempre falha, é só rerunnar").

- **Validação com dados reais de produção**: Após a primeira execução completa, comparar os dados no destino com a fonte em produção para as entidades mais críticas. Validar que: contagens conferem (registros de vendas de ontem no pipeline = registros de vendas de ontem no ERP), métricas numéricas conferem (faturamento do mês até ontem confere), e não há dados duplicados ou faltantes. Se os consumidores já tinham dados de referência (reports manuais, planilhas, pipeline anterior), comparar resultados para identificar discrepâncias.

- **Monitoramento da primeira semana**: Monitorar ativamente nos primeiros 7 dias: toda execução completou dentro do SLA (se não, investigar o que atrasou), volume de dados processados é consistente dia a dia (variação normal é esperada; queda abrupta indica problema na fonte), custo de operação está dentro do projetado (sem queries escapando sem filtro de partição), e alertas estão funcionando (se não houve nenhum alerta em 7 dias, verificar que os alertas estão realmente ativos — não é normal zero alertas em uma semana de operação nova).

- **Ajustes e otimizações pós-lançamento**: Com base nas primeiras execuções reais, fazer ajustes: tasks que levam mais tempo que o estimado (otimizar query, adicionar particionamento, aumentar paralelismo), data quality checks que são muito restritivos (threshold de volume precisa de ajuste com dados reais), alertas muito ruidosos (threshold de duração precisa de calibração com execução real), e jobs que falham intermitentemente (adicionar retry, investigar causa raiz). Os primeiros 7 dias são o período de calibração — é esperado que ajustes sejam necessários.

- **Handover operacional**: Transferir formalmente a operação do pipeline do time de engenharia de dados para o time de operações/plataforma. Entregar: acesso a todas as ferramentas (orquestrador, warehouse, monitoramento, CI/CD), runbook atualizado com aprendizados da primeira semana, SLA de suporte do time de engenharia (quando escalar, tempo de resposta), e documentação técnica do pipeline (DAG, modelos dbt, integrações). O time de operações deve demonstrar capacidade de lidar com incidentes comuns (re-run, investigação de atraso, verificação de qualidade) sem suporte de engenharia.

- **Relatório de lançamento e aceite**: Produzir relatório formal de lançamento com: métricas da primeira semana (execuções, SLA cumprido, custo real, incidentes), comparação com expectativas (SLA acordado vs. atingido, custo projetado vs. real), lista de ajustes feitos, problemas conhecidos e plano de resolução, e recomendações para próximas iterações (novas fontes, otimizações, expansão de escopo). O relatório serve como aceite formal do entregável e como base para o contrato de manutenção contínua.

### Perguntas

1. A primeira execução completa em produção foi monitorada em tempo real e todas as tasks completaram com sucesso? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados]
2. A validação de dados reais (fonte vs. destino em produção) foi realizada para entidades críticas? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados]
3. O SLA de freshness foi cumprido na primeira execução real? [fonte: Engenheiro de Dados, BI] [impacto: Engenheiro de Dados, PM]
4. O custo da primeira semana de operação está dentro do projetado? [fonte: Engenheiro de Dados, Financeiro] [impacto: PM, Engenheiro de Dados]
5. Os consumidores confirmaram que os dados no novo pipeline estão corretos e usáveis? [fonte: BI, Data Science] [impacto: BI, Engenheiro de Dados]
6. Os alertas dispararam corretamente quando houve incidente (ou foram testados se não houve incidente)? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps]
7. Os ajustes de performance, thresholds e alertas baseados nas primeiras execuções reais foram feitos? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
8. O handover operacional foi formalizado com transferência de acessos, runbook e documentação? [fonte: Engenheiro de Dados, PM] [impacto: Operações, Engenheiro de Dados]
9. O time de operações demonstrou capacidade de lidar com incidentes comuns sem suporte de engenharia? [fonte: Operações, PM] [impacto: Operações]
10. Se há pipeline anterior, o período de convivência foi monitorado e o critério de desligamento do antigo foi validado? [fonte: BI, TI] [impacto: PM, Engenheiro de Dados]
11. O relatório de lançamento foi produzido com métricas, custos, incidentes e recomendações? [fonte: PM, Engenheiro de Dados] [impacto: PM]
12. O aceite formal de entrega foi obtido dos consumidores e do patrocinador? [fonte: BI, Diretoria] [impacto: PM]
13. O SLA de suporte do time de engenharia para os primeiros 30 dias foi definido e comunicado? [fonte: TI, PM] [impacto: Operações, Engenheiro de Dados]
14. O monitoramento de custo contínuo está ativo com alertas para anomalias (query sem filtro, warehouse esquecido)? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, Financeiro]
15. O pipeline antigo (se existia) foi desligado ou está com data de desligamento definida? [fonte: TI, BI] [impacto: PM, Engenheiro de Dados]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos centralizar todos os dados da empresa"** — Escopo infinito. "Todos os dados" inclui dezenas de fontes, centenas de tabelas e anos de histórico. Pipeline de dados viável começa com 3-5 fontes prioritárias que resolvem um use case concreto (ex.: dashboard de vendas). Escopo total vem em fases iterativas, não em um big bang.
- **"Os dados estão todos no Excel do fulano"** — Dados operacionais em planilhas significam ausência de sistema fonte confiável. O pipeline não resolve o problema — ele apenas automatiza a carga de dados ruins. O primeiro passo é estruturar a fonte, não o pipeline.
- **"Precisamos em tempo real"** — 90% dos pedidos de "tempo real" funcionam perfeitamente com batch horário ou diário. Streaming é 5-10x mais complexo e caro que batch. Perguntar: "o que acontece de concreto se o dado chegar 1 hora atrasado?" Se a resposta for "nada de grave", não é tempo real.

### Etapa 02 — Discovery

- **"A API está documentada, é só chamar"** — Documentação de API frequentemente está desatualizada, incompleta ou descreve a versão anterior. Testar a API com dados reais antes de contar com ela no escopo. Rate limits, paginação e autenticação são os campos minados habituais.
- **"Os dados são limpos, não precisa de tratamento"** — Nenhum dado de produção é limpo. Nulos onde não deveria, formatos inconsistentes (data como string em 5 formatos diferentes), duplicados, e encoding incorreto são a norma. O esforço de limpeza geralmente supera o esforço de extração.
- **"Não sabemos exatamente quantos registros são"** — Se o volume não é conhecido, é impossível dimensionar infraestrutura e estimar custo. A diferença entre 10.000 e 10.000.000 de registros é a diferença entre pandas e Spark. Profiling é obrigatório.

### Etapa 03 — Alignment

- **"O DBA vai liberar o acesso quando precisar"** — "Quando precisar" se transforma em semanas de processo burocrático com segurança, compliance e infra. Solicitar acesso na Inception, não no Setup. Pipeline sem acesso à fonte é pipeline que não executa.
- **"O custo de warehouse a gente vê depois"** — BigQuery, Snowflake e Databricks podem gerar faturas de milhares de dólares por mês com uso descuidado. Uma query mal escrita no Snowflake pode consumir centenas de credits. Projetar custo antes de escolher ferramentas é obrigatório.
- **"Não precisamos de ambientes separados, é só dados"** — Pipeline em ambiente único testa com dados de produção (violação de LGPD se há PII) ou, pior, modifica dados de produção durante testes. Staging isolado é obrigatório.

### Etapa 04 — Definition

- **Regras de negócio "na cabeça do analista"** — Transformações não documentadas que o analista "sabe fazer" no Excel mas nunca escreveu. Quando o analista sai da empresa, as regras se perdem. Documentar cada regra com exemplo e teste antes de implementar.
- **DAG "tudo em série"** — Pipeline que executa todas as tasks em sequência sem paralelismo. Fontes independentes podem ser extraídas em paralelo; transformações sem dependência podem rodar simultaneamente. Pipeline sem paralelismo é pipeline 3x mais lento que o necessário.
- **"Não precisa de lineage, a gente sabe de onde vem"** — "A gente sabe" enquanto o time é pequeno e o pipeline é simples. Com 50 tabelas e 10 fontes, ninguém sabe de cor de onde veio cada dado. Lineage é obrigatório para debugging e compliance.

### Etapa 05 — Architecture

- **"Vamos usar Spark para tudo"** — Spark é overhead para volumes que pandas ou polars processam em segundos. Se o pipeline processa <10M registros por execução, Spark adiciona complexidade e custo de cluster sem benefício. Reservar Spark para o que realmente precisa de distribuição.
- **"Vamos usar Airflow porque é o padrão"** — Airflow é poderoso mas operacionalmente complexo (scheduler, webserver, workers, metastore). Para pipelines simples, Prefect ou Dagster são mais leves. Para pipelines serverless, Step Functions ou Cloud Workflows podem ser suficientes. Escolher por adequação, não por hype.
- **"Não precisa de IaC, criamos pelo console"** — Infraestrutura criada manualmente no console da cloud é irreproduzível, não versionada e impossível de auditar. Quando staging precisa ser recriado ou quando há disaster recovery, sem IaC o processo é manual e propenso a erro.

### Etapa 06 — Setup

- **Credenciais de produção no código** — API keys, passwords e tokens commitados no repositório. Violação de segurança que exige rotação de todos os secrets se descoberta. Secrets devem estar em secret manager (Vault, AWS Secrets Manager, GCP Secret Manager), nunca no código.
- **"O ambiente de dev é a máquina do engenheiro"** — Cada engenheiro com setup diferente, versão diferente de Python, dbt e libs. Resultado: "funciona na minha máquina". Ambiente de desenvolvimento deve ser reproduzível (Docker, devcontainer, ou managed como dbt Cloud).
- **Orquestrador sem integração com alertas** — Airflow rodando sem notificação de falha. Tasks falham silenciosamente, e ninguém sabe até o analista reclamar. Alerta é configuração de dia 1, não de semana 3.

### Etapa 07 — Build

- **Transformações sem teste** — Modelo dbt sem dbt test, script Python sem assertion. A transformação "funciona" até que um edge case na fonte produza resultado errado — e ninguém detecta porque não há teste. Mínimo: not_null em PKs, unique em PKs, accepted_values em colunas categóricas.
- **Backfill feito "de uma vez" sem monitoramento** — Carregar 3 anos de dados em uma execução sem monitorar impacto na fonte (pode degradar o sistema operacional) ou no warehouse (pode gerar custo inesperado). Backfill deve ser feito em lotes com monitoramento de impacto.
- **Documentação deixada para depois** — "Depois a gente documenta." Depois nunca chega. Cada modelo/job deve ser documentado quando implementado — descrição, regras de negócio, owner, SLA. Pipeline sem documentação é pipeline que só o autor mantém.

### Etapa 08 — QA

- **"Os números parecem certos"** — Validação visual sem comparação formal com a fonte. "Parece certo" não é validação. Comparar contagens, somas e distribuições entre fonte e destino com queries explícitas e resultado documentado.
- **QA apenas com dados perfeitos** — Teste com dataset limpo e pequeno. Dados reais têm nulos, duplicados, encoding incorreto, e volume variável. QA deve incluir dados sujos para validar que os data quality checks funcionam.
- **Teste de idempotência esquecido** — Pipeline roda uma vez em QA e é declarado funcional. Na primeira falha em produção que exige re-run, duplica dados porque não é idempotente. Teste de reprocessamento é obrigatório.

### Etapa 09 — Launch Prep

- **"Vamos ligar o pipeline e avisar os analistas depois"** — Consumidores descobrem dados novos sem aviso, não sabem o schema, não sabem o SLA, e começam a usar dados parciais de backfill como se fossem finais. Comunicação formal com documentação antes do go-live é obrigatória.
- **Sem runbook de operações** — "Se der problema a gente liga para o engenheiro." O engenheiro não está disponível 24/7 e os incidentes mais comuns têm resolução simples (re-run, verificar credencial expirada). Runbook permite que operações resolva sem engenharia.
- **Backfill em produção sem monitoramento** — Executar backfill de anos de dados durante o horário comercial sem monitorar impacto na fonte. O sistema operacional degrada, os usuários reclamam, e o DBA desliga o acesso do pipeline de emergência. Backfill em produção deve ser feito em janela de baixo uso com monitoramento ativo.

### Etapa 10 — Go-Live

- **"O pipeline está rodando, projeto encerrado"** — Pipeline sem monitoramento ativo na primeira semana. Falhas intermitentes, thresholds mal calibrados e custos inesperados passam despercebidos. A primeira semana é a mais crítica.
- **Go-live antes do backfill completo** — Dashboard ativado com dados históricos parciais. Analista compara janeiro com fevereiro, mas janeiro tem dados incompletos do backfill. Resultado: decisões baseadas em dados errados. Backfill deve ser completo e validado antes de ativar consumidores.
- **Pipeline antigo desligado no dia do go-live** — Se o novo pipeline falha, não há como voltar. Manter o pipeline antigo ativo por pelo menos 2 semanas como contingência é barato e seguro.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é pipeline de dados** ou que a variante está incorreta e precisa ser reclassificada.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Queremos um dashboard interativo com filtros" | Projeto de BI/analytics, não de pipeline | O pipeline é meio, não fim. Incluir o projeto de BI no escopo ou separar em dois projetos. |
| "Os dados precisam ser editados manualmente pela equipe" | Aplicação CRUD com interface, não pipeline | Reclassificar para web-app de gestão de dados |
| "Queremos que o sistema envie alertas baseados nos dados" | Aplicação de monitoramento/regras de negócio | Pipeline alimenta, mas o sistema de alertas é projeto separado |
| "Precisa de um modelo de ML que preveja vendas" | Projeto de ML com pipeline como componente | Reclassificar de V1/V2 para V5 (ML Pipeline) ou separar os projetos |
| "Os dados vêm de sensores IoT em tempo real com milhões de eventos/segundo" | Streaming complexo com edge computing | Reclassificar de V1 (batch) para V3 (streaming) — arquitetura completamente diferente |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não temos acesso ao banco de origem" | 01 | Pipeline sem fonte é pipeline que não roda | Resolver acesso (credenciais, VPN, firewall) antes de avançar |
| "Não sabemos o volume de dados" | 02 | Impossível dimensionar infra e estimar custo | Executar profiling das fontes antes de definir arquitetura |
| "O DBA não autoriza extração no horário comercial e não há janela noturna" | 03 | Extração bloqueada sem janela disponível | Negociar janela com DBA ou usar CDC (não impacta produção) |
| "O orçamento é só para desenvolvimento, operação será zero" | 01 | Pipeline em cloud tem custo mensal obrigatório | Apresentar TCO (dev + operação) antes de continuar |
| "As regras de negócio ninguém sabe, estão no Excel do cara que saiu" | 04 | Transformações impossíveis de especificar | Investir tempo em engenharia reversa das regras antes de implementar |
| "O destino (warehouse) ainda não foi decidido" | 05 | Impossível definir modelos, transformações e custo | Escolher warehouse antes do Setup |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Temos 50 fontes de dados para integrar" | 01 | Escopo massivo, prazo provavelmente subestimado | Priorizar 5-10 fontes mais críticas para MVP, restante em fases |
| "O schema do banco muda toda semana" | 02 | Pipeline quebra com schema evolution sem detecção | Implementar schema detection e alertas de mudança desde o Setup |
| "A equipe de dados somos eu e um estagiário" | 01 | Time subdimensionado para a complexidade | Ajustar escopo ao tamanho do time ou expandir equipe |
| "O dado precisa estar pronto às 6h para o board meeting" | 03 | SLA rígido em horário de madrugada sem on-call | Definir modelo de on-call e plano de contingência para atrasos |
| "Não precisamos de data quality checks" | 04 | Dados incorretos chegam ao dashboard sem detecção | DQ checks são obrigatórios — erros de dados não detectados geram decisões erradas |
| "Vamos usar o BigQuery no plano on-demand sem limites" | 05 | Uma query mal escrita pode custar centenas de dólares | Configurar quotas, alertas de custo e custom cost controls desde o Setup |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Problema concreto de dados identificado com use case claro (pergunta 1)
- Consumidores reais dos dados identificados (pergunta 2)
- Fontes de dados mapeadas com acesso confirmado ou em processo (perguntas 3 e 4)
- Orçamento de desenvolvimento e operação aprovado (pergunta 7)
- Classificação de sensibilidade dos dados realizada (pergunta 8)

### Etapa 02 → 03

- Profiling de cada fonte realizado (pergunta 1)
- Modelo de dados do destino definido ao menos em nível conceitual (pergunta 2)
- Regras de transformação documentadas e aprovadas (pergunta 3)
- SLA de freshness acordado com consumidores reais (pergunta 10)
- Requisitos de masking e anonimização identificados (pergunta 11)

### Etapa 03 → 04

- Ownership de dados definido (pergunta 1)
- Contrato de dados formalizado com consumidores (pergunta 2)
- Custo operacional projetado e aprovado (pergunta 3)
- Modelo de operação e on-call definido (pergunta 5)

### Etapa 04 → 05

- DAG de execução completo produzido (pergunta 1)
- Cada tarefa especificada com lógica, testes e comportamento em falha (pergunta 2)
- Modelo de dados detalhado por camada documentado (pergunta 3)
- Alertas e thresholds especificados (pergunta 7)
- Documentação de definição aprovada por stakeholders (pergunta 15)

### Etapa 05 → 06

- Orquestrador, warehouse e framework de transformação escolhidos (perguntas 1, 2, 4)
- Ferramenta de ingestão definida por fonte (pergunta 3)
- Custo mensal calculado e aprovado (pergunta 8)
- Segurança e controle de acesso desenhados (pergunta 6)
- Arquitetura revisada por segurança e compliance (pergunta 15)

### Etapa 06 → 07

- Infraestrutura provisionada via IaC com ambientes separados (perguntas 1 e 2)
- Orquestrador configurado com conexões e alertas (pergunta 3)
- Framework de transformação com primeiro modelo end-to-end funcionando (pergunta 4)
- Pipeline de CI/CD testado com mudança real (pergunta 15)

### Etapa 07 → 08

- Ingestão de cada fonte implementada e validada (pergunta 1)
- Transformações implementadas com testes (pergunta 2)
- Backfill concluído e validado (pergunta 4)
- DAG completo executado end-to-end em staging (pergunta 9)

### Etapa 08 → 09

- Validação end-to-end (fonte vs. destino) realizada (pergunta 1)
- Cenários de falha testados (pergunta 2)
- Custo de operação medido e dentro do orçamento (pergunta 4)
- Segurança de acesso verificada (pergunta 5)
- Consumidores validaram os dados (pergunta 7)

### Etapa 09 → 10

- Promoção para produção via CI/CD executada (pergunta 1)
- Backfill em produção concluído e validado (pergunta 2)
- Runbook de operações produzido (pergunta 3)
- Consumidores notificados (pergunta 4)
- Plano de rollback documentado (pergunta 5)

### Etapa 10 → Encerramento

- Primeira execução em produção monitorada com sucesso (pergunta 1)
- Dados validados com fonte em produção (pergunta 2)
- SLA de freshness cumprido (pergunta 3)
- Handover operacional formalizado (pergunta 8)
- Aceite formal obtido (pergunta 12)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de pipeline de dados. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 ETL Batch | V2 ELT DW | V3 Streaming | V4 Integração CDC | V5 ML Pipeline |
|---|---|---|---|---|---|
| 01 Inception | 1 | 2 | 2 | 2 | 3 |
| 02 Discovery | 2 | 3 | 3 | 3 | 4 |
| 03 Alignment | 2 | 3 | 2 | 3 | 2 |
| 04 Definition | 2 | 4 | 4 | 3 | 5 |
| 05 Architecture | 2 | 3 | 5 | 3 | 4 |
| 06 Setup | 2 | 3 | 4 | 3 | 4 |
| 07 Build | 3 | 4 | 5 | 4 | 5 |
| 08 QA | 2 | 3 | 4 | 3 | 4 |
| 09 Launch Prep | 1 | 2 | 3 | 2 | 2 |
| 10 Go-Live | 1 | 2 | 3 | 2 | 2 |
| **Total relativo** | **18** | **29** | **35** | **28** | **35** |

**Observações por variante:**

- **V1 ETL Batch**: Esforço concentrado no Build (implementar extrações e transformações). Discovery e Definition são proporcionais ao número de fontes. Pipeline mais simples de operar e com menor custo.
- **V2 ELT DW**: Pico na Definition (modelo dimensional, regras de negócio, testes de qualidade) e no Build (dbt models, ingestão de múltiplas fontes). O gargalo oculto é a validação com consumidores — regras de negócio frequentemente mudam durante a implementação.
- **V3 Streaming**: Architecture é a etapa mais pesada (Kafka, Flink/Spark Streaming, schema registry, exactly-once). Build é intenso (processamento de eventos, estado, janelas temporais). QA exige testes de carga e latência sob condições realistas. Operação é significativamente mais complexa que batch.
- **V4 Integração CDC**: Peso distribuído entre Discovery (mapear sistemas e schemas), Build (CDC, conflict resolution, idempotência) e QA (validar consistência eventual entre sistemas). A complexidade cresce linearmente com o número de sistemas integrados.
- **V5 ML Pipeline**: Definition é a mais pesada (feature engineering, schema de features, versionamento). Build é intenso (extractors, transformers, feature store, training pipeline). A intersecção com data science exige ciclos de feedback frequentes.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Pipeline batch, sem streaming (Etapa 01, pergunta 6 → latência diária/horária) | Etapa 02: pergunta 14 (tópicos/eventos streaming). Etapa 05: pergunta 7 (message broker). Etapa 06: pergunta 13 (provisionamento Kafka). Etapa 07: pergunta 14 (latência de streaming). Etapa 08: pergunta 11 (teste de throughput streaming). |
| Fonte única, sem múltiplas fontes (Etapa 01, pergunta 3) | Etapa 02: pergunta 5 (mapa de dependências simplificado). Etapa 04: DAG trivial (sequência linear). |
| Sem dados sensíveis / PII (Etapa 01, pergunta 8) | Etapa 02: perguntas 9 e 11 (retenção e masking). Etapa 04: pergunta 11 (política de acesso por camada para PII). Etapa 05: pergunta 6 (RBAC e masking para PII). |
| Sem pipeline anterior para substituir (Etapa 01, pergunta 9) | Etapa 09: pergunta 11 (período de convivência). Etapa 10: perguntas 10 e 15 (convivência e desligamento do antigo). |
| Sem necessidade de ML / feature store (Etapa 01, pergunta 13) | Etapa 02: perguntas sobre feature engineering. Etapa 05: feature store e training pipeline não se aplicam. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Streaming confirmado (Etapa 01, pergunta 6 → real-time) | Etapa 02: pergunta 14 (schema de eventos) se torna bloqueadora. Etapa 05: pergunta 7 (message broker) é gate. Etapa 06: pergunta 13 (provisionamento de broker). Etapa 07: pergunta 14 (latência). Etapa 08: pergunta 11 (teste de carga streaming). |
| Dados com PII identificados (Etapa 01, pergunta 8) | Etapa 02: pergunta 11 (masking e anonimização) é gate. Etapa 03: pergunta 4 (estratégia de staging com dados anonimizados). Etapa 05: pergunta 6 (RBAC e criptografia). Etapa 08: pergunta 5 (auditoria de segurança). |
| Pipeline substitui pipeline anterior (Etapa 01, pergunta 9) | Etapa 02: levantamento do pipeline atual (tecnologia, fontes, regras). Etapa 09: perguntas 4 e 11 (comunicação aos consumidores, período de convivência). Etapa 10: perguntas 10 e 15 (monitoramento de convivência, desligamento do antigo). |
| Volume >100M registros por execução (Etapa 01, pergunta 5) | Etapa 05: pergunta 5 (particionamento) se torna crítica para custo. Etapa 05: Spark se torna provável necessidade. Etapa 07: pergunta 4 (backfill em lotes obrigatório). Etapa 08: pergunta 3 (teste de performance obrigatório com volume real). |
| Múltiplas fontes com schemas instáveis (Etapa 02, pergunta 13) | Etapa 05: pergunta 11 (schema evolution detection) se torna gate. Etapa 07: implementar detecção automática de mudança de schema com alerta. |
| Custo de warehouse é restrição forte (Etapa 01, pergunta 7) | Etapa 05: pergunta 5 (particionamento e custo) se torna a decisão mais importante. Etapa 08: pergunta 4 (medição de custo) é gate antes do go-live. Etapa 10: pergunta 14 (monitoramento de custo contínuo) é obrigatório. |
