---
title: "Data Platform / Analytics — Blueprint"
description: "Infraestrutura centralizada de dados: data warehouse, lakehouse ou data mesh. Foco em governança, catálogo de dados, self-service analytics e consumo por múltiplas equipes."
category: project-blueprint
type: data-platform
status: rascunho
created: 2026-04-13
---

# Data Platform / Analytics

## Descrição

Infraestrutura centralizada de dados: data warehouse, lakehouse ou data mesh. Foco em governança, catálogo de dados, self-service analytics e consumo por múltiplas equipes.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda plataforma de dados é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Data Warehouse Centralizado

Repositório único de dados estruturados, tipicamente modelado em star ou snowflake schema, alimentado por pipelines de ETL/ELT a partir de fontes transacionais (ERPs, CRMs, sistemas legados). O foco é consolidar dados de múltiplos sistemas operacionais em uma fonte confiável para relatórios gerenciais e dashboards de BI. Atende primariamente analistas de negócio que consomem dados via ferramentas como Power BI, Looker ou Tableau. O volume de dados é moderado (GBs a baixos TBs), com atualização tipicamente batch (diária ou horária). Exemplos: warehouse corporativo para relatórios financeiros, consolidação de vendas multi-canal, painel de indicadores de RH.

### V2 — Data Lakehouse

Combina a flexibilidade do data lake (armazenamento de dados brutos em formatos abertos — Parquet, Delta, Iceberg) com as garantias transacionais do data warehouse (ACID, time travel, schema enforcement). O foco é suportar workloads analíticos e de machine learning sobre o mesmo armazenamento, eliminando a necessidade de copiar dados entre lake e warehouse. Lida com volumes maiores (TBs a PBs), dados semi-estruturados (JSON, logs) e streaming. Exige governança robusta porque o dado cru coexiste com o dado curado. Exemplos: plataforma de analytics para fintech com dados de transações e modelos de fraude, plataforma de dados de e-commerce com clickstream e recomendação.

### V3 — Data Mesh

Arquitetura descentralizada onde cada domínio de negócio (marketing, vendas, logística, produto) é responsável por produzir e publicar seus próprios data products como APIs ou tabelas acessíveis, seguindo padrões globais de interoperabilidade e governança federada. O foco não é na infraestrutura central, mas na responsabilidade distribuída — cada time é dono do seu pipeline e da qualidade dos seus dados. Exige maturidade organizacional alta: times precisam ter engenheiros de dados ou ao menos analistas com capacidade de operar pipelines. Exemplos: empresa com +10 squads independentes que precisam compartilhar dados entre domínios sem gargalo central.

### V4 — Self-Service Analytics

Plataforma focada em empoderar usuários de negócio para explorar dados, criar dashboards e extrair insights sem depender de engenheiros de dados ou TI para cada nova pergunta. O foco é na camada de consumo: semantic layer, catálogo de dados pesquisável, linhagem visível, e ferramentas de BI acessíveis para não-técnicos. A infraestrutura de ingestão e transformação pode ser simples — o diferencial está na experiência do consumidor de dados. Exemplos: plataforma de BI para rede de varejo onde gerentes regionais montam seus próprios relatórios, ambiente de analytics para startup que quer cultura data-driven.

### V5 — Real-Time / Streaming Analytics

Plataforma orientada a processamento de eventos em tempo real ou near-real-time, com ingestão contínua (Kafka, Kinesis, Pub/Sub), transformação em streaming (Flink, Spark Structured Streaming, ksqlDB) e consumo em dashboards ao vivo ou triggers automáticos. O foco é latência — dados precisam estar disponíveis para consumo em segundos ou minutos, não horas. A complexidade de operação é significativamente maior que batch: monitoramento de lag, back-pressure, exactly-once semantics, e re-processamento de eventos falhos são preocupações constantes. Exemplos: monitoramento de IoT industrial, detecção de fraude em tempo real, dashboard de operações logísticas com rastreamento ao vivo.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Armazenamento | Orquestração | Transformação | BI / Consumo | Observações |
|---|---|---|---|---|---|
| V1 — DW Centralizado | BigQuery, Snowflake ou Redshift | Airflow ou Dagster | dbt | Power BI, Looker ou Metabase | dbt como padrão de transformação. Snowflake se multi-cloud. BigQuery se GCP-native. |
| V2 — Lakehouse | Databricks (Delta), Snowflake (Iceberg) ou Trino + MinIO | Airflow, Dagster ou Databricks Workflows | dbt ou Spark SQL | Looker, Superset ou Databricks SQL | Delta Lake ou Iceberg obrigatório para ACID. Custo de storage menor que DW puro. |
| V3 — Data Mesh | Depende do domínio — cada squad escolhe | Cada domínio opera seu pipeline | dbt por domínio, contratos via protobuf/JSON Schema | Catálogo centralizado (DataHub, Atlan) + BI por domínio | Plataforma de self-serve (templates, infra-as-code) é pré-requisito. Governança federada obrigatória. |
| V4 — Self-Service | BigQuery, Snowflake ou Postgres analítico | Airflow ou Dagster | dbt com semantic layer (Cube, Lightdash) | Metabase, Lightdash ou Looker | Catálogo de dados (DataHub, Atlan, Amundsen) é diferencial. Semantic layer evita SQL direto. |
| V5 — Streaming | Kafka + Flink ou Kinesis + Lambda | Kafka Connect, Flink CDC | Flink SQL, ksqlDB ou Spark Structured Streaming | Grafana, Kibana ou dashboard custom | Confluent Cloud simplifica operação de Kafka. Schema Registry obrigatório para contratos. |

---

## Etapa 01 — Inception

- **Origem da demanda**: A necessidade de uma plataforma de dados costuma surgir de dores concretas — relatórios manuais em planilhas que levam dias para consolidar, dados inconsistentes entre departamentos ("o número de vendas do financeiro não bate com o do comercial"), incapacidade de responder perguntas de negócio sem acionar TI, ou exigência regulatória de auditoria e rastreabilidade de dados. Entender o gatilho real é essencial porque ele define o critério de sucesso: se o problema é inconsistência, a prioridade é single source of truth; se é velocidade de resposta, a prioridade é self-service.

- **Maturidade de dados da organização**: Empresas que nunca tiveram um warehouse centralizado enfrentam desafios diferentes de empresas que já operam um e querem evoluir para lakehouse ou mesh. No primeiro caso, o maior esforço está em identificar e conectar as fontes de dados — muitas vezes espalhadas em planilhas, ERPs legados, sistemas proprietários sem API. No segundo caso, o desafio é migrar sem interromper os consumidores existentes (dashboards, relatórios automatizados, pipelines de ML). Mapear a maturidade de dados na Inception evita propor uma arquitetura sofisticada para uma organização que ainda não tem o básico resolvido.

- **Stakeholders e consumidores de dados**: O patrocinador formal costuma ser o C-level (CDO, CTO, CFO), mas os consumidores reais são analistas de negócio, cientistas de dados e gerentes operacionais. Cada grupo tem expectativas diferentes: o C-level quer KPIs estratégicos com atualização diária, o analista quer explorar dados livremente sem depender de engenharia, e o cientista de dados quer acesso a dados brutos em formato compatível com notebooks e modelos de ML. Identificar todos os perfis de consumidor desde o início é obrigatório para dimensionar a camada de consumo.

- **Expectativas de latência**: A diferença entre dados atualizados diariamente (batch), a cada hora (micro-batch) e em tempo real (streaming) tem impacto direto na complexidade da arquitetura, no custo de infraestrutura e no perfil do time necessário para operar. Muitos projetos começam pedindo "tempo real" quando na verdade batch diário resolve 90% dos casos de uso. Esclarecer as expectativas reais de latência por caso de uso evita over-engineering e reduz custo significativamente.

- **Regulamentações e compliance**: Plataformas de dados centralizam informações sensíveis de múltiplas fontes — dados financeiros, dados pessoais de clientes (LGPD/GDPR), dados de saúde (HIPAA), dados de cartão (PCI DSS). As regulamentações aplicáveis definem requisitos obrigatórios de mascaramento, anonimização, retenção, auditoria de acesso e direito ao esquecimento que impactam profundamente a arquitetura de storage, o modelo de governança e os controles de acesso. Identificar quais regulamentações se aplicam na Inception é pré-requisito para evitar refatoração de segurança após o go-live.

- **Orçamento e modelo de custo**: Plataformas de dados em cloud têm modelo de custo baseado em consumo (compute por hora, storage por TB, queries por volume processado) que pode surpreender se não for projetado. Um warehouse que processa 1TB/dia custa radicalmente diferente de um que processa 100TB/dia. O custo de operação mensal frequentemente supera o custo de desenvolvimento — e precisa ser apresentado ao patrocinador nesta fase com projeções de cenário otimista, esperado e pessimista para evitar cancelamento do projeto por surpresa financeira.

### Perguntas

1. Qual é o gatilho real desta demanda — relatórios manuais, dados inconsistentes, exigência regulatória ou incapacidade de responder perguntas de negócio? [fonte: Diretoria, CDO, CFO] [impacto: PM, Arquiteto de Dados]
2. Quem são os consumidores reais dos dados (analistas, cientistas de dados, gerentes, sistemas automatizados) e quais são suas necessidades específicas? [fonte: Áreas de negócio, TI] [impacto: Arquiteto de Dados, Dev]
3. Qual é o nível de maturidade de dados atual — já existe warehouse, pipelines de ETL, ou tudo está em planilhas e sistemas isolados? [fonte: TI, CDO] [impacto: Arquiteto de Dados, PM]
4. Quais são as fontes de dados que precisam ser integradas no MVP (ERPs, CRMs, bancos transacionais, APIs, planilhas, arquivos)? [fonte: TI, Áreas de negócio] [impacto: Engenheiro de Dados, Dev]
5. Qual é a expectativa de latência dos dados — atualização diária é suficiente ou há casos de uso que exigem near-real-time? [fonte: Áreas de negócio, Diretoria] [impacto: Arquiteto de Dados, DevOps]
6. Quais regulamentações se aplicam aos dados (LGPD, GDPR, HIPAA, PCI DSS, SOX) e existe um DPO ou área de compliance envolvida? [fonte: Jurídico, Compliance, DPO] [impacto: Arquiteto de Dados, Segurança]
7. Qual é o orçamento total disponível, separando custo de desenvolvimento e custo de operação mensal em cloud? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto de Dados]
8. Qual é o prazo esperado para o primeiro caso de uso funcional e existe data de negócio que justifica esse prazo? [fonte: Diretoria, Áreas de negócio] [impacto: PM, Dev]
9. O projeto substituirá uma plataforma existente ou será construído do zero ao lado de soluções atuais? [fonte: TI, CDO] [impacto: Arquiteto de Dados, PM]
10. Existe um time de engenharia de dados interno ou o projeto depende inteiramente de consultoria externa? [fonte: RH, TI, CDO] [impacto: PM, Arquiteto de Dados]
11. Qual é o volume estimado de dados a ser processado (GBs, TBs, PBs) e qual a projeção de crescimento anual? [fonte: TI, Áreas de negócio] [impacto: Arquiteto de Dados, DevOps]
12. Quem toma decisões de arquitetura técnica — existe um arquiteto de dados ou um comitê técnico? [fonte: TI, Diretoria] [impacto: Arquiteto de Dados, PM]
13. O cliente tem preferência ou restrição por cloud provider (AWS, GCP, Azure) ou por ferramentas específicas? [fonte: TI, Diretoria, Compras] [impacto: Arquiteto de Dados, Dev]
14. Há dados legados que precisam ser migrados de sistemas anteriores para a nova plataforma? [fonte: TI, Áreas de negócio] [impacto: Engenheiro de Dados, PM]
15. Existe expectativa de suporte a machine learning ou AI sobre os dados da plataforma agora ou no futuro próximo? [fonte: CDO, Ciência de Dados, Diretoria] [impacto: Arquiteto de Dados, Dev]

