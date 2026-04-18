---
title: "Environment Discovery — Blueprint"
description: "Levantamento do cenário atual do cliente: infraestrutura, sistemas, stack, equipe, contratos, custos, normas e boas práticas. Objetivo: identificar o que pode ser reaproveitado e quais restrições o ambiente impõe sobre qualquer projeto novo."
category: project-blueprint
type: environment
status: rascunho
created: 2026-04-13
---

# Environment Discovery

## Descrição

Levantamento completo do cenário tecnológico, operacional e financeiro do cliente antes de iniciar qualquer projeto. Este blueprint não descreve um tipo de projeto — ele descreve o **contexto onde o projeto vai existir**. O objetivo é identificar o que pode ser reaproveitado (infra, ferramentas, contratos, equipe), quais restrições o ambiente impõe (compliance, normas, vendor lock-in), e onde estão os custos já comprometidos que afetam o TCO de qualquer solução nova.

Este documento deve ser executado **antes ou em paralelo à Etapa 01 (Inception)** de qualquer outro blueprint de projeto. As respostas aqui coletadas alimentam diretamente as decisões de Architecture (Etapa 05) e as estimativas de custo de todos os outros tipos de projeto.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

> **Nota:** Este blueprint usa **Domínios** em vez de Etapas. Cada domínio representa uma área do ambiente do cliente que precisa ser mapeada. A ordem é sugerida mas não obrigatória — o entrevistador pode percorrer os domínios na sequência que fizer mais sentido para cada cliente.

> [!tip]
> **Priorização por entregável.** Nem toda pergunta precisa estar respondida para cada entregável (One-Pager, Executive, Delivery). Use o template [question-priority-template.md](question-priority-template.md) para mapear o bitmap `[OP][EX][DR]` de cada pergunta — ele é lido pelo skill `deliverable-distiller` (Fase 3) como sugestão de densidade (não como filtro mecânico).

---

## Variantes de Ambiente

O perfil do ambiente do cliente determina a profundidade e a relevância de cada domínio. Ambientes mais maduros têm mais restrições (normas, contratos, aprovações), mas também mais recursos reaproveitáveis.

### V1 — Startup / Early Stage

Pouca ou nenhuma infraestrutura legada. Stack escolhida recentemente, geralmente por um fundador técnico. Poucos contratos SaaS, todos em planos gratuitos ou iniciais. Sem equipe de TI formal — os devs fazem tudo. Sem normas internas de compliance além do básico. O risco aqui não é complexidade, é a ausência de fundação: decisões de infra tomadas sob pressão sem considerar escala futura, secrets em planilhas, deploy manual, e zero observabilidade.

### V2 — PME em Crescimento

Infraestrutura mista — alguns serviços em cloud, alguns em hospedagem compartilhada, talvez um servidor dedicado. Contratos SaaS acumulados ao longo dos anos sem revisão (muitos subutilizados). Equipe de TI pequena (1-5 pessoas) que acumula funções de dev, infra e suporte. Normas internas existem mas são informais ("a gente sempre faz assim"). O risco é a dívida técnica invisível: integrações frágeis, processos manuais disfarçados de automação, e conhecimento concentrado em 1-2 pessoas.

### V3 — Enterprise On-Premise

Datacenter próprio ou colocation, com investimento pesado em hardware (CAPEX). Stack legada significativa (Java/.NET antigo, Oracle, SAP). Equipe de TI grande e especializada, com silos entre infra, dev, segurança e operações. Processos formais de change management, CAB (Change Advisory Board), e ciclos de aprovação longos. Contratos enterprise com SLAs rígidos e penalidades. O risco é a inércia: o ambiente é tão pesado que qualquer projeto novo precisa se adaptar às restrições existentes em vez de escolher a melhor solução.

### V4 — Enterprise Cloud-First

Já migrou para cloud (AWS, Azure, GCP) ou nasceu na nuvem. Billing consolidado com descontos por compromisso (Reserved Instances, Savings Plans). Equipe com cultura DevOps/SRE. Infrastructure as Code estabelecido (Terraform, Pulumi). Guardrails de segurança via policies automatizadas. O risco é o vendor lock-in: serviços proprietários do cloud provider (Lambda, Azure Functions, Cloud Run) que tornam migração futura cara, e billing que cresce silenciosamente sem governança de FinOps.

### V5 — Ambiente Regulado

Instituição financeira, saúde, governo, ou empresa com requisitos regulatórios pesados (BACEN, LGPD, HIPAA, SOX, PCI-DSS). Infraestrutura com controles de acesso rigorosos, segregação de ambientes, criptografia obrigatória, logs de auditoria imutáveis. Equipe de InfoSec/Compliance com poder de veto sobre decisões técnicas. Fornecedores precisam de certificação ou homologação. O risco é o custo oculto de compliance: cada decisão técnica precisa passar por aprovação de segurança, e fornecedores não homologados são bloqueados independente de mérito técnico.

---

## Domínio 01 — Infraestrutura & Cloud

- **Modelo de infraestrutura atual**: Identificar se o cliente opera em cloud pública (AWS, Azure, GCP), cloud privada, datacenter próprio, colocation, hospedagem compartilhada ou modelo híbrido. Cada modelo tem implicações diretas no custo, na velocidade de provisionamento e nas opções arquiteturais disponíveis para projetos novos. Um cliente 100% on-premise não pode usar serverless sem antes estabelecer uma ponte com cloud — o que muda completamente o timeline e o custo de qualquer projeto.

- **Contas e billing de cloud**: Se o cliente já tem conta em cloud provider, verificar: conta única ou multi-account (AWS Organizations, Azure Management Groups), modelo de billing (pay-as-you-go, Reserved Instances, Savings Plans, Enterprise Agreement), budget alerts configurados, e quem tem acesso à console de billing. Projetos novos lançados na mesma conta sem cost allocation tags se misturam no billing e se tornam impossíveis de rastrear. A existência de compromissos de reserva (RIs) já pagos pode tornar determinadas instâncias/regiões mais baratas que as alternativas ótimas.

- **Rede e conectividade**: Mapear a topologia de rede: VPCs/VNets existentes, peering entre contas/regiões, VPN site-to-site com escritórios ou datacenter, Direct Connect/ExpressRoute, e políticas de firewall. Projetos que precisam acessar sistemas on-premise a partir da cloud (ou vice-versa) dependem de conectividade já estabelecida — provisionamento de VPN ou link dedicado pode levar semanas a meses e dominar o timeline do projeto.

- **Regiões e disponibilidade**: Identificar em quais regiões geográficas a infraestrutura está implantada e se há estratégia de disaster recovery (multi-region, multi-AZ). Para projetos com requisitos de LGPD, dados de cidadãos brasileiros podem precisar residir em região brasileira (sa-east-1 na AWS, Brazil South na Azure). A ausência de região brasileira no setup atual pode exigir migração ou replicação antes do projeto começar.

- **Ambientes existentes**: Verificar quantos ambientes existem (dev, staging, UAT, produção) e como são provisionados. Ambientes criados manualmente sem IaC são custosos de replicar e propensos a drift de configuração. A existência de ambientes padronizados e reproduzíveis (via Terraform, CloudFormation, Pulumi) é um ativo reaproveitável que acelera o setup de qualquer projeto novo.

- **Observabilidade de infraestrutura**: Verificar se existe monitoramento de infra (CloudWatch, Azure Monitor, Datadog, Grafana + Prometheus), alertas configurados, e dashboards operacionais. A ausência de observabilidade significa que problemas de performance ou disponibilidade em projetos novos serão detectados por usuários reclamando, não por alertas automáticos — o que muda completamente o modelo operacional e o SLA possível.

### Perguntas

