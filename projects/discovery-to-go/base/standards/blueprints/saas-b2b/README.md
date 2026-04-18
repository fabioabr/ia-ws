---
title: "SaaS Público B2B — Blueprint"
description: "Produto digital vendido para empresas. Contratos anuais, onboarding assistido, SSO corporativo (SAML/OIDC), SLAs, permissões por organização e auditoria."
category: project-blueprint
type: saas-b2b
status: rascunho
created: 2026-04-13
---

# SaaS Público B2B

## Descrição

Produto digital vendido para empresas. Contratos anuais, onboarding assistido, SSO corporativo (SAML/OIDC), SLAs, permissões por organização e auditoria. O modelo B2B se diferencia do B2C pela complexidade do processo de venda (ciclo longo, múltiplos decisores), pela necessidade de isolamento de dados entre organizações (multi-tenancy com segregação rigorosa), e pela exigência de compliance corporativo (SOC 2, ISO 27001, LGPD/GDPR com DPA).

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo SaaS B2B é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — SaaS B2B Horizontal (PME)

Produto genérico que atende pequenas e médias empresas de qualquer setor — gestão de projetos, CRM leve, comunicação interna, assinatura eletrônica. O processo de venda é self-service ou low-touch (trial gratuito → conversão). Contratos mensais ou anuais com valor baixo a médio ($20–500/mês por workspace). Multi-tenancy simples (tenant = organização), sem necessidade de SSO corporativo no MVP. O foco é velocidade de onboarding, simplicidade de UX e retenção via produto (product-led growth). Exemplos: Notion, Basecamp, Pipedrive, PandaDoc.

### V2 — SaaS B2B Vertical (Nicho)

Produto especializado para um setor específico — healthtech, legaltech, fintech, edtech, agritech. O domínio do negócio é complexo e regulado. O processo de venda é consultivo (demo → proposal → contrato). Contratos anuais de valor médio a alto ($500–5.000/mês). Requer conhecimento profundo do domínio para modelar corretamente os fluxos e as regras de negócio. Compliance setorial é obrigatório (HIPAA para saúde, regulação do Bacen para fintech, LGPD com especificidades do setor). Exemplos: Tasy (saúde), Jusbrasil (jurídico), Conta Azul (contabilidade), Totvs Agro.

### V3 — SaaS B2B Enterprise

Produto vendido para grandes corporações com ciclo de venda longo (3–12 meses), múltiplos stakeholders (TI, compliance, procurement, usuários finais), e exigências de segurança e auditoria rigorosas. Contratos anuais de valor alto ($5.000–100.000+/mês). SSO corporativo obrigatório (SAML 2.0, OIDC), SCIM para provisionamento de usuários, audit logs exportáveis, SLAs contratuais com penalidades, e frequentemente exige deploy em região específica ou VPC dedicada. O foco é customização por cliente (feature flags, white-label), suporte dedicado e integrações com stack corporativa (Salesforce, SAP, ServiceNow). Exemplos: Salesforce, Workday, ServiceNow, Datadog.

### V4 — SaaS B2B com Marketplace / Plataforma

Produto que conecta duas ou mais partes — fornecedores e compradores, prestadores e contratantes, produtores e distribuidores. Além do multi-tenancy tradicional, há lógica de matching, transações entre partes, e frequentemente comissionamento ou split de pagamento. A complexidade está na dinâmica de dois lados (supply e demand), onboarding diferenciado por perfil, e governança de conteúdo/oferta. Exemplos: Vtex (e-commerce B2B), Mercado Livre Ads, Convenia (marketplace de benefícios).

### V5 — SaaS B2B API-First / Infraestrutura

Produto cujo consumidor principal é outro sistema, não um humano. API como produto principal, com dashboard de administração secundário. Modelo de cobrança por uso (requests, volume de dados, usuários ativos). Documentação de API, SDK, sandbox e developer experience são o diferencial competitivo. Uptime e latência são SLAs contratuais — downtime impacta diretamente o negócio do cliente. Exemplos: Stripe, Twilio, Algolia, SendGrid, AWS (cada serviço individualmente).

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend | Banco de Dados | Infra | Observações |
|---|---|---|---|---|---|
| V1 — Horizontal PME | Next.js ou Remix | Node.js (NestJS) ou Rails | PostgreSQL + Redis | Vercel + Railway ou Render | Product-led growth exige onboarding rápido. Auth via Clerk ou Auth0. |
| V2 — Vertical Nicho | Next.js | Node.js (NestJS) ou .NET | PostgreSQL | AWS (ECS/EKS) ou GCP (Cloud Run) | Compliance setorial pode exigir infra dedicada. Modelagem de domínio é o core. |
| V3 — Enterprise | Next.js ou Angular | Node.js (NestJS), Java (Spring) ou .NET | PostgreSQL + Redis + ElasticSearch | AWS ou Azure (exigência do cliente) | SSO (SAML/OIDC), SCIM, audit logs, multi-region. Terraform obrigatório. |
| V4 — Marketplace | Next.js | Node.js (NestJS) | PostgreSQL + Redis | AWS (ECS) | Split payment via Stripe Connect ou similar. Filas para matching. |
| V5 — API-First | Dashboard: Next.js | Node.js, Go ou Rust | PostgreSQL + Redis + ClickHouse (analytics) | AWS ou GCP com CDN edge | Rate limiting, API gateway, SDK generation (OpenAPI). Observability é crítica. |

---

## Etapa 01 — Inception

- **Modelo de negócio e monetização**: SaaS B2B pode monetizar por assinatura fixa (por seat, por workspace, por tier de features), por uso (volume de transações, API calls, armazenamento), ou modelo híbrido (base fixa + excedente). A escolha do modelo de pricing impacta diretamente a arquitetura — cobrança por uso exige metering em tempo real, cobrança por seat exige controle de licenças ativas, e tiers de features exigem sistema de feature flags robusto. Identificar o modelo na Inception é pré-requisito para dimensionar corretamente o esforço de billing e permissões.

- **Ciclo de venda e decisores**: Em B2B, quem compra raramente é quem usa. O comprador (procurement, CTO, VP) avalia ROI, compliance e integração com stack existente. O usuário final (analista, operador, gerente de time) avalia usabilidade e produtividade. O projeto precisa atender ambos desde o início — um produto fácil de usar mas que não passa pelo security review corporativo não vende, e um produto que passa em todas as auditorias mas tem UX ruim não retém. Mapear os decisores e seus critérios de avaliação na Inception define as prioridades de desenvolvimento.

- **Requisitos regulatórios e de compliance**: Empresas clientes frequentemente exigem conformidade com frameworks de segurança (SOC 2 Type II, ISO 27001), legislação de dados (LGPD, GDPR), e regulamentações setoriais (HIPAA, PCI-DSS, regulações do Bacen). Esses requisitos não são "nice to have" — são pré-requisitos contratuais. Um SaaS B2B que não pode demonstrar conformidade perde deals enterprise. Identificar quais certificações e conformidades são necessárias na Inception impacta a arquitetura (criptografia, audit logs, residência de dados), o cronograma (certificações levam meses) e o custo (auditorias externas custam dezenas de milhares de reais).

- **Multi-tenancy como premissa arquitetural**: Todo SaaS B2B é multi-tenant por definição — múltiplas organizações compartilham a mesma infraestrutura. A questão é o nível de isolamento: banco de dados compartilhado com tenant_id em cada tabela (mais barato, mais simples, menor isolamento), schema separado por tenant (isolamento médio, complexidade de migrations), ou banco de dados separado por tenant (máximo isolamento, custo e complexidade operacional altos). A decisão depende dos requisitos de compliance, do volume esperado de tenants, e do perfil dos clientes — enterprise clients frequentemente exigem isolamento de dados demonstrável.

- **Existência de produto legado ou concorrente interno**: Muitos projetos B2B não nascem do zero — substituem uma solução interna (planilha complexa, sistema legado, ERP customizado) ou um concorrente que o cliente quer abandonar. Entender o legado é fundamental porque define: o baseline de funcionalidades que o MVP precisa cobrir para que a migração seja aceitável, o volume de dados a migrar, as integrações existentes que precisam ser mantidas, e as expectativas de UX que os usuários já têm (mesmo que ruins, são familiares). Ignorar o legado resulta em MVP que ninguém adota porque "falta aquela feature que a planilha tinha".

- **Estrutura do time e capacidade de execução**: SaaS B2B é um compromisso de longo prazo — não é projeto com data de entrega e encerramento. Após o go-live, o produto precisa de evolução contínua (features), manutenção (bugs, updates de segurança), operação (infra, monitoramento) e suporte (atendimento ao cliente). Se o time é uma startup de 3 pessoas, a arquitetura e as escolhas tecnológicas devem otimizar para velocidade e simplicidade. Se é uma empresa com time dedicado de 20+ engenheiros, a arquitetura pode (e deve) ser mais robusta e escalável. O tamanho do time define o que é realista entregar e manter.

### Perguntas

1. Qual é o modelo de monetização previsto — assinatura por seat, por uso, por tier de features, ou modelo híbrido? [fonte: Diretoria, Produto, Financeiro] [impacto: Arquiteto, Dev, PM]
2. Qual é o ciclo de venda típico do cliente-alvo — self-service com trial, venda consultiva com demo, ou enterprise com RFP? [fonte: Comercial, Diretoria] [impacto: PM, Dev, Designer]
3. Quais certificações e conformidades regulatórias são pré-requisitos para fechar contratos (SOC 2, ISO 27001, LGPD, HIPAA)? [fonte: Jurídico, Compliance, Comercial] [impacto: Arquiteto, Dev, DevOps, PM]
4. Qual é o nível de isolamento de dados exigido entre organizações clientes (multi-tenancy compartilhado, schema separado, banco separado)? [fonte: Compliance, TI, Clientes enterprise] [impacto: Arquiteto, Dev, DevOps]
5. O produto substitui uma solução existente (planilha, sistema legado, concorrente) ou resolve um problema novo sem baseline? [fonte: Produto, Comercial] [impacto: PM, Dev, Designer]
6. Qual é o tamanho e a senioridade do time técnico disponível para desenvolver e manter o produto após o lançamento? [fonte: CTO, RH, Diretoria] [impacto: Arquiteto, PM]
7. Existe expectativa de integração com ferramentas corporativas dos clientes (Salesforce, SAP, Active Directory, Slack, Teams)? [fonte: Comercial, Produto, TI dos clientes] [impacto: Arquiteto, Dev]
8. Qual é o prazo esperado para o MVP e existe um evento de negócio que justifica essa data (rodada de investimento, contrato assinado, deadline regulatório)? [fonte: Diretoria, Investidores] [impacto: PM, Dev]
9. Quem são os 3-5 clientes piloto que vão usar o produto no lançamento e qual o nível de acesso que temos a eles para feedback? [fonte: Comercial, Diretoria] [impacto: PM, Produto, Designer]
10. O produto terá versão white-label ou customizações por cliente, ou será uma experiência única para todos? [fonte: Comercial, Produto] [impacto: Arquiteto, Dev, Designer]
11. Qual é a expectativa de SLA de disponibilidade para os clientes (99.9%, 99.95%, 99.99%) e há penalidades contratuais? [fonte: Comercial, Jurídico] [impacto: DevOps, Arquiteto]
12. O produto precisará suportar múltiplos idiomas ou operação em múltiplos países com requisitos legais distintos? [fonte: Comercial, Diretoria, Jurídico] [impacto: Dev, Arquiteto, PM]
13. Existe orçamento definido separando custo de desenvolvimento, custo de infraestrutura mensal e custo de certificações? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto, DevOps]
14. Qual é o volume esperado de organizações e usuários nos primeiros 12 meses (10 orgs com 50 usuários vs. 1000 orgs com 5 usuários cada)? [fonte: Comercial, Produto] [impacto: Arquiteto, DevOps, Dev]
15. O produto terá API pública para que clientes integrem com seus próprios sistemas, ou será exclusivamente via interface web? [fonte: Produto, Comercial, TI dos clientes] [impacto: Arquiteto, Dev]

