---
title: "Extensão de Plataforma — Blueprint"
description: "Plugin, add-on, app ou customização sobre uma plataforma existente. Ex: Salesforce AppExchange, SAP addon, ServiceNow app, Shopify app, extensão de browser."
category: project-blueprint
type: platform-extension
status: rascunho
created: 2026-04-13
---

# Extensão de Plataforma

## Descrição

Plugin, add-on, app ou customização sobre uma plataforma existente. Ex: Salesforce AppExchange, SAP addon, ServiceNow app, Shopify app, extensão de browser. O projeto opera dentro dos limites e regras impostos pela plataforma hospedeira — APIs, SDKs, sandboxes, ciclos de review e políticas de publicação definem o que é possível e o que não é.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda extensão de plataforma é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Plugin de Marketplace (AppExchange, Shopify App Store)

Extensão publicada em marketplace oficial da plataforma, com processo de review e certificação obrigatório. O código precisa seguir as diretrizes do marketplace (segurança, UX, performance), passar por revisões manuais ou automatizadas, e o ciclo de publicação depende do SLA do review do marketplace. O foco é conformidade com as políticas de publicação e compatibilidade com as versões suportadas da plataforma. Exemplos: app Salesforce AppExchange, app Shopify App Store, plugin WordPress.org, extensão Atlassian Marketplace.

### V2 — Customização Interna (Tenant-Specific)

Extensão desenvolvida exclusivamente para o ambiente (tenant) de um único cliente, sem intenção de publicação em marketplace. O código opera dentro da instância do cliente e pode usar configurações e dados específicos daquele tenant. O foco é resolver um problema de negócio pontual usando as capacidades da plataforma, com menos restrições de review mas maior risco de acoplamento com customizações existentes. Exemplos: Lightning Component customizado para uma org Salesforce, flow customizado no ServiceNow, módulo ABAP para um mandante SAP específico.

### V3 — Extensão de Browser / Desktop

Extensão publicada nas stores de browsers (Chrome Web Store, Firefox Add-ons, Edge Add-ons) ou integrada a aplicações desktop. O ciclo de review e as políticas de permissão são definidos pela store do browser. O foco é lidar com as restrições de sandbox do browser (content scripts, background workers, manifest permissions) e com o ciclo de atualização automática que a store gerencia. Exemplos: extensão Chrome para produtividade, add-on Firefox para acessibilidade, plugin VS Code, extensão Figma.

### V4 — Conector / Integração (iPaaS, Middleware)

Extensão que conecta duas ou mais plataformas via APIs, webhooks ou filas de mensagens. Pode ser publicada em marketplace de iPaaS (Zapier, Make, Workato) ou operar como middleware interno. O foco é a confiabilidade da troca de dados entre sistemas, tratamento de erros e retries, e mapeamento de modelos de dados entre plataformas com esquemas diferentes. Exemplos: conector Zapier customizado, integração Workato, adapter MuleSoft, trigger customizado no Power Automate.

### V5 — Módulo ERP / CRM (SAP, Dynamics, Oracle)

Extensão pesada sobre ERP ou CRM enterprise, envolvendo transações customizadas, telas de cadastro, relatórios e jobs batch. Opera dentro do ecossistema técnico da plataforma (ABAP para SAP, X++ para Dynamics, PL/SQL para Oracle), com ciclos de transporte entre ambientes (dev → QA → produção) e forte dependência de consultores certificados na plataforma. Exemplos: addon SAP com transação Z, módulo Dynamics 365 com entidade customizada, extensão Oracle EBS.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Linguagem / SDK | Plataforma-alvo | Ambiente de Dev | Publicação | Observações |
|---|---|---|---|---|---|
| V1 — Plugin Marketplace | Apex/LWC, Liquid/React, PHP | Salesforce, Shopify, WordPress | Scratch Orgs, Shopify CLI, wp-env | Marketplace review + listing | Ciclo de review pode levar dias a semanas. Automação de testes é pré-requisito. |
| V2 — Customização Interna | Apex/LWC, JavaScript, ABAP, Power Fx | Salesforce, ServiceNow, SAP, Power Platform | Sandbox do tenant | Deploy direto no tenant | Sem review externo, mas precisa de change management interno. |
| V3 — Extensão Browser/Desktop | TypeScript/JavaScript, Manifest V3 | Chrome, Firefox, Edge, VS Code, Figma | Browser DevTools, vsce | Chrome Web Store, Firefox Add-ons | Manifest V3 obrigatório para Chrome desde 2024. Service Workers substituem background pages. |
| V4 — Conector/Integração | Node.js, Python, plataforma low-code | Zapier, Make, Workato, MuleSoft | CLI da plataforma iPaaS | Marketplace iPaaS ou deploy interno | Autenticação OAuth2 é padrão. Tratamento de rate limits é crítico. |
| V5 — Módulo ERP/CRM | ABAP, X++, PL/SQL, AL | SAP, Dynamics 365, Oracle, Business Central | Ambiente de desenvolvimento dedicado | Transporte entre ambientes (dev→QA→prod) | Consultores certificados geralmente obrigatórios. Ciclo de transporte é lento. |

---

## Etapa 01 — Inception

- **Origem da demanda e contexto de plataforma**: A necessidade geralmente surge de uma limitação funcional da plataforma base — o sistema padrão não atende um fluxo de negócio específico, ou existe um processo manual repetitivo que poderia ser automatizado dentro da plataforma. Entender o gatilho real é crucial porque frequentemente o cliente descreve a solução ("precisamos de um plugin") quando o correto seria entender o problema ("nossos vendedores perdem 2h/dia preenchendo dados em dois sistemas"). A raiz do problema pode revelar que a extensão não é a melhor abordagem — talvez uma configuração nativa da plataforma resolva, ou talvez o problema exija uma solução fora da plataforma.

- **Maturidade da plataforma base no cliente**: Antes de estender uma plataforma, é preciso entender o estado atual da instância do cliente. Uma org Salesforce com 200 custom objects, 50 flows e 10 pacotes gerenciados instalados é radicalmente diferente de uma org limpa recém-contratada. A extensão precisa coexistir com tudo que já existe — e conflitos com customizações anteriores (triggers concorrentes, campos com mesmo nome, automações que disparam em cadeia) são a maior causa de bugs em projetos de extensão de plataforma. Mapear o estado atual da instância é pré-requisito para estimar esforço com realismo.

- **Limites da plataforma como restrição de escopo**: Toda plataforma impõe limites técnicos — governor limits no Salesforce (consultas SOQL, DML statements, CPU time), quotas de API no Shopify (rate limits por app), tamanho máximo de pacote na Chrome Web Store, e limites de armazenamento no ServiceNow. Esses limites não são negociáveis e devem ser mapeados desde a Inception, porque podem inviabilizar abordagens que parecem razoáveis no papel. Um plugin que precisa processar 50.000 registros por transação no Salesforce vai esbarrar em governor limits e precisará de abordagem assíncrona (Batch Apex) desde o início.

- **Modelo de licenciamento e custo de plataforma**: O custo da extensão não é apenas o desenvolvimento — inclui o custo da plataforma base. Se o cliente ainda não tem a plataforma, ou se a extensão exige licenças adicionais (ex.: Platform Events no Salesforce, API add-on no ServiceNow), esse custo recorrente precisa ser apresentado na Inception. Extensões que dependem de features de licenças enterprise em plataformas onde o cliente tem licença básica podem ser inviáveis financeiramente.

- **Identificação do administrador da plataforma**: Todo projeto de extensão precisa de um administrador da plataforma do lado do cliente — alguém com acesso admin à instância, conhecimento das customizações existentes, e autoridade para aprovar mudanças de configuração. A ausência desse papel gera atrasos constantes: o dev precisa de permissão para criar um campo customizado, não sabe quem aprovar, escala para o gerente que escala para TI, que demora uma semana para responder. Identificar esse papel e confirmar sua disponibilidade é obrigatório.

- **Compatibilidade com roadmap da plataforma**: Plataformas enterprise lançam releases periódicos (Salesforce: 3x/ano, SAP: releases semestrais, Chrome: a cada 4 semanas) que podem depreciar APIs, mudar comportamentos, ou introduzir features nativas que tornam a extensão redundante. Verificar o roadmap público da plataforma para os próximos 6-12 meses evita construir algo que será substituído por funcionalidade nativa, ou que quebrará na próxima release por uso de API deprecada.

### Perguntas

1. Qual é o problema de negócio que a extensão deve resolver — e por que a funcionalidade nativa da plataforma não resolve? [fonte: Área de negócio, TI] [impacto: Arquiteto, PM]
2. Qual é a plataforma-base, qual versão/edição está em uso, e qual o nível de licenciamento atual do cliente? [fonte: TI, Administrador da plataforma] [impacto: Arquiteto, Dev]
3. Quem é o administrador da plataforma do lado do cliente e qual sua disponibilidade para o projeto? [fonte: TI, Diretoria] [impacto: PM, Dev]
4. Qual é o estado atual da instância — quantas customizações, pacotes instalados, automações ativas existem? [fonte: Administrador da plataforma, TI] [impacto: Arquiteto, Dev]
5. A extensão será publicada em marketplace ou usada exclusivamente no ambiente do cliente? [fonte: Diretoria, Produto] [impacto: Arquiteto, Dev, PM]
6. Existe orçamento para licenças adicionais de plataforma que a extensão possa exigir? [fonte: Financeiro, TI] [impacto: Arquiteto, PM]
7. Quais são os limites técnicos da plataforma relevantes para o caso de uso (governor limits, quotas de API, storage)? [fonte: TI, Administrador da plataforma] [impacto: Arquiteto, Dev]
8. Qual é o prazo esperado para entrega e existe alguma release de plataforma prevista nesse período que impacte o projeto? [fonte: TI, Diretoria] [impacto: PM, Dev]
9. Quantos usuários finais usarão a extensão e qual o perfil técnico deles (técnicos, analistas de negócio, executivos)? [fonte: RH, Área de negócio] [impacto: Designer, Dev]
10. A extensão precisa integrar com sistemas externos à plataforma-base (ERPs, APIs de terceiros, outros SaaS)? [fonte: TI, Área de negócio] [impacto: Arquiteto, Dev]
11. Existe alguma restrição de compliance ou segurança que afete o que pode ser instalado ou executado na plataforma? [fonte: Segurança, Compliance, DPO] [impacto: Arquiteto, Dev]
12. O cliente já teve experiências anteriores com extensões na mesma plataforma — houve problemas ou aprendizados? [fonte: TI, Administrador da plataforma] [impacto: PM, Arquiteto]
13. Existe uma janela de manutenção definida na plataforma que restrinja deploys ou migrações? [fonte: TI, Operações] [impacto: PM, DevOps]
14. Quem toma decisões técnicas sobre a plataforma — existe um comitê de arquitetura ou governança de TI? [fonte: Diretoria, TI] [impacto: Arquiteto, PM]
15. O roadmap da plataforma para os próximos 6-12 meses foi verificado para features que possam tornar a extensão redundante? [fonte: TI, Fornecedor da plataforma] [impacto: Arquiteto, PM, Produto]

