---
title: "Marketplace / Plataforma — Blueprint"
description: "Plataforma two-sided ou multi-sided que conecta oferta e demanda. Gestão de comissões, split de pagamento, cold start problem, reputação e fulfillment."
category: project-blueprint
type: marketplace
status: rascunho
created: 2026-04-13
---

# Marketplace / Plataforma

## Descrição

Plataforma two-sided ou multi-sided que conecta oferta e demanda. Gestão de comissões, split de pagamento, cold start problem, reputação e fulfillment.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo marketplace é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Marketplace de Produtos Físicos

Plataforma que conecta vendedores (sellers) a compradores (buyers) para venda de produtos físicos com entrega. O desafio central é o fulfillment — logística de envio, rastreamento, prazo de entrega, devoluções e trocas. O split de pagamento (percentual da plataforma vs. seller) precisa ser transparente e automatizado. Catálogo de produtos com variações (tamanho, cor), estoque por seller, e busca com filtros são features core. Cold start é duplo: sem sellers não há catálogo, sem catálogo não há buyers. Exemplos: marketplace de artesanato, moda, eletrônicos usados, materiais de construção.

### V2 — Marketplace de Serviços

Plataforma que conecta prestadores de serviço a contratantes. Não há produto físico nem estoque — o "produto" é a disponibilidade e a qualificação do prestador. O desafio central é matching (conectar a demanda certa ao prestador certo), agendamento (disponibilidade, calendário, conflitos de horário), e confiança (avaliações, verificação de identidade, certificações). O pagamento pode ser por hora, por projeto, ou por milestone. Disputa e reembolso são mais complexos que em produto (o que é "serviço não entregue"?). Exemplos: marketplace de freelancers, serviços domésticos, consultorias, aulas particulares.

### V3 — Marketplace de Aluguel / Reservas

Plataforma para aluguel temporário de bens ou espaços. O desafio central é a gestão de disponibilidade (calendário com bloqueios, conflitos de reserva, mínimo de diárias), política de cancelamento (flexível, moderada, rígida com datas limite), e sazonalidade (preços dinâmicos por época, mínimo de diárias em alta temporada). O pagamento envolve antecipação (cobrar no momento da reserva ou no check-in), caução (depósito de segurança), e split com o proprietário após a estadia. Exemplos: aluguel de imóveis por temporada, coworking, equipamentos, veículos.

### V4 — Marketplace B2B / Procurement

Plataforma que conecta empresas compradoras a fornecedores. O fluxo é mais complexo que B2C: cotação (RFQ), negociação, pedido mínimo (MOQ), condições de pagamento (boleto 30/60/90 dias), nota fiscal, e compliance fiscal. Os compradores frequentemente precisam de aprovação interna antes de fechar pedido (workflow de compras). O catálogo é menos visual e mais técnico (especificações, fichas técnicas, certificados). A confiança é baseada em CNPJ verificado, histórico de transações, e referências. Exemplos: marketplace de insumos industriais, marketplace de embalagens, plataforma de fornecedores para restaurantes.

### V5 — Marketplace de Conteúdo Digital

Plataforma para venda de produtos digitais — cursos, templates, plugins, ebooks, assets de design, músicas, fotos. Não há logística física — a entrega é download ou acesso online. O desafio central é proteção de propriedade intelectual (DRM, prevenção de pirataria, licenciamento), modelo de monetização (venda única, assinatura, freemium com upgrade), e distribuição (CDN para arquivos grandes, streaming para vídeo/áudio). O split de pagamento é mais simples (percentual fixo), mas a gestão de licenças (pessoal, comercial, extended) adiciona complexidade. Exemplos: marketplace de cursos, templates de design, plugins WordPress, banco de imagens.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Frontend | Backend | Banco de Dados | Pagamentos | Observações |
|---|---|---|---|---|---|
| V1 — Produtos Físicos | Next.js | Node.js (NestJS) ou Ruby on Rails | PostgreSQL + Elasticsearch | Stripe Connect ou Pagar.me Split | Elasticsearch obrigatório para busca com filtros em catálogo grande. Redis para cache de catálogo. |
| V2 — Serviços | Next.js ou React Native (mobile) | Node.js (NestJS) | PostgreSQL + Redis | Stripe Connect | Redis para fila de matching. Calendar API para gestão de disponibilidade. Push notifications obrigatório. |
| V3 — Aluguel/Reservas | Next.js | Node.js (NestJS) ou Python (Django) | PostgreSQL + Redis | Stripe Connect com authorization/capture | Redis para locks de reserva (evitar double-booking). Pricing engine para sazonalidade. |
| V4 — B2B/Procurement | Next.js ou React | Java (Spring) ou .NET | PostgreSQL | Boleto + Pix (Pagar.me, Asaas) | Workflow de cotação e aprovação é core. Integração com sistemas ERP e NF-e obrigatória. |
| V5 — Conteúdo Digital | Next.js | Node.js (NestJS) | PostgreSQL + S3/R2 | Stripe ou Hotmart (se cursos) | CDN para delivery de assets. Signed URLs para proteção de downloads. Streaming para vídeo. |

---

## Etapa 01 — Inception

- **Modelo de negócio e monetização**: O modelo de receita de um marketplace define toda a arquitetura financeira. As opções principais são: comissão por transação (percentual fixo ou variável sobre cada venda), assinatura do seller (mensalidade para listar na plataforma), listing fee (cobrança por anúncio publicado), featured listing (destaque pago), e combinações destes. A escolha impacta diretamente a complexidade do split de pagamento, a estratégia de cold start (sellers pagam antes de vender?), e o breakeven da plataforma. Se o modelo não está definido, todas as decisões técnicas subsequentes estão suspensas.

- **Cold start problem**: Todo marketplace enfrenta o dilema do ovo e da galinha — sem oferta, os compradores não vêm; sem compradores, os sellers não investem tempo listando produtos. A estratégia de cold start deve ser discutida na Inception porque impacta o MVP: começar pelo lado da oferta (recrutar sellers manualmente, oferecer comissão zero nos primeiros meses, fazer curadoria do catálogo inicial) ou pelo lado da demanda (garantir tráfego inicial via marketing, parcerias, ou base existente de clientes). Se o cliente não tem estratégia de cold start, o marketplace vai ser lançado vazio e morrer vazio.

- **Regulamentação e compliance**: Marketplaces têm obrigações legais específicas que variam por setor. Split de pagamento exige que a plataforma seja registrada como subcredenciador (ou use um PSP que faz o split — Stripe Connect, Pagar.me Split, Zoop). O marketplace é responsável solidário pela qualidade do produto ou serviço em muitos cenários (CDC art. 18). Dados de sellers e buyers estão sujeitos à LGPD. Se o marketplace opera com alimentos, saúde, educação ou serviços financeiros, há regulamentações setoriais específicas (Anvisa, MEC, Bacen). Essas obrigações precisam ser identificadas aqui porque afetam escopo, custo e prazo de forma significativa.

- **Stakeholders e papéis da plataforma**: Mapear todos os lados do marketplace — não são apenas "vendedor" e "comprador". Frequentemente existem: seller (quem lista e vende), buyer (quem compra), operador da plataforma (curadoria, suporte, moderação), parceiro logístico (transportadora, motoboy), e parceiro financeiro (gateway, banco). Cada lado tem necessidades, interfaces e fluxos diferentes. Se o entrevistador mapear apenas dois lados, vai descobrir o terceiro durante o build — e terceiros lados adicionam interfaces e regras que não estavam no escopo.

- **Escopo geográfico e logístico**: A cobertura geográfica do marketplace define requisitos de logística, tributação e localização. Um marketplace local (mesma cidade) pode usar entrega própria ou parceiro local. Um marketplace nacional precisa de integração com transportadoras (Correios, Jadlog, Loggi), cálculo de frete por CEP, e gestão de múltiplos prazos de entrega. Um marketplace internacional adiciona complexidade tributária (impostos de importação), múltiplas moedas, e compliance em múltiplas jurisdições. Começar local e expandir gradualmente é o caminho mais seguro — mas a arquitetura precisa contemplar a expansão desde o início para não exigir rewrite.

- **Diferencial competitivo e proposta de valor**: O mercado de marketplaces é maduro e competitivo. O cliente precisa responder: por que um seller listaria aqui em vez de no Mercado Livre? Por que um buyer compraria aqui em vez de na Amazon? Se a resposta é "preço mais baixo" ou "interface mais bonita", o marketplace provavelmente vai fracassar. Diferenciais reais são: nicho específico que as grandes plataformas não atendem bem, curadoria de qualidade que as plataformas genéricas não fazem, comunidade estabelecida que se transfere para a plataforma, ou modelo de negócio inovador que resolve uma dor real não atendida.

### Perguntas

1. Qual é o modelo de monetização da plataforma — comissão por transação, assinatura do seller, listing fee, ou combinação? [fonte: Diretoria, Financeiro, Comercial] [impacto: Arquiteto, Dev, PM]
2. Qual é a estratégia de cold start — como atrair a primeira base de sellers e de buyers antes do efeito de rede? [fonte: Diretoria, Marketing, Comercial] [impacto: PM, Marketing, Dev]
3. O marketplace envolve produto físico com logística, serviço, aluguel, ou conteúdo digital? [fonte: Diretoria] [impacto: Arquiteto, Dev, PM]
4. Quem são todos os lados da plataforma (seller, buyer, operador, parceiro logístico, parceiro financeiro)? [fonte: Diretoria, Comercial, Operações] [impacto: PM, Dev, Designer]
5. Qual é o escopo geográfico inicial e o plano de expansão (local, nacional, internacional)? [fonte: Diretoria, Comercial] [impacto: Arquiteto, Dev, DevOps]
6. Existe regulamentação setorial específica que afeta o marketplace (Anvisa, MEC, Bacen, CDC)? [fonte: Jurídico, Compliance, Diretoria] [impacto: PM, Arquiteto, Dev]
7. Qual é o diferencial competitivo em relação a marketplaces existentes no mesmo nicho? [fonte: Diretoria, Comercial, Marketing] [impacto: PM, Designer]
8. O cliente já tem uma base existente de sellers ou buyers que pode ser migrada para a plataforma? [fonte: Comercial, Diretoria] [impacto: PM, Dev, Marketing]
9. Qual é o orçamento total aprovado, separando desenvolvimento, operação mensal e marketing de aquisição? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
10. Qual é o prazo esperado para o MVP e existe data de negócio que o justifica (evento, sazonalidade, investimento)? [fonte: Diretoria] [impacto: PM, Dev]
11. O split de pagamento será gerenciado por PSP com split nativo (Stripe Connect, Pagar.me) ou solução própria? [fonte: Financeiro, TI, Diretoria] [impacto: Arquiteto, Dev]
12. Quem toma decisões de produto — existe um Product Owner definido com autoridade para priorizar? [fonte: Diretoria] [impacto: PM]
13. Existe expectativa de app mobile nativo ou o MVP será web responsivo? [fonte: Diretoria, Comercial, Marketing] [impacto: Arquiteto, Dev, Designer]
14. Qual é o ticket médio esperado e o volume de transações projetado para os primeiros 6 meses? [fonte: Financeiro, Comercial] [impacto: Arquiteto, Dev, PM]
15. O cliente tem experiência prévia operando marketplace ou plataforma digital, ou é a primeira vez? [fonte: Diretoria] [impacto: PM]

