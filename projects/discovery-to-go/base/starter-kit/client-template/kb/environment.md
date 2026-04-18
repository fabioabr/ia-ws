---
title: "Environment Discovery"
description: "Cenário atual da empresa: infraestrutura, sistemas, stack, equipe, custos, normas e boas práticas."
category: knowledge-base
type: environment
status: pendente
company: "{COMPANY_NAME}"
filled-by: "{NAME}"
filled-date: "{DATE}"
last-updated: "{DATE}"
---

# Environment Discovery — {COMPANY_NAME}

> **Instruções:** Marque com `[X]` as opções que se aplicam. Use "N/A" para itens que não se aplicam e "A DESCOBRIR" para itens que você não sabe ainda. Este documento será usado como base de conhecimento (RAG) durante o discovery de projetos.

> Marque `[X] Não sei` quando não tiver a informação. O processo de discovery vai investigar esses pontos nas fases seguintes — é melhor admitir que não sabe do que chutar.

---

## Domínio 01 — Infraestrutura & Cloud

### Modelo de infraestrutura

> Saber onde a infra está hospedada define restrições de custo, latência, compliance e portabilidade para o novo projeto.

**Tipo:**
- [ ] Cloud pública
- [ ] Cloud privada
- [ ] Datacenter próprio
- [ ] Hospedagem compartilhada
- [ ] Híbrido
- [ ] Não sei

**Cloud provider principal:**
- [ ] AWS
- [ ] Azure
- [ ] GCP
- [ ] Oracle Cloud
- [ ] Outro: {qual}
- [ ] Nenhum (on-premise)
- [ ] Não sei

**Modelo de conta:**
- [ ] Single-account
- [ ] Multi-account
- [ ] N/A
- [ ] Não sei

**Billing:**
- [ ] Pay-as-you-go
- [ ] Reserved Instances
- [ ] Savings Plans
- [ ] Enterprise Agreement
- [ ] Outro: {qual}
- [ ] Não sei

**Budget alerts e cost tags:**
- [ ] Sim, configurados
- [ ] Não
- [ ] Não sei

### Rede e conectividade

> Conexões dedicadas entre escritórios e cloud afetam a arquitetura de integração e os requisitos de segurança.

**VPN site-to-site:**
- [ ] Sim — para: {destino}
- [ ] Não
- [ ] Não sei

**Direct Connect / ExpressRoute:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Restrições de firewall para registries/APIs externas:**
- [ ] Sim — quais: {descrever}
- [ ] Não
- [ ] Não sei

**Topologia de VPCs/VNets:** {descrever ou "N/A"}

### Regiões e disponibilidade

> A localização dos servidores impacta latência para usuários, custos de transferência e obrigações legais de residência de dados.

**Regiões em uso:** {ex.: us-east-1, sa-east-1}

**Residência de dados obrigatória no Brasil:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Disaster recovery:**
- [ ] Multi-AZ
- [ ] Multi-region
- [ ] Nenhum
- [ ] Não sei

### Ambientes e provisionamento

> Quantidade de ambientes e nível de automação determinam a velocidade e segurança de entregas do novo projeto.

**Ambientes existentes:**
- [ ] Desenvolvimento (dev)
- [ ] Staging
- [ ] UAT
- [ ] Produção
- [ ] Não sei

**Provisionamento:**
- [ ] Manual
- [ ] IaC — Terraform
- [ ] IaC — CloudFormation
- [ ] IaC — Pulumi
- [ ] IaC — Outro: {qual}
- [ ] Scripts ad-hoc
- [ ] Não sei

**IaC cobertura:**
- [ ] Total (todos os recursos)
- [ ] Parcial
- [ ] Nenhuma
- [ ] Não sei

### Observabilidade de infra

> Monitoramento e alertas determinam a capacidade de detectar e reagir a problemas antes que afetem os usuários.

**Ferramenta:**
- [ ] CloudWatch
- [ ] Datadog
- [ ] Grafana + Prometheus
- [ ] Zabbix
- [ ] Nagios
- [ ] Outra: {qual}
- [ ] Nenhuma
- [ ] Não sei

