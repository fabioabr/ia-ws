---
title: "Environment Discovery"
description: "Cenário atual da empresa: infraestrutura, sistemas, stack, equipe, custos, normas e boas práticas."
category: knowledge-base
type: environment
status: parcial
company: "Patria"
filled-by: "fabio.rodrigues.consult@patria.com"
filled-date: "2026-04-17"
last-updated: "2026-04-17"
completude-por-entregavel:
  one-pager: "100%"
  executive: "~30%"
  delivery: "~11%"
source: "Preenchido parcialmente a partir de (1) repositório datalake-iac-dev (Terraform IaC do Data Lake GCP) e (2) Mapa DataLake Patria v1.1 (Abr/2026, AS-IS, NÃO EXAUSTIVO), autoria de Fabio A. B. Rodrigues - Arquitetura e Produtividade Corporativa"
---

# Environment Discovery — Patria

> **Instruções:** Marque com `[X]` as opções que se aplicam. Use "N/A" para itens que não se aplicam e "A DESCOBRIR" para itens que você não sabe ainda. Este documento será usado como base de conhecimento (RAG) durante o discovery de projetos.

> Marque `[X] Não sei` quando não tiver a informação. O processo de discovery vai investigar esses pontos nas fases seguintes — é melhor admitir que não sabe do que chutar.

> **Nota:** Este preenchimento inicial foi derivado de duas fontes: (1) repositório `datalake-iac-dev` (Terraform do Data Lake GCP) e (2) **Mapa DataLake Patria v1.1 (Abr/2026)** — visão AS-IS e não exaustiva da arquitetura corporativa, autoria de Fabio A. B. Rodrigues. Os campos marcados refletem o que foi observado nessas fontes — podem não representar o ambiente corporativo completo. Revisar e complementar com áreas de negócio e TI.

> **Jurisdições identificadas:** Brasil (BR), Chile (CH) e Cayman (CA).

## Progresso por entregável

> Quanto deste `environment.md` está respondido para cada entregável do Discovery-to-Go. Referência de bitmap em [question-priority.md](question-priority.md). Atualizar sempre que uma resposta for complementada.

| Entregável | Perguntas mínimas | Respondidas | % | Status |
|-----------|-------------------|-------------|---|--------|
| **One-Pager** (OP) | ~8 (escopo/custo/esforço) | 8 | **100%** | Pronto para gerar |
| **Executive** (EX) | ~120 | ~36 | **~30%** | Bloco de segurança/privacidade e financeiro/governança a completar |
| **Delivery** (DR) | ~564 (todas) | ~62 | **~11%** | Depende de entrevistas/workshops nas fases seguintes do Discovery |

> [!tip]
> **Leitura:** o One-Pager já pode ser gerado com o que está aqui. Executive e Delivery acumulam lacunas que são esperadas — o Discovery Pipeline (entrevistas + RAG nas Fases 1 e 2) é o que fecha esses gaps. Atualize esta tabela quando cruzar um marco (ex: +10% em EX).

---

## Domínio 01 — Infraestrutura & Cloud

### Modelo de infraestrutura

> Saber onde a infra está hospedada define restrições de custo, latência, compliance e portabilidade para o novo projeto.

**Tipo:**
- [X] Cloud pública
- [ ] Cloud privada
- [ ] Datacenter próprio
- [ ] Hospedagem compartilhada
- [ ] Híbrido
- [ ] Não sei

**Cloud provider principal:**
- [ ] AWS
- [ ] Azure
- [X] GCP
- [ ] Oracle Cloud
- [ ] Outro: {qual}
- [ ] Nenhum (on-premise)
- [ ] Não sei

> Observado: 3 projetos GCP — `pat-datalake-dev`, `pat-datalake-hml`, `pat-datalake-prd`. Existe também projeto separado para rede: `pat-scl-networking`.
>
> Confirmado (Abr/2026): **somente GCP como cloud corporativa** — não há Azure (infra), AWS ou on-premise (apesar do ecossistema Microsoft Azure DevOps/Key Vault/SharePoint ser SaaS consumido).

**Modelo de conta:**
- [ ] Single-account
- [X] Multi-account
- [ ] N/A
- [ ] Não sei

> Observado: múltiplos projetos GCP segregados por ambiente (dev/hml/prd) + projeto dedicado de rede.

**Billing:**
- [X] Pay-as-you-go
- [ ] Reserved Instances
- [ ] Savings Plans
- [ ] Enterprise Agreement
- [ ] Outro: {qual}
- [ ] Não sei

**Budget alerts e cost tags:**
- [ ] Sim, configurados
- [X] Não
- [ ] Não sei

> Observado: labels padrão `projectid=prj-2025-037`, `cost_center=not_defined`, `area=it`. Cost center ainda não definido.

### Rede e conectividade

> Conexões dedicadas entre escritórios e cloud afetam a arquitetura de integração e os requisitos de segurança.

**VPN site-to-site:**
- [ ] Sim — para: {destino}
- [ ] Não
- [X] Não sei

**Direct Connect / ExpressRoute:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Restrições de firewall para registries/APIs externas:**
- [ ] Sim — quais: {descrever}
- [ ] Não
- [X] Não sei

**Topologia de VPCs/VNets:** VPC centralizada no projeto `pat-scl-networking`. Data Lake DEV usa `pat-vpc-dl-dev` com subnet `pat-snt-vpc-pat-vpc-dl-dev-us-central1-01`. Ambientes HML e PRD presumivelmente possuem VPCs análogas. VMs configuradas **sem IP externo** (`external_access = false`).

### Regiões e disponibilidade

> A localização dos servidores impacta latência para usuários, custos de transferência e obrigações legais de residência de dados.

**Regiões em uso:** `us-central1` (zone `us-central1-b`) para todos os ambientes do Data Lake.

**Residência de dados obrigatória no Brasil:**
- [ ] Sim
- [X] Não
- [ ] Não sei

> Confirmado (Abr/2026): ok manter dados regulatórios (BACEN/CVM/CMF) em `us-central1` — não há requisito legal de residência.

**Disaster recovery:**
- [X] Multi-AZ
- [ ] Multi-region
- [ ] Nenhum
- [ ] Não sei

> Confirmado (Abr/2026): estratégia Multi-AZ. RPO/RTO alvo ainda A DESCOBRIR.

### Ambientes e provisionamento

> Quantidade de ambientes e nível de automação determinam a velocidade e segurança de entregas do novo projeto.

**Ambientes existentes:**
- [X] Desenvolvimento (dev)
- [ ] Staging
- [X] UAT
- [X] Produção
- [ ] Não sei

> Observado: `dev` + `hml` (homologação/UAT) + `prd`. Não há ambiente de `staging` explícito.

**Provisionamento:**
- [ ] Manual
- [X] IaC — Terraform
- [ ] IaC — CloudFormation
- [ ] IaC — Pulumi
- [ ] IaC — Outro: {qual}
- [ ] Scripts ad-hoc
- [ ] Não sei

> Observado: Terraform >= 1.0, providers `google` e `google-beta` >= 5.0. Backend remoto em bucket GCS `datalake_terraform_state`.

**IaC cobertura:**
- [ ] Total (todos os recursos)
- [X] Parcial (somente DataLake)
- [ ] Nenhuma
- [ ] Não sei

> Confirmado (Abr/2026): IaC cobre **apenas o DataLake** (BigQuery, Dataplex, Storage, IAM, Composer, VMs, Pub/Sub, Artifact Registry). Demais sistemas corporativos não são provisionados por Terraform.

### Observabilidade de infra

> Monitoramento e alertas determinam a capacidade de detectar e reagir a problemas antes que afetem os usuários.

**Ferramenta:**
- [ ] CloudWatch
- [ ] Datadog
- [ ] Grafana + Prometheus
- [ ] Zabbix
- [ ] Nagios
- [X] Outra: Google Cloud Monitoring + Logging (uso ativo)
- [ ] Nenhuma
- [ ] Não sei

