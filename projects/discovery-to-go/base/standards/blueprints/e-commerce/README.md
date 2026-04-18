---
title: "E-commerce — Blueprint"
description: "Loja virtual com catálogo de produtos, carrinho, checkout, processamento de pagamentos, gestão de pedidos e estoque. Pode ser B2C, B2B ou D2C."
category: project-blueprint
type: e-commerce
status: rascunho
created: 2026-04-13
---

# E-commerce

## Descrição

Loja virtual com catálogo de produtos, carrinho, checkout, processamento de pagamentos, gestão de pedidos e estoque. Pode ser B2C, B2B ou D2C.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo e-commerce é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Loja D2C (Direct to Consumer)

Marca própria vendendo diretamente ao consumidor final, sem intermediários. Catálogo tipicamente pequeno a médio (10 a 500 SKUs), com foco em branding, storytelling de produto e experiência de compra premium. O checkout precisa ser simples e rápido — cada clique a mais é perda de conversão. Frequentemente integrado com redes sociais (Instagram Shopping, TikTok Shop) e influenciadores. A margem é alta (sem intermediário), então o investimento em experiência de compra se paga rapidamente. Exemplos: marca de cosméticos, grife de moda, suplementos, café especial, vinícola.

### V2 — Marketplace

Plataforma que conecta múltiplos vendedores a compradores, sem necessariamente ter estoque próprio. A complexidade está na gestão de múltiplos sellers (cadastro, aprovação, comissionamento), split de pagamento entre plataforma e vendedor, gestão de frete por seller (cada vendedor com CEP de origem e tabela de frete diferentes), e resolução de disputas. O catálogo pode crescer rapidamente (milhares a milhões de SKUs) e a qualidade é desigual entre sellers. Exemplos: marketplace de artesanato, marketplace de produtos regionais, shopping virtual multi-loja.

### V3 — B2B (Business to Business)

Loja onde o comprador é outra empresa — com regras de preço por cliente/contrato, quantidade mínima por pedido, prazo de pagamento (boleto 30/60/90 dias), catálogo restrito por perfil de comprador, e frequentemente integração com ERP do comprador via EDI ou API. O checkout é mais complexo que B2C: aprovação de pedido por múltiplos níveis hierárquicos, endereço de faturamento diferente de entrega, e CNPJ obrigatório. O volume de transações é menor, mas o ticket médio é significativamente maior. Exemplos: distribuidora de insumos, atacadista de alimentos, fornecedor de material de escritório para empresas.

### V4 — Loja de Assinatura (Subscription Commerce)

Modelo recorrente onde o cliente assina um plano e recebe produtos periodicamente (mensal, bimestral) — com ou sem curadoria. A complexidade está na gestão de ciclos de cobrança recorrente, dunning (recuperação de pagamentos falhos), gestão de planos (upgrade, downgrade, pausa, cancelamento), e logística de envio periódico. O LTV (Lifetime Value) é a métrica central — não o ticket individual. Frequentemente exige dashboard de métricas de retenção (churn, MRR, cohort analysis). Exemplos: clube de vinhos, box de snacks, assinatura de café, kit de produtos de beleza.

### V5 — E-commerce Omnichannel

Operação que integra loja virtual com lojas físicas — estoque unificado, compra online com retirada na loja (BOPIS), compra na loja com entrega em casa (ship-from-store), e visão unificada do cliente em todos os canais. A complexidade está na sincronização de estoque em tempo real entre múltiplos pontos (warehouse central, lojas físicas, fornecedores com drop-shipping), na gestão de preços e promoções que podem variar por canal, e na experiência consistente do cliente independente de onde ele compra. Exemplos: rede de varejo com e-commerce, franquia com loja virtual, marca com flagship stores e canal online.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Plataforma | Pagamentos | Frete | Busca | Observações |
|---|---|---|---|---|---|
| V1 — D2C | Shopify, VTEX IO ou headless (Medusa, Saleor) | Stripe, Mercado Pago ou PagSeguro | Melhor Envio, Correios API ou Kangu | Algolia ou busca nativa | Shopify para time não-técnico. Headless para customização total e controle de marca. |
| V2 — Marketplace | VTEX, Mirakl ou custom (Medusa + multi-vendor) | Split payment (Stripe Connect, Zoop, Pagar.me) | Por seller — Melhor Envio ou integração direta | Algolia ou Elasticsearch | Split de pagamento é obrigatório. VTEX tem marketplace nativo. Custom exige esforço significativo. |
| V3 — B2B | VTEX B2B, Shopify Plus ou custom (Saleor, Medusa) | Boleto (Pagar.me, Asaas), PIX, crédito com prazo | Transportadora própria ou Intelipost | Elasticsearch | Tabela de preço por cliente e aprovação hierárquica são diferenciais. ERP integration obrigatória. |
| V4 — Assinatura | Shopify + ReCharge, VTEX Subscriptions ou custom | Cobrança recorrente (Stripe Billing, Vindi, Asaas) | Logística recorrente — contrato com transportadora | Não se aplica (catálogo pequeno) | Dunning e gestão de churn são críticos. Gateway com retry automático obrigatório. |
| V5 — Omnichannel | VTEX, Shopify Plus + POS, ou Commercetools | Gateway unificado cross-channel | OMS (Order Management System) com routing inteligente | Algolia ou Elasticsearch | OMS é o coração — sem ele, estoque unificado é impossível. VTEX tem OMS nativo. |

---

## Etapa 01 — Inception

- **Origem da demanda**: A necessidade de e-commerce costuma surgir de cenários específicos — expansão para canal digital de uma operação física, insatisfação com plataforma atual (lenta, cara, limitada), lançamento de marca D2C, ou digitalização forçada por mudanças de mercado. O gatilho real define prioridades: se o problema é a plataforma atual, migração de dados e SEO são críticos; se é expansão para digital, a prioridade é time-to-market; se é D2C, a experiência de marca é o diferencial. Entender o gatilho antes de discutir stack evita soluções desalinhadas.

- **Modelo de negócio e monetização**: Verificar como o e-commerce gera receita — venda direta de produtos (margem sobre custo), marketplace com comissão sobre vendas de terceiros, assinatura recorrente, ou modelo híbrido. Cada modelo tem implicações diretas na arquitetura: venda direta precisa de gestão de estoque e custo, marketplace precisa de split de pagamento e multi-seller, assinatura precisa de cobrança recorrente e gestão de ciclo de vida. Misturar modelos no MVP sem planejamento gera complexidade que inviabiliza o prazo.

- **Stakeholders e cadeia operacional**: O e-commerce envolve mais áreas do que o cliente costuma antecipar — marketing (campanhas, SEO, mídia paga), operações/logística (estoque, picking, packing, envio), financeiro (conciliação de pagamentos, chargebacks, fiscal), SAC (trocas, devoluções, reclamações), e TI (integrações, manutenção). Se qualquer uma dessas áreas não participa desde a Inception, o projeto será surpreendido por requisitos não mapeados que aparecem durante o Build ou, pior, após o go-live.

- **Volume e projeção de operação**: Dimensionar o volume esperado de pedidos por dia/mês, ticket médio, número de SKUs ativos, e picos sazonais (Black Friday, Natal, Dia das Mães). Esses números definem a plataforma adequada: 50 pedidos/dia é radicalmente diferente de 5.000 pedidos/dia em termos de infraestrutura, gateway de pagamento, logística e SAC. Picos sazonais de 10-50x o volume normal exigem planejamento de auto-scaling e testes de carga específicos. Uma plataforma dimensionada para 50 pedidos/dia que recebe 5.000 na Black Friday cai.

- **Presença em marketplaces externos**: Verificar se o cliente já vende ou planeja vender em marketplaces externos (Mercado Livre, Amazon, Shopee, Magazine Luiza) além da loja própria. A integração com marketplaces externos exige hubs de integração (Bling, Tiny, Anymarket) que sincronizam estoque, preço e pedidos entre a loja própria e os canais externos. Se isso tem qualquer chance de acontecer, a arquitetura de estoque e pedidos precisa prever desde o início — adicionar marketplaces depois é refatoração pesada.

- **Obrigações fiscais e tributárias**: E-commerce no Brasil tem complexidade tributária relevante — ICMS interestadual (DIFAL), substituição tributária, regime fiscal do produto (NCM), emissão de nota fiscal eletrônica (NF-e) obrigatória para cada venda, e integração com SEFAZ. Se o cliente não tem contador ou sistema fiscal integrado, o e-commerce não pode operar legalmente. Identificar se a emissão de NF-e será feita pelo ERP existente, por integração direta (Bling, Omie, Tiny), ou por módulo da plataforma de e-commerce é pré-requisito nesta fase.

### Perguntas

1. Qual é o gatilho real desta demanda — expansão digital, migração de plataforma, lançamento de marca D2C, ou digitalização do negócio? [fonte: Diretoria, Comercial] [impacto: PM, Arquiteto]
2. Qual é o modelo de monetização — venda direta, marketplace com comissão, assinatura recorrente, ou modelo híbrido? [fonte: Diretoria, Financeiro] [impacto: Arquiteto, Dev]
3. Quais áreas da empresa estão envolvidas e representadas no projeto (marketing, logística, financeiro, SAC, TI)? [fonte: Diretoria] [impacto: PM]
4. Qual é o volume estimado de pedidos por dia/mês, ticket médio e número de SKUs ativos no MVP? [fonte: Comercial, Operações] [impacto: Arquiteto, DevOps]
5. Quais são os picos sazonais esperados e qual o fator de multiplicação de volume nesses períodos? [fonte: Comercial, Marketing] [impacto: Arquiteto, DevOps]
6. O e-commerce substituirá uma plataforma existente ou será criado do zero? [fonte: TI, Diretoria] [impacto: Dev, PM, SEO]
7. O cliente já vende ou planeja vender em marketplaces externos (Mercado Livre, Amazon, Shopee)? [fonte: Comercial, Diretoria] [impacto: Arquiteto, Dev]
8. Qual é o orçamento total disponível, separando custo de desenvolvimento, plataforma mensal e operação? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
9. Qual é o prazo esperado para o go-live e existe data de negócio que justifica (Black Friday, lançamento, campanha)? [fonte: Diretoria, Marketing] [impacto: PM, Dev]
10. A emissão de NF-e está resolvida — ERP existente, hub de integração ou módulo da plataforma? [fonte: Financeiro, Contabilidade, TI] [impacto: Dev, Arquiteto]
11. Quem toma decisões de produto, design e pricing — existe um aprovador único ou múltiplas áreas? [fonte: Diretoria] [impacto: PM]
12. Existe catálogo de produtos estruturado com fotos, descrições, preços, SKUs e estoque? [fonte: Comercial, Marketing] [impacto: Dev, Conteúdo, PM]
13. O cliente tem preferência ou restrição por alguma plataforma de e-commerce específica? [fonte: TI, Diretoria] [impacto: Arquiteto, Dev]
14. Qual é o nível de maturidade digital do time que vai operar o e-commerce (marketing, SAC, logística)? [fonte: RH, Diretoria] [impacto: PM, Dev]
15. Existe operação logística própria ou o fulfillment será terceirizado (3PL)? [fonte: Operações, Diretoria] [impacto: Arquiteto, DevOps]