**Alertas configurados:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Dashboards operacionais:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Containers e orquestração

> O uso de containers influencia a estratégia de deploy, escalabilidade e a curva de aprendizado necessária para o time.

**Usa containers (Docker):**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Orquestrador:**
- [ ] Kubernetes (EKS)
- [ ] Kubernetes (AKS)
- [ ] Kubernetes (GKE)
- [ ] Kubernetes (self-managed)
- [ ] ECS
- [ ] Fargate
- [ ] Docker Compose
- [ ] Nenhum
- [ ] Não sei

**Se Kubernetes:**
- [ ] Namespaces configurados
- [ ] Resource quotas definidas
- [ ] Ingress controller ativo
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer particularidade de infraestrutura que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 02 — Sistemas Contratados & SaaS

### Inventário de sistemas ativos

> Mapear os sistemas contratados evita sobreposição de funcionalidades e identifica oportunidades de integração ou substituição.

| Sistema | Tipo | Fornecedor | Contrato | Renovação | Custo mensal | API disponível | SSO integrado |
|---------|------|-----------|----------|-----------|-------------|----------------|---------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

### Provedor de identidade (SSO)

> O IdP define como os usuários fazem login. Integrar com o SSO existente reduz fricção e aumenta segurança.

**IdP:**
- [ ] Azure AD / Entra ID
- [ ] Okta
- [ ] Google Workspace
- [ ] Auth0
- [ ] Keycloak
- [ ] Outro: {qual}
- [ ] Nenhum
- [ ] Não sei

**Protocolo:**
- [ ] SAML
- [ ] OIDC
- [ ] Ambos
- [ ] N/A
- [ ] Não sei

**Sistemas integrados ao SSO:** {listar}

**Sistemas com login separado:** {listar}

### Sistemas legados sem substituição planejada

> Sistemas legados são fontes frequentes de risco técnico, dependência de fornecedor e gargalos de integração.

| Sistema | Tecnologia | O que faz | Risco |
|---------|-----------|-----------|-------|
| | | | |
| | | | |

### Shadow IT identificado

> Ferramentas não oficiais revelam necessidades não atendidas e riscos de segurança que o novo projeto pode endereçar.

| Ferramenta | Quem usa | Para quê | Por que não usa o oficial |
|-----------|---------|---------|--------------------------|
| | | | |
| | | | |

### Notas adicionais

> Registre aqui qualquer informação sobre sistemas e SaaS que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 03 — Stack de Desenvolvimento

### Linguagens e frameworks

> Conhecer a stack atual permite avaliar compatibilidade, reuso de código e necessidade de capacitação do time.

| Camada | Linguagem | Framework | Observações |
|--------|-----------|-----------|-------------|
| Front-end | | | |
| Back-end | | | |
| Mobile | | | |
| Scripts/automação | | | |

### Versionamento

> O fluxo de versionamento impacta diretamente a velocidade de entrega, qualidade do código e colaboração entre devs.

**Plataforma:**
- [ ] GitHub
- [ ] GitLab
- [ ] Bitbucket
- [ ] Azure DevOps
- [ ] Outro: {qual}
- [ ] Não sei

**Plano/tier:**
- [ ] Free
- [ ] Team
- [ ] Enterprise
- [ ] Não sei

**Modelo de branching:**
- [ ] GitFlow
- [ ] Trunk-based development
- [ ] Feature branches
- [ ] Sem padrão definido
- [ ] Não sei

**PRs obrigatórios:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Aprovações mínimas por PR:**
- [ ] 0
- [ ] 1
- [ ] 2+
- [ ] Não sei

### Padrões e convenções

> Padrões de código e API garantem consistência entre times e reduzem atrito na integração entre serviços.

**Style guide documentado:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Linting automatizado:**
- [ ] ESLint
- [ ] Prettier
- [ ] Ruff / Black (Python)
- [ ] Outro: {qual}
- [ ] Nenhum
- [ ] Não sei

**Padrão de API:**
- [ ] REST
- [ ] GraphQL
- [ ] gRPC
- [ ] Ambos (REST + GraphQL)
- [ ] Sem padrão definido
- [ ] Não sei

