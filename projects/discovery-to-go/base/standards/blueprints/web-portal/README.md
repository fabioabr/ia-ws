---
title: "Portal Web Autenticado — Blueprint"
description: "Aplicação web com autenticação, perfil de usuário e conteúdo personalizado. Backend simples (monolítico ou BFF leve). Sem complexidade de microserviços."
category: project-blueprint
type: web-portal
status: rascunho
created: 2026-04-13
---

# Portal Web Autenticado

## Descrição

Aplicação web com autenticação, perfil de usuário e conteúdo personalizado. Backend simples (monolítico ou BFF leve). Sem complexidade de microserviços. Inclui fluxos de login, cadastro, recuperação de senha, gerenciamento de perfil e áreas restritas com controle de acesso baseado em roles. Diferencia-se de um SaaS por não ter billing, multi-tenancy complexa ou marketplace — é um portal com conteúdo e funcionalidades acessíveis a usuários autenticados.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo portal web é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Portal de Conteúdo Restrito

Portal com autenticação cujo propósito principal é controlar o acesso a conteúdo que não é público — artigos, vídeos, documentos, cursos ou materiais exclusivos para membros. O backend é leve (autenticação + controle de acesso + servir conteúdo protegido). Não há lógica de negócio complexa — o valor está no conteúdo, não na funcionalidade. Exemplos: área de membros de associação profissional, portal de treinamento corporativo, biblioteca digital com acesso restrito, portal de comunicação interna.

### V2 — Portal de Autoatendimento

Portal onde o usuário autenticado realiza operações sobre seus próprios dados — consultar histórico, atualizar cadastro, abrir chamados, agendar serviços, gerar boletos ou segundas vias. O backend tem lógica de negócio moderada e frequentemente integra com sistemas legados (ERP, CRM, billing) via API. O foco é reduzir atendimento humano oferecendo self-service digital. Exemplos: portal do cliente de telecom, portal do aluno de universidade, portal do paciente de clínica, portal do associado de cooperativa.

### V3 — Portal Colaborativo / Comunidade

Portal onde múltiplos usuários autenticados interagem entre si — fóruns, comentários, mensagens, compartilhamento de conteúdo, votação ou avaliação. O backend precisa lidar com conteúdo gerado pelo usuário (UGC), moderação, notificações e busca. A complexidade não está na autenticação, mas na dinâmica social e nos fluxos de moderação. Exemplos: comunidade de produto, fórum técnico, portal de voluntários, rede interna de colaboradores.

### V4 — Portal Administrativo / Backoffice

Portal interno para funcionários ou parceiros com dashboards, relatórios, gestão de entidades (CRUD de clientes, pedidos, produtos, tickets) e controle de acesso granular por role (admin, gerente, operador, auditor). O backend tem lógica de negócio relevante e frequentemente é o sistema central de operação do negócio. O foco é produtividade operacional — UX precisa ser funcional, não necessariamente bonita. Exemplos: painel administrativo de e-commerce, backoffice de operações logísticas, portal de gestão de parceiros, sistema de atendimento ao cliente.

### V5 — Portal Multi-perfil com Onboarding

Portal que atende diferentes perfis de usuário (ex.: aluno e professor, comprador e vendedor, paciente e médico), cada um com fluxo de onboarding, dashboard e funcionalidades distintas. O backend precisa de modelo de permissões sofisticado (RBAC ou ABAC) e fluxos condicionais. A complexidade está na multiplicidade de jornadas e na necessidade de manter coerência de experiência entre perfis. Exemplos: portal escolar (aluno + professor + responsável + coordenador), marketplace de serviços (prestador + contratante), plataforma de saúde (paciente + médico + laboratório).

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend | Auth | Banco de Dados | Observações |
|---|---|---|---|---|---|
| V1 — Conteúdo Restrito | Next.js ou Astro | BFF leve (Next.js API Routes) ou serverless | Auth.js (NextAuth) ou Clerk | PostgreSQL ou CMS headless | Auth simples com JWT/session. CMS headless pode servir conteúdo protegido via API com token. |
| V2 — Autoatendimento | Next.js ou React + Vite | Node.js (Express/Fastify) ou .NET | Keycloak ou Auth0 | PostgreSQL + cache Redis | Integração com legado via API gateway. Auth robusto com MFA. Redis para sessões e cache de dados frequentes. |
| V3 — Colaborativo | Next.js ou React + Vite | Node.js (Express/Fastify) | Auth.js ou Supabase Auth | PostgreSQL + Supabase ou Firebase | Real-time para notificações (WebSocket ou SSE). Busca full-text com PostgreSQL ou Meilisearch. |
| V4 — Backoffice | React + Vite ou Refine/AdminJS | Node.js (Express/Fastify) ou .NET | Keycloak ou OIDC corporativo | PostgreSQL | RBAC granular. Frameworks admin (Refine, AdminJS, react-admin) aceleram CRUD. Dashboards com Recharts ou Tremor. |
| V5 — Multi-perfil | Next.js | Node.js (Express/Fastify) ou NestJS | Keycloak ou Auth0 | PostgreSQL | RBAC/ABAC obrigatório. Onboarding condicional por perfil. Modelo de dados com polimorfismo de usuário. |

---

## Etapa 01 — Inception

- **Origem da demanda e problema de negócio**: A necessidade de um portal autenticado costuma surgir de dores operacionais concretas — atendimento sobrecarregado que poderia ser autoatendimento, conteúdo sensível distribuído por e-mail ou WhatsApp sem controle de acesso, operações internas feitas em planilhas ou sistemas legados com UX precária, ou necessidade de digitalizar um processo que hoje é presencial ou telefônico. Entender o problema real é crítico porque define o critério de sucesso: se o problema é reduzir chamados de suporte, a métrica é volume de tickets; se é controlar acesso a conteúdo, a métrica é compliance de acesso.

- **Stakeholders e usuários finais**: Em portais autenticados, há sempre ao menos dois grupos distintos: os stakeholders que patrocinam o projeto (diretoria, gerência de TI) e os usuários finais que vão usar o portal diariamente (clientes, alunos, funcionários, parceiros). Frequentemente existe um terceiro grupo — os operadores internos que administram o portal (suporte, moderação, gestão de conteúdo). Esses três grupos têm expectativas diferentes e todas precisam ser mapeadas na Inception. O patrocinador quer ROI e redução de custo, o usuário final quer facilidade e rapidez, o operador quer ferramentas de gestão eficientes.

- **Base de usuários existente e migração de contas**: Se o portal substitui um sistema existente (mesmo que rudimentar — planilha de senhas, sistema legado, área restrita em WordPress), é provável que exista uma base de usuários com credenciais. A migração dessas contas precisa ser planejada desde a Inception: formato atual dos dados (hash das senhas, campos do perfil), estratégia de migração (import em massa com reset de senha obrigatório, ou migração transparente com rehash no primeiro login), e comunicação aos usuários sobre a transição. Subestimar este trabalho é um dos maiores riscos de portais que substituem sistemas legados.

- **Modelo de autenticação e identidade**: Definir cedo se o portal terá autenticação própria (e-mail + senha gerenciados pelo sistema), login social (Google, Facebook, Apple), login corporativo (SSO via SAML ou OIDC com IdP da empresa como Azure AD ou Okta), ou combinação desses. A escolha impacta a arquitetura desde o início — SSO corporativo exige integração com o IdP do cliente, que pode ter seu próprio time, processos de aprovação e SLA de integração. Se a resposta for "os funcionários já usam Azure AD para tudo", a integração com o IdP corporativo é pré-requisito, não feature futura.

- **Expectativa de escala e performance**: Portais autenticados têm padrões de uso previsíveis que definem a arquitetura. Um portal corporativo interno com 500 usuários tem requisitos radicalmente diferentes de um portal de autoatendimento com 500.000 clientes. Picos de acesso concentrado (ex.: portal de universidade no dia da matrícula, portal de associação no dia de votação) exigem planejamento de capacidade que não pode ser feito depois. Perguntar sobre volume esperado, picos sazonais e requisitos de disponibilidade (99.9% vs. 99.99%) é obrigatório nesta fase.

- **Conformidade regulatória e dados sensíveis**: Portais autenticados por definição lidam com dados pessoais (e-mail, nome, senha, perfil). Dependendo do domínio, podem lidar com dados sensíveis (saúde, financeiro, educacional). LGPD e GDPR exigem consentimento informado, direito de exclusão, portabilidade de dados e notificação de vazamento. Se o portal trata dados de saúde, há regulamentações adicionais (HIPAA nos EUA, resoluções CFM no Brasil). Identificar o nível de conformidade exigido na Inception é obrigatório — retrofitar compliance em um portal já construído é ordens de magnitude mais caro do que projetar compliance desde o início.

### Perguntas

1. Qual problema de negócio específico o portal resolve — redução de atendimento humano, controle de acesso a conteúdo, digitalização de processo ou outro? [fonte: Diretoria, Gerência de Operações] [impacto: PM, Dev, Arquiteto]
2. Quem são os usuários finais do portal (clientes, funcionários, parceiros, alunos) e qual o volume estimado de usuários ativos? [fonte: Operações, Comercial, RH] [impacto: Arquiteto, Dev, DevOps]
3. O portal substitui algum sistema existente e há base de usuários com credenciais a migrar? [fonte: TI, Operações] [impacto: Dev, Arquiteto, PM]
4. Qual modelo de autenticação é esperado — e-mail/senha próprio, login social, SSO corporativo (Azure AD, Okta) ou combinação? [fonte: TI, Segurança da Informação] [impacto: Arquiteto, Dev]
5. Existem picos de acesso previsíveis (sazonais, eventos, campanhas) e qual é o requisito de disponibilidade? [fonte: Operações, Marketing, TI] [impacto: Arquiteto, DevOps]
6. Quais dados pessoais ou sensíveis o portal vai armazenar e quais regulamentações se aplicam (LGPD, GDPR, regulação setorial)? [fonte: Jurídico, DPO, Compliance] [impacto: Arquiteto, Dev, Segurança]
7. Quem é o patrocinador do projeto e quem são os operadores internos que vão administrar o portal no dia a dia? [fonte: Diretoria, RH, Operações] [impacto: PM, Dev]
8. Qual é o orçamento total disponível, separando desenvolvimento, infraestrutura e operação mensal recorrente? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
9. Qual é o prazo esperado para o go-live e existe data de negócio que o justifica (lançamento, migração obrigatória, fim de contrato de sistema legado)? [fonte: Diretoria, TI] [impacto: PM, Dev]
10. O portal precisa integrar com sistemas internos existentes (ERP, CRM, billing, Active Directory)? Quais e com qual nível de documentação? [fonte: TI, Fornecedores de sistemas] [impacto: Arquiteto, Dev]
11. Existem requisitos de acessibilidade (WCAG 2.1 AA) ou internacionalização (múltiplos idiomas)? [fonte: Jurídico, Compliance, Comercial] [impacto: Dev, Designer]
12. Quantos perfis de usuário distintos o portal terá e quais permissões diferenciadas cada perfil precisa? [fonte: Operações, Diretoria] [impacto: Arquiteto, Dev]
13. Há expectativa de aplicativo mobile nativo no futuro ou o portal web responsivo é suficiente? [fonte: Diretoria, Marketing] [impacto: Arquiteto, Dev]
14. Quem controla a infraestrutura de hospedagem — o cliente exige cloud específica (AWS, Azure, GCP) ou on-premise? [fonte: TI, Segurança da Informação] [impacto: Arquiteto, DevOps]
15. O cliente tem time técnico interno que vai operar o portal pós-lançamento ou dependerá de suporte externo contínuo? [fonte: Diretoria, TI, RH] [impacto: PM, DevOps]

