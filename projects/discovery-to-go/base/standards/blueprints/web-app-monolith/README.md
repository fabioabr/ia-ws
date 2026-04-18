---
title: "Web App Monolítica — Blueprint"
description: "Aplicação web completa com backend único e coeso. Toda a lógica de negócio em um processo. Frameworks como Django, Rails, Laravel ou NestJS monolito."
category: project-blueprint
type: web-app-monolith
status: rascunho
created: 2026-04-13
---

# Web App Monolítica

## Descrição

Aplicação web completa com backend único e coeso. Toda a lógica de negócio em um processo, com banco de dados compartilhado. Frameworks full-stack como Django, Rails, Laravel, NestJS ou Spring Boot. Deploy como unidade única. Ideal para times pequenos a médios, domínios de complexidade moderada, e projetos que precisam de velocidade de entrega sem overhead de infraestrutura distribuída.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda aplicação monolítica é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — SaaS B2B com Painel Administrativo

Aplicação multi-tenant com painel admin robusto para gestão de dados, usuários e configurações por cliente. Domínio de negócio tipicamente moderado (CRM simples, gestão de projetos, ferramenta de produtividade). O painel administrativo frequentemente representa 60-70% do esforço de desenvolvimento. Autenticação com múltiplos roles (admin, gerente, operador, viewer), billing integrado, e onboarding de novos tenants são features centrais. Exemplos: ferramenta de gestão de tarefas, CRM para PMEs, plataforma de agendamento, sistema de helpdesk.

### V2 — Aplicação Interna (Back-office / ERP Departamental)

Sistema interno usado por funcionários da empresa cliente — não exposto à internet pública. Foco em produtividade operacional: formulários complexos, workflows de aprovação, relatórios, integrações com sistemas internos (ERP, RH, financeiro). Requisitos de UX são mais baixos que em produtos SaaS, mas requisitos de segurança e auditoria podem ser altos (controle de acesso granular, log de ações, compliance). Time de usuários é pequeno (10-200) e conhecido. Exemplos: sistema de aprovação de compras, gestão de contratos, portal do RH, backoffice de operações.

### V3 — MVP / Startup Product

Produto digital em estágio inicial — validação de hipótese de mercado com velocidade de entrega como prioridade absoluta. O escopo é intencionalmente reduzido ao mínimo necessário para testar product-market fit. A arquitetura monolítica é a escolha correta porque permite iteração rápida, deploy simples e custo de operação baixo. O desafio é equilibrar velocidade com qualidade mínima de código que permita evolução posterior sem reescrever do zero. Exemplos: MVP de marketplace, MVP de plataforma de ensino, produto digital em fase de validação com investidores.

### V4 — Portal com Área Logada e Conteúdo

Aplicação que combina conteúdo público (blog, institucional, documentação) com área logada que oferece funcionalidades específicas (dashboard, configurações, histórico, downloads). O frontend tem duas "personalidades" — páginas públicas otimizadas para SEO e performance, e área logada otimizada para funcionalidade e interatividade. Server-side rendering para páginas públicas e SPA ou CSR para área logada é o padrão arquitetural comum. Exemplos: portal de cursos com área do aluno, site de serviço com área do cliente, portal de associação com área de membros.

### V5 — API Monolítica com Frontend Desacoplado

Backend monolítico que expõe API REST ou GraphQL consumida por frontend SPA (React, Vue, Angular) deployado separadamente. A separação de deploy entre frontend e backend permite que times de frontend e backend trabalhem com ciclos independentes, mas toda a lógica de negócio permanece em um único processo no backend. É o meio-termo entre monolito full-stack (tudo junto) e microserviços (tudo separado). Exemplos: dashboard analítico, sistema de gestão com frontend moderno, aplicação que precisa de app mobile no futuro (mesma API serve web e mobile).

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Backend | Frontend | Banco de Dados | Hospedagem | Observações |
|---|---|---|---|---|---|
| V1 — SaaS B2B | NestJS ou Rails | Next.js (SSR) ou React | PostgreSQL | AWS (ECS/Fargate) ou Railway | Multi-tenancy por schema ou tenant_id. Stripe para billing. |
| V2 — Back-office | Django ou Laravel | Templates server-side ou React Admin | PostgreSQL | VPS (Hetzner, DigitalOcean) ou AWS | LDAP/SSO para autenticação corporativa. |
| V3 — MVP/Startup | Next.js full-stack ou Rails | Next.js (integrado) ou React | PostgreSQL ou Supabase | Vercel, Railway ou Render | Priorizar velocidade. Supabase como BaaS para acelerar. |
| V4 — Portal + Área Logada | Next.js ou NestJS + Next.js | Next.js (SSR público + CSR logado) | PostgreSQL | Vercel ou AWS | SSR para SEO público. Auth com NextAuth ou Clerk. |
| V5 — API + SPA | NestJS, Django REST ou Spring Boot | React, Vue ou Angular (SPA) | PostgreSQL | Backend: AWS/Railway. Frontend: Vercel/Netlify | OpenAPI obrigatório. CORS configurado. Deploy separado. |

---

## Etapa 01 — Inception

- **Origem da demanda e escopo real**: A demanda por aplicação web monolítica geralmente surge de necessidade de digitalizar um processo manual (planilhas Excel, e-mails, documentos físicos), substituir um sistema legado que não atende mais (Access, sistema desktop, Delphi, PHP antigo), ou criar um produto digital novo. Entender o gatilho real é crucial — se o problema é processo manual, o foco do projeto é workflow e usabilidade; se é sistema legado, o foco inclui migração de dados e paridade de funcionalidades; se é produto novo, o foco é velocidade de entrega e validação de mercado. Cada cenário tem perfil de risco completamente diferente.

- **Stakeholders e usuários reais**: Identificar quem patrocina o projeto (quem paga), quem decide funcionalidades (product owner), e quem vai usar o sistema no dia a dia (usuários finais). Em aplicações internas, o patrocinador costuma ser um diretor que não vai usar o sistema — os usuários reais são operadores, analistas ou gerentes cujas necessidades são frequentemente diferentes do que o patrocinador imagina. Incluir representantes dos usuários reais desde a Inception evita o cenário clássico de entregar um sistema que agrada a diretoria mas é rejeitado por quem precisa usar.

- **Expectativa de escala e crescimento**: Monolitos atendem perfeitamente aplicações com até milhares de usuários concorrentes — o mito de que "monolito não escala" é falso para a maioria dos casos reais. Levantar a expectativa de crescimento para 12-24 meses: número de usuários, volume de dados, e concorrência de requests. Se a expectativa é 100 usuários fazendo CRUD, um monolito em VPS resolve por anos. Se é 100.000 usuários com operações pesadas em tempo real, vale avaliar se componentes específicos precisarão ser extraídos para serviços independentes no futuro — e desenhar o monolito de forma modular para facilitar essa extração.

- **Orçamento e modelo de operação**: Monolitos são significativamente mais baratos de operar que microserviços — um servidor ou container hospedando toda a aplicação, um banco de dados, e um pipeline de CI/CD. O custo mensal típico varia de $20-50/mês (VPS compartilhada para MVP) a $500-2.000/mês (instância dedicada com banco gerenciado para SaaS em crescimento). Apresentar o TCO (desenvolvimento + operação mensal + suporte) para que o cliente tome decisão informada. Clientes vindos de agências que cobravam apenas o desenvolvimento frequentemente não antecipam custos recorrentes de hosting e manutenção.

- **Requisitos de segurança e compliance**: Aplicações web com dados de usuários têm obrigações de LGPD por padrão (consentimento, direito de acesso, direito de exclusão). Sistemas que lidam com dados financeiros podem ter requisitos de PCI-DSS. Sistemas de saúde têm requisitos de HIPAA ou regulamentações locais. Sistemas internos corporativos podem exigir SSO via LDAP/SAML/OIDC e auditoria de ações. Identificar requisitos de compliance na Inception é obrigatório porque impactam diretamente a arquitetura (criptografia, logging de auditoria, controle de acesso, retenção de dados).

- **Capacidade técnica do time de operação pós-entrega**: Se o projeto será entregue para um time interno do cliente operar e evoluir, é necessário alinhar a stack com a capacidade técnica desse time. Entregar um sistema em Elixir/Phoenix para uma empresa cujo time interno só conhece PHP é receita para abandono ou reescrita. A escolha de framework e linguagem deve considerar não apenas adequação técnica, mas também empregabilidade (facilidade de contratar devs que conheçam a stack) e continuidade (time do cliente consegue manter e evoluir sem depender eternamente da agência/consultoria).

### Perguntas

1. Qual é o gatilho real da demanda — digitalizar processo manual, substituir sistema legado, ou criar produto novo? [fonte: Diretoria, Produto, TI] [impacto: PM, Arquiteto, Dev]
2. Quem é o patrocinador executivo, quem define funcionalidades, e quem são os usuários reais que vão operar o sistema diariamente? [fonte: Diretoria, RH, Operações] [impacto: PM, UX, Dev]
3. Qual é a expectativa de número de usuários, volume de dados e concorrência para os próximos 12-24 meses? [fonte: Produto, Comercial, Diretoria] [impacto: Arquiteto, DevOps]
4. Qual é o orçamento total disponível, separando desenvolvimento, infraestrutura mensal e suporte/manutenção? [fonte: Financeiro, Diretoria] [impacto: PM, DevOps]
5. Existe sistema legado que será substituído ou é criação do zero? [fonte: TI, Operações] [impacto: Dev, PM, Arquiteto]
6. Quais dados sensíveis o sistema vai processar e quais requisitos de compliance se aplicam (LGPD, PCI-DSS, HIPAA, SOC2)? [fonte: Jurídico, DPO, Compliance] [impacto: Arquiteto, Dev, DevOps]
7. O sistema será operado e evoluído por time interno do cliente ou ficará sob responsabilidade do time que desenvolveu? [fonte: CTO, Diretoria] [impacto: PM, Arquiteto, Dev]
8. Se time interno, qual é a capacidade técnica desse time (linguagens, frameworks, experiência com cloud)? [fonte: CTO, Tech Lead do cliente] [impacto: Arquiteto, Dev]
9. Qual é o prazo esperado para o go-live e existe data de negócio que o justifica (contrato, regulatório, lançamento)? [fonte: Diretoria, Comercial] [impacto: PM, Dev]
10. Há preferência ou restrição por cloud provider, linguagem, framework ou banco de dados? [fonte: TI, CTO] [impacto: Arquiteto, Dev]
11. O sistema precisará de aplicativo mobile nativo no futuro (iOS, Android) consumindo a mesma API? [fonte: Produto, Diretoria] [impacto: Arquiteto, Dev]
12. Existe conteúdo público (blog, landing page) que precisa de SEO, ou o sistema é 100% área logada? [fonte: Marketing, Produto] [impacto: Arquiteto, Dev]
13. O domínio DNS, certificados e ambientes cloud já estão disponíveis ou precisam ser provisionados? [fonte: TI, DevOps] [impacto: DevOps, Dev]
14. Quantas pessoas vão trabalhar no desenvolvimento simultaneamente e qual o nível de senioridade? [fonte: CTO, PM] [impacto: Arquiteto, PM]
15. Há integrações obrigatórias no MVP (gateway de pagamento, ERP, CRM, serviço de e-mail, SSO corporativo)? [fonte: TI, Produto, Comercial] [impacto: Dev, Arquiteto]