**Versionamento de API:**
- [ ] URL (/v1, /v2)
- [ ] Header
- [ ] Nenhum
- [ ] Não sei

### Packages internos

> Bibliotecas internas compartilhadas aceleram o desenvolvimento e garantem padronização entre projetos.

**Registry privado:**
- [ ] npm (Verdaccio, GitHub Packages)
- [ ] PyPI
- [ ] Maven / Nexus
- [ ] NuGet
- [ ] Docker Registry
- [ ] Nenhum
- [ ] Não sei

**Packages compartilhados:** {listar: design system, SDK de auth, helpers, etc.}

### Bancos de dados

> O mapa de bancos de dados revela restrições de licenciamento, capacidade e compatibilidade para o novo projeto.

| Banco | Tipo | Ambiente | Gerenciado | Capacidade | Licença |
|-------|------|----------|-----------|-----------|---------|
| | | | | | |
| | | | | | |

### Mensageria e filas

> Brokers de mensageria definem como os sistemas se comunicam de forma assíncrona, impactando resiliência e escalabilidade.

**Brokers em uso:**
- [ ] RabbitMQ
- [ ] Apache Kafka
- [ ] AWS SQS / SNS
- [ ] Azure Service Bus
- [ ] Google Pub/Sub
- [ ] Redis (Pub/Sub ou Streams)
- [ ] Nenhum
- [ ] Não sei

### Débito técnico conhecido

> Débitos técnicos não resolvidos podem comprometer prazos e qualidade do novo projeto se não forem considerados desde o início.

1. {descrever}
2. {descrever}
3. {descrever}

### Notas adicionais

> Registre aqui qualquer informação sobre stack de desenvolvimento que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 04 — DevOps & Entrega Contínua

### CI/CD

> O nível de automação do pipeline determina a velocidade e confiabilidade com que código chega a produção.

**Ferramenta:**
- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] Jenkins
- [ ] CircleCI
- [ ] Azure Pipelines
- [ ] AWS CodePipeline
- [ ] Outra: {qual}
- [ ] Nenhuma
- [ ] Não sei

**Cobertura:**
- [ ] Todos os projetos
- [ ] Apenas alguns
- [ ] Nenhum
- [ ] Não sei

**Stages no pipeline:**
- [ ] Lint
- [ ] Test (unitários)
- [ ] Test (integração)
- [ ] Build
- [ ] Security scan (SAST/DAST)
- [ ] Deploy automático
- [ ] Deploy com aprovação
- [ ] Não sei

### Deploy

> A estratégia de deploy e rollback define o risco de cada entrega e a capacidade de reverter problemas rapidamente.

**Estratégia:**
- [ ] Automático em push/merge
- [ ] Manual por aprovação
- [ ] Release trains (periodicidade fixa)
- [ ] FTP / cópia manual
- [ ] Não sei

**Rollback:**
- [ ] Blue-green
- [ ] Canary
- [ ] Rolling update
- [ ] Feature flags
- [ ] Nenhum (redeploy versão anterior)
- [ ] Não sei

**Frequência média de deploy em produção:**
- [ ] Diário (ou mais)
- [ ] Semanal
- [ ] Mensal
- [ ] Trimestral ou menos
- [ ] Não sei

**Lead time (merge → produção):**
- [ ] Minutos
- [ ] Horas
- [ ] Dias
- [ ] Semanas
- [ ] Não sei

### Gestão de secrets

> A forma como credenciais e chaves são armazenadas é um dos maiores vetores de risco de segurança em projetos.

**Método:**
- [ ] HashiCorp Vault
- [ ] AWS Secrets Manager
- [ ] Azure Key Vault
- [ ] GCP Secret Manager
- [ ] Variáveis de ambiente (CI/CD)
- [ ] Hardcoded / .env commitado
- [ ] Outro: {qual}
- [ ] Não sei

### Observabilidade de aplicação

> APM, logs e tracing são essenciais para diagnosticar problemas em produção e medir a saúde real dos serviços.

**APM:**
- [ ] Datadog
- [ ] New Relic
- [ ] Dynatrace
- [ ] Application Insights
- [ ] Outra: {qual}
- [ ] Nenhuma
- [ ] Não sei