---

## Etapa 02 — Discovery

- **Inventário de funcionalidades da plataforma**: Levantar o que a plataforma já oferece nativamente para o caso de uso — configurações padrão, workflows nativos, objetos/entidades existentes, e APIs disponíveis. Essa análise é obrigatória porque a extensão deve complementar a plataforma, não reimplementar funcionalidades que já existem. Reimplementar via código o que a plataforma faz via configuração resulta em extensão frágil (não se beneficia de atualizações automáticas da plataforma), cara (mais código para manter), e propensa a conflitos com futuras releases.

- **Mapeamento de customizações existentes**: Inventariar todas as customizações ativas na instância do cliente — campos customizados, objetos, triggers, flows, validations rules, processos automáticos, pacotes gerenciados de terceiros. Cada customização existente é um potencial ponto de conflito com a nova extensão. Triggers que disparam no mesmo evento podem causar loops infinitos, validations rules podem rejeitar dados que a extensão tenta inserir, e pacotes gerenciados podem consumir governor limits que a extensão precisa. Este inventário é o artefato mais importante do Discovery.

- **Modelo de dados da plataforma**: Mapear os objetos/entidades da plataforma que a extensão vai ler, escrever ou estender. Entender os relacionamentos entre objetos (lookup, master-detail, junction objects), os campos calculados que dependem dos dados afetados, e os índices existentes que impactam performance de consultas. Em plataformas como Salesforce, a forma como os objetos se relacionam define diretamente a estratégia de consulta (SOQL) e os limites de DML — uma escolha errada de relacionamento na modelagem pode gerar problemas de performance impossíveis de corrigir sem refatoração pesada.

- **Requisitos de integração com sistemas externos**: Identificar se a extensão precisa trocar dados com sistemas fora da plataforma — ERPs, bancos de dados legados, APIs de terceiros, serviços de e-mail, ou outras instâncias da mesma plataforma. Cada integração adiciona complexidade significativa: autenticação (OAuth2, API keys, certificados), tratamento de latência (callouts com timeout), limites de integração da plataforma (callout limits no Salesforce, API quotas no ServiceNow), e necessidade de retry/compensação quando a integração falha.

- **Requisitos de segurança e compliance da plataforma**: Plataformas enterprise têm modelos de segurança próprios — profiles, permission sets e sharing rules no Salesforce; roles e ACLs no ServiceNow; authorization objects no SAP. A extensão deve operar dentro do modelo de segurança existente, não contorná-lo. Verificar: quais perfis terão acesso à extensão, se há dados sensíveis envolvidos (PII, financeiros, saúde), se há requisitos regulatórios (LGPD, SOX, HIPAA) que impactam como os dados são armazenados e processados, e se a plataforma tem recursos nativos de auditoria que precisam ser preservados.

- **Fronteira entre extensão e aplicação standalone**: Verificar explicitamente se os requisitos cabem dentro dos limites da plataforma. Se a extensão precisa de processamento pesado que excede governor limits, armazenamento massivo que excede quotas, ou UX radicalmente diferente do padrão da plataforma, o projeto pode não ser uma extensão — pode ser uma aplicação standalone que se integra com a plataforma via API. Essa reclassificação muda completamente a arquitetura, o custo e o cronograma.

### Perguntas

1. Quais funcionalidades nativas da plataforma já existem para o caso de uso e por que são insuficientes? [fonte: Administrador da plataforma, Área de negócio] [impacto: Arquiteto, Dev]
2. Quantas customizações ativas existem na instância (campos, objetos, triggers, flows, pacotes gerenciados)? [fonte: Administrador da plataforma, TI] [impacto: Arquiteto, Dev]
3. Quais objetos/entidades da plataforma a extensão vai ler, escrever ou estender, e quais seus relacionamentos? [fonte: Administrador da plataforma, TI] [impacto: Dev, Arquiteto]
4. Existe integração com sistemas externos necessária e quais APIs/protocolos serão usados? [fonte: TI, Área de negócio] [impacto: Dev, Arquiteto]
5. Quais perfis de segurança terão acesso à extensão e há dados sensíveis (PII, financeiros) envolvidos? [fonte: Segurança, Compliance, TI] [impacto: Arquiteto, Dev]
6. Os requisitos de volume de dados (registros processados por transação, storage) cabem nos limites da plataforma? [fonte: TI, Administrador da plataforma] [impacto: Arquiteto, Dev]
7. Existe processo de negócio documentado (fluxograma, BPMN) que a extensão precisa suportar? [fonte: Área de negócio, Processos] [impacto: Dev, PM]
8. Quais são os requisitos de UX — a extensão deve seguir o design system da plataforma ou tem liberdade visual? [fonte: Área de negócio, Designer] [impacto: Designer, Dev]
9. Há requisitos de internacionalização (múltiplos idiomas, fusos horários, moedas) dentro da plataforma? [fonte: Área de negócio, TI] [impacto: Dev]
10. Quais são os requisitos de relatórios e dashboards — a extensão precisa alimentar reports nativos da plataforma? [fonte: Área de negócio, Gestão] [impacto: Dev, Arquiteto]
11. Existe necessidade de processamento assíncrono (batch, filas, scheduled jobs) para volumes grandes? [fonte: TI, Área de negócio] [impacto: Arquiteto, Dev]
12. O projeto substitui uma extensão ou customização existente que precisa ser desativada ou migrada? [fonte: Administrador da plataforma, TI] [impacto: Dev, PM]
13. Há requisitos de auditoria (quem alterou o quê, quando) além do que a plataforma oferece nativamente? [fonte: Compliance, Segurança] [impacto: Dev, Arquiteto]
14. Qual é o volume de usuários concorrentes esperado e há picos sazonais de uso que impactem performance? [fonte: Área de negócio, TI] [impacto: Arquiteto, Dev]
15. Os requisitos cabem inteiramente dentro dos limites da plataforma ou há indicação de que deveria ser uma aplicação standalone? [fonte: TI, Arquiteto] [impacto: Arquiteto, PM, Dev]

---

## Etapa 03 — Alignment

- **Governança de mudanças na plataforma**: Definir formalmente o processo de aprovação de mudanças na instância da plataforma — quem solicita, quem revisa, quem aprova, e qual o SLA de aprovação. Em organizações enterprise, mudanças na plataforma passam por Change Advisory Board (CAB) ou comitê de governança de TI, com reuniões semanais ou quinzenais. Se o projeto depende de aprovações do CAB para deploy de cada incremento, o cronograma precisa refletir esse ciclo — uma sprint de duas semanas pode resultar em apenas um deploy se o CAB só se reúne na quarta-feira.

- **Estratégia de versionamento e compatibilidade**: Alinhar como a extensão será versionada e como lidará com atualizações da plataforma base. Plataformas como Salesforce têm 3 releases por ano que podem depreciar APIs ou mudar comportamentos. A extensão precisa de estratégia para testar compatibilidade com novas releases (sandbox de preview), para manter versões anteriores quando necessário (marketplace), e para comunicar breaking changes aos usuários. Sem essa estratégia, cada release da plataforma se torna uma emergência.

- **Separação de responsabilidades entre dev e admin**: Alinhar o que será implementado via código (Apex, LWC, ABAP, etc.) e o que será implementado via configuração da plataforma (declarativo — flows, validation rules, page layouts, profiles). A fronteira entre código e configuração define quem mantém cada parte após o go-live. Se o administrador da plataforma do cliente pode manter as partes declarativas, o custo de manutenção cai significativamente. Se tudo for código, qualquer alteração pós-launch requer desenvolvedor — o que é mais caro e mais lento.

- **Ambiente de desenvolvimento e sandbox strategy**: Alinhar a estratégia de ambientes para o projeto. Plataformas enterprise oferecem diferentes tipos de sandbox (Salesforce: Developer, Developer Pro, Partial Copy, Full Copy; SAP: mandantes de desenvolvimento, QA e produção). O tipo de sandbox impacta diretamente o que é possível testar — um Developer sandbox não tem dados reais, então testes de performance e migração exigem Partial ou Full Copy. O custo de sandboxes adicionais deve ser previsto no orçamento.

- **Critérios de review do marketplace (se aplicável)**: Se a extensão será publicada em marketplace, levantar e documentar todos os critérios de review antes de iniciar o build. Cada marketplace tem regras específicas — a Salesforce exige Security Review com scan de código obrigatório, a Chrome Web Store exige justificativa para cada permissão declarada no manifest, a Shopify exige conformidade com Polaris design system. Falhar no review após o build completo é custoso — pode exigir refatoração arquitetural.

### Perguntas