---

## Etapa 02 — Discovery

- **Levantamento de funcionalidades e priorização**: Mapear todas as funcionalidades desejadas e classificar em três grupos: MVP (mínimo para go-live), next (segunda release, planejada), e backlog (futuro indefinido). A armadilha clássica é o MVP inflado — tudo é "obrigatório" segundo o cliente, mas a análise revela que 30-40% das funcionalidades podem esperar sem impactar o lançamento. A priorização deve ser feita com critério de negócio: quais funcionalidades geram receita ou bloqueiam operação desde o dia 1? Essas são MVP. O resto é next ou backlog.

- **Personas e jornadas de usuário**: Definir as personas (perfis de usuário com necessidades e comportamentos distintos) e mapear as jornadas críticas de cada uma. Exemplo em SaaS B2B: admin (configura tenant, gerencia usuários, consulta billing), gerente (aprova solicitações, vê relatórios), operador (executa tarefas do dia a dia, entrada de dados). Cada persona terá telas, permissões e fluxos diferentes. Jornadas de usuário documentadas são o insumo para wireframes e para definir os gates de QA — o que testar é definido pelas jornadas críticas.

- **Requisitos de autenticação e autorização**: Definir o modelo de autenticação (e-mail/senha, social login, SSO corporativo via SAML/OIDC, MFA) e o modelo de autorização (RBAC com roles fixos, RBAC com roles customizáveis por tenant, ABAC com policies granulares). A complexidade de autorização é frequentemente subestimada — "admin e usuário normal" na Inception se torna "admin global, admin do tenant, gerente, operador, viewer, e permissões customizáveis por módulo" durante o build. Definir o modelo com granularidade real na Discovery evita refatoração de middleware e banco durante o Build.

- **Requisitos de relatórios e dashboards**: Levantar quais dados os usuários precisam visualizar (KPIs, métricas de negócio, listagens com filtros), em qual formato (tabelas, gráficos, PDF para impressão), e com qual frequência de atualização (real-time, a cada 5 minutos, diário). Relatórios em monolito podem ser gerados diretamente do banco de dados principal — mas consultas analíticas pesadas (aggregations em milhões de registros) podem impactar a performance das operações transacionais. Se o volume de dados justifica, considerar read replicas ou um modelo CQRS leve (tabela desnormalizada para leitura atualizada via triggers ou jobs).

- **Integrações externas**: Mapear todas as integrações obrigatórias para o MVP: gateway de pagamento (Stripe, PagSeguro, Asaas), serviço de e-mail transacional (SendGrid, SES, Resend), armazenamento de arquivos (S3, Cloudinary), SSO corporativo (LDAP, SAML, OIDC), ERPs (SAP, TOTVS, via API ou arquivo), e APIs de parceiros. Cada integração deve ser avaliada: existe SDK ou client library na linguagem escolhida? A documentação é boa? Há sandbox/ambiente de teste? Qual é o SLA do provedor? Integrações com sistemas legados que só oferecem SOAP ou FTP são sinais de esforço adicional significativo.

- **Requisitos de notificações**: Mapear todos os eventos que disparam notificações e os canais desejados — e-mail transacional (confirmação de cadastro, reset de senha, alertas), push notification (web e mobile, se aplicável), SMS (verificação de telefone, alertas urgentes), notificações in-app (badge, toast, centro de notificações). Definir se o envio é síncrono (durante o request do usuário) ou assíncrono (via job queue). Notificações síncronas bloqueiam o request e afetam latência — para monolitos, um job queue (Sidekiq, Celery, BullMQ) é o padrão para envio assíncrono sem adicionar complexidade de microserviço.

### Perguntas

1. Todas as funcionalidades foram levantadas e classificadas em MVP, next e backlog com critério de negócio? [fonte: Produto, Diretoria] [impacto: PM, Dev]
2. As personas foram definidas com perfis, necessidades e comportamentos distintos para cada tipo de usuário? [fonte: Produto, UX, Operações] [impacto: UX, Dev]
3. As jornadas críticas de cada persona foram mapeadas com telas e ações por passo? [fonte: Produto, UX] [impacto: UX, Dev, QA]
4. O modelo de autenticação foi definido (e-mail/senha, social, SSO, MFA) com requisitos concretos? [fonte: TI, Produto, Security] [impacto: Dev, Arquiteto]
5. O modelo de autorização foi definido com granularidade real (roles, permissões por módulo, customização por tenant)? [fonte: Produto, TI] [impacto: Dev, Arquiteto]
6. Os requisitos de relatórios e dashboards foram levantados com KPIs, formato e frequência de atualização? [fonte: Diretoria, Operações, Produto] [impacto: Dev, Arquiteto]
7. Todas as integrações externas obrigatórias no MVP foram mapeadas com SDK, sandbox e SLA verificados? [fonte: TI, Produto, Comercial] [impacto: Dev, Arquiteto]
8. Os canais de notificação e eventos que os disparam foram documentados (e-mail, push, SMS, in-app)? [fonte: Produto, UX] [impacto: Dev]
9. O volume de dados esperado no primeiro ano foi estimado (registros, storage, crescimento mensal)? [fonte: Produto, TI] [impacto: Arquiteto, DevOps]
10. Há requisitos de internacionalização (múltiplos idiomas, moedas, formatos de data/número)? [fonte: Comercial, Produto] [impacto: Dev, Arquiteto]
11. Há requisitos de acessibilidade (WCAG 2.1 AA, legislação como LBI)? [fonte: Jurídico, Compliance, Produto] [impacto: Dev, UX]
12. O sistema precisa funcionar offline ou com conectividade intermitente (PWA com sync)? [fonte: Produto, Operações] [impacto: Arquiteto, Dev]
13. Há requisitos de upload e gerenciamento de arquivos (documentos, imagens, vídeos) — volume e tamanho máximo? [fonte: Produto, Operações] [impacto: Dev, DevOps]
14. Existem processos com workflow de aprovação (solicitação → revisão → aprovação → execução)? [fonte: Operações, Produto] [impacto: Dev]
15. O sistema precisa suportar operações em tempo real (chat, notificações live, dashboards com refresh automático)? [fonte: Produto, Operações] [impacto: Arquiteto, Dev]

---

## Etapa 03 — Alignment

- **Escolha do framework e linguagem**: Alinhar a decisão de stack com todos os stakeholders. A escolha deve considerar: experiência do time (produtividade imediata vs. curva de aprendizado), ecossistema de bibliotecas para as integrações necessárias, facilidade de contratação futura (relevante se o cliente vai internalizar a manutenção), e adequação ao tipo de problema. Django e Rails são excelentes para CRUD-heavy com admin panel robusto. NestJS é ideal para APIs com TypeScript e integração com frontend React/Next.js. Laravel é forte em ecossistema e comunidade. Spring Boot é o padrão enterprise Java com máxima robustez. A escolha de framework é uma das decisões mais difíceis de reverter — trocar depois custa uma reescrita.

- **Frontend acoplado ou desacoplado**: Decidir se o frontend será server-side rendered (templates do framework — Django Templates, Blade, ERB) ou um SPA separado (React, Vue, Angular consumindo API). Server-side rendering é mais rápido de implementar para aplicações CRUD, mais simples de debugar, e tem SEO nativo — mas a experiência do usuário é menos fluida. SPA separado oferece UX moderna (navegação sem reload, estado client-side), mas adiciona complexidade (CORS, autenticação com token, dois deploys, dois pipelines de CI/CD). A decisão deve considerar o perfil do usuário e o tipo de interação predominante.

- **Definição do modelo de dados conceitual**: Alinhar as entidades principais do domínio (Usuário, Tenant, Pedido, Produto, etc.), seus relacionamentos e as regras de negócio mais importantes. O modelo de dados conceitual é a base para o schema de banco de dados e para a estrutura de módulos da aplicação. Em monolitos, o banco é compartilhado — o que significa que relações entre entidades são foreign keys reais, joins são possíveis, e transações ACID cobrem todas as entidades. Esse é um dos benefícios fundamentais do monolito que não existe em microserviços.

- **Estratégia de deploy e ambientes**: Alinhar onde e como a aplicação será hospedada. Opções: PaaS gerenciado (Railway, Render, Heroku — zero DevOps, custo moderado), container em cloud (ECS/Fargate, Cloud Run — mais controle, custo variável), VPS (DigitalOcean, Hetzner — máximo controle, requer conhecimento de sysadmin), ou on-premise (servidor do cliente — requisitos de compliance ou política da empresa). Definir ao menos dois ambientes: staging (para validação antes do deploy) e production. Preview deployments por PR são recomendados se o PaaS suportar.