**Logging centralizado:**
- [ ] ELK (Elasticsearch + Logstash + Kibana)
- [ ] Grafana Loki
- [ ] CloudWatch Logs
- [ ] Splunk
- [ ] Outro: {qual}
- [ ] Nenhum
- [ ] Não sei

**Tracing distribuído:**
- [ ] OpenTelemetry
- [ ] Jaeger
- [ ] Zipkin
- [ ] Nenhum
- [ ] Não sei

### Gestão de incidentes

> Processos de resposta a incidentes impactam o tempo de recuperação e a maturidade operacional do novo projeto.

**Ferramenta de on-call:**
- [ ] PagerDuty
- [ ] Opsgenie
- [ ] Grafana OnCall
- [ ] Nenhuma
- [ ] Não sei

**Escalation policy definida:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Post-mortems documentados:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Runbooks existentes:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre DevOps e entrega contínua que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 05 — Segurança & Compliance

### Políticas

> Políticas de segurança documentadas definem as regras do jogo — sem elas, cada projeto inventa suas próprias práticas.

**Política de segurança da informação documentada:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Classificação de dados (público, interno, confidencial, restrito):**
- [ ] Sim, implementada
- [ ] Sim, apenas documentada
- [ ] Não
- [ ] Não sei

### Compliance regulatório

> Regulamentações aplicáveis definem requisitos obrigatórios que podem impactar arquitetura, prazos e custos do projeto.

**Regulamentações aplicáveis:**
- [ ] LGPD
- [ ] GDPR
- [ ] PCI-DSS
- [ ] HIPAA
- [ ] SOX
- [ ] BACEN (regulamentação bancária)
- [ ] Marco Civil da Internet
- [ ] ISO 27001
- [ ] SOC 2
- [ ] Nenhuma específica
- [ ] Outra: {qual}
- [ ] Não sei

### Privacidade

> Maturidade em privacidade determina se o projeto precisa criar processos de LGPD/GDPR do zero ou pode reaproveitar os existentes.

**DPO nomeado:**
- [ ] Sim — nome: {nome}
- [ ] Não
- [ ] Não sei

**ROPA (Record of Processing Activities) mantido:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Processo para direitos de titulares (acesso, retificação, exclusão):**
- [ ] Sim, automatizado
- [ ] Sim, manual
- [ ] Não
- [ ] Não sei

### Controle de acesso

> Controles de acesso mal configurados são a causa mais comum de vazamentos de dados e acessos indevidos.

**MFA obrigatório:**
- [ ] Sim, para todos
- [ ] Sim, apenas para admin/produção
- [ ] Não
- [ ] Não sei

**Princípio do menor privilégio:**
- [ ] Sim, aplicado sistematicamente
- [ ] Parcial
- [ ] Não
- [ ] Não sei

**Segregação de ambientes (dev não acessa produção):**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Offboarding automático revoga acessos:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Vulnerabilidades

> Identificar e corrigir vulnerabilidades de forma proativa evita incidentes de segurança que podem paralisar o negócio.

**Scan automatizado:**
- [ ] Snyk
- [ ] Dependabot
- [ ] SonarQube
- [ ] Trivy
- [ ] Outro: {qual}
- [ ] Nenhum
- [ ] Não sei

**Integrado ao CI/CD:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Pen test periódico:**
- [ ] Sim, anual
- [ ] Sim, semestral
- [ ] Nunca realizado
- [ ] Não sei

**SLA para correção de CVEs críticos:**
- [ ] 24h
- [ ] 7 dias
- [ ] 30 dias
- [ ] Sem SLA definido
- [ ] Não sei

### Criptografia

> Criptografia protege dados sensíveis contra interceptação e acesso não autorizado, sendo requisito de compliance.

**Dados em trânsito (TLS 1.2+):**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Dados em repouso (AES-256 ou equivalente):**
- [ ] Sim
- [ ] Não
- [ ] Parcial (apenas alguns sistemas)
- [ ] Não sei