---

## Etapa 02 — Discovery

- **Inventário de fontes de dados**: Mapear exaustivamente todas as fontes de dados que alimentarão a plataforma — bancos transacionais (PostgreSQL, MySQL, SQL Server, Oracle), ERPs (SAP, TOTVS, Oracle EBS), CRMs (Salesforce, HubSpot, Dynamics), APIs REST/GraphQL de SaaS (Stripe, Shopify, Google Ads), planilhas compartilhadas (Google Sheets, Excel em SharePoint), arquivos em filesystems (CSVs, JSONs em SFTP, S3), e fontes de eventos (logs de aplicação, webhooks, IoT). Para cada fonte, documentar: tecnologia, método de acesso disponível (API, JDBC, CDC, export manual), volume de dados, frequência de atualização, e responsável técnico. Este inventário define diretamente o esforço de ingestão.

- **Casos de uso prioritários**: Listar os 3 a 5 casos de uso de dados que o negócio espera resolver com o MVP — e ordená-los por valor de negócio e viabilidade técnica. Exemplos: "consolidar vendas de todas as lojas em um dashboard diário", "calcular margem por produto cruzando dados de ERP e CRM", "detectar churn previsto com modelo de ML". Cada caso de uso define quais fontes são obrigatórias, qual latência é necessária, e quais métricas serão consumidas. Um projeto que tenta resolver 15 casos de uso no MVP invariavelmente não entrega nenhum — foco é obrigatório.

- **Qualidade dos dados nas fontes**: Avaliar o estado real dos dados nas fontes: campos com valores nulos ou inconsistentes, duplicações, formatos divergentes (datas em DD/MM/YYYY em um sistema e YYYY-MM-DD em outro), encoding, e dados legados sem documentação de significado. Dados de baixa qualidade não se corrigem magicamente ao serem carregados em um warehouse — se entram sujos, saem sujos. Investir em data quality no pipeline de ingestão (validação, limpeza, deduplicação) é obrigatório, e o esforço precisa estar refletido no cronograma.

- **Modelo de governança existente**: Verificar se a organização já possui alguma forma de governança de dados — glossário de termos de negócio, data stewards definidos por domínio, políticas de acesso documentadas, classificação de sensibilidade de dados. Em organizações sem governança, o projeto de plataforma de dados frequentemente se torna o primeiro esforço de governança — o que aumenta significativamente o escopo e a resistência organizacional. Se não há nenhuma governança, incluir a criação de um modelo mínimo viável de governança no escopo do projeto.

- **Perfis de consumo e ferramentas de BI**: Mapear como cada grupo de consumidores espera acessar os dados: analistas de negócio via ferramentas de BI (Power BI, Looker, Tableau, Metabase), cientistas de dados via notebooks (Jupyter, Databricks Notebooks), engenheiros via SQL direto ou APIs, e sistemas automatizados via queries agendadas ou triggers. Cada perfil implica requisitos diferentes de semantic layer, controle de acesso, performance de queries e formato de dados servidos. Um warehouse otimizado para dashboards de BI pode ter performance inadequada para queries ad-hoc de data science.

- **Requisitos de segurança e acesso**: Identificar os requisitos de controle de acesso granular — quem pode ver quais dados, em qual nível de detalhe. Em plataformas de dados, row-level security (um gerente vê apenas dados da sua região), column-level security (dados de PII mascarados para analistas que não precisam), e tag-based access control (dados classificados como "sensível" requerem aprovação para acesso) são requisitos comuns. Avaliar se o modelo de acesso pode ser gerenciado pela ferramenta de warehouse (BigQuery IAM, Snowflake RBAC) ou se precisa de uma camada adicional de governança (Apache Ranger, Privacera).

### Perguntas

1. Quantas fontes de dados distintas precisam ser integradas no MVP e quais são suas tecnologias de acesso (API, JDBC, CDC, CSV)? [fonte: TI, Áreas de negócio] [impacto: Engenheiro de Dados, Arquiteto de Dados]
2. Quais são os 3 a 5 casos de uso prioritários de dados que o negócio espera resolver no MVP, ordenados por valor? [fonte: Diretoria, Áreas de negócio] [impacto: PM, Arquiteto de Dados]
3. Qual é o estado atual da qualidade dos dados nas fontes — existem problemas conhecidos de duplicação, inconsistência ou campos nulos? [fonte: TI, Áreas de negócio] [impacto: Engenheiro de Dados, QA]
4. Existe alguma forma de governança de dados na organização (glossário, data stewards, políticas de acesso documentadas)? [fonte: CDO, TI, Compliance] [impacto: Arquiteto de Dados, PM]
5. Quais ferramentas de BI o time de negócio já utiliza ou tem preferência (Power BI, Looker, Tableau, Metabase)? [fonte: Áreas de negócio, TI] [impacto: Arquiteto de Dados, Dev]
6. Quais dados são considerados sensíveis (PII, financeiros, saúde) e quais regras de mascaramento ou anonimização se aplicam? [fonte: Jurídico, DPO, Compliance] [impacto: Segurança, Engenheiro de Dados]
7. Qual é o volume diário de dados gerados por cada fonte e qual o volume total acumulado a ser carregado na migração inicial? [fonte: TI] [impacto: Arquiteto de Dados, DevOps]
8. Existem SLAs internos de disponibilidade dos dados (ex.: dashboard atualizado até 8h da manhã com dados do dia anterior)? [fonte: Diretoria, Áreas de negócio] [impacto: Engenheiro de Dados, DevOps]
9. O time de negócio tem capacidade de escrever SQL ou a plataforma precisa oferecer camada visual sem código? [fonte: Áreas de negócio, RH] [impacto: Arquiteto de Dados, Dev]
10. Há requisitos de auditoria — quem acessou qual dado, quando e para quê — impostos por regulamentação ou política interna? [fonte: Compliance, Jurídico, Auditoria] [impacto: Segurança, Arquiteto de Dados]
11. Existe algum pipeline de dados em produção que precisa ser migrado ou substituído sem interrupção? [fonte: TI, Engenharia de Dados atual] [impacto: Engenheiro de Dados, PM]
12. Quais são os horários de pico de consumo de dados e quais os SLAs de performance de queries esperados? [fonte: Áreas de negócio, TI] [impacto: Arquiteto de Dados, DevOps]
13. Há necessidade de compartilhar dados com parceiros externos ou fornecedores com controle de acesso separado? [fonte: Comercial, Jurídico, TI] [impacto: Segurança, Arquiteto de Dados]
14. O projeto precisa suportar dados não-estruturados (imagens, PDFs, áudio, vídeo) além de dados tabulares? [fonte: Áreas de negócio, TI] [impacto: Arquiteto de Dados, Dev]
15. Existe orçamento e responsável definidos para a produção de documentação de dados (dicionário, linhagem, catálogo)? [fonte: CDO, Financeiro] [impacto: PM, Arquiteto de Dados]

---

## Etapa 03 — Alignment

- **Modelo de governança de dados**: Alinhar formalmente quem é responsável por cada domínio de dados (data owners), quem garante qualidade e padrões (data stewards), e como decisões de acesso e classificação são tomadas. Em organizações com múltiplas áreas de negócio, a governança é frequentemente o ponto de maior conflito — marketing quer acesso irrestrito aos dados de vendas, jurídico quer restringir tudo, e o financeiro quer controle sobre quem vê margem. Definir o modelo de governança antes do setup da plataforma evita implementar controles que depois precisam ser refeitos quando os stakeholders finalmente se alinham.

- **Priorização de fontes e casos de uso do MVP**: Garantir que todos os stakeholders concordam com o escopo do MVP — quais fontes serão integradas, quais não, quais casos de uso serão atendidos e quais ficam para fases futuras. Em projetos de data platform, a tentação de incluir "mais uma fontezinha" ou "mais um relatório" é constante e corrosiva. Sem priorização rígida, o MVP se expande silenciosamente até se tornar inviável no prazo. O alinhamento deve produzir um documento formal com fontes, casos de uso e métricas do MVP, assinado pelo patrocinador.

- **Modelo de custo projetado e aprovado**: Apresentar a projeção de custo mensal da plataforma em produção — compute (clusters de processamento, serverless queries), storage (dados brutos, dados transformados, snapshots), networking (egress entre regiões, entre clouds), ferramentas SaaS (BI, catálogo, orquestração managed) e licenças. Projetar três cenários (otimista, esperado, pessimista) com base no volume de dados e no número de queries esperados. Obter aprovação formal do financeiro antes de avançar — plataformas de dados sem budget aprovado para operação são desligadas 6 meses após o lançamento.

- **Responsabilidade operacional pós-lançamento**: Definir quem vai operar a plataforma após o go-live — um time de engenharia de dados interno (ideal), um contrato de operação terceirizado, ou os próprios desenvolvedores do projeto (arriscado). Operação de plataforma de dados inclui: monitorar e corrigir pipelines que falham, ajustar performance de queries lentas, gerenciar custo de compute, rotacionar credenciais, e responder a incidentes de dados. Sem time operacional definido, a plataforma degrada em semanas.

- **SLA de dados e contrato com consumidores**: Definir formalmente os SLAs de dados por caso de uso: freshness (dados atualizados até que horas), completeness (percentual mínimo de registros completos), accuracy (taxa de erro aceitável), e availability (uptime do ambiente de queries). Esses SLAs funcionam como contrato entre o time de dados e os consumidores — sem eles, qualquer falha de pipeline é "urgente" e qualquer delay é "inaceitável", porque não há expectativa formal contra a qual medir.