1. O ambiente atual é cloud pública, cloud privada, datacenter próprio, hospedagem compartilhada, ou híbrido? [fonte: TI, Infra] [impacto: Dev, DevOps, Arquiteto]
2. Qual cloud provider é usado (AWS, Azure, GCP) e há compromisso contratual (Reserved Instances, Enterprise Agreement)? [fonte: TI, Financeiro, Compras] [impacto: DevOps, Arquiteto, PM]
3. A conta de cloud é single-account ou multi-account com Organizations/Management Groups? [fonte: TI, Infra] [impacto: DevOps]
4. Existem budget alerts e cost allocation tags configurados para rastrear custos por projeto? [fonte: TI, FinOps, Financeiro] [impacto: PM, DevOps]
5. Qual é a topologia de rede atual — VPCs, peering, VPN site-to-site, Direct Connect? [fonte: Infra, Redes] [impacto: DevOps, Arquiteto]
6. Em quais regiões geográficas a infraestrutura está implantada e há exigência de residência de dados no Brasil? [fonte: Infra, Jurídico, Compliance] [impacto: DevOps, Arquiteto]
7. Existe estratégia de disaster recovery configurada (multi-AZ, multi-region, backup offsite)? [fonte: Infra, TI] [impacto: DevOps, Arquiteto]
8. Quantos ambientes existem (dev, staging, UAT, produção) e como são provisionados (manual, IaC, scripts)? [fonte: TI, DevOps interno] [impacto: DevOps, Dev]
9. Existe Infrastructure as Code (Terraform, CloudFormation, Pulumi, Ansible) em uso? Qual e com que cobertura? [fonte: DevOps interno, TI] [impacto: DevOps]
10. Qual ferramenta de monitoramento de infraestrutura está em uso (CloudWatch, Datadog, Grafana, Zabbix, Nagios)? [fonte: Infra, TI] [impacto: DevOps, Dev]
11. Existe orquestração de containers (Kubernetes, ECS, AKS) ou os workloads rodam em VMs/bare metal? [fonte: TI, DevOps interno] [impacto: Dev, DevOps, Arquiteto]
12. Qual é o processo para provisionar um novo servidor ou serviço — self-service, ticket para TI, ou CAB com aprovação? [fonte: TI, Infra] [impacto: PM, DevOps]
13. Existe alguma restrição de rede que bloqueie acesso a registries (npm, Docker Hub, PyPI) ou APIs externas? [fonte: Infra, Segurança] [impacto: Dev, DevOps]
14. Qual é o SLA de disponibilidade da infraestrutura atual e existe monitoramento de uptime? [fonte: TI, Infra] [impacto: DevOps, PM]
15. Há planos de migração de infra em andamento (on-prem para cloud, troca de provider) que impactariam um projeto novo? [fonte: TI, Diretoria] [impacto: Arquiteto, DevOps, PM]

---

## Domínio 02 — Sistemas Contratados & SaaS

- **Inventário de sistemas ativos**: Levantar todos os sistemas contratados em uso — ERP (SAP, Oracle, TOTVS), CRM (Salesforce, HubSpot, Pipedrive), RH (Gupy, ADP, Senior), financeiro (Conta Azul, Omie, SAP), e-mail e produtividade (Google Workspace, Microsoft 365), comunicação (Slack, Teams), e qualquer outro SaaS que a empresa paga. O inventário serve para identificar o que já existe e pode ser integrado em vez de ser substituído ou duplicado por um projeto novo — e para descobrir custos SaaS que o cliente pode não estar contabilizando como custo de TI.

- **Contratos e licenciamento**: Para cada sistema ativo, identificar: tipo de contrato (mensal, anual, enterprise agreement), data de renovação, cláusulas de lock-in, limite de usuários ou volume, e custo atual. Contratos prestes a vencer são oportunidades para renegociar ou migrar. Contratos com lock-in de 3 anos limitam a liberdade de escolha — se o cliente tem Oracle até 2028, não adianta recomendar PostgreSQL como "economia" porque o Oracle já está pago.

- **APIs e capacidade de integração**: Verificar quais sistemas exposem APIs (REST, SOAP, webhooks, SDK), qual o nível de documentação dessas APIs, e se há limites de rate limiting ou custos adicionais por chamada de API. Muitos ERPs e CRMs enterprise cobram extra por acesso à API ou limitam severamente o volume de chamadas — o que pode inviabilizar uma integração que no papel parecia simples. A qualidade da API existente determina se a integração será fluida ou se precisará de middleware/adaptador.

- **SSO e diretório de identidade**: Identificar se a empresa usa um provedor de identidade centralizado (Azure AD/Entra ID, Google Workspace, Okta, Auth0) e se os sistemas SaaS estão integrados via SSO (SAML, OIDC). A existência de SSO corporativo é um ativo reutilizável crucial — qualquer projeto novo com autenticação deve se integrar ao IdP existente em vez de criar login próprio. A ausência de SSO é um sinal de maturidade baixa e uma oportunidade de melhoria que pode ser embutida no projeto.

- **Sistemas legados sem substituição planejada**: Identificar sistemas antigos que a empresa depende mas que não têm plano de modernização — ERPs customizados em Delphi, planilhas Excel com macros VBA que controlam processos críticos, Access databases, ou sistemas desktop que só rodam em Windows XP. Esses sistemas não podem ser ignorados: qualquer projeto novo que interaja com dados ou processos cobertos por eles precisará de estratégia de integração (API wrapper, ETL, ou convivência manual).

- **Shadow IT e ferramentas não oficiais**: Levantar ferramentas que os times usam sem aprovação formal de TI — Notion, Trello, Airtable, Google Sheets compartilhados, WhatsApp para processos de negócio. Shadow IT revela necessidades reais que os sistemas oficiais não atendem. Entender o que os times estão "resolvendo por fora" pode reorientar o escopo do projeto novo — às vezes a necessidade real não é o sistema que o cliente pediu, mas automatizar o que hoje é feito em planilha.

### Perguntas

1. Quais sistemas ERP, CRM, RH, financeiro e de produtividade estão em uso hoje? [fonte: TI, Financeiro, cada departamento] [impacto: Arquiteto, Dev]
2. Existe um inventário centralizado de todos os sistemas SaaS contratados com custo e responsável? [fonte: TI, Financeiro, Compras] [impacto: PM, Arquiteto]
3. Quais desses contratos têm cláusula de lock-in ou renovação automática próxima? [fonte: Jurídico, Compras, Financeiro] [impacto: PM, Arquiteto]
4. Qual o custo mensal total estimado com assinaturas SaaS e licenças de software? [fonte: Financeiro, TI] [impacto: PM]
5. Quais sistemas exposem APIs (REST, SOAP, webhooks) e qual é a qualidade da documentação? [fonte: TI, Fornecedores de cada sistema] [impacto: Dev, Arquiteto]
6. Existe custo adicional para acesso à API de algum sistema (ex.: Salesforce API, SAP BTP)? [fonte: Fornecedores, Compras] [impacto: Dev, PM]
7. A empresa usa provedor de identidade centralizado (Azure AD, Okta, Google Workspace) com SSO? [fonte: TI, Segurança] [impacto: Dev, Arquiteto]
8. Quais sistemas já estão integrados ao SSO e quais têm login separado? [fonte: TI] [impacto: Dev]
9. Existem sistemas legados sem plano de substituição que o projeto novo precisará integrar? [fonte: TI, Operações, cada departamento] [impacto: Dev, Arquiteto]
10. Há ERPs ou sistemas customizados on-premise que só podem ser acessados pela rede interna? [fonte: TI, Infra] [impacto: DevOps, Dev]
11. Quais processos críticos de negócio dependem de planilhas Excel, Access, ou ferramentas manuais? [fonte: Operações, cada departamento] [impacto: Arquiteto, Dev, PO]
12. Existem ferramentas de shadow IT (Notion, Trello, Airtable, WhatsApp para processos) em uso pelos times? [fonte: Cada departamento, RH] [impacto: PO, Arquiteto]
13. Há sistemas em avaliação ou em processo de contratação que podem afetar o projeto novo? [fonte: TI, Compras, Diretoria] [impacto: Arquiteto, PM]
14. Os dados entre os sistemas atuais estão sincronizados ou existem silos com dados duplicados/conflitantes? [fonte: TI, Operações] [impacto: Dev, Arquiteto]
15. Existe alguma restrição contratual que limite integração, exportação de dados ou uso de APIs de sistemas contratados? [fonte: Jurídico, Compras, Fornecedores] [impacto: Dev, Arquiteto]

---

## Domínio 03 — Stack de Desenvolvimento

- **Linguagens e frameworks em uso**: Identificar todas as linguagens de programação e frameworks usados na empresa — front-end (React, Angular, Vue, Svelte), back-end (Node.js, Java/Spring, .NET, Python/Django, Go, PHP/Laravel), mobile (Swift, Kotlin, React Native, Flutter), e scripts/automação (Python, Bash, PowerShell). A stack existente é o fator número um na escolha de tecnologia para projetos novos: se a equipe trabalha com React e Node.js há 3 anos, recomendar Angular e Java sem justificativa forte é gerar curva de aprendizado desnecessária e risco de entrega.