---

## Etapa 02 — Discovery

- **Catálogo de produtos**: Levantar a estrutura completa do catálogo — número de categorias e subcategorias, número de SKUs, atributos por tipo de produto (tamanho, cor, material, voltagem), variações de produto (um produto com 5 cores e 3 tamanhos = 15 SKUs), e tipo de mídia por produto (fotos, vídeos, documentos técnicos). A complexidade do catálogo impacta diretamente a modelagem de dados, a busca e filtros, e o esforço de cadastro. Um catálogo de 50 SKUs simples é radicalmente diferente de um catálogo de 50.000 SKUs com 20 atributos filtráveis cada.

- **Jornada de compra e checkout**: Mapear a jornada completa do comprador — desde a descoberta do produto (busca, navegação por categoria, recomendação) até o pós-venda (rastreamento, troca, devolução). O checkout é o ponto mais sensível: cada campo desnecessário, cada etapa adicional e cada redirect para gateway externo aumenta a taxa de abandono. Identificar se o checkout deve ser one-page (todos os passos na mesma tela), multi-step (etapas separadas com progresso visível), ou transparente (cartão processado sem sair do site). Para B2B, mapear também o fluxo de aprovação de pedido por múltiplos níveis.

- **Meios de pagamento**: Mapear quais meios de pagamento o cliente precisa oferecer — cartão de crédito (parcelamento em até quantas vezes, com ou sem juros), cartão de débito, PIX (com ou sem desconto), boleto bancário (com vencimento e juros de atraso), carteiras digitais (Apple Pay, Google Pay, PayPal), e condições especiais para B2B (faturamento contra CNPJ, prazo 30/60/90 dias). Cada meio de pagamento exige integração específica com o gateway, configuração de antifraude, e regras de conciliação financeira.

- **Logística e frete**: Mapear a operação logística completa — warehouse centralizado ou distribuído, processo de picking/packing, transportadoras contratadas, modalidades de envio (econômico, expresso, agendado, retirada na loja), cálculo de frete (por peso/dimensões, por faixa de CEP, frete grátis acima de valor mínimo), rastreamento de envio, e prazos de entrega por região. O frete é frequentemente o fator #1 de abandono de carrinho no Brasil — se o cálculo de frete é lento ou o valor é inesperadamente alto, a venda é perdida.

- **Integrações obrigatórias**: Mapear todos os sistemas que precisam se comunicar com o e-commerce no MVP — ERP (pedidos, estoque, NF-e), CRM (dados de cliente, histórico de compras), plataforma de e-mail marketing (automação de carrinho abandonado, pós-venda), analytics (GA4, Meta Pixel, conversões), hub de marketplaces (se vende em canais externos), e ferramentas de atendimento (Zendesk, Freshdesk, WhatsApp Business). Cada integração é um projeto dentro do projeto — subestimar integrações é o erro mais comum em projetos de e-commerce.

- **Política comercial**: Documentar as regras comerciais que o e-commerce precisa suportar — política de preços (preço único, preço por região, preço por quantidade, preço por contrato B2B), política de promoções (cupons de desconto, frete grátis condicional, compre X leve Y, desconto progressivo), política de trocas e devoluções (prazo, condições, quem paga o frete de retorno), e política de cancelamento (prazo, reembolso automático ou manual). Regras comerciais não mapeadas no Discovery aparecem como bugs no Build — "o sistema não faz desconto progressivo" não é bug, é requisito não levantado.

### Perguntas

1. Quantos SKUs o catálogo terá no MVP e qual a estrutura de categorias e atributos filtráveis? [fonte: Comercial, Marketing] [impacto: Dev, Arquiteto]
2. A jornada de compra foi mapeada da descoberta ao pós-venda, incluindo todos os touchpoints? [fonte: Marketing, UX, Comercial] [impacto: Designer, Dev]
3. Quais meios de pagamento são obrigatórios no MVP (cartão, PIX, boleto, carteiras digitais, faturamento B2B)? [fonte: Financeiro, Comercial] [impacto: Dev, Arquiteto]
4. Qual é a operação logística — warehouse próprio, 3PL, drop-shipping, retirada na loja? [fonte: Operações, Logística] [impacto: Arquiteto, Dev]
5. Quais transportadoras e modalidades de frete precisam ser suportadas no MVP? [fonte: Operações, Logística] [impacto: Dev]
6. Quais integrações com sistemas existentes são obrigatórias no MVP (ERP, CRM, e-mail marketing, marketplaces)? [fonte: TI, Comercial, Marketing] [impacto: Dev, Arquiteto]
7. A política de preços inclui variações por região, quantidade, contrato ou canal? [fonte: Comercial, Financeiro] [impacto: Dev, Arquiteto]
8. As regras de promoção foram documentadas (cupons, frete grátis, compre X leve Y, desconto progressivo)? [fonte: Marketing, Comercial] [impacto: Dev]
9. A política de trocas e devoluções foi formalizada (prazo, condições, frete de retorno, reembolso)? [fonte: Jurídico, SAC, Comercial] [impacto: Dev, SAC]
10. Há requisitos de LGPD — consentimento de cookies, política de privacidade, opt-out de marketing? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, DevOps]
11. O cliente tem expectativas de performance (tempo de carregamento, Lighthouse score, Core Web Vitals)? [fonte: Marketing, TI] [impacto: Dev]
12. Quais métricas de negócio o cliente quer monitorar (conversão, ticket médio, abandono de carrinho, CAC, LTV)? [fonte: Marketing, Diretoria] [impacto: Dev, Marketing]
13. Existe site anterior do qual será necessário migrar dados (produtos, clientes, pedidos, SEO/URLs)? [fonte: TI, Comercial] [impacto: Dev, SEO, PM]
14. Há requisitos de acessibilidade (WCAG 2.1 AA, legislação específica) para o e-commerce? [fonte: Jurídico, Compliance] [impacto: Dev, Designer]
15. O e-commerce precisará suportar múltiplos idiomas, moedas ou versões regionais? [fonte: Comercial, Diretoria] [impacto: Dev, Arquiteto]

---

## Etapa 03 — Alignment

- **Plataforma: SaaS vs. headless vs. custom**: Alinhar a decisão arquitetural mais importante do projeto. SaaS (Shopify, VTEX) oferece time-to-market rápido, manutenção incluída e ecossistema de apps/extensões — mas limita customização e tem custo recorrente significativo (% sobre vendas ou mensalidade alta). Headless (Medusa, Saleor, Commerce.js + frontend custom) oferece liberdade total de frontend e experiência de marca — mas exige time técnico forte e tempo de desenvolvimento maior. A escolha impacta custo, prazo, flexibilidade e dependência de fornecedor. Decidir sem envolver todos os stakeholders (negócio, TI, financeiro) resulta em arrependimento tardio.

- **Gateway de pagamento e antifraude**: Alinhar a escolha do gateway considerando: meios de pagamento suportados (cartão, PIX, boleto), taxas por transação, prazo de repasse (D+2, D+14, D+30), suporte a split de pagamento (obrigatório para marketplace), integração com antifraude (nativo ou externo), e checkout transparente vs. redirect. No Brasil, Stripe (entrando com força), Mercado Pago (maior base de compradores), Pagar.me e Zoop são as opções mais comuns. A taxa do gateway impacta diretamente a margem — 1% a mais no gateway em um e-commerce de R$1M/mês são R$10K/mês a menos de lucro.

- **Operação logística e SLA de envio**: Alinhar com a operação como o fluxo físico vai funcionar — quem recebe o pedido, em que formato, como é feito o picking (separação dos produtos), packing (embalagem), etiquetagem (integração com transportadora para gerar etiqueta), despacho, e rastreamento. Definir os SLAs de expedição (pedido aprovado até 12h = despacho no mesmo dia), as regiões atendidas, e os custos de frete projetados. Se a operação logística não está pronta quando o e-commerce vai ao ar, os pedidos ficam parados — e-commerce sem logística é site de catálogo.

- **Modelo de atendimento ao cliente (SAC)**: Definir como reclamações, dúvidas, trocas e devoluções serão tratadas — canal (e-mail, chat, WhatsApp, telefone), horário de atendimento, SLA de primeira resposta, e ferramentas (Zendesk, Freshdesk, Intercom). O CDC (Código de Defesa do Consumidor) exige resposta em prazo razoável e direito de arrependimento em 7 dias para compras online. Se não há equipe de SAC definida antes do go-live, as reclamações vão para Procon e Reclame Aqui — com impacto direto na reputação e nas vendas.

- **Gestão de conteúdo de produto**: Alinhar quem é responsável por cadastrar e manter o conteúdo de produtos — fotos (quantas por produto, qualidade mínima, fundo branco obrigatório?), descrições (texto comercial + especificações técnicas), vídeos, e atributos filtráveis. Em e-commerce, a qualidade do conteúdo de produto é diretamente proporcional à conversão — produtos com foto ruim e descrição genérica vendem significativamente menos. Definir o padrão de qualidade e o responsável antes do build evita catálogo inconsistente.

### Perguntas