> Confirmado (Abr/2026): Google Cloud Monitoring + Logging em uso ativo (não só APIs habilitadas).

**Alertas configurados:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Dashboards operacionais:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Containers e orquestração

> O uso de containers influencia a estratégia de deploy, escalabilidade e a curva de aprendizado necessária para o time.

**Usa containers (Docker):**
- [X] Sim
- [ ] Não
- [ ] Não sei

> Observado: Docker usado em VMs dev/hml para rodar Airflow. Artifact Registry hospeda imagens Docker (`public-equities-cmf-nobank-bronze`, `splitc-iliquidos-bra-repository`, `splitc-realestate-bra-repository`, `splitc-chl-repository`, `nexxus-limitsctl-chl-repository`, `sox-controls-repository`, `public-equities-cmf-nobank-webscrapping`).

**Orquestrador:**
- [ ] Kubernetes (EKS)
- [ ] Kubernetes (AKS)
- [ ] Kubernetes (GKE)
- [ ] Kubernetes (self-managed)
- [ ] ECS
- [ ] Fargate
- [X] Docker Compose
- [ ] Nenhum
- [ ] Não sei

> Observado no Data Lake: VMs rodam Airflow em Docker (sem Kubernetes). PRD usa **Cloud Composer** (Airflow gerenciado).
>
> Confirmado (Abr/2026): **não há Kubernetes/GKE em uso corporativo** fora do DataLake.

**Se Kubernetes:**
- [ ] Namespaces configurados
- [ ] Resource quotas definidas
- [ ] Ingress controller ativo
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer particularidade de infraestrutura que não se encaixe nos campos anteriores.

```
- APIs GCP habilitadas no Data Lake: dataplex, bigquery, iam, artifactregistry, cloudbuild,
  run, cloudfunctions, storage, logging, monitoring, eventarc, pubsub, cloudresourcemanager,
  aiplatform (Vertex AI/Gemini), compute.

- Cloud Run e Cloud Functions Gen2 habilitados — uso efetivo A DESCOBRIR.

- Vertex AI/Gemini habilitado — indicativo de uso de IA para processamento
  (README menciona "PDF AI Processing com Gemini").
```

---

## Domínio 02 — Sistemas Contratados & SaaS

### Inventário de sistemas ativos

> Mapear os sistemas contratados evita sobreposição de funcionalidades e identifica oportunidades de integração ou substituição.

| Sistema | Tipo | Fornecedor | Contrato | Renovação | Custo mensal | API disponível | SSO integrado |
|---------|------|-----------|----------|-----------|-------------|----------------|---------------|
| Oracle Fusion GL (Cayman) | ERP — General Ledger | Oracle | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via Incorta / BICC) | A DESCOBRIR |
| Oracle (HCM, SCM, AP, Common, Financials, AuditTemp) | ERP | Oracle | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (fonte de dados) | A DESCOBRIR |
| iLevel | FP&A | iLevel/S&P | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (integrado) | A DESCOBRIR |
| Efront | Private Equity / gestão de fundos | BlackRock | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Geneva (Chile) | TPA — Líquidos, Ilíquidos, Real Estate | SS&C Technologies | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via Sensedia) | A DESCOBRIR |
| Sistema Derivados (Chile) | TPA — Derivativos | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via Sensedia) | A DESCOBRIR |
| Sistema Remuneraciones (Chile) | Remuneração de fundos chilenos | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via Sensedia) | A DESCOBRIR |
| Ilíquidos (Brasil) | TPA — Dados de fundos ilíquidos | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via N8N) | A DESCOBRIR |
| Real Estate (Brasil) | TPA — Dados de fundos imobiliários | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (via Sensedia/N8N) | A DESCOBRIR |
| SplitC BR / SplitC CH | Sistema destino (cotização/splitting) | Interno (Patria) | N/A | N/A | N/A | Sim | A DESCOBRIR |
| Nexxus BR / Nexxus CH | Sistema destino | Interno (Patria) | N/A | N/A | N/A | Sim | A DESCOBRIR |
| Snowflake | Data warehouse (fonte SOX Controls) | Snowflake | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Active Directory | IdP / diretório corporativo | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (LDAP / Kerberos / SAML) | Sim (IdP próprio) |
| GPI | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Artikos | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Pentaho (Pentano) | BI / ETL (legacy) | Hitachi Vantara | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| BluePrism | RPA | SS&C Blue Prism | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Veeam (Veam) | Backup | Veeam | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Thycotic (Delinea) | PAM — Privileged Access Management | Delinea | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| N8N | Orquestrador / automação de workflows | n8n.io (open-source) | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Sensedia | API Gateway / management | Sensedia | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Incorta | Middleware ETL (Oracle Fusion GL → BigQuery) | Incorta | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| BICC | Business Intelligence Cloud Connector | Oracle | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Power BI | BI / dashboards | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | Provável (ecossistema Microsoft) |
| GA4 (Google Analytics 4) | Web analytics | Google | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (BigQuery export) | A DESCOBRIR |
| SharePoint | Repositório corporativo / colaboração | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim (FPA extraction) | A DESCOBRIR |
| Azure DevOps | Pipelines / repositório | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| GitHub | Repositório / Actions | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Azure Key Vault | Secret manager | Microsoft | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |
| Google Cloud | Cloud provider | Google | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR | Sim | A DESCOBRIR |

### Provedor de identidade (SSO)

> O IdP define como os usuários fazem login. Integrar com o SSO existente reduz fricção e aumenta segurança.

**IdP:**
- [X] Azure AD / Entra ID
- [ ] Okta
- [ ] Google Workspace
- [ ] Auth0
- [ ] Keycloak
- [X] Outro: Active Directory (on-premise ou híbrido)
- [ ] Nenhum
- [ ] Não sei

> Observado: o mapa DataLake v1.1 lista **Active Directory (AD)** como componente SOX Controls — confirma diretório corporativo Microsoft. Emails usam domínio `@patria.com`. Uso combinado de AD on-premise + Azure AD (Entra ID) é prática comum em ambientes híbridos com Azure DevOps + Key Vault + SharePoint. A DESCOBRIR se há federação.

**Protocolo:**
- [ ] SAML
- [ ] OIDC
- [ ] Ambos
- [ ] N/A
- [X] Não sei

**Sistemas integrados ao SSO:** A DESCOBRIR

**Sistemas com login separado:** A DESCOBRIR

### Sistemas legados sem substituição planejada

> Sistemas legados são fontes frequentes de risco técnico, dependência de fornecedor e gargalos de integração.

| Sistema | Tecnologia | O que faz | Risco |
|---------|-----------|-----------|-------|
| **Incorta** | Incorta Direct Data Platform | Middleware ETL entre Oracle Fusion GL (Cayman) e BICC | **EOL confirmado — desabilitação planejada para 06/2026.** Requer plano de substituição urgente |
| Oracle Fusion GL | Oracle Cloud ERP | General Ledger da entidade Cayman — dados contábeis | Dependência crítica do middleware Incorta para extração (Incorta sai em 06/2026) |
| Oracle ERP (HCM, SCM, AP, Financials, AuditTemp) | Oracle DB | ERP corporativo | A DESCOBRIR |
| Pentaho | Pentaho CE/EE | BI / ETL (legado — listado em SOX Controls) | Plataforma em declínio desde aquisição pela Hitachi; avaliar substituição |
| Geneva | SS&C Geneva | TPA de portfólio (Líquidos/Ilíquidos/Real Estate Chile) | A DESCOBRIR (fornecedor único) |

### Shadow IT identificado

> Ferramentas não oficiais revelam necessidades não atendidas e riscos de segurança que o novo projeto pode endereçar.

| Ferramenta | Quem usa | Para quê | Por que não usa o oficial |
|-----------|---------|---------|--------------------------|
| | | | |
| | | | |