- **Versionamento e repositórios**: Verificar qual plataforma de repositório é usada (GitHub, GitLab, Bitbucket, Azure DevOps), qual o modelo de branching (GitFlow, trunk-based, feature branches), e se há padrões de code review (PRs obrigatórios, aprovações mínimas, CI gates). A existência de uma organização GitHub ou GitLab com CI/CD configurado é um ativo reaproveitável direto — projetos novos podem herdar pipelines, templates de PR, e hooks existentes em vez de configurar do zero.

- **Padrões e convenções internas**: Verificar se existem padrões de código documentados — style guides, linting rules (ESLint, Prettier, RuboCop), naming conventions, padrões de API (REST vs. GraphQL, versionamento de API), e templates de projeto (boilerplates, cookiecutters, monorepo templates). Padrões documentados e aplicados automaticamente por tooling são um ativo de maturidade alta — projetos novos que seguem os mesmos padrões se integram ao ecossistema sem atrito. Ausência de padrões é um sinal de que cada projeto é um silo com convenções próprias.

- **Bibliotecas e pacotes internos**: Verificar se a empresa mantém packages internos publicados em registry privado (npm private, PyPI privado, Maven Nexus, NuGet privado) — componentes de UI compartilhados, SDKs de integração, helpers de autenticação. Pacotes internos maduros são o ativo mais valioso de reaproveitamento: um SDK que encapsula a autenticação com o IdP corporativo pode economizar semanas de desenvolvimento. A ausência de packages internos significa que cada projeto reinventa as mesmas integrações.

- **Banco de dados e persistência**: Mapear quais bancos de dados estão em uso — relacional (PostgreSQL, MySQL, SQL Server, Oracle), NoSQL (MongoDB, DynamoDB, Redis, Cassandra), search (Elasticsearch, OpenSearch), cache (Redis, Memcached), e filas (RabbitMQ, SQS, Kafka). A existência de um cluster PostgreSQL gerenciado (RDS, Cloud SQL) com backup e monitoring configurados é um ativo reaproveitável — mais barato e seguro do que provisionar instância nova. Licenças Oracle ou SQL Server Enterprise já pagas podem tornar economicamente inviável a migração para PostgreSQL mesmo que tecnicamente seja melhor.

- **Débito técnico conhecido**: Perguntar diretamente quais são os maiores problemas técnicos conhecidos — "o deploy demora 40 minutos", "o sistema legado cai toda segunda", "não temos testes automatizados", "o banco está sem índice e lento". Débito técnico existente é contexto obrigatório: um projeto novo que depende do sistema legado que "cai toda segunda" vai herdar essa instabilidade. Saber o débito antes de começar permite planejar mitigações ou definir pré-requisitos de correção.

### Perguntas

1. Quais linguagens de programação e frameworks são usados ativamente pela equipe hoje? [fonte: TI, Devs, Tech Lead] [impacto: Dev, Arquiteto]
2. Qual plataforma de repositório é usada (GitHub, GitLab, Bitbucket, Azure DevOps) e qual o plano/tier? [fonte: TI, DevOps] [impacto: Dev, DevOps]
3. Qual modelo de branching é seguido (GitFlow, trunk-based, feature branches) e PRs têm aprovação obrigatória? [fonte: Tech Lead, DevOps] [impacto: Dev]
4. Existem padrões de código documentados e aplicados automaticamente (ESLint, Prettier, style guides)? [fonte: Tech Lead, Dev] [impacto: Dev]
5. Há padrões de API definidos (REST, GraphQL, versionamento, paginação, autenticação de APIs)? [fonte: Tech Lead, Arquiteto interno] [impacto: Dev, Arquiteto]
6. A empresa mantém pacotes internos em registry privado (npm, PyPI, Maven, NuGet)? Quais? [fonte: Tech Lead, Dev] [impacto: Dev, Arquiteto]
7. Existem componentes de UI compartilhados (design system interno, biblioteca de componentes)? [fonte: Dev Front-end, Designer] [impacto: Dev, Designer]
8. Quais bancos de dados estão em uso (PostgreSQL, MySQL, Oracle, MongoDB, Redis, Elasticsearch)? [fonte: TI, DBA, Dev] [impacto: Dev, Arquiteto, DevOps]
9. Os bancos existentes têm capacidade ociosa que poderia ser usada por um projeto novo ou estão no limite? [fonte: DBA, Infra] [impacto: DevOps, Arquiteto]
10. Existem licenças de banco de dados pagas (Oracle, SQL Server Enterprise) com capacidade reaproveitável? [fonte: Financeiro, TI, Compras] [impacto: Arquiteto, PM]
11. Quais filas de mensageria ou brokers estão em uso (RabbitMQ, Kafka, SQS, Azure Service Bus)? [fonte: TI, Dev] [impacto: Dev, Arquiteto]
12. Existe dívida técnica conhecida que afetaria um projeto novo (deploy lento, testes ausentes, sistema instável)? [fonte: Tech Lead, Dev, TI] [impacto: Dev, PM, Arquiteto]
13. O time tem experiência com testes automatizados (unit, integration, e2e) e qual a cobertura média? [fonte: Tech Lead, QA] [impacto: Dev, QA]
14. Existe monorepo ou os projetos são repositórios individuais? Há templates/boilerplates reutilizáveis? [fonte: Tech Lead, DevOps] [impacto: Dev]
15. Quais são as maiores reclamações técnicas do time de desenvolvimento hoje? [fonte: Dev, Tech Lead] [impacto: Arquiteto, PM, Dev]

---

## Domínio 04 — DevOps & Entrega Contínua

- **Pipeline de CI/CD existente**: Verificar se a empresa tem pipelines de integração contínua e deploy contínuo configurados, qual ferramenta é usada (GitHub Actions, GitLab CI, Jenkins, CircleCI, Azure DevOps Pipelines, ArgoCD), e qual é a cobertura — todos os projetos passam pelo pipeline ou apenas alguns? A existência de pipelines maduros com stages de lint, test, build, e deploy é um ativo diretamente reaproveitável. A ausência de CI/CD significa que o primeiro sprint de qualquer projeto novo incluirá setup de infraestrutura de entrega.

- **Estratégia de deploy**: Identificar como os deploys acontecem — deploy contínuo em push para main, deploy manual por aprovação, release trains em datas fixas, ou "o João sobe por FTP". Verificar se há blue-green, canary, rolling update, ou se é tudo direto em produção. A estratégia de deploy existente define o risco de cada release e a velocidade de iteração possível — projetos novos herdam essa velocidade ou precisam de investimento para melhorá-la.

- **Gestão de secrets e configurações**: Verificar como secrets (API keys, tokens, senhas de banco) são gerenciados — ambiente (variáveis de ambiente), vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault), ou hardcoded no código ("faz 5 anos que está assim"). A gestão de secrets é um dos indicadores mais reveladores de maturidade operacional. Se secrets estão hardcoded ou em planilhas compartilhadas, o primeiro passo antes de qualquer projeto novo é resolver isso — não é possível operar com segurança sem gestão de secrets adequada.

- **Container e orquestração**: Verificar se a empresa usa containers (Docker) e como são orquestrados — Kubernetes (EKS, AKS, GKE, self-managed), ECS/Fargate, Docker Compose em VM, ou diretamente em VM sem containers. Se Kubernetes existe, verificar se há namespaces, resource quotas, ingress controllers, e service mesh (Istio, Linkerd) configurados. Um cluster Kubernetes existente e operacional é um dos ativos mais valiosos para reaproveitamento — projetos novos podem ser deployados como workloads adicionais no mesmo cluster.

- **Observabilidade de aplicação**: Verificar se existe monitoramento de aplicação além de infraestrutura — APM (Datadog, New Relic, Dynatrace), logging centralizado (ELK, Grafana Loki, CloudWatch Logs), tracing distribuído (Jaeger, Zipkin, OpenTelemetry). Observabilidade de aplicação é diferente de monitoramento de infra: infra te diz que o servidor está rodando, aplicação te diz que a API está retornando 500 em 3% das requests. Projetos novos sem observabilidade operam no escuro.