---

## Etapa 02 — Discovery

- **Mapeamento de jornadas de usuário**: Levantar todas as jornadas distintas que o portal precisa suportar — desde o primeiro acesso (cadastro ou convite), passando pelo onboarding (primeiro login, preenchimento de perfil), até as ações recorrentes do dia a dia (consultas, operações, interações). Cada perfil de usuário pode ter jornadas diferentes (ex.: aluno consulta notas, professor lança notas, coordenador gera relatórios). Jornadas não mapeadas viram features esquecidas que aparecem durante o build ou, pior, após o lançamento quando o usuário real não consegue completar uma tarefa que deveria ser básica.

- **Requisitos de autenticação e segurança**: Detalhar os requisitos além do login básico — MFA (autenticação multifator) obrigatória ou opcional, política de senha (comprimento mínimo, complexidade, expiração), sessão com timeout configurável, bloqueio após tentativas falhas, fluxo de recuperação de senha (link por e-mail com expiração, código por SMS), e fluxo de convite (admin convida usuário que recebe link para definir senha). Cada um desses requisitos tem impacto direto no esforço de desenvolvimento e na escolha da solução de autenticação — soluções como Clerk ou Auth0 resolvem a maioria nativamente, enquanto autenticação custom exige implementação manual de cada um.

- **Integrações com sistemas existentes**: Mapear todas as integrações previstas com detalhamento técnico: quais sistemas (ERP, CRM, billing, Active Directory, sistema legado), protocolo de comunicação (REST API, SOAP, gRPC, file-based), formato de dados (JSON, XML, CSV), frequência de sincronização (tempo real via webhook, polling periódico, batch diário), e disponibilidade de documentação de API. Integrações com sistemas legados sem API são o maior risco técnico de portais de autoatendimento — frequentemente exigem desenvolvimento de adaptadores, web scraping de interfaces legadas ou acesso direto ao banco de dados do sistema antigo, cada uma com seus próprios riscos.

- **Modelo de permissões e controle de acesso**: Definir o modelo de autorização com precisão — quais ações cada perfil pode executar (criar, ler, atualizar, deletar) sobre quais recursos (próprios, do grupo, de todos). RBAC (Role-Based Access Control) é suficiente para a maioria dos portais (admin vê tudo, gerente vê sua equipe, usuário vê só o próprio). ABAC (Attribute-Based Access Control) é necessário quando as permissões dependem de atributos dinâmicos (ex.: "médico só pode ver prontuário de pacientes da sua clínica"). Definir o modelo errado resulta em ou permissões excessivas (risco de segurança) ou permissões insuficientes (usuários bloqueados de ações legítimas, gerando tickets de suporte).

- **Requisitos de notificação**: Mapear todos os eventos que geram notificação ao usuário — boas-vindas no cadastro, confirmação de e-mail, reset de senha, ações pendentes, atualizações de status, lembretes de prazo. Definir os canais de notificação (e-mail, SMS, push notification, in-app notification) e se o usuário pode configurar suas preferências (opt-in/opt-out por canal e por tipo de notificação). A infraestrutura de e-mail transacional (SendGrid, Resend, AWS SES) precisa ser provisionada e configurada cedo — problemas de deliverability (e-mails caindo em spam) são frequentes e demoram para resolver quando o domínio é novo.

- **Fronteira do portal**: Verificar explicitamente se existe qualquer requisito que empurre o projeto para fora do escopo de portal autenticado simples: billing recorrente com gestão de assinaturas, marketplace com transações entre usuários, workflow engine com processos de aprovação multi-step complexos, BI e analytics avançados com data warehouse, ou integração com hardware IoT. Se qualquer um desses existir em nível significativo, o projeto pode precisar ser reclassificado para SaaS, marketplace ou plataforma — com impacto direto em arquitetura, custo e prazo.

### Perguntas

1. Quais são as jornadas distintas de cada perfil de usuário, do primeiro acesso até as ações recorrentes do dia a dia? [fonte: Operações, UX, Usuários finais] [impacto: Designer, Dev, PM]
2. Quais requisitos de segurança de autenticação são obrigatórios — MFA, política de senha, timeout de sessão, bloqueio por tentativas? [fonte: Segurança da Informação, Compliance] [impacto: Arquiteto, Dev]
3. O fluxo de cadastro é aberto (self-signup) ou fechado (apenas por convite de um administrador)? [fonte: Operações, Diretoria] [impacto: Dev, Arquiteto]
4. Quais sistemas internos precisam ser integrados e qual o nível de documentação de suas APIs? [fonte: TI, Fornecedores de sistemas] [impacto: Arquiteto, Dev]
5. O modelo de permissões é simples (RBAC com poucos perfis) ou exige controle granular por atributo (ABAC)? [fonte: Operações, Segurança da Informação] [impacto: Arquiteto, Dev]
6. Quais eventos geram notificação ao usuário e quais canais são esperados (e-mail, SMS, push, in-app)? [fonte: Operações, Marketing, UX] [impacto: Dev, DevOps]
7. O usuário pode configurar suas preferências de notificação (opt-in/opt-out por tipo e canal)? [fonte: UX, Operações] [impacto: Dev]
8. Qual volume de dados o portal precisa exibir e qual a expectativa de tempo de resposta para consultas (ex.: histórico de 2 anos)? [fonte: Operações, TI] [impacto: Arquiteto, Dev]
9. Existe requisito de funcionamento offline ou o portal é exclusivamente online? [fonte: Operações, Diretoria] [impacto: Arquiteto, Dev]
10. O portal precisa gerar documentos (PDF de relatórios, boletos, certificados, contratos)? [fonte: Operações, Financeiro] [impacto: Dev]
11. Há requisitos de auditoria — log de quem fez o quê e quando, com retenção obrigatória? [fonte: Compliance, Segurança da Informação, Jurídico] [impacto: Arquiteto, Dev]
12. O portal terá área pública (landing page, FAQ, status page) além da área autenticada? [fonte: Marketing, Diretoria] [impacto: Dev, Designer]
13. Existe requisito de LGPD além do básico — consentimento granular, portabilidade de dados, direito ao esquecimento com prazo? [fonte: Jurídico, DPO] [impacto: Arquiteto, Dev]
14. Os dados do sistema legado a integrar são confiáveis ou será necessário tratamento e normalização? [fonte: TI, Operações] [impacto: Dev, PM]
15. Existem requisitos de busca — busca simples por texto ou busca avançada com filtros, facetas e relevância? [fonte: Operações, UX] [impacto: Arquiteto, Dev]

---

## Etapa 03 — Alignment

- **Decisão de arquitetura de autenticação**: Alinhar formalmente a solução de autenticação — serviço gerenciado (Auth0, Clerk, Cognito, Firebase Auth) vs. self-hosted (Keycloak, Authentik) vs. autenticação custom (implementação manual com bcrypt + JWT/sessions). Serviços gerenciados eliminam 80% do esforço de autenticação, mas têm custo por MAU (Monthly Active User) que escala e dependência de vendor. Self-hosted (Keycloak) é gratuito em licença, robusto em features (SAML, OIDC, MFA, User Federation), mas exige infraestrutura e manutenção. Custom é a opção mais flexível e mais arriscada — implementar autenticação segura do zero exige expertise em segurança que a maioria dos times não tem, e qualquer falha é vulnerabilidade crítica.

- **Decisão de arquitetura backend**: Alinhar se o backend será monolítico (uma aplicação serve tudo — API, autenticação, lógica de negócio, admin), BFF (Backend for Frontend — backend leve que orquestra chamadas a serviços e APIs externas), ou serverless functions (handlers individuais por rota, escalando independentemente). Monolítico é o padrão correto para a maioria dos portais web — simples de deployar, debugar e operar. BFF faz sentido quando o portal é frontend de um ecossistema de APIs que já existem. Serverless faz sentido para portais com tráfego muito variável e poucas rotas de API pesadas. A decisão impacta diretamente custo de infraestrutura, complexidade de deploy e modelo de operação.

- **Formato e completude do design**: Alinhar o formato de entrega do design (Figma com componentes organizados, protótipo interativo, design system documentado) e o nível de completude esperado antes do build. Em portais autenticados, o design precisa cobrir significativamente mais estados que um site estático: tela de login, tela de cadastro, tela de recuperação de senha, tela de MFA, dashboard logado, estados de loading, estados de erro, estados vazios (empty states — "você ainda não tem nenhum pedido"), modais de confirmação, e toasts de feedback. Cada estado não desenhado é uma decisão que o dev vai tomar sozinho — e frequentemente tomar errado.

- **Estratégia de testes**: Alinhar o nível de cobertura de testes esperado — sem testes (aceitável apenas para MVPs descartáveis), testes E2E dos fluxos críticos (login, cadastro, operações principais), testes unitários de lógica de negócio, ou cobertura completa. Em portais autenticados, testes E2E dos fluxos de autenticação são investimento de alto retorno — um bug no fluxo de login bloqueia 100% dos usuários, enquanto um bug em uma página interna afeta apenas quem acessa aquela funcionalidade. A decisão impacta o setup (ferramentas de teste, CI pipeline) e o esforço do build.

- **SLA de operação pós-lançamento**: Definir o modelo de operação contínua — quem monitora, quem corrige bugs em produção, qual o tempo de resposta para incidentes críticos (portal fora do ar, vazamento de dados, funcionalidade quebrada). Portais autenticados têm expectativa de disponibilidade significativamente maior que sites estáticos — se o portal é a única forma do usuário acessar um serviço (consultar saldo, abrir chamado, acessar material), qualquer indisponibilidade gera impacto imediato em atendimento. SLA deve incluir: horário de cobertura, tempo de resposta por severidade, canal de acionamento e procedimento de escalação.

### Perguntas

1. A solução de autenticação foi escolhida (gerenciada, self-hosted ou custom) com justificativa técnica e financeira documentada? [fonte: TI, Segurança da Informação, Financeiro] [impacto: Arquiteto, Dev]
2. A arquitetura de backend foi decidida (monolítico, BFF ou serverless) considerando o perfil do time e a complexidade das integrações? [fonte: TI, Arquiteto] [impacto: Dev, DevOps]
3. O design cobre todos os estados de autenticação (login, cadastro, recuperação, MFA, erro, sucesso)? [fonte: Designer, UX] [impacto: Dev]
4. O design inclui empty states, estados de loading, estados de erro e toasts de feedback para todas as telas? [fonte: Designer, UX] [impacto: Dev]
5. A estratégia de testes foi definida — quais fluxos terão testes automatizados e qual ferramenta será usada? [fonte: QA, Dev] [impacto: Dev, QA]
6. O SLA de operação pós-lançamento foi definido (horário de cobertura, tempo de resposta, canal de acionamento)? [fonte: Diretoria, TI] [impacto: PM, DevOps, Dev]
7. As dependências externas críticas (IdP corporativo, APIs de sistemas legados, provedor de e-mail transacional) foram mapeadas com SLA e responsável? [fonte: TI, Fornecedores] [impacto: PM, Arquiteto]
8. O fluxo de aprovação de design e funcionalidades foi definido — quem aprova, em quanto tempo, e o que acontece se atrasar? [fonte: Diretoria, Marketing] [impacto: PM, Dev]
9. A abordagem mobile foi alinhada — o portal é mobile-first, responsivo partindo do desktop, ou tem app nativo planejado? [fonte: Diretoria, UX] [impacto: Dev, Designer, Arquiteto]
10. O modelo de versionamento e deploy foi alinhado — deploy contínuo, releases periódicas, ou janelas de manutenção? [fonte: TI, Operações] [impacto: Dev, DevOps]
11. A política de retenção de dados e backup foi definida (RPO e RTO)? [fonte: TI, Segurança da Informação, Jurídico] [impacto: DevOps, Arquiteto]
12. O time de desenvolvimento tem acesso a ambientes de sandbox das integrações externas (sandbox do ERP, ambiente de testes do IdP)? [fonte: TI, Fornecedores] [impacto: Dev]
13. Existe processo definido para gestão de mudanças de escopo — como novas features são priorizadas e quem autoriza alterações? [fonte: Diretoria, PM] [impacto: PM, Dev]
14. O cliente entende que portal autenticado exige monitoramento contínuo e não é "set and forget" como um site estático? [fonte: Diretoria, TI] [impacto: PM, DevOps]
15. As métricas de sucesso do portal foram definidas — qual KPI comprova que o portal está atingindo o objetivo de negócio? [fonte: Diretoria, Operações] [impacto: PM, Dev]