- **SLA e modelo de suporte pós-lançamento**: Definir formalmente o que acontece após o go-live. Quem corrige bugs? Qual o tempo de resposta? Existe contrato de suporte com SLA? Se o sistema é crítico para operação (sistema de vendas, gestão de pedidos), downtime de 24h pode significar perda de receita. O modelo de suporte deve estar formalizado antes do go-live — não como negociação apressada quando o primeiro bug crítico aparece.

### Perguntas

1. A decisão de framework e linguagem foi tomada considerando experiência do time, ecossistema e contratação futura? [fonte: CTO, Tech Lead, Diretoria] [impacto: Dev, Arquiteto]
2. A decisão entre frontend acoplado (server-side) e desacoplado (SPA) foi tomada com justificativa documentada? [fonte: Tech Lead, UX] [impacto: Dev]
3. O modelo de dados conceitual com entidades principais, relacionamentos e regras de negócio foi alinhado com stakeholders? [fonte: Produto, Analista de negócio] [impacto: Dev, Arquiteto]
4. A estratégia de deploy e hospedagem foi definida (PaaS, container, VPS, on-premise) com custo projetado? [fonte: TI, Financeiro, CTO] [impacto: DevOps, Dev]
5. Os ambientes (staging e production no mínimo) foram definidos e a paridade entre eles foi acordada? [fonte: DevOps, Tech Lead] [impacto: DevOps, Dev]
6. O modelo de suporte e manutenção pós-lançamento foi formalizado com SLA de resposta a bugs? [fonte: Diretoria, PM] [impacto: PM, Dev]
7. O processo de aprovação de entregas parciais foi definido (quem revisa, quem aprova, prazo máximo de feedback)? [fonte: Diretoria, Produto] [impacto: PM, Dev]
8. A estratégia de multi-tenancy (se aplicável) foi decidida — shared database com tenant_id, schema-per-tenant ou instância separada? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps]
9. O fluxo de deploy foi alinhado — push para main = deploy automático, ou deploy manual com aprovação? [fonte: CTO, DevOps] [impacto: Dev, DevOps]
10. O modelo de branching foi definido (trunk-based, GitFlow, feature branches com PR obrigatório)? [fonte: Tech Lead] [impacto: Dev]
11. As dependências externas críticas (APIs, SaaS, serviços de infraestrutura) foram mapeadas com fallback definido? [fonte: TI, Arquiteto] [impacto: Dev, DevOps]
12. O design será entregue em formato utilizável (Figma com componentes) ou o time de dev terá liberdade para UI? [fonte: UX, Diretoria] [impacto: Dev, UX]
13. O processo de comunicação entre time de desenvolvimento e stakeholders foi definido (canal, frequência, formato)? [fonte: PM, Diretoria] [impacto: PM]
14. O escopo do MVP foi congelado e todos os stakeholders concordam que não haverá adições sem renegociação de prazo? [fonte: Diretoria, Produto] [impacto: PM, Dev]
15. O time de desenvolvimento tem acesso a todas as ferramentas necessárias (repositório, cloud, serviços SaaS, ambientes de sandbox)? [fonte: TI, DevOps] [impacto: Dev, DevOps]

---

## Etapa 04 — Definition

- **Modelagem de banco de dados**: Produzir o ERD (Entity-Relationship Diagram) completo com todas as tabelas, colunas (nome, tipo, constraints), índices, e foreign keys. Em monolitos, o banco de dados é o coração da aplicação — um modelo de dados mal desenhado gera queries lentas, lógica de negócio distribuída em workarounds, e migrações arriscadas após o go-live. Atenção especial a: normalização adequada (evitar redundância que gera inconsistência), índices para as queries mais frequentes (identificar antes de ter dados reais, não depois de o sistema ficar lento), e campos de auditoria em tabelas sensíveis (created_at, updated_at, created_by, updated_by).

- **Wireframes e protótipos de telas**: Produzir wireframes para cada tela do MVP — não apenas as telas principais, mas também: estados de erro, estados de vazio (listagem sem dados), modals de confirmação, fluxos de onboarding, e telas de configuração. Wireframes aprovados são o contrato entre UX, desenvolvimento e stakeholders — mudanças após aprovação do wireframe são change requests com impacto em prazo. Para MVPs, wireframes de média fidelidade (Figma com componentes de UI library) são preferíveis a wireframes de baixa fidelidade que deixam margem para interpretação.

- **Especificação de APIs (se frontend desacoplado)**: Para variante V5 (API + SPA), documentar todos os endpoints da API com OpenAPI 3.0: path, método, parâmetros, request body, response body (sucesso e cada tipo de erro), autenticação necessária, e exemplos de uso. A spec deve ser escrita antes do build para permitir desenvolvimento paralelo — frontend implementa contra a spec (usando mock server como Prism), backend implementa a spec. Endpoints sem especificação resultam em contratos implícitos que divergem entre frontend e backend.

- **Mapa de permissões por role**: Produzir uma matriz de permissões: roles (admin, gerente, operador, viewer) nas linhas, funcionalidades/módulos nas colunas, e ações permitidas nas células (create, read, update, delete, approve). A matriz de permissões é o insumo para implementar o middleware de autorização e para os testes de QA. Em sistemas multi-tenant, a matriz deve incluir a dimensão tenant — admin global vs. admin do tenant vs. operador do tenant têm permissões diferentes.

- **Especificação de workflows e regras de negócio**: Para cada processo de negócio com mais de 2 passos (ex.: pedido → aprovação → execução → conclusão), documentar: estados possíveis (draft, pending_approval, approved, rejected, in_progress, completed, cancelled), transições permitidas (quem pode mover de qual estado para qual), ações automáticas em cada transição (enviar e-mail, atualizar estoque, gerar cobrança), e tratamento de exceções (o que acontece se o aprovador rejeitar? se o prazo expirar?). Workflows não documentados resultam em edge cases descobertos em produção.

- **Critérios de aceite por funcionalidade**: Para cada funcionalidade do MVP, documentar critérios de aceite específicos e testáveis. Formato recomendado: "Dado [contexto], quando [ação], então [resultado esperado]" (Gherkin). Critérios vagos como "o sistema deve ser rápido" ou "a tela deve ser bonita" não são testáveis. Critérios específicos como "a listagem de pedidos com filtro por data deve retornar em menos de 2 segundos para até 10.000 registros" permitem que o QA valide objetivamente.

### Perguntas

1. O ERD completo foi produzido com tabelas, colunas, tipos, constraints, índices e foreign keys? [fonte: Arquiteto, Dev] [impacto: Dev]
2. Os wireframes cobrem todas as telas do MVP incluindo estados de erro, vazio e modals de confirmação? [fonte: UX, Produto] [impacto: Dev, UX]
3. A especificação de API (se frontend desacoplado) foi documentada em OpenAPI com todos os endpoints e schemas? [fonte: Tech Lead, Dev] [impacto: Dev]
4. A matriz de permissões por role foi produzida para todas as funcionalidades com granularidade de ação (CRUD + approve)? [fonte: Produto, Security] [impacto: Dev, QA]
5. Os workflows com múltiplos estados foram documentados com transições, ações automáticas e tratamento de exceções? [fonte: Produto, Analista de negócio] [impacto: Dev]
6. Os critérios de aceite foram escritos para cada funcionalidade do MVP em formato testável? [fonte: Produto, QA] [impacto: QA, Dev]
7. A estrutura de módulos da aplicação foi definida com separação clara de responsabilidades? [fonte: Arquiteto, Tech Lead] [impacto: Dev]
8. As validações de input (formato, tamanho, obrigatoriedade) foram especificadas para cada campo de cada formulário? [fonte: Produto, UX] [impacto: Dev, QA]
9. O modelo de notificações foi especificado (qual evento dispara qual notificação para qual canal)? [fonte: Produto, UX] [impacto: Dev]
10. O esquema de URLs e rotas foi definido de forma consistente e intuitiva? [fonte: Tech Lead, UX] [impacto: Dev]
11. As queries de relatório mais pesadas foram identificadas e a estratégia de performance definida (índices, read replica, cache)? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
12. O plano de migração de dados do sistema legado (se aplicável) foi especificado com mapeamento campo a campo? [fonte: TI, Analista de negócio] [impacto: Dev, PM]
13. Os campos de auditoria (created_at, updated_at, created_by) foram previstos nas tabelas que exigem rastreabilidade? [fonte: Compliance, Produto] [impacto: Dev]
14. Os limites e constraints do sistema foram definidos (máximo de registros por listagem, tamanho de upload, timeout de operação)? [fonte: Arquiteto, Produto] [impacto: Dev, QA]
15. A documentação de Definition foi revisada e aprovada por todos os stakeholders antes de iniciar o Setup? [fonte: Diretoria, Produto, Tech Lead] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Estrutura modular do monolito**: Organizar o código em módulos coesos com fronteiras claras — cada módulo encapsula um domínio de negócio (users, orders, billing, notifications) com seus próprios models, services, controllers e testes. Módulos se comunicam via interfaces públicas (service layer), nunca acessando diretamente o model ou o banco de outro módulo. Essa disciplina é o que diferencia um monolito bem estruturado de um big ball of mud — e é o que permite extrair módulos para microserviços no futuro, se necessário, sem reescrever do zero.

- **Estratégia de autenticação**: Para aplicações com frontend acoplado (server-side rendering), sessões no servidor (cookie-based) são o padrão mais simples e seguro — o framework gerencia automaticamente. Para aplicações com SPA desacoplado, JWT (access token de curta duração + refresh token em httpOnly cookie) é o padrão recomendado. Para aplicações que precisarão de mobile no futuro, JWT facilita a reutilização da API. Serviços gerenciados de auth (Auth0, Clerk, Supabase Auth) eliminam a necessidade de implementar login, registro, reset de senha e MFA — mas adicionam dependência externa e custo.