1. O processo de aprovação de mudanças na plataforma (CAB, governança de TI) foi mapeado com SLA de aprovação documentado? [fonte: TI, Governança] [impacto: PM, Dev]
2. A estratégia de versionamento da extensão frente a releases da plataforma-base foi acordada? [fonte: TI, Administrador da plataforma] [impacto: Dev, Arquiteto]
3. A fronteira entre código customizado e configuração declarativa foi definida com justificativa documentada? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev, Admin]
4. A estratégia de sandboxes/ambientes foi definida e os custos de ambientes adicionais estão previstos no orçamento? [fonte: TI, Financeiro] [impacto: Dev, PM]
5. Se marketplace: os critérios de review foram levantados e documentados antes do início do build? [fonte: Documentação do marketplace, Fornecedor da plataforma] [impacto: Dev, Arquiteto, QA]
6. O modelo de segurança da extensão (profiles, permissions, sharing rules) foi alinhado com o modelo existente da plataforma? [fonte: Administrador da plataforma, Segurança] [impacto: Dev, Arquiteto]
7. Os stakeholders concordam com o escopo do MVP e entendem quais funcionalidades ficam para versões futuras? [fonte: Diretoria, Área de negócio] [impacto: PM, Dev]
8. O time de desenvolvimento tem certificações ou experiência comprovada na plataforma-alvo? [fonte: TI, RH] [impacto: PM, Dev]
9. O SLA de suporte pós-lançamento foi definido (quem mantém a extensão, tempo de resposta, modelo de contrato)? [fonte: Diretoria, TI] [impacto: PM, Dev]
10. A estratégia de rollback em caso de problema pós-deploy foi alinhada com a governança de mudanças? [fonte: TI, Governança] [impacto: Dev, DevOps, PM]
11. O treinamento do administrador da plataforma e dos usuários finais foi planejado e orçado? [fonte: RH, TI] [impacto: PM, Dev]
12. Dependências de terceiros (pacotes gerenciados, APIs externas) foram listadas com alternativas em caso de indisponibilidade? [fonte: TI, Fornecedores] [impacto: Arquiteto, Dev]
13. O time de QA tem acesso à plataforma e conhecimento suficiente para testar dentro do ecossistema? [fonte: QA, TI] [impacto: QA, PM]
14. Existe processo definido para revisão e aprovação de entregas parciais durante o build (demo, sprint review)? [fonte: Diretoria, Área de negócio] [impacto: PM, Dev]
15. O cliente foi informado sobre o impacto de mudanças de escopo no prazo, custo e risco de rejeição no marketplace review? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Especificação funcional alinhada com a plataforma**: Produzir a especificação funcional detalhada mapeando cada requisito para a capacidade correspondente da plataforma — quais objetos/entidades serão criados ou estendidos, quais campos customizados são necessários, quais automações (triggers, flows, webhooks) serão implementadas, e quais telas ou componentes de UI serão desenvolvidos. A especificação deve usar a terminologia da plataforma (ex.: "Lightning Web Component" e não "componente frontend"), porque a equipe de review do marketplace e o administrador do cliente pensam nesses termos.

- **Modelo de dados customizado**: Definir formalmente cada objeto/entidade customizado com seus campos (nome, tipo, obrigatório/opcional, valores padrão, validações), relacionamentos com objetos nativos e customizados existentes, e regras de compartilhamento (sharing rules). Em plataformas como Salesforce, o modelo de dados define automaticamente grande parte da UI (page layouts) e da segurança (OWD, sharing). Uma decisão errada de relacionamento (lookup vs. master-detail) impacta cascading deletes, roll-up summaries, e segurança herdada — e é dolorosa de corrigir depois que há dados em produção.

- **Mapeamento de automações e side-effects**: Documentar todos os pontos onde a extensão dispara automações (before/after insert, before/after update, scheduled triggers) e verificar se existem automações existentes nos mesmos pontos. Duas automações no mesmo evento podem gerar resultados imprevisíveis — especialmente em plataformas onde a ordem de execução não é garantida (Salesforce flows vs. triggers). O mapeamento deve incluir side-effects: envio de e-mails, chamadas externas (callouts), atualizações em cadeia em objetos relacionados, e publicação de eventos.

- **Especificação de permissões e perfis**: Definir a matriz de permissões por perfil de usuário — quais objetos cada perfil pode ler, criar, editar e deletar, quais campos são visíveis, quais ações são permitidas, e quais dashboards ou relatórios são acessíveis. Em plataformas enterprise, a granularidade de permissões é alta e a configuração é complexa. Definir antes do build evita o padrão "dar admin para todo mundo" no sandbox e descobrir em produção que os perfis reais não têm acesso ao que precisam.

- **Wireframes respeitando o design system da plataforma**: Se a plataforma tem design system oficial (Salesforce Lightning Design System, Shopify Polaris, SAP Fiori Design Guidelines), os wireframes e protótipos devem seguir esses guidelines desde a definição. Componentes customizados que ignoram o design system da plataforma resultam em UX inconsistente para o usuário e em rejeição no review de marketplace. O grau de customização visual permitido varia por plataforma — no Salesforce é relativamente alto, no Shopify é mais restrito.

- **Plano de migração de dados (se aplicável)**: Se a extensão substitui uma customização anterior ou importa dados de um sistema externo, definir o plano de migração: volume de registros, mapeamento campo a campo entre origem e destino, regras de transformação, validações pós-migração, e estratégia de rollback se a migração falhar. Migrações em plataformas enterprise são especialmente sensíveis porque triggers e automações existentes disparam durante a importação — o que pode causar efeitos colaterais massivos se não forem desativados temporariamente.

### Perguntas

1. A especificação funcional usa a terminologia e os conceitos da plataforma-alvo (objetos, componentes, automações)? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev, QA]
2. O modelo de dados customizado foi definido campo a campo com tipos, validações, relacionamentos e regras de compartilhamento? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev]
3. Todas as automações (triggers, flows, webhooks) foram mapeadas com verificação de conflito com automações existentes? [fonte: Administrador da plataforma, Arquiteto] [impacto: Dev]
4. A matriz de permissões por perfil de usuário foi definida formalmente com todos os objetos e ações? [fonte: Administrador da plataforma, Segurança] [impacto: Dev]
5. Os wireframes seguem o design system oficial da plataforma (SLDS, Polaris, Fiori)? [fonte: Designer, Documentação da plataforma] [impacto: Dev, Designer]
6. O plano de migração de dados foi definido com volume, mapeamento de campos, regras de transformação e rollback? [fonte: TI, Administrador da plataforma] [impacto: Dev, PM]
7. Todos os limites técnicos da plataforma foram verificados contra os requisitos (governor limits, API quotas, storage)? [fonte: Arquiteto, Documentação da plataforma] [impacto: Dev]
8. Os critérios de aceitação de cada funcionalidade foram definidos em linguagem que permita teste automatizado? [fonte: Área de negócio, QA] [impacto: QA, Dev]
9. As dependências de pacotes gerenciados ou bibliotecas de terceiros foram listadas com versões e licenças verificadas? [fonte: Arquiteto, TI] [impacto: Dev]
10. O comportamento esperado em cenários de erro (timeout de API, dados inválidos, permissão negada) foi especificado? [fonte: Arquiteto, Área de negócio] [impacto: Dev, QA]
11. Os relatórios e dashboards necessários foram especificados com campos, filtros, agrupamentos e perfis de acesso? [fonte: Área de negócio, Gestão] [impacto: Dev]
12. A estratégia de logging e monitoramento dentro da plataforma foi definida (debug logs, custom logs, alertas)? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
13. Os fluxos de notificação (e-mails, push, in-app) foram especificados com templates, triggers e destinatários? [fonte: Área de negócio] [impacto: Dev]
14. As regras de validação de dados de entrada foram especificadas para cada campo e cada cenário de submissão? [fonte: Área de negócio, Arquiteto] [impacto: Dev, QA]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders e pelo administrador da plataforma? [fonte: Diretoria, TI, Administrador da plataforma] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Decisões de arquitetura dentro dos limites da plataforma**: A arquitetura de uma extensão de plataforma é fundamentalmente diferente de uma aplicação standalone — o "teto" técnico é definido pela plataforma, não pelo arquiteto. Decisões como uso de processamento síncrono vs. assíncrono (Apex síncrono vs. Batch Apex, ABAP dialog vs. background), armazenamento em objetos customizados vs. big objects vs. external objects, e comunicação via Platform Events vs. callouts diretos são limitadas pelo que a plataforma oferece. A arquitetura deve maximizar o uso de primitivas nativas da plataforma — quanto mais nativo, mais fácil de manter e menos provável de quebrar em atualizações.

- **Padrão de separação de camadas**: Mesmo dentro de uma plataforma, a separação de responsabilidades é crítica. Em Salesforce: trigger handlers desacoplados dos triggers, service layer para lógica de negócio reutilizável, selector layer para queries, e domain layer para validações. Em SAP: separação entre dialog programs e function modules, com lógica de negócio em classes ABAP OO. A ausência de camadas resulta em "God triggers" com milhares de linhas que ninguém entende ou consegue testar — o anti-pattern mais comum em extensões de plataforma enterprise.

- **Estratégia de testes automatizados**: Plataformas enterprise exigem cobertura mínima de testes para deploy em produção (Salesforce: 75% de cobertura Apex obrigatório). Mas cobertura não é qualidade — 75% de cobertura com asserts vazios não detecta nenhum bug. A estratégia de testes deve definir: testes unitários para cada service/domain class, testes de integração para fluxos completos (criar → processar → verificar resultado), testes de bulk (inserir 200 registros de uma vez para validar governor limits), e mocks para callouts externos. A arquitetura deve ser testável desde o início — se não é possível instanciar um componente isoladamente para teste, a arquitetura precisa mudar.

- **Estratégia de empacotamento e distribuição**: Se a extensão será publicada em marketplace, definir o tipo de pacote (Salesforce: Managed Package 2GP, Unlocked Package; Shopify: App com instalação via OAuth; Chrome: Extension com manifest.json). O tipo de pacote define o que pode e o que não pode ser modificado pelo cliente após instalação, como upgrades são distribuídos, e qual é o processo de review. Managed Packages no Salesforce protegem o código-fonte — o cliente não pode ver ou alterar — mas limitam a flexibilidade. Unlocked Packages permitem mais flexibilidade mas expõem o código.

- **Estratégia de tratamento de erros e resiliência**: Extensões que dependem de integrações externas precisam de estratégia robusta para falhas — retry com backoff exponencial, circuit breaker para APIs instáveis, dead letter queue para mensagens que falharam após retry, e alertas automáticos para o admin quando erros persistem. Plataformas como Salesforce oferecem mecanismos nativos (Platform Events para retry, Limits class para verificar governor limits antes de operar), mas eles precisam ser arquitetados desde o início — não é algo que se adiciona depois.