- **Gestão de incidentes e on-call**: Verificar se existe processo de resposta a incidentes — escalation policy, ferramenta de on-call (PagerDuty, Opsgenie, Grafana OnCall), runbooks documentados, post-mortems. A ausência de processo de incidentes significa que problemas em produção são resolvidos por quem estiver disponível, sem priorização ou documentação. Projetos novos entregues nesse contexto terão SLA efetivo de "depende de quem viu o problema primeiro".

### Perguntas

1. Existem pipelines de CI/CD configurados? Qual ferramenta (GitHub Actions, GitLab CI, Jenkins, Azure Pipelines)? [fonte: DevOps interno, TI] [impacto: DevOps, Dev]
2. Todos os projetos passam pelo pipeline de CI/CD ou apenas alguns? [fonte: DevOps interno, Tech Lead] [impacto: DevOps, Dev]
3. Como os deploys acontecem — automático em push para main, manual por aprovação, ou release trains? [fonte: DevOps interno, Tech Lead] [impacto: DevOps, PM]
4. Existe estratégia de deploy com rollback (blue-green, canary, rolling update) ou é direto em produção? [fonte: DevOps interno] [impacto: DevOps, Dev]
5. Como secrets são gerenciados — Vault, Secrets Manager, variáveis de ambiente, ou hardcoded? [fonte: DevOps interno, Segurança] [impacto: Dev, DevOps, Segurança]
6. A empresa usa containers (Docker) em produção? Se sim, qual orquestrador (Kubernetes, ECS, Compose)? [fonte: TI, DevOps interno] [impacto: DevOps, Dev, Arquiteto]
7. Se Kubernetes, existe cluster em produção com namespaces, quotas e ingress configurados? [fonte: DevOps interno] [impacto: DevOps, Dev]
8. Existe monitoramento de aplicação (APM) além de infra — Datadog, New Relic, Dynatrace? [fonte: TI, DevOps interno] [impacto: Dev, DevOps]
9. Existe logging centralizado (ELK, Loki, CloudWatch Logs) acessível aos desenvolvedores? [fonte: DevOps interno, TI] [impacto: Dev]
10. Existe tracing distribuído (Jaeger, OpenTelemetry) ou cada serviço loga isoladamente? [fonte: DevOps interno, Tech Lead] [impacto: Dev, Arquiteto]
11. Existe processo formal de resposta a incidentes com escalation policy e ferramenta de on-call? [fonte: TI, DevOps interno] [impacto: DevOps, PM]
12. Post-mortems são realizados e documentados após incidentes significativos? [fonte: Tech Lead, TI] [impacto: PM, Dev]
13. Qual é a frequência média de deploys em produção (diário, semanal, mensal, trimestral)? [fonte: DevOps interno, Tech Lead] [impacto: PM, Dev]
14. Existe environment promotion automático (dev → staging → prod) ou cada ambiente é independente? [fonte: DevOps interno] [impacto: DevOps, Dev]
15. Quanto tempo leva do merge na main até o código estar em produção (lead time de deploy)? [fonte: DevOps interno, Tech Lead] [impacto: PM, Dev]

---

## Domínio 05 — Segurança & Compliance

- **Políticas de segurança formais**: Verificar se a empresa tem política de segurança da informação documentada — classificação de dados, controle de acesso, criptografia, gestão de vulnerabilidades, e resposta a incidentes de segurança. Políticas formais definem o que é obrigatório para qualquer projeto novo: se a política exige criptografia em trânsito e em repouso, não é negociável — é pré-requisito. A ausência de políticas não significa ausência de risco; significa que o risco existe sem governança.

- **Compliance regulatório aplicável**: Identificar quais regulamentações se aplicam ao negócio do cliente — LGPD (dados pessoais de brasileiros), GDPR (se opera na EU), PCI-DSS (dados de cartão), HIPAA (dados de saúde), SOX (controles financeiros de empresas listadas), BACEN (instituições financeiras), Marco Civil da Internet. Cada regulamentação impõe requisitos técnicos específicos: PCI-DSS exige segmentação de rede, LGPD exige consentimento e portabilidade, SOX exige trilhas de auditoria imutáveis. Projetos que ignoram compliance no discovery descobrem os requisitos no QA — quando o custo de correção é 10x maior.

- **Controle de acesso e autenticação**: Mapear como o acesso a sistemas e dados é controlado — RBAC (Role-Based Access Control), ABAC (Attribute-Based), princípio do menor privilégio, revisão periódica de acessos, MFA obrigatório. Verificar se há segregação de ambientes (dev não acessa dados de produção), e se existe processo de onboarding/offboarding que revoga acessos automaticamente ao desligar funcionário. A ausência de controle de acesso adequado é um risco de segurança direto e uma não-conformidade em qualquer framework regulatório.

- **Gestão de vulnerabilidades**: Verificar se a empresa faz scan de vulnerabilidades (Snyk, Dependabot, SonarQube, OWASP ZAP), pen test periódico, e se há processo para corrigir vulnerabilidades descobertas com SLA definido. A existência de scan automatizado no pipeline de CI/CD é um ativo reaproveitável: projetos novos que entram no mesmo pipeline herdam a proteção automaticamente. A ausência de gestão de vulnerabilidades significa que dependências com CVEs conhecidos estão em produção sem ninguém saber.

- **Criptografia e proteção de dados**: Verificar se existe padrão de criptografia para dados em trânsito (TLS 1.2+) e em repouso (AES-256, KMS), como chaves de criptografia são gerenciadas (AWS KMS, Azure Key Vault, HSM), e se há classificação de dados (público, interno, confidencial, restrito) que determina o nível de proteção. Projetos que lidam com dados pessoais ou financeiros precisam dessas definições antes do setup — descobrir no meio do build que "tudo precisa ser criptografado" gera refatoração significativa.

- **DPO e processos de privacidade**: Verificar se a empresa tem DPO (Data Protection Officer) nomeado, se existe ROPA (Record of Processing Activities), e se há processo para atender direitos dos titulares (acesso, retificação, exclusão, portabilidade). Projetos que coletam ou processam dados pessoais precisam ser registrados no ROPA e ter fluxo de atendimento a direitos integrado. A ausência de DPO em empresa que trata dados pessoais é uma não-conformidade LGPD que deve ser sinalizada como risco.

### Perguntas

1. Existe política de segurança da informação documentada e atualizada? [fonte: Segurança, Compliance, TI] [impacto: Dev, DevOps, Arquiteto]
2. Quais regulamentações se aplicam ao negócio (LGPD, GDPR, PCI-DSS, HIPAA, SOX, BACEN)? [fonte: Jurídico, Compliance, DPO] [impacto: Arquiteto, Dev, PM]
3. A empresa tem DPO nomeado e ROPA (Record of Processing Activities) mantido? [fonte: Jurídico, DPO, RH] [impacto: Arquiteto, Dev]
4. Existe MFA obrigatório para acesso a sistemas corporativos e ambientes de produção? [fonte: Segurança, TI] [impacto: DevOps, Dev]
5. O princípio do menor privilégio é aplicado — devs têm acesso apenas ao que precisam? [fonte: Segurança, TI] [impacto: DevOps]
6. Existe segregação de ambientes — dev acessa dados de produção? [fonte: Segurança, TI, DBA] [impacto: DevOps, Dev]
7. O processo de offboarding revoga automaticamente acessos quando um funcionário é desligado? [fonte: RH, TI, Segurança] [impacto: Segurança]
8. Existe scan de vulnerabilidades automatizado (Snyk, Dependabot, SonarQube) no pipeline de CI/CD? [fonte: DevOps interno, Segurança] [impacto: Dev, DevOps]
9. Pen tests são realizados periodicamente? Com qual frequência e por quem (interno ou terceiro)? [fonte: Segurança, TI] [impacto: Dev, PM]
10. Qual o SLA para correção de vulnerabilidades críticas descobertas (CVEs, pen test findings)? [fonte: Segurança, TI] [impacto: Dev, PM]
11. Existe padrão de criptografia para dados em trânsito (TLS 1.2+) e em repouso (AES-256)? [fonte: Segurança, Infra] [impacto: Dev, DevOps, Arquiteto]
12. Como chaves de criptografia são gerenciadas (KMS, Vault, HSM, ou manual)? [fonte: Segurança, Infra] [impacto: DevOps, Dev]
13. Existe classificação formal de dados (público, interno, confidencial, restrito)? [fonte: Segurança, Compliance] [impacto: Arquiteto, Dev]
14. Existe processo para atender direitos de titulares LGPD (acesso, retificação, exclusão, portabilidade)? [fonte: DPO, Jurídico] [impacto: Dev, Arquiteto]
15. Fornecedores e SaaS externos passam por avaliação de segurança antes da contratação? [fonte: Segurança, Compras] [impacto: Arquiteto, PM]