---

## Etapa 02 — Discovery

- **Jornada completa de cada lado**: Mapear a jornada de ponta a ponta para cada participante da plataforma. Para o seller: cadastro → verificação → criação de catálogo → recebimento de pedido → processamento → envio → recebimento de pagamento → gestão de disputas. Para o buyer: busca → comparação → carrinho → checkout → pagamento → rastreamento → recebimento → avaliação → devolução. Para o operador: aprovação de sellers → moderação de catálogo → gestão de disputas → relatórios → payouts. Cada etapa da jornada tem requisitos de interface, regras de negócio e integrações próprias — pular uma é garantir retrabalho.

- **Política de comissão e split**: Detalhar o modelo de split de pagamento — percentual da plataforma (fixo ou variável por categoria?), quando o seller recebe (após entrega confirmada? D+14?), como são tratados reembolsos (quem perde a comissão?), e qual o minimum payout (valor mínimo para transferência ao seller). O PSP escolhido (Stripe Connect, Pagar.me Split, Zoop, iugu) define as possibilidades técnicas — nem todos suportam split em D+X variável ou multiple receivers. A complexidade financeira de marketplace é frequentemente subestimada porque parece "só um percentual", mas envolve conciliação, chargebacks, e retenções.

- **Sistema de reputação e confiança**: Em marketplaces, a confiança é o ativo mais valioso — e o mais difícil de construir. Definir como a reputação é calculada: avaliação por estrelas (1-5), review textual, taxa de resposta, taxa de entrega no prazo, taxa de disputa. Definir consequências da reputação baixa: aviso, redução de visibilidade, suspensão, banimento. Definir como prevenir manipulação: avaliações verificadas (apenas de compradores reais), detecção de avaliações falsas (mesmo IP, padrão de texto), e resposta do seller às avaliações. Um marketplace sem sistema de reputação confiável não escala — o buyer não confia, o seller sério desiste.

- **Gestão de catálogo**: Definir o modelo de catálogo — quem cria as listagens (seller livre, ou curadoria da plataforma?), quais campos são obrigatórios (título, descrição, preço, fotos, categoria, condição), como são tratadas variações (tamanho, cor, modelo — cada variação com estoque e preço próprio?), e como é feita a moderação (aprovação manual antes de publicar, ou publicação automática com moderação reativa). Para marketplace de produtos, o catálogo é a experiência principal do buyer — um catálogo bagunçado com fotos ruins e descrições inconsistentes mata a confiança antes do primeiro pedido.

- **Fluxo de pagamento e financial engine**: Mapear o fluxo financeiro completo — do momento em que o buyer paga até o momento em que o seller recebe. Pontos de atenção: captura imediata vs. autorização com captura posterior (essencial para reservas e serviços), escrow (retenção do valor até confirmação de entrega), split automático vs. manual, chargebacks (quem absorve? plataforma ou seller?), e reconciliação (como o seller vê o extrato de ganhos). Marketplace que não resolve o fluxo financeiro com clareza perde sellers — porque ninguém quer vender sem saber quando e quanto vai receber.

- **Busca e descoberta**: Para marketplaces com catálogo, a busca é a feature mais crítica para conversão. Requisitos típicos: busca textual com relevância (não apenas match exato), filtros por categoria, preço, localização, avaliação e atributos específicos, ordenação por relevância, preço, mais vendidos e mais recentes, e sugestões de busca (autocomplete). Se o catálogo terá mais de 1.000 itens, Elasticsearch ou Algolia são praticamente obrigatórios — busca em banco relacional não escala em relevância nem em performance. A qualidade da busca define diretamente a taxa de conversão.

### Perguntas

1. A jornada completa de cada lado da plataforma (seller, buyer, operador) foi mapeada passo a passo? [fonte: Comercial, Operações, Diretoria] [impacto: PM, Dev, Designer]
2. O modelo de comissão e split foi detalhado — percentual, timing de repasse, tratamento de reembolsos e minimum payout? [fonte: Financeiro, Diretoria] [impacto: Dev, Arquiteto]
3. O sistema de reputação foi especificado — como é calculado, quais as consequências, como evitar manipulação? [fonte: Comercial, Diretoria, Operações] [impacto: Dev, PM]
4. O modelo de catálogo foi definido — quem cria, quais campos, como moderação funciona, variações de produto? [fonte: Comercial, Operações] [impacto: Dev, Designer]
5. O fluxo financeiro completo foi mapeado — da cobrança ao payout, incluindo escrow, chargeback e reconciliação? [fonte: Financeiro, Diretoria] [impacto: Arquiteto, Dev]
6. Os requisitos de busca e descoberta foram definidos — filtros, ordenação, autocomplete, relevância? [fonte: Comercial, Marketing] [impacto: Dev, Arquiteto]
7. A política de disputas e reembolsos foi definida — quem media, quais os prazos, quem absorve o custo? [fonte: Jurídico, Comercial, Diretoria] [impacto: Dev, PM]
8. Os requisitos de verificação de seller foram definidos — documentação, identidade, endereço, conta bancária? [fonte: Compliance, Jurídico, Comercial] [impacto: Dev, PM]
9. A estratégia de logística (se produto físico) foi definida — integração com transportadoras, cálculo de frete, rastreamento? [fonte: Operações, Logística, Comercial] [impacto: Dev, Arquiteto]
10. O volume esperado de sellers e listings no MVP e em 12 meses foi estimado para dimensionar a infraestrutura? [fonte: Comercial, Diretoria] [impacto: Arquiteto, Dev, DevOps]
11. Os requisitos de LGPD foram mapeados — dados de sellers e buyers, consentimento, portabilidade, exclusão? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, Arquiteto]
12. A política de conteúdo proibido foi definida — quais produtos/serviços não podem ser listados? [fonte: Jurídico, Compliance, Diretoria] [impacto: Dev, Operações]
13. Os canais de comunicação entre seller e buyer foram definidos — chat interno, e-mail, telefone? [fonte: Comercial, Diretoria] [impacto: Dev]
14. Os KPIs de sucesso do marketplace foram definidos — GMV, take rate, NPS de seller, NPS de buyer, retenção? [fonte: Diretoria, Comercial, Financeiro] [impacto: PM, Dev]
15. A estratégia de marketing e aquisição de sellers e buyers foi planejada com orçamento e responsável definidos? [fonte: Marketing, Diretoria, Financeiro] [impacto: PM, Marketing]

---

## Etapa 03 — Alignment

- **Escopo do MVP por lado**: Alinhar o que cada lado da plataforma terá no MVP. O erro mais comum é construir o MVP completo para o buyer mas esquecer o lado do seller — que precisa de painel para gestão de catálogo, pedidos, financeiro e comunicação. Ou construir experiência perfeita para ambos mas sem o painel de operações que a plataforma precisa para moderar, resolver disputas e acompanhar métricas. Cada lado cortado do MVP é um lado que operará manualmente — o que é aceitável com 20 sellers mas inviável com 200.

- **PSP e modelo de split alinhados**: A escolha do PSP (Payment Service Provider) para split de pagamento deve estar fechada antes da Architecture, porque cada PSP tem APIs, fluxos e limitações diferentes. Stripe Connect é o mais completo para marketplaces globais mas tem complexidade de onboarding do seller (KYC). Pagar.me Split é a melhor opção Brasil-nativa com Pix e boleto. Zoop é indicado para quem quer white-label. Se o cliente quer Pix como método principal (e no Brasil quase sempre quer), verificar que o PSP suporta Pix com split automático — nem todos suportam.

- **Termos de uso e contratos**: Marketplace é uma relação tripartite (plataforma-seller-buyer) que exige termos de uso robustos — termos gerais da plataforma, termos de adesão do seller (comissão, obrigações, penalidades), e política de privacidade. Esses documentos devem ser redigidos por advogado especializado em direito digital antes do go-live — não por template genérico da internet. O fluxo de aceite dos termos deve ser implementado no sistema (checkbox obrigatório com versionamento — se os termos mudam, o seller precisa re-aceitar). Marketplace sem termos adequados é bomba jurídica com prazo de validade.

- **Decisão sobre app mobile**: Marketplaces de serviços e de produtos com logística quase sempre precisam de notificações push em tempo real — novo pedido, pedido aceito, entregador a caminho, pagamento recebido. Web push resolve parcialmente, mas a experiência é inferior a push nativo. A decisão entre web responsivo (MVP mais rápido), PWA (push em Android, limitado no iOS), e app nativo (melhor experiência, maior custo) deve ser tomada aqui porque impacta a arquitetura (API-first é obrigatório se app nativo está no roadmap) e o orçamento (app nativo dobra ou triplica o custo de frontend).

- **Política de onboarding de seller**: Definir o fluxo de aprovação de sellers — cadastro livre (qualquer um publica) vs. curadoria (aprovação manual pela equipe da plataforma). Sellers não verificados geram risco de fraude, produtos ilegais, e perda de confiança. Sellers com processo de aprovação longo geram atrito de onboarding e perda de adesão. O equilíbrio depende do nicho: marketplace de freelancers pode ter cadastro aberto com verificação posterior, marketplace de alimentos precisa de verificação antes da primeira listagem por requisitos sanitários.

### Perguntas