### Perguntas

1. O modelo de governança de dados foi definido com data owners e data stewards nomeados por domínio? [fonte: CDO, Diretoria, Áreas de negócio] [impacto: Arquiteto de Dados, PM]
2. Todos os stakeholders concordam com o escopo do MVP (fontes, casos de uso, métricas) e isso está documentado formalmente? [fonte: Diretoria, Áreas de negócio] [impacto: PM, Dev]
3. A projeção de custo mensal da plataforma em produção foi apresentada em três cenários e aprovada pelo financeiro? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto de Dados]
4. O time que vai operar a plataforma após o go-live está definido (interno, terceirizado, híbrido) e com capacidade confirmada? [fonte: RH, TI, Diretoria] [impacto: PM, DevOps]
5. Os SLAs de dados (freshness, completeness, accuracy, availability) foram definidos e acordados com os consumidores? [fonte: Áreas de negócio, TI] [impacto: Engenheiro de Dados, PM]
6. O cloud provider e a região (region) foram escolhidos considerando latência, custo, residência de dados e compliance? [fonte: TI, Jurídico, Financeiro] [impacto: Arquiteto de Dados, DevOps]
7. A política de retenção de dados foi definida — quanto tempo cada tipo de dado é mantido e quando é purgado ou arquivado? [fonte: Jurídico, Compliance, CDO] [impacto: Engenheiro de Dados, DevOps]
8. As dependências externas críticas (acessos a APIs, credenciais de fontes, aprovações de compliance) foram listadas com prazos? [fonte: TI, Fornecedores, Jurídico] [impacto: PM, Engenheiro de Dados]
9. O modelo de controle de acesso (RBAC, row-level, column-level) foi definido e todos os stakeholders concordam? [fonte: CDO, Compliance, Áreas de negócio] [impacto: Segurança, Arquiteto de Dados]
10. O processo de onboarding de novas fontes de dados pós-MVP foi definido (quem solicita, quem aprova, quem implementa)? [fonte: CDO, TI] [impacto: PM, Engenheiro de Dados]
11. Existe processo definido para revisão e aprovação de entregas parciais (pipeline por pipeline, dashboard por dashboard)? [fonte: Diretoria, Áreas de negócio] [impacto: PM, Dev]
12. O time de desenvolvimento tem acesso a ambientes sandbox das fontes de dados para desenvolvimento sem risco a produção? [fonte: TI, Fornecedores] [impacto: Engenheiro de Dados, Dev]
13. O modelo de versionamento de schemas e contratos de dados foi definido (breaking changes, backward compatibility)? [fonte: TI, CDO] [impacto: Arquiteto de Dados, Engenheiro de Dados]
14. O cliente foi informado sobre o impacto de mudanças de escopo (novas fontes, novos casos de uso) no prazo e no custo? [fonte: Diretoria] [impacto: PM]
15. O treinamento do time de negócio para uso das ferramentas de BI foi planejado com data e responsável? [fonte: RH, Áreas de negócio, CDO] [impacto: PM, Dev]

---

## Etapa 04 — Definition

- **Modelagem dimensional**: Definir o modelo de dados do warehouse — fatos (tabelas de métricas com granularidade definida: fato_vendas com uma linha por item vendido, fato_atendimentos com uma linha por ticket) e dimensões (tabelas descritivas com atributos: dim_cliente, dim_produto, dim_tempo, dim_loja). A granularidade de cada fato é a decisão mais importante — ela determina o volume de dados, a performance de queries e a flexibilidade analítica. Granularidade muito alta (uma linha por clique) gera custos de storage e compute desnecessários se os consumidores só precisam de agregações diárias. Granularidade muito baixa (uma linha por mês) impede drill-down. Definir com os consumidores finais antes de implementar.

- **Mapeamento de pipelines por fonte**: Para cada fonte de dados, documentar o pipeline completo: método de extração (full load, incremental por timestamp, CDC via Debezium/DMS), frequência (diário, horário, real-time), transformações necessárias (limpeza, deduplicação, join com outras fontes, cálculo de métricas derivadas), e destino (tabela raw, staging, ou diretamente curated). Cada pipeline é uma unidade de trabalho estimável — um pipeline simples de CSV diário é radicalmente diferente de um pipeline CDC de banco Oracle com transformações complexas.

- **Dicionário de dados e glossário de negócio**: Produzir o dicionário de dados que descreve cada tabela e campo do modelo final — nome técnico, nome de negócio, tipo de dado, descrição, fonte de origem, regra de transformação, e classificação de sensibilidade. Paralelamente, produzir o glossário de negócio que define os termos usados pela organização de forma unívoca: "receita líquida" significa X, "cliente ativo" significa Y, "churn" significa Z. Sem glossário, cada área usa termos iguais com significados diferentes — e os dashboards produzem números que ninguém confia.

- **Definição de métricas e KPIs**: Especificar cada métrica que será calculada na plataforma — fórmula exata, granularidade, filtros padrão, e responsável pela definição. Exemplo: "Ticket Médio = soma(valor_pedido) / contagem_distinta(pedido_id), filtrado por status = 'concluído', granularidade diária por loja". Métricas definidas informalmente ("ticket médio") sem especificação formal resultam em dashboards que mostram números diferentes do que o financeiro calcula em planilha — destruindo a confiança na plataforma antes mesmo do go-live.

- **Estratégia de testes de dados**: Definir como a qualidade dos dados será validada em cada camada do pipeline: testes na ingestão (schema validation, contagem de registros, detecção de nulos em campos obrigatórios), testes na transformação (reconciliação de totais entre origem e destino, validação de business rules), e testes no consumo (métricas calculadas batem com fonte de verdade conhecida). Ferramentas como Great Expectations, dbt tests, Soda ou Elementary automatizam esses testes. Sem testes de dados automatizados, erros silenciosos se propagam até os dashboards e só são descobertos quando o CFO percebe um número errado na apresentação ao board.

- **Linhagem de dados (data lineage)**: Documentar a linhagem completa de cada métrica — de qual sistema fonte veio, por quais transformações passou, e em qual dashboard ou relatório é consumida. A linhagem é obrigatória para auditoria (provar que o número é correto e rastreável), para impacto (quando uma fonte muda, saber quais dashboards são afetados), e para debugging (quando um número parece errado, rastrear até a fonte). Ferramentas como dbt + docs, DataHub ou OpenLineage automatizam a captura de linhagem.

### Perguntas

1. O modelo dimensional (fatos e dimensões) foi definido com granularidade aprovada pelos consumidores de dados? [fonte: Áreas de negócio, CDO] [impacto: Engenheiro de Dados, Arquiteto de Dados]
2. Cada pipeline foi documentado com método de extração, frequência, transformações e destino? [fonte: TI, Engenheiro de Dados atual] [impacto: Engenheiro de Dados, Dev]
3. O dicionário de dados foi produzido com nome técnico, nome de negócio, tipo, descrição e classificação de sensibilidade? [fonte: CDO, TI, Áreas de negócio] [impacto: Engenheiro de Dados, Arquiteto de Dados]
4. O glossário de termos de negócio foi definido e validado por todas as áreas consumidoras? [fonte: Áreas de negócio, CDO] [impacto: PM, Engenheiro de Dados]
5. As métricas e KPIs foram especificados com fórmula exata, granularidade, filtros e responsável pela definição? [fonte: Áreas de negócio, Financeiro, Diretoria] [impacto: Engenheiro de Dados, Dev]
6. A estratégia de testes de dados foi definida para cada camada (ingestão, transformação, consumo)? [fonte: TI, QA] [impacto: Engenheiro de Dados, QA]
7. A linhagem de dados foi documentada da fonte ao dashboard para as métricas críticas? [fonte: CDO, TI] [impacto: Engenheiro de Dados, Arquiteto de Dados]
8. As regras de tratamento de dados nulos, duplicados e inconsistentes foram especificadas por pipeline? [fonte: Áreas de negócio, TI] [impacto: Engenheiro de Dados, QA]
9. O esquema de particionamento e clustering das tabelas foi definido para otimizar as queries mais frequentes? [fonte: Arquiteto de Dados] [impacto: Engenheiro de Dados, DevOps]
10. As regras de slowly changing dimensions (SCD tipo 1, 2 ou 3) foram definidas para cada dimensão? [fonte: Áreas de negócio, CDO] [impacto: Engenheiro de Dados]
11. O volume de dados históricos a ser carregado na carga inicial foi quantificado e o esforço estimado? [fonte: TI, Áreas de negócio] [impacto: Engenheiro de Dados, PM]
12. Os contratos de dados entre produtores e consumidores foram formalizados (schema, SLA, responsável)? [fonte: CDO, TI] [impacto: Arquiteto de Dados, PM]
13. As regras de mascaramento e anonimização de dados sensíveis foram definidas por campo e por perfil de acesso? [fonte: Jurídico, DPO, Compliance] [impacto: Segurança, Engenheiro de Dados]
14. Os dashboards e relatórios do MVP foram wireframados com as métricas, filtros e granularidade esperados? [fonte: Áreas de negócio, Designer] [impacto: Dev, Engenheiro de Dados]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes do início do Setup? [fonte: Diretoria, CDO, Áreas de negócio] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Escolha do warehouse/lakehouse**: A seleção da engine de armazenamento e processamento define o ecossistema e deve considerar o perfil do time, o cloud provider e os padrões de query. BigQuery é indicado para times em GCP que querem serverless puro (sem clusters para gerenciar), com pricing por volume de dados processado por query — ideal para workloads intermitentes. Snowflake é indicado para ambientes multi-cloud, com separação de compute e storage que permite escalar independentemente, e com Snowflake Marketplace para compartilhamento de dados. Databricks é indicado quando há workloads mistos de SQL analytics e machine learning, com Delta Lake como formato de storage — forte para lakehouse. Redshift é indicado para times fortemente investidos em AWS com workloads previsíveis onde reserved instances reduzem custo.

- **Orquestração de pipelines**: A escolha do orquestrador define como os pipelines são agendados, monitorados e recuperados em caso de falha. Apache Airflow é o padrão de mercado — maduro, com ecossistema enorme de operadores e integrações, mas exige infraestrutura para hospedar (Composer no GCP, MWAA na AWS, ou self-hosted). Dagster é a alternativa moderna com foco em data assets (em vez de tarefas), software-defined assets que facilitam a linhagem, e melhor experiência de desenvolvimento local. Prefect e Mage são opções mais simples para times menores. Databricks Workflows é indicado quando toda a stack já está em Databricks. A escolha deve considerar a complexidade dos pipelines, o tamanho do time e a disposição de operar infraestrutura.