---

## Domínio 06 — Dados & Integrações

- **Fontes de dados e ownership**: Mapear quais são as fontes de dados autoritativas da empresa — qual sistema é o "dono" de cada entidade (cliente, produto, pedido, funcionário). É comum que a mesma entidade exista em múltiplos sistemas com dados conflitantes — o CRM tem um endereço do cliente, o ERP tem outro, e a planilha de vendas tem um terceiro. Identificar a fonte autoritativa de cada entidade é pré-requisito para qualquer projeto que consuma ou produza dados — sem isso, o projeto perpetua inconsistências.

- **Formatos e qualidade dos dados**: Verificar em que formato os dados estão armazenados (SQL, CSV, JSON, XML, planilhas), qual a qualidade percebida (dados duplicados, campos vazios, encoding inconsistente, datas em formatos diferentes), e se existe processo de limpeza ou enriquecimento. Dados de baixa qualidade são o problema mais subestimado em projetos de integração e analytics — um pipeline tecnicamente perfeito que ingere dados sujos produz resultados sujos. O esforço de limpeza pode facilmente superar o esforço de desenvolvimento.

- **Integrações existentes**: Mapear todas as integrações ativas entre sistemas — sincrônicas (API call direto), assíncronas (mensageria, webhooks), batch (ETL noturno, arquivo SFTP), e manuais (alguém exporta CSV e importa em outro sistema). Para cada integração, identificar: quem mantém, se tem monitoramento, o que acontece quando falha, e qual o volume de dados trafegado. Integrações existentes que funcionam são ativos reutilizáveis. Integrações frágeis (sem retry, sem monitoramento, sem alerta de falha) são riscos que o projeto novo pode herdar.

- **Data lake ou data warehouse existente**: Verificar se a empresa tem repositório centralizado de dados para analytics (BigQuery, Redshift, Snowflake, Databricks, data lake no S3). Se existe, verificar: o que está populado, qual a frequência de atualização, quem consome, e qual o custo mensal. A existência de um DW/lake pode eliminar a necessidade de o projeto novo construir seu próprio repositório de dados — bastando adicionar novas fontes ao pipeline existente.

- **Governança de dados**: Verificar se existe catálogo de dados (dbt docs, DataHub, Amundsen), política de retenção (quanto tempo dados são mantidos e quando são purgados), masking para dados sensíveis em ambientes não-produtivos, e processo para solicitar acesso a datasets. Governança de dados madura indica que o projeto novo terá regras claras para seguir. Ausência de governança indica que dados de produção podem estar em laptops de analistas e em queries de Tableau sem controle de acesso.

- **Backup e recuperação de dados**: Verificar a estratégia de backup — frequência (diário, horário, contínuo), retenção (7 dias, 30 dias, 1 ano), teste de restore (quando foi o último), e RPO/RTO definidos para cada sistema. Projetos novos que dependem de dados existentes precisam de garantia de que esses dados estão protegidos. Um projeto que integra com o ERP assume implicitamente que o ERP tem backup confiável — se não tem, o risco é compartilhado.

### Perguntas

1. Quais são as fontes de dados autoritativas para cada entidade principal (cliente, produto, pedido, funcionário)? [fonte: TI, cada departamento, DBA] [impacto: Arquiteto, Dev]
2. Existem dados duplicados ou conflitantes entre sistemas diferentes para a mesma entidade? [fonte: TI, Operações] [impacto: Dev, Arquiteto]
3. Qual a qualidade percebida dos dados — campos vazios, encoding inconsistente, duplicatas frequentes? [fonte: TI, Analistas de dados, Operações] [impacto: Dev, Arquiteto]
4. Quais integrações entre sistemas existem hoje e como funcionam (API, mensageria, ETL batch, CSV manual)? [fonte: TI, DevOps interno] [impacto: Dev, Arquiteto]
5. As integrações existentes têm monitoramento, retry automático e alerta de falha? [fonte: TI, DevOps interno] [impacto: DevOps, Dev]
6. Existe data lake ou data warehouse centralizado (BigQuery, Redshift, Snowflake, Databricks)? [fonte: TI, Data Team] [impacto: Arquiteto, Dev]
7. Se existe DW/lake, o que está populado, com qual frequência é atualizado e quem consome? [fonte: Data Team, TI] [impacto: Arquiteto, Dev]
8. Existe catálogo de dados documentando tabelas, colunas, owners e SLAs de qualidade? [fonte: Data Team, TI] [impacto: Dev, Arquiteto]
9. Existe política de retenção de dados — quanto tempo dados são mantidos e quando são purgados? [fonte: Jurídico, Compliance, TI] [impacto: Arquiteto, Dev]
10. Dados sensíveis são mascarados em ambientes de staging/dev ou cópias completas de produção são usadas? [fonte: Segurança, DBA, TI] [impacto: Dev, Segurança]
11. Qual a estratégia de backup — frequência, retenção, e quando foi o último teste de restore? [fonte: DBA, Infra, TI] [impacto: DevOps]
12. Qual é o RPO (Recovery Point Objective) e RTO (Recovery Time Objective) definidos para os sistemas principais? [fonte: TI, Diretoria] [impacto: DevOps, Arquiteto]
13. Existem processos de ETL/ELT em produção? Qual ferramenta (Airflow, dbt, Glue, Informatica, SSIS)? [fonte: Data Team, TI] [impacto: Dev, Arquiteto]
14. Há restrições de compliance sobre onde dados podem ser armazenados (residência, soberania de dados)? [fonte: Jurídico, DPO, Compliance] [impacto: Arquiteto, DevOps]
15. Existem APIs internas documentadas para acesso a dados ou cada time faz queries diretas no banco? [fonte: Tech Lead, TI] [impacto: Arquiteto, Dev]

---

## Domínio 07 — Gestão & Metodologia

- **Metodologia de gestão de projetos**: Identificar como projetos são gerenciados — Scrum, Kanban, SAFe, waterfall, ou "sem processo definido". Verificar o nível de adoção real (não o que está no slide da diretoria, mas o que realmente acontece no dia a dia). A metodologia existente define a cadência de entregas, a forma de priorização, e o nível de autonomia do time. Projetos novos que tentam impor metodologia diferente da cultura existente encontram resistência — é mais produtivo adaptar-se ao que funciona e melhorar incrementalmente.

- **Ferramentas de gestão**: Mapear as ferramentas usadas para gestão de projetos e tarefas — Jira, Linear, ClickUp, Azure DevOps Boards, Asana, Monday, Trello, ou planilha Excel. Verificar se há integração com repositório de código (PR linkado ao ticket) e se existe visibilidade para stakeholders (dashboards, reports). A ferramenta existente pode ser reaproveitada para o projeto novo — criar um workspace ou board no mesmo tool reduz atrito e mantém a visibilidade centralizada.

- **Cadência de cerimônias**: Verificar quais cerimônias são praticadas — daily standup, sprint planning, sprint review/demo, retrospectiva, grooming/refinement — e com qual frequência. Verificar se stakeholders participam das demos e se o feedback é incorporado no sprint seguinte. A cadência existente é o ritmo real do time — projetos novos devem se encaixar nesse ritmo ou propor mudanças com justificativa clara.

- **Documentação de projetos**: Verificar onde e como a documentação é mantida — Confluence, Notion, Google Docs, SharePoint, README no repo, ou "não documentamos". Verificar se existe padrão de documentação (ADRs, RFCs, design docs) e se a documentação é mantida atualizada ou é escrita uma vez e abandonada. A forma como a empresa documenta determina como o conhecimento do projeto novo será preservado após a entrega.

- **Comunicação e colaboração**: Mapear os canais de comunicação — Slack, Teams, Discord, e-mail, WhatsApp — e quais são usados para o quê (alertas técnicos no Slack, aprovações por e-mail, discussões informais no WhatsApp). Verificar se há canais dedicados por projeto ou time. A estrutura de comunicação existente é onde o projeto novo vai operar — criar canais novos em plataforma diferente da usada pela empresa é garantia de que ninguém vai ver as mensagens.

