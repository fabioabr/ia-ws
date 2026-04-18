---
title: "SaaS Interno / Ferramenta Corporativa — Blueprint"
description: "Sistema digital para uso interno da empresa. Usuários são colaboradores, não clientes. Foco em produtividade operacional, integração com sistemas legados e controle de acesso por papel."
category: project-blueprint
type: internal-saas
status: rascunho
created: 2026-04-13
---

# SaaS Interno / Ferramenta Corporativa

## Descrição

Sistema digital para uso interno da empresa. Usuários são colaboradores, não clientes. Foco em produtividade operacional, integração com sistemas legados e controle de acesso por papel.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda ferramenta interna é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Painel Administrativo / Backoffice

Interface web para que operadores internos gerenciem entidades de negócio — cadastros, pedidos, tickets, contratos. CRUD centralizado com filtros, busca e exportação. Sem lógica de workflow complexa — o fluxo é linear (criar, editar, visualizar, inativar). Controle de acesso básico por papel (admin, operador, visualizador). Tipicamente substitui planilhas Excel ou processos manuais em e-mail. Exemplos: painel de gestão de clientes, sistema de controle de patrimônio, cadastro de fornecedores.

### V2 — Ferramenta de Workflow / Aprovação

Sistema com fluxo de estados definido — solicitação → análise → aprovação → execução → conclusão. Múltiplos atores participam em etapas diferentes com permissões distintas. Regras de negócio governam transições (quem pode aprovar, limites de alçada, SLA por etapa). Notificações e escalações são críticas para evitar gargalos. A complexidade principal está na modelagem do workflow e nas regras de transição, não na interface. Exemplos: sistema de aprovação de despesas, fluxo de solicitação de compras, gestão de chamados internos de TI, onboarding de colaboradores.

### V3 — Dashboard / BI Operacional

Painel de indicadores e relatórios para acompanhamento de métricas operacionais em tempo real ou near-real-time. Consome dados de múltiplas fontes (ERP, CRM, planilhas, APIs internas) e apresenta em visualizações consolidadas (gráficos, tabelas, KPIs). Pouca ou nenhuma entrada de dados pelo usuário — o foco é leitura e análise. A complexidade está na integração com fontes de dados, na transformação/agregação e na atualização periódica. Exemplos: dashboard de vendas diárias, painel de SLA de atendimento, monitor de disponibilidade de sistemas, relatório operacional para diretoria.

### V4 — Portal de Autoatendimento Interno

Plataforma onde colaboradores resolvem suas próprias demandas sem acionar outro departamento — consulta de holerite, solicitação de férias, reserva de sala, atualização cadastral, abertura de ticket de TI. O foco é reduzir a carga operacional de áreas de suporte (RH, TI, Facilities) transferindo ações simples para o próprio colaborador. Integração com sistemas de RH (TOTVS, SAP, Workday) e Active Directory/SSO é quase sempre necessária. Exemplos: portal do colaborador, intranet de autoatendimento, portal de benefícios.

### V5 — Sistema Legado Modernizado

Substituição de sistema interno existente (geralmente desktop, Access, Delphi, VB6, ou planilha Excel complexa) por versão web moderna. O desafio principal não é técnico — é mapear com fidelidade todas as regras de negócio implícitas acumuladas ao longo de anos no sistema antigo, muitas das quais não estão documentadas e vivem apenas na memória dos operadores. Migração de dados históricos é quase sempre obrigatória. Exemplos: migração de ERP customizado em Access para web, modernização de sistema de controle de estoque em Delphi, substituição de planilha de controle financeiro com macros VBA.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend | Banco de Dados | Autenticação | Observações |
|---|---|---|---|---|---|
| V1 — Backoffice | React + Refine ou Retool | Node.js (NestJS) ou .NET | PostgreSQL | Keycloak ou Auth0 | Refine acelera CRUDs. Retool se time é pequeno e prazo curto. |
| V2 — Workflow | React + componente de state machine | Node.js (NestJS) ou Java (Spring) | PostgreSQL + Redis | Keycloak com RBAC granular | XState ou Temporal para orquestração de workflow. Redis para filas e cache de estado. |
| V3 — Dashboard/BI | React + Tremor ou Recharts | Node.js ou Python (FastAPI) | PostgreSQL + ClickHouse ou BigQuery | SSO corporativo | ClickHouse para queries analíticas pesadas. Metabase como alternativa low-code. |
| V4 — Autoatendimento | React ou Next.js | Node.js (NestJS) | PostgreSQL | SSO/SAML + AD integration | Integração com APIs de RH é o gargalo principal. Mobile-responsive obrigatório. |
| V5 — Legado Modernizado | React ou Angular (conforme time) | .NET ou Java (conforme legado) | PostgreSQL + migração de dados | Manter autenticação existente ou migrar para Keycloak | Priorizar paridade funcional. Migração de dados é projeto paralelo. |

---

## Etapa 01 — Inception

- **Dor operacional como gatilho**: Ferramentas internas nascem de dor operacional concreta — processos manuais que consomem horas, planilhas que não escalam, erros humanos em tarefas repetitivas, ou falta de visibilidade sobre operações críticas. Entender a dor real (e não apenas o pedido do stakeholder) é fundamental porque a solução pode ser radicalmente diferente do que foi pedido. Um pedido de "sistema de controle de estoque" pode esconder uma dor de "não sabemos quanto tempo leva para repor um item" — que se resolve com um dashboard, não com um CRUD de estoque.

- **Sponsor vs. usuários reais**: O patrocinador do projeto costuma ser o diretor ou gerente da área que sente a dor, mas os usuários diários são operadores de nível mais baixo na hierarquia — analistas, assistentes, estagiários. Esses dois grupos têm expectativas diferentes: o sponsor quer relatórios e visibilidade, o operador quer velocidade e simplicidade. Se o discovery ouvir apenas o sponsor, o sistema vai ser bonito para apresentar em reunião de diretoria mas doloroso de usar 8 horas por dia. Mapear ambos os perfis desde a Inception é obrigatório.

- **Processo atual como referência inescapável**: Todo sistema interno substitui algum processo existente — mesmo que seja "ninguém faz isso hoje e por isso dá problema". Mapear o processo atual (as-is) com suas gambiarras, exceções e workarounds é pré-requisito para desenhar o processo futuro (to-be). Sem esse mapeamento, o time de desenvolvimento vai implementar o processo idealizado pelo sponsor, que não contempla as 15 exceções que o operador enfrenta diariamente e que tornam o sistema inutilizável na prática.

- **Integração com ecossistema corporativo**: Sistemas internos raramente existem isolados. Eles consomem dados de ERPs (SAP, TOTVS, Oracle), autenticam via Active Directory ou LDAP, enviam notificações por e-mail corporativo (Exchange, Google Workspace), e frequentemente precisam exportar dados para outros sistemas. A lista de integrações obrigatórias precisa ser levantada na Inception porque cada integração adiciona complexidade, dependência de time externo (TI corporativa), e risco de bloqueio se a API não existir ou não estiver documentada.

- **Compliance e segurança interna**: Ferramentas internas frequentemente manipulam dados sensíveis — folha de pagamento, dados pessoais de colaboradores (LGPD), informações financeiras (SOX), dados de clientes. Os requisitos de segurança (criptografia, auditoria de acessos, logs de alteração) e compliance (quem pode ver o quê, retenção de dados, trilha de auditoria) precisam ser identificados na Inception porque impactam a arquitetura de forma irreversível — adicionar trilha de auditoria em um sistema já em produção é ordens de magnitude mais caro do que prever desde o início.

- **Expectativa de adoção e change management**: Ferramentas internas têm um desafio que produtos externos não têm: os usuários são obrigados a usar. Mas "obrigados" não significa "engajados". Se o sistema novo é mais lento ou complexo que o processo manual anterior (planilha + e-mail), os operadores vão resistir, encontrar workarounds, e o sistema vai ser subutilizado. A estratégia de adoção (treinamento, migração gradual, período de convivência com sistema antigo) precisa ser discutida desde a Inception para estar refletida no cronograma.

### Perguntas

1. Qual é a dor operacional concreta que este sistema resolve — qual processo manual, planilha ou gargalo será substituído? [fonte: Gerente da área, Operadores] [impacto: PM, Dev, Arquiteto]
2. Quem é o patrocinador formal do projeto e quem são os usuários que vão operar o sistema diariamente (nome, cargo, volume de uso)? [fonte: Diretoria, RH, Gerência operacional] [impacto: PM, Designer, Dev]
3. Quantos usuários simultâneos são esperados e qual o horário de pico de uso (horário comercial, 24/7, turnos)? [fonte: Gerência operacional, TI] [impacto: Arquiteto, Dev, DevOps]
4. O sistema substitui algum processo ou ferramenta existente? Se sim, qual e há quanto tempo está em uso? [fonte: Gerência operacional, Operadores] [impacto: PM, Dev, Analista de negócios]
5. O processo atual (as-is) está documentado formalmente ou existe apenas na prática dos operadores? [fonte: Gerência operacional, Qualidade/Processos] [impacto: Analista de negócios, PM]
6. Quais sistemas internos existentes precisam ser integrados (ERP, CRM, AD, e-mail, BI)? [fonte: TI, Gerência operacional] [impacto: Arquiteto, Dev, DevOps]
7. Como os usuários se autenticam hoje nos sistemas corporativos — Active Directory, LDAP, Google Workspace, SSO? [fonte: TI, Segurança da informação] [impacto: Arquiteto, Dev]
8. Existem requisitos de compliance que afetam este sistema — LGPD, SOX, auditoria interna, política de retenção de dados? [fonte: Jurídico, Compliance, DPO] [impacto: Arquiteto, Dev, Segurança]
9. Qual é o orçamento total aprovado e existe verba separada para operação mensal (infra, licenças, suporte)? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
10. Qual é o prazo esperado e existe algum driver de negócio externo (auditoria, regulamentação, fusão, safra)? [fonte: Diretoria, Compliance] [impacto: PM, Dev]
11. O time de TI corporativo vai participar ativamente (infra, integrações, deploy) ou o projeto é autônomo? [fonte: TI, Diretoria] [impacto: DevOps, Arquiteto, PM]
12. Existe estratégia de adoção planejada — big bang (todos migram no mesmo dia) ou migração gradual por área/time? [fonte: Diretoria, RH, Gerência operacional] [impacto: PM, Dev]
13. O sistema precisa funcionar em dispositivos móveis (tablets no chão de fábrica, celular em campo)? [fonte: Gerência operacional, Operadores] [impacto: Designer, Dev]
14. Há dados históricos que precisam ser migrados do sistema ou processo atual para o novo sistema? [fonte: TI, Gerência operacional] [impacto: Dev, DBA, PM]
15. Quem é o ponto focal de TI corporativa para questões de infraestrutura, rede, firewall e liberação de acessos? [fonte: TI] [impacto: DevOps, Arquiteto, PM]