**Gestão de chaves:**
- [ ] KMS (cloud provider)
- [ ] HashiCorp Vault
- [ ] HSM
- [ ] Manual
- [ ] Não definido
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre segurança e compliance que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 06 — Dados & Integrações

### Fontes autoritativas

> Saber qual sistema é dono de cada dado evita conflitos de sincronização e duplicação entre sistemas.

| Entidade | Sistema dono (source of truth) | Observações |
|----------|-------------------------------|-------------|
| Cliente | | |
| Produto | | |
| Pedido | | |
| Funcionário | | |
| Financeiro | | |

### Qualidade dos dados

> Dados inconsistentes ou incompletos comprometem relatórios, decisões e a confiabilidade do novo sistema.

**Dados duplicados entre sistemas:**
- [ ] Sim, frequente
- [ ] Raramente
- [ ] Não
- [ ] Não sei

**Encoding inconsistente:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Campos vazios em entidades críticas:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Integrações existentes

> O mapa de integrações revela dependências críticas e pontos de falha que o novo projeto precisa considerar.

| De | Para | Tipo | Volume | Monitoramento | Responsável |
|----|------|------|--------|---------------|-------------|
| | | | | | |
| | | | | | |

### Data warehouse / Data lake

> A existência de um data warehouse ou data lake influencia a estratégia de analytics e BI do novo projeto.

**Existe:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Ferramenta:**
- [ ] BigQuery
- [ ] Redshift
- [ ] Snowflake
- [ ] Databricks
- [ ] S3 + Athena
- [ ] Synapse Analytics
- [ ] Outro: {qual}
- [ ] Nenhum
- [ ] Não sei

**O que está populado:** {vendas, marketing, RH, etc.}

**Frequência de atualização:**
- [ ] Real-time / streaming
- [ ] Horário
- [ ] Diário
- [ ] Semanal
- [ ] Não sei

**Custo mensal:** {R$ X}

### ETL/ELT

> Pipelines de dados existentes podem ser reaproveitados ou precisam ser adaptados para alimentar o novo projeto.

**Ferramenta:**
- [ ] Apache Airflow
- [ ] dbt
- [ ] AWS Glue
- [ ] Informatica
- [ ] SSIS
- [ ] Talend
- [ ] Scripts manuais (Python, SQL)
- [ ] Nenhum
- [ ] Não sei

### Backup e recuperação

> Políticas de backup e RPO/RTO definem quanto dado pode ser perdido e em quanto tempo o sistema precisa voltar a funcionar.

**Frequência de backup:**
- [ ] Contínuo
- [ ] Horário
- [ ] Diário
- [ ] Semanal
- [ ] Não sei

**Retenção:**
- [ ] 7 dias
- [ ] 30 dias
- [ ] 90 dias
- [ ] 1 ano+
- [ ] Não sei

**Último teste de restore:** {data ou "nunca testado"}

**RPO definido:** {X horas ou "não definido"}

**RTO definido:** {X horas ou "não definido"}

### Notas adicionais

> Registre aqui qualquer informação sobre dados e integrações que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
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
- [ ] Não sei

**Adoção real:**
- [ ] Seguido rigorosamente
- [ ] Adaptado ao contexto
- [ ] Existe no papel mas não na prática
- [ ] Não sei

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
- [ ] Não sei

**Integrada com repo de código:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Documentação:**
- [ ] Confluence
- [ ] Notion
- [ ] Google Docs
- [ ] SharePoint
- [ ] Wiki no repo (GitHub/GitLab)
- [ ] Outra: {qual}
- [ ] Nenhuma centralizada
- [ ] Não sei

### Cerimônias praticadas

> Cerimônias praticadas revelam a maturidade ágil real do time e onde há espaço para melhoria de comunicação.

- [ ] Daily standup
- [ ] Sprint planning
- [ ] Sprint review / demo
- [ ] Retrospectiva
- [ ] Grooming / refinement
- [ ] Não sei

**Stakeholders participam das demos:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Comunicação

> Os canais de comunicação afetam a velocidade de decisão e a rastreabilidade de acordos do projeto.

**Principal:**
- [ ] Slack
- [ ] Microsoft Teams
- [ ] Discord
- [ ] Google Chat
- [ ] Outro: {qual}
- [ ] Não sei