### Notas adicionais

> Registre aqui qualquer informação sobre sistemas e SaaS que não se encaixe nos campos anteriores.

```
Fontes regulatórias integradas ao Data Lake:
- CMF (Comisión para el Mercado Financiero - Chile) — Chile banks
- CVM (Comissão de Valores Mobiliários - Brasil) — Brazilian companies
- BACEN/COSIF (Banco Central do Brasil) — Brazilian banks
- SOX Controls — auditoria interna

Sistemas fontes de SOX Controls (Mapa DataLake v1.1):
- Oracle HCM, Efront, Geneva, GPI, AD (Active Directory), Snowflake, Artikos,
  BluePrism, Pentaho, Veeam, Thycotic — consolidados via Python

Integradores/Middleware observados:
- N8N — orquestração de ingestão (BR ilíquidos, real estate, scheduler CH)
- Sensedia — API Gateway (Geneva, Derivados, Remuneraciones CH; Real Estate BR)
- Incorta — middleware ETL (Oracle Fusion GL Cayman → Airflow → BigQuery)
- Python (Selenium) — webscraping de BACEN e CMF
- Python — integração SOX Controls
- Airflow — orquestração geral
- Cloud Pub/Sub — streaming

Protocolos de ingestão observados:
- APIs REST/SOAP, SFTP, E-mail + anexos, SharePoint, BICC (Oracle BI Cloud Connector)

Projetos/produtos observados no Data Lake:
- Public Equities CMF NoBank (XBRL + PDF processing com Gemini)
- SPLITC BR (Ilíquidos + Real Estate) + SPLITC CH
- Nexxus BR + Nexxus CH + Nexxus LimitsCtl Chile
- CHL LimitsCtrl
- Gold Finance (dataset consolidado financeiro / General Ledger)
- Capivara (datalake específico)
- Invested Companies Debt

Jurisdições mapeadas:
- Brasil (BR) — TPAs (Ilíquidos, Real Estate), BACEN, CVM; Líquidos marcado como
  "NÃO EXISTE NO AS-IS" (gap mapeado)
- Chile (CH) — TPAs (Geneva, Derivados, Remuneraciones), CMF
- Cayman (CA) — Oracle Fusion GL (contábil / General Ledger)

Consumo / camadas de saída:
- Camada Semântica (Excel)
- Power BI (principal ferramenta de dashboards)
- GA4BigQuery (Google Analytics 4 exportado)
- Destinos: Colaboradores + área de Governança de TI e Auditoria

Arquiteto responsável pelo Mapa DataLake v1.1: Fabio A. B. Rodrigues
(Arquitetura e Produtividade Corporativa).
```

---

## Domínio 03 — Stack de Desenvolvimento

### Linguagens e frameworks

> Conhecer a stack atual permite avaliar compatibilidade, reuso de código e necessidade de capacitação do time.

| Camada | Linguagem | Framework | Observações |
|--------|-----------|-----------|-------------|
| Front-end | A DESCOBRIR | A DESCOBRIR | |
| Back-end | Python (presumido) | Apache Airflow | DAGs Airflow para orquestração do Data Lake |
| Mobile | A DESCOBRIR | A DESCOBRIR | |
| Scripts/automação | Bash, HCL (Terraform) | Terraform, GitHub Actions, Azure Pipelines | IaC e CI/CD |

### Versionamento

> O fluxo de versionamento impacta diretamente a velocidade de entrega, qualidade do código e colaboração entre devs.

**Plataforma:**
- [X] GitHub
- [ ] GitLab
- [ ] Bitbucket
- [X] Azure DevOps
- [ ] Outro: {qual}
- [ ] Não sei

> Observado: coexistência de GitHub (workflows `.github/workflows/`) e Azure DevOps (citado no README original como plataforma de pipelines, grupo `gcp` no Key Vault).

**Plano/tier:**
- [ ] Free
- [ ] Team
- [ ] Enterprise
- [X] Não sei

**Modelo de branching:**
- [X] GitFlow
- [ ] Trunk-based development
- [ ] Feature branches
- [ ] Sem padrão definido
- [ ] Não sei

> Observado: fluxo `feature/* → development → homologation → produccion/production`. Cada branch tem pipeline próprio.

**PRs obrigatórios:**
- [ ] Sim
- [ ] Não
- [X] Não sei

> Observação: README menciona "merge da feature branch em development (via Pull Request)", mas não há evidência de regra obrigatória.

**Aprovações mínimas por PR:**
- [ ] 0
- [ ] 1
- [ ] 2+
- [X] Não sei

### Padrões e convenções

> Padrões de código e API garantem consistência entre times e reduzem atrito na integração entre serviços.

**Style guide documentado:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Linting automatizado:**
- [ ] ESLint
- [ ] Prettier
- [ ] Ruff / Black (Python)
- [ ] Outro: {qual}
- [ ] Nenhum
- [X] Não sei

**Padrão de API:**
- [ ] REST
- [ ] GraphQL
- [ ] gRPC
- [ ] Ambos (REST + GraphQL)
- [ ] Sem padrão definido
- [X] Não sei

**Versionamento de API:**
- [ ] URL (/v1, /v2)
- [ ] Header
- [ ] Nenhum
- [X] Não sei

### Packages internos

> Bibliotecas internas compartilhadas aceleram o desenvolvimento e garantem padronização entre projetos.

**Registry privado:**
- [ ] npm (Verdaccio, GitHub Packages)
- [ ] PyPI
- [ ] Maven / Nexus
- [ ] NuGet
- [X] Docker Registry
- [ ] Nenhum
- [ ] Não sei

> Observado: Google Artifact Registry com múltiplos repositórios Docker para projetos internos (CMF NoBank bronze/webscrapping, SPLITC iliquidos/realestate BR, SPLITC CHL, Nexxus LimitsCtl CHL, SOX Controls).

**Packages compartilhados:** A DESCOBRIR (imagens Docker estão segregadas por projeto, não por biblioteca compartilhada aparente).

### Bancos de dados

> O mapa de bancos de dados revela restrições de licenciamento, capacidade e compatibilidade para o novo projeto.

| Banco | Tipo | Ambiente | Gerenciado | Capacidade | Licença |
|-------|------|----------|-----------|-----------|---------|
| BigQuery | Data warehouse / OLAP (camadas Prata e Ouro do Data Lake) | dev + hml + prd | Sim (GCP) | A DESCOBRIR | Pay-per-use |
| Snowflake | Data warehouse (fonte SOX Controls) | A DESCOBRIR | Sim (Snowflake) | A DESCOBRIR | Comercial |
| Oracle Fusion (Cayman) | ERP Cloud — General Ledger | Produção | Sim (Oracle Cloud) | A DESCOBRIR | Comercial |
| Oracle DB | RDBMS (OLTP, ERP on-premise/Cloud) | Corporativo | A DESCOBRIR | A DESCOBRIR | Comercial |
| Dataplex (catálogo + zones) | Governança / lakehouse | dev + hml + prd | Sim (GCP) | A DESCOBRIR | Pay-per-use |
| Google Cloud Storage | Object storage (camada Bronze do Data Lake) | dev + hml + prd | Sim (GCP) | A DESCOBRIR | Pay-per-use |

### Mensageria e filas

> Brokers de mensageria definem como os sistemas se comunicam de forma assíncrona, impactando resiliência e escalabilidade.

**Brokers em uso:**
- [ ] RabbitMQ
- [ ] Apache Kafka
- [ ] AWS SQS / SNS
- [ ] Azure Service Bus
- [X] Google Pub/Sub
- [ ] Redis (Pub/Sub ou Streams)
- [ ] Nenhum
- [ ] Não sei

> Observado: `pubsub.tf` presente + API `pubsub.googleapis.com` e `eventarc.googleapis.com` habilitadas (provavelmente para Cloud Functions Gen2 event-driven).

