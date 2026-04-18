---
title: "Site Estático / Landing Page — Blueprint"
description: "Site institucional, marketing, portfolio ou documentação técnica. Sem backend próprio. Gerado estaticamente ou via CMS headless. Hospedado em CDN."
category: project-blueprint
type: static-site
status: rascunho
created: 2026-04-13
---

# Site Estático / Landing Page

## Descrição

Site institucional, marketing, portfolio ou documentação técnica. Sem backend próprio. Gerado estaticamente ou via CMS headless. Hospedado em CDN.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo site estático é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Landing Page de Campanha

Página única ou conjunto pequeno (2-5 páginas) com prazo curto, vinculada a uma campanha de marketing com data de início definida. Conteúdo é fixo após o lançamento e raramente atualizado. Vida útil tipicamente curta (semanas a meses). O foco é conversão (formulário, CTA) e performance de carregamento para maximizar Quality Score em ads pagos. Sem CMS — conteúdo no próprio código. Exemplos: página de lançamento de produto, squeeze page para captação de leads, página de evento.

### V2 — Site Institucional

5 a 20 páginas com conteúdo relativamente estável (sobre, serviços, equipe, contato, blog opcional). Atualizado por não-técnicos com frequência baixa a moderada (mensal). CMS headless geralmente necessário. O foco é credibilidade, SEO orgânico e clareza de comunicação. Exemplos: site corporativo, escritório de advocacia, clínica, consultoria.

### V3 — Blog / Documentação

Volume alto de conteúdo (dezenas a centenas de páginas/posts), com publicação frequente (semanal ou diária). CMS headless obrigatório ou conteúdo em Markdown com pipeline automatizado. O foco é SEO, tempo de build com volume crescente, e facilidade de publicação pelo time de conteúdo. Exemplos: blog corporativo, documentação de produto (docs), base de conhecimento.

### V4 — Portfólio / Showcase Visual

Projeto com peso visual alto — galeria de imagens, vídeos, animações, transições. Número de páginas médio (10-30), mas cada página é pesada em assets. O foco é impacto visual sem destruir a performance — pipeline de imagens e lazy loading são críticos. CMS pode ou não ser necessário dependendo da autonomia do dono do conteúdo. Exemplos: portfólio de fotógrafo, estúdio de design, agência criativa, catálogo de produtos sem e-commerce.

### V5 — Documentação Técnica (Docs)

Estrutura hierárquica profunda (seções, subseções, artigos), com busca full-text, versionamento por release, e frequentemente gerado a partir de código-fonte (docstrings, OpenAPI). O foco é navegabilidade, busca e manutenção automatizada. CMS raramente usado — conteúdo em Markdown no repositório, versionado junto com o código. Exemplos: docs de API, guia de SDK, manual de produto, wiki técnica.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | SSG | CMS | Hospedagem | Formulários | Observações |
|---|---|---|---|---|---|
| V1 — Landing Page | Astro | Sem CMS | Netlify ou Cloudflare Pages | Netlify Forms ou Formspree | Zero JS por padrão. Build em segundos. Plano gratuito resolve. |
| V2 — Institucional | Next.js ou Astro | Sanity ou Contentful | Vercel ou Netlify | Formspree ou serverless function | CMS necessário para autonomia editorial. ISR se conteúdo muda semanalmente. |
| V3 — Blog/Docs | Next.js ou Hugo | Sanity ou Markdown no repo | Vercel ou Cloudflare Pages | Não se aplica | Hugo para volume extremo (build 10x mais rápido). Next.js se precisa de ISR. |
| V4 — Portfólio Visual | Astro ou Next.js | Sanity ou Contentful | Vercel | Não se aplica | Cloudinary ou imgix obrigatório para pipeline de imagens pesado. |
| V5 — Docs Técnica | Astro Starlight, Docusaurus ou MkDocs | Markdown no repo | Cloudflare Pages ou Netlify | Não se aplica | Versionamento por branch/tag. Busca via Algolia DocSearch ou Pagefind. |

---

## Etapa 01 — Inception

- **Origem da demanda**: A necessidade costuma surgir de eventos de negócio — rebranding, lançamento de produto, troca de agência, ou insatisfação com o site legado (lento, difícil de editar, caro de manter). Entender o gatilho real é importante porque ele define o critério de sucesso: se o problema é velocidade, performance é KPI central; se é autonomia editorial, o CMS é prioridade.

- **Stakeholders reais vs. formais**: O patrocinador formal costuma ser o gerente de marketing ou o CEO, mas os usuários reais do sistema pós-entrega são o time de conteúdo (redatores, designers de comunicação). É frequente que esses dois grupos tenham expectativas diferentes — o patrocinador quer algo "moderno e bonito", enquanto o time operacional quer algo fácil de atualizar sem acionar o dev. Identificar ambos desde o início evita conflito de escopo no final.

- **Ausência de dono de conteúdo definido**: Projetos de site estático frequentemente chegam sem um responsável claro pela governança editorial pós-entrega. Isso se torna um problema crítico quando o conteúdo precisa ser preenchido antes do lançamento — e o time de desenvolvimento fica bloqueado esperando textos, imagens e aprovações que nunca chegam. Definir o content owner na Inception é pré-requisito para estimar cronograma com realismo.

- **Orçamento invisível de operação**: Clientes acostumados com WordPress em hospedagem compartilhada ($10/mês) frequentemente não antecipam os custos de CDN, CMS headless SaaS e pipelines de CI/CD, que juntos podem somar $100–500/mês dependendo das escolhas. O custo de operação contínua precisa ser apresentado nesta fase para evitar surpresa após o go-live.

- **Identidade visual consolidada como pré-requisito**: Projetos que chegam sem brand guide aprovado geram retrabalho inevitável — paleta muda, tipografia muda, e o código precisa acompanhar. Se o cliente ainda está em processo de branding paralelo, o correto é condicionar o início do desenvolvimento à entrega do brand guide final, e não trabalhar com referências provisórias.

- **Escopo multilíngue e regional**: A adição de um segundo idioma ou de versões regionais (ex.: .com.br vs. .com) não é uma feature incremental — ela impacta a estrutura de rotas, o modelo de conteúdo no CMS, a estratégia de SEO internacional (hreflang), e possivelmente o custo de CDN (múltiplos edge regions). Se isso tem qualquer chance de aparecer no futuro, precisa ser identificado aqui para que a arquitetura já contemple o suporte, mesmo que a implementação venha depois.

### Perguntas

1. Qual é o gatilho real desta demanda — rebranding, lançamento de produto, site legado lento, ou insatisfação com a agência anterior? [fonte: Diretoria, Marketing] [impacto: PM, Dev]
2. Quem é o patrocinador formal do projeto e quem são os usuários reais que vão operar o sistema após o lançamento? [fonte: Diretoria, RH] [impacto: PM, Conteúdo]
3. Existe um responsável claramente definido pela atualização de conteúdo após o go-live? [fonte: Marketing, Diretoria] [impacto: Dev, Conteúdo, PM]
4. Qual é o orçamento total disponível, separando custo de desenvolvimento e custo de operação mensal recorrente? [fonte: Financeiro, Diretoria] [impacto: Dev, PM]
5. O site substituirá um site existente ou será criado do zero? [fonte: Marketing, TI] [impacto: Dev, SEO]
6. Existe guia de identidade visual aprovado (paleta, tipografia, brand guide) pronto para uso? [fonte: Marketing, Agência de branding] [impacto: Designer, Dev]
7. O projeto precisará suportar múltiplos idiomas ou versões regionais agora ou no futuro próximo? [fonte: Comercial, Diretoria] [impacto: Dev, Conteúdo, SEO]
8. Qual é o prazo esperado para o go-live e existe alguma data de negócio que o justifica (evento, campanha, lançamento)? [fonte: Marketing, Diretoria] [impacto: PM, Dev]
9. Quem toma decisões de design e conteúdo — existe um aprovador único ou um comitê com múltiplas vozes? [fonte: Diretoria] [impacto: PM, Designer]
10. Há expectativas de integração com sistemas externos (CRM, ERP, plataforma de e-mail marketing, analytics)? [fonte: TI, Marketing, Comercial] [impacto: Dev, DevOps]
11. O cliente tem preferência ou restrição técnica por alguma plataforma, framework ou linguagem específica? [fonte: TI, Diretoria] [impacto: Dev]
12. Qual é o nível de maturidade digital do time que vai operar o site após o lançamento (técnicos, redatores, executivos)? [fonte: RH, Marketing] [impacto: Dev, Conteúdo]
13. Existe conteúdo legado a migrar de um site anterior ou o conteúdo será produzido do zero? [fonte: Marketing, TI] [impacto: Dev, Conteúdo, PM]
14. O domínio já está registrado? Quem controla o DNS atualmente e o cliente tem acesso ao painel? [fonte: TI, Fornecedor de hospedagem] [impacto: DevOps, Dev]
15. Haverá campanhas de marketing ativas no dia do lançamento que dependem do site no ar para gerar resultado? [fonte: Marketing, Comercial] [impacto: PM, DevOps]

---

## Etapa 02 — Discovery

- **Inventário de conteúdo**: Levantar o número total de páginas, tipos de conteúdo (institucional, blog, landing pages, documentação, portfólio, caso de sucesso) e volume de mídia (imagens, vídeos hospedados externamente ou inline, PDFs para download). Este inventário define diretamente o esforço de build — um site de 5 páginas com conteúdo estável é radicalmente diferente de um blog com 300 posts a migrar, mesmo que ambos sejam "sites estáticos".

- **Requisitos de SEO**: Identificar o nível de maturidade SEO esperado: meta tags customizadas por página, sitemap.xml automático, dados estruturados Schema.org (Article, Organization, Product, FAQ), Open Graph e Twitter Card para compartilhamento em redes sociais, breadcrumbs, e canonical tags. Projetos com histórico de SEO no site anterior precisam de atenção redobrada ao mapa de redirecionamentos para não perder autoridade de domínio construída ao longo de anos.

- **Benchmarks de performance**: Levantar se o cliente tem expectativas formais de Lighthouse score (Performance, Accessibility, SEO, Best Practices) ou de Core Web Vitals (LCP, CLS, INP). Sites que serão usados como base para campanhas de Google Ads têm requisito implícito de Landing Page Experience — pages com Lighthouse Performance abaixo de 70 impactam diretamente o Quality Score e o custo por clique.