- **Estratégia de performance com governor limits**: Em plataformas com limites de execução por transação (Salesforce, ServiceNow), a performance não é sobre otimizar código — é sobre não exceder limites. A arquitetura deve prever: bulkificação de todas as operações (nunca query/DML dentro de loop), uso de coleções e maps ao invés de queries repetidas, processamento assíncrono para operações pesadas, e monitoramento de consumo de limites em tempo de execução. Uma transação que consome 90% do limite de CPU em cenário de teste vai falhar em produção com mais dados e automações concorrentes.

### Perguntas

1. A arquitetura maximiza o uso de primitivas nativas da plataforma ou depende excessivamente de código customizado? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev, Arquiteto]
2. A separação de camadas (trigger handler, service, selector, domain) está definida e o time concorda com o padrão? [fonte: Arquiteto, Dev] [impacto: Dev]
3. A estratégia de testes automatizados cobre unitários, integração, bulk e mocks para callouts? [fonte: Arquiteto, QA] [impacto: Dev, QA]
4. O tipo de pacote/distribuição foi escolhido com base nos requisitos de proteção de código e flexibilidade do cliente? [fonte: Arquiteto, Produto] [impacto: Dev, PM]
5. A estratégia de tratamento de erros inclui retry, circuit breaker e alertas para o admin? [fonte: Arquiteto] [impacto: Dev]
6. Todas as operações que acessam dados estão bulkificadas e livres de queries/DML dentro de loops? [fonte: Arquiteto, Dev] [impacto: Dev]
7. A arquitetura foi validada contra os governor limits da plataforma em cenário de pior caso (volume máximo, automações concorrentes)? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev]
8. A estratégia de comunicação entre componentes (events, callbacks, pubsub) foi definida e é suportada nativamente? [fonte: Arquiteto] [impacto: Dev]
9. Se marketplace: a arquitetura passa nos critérios de security review da plataforma (sem SOQL injection, sem XSS, com FLS enforcement)? [fonte: Arquiteto, Documentação do marketplace] [impacto: Dev, QA]
10. A estratégia de migração de dados inclui desativação temporária de triggers/automações durante a importação? [fonte: Arquiteto, Administrador da plataforma] [impacto: Dev]
11. Os custos de infraestrutura foram calculados (sandboxes, ambientes, licenças adicionais) em cenário esperado e pior caso? [fonte: Financeiro, TI] [impacto: PM]
12. A extensão pode ser desinstalada de forma limpa sem deixar resíduos (objetos órfãos, dados inacessíveis)? [fonte: Arquiteto] [impacto: Dev, Admin]
13. A arquitetura suporta versionamento e upgrade sem perda de dados ou indisponibilidade? [fonte: Arquiteto] [impacto: Dev, DevOps]
14. A estratégia de logging permite diagnóstico de problemas em produção sem acesso direto ao ambiente do cliente? [fonte: Arquiteto] [impacto: Dev, Suporte]
15. O modelo de branches, ambientes (sandbox dev → sandbox QA → produção) e ciclo de deploy foi documentado e aprovado? [fonte: Arquiteto, TI] [impacto: Dev, DevOps, PM]

---

## Etapa 06 — Setup

- **Configuração dos ambientes de sandbox**: Provisionar os sandboxes necessários conforme a estratégia definida na Etapa 05. Cada tipo de sandbox serve um propósito distinto: Developer para desenvolvimento isolado, Partial Copy para testes com subset de dados reais, Full Copy para testes de performance e migração com volume real. A configuração deve incluir replicação das customizações relevantes de produção no sandbox — sem isso, o dev trabalha em ambiente "limpo" e a extensão falha ao encontrar as customizações do cliente em produção.

- **Setup do ambiente de desenvolvimento local**: Configurar o ambiente de desenvolvimento que conecta com a plataforma. Para Salesforce: VS Code com Salesforce Extension Pack, Salesforce CLI (sf), conexão com scratch org ou sandbox, configuração de manifests (sfdx-project.json). Para Shopify: Shopify CLI, tema de desenvolvimento, configuração de app partner. Para Chrome: setup de carregamento de extensão não empacotada via chrome://extensions. O tempo de setup de ambiente em plataformas enterprise é significativamente maior que em projetos web tradicionais — pode levar dias se envolver aprovações de acesso.

- **Configuração do pipeline de CI/CD**: Adaptar o pipeline de CI/CD ao modelo de deploy da plataforma. Em Salesforce: source push para scratch orgs, package version creation, e deploy para sandbox/produção via GitHub Actions ou equivalente. Em SAP: configurar transporte entre mandantes (SE09/SE10, CTS+). Cada commit deve disparar: lint de código (PMD para Apex, ESLint para LWC), execução de testes automatizados na plataforma (não apenas testes locais), e validação de pacote. O pipeline deve incluir um step de validate-only deploy que verifica se o deploy será aceito sem efetivamente aplicar as mudanças.

- **Configuração de permissões e acessos do time**: Garantir que cada membro do time tem o nível de acesso correto à plataforma — desenvolvedores precisam de acesso de deploy ao sandbox, testers precisam de acesso de leitura/escrita aos dados de teste, o PM precisa de acesso de visualização para acompanhar progresso. Em ambientes enterprise, a concessão de acessos pode demorar dias ou semanas se depende de processos formais de TI. Solicitar todos os acessos necessários com antecedência é obrigatório.

- **Seed data e dados de teste**: Popular os ambientes de desenvolvimento e teste com dados representativos. Extensões de plataforma dependem fortemente de dados existentes — uma extensão que processa pedidos precisa de pedidos no sandbox para funcionar. Criar scripts de geração de dados de teste (Data Factory) que criam cenários completos (objetos pai + filhos + relacionamentos) com um comando é investimento que se paga ao longo do projeto — especialmente quando scratch orgs são descartáveis e precisam ser populadas frequentemente.

- **Configuração de monitoramento e debug**: Configurar as ferramentas de debug e monitoramento da plataforma — Debug Logs no Salesforce (com níveis de log configurados por usuário), system logs no ServiceNow, traces no SAP (ST05, ST12). Verificar que os logs capturam informações suficientes para diagnóstico sem gerar volume excessivo que impacte performance. Configurar alertas para exceções não tratadas e para consumo de governor limits acima de thresholds definidos (ex.: alerta se uma transação consumir mais de 80% do CPU time limit).

### Perguntas

1. Os sandboxes foram provisionados com as customizações de produção replicadas e dados de teste representativos? [fonte: Administrador da plataforma, TI] [impacto: Dev]
2. O ambiente de desenvolvimento local foi configurado e todos os devs conseguem fazer deploy no sandbox de desenvolvimento? [fonte: Dev] [impacto: Dev]
3. O pipeline de CI/CD inclui lint, testes automatizados na plataforma, e validate-only deploy? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
4. Todos os membros do time têm os acessos necessários à plataforma com os perfis de permissão corretos? [fonte: TI, Administrador da plataforma] [impacto: Dev, QA, PM]
5. Os scripts de geração de dados de teste (Data Factory) foram criados e testados para todos os cenários relevantes? [fonte: Dev, QA] [impacto: Dev, QA]
6. As ferramentas de debug e monitoramento da plataforma estão configuradas com níveis de log apropriados? [fonte: Dev, Administrador da plataforma] [impacto: Dev]
7. O .gitignore e as políticas de repositório estão configurados para excluir credenciais, tokens e metadados locais? [fonte: Dev] [impacto: Dev, Segurança]
8. O manifesto do pacote/projeto (sfdx-project.json, manifest.json, package.json) está configurado e versionado? [fonte: Dev] [impacto: Dev]
9. O process de deploy entre ambientes (dev → QA → produção) foi testado end-to-end com um incremento real? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
10. Os webhooks ou integrações externas estão configurados com variáveis de ambiente separadas por ambiente? [fonte: Dev] [impacto: Dev, DevOps]
11. O processo de onboarding de novos desenvolvedores foi documentado com instruções de setup do ambiente? [fonte: Dev] [impacto: Dev]
12. O ambiente de QA está funcional, isolado do desenvolvimento, e com dados representativos para testes? [fonte: QA, Dev] [impacto: QA]
13. As licenças e permissões necessárias na plataforma foram ativadas para todos os ambientes? [fonte: TI, Financeiro] [impacto: Dev, PM]
14. Os alertas de monitoramento (exceções, consumo de governor limits) estão configurados e testados? [fonte: Dev, Administrador da plataforma] [impacto: Dev, DevOps]
15. O fluxo completo de commit → CI → deploy no sandbox foi validado com sucesso pelo menos uma vez? [fonte: Dev] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Implementação seguindo padrões da plataforma**: Desenvolver seguindo os padrões arquiteturais definidos na Etapa 05 — separation of concerns, trigger handlers, service layer. Cada componente deve ser implementado com os idioms da plataforma: em Salesforce, usar LWC ao invés de Aura (que está em maintenance mode), usar Apex com bulkificação nativa, usar Custom Metadata Types ao invés de Custom Settings para configurações. Ignorar os padrões da plataforma gera dívida técnica que é muito mais cara de resolver em plataformas enterprise do que em projetos web — porque refatorar código em produção requer novo ciclo de deploy com riscos.

- **Desenvolvimento com governor limits em mente**: Cada linha de código deve considerar os limites de execução. Nunca fazer query dentro de loop (trigger com 200 registros = 200 queries = estoura o limite de 100 SOQL queries). Nunca fazer callout dentro de loop. Nunca instanciar componentes de UI desnecessariamente. Esses erros não aparecem em testes com 1 registro — aparecem em produção com 200 registros no trigger, causando exceções não tratadas e perda de dados. Code review focado em governor limits é tão importante quanto code review funcional.

- **Testes automatizados com cobertura real**: Implementar testes que validam comportamento, não apenas cobertura. Cada test method deve ter asserts explícitos verificando resultado esperado. Testes de bulk são obrigatórios — inserir 200 registros de uma vez para validar que triggers e automações respeitam governor limits em volume. Mocks para callouts externos devem simular cenários de sucesso, erro e timeout. A cobertura mínima da plataforma (75% no Salesforce) é baseline — o target deve ser 85-90% com cobertura de cenários positivos e negativos.