1. O escopo do MVP foi definido para cada lado da plataforma — seller, buyer, operador — com critério de corte? [fonte: Diretoria, Comercial, PM] [impacto: PM, Dev]
2. O PSP para split de pagamento foi escolhido e validado tecnicamente (suporta Pix, split, escrow, payout)? [fonte: Financeiro, TI, Diretoria] [impacto: Arquiteto, Dev]
3. Os termos de uso, termos do seller e política de privacidade foram redigidos por advogado especializado? [fonte: Jurídico] [impacto: PM, Dev]
4. A decisão entre web responsivo, PWA e app nativo foi tomada com base em necessidade de push e orçamento? [fonte: Diretoria, Comercial, TI] [impacto: Arquiteto, Dev, Designer]
5. A política de onboarding de seller foi definida — cadastro livre, curadoria manual, ou verificação automática? [fonte: Comercial, Compliance, Diretoria] [impacto: Dev, PM, Operações]
6. O fluxo de disputas entre seller e buyer foi desenhado — quem media, prazos, escalação, e decisão final? [fonte: Jurídico, Comercial, Diretoria] [impacto: Dev, PM, Operações]
7. O modelo de categorias e taxonomia do catálogo foi definido e validado com sellers potenciais? [fonte: Comercial, Operações] [impacto: Dev, Designer]
8. O SLA de suporte ao seller e ao buyer foi definido (tempo de resposta, canais, horário de atendimento)? [fonte: Diretoria, Operações] [impacto: PM, Operações]
9. O time de operações do marketplace (curadoria, suporte, moderação) foi dimensionado e orçado? [fonte: Diretoria, Financeiro, RH] [impacto: PM]
10. O design foi entregue cobrindo os fluxos de seller, buyer e operador com estados de vazio, erro e loading? [fonte: Designer] [impacto: Dev]
11. A estratégia de comunicação seller-buyer foi definida — chat interno com moderação ou contato direto? [fonte: Comercial, Jurídico, Diretoria] [impacto: Dev]
12. O modelo de manutenção e evolução pós-lançamento foi formalizado (time dedicado, roadmap, budget)? [fonte: Diretoria, Financeiro] [impacto: PM, Dev]
13. Os meios de pagamento do MVP foram definidos — cartão, Pix, boleto, combinações? [fonte: Financeiro, Comercial, Diretoria] [impacto: Dev, Arquiteto]
14. O processo de onboarding de buyers (cadastro, verificação de e-mail, primeiro pedido) foi desenhado? [fonte: Comercial, Marketing, Designer] [impacto: Dev, Designer]
15. O cliente entende que marketplace é operação contínua — e não projeto com data de fim? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Modelo de dados do catálogo**: Definir a estrutura de dados do catálogo com atenção a: hierarquia de categorias (até quantos níveis?), atributos por categoria (tamanho em roupas, quilometragem em carros, carga horária em cursos), variações de produto (SKU por combinação de atributos, cada variação com preço e estoque próprios), imagens (número mínimo/máximo, dimensões, formato), e campos de SEO (slug, meta description, tags). O modelo de catálogo é o asset mais importante do marketplace — se mal modelado, a busca não funciona, os filtros são inúteis, e os sellers não conseguem listar corretamente.

- **Fluxo de pedido state machine**: Modelar o ciclo de vida completo de um pedido como state machine formal — cada estado (pendente, pago, confirmado pelo seller, em separação, enviado, entregue, concluído, cancelado, em disputa) com suas transições permitidas, quem pode executar cada transição, e as ações automáticas associadas (notificação, atualização de estoque, liberação de pagamento, cálculo de comissão). Pedidos em marketplace são mais complexos que em e-commerce simples porque envolvem dois lados: o seller confirma, o buyer pode cancelar, o entregador atualiza status, e a plataforma media tudo.

- **Regras financeiras detalhadas**: Documentar cada regra do financial engine — cálculo de comissão (percentual fixo ou variável por categoria?), timing de payout (D+14 após entrega? D+30?), tratamento de reembolso parcial e total (quem paga a comissão? a taxa de gateway?), minimum payout, and taxa de saque (se houver). Cada cenário financeiro precisa de exemplo numérico: "Buyer paga R$ 100, taxa de gateway R$ 3,50, comissão da plataforma 15% (R$ 15), seller recebe R$ 81,50 em D+14 após confirmação de entrega". Sem exemplos numéricos, o dev vai implementar errado e o seller vai reclamar.

- **Especificação de busca e filtros**: Definir a experiência de busca com nível de detalhe técnico — quais campos são buscáveis (título, descrição, tags, nome do seller), quais filtros estão disponíveis (categoria, faixa de preço, localização, avaliação, frete grátis), quais ordenações são suportadas (relevância, menor preço, maior preço, mais vendidos, mais recentes), e como funciona o autocomplete (por produto, por categoria, por seller). Para cada filtro, definir se é single-select ou multi-select, se os contadores são dinâmicos (atualizam conforme outros filtros são aplicados), e se há filtros dependentes (subcategoria muda conforme categoria selecionada).

- **Painel do seller**: Especificar o painel administrativo do seller com todas as funcionalidades — gestão de catálogo (criar, editar, pausar, excluir listagens), gestão de pedidos (visualizar, confirmar, imprimir etiqueta, informar rastreamento), financeiro (extrato, payout pendente, histórico de recebimentos), comunicação (mensagens com buyers, notificações da plataforma), e métricas (visualizações, conversão, avaliação). O painel do seller é frequentemente negligenciado no MVP — o resultado é sellers gerenciando por planilha e WhatsApp, o que não escala.

- **Painel de operações da plataforma**: Especificar as funcionalidades do operador da plataforma — aprovação de sellers, moderação de catálogo (produtos proibidos, fotos inadequadas, descrições falsas), gestão de disputas (evidências de ambos os lados, decisão, reembolso), relatórios operacionais (GMV, take rate, sellers ativos, buyers ativos, taxa de disputa), e configurações (percentual de comissão, categorias, featured listings). O painel de operações é o que permite que o marketplace funcione como negócio — sem ele, cada operação exige acesso ao banco de dados.

### Perguntas

1. O modelo de dados do catálogo foi definido com categorias, atributos por categoria, variações, imagens e SEO? [fonte: Comercial, Operações] [impacto: Dev, Designer, Arquiteto]
2. O fluxo de pedido foi modelado como state machine com todos os estados, transições, permissões e ações automáticas? [fonte: Comercial, Operações, Financeiro] [impacto: Dev, Arquiteto]
3. As regras financeiras foram documentadas com exemplos numéricos para cada cenário (venda, reembolso, chargeback)? [fonte: Financeiro, Diretoria] [impacto: Dev, Arquiteto]
4. A experiência de busca e filtros foi especificada com campos buscáveis, filtros, ordenações e autocomplete? [fonte: Comercial, Marketing, Designer] [impacto: Dev, Arquiteto]
5. O painel do seller foi especificado com todas as funcionalidades — catálogo, pedidos, financeiro, comunicação, métricas? [fonte: Comercial, Operações] [impacto: Dev, Designer]
6. O painel de operações foi especificado — aprovação, moderação, disputas, relatórios, configurações? [fonte: Operações, Diretoria] [impacto: Dev, Designer]
7. O fluxo de cadastro e verificação do seller (KYC) foi detalhado — documentos, validação, prazos, automação? [fonte: Compliance, Jurídico, Comercial] [impacto: Dev, PM]
8. A política de frete (se produto físico) foi especificada — cálculo, responsável pelo envio, rastreamento, devolução? [fonte: Operações, Logística, Comercial] [impacto: Dev, Arquiteto]
9. O sistema de avaliações e reviews foi especificado — campos, moderação, resposta do seller, cálculo de rating? [fonte: Comercial, Operações] [impacto: Dev]
10. Os wireframes cobrem os fluxos de seller, buyer e operador com estados de vazio, erro e edge cases? [fonte: Designer] [impacto: Dev, Designer]
11. O modelo de notificações foi definido — quais eventos disparam notificação, para quem, por qual canal? [fonte: Comercial, Operações] [impacto: Dev]
12. Os requisitos de performance foram definidos — tempo de busca, tempo de checkout, throughput de pedidos simultâneos? [fonte: TI, Comercial] [impacto: Arquiteto, Dev]
13. A política de cancelamento foi detalhada — quem pode cancelar, em qual estado, com ou sem penalidade? [fonte: Jurídico, Comercial] [impacto: Dev]
14. O esquema de dados estruturados (Schema.org Product, Offer, Review) foi mapeado para SEO de catálogo? [fonte: Marketing, Agência de SEO] [impacto: Dev, SEO]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders (negócio, financeiro, jurídico)? [fonte: Diretoria] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Search engine**: Para marketplaces com mais de 1.000 listagens, busca em banco relacional (LIKE + filtros SQL) não escala em performance nem em relevância. Elasticsearch é o padrão de mercado — suporta full-text search com ranking por relevância, faceted filters com contadores dinâmicos, autocomplete com fuzzy matching, e geo-search (filtro por distância). Algolia é alternativa managed (zero infra) com experiência de busca excelente, mas custo elevado em volume alto. Meilisearch é opção open-source mais leve para volumes menores. A escolha deve considerar volume de catálogo, complexidade dos filtros, e budget para infraestrutura.

- **Payment engine com split**: A arquitetura financeira de marketplace tem complexidade própria. O PSP com split nativo (Stripe Connect, Pagar.me Split) resolve: cobrança do buyer, retenção em escrow, split automático (plataforma recebe comissão, seller recebe o resto), e payout programado para o seller. Para cenários complexos (split em mais de 2 partes — ex.: plataforma + seller + parceiro logístico), verificar que o PSP suporta multiple receivers. A tabela de comissões variáveis por categoria exige lógica no backend que calcula o split antes de enviar para o PSP — o PSP executa, não decide.

- **Arquitetura de catálogo e indexação**: O catálogo vive em duas camadas — banco de dados relacional (PostgreSQL) como source of truth, e search engine (Elasticsearch) como índice de busca. Toda escrita (criar, editar, excluir produto) vai para o banco, e um pipeline de indexação (síncrono via evento ou assíncrono via fila) replica para o search engine. A consistência eventual entre as duas camadas é aceitável (seller edita produto, busca reflete em 1-2 segundos) desde que o painel do seller sempre leia do banco (dados sempre atualizados). O pipeline de indexação deve tratar falhas (retry, dead letter queue) e suportar re-indexação completa sem downtime (rebuild do índice inteiro quando o schema do Elasticsearch muda).

- **Infraestrutura e escalabilidade**: Marketplace tem padrões de tráfego previsíveis (pico em horário comercial, queda à noite) e imprevisíveis (promoção viral, featured listing que viraliza). A infra deve suportar auto-scaling — containers (Docker + ECS/EKS ou Cloud Run) com scaling baseado em CPU/request count. O banco de dados é frequentemente o gargalo: read replicas para queries pesadas (busca, relatórios), connection pooling (PgBouncer), e separação de reads e writes (CQRS leve). Cache (Redis) é obrigatório para: sessões, catálogo de categorias, dados de seller que mudam raramente, e rate limiting.

- **CDN e performance de catálogo**: Imagens de catálogo são o maior volume de dados em marketplace de produtos — centenas de milhares de imagens que precisam ser servidas rapidamente em múltiplos tamanhos (thumbnail, lista, detalhe, zoom). Cloudinary ou imgix para transformação on-the-fly (resize, crop, format conversion para WebP/AVIF) com CDN global são o padrão. Se o orçamento é restrito, Cloudflare Images ou S3 + CloudFront com Lambda@Edge para transformação resolvem com menor custo. O pipeline de upload do seller deve validar (formato, tamanho, resolução mínima) e processar (otimizar, gerar thumbnails) automaticamente.