---

## Etapa 04 — Definition

- **Modelo de dados e entidades**: Definir o modelo de dados completo do portal — entidades (User, Profile, Role, Permission, Content, Notification, AuditLog), atributos de cada entidade (tipos, obrigatoriedades, tamanhos, constraints), e relacionamentos entre entidades (um User tem um Profile, um User tem muitas Roles, uma Role tem muitas Permissions). O modelo de dados é o artefato mais crítico desta fase porque toda a lógica de negócio do portal é construída sobre ele. Mudanças no modelo de dados após o início do build geram migrações de banco, refatoração de API e retrabalho de frontend — e o custo dessas mudanças cresce exponencialmente com o volume de dados em produção.

- **Especificação de APIs e contratos**: Definir os endpoints da API com contratos formais — método HTTP, path, parâmetros, corpo da requisição (schema JSON), resposta de sucesso (schema JSON com códigos HTTP), e respostas de erro (códigos HTTP, formato da mensagem de erro). Usar OpenAPI/Swagger como formato padrão permite geração automática de documentação, clients e validação. Em portais com integrações externas, definir também os contratos esperados das APIs de terceiros — incluindo comportamento em caso de indisponibilidade (retry, fallback, circuit breaker). APIs sem contrato formal resultam em frontend e backend trabalhando com expectativas diferentes, gerando bugs de integração durante o build.

- **Wireframes e protótipos de fluxos**: Produzir wireframes ou protótipos interativos (Figma prototype) para todos os fluxos críticos: cadastro completo (incluindo verificação de e-mail), login (incluindo MFA se aplicável), recuperação de senha, onboarding de primeiro acesso, dashboard principal, e as 3-5 operações mais frequentes do portal. Protótipos devem ser testados com usuários reais representativos antes de avançar para design de alta fidelidade. Validar protótipos cedo é significativamente mais barato do que refatorar funcionalidades prontas porque o fluxo não faz sentido para o usuário.

- **Mapa de telas e navegação**: Produzir o mapa completo de telas do portal com hierarquia de navegação — menu principal (itens por perfil), breadcrumbs, navegação contextual (links dentro de telas), e fluxos de saída (logout, voltar, cancelar). O mapa deve distinguir telas públicas (landing page, login, cadastro) de telas autenticadas (dashboard, perfil, funcionalidades), e telas restritas por perfil (admin vs. usuário comum). O mapa de telas é o equivalente do sitemap para portais — é a base para estimar esforço de build e planejar sprints.

- **Especificação de regras de negócio**: Documentar formalmente as regras de negócio que o portal implementa — validações de dados (CPF válido, e-mail único, idade mínima), regras de estado (pedido pode ser cancelado até 24h antes, senha expira em 90 dias), regras de acesso (gerente vê dados da sua unidade, auditor vê tudo mas não edita), e regras de cálculo (se aplicável). Regras de negócio não documentadas viram "conhecimento tribal" que vive na cabeça de uma pessoa — quando essa pessoa não está disponível durante o build, o dev assume ou inventa, e o resultado raramente é correto.

- **Plano de migração de dados**: Se o portal substitui um sistema existente, especificar o plano de migração com detalhamento: quais tabelas/entidades serão migradas, mapeamento campo a campo entre o schema antigo e o novo, regras de transformação (normalização de dados, deduplicação, validação), estratégia para dados inconsistentes (descartar, corrigir manualmente, importar com flag de revisão), e cronograma de execução (migração única big-bang ou migração incremental com período de coexistência). A migração de dados é frequentemente o maior risco de portais que substituem sistemas legados — dados reais são sujos, inconsistentes e maiores do que qualquer estimativa otimista.

### Perguntas

1. O modelo de dados foi definido com todas as entidades, atributos, tipos e relacionamentos documentados formalmente? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
2. Os contratos de API (endpoints, schemas de request/response, códigos de erro) foram especificados em formato padronizado (OpenAPI)? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
3. Os wireframes ou protótipos dos fluxos críticos foram testados com usuários representativos e aprovados? [fonte: UX, Designer, Usuários finais] [impacto: Dev, Designer, PM]
4. O mapa completo de telas e navegação distingue corretamente telas públicas, autenticadas e restritas por perfil? [fonte: UX, Designer, Operações] [impacto: Dev, Designer]
5. As regras de negócio foram documentadas formalmente com exemplos e casos limite? [fonte: Operações, Diretoria, Analista de Negócios] [impacto: Dev, QA]
6. O plano de migração de dados (se aplicável) inclui mapeamento campo a campo, regras de transformação e cronograma? [fonte: TI, DBA, Operações] [impacto: Dev, PM]
7. As validações de cada campo de formulário foram especificadas (obrigatoriedade, formato, tamanho, mensagem de erro)? [fonte: UX, Analista de Negócios] [impacto: Dev]
8. Os fluxos de erro e exceção foram mapeados — o que acontece quando a API de integração está fora, quando o pagamento falha, quando o upload excede o limite? [fonte: Arquiteto, Operações] [impacto: Dev, QA]
9. O modelo de permissões (RBAC ou ABAC) foi especificado com matriz completa de perfil × ação × recurso? [fonte: Segurança da Informação, Operações] [impacto: Dev, Arquiteto]
10. Os templates de e-mail transacional (boas-vindas, reset de senha, notificações) foram redigidos e aprovados? [fonte: Marketing, Operações, UX] [impacto: Dev, Conteúdo]
11. Os critérios de aceitação de cada funcionalidade foram escritos de forma testável (dado X, quando Y, então Z)? [fonte: Analista de Negócios, QA] [impacto: Dev, QA]
12. O volume de dados a migrar foi quantificado com precisão e o esforço de migração incluído no cronograma? [fonte: TI, DBA] [impacto: Dev, PM]
13. Os requisitos de auditoria foram especificados — quais eventos registrar, formato do log, período de retenção? [fonte: Compliance, Segurança da Informação] [impacto: Dev, Arquiteto]
14. O comportamento de sessão expirada foi definido — o que acontece quando o token expira durante uma operação em andamento? [fonte: UX, Arquiteto] [impacto: Dev]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes de avançar para Architecture? [fonte: Diretoria, Operações, TI] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Arquitetura de aplicação**: Definir a estrutura da aplicação backend — monolítico com camadas (controller → service → repository), modular monolith (módulos independentes dentro de um único deploy), ou BFF leve que orquestra chamadas a APIs existentes. Para portais web com complexidade moderada, monolítico com camadas é o padrão correto — simples de entender, deployar e operar. Microserviços são overkill para portal web e devem ser ativamente desencorajados a menos que haja justificativa excepcional (ex.: módulo de processamento de arquivos que precisa escalar independentemente). A estrutura interna do monolítico deve seguir separação clara: rotas/controllers (HTTP), serviços (lógica de negócio), repositórios (acesso a dados), e middlewares (autenticação, autorização, logging).

- **Banco de dados e persistência**: PostgreSQL é o banco de dados recomendado como padrão para portais web — robusto, maduro, com excelente suporte a JSON (jsonb), full-text search nativo, e ecossistema de ferramentas amplo. A decisão a ser feita é: gerenciado em cloud (RDS, Supabase, Neon) vs. self-hosted (Docker, VM dedicada). Gerenciado elimina a carga de backups, patches e failover — custo justificado para projetos que não têm DBA dedicado. Definir também a estratégia de migração de schema (Prisma Migrate, Drizzle Kit, Flyway, Liquibase) — schema changes devem ser versionados no repositório e aplicados automaticamente no deploy, nunca manualmente no banco.

- **Infraestrutura de autenticação e autorização**: Detalhar a implementação técnica da autenticação: provedor escolhido (Keycloak, Auth0, Clerk, Auth.js), protocolo (JWT stateless vs. sessions stateful), armazenamento de sessão (cookie httpOnly secure vs. localStorage — cookie é o padrão correto por segurança), refresh token strategy (rotação automática, expiração configurada), e middleware de autorização (verificação de role/permission em cada rota da API). Se SSO corporativo, detalhar a integração com o IdP (SAML vs. OIDC, discovery URL, mapeamento de claims para roles internas). A autenticação é a superfície de ataque mais crítica do portal — qualquer falha aqui é vulnerabilidade de segurança P0.

- **Infraestrutura de e-mail transacional**: Selecionar e configurar o provedor de e-mail transacional (SendGrid, Resend, AWS SES, Postmark) para envio de e-mails de cadastro, verificação, reset de senha e notificações. Configurar SPF, DKIM e DMARC no domínio para maximizar deliverability — sem essa configuração, e-mails transacionais caem em spam, o que bloqueia fluxos críticos como cadastro e recuperação de senha. O provedor deve suportar templates HTML responsivos, variáveis de personalização, e tracking de abertura/clique. Planejar também a fila de envio — e-mails não devem ser enviados sincronamente no request da API, mas via job queue (BullMQ, SQS) para não impactar o tempo de resposta.

- **Estratégia de cache e performance**: Definir as camadas de cache — cache de sessão (Redis para sessões stateful ou JWT com refresh controlado), cache de dados frequentes (Redis para dados que mudam raramente, como listas de estados, configurações de sistema), cache de API (stale-while-revalidate para dados de integrações externas com latência alta), e cache de frontend (React Query ou SWR com configuração de staleTime por tipo de dado). Para portais de autoatendimento com consultas a sistemas legados lentos, o cache é a diferença entre uma experiência de 200ms e uma experiência de 5 segundos.

- **Estratégia de observabilidade**: Definir a stack de monitoramento — logs estruturados (Pino ou Winston para Node.js, com nível por ambiente), métricas de aplicação (latência de API, taxa de erro, sessões ativas), monitoramento de infraestrutura (CPU, memória, disco, conexões de banco), e alertas automatizados (alerta em Slack/Teams quando taxa de erro 5xx ultrapassa 1% ou latência P95 ultrapassa 2s). Para portais em produção, a observabilidade não é opcional — é a diferença entre descobrir um problema pelo monitoramento em 5 minutos e descobrir pelo usuário ligando para o suporte 2 horas depois.

### Perguntas