- **Integrações com terceiros**: Mapear todas as integrações previstas — formulários de contato, chat ao vivo (Intercom, Crisp, HubSpot), mapas (Google Maps, Mapbox), players de vídeo (YouTube, Vimeo, Mux), pixels de tracking (GA4, Meta Pixel, LinkedIn Insight Tag), e ferramentas de heatmap (Hotjar, Microsoft Clarity). Cada integração que carrega JavaScript de terceiros tem potencial de impactar significativamente o Lighthouse Performance e deve ser planejada com estratégia de carregamento assíncrono ou facade pattern.

- **Frequência de atualização do conteúdo**: Esta resposta determina a necessidade de CMS headless. Conteúdo que muda diariamente ou semanalmente por pessoas não-técnicas justifica investimento em CMS. Conteúdo que muda raramente e é gerenciado por desenvolvedores pode viver em arquivos Markdown no repositório, com deploy a cada PR — mais simples, mais barato, menos dependência de serviço externo.

- **Existência de assets prontos**: Verificar o que já existe: brand guide com paleta e tipografia aprovadas, copywriting finalizado e aprovado pela liderança, fotos profissionais licenciadas, ícones e ilustrações. A ausência de qualquer um desses itens não é bloqueador para iniciar o desenvolvimento, mas é bloqueador para finalizar — e precisa estar refletida no cronograma como dependência externa com prazo acordado.

- **Fronteira do estático**: Verificar explicitamente se existe qualquer requisito que empurre o projeto para fora do domínio estático: área de membros com login, conteúdo personalizado por usuário, e-commerce, calculadoras com lógica server-side, ou dashboards com dados em tempo real. Se qualquer um desses existir, o projeto deixa de ser puramente estático e precisa ser reclassificado — adicionando backend, serverless functions ou BFF — com impacto direto em custo e complexidade.

### Perguntas

1. Quantas páginas distintas o site terá no MVP e quais são os templates de layout necessários? [fonte: Marketing, Diretoria] [impacto: Designer, Dev, PM]
2. Qual é a frequência esperada de atualização de conteúdo e quem fará essas atualizações (dev, redator, editor)? [fonte: Marketing, Conteúdo] [impacto: Dev, Conteúdo]
3. O site precisará de um CMS headless ou o conteúdo pode viver em arquivos Markdown no repositório? [fonte: Conteúdo, Marketing] [impacto: Dev, DevOps]
4. Quais integrações com terceiros são obrigatórias no MVP (formulários, chat, analytics, pixels, mapas)? [fonte: Marketing, Comercial, TI] [impacto: Dev]
5. Existe um site atual do qual será necessário migrar conteúdo? Quantas URLs estão indexadas pelo Google? [fonte: TI, Agência anterior, Marketing] [impacto: Dev, SEO]
6. Quais são os requisitos de SEO — meta tags customizadas por página, dados estruturados, sitemap, hreflang? [fonte: Marketing, Agência de SEO] [impacto: Dev, SEO]
7. O cliente tem expectativas formais de Lighthouse score ou Core Web Vitals mínimos aceitáveis? [fonte: Marketing, TI] [impacto: Dev]
8. Quais assets de design já existem prontos (brand guide, fotos licenciadas, ícones, copy aprovado)? [fonte: Marketing, Agência de branding] [impacto: Designer, Dev, PM]
9. O site precisará funcionar offline ou como PWA instalável em dispositivos móveis? [fonte: Diretoria, Comercial] [impacto: Dev]
10. Há requisitos formais de acessibilidade (WCAG 2.1 AA, legislação específica como a LBI no Brasil)? [fonte: Jurídico, Compliance] [impacto: Dev, Designer]
11. Qual é o público-alvo geográfico e qual a expectativa de performance para essa região (latência de CDN)? [fonte: Marketing, Comercial] [impacto: Dev, DevOps]
12. O site terá área restrita, login, ou qualquer conteúdo personalizado por usuário? [fonte: Diretoria, Comercial] [impacto: Dev, Arquiteto]
13. Há requisitos de LGPD/GDPR — banner de cookies, política de privacidade, opt-out de tracking? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, DevOps]
14. Quais métricas o cliente quer monitorar e qual ferramenta de analytics será usada? [fonte: Marketing, Diretoria] [impacto: Dev, Marketing]
15. Existe orçamento e responsável definidos para produção de conteúdo (copywriting, fotografia, vídeo)? [fonte: Financeiro, Marketing] [impacto: PM, Conteúdo]

---

## Etapa 03 — Alignment

- **Governança editorial**: Definir formalmente quem escreve, quem revisa, quem aprova e quem tem permissão de publicar no CMS. Em empresas maiores, a cadeia de aprovação pode envolver marketing, jurídico e diretoria — o que significa que uma alteração simples pode levar dias. O fluxo de publicação precisa ser acordado antes do setup do CMS, pois diferentes ferramentas oferecem níveis distintos de controle de workflow (rascunho → revisão → aprovado → publicado).

- **Decisão CMS headless vs. conteúdo em repositório**: Esta é a decisão arquitetural mais importante desta fase. CMS headless (Contentful, Sanity, Strapi) é necessário quando o conteúdo é atualizado por não-desenvolvedores com frequência, quando há múltiplos autores, ou quando o fluxo de aprovação precisa ser gerenciado visualmente. Conteúdo em repositório (arquivos Markdown ou JSON commitados via PR) é adequado quando apenas desenvolvedores editam, quando a frequência é baixa, ou quando o cliente quer minimizar custos e dependências externas. A escolha impacta setup, custo mensal e treinamento.

- **Formato e completude do design**: Alinhar o formato de entrega do design (Figma com componentes organizados, Adobe XD, Zeplin, ou apenas referências visuais soltas) e o nível de completude esperado antes do início do build. Designs incompletos — sem estados de hover, sem versões mobile, sem estados de erro em formulários — geram decisões não documentadas durante o desenvolvimento que frequentemente resultam em inconsistências e revisões custosas. O correto é definir um checklist de entregáveis do design como gate de entrada do Build.

- **Abordagem mobile**: Alinhar se o projeto é mobile-first (projetado e desenvolvido prioritariamente para telas pequenas, adaptado para desktop) ou responsivo tradicional (desktop como referência principal, adaptado para mobile). A escolha impacta como os componentes são construídos, como os layouts são testados, e qual breakpoint é tratado como "primário" nas revisões com o cliente. Com mais de 60% do tráfego web vindo de mobile em média, mobile-first é o padrão recomendado salvo exceção justificada.

- **SLA de atualização pós-lançamento**: Definir o modelo de manutenção contínua antes do go-live — quem aciona quando há uma correção urgente (ex.: erro de ortografia em texto crítico, link quebrado), quem executa, e em quanto tempo. Se a manutenção ficará com o time do cliente via CMS, documentar o processo. Se ficará com a agência ou dev externo, formalizar contrato de suporte com SLA. Sites sem modelo de manutenção definido tendem a acumular problemas silenciosamente até virarem projetos de reforma.

### Perguntas

1. O fluxo editorial (escreve → revisa → aprova → publica) foi definido formalmente e todos os envolvidos concordam? [fonte: Marketing, Jurídico, Diretoria] [impacto: Dev, Conteúdo]
2. A cadeia de aprovação de conteúdo envolve mais de uma área da empresa (marketing, jurídico, diretoria)? [fonte: Marketing, Diretoria] [impacto: PM, Conteúdo]
3. A decisão entre CMS headless e conteúdo em repositório foi tomada com justificativa documentada? [fonte: TI, Conteúdo] [impacto: Dev, DevOps]
4. Se CMS headless, qual ferramenta foi escolhida e o custo mensal recorrente está previsto no orçamento? [fonte: TI, Financeiro] [impacto: Dev, PM]
5. O design foi entregue em formato utilizável com componentes organizados, não apenas imagens ou PDFs? [fonte: Designer, Agência de design] [impacto: Dev]
6. O design cobre todos os breakpoints necessários (mobile 375px, tablet 768px, desktop 1024px, wide 1440px)? [fonte: Designer, Agência de design] [impacto: Dev]
7. O design inclui estados de interação (hover, focus, active, disabled, estados de erro em formulários)? [fonte: Designer, Agência de design] [impacto: Dev]
8. A abordagem de desenvolvimento foi alinhada — mobile-first ou responsivo partindo do desktop? [fonte: Marketing, Designer] [impacto: Dev, QA]
9. O SLA de publicação de conteúdo após o lançamento foi definido (quem aciona, quem executa, prazo)? [fonte: Diretoria, Marketing] [impacto: PM, Conteúdo, Dev]
10. O modelo de manutenção pós-lançamento foi formalizado (time interno via CMS ou contrato de suporte externo)? [fonte: Diretoria, Financeiro] [impacto: PM, Dev]
11. O cliente entende e aceitou o modelo de deploy — push para main igual a site atualizado automaticamente? [fonte: TI, Diretoria] [impacto: Dev, Conteúdo]
12. As dependências externas críticas (conteúdo, assets, aprovações) foram listadas com prazos acordados? [fonte: Marketing, Designer, Diretoria] [impacto: PM]
13. O time de desenvolvimento tem acesso a todas as ferramentas necessárias (repositório, CMS sandbox, hospedagem)? [fonte: TI, Fornecedores SaaS] [impacto: Dev, DevOps]
14. Existe processo definido para revisão e aprovação de entregas parciais durante o build? [fonte: Diretoria, Marketing] [impacto: PM, Dev, Designer]
15. O cliente foi informado sobre o impacto de mudanças de escopo no prazo e no custo do projeto? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Arquitetura de informação e sitemap**: Produzir o sitemap completo com hierarquia de páginas (home → seções → subpáginas), relações de navegação (menu principal, menu secundário, footer, breadcrumbs) e tipologia de cada página (template único ou compartilhado). O sitemap é o artefato que permite estimar com precisão o esforço de build — cada template distinto representa um componente de layout a ser implementado — e é a base para o planejamento de conteúdo.