- **Messaging e notificações em tempo real**: Marketplace precisa de canal de comunicação entre seller e buyer (para dúvidas pré-compra, negociação, pós-venda) e de notificações em tempo real (novo pedido para o seller, atualização de status para o buyer). Para chat, opções: implementação própria com WebSocket (Socket.io, Ably) para controle total, ou serviço managed (Stream, SendBird) para velocidade de implementação. Para notificações: push via Firebase Cloud Messaging (Android + web), APNs (iOS), e-mail transacional (Resend, SendGrid), e notificações in-app (badge + lista). Cada canal tem particularidades de entrega e fallback — e-mail é o mais confiável, push é o mais imediato.

### Perguntas

1. O search engine foi escolhido (Elasticsearch, Algolia, Meilisearch) com base em volume de catálogo e complexidade de filtros? [fonte: TI, Arquiteto] [impacto: Dev, Arquiteto]
2. O PSP para split foi validado tecnicamente — suporta todos os cenários financeiros definidos (escrow, multi-split, Pix)? [fonte: Financeiro, TI] [impacto: Dev, Arquiteto]
3. A arquitetura de catálogo (banco + search engine + pipeline de indexação) foi desenhada com tratamento de falhas? [fonte: Arquiteto] [impacto: Dev]
4. A infra suporta auto-scaling e os gargalos de banco foram endereçados (read replicas, connection pooling)? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
5. O pipeline de imagens (upload, validação, otimização, CDN) foi desenhado com Cloudinary, imgix ou solução equivalente? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
6. A solução de messaging (chat, notificações, push) foi escolhida — própria ou serviço managed? [fonte: Arquiteto, TI, Financeiro] [impacto: Dev]
7. A integração com transportadoras (se produto físico) foi especificada — API de cotação, etiqueta, rastreamento? [fonte: Operações, Logística, TI] [impacto: Dev, Arquiteto]
8. A estratégia de cache (Redis) foi definida para sessões, catálogo, rate limiting e dados de referência? [fonte: Arquiteto] [impacto: Dev]
9. O pipeline de CI/CD foi desenhado com ambientes separados, deploy preview, e aprovação para produção? [fonte: TI, Dev] [impacto: DevOps, Dev]
10. A segurança foi planejada — rate limiting, proteção contra scraping de catálogo, WAF, e prevenção de fraude? [fonte: Segurança, TI, Arquiteto] [impacto: Dev, DevOps]
11. Os custos mensais de operação foram calculados (infra, PSP, search engine, CDN, messaging) em cenário atual e projetado? [fonte: Financeiro, TI] [impacto: PM, Arquiteto]
12. A estratégia de SEO técnico foi definida — SSR/SSG para páginas de catálogo, sitemap dinâmico, dados estruturados? [fonte: Marketing, Arquiteto] [impacto: Dev, SEO]
13. A arquitetura suporta o roadmap futuro (app nativo, múltiplas regiões, novos meios de pagamento) sem rewrite? [fonte: Diretoria, Arquiteto] [impacto: Arquiteto, Dev]
14. O monitoramento de aplicação (logs, métricas, alertas, APM) foi planejado com ferramentas e thresholds? [fonte: DevOps, TI] [impacto: DevOps, Dev]
15. A documentação de arquitetura foi revisada e aprovada pelo time técnico e pelo sponsor? [fonte: TI, Diretoria] [impacto: Arquiteto, PM]

---

## Etapa 06 — Setup

- **Ambiente de desenvolvimento com serviços de dependência**: Configurar Docker Compose com: banco PostgreSQL, Elasticsearch (ou search engine escolhido), Redis, e mock dos serviços externos (PSP sandbox, API de transportadora sandbox). O dev deve conseguir subir todo o ecossistema localmente em um único comando. Serviços externos devem usar sandbox/test mode com API keys de teste — nunca apontar para produção durante desenvolvimento. Documentar em README com instruções passo a passo testadas por alguém de fora do time.

- **Configuração do PSP**: Criar conta no PSP escolhido, configurar webhooks (notificações de pagamento, chargeback, payout), criar o marketplace account (no Stripe Connect, é o connected account), e testar o fluxo completo em sandbox: buyer paga → escrow retém → seller confirma entrega → split é executado → seller recebe payout. O fluxo em sandbox deve funcionar perfeitamente antes de qualquer código de build — bugs de integração financeira descobertos durante o build geram atrasos desproporcionais porque dependem de suporte do PSP para debug.

- **Setup do search engine**: Configurar o Elasticsearch (ou alternativa) com: índices definidos (products, sellers, categories), mappings com tipos corretos (keyword vs. text, geo_point para localização), analyzers para português (stemming, stop words, sinônimos), e pipeline de indexação inicial. Testar busca com dados de seed para validar que a relevância faz sentido — "camiseta azul" deve retornar camisetas azuis, não qualquer produto que tenha a palavra "azul" na descrição de forma irrelevante.

- **Ambientes de staging e produção**: Provisionar staging com configuração idêntica a produção — mesmo search engine, mesmo PSP (em sandbox mode), mesma CDN, mesmo cache. O ambiente de staging é onde o fluxo financeiro será testado end-to-end com cartões de teste antes do go-live. A divergência entre staging e produção em marketplace é especialmente perigosa porque envolve dinheiro real — um bug financeiro que passa em staging e aparece em produção resulta em sellers recebendo valor errado ou buyers sendo cobrados incorretamente.

- **Seed de dados para marketplace**: Criar seed com dados que simulam um marketplace em operação — pelo menos 5 sellers com perfis diferentes (novo, verificado, com avaliações), 50+ produtos distribuídos em categorias com variações, 20+ pedidos em diferentes estados (pendente, pago, enviado, entregue, em disputa), e 30+ avaliações. O seed deve permitir testar: busca com filtros (há resultados para filtrar), painel do seller (há pedidos para gerenciar), painel do operador (há disputas para resolver), e dashboard (há dados para visualizar). Marketplace vazio é impossível de testar.

- **Configuração de domínio e SSL**: Registrar ou configurar o domínio principal, subdomínios (seller.plataforma.com ou plataforma.com/seller, api.plataforma.com), SSL para todos os domínios, e CDN para assets estáticos e imagens de catálogo. Marketplace que processa pagamento DEVE ter SSL — PSPs exigem HTTPS para webhooks e o PCI DSS exige criptografia de dados em trânsito. Configurar com antecedência para que o domínio esteja estável no go-live.

### Perguntas

1. O ambiente de desenvolvimento local com todos os serviços (banco, search, cache, PSP sandbox) sobe em um único comando? [fonte: Dev] [impacto: Dev]
2. A conta do PSP foi criada, webhooks configurados e o fluxo completo testado em sandbox (pagamento → split → payout)? [fonte: Dev, Financeiro] [impacto: Dev, Arquiteto]
3. O search engine foi configurado com índices, mappings, analyzers para português e pipeline de indexação? [fonte: Dev, Arquiteto] [impacto: Dev]
4. Os ambientes de staging e produção estão provisionados com configuração idêntica e isolamento completo? [fonte: DevOps, TI] [impacto: Dev, DevOps]
5. O seed de dados cria um marketplace funcional com sellers, produtos, pedidos, avaliações e disputas? [fonte: Dev] [impacto: Dev, QA]
6. O domínio, subdomínios e SSL estão configurados e funcionando em staging? [fonte: TI, DevOps] [impacto: DevOps, Dev]
7. As variáveis de ambiente estão documentadas e configuradas separadamente por ambiente (dev, staging, prod)? [fonte: Dev] [impacto: Dev, DevOps]
8. O pipeline de CI/CD está configurado com lint, testes, build e deploy automático por ambiente? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
9. O CDN para imagens de catálogo está configurado com pipeline de transformação (resize, WebP/AVIF)? [fonte: Dev, DevOps] [impacto: Dev]
10. Os webhooks do PSP estão configurados para staging e produção com URLs corretas e verificação de assinatura? [fonte: Dev] [impacto: Dev, Segurança]
11. O processo de onboarding de seller em sandbox foi testado end-to-end (cadastro → verificação → listagem → venda)? [fonte: Dev, Comercial] [impacto: Dev, PM]
12. O README do projeto documenta setup local, arquitetura, e convenções de código? [fonte: Dev] [impacto: Dev]
13. Os acessos a APIs de terceiros (transportadoras, CEP, validação de documento) foram obtidos com contas de teste? [fonte: Dev, TI] [impacto: Dev]
14. O .gitignore exclui secrets, .env, e arquivos gerados, e não há credenciais no histórico do repositório? [fonte: Dev, Segurança] [impacto: Dev, Segurança]
15. O monitoramento básico (error tracking, uptime, log aggregation) está configurado em staging? [fonte: DevOps] [impacto: DevOps, Dev]

---

## Etapa 07 — Build

- **Cadastro e verificação de seller (KYC)**: Implementar o fluxo de onboarding do seller — cadastro com dados pessoais/empresariais, upload de documentos (CPF/CNPJ, comprovante de endereço, dados bancários), verificação automática (validação de CPF/CNPJ via API, verificação de conta bancária) ou manual (operador revisa documentos), e ativação da conta para começar a vender. O KYC é requisito regulatório para split de pagamento — o PSP exige que o connected account (seller) esteja verificado antes de receber payouts. Fluxo de KYC mal implementado gera: sellers abandonando o cadastro por excesso de burocracia, ou sellers fraudulentos passando pela verificação por falta de rigor.

- **Catálogo e busca**: Implementar o CRUD de catálogo no painel do seller (criar, editar, pausar, excluir listagens com variações, imagens e atributos por categoria), o pipeline de indexação para o search engine (cada mudança no catálogo reflete na busca em segundos), e a experiência de busca e navegação no lado do buyer (busca textual, filtros facetados, ordenação, paginação, autocomplete). A qualidade da busca é o fator mais importante de conversão em marketplace — cada melhoria de relevância se traduz diretamente em GMV. Testar com volume real de catálogo (não 5 produtos de teste) para validar performance e relevância.

- **Checkout e payment engine**: Implementar o fluxo de checkout — carrinho (com itens de múltiplos sellers se aplicável), cálculo de frete (por seller, com cotação em tempo real via API de transportadora), seleção de meio de pagamento (cartão, Pix, boleto), integração com PSP para cobrança, split automático, e confirmação de pedido com notificação para seller e buyer. O checkout é a feature mais crítica do marketplace — qualquer falha aqui (timeout do PSP, cálculo de frete errado, split incorreto) resulta em perda de receita direta. Implementar com testes automatizados para cada cenário: pagamento aprovado, negado, Pix expirado, boleto vencido.

- **Gestão de pedidos e fulfillment**: Implementar o ciclo de vida do pedido conforme a state machine definida — seller confirma pedido, imprime etiqueta, informa código de rastreamento, buyer acompanha entrega, buyer confirma recebimento (ou confirmação automática após X dias), e plataforma libera pagamento ao seller. Cada transição de estado dispara notificações, atualiza dashboards, e pode disparar ações financeiras (reembolso em cancelamento, split em conclusão). Implementar também os fluxos de exceção: seller não confirma em 48h (cancelamento automático), buyer reclama de produto diferente do anunciado (abertura de disputa).