1. A arquitetura de aplicação foi definida (monolítico, modular monolith, BFF) com justificativa documentada para a escolha? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
2. O banco de dados foi escolhido (PostgreSQL gerenciado vs. self-hosted) e a estratégia de migração de schema definida? [fonte: Arquiteto, DBA, TI] [impacto: Dev, DevOps]
3. A implementação técnica de autenticação foi detalhada — provedor, protocolo, armazenamento de sessão, refresh strategy? [fonte: Arquiteto, Segurança da Informação] [impacto: Dev]
4. A integração com IdP corporativo (se aplicável) foi especificada — protocolo, discovery URL, mapeamento de claims? [fonte: TI, Segurança da Informação, Fornecedor IdP] [impacto: Dev, Arquiteto]
5. O provedor de e-mail transacional foi escolhido e os registros SPF/DKIM/DMARC estão planejados? [fonte: TI, DevOps] [impacto: Dev, DevOps]
6. A estratégia de cache foi definida por camada (sessão, dados, API, frontend)? [fonte: Arquiteto] [impacto: Dev]
7. A stack de observabilidade foi definida (logs, métricas, alertas) com thresholds de alerta configurados? [fonte: Arquiteto, DevOps] [impacto: DevOps, Dev]
8. A estratégia de tratamento de erros em integrações foi definida (retry, fallback, circuit breaker)? [fonte: Arquiteto] [impacto: Dev]
9. Os ambientes foram definidos (development, staging, production) com estratégia de dados em cada um (dados de teste vs. cópia sanitizada de produção)? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
10. A arquitetura suporta o escopo futuro previsto (app mobile via API, novos perfis, crescimento de volume)? [fonte: Diretoria, Arquiteto] [impacto: Arquiteto, Dev]
11. Os custos mensais de infraestrutura foram calculados em cenário esperado e cenário de pico? [fonte: Financeiro, Arquiteto, DevOps] [impacto: PM, DevOps]
12. A estratégia de backup e disaster recovery foi definida (RPO, RTO, procedimento de restauração testado)? [fonte: TI, Segurança da Informação] [impacto: DevOps]
13. O pipeline de CI/CD foi desenhado com build, testes automatizados, deploy em staging e promoção para produção? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
14. A estratégia de rate limiting e proteção contra abuso foi definida (rate limit por IP, por usuário, CAPTCHA em cadastro)? [fonte: Segurança da Informação, Arquiteto] [impacto: Dev]
15. O documento de arquitetura foi revisado por ao menos um segundo arquiteto ou dev sênior antes de avançar? [fonte: TI, Arquiteto] [impacto: Dev, DevOps]

---

## Etapa 06 — Setup

- **Estrutura do repositório**: Organizar o repositório com separação clara entre frontend e backend — monorepo (Turborepo, Nx) com packages separados ou repositórios distintos. Em portais web, monorepo é geralmente a melhor escolha — permite compartilhar tipos TypeScript entre frontend e backend (schemas de API, tipos de entidade), executar lint e testes em um único CI pipeline, e manter versionamento consistente. A estrutura interna deve ter separação clara: `/apps/web` (frontend), `/apps/api` (backend), `/packages/shared` (tipos e utilidades compartilhados), `/packages/db` (schema do banco e migrações).

- **Configuração do banco de dados**: Provisionar o banco de dados nos ambientes de desenvolvimento, staging e produção. Criar o schema inicial com as migrações definidas na etapa anterior. Configurar connection pooling (PgBouncer ou connection pool nativo do ORM) para evitar exaustão de conexões em picos de uso — PostgreSQL tem limite de conexões simultâneas que, sem pooling, é atingido rapidamente em aplicações com muitas instâncias. Definir a estratégia de seed — dados iniciais necessários para o funcionamento do sistema (roles padrão, configurações, admin inicial) devem ser criados automaticamente via script de seed, não manualmente.

- **Setup da autenticação**: Configurar o provedor de autenticação escolhido — criar o tenant/realm (Keycloak) ou application (Auth0, Clerk), configurar os fluxos de login/cadastro/reset, integrar com o backend da aplicação, e testar o fluxo completo end-to-end em ambiente de desenvolvimento. Se SSO corporativo, coordenar com o time de TI do cliente a configuração no IdP — registro da aplicação, redirect URIs, mapeamento de grupos para roles. Esta configuração frequentemente tem lead time de dias a semanas no lado do cliente — não deixar para a última hora.

- **Configuração de e-mail transacional**: Provisionar o provedor de e-mail (SendGrid, Resend, AWS SES), configurar o domínio de envio com SPF, DKIM e DMARC, criar os templates de e-mail (boas-vindas, verificação, reset, notificações), e enviar e-mails de teste para validar deliverability em múltiplos clientes (Gmail, Outlook, Yahoo). Deliverability de e-mail em domínios novos é notoriamente baixa — recomenda-se "aquecer" o domínio enviando volumes crescentes nas semanas antes do go-live. Um e-mail de reset de senha que cai em spam é equivalente a um portal sem recuperação de senha.

- **Pipeline de CI/CD**: Configurar o pipeline completo: push para feature branch dispara lint + build + testes unitários, PR para main dispara testes E2E + deploy em staging, merge para main dispara deploy em produção (automático ou com aprovação manual). Incluir no pipeline: verificação de tipos TypeScript (tsc --noEmit), lint (ESLint), formatação (Prettier), testes unitários (Vitest ou Jest), testes E2E (Playwright ou Cypress) ao menos para fluxos de autenticação, e migration check (verificar que migrações de banco são reversíveis). GitHub Actions é a escolha padrão — gratuito para repositórios públicos, plano generoso para privados.

- **Variáveis de ambiente e secrets**: Configurar todas as chaves, tokens e URLs como variáveis de ambiente — nunca hardcoded. Isso inclui: credenciais do banco de dados, secrets do provedor de autenticação, API keys de integrações externas, tokens de e-mail transacional, e qualquer outro segredo. Usar .env.local (no .gitignore) para desenvolvimento, e secrets do CI/CD provider (GitHub Secrets, Vercel Environment Variables) para staging e produção. Documentar todas as variáveis necessárias em um .env.example commitado no repositório — com valores de exemplo, nunca com secrets reais.

### Perguntas

1. A estrutura do repositório (monorepo ou multi-repo) foi definida, configurada e documentada no README? [fonte: Dev, Arquiteto] [impacto: Dev]
2. O banco de dados foi provisionado nos três ambientes (dev, staging, produção) com schema inicial aplicado? [fonte: DevOps, DBA] [impacto: Dev, DevOps]
3. O connection pooling foi configurado e testado sob carga simulada? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
4. O script de seed cria corretamente os dados iniciais (roles, admin, configurações) em um banco limpo? [fonte: Dev] [impacto: Dev]
5. O provedor de autenticação foi configurado e o fluxo completo (cadastro → login → logout → reset) funciona end-to-end? [fonte: Dev, TI] [impacto: Dev]
6. A integração com IdP corporativo (se aplicável) foi configurada, testada e funciona nos ambientes de dev e staging? [fonte: TI, Segurança da Informação, Fornecedor IdP] [impacto: Dev]
7. O e-mail transacional foi configurado com SPF/DKIM/DMARC e os templates testados em Gmail, Outlook e Yahoo? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
8. O pipeline de CI/CD está completo com lint, build, testes e deploy automático para staging? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
9. O .env.example está documentado no repositório com todas as variáveis necessárias e instruções de preenchimento? [fonte: Dev] [impacto: Dev]
10. Os secrets de produção estão configurados no provider de CI/CD e não existem em nenhum arquivo commitado? [fonte: Dev, Segurança da Informação] [impacto: Dev, DevOps]
11. O ambiente de staging está funcional, isolado de produção, e acessível para testes pelo time e pelo cliente? [fonte: DevOps, PM] [impacto: Dev, QA, PM]
12. O processo de onboarding de novos desenvolvedores foi documentado com instruções de setup local completo? [fonte: Dev] [impacto: Dev]
13. O monitoramento e alertas de infraestrutura estão configurados e testados (alerta dispara corretamente em condição simulada)? [fonte: DevOps] [impacto: DevOps, Dev]
14. Os endpoints de healthcheck da aplicação e do banco estão implementados e configurados no load balancer? [fonte: Dev, DevOps] [impacto: DevOps]
15. O pipeline de CI/CD foi testado com um PR real — lint passou, build completou, testes rodaram, deploy em staging funcionou? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Fluxos de autenticação**: Implementar primeiro os fluxos de autenticação completos — cadastro com verificação de e-mail, login com credenciais, login social (se aplicável), MFA (se aplicável), recuperação de senha, logout, e refresh de sessão transparente. Esses fluxos são a fundação sobre a qual todo o resto do portal é construído — não é possível testar nenhuma funcionalidade autenticada enquanto a autenticação não estiver funcional e estável. Implementar também o middleware de proteção de rotas (redirect para login se não autenticado, redirect para dashboard se já autenticado tentando acessar login, verificação de permissão por rota).

- **Componentes base e design system**: Implementar os componentes reutilizáveis do design system antes de iniciar os templates de tela — tipografia, paleta de cores como variáveis CSS/tokens, espaçamento, e componentes atômicos (Button, Input, Select, Textarea, Checkbox, Radio, Badge, Avatar, Card, Modal, Toast, Table, Pagination, Skeleton/Loading). Em portais autenticados, a biblioteca de componentes é significativamente maior que em sites estáticos porque há mais tipos de interação: formulários complexos, tabelas com ordenação e filtro, modais de confirmação, dropdowns de ação, notificações inline, e indicadores de status. Usar Radix UI, Headless UI ou shadcn/ui como base acelera o desenvolvimento e garante acessibilidade nativa.

- **Implementação das APIs**: Implementar os endpoints da API seguindo os contratos definidos na etapa 04, com validação de entrada (Zod, Joi ou class-validator), tratamento de erros padronizado (formato de erro consistente com código, mensagem e detalhes), e middleware de autorização (verificar que o usuário autenticado tem permissão para a operação solicitada). Cada endpoint deve ter ao menos um teste automatizado que valida o contrato — request válido retorna resposta no formato esperado, request inválido retorna erro no formato esperado, request sem autenticação retorna 401, request sem permissão retorna 403.

- **Integrações com sistemas externos**: Implementar as integrações com sistemas legados e APIs externas mapeadas na etapa 02 — com circuit breaker (falha do sistema externo não derruba o portal), retry com backoff exponencial (falhas transitórias se resolvem sozinhas), timeout configurado (request que demora mais de 10s é abortado), e fallback gracioso (se o sistema de billing está fora, mostrar "dados temporariamente indisponíveis" em vez de erro 500). Cada integração deve ter seu próprio módulo isolado com interface bem definida — facilitando substituição futura e testabilidade com mocks.

- **Migração de dados (se aplicável)**: Executar a migração de dados do sistema legado conforme o plano definido na etapa 04. A migração deve ser idempotente (pode ser executada múltiplas vezes sem duplicar dados), reversível (há script de rollback), e validada com contagem e amostragem (total de registros migrados confere com a origem, e amostra aleatória é verificada campo a campo). A migração de usuários merece atenção especial — senhas hashadas em algoritmo antigo (MD5, SHA1 sem salt) precisam de estratégia de rehash (migrar hash antigo, e no primeiro login do usuário, rehash para bcrypt/argon2 transparentemente).

- **Acessibilidade e responsividade**: Implementar conformidade WCAG 2.1 AA ao longo do build, integrada ao desenvolvimento de cada componente — contraste mínimo 4.5:1, labels em todos os campos de formulário, landmarks semânticos, navegação por teclado funcional (Tab, Shift+Tab, Enter, Escape em modais), foco visível em todos os elementos interativos, e anúncios de estado para screen readers (ARIA live regions para toasts, erros de formulário e loading). Em portais autenticados, formulários são os componentes mais críticos para acessibilidade — um formulário de cadastro inacessível exclui completamente uma parcela dos usuários potenciais.

### Perguntas