---

## Etapa 02 — Discovery

- **Mapeamento do processo as-is**: Documentar o processo atual passo a passo — não o processo idealizado que o gerente descreve na reunião, mas o processo real que os operadores executam no dia a dia, incluindo gambiarras, exceções e workarounds que existem porque o sistema atual (ou a planilha) não resolve todos os casos. O mapeamento deve ser feito com observação direta (shadowing do operador) ou entrevista detalhada com quem executa, não apenas com quem gerencia. Cada exceção não mapeada aqui vai virar um bug report no futuro — "o sistema não deixa fazer X, mas a gente sempre fez X".

- **Volumetria e padrões de uso**: Levantar números concretos — quantos registros são criados por dia, quantos usuários acessam simultaneamente no pico, qual o volume de dados históricos (em registros e GB), qual a frequência de consulta vs. escrita. Esses números definem decisões de arquitetura: 10 usuários com 1000 registros é radicalmente diferente de 500 usuários com 10 milhões de registros, mesmo que o processo de negócio seja idêntico. Estimar sem volumetria é chutar — e chutes em infra resultam em sistema lento ou em custo desnecessário.

- **Papéis e permissões**: Mapear todos os papéis que interagem com o sistema e o que cada um pode fazer — visualizar, criar, editar, aprovar, excluir, exportar. Em ferramentas internas, o controle de acesso não é apenas funcional (o que pode fazer) mas frequentemente também de dados (o que pode ver) — um gerente regional vê apenas os dados da sua região, um diretor vê tudo. RBAC (Role-Based Access Control) é o mínimo, mas muitos cenários exigem ABAC (Attribute-Based Access Control) ou row-level security. Se essa complexidade não for mapeada aqui, a implementação vai ser genérica ("todo mundo vê tudo") e depois precisará ser retrofitada com controle granular — o que é custoso e propenso a erros.

- **Requisitos de auditoria e rastreabilidade**: Identificar se o sistema precisa manter registro de quem fez o quê e quando — log de alterações, trilha de auditoria, versionamento de registros. Em ambientes regulados (financeiro, saúde, governo), a trilha de auditoria é obrigatória por lei ou norma interna. Mesmo em ambientes não regulados, é comum que a diretoria peça "quem aprovou essa despesa?" meses depois. A decisão de implementar audit logging afeta o design do banco de dados desde o início — adicionar depois significa alterar cada tabela e cada endpoint.

- **Integrações detalhadas**: Para cada integração identificada na Inception, detalhar: qual a direção (leitura, escrita, bidirecional), qual o protocolo (REST API, SOAP, arquivo CSV/SFTP, webhook, banco direto), qual a frequência (tempo real, batch diário, sob demanda), quem é o dono técnico da API ou sistema de origem, e se existe documentação. Integrações com sistemas legados corporativos (SAP, TOTVS, Oracle) frequentemente exigem middleware ou ETL porque as APIs são limitadas, mal documentadas ou inexistentes — e o time de TI que mantém esses sistemas tem prioridades próprias e SLA lento.

- **Requisitos offline e de rede**: Em ambientes corporativos, nem sempre a rede é confiável — chão de fábrica, campo, filiais remotas. Se o sistema precisa funcionar com conectividade intermitente, isso muda fundamentalmente a arquitetura: sync offline, conflict resolution, e cache local em Service Worker ou banco embarcado (IndexedDB, SQLite via WASM). Essa decisão afeta tudo — da escolha do framework frontend à modelagem do backend — e não pode ser descoberta na fase de build.

### Perguntas

1. O processo atual (as-is) foi mapeado com observação direta dos operadores, incluindo exceções e workarounds? [fonte: Gerência operacional, Operadores, Qualidade] [impacto: Analista de negócios, PM, Dev]
2. Quantos registros são criados/editados por dia, qual o volume de dados históricos, e quantos usuários simultâneos no pico? [fonte: TI, Gerência operacional] [impacto: Arquiteto, Dev, DBA]
3. Quais são todos os papéis de usuário e o que cada um pode ver, criar, editar, aprovar e excluir? [fonte: Gerência operacional, RH, Segurança] [impacto: Arquiteto, Dev]
4. O controle de acesso é apenas funcional (o que pode fazer) ou também de dados (o que pode ver por região/área/nível)? [fonte: Gerência operacional, Segurança, Compliance] [impacto: Arquiteto, Dev, DBA]
5. Existe obrigatoriedade de trilha de auditoria — registrar quem alterou o quê e quando? [fonte: Compliance, Auditoria interna, Jurídico] [impacto: Arquiteto, Dev, DBA]
6. Para cada integração mapeada: qual a direção, protocolo, frequência, dono técnico e existência de documentação? [fonte: TI, Fornecedores de sistema] [impacto: Dev, Arquiteto]
7. As APIs dos sistemas legados a integrar estão disponíveis, documentadas e têm ambiente de teste? [fonte: TI, Fornecedores de ERP/CRM] [impacto: Dev, Arquiteto, PM]
8. O sistema precisa funcionar com conectividade intermitente ou offline (fábrica, campo, filial remota)? [fonte: Gerência operacional, TI] [impacto: Arquiteto, Dev]
9. Quais relatórios e exportações são obrigatórios no MVP (PDF, Excel, CSV, dashboards)? [fonte: Gerência operacional, Diretoria] [impacto: Dev, Designer]
10. Existem regras de negócio implícitas que não estão documentadas e vivem apenas na experiência dos operadores? [fonte: Operadores seniores, Gerência operacional] [impacto: Analista de negócios, Dev]
11. Qual é o nível de maturidade digital dos usuários finais — conseguem navegar em sistemas web ou precisam de interface simplificada? [fonte: RH, Gerência operacional] [impacto: Designer, Dev]
12. O sistema precisa enviar notificações (e-mail, push, SMS) e, se sim, quais eventos disparam cada notificação? [fonte: Gerência operacional] [impacto: Dev, Arquiteto]
13. Há requisitos de disponibilidade (SLA de uptime) — o sistema precisa funcionar 24/7 ou apenas em horário comercial? [fonte: TI, Diretoria] [impacto: DevOps, Arquiteto]
14. Existem requisitos de retenção de dados — por quanto tempo os dados devem ser mantidos e quando podem ser expurgados? [fonte: Jurídico, Compliance, Auditoria] [impacto: DBA, Arquiteto]
15. Quais KPIs ou métricas o sponsor espera extrair do sistema para justificar o investimento (ROI do projeto)? [fonte: Diretoria, Financeiro] [impacto: PM, Dev, Analista de negócios]

---

## Etapa 03 — Alignment

- **Processo to-be validado com operadores**: O processo futuro (to-be) não pode ser definido apenas pelo gerente em sala de reunião. Precisa ser validado com os operadores que vão executá-lo diariamente — eles são os únicos que sabem se as exceções do processo as-is foram contempladas, se o fluxo proposto é mais rápido ou mais lento que o atual, e se alguma etapa crítica foi inadvertidamente removida. Validação significa mostrar o fluxo desenhado, caminhar passo a passo, e perguntar "e quando acontece X, como fica?". Sem essa validação, o risco de rejeição na adoção é altíssimo.

- **Decisão build vs. buy vs. low-code**: Ferramentas internas têm alternativas que produtos externos não têm — plataformas low-code (Retool, Appsmith, Budibase), ERPs configuráveis (módulos do SAP, TOTVS), e até automações em Power Automate ou Zapier. A decisão de construir do zero deve ter justificativa documentada — geralmente a justificativa é: as regras de negócio são tão específicas que nenhuma ferramenta pronta resolve sem customização excessiva, ou o volume de uso justifica investimento em UX otimizada para velocidade. Se a justificativa for fraca, considerar seriamente low-code — entrega mais rápida e manutenção mais barata para ferramentas internas com vida útil incerta.

- **Formato de entrega e escopo do MVP**: Alinhar explicitamente o que entra e o que fica fora do MVP. Em ferramentas internas, o escopo tende a inflar porque cada operador pede "só mais esse campo" ou "só mais esse relatório". O critério para MVP deve ser: quais funcionalidades são necessárias para que o processo to-be funcione end-to-end, sem workarounds manuais? Tudo que é "nice-to-have" vai para backlog de versões futuras. Sem esse corte claro, o projeto vira uma esteira infinita de "só mais uma coisa".

- **SLA e modelo de suporte pós-lançamento**: Ferramentas internas precisam de suporte contínuo — bugs, dúvidas de operadores, ajustes de regra de negócio, criação de novos usuários. Definir antes do go-live: quem é o ponto focal de suporte (N1 — time interno? N2 — dev?), qual o SLA de resposta para bugs críticos (sistema fora do ar) vs. melhorias, e como solicitações de mudança são priorizadas. Sem esse acordo, o time de desenvolvimento vira suporte perpétuo sem planejamento, e features novas nunca são entregues.

- **Estratégia de testes com dados reais**: Em ferramentas internas, testes com dados fictícios raramente revelam os problemas reais. Dados de produção têm inconsistências acumuladas ao longo de anos — CPFs inválidos, nomes com caracteres especiais, registros com campos obrigatórios vazios, datas em formato errado. A estratégia de teste deve prever: acesso a um snapshot anonimizado dos dados reais para QA, definição de quem do lado do cliente vai validar os cenários de negócio (UAT), e tempo no cronograma para os operadores testarem com casos que eles conhecem e o dev não.

### Perguntas