- **Sistema de avaliações**: Implementar avaliações de buyer para seller — rating (1-5 estrelas), review textual, upload de fotos do produto recebido, e exibição no perfil do seller e na página do produto. Implementar moderação (filtrar linguagem ofensiva, detectar avaliações falsas) e resposta do seller à avaliação. O rating agregado do seller deve ser calculado de forma ponderada (avaliações recentes têm mais peso) e exibido em todos os contextos onde o seller aparece (listagem, busca, perfil). Avaliações verificadas (apenas de compradores que realmente compraram) têm mais credibilidade que avaliações abertas.

- **Painel de operações**: Implementar as ferramentas do operador da plataforma — dashboard de KPIs (GMV, número de transações, sellers ativos, buyers ativos, taxa de disputa), moderação de catálogo (fila de produtos para revisão com aprovação/rejeição), gestão de disputas (visualização de evidências, comunicação com ambos os lados, decisão e execução de reembolso), gestão de sellers (aprovação, suspensão, banimento), e configurações (comissões, categorias, featured listings). O painel de operações transforma dados em ações — sem ele, operar o marketplace exige acesso direto ao banco de dados e execução manual de queries.

### Perguntas

1. O fluxo de cadastro e KYC do seller está implementado com verificação de documentos e ativação da conta? [fonte: Compliance, Dev, Comercial] [impacto: Dev, PM]
2. O catálogo suporta variações, atributos por categoria e pipeline de indexação para busca em tempo real? [fonte: Dev, Arquiteto] [impacto: Dev]
3. O checkout está implementado com carrinho multi-seller, cálculo de frete, split de pagamento e todos os meios de pagamento do MVP? [fonte: Dev, Financeiro] [impacto: Dev, Arquiteto]
4. A gestão de pedidos implementa toda a state machine com transições, notificações e ações automáticas? [fonte: Dev, Comercial] [impacto: Dev]
5. O sistema de avaliações está implementado com verificação, moderação e rating agregado ponderado? [fonte: Dev, Comercial] [impacto: Dev]
6. O painel de operações está implementado com dashboard, moderação, disputas, gestão de sellers e configurações? [fonte: Dev, Operações] [impacto: Dev, Operações]
7. O search está funcionando com relevância adequada, filtros facetados e performance testada com volume de catálogo realista? [fonte: Dev, QA] [impacto: Dev]
8. As notificações (e-mail, push, in-app) estão implementadas para todos os eventos definidos na matriz? [fonte: Dev] [impacto: Dev]
9. O chat seller-buyer (se no escopo do MVP) está implementado com moderação e histórico persistente? [fonte: Dev] [impacto: Dev]
10. As pages do catálogo são SSR/SSG para SEO com dados estruturados (Product, Offer, Review) implementados? [fonte: Dev, Marketing] [impacto: Dev, SEO]
11. O painel do seller está completo — catálogo, pedidos, financeiro, comunicação e métricas? [fonte: Dev, Comercial] [impacto: Dev, Designer]
12. O fluxo de disputa está implementado — abertura, evidências, comunicação, decisão e execução de reembolso? [fonte: Dev, Operações, Jurídico] [impacto: Dev]
13. O pipeline de imagens (upload, validação, otimização, CDN) está funcionando com performance aceitável? [fonte: Dev] [impacto: Dev, DevOps]
14. Os testes automatizados cobrem os cenários financeiros (pagamento, split, reembolso, chargeback)? [fonte: Dev, QA] [impacto: Dev, QA]
15. O progresso está dentro do cronograma e os riscos de atraso foram comunicados ao sponsor? [fonte: PM] [impacto: PM, Diretoria]

---

## Etapa 08 — QA

- **Teste do fluxo financeiro end-to-end**: Testar em sandbox do PSP todos os cenários financeiros: pagamento com cartão aprovado, negado, e com 3DS; Pix gerado, pago e expirado; boleto gerado, pago e vencido; reembolso total e parcial; chargeback; e payout para seller com verificação de valores (comissão, taxa de gateway, líquido do seller). Cada cenário deve ter asserção automática de valores — R$ 100 cobrados com 15% de comissão e R$ 3,50 de taxa deve resultar em exatamente R$ 81,50 para o seller. Diferença de centavos em marketplace escala para milhares de reais em volume.

- **Teste de concorrência no catálogo**: Simular cenários de concorrência — dois buyers comprando o último item em estoque simultaneamente (race condition de estoque), seller editando produto enquanto buyer está no checkout (preço muda durante a compra), e múltiplos sellers editando suas listagens simultaneamente (locks no search engine index). Em marketplace, concorrência é cenário real do dia a dia, não edge case teórico. Se o sistema permite vender produto sem estoque ou cobrar preço diferente do exibido, a confiança do marketplace é destruída.

- **Teste de busca e relevância**: Testar a busca com cenários reais — buscar por nome exato do produto (deve ser o primeiro resultado), buscar por sinônimo (deve encontrar), buscar com erro de digitação (fuzzy matching), buscar dentro de categoria com filtros (resultados consistentes), e buscar termo que não existe (mensagem amigável de "nenhum resultado"). Validar que os contadores dos filtros facetados estão corretos (se o filtro diz "15 resultados", deve mostrar exatamente 15). Busca com resultados inconsistentes ou relevância ruim é o killer number one de conversão em marketplace.

- **Teste do painel do seller**: Testar com perfil de seller real (não admin) — o seller consegue criar listagem completa com variações e imagens sem assistência? Consegue gerenciar pedidos (confirmar, enviar, resolver problemas)? Consegue entender seu extrato financeiro e saber quando vai receber? O painel do seller é testado pela perspectiva de usabilidade, não apenas funcionalidade — se funciona mas é confuso, o seller vai ligar para o suporte a cada ação, e o suporte não escala.

- **Teste de segurança específico de marketplace**: Além do OWASP Top 10, marketplace tem vetores de ataque específicos: seller tentando ver dados de outro seller, buyer tentando manipular preço no checkout (alterar request), scraping automatizado do catálogo (roubo de dados de produtos e preços), criação massiva de contas falsas (spam de listings ou avaliações), e manipulação de avaliações (self-review, review bombing). Rate limiting, validação server-side de todos os valores financeiros, e monitoramento de padrões anômalos são obrigatórios.

- **Teste de performance com carga de marketplace**: Simular o cenário de pico — 100+ buyers navegando e buscando simultaneamente, 20+ checkouts paralelos com consulta de frete e pagamento, 10+ sellers editando catálogo simultaneamente, e search engine reindexando. O teste deve revelar: tempo de resposta da busca sob carga (aceitável: <500ms), tempo de checkout (<3s), e throughput de pedidos por minuto sem erro. Marketplace que fica lento na Black Friday ou em dia de promoção perde vendas irrecuperáveis — o buyer simplesmente sai e compra no concorrente.

- **Teste de webhook e reconciliação financeira**: Validar que todos os webhooks do PSP são recebidos, processados e refletidos corretamente no sistema — pagamento confirmado atualiza status do pedido, chargeback notifica seller e operador, payout executado atualiza extrato do seller. Simular falha de webhook (webhook não chegou, chegou duplicado, chegou fora de ordem) e verificar que o sistema trata corretamente — idempotência de webhook (processar o mesmo evento duas vezes não gera efeito duplicado) é obrigatória.

### Perguntas

1. Todos os cenários financeiros foram testados em sandbox com asserção de valores (comissão, taxa, líquido)? [fonte: QA, Dev, Financeiro] [impacto: Dev, Financeiro]
2. Os testes de concorrência cobrem race conditions de estoque, preço e edição simultânea? [fonte: QA, Dev] [impacto: Dev, Arquiteto]
3. A busca foi testada com cenários reais (nome exato, sinônimo, typo, sem resultado) e contadores de filtros validados? [fonte: QA, Comercial] [impacto: Dev]
4. O painel do seller foi testado por alguém com perfil de seller (não dev, não admin)? [fonte: Comercial, QA] [impacto: Dev, Designer]
5. Os testes de segurança cobrem vetores específicos de marketplace (cross-seller access, price manipulation, scraping)? [fonte: Segurança, QA] [impacto: Dev, Segurança]
6. Os testes de carga simulam o cenário de pico com busca, checkout e edição de catálogo simultâneos? [fonte: QA, Dev] [impacto: Dev, DevOps]
7. Os webhooks do PSP foram testados com cenários de falha (duplicado, fora de ordem, timeout) e idempotência validada? [fonte: Dev, QA] [impacto: Dev]
8. O fluxo de disputa foi testado end-to-end — abertura, evidências, decisão e execução de reembolso? [fonte: QA, Operações] [impacto: Dev, Operações]
9. O SEO de catálogo foi validado — SSR funciona, dados estruturados sem erro, sitemap com URLs de produção? [fonte: Dev, Marketing] [impacto: Dev, SEO]
10. O fluxo de KYC do seller foi testado com documentos válidos, inválidos e rejeitados? [fonte: QA, Compliance] [impacto: Dev, PM]
11. O sistema de avaliações foi testado — verificação de comprador real, moderação, cálculo de rating agregado? [fonte: QA, Dev] [impacto: Dev]
12. As notificações (e-mail, push, in-app) foram testadas para cada evento e cada destinatário? [fonte: QA, Dev] [impacto: Dev]
13. O cálculo de frete (se aplicável) foi testado com CEPs reais e os valores batem com as transportadoras? [fonte: QA, Operações] [impacto: Dev]
14. O painel de operações foi testado pela equipe de operações que vai usá-lo no dia a dia? [fonte: Operações, QA] [impacto: Dev, Operações]
15. Todos os bugs classificados como bloqueadores e críticos foram corrigidos e retestados? [fonte: QA, PM] [impacto: Dev, PM]

---

## Etapa 09 — Launch Prep

- **Onboarding dos primeiros sellers**: Recrutar e onboardar os sellers que formarão o catálogo inicial antes do lançamento público. Esses sellers devem estar com cadastro verificado (KYC aprovado), catálogo listado com fotos e descrições de qualidade, e conta bancária para payout configurada. Se o marketplace lança vazio ou com catálogo de baixa qualidade, a primeira impressão dos buyers é de plataforma abandonada — e não há segunda chance. O número ideal depende do nicho: 10-20 sellers com catálogo curado é melhor que 200 sellers com listagens ruins.

- **Teste de pagamento em produção (transação real)**: Antes do lançamento público, executar pelo menos uma transação real em produção — não sandbox. Comprar um produto com cartão real, pagar frete real, e verificar que o seller recebe o payout correto no valor correto no prazo correto. Sandbox do PSP não testa: 3DS real, aprovação real do banco emissor, tempo real de compensação de Pix, e payout real para conta bancária. Uma única transação real de teste previne que o primeiro buyer real encontre o problema.