1. Os fluxos de autenticação completos (cadastro, login, MFA, reset, logout, refresh) estão implementados e testados? [fonte: Dev, QA] [impacto: Dev, QA]
2. O middleware de proteção de rotas funciona corretamente — redirect para login, verificação de permissão, sessão expirada? [fonte: Dev] [impacto: Dev, QA]
3. Todos os componentes base do design system foram implementados, documentados e revisados antes dos templates de tela? [fonte: Designer, Dev] [impacto: Dev]
4. Os endpoints da API estão implementados com validação de entrada, tratamento de erros padronizado e testes de contrato? [fonte: Dev, QA] [impacto: Dev, QA]
5. As integrações com sistemas externos têm circuit breaker, retry, timeout e fallback implementados? [fonte: Dev, Arquiteto] [impacto: Dev]
6. A migração de dados (se aplicável) foi executada em staging com sucesso e os totais conferem com a origem? [fonte: Dev, DBA] [impacto: Dev, PM]
7. A estratégia de rehash de senhas migradas (se aplicável) foi implementada e testada? [fonte: Dev, Segurança da Informação] [impacto: Dev]
8. Os formulários têm validação client-side e server-side consistentes, com mensagens de erro claras por campo? [fonte: Designer, Dev] [impacto: Dev, QA]
9. Os empty states estão implementados em todas as telas de listagem — mensagem útil e CTA quando não há dados? [fonte: Designer, UX] [impacto: Dev]
10. Os e-mails transacionais estão sendo enviados corretamente via job queue (não sincronamente no request da API)? [fonte: Dev] [impacto: Dev, DevOps]
11. Os testes E2E dos fluxos críticos (login, cadastro, operações principais) estão implementados e passando no CI? [fonte: Dev, QA] [impacto: Dev, QA]
12. A implementação de acessibilidade está sendo feita ao longo do build com axe-core ou pa11y, não apenas no final? [fonte: Dev, Designer] [impacto: Dev, QA]
13. O audit log está registrando corretamente as ações sensíveis (login, alteração de dados, operações de admin)? [fonte: Dev, Compliance] [impacto: Dev, Segurança]
14. O progresso da migração de dados (se aplicável) está dentro do prazo e sem bloqueadores de qualidade? [fonte: Dev, PM, DBA] [impacto: PM, Dev]
15. Os estados de loading, erro e timeout em chamadas de API estão implementados em todas as telas? [fonte: Designer, Dev] [impacto: Dev, QA]

---

## Etapa 08 — QA

- **Testes de autenticação e autorização**: Testar exaustivamente todos os fluxos de autenticação — cadastro com dados válidos e inválidos, login com credenciais corretas e erradas, bloqueio após N tentativas falhas, recuperação de senha com e-mail existente e inexistente, MFA com código correto e expirado, sessão expirada durante operação, logout que invalida sessão/token de fato. Testar autorização tentando acessar recursos de outro usuário (IDOR — Insecure Direct Object Reference), tentando acessar rotas de admin com perfil de usuário comum, e tentando manipular tokens JWT no frontend. Falhas de autenticação e autorização são vulnerabilidades de segurança — não são bugs cosméticos.

- **Testes de integração com sistemas externos**: Testar cada integração em cenário normal (sistema disponível, dados corretos) e em cenário de falha (sistema indisponível, timeout, dados inesperados). Verificar que o circuit breaker funciona — quando o sistema externo está fora, o portal degrada graciosamente sem derrubar. Verificar que o retry resolve falhas transitórias sem duplicar operações (idempotência). Se o sistema externo tem ambiente de sandbox, executar testes contra o sandbox com dados representativos de produção. Se não tem sandbox, documentar o gap de teste e o risco associado.

- **Testes de performance e carga**: Executar testes de carga (k6, Artillery, Locust) simulando o cenário esperado de uso — número de usuários simultâneos, taxa de login por minuto, volume de consultas à API. Identificar gargalos: queries lentas no banco (falta de índice), serialização de respostas grandes (paginação inadequada), conexões de banco esgotadas (pool insuficiente), ou memória crescente (memory leak). Em portais de autoatendimento, simular o cenário de pico (ex.: todos os alunos acessando no dia da matrícula) é obrigatório — descobrir que o portal não aguenta a carga no dia do pico é catastrófico.

- **Testes de segurança**: Executar verificação de vulnerabilidades comuns — OWASP Top 10 como referência. Os mais relevantes para portais web: Injection (SQL injection via inputs, XSS via conteúdo gerado pelo usuário), Broken Authentication (sessões que não expiram, tokens previsíveis, falta de rate limiting no login), Broken Access Control (IDOR, escalação de privilégio), Security Misconfiguration (headers de segurança ausentes — CSP, X-Frame-Options, HSTS, X-Content-Type-Options), e Sensitive Data Exposure (senhas em log, dados pessoais em URL, falta de HTTPS). Ferramentas como OWASP ZAP ou Burp Suite Community podem automatizar parte desses testes.

- **Testes de responsividade e cross-browser**: Validar todas as telas do portal nos breakpoints definidos (375px mobile, 768px tablet, 1024px desktop, 1440px wide) em browsers reais ou emulação. Portais autenticados têm componentes mais complexos que sites estáticos — tabelas com muitas colunas que precisam de scroll horizontal ou reformatação em mobile, formulários extensos que precisam de step wizard em telas pequenas, dashboards com gráficos que precisam redimensionar, e modais que precisam ocupar tela cheia em mobile. Testar também a experiência de login em mobile — campos de e-mail e senha devem acionar o teclado correto, autofill deve funcionar, e o botão de submit deve estar visível sem scroll.

- **Testes de fluxo completo (smoke test)**: Executar um smoke test que percorre a jornada completa do usuário — do cadastro ao uso da funcionalidade principal — em ambiente de staging com dados representativos. O smoke test deve ser executável em menos de 30 minutos e cobrir: cadastro, verificação de e-mail, primeiro login, onboarding, navegação ao dashboard, execução da operação principal, recebimento de notificação, alteração de perfil, e logout. Este teste deve ser automatizado (Playwright ou Cypress) e executado antes de cada deploy para produção.

### Perguntas

1. Todos os fluxos de autenticação foram testados com cenários válidos e inválidos, incluindo tentativa de IDOR e escalação de privilégio? [fonte: QA, Segurança da Informação] [impacto: Dev, Segurança]
2. As integrações com sistemas externos foram testadas em cenário de falha (timeout, indisponibilidade) e o fallback funciona? [fonte: QA, Dev] [impacto: Dev]
3. O teste de carga foi executado simulando o cenário de pico esperado e os gargalos identificados foram resolvidos? [fonte: QA, DevOps, Dev] [impacto: Dev, DevOps]
4. A verificação de segurança OWASP Top 10 foi executada e as vulnerabilidades encontradas foram corrigidas? [fonte: Segurança da Informação, QA] [impacto: Dev, Segurança]
5. Os headers de segurança estão configurados corretamente (CSP, HSTS, X-Frame-Options, X-Content-Type-Options)? [fonte: Dev, Segurança da Informação] [impacto: Dev]
6. Os testes de responsividade cobrem todos os breakpoints em todas as telas, incluindo formulários e tabelas complexas? [fonte: QA, Designer] [impacto: Dev, Designer]
7. O smoke test automatizado percorre a jornada completa do usuário e está integrado ao pipeline de CI/CD? [fonte: QA, Dev] [impacto: Dev, QA]
8. Os e-mails transacionais chegam no inbox (não em spam) dos principais provedores (Gmail, Outlook, Yahoo)? [fonte: QA, DevOps] [impacto: Dev, DevOps]
9. A migração de dados (se aplicável) foi validada em staging — totais conferem, amostra verificada, e fluxos funcionam com dados migrados? [fonte: QA, Dev, DBA] [impacto: Dev, PM]
10. A sessão expirada durante uma operação em andamento é tratada corretamente — não perde dados do formulário, redireciona para login e retorna? [fonte: QA, UX] [impacto: Dev]
11. O comportamento de rate limiting foi testado — tentativas excessivas de login são bloqueadas sem afetar usuários legítimos? [fonte: QA, Segurança da Informação] [impacto: Dev]
12. Os logs de auditoria registram corretamente todas as ações sensíveis e são consultáveis pela equipe de operações? [fonte: QA, Compliance] [impacto: Dev]
13. O teste de acessibilidade com screen reader (NVDA ou VoiceOver) foi realizado nos fluxos críticos (cadastro, login, operações principais)? [fonte: QA, Dev] [impacto: Dev]
14. Os dados sensíveis não aparecem em logs, URLs ou respostas de API que não deveriam contê-los? [fonte: Segurança da Informação, QA] [impacto: Dev, Segurança]
15. A revisão ortográfica e de consistência de conteúdo foi concluída em todas as telas, e-mails e mensagens de erro? [fonte: QA, Conteúdo] [impacto: Conteúdo, Dev]

---

## Etapa 09 — Launch Prep

- **Plano de migração de dados em produção**: Se há migração de dados de sistema legado, preparar o plano detalhado de execução em produção — sequência de scripts, tempo estimado de execução (testar com volume real em staging), janela de manutenção necessária (período em que o sistema antigo está congelado e o novo ainda não está acessível), e validação pós-migração (queries de contagem e amostragem para confirmar integridade). Se a migração inclui usuários com senhas, testar que o fluxo de rehash no primeiro login funciona corretamente. Ter script de rollback testado e pronto — se a migração falhar parcialmente, é preciso reverter para o estado anterior limpo.

- **Comunicação aos usuários sobre a transição**: Preparar e agendar as comunicações para os usuários finais — e-mail informando sobre o novo portal (o que muda, quando muda, como acessar), FAQ com respostas para as perguntas mais esperadas (minha senha funciona? meus dados estão lá? como recupero acesso?), e página de status visível durante a janela de migração. Se o portal substitui um sistema com URL diferente, configurar redirect da URL antiga para a nova. A comunicação deve ser enviada com antecedência suficiente (1-2 semanas) e repetida no dia do lançamento. Usuários pegos de surpresa por uma mudança de sistema geram pico de suporte evitável.

- **Configuração de monitoramento e alertas**: Ativar o monitoramento completo antes do go-live — uptime check (UptimeRobot, Better Uptime ou Checkly) com verificação a cada 1 minuto, alertas de taxa de erro (5xx > 1%, latência P95 > 2s, falha de login > 10% das tentativas), dashboards de métricas de negócio (cadastros por hora, logins por hora, operações completadas), e canal de incidentes (Slack ou Teams) onde os alertas são recebidos pelo time de operação. Testar os alertas antes do go-live — simular a condição de alerta e verificar que a notificação chega ao canal correto em tempo aceitável.

- **Treinamento de operadores internos**: Realizar sessão de treinamento com o time que vai operar o portal internamente — administradores que gerenciam usuários (criar conta, resetar senha, desativar usuário, alterar permissões), operadores de suporte que atendem usuários com problemas (como consultar o log de ações de um usuário, como reproduzir um problema reportado), e gestores que acompanham métricas (onde ver o dashboard, como interpretar os números). Entregar documentação em formato acessível (Notion, Google Docs) com capturas de tela — o treinamento presencial é esquecido em semanas, a documentação permanece.

- **Plano de rollback e contingência**: Documentar o plano de rollback completo — critérios de acionamento (formulário de cadastro quebrado, taxa de erro acima de 5%, integração principal fora), sequência de ações (reverter deploy, reverter migração de dados se necessário, reativar sistema anterior, comunicar usuários), responsável pela decisão de rollback, e tempo estimado de execução do rollback. Se a migração de dados é irreversível em tempo hábil (ex.: sistema legado foi desligado), o plano de contingência deve prever correção forward (fix no sistema novo) em vez de rollback — e o time deve estar preparado para operar em modo de emergência nas primeiras horas.