1. A decisão entre SaaS, headless e custom foi tomada com justificativa documentada envolvendo negócio, TI e financeiro? [fonte: TI, Diretoria, Financeiro] [impacto: Arquiteto, Dev, PM]
2. O gateway de pagamento foi escolhido considerando taxas, meios suportados, prazo de repasse e antifraude? [fonte: Financeiro, TI] [impacto: Dev, Financeiro]
3. A operação logística está definida com fluxo de picking/packing/despacho e SLAs de expedição? [fonte: Operações, Logística] [impacto: Dev, Operações]
4. O modelo de SAC foi definido com canal, horário, SLA e ferramenta antes do go-live? [fonte: SAC, Diretoria] [impacto: PM, Dev]
5. O responsável pelo conteúdo de produto (fotos, descrições, atributos) foi definido com padrão de qualidade? [fonte: Marketing, Comercial] [impacto: Conteúdo, Dev, PM]
6. O fluxo de checkout foi alinhado (one-page, multi-step, transparente) e aprovado por UX e negócio? [fonte: UX, Comercial] [impacto: Dev, Designer]
7. O processo de emissão de NF-e e integração fiscal foi validado com o contador e o ERP? [fonte: Contabilidade, TI] [impacto: Dev, Financeiro]
8. As dependências externas críticas (acesso a APIs de gateway, transportadora, ERP) foram listadas com prazos? [fonte: TI, Fornecedores] [impacto: PM, Dev]
9. O modelo de custo recorrente (plataforma, gateway, apps, hosting) foi projetado e aprovado pelo financeiro? [fonte: Financeiro, TI] [impacto: PM, Arquiteto]
10. O SLA de disponibilidade do e-commerce foi definido (ex.: 99.9% uptime, especialmente em picos sazonais)? [fonte: TI, Diretoria] [impacto: DevOps, Arquiteto]
11. A estratégia de SEO de e-commerce foi alinhada (URLs de produto, categorias, canonical, dados estruturados Product)? [fonte: Marketing, Agência de SEO] [impacto: Dev, SEO]
12. O design inclui todos os estados do checkout (loading, erro de pagamento, sucesso, pendente, estoque esgotado)? [fonte: Designer, UX] [impacto: Dev]
13. O time de desenvolvimento tem acesso a sandbox de gateway, ERP e transportadoras para testes? [fonte: TI, Fornecedores] [impacto: Dev]
14. Existe processo definido para revisão e aprovação de entregas parciais durante o build? [fonte: Diretoria, Comercial] [impacto: PM, Dev]
15. O cliente foi informado sobre o impacto de mudanças de escopo (novos meios de pagamento, novos canais) no prazo? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Arquitetura de catálogo e taxonomia**: Definir a estrutura completa do catálogo — árvore de categorias (até 3 níveis recomendado para navegação), atributos por tipo de produto (roupas: tamanho, cor, material; eletrônicos: voltagem, potência, dimensões), variações de produto (produto pai com SKUs filhos por combinação de atributos), e regras de filtro na listagem (quais atributos são filtráveis, qual a ordem de apresentação). A taxonomia define diretamente a navegação, a busca e o SEO do catálogo — uma taxonomia mal estruturada resulta em produtos difíceis de encontrar e categorias confusas que aumentam a taxa de bounce.

- **Modelo de precificação e promoções**: Especificar todas as regras de preço que o sistema precisa suportar — preço de tabela, preço promocional com data de início/fim, preço por quantidade (a partir de 10 unidades, desconto de 5%), preço por grupo de cliente (atacado vs. varejo), e preço por região. Para promoções, definir: tipos de cupom (percentual, valor fixo, frete grátis), regras de aplicação (categoria específica, produto específico, valor mínimo de carrinho), combinação de promoções (cupom acumula com promoção de categoria?), e limites (máximo de usos por cupom, por cliente). Regras de preço não especificadas aparecem como "bugs" durante o build.

- **Fluxo de pedido e estados**: Documentar a máquina de estados do pedido — desde a criação (carrinho convertido em pedido) até o encerramento (entregue, devolvido ou cancelado). Estados típicos: aguardando pagamento → pagamento aprovado → em separação → faturado (NF-e emitida) → despachado → em trânsito → entregue. Cada transição de estado pode gerar ações automáticas: e-mail de confirmação, atualização de estoque, geração de NF-e, notificação de rastreamento. Para marketplace, adicionar estados de split de pagamento e repasse ao seller.

- **Modelo de estoque**: Definir como o estoque será gerenciado — estoque centralizado (um warehouse), estoque distribuído (múltiplos centros de distribuição), estoque compartilhado com loja física (omnichannel), ou drop-shipping (estoque no fornecedor). Para cada modelo, definir: reserva de estoque no momento do pedido ou do pagamento, tratamento de estoque zerado (produto some da loja, mostra "indisponível", ou permite pre-order), e regras de prioridade quando múltiplas localidades têm estoque (routing por proximidade ao CEP de entrega, por custo de frete, ou por disponibilidade).

- **Estrutura de URLs e SEO de catálogo**: Definir a estrutura de URLs de produto, categoria e listagem — /produto/nome-do-produto-SKU ou /categoria/subcategoria/produto? URLs devem ser descritivas, conter a keyword principal, e não mudar após publicação. Para e-commerce com catálogo grande, o SEO de categoria (páginas de listagem com descrição única, H1 otimizado, dados estruturados CollectionPage) frequentemente gera mais tráfego orgânico que páginas de produto individual. Definir canonical tags para variações de produto que geram URLs diferentes (/camiseta-azul vs. /camiseta-vermelha) para evitar conteúdo duplicado.

- **E-mails transacionais e automações**: Especificar cada e-mail que o sistema precisa enviar automaticamente — confirmação de pedido, pagamento aprovado, NF-e emitida, produto despachado (com código de rastreamento), produto entregue, e solicitação de avaliação. Adicionalmente, configurar automações de marketing integradas: carrinho abandonado (30 min, 24h, 72h), produto visualizado sem compra, recompra baseada em histórico. E-mails transacionais bem feitos aumentam a confiança do comprador e reduzem tickets de SAC — cada e-mail não enviado gera uma ligação perguntando "cadê meu pedido?".

### Perguntas

1. A taxonomia de categorias e a estrutura de atributos filtráveis foram definidas e aprovadas? [fonte: Comercial, Marketing] [impacto: Dev, SEO]
2. Todas as regras de precificação foram especificadas (preço por quantidade, região, grupo de cliente, promoções)? [fonte: Comercial, Financeiro] [impacto: Dev, Arquiteto]
3. A máquina de estados do pedido foi documentada com todas as transições e ações automáticas? [fonte: Operações, Comercial, TI] [impacto: Dev, Arquiteto]
4. O modelo de estoque foi definido (centralizado, distribuído, drop-shipping) com regras de reserva e routing? [fonte: Operações, Logística] [impacto: Dev, Arquiteto]
5. A estrutura de URLs de produto e categoria foi definida e é consistente com a estratégia de SEO? [fonte: Marketing, Agência de SEO] [impacto: Dev, SEO]
6. Os e-mails transacionais e automações de marketing foram especificados com triggers e conteúdo? [fonte: Marketing, Comercial] [impacto: Dev, Marketing]
7. As regras de cálculo de frete foram documentadas (peso/dimensão, faixa de CEP, frete grátis, prazo)? [fonte: Operações, Logística] [impacto: Dev]
8. O fluxo de troca e devolução foi especificado com estados, prazos e regras de reembolso? [fonte: SAC, Jurídico, Operações] [impacto: Dev, SAC]
9. Os dados estruturados Schema.org (Product, Offer, AggregateRating, BreadcrumbList) foram mapeados? [fonte: Agência de SEO, Marketing] [impacto: Dev, SEO]
10. As regras de validação de cadastro de produto foram definidas (campos obrigatórios, formatos de imagem, limites de caracteres)? [fonte: Comercial, Marketing] [impacto: Dev]
11. O modelo de avaliações e reviews de produto foi especificado (moderação, resposta do lojista, exibição)? [fonte: Marketing, SAC] [impacto: Dev]
12. O fluxo de cadastro e login do cliente foi definido (campos, verificação de e-mail, login social, guest checkout)? [fonte: UX, Marketing] [impacto: Dev, Designer]
13. O mapa de redirecionamentos do site anterior foi produzido cobrindo URLs de produto e categoria? [fonte: TI, Agência anterior, SEO] [impacto: Dev, SEO]
14. As regras de antifraude foram definidas (limites, blacklists, análise manual acima de valor X)? [fonte: Financeiro, TI] [impacto: Dev, Financeiro]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes do início do Setup? [fonte: Diretoria, Comercial] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Plataforma de e-commerce**: Se a decisão é SaaS (Shopify, VTEX), a arquitetura é majoritariamente definida pela plataforma — o foco é em customização via tema/storefront, apps/extensões, e integrações. Se a decisão é headless, definir: backend de commerce (Medusa, Saleor, Commerce.js, ou VTEX IO como BFF), frontend (Next.js, Remix, ou Hydrogen para Shopify), e como as camadas se comunicam (API REST, GraphQL). Se custom, definir a stack completa de backend, frontend e infraestrutura. A complexidade de arquitetura cresce exponencialmente de SaaS para headless para custom — e o time precisa ter capacidade para sustentá-la.

- **Gateway de pagamento e checkout**: Definir a arquitetura de pagamento: checkout transparente (formulário de cartão no próprio site, exige PCI DSS compliance do gateway) vs. redirect (redireciona para página do gateway — mais simples, menos controle), tokenização de cartão para compras futuras (exige contrato específico com gateway), retry automático para PIX e boleto vencidos, e webhook de confirmação de pagamento (como o e-commerce é notificado quando o pagamento é aprovado). Para marketplace, definir o fluxo de split — o gateway divide automaticamente entre plataforma e seller, ou o split é feito manualmente após recebimento.

- **Busca e filtros**: A busca é uma das funcionalidades mais críticas de um e-commerce — compradores que usam busca convertem 2-3x mais que navegação por categoria. Definir: busca full-text com tolerância a erros de digitação (fuzzy search), autocomplete com sugestões de produto e categoria, filtros por atributo (tamanho, cor, preço, marca) com contagem de resultados por filtro (faceted search), e ordenação (relevância, preço, mais vendidos, avaliações). Algolia é a solução mais rápida de implementar com melhor UX, mas tem custo baseado em operações de busca. Elasticsearch é a alternativa self-hosted com mais controle e sem custo de licença.

- **Infraestrutura e escalabilidade**: Definir como a infraestrutura escala para absorver picos de tráfego — auto-scaling de servidores (se custom/headless), CDN para assets estáticos e páginas de produto cacheadas, cache de busca e filtros para evitar queries ao banco a cada requisição, e queue para processamento assíncrono de tarefas pesadas (envio de e-mails, geração de NF-e, atualização de estoque em marketplaces). Para Black Friday, a infraestrutura precisa escalar 10-50x em minutos — se o auto-scaling não foi testado, a loja cai no momento de maior receita do ano.

- **Integrações e middleware**: Definir a camada de integração entre o e-commerce e os sistemas externos — ERP (pedidos, estoque, NF-e), transportadoras (cálculo de frete, geração de etiqueta, rastreamento), gateway de pagamento (processamento, conciliação, chargebacks), hub de marketplaces (sincronização de catálogo, estoque e pedidos), e-mail marketing (automações de ciclo de vida), e analytics (eventos de e-commerce enhanced). Se há mais de 3 integrações, considerar um middleware/iPaaS (n8n, Make, ou custom queue-based) para centralizar a orquestração e evitar integrações ponto-a-ponto que se tornam ingerenciáveis.