- **SEO e indexação do catálogo**: Configurar o sitemap dinâmico (todas as páginas de produto, categorias, sellers devem estar no sitemap), verificar que as páginas de catálogo são server-side rendered (não apenas client-side), submeter o sitemap no Google Search Console, e validar os dados estruturados (Schema.org Product, Offer, AggregateRating, Review) com o Rich Results Test. Em marketplace, cada página de produto é uma landing page potencial — se o Google não indexa, o tráfego orgânico é zero e toda aquisição depende de mídia paga.

- **Comunicação de lançamento e marketing**: Preparar a comunicação de lançamento segmentada — para sellers (o que muda, como começar a vender, suporte disponível), para buyers (o que é a plataforma, como comprar, garantias), e para o mercado (press release, redes sociais, parcerias). A comunicação de lançamento define a primeira percepção do marketplace — lançar sem barulho significa zero tráfego, lançar com expectativa alta sem catálogo preparado gera frustração.

- **Plano de contingência financeira**: Documentar o que fazer se: webhook do PSP falhar e pagamentos não forem confirmados (processamento manual? retry?), seller alegar que não recebeu payout (como verificar no dashboard do PSP?), buyer disputar cobrança no cartão (chargeback — quem é notificado, qual o prazo de resposta?), e split calcular valor errado (como corrigir e compensar seller?). Problemas financeiros em marketplace são os mais urgentes — seller que não recebe deixa de enviar, buyer que é cobrado errado abre reclamação no Procon. O plano deve ter responsável e canal de escalação rápida.

- **Monitoramento reforçado**: Configurar alertas específicos para marketplace: taxa de erro no checkout acima de 2% (possível problema no PSP), fila de indexação do search engine crescendo (busca vai ficar desatualizada), webhook do PSP não recebido há mais de 5 minutos (possível falha de integração), e número de disputas abertas por dia acima do normal (possível problema de qualidade). O time técnico deve estar de plantão nos primeiros 7 dias com canal de comunicação rápido e acesso a produção para debug.

### Perguntas

1. Os primeiros sellers foram recrutados, verificados e têm catálogo listado com qualidade aprovada? [fonte: Comercial, Operações] [impacto: PM, Marketing]
2. Foi executada pelo menos uma transação real em produção com pagamento, split e payout confirmados? [fonte: Dev, Financeiro] [impacto: Dev, Financeiro]
3. O SEO do catálogo está configurado — SSR, sitemap dinâmico, dados estruturados validados, Search Console verificado? [fonte: Dev, Marketing] [impacto: SEO, Dev]
4. A comunicação de lançamento está preparada e segmentada por público (sellers, buyers, mercado)? [fonte: Marketing, Diretoria] [impacto: PM, Marketing]
5. O plano de contingência financeira está documentado com procedimentos para webhook failure, payout incorreto e chargeback? [fonte: Financeiro, Dev, Jurídico] [impacto: Dev, Financeiro, PM]
6. O monitoramento reforçado está configurado com alertas para checkout, search, webhooks e disputas? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
7. O time de operações está treinado e pronto para moderar catálogo, resolver disputas e gerenciar sellers? [fonte: Operações, PM] [impacto: Operações]
8. Os termos de uso e políticas estão publicados no site e o fluxo de aceite pelo seller está funcional? [fonte: Jurídico, Dev] [impacto: Dev, Jurídico]
9. O plano de rollback está documentado — se o marketplace precisar ser retirado do ar, qual a sequência e quem decide? [fonte: TI, Diretoria] [impacto: PM, DevOps]
10. Os meios de pagamento foram validados em produção — cartão com 3DS, Pix com QR code, boleto com vencimento? [fonte: Dev, Financeiro] [impacto: Dev]
11. O suporte ao seller e ao buyer está operacional — canal definido, equipe treinada, SLA comunicado? [fonte: Operações, PM] [impacto: Operações, PM]
12. Os analytics e eventos de conversão (view product, add to cart, purchase) estão configurados e validados? [fonte: Marketing, Dev] [impacto: Marketing, Dev]
13. O treinamento do time de operações (moderação, disputas, suporte) foi realizado com cenários reais? [fonte: Operações, PM] [impacto: Operações]
14. A hospedagem está dimensionada para o tráfego esperado no lançamento (considerar pico de curiosidade)? [fonte: DevOps, TI] [impacto: DevOps]
15. Todos os stakeholders foram notificados sobre a data de lançamento e seus papéis no dia? [fonte: PM, Diretoria] [impacto: PM]

---

## Etapa 10 — Go-Live

- **Ativação e smoke test de marketplace**: Ativar o marketplace para acesso público e executar smoke test em produção — busca retorna resultados, página de produto carrega com dados reais, checkout funciona com pagamento real, seller recebe notificação de pedido, painel de operações mostra dados corretos. O smoke test deve ser executado por 3 pessoas diferentes em dispositivos diferentes — o fundador no desktop, o seller no celular, e o operador no painel. Se qualquer fluxo crítico falhar, avaliar se é corrigível em minutos ou se adia o lançamento.

- **Monitoramento financeiro nas primeiras horas**: Acompanhar cada transação real nas primeiras horas — pagamento confirmado pelo PSP, split executado corretamente, valor creditado na conta da plataforma e do seller. Comparar valores com as regras financeiras definidas (comissão, taxa, líquido). Se houver divergência em qualquer transação, pausar e investigar antes que o volume aumente. Um bug financeiro que afeta 1 transação é corrigível — o mesmo bug em 1.000 transações é crise operacional.

- **Monitoramento de search e catálogo**: Verificar que o search engine está respondendo com latência aceitável (<500ms), que os filtros facetados estão corretos, e que novos produtos adicionados por sellers são indexados em tempo real. Se o search ficar lento ou desatualizado no dia do lançamento, a experiência do buyer é diretamente impactada — busca que não encontra o que existe é equivalente a prateleira vazia em loja física.

- **Suporte ativo a sellers e buyers**: No primeiro dia, ter canal de suporte dedicado com resposta em minutos, não horas. Sellers terão dúvidas sobre como gerenciar pedidos, entender o financeiro, e resolver problemas com listagens. Buyers terão dúvidas sobre como comprar, rastrear entrega, e abrir reclamação. Cada dúvida não respondida no primeiro dia é um seller que desiste ou um buyer que não volta. O suporte ativo nos primeiros dias é investimento em retenção — não custo operacional.

- **Coleta de métricas de baseline**: Registrar as métricas do dia 1 como baseline — GMV (Gross Merchandise Value), número de transações, ticket médio, taxa de conversão (visitors → purchase), taxa de aprovação de pagamento, número de sellers ativos que receberam pedido, e NPS ou satisfação qualitativa de sellers e buyers. Essas métricas definem o ponto de partida para otimização — sem baseline, é impossível medir se as mudanças futuras estão melhorando ou piorando a plataforma.

- **Encerramento formal e roadmap**: Entregar formalmente ao cliente: acesso ao repositório com documentação, acesso à infraestrutura com runbook de operação, acesso ao PSP com documentação de fluxos financeiros, acesso ao search engine com documentação de indexação, guia de operações (moderação, disputas, suporte), e roadmap de próximas features priorizadas pelo feedback do lançamento. Marketplace é produto vivo — o go-live não é o fim, é o início da operação. O aceite formal do MVP fecha a primeira fase e inicia o ciclo contínuo de produto.

### Perguntas

