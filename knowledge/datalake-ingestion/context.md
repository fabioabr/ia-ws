---
title: Context Pack — Datalake Ingestion
pack-id: datalake-ingestion
description: Context pack para projetos de ingestão de dados em datalake. Cobre pipeline Bronze/Silver/Gold (medallion), qualidade de dados, schemas, janelas, reprocessamento, governança e linhagem.
version: 00.01.000
status: ativo
author: claude-code
category: context-pack
project-name: global
area: tecnologia
tags:
  - context-pack
  - datalake
  - ingestion
  - etl
  - medallion
created: 2026-04-07 12:00
---

# Context Pack — Datalake Ingestion

## Quando usar

O orchestrator deve carregar este pack quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Menção a "datalake", "data warehouse", "lakehouse", "ETL", "ELT", "pipeline de dados"
- Termos: bronze/silver/gold, medallion, raw zone, refined zone, curated zone
- Stack mencionada: Spark, Databricks, Snowflake, Redshift, BigQuery, Synapse, Delta Lake, Iceberg
- Volume grande de dados (TB+, milhões de registros)
- Necessidade de processamento batch ou streaming
- Origem transacional (bancos, eventos, APIs) → destino analítico

## Concerns por eixo

### Product + Valor + Organização (po) — blocos 1-4

**Tópicos obrigatórios do checklist:**

- Quem consome os dados finais (analistas, dashboards, ML, aplicações downstream)
- Casos de uso prioritários (top 3 perguntas que os dados precisam responder)
- SLA de frescor por caso de uso (real-time / micro-batch / horário / diário / D+1)
- Granularidade exigida (linha por transação, agregada, snapshot diário)
- Histórico mínimo retido (90 dias / 2 anos / forever)
- OKRs mensuráveis (ex: redução de tempo de reporting, aumento de cobertura de dados)
- ROI esperado
- Quem é o "dono do dado" (data owner) por domínio — governança
- Estrutura do time de dados (engineer, analyst, scientist, steward)
- Processo de aprovação de mudança na Gold

**Sinais de resposta incompleta:**
- "Vamos consolidar tudo num lugar" (sem caso de uso claro)
- "Pra todo mundo da empresa" (sem persona analítica definida)
- "Real-time" sem definição de janela aceitável
- "Melhorar as decisões" (OKR vago)

### Técnico (solution-architect) — blocos 5, 7, 8

**Categorias aplicáveis:**

- **Tecnologia:** plataforma de processamento (Spark, Flink), formato de armazenamento (Parquet, Delta, Iceberg, Hudi), orquestrador (Airflow, Dagster, ADF), linguagem (SQL, Python, Scala)
- **Segurança:** controle de acesso por camada, mascaramento de dados sensíveis, criptografia at-rest, network isolation
- **Arquitetura:** Lambda × Kappa × Medallion (Bronze/Silver/Gold), batch × streaming × CDC, estratégia de particionamento
- **Integrações:** sistemas de origem, catálogo (Atlas, Purview, Collibra), downstream (BI, ML)
- **Observabilidade:** pipelines, qualidade de dados (Great Expectations, Deequ), freshness, completude, linhagem
- **Build vs Buy:** plataforma (Databricks/Snowflake/BigQuery/self-hosted), orquestrador (MWAA/Astronomer/self-hosted Airflow), catálogo
- **TCO:** custo por TB processado (compute) × custo por query × custo por slot × custo por camada + storage + transfer + governança + reprocessamento

**Perguntas recomendadas:**

- Quais sistemas de origem? (lista exaustiva, com tecnologia e responsável)
- Qual a janela de carga mínima por tabela?
- Como lidar com schema evolution nas origens?
- Há necessidade de CDC (Change Data Capture)?
- Como tratar dados corrompidos/atrasados/duplicados?
- Plataforma: Databricks vs Snowflake vs BigQuery — qual casa com equipe e bounds?
- Política de reprocessamento histórico — quando e como?

### Privacidade (cyber-security-architect, **obrigatório**) — bloco 6

O cyber-security-architect sempre roda este bloco. Em projetos de ingestão de datalake, o **modo profundo é quase sempre o caso** — ingestão costuma carregar PII, dados financeiros ou dados de saúde. O modo magro se aplica apenas a pipelines de dados puramente técnicos (ex: métricas de máquinas, logs de sistema sem identificação de pessoa).

**Concerns específicos de ingestão:**

- Mascaramento / pseudonimização / anonimização por camada (Bronze = raw, Silver = pseudonimizado, Gold = agregado?)
- Linhagem de dados pessoais (onde uma PII entra e todos os destinos que vai)
- Direito ao esquecimento em datalake append-only (como "apagar" um registro sem quebrar histórico)
- Retenção por categoria de dado
- Controle de acesso por coluna (quem pode ver PII vs quem só vê agregado)
- Transferência internacional (se data warehouse em cloud fora do Brasil)
- DPO precisa aprovar queries que cruzam PII?

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|---|---|
| 1 | **Bronze sem versionamento (overwrite)** | Impossibilita reprocessamento e auditoria histórica |
| 2 | **Sem schema evolution policy** | Mudança em origem quebra pipeline em produção |
| 3 | **Pipelines não-idempotentes** | Replay duplica dados, corrompe métricas |
| 4 | **Gold sem testes de qualidade** | Dashboards mostrando dados inconsistentes ao usuário final |
| 5 | **Particionamento por timestamp ingestion (não evento)** | Late data fica em partições erradas, agregações ficam erradas |
| 6 | **Medallion sem governança** | Vira "datalake → dataswamp" em 6 meses |
| 7 | **Lambda architecture quando Kappa basta** | Duplicação de pipelines batch + streaming |
| 8 | **Sem data contracts entre origens e ingestão** | Mudanças unilaterais quebram tudo |
| 9 | **Monitoring só de erro de execução, sem freshness** | Pipeline roda OK mas dados estão atrasados |
| 10 | **PII sem mascaramento já na Bronze** | Vazamento de dados pessoais não-pseudonimizados |

## Edge cases para o 10th-man verificar

- O que acontece quando uma origem fica fora do ar por 24 horas?
- Como reprocessar 2 anos de histórico em uma nova lógica de negócio?
- Como lidar com schema evolution backward-incompatible numa origem crítica?
- Late-arriving data: como lidar com evento de ontem que chegou hoje?
- Duplicação por retry de pipeline: idempotência garantida em qual nível?
- Pipeline que roda de madrugada e falha — quando o usuário descobre?
- Custo explode 3x em um mês — como detectar e investigar antes do mês fechar?
- Compliance LGPD pede exclusão de pessoa específica — como remover de Bronze, Silver, Gold e backups?
- Origem mudou de timezone — como retroagir histórico?
- Dois domínios geram dados conflitantes — quem ganha?
- Pipeline crítico depende de alguém de férias — quem mantém em standby?

## Custom-specialists disponíveis

O catálogo de custom-specialists para projetos de ingestão de datalake está no **spec-pack** correspondente: [[../datalake-ingestion/specialists|knowledge/datalake-ingestion/specialists.md]]. O orchestrator carrega o spec-pack junto com este context-pack durante o Setup.

Lembrete: LGPD/Privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect`.

## Report Profile

Seções extras, métricas obrigatórias e diagramas específicos para o delivery report estão definidos em [[report-profile]].