- **Segurança e compliance**: Definir os requisitos de segurança específicos de e-commerce — PCI DSS (o gateway é o responsável, mas o e-commerce não pode armazenar dados de cartão em texto), LGPD (consentimento para marketing, política de privacidade, direito ao esquecimento), SSL/TLS obrigatório em todo o site (não apenas no checkout), proteção contra ataques comuns (SQL injection, XSS, CSRF), rate limiting no checkout (prevenção de brute force em cupons), e WAF (Web Application Firewall) para proteção em produção.

### Perguntas

1. A arquitetura da plataforma (SaaS, headless ou custom) foi detalhada com diagramas de componentes e fluxos? [fonte: TI, Arquiteto] [impacto: Dev, DevOps]
2. A integração com o gateway de pagamento foi desenhada com checkout transparente ou redirect, webhook e retry? [fonte: TI, Financeiro] [impacto: Dev]
3. A solução de busca e filtros foi escolhida (Algolia, Elasticsearch, nativa) com custos projetados? [fonte: TI, Marketing] [impacto: Dev, Arquiteto]
4. A estratégia de escalabilidade para picos sazonais foi definida com auto-scaling, cache e CDN? [fonte: TI, DevOps] [impacto: DevOps, Arquiteto]
5. A camada de integrações foi desenhada (direta, via middleware/iPaaS, via queue) para ERP, transportadora e marketplaces? [fonte: TI] [impacto: Dev, Arquiteto]
6. Os requisitos de segurança (PCI, LGPD, SSL, WAF) foram definidos e a responsabilidade de cada camada documentada? [fonte: Segurança, Jurídico, TI] [impacto: Dev, DevOps, Segurança]
7. O modelo de ambientes (production, staging, sandbox) foi definido com dados e configurações isolados? [fonte: TI] [impacto: Dev, DevOps]
8. Os custos mensais de plataforma, gateway, apps, hosting e integrações foram projetados em três cenários? [fonte: Financeiro, TI] [impacto: PM, Arquiteto]
9. A estratégia de cache foi definida (TTL de páginas de produto, invalidação após atualização de preço/estoque)? [fonte: TI] [impacto: Dev, DevOps]
10. A arquitetura suporta a evolução futura (novos canais, marketplace, internacionalização, app mobile)? [fonte: Diretoria, Comercial] [impacto: Arquiteto]
11. A estratégia de monitoramento (APM, logs, alertas) foi definida para detectar problemas antes do cliente? [fonte: TI, DevOps] [impacto: DevOps, Dev]
12. O pipeline de CI/CD foi desenhado com preview por branch, testes automatizados e deploy seguro? [fonte: TI] [impacto: Dev, DevOps]
13. A estratégia de backup e disaster recovery foi definida (RPO, RTO) para dados de produtos, clientes e pedidos? [fonte: TI, Compliance] [impacto: DevOps, Arquiteto]
14. A solução de e-mail transacional foi escolhida (SendGrid, Resend, Amazon SES) com templates e variáveis definidos? [fonte: Marketing, TI] [impacto: Dev]
15. O diagrama de arquitetura foi documentado, revisado e aprovado pelo time técnico e pelo patrocinador? [fonte: TI, Diretoria] [impacto: PM, Arquiteto, Dev]

---

## Etapa 06 — Setup

- **Configuração da plataforma**: Para SaaS (Shopify, VTEX): criar a loja/account, configurar moeda, idioma, país, fuso horário, e dados da empresa (CNPJ, endereço, logo). Instalar e configurar o tema/storefront, e criar as categorias do catálogo. Para headless/custom: setup do repositório, scaffolding do frontend e backend, e configuração do banco de dados. Independente da abordagem, o ambiente de desenvolvimento deve estar funcional antes de iniciar o build — dev deve conseguir adicionar um produto e fazer um pedido de teste end-to-end.

- **Configuração do gateway de pagamento**: Criar a conta no gateway escolhido, enviar documentação para aprovação (contrato social, CNPJ, dados bancários para repasse), configurar os meios de pagamento (cartão com bandeiras, PIX com chave, boleto com dados do beneficiário), ativar antifraude, e configurar os webhooks de confirmação de pagamento apontando para o e-commerce. Testar em ambiente sandbox: pagamento aprovado, pagamento recusado, pagamento pendente (PIX aguardando), e estorno/chargeback. A aprovação de conta no gateway pode levar de 24h a 2 semanas — não deixar para última hora.

- **Configuração de logística e frete**: Cadastrar as transportadoras contratadas na plataforma ou no hub de frete (Melhor Envio, Intelipost, Kangu), configurar tabelas de frete por modalidade e região, configurar regras de frete grátis (acima de R$X, para região Y), e testar o cálculo de frete com CEPs de diferentes regiões. Configurar a integração para geração automática de etiqueta de envio e rastreamento. Testar o fluxo completo: pedido aprovado → etiqueta gerada → código de rastreamento atualizado → comprador notificado.

- **Integração com ERP e NF-e**: Configurar a integração com o ERP para: envio de pedidos (e-commerce → ERP quando pagamento aprovado), consulta de estoque (ERP → e-commerce para atualização periódica ou em tempo real), e emissão de NF-e (ERP emite com dados do pedido). Testar o fluxo completo em sandbox: pedido no e-commerce → pedido no ERP → NF-e emitida → XML disponível → e-mail com NF-e enviado ao comprador. Se o ERP não tem API, considerar hubs de integração (Bling, Tiny, Omie) como middleware.

- **Configuração de domínio e SSL**: Registrar ou configurar o domínio principal do e-commerce, apontar o DNS para a plataforma de hospedagem, ativar SSL/TLS em todo o site (obrigatório para e-commerce — browsers marcam sites sem HTTPS como "não seguros"), e configurar redirects de www para raiz ou vice-versa. Se a loja terá subdomínio (loja.marca.com.br vs. marca.com.br), configurar com antecedência. Para Shopify e VTEX, o SSL é automático após DNS configurado.

- **Ambientes de teste e sandbox**: Configurar ambientes de sandbox para cada integração — gateway de pagamento em modo teste (transações não reais), ERP em ambiente de homologação, transportadora com conta de teste. O time de QA e os stakeholders precisam conseguir fazer pedidos de teste end-to-end sem gerar transações financeiras reais, sem emitir NF-e real, e sem despachar produtos reais. Se qualquer integração não tem sandbox, documentar o risco e definir o processo de teste em produção com controles manuais.

### Perguntas

1. A plataforma de e-commerce está configurada com dados da empresa, moeda, idioma e tema/storefront? [fonte: Dev, TI] [impacto: Dev]
2. O gateway de pagamento foi aprovado, configurado com todos os meios de pagamento e testado em sandbox? [fonte: Financeiro, Dev] [impacto: Dev, Financeiro]
3. As transportadoras e regras de frete estão cadastradas e o cálculo foi testado com CEPs de diferentes regiões? [fonte: Operações, Dev] [impacto: Dev, Operações]
4. A integração com o ERP está funcional para pedidos, estoque e NF-e em ambiente de sandbox? [fonte: TI, Dev] [impacto: Dev, Financeiro]
5. O domínio está configurado na plataforma com SSL ativo e funcionando? [fonte: TI, DevOps] [impacto: DevOps, Dev]
6. Os ambientes de sandbox de todas as integrações estão configurados e acessíveis para testes? [fonte: TI, Fornecedores] [impacto: Dev, QA]
7. O pipeline de CI/CD está funcional com preview por branch e deploy automático? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
8. As variáveis de ambiente estão configuradas corretamente em cada ambiente (dev, staging, produção)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
9. O fluxo de pedido completo (carrinho → checkout → pagamento → confirmação) funciona end-to-end em sandbox? [fonte: Dev, QA] [impacto: Dev, QA]
10. O e-mail transacional está configurado e testado (confirmação de pedido, pagamento, despacho)? [fonte: Dev, Marketing] [impacto: Dev, Marketing]
11. Os primeiros produtos de teste foram cadastrados com todos os atributos, fotos e variações? [fonte: Dev, Comercial] [impacto: Dev, Conteúdo]
12. O analytics (GA4) e o e-commerce enhanced estão configurados com eventos de view_item, add_to_cart, purchase? [fonte: Dev, Marketing] [impacto: Dev, Marketing]
13. O acesso do time (marketing, operações, SAC) ao painel administrativo foi configurado com permissões corretas? [fonte: TI, Dev] [impacto: Dev, PM]
14. O processo de onboarding de novos desenvolvedores foi documentado com instruções de setup local? [fonte: Dev] [impacto: Dev]
15. O pipeline foi testado com um pedido real de teste end-to-end — produto cadastrado, carrinho, checkout, pagamento sandbox, confirmação? [fonte: Dev, QA] [impacto: Dev, QA]

---

## Etapa 07 — Build

- **Catálogo e busca**: Implementar a navegação por categorias, a busca com autocomplete e correção de erros, os filtros facetados com contagem de resultados, a ordenação, e as páginas de listagem (PLP) e detalhe de produto (PDP) com todos os elementos definidos: fotos com zoom, variações com seletor visual (cor como swatch, tamanho como botão), preço com promoção destacada, cálculo de frete inline, botão de adicionar ao carrinho com feedback visual, e produtos relacionados/recomendados. A PDP é a página mais importante do e-commerce — se o comprador não encontra a informação que precisa ou não confia no produto, a venda não acontece.

- **Carrinho e checkout**: Implementar o carrinho com: adição/remoção de itens, atualização de quantidade, cálculo de frete por CEP, aplicação de cupom de desconto, resumo com subtotal/frete/desconto/total, e persistência (carrinho salvo se o usuário sai e volta). O checkout deve incluir: identificação (login, cadastro ou guest checkout), endereço de entrega (com busca de CEP para auto-preenchimento via ViaCEP), seleção de frete (modalidades com prazo e preço), pagamento (formulário de cartão, QR code de PIX, geração de boleto), e confirmação. Cada campo desnecessário no checkout aumenta abandono — remover tudo que não é obrigatório.

- **Integrações de pagamento**: Implementar a integração com o gateway para cada meio de pagamento — cartão de crédito com parcelamento (opções de 1x a 12x com ou sem juros, cálculo de valor por parcela), PIX com QR code e expiração, boleto com vencimento e instruções, e carteiras digitais se aplicável. Implementar os webhooks de confirmação: pagamento aprovado → atualizar status do pedido → reservar estoque → disparar e-mail de confirmação. Implementar também: pagamento recusado → notificar comprador → liberar reserva de estoque, e estorno → processar reembolso → notificar comprador.