- **Processo de aprovação e governança**: Verificar como decisões são tomadas — quem aprova orçamento, quem aprova escopo, quem aprova mudanças técnicas. Verificar se existe CAB (Change Advisory Board), comitê de arquitetura, ou processo formal de RFC/ADR para decisões técnicas significativas. Processos de aprovação lentos não são elimináveis por um projeto novo — precisam ser mapeados e incorporados no cronograma como lead time real.

### Perguntas

1. Qual metodologia de gestão de projetos é usada na prática (Scrum, Kanban, SAFe, waterfall, nenhuma)? [fonte: PM, Tech Lead, Diretoria] [impacto: PM]
2. Qual ferramenta de gestão de projetos está em uso (Jira, Linear, ClickUp, Azure Boards, planilha)? [fonte: PM, TI] [impacto: PM]
3. A ferramenta de gestão está integrada com o repositório de código (PR linkado ao ticket)? [fonte: DevOps interno, PM] [impacto: Dev, PM]
4. Quais cerimônias são praticadas regularmente (daily, planning, review, retro, refinement)? [fonte: PM, Tech Lead] [impacto: PM, Dev]
5. Stakeholders participam das sprint reviews/demos e o feedback é incorporado? [fonte: PM, Diretoria] [impacto: PM, PO]
6. Onde a documentação técnica e de projeto é mantida (Confluence, Notion, Google Docs, SharePoint, repo)? [fonte: PM, Tech Lead, TI] [impacto: Dev, PM]
7. Existe padrão de documentação técnica (ADRs, RFCs, design docs) seguido pelo time? [fonte: Tech Lead, Arquiteto interno] [impacto: Dev, Arquiteto]
8. A documentação é mantida atualizada ou é escrita uma vez e abandonada? [fonte: Dev, PM, Tech Lead] [impacto: PM]
9. Quais canais de comunicação são usados para o quê (Slack, Teams, e-mail, WhatsApp)? [fonte: PM, TI, qualquer departamento] [impacto: PM]
10. Existe canal dedicado por projeto/time ou tudo é misturado em canais genéricos? [fonte: PM, TI] [impacto: PM]
11. Qual é o processo de aprovação de orçamento para projetos novos (quem aprova, quanto demora)? [fonte: Financeiro, Diretoria] [impacto: PM]
12. Existe CAB (Change Advisory Board) ou comitê de arquitetura que aprova mudanças técnicas? [fonte: TI, Diretoria] [impacto: Arquiteto, PM]
13. Quanto tempo leva em média para uma decisão de escopo ou mudança ser aprovada? [fonte: PM, Diretoria] [impacto: PM]
14. Como a priorização de demandas funciona — backlog centralizado, cada área pede direto, ou político? [fonte: PM, Diretoria, cada departamento] [impacto: PM, PO]
15. Existe processo de lessons learned ou post-mortem após a conclusão de projetos? [fonte: PM, Tech Lead] [impacto: PM]

---

## Domínio 08 — Equipe & Capacidades

- **Estrutura do time técnico**: Mapear a composição da equipe — quantos devs (front, back, full-stack, mobile), quantos DevOps/SRE, quantos QA, quantos designers, quantos PMs, quantos analistas de dados. Verificar se o time é interno, terceirizado, ou misto. A capacidade real do time define o que é possível entregar em paralelo com o projeto novo — se o time já está 100% alocado em manutenção e projetos em andamento, o projeto novo precisa de headcount adicional ou redução de escopo em outro lugar.

- **Senioridade e especialização**: Identificar o nível de experiência do time — juniors que precisam de mentoria constante, plenos que entregam com autonomia moderada, e seniors que podem tomar decisões arquiteturais. Verificar se existem especialistas em áreas críticas para o projeto novo (segurança, performance, acessibilidade, mobile, dados). A composição de senioridade define se o projeto pode ser executado com autonomia ou se precisa de acompanhamento técnico externo.

- **Conhecimento concentrado (bus factor)**: Identificar se existem pessoas que são "ponto único de falha" — o único que sabe como o deploy funciona, o único que entende o sistema legado, o único que tem acesso ao servidor de produção. Bus factor 1 em qualquer área crítica é risco operacional direto. Projetos novos que dependem dessas pessoas herdam o risco — se a pessoa ficar doente, o projeto para.

- **Disponibilidade e alocação atual**: Verificar quanto do tempo do time está disponível para o projeto novo — se já estão 100% alocados em manutenção, suporte e outros projetos, a alocação para o projeto novo é zero sem realocação. Verificar se existe pool de desenvolvedores alocáveis ou se cada pessoa está atribuída a um produto/sistema fixo. A disponibilidade real (não a teórica) define o timeline possível.

- **Capacitação e treinamento**: Verificar se a empresa investe em capacitação — budget de treinamento, conferências, certificações, tempo alocado para aprendizado. Se o projeto novo exige skills que o time não tem (ex.: Kubernetes, React Native, ML), verificar se há disposição e tempo para treinamento antes do kick-off ou se é necessário contratar. A gap de skills não mapeado se transforma em atraso de entrega — o dev que nunca usou Kubernetes não vai configurar um cluster em produção no primeiro sprint.

- **Turnover e retenção**: Verificar a taxa de turnover do time técnico nos últimos 12 meses e as causas (mercado, salário, cultura, burnout). Projetos longos (6+ meses) em ambientes com turnover alto têm risco real de perder pessoas-chave durante a execução — e a substituição de um dev que conhece o contexto custa meses de ramp-up. Turnover alto também pode indicar problemas culturais que afetarão o projeto novo.

### Perguntas

1. Qual é a composição atual do time técnico (devs, DevOps, QA, designers, PMs, analistas)? [fonte: RH, Tech Lead, Diretoria] [impacto: PM, Arquiteto]
2. O time é interno, terceirizado ou misto? Se terceirizado, qual empresa e tipo de contrato? [fonte: RH, Compras, Diretoria] [impacto: PM]
3. Qual é a distribuição de senioridade (junior, pleno, senior) no time técnico? [fonte: Tech Lead, RH] [impacto: PM, Arquiteto]
4. Existem especialistas em áreas críticas para o projeto (segurança, mobile, dados, cloud, acessibilidade)? [fonte: Tech Lead, RH] [impacto: Arquiteto, PM]
5. Existem pessoas que são "ponto único de falha" para sistemas ou processos críticos (bus factor = 1)? [fonte: Tech Lead, TI] [impacto: PM, Arquiteto]
6. Quanto do tempo do time está disponível para um projeto novo vs. manutenção e outros projetos? [fonte: PM, Tech Lead, Diretoria] [impacto: PM]
7. O time já trabalhou junto antes ou será formado para este projeto? [fonte: PM, RH, Tech Lead] [impacto: PM]
8. O time tem experiência com as tecnologias previstas para o projeto novo? [fonte: Tech Lead, Dev] [impacto: Arquiteto, PM]
9. Se há gap de skills, existe budget e tempo para treinamento antes do kick-off? [fonte: RH, Financeiro, Diretoria] [impacto: PM]
10. Qual é a taxa de turnover do time técnico nos últimos 12 meses? [fonte: RH] [impacto: PM]
11. Quais são as principais causas de saída — salário, cultura, burnout, mercado? [fonte: RH, Tech Lead] [impacto: PM, Diretoria]
12. O time tem experiência com trabalho remoto, híbrido ou é 100% presencial? [fonte: RH, Tech Lead] [impacto: PM]
13. Existem rituais de compartilhamento de conhecimento (tech talks, pair programming, code review)? [fonte: Tech Lead, Dev] [impacto: PM, Dev]
14. O time tem autonomia para tomar decisões técnicas ou precisa de aprovação para cada escolha? [fonte: Tech Lead, Diretoria] [impacto: Dev, Arquiteto]
15. Existe plano de contratação em andamento que possa reforçar o time para o projeto novo? [fonte: RH, Diretoria] [impacto: PM]

---

## Domínio 09 — Financeiro (OPEX / CAPEX / TCO)