- **Job queue e processamento assíncrono**: Monolitos precisam de job queue para operações que não devem bloquear o request do usuário: envio de e-mails, geração de relatórios PDF, processamento de uploads pesados, sincronização com sistemas externos, e limpeza periódica de dados. Sidekiq (Ruby), Celery (Python), BullMQ (Node.js) e Laravel Queues são as opções mais maduras por ecossistema. O job queue roda no mesmo processo ou em worker separado (mesmo código, modo de execução diferente) — é o primeiro passo natural de "separação" em monolitos sem chegar em microserviços.

- **Estratégia de cache**: Definir onde e como usar cache para melhorar performance sem adicionar complexidade excessiva. Níveis de cache: HTTP cache headers (para assets e páginas públicas), application cache (Redis ou in-memory para dados frequentemente acessados e raramente modificados — configurações, permissões, lookups), e query cache (para relatórios pesados recalculados periodicamente). Em monolitos, cache invalidation é mais simples que em microserviços porque o código que escreve e o que lê estão no mesmo processo — invalidar cache no momento do write é trivial.

- **Pipeline de CI/CD**: Configurar pipeline automatizado: push para branch → lint + type-check → testes unitários → testes de integração → build → deploy para staging (a cada merge na main) → deploy para produção (manual trigger ou automático com gate de aprovação). GitHub Actions é a opção mais popular e gratuita para repositórios no GitHub. O pipeline deve incluir: migration check (verificar que as migrations rodam sem erro em banco limpo e em banco com dados), dependency audit (verificar vulnerabilidades em pacotes), e test coverage report.

- **Estratégia de file storage**: Definir onde arquivos uploaded por usuários serão armazenados. Filesystem local (simples mas não escala horizontalmente e perde dados se o servidor falhar), object storage (S3, GCS, Cloudflare R2 — escalável, durável, barato), ou serviço de mídia (Cloudinary, imgix — com transformação de imagem on-the-fly). Para aplicações com upload de documentos, S3 é o padrão. Para aplicações com imagens que precisam de thumbnails e resize, Cloudinary ou S3 + processamento no upload são as opções. Nunca armazenar arquivos no banco de dados (blob) — performance e custo são muito piores que object storage.

### Perguntas

1. A aplicação foi estruturada em módulos coesos com fronteiras claras e comunicação via service layer? [fonte: Arquiteto, Tech Lead] [impacto: Dev]
2. A estratégia de autenticação foi definida (session-based, JWT, serviço gerenciado) considerando o modelo de frontend? [fonte: Arquiteto, Security] [impacto: Dev]
3. O job queue foi escolhido e os tipos de operação assíncrona foram listados (e-mail, relatórios, sync, cleanup)? [fonte: Arquiteto, Dev] [impacto: Dev]
4. A estratégia de cache foi definida por nível (HTTP, application, query) com TTL e invalidação documentados? [fonte: Arquiteto, Dev] [impacto: Dev]
5. O pipeline de CI/CD foi desenhado com lint, testes, migration check e deploy automatizado? [fonte: DevOps, Tech Lead] [impacto: Dev, DevOps]
6. A estratégia de file storage foi definida (S3, Cloudinary, filesystem) com limite de tamanho e tipos aceitos? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps]
7. O banco de dados de produção será gerenciado (RDS, Cloud SQL) ou auto-hospedado com backup manual? [fonte: DevOps, CTO] [impacto: DevOps]
8. A estratégia de logging foi definida (formato, nível, destino, retenção)? [fonte: DevOps, Arquiteto] [impacto: Dev, DevOps]
9. O modelo de error handling e error reporting (Sentry, Bugsnag) foi escolhido? [fonte: Dev, DevOps] [impacto: Dev]
10. A estratégia de rate limiting foi definida para APIs públicas (se aplicável) com thresholds por endpoint? [fonte: Arquiteto, Security] [impacto: Dev]
11. Os custos mensais de infraestrutura foram calculados em cenário normal e cenário de pico? [fonte: Financeiro, DevOps] [impacto: PM, DevOps]
12. A estratégia de backup de banco de dados foi definida (frequência, retenção, teste de restore)? [fonte: DevOps, Arquiteto] [impacto: DevOps]
13. A estratégia de migrations de banco foi definida (ferramenta, processo de rollback, tratamento de dados existentes)? [fonte: Tech Lead, Dev] [impacto: Dev]
14. Se multi-tenant, a estratégia de isolamento foi detalhada tecnicamente (queries com tenant_id, middleware, testes)? [fonte: Arquiteto, Dev] [impacto: Dev]
15. A arquitetura foi documentada e aprovada por tech lead e stakeholders técnicos? [fonte: CTO, Tech Lead, Arquiteto] [impacto: Dev, Arquiteto]

---

## Etapa 06 — Setup

- **Scaffolding do projeto**: Criar o projeto com a estrutura de pastas definitiva, configurações de linter (ESLint, Rubocop, Flake8, PHPStan), formatador (Prettier, Black), e editor config (.editorconfig). Configurar o ORM com conexão ao banco de dados, rodar a primeira migration (geralmente criação de tabela de usuários e sessões), e verificar que o servidor roda localmente sem erros. O README do repositório deve incluir instruções de setup local que permitam a qualquer dev do time rodar o projeto com um único comando (ou o mais próximo disso).

- **Autenticação e autorização como primeira feature**: Implementar login, registro, reset de senha e middleware de autorização como primeira funcionalidade — antes de qualquer lógica de negócio. Toda feature subsequente depende de saber quem é o usuário e o que ele pode fazer. Se for usar serviço gerenciado (Auth0, Clerk), integrar e validar o fluxo completo nesta fase. Se for implementar do zero, usar a solução nativa do framework (Django Auth, Devise, Passport, Laravel Auth) e não reinventar — autenticação custom é fonte de vulnerabilidades.

- **Pipeline de CI/CD configurado**: Configurar o pipeline antes de escrever código de negócio. O primeiro PR deve já passar por lint, testes (mesmo que sejam apenas smoke tests iniciais) e deploy automático para staging. Configurar deploy previews por PR se a plataforma suportar (Vercel, Railway, Render). O pipeline deve incluir: verificação de migrations (rodar em banco limpo para garantir que todas as migrations são reproduzíveis), verificação de dependências (npm audit, bundle-audit, safety), e code coverage mínimo (começar com 60%, aumentar progressivamente).

- **Seed de dados para desenvolvimento**: Criar scripts de seed que populam o banco com dados realistas para desenvolvimento e testes. O seed deve criar: usuários com diferentes roles (admin, operador, viewer), dados de negócio em volume suficiente para testar listagens com paginação e filtros (pelo menos 100 registros nas entidades principais), e cenários de edge case (registro com campos opcionais vazios, registro com dados no limite máximo). Seeds bem feitos aceleram o desenvolvimento e tornam o onboarding de novos devs imediato.

- **Configuração de variáveis de ambiente**: Todas as configurações externas (database URL, secret keys, API keys de integrações, configurações de e-mail) devem ser variáveis de ambiente — nunca hardcoded. Criar .env.example com todas as variáveis documentadas (nome, descrição, exemplo de valor), .env.local para desenvolvimento (no .gitignore), e configurar as variáveis nos ambientes de staging e produção via painel da plataforma de hospedagem ou secrets manager.