- **Fluxo de pedido e logística**: Implementar a máquina de estados do pedido conforme definido na Etapa 04 — cada transição de estado dispara ações automáticas (e-mails, atualização de estoque, NF-e, etiqueta de envio). Implementar a integração com transportadoras para: cálculo de frete no checkout, geração de etiqueta após faturamento, captura de código de rastreamento, e atualização automática de status de entrega. Implementar a página "Meus Pedidos" do comprador com timeline de status, código de rastreamento clicável, e opções de cancelamento/troca quando aplicável.

- **Cadastro de produtos e conteúdo**: Implementar a interface de cadastro/edição de produtos no admin — ou configurar o PIM (Product Information Management) se a plataforma oferecer. Paralelamente, executar o cadastro de todos os produtos do MVP com: fotos otimizadas (WebP, múltiplos tamanhos), descrições comerciais e técnicas, atributos filtráveis preenchidos, preços e estoque configurados, e SEO por produto (título, description, URL). O cadastro de produtos é frequentemente o gargalo do build em e-commerce — 500 SKUs com 5 fotos cada = 2.500 fotos para tratar e subir.

- **SEO de e-commerce**: Implementar os elementos de SEO específicos para e-commerce — dados estruturados Product (nome, preço, disponibilidade, avaliações), BreadcrumbList para navegação hierárquica, canonical tags para variações de produto, meta tags únicas por produto e categoria, sitemap dividido por tipo (produtos, categorias, páginas institucionais), e URLs amigáveis. Para lojas com grande catálogo, implementar pagination com rel="next/prev" ou infinite scroll com suporte a indexação. O SEO de e-commerce é responsável por 30-50% do tráfego em lojas maduras — negligenciar é perder receita orgânica.

### Perguntas

1. A PDP (página de produto) está completa com fotos, variações, preço, frete, descrição e botão de compra? [fonte: Designer, Comercial] [impacto: Dev]
2. O carrinho persiste entre sessões e lida corretamente com produtos fora de estoque ou preço alterado? [fonte: Dev, QA] [impacto: Dev]
3. O checkout funciona end-to-end com todos os meios de pagamento testados em sandbox? [fonte: Dev, QA] [impacto: Dev, Financeiro]
4. Os webhooks de pagamento estão implementados (aprovado, recusado, estornado) com ações automáticas corretas? [fonte: Dev] [impacto: Dev]
5. A máquina de estados do pedido está implementada com todas as transições e e-mails transacionais? [fonte: Dev, Operações] [impacto: Dev]
6. A integração com transportadoras funciona (cálculo de frete, etiqueta, rastreamento)? [fonte: Dev, Operações] [impacto: Dev, Operações]
7. O cadastro de produtos do MVP está completo com fotos otimizadas, descrições, atributos e SEO? [fonte: Comercial, Marketing, Conteúdo] [impacto: Conteúdo, PM]
8. A busca e filtros estão implementados com autocomplete, fuzzy search e contagem de resultados por filtro? [fonte: Dev] [impacto: Dev]
9. Os dados estruturados Product, BreadcrumbList e canonical tags estão implementados e validados? [fonte: Dev, SEO] [impacto: Dev, SEO]
10. O fluxo de troca e devolução está implementado com os estados e prazos definidos? [fonte: Dev, SAC] [impacto: Dev, SAC]
11. Os e-mails transacionais estão implementados, testados e com template alinhado à marca? [fonte: Dev, Marketing] [impacto: Dev, Marketing]
12. A integração com o ERP está funcional para pedidos, estoque e NF-e com dados reais em staging? [fonte: Dev, TI] [impacto: Dev, Financeiro]
13. As automações de marketing (carrinho abandonado, pós-venda) estão configuradas e testadas? [fonte: Dev, Marketing] [impacto: Dev, Marketing]
14. A acessibilidade (WCAG 2.1 AA) está sendo implementada ao longo do build, especialmente no checkout? [fonte: Designer, QA] [impacto: Dev, QA]
15. A página "Minha Conta" está completa com pedidos, endereços, dados pessoais e favoritos? [fonte: Designer, Dev] [impacto: Dev]

---

## Etapa 08 — QA

- **Teste de checkout end-to-end**: Testar o fluxo completo de compra com cada meio de pagamento — cartão aprovado, cartão recusado, cartão com 3D Secure, PIX gerado e pago, PIX expirado, boleto gerado e pago, boleto vencido. Para cada cenário, verificar: status do pedido atualizado corretamente, estoque reservado/liberado conforme esperado, e-mail transacional enviado, e NF-e emitida (se integração está ativa). Testar também: compra como guest (sem cadastro), compra com cadastro novo, compra com login existente, e compra com cupom de desconto. O checkout é onde o dinheiro entra — qualquer bug aqui é perda direta de receita.

- **Teste de cálculo de frete e prazo**: Verificar o cálculo de frete com CEPs representativos de cada região — capitais, interior, áreas de risco, áreas rurais. Confirmar que o prazo informado é realista (não prometer entrega em 2 dias para um CEP que a transportadora leva 7). Testar cenários especiais: frete grátis aplicado corretamente acima do valor mínimo, produto com dimensão/peso atípico (oversize), envio para CEP não atendido (mensagem de erro clara, não erro genérico). Frete incorreto gera reclamação, cancelamento ou prejuízo logístico.

- **Teste de estoque e concorrência**: Simular cenários de concorrência — dois compradores adicionam o último item ao carrinho ao mesmo tempo: apenas um deve conseguir finalizar a compra, o outro deve ver mensagem de estoque esgotado. Verificar que a reserva de estoque é liberada corretamente quando: o pagamento é recusado, o pedido é cancelado, o boleto/PIX vence sem pagamento. Testar o comportamento quando o estoque é zerado durante a navegação do comprador — o produto deve mostrar "indisponível" sem erro.

- **Teste de performance e carga**: Rodar testes de carga simulando o tráfego esperado em dia normal e em pico sazonal (Black Friday). Medir: tempo de carregamento da PLP e PDP, tempo de resposta do carrinho e checkout, tempo de resposta da busca, e taxa de erro sob carga. Para plataformas SaaS (Shopify, VTEX), o teste de infraestrutura é menos relevante, mas o teste de performance do frontend (Lighthouse) é obrigatório. Para headless/custom, o teste de carga na API e no banco de dados é crítico — identificar bottlenecks antes do pico sazonal.

- **Teste de integrações**: Testar cada integração end-to-end em staging com dados realistas — pedido sincronizado com ERP, NF-e emitida corretamente, etiqueta de envio gerada, código de rastreamento atualizado, produto sincronizado com marketplace externo. Testar cenários de falha: ERP indisponível (pedido deve ficar em fila e sincronizar quando ERP voltar), transportadora com erro (alerta para operação, não erro para comprador), gateway com timeout (retry com backoff). Integrações que funcionam no happy path e falham no edge case geram operação manual e reclamação.

- **Teste de segurança**: Verificar vulnerabilidades específicas de e-commerce — SQL injection em campos de busca e formulários, XSS em campos de cadastro e avaliação, CSRF em ações de checkout e pagamento, brute force em cupons de desconto (tentativa automatizada de milhares de códigos), e exposição de dados sensíveis em responses de API (dados de cartão, CPF completo em resposta JSON). Para plataformas SaaS, a segurança de infraestrutura é de responsabilidade da plataforma — mas customizações e apps de terceiros precisam ser auditados.

- **Teste mobile e responsividade**: Testar a experiência completa de compra em dispositivos móveis — navegação por categoria, busca, filtros, PDP, carrinho, checkout e pagamento. Em e-commerce, 60-75% do tráfego vem de mobile, mas a conversão mobile é tipicamente 2-3x menor que desktop — cada fricção no mobile é perda amplificada. Verificar: botões com área de toque ≥ 44px, formulários com teclado adequado (numérico para CEP e cartão), e checkout que funciona sem zoom.

### Perguntas

1. O checkout foi testado end-to-end com cada meio de pagamento (aprovado, recusado, pendente, expirado, estornado)? [fonte: Dev, QA] [impacto: Dev, Financeiro]
2. O cálculo de frete foi testado com CEPs de todas as regiões, incluindo áreas de risco e produtos oversize? [fonte: QA, Operações] [impacto: Dev, Operações]
3. Os cenários de concorrência de estoque foram testados (último item, reserva, liberação)? [fonte: QA, Dev] [impacto: Dev]
4. O teste de carga simulou o tráfego de pico sazonal e os tempos de resposta são aceitáveis? [fonte: DevOps, QA] [impacto: DevOps, Dev]
5. Todas as integrações foram testadas end-to-end incluindo cenários de falha e recovery? [fonte: Dev, QA] [impacto: Dev]
6. O teste de segurança cobriu SQL injection, XSS, CSRF, brute force de cupons e exposição de dados? [fonte: Segurança, QA] [impacto: Dev, Segurança]
7. A experiência completa de compra foi testada em dispositivos móveis reais (não apenas emulação)? [fonte: QA, Designer] [impacto: Dev, Designer]
8. Os e-mails transacionais foram verificados em múltiplos clientes de e-mail (Gmail, Outlook, mobile)? [fonte: QA, Marketing] [impacto: Dev, Marketing]
9. O Lighthouse foi rodado para PLP, PDP, carrinho e checkout com scores documentados? [fonte: Dev] [impacto: Dev, SEO]
10. O fluxo de troca e devolução foi testado end-to-end incluindo reembolso e reposição de estoque? [fonte: QA, SAC] [impacto: Dev, SAC]
11. A busca e filtros foram testados com termos reais (incluindo erros de digitação, acentos e termos ambíguos)? [fonte: QA] [impacto: Dev]
12. O robots.txt e sitemap.xml estão corretos e não bloqueiam páginas de produto/categoria? [fonte: Dev, SEO] [impacto: SEO, Dev]
13. Os eventos de e-commerce enhanced (GA4) estão disparando corretamente em cada etapa do funil? [fonte: Dev, Marketing] [impacto: Marketing]
14. O fluxo de cadastro/login foi testado incluindo recuperação de senha, login social e guest checkout? [fonte: QA] [impacto: Dev]
15. A revisão de conteúdo de produtos (ortografia, descrições, preços, fotos) foi concluída em todos os SKUs do MVP? [fonte: Comercial, Marketing] [impacto: Conteúdo]

---

## Etapa 09 — Launch Prep