- **Camada de transformação (dbt)**: dbt (data build tool) se consolidou como padrão de mercado para transformação SQL em warehouses — permite modelar transformações como código versionado, com testes automatizados, documentação gerada, e linhagem nativa. A decisão principal é entre dbt Core (open-source, rodado via Airflow ou CI/CD) e dbt Cloud (SaaS com IDE web, agendamento e monitoramento integrados). dbt Cloud simplifica a operação e é ideal para times menores, mas tem custo mensal significativo em planos Team/Enterprise. Para lakehouse com Spark, o equivalente é usar Spark SQL com dbt-spark adapter ou transformações em PySpark orquestradas pelo Airflow.

- **Catálogo e descoberta de dados**: Em plataformas com dezenas de tabelas e múltiplos consumidores, a camada de catálogo é essencial para que as pessoas encontrem os dados certos sem perguntar ao engenheiro de dados. DataHub (open-source, LinkedIn) e Atlan (SaaS) são as opções mais maduras — oferecem busca semântica, linhagem visual, glossário integrado, e profiling automático de dados. OpenMetadata é alternativa open-source mais recente. O catálogo deve ser integrado ao dbt para herdar documentação e linhagem automaticamente. Sem catálogo, a plataforma se torna uma caixa preta onde só quem construiu sabe o que existe.

- **Observabilidade de dados**: Monitorar a saúde dos pipelines (falhas, atrasos) é necessário mas insuficiente — é preciso monitorar a saúde dos dados em si. Data observability cobre: freshness (dados pararam de chegar?), volume (número de registros mudou drasticamente?), schema (colunas desapareceram ou mudaram de tipo?), distribution (valores estão fora do range esperado?), e linhagem de impacto (se essa tabela quebrou, quais dashboards são afetados?). Ferramentas como Elementary (open-source para dbt), Monte Carlo (SaaS), e Soda Core automatizam esses monitoramentos. Sem observabilidade, problemas silenciosos se propagam até o consumidor final.

- **Segurança e controle de acesso**: Definir a arquitetura de segurança em múltiplas camadas: autenticação (SSO via SAML/OIDC com identity provider corporativo), autorização (RBAC com roles granulares — analista de vendas vê dados de vendas mas não de RH), encriptação (at rest e in transit), mascaramento dinâmico (PII mascarado para roles sem privilégio), e auditoria (logs de acesso a dados sensíveis com retenção definida). Em ambientes regulados (financeiro, saúde), a arquitetura de segurança é frequentemente o gate mais exigente da revisão de compliance.

### Perguntas

1. O warehouse/lakehouse foi escolhido com justificativa técnica considerando perfil do time, cloud provider e padrão de workload? [fonte: TI, Arquiteto de Dados] [impacto: Engenheiro de Dados, Dev]
2. O orquestrador de pipelines foi escolhido considerando complexidade dos workflows, tamanho do time e custo de operação? [fonte: TI, Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
3. A decisão entre dbt Core e dbt Cloud foi tomada com justificativa de custo e operação? [fonte: TI, Financeiro] [impacto: Engenheiro de Dados, Dev]
4. A solução de catálogo de dados foi escolhida e o plano de integração com dbt e warehouse definido? [fonte: CDO, TI] [impacto: Arquiteto de Dados, Dev]
5. A estratégia de observabilidade de dados (freshness, volume, schema, distribution) foi definida com ferramentas e alertas? [fonte: TI, CDO] [impacto: Engenheiro de Dados, DevOps]
6. A arquitetura de segurança (autenticação, RBAC, mascaramento, auditoria) foi definida e aprovada por compliance? [fonte: Segurança, Compliance, TI] [impacto: Arquiteto de Dados, Segurança]
7. O modelo de ambientes (development, staging, production) foi definido com isolamento de dados e acessos? [fonte: TI] [impacto: Engenheiro de Dados, DevOps]
8. A estratégia de ingestão por tipo de fonte foi definida (full load, incremental, CDC) com ferramentas específicas? [fonte: TI, Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
9. Os custos mensais de operação foram calculados em cenários otimista, esperado e pessimista com base no volume projetado? [fonte: Financeiro, TI] [impacto: PM, Arquiteto de Dados]
10. A estratégia de backup e disaster recovery foi definida (RPO, RTO, regiões de failover)? [fonte: TI, Compliance] [impacto: DevOps, Arquiteto de Dados]
11. A semantic layer (Cube, Lightdash, Looker LookML) foi definida para garantir consistência de métricas entre consumidores? [fonte: Áreas de negócio, CDO] [impacto: Dev, Engenheiro de Dados]
12. A estratégia de versionamento de infraestrutura (Terraform, Pulumi, CloudFormation) foi definida? [fonte: TI, DevOps] [impacto: DevOps, Engenheiro de Dados]
13. Os limites de custo e alertas de billing foram configurados no cloud provider para evitar surpresas? [fonte: Financeiro, TI] [impacto: PM, DevOps]
14. A arquitetura suporta a evolução futura prevista (novas fontes, streaming, ML, data mesh)? [fonte: CDO, Diretoria] [impacto: Arquiteto de Dados]
15. O diagrama de arquitetura foi documentado, revisado e aprovado pelo time técnico e pelo patrocinador? [fonte: TI, Diretoria] [impacto: PM, Arquiteto de Dados, Dev]

---

## Etapa 06 — Setup

- **Provisionamento de infraestrutura**: Criar toda a infraestrutura via IaC (Infrastructure as Code) — Terraform, Pulumi ou CloudFormation — nunca manualmente pelo console. Isso inclui: projeto/account no cloud provider com billing configurado, warehouse/lakehouse com clusters ou serverless configurados, buckets de storage para raw/staging/curated com lifecycle policies, service accounts com least-privilege, e networking (VPC, subnets, firewall rules se aplicável). Infraestrutura provisionada manualmente é impossível de reproduzir, auditar ou destruir com segurança — e invariavelmente diverge entre ambientes.

- **Configuração do orquestrador**: Instalar e configurar o orquestrador de pipelines com: ambientes separados (dev, staging, prod), conexões com todas as fontes de dados e destinos configuradas via variáveis de ambiente, pools de workers dimensionados para o volume esperado, alertas de falha configurados (Slack, e-mail, PagerDuty), e acesso do time de engenharia com roles adequados. Para Airflow managed (Composer, MWAA), ativar as configurações de auto-scaling e definir limites de custo. Testar o orquestrador com um DAG trivial end-to-end antes de começar os pipelines reais.

- **Setup do repositório e CI/CD**: Organizar o repositório com separação clara entre: pipelines de ingestão, modelos dbt (staging, intermediate, marts), testes, seeds, macros, e configurações. Configurar o CI/CD para que cada PR rode: linting (sqlfluff para SQL, ruff para Python), compilação do dbt (dbt compile), testes unitários, e opcionalmente build contra ambiente de staging. Cada merge para main dispara deploy automático dos modelos dbt e dos DAGs de orquestração para o ambiente de produção. Sem CI/CD, mudanças em pipelines são feitas diretamente em produção — receita para incidentes.

- **Conectores de fontes de dados**: Configurar e testar a conectividade com cada fonte de dados do MVP — credenciais, endpoints, rate limits, e timeouts. Para bancos de dados, configurar conexões JDBC/ODBC com read replicas (nunca ler de produção primária). Para APIs de SaaS, configurar tokens OAuth com escopos mínimos necessários. Para arquivos, configurar acesso ao storage (S3, GCS, SFTP) com credenciais rotacionáveis. Testar cada conector com uma extração trivial (SELECT * LIMIT 10 ou GET /endpoint?limit=1) para confirmar conectividade antes de construir os pipelines reais.

- **Ambientes isolados**: Configurar pelo menos três ambientes completamente isolados — desenvolvimento (dados de amostra ou mock, custo mínimo), staging (dados reais ou anonimizados, configuração idêntica à produção), e produção (dados reais, acesso restrito). O isolamento deve cobrir: datasets/schemas separados no warehouse, buckets de storage distintos, variáveis de ambiente separadas, e credenciais diferentes. Engenheiros de dados devem conseguir rodar pipelines completos em dev sem afetar produção — se isso não é possível, o setup está incompleto.

- **Configuração de alertas e monitoramento**: Configurar alertas desde o setup — não esperar o go-live. Alertas obrigatórios: falha de DAG/task no orquestrador, query de ingestão com zero registros quando deveria ter dados, custo diário de compute excedendo threshold, e latência de pipeline excedendo SLA definido. Configurar dashboards operacionais no Grafana, Datadog ou na ferramenta nativa do cloud provider mostrando: status dos pipelines, volume de dados processado, custo acumulado, e latência de queries. O time de operação deve poder diagnosticar problemas olhando dashboards, não logs.

### Perguntas

1. Toda a infraestrutura foi provisionada via IaC (Terraform/Pulumi) e o código está versionado no repositório? [fonte: DevOps, TI] [impacto: DevOps, Engenheiro de Dados]
2. O orquestrador está configurado com ambientes separados, conexões com fontes e alertas de falha? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
3. O repositório está organizado com separação clara entre ingestão, transformação, testes e configurações? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
4. O CI/CD está configurado com linting, compilação dbt e testes rodando em cada PR antes do merge? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, Dev]
5. Todos os conectores com fontes de dados do MVP foram testados com extração trivial confirmando conectividade? [fonte: TI, Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
6. Os ambientes dev/staging/prod estão completamente isolados em dados, credenciais e billing? [fonte: DevOps, TI] [impacto: DevOps, Engenheiro de Dados]
7. As credenciais e secrets estão em secret manager (AWS Secrets Manager, GCP Secret Manager, Vault) e nunca hardcoded? [fonte: Segurança, DevOps] [impacto: DevOps, Engenheiro de Dados]
8. O warehouse/lakehouse está configurado com os datasets/schemas para raw, staging e curated definidos na arquitetura? [fonte: Engenheiro de Dados, Arquiteto de Dados] [impacto: Engenheiro de Dados]
9. Os alertas de falha de pipeline, custo excessivo e SLA breach estão configurados e testados? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, PM]
10. O acesso do time de engenharia foi configurado com roles adequados (admin vs. editor vs. viewer) em cada ferramenta? [fonte: TI, Segurança] [impacto: DevOps, Engenheiro de Dados]
11. O dbt project foi inicializado com profiles configurados para cada ambiente e o primeiro modelo compila com sucesso? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados]
12. O dashboard operacional está configurado mostrando status de pipelines, volume processado e custo acumulado? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, PM]
13. O processo de onboarding de novos engenheiros foi documentado com instruções de setup local e acesso? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
14. Os limites de billing e alertas de custo estão configurados no cloud provider com thresholds aprovados pelo financeiro? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
15. O pipeline de CI/CD foi testado com um PR real — linting passou, dbt compilou, testes passaram, deploy completou? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, Dev]