---

## Etapa 02 — Discovery

- **Mapeamento de personas e jornadas por papel**: Em B2B, o mesmo produto é usado por personas com necessidades radicalmente diferentes — o admin da organização configura permissões e gerencia usuários, o gerente acompanha métricas e dashboards, o operador executa tarefas diárias no sistema. Cada persona tem uma jornada distinta com pontos de dor diferentes. Mapear todas as personas com suas jornadas, frequência de uso e critérios de satisfação é essencial para priorizar features no MVP. Um produto que atende bem o operador mas negligencia o admin não será adotado por organizações que exigem controle.

- **Requisitos de autenticação e autorização**: B2B exige camadas de permissão que não existem em B2C — permissões por organização (tenant), por papel dentro da organização (admin, gerente, membro), por recurso específico (acesso a módulo X mas não a Y), e frequentemente permissões granulares por ação (pode visualizar mas não editar, pode editar mas não deletar). SSO corporativo (SAML 2.0, OIDC) é requisito comum em clientes enterprise — sem SSO, o deal não fecha. SCIM (System for Cross-domain Identity Management) para provisionamento automático de usuários via Active Directory é esperado em contratos enterprise maduros.

- **Integrações como diferencial competitivo**: Empresas B2B não operam com uma ferramenta só — o produto precisa se encaixar no ecossistema existente do cliente. Integrações típicas incluem: CRM (Salesforce, HubSpot), ERP (SAP, Totvs), comunicação (Slack, Teams), identity provider (Okta, Azure AD), armazenamento (Google Drive, OneDrive, S3), e ferramentas específicas do setor. Cada integração tem custo de desenvolvimento, manutenção e suporte — não é "só uma API". Mapear quais integrações são bloqueadoras para os clientes piloto e quais são diferencial competitivo define a prioridade.

- **Modelo de dados multi-tenant**: Levantar a estrutura de dados considerando o isolamento entre organizações. Cada entidade do sistema precisa ser avaliada: dados exclusivos do tenant (configurações, usuários, conteúdo de negócio), dados compartilhados entre tenants (catálogos de referência, templates do sistema), e dados que cruzam tenants (apenas em modelos de marketplace ou plataforma). O modelo de dados multi-tenant impacta diretamente a performance de queries (filtrar por tenant_id em toda query), a segurança (risco de vazamento de dados entre tenants), e a complexidade de migrations (aplicar mudança em milhares de tenants sem downtime).

- **Requisitos de auditoria e rastreabilidade**: Clientes B2B enterprise exigem saber quem fez o quê, quando e de onde. Audit logs não são feature — são requisito contratual. O discovery deve levantar: quais ações precisam ser auditadas (login, CRUD de dados sensíveis, mudanças de permissão, exportação de dados), qual o formato de armazenamento (structured JSON, indexável para busca), qual o período de retenção (compliance pode exigir 5+ anos), e se os logs precisam ser exportáveis (para o SIEM do cliente — Splunk, Datadog, ElasticSearch). Implementar auditoria depois que o sistema está em produção é extremamente custoso porque exige instrumentar retrospectivamente todas as ações.

- **Billing e gestão de assinaturas**: Levantar os requisitos completos de cobrança — planos disponíveis (free, starter, professional, enterprise), ciclo de cobrança (mensal, anual, customizado), métodos de pagamento (cartão de crédito via Stripe, boleto para Brasil, wire transfer para enterprise), gestão de upgrades e downgrades (proration, créditos), cobrança por excedente (overage) se modelo por uso, e emissão de nota fiscal (obrigatória no Brasil). A integração com gateway de pagamento e a lógica de billing são frequentemente subestimadas — billing é domínio complexo com edge cases que aparecem meses depois do lançamento.

### Perguntas

1. Quais são as personas principais do produto e qual a jornada crítica de cada uma dentro do sistema? [fonte: Produto, Comercial, Clientes piloto] [impacto: Designer, Dev, PM]
2. Quais níveis de permissão são necessários (organização, papel, recurso, ação) e como são gerenciados pelo admin do cliente? [fonte: Produto, Clientes piloto, TI] [impacto: Arquiteto, Dev]
3. SSO corporativo (SAML/OIDC) é requisito para o MVP ou pode ser entregue em fase posterior? [fonte: Comercial, Clientes enterprise] [impacto: Arquiteto, Dev]
4. Quais integrações com sistemas externos são bloqueadoras para os clientes piloto (CRM, ERP, IdP, comunicação)? [fonte: Comercial, Clientes piloto, TI dos clientes] [impacto: Dev, Arquiteto]
5. Qual é o modelo de dados multi-tenant — dados isolados por organização, dados compartilhados e dados que cruzam tenants? [fonte: Produto, Arquiteto] [impacto: Arquiteto, Dev]
6. Quais ações do sistema precisam de audit log e qual o período de retenção exigido pelos clientes? [fonte: Compliance, Jurídico, Clientes enterprise] [impacto: Arquiteto, Dev, DevOps]
7. Quais são os planos de pricing, ciclos de cobrança e métodos de pagamento que o MVP precisa suportar? [fonte: Produto, Financeiro, Comercial] [impacto: Dev, Arquiteto]
8. Existe necessidade de emissão de nota fiscal automatizada e integração com sistema contábil? [fonte: Financeiro, Jurídico] [impacto: Dev, PM]
9. Qual é o volume e a complexidade de dados que cada organização cliente típica terá no sistema? [fonte: Produto, Clientes piloto] [impacto: Arquiteto, Dev, DevOps]
10. O produto precisa funcionar offline ou com conectividade intermitente para alguma persona? [fonte: Produto, Clientes piloto] [impacto: Arquiteto, Dev]
11. Quais são os fluxos de onboarding esperados — self-service automatizado, assistido por CS, ou implementação consultiva? [fonte: Produto, Comercial] [impacto: Dev, Designer, PM]
12. Existe necessidade de importação/exportação massiva de dados (CSV, Excel, API bulk) para migração dos clientes? [fonte: Produto, Comercial, Clientes piloto] [impacto: Dev, Arquiteto]
13. O produto terá notificações (e-mail, in-app, push, webhook) e quais eventos disparam cada tipo? [fonte: Produto, Clientes piloto] [impacto: Dev, Arquiteto]
14. Quais métricas de produto o time precisa monitorar (activation, retention, churn, feature usage) e como serão coletadas? [fonte: Produto, Diretoria] [impacto: Dev, Arquiteto, PM]
15. Há requisitos de acessibilidade (WCAG 2.1 AA) obrigatórios para os clientes-alvo (exigência contratual ou legal)? [fonte: Comercial, Jurídico, Compliance] [impacto: Dev, Designer]

---

## Etapa 03 — Alignment

- **Definição do MVP com clientes piloto**: Em B2B, o MVP não é definido em abstrato — é definido com os clientes piloto que aceitaram usar e pagar pelo produto. O alignment deve produzir uma lista priorizada de funcionalidades que atende as necessidades críticas dos 3-5 clientes piloto sem tentar resolver todos os problemas de todos os segmentos. O risco clássico é expandir o MVP para acomodar pedidos de um cliente enterprise que promete contrato grande — e entregar um produto medíocre para todos em vez de excelente para poucos. A priorização deve ser explícita: o que entra no MVP, o que entra na v1.1, e o que é backlog futuro.

- **Modelo de permissões e papéis acordado**: Definir formalmente a estrutura de permissões que o sistema vai implementar — não como abstração técnica, mas como regras de negócio validadas com os clientes piloto. Quais papéis existem por padrão (owner, admin, member, viewer), o cliente pode criar papéis customizados ou são fixos, quais ações cada papel pode executar em cada recurso, e como funciona o convite e remoção de membros. Um sistema de permissões mal definido gera retrabalho estrutural — alterar a granularidade de permissões depois que organizações já estão configuradas é migração de dados delicada.

- **SLA e modelo de suporte acordados**: Antes do build, definir o que está sendo prometido ao cliente em termos de disponibilidade (uptime SLA), tempo de resposta para incidentes (critical, high, medium, low), canais de suporte (e-mail, chat, telefone, portal dedicado), e horário de cobertura (8x5, 12x7, 24x7). Cada nível de SLA tem implicação direta na arquitetura (redundância, failover, monitoramento) e no custo operacional (equipe de plantão). Prometer SLA de 99.99% sem a infraestrutura e o time para sustentar é irresponsável e gera penalidades contratuais.

- **Estratégia de migração de dados dos clientes piloto**: Se os clientes piloto têm dados em sistemas legados que precisam migrar para o novo SaaS, o processo de migração precisa ser planejado como parte do projeto — não como afterthought. Definir: quais dados serão migrados (completo ou apenas ativos), qual o formato de origem (CSV, API do sistema legado, banco de dados), quem é responsável pela extração (cliente ou time de implementação), e qual o critério de validação pós-migração. Migração mal executada é a causa número um de churn nos primeiros 90 dias — o cliente volta para o sistema anterior porque "os dados não estão certos".

- **Acordo de escopo de integrações no MVP**: Integrações são black hole de escopo em B2B — cada cliente quer integração com um sistema diferente, cada sistema tem API diferente (ou não tem API), e a manutenção de integrações é contínua (APIs de terceiros mudam, tokens expiram, rate limits mudam). O alignment precisa definir com clareza: quais integrações estão no MVP (com justificativa de negócio), quais são pós-MVP, e o que acontece quando um cliente pede integração que não está no roadmap — webhook genérico para que o próprio cliente integre (melhor), ou desenvolvimento custom por demanda (pior, não escala).

### Perguntas