- **Integração com automações existentes**: Durante o build, testar continuamente a coexistência da extensão com as customizações existentes na instância. Ativar a extensão em sandbox com as automações de produção ativas e verificar: triggers que disparam em cadeia, flows que competem por execução, validation rules que rejeitam dados da extensão, e processos agendados que interferem com jobs da extensão. Este teste contínuo evita a descoberta tardia de conflitos que são muito mais caros de resolver quando o build está completo.

- **UX consistente com a plataforma**: Implementar a UI usando os componentes nativos da plataforma sempre que possível — Lightning Web Components base no Salesforce, Polaris components no Shopify, Fiori elements no SAP. Componentes customizados só devem existir quando não há equivalente nativo. A consistência visual com a plataforma reduz a curva de aprendizado do usuário (que já conhece os padrões da plataforma) e reduz o risco de rejeição no review de marketplace.

- **Documentação inline e metadados**: Documentar o código com comentários que expliquem o "porquê" (não o "o quê") e manter os metadados da plataforma atualizados — descriptions em objetos e campos customizados, help text em campos de formulário, tooltips em componentes de UI. Em plataformas enterprise, o administrador que vai manter a extensão após o go-live depende dessa documentação para entender o que cada campo e automação faz — sem ela, qualquer manutenção requer o desenvolvedor original.

### Perguntas

1. O código segue os padrões da plataforma definidos na Etapa 05 (separation of concerns, naming conventions, idioms)? [fonte: Arquiteto, Dev] [impacto: Dev]
2. Todas as operações de dados estão bulkificadas e livres de queries/DML dentro de loops? [fonte: Dev, Arquiteto] [impacto: Dev, QA]
3. Os testes automatizados cobrem cenários positivos, negativos e de bulk com asserts explícitos? [fonte: Dev, QA] [impacto: Dev, QA]
4. A extensão foi testada com as automações existentes de produção ativas no sandbox de desenvolvimento? [fonte: Dev, Administrador da plataforma] [impacto: Dev]
5. A UI utiliza componentes nativos da plataforma e segue o design system oficial? [fonte: Designer, Dev] [impacto: Dev, Designer]
6. Os metadados da plataforma (descriptions, help text, tooltips) estão preenchidos em todos os campos e objetos customizados? [fonte: Dev] [impacto: Admin, Conteúdo]
7. Os callouts externos têm tratamento de erro (retry, timeout, fallback) implementado e testado? [fonte: Dev] [impacto: Dev, QA]
8. O code review focou em governor limits, segurança (FLS, CRUD, injection) e padrões da plataforma? [fonte: Dev, Arquiteto] [impacto: Dev]
9. Os componentes de UI são responsivos e funcionam em todos os form factors suportados pela plataforma (desktop, tablet, mobile)? [fonte: Dev, Designer] [impacto: Dev, QA]
10. A migração de dados (se aplicável) foi testada com volume representativo e validação pós-migração automatizada? [fonte: Dev, QA] [impacto: Dev, PM]
11. O processamento assíncrono (batch, queueable, scheduled) foi implementado com mecanismo de monitoramento e reprocessamento? [fonte: Dev] [impacto: Dev]
12. As permissões e perfis foram configurados e validados — cada perfil acessa exatamente o que deve (nem mais, nem menos)? [fonte: Dev, Administrador da plataforma] [impacto: Dev, Segurança]
13. A extensão pode ser instalada/ativada e desinstalada/desativada sem efeitos colaterais em dados ou automações existentes? [fonte: Dev, Arquiteto] [impacto: Dev, Admin]
14. Os relatórios e dashboards estão implementados e populados com dados de teste que validam a exibição correta? [fonte: Dev, Área de negócio] [impacto: Dev]
15. O progresso do build está sendo comunicado e demonstrado regularmente para os stakeholders (demos, sprint reviews)? [fonte: PM, Área de negócio] [impacto: PM, Dev]

---

## Etapa 08 — QA

- **Testes funcionais em sandbox com dados reais**: Executar os testes funcionais em sandbox Partial Copy ou Full Copy, com dados que representam o volume e a variedade de produção. Extensões que funcionam perfeitamente com 10 registros de teste podem falhar com 100.000 registros reais — queries sem índice, batch jobs que excedem tempo, e UIs que congelam com listagens grandes. O QA em sandbox limpo é insuficiente — é preciso testar com a "sujeira" real dos dados de produção (campos nulos, registros sem relacionamento, dados inconsistentes herdados de migrações anteriores).

- **Testes de regressão nas funcionalidades existentes**: Verificar que a extensão não quebrou funcionalidades existentes da plataforma. Executar o test suite completo da org (não apenas os testes da extensão), verificar que flows existentes continuam funcionando, que relatórios existentes retornam resultados corretos, e que integrações existentes não foram afetadas. Este teste é frequentemente negligenciado — o time testa a extensão nova mas não verifica que o sistema existente continua íntegro.

- **Testes de performance e governor limits**: Executar cenários de pior caso: trigger processando o máximo de registros por transação (200 no Salesforce), jobs batch com volume máximo, callouts com latência alta (simular com delay), e operações concorrentes de múltiplos usuários. Monitorar consumo de governor limits durante cada cenário — se qualquer transação consome mais de 70% de qualquer limite, é risco de falha em produção onde automações concorrentes consomem parte do limite. Usar ferramentas de profiling da plataforma (Debug Logs com nível FINEST, Developer Console, SAP ST12).

- **Security review e compliance**: Se marketplace: executar o scan de segurança exigido pela plataforma antes de submeter para review. No Salesforce: Checkmarx/PMD scan para SOQL injection, XSS, FLS enforcement, CRUD checks. Na Chrome Web Store: verificar justificativas de permissões, política de privacidade, e compliance com Chrome Web Store policies. Mesmo sem marketplace, executar verificações de segurança: dados sensíveis não expostos em logs, permissões mínimas aplicadas (principle of least privilege), e inputs sanitizados contra injection.

- **Testes de upgrade e compatibilidade**: Se a extensão será versionada (marketplace ou internal distribution), testar o cenário de upgrade: instalar a versão anterior, popular com dados, executar o upgrade para a nova versão, e verificar que dados e configurações são preservados. Em plataformas com releases periódicos, testar a extensão no sandbox de preview da próxima release da plataforma para antecipar incompatibilidades.

- **User Acceptance Testing (UAT) com usuários reais**: Colocar a extensão nas mãos dos usuários finais reais — não apenas do product owner ou do gerente. Usuários reais descobrem problemas que testers profissionais não encontram: fluxos inesperados, interpretações diferentes de labels, erros em cenários de negócio que não foram mapeados, e feedback de usabilidade que impacta adoção. O UAT deve ter critérios de aceite formais — não é "brincar no sistema" e dizer "tá bom".

### Perguntas

1. Os testes funcionais foram executados em sandbox com dados representativos de produção (volume e variedade)? [fonte: QA, Administrador da plataforma] [impacto: QA, Dev]
2. O test suite completo da org foi executado para verificar que funcionalidades existentes não foram afetadas? [fonte: QA, Administrador da plataforma] [impacto: QA, Dev]
3. Os testes de governor limits foram executados com cenário de pior caso (200 registros por trigger, batch máximo)? [fonte: QA, Dev] [impacto: Dev, QA]
4. O scan de segurança foi executado e todos os achados foram corrigidos ou justificados? [fonte: Dev, Segurança] [impacto: Dev, QA]
5. O cenário de upgrade (versão anterior → nova versão) foi testado com preservação de dados confirmada? [fonte: QA, Dev] [impacto: Dev]
6. O UAT foi realizado com usuários finais reais e os critérios de aceite formais foram atendidos? [fonte: Área de negócio, QA] [impacto: PM, Dev]
7. Os callouts externos foram testados com cenários de falha (timeout, erro 500, serviço indisponível)? [fonte: QA, Dev] [impacto: Dev]
8. As permissões foram validadas por perfil — cada perfil acessa exatamente o permitido e nada mais? [fonte: QA, Segurança] [impacto: Dev, Segurança]
9. A migração de dados foi validada com verificação automatizada de integridade pós-migração? [fonte: QA, Dev] [impacto: Dev, PM]
10. A extensão foi testada no sandbox de preview da próxima release da plataforma? [fonte: QA, Dev] [impacto: Dev]
11. Os relatórios e dashboards retornam dados corretos e performance aceitável com volume representativo? [fonte: QA, Área de negócio] [impacto: Dev]
12. Os fluxos de erro (dados inválidos, permissão negada, timeout) mostram mensagens claras e acionáveis ao usuário? [fonte: QA, Designer] [impacto: Dev]
13. O comportamento da extensão com múltiplos usuários concorrentes foi testado sem deadlocks ou racing conditions? [fonte: QA, Dev] [impacto: Dev]
14. A documentação de usuário (guia de uso, FAQ, troubleshooting) foi revisada e está completa? [fonte: QA, PM] [impacto: PM, Conteúdo]
15. Todos os bugs encontrados foram classificados por severidade e os críticos foram corrigidos e re-testados? [fonte: QA, PM] [impacto: Dev, PM]

---

## Etapa 09 — Launch Prep

- **Submissão para review de marketplace (se aplicável)**: Submeter o pacote para review com antecedência suficiente — o SLA de review varia por marketplace (Salesforce AppExchange: 2-6 semanas para security review, Chrome Web Store: 1-5 dias, Shopify: 7-14 dias). A submissão deve incluir todos os artefatos exigidos: descrição do app, screenshots, vídeo demonstrativo, política de privacidade, documentação de uso, e contato de suporte. Rejeições são comuns na primeira submissão — planejar pelo menos 2 ciclos de review no cronograma para acomodar correções e resubmissão.

- **Plano de deploy em produção**: Documentar a sequência exata de ações para o deploy: quem executa, em que horário, qual a janela de manutenção, quais os pré-requisitos (desativar automações temporariamente, comunicar usuários), quais validações pós-deploy, e qual o critério de sucesso. Em plataformas enterprise, o deploy não é "merge para main" — é uma sequência de transportes entre ambientes com aprovações formais que pode levar horas. Cada step deve ter um responsável designado e um checkpoint de validação.