- **Checklist legal e compliance**: Verificar todos os artefatos de conformidade — política de privacidade publicada e acessível (com menção específica ao portal), termos de uso publicados e com aceite no cadastro (checkbox obrigatório ou tela de aceite no primeiro login), banner de cookies (se aplicável), registro de atividades de tratamento de dados (exigido pela LGPD), nomeação de DPO (Data Protection Officer) ou encarregado de dados pessoais, e procedimento de resposta a incidentes de segurança documentado. Cada um desses itens tem implicação legal direta — portal sem política de privacidade está em descumprimento da LGPD desde o primeiro cadastro.

### Perguntas

1. O plano de migração de dados em produção está documentado com sequência, tempo estimado, janela de manutenção e script de rollback? [fonte: Dev, DBA, PM] [impacto: Dev, DevOps, PM]
2. A comunicação aos usuários sobre a transição foi preparada, revisada e agendada para envio com antecedência? [fonte: Marketing, Operações, PM] [impacto: PM, Operações]
3. O monitoramento de uptime, taxa de erro e métricas de negócio está ativo e os alertas foram testados? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
4. O treinamento de operadores internos (admin, suporte, gestores) foi realizado e a documentação entregue? [fonte: PM, Operações] [impacto: Operações, PM]
5. O plano de rollback está documentado com critérios claros de acionamento, sequência de ações e responsável designado? [fonte: Dev, DevOps, PM] [impacto: DevOps, PM]
6. A política de privacidade e os termos de uso estão publicados, revisados pelo jurídico e com aceite no fluxo de cadastro? [fonte: Jurídico, DPO, Dev] [impacto: Dev, Jurídico]
7. O banner de cookies (se aplicável) está funcional e respeita as opções do usuário (opt-out efetivamente para tracking)? [fonte: Dev, Jurídico] [impacto: Dev]
8. O redirect da URL do sistema antigo para o novo portal está configurado e testado (se aplicável)? [fonte: Dev, TI] [impacto: Dev, DevOps]
9. Os backups de produção foram verificados — backup funciona, restore foi testado, e RPO/RTO estão dentro do especificado? [fonte: DevOps, DBA] [impacto: DevOps]
10. Todos os stakeholders foram notificados sobre a data, horário e impactos esperados do go-live? [fonte: PM, Diretoria] [impacto: PM]
11. O time de suporte está preparado para o aumento esperado de chamados na primeira semana? [fonte: Operações, Suporte] [impacto: PM, Operações]
12. A janela de go-live foi escolhida estrategicamente — horário de baixo uso, dia útil, com time de suporte e dev disponíveis? [fonte: Operações, TI, PM] [impacto: PM, DevOps]
13. Os endpoints de healthcheck estão retornando status correto e o load balancer remove instâncias unhealthy automaticamente? [fonte: DevOps, Dev] [impacto: DevOps]
14. A lista de acessos a serem entregues ao cliente foi revisada e todos os acessos foram testados? [fonte: Dev, DevOps, PM] [impacto: PM]
15. O procedimento de resposta a incidentes de segurança está documentado e o time sabe quem acionar em caso de vazamento? [fonte: Segurança da Informação, Jurídico, DPO] [impacto: Segurança, PM]

---

## Etapa 10 — Go-Live

- **Execução da migração de dados em produção**: Executar a migração conforme o plano da etapa anterior — dentro da janela de manutenção comunicada, seguindo a sequência documentada, monitorando o progresso em tempo real. Após a conclusão, rodar as queries de validação (contagem de registros, verificação de integridade, amostragem aleatória) e comparar com os resultados esperados. Se houver divergência acima do threshold aceitável (definido previamente), acionar o procedimento de rollback ou correção. Registrar o tempo real de execução para comparação com a estimativa — útil para futuras migrações.

- **Ativação do portal e smoke test em produção**: Após a migração (se aplicável) e o deploy final em produção, executar o smoke test completo — cadastro de usuário de teste, login, navegação ao dashboard, execução da operação principal, recebimento de e-mail, alteração de perfil, logout. Executar de dispositivos diferentes (desktop e mobile) em redes diferentes (sem cache). Verificar que as integrações com sistemas externos estão funcionando em produção — variáveis de ambiente de produção podem apontar para endpoints diferentes de staging, e a primeira chamada real pode revelar problemas de firewall, certificado ou permissão que não existiam em sandbox.

- **Monitoramento ativo nas primeiras horas**: Nas primeiras 4-6 horas após o go-live, monitorar ativamente: taxa de erro de API (5xx devem ser próximos de zero), taxa de sucesso de login (falhas acima de 5% indicam problema de autenticação ou migração), tempo de resposta das integrações externas (latência alta indica problema de rede ou sobrecarga), volume de cadastros e logins (validar que está dentro do esperado — zero pode indicar problema de DNS ou acesso), e canal de suporte (tickets chegando indicam problemas que o monitoramento técnico pode não capturar). Ter pelo menos um dev e um operador de suporte dedicados ao monitoramento durante este período.

- **Comunicação de lançamento**: Enviar a comunicação final aos usuários confirmando que o novo portal está no ar — com link direto, instruções de primeiro acesso (especialmente se houve migração de contas — "use seu e-mail existente e clique em Esqueci Minha Senha para definir nova senha"), e canal de suporte para dúvidas. Se há campanhas de marketing vinculadas ao lançamento, confirmar com o time de marketing que os links estão corretos e os pixels de tracking estão ativos. Timing é importante — enviar a comunicação apenas após confirmar que o portal está estável, não simultaneamente ao go-live.

- **Monitoramento da primeira semana**: Após as primeiras horas críticas, manter monitoramento diário durante 7 dias: métricas de adoção (quantos usuários migraram, quantos se cadastraram, taxa de ativação), métricas de performance (Core Web Vitals reais via CrUX, latência de API P50/P95/P99), erros recorrentes (erros que se repetem com padrão indicam bug sistêmico, não falha transitória), e feedback de usuários (via canal de suporte ou pesquisa in-app). A primeira semana é o período onde a maioria dos bugs de produção emerge — dados reais de volume real exercitam caminhos que os testes não cobriram.

- **Entrega e handoff ao cliente**: Entregar formalmente todos os acessos ao cliente com documentação: acesso ao repositório (GitHub/GitLab) com instruções de deploy, acesso à infraestrutura (cloud provider, banco de dados, monitoring dashboard), acesso ao provedor de autenticação (Keycloak admin, Auth0 dashboard), acesso ao provedor de e-mail transacional, e documentação técnica (arquitetura, modelo de dados, fluxos de integração, procedimentos de operação). A documentação mínima deve incluir: como deployar, como criar/gerenciar usuários, como interpretar os dashboards de monitoramento, procedimento de backup e restore, e contato de suporte técnico com SLA.

### Perguntas

1. A migração de dados em produção foi executada com sucesso e os totais conferem com o esperado? [fonte: Dev, DBA, PM] [impacto: Dev, PM]
2. O smoke test completo foi executado em produção com dados reais e todas as funcionalidades críticas estão operacionais? [fonte: QA, Dev] [impacto: Dev, PM]
3. As integrações com sistemas externos estão funcionando em produção — não apenas em staging? [fonte: Dev, QA] [impacto: Dev]
4. A taxa de erro de API nas primeiras horas está dentro do aceitável (< 1% de 5xx)? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
5. Os e-mails transacionais estão sendo entregues corretamente em produção (cadastro, reset, notificações)? [fonte: QA, DevOps] [impacto: Dev, DevOps]
6. A comunicação de lançamento foi enviada aos usuários após confirmação de estabilidade do portal? [fonte: Marketing, Operações, PM] [impacto: PM, Operações]
7. O monitoramento de disponibilidade está ativo e os alertas foram validados em produção? [fonte: DevOps] [impacto: DevOps]
8. O canal de suporte está operacional e o time de suporte está recebendo e respondendo aos primeiros tickets? [fonte: Operações, Suporte] [impacto: Operações, PM]
9. As métricas de adoção estão sendo acompanhadas — cadastros, logins, operações completadas — e estão dentro do esperado? [fonte: PM, Operações] [impacto: PM]
10. Os logs de auditoria em produção estão registrando corretamente e são consultáveis? [fonte: Dev, Compliance] [impacto: Dev, Segurança]
11. O plano de rollback está pronto para acionamento imediato e o sistema anterior permanece acessível durante o período de contingência? [fonte: DevOps, TI] [impacto: DevOps, PM]
12. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou que consegue acessar? [fonte: Dev, DevOps, PM] [impacto: PM]
13. O aceite formal de entrega foi obtido do cliente (e-mail, assinatura de ata ou confirmação documentada)? [fonte: Diretoria, PM] [impacto: PM]
14. O plano de suporte pós-lançamento foi ativado (canal definido, SLA comunicado, time escalado para a primeira semana)? [fonte: Diretoria, PM] [impacto: PM, Dev, DevOps]
15. A documentação técnica de operação foi entregue e inclui procedimentos de deploy, backup, restore e tratamento de incidentes? [fonte: Dev, DevOps] [impacto: PM, DevOps]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"É só um site com login"** — O cliente minimiza a complexidade porque a referência mental é um site estático com uma tela de login na frente. Na realidade, autenticação, controle de acesso, gestão de sessão, recuperação de senha, segurança de dados pessoais e operação contínua transformam o projeto em uma aplicação web com requisitos de backend, infraestrutura e monitoramento. Se o cliente espera custo e prazo de site estático, o desalinhamento vai explodir no meio do projeto.
- **"Todos os funcionários vão usar, são 5.000"** — O cliente informa o total de funcionários, não os usuários ativos simultâneos. 5.000 funcionários podem significar 50 acessos simultâneos (portal de RH consultado ocasionalmente) ou 2.000 acessos simultâneos (portal de operações usado o dia inteiro). Sem entender o padrão de uso, a arquitetura pode ser superdimensionada (custo desnecessário) ou subdimensionada (portal cai no primeiro dia).
- **"A gente usa Azure AD para tudo, é só plugar"** — Integração com IdP corporativo nunca é "só plugar". Exige registro da aplicação no Azure AD/Okta (com aprovação do time de segurança do cliente), configuração de claims e grupos, mapeamento para roles internas, e testes em ambiente de sandbox que pode não existir. O lead time dessa integração costuma ser de semanas, não dias, e depende de um time que não responde ao nosso PM.

### Etapa 02 — Discovery

- **"O sistema legado tem uma API, é só chamar"** — "Tem uma API" pode significar REST bem documentada com Swagger ou endpoint SOAP dos anos 2000 sem documentação, com autenticação por IP e disponível apenas em horário comercial. Sem verificar a qualidade real da API (documentação, disponibilidade, performance, formato de dados), a estimativa de integração é chute.
- **"Segurança é com o time de TI, não precisamos nos preocupar"** — Segurança é responsabilidade compartilhada. O time de TI cuida da infraestrutura, mas a aplicação precisa implementar autenticação segura, autorização granular, proteção contra OWASP Top 10, e tratamento correto de dados sensíveis. Delegar segurança completamente para "o time de TI" resulta em portal com vulnerabilidades na camada de aplicação que firewall e WAF não resolvem.
- **"Os dados são simples, tipo nome e e-mail"** — Projetos que começam com "nome e e-mail" inevitavelmente crescem para incluir CPF, endereço, dados financeiros, histórico de interações, documentos enviados e preferências. Se o modelo de dados for projetado para "nome e e-mail", cada campo adicional é uma migração de schema, alteração de API e retrabalho de formulário. Projetar o modelo de dados com visão de 12 meses, não apenas do MVP.