1. A lista de funcionalidades do MVP foi validada com os clientes piloto e não apenas definida internamente? [fonte: Produto, Comercial, Clientes piloto] [impacto: PM, Dev, Designer]
2. A priorização do MVP separa claramente o que é v1.0, v1.1 e backlog futuro, com justificativa documentada? [fonte: Produto, Diretoria] [impacto: PM, Dev]
3. O modelo de permissões (papéis, ações, recursos) foi definido como regra de negócio e validado com clientes? [fonte: Produto, Clientes piloto] [impacto: Arquiteto, Dev]
4. O SLA de disponibilidade e tempo de resposta a incidentes foi definido com base na infraestrutura planejada? [fonte: DevOps, Comercial, Jurídico] [impacto: DevOps, Arquiteto, PM]
5. O modelo de suporte (canais, horário, equipe) foi dimensionado e o custo está previsto no orçamento? [fonte: Diretoria, Financeiro, Operações] [impacto: PM, DevOps]
6. A estratégia de migração de dados dos clientes piloto foi planejada com formato, responsável e critério de validação? [fonte: Comercial, Clientes piloto, TI dos clientes] [impacto: Dev, PM]
7. As integrações do MVP foram definidas com escopo fechado e as integrações futuras foram comunicadas aos clientes? [fonte: Produto, Comercial] [impacto: Dev, Arquiteto]
8. A estratégia de onboarding do primeiro cliente foi desenhada com passo a passo e responsáveis definidos? [fonte: Produto, CS, Comercial] [impacto: PM, Dev, Designer]
9. O contrato ou termo de uso do produto foi revisado pelo jurídico e está alinhado com o SLA prometido? [fonte: Jurídico, Comercial] [impacto: PM, Jurídico]
10. O design de alta fidelidade cobre os fluxos críticos de todas as personas definidas no Discovery? [fonte: Designer, Produto] [impacto: Dev, PM]
11. O modelo de billing foi validado tecnicamente — o gateway de pagamento suporta os cenários de pricing definidos? [fonte: Financeiro, Dev, Fornecedor de pagamento] [impacto: Dev, Arquiteto]
12. Os ambientes de desenvolvimento, staging e produção foram acordados com critérios claros de promoção? [fonte: DevOps, Dev] [impacto: Dev, DevOps, QA]
13. O cliente entende que mudanças de escopo no MVP após o início do build impactam prazo e custo? [fonte: Diretoria, Comercial] [impacto: PM]
14. Os critérios de aceitação do MVP foram definidos de forma mensurável (não apenas "funcionar bem")? [fonte: Produto, Clientes piloto] [impacto: QA, PM, Dev]
15. O processo de feedback dos clientes piloto foi estruturado (canal, frequência, responsável por triagem)? [fonte: Produto, CS] [impacto: PM, Produto]

---

## Etapa 04 — Definition

- **Modelo de dados multi-tenant detalhado**: Especificar o schema do banco de dados com todas as entidades, seus relacionamentos e a estratégia de isolamento por tenant. Cada tabela deve ter a definição clara de: qual campo identifica o tenant, se há foreign keys cross-tenant (geralmente proibidas), quais índices são necessários para queries filtradas por tenant sem degradação de performance, e como soft delete é tratado (dados deletados pelo usuário mas retidos para auditoria). O modelo de dados é o artefato mais custoso de refatorar depois que há dados reais — erros de modelagem identificados em produção exigem migrations complexas com downtime ou backfill.

- **Especificação de APIs (contratos)**: Definir os contratos de API antes do build — endpoints, métodos HTTP, payloads de request e response, códigos de erro, e regras de autenticação/autorização por endpoint. Usar OpenAPI (Swagger) como formato de especificação permite geração automática de documentação, validação de contratos em testes, e geração de SDKs. Em B2B, a API pública (se houver) é um produto — clientes integram seus sistemas com ela e esperam estabilidade. Breaking changes na API após clientes estarem integrados destroem confiança e geram churn.

- **Wireframes e protótipos de fluxos complexos**: Em B2B, os fluxos mais críticos frequentemente envolvem múltiplas etapas e decisões condicionais — configuração de organização, convite e gestão de usuários, setup de integrações, configuração de workflows de negócio, e dashboards com filtros combinados. Esses fluxos precisam de protótipo interativo (Figma prototyping, não apenas telas estáticas) validado com os clientes piloto antes do build. Um fluxo de onboarding mal desenhado pode significar que 40% dos clientes desistem antes de completar a configuração.

- **Mapa de notificações e comunicações**: Definir todas as comunicações automáticas que o sistema vai enviar — e-mails transacionais (convite, reset de senha, confirmação de ação), e-mails de produto (trial expirando, uso baixo, novo feature), notificações in-app (ação pendente, alerta de sistema), e webhooks (evento para integrações de terceiros). Para cada comunicação: gatilho, destinatário, canal, template de conteúdo, e regras de frequência (evitar spam). A ausência de mapa de notificações resulta em e-mails implementados ad hoc durante o build com inconsistência de linguagem, design e regras.

- **Especificação de billing e subscription lifecycle**: Detalhar o ciclo de vida completo da assinatura: criação (checkout, período de trial), ativação (pagamento confirmado), cobrança recorrente (renovação automática, retry de falha), upgrade e downgrade (proration, créditos), cancelamento (imediato vs. fim do ciclo), e reativação. Cada transição tem regras de negócio específicas e edge cases que precisam estar documentados antes do build — o gateway de pagamento (Stripe, Braintree) tem seus próprios fluxos e webhooks que precisam ser mapeados aos estados do sistema.

- **Estrutura de feature flags e rollout progressivo**: Definir quais funcionalidades serão controladas por feature flags (por tenant, por plano, por usuário), qual a ferramenta de feature flags (LaunchDarkly, Flagsmith, custom), e qual o processo de rollout progressivo (canary deploy para 5% dos tenants → 25% → 100%). Em B2B, feature flags são essenciais não apenas para deploy seguro mas para gerenciar features que são exclusivas de planos superiores (gating) ou que foram prometidas apenas para clientes específicos (customer-specific flags).

### Perguntas

1. O modelo de dados multi-tenant foi especificado com schema completo, índices, e estratégia de isolamento documentada? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
2. Os contratos de API foram definidos em formato OpenAPI com endpoints, payloads, erros e regras de autenticação? [fonte: Arquiteto, Dev, Produto] [impacto: Dev]
3. Os protótipos de fluxos complexos (onboarding, permissões, billing) foram validados com clientes piloto? [fonte: Designer, Produto, Clientes piloto] [impacto: Dev, Designer, PM]
4. O mapa de notificações foi especificado com gatilho, destinatário, canal e template para cada comunicação? [fonte: Produto, Marketing, Designer] [impacto: Dev, Designer]
5. O ciclo de vida da assinatura foi detalhado com todos os estados, transições e edge cases documentados? [fonte: Produto, Financeiro, Fornecedor de pagamento] [impacto: Dev, Arquiteto]
6. A estrutura de feature flags foi definida (por tenant, por plano, por usuário) com ferramenta e processo de rollout? [fonte: Produto, Dev] [impacto: Dev, Arquiteto, PM]
7. Os fluxos de SSO (SAML/OIDC) foram mapeados com diagramas de sequência incluindo edge cases (token expirado, provedor indisponível)? [fonte: Arquiteto, TI dos clientes] [impacto: Dev, Arquiteto]
8. O mapa de redirecionamentos de URLs (se houver produto legado sendo substituído) foi produzido? [fonte: Produto, TI] [impacto: Dev, SEO]
9. As regras de rate limiting para API pública foram definidas por plano e por endpoint? [fonte: Produto, Arquiteto] [impacto: Dev, DevOps]
10. A estrutura de audit logs foi especificada — quais eventos, quais campos, formato de armazenamento e busca? [fonte: Compliance, Produto, Arquiteto] [impacto: Dev, DevOps]
11. O modelo de importação/exportação de dados foi definido com formatos aceitos, limites de volume e validações? [fonte: Produto, Clientes piloto] [impacto: Dev]
12. Os templates de e-mail transacional foram definidos com conteúdo, design e variáveis por tipo de comunicação? [fonte: Marketing, Designer, Produto] [impacto: Dev, Designer]
13. Os dashboards e relatórios foram especificados com métricas, filtros, granularidade temporal e permissão de acesso? [fonte: Produto, Clientes piloto] [impacto: Dev, Designer]
14. Os critérios de validação de dados de entrada foram especificados por campo (formatos, limites, unicidade por tenant)? [fonte: Produto, Arquiteto] [impacto: Dev]
15. A documentação de definição foi revisada e aprovada por Produto, Arquitetura e pelos clientes piloto antes do Setup? [fonte: Diretoria, Produto, Clientes piloto] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Estratégia de multi-tenancy no banco de dados**: A decisão arquitetural mais impactante em SaaS B2B. Banco compartilhado com tenant_id é a abordagem mais simples e escalável horizontalmente — funciona bem para milhares de tenants pequenos (V1 Horizontal). Schema por tenant oferece isolamento lógico sem custo de infraestrutura separada — adequado para V2 Vertical com dezenas a centenas de tenants. Banco separado por tenant oferece máximo isolamento e permite compliance com residência de dados por região — necessário para V3 Enterprise com exigências regulatórias rigorosas, mas cada tenant é uma instância operacional separada que precisa de migrations, backup e monitoramento individuais. A escolha errada nesta fase é a mais cara de corrigir depois.

- **Autenticação e autorização**: Definir a stack de auth considerando os múltiplos cenários B2B. Para autenticação: suporte a credenciais locais (e-mail/senha), SSO via SAML 2.0 e OIDC (cada organização pode ter seu próprio Identity Provider — Okta, Azure AD, Google Workspace), MFA obrigatório por política da organização, e SCIM para provisionamento automático de usuários. Para autorização: RBAC (Role-Based Access Control) como base, com possibilidade de ABAC (Attribute-Based Access Control) para permissões granulares. Soluções como Auth0, Clerk ou WorkOS abstraem boa parte da complexidade — build from scratch só se justifica para requisitos muito específicos.

- **Arquitetura de billing e metering**: Se o modelo de pricing envolve cobrança por uso, a arquitetura precisa de metering — captura de eventos de uso em tempo real (API calls, storage, seats ativos) com agregação e cálculo de cobrança. Stripe Billing é o padrão para SaaS B2B por suportar subscription management, proration, invoicing, e cobrança por uso (metered billing). Para o mercado brasileiro, integrar com gateway local (Pagar.me, Iugu) para boleto e PIX. O billing deve ser tratado como sistema crítico — falha de cobrança é perda direta de receita, e cobrança incorreta é churn.

- **Observabilidade e monitoramento**: SaaS B2B com SLA contratual precisa de observabilidade completa — não apenas "o servidor está no ar". Definir: métricas de infraestrutura (CPU, memória, disco, network), métricas de aplicação (latência P50/P95/P99 por endpoint, error rate, throughput), métricas de negócio (sign-ups, ativações, churn), e logging estruturado (cada request identificado por tenant_id, user_id, request_id para correlação). A stack típica é Datadog ou Grafana Cloud para métricas e dashboards, e Sentry para error tracking. Alertas devem ser configurados com thresholds que acionam antes do SLA ser violado, não depois.