- **Modelo de conteúdo por template**: Para cada tipo de página, definir os campos estruturados que o CMS precisará suportar. Exemplos: uma página institucional tem hero (título, subtítulo, CTA, imagem de fundo), seções livres (rich text + imagem), bloco de depoimentos, e rodapé de CTA. Um post de blog tem título, slug, autor, data, tags, imagem de capa, corpo (rich text), meta SEO separado. Modelar o conteúdo antes do setup do CMS evita refatoração de schema depois que há conteúdo real cadastrado — o que é doloroso em qualquer CMS headless.

- **Estrutura de URLs e slugs**: Definir a estrutura de URLs antes do início do build para evitar redirects desnecessários após o lançamento. Decidir: /blog/titulo-do-post ou /noticias/titulo-do-post? /sobre ou /about? /contato ou /fale-conosco? URLs devem ser consistentes com a estratégia SEO, intuitivas para o usuário e alinhadas com a terminologia oficial da marca. Mudanças de URL após indexação pelo Google custam autoridade SEO, mesmo com 301 correto.

- **Mapa de redirecionamentos**: Se o projeto substitui um site existente, levantar todas as URLs ativas do site atual (via Google Search Console, Screaming Frog ou sitemap existente) e mapear cada uma para sua equivalente no novo site. URLs sem equivalente devem redirecionar para a página mais relevante ou para a home, nunca resultar em 404. Este trabalho é frequentemente subestimado — um site com 200 páginas pode gerar um mapa de redirecionamentos complexo que leva dias para ser validado.

- **Esquema de metadados SEO**: Definir o padrão de preenchimento de metadados para cada template — título da aba (formato: "Página | Nome do Site"), meta description (tamanho ideal 150–160 caracteres), Open Graph (og:title, og:description, og:image com dimensões padrão 1200×630px), dados estruturados Schema.org por tipo de página. Idealmente esses campos são gerenciáveis pelo CMS de forma independente do conteúdo principal da página, com fallbacks automáticos quando não preenchidos.

- **Breakpoints e comportamento responsivo**: Definir o conjunto de breakpoints que o projeto vai suportar (ex.: 375px mobile, 768px tablet, 1024px desktop, 1440px wide) e documentar como cada componente se comporta em cada um. Especial atenção a componentes complexos como navegação (menu hambúrguer no mobile, dropdown no desktop), tabelas (scroll horizontal ou reformatação em cards), e imagens de hero (crop diferente por breakpoint usando art direction).

### Perguntas

1. O sitemap completo foi validado e aprovado pelo cliente, incluindo todas as páginas previstas para o MVP? [fonte: Marketing, Diretoria] [impacto: Designer, Dev, PM]
2. Os modelos de conteúdo foram definidos campo a campo para cada template de página (obrigatórios, opcionais, tipos)? [fonte: Conteúdo, Designer] [impacto: Dev]
3. A estrutura de URLs e slugs foi definida e é consistente com a estratégia SEO e terminologia da marca? [fonte: Marketing, Agência de SEO] [impacto: Dev, SEO]
4. Foi produzido o mapa completo de redirecionamentos do site anterior para o novo, cobrindo todas as URLs indexadas? [fonte: TI, Agência anterior, Agência de SEO] [impacto: Dev, SEO]
5. O esquema de metadados SEO foi especificado para cada template (título, description, OG, canonical, Schema.org)? [fonte: Agência de SEO, Marketing] [impacto: Dev, SEO]
6. Os breakpoints e o comportamento responsivo de cada componente foram documentados formalmente? [fonte: Designer] [impacto: Dev, QA]
7. Existe wireframe ou protótipo aprovado antes de avançar para o design de alta fidelidade? [fonte: Designer, Diretoria] [impacto: Dev, PM]
8. As regras de fallback para campos opcionais não preenchidos foram definidas (imagem padrão, texto genérico)? [fonte: Designer, Conteúdo] [impacto: Dev]
9. O modelo de tags, categorias e filtros foi especificado para seções de listagem (blog, portfólio, casos)? [fonte: Conteúdo, Marketing] [impacto: Dev, SEO]
10. Foram identificados todos os componentes com variações (card com e sem imagem, hero com e sem vídeo)? [fonte: Designer] [impacto: Dev]
11. O volume de conteúdo a migrar foi quantificado com precisão e o esforço de migração foi estimado no cronograma? [fonte: TI, Marketing, Agência anterior] [impacto: Dev, PM, Conteúdo]
12. As regras de validação de campos no CMS foram especificadas (limite de caracteres, formatos de imagem aceitos)? [fonte: Conteúdo, Designer] [impacto: Dev]
13. O esquema de dados estruturados Schema.org foi mapeado por tipo de conteúdo (Article, Organization, FAQ, Product)? [fonte: Agência de SEO] [impacto: Dev, SEO]
14. Os critérios de qualidade do conteúdo migrado foram definidos (revisão de texto, reotimização de imagens)? [fonte: Marketing, Conteúdo] [impacto: Conteúdo, PM]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes do início do Setup? [fonte: Diretoria, Marketing] [impacto: PM, Dev, Designer]

---

## Etapa 05 — Architecture

- **Escolha do SSG**: A seleção do Static Site Generator define o ecossistema de desenvolvimento e deve considerar o perfil do time. Next.js é indicado quando o time já trabalha com React, quando há necessidade de ISR (Incremental Static Regeneration para conteúdo que muda frequentemente sem rebuild completo), ou quando há planos de adicionar rotas de API no futuro. Astro é indicado para projetos com foco extremo em performance (zero JS por padrão, islands architecture) e para times que não querem se comprometer com um único framework de componentes. Hugo é indicado para projetos com grande volume de conteúdo em Markdown e time familiarizado com Go templates — seus builds são ordens de magnitude mais rápidos que alternativas JS. Eleventy é indicado quando a simplicidade e flexibilidade de templating são prioritárias sobre ecossistema.

- **Escolha do CMS headless**: Se o CMS for necessário, a seleção deve considerar: perfil técnico do time de conteúdo (CMS mais simples para não-técnicos vs. mais flexível para devs), volume de conteúdo esperado, orçamento mensal, e necessidade de self-hosting. Contentful e Sanity são os mais maduros para times não-técnicos, mas têm custo relevante em planos enterprise. Strapi é a melhor opção self-hosted open-source — zero custo de licença, mas exige infraestrutura para hospedar (servidor Node.js + banco de dados). Decap CMS (ex-Netlify CMS) é Git-based e gratuito — ideal para projetos pequenos onde o fluxo de publicação via PR é aceitável.

- **Hospedagem e CDN**: A escolha da plataforma de hospedagem impacta o workflow de deploy, os custos e os limites de build. Vercel oferece a melhor integração com Next.js (mesma empresa), deploy previews automáticos por PR, e edge functions nativas — porém tem pricing baseado em bandwidth e execuções que pode surpreender em sites de alto tráfego. Netlify é mais agnóstico de framework, tem generoso plano gratuito para projetos pequenos, e Netlify Forms elimina a necessidade de backend para formulários simples. Cloudflare Pages tem edge CDN global extremamente rápido e plano gratuito muito generoso — ideal quando custo é restrição principal. AWS CloudFront + S3 é a opção de maior controle e menor custo em escala, mas exige configuração manual e conhecimento de AWS.

- **Pipeline de imagens**: Imagens são o maior fator de impacto no Lighthouse Performance de sites estáticos. A estratégia deve definir: otimização automática no build (sharp, imagemin) ou em CDN (Cloudinary, imgix, Cloudflare Images), formatos modernos (WebP e AVIF com fallback para browsers legados), lazy loading nativo (loading="lazy") ou via Intersection Observer, e srcset com múltiplos tamanhos para servir a resolução adequada por dispositivo. Projetos com Next.js têm next/image como solução nativa que resolve a maioria desses requisitos automaticamente.

- **Solução para formulários**: Sites estáticos não têm backend, mas frequentemente precisam de formulários de contato. As opções variam em complexidade: Netlify Forms é zero-config para sites hospedados no Netlify (detecta automaticamente o atributo netlify no HTML), Formspree e Web3Forms são serviços externos que processam submissões e enviam e-mail — planos gratuitos cobrem maioria dos casos, Resend ou AWS SES via serverless function (Vercel Edge Function, Netlify Function) oferecem mais controle e personalização do e-mail, mas exigem código. A escolha deve considerar volume de submissões esperado, necessidade de integração com CRM, e se há dados sensíveis no formulário (que exigem HTTPS end-to-end, mas não necessariamente backend próprio).

- **Estratégia de build e deploy**: Definir o pipeline de CI/CD: qualquer push para main dispara build e deploy automático, PRs geram deploy preview em URL temporária para revisão, branches de feature têm deploys opcionais. GitHub Actions é a opção mais flexível e gratuita para repositórios públicos — permite builds customizados, testes automatizados antes do deploy, e notificações. Vercel CI e Netlify CI são mais simples de configurar (zero config para frameworks suportados) mas menos customizáveis. O pipeline deve incluir ao menos: lint, build com sucesso, e link checker antes de mergear para main.

- **Fontes tipográficas**: A escolha entre self-hosted e Google Fonts tem implicações em performance e privacidade. Google Fonts tem cache compartilhado entre sites (vantagem de performance em browsers antigos, mas irrelevante em browsers modernos que isolam cache por domínio), fácil integração, mas envia o IP do visitante para servidores do Google — o que pode ser relevante para compliance LGPD/GDPR. Self-hosted (fontes servidas do mesmo CDN do site) elimina a dependência externa, melhora o LCP (sem request adicional no critical path), e remove a preocupação de privacidade — é o padrão recomendado para projetos com requisitos de conformidade.

### Perguntas