- **Modelo de custo atual de TI**: Identificar como os custos de TI estão distribuídos entre CAPEX (servidores, licenças perpétuas, hardware) e OPEX (assinaturas SaaS, cloud, manutenção). O modelo de custo define como o projeto novo será financiado e justificado — empresas com cultura CAPEX forte podem resistir a modelos pay-as-you-go de cloud, mesmo que sejam mais econômicos, porque o processo de aprovação de OPEX é diferente do de CAPEX. Entender essa dinâmica evita propor soluções financeiramente inviáveis do ponto de vista de aprovação interna.

- **Budget de TI anual e alocação**: Verificar qual é o budget anual de TI, como está distribuído (operação vs. projetos novos vs. inovação), e quanto já está comprometido. Um projeto novo que custa R$500k é viável se o budget de projetos é R$2M e só R$800k estão comprometidos. É inviável se o budget é R$600k e já está 100% alocado. Essa informação define o escopo máximo possível antes de qualquer discussão técnica.

- **Custos de cloud atuais e projeção**: Se o cliente já usa cloud, obter o billing mensal atual (ou médio dos últimos 6 meses), identificar os maiores custos (compute, storage, data transfer, managed services), e verificar se existe análise de custo por projeto/time. Projetos novos que adicionam workloads à cloud precisam estimar o custo incremental — não o custo total. Se o cluster Kubernetes já existe e tem capacidade ociosa, o custo incremental de um novo serviço é próximo de zero. Se está no limite, o custo inclui upgrade do cluster.

- **Contratos de suporte e manutenção**: Levantar custos recorrentes de suporte — contratos de suporte de fornecedores (Oracle Support, SAP Maintenance, Microsoft Premier), SLAs de hospedagem, contratos de agência ou software house para manutenção de sistemas. Esses custos são compromissos já assumidos que não podem ser realocados no curto prazo. Um projeto novo que propõe substituir o sistema mantido pela agência precisa considerar que o contrato da agência pode ter multa de rescisão ou aviso prévio.

- **TCO de soluções comparáveis**: Verificar se a empresa já calculou TCO de projetos anteriores ou de soluções consideradas. Se o cliente avaliou 3 plataformas de e-commerce antes de decidir construir, os TCOs comparativos são contexto valioso. Se nunca calculou TCO, o projeto novo precisa incluir esse exercício como entregável — e o entrevistador deve mapear os componentes de custo que o cliente normalmente esquece (custo de time, custo de oportunidade, custo de manutenção pós-launch).

- **Processo de aprovação financeira**: Verificar quem aprova investimentos em TI, qual o threshold para cada nível de aprovação (gerente até R$50k, diretor até R$200k, board acima), e quanto tempo o processo leva. Projetos que ultrapassam o threshold do patrocinador direto precisam de aprovação de nível superior — o que pode adicionar semanas ou meses ao timeline antes do kick-off técnico. Esse lead time de aprovação financeira raramente é contabilizado no cronograma.

### Perguntas

1. Qual é o modelo de custo predominante de TI — CAPEX (hardware, licenças perpétuas) ou OPEX (assinaturas, cloud)? [fonte: Financeiro, TI, CFO] [impacto: PM, Arquiteto]
2. Qual é o budget anual de TI e como está distribuído (operação, projetos novos, inovação)? [fonte: Financeiro, CTO, CFO] [impacto: PM]
3. Quanto do budget de TI para este ano já está comprometido com projetos em andamento? [fonte: Financeiro, PM, CTO] [impacto: PM]
4. Qual é o billing mensal atual de cloud (AWS, Azure, GCP) e quais são os maiores componentes de custo? [fonte: FinOps, TI, Financeiro] [impacto: DevOps, Arquiteto]
5. Existem Reserved Instances, Savings Plans ou Enterprise Agreement que ofereçam desconto já contratado? [fonte: FinOps, TI, Compras] [impacto: Arquiteto, DevOps]
6. O custo de cloud é rastreado por projeto/time ou vai tudo em uma conta única sem separação? [fonte: FinOps, TI] [impacto: PM, DevOps]
7. Quais são os custos recorrentes de suporte e manutenção de fornecedores (Oracle, SAP, agências)? [fonte: Financeiro, Compras, TI] [impacto: PM]
8. Existem contratos de manutenção com multa de rescisão que impactariam a substituição de sistemas? [fonte: Jurídico, Compras] [impacto: PM, Arquiteto]
9. A empresa já calculou TCO de projetos anteriores ou de soluções avaliadas (build vs. buy)? [fonte: TI, Financeiro, PM] [impacto: Arquiteto, PM]
10. Quais componentes de custo de TI são tipicamente esquecidos nas estimativas (suporte, treinamento, turnover)? [fonte: Financeiro, PM, TI] [impacto: PM]
11. Quem aprova investimentos em TI e qual o threshold por nível (gerente, diretor, board)? [fonte: Financeiro, Diretoria] [impacto: PM]
12. Quanto tempo leva o processo de aprovação financeira de um projeto novo? [fonte: Financeiro, PM, Diretoria] [impacto: PM]
13. Existe budget separado para segurança, compliance ou infraestrutura, ou tudo compete do mesmo pool? [fonte: Financeiro, CTO] [impacto: PM, Arquiteto]
14. O custo de pessoal interno é contabilizado no TCO de projetos ou é tratado como custo fixo separado? [fonte: Financeiro, RH] [impacto: PM]
15. Existe expectativa de ROI ou payback period definida para projetos de TI? [fonte: Diretoria, CFO] [impacto: PM, PO]

---

## Domínio 10 — Governança, Normas & Boas Práticas

- **Normas e padrões técnicos internos**: Verificar se a empresa tem padrões técnicos formalizados — arquitetura de referência, catálogo de tecnologias aprovadas, design patterns obrigatórios, naming conventions para recursos de cloud, padrões de logging e tracing. Padrões internos são restrições de projeto (não é possível usar tecnologia fora do catálogo sem aprovação) mas também aceleradores (se existe um padrão de API documentado, o projeto novo não precisa definir o seu). A existência e a rigidez desses padrões variam enormemente entre empresas.

- **Processo de homologação de tecnologia**: Verificar se existe processo formal para aprovar o uso de tecnologias, frameworks ou fornecedores novos — comitê de arquitetura, RFC/ADR, avaliação de segurança. Em enterprises, propor uma tecnologia fora do catálogo pode levar meses para ser aprovada. Em startups, a decisão é instantânea. O entrevistador precisa calibrar as recomendações técnicas conforme a velocidade de aprovação do cliente — não adianta recomendar Rust se o processo de homologação demora 6 meses e o projeto precisa começar em 2 semanas.

- **Processo de change management**: Verificar como mudanças em produção são governadas — CAB com agenda fixa, janela de manutenção definida, aprovação de emergência para hotfixes. Em ambientes regulados, qualquer mudança em produção exige documentação formal, aprovação, e janela agendada. Isso impacta diretamente a velocidade de deploy do projeto novo — se o CAB se reúne quinzenalmente, deploys acontecem no máximo 2x por mês, independente da capacidade técnica de CI/CD.

- **Auditoria e trilhas de controle**: Verificar se existe requisito de auditoria — quem fez o quê, quando, e por quê. Em ambientes SOX ou regulados, trilhas de auditoria imutáveis são obrigatórias para qualquer sistema que toque dados financeiros ou pessoais. Isso impacta a arquitetura do projeto novo — audit logs precisam ser planejados desde o design, não adicionados depois. A existência de infraestrutura de auditoria (Splunk, CloudTrail, Azure Activity Log) é um ativo reaproveitável.

- **SLAs e SLOs definidos**: Verificar se a empresa tem SLAs formais com clientes ou SLOs internos para disponibilidade, latência, tempo de resposta a incidentes. SLAs existentes definem o piso de qualidade para qualquer projeto novo — se o SLA corporativo é 99.9% de uptime, o projeto novo precisa ser desenhado para atender esse SLA, o que implica redundância, failover, e monitoring. Sem SLAs definidos, a expectativa é implícita e descobre-se na primeira queda.

- **Propriedade intelectual e licenciamento**: Verificar quem é dono do código produzido — a empresa, a software house, ou depende do contrato. Verificar se existem restrições de licenciamento de open source (GPL vs. MIT, restrições corporativas ao uso de AGPL). Em projetos terceirizados, a transferência de IP precisa estar no contrato antes do kick-off. Em empresas com política rígida de open source, dependências GPL podem ser vetadas mesmo que sejam a melhor solução técnica.