- **Plano de rollback da plataforma**: Documentar o plano de rollback específico para a plataforma — em Salesforce, como reverter um managed package (uninstall) ou um deploy (redeploy da versão anterior via source tracking), em SAP como reverter um transporte (contra-transporte), em Chrome como reverter uma versão na Chrome Web Store. O rollback em plataformas enterprise é mais complexo que em web apps porque pode envolver dados (registros criados durante o período) que precisam ser tratados na reversão.

- **Comunicação e change management**: Preparar a comunicação para todos os afetados pelo go-live: usuários finais (o que muda, quando muda, onde buscar ajuda), administradores da plataforma (o que foi instalado, o que monitorar, como reportar problemas), e gestores (quais os resultados esperados, como medir sucesso). Em plataformas enterprise com centenas de usuários, a comunicação inadequada resulta em ligações ao helpdesk, resistência à mudança, e percepção negativa da extensão antes mesmo de ser usada.

- **Treinamento de usuários finais e administradores**: Realizar treinamento diferenciado por perfil — usuários finais recebem treinamento focado em "como usar" com hands-on no sandbox, administradores recebem treinamento focado em "como configurar e troubleshootar" com acesso a logs e documentação técnica. Entregar material de referência (guia rápido, FAQ, vídeos curtos) que os usuários possam consultar após o treinamento. O treinamento deve usar dados e cenários reais do negócio — treinamento genérico com dados fictícios não cria conexão com o dia a dia.

- **Verificação de licenças e custos recorrentes**: Confirmar que todas as licenças necessárias para operação da extensão estão ativas e que os custos recorrentes foram comunicados e aprovados — licenças de plataforma, licenças de pacotes gerenciados de terceiros, custos de armazenamento adicional, e custos de integrações externas. Extensões que param de funcionar porque uma licença expirou ou uma API key não foi renovada são problemas evitáveis com verificação antecipada.

### Perguntas

1. Se marketplace: a submissão para review foi feita com antecedência suficiente e o cronograma prevê ciclo de correções e resubmissão? [fonte: Dev, PM] [impacto: PM, Dev]
2. O plano de deploy em produção está documentado com sequência exata, responsáveis, janela de manutenção e critério de sucesso? [fonte: Dev, TI, Governança] [impacto: Dev, DevOps, PM]
3. O plano de rollback está documentado com procedimento específico para a plataforma e critérios de acionamento? [fonte: Dev, TI] [impacto: Dev, DevOps, PM]
4. A comunicação para usuários finais, administradores e gestores foi preparada e agendada? [fonte: PM, Change Management] [impacto: PM]
5. O treinamento diferenciado por perfil (usuário final vs. administrador) foi realizado com material de referência entregue? [fonte: PM, Dev] [impacto: PM, Conteúdo]
6. Todas as licenças e custos recorrentes necessários para operação da extensão estão ativos e aprovados? [fonte: Financeiro, TI] [impacto: PM]
7. O deploy foi validado em ambiente de QA/staging com sequência idêntica à de produção (dry run)? [fonte: Dev, QA] [impacto: Dev, DevOps]
8. As automações que precisam ser temporariamente desativadas durante o deploy foram listadas com procedimento de reativação? [fonte: Dev, Administrador da plataforma] [impacto: Dev, Admin]
9. O monitoramento pós-deploy foi configurado com alertas para exceções, consumo de governor limits e erros de integração? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
10. O helpdesk ou canal de suporte está informado sobre o go-live e sabe como escalar problemas relacionados à extensão? [fonte: Suporte, PM] [impacto: PM, Suporte]
11. A documentação técnica (arquitetura, modelo de dados, configurações, troubleshooting) foi entregue ao administrador da plataforma? [fonte: Dev] [impacto: Admin, Dev]
12. A lista de acessos a serem entregues ao cliente foi revisada e todos os acessos foram testados? [fonte: Dev, DevOps] [impacto: PM]
13. O backup do estado atual da plataforma foi realizado antes do deploy (metadata backup, data export)? [fonte: Administrador da plataforma, TI] [impacto: DevOps, Dev]
14. A janela de deploy foi escolhida em horário de baixo uso da plataforma com time de suporte disponível? [fonte: TI, PM] [impacto: PM, DevOps]
15. Todos os stakeholders foram notificados sobre data, horário, impactos esperados e contato de emergência? [fonte: Diretoria, PM] [impacto: PM]

---

## Etapa 10 — Go-Live

- **Execução do deploy seguindo o plano documentado**: Executar o deploy em produção seguindo exatamente o plano da Etapa 09 — sem improvisos. Em plataformas enterprise, a sequência importa: desativar automações que conflitam, executar o deploy/transporte, rodar scripts de migração de dados se aplicável, reativar automações, e executar verificações pós-deploy. Cada step deve ser confirmado antes de avançar para o próximo. Qualquer desvio do plano deve ser comunicado e avaliado antes de prosseguir — "consertar na hora" em produção enterprise é o caminho mais rápido para um incidente.

- **Verificação pós-deploy imediata**: Nos primeiros 30 minutos após o deploy, executar uma lista de verificações rápidas: extensão visível e acessível para os perfis corretos, funcionalidades principais operando (criar, ler, atualizar, deletar), integrações externas respondendo, e logs sem exceções não tratadas. Em plataformas com governor limits, verificar o consumo de limites nas primeiras transações reais — uma transação que consome 95% do CPU limit no primeiro uso é bomba-relógio que vai explodir quando houver mais dados ou usuários concorrentes.

- **Monitoramento da primeira semana**: A primeira semana após o go-live é a mais crítica. Monitorar: taxa de erros (exceções por hora/dia), consumo de governor limits (transações que se aproximam dos limites), performance de integrações (latência e taxa de falha de callouts), volume de tickets de suporte (indicador de usabilidade), e feedback qualitativo dos usuários (resistência, confusão, erros frequentes). Configurar dashboard de monitoramento que o time possa consultar diariamente sem precisar acessar a plataforma do cliente.

- **Suporte ativo pós-lançamento**: Manter o time de desenvolvimento em standby durante a primeira semana — com SLA de resposta definido (ex.: bugs críticos em 2h, bugs menores em 24h). O suporte ativo não é apenas corrigir bugs — é também responder dúvidas do administrador, ajustar configurações que não foram previstas, e coletar feedback que alimentará a próxima versão. Sem suporte ativo, problemas pequenos acumulam e a percepção da extensão deteriora antes de se consolidar.

- **Entrega e handoff formal**: Entregar formalmente todos os artefatos ao cliente: código-fonte (se aplicável — managed packages protegem o código), documentação técnica (modelo de dados, arquitetura, dependências), documentação de operação (como configurar, monitorar, troubleshootar), material de treinamento, e todos os acessos (repositório, pipeline CI/CD, ambientes de sandbox, dashboards de monitoramento). O handoff deve incluir sessão de transferência de conhecimento com o administrador da plataforma — não apenas enviar documentação por e-mail.

- **Aceite formal e encerramento**: Obter aceite formal do cliente baseado nos critérios de aceitação definidos na Etapa 04. O aceite deve cobrir: funcionalidades entregues conforme especificação, testes de aceitação aprovados, documentação entregue, treinamento realizado, e acessos transferidos. Itens pendentes (bugs não-críticos, melhorias para versão futura) devem ser documentados em backlog formal entregue ao cliente. O aceite formal marca o início do período de garantia — cujo escopo e duração devem estar claros no contrato.

### Perguntas

1. O deploy em produção foi executado seguindo exatamente o plano documentado, sem improvisos? [fonte: Dev, TI] [impacto: Dev, DevOps]
2. As verificações pós-deploy imediatas (acesso, CRUD, integrações, logs) foram executadas e passaram? [fonte: Dev, QA] [impacto: Dev]
3. As automações desativadas durante o deploy foram reativadas e estão funcionando corretamente? [fonte: Dev, Administrador da plataforma] [impacto: Dev, Admin]
4. O consumo de governor limits nas primeiras transações reais foi verificado e está dentro do esperado? [fonte: Dev] [impacto: Dev]
5. Os usuários finais conseguem acessar e usar a extensão com os perfis corretos? [fonte: Área de negócio, QA] [impacto: Dev, PM]
6. As integrações externas estão respondendo em produção com latência e taxa de erro aceitáveis? [fonte: Dev, DevOps] [impacto: Dev]
7. O dashboard de monitoramento está ativo e o time pode consultar métricas diariamente? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
8. O canal de suporte pós-lançamento está ativo e o SLA de resposta foi comunicado ao cliente? [fonte: PM, Dev] [impacto: PM, Suporte]
9. O aceite formal foi obtido com base nos critérios de aceitação definidos na Etapa 04? [fonte: Diretoria, Área de negócio] [impacto: PM]
10. Todos os acessos foram entregues formalmente e cada pessoa confirmou que consegue acessar? [fonte: Dev, DevOps] [impacto: PM]
11. A documentação técnica e de operação foi entregue ao administrador da plataforma com sessão de transferência de conhecimento? [fonte: Dev, PM] [impacto: Admin, PM]
12. O backlog de itens pendentes (bugs não-críticos, melhorias futuras) foi documentado e entregue ao cliente? [fonte: PM, Dev] [impacto: PM]
13. O monitoramento da primeira semana revelou algum problema que precisa de correção imediata? [fonte: Dev, DevOps] [impacto: Dev, PM]
14. O feedback qualitativo dos primeiros usuários foi coletado e documentado para informar versões futuras? [fonte: PM, Área de negócio] [impacto: PM, Produto]
15. O plano de suporte pós-garantia (modelo de contrato, SLA, canal de comunicação) foi formalizado? [fonte: Diretoria, PM] [impacto: PM]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"A plataforma faz tudo, só precisa de um ajuste"** — O cliente minimiza a complexidade da extensão porque "já tem a plataforma". Um "ajuste" em Salesforce pode envolver custom objects, triggers, LWC, integração via callout, e security review — semanas de trabalho. Alinhar expectativa de esforço com base em análise técnica, não na percepção do cliente.
- **"Não precisamos envolver TI, é só um plugin"** — Extensões de plataforma operam dentro de instâncias gerenciadas por TI. Sem o administrador da plataforma envolvido desde o início, o projeto vai esbarrar em restrições de acesso, conflitos com customizações existentes, e processos de governança que bloqueiam o deploy.
- **"Podemos decidir a plataforma depois"** — Se a plataforma-base ainda não foi escolhida, o projeto não é uma extensão de plataforma — é um projeto de seleção de plataforma + implementação. Misturar as duas decisões gera retrabalho quando a plataforma escolhida tem limitações que invalidam o design inicial.