---

## Etapa 07 — Build

- **Pipelines de ingestão**: Implementar cada pipeline de extração conforme documentado na Definition — método de extração (full, incremental, CDC), frequência, tratamento de erros e retries, e destino na camada raw. Cada pipeline deve ser idempotente (re-executar não duplica dados), observável (logs estruturados com contagem de registros extraídos, duração, e status), e resiliente (retry automático com backoff exponencial para falhas transientes, alerta para falhas persistentes). Pipelines devem ser desenvolvidos e testados em ambiente de dev com dados de amostra antes de apontar para fontes de produção.

- **Camada de transformação (dbt models)**: Implementar os modelos dbt em três camadas: staging (limpeza mínima e tipagem — uma staging model por fonte), intermediate (joins entre fontes, business logic, deduplicação), e marts (tabelas finais otimizadas para consumo — fatos e dimensões prontas para BI). Cada modelo deve ter: documentação inline (description em schema.yml), testes de integridade (unique, not_null, accepted_values, relationships), e tags para execução seletiva. O padrão de nomenclatura deve ser consistente: stg_fonte__entidade, int_processo__resultado, fct_metrica, dim_entidade.

- **Carga histórica (backfill)**: Executar a carga inicial de dados históricos — frequentemente o maior esforço do build. Para fontes com anos de histórico e milhões de registros, a carga precisa ser feita em batches para não sobrecarregar a fonte nem estourar o custo de compute no warehouse. Definir com antecedência: quantos anos de histórico serão carregados, se a carga será feita em paralelo por períodos (mês a mês, ano a ano), e qual o deadline. Testar a reconciliação de totais entre fonte e destino após a carga completa — se o total de vendas no warehouse diverge do total no ERP, a plataforma nasce desacreditada.

- **Dashboards e camada de consumo**: Implementar os dashboards e relatórios definidos no MVP — conectando a ferramenta de BI ao warehouse, configurando a semantic layer quando aplicável, e construindo as visualizações com filtros, drill-downs e formatação acordados com os consumidores. Cada dashboard deve ser validado com dados reais (não mock) e com o stakeholder que vai usá-lo no dia a dia. Dashboards construídos sem validação com o consumidor final frequentemente mostram os dados certos no formato errado — e são abandonados em favor de planilhas.

- **Testes de dados automatizados**: Implementar testes automatizados em cada camada do pipeline usando dbt tests, Great Expectations ou Soda. Testes mínimos obrigatórios: unique e not_null em chaves primárias, relationships entre fatos e dimensões (FK integrity), accepted_values para campos com domínio fechado (status, tipo, categoria), e reconciliação de totais (soma de vendas na staging = soma de vendas na mart). Testes devem rodar automaticamente a cada execução do pipeline e falhas devem gerar alertas antes que dados incorretos cheguem ao dashboard.

- **Documentação e catálogo**: Popular o catálogo de dados com: descrições de tabelas e campos (herdadas do dbt docs quando possível), linhagem visual end-to-end, tags de classificação (PII, financeiro, público), e ownership (qual time é responsável por cada dataset). A documentação deve ser tratada como código — versionada, revisada em PR, e atualizada junto com cada mudança de modelo. Documentação feita "depois" nunca é feita — ou se é feita, está desatualizada no dia seguinte.

### Perguntas

1. Todos os pipelines de ingestão do MVP estão implementados, idempotentes e com retry automático? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
2. Os modelos dbt estão organizados em staging/intermediate/marts com nomenclatura consistente e documentação inline? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
3. A carga histórica foi executada e os totais reconciliam com os sistemas-fonte dentro da margem aceitável? [fonte: Engenheiro de Dados, Áreas de negócio] [impacto: Engenheiro de Dados, QA]
4. Os dashboards do MVP foram implementados e validados com os consumidores finais usando dados reais? [fonte: Áreas de negócio] [impacto: Dev, PM]
5. Os testes de dados automatizados (unique, not_null, relationships, reconciliação) estão implementados e passando? [fonte: Engenheiro de Dados, QA] [impacto: Engenheiro de Dados, QA]
6. O catálogo de dados está populado com descrições, linhagem, tags de classificação e ownership? [fonte: Engenheiro de Dados, CDO] [impacto: Engenheiro de Dados, Arquiteto de Dados]
7. As regras de mascaramento e anonimização estão implementadas e verificadas para dados sensíveis? [fonte: Segurança, Compliance] [impacto: Segurança, Engenheiro de Dados]
8. O controle de acesso (RBAC, row-level, column-level) está implementado e testado com cada perfil de usuário? [fonte: Segurança, TI] [impacto: Segurança, Engenheiro de Dados]
9. Os pipelines estão sendo executados em staging com dados reais e respeitando os SLAs de freshness definidos? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
10. As slowly changing dimensions estão implementadas com a estratégia correta (SCD tipo 1, 2 ou 3) por dimensão? [fonte: Engenheiro de Dados, Arquiteto de Dados] [impacto: Engenheiro de Dados]
11. A semantic layer está configurada e as métricas são consumidas de forma consistente entre dashboards? [fonte: Engenheiro de Dados, Áreas de negócio] [impacto: Dev, Engenheiro de Dados]
12. Os DAGs de orquestração estão configurados com dependências corretas, timeouts e alertas de falha? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
13. O progresso da implementação de pipelines está dentro do cronograma e sem bloqueadores de acesso a fontes? [fonte: PM, Engenheiro de Dados] [impacto: PM, Dev]
14. A documentação técnica (runbooks, diagramas, decisões de arquitetura) está atualizada no repositório? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, Dev]
15. A performance de queries dos dashboards é aceitável (tempo de resposta < 10s para queries interativas)? [fonte: Áreas de negócio, Engenheiro de Dados] [impacto: Dev, Engenheiro de Dados]

---

## Etapa 08 — QA

- **Reconciliação de dados end-to-end**: Comparar métricas calculadas na plataforma com os valores conhecidos dos sistemas-fonte para cada caso de uso do MVP. Exemplo: total de vendas do mês no dashboard deve bater com o relatório do ERP, número de clientes ativos deve bater com o CRM. Divergências são esperadas quando há diferenças de regra (ex.: o ERP inclui devoluções, o dashboard filtra) — mas devem ser documentadas e aprovadas pelo negócio. Reconciliação sem a participação do dono da métrica é inútil — o engenheiro não sabe se o número está certo, só o negócio sabe.

- **Testes de performance e escalabilidade**: Simular o volume de queries esperado em horário de pico — se 30 analistas abrem o Power BI às 8h da manhã e cada um roda 5 queries, o warehouse precisa suportar 150 queries concorrentes sem degradação. Testar com volumes de dados projetados para 6-12 meses à frente para identificar gargalos antes que apareçam em produção. Em warehouses com pricing por query (BigQuery), testar também o custo por query — uma query mal otimizada que faz full scan em tabela de 1TB pode custar dezenas de dólares.

- **Validação de controles de segurança**: Testar cada controle de acesso com login de cada perfil de usuário — analista de vendas não deve ver dados de RH, gerente regional deve ver apenas dados da sua região (row-level security), campos de PII devem estar mascarados para perfis sem privilégio. Testar também cenários negativos: tentar acessar dados proibidos via SQL direto, tentar escalar privilégio, tentar exportar dados sensíveis. Em ambientes regulados, documentar os resultados dos testes de segurança como evidência para auditoria.

- **Teste de resiliência de pipelines**: Simular falhas comuns e verificar que os pipelines se recuperam corretamente: fonte de dados indisponível (o pipeline deve retry e alertar, não falhar silenciosamente), dados com schema inesperado (coluna nova ou removida na fonte — o pipeline deve detectar e alertar), volume de dados anormal (10x mais registros que o esperado — o pipeline deve processar sem OOM ou timeout), e re-execução após falha (idempotência — re-executar não duplica dados).

- **Validação de SLAs de dados**: Verificar que cada SLA definido no Alignment está sendo cumprido em staging — freshness (dados chegam no horário acordado), completeness (percentual de registros completos acima do threshold), accuracy (métricas batem com fonte de verdade), e availability (ambiente de queries disponível nos horários de uso). Registrar os resultados como baseline — serão usados para monitoramento contínuo em produção.

- **Teste de disaster recovery**: Simular cenário de perda de dados ou indisponibilidade e verificar que o plano de DR funciona — restore de backup dentro do RTO definido, failover para região secundária se aplicável, e re-processamento de pipelines a partir de um ponto no tempo (replay). Em plataformas baseadas em formatos open table (Delta, Iceberg), testar o time travel para recuperar dados de versões anteriores. DR não testado é DR que não funciona.

### Perguntas

1. A reconciliação de métricas entre a plataforma e os sistemas-fonte foi validada e aprovada pelos donos das métricas? [fonte: Áreas de negócio, Financeiro] [impacto: Engenheiro de Dados, QA]
2. Os testes de performance com volume projetado para 6-12 meses foram executados e o tempo de resposta é aceitável? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
3. Os controles de segurança foram testados com cada perfil de usuário, incluindo cenários negativos? [fonte: Segurança, Compliance] [impacto: Segurança, Engenheiro de Dados]
4. Os pipelines foram testados contra falhas comuns (fonte indisponível, schema change, volume anormal) e se recuperam corretamente? [fonte: Engenheiro de Dados, QA] [impacto: Engenheiro de Dados, DevOps]
5. Todos os SLAs de dados (freshness, completeness, accuracy, availability) estão sendo cumpridos em staging? [fonte: Engenheiro de Dados, Áreas de negócio] [impacto: Engenheiro de Dados, PM]
6. O teste de disaster recovery foi executado e o restore completou dentro do RTO definido? [fonte: DevOps, TI] [impacto: DevOps, Engenheiro de Dados]
7. Os dashboards foram validados pelos consumidores finais com dados reais em sessão de aceite? [fonte: Áreas de negócio] [impacto: Dev, PM]
8. Os testes automatizados de dados rodam a cada execução de pipeline e falhas geram alertas antes de afetar dashboards? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, QA]
9. A linhagem de dados está visível no catálogo e foi validada para as métricas críticas? [fonte: CDO, Engenheiro de Dados] [impacto: Engenheiro de Dados, Arquiteto de Dados]
10. O custo de queries em produção foi projetado com base nos testes de staging e está dentro do orçamento? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
11. A documentação de runbooks (como reagir a falha de pipeline, como re-executar carga) está completa e testada? [fonte: Engenheiro de Dados] [impacto: Engenheiro de Dados, DevOps]
12. Os alertas de monitoramento foram testados — falha simulada gerou notificação no canal correto? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps]
13. O glossário de termos de negócio foi revisado com os consumidores e está acessível no catálogo? [fonte: CDO, Áreas de negócio] [impacto: PM, Engenheiro de Dados]
14. A performance dos dashboards em horário de pico simulado é aceitável (< 10s para queries interativas)? [fonte: Áreas de negócio, Engenheiro de Dados] [impacto: Dev, Engenheiro de Dados]
15. O aceite formal dos casos de uso do MVP foi obtido de cada stakeholder consumidor? [fonte: Áreas de negócio, Diretoria] [impacto: PM]