### Débito técnico conhecido

> Débitos técnicos não resolvidos podem comprometer prazos e qualidade do novo projeto se não forem considerados desde o início.

1. Coexistência de GitHub Actions e Azure Pipelines para o mesmo repositório — potencial ambiguidade sobre qual é o pipeline oficial.
2. Label `cost_center = not_defined` no IaC — rastreamento de custos por área ainda não implementado.
3. Pipeline de deploy dividido em 6 fases com tratamento de erros conhecidos via regex de sanitização — sinaliza dependências entre recursos não totalmente resolvidas via `depends_on`.

### Notas adicionais

> Registre aqui qualquer informação sobre stack de desenvolvimento que não se encaixe nos campos anteriores.

```
- Terraform version: 1.9.0 (CI/CD) / >= 1.0 (mínimo declarado)
- Google provider: >= 5.0
- Composer image: composer-2.13.7-airflow-2.10.5 (produção)
- VM Airflow: Debian 11, n2-standard-2, disco 50GB
```

---

## Domínio 04 — DevOps & Entrega Contínua

### CI/CD

> O nível de automação do pipeline determina a velocidade e confiabilidade com que código chega a produção.

**Ferramenta:**
- [X] GitHub Actions
- [ ] GitLab CI
- [ ] Jenkins
- [ ] CircleCI
- [X] Azure Pipelines
- [ ] AWS CodePipeline
- [ ] Outra: {qual}
- [ ] Nenhuma
- [ ] Não sei

> Observado: repositório tem AMBOS — workflows GitHub Actions (`.github/workflows/terraform-cd-dev|hml|prd.yaml` + `terraform-ci-basic.yaml`) e referências a Azure Pipelines (`.azure/azure-pipeline-dev|hml|prd|validate.yaml` no README).

**Cobertura:**
- [ ] Todos os projetos
- [ ] Apenas alguns
- [ ] Nenhum
- [X] Não sei

**Stages no pipeline:**
- [ ] Lint
- [X] Test (unitários) — apenas `terraform validate`
- [ ] Test (integração)
- [X] Build — `terraform plan`
- [ ] Security scan (SAST/DAST)
- [ ] Deploy automático
- [X] Deploy com aprovação — GitHub Environments (`environment: development`)
- [ ] Não sei

> Observado: pipeline executa `terraform validate → plan → safety checks (proteção de VM) → apply em 6 fases sequenciais`. Safety check aborta pipeline se VM do Airflow seria destruída ou recriada.

### Deploy

> A estratégia de deploy e rollback define o risco de cada entrega e a capacidade de reverter problemas rapidamente.

**Estratégia:**
- [X] Automático em push/merge
- [ ] Manual por aprovação
- [ ] Release trains (periodicidade fixa)
- [ ] FTP / cópia manual
- [ ] Não sei

> Observado: push em `dev` / `homologation` / `produccion` dispara deploy automático. GitHub Environments podem exigir aprovação — A DESCOBRIR se está configurada.

**Rollback:**
- [ ] Blue-green
- [ ] Canary
- [ ] Rolling update
- [ ] Feature flags
- [X] Nenhum (redeploy versão anterior)
- [ ] Não sei

> Observado: não há estratégia de rollback automatizada no IaC. Terraform state pode ser usado para rollback manual.

**Frequência média de deploy em produção:**
- [ ] Diário (ou mais)
- [ ] Semanal
- [ ] Mensal
- [ ] Trimestral ou menos
- [X] Não sei

**Lead time (merge → produção):**
- [ ] Minutos
- [ ] Horas
- [ ] Dias
- [ ] Semanas
- [X] Não sei

### Gestão de secrets

> A forma como credenciais e chaves são armazenadas é um dos maiores vetores de risco de segurança em projetos.

**Método:**
- [ ] HashiCorp Vault
- [ ] AWS Secrets Manager
- [X] Azure Key Vault
- [ ] GCP Secret Manager
- [X] Variáveis de ambiente (CI/CD)
- [ ] Hardcoded / .env commitado
- [ ] Outro: GitHub Secrets (Workload Identity Federation)
- [ ] Não sei

> Observado: Azure Key Vault armazena `AIRFLOW_PASS`, `GIT_USER`, `GIT_TOKEN` e credenciais GCP (`pat-datalake-{env}.json`). GitHub Secrets armazena `GCP_WIF_PROVIDER`, `GCP_SA_EMAIL`, `AIRFLOW_PASSWORD`. Workload Identity Federation é usado para autenticar GitHub Actions no GCP sem chaves de service account.

### Observabilidade de aplicação

> APM, logs e tracing são essenciais para diagnosticar problemas em produção e medir a saúde real dos serviços.

**APM:**
- [ ] Datadog
- [ ] New Relic
- [ ] Dynatrace
- [ ] Application Insights
- [ ] Outra: {qual}
- [ ] Nenhuma
- [X] Não sei

**Logging centralizado:**
- [ ] ELK (Elasticsearch + Logstash + Kibana)
- [ ] Grafana Loki
- [ ] CloudWatch Logs
- [ ] Splunk
- [X] Outro: Google Cloud Logging
- [ ] Nenhum
- [ ] Não sei

> Observado: API `logging.googleapis.com` habilitada. Uso efetivo em aplicações — A DESCOBRIR.

**Tracing distribuído:**
- [ ] OpenTelemetry
- [ ] Jaeger
- [ ] Zipkin
- [ ] Nenhum
- [X] Não sei

### Gestão de incidentes

> Processos de resposta a incidentes impactam o tempo de recuperação e a maturidade operacional do novo projeto.

**Ferramenta de on-call:**
- [ ] PagerDuty
- [ ] Opsgenie
- [ ] Grafana OnCall
- [ ] Nenhuma
- [X] Não sei

**Escalation policy definida:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Post-mortems documentados:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Runbooks existentes:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre DevOps e entrega contínua que não se encaixe nos campos anteriores.

```
Pipeline de deploy do Data Lake opera em 6 fases sequenciais:
  Phase 0: Storage (buckets GCS)
  Phase 1: BigQuery datasets (parallelism=2)
  Phase 2: Dataplex Lakes (parallelism=1)
  Phase 3: Project IAM
  Phase 4: Dataplex IAM
  Phase 5: BigQuery IAM
  Phase 6: IAM Replace (force-replace de bindings)

Safety checks explícitos abortam a pipeline se a VM do Airflow (dev/hml) for afetada.
Erros "conhecidos" (ex.: Already Exists, resourceInUseByAnotherResource) são
sanitizados via regex para tolerar re-execuções idempotentes.
```

---

## Domínio 05 — Segurança & Compliance

### Políticas

> Políticas de segurança documentadas definem as regras do jogo — sem elas, cada projeto inventa suas próprias práticas.

**Política de segurança da informação documentada:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Classificação de dados (público, interno, confidencial, restrito):**
- [ ] Sim, implementada
- [ ] Sim, apenas documentada
- [ ] Não
- [X] Não sei

> Observação: existem módulos Terraform para `taxonomy` (Data Catalog / policy tags) e Dataplex — infraestrutura para classificação existe, mas uso real A DESCOBRIR.

### Compliance regulatório

> Regulamentações aplicáveis definem requisitos obrigatórios que podem impactar arquitetura, prazos e custos do projeto.

**Regulamentações aplicáveis:**
- [ ] LGPD
- [ ] GDPR
- [ ] PCI-DSS
- [ ] HIPAA
- [X] SOX
- [X] BACEN (regulamentação bancária)
- [ ] Marco Civil da Internet
- [ ] ISO 27001
- [ ] SOC 2
- [ ] Nenhuma específica
- [X] Outra: CMF (Comisión para el Mercado Financiero - Chile), CVM (Comissão de Valores Mobiliários - Brasil)
- [ ] Não sei