### Perguntas

1. Existe catálogo de tecnologias aprovadas (linguagens, frameworks, bancos, cloud services)? [fonte: TI, Arquiteto interno, Segurança] [impacto: Dev, Arquiteto]
2. Qual é o processo para homologar uma tecnologia nova não presente no catálogo? Quanto tempo leva? [fonte: TI, Arquiteto interno, Comitê de Arquitetura] [impacto: Arquiteto, PM]
3. Existe arquitetura de referência documentada que projetos novos devem seguir? [fonte: Arquiteto interno, TI] [impacto: Arquiteto, Dev]
4. Existe processo de change management (CAB, janela de manutenção, aprovação de emergência)? [fonte: TI, Operações] [impacto: DevOps, PM]
5. Qual é a frequência do CAB e quanto tempo leva para aprovar uma mudança em produção? [fonte: TI, Operações] [impacto: PM, DevOps]
6. Existe requisito de trilha de auditoria para mudanças em sistemas (quem, quando, o quê, por quê)? [fonte: Compliance, Segurança, Auditoria Interna] [impacto: Dev, Arquiteto]
7. A empresa tem SLAs formais com clientes ou SLOs internos para disponibilidade e performance? [fonte: Operações, TI, Comercial] [impacto: Arquiteto, DevOps]
8. Existe processo formal de post-mortem após incidentes com ações de melhoria rastreadas? [fonte: TI, DevOps interno] [impacto: DevOps, PM]
9. Quem é o dono do código produzido em projetos terceirizados — a empresa, a software house, ou depende? [fonte: Jurídico, Compras] [impacto: PM, Arquiteto]
10. Existe política corporativa sobre uso de open source (restrições a GPL/AGPL, processo de aprovação)? [fonte: Jurídico, TI, Segurança] [impacto: Dev, Arquiteto]
11. Projetos anteriores geraram documentação técnica reutilizável (ADRs, design docs, runbooks)? [fonte: Tech Lead, PM] [impacto: Arquiteto, Dev]
12. Existe processo de code review obrigatório para merge em branches protegidas? [fonte: Tech Lead, DevOps interno] [impacto: Dev]
13. Existe policy-as-code para guardrails de infraestrutura (OPA, Sentinel, AWS Config Rules)? [fonte: DevOps interno, Segurança] [impacto: DevOps]
14. Existe programa de melhoria contínua de processos (ITIL, DevOps maturity model, DORA metrics)? [fonte: TI, Diretoria] [impacto: PM, DevOps]
15. Quais são as maiores dores de governança que o time enfrenta hoje — burocracia excessiva, falta de padrão, ou ambos? [fonte: Dev, Tech Lead, PM] [impacto: PM, Arquiteto]

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante o environment discovery.

### Respostas de Risco Crítico

Indicam que o ambiente tem **problemas fundamentais** que afetarão qualquer projeto novo.

| Resposta do cliente | Domínio | Risco | Ação |
|---|---|---|---|
| "Os secrets estão no código, faz anos que é assim" | 04 | Vazamento de credenciais no repositório, incidente de segurança iminente | Resolver gestão de secrets ANTES de qualquer projeto novo |
| "Não temos backup testado" | 06 | Perda de dados irrecuperável em caso de falha | Exigir teste de restore como pré-requisito |
| "Só o João sabe como funciona o deploy/servidor/sistema X" | 08 | Bus factor = 1, risco operacional direto | Documentar conhecimento e cross-treinar antes de depender |
| "Não temos controle de quem acessa o quê em produção" | 05 | Violação de compliance e risco de segurança | Implementar RBAC e auditoria antes de adicionar sistemas novos |
| "O budget de TI já está 100% comprometido este ano" | 09 | Projeto novo sem orçamento = cancelamento ou atraso | Alinhar realocação de budget ou postergar projeto |

### Respostas de Bloqueio para Projetos Novos

Indicam que **uma condição do ambiente precisa ser resolvida** antes de iniciar o projeto.

| Resposta do cliente | Domínio | Risco | Ação |
|---|---|---|---|
| "Não temos acesso à console de cloud" | 01 | Impossível provisionar infraestrutura | Obter acesso antes do kick-off |
| "O ERP não tem API, só acessamos por tela" | 02 | Integração impossível sem desenvolvimento customizado (scraping, RPA, ou API wrapper) | Estimar esforço de integração separadamente |
| "Nunca usamos containers ou CI/CD" | 04 | Setup de infraestrutura de entrega vai consumir sprints inteiros antes de começar a entregar valor | Incluir setup de DevOps no escopo e timeline |
| "O processo de aprovação de tecnologia leva 6 meses" | 10 | Timeline do projeto inviável se depender de tecnologia não homologada | Limitar recomendações ao catálogo aprovado ou iniciar homologação em paralelo |
| "Estamos migrando de cloud provider nos próximos 3 meses" | 01 | Projeto novo pode ser construído na plataforma errada | Alinhar timeline com migração ou esperar conclusão |

### Respostas de Alerta

Não bloqueiam, mas indicam **complexidade adicional** que deve ser orçada.

| Resposta do cliente | Domínio | Risco | Ação |
|---|---|---|---|
| "Cada time usa linguagem/framework diferente" | 03 | Fragmentação de stack dificulta reaproveitamento e contratação | Recomendar convergência gradual na stack do projeto novo |
| "Temos 200+ microsserviços" | 03 | Complexidade operacional alta, observabilidade crítica | Investir em tracing distribuído e service mesh |
| "O turnover do time técnico foi 40% nos últimos 12 meses" | 08 | Perda de conhecimento contínua, ramp-up permanente | Documentação robusta e pair programming obrigatórios |
| "Os dados entre sistemas não batem" | 06 | Qualidade de dados baixa, projeto precisa incluir reconciliação | Orçar limpeza de dados como fase do projeto |
| "Compliance nunca barrou nada, a gente resolve depois" | 05 | Falsa sensação de segurança — o bloqueio vai aparecer no momento mais caro (go-live) | Envolver compliance desde o discovery |
| "A gente faz deploy direto em produção sem staging" | 04 | Zero validação antes de impactar usuários reais | Incluir criação de ambiente de staging no escopo |

---

## Checklist de Saída do Environment Discovery

O environment discovery está completo quando todas as perguntas abaixo puderem ser respondidas com confiança:

### Infraestrutura

- [ ] O modelo de infra está mapeado (cloud/on-prem/híbrido) com custos e capacidade
- [ ] Existe clareza sobre o que pode ser reaproveitado vs. o que precisa ser provisionado

### Sistemas

- [ ] Inventário completo de SaaS e sistemas com custos e contratos
- [ ] APIs disponíveis e restrições de integração documentadas
- [ ] SSO e provedor de identidade identificados

### Stack

- [ ] Linguagens, frameworks e ferramentas do time mapeados
- [ ] Padrões de código e convenções documentados ou confirmada ausência
- [ ] Bancos de dados em uso com capacidade e licenciamento

### DevOps

- [ ] CI/CD existente mapeado ou confirmada ausência (que entra no escopo do projeto)
- [ ] Estratégia de deploy e gestão de secrets conhecidas
- [ ] Observabilidade existente ou gap documentado

### Segurança

- [ ] Regulamentações aplicáveis identificadas
- [ ] Políticas de acesso, criptografia e vulnerabilidades mapeadas
- [ ] DPO e processos LGPD identificados (se aplicável)

### Dados

- [ ] Fontes autoritativas por entidade mapeadas
- [ ] Integrações existentes documentadas
- [ ] Qualidade de dados avaliada

### Gestão

- [ ] Metodologia, ferramentas e cadência conhecidas
- [ ] Canais de comunicação e processo de aprovação mapeados

### Equipe

- [ ] Composição, senioridade e disponibilidade do time mapeadas
- [ ] Gaps de skills identificados com plano de mitigação
- [ ] Bus factor crítico documentado

### Financeiro

- [ ] Budget disponível e compromissos existentes conhecidos
- [ ] Custos recorrentes de TI mapeados
- [ ] Processo de aprovação financeira com timeline claro

### Governança

- [ ] Catálogo de tecnologias e processo de homologação conhecidos
- [ ] Processo de change management e CAB documentados
- [ ] Requisitos de auditoria e trilha de controle identificados