### Etapa 02 — Discovery

- **"A org está limpa, não tem customização"** — Raramente verdade. Organizações que dizem não ter customizações geralmente não sabem que têm — fields criados por usuários, flows automáticos, pacotes gerenciados instalados anos atrás. O inventário técnico feito por quem conhece a plataforma sempre revela surpresas.
- **"Podemos ignorar os governor limits, o volume é pequeno"** — Volume pequeno hoje não significa volume pequeno amanhã. E governor limits não são apenas sobre volume — callout limits, CPU time, e heap size podem ser alcançados com operações complexas em poucos registros. Projetar para os limites desde o início é obrigatório.
- **"A extensão só lê dados, não precisa de permissões especiais"** — Mesmo leitura exige Field Level Security (FLS) e object-level CRUD checks em plataformas como Salesforce. Extensão que ignora FLS falha no security review e constitui vulnerabilidade de segurança.

### Etapa 03 — Alignment

- **"O CAB aprova rápido, não se preocupe"** — Comitês de aprovação de mudança em organizações enterprise são imprevisíveis. Um deploy que depende de aprovação do CAB deve ter buffer de pelo menos uma semana no cronograma. Se o CAB rejeitar, o próximo slot pode ser daqui a duas semanas.
- **"Usamos a mesma sandbox para dev e teste"** — Ambientes compartilhados geram conflitos — um dev reseta dados que o tester estava usando, ou o tester encontra bugs que só existem porque o dev está no meio de uma implementação. Sandboxes isolados por propósito são obrigatórios.
- **"O time já trabalhou com a plataforma, não precisa de treinamento"** — Experiência genérica na plataforma não é experiência nos padrões específicos do projeto. Um dev que sabe Apex não necessariamente sabe Apex com separation of concerns, bulk patterns e security review compliance. Alinhamento técnico do time é necessário.

### Etapa 04 — Definition

- **"Os campos são os mesmos do objeto padrão, só com nomes diferentes"** — Campos "iguais" com nomes diferentes sugerem duplicação desnecessária. Antes de criar um custom object, verificar se o objeto padrão com campos customizados resolve. Duplicação de dados entre objetos standard e custom gera problemas de sincronização permanentes.
- **"As permissões são simples — admin e usuário"** — Dois perfis raramente bastam em plataformas enterprise. Geralmente há pelo menos: admin, gestor (vê tudo mas não configura), operador (cria e edita), e visualizador (só lê). Definir perfis insuficientes resulta em "dar admin para todo mundo" — violação de segurança.
- **"Não precisa testar automações existentes, não vamos mexer nelas"** — A extensão pode disparar automações existentes ao inserir/atualizar registros em objetos que já têm triggers ou flows. Mesmo sem mexer nas automações, a interação é inevitável e precisa ser mapeada.

### Etapa 05 — Architecture

- **"Vamos fazer tudo em código, é mais flexível"** — Código customizado em excesso ignora as capacidades declarativas da plataforma (flows, validation rules, formula fields). O resultado é uma extensão que requer desenvolvedor para qualquer alteração — até mudar o texto de uma mensagem de erro. Maximizar uso declarativo é princípio fundamental.
- **"Não precisamos de testes, o Salesforce exige 75% e a gente atinge fácil"** — 75% de cobertura com asserts vazios é fraude de métricas. Cobertura sem validação de comportamento não detecta nenhum bug. A estratégia de testes deve focar em qualidade dos asserts, não em percentual de cobertura.
- **"Empacotamento gerenciado é complicado demais, vamos com deploy direto"** — Deploy direto (sem pacote) funciona para customizações internas, mas impossibilita distribuição, versionamento e upgrade automatizado. Se a extensão pode ser usada por mais de um cliente, empacotamento é investimento necessário.

### Etapa 06 — Setup

- **"Usamos o sandbox que já existe"** — Sandbox criado há meses pode estar defasado em relação a produção — metadados diferentes, dados inconsistentes, customizações que foram adicionadas em produção e não propagadas. Refresh do sandbox antes de iniciar o desenvolvimento é obrigatório.
- **"O pipeline é manual — a gente faz deploy pelo VS Code"** — Deploy manual sem automação é propenso a erros (esquecer componentes, deploy incompleto) e não escalável. Pipeline automatizado com lint, testes e validate-only é investimento mínimo para qualquer projeto que terá mais de 2 deploys.
- **"O dev usa a conta admin para tudo"** — Devs com conta admin em sandbox não testam o modelo de permissões durante o desenvolvimento. Bugs de permissão aparecem apenas quando o usuário real (sem admin) tenta usar. Devs devem ter perfis equivalentes aos usuários finais no sandbox de desenvolvimento.

### Etapa 07 — Build

- **"Funciona com 1 registro no teste, está bom"** — 1 registro não testa bulkificação. Trigger que funciona com 1 registro pode estourar governor limits com 200 (Salesforce insere até 200 registros por trigger invocation via Data Loader ou API). Testes com volume mínimo de 200 são obrigatórios.
- **"Vamos desabilitar as validations rules do cliente para o dev funcionar"** — Se a extensão precisa que validations rules sejam desabilitadas, ela está inserindo dados inválidos. O correto é respeitar as validações existentes e ajustar os dados que a extensão manipula para conformidade.
- **"O admin do cliente ajusta depois as permissões"** — Delegar configuração de permissões ao admin sem documentação detalhada resulta em permissões incorretas (acesso demais ou de menos). A extensão deve entregar permissões pré-configuradas (permission sets) que o admin apenas atribui aos perfis.

### Etapa 08 — QA

- **"Testamos na scratch org, está perfeito"** — Scratch org é ambiente limpo, sem customizações legadas. Testes que passam em scratch org podem falhar espetacularmente na org do cliente onde triggers de 2019, flows de 2021, e pacotes gerenciados de terceiros competem por governor limits. QA final deve ser em sandbox com dados e customizações de produção.
- **"O security review a gente submete e vê o que acontece"** — Submissão para review sem auditoria prévia resulta em rejeição, espera de semanas para resubmissão, e refatoração sob pressão. Executar PMD/Checkmarx scan internamente antes de submeter é obrigatório.
- **"Os usuários testaram e disseram que está bom"** — UAT sem critérios formais é opiniômetro. "Está bom" não é critério de aceite. Definir cenários de teste com entrada esperada, ação, e resultado esperado antes do UAT.

### Etapa 09 — Launch Prep

- **"O review do marketplace é rápido, não precisa folga no cronograma"** — Security review do Salesforce AppExchange leva 2-6 semanas, e rejeições na primeira tentativa são comuns (>50% dos casos). Cronograma sem buffer para resubmissão é cronograma com atraso garantido.
- **"Os usuários já sabem usar a plataforma, não precisam de treinamento"** — Saber usar a plataforma não é saber usar a extensão. Funcionalidades novas, mesmo que sigam o design system da plataforma, requerem explicação de fluxo, propósito e boas práticas. Extensão sem treinamento = extensão sem adoção.
- **"Fazemos deploy na sexta à noite quando ninguém está usando"** — Deploy em horário sem usuários parece seguro, mas significa que se algo falhar, o time precisa resolver de madrugada ou no fim de semana. Melhor: deploy em horário de baixo uso dentro do expediente, com time disponível para suporte.

### Etapa 10 — Go-Live

- **"O deploy foi feito, projeto encerrado"** — Sem monitoramento na primeira semana, problemas de performance, governor limits e erros de integração passam despercebidos até que os usuários comecem a reclamar em massa. A primeira semana pós-deploy é parte do projeto.
- **"O rollback é só desinstalar o pacote"** — Desinstalar um pacote que criou registros, campos e automações não é trivial. Dados criados pela extensão podem precisar ser preservados ou migrados. O plano de rollback deve cobrir o tratamento de dados, não apenas a remoção de código.
- **"Entregamos o código, o cliente que se vire"** — Handoff sem transferência de conhecimento para o administrador da plataforma resulta em extensão que ninguém sabe manter. Uma sessão de 2-4h de transferência de conhecimento é investimento que protege o trabalho entregue.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é extensão de plataforma** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "A plataforma é só o banco de dados, o frontend é nosso" | Web app com integração via API, não extensão de plataforma | Reclassificar para web-app |
| "Precisamos de uma plataforma inteira, não só um plugin" | Projeto de implementação de plataforma, não extensão | Reclassificar para platform-implementation |
| "Não temos plataforma ainda, estamos avaliando" | Projeto de seleção de plataforma + implementação | Separar em 2 projetos: seleção e extensão |
| "A extensão precisa rodar fora da plataforma também" | Aplicação standalone com integração, não extensão | Reclassificar para web-app ou saas |
| "Queremos substituir o módulo nativo da plataforma" | Reimplementação de funcionalidade core — risco alto e frequentemente inviável | Avaliar se configuração nativa resolve ou reclassificar |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos quem é o admin da plataforma" | 01 | Sem admin, nenhuma configuração ou deploy é possível | Identificar e envolver admin antes de avançar |
| "Não temos sandbox disponível" | 01 | Sem sandbox, desenvolvimento e testes são impossíveis | Provisionar sandbox antes da Etapa 06 |
| "A plataforma está em processo de migração" | 01 | Extensão desenvolvida para versão atual pode ser invalidada pela migração | Travar até migração concluída ou definir versão-alvo |
| "TI não aprova instalação de pacotes externos" | 03 | Se a extensão usa pacotes de terceiros, deploy será bloqueado | Alinhar com TI antes de incluir dependências externas |
| "Não temos acesso ao environment de produção" | 06 | Deploy em produção impossível | Resolver acesso formal antes do build |
| "O CAB está congelado por auditoria" | 09 | Deploy bloqueado sem data de liberação | Aguardar liberação do CAB ou negociar exceção formal |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "A org tem muitas customizações, mas ninguém documenta" | 02 | Conflitos imprevisíveis com automações existentes | Investir tempo extra em inventário técnico da org |
| "O último projeto na plataforma deu problema" | 01 | Resistência organizacional e escrutínio elevado | Identificar causas do fracasso anterior e endereçar proativamente |
| "Não temos consultores certificados na plataforma" | 03 | Time sem experiência gera bugs de plataforma, não de lógica | Avaliar necessidade de consultoria especializada |
| "Usamos a mesma org para produção e testes" | 03 | Teste em produção é risco direto para dados reais | Provisionar sandbox dedicado antes do build |
| "O review do marketplace é só formalidade" | 05 | Subestimar review resulta em rejeição e atraso | Levantar critérios reais e incluir buffer no cronograma |
| "A plataforma vai ser atualizada no meio do projeto" | 03 | Release da plataforma pode quebrar a extensão em desenvolvimento | Testar no sandbox preview da nova release antes de deployar |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Problema de negócio e limitação da funcionalidade nativa identificados (pergunta 1)
- Plataforma-base, versão e licenciamento confirmados (pergunta 2)
- Administrador da plataforma identificado e disponível (pergunta 3)
- Destino da extensão definido — marketplace ou uso interno (pergunta 5)
- Roadmap da plataforma verificado para os próximos 6-12 meses (pergunta 15)