- **Configuração de produção do gateway**: Migrar do modo sandbox para modo de produção no gateway de pagamento — ativar credenciais de produção, configurar meios de pagamento definitivos (com taxas e prazos de repasse reais), ativar antifraude em modo de produção, e configurar a conta bancária de recebimento. Fazer um pedido real de valor mínimo (R$1) com cartão da empresa para validar que o fluxo funciona end-to-end em produção — pagamento processado, repasse agendado, NF-e emitida. Uma configuração errada de gateway em produção resulta em pedidos aprovados sem recebimento ou pedidos recusados sem motivo.

- **Plano de cutover e migração**: Se substituindo plataforma existente, documentar a sequência exata: congelar preços e estoque na plataforma antiga, migrar dados finais (produtos, clientes, pedidos em aberto), trocar DNS, validar checkout com pedido real, e desativar plataforma antiga após período de paralelo. Para SEO, configurar redirects 301 de todas as URLs antigas para as novas (produto por produto, categoria por categoria). Testar cada redirect antes do go-live. Reduzir TTL do DNS para 300s com 24-48h de antecedência.

- **Operação logística validada**: Confirmar que a operação logística está pronta para processar pedidos reais — picking/packing com equipe treinada, embalagens em estoque, etiquetas sendo geradas corretamente, transportadoras com coleta agendada ou ponto de postagem identificado. Fazer um pedido real de teste e executar o fluxo físico completo: separar o produto, embalar, etiquetar, despachar, e confirmar entrega. Se a operação nunca processou um pedido digital antes, fazer ao menos 10 pedidos de teste antes do go-live.

- **Treinamento do time operacional**: Treinar cada área que vai operar o e-commerce — marketing (como cadastrar produtos, criar promoções, publicar banners), operações/logística (como visualizar pedidos, gerar etiquetas, atualizar status), SAC (como consultar pedidos, processar trocas/devoluções, acionar estorno), e financeiro (como acompanhar conciliação, verificar repasses, tratar chargebacks). Entregar documentação com capturas de tela para cada fluxo. Treinamento sem documentação é esquecido em duas semanas.

- **Analytics e conversão configurados**: Configurar todos os eventos de e-commerce enhanced no GA4 — view_item, add_to_cart, begin_checkout, add_payment_info, purchase, refund. Configurar metas de conversão. Se há mídia paga ativa no lançamento (Meta Ads, Google Ads), configurar os pixels de conversão com valor de compra para que o ROAS possa ser medido desde o primeiro dia. Testar cada evento com o GA4 DebugView e o Meta Pixel Helper antes do lançamento — dados de conversão perdidos nos primeiros dias não podem ser recuperados.

- **Plano de rollback**: Documentar o plano de rollback — se o checkout apresenta problemas graves nas primeiras horas, qual a sequência de ações? Para migração de plataforma, manter a loja antiga funcional por pelo menos 48h. Para loja nova, ter um landing page de "em breve" como fallback. Definir critérios claros de acionamento (taxa de erro no checkout > 5%, gateway com falha sistêmica, estoque não sincronizando) e quem tem autoridade para decidir.

### Perguntas

1. O gateway de pagamento foi migrado para produção e validado com pedido real de valor mínimo? [fonte: Financeiro, Dev] [impacto: Dev, Financeiro]
2. O plano de cutover está documentado com sequência exata, responsáveis e critérios de validação? [fonte: Dev, PM] [impacto: Dev, DevOps, PM]
3. Os redirects 301 do site anterior foram configurados e testados individualmente? [fonte: Dev, SEO] [impacto: SEO, Dev]
4. O TTL do DNS foi reduzido para 300s com pelo menos 24h de antecedência? [fonte: TI, DevOps] [impacto: DevOps, Dev]
5. A operação logística processou pedidos de teste com fluxo físico completo (picking, packing, despacho)? [fonte: Operações] [impacto: Operações, PM]
6. O treinamento de cada área (marketing, operações, SAC, financeiro) foi realizado e documentação entregue? [fonte: PM, Dev] [impacto: PM]
7. Os eventos de e-commerce enhanced (GA4) e pixels de conversão estão configurados e validados? [fonte: Marketing, Dev] [impacto: Marketing]
8. O plano de rollback está documentado com critérios de acionamento e responsável designado? [fonte: TI, Diretoria] [impacto: PM, DevOps]
9. A propriedade foi verificada no Google Search Console e o sitemap está pronto para submissão? [fonte: Dev, SEO] [impacto: SEO]
10. O monitoramento de disponibilidade (UptimeRobot, Better Uptime) está configurado com alertas? [fonte: DevOps] [impacto: DevOps, Dev]
11. A lista de todos os acessos a entregar ao cliente foi revisada e testada? [fonte: Dev, DevOps] [impacto: PM]
12. Todos os stakeholders foram notificados sobre data, horário e impactos do go-live? [fonte: Diretoria, PM] [impacto: PM]
13. A janela de go-live foi escolhida estrategicamente (não véspera de Black Friday, com time disponível por 48h)? [fonte: PM, TI] [impacto: PM, DevOps]
14. A plataforma/loja antiga está garantida como ativa por pelo menos 48h após o cutover como fallback? [fonte: TI] [impacto: DevOps, PM]
15. O estoque está sincronizado e correto na plataforma nova antes da abertura para vendas? [fonte: Operações, TI] [impacto: Operações, Dev]

---

## Etapa 10 — Go-Live

- **Cutover e abertura da loja**: Executar o cutover conforme o plano — trocar DNS, verificar propagação, confirmar SSL, e abrir a loja para vendas. Fazer imediatamente um pedido real de teste (compra com cartão da empresa) e acompanhar o fluxo completo: pagamento processado, pedido aparece no admin, estoque decrementado, e-mail de confirmação recebido, pedido sincronizado com ERP, NF-e emitida. Se qualquer etapa falhar, corrigir antes de anunciar o lançamento publicamente. A primeira venda real é o teste mais importante — se ela funcionar end-to-end, o sistema está operacional.

- **Monitoramento das primeiras 24 horas**: Monitorar ativamente nas primeiras 24h: taxa de erro no checkout (meta: < 1%), tempo de resposta das páginas (meta: < 3s em mobile), status das integrações (ERP sincronizando, gateway respondendo, transportadora gerando etiquetas), e alertas de disponibilidade. Ter ao menos uma pessoa do time técnico de plantão nas primeiras 48h para reagir rapidamente a qualquer incidente. Problemas nas primeiras horas — gateway com erro, frete calculando errado, e-mail não chegando — têm impacto amplificado porque é quando o marketing está gerando tráfego para a nova loja.

- **Validação de conversões e analytics**: Verificar que os eventos de e-commerce enhanced estão sendo disparados com dados corretos — view_item com ID e preço do produto, add_to_cart com quantidade e valor, purchase com transaction_id, valor total e itens. Verificar no GA4 Real-Time que os eventos estão chegando. Se há mídia paga ativa, confirmar que os pixels de conversão (Meta, Google Ads) estão reportando vendas com valor correto — dados de conversão errados nas primeiras horas invalidam a otimização de campanha.

- **Monitoramento da primeira semana**: Monitorar diariamente: número de pedidos vs. projeção, ticket médio, taxa de conversão por etapa do funil (PDP → carrinho → checkout → pagamento → confirmação), taxa de abandono de carrinho, taxa de pagamento recusado, volume de tickets de SAC por tipo (dúvida, reclamação, troca), e custo de operação (gateway, plataforma, infraestrutura). Comparar com as projeções da Inception e documentar desvios. Se a taxa de conversão é significativamente menor que o esperado, investigar imediatamente — pode ser problema técnico (checkout lento, erro de pagamento) ou problema de produto (frete caro, preço fora de mercado).

- **Submissão do sitemap e SEO pós-lançamento**: Submeter o sitemap no Google Search Console e solicitar indexação das páginas principais. Monitorar nos primeiros dias: erros de cobertura (URLs bloqueadas, redirects incorretos, canonical conflitantes), e indexação progressiva de páginas de produto e categoria. Para migrações, verificar que os redirects 301 estão funcionando e que o Google está transferindo a autoridade das URLs antigas para as novas. O tráfego orgânico pode cair temporariamente após migração e se recuperar em 4-8 semanas — queda permanente indica problema de redirect ou canonical.

- **Entrega e handoff ao cliente**: Entregar formalmente todos os acessos: painel admin da plataforma com roles configurados, gateway de pagamento com acesso ao dashboard financeiro, hub de frete com acesso à gestão de envios, ERP com visibilidade de pedidos do e-commerce, Google Analytics e Search Console, e repositório de código (se headless/custom). Documentação mínima: como cadastrar/editar produtos, como processar pedidos, como criar promoções, como tratar devoluções, como acessar relatórios de vendas, e contato de suporte técnico com SLA.

### Perguntas

1. A propagação do DNS foi confirmada e o SSL está ativo sem alertas de segurança? [fonte: DevOps, TI] [impacto: DevOps, Dev]
2. O pedido real de teste funciona end-to-end (pagamento, estoque, ERP, NF-e, e-mail)? [fonte: Dev, QA] [impacto: Dev, Financeiro, Operações]
3. O monitoramento das primeiras 24h está ativo com time técnico de plantão? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
4. Os eventos de e-commerce enhanced e pixels de conversão estão reportando vendas reais corretamente? [fonte: Marketing, Dev] [impacto: Marketing]
5. As integrações (ERP, gateway, transportadora) estão sincronizando em produção sem erros? [fonte: Dev, TI] [impacto: Dev, Operações]
6. A taxa de erro no checkout está abaixo de 1% nas primeiras horas? [fonte: DevOps, Dev] [impacto: Dev, Financeiro]
7. O SAC está operacional e preparado para atender os primeiros clientes? [fonte: SAC, PM] [impacto: SAC, PM]
8. O sitemap foi submetido no Google Search Console e os redirects do site anterior estão funcionando? [fonte: Dev, SEO] [impacto: SEO]
9. O estoque na plataforma está correto e sincronizando com o ERP em produção? [fonte: Operações, TI] [impacto: Operações, Dev]
10. A loja/plataforma anterior está ativa e funcional durante o período de fallback de 48h? [fonte: TI] [impacto: DevOps, PM]
11. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou que consegue acessar? [fonte: Dev, PM] [impacto: PM]
12. O aceite formal de entrega foi obtido do cliente (e-mail, assinatura de ata, ou confirmação documentada)? [fonte: Diretoria] [impacto: PM]
13. O plano de suporte pós-lançamento foi ativado com canal e SLA comunicados ao cliente? [fonte: Diretoria, PM] [impacto: PM, Dev]
14. As métricas da primeira semana (pedidos, conversão, ticket médio, abandono) estão sendo acompanhadas vs. projeção? [fonte: Marketing, Comercial, PM] [impacto: PM, Marketing]
15. O Lighthouse foi re-executado em produção para PDP, PLP e checkout com scores documentados como baseline? [fonte: Dev] [impacto: Dev, SEO]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos algo tipo Amazon"** — O cliente referencia o maior marketplace do mundo como benchmark para uma loja D2C de 50 SKUs. Alinhar expectativas imediatamente: Amazon tem 15.000 engenheiros e um orçamento de bilhões. O foco deve ser no que diferencia a loja do cliente, não em replicar features de um gigante.
- **"Não precisa de nota fiscal, a gente resolve depois"** — NF-e é obrigação legal para vendas online no Brasil. "Resolver depois" significa operar ilegalmente até que a Receita Federal detecte. A integração fiscal precisa estar no escopo do MVP, não como "fase 2".
- **"O prazo é para a Black Friday"** — Se estamos em setembro e o prazo é novembro, o projeto tem 2 meses para o go-live mais exigente do ano em termos de performance. Se o e-commerce nunca operou, lançar na Black Friday é um risco alto. Considerar lançar antes (outubro) com tráfego baixo para estabilizar antes do pico.