> Observado: repositório Docker `sox-controls-repository` indica processos SOX ativos. Data Lake ingere COSIF (BACEN), CVM (Brasil), CMF (Chile) — sugere escopo regulatório multi-jurisdição, típico de gestora de ativos. LGPD/GDPR A DESCOBRIR (provável, mas não evidenciado no IaC).

### Privacidade

> Maturidade em privacidade determina se o projeto precisa criar processos de LGPD/GDPR do zero ou pode reaproveitar os existentes.

**DPO nomeado:**
- [ ] Sim — nome: {nome}
- [ ] Não
- [X] Não sei

**ROPA (Record of Processing Activities) mantido:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Processo para direitos de titulares (acesso, retificação, exclusão):**
- [ ] Sim, automatizado
- [ ] Sim, manual
- [ ] Não
- [X] Não sei

### Controle de acesso

> Controles de acesso mal configurados são a causa mais comum de vazamentos de dados e acessos indevidos.

**MFA obrigatório:**
- [ ] Sim, para todos
- [ ] Sim, apenas para admin/produção
- [ ] Não
- [X] Não sei

**Princípio do menor privilégio:**
- [ ] Sim, aplicado sistematicamente
- [X] Parcial
- [ ] Não
- [ ] Não sei

> Observado: IAM granular por dataset/zone/lake (ex.: `oracle_common_bronze_viewer`, `bacen_bra_cosif_banks_gold_viewer`) — há esforço de least-privilege no Data Lake. Listas de usuários específicas por dataset (ex.: apenas 3 emails têm acesso a `bacen_bra_cosif_banks_silver`).

**Segregação de ambientes (dev não acessa produção):**
- [X] Sim
- [ ] Não
- [ ] Não sei

> Observado: 3 projetos GCP separados (dev/hml/prd), cada um com próprio service account (`airflow-{env}@pat-datalake-{env}.iam.gserviceaccount.com`) e credenciais distintas.

**Offboarding automático revoga acessos:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Vulnerabilidades

> Identificar e corrigir vulnerabilidades de forma proativa evita incidentes de segurança que podem paralisar o negócio.

**Scan automatizado:**
- [ ] Snyk
- [ ] Dependabot
- [ ] SonarQube
- [ ] Trivy
- [ ] Outro: {qual}
- [ ] Nenhum
- [X] Não sei

**Integrado ao CI/CD:**
- [ ] Sim
- [X] Não
- [ ] Não sei

> Observado no pipeline: apenas `terraform validate` + `terraform plan`. Nenhum stage de security scan (SAST/DAST/SCA).

**Pen test periódico:**
- [ ] Sim, anual
- [ ] Sim, semestral
- [ ] Nunca realizado
- [X] Não sei

**SLA para correção de CVEs críticos:**
- [ ] 24h
- [ ] 7 dias
- [ ] 30 dias
- [ ] Sem SLA definido
- [X] Não sei

### Criptografia

> Criptografia protege dados sensíveis contra interceptação e acesso não autorizado, sendo requisito de compliance.

**Dados em trânsito (TLS 1.2+):**
- [X] Sim
- [ ] Não
- [ ] Não sei

> Observação: serviços GCP (BigQuery, GCS, Dataplex) usam TLS por padrão.

**Dados em repouso (AES-256 ou equivalente):**
- [X] Sim
- [ ] Não
- [ ] Parcial (apenas alguns sistemas)
- [ ] Não sei

> Observação: GCS e BigQuery usam AES-256 por padrão (criptografia gerenciada pela Google). VM Airflow suporta `kms_key_self_link` (CMEK opcional) — uso real A DESCOBRIR.

**Gestão de chaves:**
- [X] KMS (cloud provider)
- [ ] HashiCorp Vault
- [ ] HSM
- [ ] Manual
- [ ] Não definido
- [ ] Não sei

> Observação: variáveis `kms_key_self_link` (VM) e `composer_kms_key_name` (Composer) presentes no IaC — preparados para CMEK. Cloud KMS usado como KMS padrão.

**PAM (Privileged Access Management):**
- [X] Sim — Thycotic (Delinea)
- [ ] Não
- [ ] Não sei

> Observado no Mapa DataLake v1.1: Thycotic listado em SOX Controls — gestão de acessos privilegiados.

### Notas adicionais

> Registre aqui qualquer informação sobre segurança e compliance que não se encaixe nos campos anteriores.

```
Autenticação GitHub Actions → GCP via Workload Identity Federation (sem chaves
estáticas de service account). Boa prática de segurança adotada.

Service accounts segregados por ambiente:
  - airflow-dev@pat-datalake-dev.iam.gserviceaccount.com
  - airflow-hml@pat-datalake-hml.iam.gserviceaccount.com (presumido)
  - airflow-prd@pat-datalake-prd.iam.gserviceaccount.com (presumido)

VMs sem IP externo — acesso somente via rede interna da VPC.

Dataplex usado como camada de governança — sinaliza maturidade em data governance.
```

---

## Domínio 06 — Dados & Integrações

### Fontes autoritativas

> Saber qual sistema é dono de cada dado evita conflitos de sincronização e duplicação entre sistemas.

| Entidade | Sistema dono (source of truth) | Observações |
|----------|-------------------------------|-------------|
| Cliente / Investidor | A DESCOBRIR | |
| Produto (fundos/ativos) | A DESCOBRIR | |
| Pedido / Transação | A DESCOBRIR | |
| Funcionário | Oracle HCM | Bronze zone: `oracle_hcm_bronze` |
| Financeiro | Oracle Financials | Bronze + silver zones: `oracle_financials_bronze`, `oracle_financials_silver` |
| FP&A | iLevel + SharePoint | Bronze + silver + gold: `ilevel_fpa_*`, `extraction_sharepoint_fpa_*` |
| Controles SOX | Sistema interno (sox-controls) | Bronze + silver: `sox_controls_bronze`, `sox_controls_silver` |
| Bancos CHL (CMF) | CMF Chile | `chl_bank_*` + `nexxus_limitsctl_chl_*` |
| Empresas BRA (CVM) | CVM Brasil | `bra_companies_*` |
| Bancos BRA (BACEN) | BACEN/COSIF | `bacen_bra_cosif_banks_*` |
| Contas a pagar | Oracle AP | `oracle_ap_bronze` |
| SCM (Supply Chain) | Oracle SCM | `oracle_scm_bronze` |
| Auditoria temporária | Oracle AuditTemp | `oracle_audittemp_bronze` |

### Qualidade dos dados

> Dados inconsistentes ou incompletos comprometem relatórios, decisões e a confiabilidade do novo sistema.

**Dados duplicados entre sistemas:**
- [ ] Sim, frequente
- [ ] Raramente
- [ ] Não
- [X] Não sei

**Encoding inconsistente:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Campos vazios em entidades críticas:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Integrações existentes

> O mapa de integrações revela dependências críticas e pontos de falha que o novo projeto precisa considerar.