1. O SSG escolhido é adequado ao perfil técnico do time e às necessidades do projeto (ISR, ecossistema, volume de build)? [fonte: TI, Dev atual] [impacto: Dev]
2. A escolha do CMS headless considera o perfil dos editores, volume de conteúdo, orçamento e necessidade de self-hosting? [fonte: Conteúdo, Financeiro, TI] [impacto: Dev, Conteúdo, DevOps]
3. A plataforma de hospedagem e CDN foi escolhida considerando custo projetado, performance e requisitos de compliance? [fonte: TI, Financeiro, Jurídico] [impacto: Dev, DevOps]
4. Existe estratégia definida para otimização de imagens (next/image, Cloudinary, otimização no build)? [fonte: Designer, TI] [impacto: Dev]
5. A solução para formulários sem backend foi escolhida e as limitações do plano gratuito foram avaliadas? [fonte: Marketing, Financeiro] [impacto: Dev]
6. O pipeline de CI/CD foi desenhado com preview por branch, lint e build obrigatórios antes do merge para main? [fonte: TI] [impacto: Dev, DevOps]
7. A estratégia de fontes foi definida (self-hosted vs. Google Fonts) considerando performance e LGPD? [fonte: Designer, Jurídico] [impacto: Dev]
8. Todas as dependências externas (APIs, SDKs de terceiros) foram listadas e sua confiabilidade avaliada? [fonte: TI, Fornecedores SaaS] [impacto: Dev, DevOps]
9. Existe estratégia para conteúdo com necessidade de atualização frequente sem rebuild completo (ISR, on-demand revalidation)? [fonte: Conteúdo, Marketing] [impacto: Dev]
10. A arquitetura suporta o escopo futuro previsto (multilíngue, mais templates, crescimento de volume de conteúdo)? [fonte: Diretoria, Marketing] [impacto: Dev, Arquiteto]
11. Os custos mensais de operação da arquitetura escolhida foram calculados em cenário esperado e pior caso? [fonte: Financeiro, TI] [impacto: PM, Dev]
12. Existe plano de contingência se o CMS headless ficar indisponível (último build cacheado no CDN como fallback)? [fonte: TI, Fornecedor CMS] [impacto: Dev, DevOps]
13. A estratégia de cache no CDN foi definida (TTL por tipo de asset, política de purge pós-publicação)? [fonte: TI] [impacto: Dev, DevOps]
14. A solução de analytics e tracking foi definida com estratégia de performance (defer/async, Tag Manager, facade)? [fonte: Marketing, TI] [impacto: Dev]
15. O modelo de branches e ambientes (production, staging, preview) foi desenhado, documentado e aprovado pelo time? [fonte: TI] [impacto: Dev, DevOps, PM]

---

## Etapa 06 — Setup

- **Estrutura do repositório**: Organizar o repositório com separação clara entre componentes reutilizáveis (botões, cards, navegação), templates de página (layouts), conteúdo (Markdown ou dados JSON quando sem CMS), assets estáticos (imagens, fontes, ícones) e configurações (SSG, CMS, CI/CD). Um repositório bem organizado desde o início reduz o tempo de onboarding de novos contribuidores e facilita a localização de arquivos durante o build — especialmente importante quando há múltiplos templates e o volume de conteúdo cresce.

- **Variáveis de ambiente**: Configurar todas as chaves e tokens externos como variáveis de ambiente — nunca hardcoded no código. Isso inclui: API key e Space ID do CMS headless, ID de propriedade do Google Analytics, tokens de deploy, chaves de formulários externos, e qualquer outro segredo. Configurar tanto localmente (.env.local, que deve estar no .gitignore) quanto na plataforma de hospedagem (Vercel Environment Variables, Netlify Environment Variables). Separar variáveis de produção e staging — CMS headless geralmente tem ambientes distintos para evitar que conteúdo em rascunho apareça em produção.

- **Deploy previews por Pull Request**: Configurar o ambiente para que cada PR aberto gere automaticamente um deploy preview com URL única e temporária. Este recurso é fundamental para o fluxo de trabalho — permite que o cliente ou o time de design revise mudanças visuais e de conteúdo antes do merge, sem precisar rodar o projeto localmente. A URL do preview deve ser compartilhada automaticamente como comentário no PR (Vercel e Netlify fazem isso nativamente com integração GitHub).

- **Setup do CMS**: Criar o workspace ou projeto no CMS escolhido, configurar os modelos de conteúdo definidos na etapa anterior (campos, validações, tipos de dados), criar os papéis de usuário (admin, editor, autor) com permissões apropriadas, e criar os ambientes (production e staging/preview). Adicionar os primeiros usuários e fazer o invite para o time de conteúdo nesta fase — treinamento funciona melhor com o CMS já configurado com os modelos reais do projeto.