### Etapa 02 → 03

- Inventário de customizações existentes na instância realizado (pergunta 2)
- Modelo de dados da plataforma mapeado para o caso de uso (pergunta 3)
- Requisitos de segurança e compliance identificados (pergunta 5)
- Fronteira entre extensão e aplicação standalone validada (pergunta 15)

### Etapa 03 → 04

- Processo de governança de mudanças mapeado com SLA (pergunta 1)
- Fronteira código vs. configuração definida (pergunta 3)
- Estratégia de sandboxes definida e orçada (pergunta 4)
- Se marketplace: critérios de review documentados (pergunta 5)

### Etapa 04 → 05

- Especificação funcional com terminologia da plataforma aprovada (pergunta 1)
- Modelo de dados customizado definido campo a campo (pergunta 2)
- Automações mapeadas com verificação de conflitos (pergunta 3)
- Matriz de permissões por perfil definida (pergunta 4)
- Documentação aprovada por todos os stakeholders e admin da plataforma (pergunta 15)

### Etapa 05 → 06

- Arquitetura definida dentro dos limites da plataforma (pergunta 1)
- Estratégia de testes cobre unitários, integração, bulk e mocks (pergunta 3)
- Tipo de pacote/distribuição escolhido (pergunta 4)
- Governor limits validados em cenário de pior caso (pergunta 7)
- Modelo de branches e ambientes documentado (pergunta 15)

### Etapa 06 → 07

- Sandboxes provisionados com customizações de produção (pergunta 1)
- Ambiente de desenvolvimento configurado e funcional para todo o time (pergunta 2)
- Pipeline CI/CD testado end-to-end (pergunta 15)
- Dados de teste criados com scripts automatizados (pergunta 5)

### Etapa 07 → 08

- Código segue padrões da plataforma com bulkificação (perguntas 1 e 2)
- Testes automatizados com cobertura real e asserts explícitos (pergunta 3)
- Extensão testada com automações de produção ativas (pergunta 4)
- Permissões configuradas e validadas por perfil (pergunta 12)

### Etapa 08 → 09

- Testes executados em sandbox com dados representativos de produção (pergunta 1)
- Test suite completo da org passou sem regressões (pergunta 2)
- Testes de governor limits em cenário de pior caso aprovados (pergunta 3)
- Scan de segurança executado sem achados críticos (pergunta 4)
- UAT aprovado com critérios formais (pergunta 6)

### Etapa 09 → 10

- Se marketplace: review aprovado ou em andamento com buffer (pergunta 1)
- Plano de deploy documentado com sequência e responsáveis (pergunta 2)
- Plano de rollback documentado com critérios de acionamento (pergunta 3)
- Treinamento realizado e material entregue (pergunta 5)
- Backup do estado atual da plataforma realizado (pergunta 13)

### Etapa 10 → Encerramento

- Deploy executado conforme plano sem improvisos (pergunta 1)
- Verificações pós-deploy imediatas aprovadas (pergunta 2)
- Governor limits verificados em transações reais (pergunta 4)
- Aceite formal obtido (pergunta 9)
- Acessos entregues e documentação transferida (perguntas 10 e 11)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de extensão de plataforma. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Plugin Marketplace | V2 Customização Interna | V3 Extensão Browser | V4 Conector/Integração | V5 Módulo ERP/CRM |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 1 | 2 | 3 |
| 02 Discovery | 3 | 3 | 2 | 3 | 4 |
| 03 Alignment | 3 | 2 | 2 | 2 | 4 |
| 04 Definition | 4 | 3 | 2 | 3 | 5 |
| 05 Architecture | 4 | 3 | 3 | 4 | 4 |
| 06 Setup | 3 | 2 | 2 | 2 | 4 |
| 07 Build | 4 | 3 | 4 | 4 | 5 |
| 08 QA | 5 | 3 | 3 | 4 | 5 |
| 09 Launch Prep | 5 | 2 | 4 | 2 | 4 |
| 10 Go-Live | 3 | 2 | 2 | 2 | 3 |
| **Total relativo** | **36** | **25** | **25** | **28** | **41** |

**Observações por variante:**

- **V1 Plugin Marketplace**: QA e Launch Prep são os mais pesados — security review, conformidade com policies do marketplace, e ciclo de submissão/correção/resubmissão. O Build também é pesado por exigir padrões de segurança rigorosos (FLS enforcement, CRUD checks, sem hardcoded IDs).
- **V2 Customização Interna**: Esforço relativamente distribuído e menor que marketplace — sem review externo, sem empacotamento. O risco principal está em conflitos com customizações existentes (Discovery e Build).
- **V3 Extensão Browser**: Build é o pico — lidar com Manifest V3, service workers, content scripts, e as restrições de sandbox do browser. Launch Prep inclui o review da Chrome Web Store que pode ter ciclos de rejeição.
- **V4 Conector/Integração**: Architecture e Build são os picos — mapeamento de dados entre sistemas com schemas diferentes, tratamento de erros, retry, e monitoramento de integrações em produção.
- **V5 Módulo ERP/CRM**: O mais pesado de todas as variantes. Definition é máxima (transações customizadas, telas, relatórios, jobs batch). Build e QA são intensos pelo volume de funcionalidades e pela complexidade de transporte entre ambientes.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Uso interno, sem marketplace (Etapa 01, pergunta 5) | Etapa 03: pergunta 5 (critérios de review marketplace). Etapa 05: perguntas 4 e 9 (empacotamento gerenciado, security review). Etapa 08: pergunta 5 (teste de upgrade de pacote). Etapa 09: pergunta 1 (submissão para review). |
| Sem integração com sistemas externos (Etapa 01, pergunta 10) | Etapa 02: pergunta 4 (integrações externas). Etapa 05: pergunta 5 (tratamento de erros de callout). Etapa 07: pergunta 7 (callouts com retry). Etapa 08: pergunta 7 (teste de falha de callout). Etapa 10: pergunta 6 (integrações em produção). |
| Sem migração de dados (Etapa 04, pergunta 6) | Etapa 05: pergunta 10 (desativação de triggers na migração). Etapa 07: pergunta 10 (teste de migração). Etapa 08: pergunta 9 (validação pós-migração). |
| Extensão sem UI customizada (Etapa 02, pergunta 8) | Etapa 04: pergunta 5 (wireframes). Etapa 07: perguntas 5 e 9 (UI nativa, responsividade). |
| Plataforma sem governor limits (Etapa 01, pergunta 7) | Etapa 05: perguntas 6 e 7 (bulkificação, validação de limits). Etapa 07: pergunta 2 (queries em loop). Etapa 08: pergunta 3 (teste de governor limits). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Publicação em marketplace (Etapa 01, pergunta 5) | Etapa 03: pergunta 5 (critérios de review) se torna bloqueadora. Etapa 05: perguntas 4 e 9 (empacotamento e security review) se tornam gates. Etapa 08: pergunta 4 (scan de segurança) é pré-requisito para submissão. Etapa 09: pergunta 1 (submissão com buffer para resubmissão) é gate. |
| Integração com sistemas externos (Etapa 01, pergunta 10) | Etapa 05: pergunta 5 (retry, circuit breaker) se torna obrigatória. Etapa 07: pergunta 7 (tratamento de erro de callout) é gate. Etapa 08: pergunta 7 (teste de falha) é obrigatório. |
| Customizações extensas na instância (Etapa 02, pergunta 2) | Etapa 04: pergunta 3 (mapeamento de conflitos) se torna crítica. Etapa 07: pergunta 4 (testes com automações ativas) é obrigatória. Etapa 08: pergunta 2 (test suite completo da org) é gate. |
| Dados sensíveis envolvidos — PII, financeiros (Etapa 02, pergunta 5) | Etapa 04: pergunta 4 (matriz de permissões) se torna gate com revisão de segurança. Etapa 05: pergunta 9 (FLS enforcement) é obrigatória. Etapa 08: pergunta 4 (scan de segurança) é bloqueador. |
| Release da plataforma durante o projeto (Etapa 01, pergunta 8) | Etapa 05: pergunta 13 (compatibilidade de upgrade) se torna crítica. Etapa 08: pergunta 10 (teste no sandbox preview) é obrigatório. |
| Volume alto de dados — >100K registros (Etapa 02, pergunta 14) | Etapa 05: perguntas 6 e 7 (bulkificação e governor limits) se tornam gates. Etapa 07: pergunta 11 (processamento assíncrono) é obrigatório. Etapa 08: pergunta 3 (teste de pior caso com volume real) é gate. |