| De | Para | Tipo | Volume | Monitoramento | Responsável |
|----|------|------|--------|---------------|-------------|
| Oracle Fusion GL (Cayman) | BigQuery (bronze) | Incorta (Middleware ETL) → Airflow → BICC | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Oracle HCM / Snowflake / Efront / Geneva / GPI / AD / Artikos / BluePrism / Pentaho / Veeam / Thycotic | BigQuery (bronze) — SOX Controls | Scripts Python (TO-DO detalhar) | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| SharePoint (FPA) | BigQuery (bronze) | SharePoint API → Airflow | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| iLevel | BigQuery (bronze) | API → Airflow | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Ilíquidos (BR) | SplitC BR + Bronze | N8N (orquestração) via SharePoint/SFTP/E-mail | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Real Estate (BR) | Nexxus BR + Bronze | Sensedia (API Gateway) + N8N | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Geneva (CH) | Nexxus CH + SplitC CH | N8N Scheduler + Sensedia (API) + Pub/Sub | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Sistema Derivados (CH) | Nexxus CH + Bronze | Sensedia (API) + Pub/Sub | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Sistema Remuneraciones (CH) | SplitC CH + Bronze | Sensedia (API) + Pub/Sub | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| CMF (Chile) | BigQuery (bronze) | Python + Selenium (webscraping) | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| CVM (Brasil) | BigQuery (bronze) | Python (dados públicos) | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| BACEN (Brasil) | BigQuery (bronze) | Python + Selenium (webscraping) | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| BigQuery (Ouro) | Excel (camada semântica) | Conectores direto | A DESCOBRIR | A DESCOBRIR | Colaboradores |
| BigQuery (Ouro) | Power BI | Conector BigQuery | A DESCOBRIR | A DESCOBRIR | Colaboradores + Governança |
| BigQuery (Ouro) | GA4BigQuery | Export BigQuery | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| GCS (Export Azure) | Azure (destino externo) | Export bucket | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |

> **Observação crítica:** o mapa explicita **"Líquidos BR — NÃO EXISTE NO AS-IS"** tanto na entrada (TPAs Brasil) quanto na saída (camada Ouro). Gap conhecido — potencial escopo para projetos futuros.

### Data warehouse / Data lake

> A existência de um data warehouse ou data lake influencia a estratégia de analytics e BI do novo projeto.

**Existe:**
- [X] Sim
- [ ] Não
- [ ] Não sei

**Ferramenta:**
- [X] BigQuery
- [ ] Redshift
- [X] Snowflake
- [ ] Databricks
- [ ] S3 + Athena
- [ ] Synapse Analytics
- [X] Outro: Google Dataplex (governança / lakehouse em cima do BigQuery + GCS)
- [ ] Nenhum
- [ ] Não sei

> Observado: arquitetura **medallion (Bronze GCS → Prata BigQuery → Ouro BigQuery)** implementada via Dataplex lakes + zones + assets. 11 lakes (`datalake_chl_bank`, `datalake_bra_companies`, `datalake_invested_companies_debt`, `datalake_ilevel_fpa`, `datalake_capivara`, `datalake_cmf_nobanks`, `datalake_oracle`, `datalake_chl_limitsctrl`, `datalake_splitc`, `datalake_nexxus`, `datalake_bacen_bra_cosif_banks`).
>
> **Snowflake** aparece no Mapa DataLake v1.1 como fonte de SOX Controls — coexistência de DWs. A DESCOBRIR qual o escopo do Snowflake vs. BigQuery e se há plano de consolidação.

**O que está populado:** Oracle (ERP/HCM/financials/common/AP/audittemp/SCM), CVM Brasil, CMF Chile, BACEN/COSIF, iLevel FPA, SharePoint FPA, SPLITC (Brasil + Chile), Nexxus LimitsCtl Chile, SOX Controls, CMF NoBanks (XBRL + PDF com Gemini), Capivara, Invested Companies Debt, Gold Finance (consolidado).

**Frequência de atualização:**
- [ ] Real-time / streaming
- [ ] Horário
- [ ] Diário
- [ ] Semanal
- [X] Não sei

> Observação: Airflow orquestra DAGs — provavelmente batch diário ou programado. A DESCOBRIR.

**Custo mensal:** A DESCOBRIR

### ETL/ELT

> Pipelines de dados existentes podem ser reaproveitados ou precisam ser adaptados para alimentar o novo projeto.

**Ferramenta:**
- [X] Apache Airflow
- [ ] dbt
- [ ] AWS Glue
- [ ] Informatica
- [ ] SSIS
- [ ] Talend
- [X] Scripts manuais (Python, SQL)
- [X] Outro: N8N (orquestração/automação), Sensedia (API Gateway), Incorta (Middleware ETL), Python+Selenium (webscraping), Pentaho (legacy), BluePrism (RPA)
- [ ] Nenhum
- [ ] Não sei

> Observado: stack de integração heterogênea e camadas:
> - **Airflow** — orquestrador principal (Docker DEV/HML, Cloud Composer 2.13.7/Airflow 2.10.5 em PRD)
> - **N8N** — automações no-code/low-code (ingestão de TPAs BR, scheduler CH)
> - **Sensedia** — API Gateway para sistemas Chile (Geneva, Derivados, Remuneraciones) e Real Estate BR
> - **Incorta** — middleware ETL especializado para Oracle Fusion GL → BigQuery
> - **Python + Selenium** — webscraping de sites regulatórios (BACEN, CMF, CVM)
> - **BICC** — conector Oracle BI Cloud (Oracle Fusion → data platform)
> - **Cloud Pub/Sub** — streaming de eventos
> - **Pentaho** — presente no SOX Controls (provável legado de ETL)
> - **BluePrism** — RPA (presente no SOX Controls)
>
> DAGs Airflow versionadas em repositório git separado (clonadas no boot da VM via `GIT_USER` e `GIT_TOKEN`).

### Backup e recuperação

> Políticas de backup e RPO/RTO definem quanto dado pode ser perdido e em quanto tempo o sistema precisa voltar a funcionar.

**Frequência de backup:**
- [ ] Contínuo
- [ ] Horário
- [ ] Diário
- [ ] Semanal
- [X] Não sei

**Retenção:**
- [ ] 7 dias
- [ ] 30 dias
- [ ] 90 dias
- [ ] 1 ano+
- [X] Não sei

**Ferramenta de backup:**
- [X] Veeam (identificado no Mapa DataLake v1.1 como componente SOX Controls)
- [ ] Outro

> Observação: Veeam é tipicamente usado para backup de VMs/infra on-premise e virtualizada — sugere que a Patria ainda tem workloads fora do GCP cobertos por Veeam.

**Último teste de restore:** A DESCOBRIR

**RPO definido:** A DESCOBRIR

**RTO definido:** A DESCOBRIR

### Notas adicionais

> Registre aqui qualquer informação sobre dados e integrações que não se encaixe nos campos anteriores.

```
Arquitetura Medallion explícita (nomenclatura do mapa v1.1):
- Bronze (Data Lake / GCS) — Dados Raw
- Prata (BigQuery) — Dados Tratados
- Ouro (BigQuery) — subcamadas observadas:
    * TPAs: Ilíquidos + Real Estate (Líquidos = gap AS-IS)
    * Dados de Órgãos Reguladores: CMF, BACEN, CVM
    * Financeiro: General Ledger (Oracle Fusion GL Cayman)
    * Auditoria: SOX Controls

Processamento de PDF com Vertex AI/Gemini (CMF NoBanks PDF bronze/silver/gold) —
indica uso de GenAI para extração de documentos regulatórios.

Export bucket "lake_export_azure" — sinaliza fluxo bidirecional GCP ↔ Azure.

Multi-jurisdição confirmada:
- Brasil (BR): TPAs + BACEN + CVM
- Chile (CH): TPAs (Geneva/Derivados/Remuneraciones) + CMF
- Cayman (CA): Oracle Fusion GL (contábil — General Ledger)

Consumo final: Colaboradores + Governança de TI e Auditoria via Power BI,
camada semântica Excel e GA4BigQuery.
```

---

## Domínio 07 — Gestão & Metodologia

### Metodologia

> Entender como o time trabalha hoje evita propor processos incompatíveis e permite uma transição mais suave.

**Método usado:**
- [ ] Scrum
- [ ] Kanban
- [ ] SAFe
- [ ] XP (Extreme Programming)
- [ ] Waterfall
- [ ] Sem processo definido
- [X] Não sei

**Adoção real:**
- [ ] Seguido rigorosamente
- [ ] Adaptado ao contexto
- [ ] Existe no papel mas não na prática
- [X] Não sei

### Ferramentas

> As ferramentas já adotadas determinam integrações disponíveis e o nível de visibilidade que o projeto terá.