- **Configuração de domínio e SSL**: Registrar ou configurar o domínio de produção e staging (staging.exemplo.com). Configurar SSL/TLS (Let's Encrypt automático na maioria dos PaaS). Se a aplicação será acessada via domínio customizado do cliente (white-label), a arquitetura de DNS e SSL deve suportar isso desde o início — adicionar suporte a domínios customizados depois de deployed é significativamente mais complexo.

### Perguntas

1. O projeto foi criado com estrutura de pastas definitiva, linter, formatador e editor config configurados? [fonte: Tech Lead, Dev] [impacto: Dev]
2. O README inclui instruções de setup local que permitem rodar o projeto em menos de 5 minutos? [fonte: Dev] [impacto: Dev]
3. A autenticação e autorização estão implementadas e funcionando como primeira feature antes da lógica de negócio? [fonte: Dev, Security] [impacto: Dev]
4. O pipeline de CI/CD está configurado e o primeiro PR passou por lint, testes e deploy em staging? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
5. Os deploy previews por PR estão funcionando (se a plataforma suportar)? [fonte: Dev, DevOps] [impacto: Dev, PM]
6. Os scripts de seed criam dados realistas suficientes para testar listagens, filtros e paginação? [fonte: Dev] [impacto: Dev, QA]
7. Todas as variáveis de ambiente estão documentadas em .env.example e configuradas nos ambientes corretos? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
8. O .gitignore está configurado para excluir .env, secrets, arquivos de build e dependências? [fonte: Dev] [impacto: Dev]
9. O banco de dados de staging está criado, as migrations rodaram com sucesso e o seed foi executado? [fonte: Dev, DevOps] [impacto: Dev]
10. O domínio e SSL estão configurados para staging e produção (mesmo que produção ainda não esteja no ar)? [fonte: DevOps, TI] [impacto: DevOps]
11. O error reporting (Sentry ou similar) está configurado e capturou pelo menos um erro de teste? [fonte: Dev] [impacto: Dev]
12. O serviço de e-mail transacional está configurado em staging e um e-mail de teste foi enviado com sucesso? [fonte: Dev, DevOps] [impacto: Dev]
13. O file storage (S3 ou similar) está configurado com buckets separados por ambiente? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
14. O job queue está configurado e um job de teste foi executado com sucesso (envio de e-mail assíncrono)? [fonte: Dev] [impacto: Dev]
15. O ambiente de staging está completamente funcional com autenticação, seed de dados e deploy automático? [fonte: DevOps, Dev] [impacto: Dev, DevOps, QA]

---

## Etapa 07 — Build

- **Implementação módulo por módulo**: Implementar cada módulo de negócio como unidade completa (model + service + controller + testes + validações + permissões) antes de avançar para o próximo. A ordem de implementação deve seguir as dependências do domínio — módulos independentes (cadastro de usuários, configurações) primeiro, módulos dependentes (pedidos que referenciam usuários e produtos) depois. Cada módulo concluído deve ser deployável em staging para feedback antecipado dos stakeholders.

- **CRUD com validação e tratamento de erros**: Para cada entidade, implementar o CRUD completo: listagem com paginação, ordenação e filtros (pelo menos os filtros que os wireframes mostram), criação com validação server-side (nunca confiar apenas em validação client-side), edição com concurrency handling (optimistic locking via updated_at ou versioning), exclusão (soft delete com deleted_at para dados que precisam de auditoria, hard delete para dados efêmeros), e detalhamento. Cada operação deve ter tratamento de erros claro — mensagem de erro legível para o usuário, log de erro com contexto para o dev.

- **Implementação de workflows e máquina de estados**: Para processos com múltiplos estados (pedido, aprovação, ticket), implementar uma state machine formal — não apenas um campo status com IF/ELSE espalhado pelo código. Bibliotecas como AASM (Ruby), django-fsm (Python), xstate (JS) ou laravel-model-states (PHP) garantem que transições inválidas são bloqueadas, ações automáticas são executadas em cada transição, e o histórico de transições é registrável. State machines formais tornam os workflows testáveis e debugáveis — "como o pedido chegou nesse estado?" é respondível pelo histórico de transições.

- **Integrações com serviços externos**: Implementar cada integração com isolamento — encapsular em um service/adapter que pode ser substituído por mock em testes e por implementação alternativa no futuro. Para gateways de pagamento, implementar com webhook handling (pagamento confirmado, estornado, disputado) e testar com sandbox do provedor. Para APIs de terceiros, implementar circuit breaker e retry — se a API do parceiro ficar fora por 10 minutos, o sistema deve degradar graciosamente, não retornar 500 para o usuário.

- **Frontend e UX**: Se frontend acoplado, implementar as telas seguindo os wireframes aprovados com atenção a: formulários com validação inline e mensagens de erro claras, listagens com paginação funcional e estados de vazio, loading states (skeleton, spinner) para operações que levam >1s, e responsividade em mobile (mesmo para aplicações internas, usuários acessam do celular). Se SPA desacoplado, o frontend consome a API documentada na OpenAPI — garantir que a spec está atualizada e que o mock server está disponível para desenvolvimento paralelo.

- **Testes automatizados**: Implementar testes ao longo do build, não como fase final. Testes unitários para lógica de negócio (service layer — cálculos, validações, regras de estado). Testes de integração para endpoints (request → response com banco real via testcontainers ou banco de teste). Testes de permissão (cada endpoint acessado por cada role — admin pode, operador não pode, etc.). Coverage mínima recomendada: 80% no service layer, 60% nos controllers. Testes que quebram no CI devem ser corrigidos imediatamente — não marcados como skip.

### Perguntas

1. Os módulos estão sendo implementados como unidades completas (model + service + controller + testes) com deploy em staging? [fonte: Tech Lead] [impacto: Dev, PM]
2. Cada CRUD tem validação server-side, tratamento de erros com mensagem clara, e paginação/filtros funcionais? [fonte: Dev, QA] [impacto: Dev]
3. Os workflows com múltiplos estados estão implementados com state machine formal (não IF/ELSE espalhado)? [fonte: Tech Lead, Dev] [impacto: Dev]
4. As integrações externas estão encapsuladas em services/adapters testáveis com circuit breaker e retry? [fonte: Dev, Arquiteto] [impacto: Dev]
5. Os webhooks de integrações (pagamento, notificações) estão implementados e testados com sandbox do provedor? [fonte: Dev] [impacto: Dev, QA]
6. O frontend está seguindo os wireframes aprovados com validação inline, loading states e responsividade? [fonte: UX, Dev] [impacto: Dev, UX]
7. Os testes unitários cobrem a lógica de negócio do service layer com coverage ≥80%? [fonte: Tech Lead, QA] [impacto: Dev, QA]
8. Os testes de integração cobrem os endpoints principais com banco real e validação de response? [fonte: Dev, QA] [impacto: Dev]
9. Os testes de permissão validam que cada role acessa apenas o que deve — admin pode, operador não pode? [fonte: Security, QA] [impacto: Dev, QA]
10. A migração de dados do sistema legado (se aplicável) está em andamento com validação de integridade? [fonte: Dev, PM] [impacto: Dev, PM]
11. As notificações (e-mail, in-app) estão implementadas e testadas com dados reais em staging? [fonte: Dev, QA] [impacto: Dev]
12. O job queue está processando operações assíncronas (e-mail, relatórios) sem erros e com retry configurado? [fonte: Dev] [impacto: Dev, DevOps]
13. Os relatórios e dashboards estão implementados com performance aceitável para o volume de dados esperado? [fonte: Dev, Produto] [impacto: Dev]
14. O conteúdo real (textos, labels, mensagens de erro) está no sistema — não lorem ipsum ou placeholders? [fonte: Produto, UX] [impacto: Dev, QA]
15. O progresso do build está visível para stakeholders com demos regulares em staging? [fonte: PM, Produto] [impacto: PM]

---

## Etapa 08 — QA

- **Testes de aceitação por funcionalidade**: Executar cada critério de aceite definido na Etapa 04 — um por um, marcando como passed ou failed. Os testes devem ser executados por alguém que não desenvolveu a funcionalidade (QA dedicado ou outro dev). Para funcionalidades com múltiplas personas, testar com cada role — o mesmo fluxo pode funcionar para admin e falhar para operador por falta de permissão ou por tela não adaptada ao role. Manter log de todos os bugs encontrados com severidade (critical, high, medium, low) e critério de bloqueio (quais severidades devem ser corrigidas antes do go-live).

- **Testes de segurança**: Validar OWASP Top 10 para a aplicação: SQL injection (tentar em campos de busca e filtros), XSS (tentar em campos de texto livre que são renderizados em outras telas), CSRF (verificar que tokens CSRF estão presentes em todos os formulários), broken authentication (tentar acessar URLs de admin como usuário não-autenticado e como usuário sem permissão), insecure direct object references (tentar acessar recurso de outro tenant alterando ID na URL), e security misconfiguration (headers de segurança configurados: X-Frame-Options, CSP, HSTS). Para sistemas com dados sensíveis, considerar pentest externo.

- **Testes de performance**: Medir tempo de resposta das operações mais frequentes e das mais pesadas: listagem com filtro (target: <500ms para até 10.000 registros), criação de registro (target: <1s), geração de relatório (target: <5s para relatórios comuns, <30s para relatórios analíticos pesados), login (target: <2s). Identificar e corrigir N+1 queries (problema endêmico em ORMs), queries sem índice, e endpoints que fazem chamadas síncronas a APIs externas lentas. Testes de carga com k6 ou Artillery simulando o padrão de uso esperado ajudam a identificar gargalos antes do go-live.

- **Testes de migração de dados**: Se há dados migrados do sistema legado, validar integridade: contagem de registros (total no legado vs. total no novo), validação de campos críticos (comparar amostra aleatória de 5-10% dos registros campo a campo), verificação de relacionamentos (foreign keys válidas, sem registros órfãos), e validação de encoding (caracteres especiais, acentos, emojis que podem corromper durante migração). Executar os relatórios principais com dados migrados e comparar resultados com os do sistema legado — divergências indicam problemas de mapeamento.

- **Teste end-to-end dos fluxos críticos**: Para cada jornada de usuário crítica definida na Discovery, executar o fluxo completo em staging: desde o login até a conclusão da ação principal, incluindo notificações, e-mails enviados, e estado final do dado no banco. Testar com dados realistas, não com "teste teste teste". Incluir cenários negativos: o que acontece quando o usuário tenta uma ação sem permissão, quando o campo obrigatório está vazio, quando a sessão expira no meio de um formulário, quando o browser faz back durante um fluxo multi-step.

- **Revisão de UX e acessibilidade**: Validar a experiência do usuário com as personas definidas na Discovery. Pedir para um representante do usuário real (não o dev) executar as jornadas principais sem assistência — observar onde hesita, onde erra, onde precisa de ajuda. Verificar acessibilidade com axe-core ou Lighthouse Accessibility: contraste de cores, labels em todos os inputs, navegação por teclado funcional, textos alternativos em imagens, e landmarks HTML para screen readers.

### Perguntas

1. Todos os critérios de aceite da Etapa 04 foram executados e marcados como passed/failed? [fonte: QA, Produto] [impacto: QA, Dev]
2. Os testes foram executados por alguém que não desenvolveu a funcionalidade? [fonte: QA, PM] [impacto: QA]
3. Os testes de segurança OWASP Top 10 foram executados e vulnerabilidades críticas/altas foram corrigidas? [fonte: Security, QA] [impacto: Dev, Security]
4. Os testes de IDOR verificaram que um tenant/usuário não acessa dados de outro alterando IDs na URL? [fonte: Security, QA] [impacto: Dev, Security]
5. Os tempos de resposta das operações mais frequentes estão dentro dos targets definidos? [fonte: Dev, QA] [impacto: Dev]
6. Os N+1 queries foram identificados e corrigidos nos endpoints de listagem? [fonte: Dev] [impacto: Dev]
7. A migração de dados (se aplicável) foi validada com contagem, amostragem e comparação de relatórios? [fonte: QA, Dev] [impacto: Dev, PM]
8. Os fluxos end-to-end das jornadas críticas foram testados com dados realistas em staging? [fonte: QA, Produto] [impacto: QA, Dev]
9. Os cenários negativos foram testados (sem permissão, campo vazio, sessão expirada, browser back)? [fonte: QA] [impacto: Dev, QA]
10. Um representante do usuário real executou as jornadas principais sem assistência e o feedback foi documentado? [fonte: Produto, UX] [impacto: UX, Dev]
11. A acessibilidade foi verificada com axe-core/Lighthouse nos fluxos principais (contraste, labels, teclado)? [fonte: QA, UX] [impacto: Dev, UX]
12. Os e-mails transacionais foram verificados quanto a conteúdo, formatação, links e entregabilidade (não cai em spam)? [fonte: QA, Marketing] [impacto: Dev]
13. O job queue foi testado sob carga (muitos jobs enfileirados simultaneamente) sem perda de mensagem? [fonte: Dev, QA] [impacto: Dev, DevOps]
14. Os relatórios foram validados com volume de dados realista e os resultados conferem com cálculos manuais? [fonte: QA, Produto] [impacto: Dev]
15. Todos os bugs de severidade critical e high foram corrigidos e retestados antes de avançar? [fonte: QA, Tech Lead] [impacto: Dev, QA, PM]

---

## Etapa 09 — Launch Prep

- **Checklist de configuração de produção**: Verificar e corrigir todas as configurações específicas de produção: DEBUG=false (erro clássico que expõe stack trace e dados sensíveis), secret keys únicas e fortes (não reutilizar de staging), CORS configurado apenas para domínios permitidos, HTTPS forçado (redirect automático de HTTP para HTTPS), headers de segurança (HSTS, X-Content-Type-Options, X-Frame-Options, CSP), e rate limiting ativo em endpoints públicos (login, registro, reset de senha). Cada item deve ser verificado manualmente — configurações que funcionam em staging podem estar incorretas em produção.

- **Plano de migração de dados final**: Se há dados a migrar do sistema legado, planejar a migração final: janela de migração (período em que o sistema legado é congelado para escrita e os dados são migrados para o novo), validação pós-migração (checklist de integridade executado imediatamente após a migração), e plano de contingência (se a migração falhar, como reverter). A janela de migração deve ser comunicada a todos os usuários com antecedência. Se o volume de dados é grande, considerar migração incremental (bulk dos dados migrado com antecedência, apenas delta migrado na janela final).

- **Backup e disaster recovery testados**: Verificar que o backup automatizado do banco de produção está configurado (frequência mínima: diário, retenção mínima: 30 dias), e que o restore funciona — testar restaurando o backup mais recente em um ambiente temporário e verificando que a aplicação roda normalmente com os dados restaurados. Documentar o procedimento de restore passo a passo — no momento de um desastre real, o engenheiro precisa seguir instruções, não improvisar.

- **Treinamento de usuários**: Realizar sessão de treinamento com os usuários finais (não apenas com o patrocinador). Cobrir: login e recuperação de senha, fluxos principais por role (admin faz X, operador faz Y), tratamento de erros mais comuns ("o que fazer quando aparece mensagem X"), e canal de suporte (para quem ligar/escrever quando algo não funciona). Entregar documentação simples com capturas de tela — não manual de 50 páginas que ninguém vai ler, mas guia rápido de 5-10 páginas com os fluxos mais frequentes.

- **Monitoramento e alertas configurados**: Configurar antes do go-live: error reporting (Sentry ou similar) capturando exceções não tratadas com notificação instantânea, monitoramento de disponibilidade (UptimeRobot, Better Uptime) com alertas por e-mail/SMS/Slack, e métricas de aplicação (tempo de resposta, taxa de erro, uso de recursos). Definir quem recebe alertas e o modelo de resposta — alerta sem responsável designado é ruído que será ignorado.

- **Plano de rollback**: Documentar o procedimento de rollback: reverter para a versão anterior do código (via CI/CD ou deploy manual da imagem anterior), verificar compatibilidade do banco (se houve migration, o rollback exige atenção especial — migrations que removem colunas ou alteram tipos não são trivialmente reversíveis). Se a migration não é backwards compatible, o plano de rollback deve incluir restore de backup de banco — e o tempo necessário para esse restore deve ser estimado e comunicado.

### Perguntas

1. O checklist de configuração de produção foi verificado item por item (DEBUG, secrets, CORS, HTTPS, headers de segurança)? [fonte: DevOps, Security] [impacto: DevOps, Dev]
2. O rate limiting está configurado em endpoints públicos (login, registro, reset de senha) com thresholds definidos? [fonte: Dev, Security] [impacto: Dev]
3. O plano de migração de dados final foi documentado com janela, validação e contingência? [fonte: Dev, PM] [impacto: Dev, PM]
4. O backup automatizado do banco de produção está configurado e o restore foi testado com sucesso? [fonte: DevOps] [impacto: DevOps]
5. O treinamento de usuários foi realizado com os perfis que vão operar o sistema diariamente? [fonte: PM, Produto] [impacto: PM]
6. A documentação de uso (guia rápido) foi entregue com capturas de tela dos fluxos mais frequentes? [fonte: PM, UX] [impacto: PM]
7. O error reporting (Sentry) está configurado em produção e capturou pelo menos um erro de teste? [fonte: Dev] [impacto: Dev]
8. O monitoramento de disponibilidade está ativo e testado (alerta chegou quando o serviço foi pausado)? [fonte: DevOps] [impacto: DevOps]
9. O plano de rollback foi documentado com procedimento de reverter código e banco? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
10. Todos os stakeholders foram notificados sobre data, horário e impactos do go-live? [fonte: PM, Diretoria] [impacto: PM]
11. Os acessos de produção (cloud, banco, CI/CD, monitoramento) estão configurados apenas para pessoas autorizadas? [fonte: DevOps, Security] [impacto: DevOps]
12. Os secrets de produção (API keys de pagamento, SMTP, integrações) foram configurados e testados? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
13. A janela de go-live foi escolhida estrategicamente (dia útil, baixo tráfego, time disponível o dia todo)? [fonte: PM, Diretoria] [impacto: PM]
14. O modelo de suporte pós-go-live está ativado com canal de comunicação e SLA de resposta definidos? [fonte: PM, Diretoria] [impacto: PM, Dev]
15. Os dados de seed de demonstração em staging foram removidos e o ambiente de produção tem apenas dados reais/migrados? [fonte: Dev, DevOps] [impacto: Dev]

---

## Etapa 10 — Go-Live

- **Deploy para produção e smoke tests**: Executar o deploy para produção via pipeline de CI/CD (não manual). Após o deploy, executar smoke tests: acessar a home (verifica que a aplicação respondeu), fazer login com usuário real (verifica autenticação e banco), executar a ação principal do sistema (verifica lógica de negócio e integrações), e verificar que o e-mail transacional chegou (verifica integração com serviço de e-mail). Se qualquer smoke test falhar, avaliar rollback imediato — um sistema que não permite login ou que não processa a ação principal não está pronto para go-live.

- **Migração de dados final (se aplicável)**: Executar a migração de dados do sistema legado na janela planejada. Congelar o sistema legado para escrita, executar a migração, rodar o checklist de validação de integridade (contagem, amostragem, relatórios), e confirmar go/no-go. Se a validação falhar, executar o plano de contingência (reverter para sistema legado). A comunicação com usuários durante a janela de migração é crucial — informar que o sistema estará indisponível, por quanto tempo, e quando retorna.

- **Cutover de DNS e SSL**: Se o sistema usa domínio customizado, executar a troca de DNS (reduzir TTL com antecedência). Verificar que o SSL foi provisionado corretamente (sem mixed content warnings). Se o sistema substitui um sistema legado no mesmo domínio, o cutover de DNS é simultâneo com a migração — planejar a sequência exata e testar com DNS local (hosts file) antes de executar o cutover real.

- **Monitoramento intensivo das primeiras 48h**: Nas primeiras 48 horas, monitorar ativamente: taxa de erro no Sentry (cada exceção é investigada — em produção recém-lançado, cada erro pode ser sintoma de problema estrutural), tempo de resposta (comparar com baseline de staging — degradação pode indicar queries sem índice com volume de dados real), jobs na fila (verificar que não há acúmulo — jobs falhados indicam problema de integração ou timeout), e feedback dos usuários (o primeiro contato com usuários reais revela problemas de UX que testes não pegaram).

- **Estabilização e correções hot-fix**: Os primeiros dias em produção inevitavelmente revelam bugs e ajustes necessários. Ter processo de hot-fix ágil: branch de fix a partir de main, correção, testes, deploy rápido (pipeline deve permitir deploy de hot-fix em menos de 15 minutos). Priorizar bugs que impedem uso (bloqueadores) sobre bugs cosméticos. Manter comunicação frequente com usuários — informar que o problema foi identificado e está sendo corrigido reduz frustração.

- **Entrega formal e encerramento**: Entregar ao cliente: acessos a todos os sistemas (repositório, cloud, CI/CD, monitoramento, domínio DNS), documentação técnica (arquitetura, modelo de dados, configurações, runbooks), documentação de usuário (guia rápido com capturas de tela), e relatório de entrega (funcionalidades implementadas, bugs conhecidos pendentes, recomendações de evolução). Obter aceite formal (e-mail ou documento assinado). Ativar contrato de suporte se aplicável.

### Perguntas

1. O deploy para produção foi executado via CI/CD (não manual) e os smoke tests passaram (login, ação principal, e-mail)? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
2. A migração de dados final (se aplicável) foi executada com validação de integridade aprovada? [fonte: Dev, QA] [impacto: Dev, PM]
3. O DNS foi configurado corretamente e o SSL está ativo sem mixed content warnings? [fonte: DevOps] [impacto: DevOps]
4. O Sentry está capturando exceções de produção e cada erro nas primeiras horas foi investigado? [fonte: Dev] [impacto: Dev]
5. O tempo de resposta em produção está compatível com o baseline de staging (sem degradação significativa)? [fonte: Dev, DevOps] [impacto: Dev]
6. Os jobs na fila estão sendo processados sem acúmulo e sem falhas sistemáticas? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
7. O processo de hot-fix está funcionando — correção urgente pode ser deployada em menos de 15 minutos? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
8. Os usuários reais conseguiram acessar o sistema, fazer login e executar as ações principais sem bloqueio? [fonte: Produto, PM] [impacto: PM, Dev]
9. O monitoramento de disponibilidade está ativo e confirmou uptime desde o go-live? [fonte: DevOps] [impacto: DevOps]
10. O sistema legado (se aplicável) está mantido como fallback pelo período de contingência acordado? [fonte: TI, DevOps] [impacto: DevOps, PM]
11. Os backups automatizados de produção estão funcionando e o primeiro backup foi verificado? [fonte: DevOps] [impacto: DevOps]
12. O feedback dos primeiros usuários foi coletado e os bugs críticos foram priorizados para hot-fix? [fonte: Produto, PM] [impacto: Dev, PM]
13. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou acesso? [fonte: DevOps, PM] [impacto: PM]
14. O aceite formal de entrega foi obtido (e-mail, assinatura, ou confirmação documentada)? [fonte: Diretoria, PM] [impacto: PM]
15. O contrato de suporte pós-lançamento foi ativado com SLA e canal de comunicação definidos? [fonte: Diretoria, PM] [impacto: PM, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Cada módulo vai ser um microserviço"** — Over-engineering para a fase atual. Se o time tem 3-5 devs e o domínio cabe em um banco de dados, microserviços adicionam complexidade sem benefício. Monolito modular entrega o mesmo valor organizacional com fração do custo operacional. Se escala individual for necessária no futuro, módulos bem isolados podem ser extraídos.
- **"O sistema precisa fazer tudo que o Excel faz"** — Escopo infinito disfarçado de requisito. O Excel é uma ferramenta genérica — o sistema deve resolver problemas específicos melhor que o Excel, não replicar toda sua funcionalidade. Priorizar os fluxos que mais geram dor no processo atual.
- **"O orçamento de infra é zero, hospedamos no servidor da empresa"** — Hosting on-premise para aplicações web modernas requer conhecimento de sysadmin, SSL, backup, segurança e disponibilidade. Se não há equipe para isso, o custo oculto de manter servidor próprio supera o custo de um PaaS gerenciado. $20-50/mês em Railway/Render resolve para a maioria dos MVPs.

### Etapa 02 — Discovery

- **"Todas as funcionalidades são MVP"** — Ausência de priorização. Se tudo é prioridade, nada é prioridade. O resultado é um "MVP" de 12 meses que não é mais M (mínimo) nem V (viável no prazo). Forçar a classificação: quais 3 funcionalidades geram receita ou evitam perda no dia 1?
- **"A autorização é simples — admin e usuário"** — No dia da entrega, se torna "admin global, admin do cliente, gerente com aprovação, operador com restrição por setor, e viewer que vê relatórios mas não edita". Definir granularidade real de permissões desde o início evita refatoração de middleware e banco.
- **"Não temos relatórios definidos, mas precisa ter dashboard"** — Dashboard sem métricas definidas resulta em tela bonita com dados inúteis. Definir KPIs concretos antes de implementar gráficos — o que o usuário precisa saber olhando o dashboard para tomar uma decisão?

### Etapa 03 — Alignment

- **"O time do cliente escolhe a stack depois da entrega"** — Se a stack não for adequada ao time que vai manter, o sistema será abandonado ou reescrito. Alinhar stack com capacidade do time de operação é obrigatório na fase de Alignment.
- **"Não precisa de staging, testa em produção"** — Testar em produção com dados reais de clientes é irresponsável. Bugs descobertos em produção afetam usuários reais e geram perda de confiança. Staging é obrigatório — o custo é mínimo comparado ao custo de um bug em produção.
- **"O escopo está aberto para evoluir durante o build"** — Sem escopo congelado, o build nunca termina. Mudanças durante o build são inevitáveis, mas devem ser tratadas como change requests com impacto em prazo e custo. "Escopo aberto" é sinônimo de projeto sem prazo.

### Etapa 04 — Definition

- **ERD "na cabeça" do dev** — Modelo de dados sem documento formal resulta em tabelas criadas no improviso, nomes inconsistentes, falta de índices, e foreign keys ausentes. O ERD documentado é gate obrigatório antes do build.
- **"Os wireframes são só para ter uma ideia"** — Wireframes ambíguos geram decisões de UX tomadas pelo dev durante o build — que frequentemente divergem do que o stakeholder esperava. Wireframes devem ser específicos o suficiente para não deixar margem de interpretação em elementos críticos.
- **"Os critérios de aceite a gente define durante o teste"** — Sem critérios definidos antes, o QA não sabe o que testar e o dev não sabe o que implementar. Resultado: funcionalidade que "funciona" mas não atende a expectativa do cliente.

### Etapa 05 — Architecture

- **"Vamos usar o framework que o dev senior conhece"** — Decisão por conveniência, não por adequação. Se o dev senior conhece Phoenix (Elixir) mas o time do cliente só trabalha com PHP, a entrega vai ser inoperável. Considerar o ciclo de vida completo: build + operação + manutenção + evolução.
- **"Banco de dados em container no mesmo servidor da app"** — Risco de perda de dados se o container falhar sem volume persistente. Banco de produção deve ser gerenciado (RDS, Cloud SQL) com backup automático, ou em instância separada com backup verificado.
- **"Não precisamos de job queue, fazemos tudo síncrono"** — Enviar e-mail no request do usuário adiciona 2-5s de latência. Gerar relatório PDF no request bloqueia o processo por minutos. Job queue é necessidade básica de qualquer monolito que faz I/O externo.

### Etapa 06 — Setup

- **"O CI/CD a gente configura depois"** — Sem CI/CD desde o início, cada merge vira "build funciona na minha máquina". Quando configurar CI/CD depois de 3 meses de código sem lint e testes, dezenas de erros aparecem de uma vez. Pipeline desde o primeiro PR é obrigatório.
- **Autenticação implementada como última feature** — Todo o desenvolvimento feito sem considerar quem é o usuário e o que ele pode fazer. Resultado: lógica de permissão adicionada como "patch" em cima de código que não foi desenhado para isso — inseguro e frágil.
- **"Seed a gente faz quando precisar"** — Sem seed de dados, cada dev testa com dados diferentes (ou sem dados). Bugs de listagem vazia, paginação e filtros não são descobertos até o QA. Seed realista desde o setup acelera o desenvolvimento e melhora a qualidade.

### Etapa 07 — Build

- **IF/ELSE para workflows** — Status como string no banco, transições controladas por condicionais espalhados em 15 arquivos diferentes. Resultado: estados impossíveis aparecem em produção, e ninguém sabe como o registro chegou lá. State machine formal é obrigatória para qualquer workflow com mais de 3 estados.
- **"Testes a gente escreve depois do build"** — Depois do build, com prazo estourado, testes são cortados. Resultado: refatoração arriscada (sem testes, qualquer mudança pode quebrar algo) e bugs em produção que custam 10x mais para corrigir. Testes junto com o build, sempre.
- **Frontend testado apenas no Chrome desktop** — Funciona no Chrome 1920px, quebra no Safari mobile, está ilegível no tablet. Testar responsividade em múltiplos browsers e breakpoints durante o build, não apenas no QA.

### Etapa 08 — QA

- **QA pelo próprio dev** — O dev que implementou conhece os caminhos felizes e inconscientemente evita os cenários que não implementou. QA deve ser feito por alguém que não escreveu o código — pode ser outro dev, mas não o mesmo.
- **"Funciona com 10 registros"** — Listagem que retorna em 50ms com 10 registros pode levar 30 segundos com 100.000. Testar com volume de dados realista — seed que representa 6-12 meses de uso real.
- **Segurança testada apenas com "acesso negado"** — Verificar que endpoint retorna 403 não é suficiente. Testar IDOR (trocar ID na URL para acessar recurso de outro tenant/usuário), SQL injection (campos de busca com payloads maliciosos), e session fixation (reutilizar token de outro usuário).

### Etapa 09 — Launch Prep

- **DEBUG=true em produção** — Erro que expõe stack trace completo, variáveis de ambiente e queries de banco para qualquer visitante. Verificar explicitamente no checklist pré-go-live — é o erro de segurança mais básico e mais comum.
- **Sem teste de restore de backup** — "O backup está configurado" não significa que funciona. Testar o restore completo em ambiente temporário e verificar que a aplicação roda com os dados restaurados. Backup sem teste de restore é ilusão de segurança.
- **Treinamento para o gerente, não para o operador** — O gerente recebe o treinamento e diz "repasso para o time". O repasse nunca acontece ou acontece de forma incompleta. Treinar diretamente quem vai usar o sistema todos os dias.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde** — Se algo der errado, o time não está disponível no fim de semana. Problemas em produção na sexta se tornam crises na segunda. Go-live em dia útil, início da manhã, com dia inteiro de buffer.
- **Deploy manual "dessa vez"** — "O pipeline está com problema, vou subir manualmente". Deploy manual é propenso a erro — arquivo esquecido, variável não configurada, migration não executada. Corrigir o pipeline e deployar via CI/CD, mesmo que demore mais.
- **"Está no ar, projeto encerrado"** — Sem monitoramento nas primeiras 48h, erros silenciosos se acumulam — jobs falhando, e-mails não enviados, performance degradando. A primeira semana em produção é parte do projeto, não pós-projeto.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é web app monolítica** e precisa ser reclassificado.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Cada módulo precisa escalar independentemente e ter deploy próprio" | Microserviços, não monolito | Reclassificar para web-app-microservices |
| "É só uma landing page com formulário de contato" | Site estático, não web app | Reclassificar para static-site |
| "Precisa de carrinho, checkout e gestão de estoque" | E-commerce, com requisitos específicos de catálogo e pagamento | Reclassificar para e-commerce |
| "São 5 aplicações diferentes que precisam conversar" | Múltiplos sistemas com integração, não um monolito | Avaliar microserviços ou integration platform |
| "O app mobile é a prioridade, web é secundário" | Mobile-first, não web app | Reclassificar para mobile-app com API backend |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O escopo ainda não está definido" | 01 | Projeto sem escopo é projeto sem prazo e sem orçamento | Definir MVP antes de avançar |
| "Não temos quem vai operar o sistema depois" | 01 | Sistema entregue sem dono operacional será abandonado | Definir equipe de operação antes de avançar |
| "O orçamento cobre só o desenvolvimento, hosting a gente vê depois" | 01 | Surpresa com custos recorrentes pós-launch | Apresentar TCO completo antes de continuar |
| "O sistema legado tem 10 anos de dados para migrar" | 02 | Migração de dados é projeto dentro do projeto | Estimar migração separadamente e incluir no escopo |
| "Não temos acesso ao servidor/cloud onde vai rodar" | 06 | Setup bloqueado por falta de acesso | Resolver acessos antes de iniciar Setup |
| "Os wireframes ainda não foram aprovados" | 04 | Build sem wireframe aprovado = retrabalho garantido | Travar início do build até wireframes aprovados |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O prazo é inegociável — 3 meses para tudo" | 01 | Prazo fixo com escopo flexível resulta em corte de qualidade | Documentar que qualidade não será sacrificada, escopo sim |
| "As aprovações passam por 4 pessoas" | 03 | Cadeia de aprovação lenta atrasa entregas e feedback | Documentar SLA de aprovação com prazo máximo por etapa |
| "O time do cliente nunca trabalhou com a stack escolhida" | 03 | Handoff de operação será problemático | Planejar treinamento técnico antes do go-live ou reconsiderar stack |
| "Não temos designer, o dev cuida do visual" | 03 | UX inconsistente, decisões visuais ad-hoc | Usar UI library pronta (Shadcn, Ant Design) para minimizar decisões visuais |
| "Performance não é importante, são poucos usuários" | 05 | Queries sem índice + volume de dados crescente = sistema lento em 6 meses | Documentar que otimização mínima é incluída independente do volume |
| "A gente define os fluxos de trabalho conforme surgem" | 04 | Workflows descobertos durante build = retrabalho e edge cases em produção | Mapear workflows formalmente antes do build |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Gatilho da demanda identificado (pergunta 1)
- Stakeholders e usuários reais mapeados (pergunta 2)
- Orçamento de desenvolvimento e operação aprovado (pergunta 4)
- Requisitos de compliance identificados (pergunta 6)
- Prazo de go-live com justificativa de negócio (pergunta 9)

### Etapa 02 → 03

- Funcionalidades classificadas em MVP, next e backlog (pergunta 1)
- Personas e jornadas críticas mapeadas (perguntas 2 e 3)
- Modelo de autenticação e autorização definido (perguntas 4 e 5)
- Integrações obrigatórias mapeadas com viabilidade verificada (pergunta 7)

### Etapa 03 → 04

- Framework e linguagem escolhidos com justificativa (pergunta 1)
- Frontend acoplado ou desacoplado decidido (pergunta 2)
- Modelo de dados conceitual alinhado (pergunta 3)
- Escopo do MVP congelado e aceito por todos (pergunta 14)

### Etapa 04 → 05

- ERD completo produzido e revisado (pergunta 1)
- Wireframes aprovados para todas as telas do MVP (pergunta 2)
- Matriz de permissões por role documentada (pergunta 4)
- Workflows documentados com estados, transições e exceções (pergunta 5)
- Critérios de aceite escritos para cada funcionalidade (pergunta 6)

### Etapa 05 → 06

- Estrutura modular definida com fronteiras entre módulos (pergunta 1)
- Estratégia de autenticação definida (pergunta 2)
- Pipeline de CI/CD desenhado (pergunta 5)
- Custos mensais calculados e aprovados (pergunta 11)
- Arquitetura documentada e aprovada (pergunta 15)

### Etapa 06 → 07

- Projeto criado com estrutura, linter e CI/CD funcionando (perguntas 1 e 4)
- Autenticação implementada e testada (pergunta 3)
- Seed de dados criado (pergunta 6)
- Ambiente de staging funcional (pergunta 15)

### Etapa 07 → 08

- Todos os módulos do MVP implementados com testes (pergunta 1)
- Workflows implementados com state machine (pergunta 3)
- Integrações testadas com sandbox (perguntas 4 e 5)
- Testes de permissão implementados (pergunta 9)

### Etapa 08 → 09

- Critérios de aceite executados com passed/failed documentados (pergunta 1)
- Testes de segurança OWASP executados (pergunta 3)
- Performance dentro dos targets (pergunta 5)
- Migração de dados validada (pergunta 7, se aplicável)
- Bugs critical e high corrigidos (pergunta 15)

### Etapa 09 → 10

- Checklist de produção verificado item por item (pergunta 1)
- Backup testado com restore bem-sucedido (pergunta 4)
- Treinamento de usuários realizado (pergunta 5)
- Monitoramento e alertas configurados (pergunta 8)
- Plano de rollback documentado (pergunta 9)

### Etapa 10 → Encerramento

- Deploy via CI/CD com smoke tests passed (pergunta 1)
- Migração de dados validada (pergunta 2, se aplicável)
- Monitoramento confirmou uptime (pergunta 9)
- Acessos entregues ao cliente (pergunta 13)
- Aceite formal obtido (pergunta 14)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de web app monolítica. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 SaaS B2B | V2 Back-office | V3 MVP/Startup | V4 Portal + Logado | V5 API + SPA |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 1 | 2 | 2 |
| 02 Discovery | 4 | 3 | 2 | 3 | 3 |
| 03 Alignment | 3 | 2 | 1 | 2 | 3 |
| 04 Definition | 4 | 4 | 2 | 3 | 4 |
| 05 Architecture | 3 | 2 | 2 | 3 | 3 |
| 06 Setup | 2 | 2 | 1 | 2 | 3 |
| 07 Build | 5 | 4 | 3 | 4 | 5 |
| 08 QA | 4 | 3 | 2 | 3 | 4 |
| 09 Launch Prep | 3 | 2 | 1 | 2 | 2 |
| 10 Go-Live | 2 | 2 | 1 | 2 | 2 |
| **Total relativo** | **32** | **26** | **16** | **26** | **31** |

**Observações por variante:**

- **V1 SaaS B2B**: Build é o mais pesado — painel admin, multi-tenancy, billing, permissões por role e por tenant. Discovery é pesado por causa da complexidade do modelo de autorização e dos fluxos multi-tenant.
- **V2 Back-office**: Definition é relativamente pesada por causa dos workflows de aprovação e relatórios complexos. Build é moderado porque o padrão é CRUD repetitivo com variações de workflow.
- **V3 MVP/Startup**: O mais leve de todas as variantes — o objetivo é velocidade de entrega. Cada etapa é reduzida ao mínimo necessário. O risco é cortar demais e acumular dívida técnica que bloqueia iterações futuras.
- **V4 Portal + Logado**: Esforço dividido entre a camada pública (SEO, performance, conteúdo) e a área logada (funcionalidades, permissões). Architecture é mais pesada por causa da dualidade SSR público + CSR logado.
- **V5 API + SPA**: Build é o mais pesado junto com V1 — dois deploys (backend API + frontend SPA), contratos de API como fonte de verdade, CORS, autenticação com token. Setup é mais pesado por causa da configuração de dois projetos e dois pipelines.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Frontend acoplado — server-side rendering (Etapa 03, pergunta 2) | Etapa 04: pergunta 3 (spec de API OpenAPI). Etapa 05: pergunta 10 (rate limiting de API pública). Etapa 06: CORS e deploy separado de frontend. |
| Sistema novo, sem legado (Etapa 01, pergunta 5) | Etapa 04: pergunta 12 (plano de migração de dados). Etapa 08: pergunta 7 (validação de migração). Etapa 09: pergunta 3 (migração final). Etapa 10: perguntas 2 e 10 (migração e sistema legado como fallback). |
| Single-tenant (Etapa 03, pergunta 8) | Etapa 04: pergunta 4 (permissões por tenant). Etapa 05: pergunta 14 (isolamento multi-tenant). Etapa 08: pergunta 4 (teste IDOR entre tenants). |
| Sem necessidade de app mobile futuro (Etapa 01, pergunta 11) | Decisão de JWT vs. session pode ser simplificada. Spec OpenAPI é menos prioritária (se frontend acoplado). |
| 100% área logada, sem conteúdo público (Etapa 01, pergunta 12) | SEO é irrelevante. SSR público não é necessário. Performance de renderização inicial é menos crítica. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Sistema substitui legado (Etapa 01, pergunta 5) | Etapa 02: volume de dados e mapeamento de entidades. Etapa 04: pergunta 12 (plano de migração) se torna gate. Etapa 08: pergunta 7 (validação de migração) se torna obrigatória. Etapa 09: pergunta 3 (migração final com janela e contingência). Etapa 10: pergunta 10 (legado como fallback). |
| Multi-tenancy confirmada (Etapa 03, pergunta 8) | Etapa 04: pergunta 4 (permissões por tenant) se torna gate. Etapa 05: pergunta 14 (isolamento técnico documentado). Etapa 07: testes de isolamento por tenant. Etapa 08: pergunta 4 (IDOR entre tenants) se torna obrigatória. |
| Frontend desacoplado — SPA (Etapa 03, pergunta 2) | Etapa 04: pergunta 3 (OpenAPI spec) se torna gate. Etapa 05: pergunta 10 (rate limiting) se torna obrigatória. Etapa 06: configuração de CORS, dois pipelines de CI/CD, dois deploys. |
| Requisitos de compliance (LGPD, PCI-DSS, SOC2) (Etapa 01, pergunta 6) | Etapa 04: pergunta 13 (campos de auditoria) se torna obrigatória. Etapa 05: criptografia at-rest no banco, logging de auditoria. Etapa 08: perguntas 3 e 4 (security testing e IDOR) se tornam gates. Etapa 09: pergunta 1 (checklist de segurança de produção). |
| App mobile futuro (Etapa 01, pergunta 11) | Etapa 03: pergunta 2 — frontend desacoplado se torna recomendação forte. Etapa 04: pergunta 3 (API spec) se torna obrigatória. Etapa 05: JWT como estratégia de autenticação (session-based não funciona para mobile). |
| Workflows complexos (Etapa 02, pergunta 14) | Etapa 04: pergunta 5 (documentação de workflows com estados e transições) se torna gate. Etapa 07: pergunta 3 (state machine formal) se torna obrigatória. Etapa 08: testar cada transição de estado incluindo cenários de rejeição e expiração. |
| Volume de dados >100.000 registros no primeiro ano (Etapa 02, pergunta 9) | Etapa 04: pergunta 11 (queries de relatório com estratégia de performance). Etapa 05: pergunta 4 (cache) se torna obrigatória. Etapa 08: perguntas 5 e 6 (performance e N+1 queries) se tornam gates. |