**E-mail usado para:**
- [ ] Aprovações formais
- [ ] Comunicação com clientes
- [ ] Nada relevante
- [ ] Não sei

**WhatsApp usado para:**
- [ ] Nada
- [ ] Comunicação informal
- [ ] Processos de negócio
- [ ] Não sei

**Canais por projeto/time:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Aprovações

> Conhecer o fluxo de aprovações evita gargalos e define expectativas realistas de tempo para decisões.

**Quem aprova escopo:**
- [ ] PM / PO
- [ ] Diretoria
- [ ] Comitê
- [ ] Não tem processo definido
- [ ] Não sei

**Quem aprova mudanças técnicas:**
- [ ] Tech Lead
- [ ] Comitê de Arquitetura
- [ ] Ninguém (autonomia do time)
- [ ] Não sei

**Tempo médio para aprovação:**
- [ ] Horas
- [ ] Dias
- [ ] Semanas
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre gestão e metodologia que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 08 — Equipe & Capacidades

### Composição do time técnico

> O tamanho e perfil do time atual definem a capacidade de execução e as lacunas que precisam ser preenchidas.

| Role | Quantidade | Interno / Terceirizado | Senioridade predominante |
|------|-----------|----------------------|-------------------------|
| Dev Front-end | | | |
| Dev Back-end | | | |
| Dev Full-stack | | | |
| Dev Mobile | | | |
| DevOps / SRE | | | |
| QA | | | |
| Designer | | | |
| PM | | | |
| Data / Analytics | | | |
| Segurança | | | |

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
- [ ] Não sei

### Riscos de equipe

> Dependência de pessoas-chave e alta rotatividade são riscos diretos para a continuidade e sucesso do projeto.

**Bus factor = 1 em:** {listar áreas/sistemas onde só 1 pessoa sabe}

**Turnover últimos 12 meses:**
- [ ] < 5%
- [ ] 5-15%
- [ ] 15-30%
- [ ] > 30%
- [ ] Não sei

**Principais causas de saída:**
- [ ] Salário / benefícios
- [ ] Cultura / gestão
- [ ] Burnout / sobrecarga
- [ ] Mercado aquecido
- [ ] Outro: {qual}
- [ ] Não sei

### Disponibilidade

> A capacidade real do time define se o projeto pode ser absorvido internamente ou precisa de reforço externo.

**Capacidade ociosa para projeto novo:**
- [ ] > 50% do time disponível
- [ ] 20-50% do time
- [ ] < 20% do time
- [ ] Zero (time 100% alocado)
- [ ] Não sei

**Modelo de trabalho:**
- [ ] 100% remoto
- [ ] Híbrido
- [ ] 100% presencial
- [ ] Não sei

### Gaps de skills conhecidos

> Identificar lacunas técnicas antecipadamente permite planejar treinamentos ou contratações antes do início do projeto.

| Skill necessária | Nível atual do time | Plano de mitigação |
|-----------------|--------------------|--------------------|
| | | |
| | | |

### Notas adicionais

> Registre aqui qualquer informação sobre equipe e capacidades que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 09 — Financeiro (OPEX / CAPEX / TCO)

### Modelo de custo

> Entender a estrutura de custos e orçamento disponível define a viabilidade financeira e o dimensionamento do projeto.

**Predominância:**
- [ ] CAPEX (investimento de capital)
- [ ] OPEX (despesa operacional)
- [ ] Misto
- [ ] Não sei

**Budget anual de TI:** {R$ X ou "não informado"}

**Distribuição:**
- Operação / manutenção: {X%}
- Projetos novos: {X%}
- Inovação / R&D: {X%}

**Já comprometido este ano:**
- [ ] < 50%
- [ ] 50-80%
- [ ] > 80%
- [ ] Não sei

### Custos de cloud

> Custos atuais de cloud servem como baseline para estimar o impacto financeiro incremental do novo projeto.

**Billing mensal médio:** {R$ X}

**Maiores componentes:**
- [ ] Compute (VMs, containers)
- [ ] Storage
- [ ] Data transfer
- [ ] Managed services (DB, cache, etc.)
- [ ] Licenças (marketplace)
- [ ] Não sei