- **Configuração de domínio e DNS**: Registrar ou transferir o domínio se necessário, configurar os registros DNS apontando para a plataforma de hospedagem (geralmente um registro CNAME ou A), ativar o SSL/TLS automático (Let's Encrypt via Vercel/Netlify, ou certificado gerenciado via Cloudflare), e definir o comportamento de www vs. naked domain (ex.: redirecionar www para raiz ou vice-versa). Esta configuração deve ser feita com antecedência suficiente para propagação de DNS não virar urgência no dia do go-live.

- **Fluxo de publicação**: Definir e documentar o fluxo completo: dev faz push para branch → CI/CD roda lint e build → deploy preview gerado → revisão e aprovação → merge para main → deploy automático em produção. Se o cliente vai publicar conteúdo via CMS, definir se a publicação no CMS dispara rebuild automático (via webhook) ou se o rebuild acontece em schedule (ex.: a cada hora). Webhooks são mais imediatos mas podem gerar muitos builds em dias de muita edição — schedule é mais econômico para sites com conteúdo que não precisa aparecer instantaneamente.

### Perguntas

1. A estrutura de pastas do repositório foi definida, documentada e seguida desde o primeiro commit? [fonte: Dev] [impacto: Dev]
2. Todas as variáveis de ambiente foram identificadas, documentadas e configuradas nos ambientes corretos (local, staging, produção)? [fonte: TI, Fornecedores SaaS] [impacto: Dev, DevOps]
3. O .gitignore está configurado corretamente para excluir .env, secrets e arquivos gerados no build? [fonte: Dev] [impacto: Dev, DevOps]
4. Os deploy previews automáticos por PR estão funcionando e gerando URLs compartilháveis nos comentários do PR? [fonte: Dev] [impacto: Dev, Designer, PM]
5. O workspace do CMS foi criado com todos os modelos de conteúdo definidos na etapa de Definition? [fonte: Dev, Fornecedor CMS] [impacto: Dev, Conteúdo]
6. Os papéis de usuário no CMS foram criados com permissões corretas para cada perfil (admin, editor, autor)? [fonte: Dev, Conteúdo] [impacto: Conteúdo]
7. Os ambientes do CMS (production e staging/preview) foram configurados e estão isolados corretamente? [fonte: Dev, Fornecedor CMS] [impacto: Dev, Conteúdo]
8. O domínio foi configurado na plataforma de hospedagem, o SSL está ativo e o comportamento www vs. naked domain está definido? [fonte: TI, Fornecedor de hospedagem] [impacto: DevOps, Dev]
9. O webhook de rebuild (publicação no CMS → deploy na hospedagem) foi configurado e testado end-to-end? [fonte: Dev] [impacto: Dev, Conteúdo]
10. O fluxo completo de publicação foi documentado de forma que o time de conteúdo possa seguir sem suporte técnico? [fonte: Dev, PM] [impacto: Conteúdo]
11. As integrações de terceiros (analytics, pixels, chat) foram configuradas com variáveis de ambiente separadas por ambiente? [fonte: Marketing, Dev] [impacto: Dev]
12. O processo de onboarding de novos desenvolvedores foi documentado no README com instruções de setup local? [fonte: Dev] [impacto: Dev]
13. Os primeiros usuários do CMS foram convidados, acessaram com sucesso e conseguem criar conteúdo de teste? [fonte: Conteúdo, Marketing] [impacto: Conteúdo, PM]
14. O ambiente de staging está funcional e completamente isolado do ambiente de produção em dados e configurações? [fonte: Dev] [impacto: Dev, DevOps, QA]
15. O pipeline de CI/CD foi testado com um PR real — lint passou, build completou, preview foi gerado? [fonte: Dev] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Sistema de componentes**: Implementar os componentes base seguindo o design system definido — tipografia (escala de tamanhos, pesos, line-heights), paleta de cores como variáveis CSS ou tokens do framework, espaçamento sistemático (múltiplos de 4px ou 8px), e componentes atômicos reutilizáveis (Button com variantes primary/secondary/ghost, Card, Badge, Input, Textarea). Componentes bem estruturados desde o início reduzem o tempo de implementação dos templates e garantem consistência visual sem esforço — qualquer mudança de cor ou tipografia propagada por variável reflete automaticamente em todo o site.

- **Templates de página**: Implementar cada template mapeado no sitemap — home (geralmente o mais complexo, com múltiplas seções), página interna genérica (hero + conteúdo rico), página de listagem (blog, casos de sucesso, produtos), página de detalhe (post individual, case individual), página de contato (formulário + mapa + informações), e página 404 customizada (com navegação funcional e CTA para home). Cada template deve ser validado contra o design aprovado antes de passar para o próximo, evitando acúmulo de débito de revisão no final.

- **Migração de conteúdo**: A entrada de conteúdo no CMS ou nos arquivos Markdown é frequentemente o maior gargalo do build em projetos de site estático. Se há conteúdo a migrar de um site legado, planejar com antecedência: quem migra (dev, redator, ou automação via script de scraping + formatação), qual é o critério de qualidade do conteúdo migrado (texto puro, imagens otimizadas, formatação revisada), e qual é o prazo. Conteúdo novo (não migrado) também precisa de prazo acordado com o cliente — entregar o site sem conteúdo final impede testes reais de layout e QA de SEO.

- **Otimização de imagens no pipeline**: Configurar a geração automática de múltiplos formatos e tamanhos durante o build. Para Next.js, next/image cuida disso on-demand com cache. Para Hugo e Eleventy, usar shortcodes ou plugins que processam imagens durante o build. Garantir que todas as imagens de conteúdo sejam servidas em WebP com fallback JPEG/PNG, que imagens de hero tenham versões 1x e 2x para retina, e que o atributo loading="lazy" esteja presente em todas as imagens abaixo do fold — esses três itens juntos representam a maior parte do ganho de Lighthouse Performance.

- **Internacionalização (se aplicável)**: Implementar o suporte a múltiplos idiomas com roteamento por locale (/pt-BR/, /en/, /es/), fallback configurado para idioma padrão quando tradução não existe, e atributos hreflang corretos no `<head>` de cada página para que o Google sirva a versão correta por região. O modelo de conteúdo no CMS deve ter sido preparado na Etapa 06 para suportar múltiplas entradas por locale — implementar i18n em um CMS já populado com conteúdo monolíngue é custoso e propenso a erros.

- **Scripts de terceiros com impacto em performance**: Integrar analytics (GA4, Plausible, Fathom), pixels de conversão (Meta Pixel, LinkedIn Insight Tag) e ferramentas de suporte (chat, heatmap) sem destruir o Lighthouse Performance. A estratégia padrão é: carregar scripts não-críticos com strategy="afterInteractive" ou strategy="lazyOnload" (Next.js) ou com defer/async, usar facade pattern para embeds pesados (vídeos do YouTube carregados como imagem clicável que instancia o iframe apenas no clique), e consolidar todos os scripts de tracking em um único container de Tag Manager sempre que possível.

- **Acessibilidade**: Implementar conformidade com WCAG 2.1 nível AA ao longo do build, não como checklist final. Os requisitos mais frequentemente negligenciados em sites estáticos são: contraste de cor mínimo 4.5:1 para texto normal e 3:1 para texto grande (verificar com ferramenta como Colour Contrast Analyser), textos alternativos descritivos e não-redundantes em todas as imagens, landmarks HTML semânticos (header, main, nav, footer) para navegação por screen reader, e foco visível em todos os elementos interativos — não remover o outline do browser sem substituir por alternativa visível.

### Perguntas

1. Todos os componentes base do design system foram implementados e revisados antes de iniciar os templates de página? [fonte: Designer] [impacto: Dev]
2. Cada template foi validado visualmente contra o design aprovado antes de avançar para o próximo? [fonte: Designer, Diretoria] [impacto: Dev, PM]
3. O conteúdo real (não lorem ipsum) está sendo usado nos templates durante o desenvolvimento para revelar problemas de layout? [fonte: Conteúdo, Marketing] [impacto: Dev, Designer]
4. O pipeline de otimização de imagens está gerando WebP/AVIF com fallback e múltiplos tamanhos via srcset? [fonte: Dev] [impacto: Dev, QA]
5. O lazy loading está implementado corretamente em todas as imagens abaixo do fold (sem lazy no hero/LCP)? [fonte: Dev] [impacto: Dev, QA]
6. Os scripts de terceiros estão sendo carregados de forma assíncrona para não bloquear o render inicial? [fonte: Marketing, Dev] [impacto: Dev]
7. A implementação de acessibilidade está sendo feita ao longo do build com axe-core ou similar, não apenas no final? [fonte: Designer, Compliance] [impacto: Dev, QA]
8. Os formulários têm validação client-side e mensagens de erro claras para cada campo com problema? [fonte: Designer] [impacto: Dev]
9. A página 404 customizada está implementada com navegação funcional e CTA relevante para recuperar o usuário? [fonte: Designer, Marketing] [impacto: Dev]
10. O i18n (se aplicável) está implementado com roteamento por locale, fallback correto e hreflang no head? [fonte: Conteúdo, Marketing] [impacto: Dev, SEO]
11. Os metadados SEO de cada página estão sendo preenchidos de forma única (não o mesmo título/description para todas)? [fonte: Conteúdo, Agência de SEO] [impacto: Dev, SEO]
12. Os dados estruturados Schema.org estão implementados e foram validados com o Google Rich Results Test? [fonte: Agência de SEO] [impacto: Dev, SEO]
13. O facade pattern está sendo usado para embeds pesados (YouTube, Vimeo, chat ao vivo)? [fonte: Dev] [impacto: Dev, QA]
14. O progresso da migração de conteúdo está dentro do prazo acordado e sem bloqueadores de aprovação? [fonte: Conteúdo, Marketing, Diretoria] [impacto: PM, Dev]
15. Os estados de erro, loading e vazio de componentes dinâmicos (listagens, formulários) estão implementados? [fonte: Designer] [impacto: Dev]

---

## Etapa 08 — QA

- **Auditoria Lighthouse por template**: Rodar o Lighthouse (via Chrome DevTools ou PageSpeed Insights) para cada template de página distinto, não apenas para a home. Targets recomendados: Performance ≥90, Accessibility ≥90, SEO ≥90, Best Practices ≥90. A pontuação de Performance em produção (com CDN real) tende a ser 5-15 pontos maior que em localhost — portanto rodar no ambiente de staging/preview antes do go-live é essencial. Os principais fatores de impacto no Performance são LCP (Largest Contentful Paint), CLS (Cumulative Layout Shift de imagens sem dimensões definidas) e INP (Interaction to Next Paint para páginas com JavaScript pesado).

- **Testes de responsividade**: Validar cada template nos breakpoints definidos (375px, 768px, 1024px, 1440px) em browsers reais ou emulação do DevTools. Focar em: textos que quebram ou transbordam o container, imagens que distorcem ou perdem o crop correto, botões e links com área de toque menor que 44×44px no mobile (requisito WCAG), e menus de navegação que ficam inacessíveis em telas pequenas. Testar também orientação landscape no mobile — frequentemente ignorada e frequentemente quebrada em sites com layouts de hero que assumem portrait.

- **Verificação de links e recursos**: Rodar um link checker automatizado (Screaming Frog, broken-link-checker, lychee) em todas as páginas para identificar links internos quebrados, imagens com src inválido, e recursos externos inacessíveis. Links externos para sites de terceiros devem abrir em nova aba (target="_blank") com rel="noopener noreferrer" por segurança. PDFs e documentos para download devem ser verificados — arquivo existe, tem tamanho razoável, abre corretamente.

- **Teste de formulários**: Submeter cada formulário com dados válidos e verificar: recebimento do e-mail de notificação no destino correto, mensagem de sucesso exibida ao usuário, e comportamento correto em caso de erro (campo obrigatório vazio, formato inválido). Testar também o comportamento anti-spam se configurado (honeypot, reCAPTCHA) — verificar que não bloqueia submissões legítimas e que bots são filtrados. Se o formulário integra com CRM, verificar que o lead aparece corretamente no sistema de destino.

- **Fluxo de publicação no CMS**: Validar o ciclo completo de publicação com um usuário do tipo editor (não admin) — criar um novo conteúdo, salvar como rascunho, solicitar revisão, publicar, verificar que aparece no site (após rebuild se necessário), despublicar, e verificar que some do site. Testar upload de imagem no CMS com arquivo de tamanho real (não apenas arquivo de 10KB de teste) para identificar limites de upload ou lentidão. Verificar que o webhook de rebuild dispara corretamente após publicação se o fluxo for webhook-based.

- **Metadados e previews sociais**: Verificar o Open Graph de cada template usando as ferramentas de debug das plataformas: Facebook Sharing Debugger, LinkedIn Post Inspector, Twitter Card Validator. Confirmar que og:image tem as dimensões corretas (1200×630px), que o título não está truncado (máximo ~60 caracteres), e que a imagem de preview está correta para cada tipo de página — não apenas a imagem padrão do site em todos os posts. Verificar também o favicon em múltiplos formatos (16×16, 32×32, 180×180 para Apple Touch Icon, SVG para browsers modernos) e o manifest.json se o site precisar funcionar como PWA instalável.

- **Teste de velocidade em CDN edge**: Rodar testes de velocidade a partir de regiões geográficas relevantes para o público-alvo do site (WebPageTest permite escolher o servidor de origem do teste). Sites hospedados em CDN global tendem a ter performance homogênea independente da região, mas vale verificar especialmente se há assets servidos de origens fora do CDN (fonts do Google, imagens de CMS headless sem CDN configurado) que podem ter latência alta para usuários distantes.

### Perguntas

1. O Lighthouse foi rodado para cada template de página distinto (não apenas a home) com scores ≥90 em todos os eixos? [fonte: Dev] [impacto: Dev, QA]
2. Os testes de responsividade cobrem todos os breakpoints definidos, incluindo orientação landscape no mobile? [fonte: Dev, QA] [impacto: Dev, Designer]
3. O link checker automatizado foi rodado e todos os 404s e recursos inválidos foram corrigidos? [fonte: Dev, QA] [impacto: Dev, SEO]
4. Todos os formulários foram testados end-to-end com dados válidos, inválidos e campos obrigatórios vazios? [fonte: QA, Marketing] [impacto: Dev, Marketing]
5. O fluxo completo de publicação no CMS foi testado por um usuário com perfil de editor (não administrador)? [fonte: Conteúdo] [impacto: Conteúdo, Dev]
6. Os metadados Open Graph foram validados com Facebook Debugger, LinkedIn Inspector e Twitter Card Validator? [fonte: Dev, Marketing] [impacto: SEO, Marketing]
7. O favicon está correto em todos os formatos necessários (16×16, 32×32, 180×180 Apple Touch, SVG)? [fonte: Designer, Dev] [impacto: Dev]
8. O teste de velocidade foi executado em CDN edge a partir das regiões geográficas do público-alvo? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
9. A revisão ortográfica e de consistência de conteúdo foi concluída em todas as páginas do site? [fonte: Conteúdo, Marketing] [impacto: Conteúdo]
10. Os dados estruturados Schema.org foram validados com o Google Rich Results Test sem erros críticos? [fonte: Dev, Agência de SEO] [impacto: SEO, Dev]
11. O robots.txt foi verificado e não está bloqueando páginas que deveriam ser indexadas em produção? [fonte: Dev] [impacto: SEO, Dev]
12. O sitemap.xml contém exclusivamente URLs do ambiente de produção (sem localhost ou staging)? [fonte: Dev] [impacto: SEO, Dev]
13. Todos os eventos de analytics configurados (conversões, CTAs, scroll) estão sendo disparados corretamente? [fonte: Dev, Marketing] [impacto: Marketing]
14. O comportamento de hover, focus e active de todos os elementos interativos foi validado em mouse e teclado? [fonte: QA, Designer] [impacto: Dev, Designer]
15. O teste de acessibilidade com screen reader (NVDA ou VoiceOver) foi realizado nas páginas principais? [fonte: QA, Dev] [impacto: Dev]

---

## Etapa 09 — Launch Prep

- **Mapa de redirecionamentos no CDN**: Configurar todas as regras de redirect (301 permanente) antes do go-live — não após. A configuração depende da plataforma: Vercel usa o arquivo vercel.json, Netlify usa o arquivo _redirects ou netlify.toml, Cloudflare Pages usa _redirects. Testar cada regra individualmente antes do go-live, especialmente as que envolvem wildcards (ex.: /blog/* → /noticias/*). Um redirect mal configurado pode resultar em loop de redirect (301 circular) ou em 404 para URLs que deveriam estar funcionando — ambos prejudicam SEO e experiência.

- **Plano de cutover de DNS**: Reduzir o TTL do domínio para 300 segundos (5 minutos) com 24-48h de antecedência — isso garante que a troca de DNS propague rapidamente no dia do go-live. Documentar a sequência exata de ações: quem acessa o painel de DNS, qual registro será alterado (CNAME, A ou AAAA), qual o valor atual e o novo valor, e como validar que a propagação ocorreu (dnschecker.org, dig). Manter a hospedagem antiga ativa e funcional por pelo menos 48h após o cutover — usuários com DNS cacheado no valor antigo continuarão acessando o site antigo durante a propagação, e isso é esperado.

- **SEO técnico pré-lançamento**: Verificar e corrigir antes do go-live: sitemap.xml gerado corretamente com todas as URLs de produção (não de staging), robots.txt com Disallow: / removido do ambiente de produção (erro clássico que bloqueia indexação), canonical tags apontando para URLs de produção (não para localhost ou staging), e verificação da propriedade no Google Search Console (via HTML tag, DNS ou Google Analytics) feita com antecedência para não atrasar a submissão do sitemap. O Search Console leva alguns dias para validar a propriedade — não deixar para fazer no dia do go-live.

- **Analytics e eventos de conversão**: Configurar as metas e eventos de conversão antes do go-live — não é possível recuperar dados do passado em analytics. No Google Analytics 4, configurar eventos de conversão para: submissão de formulário de contato, clique em CTA principal, scroll até 90% da home, e qualquer ação de negócio relevante. Se há Meta Pixel ou LinkedIn Insight Tag, configurar os eventos de conversão correspondentes para que campanhas pagas possam medir resultados desde o primeiro dia. Testar cada evento com o GA4 DebugView e o Meta Pixel Helper antes do lançamento.

- **Treinamento do time de conteúdo**: Realizar sessão de treinamento com todos os usuários que vão operar o CMS após o lançamento — não apenas os admins. Cobrir: criação e edição de conteúdo, upload e gerenciamento de mídia, uso de rascunhos e fluxo de aprovação, publicação e agendamento, e contato de suporte em caso de problema. Entregar documentação em formato simples (Google Doc ou Notion) com capturas de tela — a memória de um treinamento presencial dura pouco, e as perguntas vão aparecer semanas depois quando o treinamento já foi esquecido.

- **Rollback e contingência**: Documentar o plano de rollback antes do go-live: se algo der errado nas primeiras horas, qual a sequência de ações para reverter? Para DNS, a reversão é apontar os registros de volta para o servidor antigo — que deve estar ativo. Para o conteúdo, garantir que o site antigo não foi desativado ou que há um snapshot funcional. Definir critérios claros de quando acionar o rollback (ex.: taxa de erro 5xx acima de 1%, formulários não funcionando, home com layout quebrado) e quem tem autoridade para tomar essa decisão.

### Perguntas

1. Todas as regras de redirect (301) foram configuradas na plataforma correta e testadas individualmente antes do go-live? [fonte: Dev, Agência de SEO] [impacto: SEO, Dev]
2. O TTL do DNS foi reduzido para 300s com pelo menos 24h de antecedência ao cutover? [fonte: TI, Fornecedor de DNS] [impacto: DevOps, Dev]
3. O plano de cutover de DNS está documentado com sequência exata, responsável designado e método de validação? [fonte: TI, DevOps] [impacto: DevOps, PM]
4. A propriedade foi verificada no Google Search Console com antecedência e o sitemap está pronto para submissão imediata? [fonte: Dev, Marketing] [impacto: SEO, Dev]
5. O robots.txt do ambiente de produção não contém Disallow: / e permite indexação de todas as páginas esperadas? [fonte: Dev] [impacto: SEO]
6. Todas as tags canônicas apontam para URLs corretas de produção (sem staging, localhost ou http)? [fonte: Dev] [impacto: SEO]
7. Os eventos de conversão no GA4 foram configurados e testados com o DebugView em ambiente de produção? [fonte: Marketing, Dev] [impacto: Marketing]
8. O Meta Pixel e outros pixels de conversão foram validados com as ferramentas de debug das respectivas plataformas? [fonte: Marketing, Dev] [impacto: Marketing]
9. O treinamento do time de conteúdo foi realizado e a documentação de operação do CMS foi entregue? [fonte: Conteúdo, PM] [impacto: Conteúdo]
10. A hospedagem antiga está garantida como ativa por pelo menos 48h após o cutover como fallback de rollback? [fonte: TI, Fornecedor de hospedagem anterior] [impacto: DevOps, PM]
11. O plano de rollback está documentado com critérios claros de acionamento e responsável designado para a decisão? [fonte: TI, Diretoria] [impacto: PM, DevOps, Dev]
12. Todos os stakeholders foram notificados sobre a data, horário e impactos esperados do go-live? [fonte: Diretoria] [impacto: PM]
13. O monitoramento de disponibilidade (UptimeRobot, Better Uptime ou similar) está configurado para alertar em tempo real? [fonte: Dev, DevOps] [impacto: DevOps, Dev]
14. A lista de acessos a serem entregues ao cliente foi revisada e todos os acessos foram testados e funcionam? [fonte: Dev, DevOps, Fornecedores SaaS] [impacto: PM]
15. A janela de cutover foi escolhida estrategicamente (horário de baixo tráfego, dia útil com time de suporte disponível)? [fonte: Marketing, TI] [impacto: PM, DevOps]

---

## Etapa 10 — Go-Live

- **Cutover de DNS e monitoramento de propagação**: Executar a troca dos registros DNS conforme o plano documentado na etapa anterior. Monitorar a propagação usando dnschecker.org para verificar que os servidores DNS ao redor do mundo estão resolvendo o domínio para o novo endereço — com TTL de 5 minutos, a propagação global deve ocorrer em menos de 30 minutos. Verificar o SSL imediatamente após a propagação — Vercel e Netlify provisionam o certificado automaticamente quando o DNS aponta corretamente, mas pode levar alguns minutos. Um certificado não provisionado resulta em aviso de segurança no browser para todos os visitantes.

- **Purge de cache e validação do deploy final**: Após confirmar que o DNS está propagado e o SSL está ativo, executar purge de cache no CDN para garantir que todas as edges estão servindo a versão mais recente do site (não um cache antigo do deploy de staging). Acessar o site de pelo menos dois dispositivos diferentes (desktop e mobile) em redes diferentes (sem cache local) e verificar visualmente as páginas principais. Confirmar que os formulários funcionam em produção — o comportamento pode diferir de staging se as variáveis de ambiente não foram configuradas corretamente.

- **Submissão do sitemap e Search Console**: Acessar o Google Search Console e submeter o sitemap.xml (URL: https://dominio.com/sitemap.xml) para solicitar indexação das páginas. O Google não indexa imediatamente — o primeiro crawl pode levar de horas a dias dependendo da autoridade do domínio. Verificar se há erros de cobertura (páginas bloqueadas por robots.txt, URLs com redirect incorreto, páginas com canonical apontando para versão diferente). Para sites que substituem um domínio existente com histórico de SEO, fazer a solicitação de mudança de endereço no Search Console se o domínio mudou.

- **Auditoria Lighthouse em produção**: Rodar o Lighthouse via PageSpeed Insights (que usa servidores externos, não localhost) para cada template de página logo após o go-live. Os scores em produção tendem a ser melhores que em staging devido ao CDN real, mas podem revelar problemas que não apareceram antes — como scripts de terceiros carregados apenas em produção (pixels de tracking, chat ao vivo) que impactam o Performance. Documentar os scores iniciais como baseline — serão usados para comparação em futuras auditorias e para demonstrar ao cliente o padrão de qualidade entregue.

- **Monitoramento da primeira semana**: Monitorar ativamente nos primeiros 7 dias após o lançamento: erros de crawl no Google Search Console (especialmente 404s inesperados e páginas bloqueadas por robots), Core Web Vitals reais do CrUX (dados reais de usuários, disponíveis no Search Console após acúmulo de tráfego suficiente), taxa de erro no hosting dashboard (5xx devem ser próximos de zero em site estático sem serverless functions), e alertas de disponibilidade (UptimeRobot ou Better Uptime em plano gratuito). Se houver campanhas pagas ativas desde o lançamento, monitorar também os eventos de conversão no analytics para confirmar que o tracking está funcionando.

- **Entrega e handoff ao cliente**: Entregar formalmente todos os acessos ao cliente com documentação do que cada acesso representa: acesso ao repositório (GitHub/GitLab) com instruções de como fazer deploy manual se necessário, acesso à plataforma de hospedagem (Vercel/Netlify) com documentação do fluxo de deploy e variáveis de ambiente, acesso ao CMS com guia de uso por perfil (admin vs. editor), acesso ao Google Analytics e Search Console, e acesso ao provedor de DNS (especialmente importante — clientes frequentemente não sabem onde seu domínio está registrado). A documentação mínima deve incluir: como rodar o projeto localmente, como fazer deploy, como adicionar/editar conteúdo no CMS, e contato de suporte técnico com SLA.

### Perguntas

1. A propagação do DNS foi confirmada em múltiplas regiões geográficas usando ferramenta de checagem global? [fonte: DevOps, Fornecedor de DNS] [impacto: DevOps, Dev]
2. O SSL foi provisionado corretamente e está válido — nenhum aviso de segurança aparece em nenhum browser? [fonte: Dev, Fornecedor de hospedagem] [impacto: DevOps, Dev]
3. O purge de cache do CDN foi executado e confirmado após o deploy final em produção? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
4. O site foi acessado e validado visualmente de dispositivos e redes diferentes (sem cache local)? [fonte: QA, Dev] [impacto: Dev, PM]
5. Os formulários foram testados em produção com submissão real e o e-mail de notificação chegou ao destino correto? [fonte: QA, Marketing] [impacto: Dev, Marketing]
6. O sitemap.xml foi submetido no Google Search Console imediatamente após a confirmação do go-live? [fonte: Dev, Agência de SEO] [impacto: SEO]
7. A auditoria Lighthouse foi re-executada em produção via PageSpeed Insights e os scores foram documentados como baseline? [fonte: Dev] [impacto: Dev, SEO, PM]
8. O monitoramento de disponibilidade está ativo e foi testado (alerta chegou quando o serviço foi pausado brevemente)? [fonte: DevOps] [impacto: DevOps, Dev]
9. Os eventos de conversão no analytics foram verificados com dados reais de usuários reais em produção? [fonte: Marketing, Dev] [impacto: Marketing]
10. O Search Console foi verificado nas primeiras horas para identificar erros de cobertura ou bloqueios de crawl? [fonte: Dev, Agência de SEO] [impacto: SEO, Dev]
11. A hospedagem antiga continua ativa e funcional durante o período de contingência de 48h? [fonte: TI, Fornecedor de hospedagem anterior] [impacto: DevOps, PM]
12. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou que consegue acessar? [fonte: Dev, DevOps, Fornecedores SaaS] [impacto: PM]
13. O aceite formal de entrega foi obtido do cliente (e-mail, assinatura de ata, ou confirmação documentada)? [fonte: Diretoria] [impacto: PM]
14. O plano de suporte pós-lançamento foi ativado (canal de comunicação definido, SLA comunicado ao cliente)? [fonte: Diretoria, PM] [impacto: PM, Dev]
15. Os redirects do site antigo foram verificados em produção para confirmar que estão funcionando corretamente? [fonte: Dev, Agência de SEO] [impacto: SEO, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos um site simples, tipo um iFood"** — O cliente diz site estático mas descreve funcionalidades que exigem backend (login, pagamento, dados em tempo real). Se a descrição inclui verbos como "o usuário se cadastra", "o cliente faz pedido" ou "mostra dados ao vivo", não é site estático. Reclassificar o projeto antes de continuar.
- **"O branding está quase pronto"** — "Quase pronto" significa que vai mudar. Qualquer trabalho de design ou desenvolvimento feito sobre um brand guide provisório será refeito. O correto é travar o início do build até o brand guide estar finalizado e aprovado formalmente.
- **"Todo mundo pode atualizar o site"** — Ausência de dono de conteúdo definido. Se todos são responsáveis, ninguém é. Resultado: conteúdo desatualizado 3 meses após o go-live.

### Etapa 02 — Discovery

- **"Não temos site anterior, é tudo novo"** — Parece simplificar, mas frequentemente significa que não há conteúdo produzido (textos, fotos, cases). O esforço de produção de conteúdo do zero costuma ser maior do que migrar conteúdo existente, e esse esforço não aparece no cronograma se não for identificado aqui.
- **"SEO não é prioridade agora"** — SEO técnico (meta tags, sitemap, canonical, dados estruturados) deve ser implementado desde o build — retrofitar SEO em um site já pronto é significativamente mais caro do que fazer certo desde o início. "Não é prioridade" não pode significar "não fazer".
- **"Talvez no futuro a gente queira login"** — Um "talvez login" muda a classificação do projeto. Não é site estático com login — é web app com páginas estáticas. Precisa ser tratado como reclassificação, não como feature futura.

### Etapa 03 — Alignment

- **"O design vai sendo feito junto com o desenvolvimento"** — Design e build em paralelo sem buffer gera retrabalho contínuo. O dev implementa baseado em wireframe, o designer entrega o final diferente, o dev refaz. O correto é ter ao menos 1-2 templates de design finalizados antes de iniciar o build.
- **"A gente decide o conteúdo depois"** — Se o conteúdo não está definido (mesmo que em rascunho), os templates serão testados com lorem ipsum. Problemas de layout só aparecem com conteúdo real — títulos de 3 palavras vs. 15 palavras quebram layouts de formas diferentes.
- **"Pode usar qualquer CMS, confiamos em vocês"** — A escolha do CMS afeta diretamente o time de conteúdo que vai usar todos os dias. Decisão sem input dos editores reais resulta em CMS subutilizado ou abandonado.

### Etapa 04 — Definition

- **Sitemap aprovado "de cabeça"** — Sitemap sem documento formal resulta em páginas esquecidas que aparecem durante o build ("ah, esquecemos da página de política de privacidade"). Aprovar por escrito é gate obrigatório.
- **"Vai ter um blog, mas a gente define os campos depois"** — Modelo de conteúdo indefinido antes do setup do CMS gera refatoração de schema com conteúdo já cadastrado. Alterar campos no CMS depois que há 50 posts publicados é doloroso.
- **URLs decididas no improviso** — Estrutura de URLs mudando durante o build resulta em URLs inconsistentes e SEO fragmentado. Definir uma vez, aprovar, e não mudar mais.

### Etapa 05 — Architecture

- **"Vamos usar Next.js porque é o mais popular"** — Escolha de stack por hype, não por adequação. Se o projeto é uma landing page de 3 páginas sem CMS, Next.js é overkill. Astro ou Hugo resolvem em um décimo do tempo de setup.
- **"Hospedamos no servidor da empresa"** — Site estático em servidor corporativo (Apache, IIS) perde todas as vantagens de CDN edge, deploy automático, preview por PR e SSL automático. O custo de CDN moderno (Netlify/Cloudflare gratuitos) é menor que a hora de devops configurando servidor.
- **"Google Fonts é gratuito, sem problema"** — Gratuito em licença, mas envia IP do visitante para o Google. Em projetos com requisitos LGPD/GDPR, isso pode ser uma violação. Self-hosted resolve sem custo adicional.

### Etapa 06 — Setup

- **Variáveis de ambiente hardcoded** — API keys do CMS, tokens de analytics ou secrets no código commitado. Violação de segurança básica que se torna difícil de reverter depois (precisa reescrever o histórico do git ou rotacionar todos os secrets).
- **CMS configurado sem ambientes separados** — Produção e staging usando o mesmo workspace do CMS. Conteúdo em rascunho aparece no site público, ou edição de teste sobrescreve conteúdo real.
- **"Deploy é manual, a gente sobe por FTP"** — Em 2026, deploy manual via FTP para site estático é anti-pattern grave. Qualquer plataforma moderna (Vercel, Netlify, Cloudflare Pages) oferece deploy automático por push, gratuito, em minutos de setup.

### Etapa 07 — Build

- **Templates testados apenas com lorem ipsum** — Layout perfeito com "Lorem ipsum dolor sit amet" quebra quando o título real tem 80 caracteres e a descrição tem 3 parágrafos. Conteúdo real (ou realista) deve ser usado desde o primeiro template.
- **Acessibilidade deixada para o final** — "Depois a gente passa o axe-core" resulta em centenas de violações acumuladas, muitas envolvendo mudança de markup estrutural. Implementar ao longo do build — cada componente deve sair acessível de fábrica.
- **Todos os scripts carregados no head** — GA4, Meta Pixel, Hotjar, Intercom, chat, todos síncronos no head. Lighthouse Performance despenca de 95 para 40. Cada script de terceiro precisa de estratégia de carregamento definida na Etapa 05.

### Etapa 08 — QA

- **"Lighthouse tá 95 na home, está ótimo"** — A home pode ter score 95 enquanto a página de blog (com 20 imagens) tem 45. Cada template precisa de auditoria individual — scores variam drasticamente entre templates.
- **QA apenas no desktop** — Tester abre no Chrome desktop, clica em tudo, declara "funciona". 60%+ dos visitantes estão no mobile. QA sem testar mobile em breakpoints reais é incompleto.
- **Formulários testados apenas com dados válidos** — Submit com dados perfeitos funciona. Mas o que acontece com campo vazio, e-mail inválido, texto com 5000 caracteres, ou caracteres especiais? Testes com dados inválidos são obrigatórios.

### Etapa 09 — Launch Prep

- **"A gente muda o DNS no dia e pronto"** — Sem reduzir TTL com antecedência, a propagação pode levar 24-48h. Usuários acessam o site antigo enquanto outros já veem o novo. Reduzir TTL para 300s com 24h de antecedência é obrigatório.
- **Treinamento de CMS para o admin, não para o editor** — O admin recebe o treinamento e depois "repassa para o time". O repasse nunca acontece, ou acontece incompleto. Treinar diretamente quem vai publicar no dia a dia.
- **Sem plano de rollback** — "Se der problema a gente resolve na hora." Na hora, com pressão, sem plano, as decisões são piores. Plano documentado com critérios de acionamento e sequência de ações é obrigatório.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde** — Se algo der errado, o time não está disponível no fim de semana. Go-live deve ser em dia útil, horário comercial, com pelo menos 4h de buffer antes do fim do expediente.
- **Hospedagem antiga desligada no mesmo dia** — DNS ainda pode estar cacheado no valor antigo para alguns usuários. Manter a hospedagem antiga ativa por pelo menos 48h é seguro e barato.
- **"O site está no ar, projeto encerrado"** — Sem monitoramento na primeira semana, erros de crawl, 404s de redirects mal configurados e pixels de tracking quebrados passam despercebidos. A primeira semana pós-go-live é parte do projeto.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é site estático** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Os usuários vão se cadastrar e fazer login" | Web app, não site estático | Reclassificar para web-app ou saas |
| "Precisa de carrinho de compras e pagamento" | E-commerce | Reclassificar para e-commerce |
| "Mostra dados em tempo real do sistema X" | Dashboard / app com backend | Reclassificar para web-app |
| "Cada cliente vê conteúdo diferente" | Personalização server-side | Reclassificar para web-app |
| "Precisa de busca avançada com filtros" | Pode exigir backend ou search service | Avaliar se Algolia/Pagefind resolve ou se precisa de reclassificação |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos quem vai atualizar o conteúdo" | 01 | Conteúdo nunca será atualizado pós-launch | Definir content owner antes de avançar |
| "O brand guide ainda está sendo feito" | 01 | Retrabalho certo em design e código | Travar início do build até brand guide aprovado |
| "O orçamento é só para o desenvolvimento" | 01 | Surpresa com custos de hospedagem/CMS pós-launch | Apresentar TCO (dev + operação) antes de continuar |
| "Não temos textos nem fotos prontos" | 02 | Build bloqueado por falta de conteúdo | Incluir produção de conteúdo no cronograma ou travar início |
| "O site antigo tem 500 páginas" | 02 | Migração de conteúdo é projeto dentro do projeto | Estimar migração separadamente e incluir no escopo |
| "Não temos acesso ao DNS" | 01 | Go-live bloqueado no último dia | Resolver acesso ao DNS antes da Etapa 06 |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "As aprovações passam por 3 áreas" | 03 | Cadeia de aprovação lenta — atrasa conteúdo e design | Documentar SLA de aprovação com prazo máximo |
| "O designer vai entregando aos poucos" | 03 | Build sem design completo gera retrabalho | Exigir ao menos 2 templates finalizados antes do build |
| "A gente nunca usou CMS" | 02 | Time de conteúdo vai resistir ou abandonar o CMS | Planejar treinamento reforçado + escolher CMS mais simples |
| "Performance não é tão importante" | 02 | Se houver ads, Quality Score vai impactar custo por clique | Documentar que performance afeta resultado de mídia paga |
| "Pode ser qualquer framework" | 05 | Decisão técnica sem critério leva a over-engineering | Aplicar critérios da seção Stack de Referência |
| "A gente resolve a manutenção depois do lançamento" | 03 | Site sem dono operacional pós-launch | Formalizar modelo de suporte antes do go-live |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Gatilho da demanda identificado (pergunta 1)
- Content owner definido (pergunta 3)
- Orçamento de desenvolvimento e operação aprovado (pergunta 4)
- Prazo de go-live com justificativa de negócio (pergunta 8)
- Domínio identificado e acesso ao DNS confirmado (pergunta 14)

### Etapa 02 → 03

- Inventário de páginas e templates do MVP quantificado (pergunta 1)
- Frequência de atualização e necessidade de CMS decidida (perguntas 2 e 3)
- Fronteira do estático validada — sem requisitos que reclassifiquem o projeto (pergunta 12)
- Requisitos de LGPD/GDPR identificados (pergunta 13)

### Etapa 03 → 04

- Governança editorial acordada (pergunta 1)
- CMS escolhido e orçamento aprovado, ou decisão de conteúdo em repositório (perguntas 3 e 4)
- Design em formato utilizável com breakpoints definidos (perguntas 5 e 6)
- Modelo de manutenção pós-lançamento formalizado (pergunta 10)

### Etapa 04 → 05

- Sitemap completo aprovado por escrito (pergunta 1)
- Modelo de conteúdo definido campo a campo (pergunta 2)
- Estrutura de URLs definida e aprovada (pergunta 3)
- Mapa de redirecionamentos completo (pergunta 4, se aplicável)
- Documentação de definição revisada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- SSG, CMS e hospedagem escolhidos e justificados (perguntas 1, 2 e 3)
- Pipeline de CI/CD desenhado (pergunta 6)
- Custos mensais de operação calculados e aprovados (pergunta 11)
- Modelo de branches e ambientes documentado (pergunta 15)

### Etapa 06 → 07

- Repositório configurado com estrutura de pastas, .gitignore e variáveis de ambiente (perguntas 1, 2 e 3)
- Deploy preview por PR funcionando (pergunta 4)
- CMS configurado com modelos de conteúdo e ambientes separados (perguntas 5, 6 e 7)
- Pipeline de CI/CD testado com PR real (pergunta 15)

### Etapa 07 → 08

- Todos os templates implementados e validados contra o design (perguntas 1 e 2)
- Conteúdo real inserido nos templates (pergunta 3)
- Migração de conteúdo concluída ou dentro do prazo (pergunta 14)
- Acessibilidade implementada ao longo do build (pergunta 7)

### Etapa 08 → 09

- Lighthouse ≥90 em todos os eixos para cada template (pergunta 1)
- Todos os formulários testados com dados válidos e inválidos (pergunta 4)
- Fluxo de publicação no CMS validado por perfil de editor (pergunta 5)
- Open Graph validado nas ferramentas de debug (pergunta 6)
- Screen reader testado nas páginas principais (pergunta 15)

### Etapa 09 → 10

- Redirects configurados e testados individualmente (pergunta 1)
- TTL do DNS reduzido com 24h de antecedência (pergunta 2)
- Search Console verificado e sitemap pronto para submissão (pergunta 4)
- Treinamento de CMS realizado e documentação entregue (pergunta 9)
- Plano de rollback documentado com critérios e responsável (pergunta 11)

### Etapa 10 → Encerramento

- DNS propagado e SSL ativo (perguntas 1 e 2)
- Site validado em dispositivos e redes diferentes (pergunta 4)
- Sitemap submetido no Search Console (pergunta 6)
- Lighthouse em produção documentado como baseline (pergunta 7)
- Acessos entregues e aceite formal obtido (perguntas 12 e 13)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de site estático. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Landing | V2 Institucional | V3 Blog/Docs | V4 Portfólio | V5 Docs Técnica |
|---|---|---|---|---|---|
| 01 Inception | 1 | 2 | 2 | 2 | 2 |
| 02 Discovery | 1 | 3 | 3 | 2 | 3 |
| 03 Alignment | 1 | 3 | 3 | 2 | 2 |
| 04 Definition | 1 | 3 | 4 | 2 | 4 |
| 05 Architecture | 1 | 3 | 3 | 3 | 3 |
| 06 Setup | 1 | 2 | 3 | 2 | 3 |
| 07 Build | 3 | 4 | 3 | 5 | 2 |
| 08 QA | 2 | 3 | 3 | 4 | 2 |
| 09 Launch Prep | 1 | 3 | 3 | 2 | 2 |
| 10 Go-Live | 1 | 2 | 2 | 2 | 1 |
| **Total relativo** | **13** | **28** | **29** | **26** | **24** |

**Observacoes por variante:**

- **V1 Landing Page**: Esforço concentrado no Build (design pixel-perfect, conversão otimizada). Discovery e Definition são mínimos porque o escopo é pequeno e fixo.
- **V2 Institucional**: Esforço distribuído uniformemente. O gargalo oculto é a produção de conteúdo — o build fica parado esperando textos e fotos aprovados.
- **V3 Blog/Docs**: Pico na Definition (modelo de conteúdo complexo com tags, categorias, autores, SEO por post) e no Setup (CMS com múltiplos modelos). Migração de conteúdo pode dominar o esforço total se houver centenas de posts legados.
- **V4 Portfólio Visual**: Build é o mais pesado de todas as variantes — cada página tem alto nível de customização visual, pipeline de imagens complexo, e otimização de performance com assets pesados.
- **V5 Docs Técnica**: Definition é pesada (estrutura hierárquica profunda, versionamento, busca). Build é relativamente leve porque o conteúdo é Markdown com styling padronizado.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sem CMS — conteúdo em repositório (Etapa 03, pergunta 3) | Etapa 04: perguntas 2, 8, 12 (modelo de conteúdo CMS, fallback de campos, validação de campos). Etapa 06: perguntas 5, 6, 7, 9, 13 (setup CMS, papéis, ambientes, webhook, convite de usuários). Etapa 07: pergunta 14 (migração de conteúdo no CMS). Etapa 08: pergunta 5 (fluxo de publicação CMS). Etapa 09: pergunta 9 (treinamento CMS). |
| Sem site anterior a substituir (Etapa 01, pergunta 5) | Etapa 04: pergunta 4 (mapa de redirecionamentos). Etapa 09: perguntas 1 e 10 (configuração de redirects, hospedagem antiga). Etapa 10: perguntas 11 e 15 (hospedagem antiga ativa, redirects em produção). |
| Idioma único, sem i18n (Etapa 01, pergunta 7) | Etapa 04: hreflang no esquema de metadados. Etapa 07: pergunta 10 (implementação de i18n). |
| Sem formulários no site (Etapa 02, pergunta 4) | Etapa 05: pergunta 5 (solução para formulários). Etapa 08: pergunta 4 (teste de formulários). Etapa 10: pergunta 5 (teste de formulários em produção). |
| Landing page sem blog/listagem (variante V1) | Etapa 04: perguntas 9 e 11 (tags/categorias, volume de migração). Etapa 07: perguntas 10, 11, 14 (i18n, SEO por página, migração). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| CMS headless escolhido (Etapa 03, pergunta 3) | Etapa 05: pergunta 2 (qual CMS) se torna bloqueadora. Etapa 06: perguntas 5-7, 9 (setup completo do CMS). Etapa 08: pergunta 5 (testar fluxo de publicação com perfil editor). Etapa 09: pergunta 9 (treinamento obrigatório antes do go-live). |
| Site substitui site existente (Etapa 01, pergunta 5) | Etapa 02: pergunta 5 (quantas URLs indexadas) se torna bloqueadora. Etapa 04: pergunta 4 (mapa de redirects) se torna gate. Etapa 09: perguntas 1 e 10 (redirects e hospedagem antiga). |
| Requisitos LGPD/GDPR identificados (Etapa 02, pergunta 13) | Etapa 05: pergunta 7 (fontes self-hosted obrigatórias). Etapa 07: pergunta 6 (scripts de terceiros com estratégia de consent). Etapa 09: cookie banner, política de privacidade como artefatos obrigatórios. |
| Campanhas de ads ativas no lançamento (Etapa 01, pergunta 15) | Etapa 08: pergunta 1 (Lighthouse Performance ≥90 se torna hard requirement, não nice-to-have). Etapa 09: perguntas 7 e 8 (eventos de conversão devem estar validados antes do go-live, não depois). Etapa 10: pergunta 9 (verificar conversões com dados reais no dia 1). |
| Múltiplos idiomas confirmados (Etapa 01, pergunta 7) | Etapa 04: modelo de conteúdo deve prever campos por locale. Etapa 05: SSG com suporte nativo a i18n. Etapa 06: CMS com ambientes por locale ou campos traduzidos. Etapa 07: pergunta 10 (i18n) se torna gate. |
| Volume de conteúdo >100 páginas (Etapa 02, pergunta 1) | Etapa 05: tempo de build se torna critério de escolha do SSG (Hugo >> Next.js >> Gatsby). Etapa 07: pergunta 14 (migração de conteúdo) se torna o maior risco do projeto. Etapa 08: pergunta 3 (link checker) se torna obrigatório com automação. |