- **Estratégia de deploy e zero-downtime**: Clientes B2B usam o produto durante o horário comercial — deploy que causa downtime é inaceitável. A estratégia de deploy deve garantir zero-downtime: blue-green deployment (dois ambientes alternando), rolling deployment (pods sendo substituídos gradualmente), ou canary deployment (nova versão para percentual pequeno de tráfego antes de rollout completo). Database migrations devem ser backward-compatible (adicionar coluna é OK, renomear coluna é breaking) para permitir que versão antiga e nova coexistam durante o deploy. Feature flags complementam o deploy — o código da feature vai para produção desligado e é ativado independentemente do deploy.

- **Segurança e proteção de dados**: Definir a postura de segurança do sistema — criptografia em trânsito (TLS 1.2+ obrigatório), criptografia at rest (banco de dados e backups criptografados), gestão de secrets (Vault, AWS Secrets Manager, nunca em variáveis de ambiente de CI/CD), proteção contra OWASP Top 10 (SQL injection, XSS, CSRF, broken auth), e política de backup e disaster recovery (RPO e RTO definidos). Para clientes enterprise, produzir documentação de segurança (security whitepaper) que responda às perguntas do security questionnaire antes que sejam feitas — isso acelera o ciclo de venda.

### Perguntas

1. A estratégia de multi-tenancy (banco compartilhado, schema separado, banco separado) foi decidida com base nos requisitos de isolamento e escala? [fonte: Arquiteto, Compliance] [impacto: Dev, DevOps]
2. A stack de autenticação suporta SSO (SAML/OIDC), MFA e SCIM para os cenários B2B mapeados? [fonte: Arquiteto, Dev] [impacto: Dev]
3. A arquitetura de billing suporta todos os cenários de pricing definidos (subscription, metered, proration, multi-currency)? [fonte: Arquiteto, Produto, Financeiro] [impacto: Dev]
4. A stack de observabilidade cobre métricas de infra, aplicação e negócio com alertas configurados? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
5. A estratégia de deploy garante zero-downtime e database migrations backward-compatible? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
6. As medidas de segurança cobrem criptografia, gestão de secrets, proteção OWASP e backup/DR? [fonte: Arquiteto, Security] [impacto: Dev, DevOps]
7. A arquitetura suporta escala horizontal (mais instâncias) ou apenas vertical (mais CPU/RAM na máquina existente)? [fonte: Arquiteto, DevOps] [impacto: DevOps, Dev]
8. A solução de filas e processamento assíncrono foi definida para tarefas pesadas (importação, relatórios, notificações)? [fonte: Arquiteto] [impacto: Dev, DevOps]
9. A estratégia de cache foi definida (Redis para sessões e dados frequentes, CDN para assets, cache de API com invalidação)? [fonte: Arquiteto] [impacto: Dev, DevOps]
10. O modelo de branches, ambientes (dev, staging, prod) e processo de promoção foi documentado? [fonte: DevOps, Dev] [impacto: Dev, DevOps, QA]
11. A estratégia de versionamento de API (URL path, header, ou query param) foi definida com política de deprecação? [fonte: Arquiteto, Produto] [impacto: Dev]
12. A arquitetura de webhooks para integrações de clientes foi definida (retry policy, signing, delivery guarantees)? [fonte: Arquiteto] [impacto: Dev]
13. Os custos mensais de infraestrutura foram projetados para cenários de 10, 100 e 1000 tenants? [fonte: DevOps, Financeiro] [impacto: PM, Arquiteto]
14. A estratégia de data residency (região de armazenamento dos dados) atende os requisitos regulatórios dos clientes-alvo? [fonte: Compliance, Jurídico, Arquiteto] [impacto: DevOps, Arquiteto]
15. O security whitepaper foi redigido para responder proativamente ao security questionnaire de clientes enterprise? [fonte: Arquiteto, Security, Jurídico] [impacto: Comercial, PM]

---

## Etapa 06 — Setup

- **Infraestrutura como código (IaC)**: Configurar toda a infraestrutura usando Terraform, Pulumi ou CDK — nunca via console manual. Isso inclui: VPC e networking (subnets, security groups, load balancer), banco de dados (RDS PostgreSQL com read replicas para staging e prod), cache (ElastiCache Redis), filas (SQS ou RabbitMQ), serviço de aplicação (ECS, EKS ou Cloud Run), e serviços auxiliares (S3 para uploads, SES para e-mail). IaC é obrigatório em B2B porque: permite replicar ambientes (staging idêntico a produção), facilita disaster recovery (recriar infraestrutura a partir do código), e garante auditoria de mudanças (toda alteração de infra é PR no repositório).

- **Pipeline de CI/CD completo**: Configurar o pipeline com as seguintes etapas: lint (ESLint, Prettier) → testes unitários → testes de integração → build → deploy para staging (automático em merge para develop) → testes e2e em staging → deploy para produção (manual ou automático após aprovação). Usar GitHub Actions, GitLab CI ou CircleCI. O pipeline deve incluir: scan de dependências vulneráveis (Dependabot, Snyk), scan de secrets no código (GitLeaks, TruffleHog), e análise de cobertura de testes. Em B2B com SLA, o pipeline é a última barreira antes de código chegar em produção — um pipeline fraco resulta em bugs em produção.

- **Ambientes isolados**: Configurar no mínimo 3 ambientes — development (para o time de dev, dados sintéticos), staging (réplica de produção com dados anonimizados, acessível para QA e clientes piloto), e production (dados reais, acesso restrito). Cada ambiente deve ter suas próprias variáveis de ambiente, banco de dados, e configurações de serviços externos. O staging deve ser o mais próximo possível de produção em configuração — diferenças entre staging e produção são a causa mais comum de "funciona no staging mas não em produção".

- **Setup do sistema de billing**: Criar a conta no gateway de pagamento (Stripe, Braintree), configurar os produtos e planos de assinatura conforme definido na etapa de Definition, configurar webhooks de pagamento (payment_succeeded, payment_failed, subscription_updated, invoice_created), e testar o fluxo completo em modo sandbox. Para o mercado brasileiro, configurar gateway local (Pagar.me, Iugu) para boleto e PIX, e integrar com serviço de emissão de NF-e (Nuvem Fiscal, eNotas). O billing deve funcionar em sandbox antes de avançar para o Build.

- **Seed data e dados de teste**: Criar scripts de seed que populam o banco com dados realistas para desenvolvimento e QA — organizações de teste com diferentes planos, usuários com diferentes papéis, dados de negócio em volume suficiente para testar performance de listagens e relatórios. Os dados de seed devem ser versionados no repositório e executáveis com um único comando. Para staging, criar processo de anonimização de dados de produção (ou usar dados sintéticos gerados por script) — nunca usar dados reais de clientes em ambientes não-produtivos.

- **Configuração de monitoramento e alertas**: Configurar a stack de observabilidade definida na Architecture — Datadog/Grafana para métricas, Sentry para errors, e alertas para thresholds críticos (error rate >1%, latência P95 >2s, CPU >80%, disco >90%). Configurar health checks no load balancer e no sistema de deploy. Criar dashboard de status (Statuspage ou BetterUptime) que será compartilhado com clientes — SaaS B2B com SLA precisa de página de status pública onde clientes acompanham incidentes e manutenções programadas.

### Perguntas

1. A infraestrutura foi provisionada via IaC (Terraform/Pulumi/CDK) e o código está versionado no repositório? [fonte: DevOps] [impacto: DevOps, Dev]
2. O pipeline de CI/CD está configurado com lint, testes, build, scan de vulnerabilidades e deploy automatizado? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
3. Os ambientes (dev, staging, prod) estão isolados com variáveis, banco de dados e configurações independentes? [fonte: DevOps] [impacto: Dev, DevOps, QA]
4. O sistema de billing está configurado no gateway de pagamento com produtos, planos e webhooks funcionando em sandbox? [fonte: Dev, Financeiro, Fornecedor de pagamento] [impacto: Dev, Financeiro]
5. Os scripts de seed data estão prontos e populam ambientes de dev com dados realistas de múltiplos tenants? [fonte: Dev] [impacto: Dev, QA]
6. O processo de anonimização de dados para staging foi implementado e testado? [fonte: DevOps, Compliance] [impacto: DevOps, Dev]
7. A stack de monitoramento (métricas, errors, alertas) está configurada e testada com alertas disparando corretamente? [fonte: DevOps] [impacto: DevOps, Dev]
8. A página de status pública foi criada e o processo de comunicação de incidentes foi definido? [fonte: DevOps, PM] [impacto: DevOps, PM, Comercial]
9. O domínio foi configurado com SSL, e os subdomínios (app, api, docs, status) estão resolvendo corretamente? [fonte: DevOps, TI] [impacto: DevOps, Dev]
10. O serviço de e-mail transacional (SendGrid, SES) está configurado e testado com templates de teste? [fonte: Dev] [impacto: Dev]
11. O processo de onboarding de novos desenvolvedores está documentado com instruções de setup local completas? [fonte: Dev] [impacto: Dev]
12. Os secrets estão armazenados em serviço de gestão (Vault, AWS Secrets Manager) e não em variáveis de ambiente de CI/CD? [fonte: DevOps, Security] [impacto: DevOps, Dev]
13. O sistema de feature flags está configurado e funcional com pelo menos uma flag de teste ativa? [fonte: Dev, Produto] [impacto: Dev, PM]
14. O ambiente de staging é acessível pelos clientes piloto (se aplicável) com credenciais de teste? [fonte: DevOps, PM, Clientes piloto] [impacto: PM, Dev]
15. O pipeline foi testado end-to-end com um PR real — lint, testes, build, deploy para staging, e rollback de staging? [fonte: DevOps, Dev] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Sistema de autenticação e gestão de organizações**: Implementar o fluxo completo de auth — registro de organização (sign-up com criação de workspace), login com credenciais locais, setup de SSO por organização (cada tenant configura seu próprio SAML/OIDC provider), MFA (TOTP ou WebAuthn), convite de membros com aceite, e gestão de sessões (expiração, revogação, token refresh). O fluxo de SSO é particularmente complexo porque cada organização cliente pode ter um Identity Provider diferente com configurações diferentes — o sistema precisa suportar múltiplas configurações SSO simultâneas, isoladas por tenant.

- **Módulo de billing e subscription**: Implementar a integração com o gateway de pagamento — checkout (criação de assinatura), portal do cliente (atualização de cartão, histórico de faturas, download de NF-e), lógica de upgrade/downgrade com proration, tratamento de falha de pagamento (retry automático, notificação ao cliente, grace period antes de suspender acesso), e cancelamento (feedback obrigatório, offerta de retenção, desligamento no fim do ciclo). Implementar metering se modelo por uso — captura de eventos, agregação por período, e cálculo de overage. A integração com Stripe é via webhooks — cada evento do Stripe precisa ser tratado idempotentemente (o mesmo webhook pode ser entregue mais de uma vez).