---

## Etapa 09 — Launch Prep

- **Plano de cutover de pipelines**: Documentar a sequência exata de ações para ativar os pipelines de produção — quem habilita cada DAG, em qual ordem, e como validar que a primeira execução completou com sucesso. Se a plataforma substitui processos existentes (relatórios em planilha, queries diretas no banco transacional), definir o período de execução paralela onde ambos os sistemas produzem resultados para comparação. Não desligar o processo antigo até que o novo esteja produzindo resultados validados por pelo menos 2 semanas — migração big-bang de dados é receita para crise.

- **Treinamento dos consumidores de dados**: Realizar sessões de treinamento segmentadas por perfil: analistas de negócio (como usar a ferramenta de BI, onde encontrar os dados, como interpretar as métricas), gerentes (como acessar dashboards, como exportar relatórios), e time de operação (como monitorar pipelines, como reagir a alertas, como escalar incidentes). Entregar documentação em formato simples com capturas de tela e exemplos práticos. Um treinamento presencial sem documentação escrita é esquecido em duas semanas — e gerar tickets de suporte por falta de documentação consome mais tempo do que produzi-la.

- **Configuração de alertas de produção**: Revisar e ajustar todos os alertas para o cenário de produção — thresholds de freshness calibrados com horários reais de carga das fontes, alertas de custo com thresholds de produção (não de staging), alertas de volume com baseline de produção, e escalation policy definida (quem é notificado primeiro, quem é o backup, quando escalar para gerente). Alertas com threshold incorreto geram fadiga de alerta (muitos falsos positivos) ou cegueira (não alertam quando deveriam).

- **Documentação operacional (runbooks)**: Produzir runbooks para cada cenário operacional previsível: pipeline falhou por timeout → como re-executar, fonte de dados indisponível → como bypass temporário, custo diário excedeu threshold → como identificar query/job responsável e otimizar, novo usuário precisa de acesso → como provisionar. Runbooks devem ser testados pelo time de operação antes do go-live — se o operador não consegue seguir o runbook com sucesso, o runbook está incompleto.

- **Período de paralelo (dual-run)**: Se a plataforma substitui processos existentes, configurar um período de execução paralela onde o processo antigo e o novo rodam simultaneamente e os resultados são comparados diariamente. O período típico é de 1 a 4 semanas dependendo da complexidade. Divergências entre os sistemas devem ser investigadas e resolvidas — frequentemente revelam bugs tanto no novo quanto no antigo. O processo antigo só deve ser desligado após aprovação formal do dono da métrica confirmando que o novo é confiável.

- **Rollback e contingência**: Documentar o plano de rollback — se os dados em produção apresentam problemas graves nas primeiras semanas, qual a sequência de ações? Manter pipelines e relatórios antigos funcionais durante o período de paralelo. Definir critérios claros de quando acionar rollback (divergência de métricas > 5%, pipeline falhando por > 24h, custo de compute 3x acima do projetado) e quem tem autoridade para tomar a decisão.

### Perguntas

1. O plano de cutover está documentado com sequência exata de ações, responsáveis e critérios de validação? [fonte: Engenheiro de Dados, PM] [impacto: Engenheiro de Dados, DevOps, PM]
2. O treinamento dos consumidores de dados foi realizado por perfil e a documentação de uso foi entregue? [fonte: Áreas de negócio, PM] [impacto: PM, Dev]
3. Os alertas de produção estão calibrados com thresholds de produção e escalation policy definida? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, Engenheiro de Dados]
4. Os runbooks operacionais foram produzidos, testados pelo time de operação e validados? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps, Engenheiro de Dados]
5. O período de dual-run foi configurado com comparação diária de resultados entre sistema antigo e novo? [fonte: Áreas de negócio, Engenheiro de Dados] [impacto: Engenheiro de Dados, QA, PM]
6. O plano de rollback está documentado com critérios claros de acionamento e responsável designado? [fonte: TI, Diretoria] [impacto: PM, DevOps, Engenheiro de Dados]
7. Os processos antigos (planilhas, queries diretas) estão mantidos funcionais durante o período de paralelo? [fonte: TI, Áreas de negócio] [impacto: PM, Engenheiro de Dados]
8. O acesso de produção foi configurado para cada perfil de consumidor com permissões corretas? [fonte: Segurança, TI] [impacto: Segurança, Engenheiro de Dados]
9. Os limites de custo de produção estão configurados com alertas automáticos e processo de resposta definido? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
10. O monitoramento de SLAs de dados está configurado com dashboard visível para o time de operação? [fonte: Engenheiro de Dados, DevOps] [impacto: DevOps, PM]
11. Todos os stakeholders foram notificados sobre a data de início do período de paralelo e do go-live definitivo? [fonte: Diretoria, PM] [impacto: PM]
12. A lista de acessos a serem entregues ao cliente foi revisada e todos os acessos foram testados e funcionam? [fonte: DevOps, Engenheiro de Dados] [impacto: PM]
13. O suporte pós-lançamento (canal, SLA, responsável) foi definido e comunicado aos consumidores? [fonte: Diretoria, PM] [impacto: PM, DevOps]
14. A janela de cutover foi escolhida estrategicamente (início de semana, com time de suporte disponível por vários dias)? [fonte: PM, TI] [impacto: PM, DevOps]
15. O catálogo de dados está acessível aos consumidores com busca, linhagem e glossário funcionando? [fonte: CDO, Engenheiro de Dados] [impacto: Engenheiro de Dados, PM]

---

## Etapa 10 — Go-Live

- **Ativação de pipelines de produção e monitoramento**: Executar a ativação dos pipelines conforme o plano de cutover — habilitar DAGs na ordem definida, aguardar a primeira execução completa, e validar os resultados antes de liberar o acesso para os consumidores. Monitorar a primeira execução completa de cada pipeline em tempo real — falhas na primeira execução em produção são comuns (credenciais de produção diferentes de staging, volume real maior que o testado, timeouts insuficientes) e precisam ser corrigidas imediatamente.

- **Validação de dados em produção**: Após a primeira carga completa em produção, executar a reconciliação de métricas com os sistemas-fonte — os mesmos testes feitos no QA, agora com dados reais de produção. Envolver os donos das métricas para confirmarem que os números fazem sentido. Liberar acesso aos dashboards para os consumidores somente após esta validação — dar acesso a dashboards com dados potencialmente incorretos destrói a confiança na plataforma de forma difícil de recuperar.

- **Monitoramento da primeira semana**: Monitorar ativamente nos primeiros 7 dias: todas as execuções de pipeline (100% de sucesso é o target), SLAs de freshness (dados disponíveis no horário acordado), custo diário de compute vs. projeção, performance de queries dos consumidores (tempo de resposta aceitável), e volume de tickets de suporte (indicador indireto de qualidade). Se o período de dual-run está ativo, comparar resultados diariamente e documentar divergências para investigação.

- **Coleta de feedback dos consumidores**: Nos primeiros dias após o go-live, coletar feedback estruturado de cada perfil de consumidor: os dados estão corretos? os dashboards são úteis? a ferramenta de BI é fácil de usar? faltam filtros ou métricas? o glossário está claro? Este feedback é essencial para priorizar a evolução da plataforma — e para identificar gaps que não apareceram nas sessões de validação do QA. Agendar sessões curtas (30 min) com cada grupo na primeira semana.

- **Descomissionamento do processo antigo**: Após o período de dual-run e a aprovação formal dos donos das métricas, desligar os processos antigos (planilhas manuais, queries diretas no banco transacional, relatórios legados). O descomissionamento deve ser comunicado com antecedência, documentado, e reversível por pelo menos mais uma semana. Muitas organizações mantêm processos antigos rodando indefinidamente "por precaução" — o que gera confusão, custo desnecessário e desconfiança nos dados novos. O desligamento formal é sinal de confiança e de encerramento do projeto.

- **Entrega e handoff ao cliente**: Entregar formalmente todos os acessos e artefatos: acesso ao repositório com código de pipelines e modelos dbt, acesso ao cloud provider com permissões de operação (não de billing), acesso ao orquestrador com roles adequados, acesso ao catálogo de dados, acesso às ferramentas de BI com dashboards publicados, documentação operacional (runbooks, arquitetura, decisões técnicas), e contato de suporte com SLA definido. A documentação mínima deve incluir: como monitorar a plataforma, como reagir a alertas, como adicionar novos pipelines, e como solicitar suporte.

### Perguntas