### Etapa 03 — Alignment

- **"Vamos fazer autenticação custom, é mais simples"** — Autenticação custom implementada por time sem expertise em segurança é o caminho mais rápido para vulnerabilidades críticas — senhas em texto plano, tokens previsíveis, sessões que nunca expiram, ou recuperação de senha que vaza se o e-mail existe. Soluções como Keycloak, Auth0 ou Clerk resolvem esses problemas nativamente e são mais baratas que o custo de um incidente de segurança.
- **"Testes a gente faz manual antes do lançamento"** — Testes manuais antes do lançamento cobrem a jornada feliz uma vez. Não cobrem regressões após cada deploy, não cobrem cenários de erro, não cobrem segurança, e não cobrem performance. Em portal autenticado onde um bug no login bloqueia 100% dos usuários, testes automatizados dos fluxos críticos são investimento, não custo.
- **"O design é responsabilidade da agência, eles entregam quando estiver pronto"** — Design entregue por agência externa sem coordenação com o time de desenvolvimento gera designs bonitos e inimplementáveis — componentes que não existem na biblioteca, estados não cobertos, layouts que ignoram dados reais. O design precisa ser feito em colaboração com o dev, não jogado por cima do muro.

### Etapa 04 — Definition

- **"O modelo de dados é parecido com o sistema antigo"** — "Parecido" não é especificação. O modelo de dados do sistema antigo pode ter campos deprecated, tabelas denormalizadas, e decisões de schema que fizeram sentido em 2010 mas são anti-patterns hoje. Replicar o modelo antigo sem questionar resulta em dívida técnica herdada. Definir o modelo do zero, baseado nos requisitos atuais, e tratar a migração como transformação.
- **"As regras de negócio todo mundo sabe, não precisa documentar"** — Regras de negócio na cabeça das pessoas são regras que vão ser implementadas erradas. "Todo mundo sabe" que o desconto é 10% — mas é 10% sobre o valor bruto ou líquido? Incide antes ou depois do imposto? Acumula com outra promoção? Cada regra não documentada é uma decisão que o dev vai tomar sozinho, e a chance de acertar é inversamente proporcional à complexidade da regra.
- **"A API é simples, uns 10 endpoints"** — "Uns 10 endpoints" sem especificação formal significa que frontend e backend vão trabalhar com contratos implícitos que divergem silenciosamente. O frontend espera um campo chamado "name", o backend retorna "full_name". O frontend espera uma lista, o backend retorna null quando vazia. Cada divergência é um bug que só aparece na integração — especificar contratos de API com OpenAPI elimina essa classe inteira de problemas.

### Etapa 05 — Architecture

- **"Vamos usar microserviços para escalar"** — Microserviços para um portal web com 5 entidades e 20 endpoints é over-engineering que multiplica complexidade operacional (deploy de N serviços, comunicação inter-serviço, observabilidade distribuída, consistência de dados) sem entregar benefício. Monolítico bem estruturado escala verticalmente até milhares de requests/segundo. Microserviços fazem sentido quando há necessidade concreta de escalar componentes independentemente — e portais web raramente têm essa necessidade.
- **"Hosting on-premise porque o cliente exige"** — Hosting on-premise para portal web em 2026 elimina as vantagens de cloud gerenciado — auto-scaling, managed database, CI/CD nativo, SSL automático, CDN global. O custo real de on-premise (hardware, licenças, manutenção, equipe de operação, disaster recovery manual) é quase sempre maior que cloud equivalente. Se o cliente exige on-premise por compliance, documentar o custo adicional e a redução de agilidade operacional explicitamente.
- **"Banco NoSQL porque os dados são flexíveis"** — NoSQL (MongoDB, DynamoDB) para portal web com entidades relacionadas (usuário tem perfil, perfil tem permissões, permissão se aplica a recursos) resulta em dados duplicados, consistência eventual onde se espera consistência forte, e queries de relacionamento que são triviais em SQL e dolorosas em NoSQL. PostgreSQL com jsonb resolve o "flexível" sem sacrificar relacionamentos.

### Etapa 06 — Setup

- **Credenciais de produção compartilhadas por Slack** — Tokens de banco de dados, API keys de autenticação ou secrets de deploy enviados em mensagens de Slack/Teams/WhatsApp. Violação de segurança que coloca credenciais em texto plano em um sistema de mensageria que pode ser comprometido. Secrets devem estar exclusivamente no vault do CI/CD provider ou em gerenciador de secrets (AWS Secrets Manager, HashiCorp Vault).
- **Ambiente de staging usando banco de produção** — Staging acessando o banco de produção para "testar com dados reais". Resultado: testes corrompem dados de produção, ou pior, operações de teste afetam usuários reais. Staging deve ter banco isolado, com dados de teste ou cópia sanitizada (sem dados pessoais reais) de produção.
- **"O CMS dos e-mails a gente configura depois"** — E-mail transacional configurado na última hora resulta em: domínio sem aquecimento (e-mails caem em spam), templates sem revisão (erros de texto, links quebrados), e fluxos de cadastro e reset que não funcionam no dia do go-live. Configurar e testar e-mail transacional na fase de Setup é obrigatório.

### Etapa 07 — Build

- **Frontend e backend desenvolvidos em silos** — Frontend implementa baseado no design, backend implementa baseado na especificação, e na integração descobre-se que os contratos não batem — campos com nomes diferentes, formatos incompatíveis, paginação diferente do esperado. Desenvolvimento deve ser integrado continuamente, com contratos de API como artefato compartilhado e integração testada a cada sprint, não apenas no final.
- **Autenticação deixada para o final** — "Primeiro vamos fazer as telas, depois colocamos o login." Resultado: todas as telas são desenvolvidas sem considerar sessão, permissões, ou estados de não-autenticado. Quando a autenticação é integrada, cada tela precisa ser revisitada para adicionar loading de sessão, redirect, e verificação de permissão. Autenticação é a primeira feature a ser implementada, não a última.
- **Validação apenas no frontend** — Formulários validam no client-side (JavaScript), mas a API aceita qualquer dado. Resultado: um Postman ou curl bypassa toda a validação e insere dados inválidos no banco. Validação deve existir em ambas as camadas — frontend para UX (feedback imediato), backend para segurança (nunca confiar no cliente).

### Etapa 08 — QA

- **"Funciona na minha máquina, em produção vai funcionar igual"** — Ambiente de desenvolvimento difere de produção em: variáveis de ambiente, versão de Node/banco, configuração de rede, DNS, e certificados SSL. Funcionar localmente é condição necessária mas não suficiente — QA deve ser executado em staging que espelha produção o mais fielmente possível.
- **Testes de segurança ignorados porque "temos firewall"** — Firewall e WAF protegem a infraestrutura, não a aplicação. SQL injection, XSS, IDOR e broken authentication são vulnerabilidades da camada de aplicação que passam transparentemente pelo firewall. Testes de segurança OWASP Top 10 são obrigatórios para portal autenticado que armazena dados pessoais.
- **Teste de carga com 10 usuários** — Teste de carga que não simula o cenário real de pico não testa nada. Se o portal vai ter 500 usuários simultâneos no pico, o teste precisa simular 500+ usuários com padrão de uso realista (mix de leitura e escrita, sessões com duração variável, picos de login concentrados). Teste com 10 usuários prova que a aplicação funciona, não que escala.

### Etapa 09 — Launch Prep

- **"Os usuários vão descobrir o novo portal sozinhos"** — Migração de sistema sem comunicação prévia gera confusão, pico de suporte e resistência. Usuários tentam acessar a URL antiga (que não funciona mais), não sabem a senha do novo sistema, e ligam irritados para o suporte. Comunicação antecipada com FAQ e instruções de acesso reduz em 80% o volume de suporte pós-lançamento.
- **Rollback não testado** — "Se der problema, revertemos o deploy." Mas o rollback de deploy não reverte a migração de dados. Se 5.000 usuários foram migrados para o novo banco e o portal tem problemas, reverter o deploy sem reverter os dados deixa os usuários sem acesso a ambos os sistemas. Plano de rollback precisa cobrir aplicação e dados, e ambos precisam ser testados antes do go-live.
- **Treinamento apenas para o gerente de TI** — O gerente de TI recebe o treinamento, promete "repassar para o time", e o time de suporte que vai atender os usuários no dia 1 nunca é treinado. Resultado: suporte não sabe responder as perguntas mais básicas e escala tudo para o dev. Treinar diretamente quem vai operar no dia a dia.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde** — Se algo der errado, o time não está disponível no fim de semana. Portal com problemas durante o fim de semana gera tickets acumulados e frustração de usuários. Go-live deve ser em dia útil, de manhã, com pelo menos 6h de buffer para monitoramento e correção.
- **Sistema antigo desligado no mesmo dia** — Se a migração teve problemas não detectados nos primeiros dias, não há como voltar. Manter o sistema antigo acessível (mesmo que em modo somente-leitura) por pelo menos 1-2 semanas é seguro e barato comparado ao custo de perda de dados ou indisponibilidade total.
- **"O portal está no ar, projeto encerrado"** — Sem monitoramento ativo na primeira semana, bugs de produção passam despercebidos — consultas lentas que só aparecem com volume real, integrações que falham intermitentemente, e-mails que caem em spam para certos provedores, e problemas de permissão que só aparecem com combinações de perfil que não foram testadas. A primeira semana pós-go-live é parte do projeto, não pós-projeto.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é portal web autenticado simples** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Os usuários vão assinar um plano e pagar mensalmente" | SaaS com billing, não portal simples | Reclassificar para saas |
| "Vendedores e compradores negociam entre si na plataforma" | Marketplace com transações entre usuários | Reclassificar para marketplace |
| "Precisa processar milhares de transações por segundo com consistência" | Sistema transacional de alta performance | Reclassificar para sistema distribuído |
| "Cada empresa-cliente tem seus próprios usuários e dados isolados" | Multi-tenancy complexa — SaaS B2B | Reclassificar para saas |
| "O portal precisa controlar dispositivos IoT em tempo real" | Sistema IoT com frontend, não portal web | Reclassificar para plataforma IoT |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos quantos usuários vai ter" | 01 | Arquitetura dimensionada no escuro — pode cair no primeiro dia ou custar 10x o necessário | Definir volume estimado com range (mínimo, esperado, pico) antes de avançar |
| "O sistema legado não tem API, só tem o banco" | 02 | Integração via acesso direto ao banco é frágil e insegura — qualquer mudança no legado quebra o portal | Avaliar construção de API wrapper sobre o legado ou reclassificar o esforço de integração |
| "Não sabemos quem vai aprovar a migração de dados" | 04 | Migração de dados bloqueada por falta de autoridade — portal lançado sem dados é inútil | Definir responsável pela aprovação da migração antes de avançar |
| "O time de segurança do cliente não respondeu sobre o SSO" | 06 | Integração com IdP corporativo bloqueada — cadastro e login ficam indefinidos | Escalar para o patrocinador do projeto e obter timeline do time de segurança |
| "Não temos ambiente de sandbox do ERP para testes" | 06 | Integração só pode ser testada em produção — risco de corrupção de dados | Exigir sandbox ou documentar formalmente o risco e obter aceite do cliente |
| "O prazo é fixo mas o escopo ainda está sendo definido" | 01 | Prazo sem escopo é receita para fracasso — o escopo vai crescer até não caber no prazo | Fixar escopo antes de fixar prazo, ou aceitar MVP mínimo para o prazo dado |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "As aprovações passam pela TI, segurança e diretoria" | 03 | Cadeia de aprovação lenta — cada decisão técnica leva semanas | Documentar SLA de aprovação com prazo máximo por nível |
| "O sistema legado é de um fornecedor que não coopera" | 02 | Integração bloqueada por falta de documentação ou suporte do fornecedor | Mapear alternativas (screen scraping, acesso ao banco, API reversa) e estimar custo de cada uma |
| "O time de TI do cliente nunca usou cloud" | 05 | Operação pós-lançamento será problemática — time não sabe operar a infraestrutura | Planejar treinamento de operação ou incluir operação gerenciada no contrato |
| "A empresa está passando por reestruturação" | 01 | Patrocinador pode mudar, prioridades podem mudar, projeto pode ser cancelado | Obter comprometimento formal por escrito com escopo e prazo |
| "Performance não é tão importante, são poucos usuários" | 05 | "Poucos usuários" hoje pode ser "muitos" amanhã sem aviso — portal lento gera abandono | Implementar baseline de performance desde o início — é mais barato que otimizar depois |
| "Podemos usar meu Gmail pessoal para enviar os e-mails" | 05 | E-mail transacional via conta pessoal viola compliance, não escala, e será bloqueado | Configurar provedor profissional de e-mail transacional obrigatoriamente |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Problema de negócio que o portal resolve identificado com clareza (pergunta 1)
- Volume estimado de usuários e padrão de uso definido (perguntas 2 e 5)
- Modelo de autenticação decidido (próprio, social, SSO corporativo) (pergunta 4)
- Requisitos de conformidade regulatória identificados (pergunta 6)
- Orçamento de desenvolvimento e operação aprovado (pergunta 8)