- **RBAC e sistema de permissões**: Implementar o controle de acesso conforme definido na etapa de Alignment — papéis por organização, permissões por recurso e ação, herança de permissões (membro herda permissões do papel, papel pode ser composto por múltiplas permissões). Cada endpoint da API e cada elemento da UI devem validar permissões — no backend via middleware que verifica permissão antes de executar a ação, no frontend via contexto de permissões que mostra/esconde elementos da UI. O sistema de permissões deve ser testado exaustivamente — uma falha de autorização (usuário de tenant A acessando dados de tenant B) é vulnerabilidade crítica que pode ser fatal para o negócio.

- **Funcionalidades core de negócio**: Implementar os módulos que resolvem o problema principal dos clientes piloto — o que diferencia o produto dos concorrentes. A prioridade deve seguir a definição do MVP: fluxos primários completos antes de funcionalidades secundárias. Cada módulo deve ser desenvolvido com testes automatizados (unitários e de integração), com dados multi-tenant validados em cada query (WHERE tenant_id = ?), e com audit log em ações críticas. O progresso deve ser demonstrado aos clientes piloto em intervalos regulares (a cada sprint) para validação contínua e ajuste de rota.

- **Notificações e comunicações**: Implementar o sistema de notificações conforme o mapa definido na Definition — e-mails transacionais com templates HTML responsivos (usando framework como MJML ou React Email), notificações in-app com estado lido/não-lido e persistência, e webhooks para integrações de clientes (com retry exponential backoff, assinatura HMAC para verificação, e log de entregas). A implementação de e-mail deve usar queue assíncrona — enviar e-mail síncrono no fluxo de request bloqueia o usuário e falha silenciosamente se o serviço de e-mail estiver lento.

- **Importação/exportação de dados**: Implementar os fluxos de importação (CSV/Excel upload, validação por linha com relatório de erros, processamento assíncrono com progress tracking) e exportação (filtro e seleção, geração em background, download via link temporário). Importação é particularmente crítica no onboarding — se o cliente não conseguir trazer seus dados do sistema anterior para o novo SaaS de forma fluida, a adoção falha. Implementar com fila assíncrona e notificação ao completar — arquivos grandes podem levar minutos e o usuário não deve ficar preso na tela esperando.

### Perguntas

1. O sistema de autenticação suporta login local, SSO (SAML/OIDC) por organização e MFA? [fonte: Dev, Arquiteto] [impacto: Dev, Security]
2. O módulo de billing processa subscription, upgrade/downgrade, falha de pagamento e cancelamento corretamente? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
3. O RBAC está implementado com validação no backend e reflexo na UI para todas as ações e recursos? [fonte: Dev, Produto] [impacto: Dev, QA]
4. O isolamento multi-tenant está garantido em toda query (WHERE tenant_id = ?) e foi testado com dados cruzados? [fonte: Dev, Security] [impacto: Dev, QA, Security]
5. As funcionalidades core do MVP estão sendo demonstradas aos clientes piloto em cadência regular? [fonte: Produto, PM] [impacto: PM, Dev, Produto]
6. O sistema de notificações (e-mail, in-app, webhooks) está implementado com queue assíncrona e retry? [fonte: Dev] [impacto: Dev]
7. A importação/exportação de dados funciona com arquivos grandes (>10MB) sem timeout ou perda de dados? [fonte: Dev, QA] [impacto: Dev]
8. Os audit logs estão sendo registrados para todas as ações críticas definidas na specficação? [fonte: Dev, Compliance] [impacto: Dev, Security]
9. Os testes automatizados cobrem fluxos cross-tenant para garantir isolamento de dados? [fonte: Dev, QA] [impacto: Dev, QA]
10. A integração com gateway de pagamento trata webhooks de forma idempotente e com logging? [fonte: Dev] [impacto: Dev, Financeiro]
11. O fluxo de onboarding da primeira organização foi testado end-to-end com dados realistas? [fonte: Dev, Produto] [impacto: Dev, PM, Produto]
12. Os dashboards e relatórios respeitam o escopo do tenant e os filtros de permissão por papel? [fonte: Dev, Produto] [impacto: Dev, QA]
13. Os feature flags estão controlando corretamente o acesso a funcionalidades por tenant e plano? [fonte: Dev, Produto] [impacto: Dev, PM]
14. Os estados de erro, loading e vazio estão implementados para todos os componentes de interface? [fonte: Designer, Dev] [impacto: Dev, Designer]
15. A documentação de API (se pública) está gerada automaticamente a partir do OpenAPI spec e acessível em staging? [fonte: Dev, Produto] [impacto: Dev]

---

## Etapa 08 — QA

- **Teste de isolamento multi-tenant**: Este é o teste mais crítico em SaaS B2B — verificar que dados de uma organização nunca são visíveis para outra. O teste deve cobrir: listagens (organização A não vê registros da organização B), busca (termo que existe em B não retorna resultados para A), relatórios (métricas de A não incluem dados de B), exportação (arquivo exportado por A contém apenas dados de A), e API (request autenticado como usuário de A retorna 403 ao acessar recurso de B). Um único vazamento de dados cross-tenant pode resultar em perda de clientes enterprise, processos legais e destruição de reputação. Este teste deve ser automatizado e executado em todo deploy.

- **Teste de permissões e RBAC**: Validar que cada papel tem exatamente as permissões definidas — nem mais, nem menos. O teste deve cobrir: admin pode tudo dentro da organização, gerente pode gerenciar membros mas não billing, membro pode executar tarefas mas não configurar, viewer pode ver mas não editar. Testar especificamente: escalação de privilégio (membro tenta acessar endpoint de admin via API direta, sem UI), IDOR (Insecure Direct Object Reference — usuário acessa recurso de outro usuário pela URL alterando o ID), e bypass de UI (ação bloqueada na UI mas permitida via API). Ferramentas como Burp Suite ou OWASP ZAP automatizam parte desses testes.

- **Teste de billing e subscription**: Validar o ciclo completo da assinatura em sandbox do gateway de pagamento — criação com cartão de teste, renovação automática (simulando avanço de tempo no Stripe test clock), falha de pagamento (cartão com número de falha), retry automático, upgrade com proration, downgrade, cancelamento, e reativação. Verificar que o acesso ao produto reflete corretamente o estado da assinatura — trial expirado bloqueia acesso, pagamento falhado após grace period bloqueia acesso, downgrade remove funcionalidades do plano superior imediatamente ou no fim do ciclo (conforme regra definida).

- **Teste de performance e carga**: Rodar testes de carga (k6, Artillery, ou Locust) simulando o volume esperado de usuários concorrentes para os primeiros 12 meses. Focar em: tempo de resposta de endpoints críticos sob carga (listagens, dashboards, relatórios), throughput de operações de escrita concorrentes (criação de registros por múltiplos usuários do mesmo tenant), e comportamento do sistema sob pico (Black Friday se aplicável, deadline mensal de reports). Identificar gargalos antes que os clientes reais os encontrem — o teste de carga deve simular cenário realista com múltiplos tenants ativos simultaneamente, não apenas um tenant com muitas requests.

- **Teste de integrações externas**: Validar cada integração com o serviço real (não mock) em ambiente de sandbox — SSO com Identity Provider de teste (Okta dev, Azure AD trial), webhook de billing com Stripe test mode, integração com CRM (Salesforce sandbox), e-mail transacional com domínio de teste. Testar especificamente os cenários de falha: o que acontece quando o IdP está indisponível (fallback para login local?), quando o webhook do Stripe falha (retry automático?), quando o CRM retorna erro (queue e retry ou falha silenciosa?). Integrações que não são testadas com cenários de falha vão falhar em produção no pior momento possível.

- **Teste de segurança e penetração**: Executar scan de vulnerabilidades automatizado (OWASP ZAP, Snyk) cobrindo OWASP Top 10, e idealmente pen test manual para fluxos críticos (autenticação, billing, acesso cross-tenant). Verificar: SQL injection em todos os inputs, XSS em campos de texto rico, CSRF em ações sensíveis (deletar, alterar permissão), exposição de dados em respostas de API (campos sensíveis não devem aparecer em listagens), e headers de segurança (HSTS, CSP, X-Frame-Options). Em B2B enterprise, o cliente vai solicitar relatório de pen test como parte do security review — ter o relatório pronto antes acelera o ciclo de venda.

### Perguntas

1. O teste de isolamento multi-tenant foi executado com verificação de listagens, busca, relatórios, exportação e API cross-tenant? [fonte: QA, Security] [impacto: Dev, Security]
2. O teste de RBAC cobre todas as combinações de papel × recurso × ação, incluindo bypass via API? [fonte: QA, Security] [impacto: Dev, Security]
3. O ciclo completo de billing foi testado em sandbox com cenários de sucesso, falha, retry, upgrade e cancelamento? [fonte: QA, Financeiro] [impacto: Dev, Financeiro]
4. O teste de carga foi executado simulando volume realista de múltiplos tenants concorrentes? [fonte: QA, DevOps] [impacto: Dev, DevOps]
5. Todas as integrações externas foram testadas com serviço real em sandbox, incluindo cenários de falha? [fonte: QA, Dev] [impacto: Dev]
6. O scan de segurança (OWASP ZAP ou equivalente) foi executado e todas as vulnerabilidades críticas foram corrigidas? [fonte: Security, QA] [impacto: Dev, Security]
7. O fluxo de SSO foi testado com Identity Provider real em modo de teste (Okta dev, Azure AD trial)? [fonte: QA, Dev] [impacto: Dev]
8. Os e-mails transacionais foram recebidos corretamente em múltiplos provedores (Gmail, Outlook, Yahoo) sem ir para spam? [fonte: QA, Marketing] [impacto: Dev]
9. A migração de dados dos clientes piloto foi testada com dados reais (anonimizados) em staging? [fonte: QA, Clientes piloto] [impacto: Dev, PM]
10. O onboarding completo de uma nova organização foi testado end-to-end por alguém que não participou do desenvolvimento? [fonte: QA, Produto] [impacto: Dev, PM, Produto]
11. Os relatórios e dashboards foram validados com dados de volume realista e os números conferem com cálculos manuais? [fonte: QA, Produto] [impacto: Dev]
12. O comportamento do sistema com assinatura expirada, trial encerrado e pagamento falhado foi validado? [fonte: QA] [impacto: Dev, Produto]
13. O teste de acessibilidade (WCAG 2.1 AA) foi executado nos fluxos críticos com axe-core e screen reader? [fonte: QA, Designer] [impacto: Dev, Designer]
14. Os headers de segurança (HSTS, CSP, X-Frame-Options) estão configurados corretamente em produção? [fonte: Security, DevOps] [impacto: DevOps, Dev]
15. O relatório de pen test (automatizado ou manual) está pronto para ser apresentado a clientes enterprise no security review? [fonte: Security] [impacto: Comercial, PM]

---

## Etapa 09 — Launch Prep

- **Migração de dados dos clientes piloto**: Executar a migração real dos dados dos clientes piloto para o ambiente de produção — não mais em staging. A migração deve seguir o runbook definido e testado na QA: extração dos dados do sistema de origem (pelo cliente ou pelo time), transformação e validação (conversão de formatos, limpeza de duplicatas, mapeamento de campos), carga no sistema (via importação bulk ou script customizado), e validação pós-migração com o cliente (o cliente precisa confirmar que "os dados estão certos"). A migração deve ser feita com tempo suficiente antes do go-live para permitir ajustes — nunca no mesmo dia.