1. Todos os pipelines de produção foram ativados e a primeira execução completa validada com sucesso? [fonte: Engenheiro de Dados, DevOps] [impacto: Engenheiro de Dados, DevOps]
2. A reconciliação de métricas em produção foi validada e aprovada pelos donos das métricas? [fonte: Áreas de negócio, Financeiro] [impacto: Engenheiro de Dados, PM]
3. O acesso aos dashboards foi liberado para os consumidores somente após validação dos dados? [fonte: PM, Áreas de negócio] [impacto: PM, Dev]
4. O custo de operação do primeiro dia/semana está dentro da projeção aprovada pelo financeiro? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
5. O monitoramento de SLAs e pipelines está ativo e gerando alertas quando há desvios? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, Engenheiro de Dados]
6. O feedback estruturado dos consumidores foi coletado na primeira semana e os gaps prioritários identificados? [fonte: Áreas de negócio] [impacto: PM, Dev]
7. O período de dual-run está ativo e a comparação diária de resultados não apresenta divergências não explicadas? [fonte: Engenheiro de Dados, Áreas de negócio] [impacto: Engenheiro de Dados, QA]
8. Os runbooks foram utilizados em pelo menos um incidente real ou simulado e se mostraram eficazes? [fonte: DevOps, Engenheiro de Dados] [impacto: DevOps, Engenheiro de Dados]
9. O descomissionamento dos processos antigos foi agendado com data e aprovação formal dos donos das métricas? [fonte: Áreas de negócio, Diretoria] [impacto: PM, Engenheiro de Dados]
10. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou que consegue acessar? [fonte: DevOps, Engenheiro de Dados] [impacto: PM]
11. O aceite formal de entrega foi obtido do patrocinador (e-mail, assinatura de ata, ou confirmação documentada)? [fonte: Diretoria] [impacto: PM]
12. O plano de suporte pós-lançamento foi ativado com canal de comunicação e SLA comunicado ao time de operação? [fonte: Diretoria, PM] [impacto: PM, DevOps]
13. A documentação operacional completa (runbooks, arquitetura, glossário, catálogo) foi entregue e revisada? [fonte: Engenheiro de Dados] [impacto: PM, Engenheiro de Dados]
14. O plano de evolução (próximas fontes, próximos casos de uso, roadmap) foi documentado e priorizado? [fonte: CDO, Diretoria, Áreas de negócio] [impacto: PM, Arquiteto de Dados]
15. Os processos antigos foram desligados formalmente após aprovação ou há data definida para descomissionamento? [fonte: TI, Áreas de negócio, Diretoria] [impacto: PM, Engenheiro de Dados]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos um dashboard, não uma plataforma de dados"** — O cliente descreve o resultado final (dashboard) sem entender que antes é necessária toda a infraestrutura de ingestão, transformação e governança. Se a expectativa é "conectar o Power BI direto no banco e pronto", o projeto não é plataforma de dados — é um relatório de BI. Alinhar que o dashboard é a ponta visível de uma cadeia completa de dados.
- **"Já temos tudo no Excel, é só automatizar"** — Planilhas com lógica de negócio embutida em fórmulas complexas, macros e dados manuais não são "fontes de dados" — são processos informais. Migrar de Excel para warehouse exige reengenharia das regras de negócio, não automação do processo existente. O esforço é frequentemente subestimado em 5-10x.
- **"Todos os departamentos precisam dos dados"** — Escopo sem priorização. Se todos os departamentos são MVP, o projeto leva 18 meses em vez de 3. Definir 3-5 casos de uso prioritários e um departamento piloto é obrigatório para viabilizar o prazo.

### Etapa 02 — Discovery

- **"Todas as nossas fontes têm API"** — Raramente verdade. ERPs legados frequentemente exigem acesso direto ao banco (JDBC), sistemas SaaS podem ter rate limits severos, e muitas "fontes" são planilhas em e-mail ou SharePoint. Validar o método real de acesso de cada fonte antes de estimar o esforço de ingestão.
- **"A qualidade dos dados é boa"** — Resposta otimista até que alguém olhe de verdade. Campos nulos, duplicações, formatos inconsistentes e dados orphaned são encontrados em 100% dos projetos de plataforma de dados. Planejar um esforço de data quality desde o Discovery, não como surpresa durante o Build.
- **"Não precisamos de governança, só de dados"** — Dados sem governança são dados sem confiança. Se ninguém define o que "cliente ativo" significa, dois dashboards vão mostrar números diferentes e ambos estarão "certos" segundo regras diferentes. Governança mínima (glossário + data owners) é obrigatória, não opcional.

### Etapa 03 — Alignment

- **"O orçamento de cloud é ilimitado"** — Não existe orçamento ilimitado. Se o financeiro não aprovou uma projeção de custo, a plataforma será desligada quando a fatura chegar. Obter aprovação de custo com cenários projetados é gate obrigatório desta etapa.
- **"O time de TI vai operar"** — Operar plataforma de dados exige skills específicos (SQL avançado, Airflow, dbt, cloud) que times de TI generalistas frequentemente não possuem. Se não há engenheiro de dados no time de operação, a plataforma vai degradar em semanas. Validar competências reais, não apenas boa vontade.
- **"Pode ser qualquer ferramenta de BI"** — A escolha da ferramenta de BI impacta diretamente os consumidores finais que vão usá-la diariamente. Analistas acostumados com Excel vão resistir a Looker. Times já investidos em Power BI não vão migrar para Metabase. Envolver os consumidores na escolha é obrigatório.

### Etapa 04 — Definition

- **Métricas definidas "de cabeça"** — "Ticket médio é vendas dividido por pedidos" parece simples até que se descubra que há 5 tipos de pedido, 3 status possíveis, e a divisão pode ser por pedidos faturados ou por pedidos criados. Métricas sem especificação formal (fórmula, filtros, granularidade) resultam em dashboards desacreditados.
- **"O modelo de dados é flexível, a gente ajusta depois"** — Mudar o modelo dimensional depois que há dados carregados e dashboards conectados é extremamente custoso. Cada mudança de granularidade exige recarga histórica, e cada mudança de dimensão exige rebuild de dashboards. Definir e aprovar o modelo antes do build é gate obrigatório.
- **"Não precisa de dicionário de dados"** — Sem dicionário, cada engenheiro interpreta campos à sua maneira. "valor" é bruto ou líquido? "data_criacao" é fuso UTC ou local? Dicionário de dados é documentação obrigatória, não nice-to-have.

### Etapa 05 — Architecture

- **"Vamos usar Databricks porque é o melhor"** — Escolha de stack por hype, não por adequação. Se o caso de uso é um warehouse simples com 5 fontes e dashboards de BI, BigQuery ou Snowflake resolve com menos complexidade e custo. Databricks brilha quando há workloads mistos de SQL e ML — não para todo projeto.
- **"Vamos colocar tudo na mesma conta/projeto"** — Ambientes dev/staging/prod no mesmo projeto de cloud sem isolamento. Uma query de teste derruba o cluster de produção, ou um engenheiro apaga dados reais achando que estava em dev. Isolamento de ambientes é obrigatório.
- **"Não precisamos de observabilidade, o Airflow já monitora"** — Airflow monitora se o pipeline rodou, não se os dados estão corretos. Pipeline pode executar com sucesso e produzir dados errados. Observabilidade de dados (freshness, volume, distribution) é complementar ao monitoramento de pipeline.

### Etapa 06 — Setup

- **Infraestrutura criada pelo console** — Clicar no console do cloud para criar recursos. Funciona na primeira vez, impossível de reproduzir, auditar ou destruir com segurança. Quando o ambiente de staging precisa ser idêntico ao de produção, não há como garantir sem IaC. Terraform ou Pulumi desde o primeiro recurso.
- **Credenciais em código ou variáveis de ambiente locais** — Tokens de API, passwords de banco e service account keys commitados no repositório ou salvos em .env sem secret manager. Violação de segurança que se torna mais grave à medida que o time cresce e os dados se tornam mais sensíveis.
- **"Vamos começar direto em produção"** — Sem ambiente de dev, cada teste é feito com dados e infraestrutura de produção. Pipeline com bug consome créditos de compute de produção, query de teste sobrecarrega o cluster, e dados de teste poluem tabelas reais. Ambientes isolados são pré-requisito.

### Etapa 07 — Build

- **Transformação em Python quando SQL resolve** — Engenheiros que escrevem transformações em PySpark ou pandas quando a mesma lógica pode ser expressa em SQL via dbt. SQL é mais legível, mais testável, mais documentável e mais performático em warehouses SQL-native. PySpark é justificado apenas para transformações que SQL não suporta (ML, processamento de texto não-estruturado, lógica procedural complexa).
- **Testes de dados deixados para o QA** — "Depois a gente adiciona os testes". Resultado: dados incorretos chegam aos dashboards durante semanas de build e criam falsa sensação de que os dados estão prontos. Testes devem ser implementados junto com cada modelo dbt — não existe model sem test.
- **Carga histórica sem reconciliação** — Carregar 3 anos de histórico sem comparar totais com a fonte. O warehouse nasce com números diferentes do ERP, e a confiança na plataforma é destruída antes do go-live.

### Etapa 08 — QA

- **"Os números parecem certos"** — QA de dados baseado em intuição ("parece razoável") em vez de reconciliação formal com sistemas-fonte. Números "que parecem certos" frequentemente têm divergências de 5-15% que só são descobertas quando o CFO compara com o relatório do ERP.
- **QA apenas com dados de staging** — Dados de staging podem ter volume, distribuição e edge cases diferentes de produção. Se o QA não inclui testes com dados reais (ao menos anonimizados), problemas de performance e de regras de negócio passam despercebidos.
- **Segurança testada apenas com perfil admin** — Admin vê tudo, então tudo "funciona". Os problemas aparecem quando o analista de vendas tenta acessar dados de RH, ou quando o gerente regional vê dados de todas as regiões em vez de apenas a sua. Testar com cada perfil real é obrigatório.

### Etapa 09 — Launch Prep

- **"Liga os pipelines e pronto"** — Sem período de dual-run, sem comparação com processo antigo, sem validação com donos das métricas. Se o dashboard novo mostra um número diferente do Excel antigo no primeiro dia, a confiança é destruída. Dual-run de 2-4 semanas é obrigatório quando há processo existente sendo substituído.
- **Treinamento apenas para o time técnico** — O engenheiro de dados recebe treinamento, mas os analistas de negócio que vão usar os dashboards diariamente não. Resultado: dashboards subutilizados e retorno ao Excel em semanas.
- **Sem plano de rollback** — "Se der problema a gente corrige." Corrigir dados incorretos em produção sob pressão é receita para piorar o problema. Plano de rollback com processos antigos mantidos funcionais é obrigatório.

### Etapa 10 — Go-Live