1. O processo to-be foi validado com os operadores reais (não apenas com a gerência) e as exceções foram contempladas? [fonte: Operadores, Gerência operacional] [impacto: Analista de negócios, Dev, PM]
2. A decisão entre build customizado, low-code ou plataforma pronta foi avaliada com critérios documentados? [fonte: TI, Diretoria, Financeiro] [impacto: Arquiteto, PM, Dev]
3. O escopo do MVP foi definido com critério claro de corte — o que entra e o que fica para versões futuras? [fonte: Gerência operacional, Diretoria] [impacto: PM, Dev]
4. O fluxo de autenticação foi alinhado com TI corporativa — SSO, AD, LDAP ou autenticação própria? [fonte: TI, Segurança da informação] [impacto: Arquiteto, Dev]
5. Os papéis e permissões foram formalizados em uma matriz de acesso (RACI ou similar) aprovada pelo sponsor? [fonte: Gerência operacional, Segurança, RH] [impacto: Dev, Arquiteto]
6. O modelo de suporte pós-lançamento foi definido — N1, N2, SLA, canal de comunicação e responsáveis? [fonte: Diretoria, TI, Gerência operacional] [impacto: PM, Dev]
7. O cliente entende e aceita o conceito de MVP — funcionalidades fora do escopo serão entregues em versões posteriores? [fonte: Diretoria, Gerência operacional] [impacto: PM]
8. A estratégia de testes com dados reais (anonimizados) foi acordada e o acesso aos dados foi viabilizado com TI? [fonte: TI, DPO, Gerência operacional] [impacto: Dev, QA, DBA]
9. O time de TI corporativa confirmou disponibilidade para liberar acessos, APIs e ambientes no prazo necessário? [fonte: TI] [impacto: DevOps, Arquiteto, PM]
10. A cadeia de aprovação de mudanças de escopo durante o projeto foi definida (quem aprova, em quanto tempo)? [fonte: Diretoria] [impacto: PM]
11. O período de convivência entre sistema antigo e novo foi definido (paralelo, migração gradual, big bang)? [fonte: Gerência operacional, TI] [impacto: PM, Dev, DevOps]
12. Os operadores que farão UAT foram identificados por nome e têm tempo reservado na agenda para testar? [fonte: Gerência operacional, RH] [impacto: PM, QA]
13. A política de backup e disaster recovery foi alinhada com a criticidade do sistema? [fonte: TI, Diretoria] [impacto: DevOps, Arquiteto]
14. O formato de entrega de relatórios e exportações foi acordado (PDF formatado, Excel com fórmulas, CSV puro)? [fonte: Gerência operacional, Diretoria] [impacto: Dev]
15. O cronograma contempla tempo para treinamento dos operadores antes do go-live? [fonte: Diretoria, RH, Gerência operacional] [impacto: PM]

---

## Etapa 04 — Definition

- **Modelagem de entidades e relacionamentos**: Mapear todas as entidades de negócio (cliente, pedido, produto, colaborador, solicitação, aprovação) com seus atributos, tipos de dados, obrigatoriedades e relacionamentos. Este modelo é a fundação do banco de dados e da API — erros aqui se propagam para todo o sistema. Atenção especial a: campos que parecem simples mas têm regras complexas (ex.: "status" que tem 12 valores possíveis com transições específicas), campos que são calculados (ex.: "valor total" = soma dos itens), e campos que vêm de integração (ex.: "nome do colaborador" vem do AD, não é editável no sistema).

- **Wireframes de fluxo completo**: Produzir wireframes que cubram o fluxo end-to-end do processo to-be — desde o login até a conclusão da tarefa principal, passando por todas as telas intermediárias, estados de erro, estados vazios (lista sem resultados, dashboard sem dados), e caminhos alternativos (aprovação negada, timeout de sessão, dados inconsistentes). Wireframes de ferramenta interna precisam focar em eficiência, não em beleza — o operador vai usar 8 horas por dia e precisa de atalhos, tab order lógico, e ações frequentes acessíveis em poucos cliques.

- **Regras de negócio documentadas**: Cada regra de negócio deve ser documentada com: condição de disparo, ação executada, exceções, e origem (quem definiu e por quê). Regras implícitas ("ah, mas quando o valor é acima de R$ 10.000 precisa de aprovação do diretor") devem ser formalizadas. A documentação de regras é o contrato entre o time de negócio e o time técnico — regras não documentadas não serão implementadas, e regras ambíguas serão implementadas conforme a interpretação do dev, que pode não ser a correta.

- **Especificação de integrações**: Para cada integração, produzir documento técnico com: endpoint ou mecanismo de acesso, formato dos dados (JSON, XML, CSV), mapeamento campo a campo (campo do sistema origem → campo do sistema interno), tratamento de erros (sistema de origem indisponível, dados inválidos, timeout), e estratégia de retry. Integrações com sistemas legados frequentemente exigem transformação de dados — formatos de data diferentes, encoding de caracteres, campos opcionais em um sistema que são obrigatórios no outro. Cada diferença precisa de tratamento explícito.

- **Plano de migração de dados**: Se há dados históricos a migrar, especificar: quais tabelas/entidades serão migradas, qual o volume (número de registros, tamanho em GB), qual o mapeamento de campos (campo antigo → campo novo), como tratar dados inconsistentes ou incompletos (limpar antes, migrar e sinalizar, ou rejeitar), e qual o critério de validação pós-migração (contagem de registros, amostragem, validação de integridade referencial). Migração de dados subestimada é a causa número um de atrasos em projetos de substituição de sistema legado.

- **Matriz de notificações e alertas**: Documentar cada evento que dispara notificação — para quem, por qual canal (e-mail, push, SMS, in-app), com qual conteúdo, e com qual urgência. Em ferramentas de workflow, as notificações são críticas para manter o fluxo andando — uma aprovação pendente sem notificação vira gargalo invisível. Atenção ao volume: notificar demais cria fadiga e o usuário passa a ignorar; notificar de menos cria atrasos. O equilíbrio deve ser definido com os operadores, não com a gerência.

### Perguntas

1. O modelo de entidades e relacionamentos foi definido com atributos, tipos, obrigatoriedades e relações formalizados? [fonte: Analista de negócios, Gerência operacional] [impacto: Dev, DBA, Arquiteto]
2. Os wireframes cobrem o fluxo completo end-to-end — login, ações principais, estados de erro, estados vazios e caminhos alternativos? [fonte: Designer, Gerência operacional, Operadores] [impacto: Dev, Designer]
3. Todas as regras de negócio foram documentadas com condição, ação, exceção e origem? [fonte: Gerência operacional, Operadores seniores, Compliance] [impacto: Dev, QA]
4. A especificação de cada integração inclui endpoint, formato, mapeamento de campos, tratamento de erros e retry? [fonte: TI, Fornecedores de sistema] [impacto: Dev, Arquiteto]
5. O plano de migração de dados está especificado com volume, mapeamento, tratamento de inconsistências e critério de validação? [fonte: TI, DBA atual, Gerência operacional] [impacto: Dev, DBA, PM]
6. A matriz de notificações e alertas foi definida — qual evento, para quem, por qual canal, com qual conteúdo? [fonte: Gerência operacional, Operadores] [impacto: Dev]
7. Os campos calculados, derivados e de integração foram identificados e suas regras de cálculo documentadas? [fonte: Gerência operacional, Analista de negócios] [impacto: Dev, DBA]
8. O comportamento de cada transição de estado (workflow) foi especificado — quem pode executar, condições e reversibilidade? [fonte: Gerência operacional, Compliance] [impacto: Dev, Arquiteto]
9. Os requisitos de performance foram especificados — tempo máximo de resposta para listagens, buscas e relatórios? [fonte: Gerência operacional, TI] [impacto: Arquiteto, Dev, DBA]
10. Os limites de campos foram definidos (tamanho máximo de texto, formatos aceitos, ranges numéricos)? [fonte: Analista de negócios, Operadores] [impacto: Dev]
11. O fluxo de tratamento de erro no processo de negócio foi definido (dado inválido, sistema indisponível, conflito de edição)? [fonte: Gerência operacional] [impacto: Dev, Designer]
12. O escopo exato dos relatórios e dashboards do MVP foi especificado com campos, filtros e agrupamentos? [fonte: Gerência operacional, Diretoria] [impacto: Dev, Designer]
13. Os critérios de aceite de cada user story ou funcionalidade foram escritos de forma verificável? [fonte: PM, Analista de negócios] [impacto: Dev, QA]
14. A documentação de definição foi revisada e aprovada formalmente pelo sponsor e pelos operadores-chave? [fonte: Diretoria, Gerência operacional] [impacto: PM, Dev]
15. O cronograma do MVP foi re-estimado com base nas definições detalhadas e os riscos foram reavaliados? [fonte: PM, Dev] [impacto: PM, Diretoria]

---

## Etapa 05 — Architecture

- **Escolha do framework backend**: A seleção do framework backend deve considerar o perfil do time e a complexidade do domínio. NestJS (Node.js/TypeScript) é indicado quando o time full-stack trabalha com TypeScript e as regras de negócio são moderadas — oferece boa estrutura com decorators, módulos e dependency injection. Spring Boot (Java) ou .NET são indicados quando as regras de negócio são complexas, quando há integração pesada com ecossistema corporativo (SAP, Oracle), ou quando o time já domina essas stacks. FastAPI (Python) é indicado quando há componente forte de dados/BI ou quando o time vem de data science. A escolha errada aqui não trava o projeto, mas reduz a produtividade do time durante todo o ciclo.

- **Modelagem do banco de dados**: PostgreSQL é o padrão recomendado para ferramentas internas — relacional, maduro, com suporte nativo a JSON (para campos semi-estruturados), full-text search, e row-level security (para controle de acesso a dados por papel). A modelagem deve prever: tabelas de auditoria (se identificado no Discovery), soft delete (se registros não devem ser apagados permanentemente), versionamento de registros (se o histórico de alterações é obrigatório), e campos de metadados (created_at, updated_at, created_by, updated_by) em todas as entidades. Índices devem ser planejados com base nos padrões de consulta mapeados — não adicionados reativamente quando o sistema fica lento.

- **Estratégia de autenticação e autorização**: Em ambientes corporativos, autenticação nunca é "criar cadastro e login". O padrão é SSO (Single Sign-On) integrado com Active Directory via SAML 2.0 ou OIDC (OpenID Connect). Keycloak é a solução open-source mais completa para identity management — suporta AD federation, RBAC, e multiple realms. Se a empresa já tem Azure AD, a integração direta via MSAL simplifica. A autorização (quem pode fazer o quê) deve ser implementada tanto no frontend (esconder botões) quanto no backend (validar permissão em cada endpoint) — autorização apenas no frontend é uma falha de segurança trivial de explorar.

- **Arquitetura de integrações**: Definir a pattern de integração para cada sistema externo. Para integrações síncronas (consulta de CEP, validação de CPF), chamada direta via HTTP com circuit breaker e timeout. Para integrações assíncronas de alto volume (sincronização de dados com ERP, processamento de arquivos), fila de mensagens (RabbitMQ, SQS) com dead letter queue para tratamento de falhas. Para integrações batch (importação diária de planilha, exportação noturna para BI), jobs agendados com monitoramento de sucesso/falha. Cada pattern tem implicações diferentes de infra, custo e complexidade.

- **Infraestrutura e deploy**: Ferramentas internas podem rodar em cloud pública (AWS, Azure, GCP), cloud privada (on-premises), ou modelo híbrido. A decisão depende de: política de segurança da empresa (dados sensíveis podem sair do datacenter?), existência de infraestrutura interna (há Kubernetes rodando?), e custo. Para cloud, containers (Docker + ECS/EKS ou Cloud Run) são o padrão. Para on-premises, a complexidade de setup e manutenção é significativamente maior e precisa de time de infra dedicado. A escolha impacta o pipeline de CI/CD, o monitoramento e o modelo de operação — e frequentemente é ditada pela TI corporativa, não pelo time de desenvolvimento.