### Etapa 02 — Discovery

- **"Nosso catálogo tem 50 produtos" (mas 5.000 SKUs)** — 50 produtos com variações de tamanho, cor e estampa podem gerar milhares de SKUs. O esforço de cadastro, gestão de estoque e busca é proporcional ao número de SKUs, não de produtos. Mapear SKUs reais, não produtos genéricos.
- **"O frete a gente vê depois"** — Frete é o fator #1 de abandono de carrinho no Brasil. Se o cálculo de frete não está mapeado no Discovery, o prazo de build vai estourar. Transportadoras, tabelas de frete e regras de frete grátis precisam ser definidos aqui.
- **"Não temos política de troca"** — O CDC garante 7 dias de arrependimento para compras online. Não ter política de troca não é opção legal — é negligência. Definir política antes do build para implementar o fluxo corretamente.

### Etapa 03 — Alignment

- **"Vamos começar com Shopify e depois migrar para headless"** — Migração de plataforma de e-commerce é projeto de 3-6 meses com risco de perda de SEO, dados e integrações. Se headless é o objetivo, começar com headless. Se Shopify atende, ficar no Shopify. "Começar com X para migrar para Y" é desperdício de investimento em 90% dos casos.
- **"O design vem da agência, vocês só implementam"** — Se a agência de design não entende de UX de e-commerce, o design vai ter checkout de 7 etapas, PDP sem cálculo de frete, e carrinho sem cupom. Design de e-commerce precisa de UX especializado em conversão, não design genérico.
- **"A gente opera a logística na hora"** — Operação logística que nunca processou um pedido digital não vai funcionar "na hora". Precisa de treinamento, integração com sistema, embalagens, e processo definido antes do go-live.

### Etapa 04 — Definition

- **Regras de promoção definidas "de cabeça"** — "Cupom de 10% no site inteiro" parece simples até descobrir que acumula com promoção de categoria, não tem limite de uso, e se aplica a produtos com margem negativa. Regras de promoção precisam de especificação formal: quais produtos, quais condições, qual limite, se acumula.
- **"O estoque é o que tem no ERP"** — Se o ERP atualiza estoque uma vez por dia e o e-commerce vende o último item, o próximo comprador vai comprar um produto que não existe. Frequência de sincronização de estoque precisa ser definida (e testada) antes do build.
- **URLs de produto com ID numérico** — /produto/12345 em vez de /camiseta-algodao-preta-m. URLs não descritivas prejudicam SEO e UX. Definir padrão de URL semântica antes do build — mudar depois gera redirects e perda de indexação.

### Etapa 05 — Architecture

- **"Vamos fazer tudo custom"** — Construir e-commerce do zero quando existem plataformas maduras (Shopify, VTEX, Medusa) que resolvem 80% dos requisitos. Custom justifica-se apenas quando o diferencial competitivo está na experiência técnica que nenhuma plataforma entrega. Para a maioria dos casos, custom é over-engineering.
- **"Não precisamos de CDN, o server aguenta"** — Página de produto com 10 fotos de alta resolução servida de um servidor único. Na Black Friday, o servidor cai. CDN é obrigatório para e-commerce — não é otimização, é requisito.
- **"O antifraude é responsabilidade do gateway"** — O gateway oferece antifraude básico, mas chargebacks caem no lojista. Se o produto tem alto risco de fraude (eletrônicos, produtos de valor alto), antifraude dedicado (ClearSale, Konduto, Signifyd) é investimento com retorno direto em redução de chargeback.

### Etapa 06 — Setup

- **Gateway configurado apenas em sandbox** — Time inteiro trabalha em sandbox por meses e descobre no dia do go-live que a conta de produção do gateway não foi aprovada (documentação pendente, dados bancários incorretos). Iniciar o processo de aprovação do gateway em produção na Etapa 06, não na Etapa 09.
- **Sem integração com ERP em staging** — "A integração com o ERP a gente testa em produção." Pedidos duplicados, NF-e com dados errados, estoque desatualizado — tudo descoberto com pedidos reais de clientes reais. Testar integração em staging com dados realistas é obrigatório.
- **Acesso do time operacional configurado no último dia** — Marketing, operações e SAC recebem acesso ao painel na véspera do go-live. Resultado: ninguém sabe onde encontrar pedidos, como processar envios ou como responder clientes. Configurar acessos e treinar na Etapa 06, não na 09.

### Etapa 07 — Build

- **Checkout testado apenas com cartão de crédito** — "PIX e boleto a gente testa depois." PIX é o meio de pagamento mais usado no Brasil. Boleto tem fluxo assíncrono com confirmação por webhook que precisa de teste dedicado. Cada meio de pagamento precisa ser testado individualmente durante o Build.
- **Catálogo com fotos de placeholder** — "A gente coloca as fotos de verdade depois." Fotos placeholder não revelam problemas de layout (proporção errada, fundo inconsistente, zoom que não funciona). Cadastro com fotos reais desde o build é obrigatório para QA visual.
- **SEO deixado para o final** — "Depois a gente otimiza o SEO." Dados estruturados, canonical tags, sitemap e URLs amigáveis devem ser implementados durante o Build. Retrofitar SEO em e-commerce com 500 produtos publicados é projeto de semanas.

### Etapa 08 — QA

- **"Fiz um pedido de teste e funcionou"** — Um pedido com cartão aprovado não é QA. QA de checkout exige: cartão recusado, PIX expirado, boleto vencido, cupom inválido, estoque zerado durante checkout, endereço inválido, CPF inválido. O happy path funciona; os edge cases é que geram prejuízo e reclamação.
- **QA sem testar mobile** — Tester no desktop Chrome. 65% dos compradores estão no celular. Checkout que funciona no desktop e falha no mobile perde a maioria dos clientes. Testar em dispositivos reais (não apenas emulação).
- **Performance testada apenas com catálogo vazio** — Lighthouse dá 95 com 10 produtos. Com 5.000 produtos, a listagem fica lenta, a busca demora, e a home com produtos recomendados carrega devagar. Testar com volume realista de catálogo.

### Etapa 09 — Launch Prep

- **Go-live sem testar gateway em produção** — Sandbox funcionou perfeitamente. Produção usa credenciais diferentes, taxas reais, antifraude ativo, e regras de aprovação do banco adquirente. Fazer pelo menos 3 pedidos reais de teste (cartão, PIX, boleto) antes de abrir a loja.
- **Operação logística não testada** — A equipe de logística nunca viu um pedido digital. No primeiro dia, não sabem onde encontrar os pedidos, como gerar etiquetas, ou como embalar para envio. Treinar e testar com pedidos reais antes do go-live.
- **"A gente avisa os clientes quando a loja estiver no ar"** — Sem plano de comunicação de lançamento. Marketing descobre que a loja abriu por acaso. Plano de lançamento (e-mail blast, redes sociais, mídia paga) coordenado com a data do go-live é obrigatório para gerar tráfego no primeiro dia.

### Etapa 10 — Go-Live

- **Go-live na Black Friday** — Primeiro dia de operação no dia de maior tráfego do ano. Se algo der errado, o impacto financeiro é máximo. Go-live com pelo menos 4-6 semanas de antecedência de picos sazonais para estabilizar operação.
- **Desativar loja antiga no mesmo dia** — DNS ainda propagando, clientes com cache vendo loja antiga. Manter loja antiga ativa por 48h com redirect para a nova é seguro e barato.
- **"A loja está no ar, projeto encerrado"** — Sem monitoramento da primeira semana, sem acompanhamento de conversão, sem ajuste de operação. As primeiras semanas são críticas para identificar problemas de UX, logística e integração que só aparecem com clientes reais.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é e-commerce tradicional** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Não vendemos produtos, vendemos serviços com agendamento" | SaaS de agendamento, não e-commerce | Reclassificar para web-app ou SaaS |
| "O cliente monta o produto customizado online" | Configurador/CPQ (Configure, Price, Quote) | Avaliar se e-commerce com customização resolve ou se precisa de app custom |
| "É mais um portal de cotação, o preço depende de negociação" | Portal B2B com cotação, não e-commerce self-service | Reclassificar para web-app B2B com fluxo de cotação |
| "Precisamos de um app mobile nativo, não de site" | App mobile, não e-commerce web | Reclassificar para mobile app (pode incluir e-commerce como backend) |
| "Os clientes vão assinar e receber conteúdo digital" | Plataforma de conteúdo/membership | Reclassificar para SaaS/membership, não e-commerce de produtos físicos |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não temos CNPJ ativo ou inscrição estadual" | 01 | Não pode vender online legalmente no Brasil | Resolver situação fiscal antes de qualquer desenvolvimento |
| "Não sabemos qual gateway de pagamento usar" | 01 | Checkout impossível sem gateway | Definir gateway antes da Etapa 03 — aprovação pode levar semanas |
| "Não temos operação logística definida" | 01 | Pedidos sem fulfillment = reclamação e cancelamento | Definir operação (warehouse, transportadora, processo) antes da Etapa 06 |
| "O catálogo de produtos não está estruturado" | 02 | Build bloqueado por falta de dados de produto | Estruturar catálogo (SKUs, atributos, fotos, preços) antes de iniciar o Build |
| "Não temos contador ou sistema para NF-e" | 01 | Operação ilegal sem emissão de NF-e | Contratar contador e sistema fiscal antes do go-live |
| "Não temos equipe para atender clientes" | 03 | Reclamações em Procon e Reclame Aqui sem SAC | Definir equipe e ferramenta de SAC antes do go-live |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Temos 10.000 SKUs com variações" | 02 | Cadastro de catálogo pode levar meses e dominar o esforço do projeto | Planejar cadastro em fases e automatizar com importação em massa |
| "O ERP é antigo e não tem API" | 02 | Integração será manual, por arquivo, ou via banco direto — frágil | Planejar middleware/hub de integração e estimar esforço de integração separadamente |
| "Queremos vender para o Brasil inteiro" | 02 | ICMS interestadual (DIFAL) é complexo e varia por estado | Envolver contador especialista em tributação de e-commerce |
| "Vamos lançar com campanha de mídia paga pesada" | 09 | Alto tráfego no primeiro dia sem estabilização prévia | Lançar com tráfego orgânico baixo primeiro, depois ativar mídia paga |
| "O preço vai mudar dependendo do marketplace" | 03 | Pricing multi-canal exige sincronização e pode gerar conflito com política de preço mínimo | Definir estratégia de pricing por canal antes de integrar marketplaces |
| "Nunca vendemos online antes" | 01 | Toda a operação digital é nova — curva de aprendizado em todas as áreas | Planejar treinamento reforçado e go-live com volume baixo para aprendizado |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Gatilho da demanda e modelo de monetização identificados (perguntas 1 e 2)
- Volume estimado de pedidos e SKUs dimensionado (pergunta 4)
- Orçamento de desenvolvimento e operação aprovado (pergunta 8)
- Prazo de go-live com justificativa de negócio (pergunta 9)
- Emissão de NF-e resolvida (pergunta 10)