- **Plano de cutover e rollback**: Documentar a sequência completa de ações do go-live: quem altera o DNS, quem ativa o billing em modo produção, quem envia o e-mail de boas-vindas aos clientes, quem monitora os dashboards nas primeiras horas. Definir critérios de rollback (error rate >5%, falha de billing, vazamento de dados cross-tenant) e a sequência de ações para reverter (apontar DNS de volta, desativar billing, comunicar clientes). O plano deve estar documentado e acessível a todo o time — não apenas na cabeça de uma pessoa. Praticar o rollback em staging antes do go-live.

- **Comunicação com clientes piloto**: Preparar a comunicação de lançamento para os clientes piloto — e-mail de boas-vindas com credenciais de produção (se diferentes de staging), guia de onboarding com passo a passo, canal de suporte prioritário para as primeiras semanas, e calendário de treinamento (se aplicável). Os clientes piloto são os primeiros embaixadores do produto — uma experiência de lançamento desorganizada (credenciais erradas, dados faltando, funcionalidade quebrando no primeiro dia) prejudica a relação para muito além do bug em si. O tom da comunicação deve transmitir controle e profissionalismo.

- **Configuração de billing em produção**: Migrar os planos e produtos do sandbox para o modo produção no gateway de pagamento. Configurar as chaves de API de produção no sistema, validar que os webhooks de produção estão apontando para os endpoints corretos, e testar com uma cobrança real de valor mínimo (se possível). Para clientes piloto com contrato assinado, criar as subscriptions no gateway e vincular aos tenants. Verificar que a emissão de NF-e está configurada com dados fiscais corretos da empresa.

- **Treinamento de equipe de suporte e CS**: O time que vai atender os clientes após o go-live precisa conhecer o produto em profundidade — não apenas os fluxos felizes, mas os cenários de erro, as limitações conhecidas, e os workarounds. Preparar playbook de suporte com: FAQ dos problemas mais prováveis (baseado nos bugs encontrados no QA), fluxo de escalonamento (quando o suporte L1 passa para L2/dev), acesso a ferramentas de troubleshooting (admin panel, logs, dashboard de monitoramento), e templates de comunicação para incidentes. O primeiro mês pós-lançamento é quando o suporte é mais demandado — o time precisa estar preparado.

- **Revisão final de segurança e compliance**: Executar uma revisão final de segurança antes do go-live — verificar que todos os secrets estão em gestão segura (não hardcoded), que os backups estão funcionando e restauráveis, que o audit log está capturando os eventos definidos, que o certificado SSL está válido e com renovação automática, e que as políticas de dados (privacy policy, terms of service, DPA) estão publicadas e acessíveis. Para clientes enterprise, confirmar que a documentação de compliance (SOC 2, security whitepaper) está pronta para ser apresentada.

### Perguntas

1. A migração de dados dos clientes piloto foi concluída em produção e validada pelos clientes? [fonte: Dev, Clientes piloto] [impacto: Dev, PM]
2. O plano de cutover está documentado com sequência de ações, responsáveis e horários definidos? [fonte: DevOps, PM] [impacto: DevOps, PM, Dev]
3. O plano de rollback foi praticado em staging e os critérios de acionamento estão claros para todo o time? [fonte: DevOps, PM] [impacto: DevOps, PM]
4. A comunicação de lançamento para os clientes piloto foi preparada com credenciais, guia e canal de suporte? [fonte: PM, Comercial, CS] [impacto: PM, CS]
5. O billing está configurado em modo produção com planos, webhooks e NF-e validados? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
6. A equipe de suporte/CS foi treinada com playbook, FAQ e acesso a ferramentas de troubleshooting? [fonte: CS, PM, Dev] [impacto: CS, PM]
7. O backup do banco de dados foi testado com restore real e o tempo de recuperação é aceitável? [fonte: DevOps] [impacto: DevOps]
8. Os secrets de produção estão em gestão segura e separados de todos os outros ambientes? [fonte: DevOps, Security] [impacto: DevOps, Dev]
9. As políticas de dados (privacy policy, ToS, DPA) estão publicadas e acessíveis no produto? [fonte: Jurídico] [impacto: Jurídico, Dev]
10. O monitoramento de disponibilidade e a página de status estão ativos e testados com alerta real? [fonte: DevOps] [impacto: DevOps]
11. O certificado SSL está válido, com renovação automática configurada e testada? [fonte: DevOps] [impacto: DevOps, Dev]
12. Todos os stakeholders foram notificados sobre data, horário e procedimentos do go-live? [fonte: PM, Diretoria] [impacto: PM]
13. A janela de go-live foi escolhida em horário de baixo uso, dia útil, com time completo disponível por 4+ horas após? [fonte: PM, DevOps] [impacto: PM, DevOps]
14. O security whitepaper e a documentação de compliance estão prontos para apresentação a clientes enterprise? [fonte: Security, Jurídico] [impacto: Comercial]
15. Os critérios de aceite do MVP foram revisados com os clientes piloto e estão satisfeitos? [fonte: Produto, Clientes piloto, PM] [impacto: PM, Produto]

---

## Etapa 10 — Go-Live

- **Execução do cutover e monitoramento em tempo real**: Executar o plano de cutover conforme documentado — ativação de DNS, billing em modo produção, envio de credenciais aos clientes. Monitorar em tempo real durante as primeiras 4 horas: dashboards de infraestrutura (CPU, memória, latência, error rate), logs de aplicação (erros 5xx, falhas de autenticação, problemas de billing), e canais de suporte (primeiros tickets dos clientes piloto). O time técnico deve estar em canal de comunicação dedicado (Slack channel, war room) com capacidade de responder a incidentes em minutos. Qualquer degradação que ultrapasse os critérios de rollback deve acionar o plano documentado — não improvisar sob pressão.

- **Validação de billing em produção com transação real**: Confirmar que a primeira cobrança real foi processada corretamente — pagamento aprovado pelo gateway, assinatura ativada no sistema, NF-e emitida (se aplicável), e-mail de confirmação enviado ao cliente. Verificar no dashboard do gateway (Stripe Dashboard) que os webhooks estão sendo entregues e processados sem erro. Se o modelo inclui trial, verificar que o countdown do trial está correto e que o billing será ativado automaticamente na data correta. Uma falha de billing no primeiro dia é visível e embaraçosa — vale verificar manualmente a primeira transação de cada cliente piloto.

- **Onboarding dos clientes piloto em produção**: Acompanhar os primeiros clientes piloto configurando suas organizações em produção — verificar que o SSO está funcionando com o IdP real do cliente (não mais sandbox), que os dados migrados estão acessíveis e corretos, que as permissões de usuários estão refletindo a estrutura organizacional do cliente, e que os fluxos críticos de negócio funcionam com dados reais. Estar disponível para troubleshooting imediato — os primeiros minutos de uso real em produção são quando os problemas que nenhum teste previu aparecem.

- **Monitoramento da primeira semana**: Além da infraestrutura, monitorar métricas de produto na primeira semana — ativações (clientes que completaram o onboarding), retention (clientes que voltaram no dia seguinte), feature usage (quais módulos estão sendo usados e quais estão sendo ignorados), e tickets de suporte (volume, categoria, tempo de resolução). Esses dados são o primeiro feedback real do mercado e devem alimentar diretamente o backlog de produto. Se clientes piloto estão ignorando uma funcionalidade que deveria ser core, isso é sinal de problema de UX ou de fit produto-mercado que precisa ser investigado imediatamente.

- **Retrospectiva de lançamento e entrega formal**: Após a primeira semana estável, conduzir retrospectiva com o time — o que funcionou, o que deu errado, o que precisa melhorar para o próximo release. Entregar formalmente ao cliente os acessos e a documentação: acesso ao painel administrativo do produto, acesso ao dashboard de billing (portal do Stripe ou equivalente), documentação de API (se pública), guia de administração, canal de suporte com SLA definido, e page de status para acompanhamento de incidentes. Obter aceite formal (e-mail, assinatura de ata) que marca a transição do modo "projeto" para o modo "produto" — com suporte contínuo, roadmap de evolução e SLA operacional.

- **Ativação de processos operacionais contínuos**: Ativar os processos que mantêm o produto saudável após o lançamento — monitoramento de disponibilidade 24/7 com alertas (PagerDuty, OpsGenie), processo de incident response com runbooks por tipo de incidente, renovação automática de certificados SSL, atualização de dependências com scan semanal de vulnerabilidades (Dependabot/Snyk), e backup validado com restore mensal. SaaS B2B é compromisso contínuo — o go-live é o início da operação, não o fim do projeto.

### Perguntas

1. O cutover foi executado conforme o plano documentado e o time está em war room monitorando em tempo real? [fonte: DevOps, PM] [impacto: DevOps, PM, Dev]
2. A primeira cobrança real foi processada corretamente no gateway com NF-e emitida e confirmação ao cliente? [fonte: Dev, Financeiro] [impacto: Financeiro, Dev]
3. Os clientes piloto completaram o onboarding em produção com SSO, dados migrados e fluxos críticos validados? [fonte: CS, Clientes piloto] [impacto: PM, Dev, CS]
4. O monitoramento de infraestrutura mostra métricas dentro dos thresholds esperados nas primeiras 4 horas? [fonte: DevOps] [impacto: DevOps, Dev]
5. Os webhooks de billing estão sendo entregues e processados sem erro no dashboard do gateway? [fonte: Dev] [impacto: Dev, Financeiro]
6. Os canais de suporte estão operacionais e os primeiros tickets foram respondidos dentro do SLA? [fonte: CS, PM] [impacto: CS]
7. O backup de produção foi verificado (executado com sucesso) imediatamente após o go-live? [fonte: DevOps] [impacto: DevOps]
8. As métricas de produto (ativação, feature usage, retention) estão sendo coletadas corretamente? [fonte: Produto, Dev] [impacto: Produto, PM]
9. A página de status está ativa e comunicando o estado real do serviço aos clientes? [fonte: DevOps] [impacto: DevOps, CS]
10. O processo de incident response foi testado com incidente simulado e o runbook foi seguido? [fonte: DevOps, PM] [impacto: DevOps]
11. A retrospectiva de lançamento foi conduzida com o time e os aprendizados foram documentados? [fonte: PM] [impacto: PM, Dev, DevOps]
12. Todos os acessos foram entregues formalmente aos clientes e cada pessoa confirmou acesso funcional? [fonte: PM, CS] [impacto: PM]
13. O aceite formal de entrega foi obtido dos clientes piloto (e-mail, assinatura, confirmação documentada)? [fonte: PM, Comercial] [impacto: PM]
14. O plano de suporte pós-lançamento está ativado com SLA, canais e escalação definidos e comunicados? [fonte: PM, CS, Diretoria] [impacto: PM, CS]
15. Os processos operacionais contínuos (monitoramento 24/7, backup, scan de vulnerabilidades) foram ativados? [fonte: DevOps] [impacto: DevOps]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Vamos começar B2C e depois pivotar para B2B"** — B2B e B2C têm requisitos arquiteturais fundamentalmente diferentes — multi-tenancy, permissões por organização, SSO corporativo, audit logs e billing por contrato não são features que se "adicionam depois". Uma arquitetura desenhada para B2C (usuário individual, self-service puro, sem isolamento organizacional) precisa de refatoração estrutural profunda para atender B2B. Decidir o modelo de negócio antes de começar.
- **"O SLA a gente define depois"** — SLA impacta diretamente a arquitetura (redundância, failover, multi-region), o custo de infraestrutura e o tamanho da equipe de operação. Definir SLA depois que a arquitetura está feita resulta em promessas que a infraestrutura não sustenta ou em refatoração cara para adicionar alta disponibilidade retroativamente.
- **"Não precisamos de compliance agora"** — Clientes enterprise perguntam sobre SOC 2, ISO 27001 e LGPD na primeira reunião de vendas. Adiar compliance significa perder deals enterprise. Além disso, implementar audit logs, criptografia e gestão de dados retroativamente é ordens de magnitude mais caro do que fazer desde o início.