- **Estratégia de cache e performance**: Sistemas internos com muitos usuários simultâneos precisam de cache em múltiplas camadas — cache de query no banco (materialized views para relatórios pesados), cache de aplicação (Redis para sessões, dados de referência que mudam raramente), e cache de frontend (React Query ou SWR para evitar re-fetches desnecessários). A estratégia de invalidação de cache é tão importante quanto o cache em si — dados stale em ferramenta de workflow geram decisões baseadas em informação desatualizada, que é pior do que não ter cache.

### Perguntas

1. O framework backend escolhido é adequado ao perfil do time, à complexidade das regras de negócio e ao ecossistema corporativo? [fonte: TI, Dev] [impacto: Dev, Arquiteto]
2. O banco de dados foi modelado com tabelas de auditoria, soft delete, metadados e índices planejados por padrão de consulta? [fonte: DBA, Arquiteto] [impacto: Dev, DBA]
3. A estratégia de autenticação (SSO/AD/OIDC) e autorização (RBAC/ABAC) foi definida e validada com TI corporativa? [fonte: TI, Segurança da informação] [impacto: Arquiteto, Dev]
4. A pattern de integração para cada sistema externo foi definida (síncrona, fila, batch) com circuit breaker e retry? [fonte: Arquiteto, TI] [impacto: Dev]
5. A decisão entre cloud pública, privada ou on-premises foi tomada com base em política de segurança e custo? [fonte: TI, Segurança, Financeiro] [impacto: DevOps, Arquiteto]
6. O pipeline de CI/CD foi desenhado com ambientes separados (dev, staging, prod) e aprovação para deploy em produção? [fonte: TI, Dev] [impacto: DevOps, Dev]
7. A estratégia de cache (Redis, materialized views, frontend cache) foi definida com política de invalidação documentada? [fonte: Arquiteto] [impacto: Dev, DBA]
8. O monitoramento de aplicação (logs, métricas, alertas) foi planejado com ferramentas e thresholds definidos? [fonte: TI, DevOps] [impacto: DevOps, Dev]
9. O backup automatizado e a estratégia de disaster recovery foram definidos com RPO e RTO acordados? [fonte: TI, Diretoria] [impacto: DevOps, DBA]
10. A escalabilidade horizontal foi considerada — o sistema suporta crescimento sem redesign da arquitetura? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
11. Os custos mensais de infraestrutura foram calculados em cenário atual e projetado (crescimento de 2x e 5x)? [fonte: Financeiro, TI] [impacto: PM, Arquiteto]
12. A estratégia de versionamento de API foi definida para garantir compatibilidade em atualizações? [fonte: Arquiteto] [impacto: Dev]
13. A segurança de rede foi planejada — VPN, firewall rules, WAF, rate limiting, proteção contra injeção? [fonte: Segurança da informação, TI] [impacto: DevOps, Arquiteto]
14. A estrutura de logs foi padronizada (formato, níveis, campos obrigatórios) para facilitar debugging em produção? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
15. A documentação de arquitetura foi revisada e aprovada pelo time de TI corporativa e pelo sponsor? [fonte: TI, Diretoria] [impacto: Arquiteto, PM]

---

## Etapa 06 — Setup

- **Ambiente de desenvolvimento local**: Configurar o ambiente local para que qualquer dev do time consiga subir o projeto em minutos — Docker Compose com banco, cache, e serviços de dependência locais, variáveis de ambiente documentadas em .env.example, seed de dados para desenvolvimento, e README com instruções passo a passo testadas por alguém que não participou do setup. Ambientes de desenvolvimento difíceis de configurar são a causa número um de onboarding lento e produtividade baixa — se leva mais de 30 minutos para subir o projeto do zero, o setup precisa ser simplificado.

- **Configuração de ambientes**: Provisionar ao menos três ambientes: desenvolvimento (para o time testar livremente), staging/homologação (para QA e UAT com dados realistas) e produção. Cada ambiente deve ter configurações isoladas — banco de dados próprio, variáveis de ambiente próprias, credenciais de integração próprias. O ambiente de staging deve ser o mais próximo possível de produção em configuração e dados (snapshot anonimizado) para que testes em staging sejam representativos. Ambientes que divergem de produção geram a falsa segurança de "funciona em staging" seguida do choque de "quebra em produção".

- **Infraestrutura como código**: Toda a infraestrutura (servidores, bancos, filas, cache, load balancers, DNS) deve ser provisionada via IaC (Terraform, Pulumi, CloudFormation) — nunca configurada manualmente pelo console. Infraestrutura manual é irreproducível: se o servidor cair, ninguém sabe recriar exatamente igual. IaC garante que o ambiente pode ser destruído e recriado identicamente, que mudanças são versionadas e reversíveis, e que novos ambientes (ex.: ambiente de DR) podem ser criados sob demanda. O investimento inicial em IaC paga-se na primeira vez que algo precisa ser recriado com urgência.

- **Integração com AD/SSO**: Configurar a integração de autenticação com o provedor de identidade corporativo — Active Directory Federation Services (ADFS), Azure AD, Google Workspace, ou Keycloak como broker. Esta configuração frequentemente depende do time de TI corporativa para liberar acesso, criar o client/app registration, configurar claims e grupos. O prazo real dessa liberação costuma ser 2-4 semanas em empresas grandes — iniciar o processo na Etapa 06 é o mínimo, e qualquer atraso aqui impacta diretamente o cronograma do build.

- **Pipeline de CI/CD com gates de qualidade**: Configurar o pipeline com: lint e formatação automáticos, testes unitários obrigatórios para merge, build completo com sucesso, e deploy automático por ambiente (push para develop → deploy em dev, merge para main → deploy em staging, tag → deploy em produção com aprovação). Incluir gates de qualidade: cobertura mínima de testes (ex.: 70%), análise estática de segurança (Snyk, Trivy para containers), e revisão obrigatória de PR. O pipeline é o guardião da qualidade — se está leniente, a qualidade deteriora rapidamente sob pressão de prazo.

- **Seed de dados e fixtures**: Criar scripts de seed que populam o banco com dados realistas para desenvolvimento e testes — não "Teste 1", "Teste 2", mas dados que simulam o cenário real (nomes brasileiros, CPFs válidos, datas coerentes, relacionamentos íntegros). Fixtures são necessários para testes automatizados e para demos ao cliente. Um banco vazio é inútil para desenvolvimento — o dev precisa ver como a interface se comporta com 5 registros e com 5.000 registros, e isso exige dados de volume.

### Perguntas

1. O ambiente de desenvolvimento local está documentado e qualquer dev consegue subir o projeto em menos de 30 minutos? [fonte: Dev] [impacto: Dev]
2. Os ambientes de dev, staging e produção estão provisionados com configurações isoladas e credenciais separadas? [fonte: DevOps, TI] [impacto: Dev, DevOps]
3. A infraestrutura foi provisionada via IaC (Terraform, Pulumi) e o código está versionado no repositório? [fonte: DevOps] [impacto: DevOps, Dev]
4. A integração com AD/SSO foi solicitada ao time de TI e o prazo de liberação está no cronograma? [fonte: TI, Segurança da informação] [impacto: Dev, PM]
5. O pipeline de CI/CD está configurado com lint, testes, build e deploy automático por ambiente? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
6. Os gates de qualidade (cobertura mínima, análise de segurança, PR review obrigatório) estão configurados e não podem ser bypassed? [fonte: Dev, Arquiteto] [impacto: Dev, QA]
7. Os scripts de seed de dados estão criados com dados realistas em volume representativo? [fonte: Dev, Analista de negócios] [impacto: Dev, QA]
8. O banco de dados de staging foi populado com snapshot anonimizado de dados reais? [fonte: DBA, TI, DPO] [impacto: Dev, QA]
9. As variáveis de ambiente estão documentadas em .env.example e nenhum secret está hardcoded no código? [fonte: Dev] [impacto: Dev, Segurança]
10. O monitoramento básico (uptime check, log aggregation, error tracking) está configurado nos ambientes de staging e produção? [fonte: DevOps, TI] [impacto: DevOps, Dev]
11. As credenciais de integração com sistemas externos foram obtidas para cada ambiente (dev, staging, prod)? [fonte: TI, Fornecedores de sistema] [impacto: Dev, DevOps]
12. O processo de deploy em produção requer aprovação manual e está documentado passo a passo? [fonte: DevOps, TI] [impacto: DevOps, PM]
13. O backup automatizado do banco está configurado e foi testado com restauração completa? [fonte: DevOps, DBA] [impacto: DBA, DevOps]
14. A estrutura de branches (gitflow, trunk-based) foi definida e o time está alinhado? [fonte: Dev, Arquiteto] [impacto: Dev]
15. O ambiente de staging está acessível pela rede corporativa do cliente para UAT? [fonte: TI] [impacto: QA, PM]

---

## Etapa 07 — Build

- **API e regras de negócio**: Implementar os endpoints da API seguindo o modelo de entidades definido, com validações em cada camada — input validation na borda (DTOs), regras de negócio na camada de serviço, e constraints no banco. Cada regra de negócio documentada na Etapa 04 deve ser rastreável até o código que a implementa — se o teste automatizado dessa regra falhar, deve ser claro qual regra de negócio está em risco. Regras de negócio complexas (cálculos de alçada, regras de transição de estado, validações cross-entity) devem ter testes unitários dedicados, não apenas testes de integração end-to-end.

- **Interface focada em eficiência**: O design de ferramenta interna prioriza eficiência sobre estética. Componentes devem suportar: navegação por teclado completa (tab order, Enter para submit, Esc para cancelar), atalhos de teclado para ações frequentes, filtros persistentes (o operador não precisa refiltrar a cada vez que navega), paginação eficiente em listagens grandes (server-side pagination, não carregar 10.000 registros no frontend), e feedback imediato em ações (loading state, toast de sucesso/erro). Um operador que executa 200 ações por dia sente cada segundo de atrito — o que é "detalhe" em produto externo é "impedimento" em ferramenta interna.

- **Integrações com sistemas externos**: Implementar cada integração conforme a especificação da Etapa 04 — com circuit breaker (Polly, resilience4j, ou implementação custom), timeout configurável, retry com backoff exponencial, e dead letter queue para mensagens que falharam após N tentativas. Cada integração deve ter health check independente — o sistema deve saber (e mostrar ao operador) quando uma integração está indisponível, em vez de exibir erro genérico. Integrações com sistemas legados frequentemente falham por motivos não técnicos — o sistema SAP reinicia toda noite às 2h, o servidor TOTVS fica lento na virada do mês — e esses padrões só aparecem com uso real.

- **Migração de dados**: Executar a migração de dados conforme o plano da Etapa 04 — idealmente em batches com validação incremental, não em big bang. Cada batch deve ser validável (contagem de registros, integridade referencial, amostragem de dados) antes de prosseguir para o próximo. Dados inconsistentes identificados durante a migração devem ser tratados conforme a estratégia definida (limpar, migrar com flag, rejeitar) e reportados ao cliente para decisão — nunca descartados silenciosamente. A migração de dados consome tempo desproporcional ao que parece — planejar 30% do esforço total do build para migração em projetos de substituição de legado não é exagero.