### Etapa 02 → 03

- Catálogo de produtos mapeado com SKUs, atributos e variações (pergunta 1)
- Meios de pagamento obrigatórios definidos (pergunta 3)
- Operação logística mapeada (perguntas 4 e 5)
- Integrações obrigatórias listadas (pergunta 6)
- Política de trocas e devoluções formalizada (pergunta 9)

### Etapa 03 → 04

- Plataforma (SaaS, headless, custom) escolhida e justificada (pergunta 1)
- Gateway de pagamento escolhido e processo de aprovação iniciado (pergunta 2)
- Operação logística definida com SLAs de expedição (pergunta 3)
- SAC definido com canal, horário e ferramenta (pergunta 4)

### Etapa 04 → 05

- Taxonomia de categorias e atributos aprovada (pergunta 1)
- Regras de precificação e promoções especificadas (pergunta 2)
- Máquina de estados do pedido documentada (pergunta 3)
- Modelo de estoque definido com regras de reserva (pergunta 4)
- Documentação aprovada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- Arquitetura da plataforma detalhada com diagramas (pergunta 1)
- Gateway e checkout desenhados (pergunta 2)
- Estratégia de escalabilidade definida para picos (pergunta 4)
- Custos mensais projetados e aprovados (pergunta 8)
- Diagrama de arquitetura aprovado (pergunta 15)

### Etapa 06 → 07

- Plataforma configurada com ambiente funcional (pergunta 1)
- Gateway configurado e testado em sandbox (pergunta 2)
- Frete configurado e testado (pergunta 3)
- Integração com ERP funcional em sandbox (pergunta 4)
- Fluxo de pedido testado end-to-end em sandbox (pergunta 15)

### Etapa 07 → 08

- PDP completa com fotos, variações, frete e compra (pergunta 1)
- Checkout funciona com todos os meios de pagamento (pergunta 3)
- Cadastro de produtos do MVP completo (pergunta 7)
- Integração com ERP funcional em staging (pergunta 12)

### Etapa 08 → 09

- Checkout testado com todos os cenários de pagamento (pergunta 1)
- Frete validado com CEPs de todas as regiões (pergunta 2)
- Teste de carga simulando pico sazonal (pergunta 4)
- Teste de segurança concluído sem vulnerabilidades críticas (pergunta 6)
- Experiência mobile testada em dispositivos reais (pergunta 7)

### Etapa 09 → 10

- Gateway migrado para produção e validado com pedido real (pergunta 1)
- Redirects configurados e testados (pergunta 3, se migração)
- Operação logística validada com fluxo físico completo (pergunta 5)
- Treinamento de todas as áreas realizado e documentado (pergunta 6)
- Plano de rollback documentado com critérios e responsável (pergunta 8)

### Etapa 10 → Encerramento

- DNS propagado e SSL ativo (pergunta 1)
- Pedido real funciona end-to-end (pergunta 2)
- Conversões e analytics reportando corretamente (pergunta 4)
- Todos os acessos entregues e aceite formal obtido (perguntas 11 e 12)
- Métricas da primeira semana acompanhadas vs. projeção (pergunta 14)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de e-commerce. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 D2C | V2 Marketplace | V3 B2B | V4 Assinatura | V5 Omnichannel |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 3 | 2 | 4 |
| 02 Discovery | 3 | 4 | 4 | 3 | 5 |
| 03 Alignment | 3 | 4 | 4 | 3 | 4 |
| 04 Definition | 3 | 5 | 5 | 4 | 5 |
| 05 Architecture | 3 | 5 | 4 | 3 | 5 |
| 06 Setup | 3 | 4 | 4 | 3 | 4 |
| 07 Build | 4 | 5 | 5 | 4 | 5 |
| 08 QA | 3 | 5 | 4 | 3 | 5 |
| 09 Launch Prep | 3 | 4 | 3 | 3 | 4 |
| 10 Go-Live | 2 | 3 | 3 | 2 | 3 |
| **Total relativo** | **29** | **42** | **39** | **30** | **44** |

**Observações por variante:**

- **V1 D2C**: Esforço mais equilibrado de todas as variantes. O Build é o mais pesado — experiência de marca diferenciada exige frontend refinado. Integrações são simples (1 gateway, 1 transportadora, 1 ERP). O gargalo oculto é a produção de conteúdo de produto (fotos, descrições).
- **V2 Marketplace**: O mais pesado em Definition e Architecture — multi-seller, split de pagamento, frete por seller e gestão de catálogo multi-fornecedor adicionam camadas de complexidade em cada etapa. QA é pesado porque cada cenário precisa ser testado para múltiplos sellers.
- **V3 B2B**: Definition e Build são pesados — tabela de preço por cliente, aprovação hierárquica, faturamento com prazo, e integração com ERP corporativo adicionam complexidade que B2C não tem. O volume de transações é menor, mas cada pedido é mais complexo.
- **V4 Assinatura**: Complexidade concentrada na Definition (ciclo de cobrança, dunning, gestão de planos) e no Build (integração com gateway de cobrança recorrente). O catálogo é tipicamente pequeno, o que reduz o esforço de cadastro e busca.
- **V5 Omnichannel**: O mais pesado no total — estoque unificado, OMS com routing inteligente, sincronização com PDV de lojas físicas, e experiência consistente cross-channel representam o maior desafio arquitetural de e-commerce. Cada etapa carrega a complexidade da integração físico-digital.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Sem site/plataforma anterior a migrar (Etapa 01, pergunta 6) | Etapa 02: pergunta 13 (migração de dados e SEO). Etapa 04: pergunta 13 (mapa de redirects). Etapa 09: perguntas 3 e 14 (redirects, loja antiga). Etapa 10: perguntas 8 e 10 (redirects, loja antiga ativa). |
| Idioma e moeda únicos (Etapa 02, pergunta 15) | Etapa 04: perguntas de i18n e multi-moeda. Etapa 05: suporte a multi-locale na arquitetura. Etapa 07: implementação de i18n. |
| Sem marketplace externo (Etapa 01, pergunta 7) | Etapa 05: perguntas sobre hub de integração com marketplaces. Etapa 06: setup de hub de marketplace. Etapa 07: sincronização de catálogo/estoque com canais externos. |
| Plataforma SaaS escolhida — não headless/custom (Etapa 03, pergunta 1) | Etapa 05: perguntas sobre arquitetura de backend, banco de dados, infraestrutura de servidores. Etapa 06: setup de repositório, CI/CD, hosting. Etapa 07: build de backend. Etapa 08: testes de carga de infraestrutura (responsabilidade da plataforma). |
| Sem cobrança recorrente — venda avulsa (Etapa 01, pergunta 2) | Etapa 04: perguntas sobre ciclo de cobrança, dunning, gestão de planos. Etapa 07: implementação de subscription billing. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Marketplace com multi-seller (Etapa 01, pergunta 2) | Etapa 03: split de pagamento se torna gate (pergunta 2). Etapa 04: máquina de estados com repasse ao seller obrigatória (pergunta 3). Etapa 05: arquitetura de multi-tenant e isolamento de dados por seller. Etapa 08: QA de cada fluxo por seller (cadastro, venda, repasse, disputa). |
| Migração de plataforma existente (Etapa 01, pergunta 6) | Etapa 02: pergunta 13 (migração de dados) se torna bloqueadora. Etapa 04: pergunta 13 (redirects) se torna gate. Etapa 09: plano de cutover com período de paralelo obrigatório. |
| B2B com tabela de preço por cliente (Etapa 02, pergunta 7) | Etapa 04: modelo de precificação com regras por grupo/contrato obrigatório (pergunta 2). Etapa 05: autenticação e autorização com perfis de comprador. Etapa 07: implementação de price lists e approval workflow. |
| Pico sazonal confirmado (Black Friday, etc.) (Etapa 01, pergunta 5) | Etapa 05: auto-scaling e cache se tornam gates (pergunta 4). Etapa 08: teste de carga com volume de pico é obrigatório (pergunta 4). Etapa 09: go-live antes do pico para estabilização se torna recomendação forte. |
| LGPD/GDPR identificados (Etapa 02, pergunta 10) | Etapa 05: requisitos de segurança e consent management obrigatórios (pergunta 6). Etapa 07: cookie banner, política de privacidade e opt-out obrigatórios. Etapa 08: teste de compliance obrigatório. |
| Omnichannel com lojas físicas (Etapa 01, variante V5) | Etapa 04: modelo de estoque unificado e routing obrigatórios (pergunta 4). Etapa 05: OMS se torna componente obrigatório da arquitetura. Etapa 07: integração com PDV e sincronização de estoque em tempo real obrigatórios. Etapa 08: testes de cenários cross-channel (compra online + retirada loja, ship-from-store). |
| Venda em marketplaces externos (Etapa 01, pergunta 7) | Etapa 05: hub de integração com marketplaces se torna componente da arquitetura. Etapa 06: setup de contas nos marketplaces e configuração do hub. Etapa 07: sincronização de catálogo, estoque e pedidos entre loja própria e canais externos. |