### Etapa 02 — Discovery

- **"Multi-tenancy é só colocar tenant_id nas tabelas"** — Multi-tenancy é decisão arquitetural profunda que afeta queries, migrations, backup, performance, segurança e compliance. Tratar como "apenas um campo" resulta em vazamento de dados entre tenants (vulnerabilidade crítica), queries sem índice que degradam com escala, e impossibilidade de atender requisitos de isolamento de clientes enterprise.
- **"SSO é para depois, vamos lançar com login e senha"** — Para clientes enterprise, SSO é pré-requisito de segurança, não feature. Sem SSO, o deal não avança do security review. Planejar a arquitetura de auth sem SSO e adicioná-lo depois resulta em refatoração do fluxo de autenticação inteiro — incluindo gestão de sessões, provisionamento de usuários e logout.
- **"Billing é simples, é só Stripe"** — Stripe resolve o processamento de pagamento, não a lógica de negócio. Proration em upgrade, grace period em falha de pagamento, emissão de NF-e, metering por uso, e reconciliação financeira são complexidades que precisam ser mapeadas no Discovery ou serão descobertas dolorosamente durante o Build.

### Etapa 03 — Alignment

- **"O MVP atende todos os segmentos"** — Um MVP que tenta atender PME, mid-market e enterprise ao mesmo tempo não atende nenhum bem. PME quer simplicidade e self-service, enterprise quer customização e suporte dedicado. Priorizar um segmento e fazer bem, depois expandir.
- **"Os clientes piloto vão se adaptar ao que entregarmos"** — Clientes piloto em B2B estão avaliando se o produto substitui o que já usam. Se o MVP não cobre os fluxos críticos que eles precisam, vão voltar para a solução anterior e a credibilidade do produto é prejudicada permanentemente. Validar o escopo com os clientes piloto antes de buildar.
- **"Integrações a gente faz sob demanda"** — Sem estratégia de integração (webhooks genéricos, API pública, marketplace de integrações), cada pedido de cliente vira código custom que o time mantém forever. O custo de manutenção de 10 integrações custom excede rapidamente o custo de uma API pública bem documentada.

### Etapa 04 — Definition

- **Modelo de dados sem tenant_id em todas as entidades** — Se a modelagem de dados não reflete multi-tenancy em cada entidade, o isolamento é impossível de garantir a posteriori. Adicionar tenant_id em tabelas que já têm milhões de registros e foreign keys cruzadas é migração com risco de downtime.
- **"A API a gente documenta quando estiver pronta"** — API sem contrato definido antes do build resulta em endpoints inconsistentes (GET /users vs. GET /user, paginação diferente por endpoint, erros sem padrão). Para B2B com API pública, inconsistência é inaceitável — clientes integram e esperam estabilidade.
- **Billing definido com "planos simples, sem complicação"** — "Simples" esconde os edge cases: o que acontece quando o cliente adiciona um seat no meio do mês? E quando o pagamento falha três vezes seguidas? E quando o cliente quer downgrade mas já usou cota do plano superior? Cada edge case não definido na Definition será resolvido com improviso no Build.

### Etapa 05 — Architecture

- **"Vamos usar microservices desde o início"** — Microservices adicionam complexidade operacional massiva (deploy independente, service discovery, distributed tracing, eventual consistency). Para um time de 3-10 pessoas construindo um MVP, monolito modular é a escolha correta. Microservices fazem sentido quando há equipes independentes que precisam deployar independentemente — não antes.
- **"Hospedamos no servidor on-premise do cliente"** — SaaS é multi-tenant por definição. Hospedar por cliente elimina as vantagens de SaaS (uma instância, muitos clientes) e transforma o produto em software instalável. Se clientes exigem on-premise, o modelo de negócio não é SaaS — é software enterprise com contrato de licença.
- **"Auth a gente faz custom, não precisa de serviço externo"** — Build from scratch de auth corporativo (SSO SAML/OIDC, MFA, SCIM, session management, rate limiting, brute force protection) consome meses de desenvolvimento e é fonte permanente de vulnerabilidades de segurança. Serviços como Auth0, Clerk ou WorkOS custam menos por mês do que um dia de salário do engenheiro que iria manter a solução custom.

### Etapa 06 — Setup

- **Staging com banco de produção** — Usar o banco de dados de produção no ambiente de staging para "ter dados reais para testar". Resultado: um teste que deleta registros em staging apaga dados de clientes reais. Ambientes devem ter bancos completamente isolados — usar dados anonimizados ou seed data em staging.
- **Secrets em variáveis de ambiente do CI/CD** — API keys, tokens de pagamento e secrets armazenados nas variáveis de ambiente do GitHub Actions ou GitLab CI. Qualquer pessoa com acesso ao repositório pode ler. Usar serviço de gestão de secrets (Vault, AWS Secrets Manager) com acesso restrito por papel.
- **"Monitoramento a gente configura depois do lançamento"** — Monitoramento é pré-requisito do go-live, não melhoria pós-lançamento. Sem alertas configurados, o primeiro a saber que o serviço caiu é o cliente — não o time. Configurar métricas, alertas e dashboard antes de subir tráfego real.

### Etapa 07 — Build

- **"O isolamento de tenant está no frontend"** — Filtrar dados por organização apenas no frontend (escondendo registros na UI) enquanto a API retorna dados de todos os tenants. Qualquer ferramenta de inspeção de rede (DevTools) expõe dados de outros clientes. O isolamento obrigatoriamente precisa estar no backend — em toda query, em todo endpoint.
- **Webhooks sem retry e sem idempotência** — Webhooks de billing (Stripe) e de integrações são entregues at-least-once, não exactly-once. Sem tratamento de idempotência, o sistema pode processar o mesmo pagamento duas vezes ou enviar o mesmo e-mail dez vezes. Cada handler de webhook precisa de idempotency key.
- **"Testes de permissão a gente faz no QA"** — Se o RBAC não é testado durante o Build com testes automatizados, vulnerabilidades de acesso se acumulam e são difíceis de identificar no QA manual. Cada endpoint deve ter teste que valida acesso por papel — o teste é parte do Build, não do QA.

### Etapa 08 — QA

- **"Testamos com um tenant, está funcionando"** — Um tenant funciona, mas dois tenants simultâneos revelam vazamento de dados, race conditions em recursos compartilhados, e queries sem filtro de tenant_id. O QA de SaaS B2B obrigatoriamente precisa de testes com múltiplos tenants ativos ao mesmo tempo.
- **Teste de billing apenas com cartão válido** — O cenário mais crítico de billing não é o pagamento com sucesso — é a falha. Cartão recusado, cartão expirado, disputa de cobrança (chargeback), trial expirado sem conversão. Se esses cenários não são testados, o sistema pode falhar silenciosamente — cobrança não processa, acesso não é bloqueado, e o cliente usa sem pagar.
- **"A performance tá boa, testei local"** — Performance local (banco na mesma máquina, sem latência de rede, sem concorrência) não reflete produção. Teste de carga em staging com latência realista, múltiplos tenants e volume de dados representativo é o mínimo. Sem isso, o primeiro lote de clientes reais vai encontrar lentidão que o dev nunca viu.

### Etapa 09 — Launch Prep

- **Migração de dados no dia do go-live** — Migrar dados de clientes na mesma janela do go-live cria dependência crítica — se a migração falha, o go-live atrasa. Migração deve ser feita com 3-5 dias de antecedência com validação do cliente. Go-live e migração são eventos separados.
- **"O suporte começa quando alguém reclamar"** — Sem playbook de suporte, equipe treinada e ferramentas configuradas, os primeiros tickets são respondidos com improviso. O cliente enterprise percebe imediatamente quando o suporte não está preparado — e isso afeta renovação de contrato.
- **Billing ativado em produção sem teste de transação real** — Ativar billing em produção e esperar que "funcione igual ao sandbox" sem testar uma transação real. Diferenças de configuração entre sandbox e produção (webhook URL, API keys, configuração de retry) podem impedir cobranças no primeiro mês inteiro.

### Etapa 10 — Go-Live