- **Go-live sem validação de dados em produção** — Liberar acesso aos dashboards antes de confirmar que os dados em produção estão corretos. Consumidores veem números errados no primeiro acesso e perdem confiança na plataforma permanentemente.
- **Desligar processo antigo no dia do go-live** — Sem período de transição, sem comparação, sem fallback. Se algo dá errado, não há como voltar. Manter processos antigos por pelo menos 2-4 semanas é seguro e barato comparado ao risco.
- **"A plataforma está no ar, projeto encerrado"** — Sem monitoramento na primeira semana, sem coleta de feedback, sem ajuste de alertas. Pipelines falham silenciosamente, custo de compute estoura, e consumidores abandonam a plataforma por falta de suporte.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é data platform** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Precisamos de um relatório no Power BI conectado direto no banco" | Relatório de BI, não plataforma de dados | Reclassificar para projeto de BI/reporting simples |
| "Queremos um sistema para os vendedores registrarem pedidos" | Sistema transacional (CRUD) | Reclassificar para web-app ou ERP |
| "Precisamos de uma API para nosso app consumir dados" | Backend API, não plataforma analítica | Reclassificar para web-app com API |
| "Queremos automatizar o envio de e-mails baseado em dados" | Marketing automation | Reclassificar para integração/automação |
| "Precisamos processar pagamentos e gerar notas fiscais" | Sistema transacional/financeiro | Reclassificar para ERP ou fintech |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos quais métricas queremos acompanhar" | 01 | Plataforma sem propósito — ninguém sabe o que medir | Realizar workshop de definição de KPIs antes de avançar |
| "O orçamento é só para o desenvolvimento, cloud a gente vê depois" | 01 | Plataforma desligada quando a fatura de cloud chegar | Apresentar projeção de custo mensal e obter aprovação antes de continuar |
| "Não temos acesso ao banco de produção do ERP" | 02 | Pipeline de ingestão bloqueado na fonte mais crítica | Resolver acesso com TI e fornecedor do ERP antes da Etapa 06 |
| "Cada departamento define suas próprias métricas" | 02 | Métricas conflitantes — dashboard desacreditado desde o dia 1 | Alinhar definições únicas com todos os departamentos antes de modelar |
| "Não temos engenheiro de dados no time" | 03 | Ninguém para operar a plataforma após o go-live | Contratar ou terceirizar operação antes de avançar |
| "Não podemos compartilhar dados entre departamentos" | 03 | Plataforma centralizada inviável se dados não podem ser cruzados | Resolver com compliance/jurídico ou reduzir escopo para um único departamento |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Nossos dados estão espalhados em 15 sistemas diferentes" | 02 | Esforço de ingestão muito maior que o estimado | Priorizar 3-5 fontes para o MVP e planejar fases |
| "A gente nunca usou ferramenta de BI" | 02 | Adoção baixa — investimento desperdiçado | Planejar treinamento reforçado e escolher ferramenta mais intuitiva |
| "O ERP é de 2005 e não tem API" | 02 | Ingestão via queries diretas no banco legado — frágil e lento | Planejar conector CDC ou replicação, não queries diretas em produção |
| "Precisamos de dados em tempo real" | 01 | Complexidade e custo 3-5x maior que batch | Validar se near-real-time ou batch horário resolve antes de desenhar streaming |
| "Cada filial tem seu próprio banco de dados" | 02 | Múltiplas instâncias com schemas potencialmente diferentes | Mapear diferenças de schema entre filiais antes de modelar |
| "A aprovação de acesso a dados passa por 3 comitês" | 03 | Onboarding de consumidores vai levar semanas, não dias | Documentar processo e antecipar solicitações de acesso |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Gatilho da demanda identificado e casos de uso iniciais listados (pergunta 1)
- Consumidores de dados identificados com suas necessidades específicas (pergunta 2)
- Orçamento de desenvolvimento e operação mensal em cloud aprovado (pergunta 7)
- Prazo do primeiro caso de uso com justificativa de negócio (pergunta 8)
- Cloud provider definido ou shortlist aprovada (pergunta 13)

### Etapa 02 → 03

- Inventário de fontes de dados do MVP completo com método de acesso validado (pergunta 1)
- Casos de uso prioritários ordenados por valor e viabilidade (pergunta 2)
- Requisitos de segurança e compliance mapeados (perguntas 6 e 10)
- Perfis de consumo e ferramentas de BI identificados (perguntas 5 e 9)

### Etapa 03 → 04

- Modelo de governança definido com data owners nomeados (pergunta 1)
- Escopo do MVP documentado e aprovado por todos os stakeholders (pergunta 2)
- Projeção de custo mensal aprovada pelo financeiro (pergunta 3)
- Time de operação pós-lançamento definido e com capacidade confirmada (pergunta 4)

### Etapa 04 → 05

- Modelo dimensional definido com granularidade aprovada (pergunta 1)
- Métricas e KPIs especificados com fórmula, granularidade e filtros (pergunta 5)
- Dicionário de dados e glossário de negócio produzidos e validados (perguntas 3 e 4)
- Estratégia de testes de dados definida por camada (pergunta 6)
- Documentação aprovada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- Warehouse/lakehouse, orquestrador e camada de transformação escolhidos e justificados (perguntas 1, 2 e 3)
- Arquitetura de segurança definida e aprovada por compliance (pergunta 6)
- Custos mensais calculados em três cenários e aprovados (pergunta 9)
- Diagrama de arquitetura documentado e aprovado (pergunta 15)

### Etapa 06 → 07

- Infraestrutura provisionada via IaC e versionada (pergunta 1)
- Conectores com fontes de dados testados com sucesso (pergunta 5)
- Ambientes dev/staging/prod isolados (pergunta 6)
- CI/CD testado com PR real (pergunta 15)

### Etapa 07 → 08

- Todos os pipelines de ingestão implementados e idempotentes (pergunta 1)
- Carga histórica executada e reconciliada (pergunta 3)
- Dashboards implementados e validados com consumidores (pergunta 4)
- Testes de dados automatizados implementados e passando (pergunta 5)

### Etapa 08 → 09

- Reconciliação de métricas aprovada pelos donos (pergunta 1)
- Controles de segurança testados com cada perfil (pergunta 3)
- SLAs de dados cumpridos em staging (pergunta 5)
- Aceite formal dos casos de uso do MVP obtido (pergunta 15)

### Etapa 09 → 10

- Plano de cutover documentado e aprovado (pergunta 1)
- Treinamento dos consumidores realizado e documentação entregue (pergunta 2)
- Runbooks testados pelo time de operação (pergunta 4)
- Plano de rollback documentado com critérios de acionamento (pergunta 6)

### Etapa 10 → Encerramento

- Pipelines de produção ativados e primeira execução validada (pergunta 1)
- Reconciliação de dados em produção aprovada pelos donos das métricas (pergunta 2)
- Todos os acessos entregues e aceite formal obtido (perguntas 10 e 11)
- Plano de evolução documentado e priorizado (pergunta 14)
- Processos antigos desligados ou com data definida de descomissionamento (pergunta 15)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de plataforma de dados. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 DW Centralizado | V2 Lakehouse | V3 Data Mesh | V4 Self-Service | V5 Streaming |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 4 | 2 | 3 |
| 02 Discovery | 3 | 4 | 5 | 3 | 4 |
| 03 Alignment | 3 | 3 | 5 | 3 | 3 |
| 04 Definition | 4 | 4 | 5 | 3 | 4 |
| 05 Architecture | 3 | 4 | 5 | 3 | 5 |
| 06 Setup | 3 | 4 | 4 | 2 | 4 |
| 07 Build | 4 | 5 | 4 | 3 | 5 |
| 08 QA | 3 | 4 | 4 | 3 | 4 |
| 09 Launch Prep | 3 | 3 | 4 | 2 | 3 |
| 10 Go-Live | 2 | 3 | 3 | 2 | 3 |
| **Total relativo** | **30** | **37** | **43** | **26** | **38** |

**Observações por variante:**

- **V1 DW Centralizado**: Esforço concentrado na Definition (modelo dimensional) e no Build (pipelines de ingestão e transformação). Complexidade moderada porque as fontes são tipicamente estruturadas e o padrão de consumo é BI tradicional.
- **V2 Lakehouse**: Mais pesado que DW por lidar com dados semi-estruturados, formatos open table (Delta/Iceberg), e frequentemente workloads de ML. O Build é o mais intenso — pipelines de ingestão com CDC e transformações com Spark são mais complexos que SQL puro.
- **V3 Data Mesh**: O mais pesado em todas as etapas de planejamento (Inception a Architecture) porque exige alinhamento organizacional profundo — cada domínio precisa aceitar a responsabilidade pelos seus dados. O Build é relativamente mais leve por ser distribuído entre squads, mas a coordenação é pesada.
- **V4 Self-Service**: O mais leve no total — o foco é na camada de consumo (catálogo, semantic layer, BI), não na infraestrutura pesada. O gargalo está no treinamento dos consumidores e na adoção da ferramenta.
- **V5 Streaming**: Architecture e Build são os mais pesados de todas as variantes — streaming exige infraestrutura especializada (Kafka, Flink), monitoramento contínuo de lag e backpressure, e tratamento de exactly-once semantics. Custo de operação é significativamente maior que batch.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Apenas batch, sem streaming (Etapa 01, pergunta 5) | Etapa 05: perguntas sobre Kafka, Flink, schema registry, lag monitoring. Etapa 06: setup de cluster Kafka, Flink. Etapa 07: pipelines de streaming. Etapa 08: testes de latência sub-segundo. |
| Sem site/plataforma anterior a substituir (Etapa 01, pergunta 9) | Etapa 09: perguntas 5 e 7 (dual-run, processos antigos). Etapa 10: perguntas 7, 9 e 15 (comparação com antigo, descomissionamento). |
| Sem requisitos de ML/AI (Etapa 01, pergunta 15) | Etapa 05: perguntas sobre feature store, notebooks, Spark para ML. Etapa 07: pipelines de feature engineering. |
| Ferramenta de BI já definida e em uso (Etapa 02, pergunta 5) | Etapa 03: pergunta sobre escolha de BI. Etapa 09: treinamento de BI (pode ser reduzido se time já usa a ferramenta). |
| Sem compartilhamento externo de dados (Etapa 02, pergunta 13) | Etapa 05: perguntas sobre data sharing, clean rooms, controle de acesso para terceiros. Etapa 06: setup de acessos externos. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Streaming confirmado (Etapa 01, pergunta 5) | Etapa 05: escolha de message broker (Kafka, Kinesis, Pub/Sub), stream processor (Flink, Spark Streaming), e schema registry se tornam gates. Etapa 06: setup de cluster Kafka e monitoramento de lag. Etapa 08: testes de resiliência e backpressure obrigatórios. |
| Dados sensíveis identificados — LGPD/PII (Etapa 02, pergunta 6) | Etapa 04: regras de mascaramento obrigatórias por campo e perfil (pergunta 13). Etapa 05: arquitetura de segurança com column-level security e auditoria de acesso obrigatórias (pergunta 6). Etapa 08: testes de segurança com cenários negativos obrigatórios (pergunta 3). |
| Plataforma substitui processos existentes (Etapa 01, pergunta 9) | Etapa 09: dual-run se torna obrigatório (pergunta 5). Etapa 10: descomissionamento formal com aprovação dos donos (pergunta 9). |
| Volume de dados > 1TB/dia (Etapa 01, pergunta 11) | Etapa 05: particionamento e clustering se tornam gates. Etapa 07: performance de pipeline e otimização de custo se tornam prioridade. Etapa 08: testes de escalabilidade obrigatórios com projeção de 6-12 meses. |
| Data mesh escolhido (Etapa 03, alinhamento de variante) | Etapa 04: contratos de dados entre domínios se tornam obrigatórios (pergunta 12). Etapa 05: plataforma de self-serve com templates de pipeline obrigatória. Etapa 07: build distribuído entre squads exige coordenação explícita. |
| Múltiplas ferramentas de BI em uso (Etapa 02, pergunta 5) | Etapa 05: semantic layer se torna obrigatória para garantir consistência de métricas entre ferramentas (pergunta 11). Etapa 07: validar mesma métrica em todas as ferramentas de BI. |