**Compromissos contratados (RI, Savings Plans):** {descrever ou "nenhum"}

**Rastreamento por projeto/time:**
- [ ] Sim, com tags
- [ ] Não
- [ ] Não sei

### Custos recorrentes de fornecedores

> Contratos existentes podem gerar economia se renegociados ou risco se houver multas de rescisão antecipada.

| Fornecedor | Serviço | Custo mensal | Contrato até | Multa de rescisão |
|-----------|---------|-------------|-------------|-------------------|
| | | | | |
| | | | | |

### Aprovação financeira

> Limites de alçada e tempo de aprovação definem a agilidade para contratar recursos e tomar decisões de investimento.

**Threshold por nível:**
- Gerente: até R$ {X}
- Diretor: até R$ {X}
- Board: acima de R$ {X}

**Tempo médio de aprovação:**
- [ ] Dias
- [ ] Semanas
- [ ] Meses
- [ ] Não sei

**ROI/payback esperado para projetos de TI:**
- [ ] Sim, até {X} meses
- [ ] Não definido
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre custos e financeiro que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```

---

## Domínio 10 — Governança, Normas & Boas Práticas

### Catálogo de tecnologias

> Um catálogo de tecnologias aprovadas acelera decisões técnicas e evita retrabalho com homologações demoradas.

**Existe catálogo de tecnologias aprovadas:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Processo de homologação para tecnologia nova:**
- [ ] Comitê de arquitetura
- [ ] RFC (Request for Comments)
- [ ] Avaliação de segurança
- [ ] Não tem processo
- [ ] Não sei

**Tempo médio de homologação:**
- [ ] Dias
- [ ] Semanas
- [ ] Meses
- [ ] Não sei

### Change management

> Processos de gestão de mudanças definem como alterações em produção são aprovadas e quando podem ser realizadas.

**CAB (Change Advisory Board) existe:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Frequência do CAB:**
- [ ] Semanal
- [ ] Quinzenal
- [ ] Mensal
- [ ] N/A
- [ ] Não sei

**Janela de manutenção definida:**
- [ ] Sim — quando: {ex.: domingo 2h-6h}
- [ ] Não
- [ ] Não sei

**Aprovação de emergência para hotfixes:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Auditoria

> Requisitos de auditoria impactam o design de logging e rastreabilidade que o novo sistema precisa implementar.

**Trilha de auditoria obrigatória:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Ferramenta:**
- [ ] CloudTrail (AWS)
- [ ] Azure Activity Log
- [ ] Splunk
- [ ] Outra: {qual}
- [ ] Nenhuma
- [ ] Não sei

### SLAs e SLOs

> SLAs e SLOs existentes estabelecem o patamar mínimo de qualidade que o novo projeto precisa igualar ou superar.

**SLA de disponibilidade definido:**
- [ ] Sim — valor: {ex.: 99.9%}
- [ ] Não
- [ ] Não sei

**SLOs internos para latência/performance:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

### Propriedade intelectual

> Questões de propriedade de código e licenças open source afetam decisões de build vs. buy e riscos jurídicos.

**Código de projetos terceirizados pertence a:**
- [ ] Empresa contratante
- [ ] Software house / fornecedor
- [ ] Depende do contrato
- [ ] Não definido
- [ ] Não sei

**Política de open source:**
- [ ] GPL bloqueado
- [ ] AGPL bloqueado
- [ ] Sem restrição
- [ ] Não definido
- [ ] Não sei

### Arquitetura de referência

> Uma arquitetura de referência documentada acelera decisões técnicas e garante aderência aos padrões da empresa.

**Existe:**
- [ ] Sim
- [ ] Não
- [ ] Não sei

**Documentada em:**
- [ ] Confluence
- [ ] ADRs no repositório
- [ ] Notion
- [ ] Draw.io / diagrams.net
- [ ] Lucid Chart
- [ ] Não documentada
- [ ] Não sei

### Notas adicionais

> Registre aqui qualquer informação sobre governança e normas que não se encaixe nos campos anteriores.

```
{espaço livre para observações}
```