- **Go-live sem war room e sem monitoramento ativo** — "Subiu, vamos almoçar." Sem monitoramento ativo nas primeiras horas, problemas que poderiam ser resolvidos em minutos se acumulam e viram crise. War room com dashboards abertos e time disponível é obrigatório por pelo menos 4 horas após o cutover.
- **Hospedagem legada desativada no mesmo dia** — O cliente tinha um sistema anterior que foi desligado no momento do go-live do novo SaaS. Se algo der errado, não há para onde voltar. Manter o sistema anterior acessível (mesmo em modo read-only) por 30 dias como contingência.
- **"O produto está no ar, projeto encerrado"** — SaaS não tem "encerramento" — o go-live é o início da operação contínua. Sem processos de monitoramento, backup, atualização de dependências e resposta a incidentes ativados, o produto degrada silenciosamente até o primeiro incidente grave, que acontece sem preparação.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é SaaS B2B** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Cada cliente terá um servidor dedicado com deploy separado" | Software enterprise on-premise, não SaaS | Reclassificar para software-enterprise ou avaliar modelo de single-tenant SaaS |
| "O produto é para consumidores individuais, sem organização" | SaaS B2C, não B2B | Reclassificar para saas-b2c |
| "Não precisa de login, é um site com conteúdo" | Site estático ou CMS | Reclassificar para static-site ou web-app |
| "É uma loja online com carrinho e checkout" | E-commerce | Reclassificar para e-commerce |
| "O cliente compra uma vez e usa para sempre, sem assinatura" | Software com licença perpétua, não SaaS | Reclassificar para software-enterprise |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos qual é o modelo de pricing ainda" | 01 | Impossível definir billing, feature gating e tiers sem modelo de pricing | Definir modelo de monetização antes de avançar |
| "Não temos clientes piloto confirmados" | 01 | MVP sem validação real — risco de construir produto que ninguém quer | Confirmar 3-5 clientes piloto antes de avançar para Discovery |
| "Compliance a gente vê depois que o produto estiver pronto" | 01 | Retrofit de compliance é 5-10x mais caro. Perde deals enterprise | Mapear requisitos de compliance antes da Architecture |
| "Não temos acesso ao Identity Provider do cliente para testar SSO" | 06 | SSO não testado com IdP real vai falhar no onboarding do cliente | Obter acesso de teste ao IdP do cliente piloto antes do QA |
| "O orçamento cobre só o desenvolvimento, infra a gente vê depois" | 01 | SaaS tem custo mensal contínuo — sem orçamento de operação, o produto morre em 6 meses | Apresentar TCO (dev + infra + operação) antes de continuar |
| "Não definimos quem vai dar suporte após o lançamento" | 03 | Primeiro ticket do cliente enterprise sem resposta destrói credibilidade | Definir modelo de suporte e dimensionar equipe antes do Build |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Cada cliente quer integrações diferentes" | 02 | Escopo de integrações explode e consome capacidade do time | Definir estratégia de integração (API + webhooks) em vez de custom por cliente |
| "O time tem 3 pessoas e o prazo é 3 meses" | 01 | MVP subentregue ou qualidade comprometida | Recalibrar escopo do MVP para a capacidade real do time |
| "Vamos suportar todos os métodos de pagamento" | 04 | Cada método de pagamento é integração separada com edge cases próprios | Priorizar 1-2 métodos no MVP, adicionar incrementalmente |
| "O cliente quer deploy em região específica (EU, BR)" | 05 | Multi-region adiciona complexidade e custo significativos | Avaliar se é requisito de compliance real ou preferência negociável |
| "Microservices desde o dia 1" | 05 | Over-engineering para o tamanho do time | Recomendar monolito modular, migrar para microservices quando justificar |
| "Os clientes são todos diferentes, cada um tem fluxo próprio" | 03 | Produto vira consultoria — cada cliente é projeto custom | Definir fluxos padronizados com pontos de configuração, não customização ilimitada |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Modelo de monetização definido (pergunta 1)
- Requisitos de compliance mapeados (pergunta 3)
- Clientes piloto identificados e com acesso para feedback (pergunta 9)
- Prazo de MVP com justificativa de negócio (pergunta 8)
- Orçamento separando dev, infra e operação (pergunta 13)

### Etapa 02 → 03

- Personas e jornadas mapeadas (pergunta 1)
- Requisitos de autenticação e autorização definidos (perguntas 2 e 3)
- Modelo de billing e pricing detalhado (pergunta 7)
- Integrações bloqueadoras identificadas (pergunta 4)

### Etapa 03 → 04

- MVP validado com clientes piloto (pergunta 1)
- Modelo de permissões acordado (pergunta 3)
- SLA de disponibilidade e suporte definidos (perguntas 4 e 5)
- Estratégia de migração dos clientes piloto planejada (pergunta 6)

### Etapa 04 → 05

- Modelo de dados multi-tenant especificado (pergunta 1)
- Contratos de API definidos em OpenAPI (pergunta 2)
- Ciclo de vida de subscription detalhado (pergunta 5)
- Audit logs especificados (pergunta 10)
- Documentação revisada por Produto, Arquitetura e clientes piloto (pergunta 15)

### Etapa 05 → 06

- Estratégia de multi-tenancy decidida e justificada (pergunta 1)
- Stack de auth com SSO definida (pergunta 2)
- Estratégia de deploy zero-downtime desenhada (pergunta 5)
- Custos projetados por cenário de crescimento (pergunta 13)
- Security whitepaper redigido (pergunta 15)

### Etapa 06 → 07

- Infraestrutura provisionada via IaC (pergunta 1)
- Pipeline de CI/CD funcionando end-to-end (perguntas 2 e 15)
- Billing configurado em sandbox com planos e webhooks testados (pergunta 4)
- Monitoramento e alertas configurados (pergunta 7)

### Etapa 07 → 08

- Autenticação com SSO e MFA funcionando (pergunta 1)
- Billing processando subscription lifecycle completo (pergunta 2)
- Isolamento multi-tenant testado com dados cruzados (pergunta 4)
- Features core demonstradas e validadas pelos clientes piloto (pergunta 5)

### Etapa 08 → 09

- Teste de isolamento multi-tenant executado e aprovado (pergunta 1)
- RBAC testado com bypass via API (pergunta 2)
- Billing testado com cenários de falha (pergunta 3)
- Teste de carga executado com resultados aceitáveis (pergunta 4)
- Scan de segurança sem vulnerabilidades críticas (pergunta 6)

### Etapa 09 → 10

- Migração dos clientes piloto concluída e validada (pergunta 1)
- Plano de rollback praticado em staging (pergunta 3)
- Billing em produção validado com transação real (pergunta 5)
- Equipe de suporte treinada com playbook (pergunta 6)
- Aceite dos clientes piloto obtido (pergunta 15)

### Etapa 10 → Encerramento

- Cutover executado com monitoramento ativo (pergunta 1)
- Billing real processado com sucesso (pergunta 2)
- Clientes piloto em onboarding em produção (pergunta 3)
- Processos operacionais contínuos ativados (pergunta 15)
- Aceite formal obtido (pergunta 13)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de SaaS B2B. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Horizontal PME | V2 Vertical Nicho | V3 Enterprise | V4 Marketplace | V5 API-First |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 3 | 3 | 3 |
| 02 Discovery | 3 | 4 | 4 | 4 | 3 |
| 03 Alignment | 2 | 3 | 4 | 3 | 2 |
| 04 Definition | 3 | 4 | 5 | 5 | 4 |
| 05 Architecture | 3 | 4 | 5 | 4 | 5 |
| 06 Setup | 3 | 3 | 4 | 3 | 4 |
| 07 Build | 4 | 5 | 5 | 5 | 4 |
| 08 QA | 3 | 4 | 5 | 4 | 4 |
| 09 Launch Prep | 2 | 3 | 4 | 3 | 3 |
| 10 Go-Live | 2 | 2 | 3 | 2 | 2 |
| **Total relativo** | **27** | **35** | **42** | **36** | **34** |

**Observações por variante:**

- **V1 Horizontal PME**: Esforço concentrado no Build (produto precisa ser self-service e intuitivo) e Definition (modelo de billing e onboarding). Discovery e Alignment são mais leves porque o segmento é genérico e o ciclo de venda é curto.
- **V2 Vertical Nicho**: Pico no Discovery (domínio complexo que precisa ser profundamente entendido) e Build (regras de negócio específicas do setor). Compliance setorial pode adicionar 1-2 pontos na Architecture e no QA.
- **V3 Enterprise**: O mais pesado em todas as etapas. Definition e Architecture são críticos (SSO, SCIM, audit logs, multi-region, feature flags). QA é pesado por incluir pen test e teste de compliance. Launch Prep é complexo pela migração e onboarding assistido.
- **V4 Marketplace**: Pico na Definition (lógica de dois lados, matching, comissionamento) e Build (fluxos distintos para cada lado do marketplace). A dinâmica supply-demand adiciona complexidade que não existe nos outros modelos.
- **V5 API-First**: Architecture é o mais pesado (rate limiting, versionamento de API, observabilidade). Build é relativamente leve (menos UI), mas QA é pesado (testes de API com cenários de carga, rate limiting e SDK compatibility).

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sem SSO no MVP — apenas login local (Etapa 02, pergunta 3) | Etapa 04: pergunta 7 (diagramas de fluxo SSO). Etapa 06: testes com IdP externo. Etapa 07: pergunta 1 parcial (SSO pode ser omitido). Etapa 08: pergunta 7 (teste SSO com IdP real). |
| Sem API pública — apenas interface web (Etapa 01, pergunta 15) | Etapa 04: perguntas 2, 9 (contratos de API, rate limiting). Etapa 05: pergunta 11 (versionamento de API). Etapa 07: pergunta 15 (documentação de API). Etapa 08: teste de SDK e API pública. |
| Modelo de pricing fixo sem cobrança por uso (Etapa 01, pergunta 1) | Etapa 05: pergunta 3 parcial (metering não necessário). Etapa 07: pergunta 2 parcial (metering de uso pode ser omitido). |
| Sem clientes enterprise no primeiro ano (Etapa 01, pergunta 14) | Etapa 04: pergunta 10 parcial (audit logs simplificados). Etapa 05: pergunta 14 (data residency). Etapa 05: pergunta 15 (security whitepaper pode ser adiado). Etapa 09: pergunta 14 (documentação de compliance). |
| Produto exclusivamente para mercado brasileiro (Etapa 01, pergunta 12) | Etapa 05: pergunta 14 (data residency simplificada — Brasil apenas). Perguntas de multi-currency em billing. Perguntas de GDPR (apenas LGPD). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| SSO corporativo no MVP (Etapa 02, pergunta 3) | Etapa 04: pergunta 7 (diagramas de fluxo SSO com edge cases) se torna bloqueadora. Etapa 06: configuração de IdP de teste se torna obrigatória. Etapa 08: pergunta 7 (teste com IdP real) se torna gate. |
| API pública para clientes (Etapa 01, pergunta 15) | Etapa 04: pergunta 2 (contratos OpenAPI) se torna bloqueadora. Etapa 05: pergunta 11 (versionamento) se torna obrigatória. Etapa 07: pergunta 15 (docs de API) se torna gate. Etapa 08: teste de SDK e rate limiting obrigatórios. |
| Clientes enterprise com contrato >$5k/mês (Etapa 01, pergunta 14) | Etapa 04: pergunta 10 (audit logs detalhados) se torna bloqueadora. Etapa 05: pergunta 15 (security whitepaper) se torna gate. Etapa 08: pergunta 15 (relatório de pen test) se torna obrigatório. Etapa 09: pergunta 14 (compliance docs) se torna gate. |
| Cobrança por uso / metered billing (Etapa 01, pergunta 1) | Etapa 04: pergunta 5 (lifecycle com metering) se torna complexa e bloqueadora. Etapa 05: pergunta 3 (arquitetura de metering em tempo real) se torna crítica. Etapa 08: pergunta 3 (teste de billing) deve incluir cenários de overage e reconciliação. |
| Migração de dados de sistema legado dos clientes (Etapa 03, pergunta 6) | Etapa 04: pergunta 11 (formatos de importação) se torna bloqueadora. Etapa 07: pergunta 7 (importação com volume real) se torna gate. Etapa 08: pergunta 9 (teste de migração com dados reais) se torna obrigatória. Etapa 09: pergunta 1 (migração em produção) se torna o maior risco do lançamento. |
| Requisitos LGPD/GDPR com DPA contratual (Etapa 01, pergunta 3) | Etapa 05: pergunta 6 (criptografia e gestão de dados) se torna bloqueadora. Etapa 05: pergunta 14 (data residency) se torna obrigatória. Etapa 09: pergunta 9 (políticas publicadas) se torna gate. Etapa 10: DPA assinado com clientes antes do onboarding. |