- **Trilha de auditoria e logs**: Implementar audit logging desde o primeiro CRUD, não como feature final. Cada criação, edição, exclusão e ação de negócio (aprovação, rejeição, transição de estado) deve gerar um registro de auditoria com: quem (user_id), quando (timestamp UTC), o quê (entidade, campo, valor anterior, valor novo), e contexto (IP, sessão). Logs de auditoria devem ser imutáveis (append-only, sem UPDATE ou DELETE) e armazenados separadamente dos dados operacionais para não impactar performance das queries de negócio.

- **Testes automatizados**: Implementar testes em três camadas — unitários para regras de negócio isoladas (cálculos, validações, transições de estado), integração para endpoints de API com banco real (não mock), e E2E para fluxos críticos de negócio (o fluxo principal de ponta a ponta). A cobertura mínima deve ser enforcada pelo pipeline de CI/CD. Em ferramentas internas, os testes de integração são mais valiosos que unitários isolados porque as regras de negócio frequentemente envolvem múltiplas entidades e o banco é parte integral da lógica (constraints, triggers, defaults).

### Perguntas

1. Todas as regras de negócio documentadas estão implementadas e cada uma tem teste automatizado correspondente? [fonte: Analista de negócios, Dev] [impacto: Dev, QA]
2. A API segue o contrato definido e as validações estão em todas as camadas (input, serviço, banco)? [fonte: Arquiteto, Dev] [impacto: Dev]
3. A interface suporta navegação por teclado, filtros persistentes e paginação server-side para listagens grandes? [fonte: Designer, Operadores] [impacto: Dev, Designer]
4. Cada integração tem circuit breaker, timeout, retry e health check independente implementados? [fonte: Arquiteto, Dev] [impacto: Dev]
5. A migração de dados está sendo executada em batches com validação incremental e relatório de inconsistências? [fonte: DBA, Dev, Gerência operacional] [impacto: Dev, DBA, PM]
6. A trilha de auditoria está implementada desde o primeiro CRUD com registros imutáveis e campos obrigatórios? [fonte: Compliance, Segurança] [impacto: Dev, DBA]
7. Os testes automatizados cobrem unitários (regras), integração (API+banco) e E2E (fluxos críticos)? [fonte: Dev, QA] [impacto: Dev, QA]
8. O controle de acesso (RBAC/ABAC) está implementado tanto no frontend (UI) quanto no backend (API)? [fonte: Segurança, Arquiteto] [impacto: Dev]
9. Os relatórios e exportações do MVP estão implementados e validados com dados realistas? [fonte: Gerência operacional, Dev] [impacto: Dev]
10. Os estados de erro, loading e vazio estão implementados para todas as telas e componentes? [fonte: Designer, Dev] [impacto: Dev, Designer]
11. As notificações (e-mail, in-app) estão implementadas para os eventos definidos na matriz de notificações? [fonte: Gerência operacional, Dev] [impacto: Dev]
12. O desempenho das queries foi validado com volume de dados representativo (não apenas 10 registros de teste)? [fonte: DBA, Dev] [impacto: Dev, DBA]
13. A documentação de API (Swagger/OpenAPI) está gerada automaticamente e atualizada com cada endpoint? [fonte: Dev, Arquiteto] [impacto: Dev]
14. O sistema de transição de estados (workflow) foi testado com todos os caminhos possíveis, incluindo edge cases? [fonte: Dev, QA, Analista de negócios] [impacto: Dev, QA]
15. O progresso está dentro do cronograma e riscos de atraso foram comunicados com antecedência ao sponsor? [fonte: PM] [impacto: PM, Diretoria]

---

## Etapa 08 — QA

- **Teste funcional por perfil de usuário**: Testar cada funcionalidade com cada perfil de acesso — o que o admin vê deve ser diferente do que o operador vê, que deve ser diferente do que o visualizador vê. Testar tentativas de acesso não autorizado (operador tentando acessar URL de admin diretamente, editar registro de outra região, exportar dados que não deveria ver). Em ferramentas internas, falhas de controle de acesso são mais graves que bugs de interface — um operador vendo dados salariais de toda a empresa é incidente de segurança, não bug.

- **Teste de performance com carga realista**: Rodar testes de carga simulando o cenário de pico mapeado no Discovery — número de usuários simultâneos, volume de operações por minuto, queries em tabelas com volume de dados de produção. Ferramentas como k6, Artillery ou JMeter podem simular a carga. O teste deve revelar: tempo de resposta das operações principais sob carga (aceitável: <2s para operações interativas, <10s para relatórios), comportamento do sistema quando a carga ultrapassa o esperado (degradação graceful vs. crash), e gargalos de banco (queries lentas, locks, deadlocks).

- **UAT (User Acceptance Testing) com operadores reais**: Os operadores identificados na Etapa 03 devem executar os cenários de negócio reais no ambiente de staging — não roteiro de teste preparado pelo dev, mas as tarefas que executam diariamente com os dados e exceções que conhecem. O UAT deve ter critérios de aceitação formais: se o operador consegue completar o fluxo principal sem assistência do dev, o UAT passou. Se precisa perguntar "como faço para X?", a interface precisa ser melhorada ou o treinamento precisa cobrir esse ponto. Bugs encontrados no UAT devem ser classificados (bloqueador, crítico, menor) e os bloqueadores resolvidos antes do go-live.

- **Teste de integrações em staging**: Testar cada integração com o sistema real em ambiente de staging (não mock). Integrações que funcionam com mock podem falhar com o sistema real por motivos inesperados — timeout diferente, formato de data diferente, encoding de caracteres, certificado SSL vencido, firewall bloqueando. Se o ambiente de staging do sistema externo não está disponível, documentar o risco e planejar teste em produção controlado logo após o go-live. Integrações não testadas com sistema real são o risco número um de falha no go-live de ferramentas internas.

- **Teste de migração de dados em staging**: Executar a migração completa de dados no ambiente de staging e validar com o cliente — contagem de registros bate, dados de amostragem estão corretos, integridade referencial está preservada, campos calculados batem com os valores do sistema antigo. Se a migração revelou inconsistências nos dados de origem (e frequentemente revela), essas inconsistências devem ser reportadas e o cliente deve decidir como tratar antes do go-live. Migração de dados que "quase funciona" é mais perigosa do que migração que falha claramente — dados parcialmente migrados geram decisões de negócio baseadas em informação incompleta.

- **Teste de segurança**: Executar validação de segurança básica — OWASP Top 10 no mínimo. Focar em: injeção SQL (usar parameterized queries em todos os endpoints), XSS (sanitização de input e encoding de output), CSRF (tokens CSRF em formulários ou same-site cookies), autenticação/autorização bypassável (tentar acessar endpoints sem token ou com token de outro perfil), e exposição de dados sensíveis em responses (retornar apenas os campos necessários, nunca o objeto completo do banco). Para ferramentas internas, o risco de ataque vem de insiders, não de hackers externos — o que torna as falhas de autorização ainda mais críticas.

### Perguntas

1. Cada funcionalidade foi testada com cada perfil de usuário e os acessos não autorizados foram bloqueados corretamente? [fonte: QA, Segurança] [impacto: Dev, Segurança]
2. Os testes de carga simulam o cenário de pico e os tempos de resposta estão dentro dos limites definidos? [fonte: QA, Dev] [impacto: Dev, DevOps, DBA]
3. O UAT foi executado por operadores reais com cenários de negócio reais e os critérios de aceitação foram formalizados? [fonte: Gerência operacional, Operadores] [impacto: PM, Dev, QA]
4. Cada integração foi testada com o sistema real em staging (não apenas com mock)? [fonte: Dev, TI] [impacto: Dev, Arquiteto]
5. A migração de dados foi executada em staging e validada pelo cliente (contagem, amostragem, integridade)? [fonte: DBA, Gerência operacional] [impacto: Dev, DBA, PM]
6. Os testes de segurança (OWASP Top 10) foram executados e todas as vulnerabilidades críticas corrigidas? [fonte: Segurança, Dev] [impacto: Dev, Segurança]
7. Os relatórios e exportações foram validados com dados reais e o formato de saída está correto? [fonte: Gerência operacional, QA] [impacto: Dev]
8. O comportamento do sistema sob falha de integração foi testado (sistema externo indisponível, timeout, dados inválidos)? [fonte: QA, Dev] [impacto: Dev]
9. Os fluxos de notificação (e-mail, in-app) foram testados end-to-end e chegam ao destino correto? [fonte: QA, Gerência operacional] [impacto: Dev]
10. A trilha de auditoria registra corretamente todas as ações de negócio com campos completos e imutáveis? [fonte: Compliance, QA] [impacto: Dev, DBA]
11. O sistema se comporta corretamente com dados extremos (campos no limite, listas com milhares de registros, upload de arquivo grande)? [fonte: QA, Dev] [impacto: Dev]
12. O backup de banco foi testado com restauração completa e o tempo de restauração está dentro do RTO definido? [fonte: DevOps, DBA] [impacto: DevOps, DBA]
13. Todos os bugs classificados como bloqueadores e críticos no UAT foram corrigidos e retestados? [fonte: QA, PM] [impacto: Dev, PM]
14. O sistema funciona corretamente nos browsers e dispositivos definidos como suportados? [fonte: QA, Dev] [impacto: Dev]
15. A documentação de operação (runbook) foi escrita e validada com simulação de incidente? [fonte: DevOps, Dev] [impacto: DevOps]

---

## Etapa 09 — Launch Prep

- **Plano de migração de dados em produção**: Documentar a sequência exata da migração de dados em produção — quando executar (janela de manutenção fora do horário comercial), quem executa, quanto tempo leva (estimado com base na execução em staging), como validar (queries de contagem e amostragem), e o que fazer se falhar (rollback do banco ou re-execução). Se o sistema novo precisa conviver com o antigo durante um período de transição, definir como os dados serão sincronizados entre os dois — dual-write é complexo e propenso a inconsistências, e frequentemente é subestimado.

- **Treinamento dos operadores**: Realizar sessões de treinamento segmentadas por perfil — o operador precisa saber executar suas tarefas diárias, o gerente precisa saber acompanhar indicadores e aprovar solicitações, o admin precisa saber criar usuários e ajustar configurações. Treinamento genérico para todos os perfis juntos é ineficiente — o operador fica entediado durante a parte de admin, o admin fica perdido durante os detalhes operacionais. Documentar tudo em guia rápido com capturas de tela — a memória do treinamento presencial se perde em 2 semanas, e o guia se torna a referência permanente.