**Gestão de projetos:**
- [ ] Jira
- [ ] Linear
- [ ] ClickUp
- [ ] Azure Boards
- [ ] Asana
- [ ] Monday
- [ ] Trello
- [ ] Planilha
- [ ] Outra: {qual}
- [X] Não sei

> Observação: dado uso de Azure DevOps, é provável Azure Boards — A DESCOBRIR.

**Integrada com repo de código:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Documentação:**
- [ ] Confluence
- [ ] Notion
- [ ] Google Docs
- [X] SharePoint
- [ ] Wiki no repo (GitHub/GitLab)
- [ ] Outra: {qual}
- [ ] Nenhuma centralizada
- [ ] Não sei

> Observado: SharePoint listado como "Repositório corporativo de documentos" na legenda do Mapa DataLake v1.1 — é a plataforma de documentação/arquivos. README do IaC em markdown coexiste no repositório. Outras plataformas A DESCOBRIR.

**Ferramentas de BI / Analytics:**
- [X] Power BI (principal)
- [X] Excel (camada semântica)
- [X] GA4 + BigQuery (web analytics)
- [ ] Tableau
- [ ] Looker
- [X] Pentaho (legado)
- [ ] Outra
- [ ] Não sei

### Cerimônias praticadas

> Cerimônias praticadas revelam a maturidade ágil real do time e onde há espaço para melhoria de comunicação.

- [ ] Daily standup
- [ ] Sprint planning
- [ ] Sprint review / demo
- [ ] Retrospectiva
- [ ] Grooming / refinement
- [X] Não sei

**Stakeholders participam das demos:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Comunicação

> Os canais de comunicação afetam a velocidade de decisão e a rastreabilidade de acordos do projeto.

**Principal:**
- [ ] Slack
- [ ] Microsoft Teams
- [ ] Discord
- [ ] Google Chat
- [ ] Outro: {qual}
- [X] Não sei

> Observação: dado uso de ecossistema Microsoft (Azure DevOps, Key Vault, SharePoint), provável Teams — A DESCOBRIR.

**E-mail usado para:**
- [X] Aprovações formais
- [X] Comunicação com clientes
- [ ] Nada relevante
- [ ] Não sei

> Observado: e-mail é explicitamente listado como canal de ingestão de dados no Mapa DataLake v1.1 ("E-mails + Anexos"). Indica uso institucional de e-mail para processos de negócio (provavelmente Outlook/Exchange, dado ecossistema Microsoft).

**WhatsApp usado para:**
- [ ] Nada
- [ ] Comunicação informal
- [ ] Processos de negócio
- [X] Não sei

**Canais por projeto/time:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Aprovações

> Conhecer o fluxo de aprovações evita gargalos e define expectativas realistas de tempo para decisões.

**Quem aprova escopo:**
- [ ] PM / PO
- [ ] Diretoria
- [ ] Comitê
- [ ] Não tem processo definido
- [X] Não sei

**Quem aprova mudanças técnicas:**
- [ ] Tech Lead
- [ ] Comitê de Arquitetura
- [ ] Ninguém (autonomia do time)
- [X] Não sei

**Tempo médio para aprovação:**
- [ ] Horas
- [ ] Dias
- [ ] Semanas
- [X] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre gestão e metodologia que não se encaixe nos campos anteriores.

```
{a preencher pela área}
```

---

## Domínio 08 — Equipe & Capacidades

### Composição do time técnico

> O tamanho e perfil do time atual definem a capacidade de execução e as lacunas que precisam ser preenchidas.

| Role | Quantidade | Interno / Terceirizado | Senioridade predominante |
|------|-----------|----------------------|-------------------------|
| Dev Front-end | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Dev Back-end | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Dev Full-stack | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Dev Mobile | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| DevOps / SRE | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| QA | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Designer | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| PM | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Data / Analytics | A DESCOBRIR | Ao menos 3 usuários identificados | A DESCOBRIR |
| Segurança | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |

### Especialistas disponíveis

> Saber quais especialistas existem internamente ajuda a dimensionar contratações e consultorias externas necessárias.

- [ ] Segurança / InfoSec
- [ ] Mobile nativo (Swift, Kotlin)
- [ ] Cloud / infraestrutura
- [ ] Dados / ML
- [ ] Acessibilidade
- [ ] Performance
- [ ] UX Research
- [ ] Outro: {qual}
- [X] Não sei

> Observação: existência de IaC maduro em Terraform + GCP + Dataplex + BigQuery + Airflow + Vertex AI sugere perfil técnico com especialização em Cloud/Dados. A DESCOBRIR se é time interno ou fornecedor.

### Riscos de equipe

> Dependência de pessoas-chave e alta rotatividade são riscos diretos para a continuidade e sucesso do projeto.

**Bus factor = 1 em:** A DESCOBRIR

**Turnover últimos 12 meses:**
- [ ] < 5%
- [ ] 5-15%
- [ ] 15-30%
- [ ] > 30%
- [X] Não sei

**Principais causas de saída:**
- [ ] Salário / benefícios
- [ ] Cultura / gestão
- [ ] Burnout / sobrecarga
- [ ] Mercado aquecido
- [ ] Outro: {qual}
- [X] Não sei

### Disponibilidade

> A capacidade real do time define se o projeto pode ser absorvido internamente ou precisa de reforço externo.

**Capacidade ociosa para projeto novo:**
- [ ] > 50% do time disponível
- [ ] 20-50% do time
- [ ] < 20% do time
- [ ] Zero (time 100% alocado)
- [X] Não sei

**Modelo de trabalho:**
- [ ] 100% remoto
- [ ] Híbrido
- [ ] 100% presencial
- [X] Não sei

### Gaps de skills conhecidos

> Identificar lacunas técnicas antecipadamente permite planejar treinamentos ou contratações antes do início do projeto.

**Confirmado (Abr/2026):** **não existem gaps críticos de skills** no time atual. A capacidade técnica para o escopo do projeto novo está coberta.

| Skill necessária | Nível atual do time | Plano de mitigação |
|-----------------|--------------------|--------------------|
| — | Sem gaps críticos identificados | N/A |

### Notas adicionais

> Registre aqui qualquer informação sobre equipe e capacidades que não se encaixe nos campos anteriores.

```
Papéis identificados:
- Arquitetura e Produtividade Corporativa:
    * Fabio A. B. Rodrigues — autor do Mapa DataLake Patria v1.1 (Abr/2026)

Usuários identificados com acesso a datasets sensíveis (BACEN/COSIF Silver/Gold):
- lucas.barreto@patria.com — Lucas Barreto
- gcarbone@patria.com — Guillermo Carbone
- ben2312@patria.com — Daniela Benavides

Área consumidora explicitamente mapeada:
- Governança de TI e Auditoria — consome SOX Controls via Power BI

Email corporativo de contato do Airflow: datalake.gcp@patria.com (grupo/mailbox).

Consultor externo identificado (preenchendo este documento):
- fabio.rodrigues.consult@patria.com — Fabio Rodrigues
```

---

## Domínio 09 — Financeiro (OPEX / CAPEX / TCO)

### Modelo de custo

> Entender a estrutura de custos e orçamento disponível define a viabilidade financeira e o dimensionamento do projeto.

**Predominância:**
- [ ] CAPEX (investimento de capital)
- [X] OPEX (despesa operacional)
- [ ] Misto
- [ ] Não sei

> Observação: cloud pay-as-you-go por natureza é OPEX. Eventuais licenças Oracle podem ser CAPEX/licenciamento separado — A DESCOBRIR.

**Modelo Patria (confirmado Abr/2026):** OPEX de cloud é custeado por **fundo global corporativo** — projetos individuais **não arcam** com o custo dos recursos cloud que consomem. Discovery também acontece **após** aprovação e liberação de valores pelo comitê global; por isso não há "budget anual do projeto" a ser validado no formato convencional. O que interessa ao One-Pager/Executive é a **estimativa de consumo cloud do projeto** (BigQuery, Composer, Cloud Run, etc.) desconsiderando free tier — serve de referência, não de compromisso de cobrança.