1. O marketplace está acessível publicamente e o smoke test foi concluído com sucesso em múltiplos dispositivos? [fonte: QA, Dev] [impacto: Dev, PM]
2. As primeiras transações reais foram monitoradas com verificação de valores de split e payout? [fonte: Financeiro, Dev] [impacto: Dev, Financeiro]
3. O search engine está respondendo com latência aceitável e indexando novos produtos em tempo real? [fonte: Dev, DevOps] [impacto: Dev]
4. O suporte ativo a sellers e buyers está operacional com resposta em minutos? [fonte: Operações, PM] [impacto: Operações, PM]
5. As métricas de baseline do dia 1 foram registradas (GMV, transações, conversão, sellers ativos)? [fonte: PM, Comercial] [impacto: PM, Marketing]
6. O monitoramento de infra e aplicação está sem alertas críticos nas primeiras horas? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
7. Os sellers estão conseguindo gerenciar pedidos e entender o financeiro sem assistência constante? [fonte: Comercial, Operações] [impacto: PM, Dev]
8. Os webhooks do PSP estão sendo recebidos e processados corretamente em produção? [fonte: Dev] [impacto: Dev]
9. O catálogo está aparecendo corretamente na busca do Google (verificar no Search Console)? [fonte: Dev, Marketing] [impacto: SEO]
10. Os bugs reportados no primeiro dia foram classificados e os bloqueadores tratados com prioridade máxima? [fonte: Dev, QA] [impacto: Dev, PM]
11. O feedback estruturado de sellers e buyers está sendo coletado nos primeiros dias? [fonte: PM, Comercial, Operações] [impacto: PM]
12. Todos os acessos foram entregues formalmente ao cliente e cada pessoa confirmou acesso? [fonte: Dev, DevOps] [impacto: PM]
13. O aceite formal de entrega do MVP foi obtido do sponsor? [fonte: Diretoria] [impacto: PM]
14. O plano de suporte pós-lançamento está ativado com SLA comunicado? [fonte: Diretoria, PM] [impacto: PM, Dev]
15. O roadmap de próximas features foi priorizado com base no feedback real dos primeiros dias? [fonte: PM, Diretoria, Comercial] [impacto: PM, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"É tipo um Mercado Livre, só que simples"** — Marketplace nunca é simples. Mesmo o MVP mínimo envolve: cadastro de seller, catálogo, busca, checkout, split de pagamento, gestão de pedidos, e painel de operações. Comparar com Mercado Livre (empresa de 10.000+ engenheiros) e dizer "simples" é sinal de que a complexidade não foi compreendida. Dimensionar corretamente antes de continuar.
- **"Primeiro construímos a plataforma, depois atraímos sellers"** — Marketplace vazio é marketplace morto. A estratégia de cold start deve ser discutida antes da primeira linha de código. Se não há plano para trazer sellers e catálogo antes do lançamento, o marketplace vai nascer deserto e morrer deserto.
- **"Não precisamos de advogado, é só um site de vendas"** — Marketplace envolve: responsabilidade solidária pelo CDC, split de pagamento (regulamentação Bacen), LGPD para dados de sellers e buyers, termos de uso que regem a relação tripartite, e política de disputa. Sem assessoria jurídica, a primeira reclamação no Procon ou processo judicial vira crise existencial.

### Etapa 02 — Discovery

- **"O pagamento é simples, é só cobrar e repassar"** — Split de pagamento envolve escrow, timing de liberação, chargebacks, reembolsos parciais, comissão variável, minimum payout, e conciliação. "Cobrar e repassar" é transferência bancária, não payment engine de marketplace. Subestimar a complexidade financeira é o erro mais caro em projetos de marketplace.
- **"Não precisamos de busca, são poucos produtos"** — "Poucos produtos" hoje são "muitos produtos" em 6 meses se o marketplace funcionar. Se a busca não for projetada para escalar, será refeita quando o catálogo crescer. E a refação de busca com dados em produção é significativamente mais complexa e arriscada do que fazer certo desde o início.
- **"Avaliações a gente coloca depois"** — Sem avaliações, o buyer não tem como avaliar a confiabilidade do seller. A confiança é o ativo mais importante do marketplace — sem ela, o buyer compra no concorrente que já tem avaliações. Sistema de reputação deve estar no MVP, não no backlog.

### Etapa 03 — Alignment

- **"O MVP é tudo — seller, buyer, operador, chat, avaliações, app mobile"** — Isso não é MVP, é o produto completo. MVP de marketplace deveria ser: seller lista, buyer busca e compra, plataforma processa pagamento e split. Chat, avaliações e app mobile são iterações posteriores. Sem corte de escopo real, o projeto leva 18 meses em vez de 4.
- **"Vamos usar Pix direto, sem intermediário"** — Pix sem PSP significa receber na conta da empresa e repassar manualmente para sellers. Não há split automático, não há escrow, não há proteção contra fraude, e não há conciliação. Para 5 sellers pode funcionar artesanalmente; para 50 é caos financeiro. PSP com split é obrigatório para marketplace que pretende escalar.
- **"O jurídico vê os termos depois do lançamento"** — Marketplace sem termos de uso é operação irregular. O seller precisa aceitar termos para vender (comissão, obrigações, penalidades), o buyer precisa aceitar termos para comprar (garantias, política de disputa). Lançar sem termos é começar a construir relações comerciais sem contrato.

### Etapa 04 — Definition

- **"O catálogo é simples, é só nome, preço e foto"** — Catálogo sem categorias estruturadas, atributos, e variações não permite busca com filtros, não permite comparação, e não permite que o seller liste corretamente produtos complexos. "Simples" no início vira refatoração cara quando o seller precisa listar "Camiseta M azul R$ 49 e G vermelha R$ 55" e o sistema só tem um campo de preço.
- **"O fluxo de pedido é igual e-commerce normal"** — Pedido em marketplace envolve dois lados com interesses distintos e tempos de resposta diferentes. O seller pode não confirmar, o buyer pode cancelar após confirmação, a entrega pode ser feita por terceiro, e a disputa envolve mediação da plataforma. Tratar como e-commerce simples gera gaps nos fluxos de exceção.
- **"As regras financeiras são só uma porcentagem"** — Comissão de 15% parece simples até considerar: o que acontece com a comissão em reembolso parcial? E em chargeback? E se o seller pede antecipação de recebíveis? E o mínimo para payout? Cada cenário financeiro precisa de regra explícita e exemplo numérico, ou o sistema vai calcular errado em produção.

### Etapa 05 — Architecture

- **"Busca no banco resolve, não precisa de Elasticsearch"** — Busca SQL com LIKE e filtros WHERE funciona para 100 produtos. Para 10.000 produtos com filtros facetados, autocomplete e relevância por ranking, a query degrada para segundos de resposta e relevância zero. Search engine dedicado não é premature optimization — é requisito funcional para marketplace.
- **"Vamos implementar o split de pagamento nós mesmos"** — Implementar split próprio significa: receber pagamento na conta da plataforma, calcular comissão, e transferir manualmente (ou por automação) para cada seller. Isso gera: risco regulatório (plataforma intermediando recursos financeiros sem licença), complexidade de conciliação, e dor de cabeça com chargebacks. PSP com split nativo é praticamente obrigatório.
- **"Não precisa de CDN para imagens, o servidor aguenta"** — Marketplace de produtos com 10.000 imagens servidas do servidor de aplicação degrada a performance de tudo — cada request de imagem compete com requests de API. CDN com transformação on-the-fly (Cloudinary, imgix) é investimento mínimo com retorno enorme em performance e experiência.

### Etapa 06 — Setup

- **"Testamos o pagamento em produção quando lançar"** — O primeiro teste de pagamento em produção deveria ter sido feito semanas antes do lançamento. Fluxo de sandbox do PSP não testa: 3DS real, aprovação real do banco, Pix com QR code real, e payout real para conta bancária. Descobrir um bug de pagamento no dia do lançamento, com sellers e buyers esperando, é a pior forma de fazer QA.
- **"O seed de dados são 3 produtos de teste"** — Marketplace com 3 produtos de teste não permite testar: busca com filtros (não há o que filtrar), paginação (tudo cabe na primeira página), e painel de operações (não há dados para dashboards). Seed mínimo: 5 sellers, 50 produtos, 20 pedidos, 30 avaliações.
- **"O Elasticsearch a gente configura depois, por enquanto busca no banco"** — Se a busca é feature core (e em marketplace sempre é), configurar o search engine "depois" significa reescrever toda a camada de busca quando já há dados em produção. Setup do search engine com mappings e analyzers corretos deve ser feito antes do build, não depois.

### Etapa 07 — Build

- **"O painel do seller fica para a v2"** — Sem painel, o seller gerencia pedidos por e-mail e catálogo por planilha enviada ao suporte. Isso funciona para 3 sellers, não para 30. Se o painel do seller não está no MVP, o marketplace não é autoatendimento — é operação manual disfarçada de plataforma.
- **"Checkout com um meio de pagamento no MVP"** — No Brasil, limitar a cartão de crédito exclui a parcela significativa de buyers que preferem Pix (instantâneo, sem taxa para buyer) ou boleto. Pix especialmente deve estar no MVP — é o meio de pagamento com maior crescimento e menor taxa para a plataforma.
- **"Testes do financeiro a gente faz manual"** — Sem testes automatizados para cenários financeiros (split, reembolso, chargeback), cada mudança de código é risco de bug financeiro em produção. Bug financeiro = seller recebe errado = seller abandona plataforma = marketplace morre. Testes financeiros automatizados são investimento de sobrevivência.

### Etapa 08 — QA

- **"Testamos só o fluxo feliz — buyer compra, seller entrega"** — O fluxo feliz representa 60-70% das transações. Os outros 30-40% são: cancelamento, reembolso, disputa, chargeback, seller que não confirma, buyer que não retira, entrega com problema. Cada fluxo de exceção precisa de teste específico, porque é nos fluxos de exceção que o marketplace perde dinheiro e confiança.
- **"O seller testou e disse que tá bom"** — "Tá bom" do seller founder-friend que está ajudando não é validação real. O seller real vai tentar listar 50 produtos com variações, fotografar com celular, e quer saber exatamente quando recebe. Teste com seller que não conhece o time de desenvolvimento — se ele consegue operar sem assistência, o painel funciona.
- **"Performance tá boa, carrega rápido"** — "Rápido" com 50 produtos é diferente de "rápido" com 5.000 produtos e 100 buyers simultâneos. Teste de carga com volume realista é obrigatório para marketplace — o dia de maior tráfego (lançamento, promoção, Black Friday) é exatamente quando a performance precisa ser melhor, não quando é aceitável degradar.

### Etapa 09 — Launch Prep

- **"Lançamos e os sellers vão aparecer"** — Sellers não aparecem organicamente em marketplace desconhecido. Se não há sellers cadastrados com catálogo antes do lançamento, o buyer encontra plataforma vazia e não volta. O onboarding dos primeiros sellers é trabalho comercial ativo — visitar, convencer, ajudar a cadastrar, curar o catálogo. Sem isso, o lançamento é um evento para zero pessoas.
- **"Não precisa testar com dinheiro real, sandbox é igual"** — Sandbox do PSP simula fluxos, mas não testa: aprovação real do banco emissor, 3DS challenge real, tempo de compensação de Pix real, e payout real para conta bancária. Uma transação real antes do lançamento previne que o primeiro buyer real seja o cobaia.
- **"Se der problema financeiro, o dev resolve"** — Problema financeiro em marketplace não é bug de software — é dinheiro de seller retido, buyer cobrado incorretamente, ou comissão calculada errada. Resolver exige: acesso ao dashboard do PSP, conhecimento das regras financeiras do marketplace, e autoridade para executar reembolso ou payout manual. O time de operações (não o dev) deve ter esse acesso e saber usá-lo antes do go-live.

### Etapa 10 — Go-Live

- **"Go-live na Black Friday para aproveitar o tráfego"** — Lançar marketplace em data de pico de volume é maximizar o risco. Se algo der errado (e algo sempre dá errado no go-live), o impacto é amplificado pelo volume. Lançar 4-6 semanas antes de datas de pico — tempo para estabilizar, corrigir bugs, e treinar operações.
- **"Marketplace no ar, marketing ativado, vamos embora"** — As primeiras 48h são críticas — monitorar cada transação, cada disputa, cada reclamação. Se o checkout falha, se o split calcula errado, se o seller não recebe notificação, o marketplace perde credibilidade antes de construí-la. Monitoramento ativo, não passivo.
- **"O projeto está entregue, agora vocês operam"** — Marketplace sem time de operações dedicado morre em semanas. Quem modera catálogo? Quem resolve disputas? Quem responde o seller que não recebeu? Quem monitora fraude? Operação de marketplace é trabalho contínuo, não handoff pontual. Se o cliente não tem time de operações dimensionado, o marketplace vai degradar rapidamente.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é marketplace** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Na verdade somos nós que vendemos, não há outros sellers" | E-commerce próprio, não marketplace | Reclassificar para e-commerce |
| "Os usuários vão colaborar e compartilhar conteúdo entre si" | Rede social ou comunidade, não marketplace | Reclassificar para web-app ou social-platform |
| "É um catálogo online, mas não tem pagamento na plataforma" | Diretório ou classificados, não marketplace transacional | Reclassificar para web-app ou static-site |
| "É uma ferramenta para nosso time comercial gerenciar pedidos" | CRM ou ferramenta interna, não marketplace | Reclassificar para internal-saas |
| "Queremos oferecer assinatura de software por plataforma" | App store ou SaaS aggregator, modelo diferente de marketplace | Avaliar se é marketplace de conteúdo digital ou modelo próprio |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não definimos o modelo de monetização ainda" | 01 | Toda a arquitetura financeira depende dessa decisão | Definir modelo de monetização antes de avançar |
| "Não temos estratégia de cold start" | 01 | Marketplace lança vazio e morre vazio | Definir estratégia de aquisição de sellers e buyers antes de continuar |
| "Não temos advogado para os termos de uso" | 03 | Operação irregular, risco jurídico alto desde o dia 1 | Contratar assessoria jurídica especializada antes do go-live |
| "O PSP não suporta o modelo de split que precisamos" | 03 | Fluxo financeiro não funciona na plataforma escolhida | Trocar de PSP ou adaptar o modelo de split antes da Architecture |
| "Não temos ninguém para operar o marketplace (moderação, suporte, disputas)" | 09 | Marketplace sem operação degrada rapidamente | Dimensionar e treinar time de operações antes do lançamento |
| "Não temos sellers confirmados para o lançamento" | 09 | Marketplace lança sem catálogo — buyer não volta | Recrutar e onboardar sellers antes do lançamento |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Queremos comissão zero para atrair sellers" | 01 | Sem receita, o marketplace não se sustenta | Documentar o plano de monetização futura e o runway sem receita |
| "O mercado é novo, não sabemos o tamanho" | 01 | Risco de product-market fit — o marketplace pode não ter demanda | Validar demanda com MVP enxuto antes de investimento pesado |
| "Cada seller pode definir sua própria política de devolução" | 02 | Inconsistência de experiência — buyer não sabe o que esperar | Definir política da plataforma como baseline com exceções controladas |
| "Queremos tudo para ontem, o investidor está pressionando" | 01 | Pressão de prazo gera corte de escopo sem critério e dívida técnica | Negociar MVP realista com critérios de corte explícitos |
| "Não temos experiência operando marketplace" | 01 | Curva de aprendizado vai gerar erros operacionais nos primeiros meses | Planejar consultoria operacional ou mentoria de marketplace |
| "O design está sendo feito por um freelancer" | 03 | Marketplace tem 3 interfaces (seller, buyer, operador) — um freelancer pode não ter capacidade | Verificar se o escopo de design é viável e se há backup |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Modelo de monetização definido (pergunta 1)
- Estratégia de cold start planejada (pergunta 2)
- Tipo de marketplace identificado — produto, serviço, aluguel, B2B, digital (pergunta 3)
- Todos os lados da plataforma mapeados (pergunta 4)
- Orçamento de desenvolvimento, operação e marketing aprovado (pergunta 9)

### Etapa 02 → 03

- Jornada de cada lado mapeada passo a passo (pergunta 1)
- Modelo de comissão e split detalhado com cenários financeiros (pergunta 2)
- Fluxo financeiro completo mapeado (pergunta 5)
- Requisitos de LGPD identificados (pergunta 11)
- KPIs de sucesso definidos (pergunta 14)

### Etapa 03 → 04

- Escopo do MVP definido para cada lado (pergunta 1)
- PSP escolhido e validado tecnicamente (pergunta 2)
- Termos de uso redigidos por advogado (pergunta 3)
- Decisão mobile (web, PWA, nativo) tomada (pergunta 4)
- Time de operações dimensionado (pergunta 9)

### Etapa 04 → 05

- Modelo de catálogo definido com categorias, atributos e variações (pergunta 1)
- State machine de pedido formalizada (pergunta 2)
- Regras financeiras documentadas com exemplos numéricos (pergunta 3)
- Busca e filtros especificados (pergunta 4)
- Painéis de seller e operador especificados (perguntas 5 e 6)

### Etapa 05 → 06

- Search engine escolhido e justificado (pergunta 1)
- PSP validado tecnicamente para todos os cenários (pergunta 2)
- Infra desenhada com auto-scaling (pergunta 4)
- Custos de operação calculados (pergunta 11)
- Arquitetura documentada e aprovada (pergunta 15)

### Etapa 06 → 07

- Ambiente local sobe com todos os serviços em um comando (pergunta 1)
- PSP configurado e fluxo testado em sandbox (pergunta 2)
- Search engine configurado com mappings e analyzers (pergunta 3)
- Pipeline de CI/CD testado (pergunta 8)
- Seed de dados cria marketplace funcional (pergunta 5)

### Etapa 07 → 08

- KYC do seller implementado (pergunta 1)
- Checkout implementado com split e todos os meios de pagamento (pergunta 3)
- State machine de pedido implementada com notificações (pergunta 4)
- Painel de operações implementado (pergunta 6)
- Testes financeiros automatizados (pergunta 14)

### Etapa 08 → 09

- Fluxo financeiro testado end-to-end com asserção de valores (pergunta 1)
- Concorrência testada (estoque, preço, edição simultânea) (pergunta 2)
- Busca validada com cenários reais (pergunta 3)
- Segurança específica de marketplace testada (pergunta 5)
- Bugs bloqueadores corrigidos e retestados (pergunta 15)

### Etapa 09 → 10

- Sellers recrutados com catálogo listado (pergunta 1)
- Transação real executada em produção (pergunta 2)
- SEO configurado e Search Console verificado (pergunta 3)
- Contingência financeira documentada (pergunta 5)
- Time de operações treinado (pergunta 13)

### Etapa 10 → Encerramento

- Smoke test concluído em produção (pergunta 1)
- Transações reais monitoradas com valores validados (pergunta 2)
- Suporte ativo operacional (pergunta 4)
- Métricas de baseline registradas (pergunta 5)
- Aceite formal obtido do sponsor (pergunta 13)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de marketplace. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Produtos Físicos | V2 Serviços | V3 Aluguel/Reservas | V4 B2B | V5 Conteúdo Digital |
|---|---|---|---|---|---|
| 01 Inception | 3 | 3 | 3 | 3 | 2 |
| 02 Discovery | 4 | 4 | 4 | 5 | 3 |
| 03 Alignment | 3 | 3 | 3 | 4 | 2 |
| 04 Definition | 5 | 4 | 4 | 5 | 3 |
| 05 Architecture | 4 | 4 | 4 | 4 | 3 |
| 06 Setup | 3 | 3 | 3 | 3 | 2 |
| 07 Build | 5 | 5 | 5 | 5 | 4 |
| 08 QA | 5 | 4 | 4 | 4 | 3 |
| 09 Launch Prep | 4 | 3 | 3 | 4 | 3 |
| 10 Go-Live | 3 | 3 | 3 | 3 | 2 |
| **Total relativo** | **39** | **36** | **36** | **40** | **27** |

**Observações por variante:**

- **V1 Produtos Físicos**: A variante mais equilibradamente pesada. Definition é 5 por causa do catálogo com variações, busca com filtros e fluxo de pedido complexo. Build é 5 pela implementação de checkout multi-seller, cálculo de frete e gestão de pedidos. QA é 5 pelos testes financeiros, de concorrência e de logística que precisam cobrir dezenas de cenários.
- **V2 Serviços**: Build é 5 pela complexidade de matching, agendamento e gestão de disponibilidade. A diferença do V1 é que não há logística física, o que simplifica QA. Porém, disputas em serviços são mais subjetivas ("o serviço foi mal feito" vs. "o produto veio quebrado"), exigindo fluxo de mediação mais robusto.
- **V3 Aluguel/Reservas**: Build é 5 pela gestão de calendário, prevenção de double-booking, políticas de cancelamento com deadlines, e pricing dinâmico. O fluxo financeiro é diferente (antecipação, caução, split pós-estadia) e adiciona complexidade à integração com PSP.
- **V4 B2B**: Discovery é 5 pela complexidade do fluxo de procurement (cotação, negociação, MOQ, condições de pagamento). Definition é 5 pelo modelo de catálogo técnico com especificações e workflow de aprovação interna. Launch Prep é 4 porque o onboarding de fornecedores B2B é mais lento e burocrático.
- **V5 Conteúdo Digital**: A variante mais leve — não há logística, fulfillment é download/acesso, e o catálogo é mais simples. A complexidade específica está na proteção de conteúdo (DRM, signed URLs, prevenção de pirataria) e no modelo de licenciamento.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Marketplace de serviço ou conteúdo digital, sem produto físico (Etapa 01, pergunta 3) | Etapa 02: pergunta 9 (logística e transportadoras). Etapa 04: pergunta 8 (política de frete). Etapa 05: pergunta 7 (integração com transportadoras). Etapa 08: pergunta 13 (teste de cálculo de frete). |
| MVP web responsivo, sem app nativo (Etapa 03, pergunta 4) | Etapa 05: considerações de push nativo (APNs). Etapa 07: menções a app store, deep links nativos. (Web push via Firebase ainda se aplica.) |
| Seller único ou plataforma própria (reclassificação para e-commerce) | Todas as perguntas de KYC, painel do seller, split de pagamento e gestão de disputas seller-buyer se tornam irrelevantes. Reclassificar para e-commerce. |
| Sem chat seller-buyer no MVP (Etapa 03, pergunta 11) | Etapa 05: pergunta 6 (solução de messaging) se simplifica — apenas notificações. Etapa 07: pergunta 9 (implementação de chat). Etapa 08: menções a teste de chat. |
| Comissão fixa sem variação por categoria (Etapa 02, pergunta 2) | Etapa 04: simplifica regras financeiras (sem tabela de comissão variável). Etapa 07: simplifica lógica de cálculo de split. |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Marketplace de produto físico com logística (Etapa 01, pergunta 3) | Etapa 02: pergunta 9 (logística) se torna gate. Etapa 04: pergunta 8 (política de frete) se torna gate. Etapa 05: pergunta 7 (integração com transportadoras) se torna gate. Etapa 08: pergunta 13 (teste de frete com CEPs reais) é obrigatória. |
| Múltiplos meios de pagamento confirmados — cartão + Pix + boleto (Etapa 03, pergunta 13) | Etapa 05: PSP deve suportar todos com split. Etapa 07: checkout implementa fluxo específico para cada meio. Etapa 08: teste de cada meio de pagamento é obrigatório. Etapa 09: pergunta 10 (validação em produção) cobre todos os meios. |
| Regulamentação setorial identificada — Anvisa, MEC, Bacen (Etapa 01, pergunta 6) | Etapa 02: requisitos regulatórios detalhados se tornam gates. Etapa 04: verificação de seller deve incluir documentação setorial. Etapa 08: compliance testing é obrigatório. Etapa 09: aprovação regulatória como pré-requisito de go-live. |
| Escopo geográfico nacional ou internacional (Etapa 01, pergunta 5) | Etapa 04: cálculo de frete multi-transportadora se torna obrigatório. Etapa 05: CDN em múltiplas regiões. Etapa 07: gestão de múltiplos prazos de entrega. Se internacional: múltiplas moedas, impostos de importação, compliance multi-jurisdição. |
| App nativo no roadmap (Etapa 03, pergunta 4) | Etapa 05: arquitetura API-first é obrigatória. Etapa 05: push via Firebase/APNs deve ser planejado. Etapa 07: API deve ser documentada e versionada para consumo mobile. |
| Volume projetado >1.000 transações/mês (Etapa 01, pergunta 14) | Etapa 05: pergunta 4 (auto-scaling) se torna gate. Etapa 05: pergunta 10 (proteção contra fraude) é obrigatória. Etapa 08: pergunta 6 (teste de carga) é gate com thresholds definidos. Etapa 09: monitoramento reforçado é obrigatório. |