- **Plano de contingência e rollback**: Documentar o plano B completo — se o sistema novo falhar nas primeiras horas, como reverter para o processo anterior? Se os dados foram migrados, como garantir que o sistema antigo ainda funciona com dados atualizados? Se houve dual-write durante transição, como desligar o sistema novo sem perder dados criados nele? Definir critérios claros de rollback (ex.: sistema indisponível por mais de 1h, erro de dados que afeta mais de 5% das transações, integração crítica inoperante) e quem tem autoridade para tomar a decisão.

- **Comunicação interna sobre a mudança**: Preparar comunicação para toda a empresa (ou para as áreas afetadas) sobre: o que muda, quando muda, o que cada pessoa precisa fazer (instalar algo, acessar URL nova, mudar processo), e quem procurar em caso de problema. Ferramentas internas afetam o dia a dia de muitas pessoas — uma mudança sem comunicação prévia gera confusão, ligações para TI, e resistência. A comunicação deve vir do sponsor (não do time técnico) para ter peso institucional.

- **Monitoramento reforçado para a primeira semana**: Configurar alertas adicionais para a primeira semana pós-go-live — tempo de resposta acima do normal, taxa de erro acima de 1%, fila de jobs crescendo sem processar, login falhando para mais de 3 usuários distintos. O time de desenvolvimento deve estar em regime de plantão (não necessariamente presencial, mas com canal de comunicação rápido e acesso a produção) durante os primeiros 5 dias úteis. Bugs reportados nessa semana devem ser tratados com prioridade máxima — a confiança dos operadores no sistema novo é frágil e se perde rapidamente com problemas não resolvidos.

- **Validação de acessos e credenciais de produção**: Verificar que todos os acessos necessários para o go-live estão configurados e testados em produção — não apenas em staging. Isso inclui: credenciais de integração com sistemas de produção (API keys, certificados), acessos de operadores ao sistema novo (logins criados, permissões configuradas), acessos de administração e suporte (deploy, logs, banco, monitoramento), e acessos de emergência (quem pode acessar o banco de produção diretamente se necessário). Um acesso não configurado no dia do go-live vira bloqueio crítico sob pressão.

### Perguntas

1. O plano de migração de dados em produção está documentado com sequência, responsável, tempo estimado e plano de rollback? [fonte: DBA, Dev, TI] [impacto: Dev, DBA, PM]
2. Os treinamentos dos operadores foram realizados segmentados por perfil e o guia rápido com capturas de tela foi entregue? [fonte: PM, Gerência operacional] [impacto: Operadores, PM]
3. O plano de contingência e rollback está documentado com critérios claros e responsável designado para decisão? [fonte: TI, Diretoria] [impacto: PM, DevOps, Dev]
4. A comunicação interna sobre a mudança foi preparada e será enviada pelo sponsor com antecedência adequada? [fonte: Diretoria, RH, Comunicação interna] [impacto: PM]
5. O monitoramento reforçado (alertas, dashboards, plantão do time) está configurado para a primeira semana? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
6. Todas as credenciais de integração de produção foram obtidas, configuradas e testadas? [fonte: TI, Fornecedores de sistema] [impacto: Dev, DevOps]
7. Os acessos de todos os operadores ao sistema de produção foram criados e testados individualmente? [fonte: TI, Gerência operacional] [impacto: Dev, PM]
8. A janela de migração de dados foi agendada fora do horário comercial e o tempo necessário foi reservado? [fonte: TI, DBA, Gerência operacional] [impacto: DBA, Dev, PM]
9. O sistema antigo será mantido ativo durante o período de transição e os operadores sabem quando parar de usá-lo? [fonte: Gerência operacional, TI] [impacto: PM, Operadores]
10. O canal de suporte pós-go-live foi definido e comunicado aos operadores (chat, e-mail, telefone)? [fonte: PM, TI] [impacto: PM, Dev]
11. O plano de go-live foi revisado em reunião com todos os envolvidos (dev, TI, operações, sponsor)? [fonte: PM] [impacto: PM, todos]
12. Os scripts de migração de dados de produção foram testados pela última vez em staging com dados atualizados? [fonte: DBA, Dev] [impacto: Dev, DBA]
13. O backup do banco de produção será feito imediatamente antes da migração e o procedimento de restore está documentado? [fonte: DBA, DevOps] [impacto: DBA, DevOps]
14. Os critérios de sucesso do go-live foram definidos e serão avaliados nas primeiras 24h (operadores conseguem trabalhar, integrações funcionam)? [fonte: Gerência operacional, PM] [impacto: PM]
15. O time de TI corporativa está ciente da data e horário do go-live e com disponibilidade para suporte de infraestrutura? [fonte: TI] [impacto: DevOps, PM]

---

## Etapa 10 — Go-Live

- **Execução da migração de dados em produção**: Executar a migração conforme o plano documentado — backup completo antes, migração em batches com validação incremental, e verificação final de contagem e integridade. O time de negócio (gerente ou operador sênior) deve validar uma amostra dos dados migrados antes de liberar o sistema para uso. Se a migração demorar mais que o previsto, acionar o plano B (estender a janela, adiar o go-live, ou entrar em produção com dados parciais e completar depois — conforme definido na Etapa 09). Nunca improvisar sob pressão.

- **Ativação do sistema e smoke test**: Após a migração, ativar o sistema e executar smoke test com o time de operações — login funciona, listagem carrega dados migrados, criação de registro funciona, integração com sistema externo responde, relatório gera corretamente. O smoke test não é QA completo — é validação rápida (30-60 minutos) dos fluxos mais críticos para confirmar que o sistema está operacional. Se qualquer item do smoke test falhar, avaliar se é corrigível em minutos ou se aciona o rollback conforme os critérios definidos.

- **Monitoramento ativo nas primeiras horas**: O time técnico deve monitorar ativamente nas primeiras 4-8 horas — dashboards de infra (CPU, memória, I/O de disco, conexões de banco), logs de erro em tempo real, métricas de application (tempo de resposta, throughput, taxa de erro), e canal de comunicação com operadores para reportar problemas imediatos. Problemas típicos das primeiras horas: queries lentas que não apareceram em staging por volume menor de dados, integração que falha em produção por credencial ou firewall, e picos de carga inesperados porque todos os operadores acessam ao mesmo tempo.

- **Suporte hands-on aos operadores**: No primeiro dia (e idealmente nos primeiros 3 dias), ter alguém do time técnico ou de negócios disponível para responder dúvidas dos operadores em tempo real — presencialmente ou por canal dedicado. As dúvidas mais frequentes não são bugs — são "como faço X?", "onde vejo Y?", "o que esse campo significa?". Cada dúvida recorrente deve ser documentada no guia rápido (FAQ) para evitar que se repita. A presença de suporte no início reduz ansiedade e resistência dos operadores e aumenta significativamente a taxa de adoção.

- **Coleta de feedback estruturado**: Nos primeiros 5 dias úteis, coletar feedback estruturado dos operadores — o que funciona bem, o que é confuso, o que está lento, o que falta. Não apenas perguntar "tudo bem?" (que sempre recebe "sim"), mas observar o uso real e identificar pontos de fricção. Organizar o feedback em: bugs (corrigir imediatamente), melhorias de usabilidade (backlog prioritário), e features faltantes (backlog normal). O feedback da primeira semana é o mais valioso que o projeto vai receber — é quando as impressões são frescas e as dores são reais.

- **Encerramento formal e handoff**: Entregar formalmente: acesso ao repositório com documentação de setup, acesso à infraestrutura com documentação de operação (runbook), credenciais de todos os serviços (banco, cache, integrações, monitoramento), documentação de arquitetura (diagrama, decisões, trade-offs), guia do operador, e contato de suporte com SLA definido. O aceite formal do sponsor fecha o projeto e inicia o período de garantia/suporte conforme contratado. Sem aceite formal, o projeto nunca termina — e o time fica eternamente respondendo "só mais uma coisinha".

### Perguntas