### Etapa 02 → 03

- Jornadas de usuário por perfil mapeadas (pergunta 1)
- Requisitos de segurança de autenticação detalhados (pergunta 2)
- Integrações externas mapeadas com nível de documentação avaliado (pergunta 4)
- Modelo de permissões definido (RBAC ou ABAC) (pergunta 5)
- Fronteira do portal validada — sem requisitos que reclassifiquem o projeto (perguntas 8 e 15)

### Etapa 03 → 04

- Solução de autenticação escolhida e justificada (pergunta 1)
- Arquitetura de backend decidida (pergunta 2)
- Design cobrindo estados de autenticação e empty states (perguntas 3 e 4)
- Estratégia de testes definida (pergunta 5)
- SLA de operação pós-lançamento definido (pergunta 6)

### Etapa 04 → 05

- Modelo de dados completo com entidades, atributos e relacionamentos (pergunta 1)
- Contratos de API especificados em formato padronizado (pergunta 2)
- Wireframes/protótipos dos fluxos críticos testados e aprovados (pergunta 3)
- Regras de negócio documentadas com exemplos (pergunta 5)
- Plano de migração de dados especificado (pergunta 6, se aplicável)
- Documentação revisada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- Arquitetura de aplicação definida e justificada (pergunta 1)
- Banco de dados e estratégia de migração de schema definidos (pergunta 2)
- Implementação técnica de autenticação detalhada (pergunta 3)
- Stack de observabilidade definida com thresholds de alerta (pergunta 7)
- Custos mensais de infraestrutura calculados e aprovados (pergunta 11)
- Pipeline de CI/CD desenhado (pergunta 13)

### Etapa 06 → 07

- Repositório configurado com estrutura de pastas e .env.example documentado (perguntas 1 e 9)
- Banco de dados provisionado nos três ambientes com schema aplicado (pergunta 2)
- Autenticação configurada e fluxo completo funcional (pergunta 5)
- E-mail transacional configurado com SPF/DKIM/DMARC e deliverability validada (pergunta 7)
- Pipeline de CI/CD testado com PR real (pergunta 15)

### Etapa 07 → 08

- Fluxos de autenticação completos implementados e testados (pergunta 1)
- APIs implementadas com validação, tratamento de erros e testes de contrato (pergunta 4)
- Integrações externas com circuit breaker e fallback funcionais (pergunta 5)
- Migração de dados executada em staging com sucesso (pergunta 6, se aplicável)
- Testes E2E dos fluxos críticos passando no CI (pergunta 11)

### Etapa 08 → 09

- Fluxos de autenticação testados com cenários de ataque (IDOR, escalação de privilégio) (pergunta 1)
- Teste de carga executado simulando cenário de pico (pergunta 3)
- Verificação de segurança OWASP Top 10 executada (pergunta 4)
- Smoke test automatizado integrado ao CI/CD (pergunta 7)
- E-mails chegando no inbox nos principais provedores (pergunta 8)

### Etapa 09 → 10

- Plano de migração de dados em produção documentado com rollback (pergunta 1, se aplicável)
- Comunicação aos usuários preparada e agendada (pergunta 2)
- Monitoramento e alertas ativos e testados (pergunta 3)
- Treinamento de operadores realizado e documentação entregue (pergunta 4)
- Plano de rollback documentado com critérios e responsável (pergunta 5)
- Artefatos de compliance publicados (pergunta 6)

### Etapa 10 → Encerramento

- Migração de dados em produção validada (pergunta 1, se aplicável)
- Smoke test completo executado em produção (pergunta 2)
- Taxa de erro de API aceitável nas primeiras horas (pergunta 4)
- Comunicação de lançamento enviada (pergunta 6)
- Acessos entregues e aceite formal obtido (perguntas 12 e 13)
- Documentação técnica de operação entregue (pergunta 15)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de portal web autenticado. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Conteúdo Restrito | V2 Autoatendimento | V3 Colaborativo | V4 Backoffice | V5 Multi-perfil |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 2 | 2 | 3 |
| 02 Discovery | 2 | 4 | 3 | 3 | 4 |
| 03 Alignment | 2 | 3 | 3 | 2 | 3 |
| 04 Definition | 2 | 4 | 4 | 4 | 5 |
| 05 Architecture | 2 | 4 | 3 | 3 | 4 |
| 06 Setup | 2 | 3 | 3 | 2 | 3 |
| 07 Build | 3 | 5 | 4 | 5 | 5 |
| 08 QA | 2 | 4 | 3 | 3 | 4 |
| 09 Launch Prep | 2 | 4 | 2 | 2 | 4 |
| 10 Go-Live | 2 | 3 | 2 | 2 | 3 |
| **Total relativo** | **21** | **37** | **29** | **28** | **38** |

**Observações por variante:**

- **V1 Conteúdo Restrito**: Esforço mais leve entre as variantes. A complexidade está na autenticação e no controle de acesso — o conteúdo em si é simples. O gargalo oculto é a produção e organização do conteúdo restrito, que frequentemente não está pronto quando o portal está.
- **V2 Autoatendimento**: O mais pesado em Discovery e Architecture por causa das integrações com sistemas legados. O esforço de integração frequentemente é 40-60% do esforço total do projeto. Launch Prep é pesado por causa da migração de dados e comunicação aos usuários existentes.
- **V3 Colaborativo**: Build é pesado por causa dos fluxos de interação entre usuários (comentários, notificações, moderação). A complexidade não está na autenticação, mas na dinâmica social e nos edge cases de conteúdo gerado pelo usuário (spam, abuso, conteúdo ofensivo).
- **V4 Backoffice**: Build é o mais pesado — cada entidade exige CRUD completo com listagem, filtros, paginação, ordenação, edição e exclusão. Frameworks admin (Refine, AdminJS) podem reduzir o esforço de 5 para 3 se o design aceitar padrões do framework.
- **V5 Multi-perfil**: O mais pesado total. Definition é 5 porque cada perfil tem seu modelo de dados, regras de negócio e fluxos distintos. Build é 5 porque cada perfil tem suas telas e jornadas. Launch Prep é pesado porque a migração de dados e comunicação precisam considerar cada perfil separadamente.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sem sistema legado a substituir (Etapa 01, pergunta 3) | Etapa 02: pergunta 14 (qualidade dos dados do legado). Etapa 04: pergunta 6 (plano de migração), pergunta 12 (volume de migração). Etapa 07: perguntas 6 e 7 (migração e rehash de senhas). Etapa 09: perguntas 1 e 2 (migração em produção, comunicação de transição). Etapa 10: pergunta 1 (execução de migração). |
| Autenticação própria sem SSO corporativo (Etapa 01, pergunta 4) | Etapa 05: pergunta 4 (integração com IdP). Etapa 06: pergunta 6 (setup de SSO). |
| Perfil único de usuário (Etapa 01, pergunta 12) | Etapa 02: pergunta 5 (modelo RBAC/ABAC se torna trivial). Etapa 04: pergunta 9 (matriz de permissões simplificada). Etapa 07: pergunta 2 (proteção de rotas simplificada). |
| Sem integrações com sistemas externos (Etapa 01, pergunta 10) | Etapa 02: perguntas 4 e 14 (mapeamento e qualidade de APIs). Etapa 05: pergunta 8 (tratamento de erros de integração). Etapa 07: pergunta 5 (circuit breaker). Etapa 08: pergunta 2 (testes de integração em falha). |
| Portal sem geração de documentos (Etapa 02, pergunta 10) | Etapa 07: perguntas relacionadas a pipeline de geração de PDF/certificados são eliminadas. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| SSO corporativo confirmado (Etapa 01, pergunta 4) | Etapa 05: pergunta 4 (detalhamento de integração com IdP) se torna bloqueadora. Etapa 06: pergunta 6 (setup de SSO com time de TI do cliente) se torna gate — lead time frequentemente de semanas. |
| Portal substitui sistema legado com base de usuários (Etapa 01, pergunta 3) | Etapa 02: pergunta 14 (qualidade dos dados) se torna crítica. Etapa 04: pergunta 6 (plano de migração) se torna gate. Etapa 07: perguntas 6 e 7 (execução de migração e rehash) se tornam críticas. Etapa 09: perguntas 1 e 2 (migração em produção e comunicação) se tornam gates. |
| Requisitos de LGPD/GDPR identificados (Etapa 01, pergunta 6) | Etapa 02: pergunta 13 (consentimento granular, portabilidade, direito ao esquecimento) se torna obrigatória. Etapa 04: pergunta 13 (requisitos de auditoria) se torna obrigatória. Etapa 09: pergunta 6 (política de privacidade e termos de uso) se torna gate. |
| Múltiplos perfis de usuário confirmados (Etapa 01, pergunta 12) | Etapa 02: pergunta 5 (modelo RBAC/ABAC) se torna crítica. Etapa 04: perguntas 4 e 9 (mapa de telas por perfil, matriz de permissões) se tornam bloqueadoras. Etapa 07: pergunta 2 (middleware de autorização) se torna crítico. Etapa 08: pergunta 1 (testes de autorização por perfil) se torna obrigatório. |
| Integrações com sistemas legados sem sandbox (Etapa 06, pergunta 12) | Etapa 07: pergunta 5 (integrações) se torna de alto risco — testes só em produção. Etapa 08: pergunta 2 (testes de integração) se torna limitado — documentar gap de teste e obter aceite do risco. Etapa 09: pergunta 5 (plano de rollback) deve considerar falha de integração como cenário prioritário. |
| Pico de uso concentrado identificado (Etapa 01, pergunta 5) | Etapa 05: perguntas 6 e 11 (cache e custos de infra em cenário de pico) se tornam críticas. Etapa 08: pergunta 3 (teste de carga com simulação do pico) se torna gate — não pode ir a produção sem validar que o portal aguenta o pico. |