**Budget anual de TI (corporativo, fundo global):** A DESCOBRIR

**Distribuição:**
- Operação / manutenção: A DESCOBRIR
- Projetos novos: A DESCOBRIR
- Inovação / R&D: A DESCOBRIR

**Já comprometido este ano:**
- [ ] < 50%
- [ ] 50-80%
- [ ] > 80%
- [X] Não sei (aplica-se ao fundo global; não rastreado por projeto)

### Custos de cloud

> Custos atuais de cloud servem como baseline para estimar o impacto financeiro incremental do novo projeto.

**Billing mensal médio (agregado 3 projetos GCP + rede):** A DESCOBRIR — mas não bloqueante para One-Pager (fundo global cobre OPEX). Necessário para Executive/Delivery como baseline e para estimativa de consumo do projeto novo (desconsiderando free tier).

**Maiores componentes:**
- [ ] Compute (VMs, containers)
- [ ] Storage
- [ ] Data transfer
- [ ] Managed services (DB, cache, etc.)
- [ ] Licenças (marketplace)
- [X] Não sei

> Inferência (apenas para hipótese, sem custo real): BigQuery (queries + storage), Cloud Composer (PRD), GCS (múltiplos buckets de data lake) e Artifact Registry provavelmente são os maiores componentes.

**Compromissos contratados (RI, Savings Plans):** A DESCOBRIR

**Rastreamento por projeto/time:**
- [ ] Sim, com tags
- [ ] Não
- [X] Não sei

> Observado: labels Terraform aplicados em recursos (`projectid=prj-2025-037`, `env`, `resource_name`), mas `cost_center` está como `not_defined` — rastreamento por cost center NÃO está efetivo.

### Custos recorrentes de fornecedores

> Contratos existentes podem gerar economia se renegociados ou risco se houver multas de rescisão antecipada.

| Fornecedor | Serviço | Custo mensal | Contrato até | Multa de rescisão |
|-----------|---------|-------------|-------------|-------------------|
| Google Cloud (GCP) | Cloud provider | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Microsoft (Azure) | Azure DevOps, Key Vault, AAD (presumido), SharePoint | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| Oracle | ERP Financials, HCM, SCM, AP | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| iLevel (S&P) | FP&A | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |
| GitHub | Repositório + Actions | A DESCOBRIR | A DESCOBRIR | A DESCOBRIR |

### Aprovação financeira

> Limites de alçada e tempo de aprovação definem a agilidade para contratar recursos e tomar decisões de investimento.

**Threshold por nível:**
- Gerente: até R$ A DESCOBRIR
- Diretor: até R$ A DESCOBRIR
- Board: acima de R$ A DESCOBRIR

**Tempo médio de aprovação:**
- [ ] Dias
- [ ] Semanas
- [ ] Meses
- [X] Não sei

**ROI/payback esperado para projetos de TI:**
- [ ] Sim, até {X} meses
- [X] Não definido (não obrigatório)
- [ ] Não sei

> Confirmado (Abr/2026): Discovery acontece **após** aprovação global do investimento pelo comitê; não é responsabilidade do One-Pager/Executive justificar ROI, **a menos que o briefing do projeto explicite essa exigência**.

### Notas adicionais

> Registre aqui qualquer informação sobre custos e financeiro que não se encaixe nos campos anteriores.

```
{a preencher pela área financeira / FinOps}
```

---

## Domínio 10 — Governança, Normas & Boas Práticas

### Catálogo de tecnologias

> Um catálogo de tecnologias aprovadas acelera decisões técnicas e evita retrabalho com homologações demoradas.

**Existe catálogo de tecnologias aprovadas:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Processo de homologação para tecnologia nova:**
- [ ] Comitê de arquitetura
- [ ] RFC (Request for Comments)
- [ ] Avaliação de segurança
- [ ] Não tem processo
- [X] Não sei

**Tempo médio de homologação:**
- [ ] Dias
- [ ] Semanas
- [ ] Meses
- [X] Não sei

### Change management

> Processos de gestão de mudanças definem como alterações em produção são aprovadas e quando podem ser realizadas.

**CAB (Change Advisory Board) existe:**
- [ ] Sim
- [ ] Não
- [X] Não sei

**Frequência do CAB:**
- [ ] Semanal
- [ ] Quinzenal
- [ ] Mensal
- [ ] N/A
- [X] Não sei

**Janela de manutenção definida:**
- [ ] Sim — quando: {ex.: domingo 2h-6h}
- [ ] Não
- [X] Não sei

**Aprovação de emergência para hotfixes:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Auditoria

> Requisitos de auditoria impactam o design de logging e rastreabilidade que o novo sistema precisa implementar.

**Trilha de auditoria obrigatória:**
- [X] Sim
- [ ] Não
- [ ] Não sei

> Observado: existência de repositório `sox-controls-repository` + lakes específicos de auditoria (`oracle_audittemp_bronze`) indicam requisitos SOX ativos.

**Ferramenta:**
- [ ] CloudTrail (AWS)
- [ ] Azure Activity Log
- [ ] Splunk
- [X] Outra: Google Cloud Audit Logs (padrão GCP)
- [ ] Nenhuma
- [ ] Não sei

### SLAs e SLOs

> SLAs e SLOs existentes estabelecem o patamar mínimo de qualidade que o novo projeto precisa igualar ou superar.

**SLA de disponibilidade definido:**
- [ ] Sim — valor: {ex.: 99.9%}
- [ ] Não
- [X] Não sei

**SLOs internos para latência/performance:**
- [ ] Sim
- [ ] Não
- [X] Não sei

### Propriedade intelectual

> Questões de propriedade de código e licenças open source afetam decisões de build vs. buy e riscos jurídicos.

**Código de projetos terceirizados pertence a:**
- [ ] Empresa contratante
- [ ] Software house / fornecedor
- [ ] Depende do contrato
- [ ] Não definido
- [X] Não sei

**Política de open source:**
- [ ] GPL bloqueado
- [ ] AGPL bloqueado
- [ ] Sem restrição
- [ ] Não definido
- [X] Não sei

### Arquitetura de referência

> Uma arquitetura de referência documentada acelera decisões técnicas e garante aderência aos padrões da empresa.

**Existe:**
- [X] Sim
- [ ] Não
- [ ] Não sei

> Observado: "Mapa DataLake Patria v1.1" (Abr/2026, AS-IS, NÃO EXAUSTIVO) é uma **arquitetura corporativa formal** de integrações de dados, autoria de Fabio A. B. Rodrigues. Cobertura completa de arquitetura corporativa (não-dados) — A DESCOBRIR.

**Documentada em:**
- [ ] Confluence
- [ ] Notion
- [ ] Google Docs
- [X] SharePoint (presumido — repositório corporativo)
- [ ] Wiki no repo (GitHub/GitLab)
- [X] Draw.io / diagrams.net (o mapa tem aparência de diagrama draw.io)
- [ ] Lucid Chart
- [ ] Não documentada
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre governança e normas que não se encaixe nos campos anteriores.

```
Evidências de governança madura no domínio de dados:
- Dataplex com lakes/zones estruturados (medallion architecture)
- IAM granular por dataset/zone/lake
- Safety checks explícitos na pipeline (proteção da VM Airflow)
- Segregação de ambientes (dev/hml/prd em projetos GCP separados)
- Service accounts dedicados por ambiente
- Workload Identity Federation (sem chaves estáticas)
- Row Access Policies no BigQuery (`corporate_all`)

A DESCOBRIR se existe governança equivalente fora do domínio de dados/IaC
(ex.: aplicações corporativas, endpoints, APIs).
```