1. A migração de dados em produção foi executada com sucesso e validada pelo time de negócio (contagem, amostragem)? [fonte: DBA, Gerência operacional] [impacto: Dev, DBA, PM]
2. O smoke test com o time de operações foi concluído com sucesso em todos os fluxos críticos? [fonte: QA, Gerência operacional] [impacto: Dev, PM]
3. O monitoramento de infra e aplicação está ativo e sem alertas críticos nas primeiras horas? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
4. O canal de suporte hands-on está ativo e os operadores sabem como reportar problemas? [fonte: PM, Gerência operacional] [impacto: PM, Dev]
5. O sistema antigo foi desativado conforme o plano ou está em período de convivência controlado? [fonte: TI, Gerência operacional] [impacto: PM, DevOps]
6. Os operadores conseguem executar suas tarefas diárias sem assistência do time técnico? [fonte: Gerência operacional, Operadores] [impacto: PM, Dev]
7. As integrações com sistemas externos estão funcionando em produção com dados reais? [fonte: Dev, TI] [impacto: Dev, Arquiteto]
8. O feedback estruturado está sendo coletado dos operadores nos primeiros dias? [fonte: PM, Gerência operacional] [impacto: PM, Dev]
9. Os bugs reportados no primeiro dia foram classificados e os bloqueadores estão sendo tratados com prioridade máxima? [fonte: Dev, QA] [impacto: Dev, PM]
10. O backup automatizado do banco de produção foi verificado e está funcionando conforme configurado? [fonte: DBA, DevOps] [impacto: DBA, DevOps]
11. As métricas de performance em produção estão dentro dos limites definidos (tempo de resposta, throughput)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
12. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou que consegue acessar? [fonte: Dev, DevOps, TI] [impacto: PM]
13. O aceite formal de entrega foi obtido do sponsor (e-mail, assinatura de ata, ou confirmação documentada)? [fonte: Diretoria] [impacto: PM]
14. O plano de suporte pós-lançamento foi ativado e o SLA está comunicado ao cliente? [fonte: Diretoria, PM] [impacto: PM, Dev]
15. O backlog de melhorias pós-go-live foi organizado com priorização baseada no feedback dos operadores? [fonte: PM, Gerência operacional] [impacto: PM, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos só um sisteminha simples de cadastro"** — O cliente descreve como CRUD mas, ao detalhar, aparecem regras de workflow, integrações com ERP, controle de acesso por região, relatórios com cruzamento de dados e notificações por e-mail. "Simples" não existe em ferramenta corporativa — se há mais de um tipo de usuário e mais de uma integração, a complexidade é real e deve ser dimensionada corretamente.
- **"O processo tá na cabeça do João"** — Quando o processo não está documentado e depende de uma pessoa, o risco é duplo: se o João sair da empresa, o processo morre; e o sistema vai ser construído baseado no que o João lembra, não no que realmente acontece. Mapeamento formal do processo as-is é obrigatório antes de avançar.
- **"A TI vai liberar acesso quando precisarmos"** — TI corporativa tem fila própria e SLA que raramente é compatível com o cronograma do projeto. Liberação de acesso a AD, VPN, firewall, APIs de sistemas legados e ambientes de staging pode levar semanas. Iniciar o processo na Inception é o mínimo.

### Etapa 02 — Discovery

- **"Todos os usuários fazem a mesma coisa"** — Se a ferramenta tem mais de um tipo de usuário, eles não fazem a mesma coisa. O gerente que diz isso geralmente não conhece os detalhes do dia a dia dos operadores. Entrevistar os operadores diretamente revela papéis, permissões e fluxos que a gerência não mencionou.
- **"Não temos dados legados para migrar"** — Verificar com cuidado. Frequentemente os dados estão em planilhas Excel, caixas de e-mail, pastas compartilhadas ou até cadernos físicos. "Não temos dados" pode significar "não temos banco de dados", o que é diferente de não ter dados.
- **"A integração com o SAP é simples, é só uma API"** — Integração com ERP nunca é "só uma API". Envolve módulos específicos, RFC customizados, formatos proprietários, time de basis que precisa liberar acesso, e ambiente de teste que pode não existir. Estimar integração com ERP como tarefa simples é garantia de atraso.

### Etapa 03 — Alignment

- **"Vamos fazer tudo no MVP, o escopo é pequeno"** — Se o escopo é "pequeno" mas inclui 15 telas, 5 perfis de acesso, 3 integrações e relatórios customizados, não é pequeno. MVP que inclui tudo não é MVP — é o projeto inteiro disfarçado de entrega inicial. Cortar escopo dói, mas não cortar dói mais no prazo e no orçamento.
- **"O gerente valida para todo o time"** — Validação de processo to-be apenas com a gerência, sem os operadores, é receita para rejeição na adoção. O gerente descreve o processo ideal, o operador vive o processo real. Se os dois não coincidem, o sistema vai ser usado sob protesto.
- **"Não precisamos de staging, testamos direto em produção"** — Testar em produção com dados reais de colaboradores, financeiros ou clientes é irresponsável. Um bug que expõe dados salariais ou corrompe dados financeiros não é reversível com "desculpa". Staging com dados anonimizados é investimento mínimo.

### Etapa 04 — Definition

- **"O modelo de dados a gente vai ajustando durante o build"** — Alterar modelo de dados com código já escrito e dados já migrados é exponencialmente mais caro do que definir corretamente antes. Cada campo adicionado depois requer: migração de banco, atualização de API, atualização de frontend, atualização de testes, e re-validação de migração de dados.
- **"As regras de negócio são óbvias, não precisa documentar"** — Regras "óbvias" são as que mais geram conflito — porque cada pessoa tem uma interpretação diferente do que é óbvio. "Aprovação acima de R$ 10.000 vai para o diretor" parece simples até descobrir que há 3 tipos de despesa com alçadas diferentes, exceções para emergência, e o conceito de "diretor" varia por unidade.
- **"Os relatórios a gente define quando o sistema estiver rodando"** — Relatórios definidos após o build frequentemente exigem dados que não foram modelados no banco. "Quero saber o tempo médio de aprovação" requer que o sistema registre o timestamp de cada transição de estado — se isso não foi modelado, o relatório é impossível sem refatoração.

### Etapa 05 — Architecture

- **"Vamos usar microservices porque é a arquitetura moderna"** — Para uma ferramenta interna com 5-50 usuários, microservices adiciona complexidade de infraestrutura (service discovery, load balancing, distributed tracing, eventual consistency) sem benefício proporcional. Monólito modular é quase sempre a escolha correta para ferramentas internas, com extração de serviços se e quando a necessidade real aparecer.
- **"Hospedamos no servidor da empresa para economizar"** — Hospedar em servidor on-premises parece economizar, mas transfere custos ocultos: manutenção de SO, patches de segurança, backup, monitoramento, e disponibilidade de alguém para reiniciar o serviço às 2h da manhã. Cloud com provisionamento correto frequentemente custa menos no TCO total.
- **"Não precisa de Redis, o banco resolve tudo"** — Para 10 usuários, o banco resolve tudo. Para 200 usuários com relatórios pesados e dashboards, queries diretamente no banco operacional degradam a performance de escrita. Cache e materialized views não são premature optimization — são planejamento baseado em volumetria mapeada.

### Etapa 06 — Setup

- **"O dev sobe na máquina dele e testa lá"** — Sem ambiente de desenvolvimento padronizado, cada dev tem uma configuração diferente (versão do banco, versão do Node, variáveis de ambiente). "Funciona na minha máquina" é o sintoma clássico. Docker Compose resolve isso com investimento de horas, não dias.
- **"Deploy é dar SSH no servidor e dar git pull"** — Deploy manual via SSH é irreproducível, propenso a erro humano, e impossível de reverter rapidamente. Pipeline de CI/CD com rollback automático é o padrão mínimo para qualquer sistema em produção.
- **"Estamos esperando TI liberar o acesso ao AD"** — Se a liberação de AD/SSO foi solicitada apenas no Setup, já está atrasado. O prazo de TI corporativa para liberações de segurança é tipicamente 2-4 semanas. O build vai avançar com autenticação local temporária, mas o risco de integração de SSO falhando no go-live é real.

### Etapa 07 — Build

- **"Fizemos login próprio, depois a gente integra com AD"** — Integrar autenticação depois é significativamente mais complexo do que integrar desde o início. Claims, roles, groups no AD podem não mapear diretamente para o modelo de permissões do sistema, e o fluxo de login muda completamente. Fazer "depois" vira refatoração.
- **"A migração de dados fica para a última semana"** — Migração deixada para o final descobre problemas quando não há mais tempo para corrigir. Dados inconsistentes no legado, campos com encoding diferente, datas em formato errado — tudo isso aparece durante a migração e precisa de tempo para tratar. Migração deve começar em paralelo com o build, não sequencialmente.
- **"Os testes a gente faz manual depois"** — Sem testes automatizados, cada mudança de código exige re-teste manual de todos os fluxos afetados. Em sistema com regras de negócio complexas, isso se torna inviável rapidamente — e o resultado é que mudanças de código são feitas sem teste, gerando bugs regressivos em produção.

### Etapa 08 — QA

- **"Testamos com o admin, funciona tudo"** — Testar apenas com perfil de administrador não revela bugs de controle de acesso. O operador pode ver dados que não deveria, executar ações proibidas, ou ter interface diferente do esperado. Cada perfil deve ser testado independentemente.
- **"O UAT é o dev mostrando o sistema para o gerente"** — Demo não é UAT. No UAT, o operador senta sozinho e tenta executar seu trabalho real. Se precisa perguntar como fazer, o sistema ou o treinamento precisam melhorar. Demo onde o dev navega e explica prova que o dev sabe usar, não que o operador sabe.
- **"Performance está boa, o sistema é rápido"** — "Rápido" com 3 registros de teste é diferente de "rápido" com 500.000 registros migrados. Teste de performance sem volume de dados representativo é enganoso. Carregar o banco de staging com volume de produção antes de testar performance.

### Etapa 09 — Launch Prep

- **"Mandamos um e-mail para todo mundo e pronto"** — Comunicação de mudança por e-mail genérico tem taxa de leitura próxima de zero. O operador descobre o sistema novo no dia em que tenta usar o antigo e não consegue. Comunicação deve ser segmentada por perfil, com sessão de Q&A, e reforçada nos dias anteriores ao go-live.
- **"Os operadores se viram, é intuitivo"** — Nenhum sistema corporativo é intuitivo para quem usou planilha por 10 anos. Treinamento é investimento, não custo — e o retorno é medido em adoção bem-sucedida vs. resistência que mata o projeto.
- **"Se der problema, a gente reverte rápido"** — "Rápido" sem plano de rollback documentado significa 4 horas de pânico enquanto alguém tenta lembrar como restaurar o banco, onde está o backup, e como reconfigurar o DNS. Plano documentado com responsáveis e sequência de ações transforma crise em procedimento.

### Etapa 10 — Go-Live

- **"Go-live na sexta à tarde antes do feriado"** — Se algo der errado, ninguém estará disponível por 3 dias. Go-live deve ser em dia útil, preferencialmente segunda ou terça, com todo o time disponível por pelo menos 3 dias úteis seguidos.
- **"Desligamos o sistema antigo no mesmo dia"** — Dados podem não ter migrado completamente, operadores podem precisar consultar histórico no sistema antigo, e o rollback se torna impossível. Manter o sistema antigo ativo por no mínimo 2 semanas em modo somente-leitura é o mínimo seguro.
- **"O projeto acabou, agora é com vocês"** — Sem período de estabilização e suporte estruturado, bugs da primeira semana se acumulam, operadores desistem de reportar, e o sistema perde credibilidade. A primeira semana pós-go-live é parte do projeto, não bonus.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é SaaS interno / ferramenta corporativa** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Os clientes finais vão acessar o sistema" | SaaS externo ou portal de clientes, não ferramenta interna | Reclassificar para saas ou web-app |
| "Vamos cobrar assinatura mensal dos usuários" | Produto SaaS com billing, não ferramenta interna | Reclassificar para saas |
| "Precisa de vitrine de produtos com carrinho" | E-commerce, não ferramenta interna | Reclassificar para e-commerce |
| "Vendedores e compradores se conectam na plataforma" | Marketplace, não ferramenta interna | Reclassificar para marketplace |
| "Precisa de app nativo para Android e iOS" | Mobile app, avaliar se web responsivo resolve ou se precisa de projeto separado | Avaliar reclassificação para mobile-app ou adição de escopo mobile |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos como funciona o processo hoje" | 01 | Não é possível automatizar um processo que ninguém consegue descrever | Mapear processo as-is antes de avançar |
| "TI não tem previsão para liberar acesso às APIs" | 01 | Integrações são bloqueador e TI não tem SLA | Escalar para diretoria e obter comprometimento formal de TI |
| "Não temos orçamento para infraestrutura cloud" | 01 | Sem infra, não há onde rodar o sistema | Apresentar TCO e aprovar orçamento antes de continuar |
| "Os dados estão espalhados em 15 planilhas de cada gerente" | 02 | Migração de dados é projeto paralelo de meses | Estimar migração separadamente e incluir no escopo |
| "O diretor precisa aprovar cada tela antes de implementar" | 03 | Aprovação por tela gera ciclo de feedback de semanas por sprint | Acordar aprovação por fluxo (não por tela) com cadência definida |
| "Não podemos dar acesso ao banco do ERP para o time externo" | 05 | Integração impossível sem acesso a dados | Negociar API, view de banco, ou extração em arquivo como alternativa |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O time de TI é terceirizado e muda a cada 6 meses" | 01 | Conhecimento institucional se perde a cada troca de time | Documentar todas as dependências de TI e não depender de pessoas específicas |
| "Usamos Excel há 15 anos e funciona bem" | 01 | Resistência à mudança será forte — operadores não veem valor | Planejar change management reforçado e demonstrar ganho tangível |
| "Cada filial faz o processo de um jeito diferente" | 02 | Processo to-be precisa unificar variantes — complexidade de definição explode | Mapear variantes, definir processo padrão com exceções controladas |
| "O sistema precisa funcionar igualzinho ao antigo" | 03 | Paridade funcional total com sistema legado é escopo infinito — cada macro de Excel é uma feature | Negociar escopo: 80% dos fluxos cobrem 95% do uso. Documentar o que fica de fora |
| "Não temos DPO definido" | 02 | Dados pessoais de colaboradores sem governança LGPD | Alertar sobre risco legal e recomendar designação de DPO antes de manipular dados sensíveis |
| "As regras mudam o tempo todo conforme a diretoria" | 04 | Regras de negócio instáveis geram retrabalho contínuo durante o build | Congelar regras para o MVP e tratar mudanças como backlog pós-entrega |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Dor operacional concreta identificada (pergunta 1)
- Sponsor e operadores reais mapeados por nome (pergunta 2)
- Processo atual identificado como documentado ou a mapear (perguntas 4 e 5)
- Integrações obrigatórias listadas (pergunta 6)
- Orçamento de desenvolvimento e operação aprovado (pergunta 9)

### Etapa 02 → 03

- Processo as-is mapeado com exceções e workarounds (pergunta 1)
- Volumetria de dados e usuários quantificada (pergunta 2)
- Papéis e permissões mapeados com controle de dados (perguntas 3 e 4)
- APIs de integração avaliadas quanto à disponibilidade e documentação (pergunta 7)
- Requisitos de disponibilidade e retenção definidos (perguntas 13 e 14)

### Etapa 03 → 04

- Processo to-be validado com operadores (pergunta 1)
- Decisão build vs. buy documentada com justificativa (pergunta 2)
- Escopo do MVP definido com critério de corte (pergunta 3)
- Autenticação alinhada com TI (pergunta 4)
- Modelo de suporte pós-lançamento formalizado (pergunta 6)

### Etapa 04 → 05

- Modelo de entidades e relacionamentos formalizado (pergunta 1)
- Wireframes de fluxo completo aprovados (pergunta 2)
- Regras de negócio documentadas com condição, ação e exceção (pergunta 3)
- Integrações especificadas com mapeamento de campos (pergunta 4)
- Plano de migração de dados especificado (pergunta 5, se aplicável)

### Etapa 05 → 06

- Stack (backend, frontend, banco) escolhida e justificada (perguntas 1 e 2)
- Autenticação e autorização definidas (pergunta 3)
- Infra (cloud/on-prem) decidida com TI (pergunta 5)
- CI/CD desenhado com ambientes separados (pergunta 6)
- Custos de operação calculados e aprovados (pergunta 11)

### Etapa 06 → 07

- Ambiente de dev local configurado e documentado (pergunta 1)
- Ambientes dev/staging/prod provisionados com isolamento (pergunta 2)
- Integração AD/SSO em andamento e com prazo no cronograma (pergunta 4)
- Pipeline de CI/CD testado com PR real (pergunta 5)
- Seed de dados realistas criado (pergunta 7)

### Etapa 07 → 08

- Regras de negócio implementadas com testes automatizados (pergunta 1)
- Integrações implementadas com circuit breaker e health check (pergunta 4)
- Migração de dados executada em batches com validação (pergunta 5)
- Trilha de auditoria implementada (pergunta 6)
- Testes automatizados cobrindo unitários, integração e E2E (pergunta 7)

### Etapa 08 → 09

- Testes por perfil de usuário concluídos (pergunta 1)
- Testes de carga executados com resultados aceitáveis (pergunta 2)
- UAT concluído por operadores reais com aceite formal (pergunta 3)
- Integrações testadas com sistema real em staging (pergunta 4)
- Migração de dados validada em staging pelo cliente (pergunta 5)

### Etapa 09 → 10

- Plano de migração de dados em produção documentado (pergunta 1)
- Treinamentos realizados e guia rápido entregue (pergunta 2)
- Plano de rollback documentado com critérios e responsável (pergunta 3)
- Credenciais de produção configuradas e testadas (pergunta 6)
- Acessos de operadores criados e testados (pergunta 7)

### Etapa 10 → Encerramento

- Migração de dados em produção validada pelo negócio (pergunta 1)
- Smoke test concluído com sucesso (pergunta 2)
- Operadores conseguem trabalhar sem assistência técnica (pergunta 6)
- Acessos entregues e aceite formal obtido (perguntas 12 e 13)
- Backlog de melhorias organizado e priorizado (pergunta 15)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de SaaS interno. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Backoffice | V2 Workflow | V3 Dashboard/BI | V4 Autoatendimento | V5 Legado Modernizado |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 2 | 2 | 4 |
| 02 Discovery | 3 | 4 | 3 | 3 | 5 |
| 03 Alignment | 2 | 3 | 2 | 3 | 4 |
| 04 Definition | 3 | 5 | 3 | 3 | 5 |
| 05 Architecture | 2 | 4 | 4 | 3 | 3 |
| 06 Setup | 2 | 3 | 3 | 3 | 3 |
| 07 Build | 3 | 5 | 4 | 4 | 5 |
| 08 QA | 3 | 4 | 3 | 3 | 5 |
| 09 Launch Prep | 2 | 3 | 2 | 3 | 4 |
| 10 Go-Live | 2 | 3 | 2 | 2 | 4 |
| **Total relativo** | **24** | **37** | **28** | **29** | **42** |

**Observações por variante:**

- **V1 Backoffice**: Esforço distribuído uniformemente. O gargalo oculto é a proliferação de CRUDs que parecem simples mas cada um tem filtros, validações e exportações próprias. Disciplina de componentes reutilizáveis desde o início é o fator decisivo de produtividade.
- **V2 Workflow**: Pico em Definition (modelar transições de estado com todas as exceções) e Build (implementar state machine com regras de alçada e notificações). Integrações com sistemas de aprovação corporativos adicionam complexidade real. É a variante mais pesada em regras de negócio.
- **V3 Dashboard/BI**: Pico em Architecture (pipeline de dados, ETL, escolha de banco analítico) e Build (visualizações performáticas com grande volume de dados). Discovery e Definition são mais leves porque a entrada de dados é mínima — o sistema consome, não produz.
- **V4 Autoatendimento**: Esforço concentrado em Build (múltiplos fluxos de autoatendimento) e Alignment (validação com RH e áreas de suporte). A integração com sistemas de RH (folha, férias, benefícios) é o risco técnico principal.
- **V5 Legado Modernizado**: A variante mais pesada em todas as etapas. Discovery consome muito tempo mapeando regras implícitas do sistema antigo. Definition é extensa porque cada campo do legado precisa de equivalente no novo. Build é pesado pela migração de dados em paralelo. QA é crítico porque os operadores comparam cada detalhe com o sistema que conhecem há anos.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sem integração com sistemas externos (Etapa 01, pergunta 6) | Etapa 02: perguntas 6 e 7 (detalhamento de integrações, APIs). Etapa 04: pergunta 4 (especificação de integrações). Etapa 05: pergunta 4 (pattern de integração). Etapa 07: pergunta 4 (circuit breaker). Etapa 08: perguntas 4 e 8 (teste de integrações). |
| Sem dados legados a migrar (Etapa 01, pergunta 14) | Etapa 04: pergunta 5 (plano de migração). Etapa 07: pergunta 5 (execução da migração). Etapa 08: pergunta 5 (validação da migração em staging). Etapa 09: perguntas 1, 8 e 12 (migração em produção). Etapa 10: pergunta 1 (validação de migração). |
| Autenticação própria, sem SSO/AD (Etapa 03, pergunta 4) | Etapa 06: pergunta 4 (integração AD/SSO). Etapa 07: menção a claims e groups do AD. |
| Sistema novo, sem processo anterior (Etapa 01, pergunta 4) | Etapa 02: pergunta 1 (mapeamento as-is). Etapa 03: pergunta 11 (convivência entre sistemas). Etapa 09: pergunta 9 (manter sistema antigo). Etapa 10: pergunta 5 (desativação de sistema antigo). |
| Dashboard somente leitura, sem input de dados (variante V3) | Etapa 04: perguntas 6 e 8 (notificações, transições de workflow). Etapa 07: perguntas 1 e 14 (regras de negócio de escrita, workflow). Etapa 08: pergunta 4 (teste de integrações de escrita). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Requisitos de auditoria identificados (Etapa 02, pergunta 5) | Etapa 05: pergunta 2 (modelagem de tabelas de auditoria) se torna gate. Etapa 07: pergunta 6 (implementação de audit trail) se torna bloqueadora. Etapa 08: pergunta 10 (validação de trilha de auditoria) é obrigatória. |
| Sistema substitui legado (Etapa 01, pergunta 4) | Etapa 02: pergunta 1 (mapeamento as-is) se torna gate. Etapa 04: pergunta 5 (plano de migração) se torna gate. Etapa 07: pergunta 5 (migração em batches) se torna o maior risco. Etapa 09: pergunta 9 (convivência com sistema antigo) é obrigatória. |
| Requisitos de compliance (LGPD, SOX) identificados (Etapa 01, pergunta 8) | Etapa 02: pergunta 14 (retenção de dados) se torna bloqueadora. Etapa 05: pergunta 13 (segurança de rede) ganha prioridade máxima. Etapa 07: pergunta 6 (audit trail) é obrigatória. Etapa 08: pergunta 6 (testes de segurança OWASP) é gate. |
| Múltiplas integrações com sistemas corporativos (Etapa 01, pergunta 6) | Etapa 02: perguntas 6 e 7 (detalhamento e APIs) se tornam gates. Etapa 04: pergunta 4 (especificação completa) se torna gate. Etapa 06: pergunta 11 (credenciais por ambiente) é obrigatória. Etapa 08: pergunta 4 (teste com sistema real) é bloqueadora para go-live. |
| Acesso offline necessário (Etapa 02, pergunta 8) | Etapa 05: arquitetura deve prever sync e conflict resolution — adiciona complexidade significativa. Etapa 07: implementação de service worker e cache local é obrigatória. Etapa 08: teste de cenários offline/online é gate. |
| Volumetria alta (>100 usuários simultâneos ou >1M registros) (Etapa 02, pergunta 2) | Etapa 05: pergunta 7 (cache e performance) se torna gate. Etapa 05: pergunta 10 (escalabilidade) é crítica. Etapa 07: pergunta 12 (performance de queries) é bloqueadora. Etapa 08: pergunta 2 (teste de carga) é obrigatória com thresholds definidos. |
