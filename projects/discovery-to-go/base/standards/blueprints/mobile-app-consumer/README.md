---
title: "Mobile App (Consumer) — Blueprint"
description: "Aplicativo para lojas públicas (App Store / Google Play). Foco em UX, performance percebida, notificações push, deep links e aquisição de usuários."
category: project-blueprint
type: mobile-app-consumer
status: rascunho
created: 2026-04-13
---

# Mobile App (Consumer)

## Descrição

Aplicativo para lojas públicas (App Store / Google Play). Foco em UX, performance percebida, notificações push, deep links e aquisição de usuários.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo app consumer é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — App de Conteúdo / Mídia

Aplicativo que entrega conteúdo consumível — notícias, vídeos, podcasts, artigos, receitas, cursos. O usuário consome conteúdo predominantemente de forma passiva, com interações limitadas a favoritos, bookmarks, compartilhamento e, em alguns casos, comentários. A monetização geralmente é por assinatura (paywall) ou por anúncios (AdMob, Meta Audience Network). O foco técnico é performance de carregamento de listas, cache offline de conteúdo já acessado, e push notifications para engajamento com novo conteúdo. Exemplos: app de jornal, app de streaming de áudio, app de receitas, app de cursos online.

### V2 — App de Marketplace / E-commerce

Aplicativo centrado em transações — browse de catálogo, carrinho, checkout, pagamento, tracking de pedido. Envolve múltiplos atores (comprador, vendedor, entregador) e integrações pesadas com gateways de pagamento, antifraude, e logística. O foco técnico é segurança de transação, experiência de checkout com mínima fricção, e tratamento de estados complexos (pedido criado → pago → separado → enviado → entregue → devolvido). Exemplos: app de delivery, app de marketplace de produtos, app de ingressos, app de reservas de hotel.

### V3 — App Social / Comunidade

Aplicativo onde os usuários geram o conteúdo principal — perfis, posts, fotos, vídeos, comentários, likes, follows, mensagens diretas. A complexidade está no feed algorítmico ou cronológico, na moderação de conteúdo gerado por usuários, e no crescimento viral (convites, compartilhamento). O foco técnico é real-time (mensagens, notificações, atualizações de feed), escalabilidade do backend para picos de uso, e compliance de conteúdo (CSAM, hate speech, DMCA). Exemplos: rede social de nicho, app de comunidade de bairro, app de fórum, app de dating.

### V4 — App Utilitário / Ferramenta

Aplicativo focado em resolver uma tarefa específica do dia a dia — calculadora financeira, scanner de documentos, gerenciador de tarefas, rastreador de hábitos, controle de despesas. Geralmente não depende de backend pesado (funciona offline ou com sync leve) e monetiza via modelo freemium, compra única ou assinatura de features premium. O foco técnico é UX extremamente polida para a tarefa principal, uso de APIs nativas do dispositivo (câmera, sensores, notificações locais), e tamanho reduzido do app. Exemplos: app de finanças pessoais, app de to-do list, app de scanner, app de meditação.

### V5 — App de Saúde / Fitness / IoT

Aplicativo que integra com dispositivos externos (wearables, sensores, equipamentos de academia) ou com APIs de saúde do sistema operacional (HealthKit, Google Health Connect). Envolve coleta contínua de dados biométricos, visualizações de progresso (gráficos, relatórios), e frequentemente requisitos regulatórios (HIPAA, ANVISA, LGPD com dados sensíveis). O foco técnico é integração Bluetooth/BLE com dispositivos, processamento de dados em background, e privacidade de dados de saúde com consentimento granular. Exemplos: app de corrida, app de monitoramento de glicose, app de academia, app de bem-estar corporativo.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Framework | Linguagem | Backend | Infra | Observações |
|---|---|---|---|---|---|
| V1 — Conteúdo/Mídia | React Native ou Flutter | TypeScript / Dart | Firebase ou Supabase | Firebase Hosting + CDN | Offline-first com cache local. Push via FCM/APNs. Plano gratuito resolve MVP. |
| V2 — Marketplace | React Native ou Nativo (Swift/Kotlin) | TypeScript / Swift / Kotlin | Node.js + PostgreSQL ou Supabase | AWS ou GCP | Integrações de pagamento exigem nativo em alguns casos. Backend robusto obrigatório. |
| V3 — Social/Comunidade | React Native ou Flutter | TypeScript / Dart | Node.js + PostgreSQL + Redis | AWS ou GCP com auto-scaling | Real-time exige WebSocket ou Firebase Realtime DB. CDN para mídia do usuário. |
| V4 — Utilitário | Flutter ou SwiftUI/Jetpack Compose | Dart / Swift / Kotlin | Serverless ou sem backend | Firebase ou Cloudflare Workers | App leve. Backend mínimo. Foco em APIs nativas do dispositivo. |
| V5 — Saúde/IoT | Nativo (Swift/Kotlin) ou Flutter | Swift / Kotlin / Dart | Node.js + PostgreSQL | AWS (HIPAA-eligible) ou GCP | BLE exige acesso nativo. Dados sensíveis exigem criptografia e compliance. |

---

## Etapa 01 — Inception

- **Origem da demanda e modelo de negócio**: A necessidade de um app consumer geralmente surge de uma oportunidade de mercado identificada (gap no segmento), pressão competitiva (concorrentes já têm app), ou migração de um serviço web para mobile. Entender o modelo de receita pretendido (assinatura, freemium, transação, anúncios, compra in-app) é fundamental nesta fase porque ele define requisitos técnicos: assinatura exige integração com StoreKit/Google Play Billing, anúncios exigem SDK de ad network, transação exige gateway de pagamento — cada um com implicações de arquitetura, compliance e taxa da loja (15-30% da Apple/Google).

- **Público-alvo e tamanho do mercado**: Apps consumer competem por atenção com milhões de outros apps nas lojas. Diferentemente de projetos internos, o público precisa ser conquistado — o que significa que a proposta de valor deve ser clara nos primeiros 10 segundos de uso. Definir personas com precisão (idade, comportamento digital, dispositivos predominantes, conexão de internet típica) impacta diretamente decisões de design (tamanho de fonte, complexidade de navegação), performance (qual LCP é aceitável em 3G) e priorização de plataforma (iOS primeiro vs. Android primeiro vs. ambos simultâneos).

- **Decisão de plataforma: iOS, Android ou ambos**: Esta é a decisão mais impactante do projeto e deve ser tomada com dados, não com opinião. Fatores: se o público-alvo é predominantemente iOS (ex.: mercado premium, EUA, Europa ocidental) ou Android (ex.: Brasil, Índia, mercados emergentes), se há budget para manter dois codebases nativos, se cross-platform (React Native, Flutter) atende os requisitos técnicos (BLE, câmera avançada, ARKit/ARCore). Lançar em ambas as plataformas simultaneamente dobra o esforço de QA e de manutenção — iniciar em uma e expandir após validação é frequentemente a decisão mais sábia.

- **Expectativa de downloads e escala**: O cliente frequentemente subestima ou superestima o volume de downloads iniciais. Superestimar leva a investimento prematuro em infraestrutura de escala; subestimar leva a problemas de performance nos primeiros picos de uso reais (matéria na mídia, campanha viral). Obter uma estimativa realista — baseada no tamanho do mercado endereçável, taxa de conversão esperada das campanhas de aquisição, e benchmarks do setor — permite dimensionar a infraestrutura adequadamente e planejar pontos de escala.

- **Requisitos regulatórios e das lojas**: Apps consumer estão sujeitos às políticas da Apple App Store e da Google Play Store, que são frequentemente atualizadas e podem rejeitar o app se violadas. Requisitos comuns que clientes desconhecem: Apple exige login com Apple se o app oferece login social, apps de assinatura devem usar o sistema de pagamento da loja (com comissão de 15-30%), apps com conteúdo gerado pelo usuário devem ter mecanismo de report/block, e apps de saúde/finanças podem exigir disclaimers específicos. Além das lojas, há regulação setorial: LGPD para dados pessoais, Lei do SAC para apps de serviço, e regulamentações específicas do setor (saúde, financeiro).

- **Competidores e diferenciação**: Antes de iniciar, mapear os 3-5 principais competidores no segmento, instalar seus apps, avaliar UX, funcionalidades e avaliações nas lojas. Se os competidores já resolvem o problema de forma satisfatória (rating > 4.5, milhões de downloads), a barreira de entrada é alta e a diferenciação precisa ser clara e articulável. Se o cliente não consegue explicar por que o usuário abandonaria o app do competidor para usar o dele, o projeto tem risco de falha de mercado, não apenas risco técnico.

### Perguntas

1. Qual é o modelo de receita previsto — assinatura, freemium, transação, anúncios ou compra in-app? [fonte: Diretoria, Produto] [impacto: Dev, Arquiteto, PM]
2. O app será lançado para iOS, Android ou ambos simultaneamente? Qual a justificativa para a escolha? [fonte: Produto, Marketing, Diretoria] [impacto: Dev, QA, PM]
3. Quem são as 3-5 personas primárias do app (idade, comportamento digital, tipo de dispositivo, qualidade de conexão)? [fonte: Produto, Marketing, Pesquisa] [impacto: Designer, Dev, QA]
4. Quais são os 3-5 principais competidores diretos e qual é a diferenciação planejada? [fonte: Produto, Diretoria, Comercial] [impacto: PM, Designer, Produto]
5. Qual é a expectativa de downloads nos primeiros 3 e 12 meses, e em que dados essa estimativa se baseia? [fonte: Marketing, Produto, Diretoria] [impacto: Arquiteto, DevOps, PM]
6. Existe orçamento para aquisição de usuários (ASO, campanhas pagas, influenciadores) ou o crescimento será orgânico? [fonte: Marketing, Financeiro, Diretoria] [impacto: PM, Marketing, Dev]
7. O projeto substituirá um app existente, migrará de um serviço web, ou será criado completamente do zero? [fonte: Produto, TI, Diretoria] [impacto: Dev, PM, Arquiteto]
8. Qual é o prazo esperado para o lançamento e existe um evento de negócio que o justifica (rodada de investimento, evento, sazonalidade)? [fonte: Diretoria, Produto] [impacto: PM, Dev]
9. Existem requisitos regulatórios específicos do setor (saúde, financeiro, educação) além das políticas das lojas? [fonte: Jurídico, Compliance, Diretoria] [impacto: Dev, Arquiteto, PM]
10. Quem toma decisões de produto e design — existe um Product Owner/Manager dedicado ou decisões são por comitê? [fonte: Diretoria, Produto] [impacto: PM, Designer]
11. O app precisará funcionar offline ou com conectividade intermitente? [fonte: Produto, Marketing] [impacto: Arquiteto, Dev]
12. Há integrações previstas com sistemas externos (CRM, ERP, gateway de pagamento, analytics, redes sociais)? [fonte: TI, Produto, Comercial] [impacto: Dev, Arquiteto, DevOps]
13. O cliente tem time técnico interno ou o app será desenvolvido e mantido inteiramente por terceiros? [fonte: TI, Diretoria, RH] [impacto: PM, Dev, Arquiteto]
14. O app coletará dados pessoais dos usuários? Existe DPO (Data Protection Officer) ou responsável por privacidade? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, Arquiteto, PM]
15. Há expectativa de monetização desde o lançamento ou o foco inicial é apenas aquisição e engajamento? [fonte: Diretoria, Produto, Financeiro] [impacto: PM, Dev]

---

## Etapa 02 — Discovery

- **Jornadas de usuário e fluxos críticos**: Mapear as jornadas completas dos usuários primários — desde o download na loja até a primeira ação de valor (first value moment). O first value moment é o ponto onde o usuário percebe que o app resolve o problema dele: no Uber é a primeira corrida completada, no Duolingo é a primeira lição finalizada. Se o first value moment demora mais de 2-3 sessões para acontecer, a taxa de retenção D7 cairá drasticamente. Mapear também os fluxos secundários que suportam a jornada: onboarding, configurações, suporte, notificações.

- **Métricas de produto e KPIs**: Definir as métricas que indicarão sucesso do app antes de iniciar o build. As métricas fundamentais para apps consumer são: DAU/MAU ratio (engajamento), retenção D1/D7/D30, LTV (Lifetime Value) por cohort, CAC (Customer Acquisition Cost), taxa de conversão do funil de onboarding, crash-free rate (>99.5% é o mínimo aceitável), e tempo de carregamento da tela principal (<2s). Sem métricas definidas, o time não tem como saber se o app está performando bem após o lançamento.

- **Requisitos de onboarding**: O onboarding é o momento mais crítico de um app consumer — 25% dos usuários abandonam após o primeiro uso, e 77% abandonam nos primeiros 3 dias. Definir: o onboarding exige cadastro antes de mostrar valor (high friction) ou permite exploração antes do cadastro (low friction)? Quantos passos tem o fluxo de onboarding? Existe login social (Google, Apple, Facebook)? O Apple Sign In é obrigatório se qualquer outro login social for oferecido (política da Apple desde 2020). O onboarding pede permissões (push, localização, câmera) — em qual momento e com qual justificativa?

- **Notificações push e engajamento**: Push notifications são o principal canal de re-engajamento em apps consumer, mas também o principal motivo de desinstalação quando mal utilizadas. Definir: quais eventos disparam notificações (novo conteúdo, promoção, lembrete, ação social), qual a frequência máxima aceitável, o usuário pode personalizar quais notificações receber (granularidade de opt-in/opt-out), e existe estratégia de segmentação (não enviar a mesma push para todos). A taxa de opt-in de push no iOS é ~50% e no Android ~80% — planejamento do momento de pedir permissão impacta essa taxa significativamente.

- **Requisitos de acessibilidade**: Apps nas lojas públicas devem atender a um público diverso — incluindo pessoas com deficiências visuais, motoras e cognitivas. No iOS, VoiceOver deve funcionar em todas as telas. No Android, TalkBack deve ser funcional. Requisitos específicos: elementos interativos com área de toque mínima de 44x44pt (iOS) e 48x48dp (Android), contraste de cores 4.5:1 para texto, labels descritivos em todos os controles, e suporte a Dynamic Type (iOS) e ajuste de tamanho de fonte (Android). Acessibilidade não é feature opcional — é requisito legal em muitos mercados e afeta diretamente a classificação do app nas lojas.

- **Estratégia de monetização e integração com lojas**: Se o app monetiza via in-app purchase ou assinatura, entender profundamente as regras das lojas: Apple exige uso do StoreKit para qualquer compra de conteúdo digital (comissão de 15-30%), Google exige Google Play Billing para o mesmo. Serviços físicos (delivery, transporte) podem usar gateway próprio sem comissão da loja. Free trials, upgrade/downgrade de planos, e restauração de compras em novo dispositivo são fluxos que devem ser mapeados aqui. A implementação de StoreKit/Play Billing é uma das integrações mais complexas e propensas a erros em apps consumer.

### Perguntas

1. Quais são os 3-5 fluxos críticos do app e qual é o first value moment para o usuário? [fonte: Produto, UX Research] [impacto: Designer, Dev, PM]
2. Quais métricas de produto serão usadas para medir sucesso (DAU/MAU, retenção, LTV, conversão)? [fonte: Produto, Diretoria, Data] [impacto: Dev, PM, Produto]
3. O onboarding exige cadastro antes de mostrar valor ou permite exploração sem login? [fonte: Produto, Marketing] [impacto: Designer, Dev]
4. Quais eventos disparam notificações push e qual a frequência máxima aceitável por tipo de notificação? [fonte: Produto, Marketing] [impacto: Dev, Produto]
5. O app precisará funcionar offline? Se sim, quais funcionalidades devem estar disponíveis sem conexão? [fonte: Produto, Diretoria] [impacto: Arquiteto, Dev]
6. Quais permissões do dispositivo o app precisará (câmera, localização, microfone, galeria, contatos, sensores)? [fonte: Produto, UX] [impacto: Dev]
7. Há requisitos formais de acessibilidade (VoiceOver, TalkBack, WCAG 2.1 AA, Dynamic Type)? [fonte: Jurídico, Compliance, Produto] [impacto: Dev, Designer, QA]
8. Qual é a estratégia de monetização detalhada — quais features são free vs. premium, qual o preço dos planos? [fonte: Produto, Financeiro, Diretoria] [impacto: Dev, PM]
9. Existe conteúdo legado (de app anterior ou serviço web) que precisará ser migrado? Qual o volume? [fonte: TI, Produto] [impacto: Dev, PM]
10. Quais integrações externas são obrigatórias no MVP (pagamento, analytics, crash reporting, chat, social login)? [fonte: Produto, TI, Marketing] [impacto: Dev, Arquiteto]
11. O app terá sistema de avaliação/review interno (rating de produtos, serviços, conteúdo)? [fonte: Produto] [impacto: Dev, Designer]
12. Qual é o público-alvo geográfico e isso implica requisitos de localização (idiomas, moedas, formatos de data)? [fonte: Marketing, Produto, Comercial] [impacto: Dev, Conteúdo]
13. Há requisitos de LGPD/GDPR — consentimento de cookies, política de privacidade, exclusão de dados pelo usuário? [fonte: Jurídico, DPO, Compliance] [impacto: Dev, Arquiteto]
14. O app precisará de deep links (abertura direta em tela específica via URL para campanhas e compartilhamento)? [fonte: Marketing, Produto] [impacto: Dev]
15. Existe orçamento e cronograma definidos para produção de conteúdo inicial (textos, imagens, vídeos do app)? [fonte: Produto, Marketing, Financeiro] [impacto: PM, Designer]

---

## Etapa 03 — Alignment

- **Decisão cross-platform vs. nativo**: Esta é a decisão arquitetural mais impactante do projeto e deve ser tomada com critérios técnicos claros, não por preferência do time. Cross-platform (React Native, Flutter) reduz custo de manutenção de dois codebases e permite time único, mas tem limitações em integrações profundas com hardware (BLE avançado, câmera com processamento em tempo real, ARKit/ARCore). Nativo (Swift/Kotlin) oferece performance máxima e acesso irrestrito a APIs do SO, mas exige dois times ou um time fluente em ambas as plataformas, e dobra o esforço de manutenção. A decisão deve considerar: quais APIs nativas o app precisa, qual o perfil do time disponível, e qual o budget de manutenção de longo prazo.

- **Alinhamento de escopo do MVP**: Apps consumer sofrem de feature creep mais do que qualquer outro tipo de projeto — o cliente quer competir com apps maduros que têm anos de desenvolvimento. Definir com rigor o que entra no MVP (funcionalidades sem as quais o app não faz sentido lançar) e o que vai para o backlog (funcionalidades que agregam valor mas não são prerequisito). O critério deve ser: "o usuário consegue atingir o first value moment apenas com as features do MVP?" Se sim, o escopo está correto. Se não, algo essencial está faltando.

- **Design system e linguagem visual**: Alinhar se o app seguirá as guidelines de plataforma (Human Interface Guidelines da Apple, Material Design do Google) ou terá design custom. Seguir guidelines de plataforma reduz o estranhamento do usuário e acelera o desenvolvimento (componentes nativos prontos), mas limita a identidade visual. Design custom oferece diferenciação mas aumenta o esforço de build e pode resultar em UX não-idiomática (gestos e padrões que o usuário não reconhece). A decisão mais comum é design custom com respeito aos padrões fundamentais de navegação de cada plataforma.

- **Estratégia de versionamento e atualizações**: Diferentemente de web, atualizações de app dependem do usuário instalar a nova versão — e nem todos atualizam. Isso significa que múltiplas versões do app coexistem em produção simultaneamente. Alinhar: a API do backend será versionada para suportar versões antigas do app? Existe versão mínima obrigatória (force update)? Qual a política de deprecação de versões antigas? Sem essa estratégia definida, o backend acumula lógica de compatibilidade retroativa que se torna impossível de manter.

- **Processo de revisão e aprovação de entregas**: Definir como o cliente acompanhará o progresso durante o build — builds de teste internos (TestFlight para iOS, Internal Testing do Google Play), demos em vídeo, ou sessões presenciais. O ciclo de feedback em app é mais lento que em web (cada build de teste exige compilação, upload, instalação), então alinhar expectativas sobre frequência de entregas parciais é crítico. Sprints de 2 semanas com build de teste entregue ao final de cada sprint é o padrão que equilibra velocidade e visibilidade.

### Perguntas

1. A decisão entre cross-platform (React Native/Flutter) e nativo (Swift/Kotlin) foi tomada com base em requisitos técnicos documentados? [fonte: TI, Dev, Arquiteto] [impacto: Dev, PM]
2. O escopo do MVP foi definido e aprovado com critério claro de corte (first value moment atingível)? [fonte: Produto, Diretoria] [impacto: PM, Dev, Designer]
3. O design seguirá guidelines de plataforma (HIG/Material Design) ou será custom? A decisão está justificada? [fonte: Designer, Produto] [impacto: Dev, Designer]
4. O design cobre ambas as plataformas (iOS e Android) com as diferenças de padrão de cada uma? [fonte: Designer] [impacto: Dev, QA]
5. O design inclui todos os estados de tela (loading, empty, error, success, offline)? [fonte: Designer] [impacto: Dev]
6. A estratégia de versionamento de API e force update de app foi definida? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps]
7. O processo de entrega e revisão durante o build está alinhado (frequência de builds de teste, canal de feedback)? [fonte: Produto, Diretoria, PM] [impacto: PM, Dev]
8. O modelo de manutenção pós-lançamento foi formalizado (equipe interna, contrato com terceiro, SLA)? [fonte: Diretoria, Financeiro] [impacto: PM, Dev]
9. As dependências externas críticas (assets, conteúdo, aprovações, integrações) foram listadas com prazos? [fonte: Produto, Marketing, TI] [impacto: PM]
10. O SLA de publicação nas lojas foi considerado no cronograma (Apple Review leva 24-48h, pode rejeitar)? [fonte: Dev, PM] [impacto: PM, Dev]
11. O cliente entende que atualizações do app dependem do usuário e que múltiplas versões coexistem? [fonte: Produto, Diretoria] [impacto: Dev, Arquiteto, PM]
12. O time de desenvolvimento tem contas de desenvolvedor ativas nas lojas (Apple Developer Program $99/ano, Google Play $25 única)? [fonte: TI, Financeiro] [impacto: Dev, DevOps]
13. O fluxo de beta testing foi definido (TestFlight, Google Play Internal Testing, Firebase App Distribution)? [fonte: Produto, QA] [impacto: Dev, QA, PM]
14. O cliente foi informado sobre o impacto da comissão das lojas (15-30%) no modelo de receita? [fonte: Financeiro, Produto, Diretoria] [impacto: PM, Produto]
15. O cliente foi informado sobre o impacto de mudanças de escopo no prazo e custo, especialmente em mobile onde recompilação e review são lentos? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Mapa de telas e navegação**: Produzir o mapa completo de telas com hierarquia de navegação (tab bar, stack navigation, drawer, modal), relações entre telas (qual tela leva a qual), e comportamento do botão back em cada nível. O mapa de telas é o artefato que permite estimar o esforço de build com precisão — cada tela distinta representa um componente a ser implementado — e é a base para o planejamento de QA. Em apps consumer, a navegação deve ser intuitiva ao ponto de dispensar instrução: se o usuário precisa pensar para onde ir, a navegação está errada.

- **Modelo de dados e estados**: Para cada funcionalidade, definir os modelos de dados (entidades, campos, tipos, relações) e os estados possíveis. Exemplo: um pedido em app de marketplace tem estados criado → pagamento_pendente → pago → em_preparo → enviado → entregue → avaliado → cancelado → reembolsado, e cada estado tem regras de transição, permissões de ação (quem pode cancelar em qual estado) e reflexos na UI (cor, ícone, ações disponíveis). Estados mal definidos geram bugs de lógica que são difíceis de reproduzir e caros de corrigir.

- **Fluxo de autenticação e segurança**: Definir o fluxo completo de autenticação — cadastro (e-mail+senha, telefone+OTP, social login), login, recuperação de senha, verificação de e-mail/telefone, biometria (Face ID, Touch ID, fingerprint), e logout. Definir também a estratégia de sessão: token JWT com refresh token, duração da sessão, comportamento quando o token expira (refresh silencioso ou force re-login), e armazenamento seguro de credenciais (Keychain no iOS, EncryptedSharedPreferences no Android). Falhas de segurança em autenticação de app consumer são particularmente graves por afetarem dados pessoais de potencialmente milhões de usuários.

- **Especificação de notificações**: Mapear cada tipo de notificação push com: evento gatilho, título e corpo da mensagem, ação ao tocar (qual tela abre, deep link), prioridade (alta = alerta imediato, normal = badge silencioso), segmentação (para quem), throttling (frequência máxima por tipo), e opt-in/opt-out granular. Incluir também notificações locais (lembretes, alertas offline) e in-app notifications (banners dentro do app quando o usuário já está usando). A especificação deve ser detalhada o suficiente para que o backend consiga implementar o sistema de envio e o mobile consiga implementar o handling de cada tipo.

- **Fluxo de pagamento (se aplicável)**: Se o app envolve transações financeiras, especificar o fluxo completo: seleção de método de pagamento (cartão, PIX, boleto, wallet do app), captura de dados de cartão (via tokenização do gateway — nunca armazenar dados de cartão no app), processamento (síncrono ou assíncrono), confirmação, e tratamento de falhas (cartão recusado, timeout, fraude detectada). Definir também: reembolso (automático ou manual), estorno parcial, e recibo/comprovante. PCI-DSS compliance exige que dados de cartão nunca transitem pelo backend do app — apenas tokens do gateway.

- **Estratégia de deep linking e ASO**: Deep links permitem que URLs externas (campanhas, e-mails, compartilhamentos) abram diretamente uma tela específica do app — ou a loja se o app não estiver instalado (deferred deep link). Definir: quais telas terão deep links, o formato das URLs (Universal Links no iOS, App Links no Android), e o comportamento de fallback (web ou loja). Para ASO (App Store Optimization), definir os keywords, screenshots, vídeo de preview, e textos de descrição da loja — que devem ser especificados nesta etapa para evitar correria no Launch Prep.

### Perguntas

1. O mapa de telas completo foi produzido e validado, incluindo hierarquia de navegação e todos os fluxos de usuário? [fonte: Produto, Designer] [impacto: Dev, QA, PM]
2. Os modelos de dados foram definidos com todos os campos, tipos, validações e estados possíveis por entidade? [fonte: Produto, Arquiteto] [impacto: Dev, Arquiteto]
3. O fluxo de autenticação foi especificado end-to-end (cadastro, login, social, recuperação, biometria, logout)? [fonte: Produto, Arquiteto] [impacto: Dev]
4. A estratégia de sessão e armazenamento seguro de tokens foi definida (JWT, refresh, duração, Keychain/Encrypted)? [fonte: Arquiteto, Dev] [impacto: Dev]
5. Cada tipo de notificação push foi especificado (gatilho, mensagem, ação, prioridade, segmentação, throttling)? [fonte: Produto, Marketing] [impacto: Dev]
6. O fluxo de pagamento foi especificado com todas as etapas, métodos e tratamento de falhas (se aplicável)? [fonte: Produto, Financeiro, Jurídico] [impacto: Dev, Arquiteto]
7. As telas com deep link foram identificadas e o formato das URLs foi definido (Universal Links, App Links)? [fonte: Marketing, Produto] [impacto: Dev]
8. Os conteúdos da loja (screenshots, vídeo preview, descrição, keywords) foram especificados para ASO? [fonte: Marketing, Produto] [impacto: Designer, Marketing]
9. Existe wireframe ou protótipo navegável aprovado antes de avançar para o design de alta fidelidade? [fonte: Designer, Produto] [impacto: Dev, PM]
10. Os breakpoints e comportamentos para diferentes tamanhos de tela foram definidos (iPhone SE vs. Pro Max, tablets)? [fonte: Designer] [impacto: Dev, QA]
11. Os fluxos de erro e edge cases foram mapeados (sem conexão, timeout, permissão negada, sessão expirada)? [fonte: Produto, Designer] [impacto: Dev]
12. O volume de dados iniciais foi estimado e o esforço de seed/migração foi incluído no cronograma? [fonte: TI, Produto] [impacto: Dev, PM]
13. Os termos de uso e política de privacidade foram redigidos e aprovados pelo jurídico? [fonte: Jurídico, Compliance] [impacto: Dev, PM]
14. As regras de moderação de conteúdo gerado por usuário foram definidas (se aplicável)? [fonte: Produto, Jurídico] [impacto: Dev, PM]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders antes do início do Setup? [fonte: Diretoria, Produto] [impacto: PM, Dev, Designer]

---

## Etapa 05 — Architecture

- **Escolha do framework mobile**: A seleção do framework define o ecossistema de desenvolvimento e as capacidades técnicas do app. React Native é indicado quando o time já trabalha com React/TypeScript, quando o app não exige integrações profundas com hardware, e quando velocidade de iteração é prioridade — hot reload e ecossistema JavaScript maduro. Flutter é indicado quando performance visual é prioridade (renderização própria, animações complexas), quando o time pode aprender Dart, e quando consistência visual pixel-perfect entre plataformas é requisito. Nativo (SwiftUI + Jetpack Compose) é indicado quando há requisitos de hardware avançado (BLE complexo, câmera com ML, AR), quando performance é absolutamente crítica, ou quando o budget permite dois times independentes.

- **Arquitetura do backend e API**: O backend de um app consumer deve ser desenhado para mobile-first — payloads JSON enxutos (não reutilizar APIs web pesadas), paginação eficiente (cursor-based, não offset), e versionamento de API para suportar apps antigos em produção. Opções: Firebase/Supabase para MVPs rápidos com funcionalidades built-in (auth, database, storage, push), Node.js/Python com PostgreSQL para controle total, ou BaaS + serverless functions para escalar sem gerenciar servidores. A decisão deve considerar: complexidade da lógica de negócio (Firebase é limitado para regras complexas), necessidade de busca full-text, e projeção de custo em escala.

- **Estratégia de cache e offline**: Apps consumer devem ser resilientes a conexão instável — o usuário espera que o app funcione no metrô, no elevador, e em áreas com sinal fraco. Definir: quais dados são cacheados localmente (SQLite, Realm, Hive, AsyncStorage), por quanto tempo o cache é válido (TTL), qual a estratégia de sync quando a conexão volta (last-write-wins, merge, conflict resolution), e quais funcionalidades ficam disponíveis offline (leitura de dados cacheados, criação de drafts que sincronizam depois). O nível de offline exigido impacta diretamente a complexidade da arquitetura.

- **Infraestrutura de push notifications**: Definir a stack de push: Firebase Cloud Messaging (FCM) para Android (obrigatório) e iOS (via APNs bridge), ou APNs direto para iOS com FCM para Android. Para envio segmentado e automatizado, considerar serviços como OneSignal, Braze ou Customer.io — que oferecem segmentação por comportamento, A/B testing de mensagens, e analytics de engajamento. A infraestrutura de push precisa lidar com: tokens de dispositivo que mudam, usuários com múltiplos dispositivos, opt-out por tipo de notificação, e rate limiting para não ser bloqueado pelas plataformas.

- **Monitoramento e crash reporting**: Apps consumer com crash-free rate abaixo de 99.5% perdem posição no ranking das lojas e recebem avaliações negativas. Configurar desde a arquitetura: crash reporting (Firebase Crashlytics é o padrão da indústria — gratuito, real-time, com stack traces simbolizados), performance monitoring (tempo de inicialização do app, tempo de resposta de API, renderização de frames), e analytics de produto (Amplitude, Mixpanel ou Firebase Analytics para rastrear funis e retenção). Esses serviços devem ser configurados como componente obrigatório da arquitetura, não como afterthought.

- **Segurança e proteção de dados**: Apps consumer armazenam dados pessoais sensíveis e estão sujeitos a ataques específicos de mobile: reverse engineering do APK/IPA (obfuscação e certificate pinning como mitigação), man-in-the-middle (TLS obrigatório, certificate pinning), e acesso físico ao dispositivo (biometria, Keychain/EncryptedSharedPreferences). Definir também: criptografia de dados em repouso (database local criptografado se houver dados sensíveis), política de expiração de sessão, e mecanismo de revogação remota de acesso (block device/user). Para apps com dados de saúde ou financeiros, os requisitos de segurança são significativamente mais rigorosos.

- **Pipeline de CI/CD mobile**: Build e deploy de apps mobile é significativamente mais complexo que web — envolve compilação nativa, assinatura de certificados, upload para lojas. Definir: CI/CD tool (Fastlane como standard para automação de build/deploy, GitHub Actions ou Bitrise como CI runner), gerenciamento de certificados e provisioning profiles (match do Fastlane para iOS), distribuição de builds de teste (TestFlight via Fastlane, Firebase App Distribution), e processo de submissão para as lojas (automático ou manual com checklist). O pipeline deve ser configurado desde o início — configurar Fastlane retroativamente em projeto avançado é doloroso.

### Perguntas

1. O framework mobile escolhido (React Native, Flutter, nativo) atende todos os requisitos técnicos identificados na Discovery? [fonte: Dev, Arquiteto] [impacto: Dev]
2. A arquitetura do backend foi desenhada mobile-first (payloads enxutos, paginação eficiente, API versionada)? [fonte: Arquiteto, Dev backend] [impacto: Dev]
3. A estratégia de cache e offline foi definida com escopo claro do que funciona sem conexão e como o sync acontece? [fonte: Arquiteto, Produto] [impacto: Dev]
4. A infraestrutura de push notifications foi desenhada com suporte a segmentação e rate limiting? [fonte: Arquiteto, Produto] [impacto: Dev, DevOps]
5. Crash reporting e performance monitoring estão incluídos na arquitetura como componentes obrigatórios? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
6. A estratégia de segurança foi definida (certificate pinning, criptografia local, biometria, sessão)? [fonte: Arquiteto, Segurança] [impacto: Dev]
7. O pipeline de CI/CD mobile foi desenhado (Fastlane, certificados, TestFlight, Firebase App Distribution)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
8. A estratégia de versionamento de API foi definida para suportar múltiplas versões do app em produção? [fonte: Arquiteto] [impacto: Dev backend]
9. Os custos mensais de infraestrutura foram projetados em cenário esperado e pior caso (pico de downloads)? [fonte: Financeiro, DevOps, Arquiteto] [impacto: PM, DevOps]
10. A arquitetura suporta o crescimento previsto (10x usuários) sem redesign fundamental? [fonte: Arquiteto] [impacto: Dev, DevOps]
11. A solução de analytics de produto foi escolhida (Amplitude, Mixpanel, Firebase Analytics) e os eventos principais mapeados? [fonte: Produto, Marketing] [impacto: Dev]
12. O modelo de branches e ambientes (production, staging, dev) foi desenhado e documentado? [fonte: Dev, DevOps] [impacto: Dev]
13. A estratégia de feature flags foi definida para controlar rollout gradual e experimentos A/B? [fonte: Produto, Arquiteto] [impacto: Dev]
14. A solução de armazenamento de mídia (imagens de perfil, uploads do usuário) foi definida (S3, Firebase Storage, Cloudinary)? [fonte: Arquiteto] [impacto: Dev, DevOps]
15. O ADR (Architecture Decision Record) foi produzido documentando todas as decisões e justificativas desta etapa? [fonte: Arquiteto] [impacto: Dev, PM]

---

## Etapa 06 — Setup

- **Estrutura do projeto mobile**: Organizar o projeto com separação clara entre camadas: UI/presentation (telas, componentes, navegação), domain/business logic (use cases, entidades, regras), data (repositories, API clients, local storage), e infrastructure (DI, configurações, constants). Em React Native, a estrutura por feature é geralmente preferida (cada feature tem suas telas, hooks, e stores). Em Flutter, clean architecture com camadas é o padrão. A estrutura definida aqui será seguida durante todo o build — mudar midway é custoso e gera inconsistência.

- **Configuração de ambientes**: Configurar pelo menos 3 ambientes: development (API local ou de staging, sem dados reais, debug habilitado), staging (API de staging, dados de teste realistas, build de release para testar performance real), e production (API de produção, dados reais, build de release otimizado). Cada ambiente deve ter suas próprias variáveis (API URL, API keys, analytics ID) configuradas via arquivo de ambiente (.env) ou build flavors (Android) / schemes (iOS). Nunca hardcodar URLs ou keys no código.

- **Setup de certificados e signing**: Para iOS: criar App ID no Apple Developer Portal, gerar certificados de distribuição e development, criar provisioning profiles para cada ambiente (development, ad-hoc, App Store), e configurar no Xcode ou via Fastlane match. Para Android: gerar keystore de upload, configurar signing configs no Gradle para debug e release, e salvar a keystore em local seguro (não no repositório). Perder a keystore do Android ou o certificado do iOS impede atualizações do app — backup seguro é obrigatório.

- **Configuração de contas nas lojas**: Criar ou verificar o Apple Developer Program (US$99/ano, requer D-U-N-S Number para empresas) e o Google Play Console (US$25 taxa única). Criar o app listing em ambas as lojas (nome, bundle ID, categoria) para reservar o nome e habilitar funcionalidades como TestFlight e Internal Testing. Configurar o IAP (In-App Purchase) sandbox se o app tiver compras. Estas configurações devem ser feitas com antecedência — a aprovação do Apple Developer Program para empresas pode levar de 2 a 14 dias.

- **Pipeline de CI/CD com Fastlane**: Configurar Fastlane para automatizar: build de desenvolvimento (para distribuição interna), build de staging (TestFlight/Firebase App Distribution), e build de produção (App Store Connect/Google Play Console). Configurar lanes para cada fluxo: `fastlane ios beta` para TestFlight, `fastlane android beta` para Firebase App Distribution. Integrar com GitHub Actions ou Bitrise para execução automática em push/PR. O pipeline deve incluir: lint, testes unitários, build com sucesso, e upload automático para distribuição de teste.

- **Distribuição de builds de teste**: Configurar o canal de distribuição de builds de teste para stakeholders e QA. TestFlight para iOS (até 10.000 testers externos, aprovação da Apple em ~24h para primeiro build). Firebase App Distribution para Android (e opcionalmente iOS). Criar grupo de testers com todos os stakeholders, QA, e membros do time de produto. Enviar o primeiro build de teste com a tela de splash screen e login básico funcionando — confirmar que todos conseguem instalar e abrir o app antes de iniciar o build de features.

### Perguntas

1. A estrutura de pastas do projeto foi definida, documentada e seguida desde o primeiro commit? [fonte: Dev] [impacto: Dev]
2. Os ambientes (development, staging, production) foram configurados com variáveis separadas por ambiente? [fonte: Dev, DevOps] [impacto: Dev]
3. Os certificados de signing foram gerados, configurados e armazenados em local seguro com backup? [fonte: Dev, DevOps] [impacto: Dev]
4. As contas nas lojas (Apple Developer Program, Google Play Console) estão ativas e o app listing foi criado? [fonte: TI, Financeiro] [impacto: Dev, PM]
5. O Fastlane está configurado com lanes para build, teste e distribuição em ambas as plataformas? [fonte: Dev, DevOps] [impacto: Dev]
6. O TestFlight e/ou Firebase App Distribution estão configurados com grupo de testers criado e funcional? [fonte: Dev, QA] [impacto: Dev, QA, PM]
7. O primeiro build de teste foi distribuído e todos os testers confirmaram instalação com sucesso? [fonte: QA, Produto] [impacto: Dev, PM]
8. O .gitignore está configurado para excluir secrets, keystores, .env, e arquivos gerados no build? [fonte: Dev] [impacto: Dev, DevOps]
9. O crash reporting (Firebase Crashlytics) está integrado e enviando eventos de teste com sucesso? [fonte: Dev] [impacto: Dev, QA]
10. O analytics de produto está integrado e rastreando ao menos o evento de abertura do app? [fonte: Dev, Produto] [impacto: Dev, Produto]
11. O push notification service (FCM/APNs) está configurado e um push de teste foi recebido com sucesso? [fonte: Dev] [impacto: Dev]
12. O backend está deployado em ambiente de staging com dados de teste e API documentada? [fonte: Dev backend, DevOps] [impacto: Dev]
13. O processo de onboarding de novos desenvolvedores foi documentado no README com instruções de setup local? [fonte: Dev] [impacto: Dev]
14. O ambiente de staging está completamente isolado do production em dados, APIs e configurações? [fonte: Dev, DevOps] [impacto: Dev, QA]
15. O pipeline de CI/CD foi testado end-to-end — push → build → testes → distribuição automática? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Sistema de componentes e design system**: Implementar os componentes base do design system — tipografia (escala de tamanhos, pesos, suporte a Dynamic Type), paleta de cores como tokens (light/dark mode se aplicável), espaçamento sistemático, e componentes atômicos reutilizáveis (Button com variantes, Card, Input, Avatar, Badge, Toast/Snackbar, Bottom Sheet). O dark mode não é "feature" — é expectativa de plataforma desde iOS 13 e Android 10. Componentes bem estruturados desde o início garantem consistência visual e reduzem o tempo de implementação de novas telas.

- **Navegação e fluxos de usuário**: Implementar a estrutura de navegação definida no mapa de telas — tab bar (ou bottom navigation), stack navigation dentro de cada tab, modais, e drawer se aplicável. A navegação em apps consumer deve ser previsível: o botão back deve sempre fazer o que o usuário espera, deep links devem abrir a tela correta com o estado correto, e o estado de navegação deve sobreviver a rotação de tela e background/foreground do app. Testar navegação com cenários complexos: deep link enquanto logado vs. deslogado, push notification que abre tela específica, e volta de background após 30 minutos.

- **Integração com APIs e tratamento de estados**: Implementar a camada de comunicação com o backend com tratamento robusto de todos os estados: loading (skeleton ou spinner — não tela em branco), success (dados renderizados), error (mensagem amigável com opção de retry, não stack trace), empty (estado vazio com CTA para ação, não "nenhum resultado"), e offline (dados cacheados com indicador de que são offline). Cada chamada de API deve ter timeout configurado (10s é razoável para mobile em 3G), retry automático para erros de rede (com backoff exponencial), e cancellation quando o usuário sai da tela.

- **Implementação de autenticação e segurança**: Implementar o fluxo completo de autenticação conforme especificado: social login (Google Sign-In, Apple Sign In — obrigatório se qualquer social login é oferecido), e-mail/senha com validação robusta, OTP por SMS/WhatsApp se aplicável, biometria como atalho de login (não como método primário). Armazenar tokens de forma segura (Keychain no iOS, EncryptedSharedPreferences no Android — nunca AsyncStorage ou SharedPreferences não criptografado). Implementar refresh de token silencioso para que o usuário não precise re-logar em uso normal.

- **Push notifications e deep links**: Implementar o handling completo de push notifications: recebimento em foreground (banner in-app ou sistema, dependendo do tipo), recebimento em background (badge e notification center), e tap handling (navegar para a tela correta via deep link). Implementar Universal Links (iOS) e App Links (Android) para deep linking HTTP, e custom scheme para deep linking interno. Testar cenários complexos: push recebida com app fechado, push recebida com usuário deslogado (deve ir para login e depois para a tela destino), e multiple pushes empilhadas.

- **Performance e otimização**: Apps consumer com tempo de inicialização acima de 3 segundos ou listas com scroll não-fluido (abaixo de 60fps) recebem avaliações negativas e são desinstalados. Otimizar desde o build: lazy loading de telas e componentes pesados, otimização de imagens (thumbnails para listas, full resolution apenas em detalhe), virtualização de listas longas (FlatList no React Native, ListView.builder no Flutter), e redução do tamanho do bundle (tree shaking, remoção de dependências não utilizadas). Monitorar o tamanho do app — cada MB acima de 100MB reduz a taxa de download em mercados com conexão lenta.

- **Testes automatizados**: Implementar testes em camadas: testes unitários para lógica de negócio (validações, transformações de dados, regras de estado), testes de integração para comunicação com API (mocking de responses), e testes de UI para fluxos críticos (onboarding, login, fluxo principal de valor). A cobertura de testes em apps consumer é frequentemente negligenciada pela pressão de prazo, mas bugs em produção em app mobile são muito mais caros de corrigir do que em web (cada fix exige nova submissão e aprovação da loja).

### Perguntas

1. Todos os componentes base do design system foram implementados, incluindo suporte a Dynamic Type e dark mode? [fonte: Designer] [impacto: Dev]
2. A navegação está funcionando corretamente com deep links, push handling, back button, e estado preservado após background? [fonte: Produto, QA] [impacto: Dev]
3. Todos os estados de API estão implementados em cada tela (loading, success, error, empty, offline)? [fonte: Designer, Produto] [impacto: Dev, QA]
4. A autenticação está implementada end-to-end com social login, biometria e armazenamento seguro de tokens? [fonte: Arquiteto, QA] [impacto: Dev]
5. O push notification handling está implementado para todos os cenários (foreground, background, tap, user deslogado)? [fonte: Dev, QA] [impacto: Dev]
6. O pipeline de otimização de imagens está funcionando (thumbnails em listas, full resolution em detalhe, cache)? [fonte: Dev] [impacto: Dev, QA]
7. As listas longas estão virtualizadas e o scroll está fluido a 60fps em dispositivos de entrada? [fonte: Dev, QA] [impacto: Dev]
8. O tempo de inicialização do app está abaixo de 3 segundos em dispositivos de entrada (cold start)? [fonte: Dev, QA] [impacto: Dev]
9. Os testes unitários cobrem a lógica de negócio crítica (autenticação, pagamento, estados de entidade)? [fonte: Dev] [impacto: Dev, QA]
10. Os formulários têm validação client-side com mensagens de erro claras e acessíveis? [fonte: Designer, Produto] [impacto: Dev]
11. O fluxo de pagamento está implementado end-to-end com tratamento de todos os cenários de falha (se aplicável)? [fonte: Produto, QA] [impacto: Dev]
12. A acessibilidade está sendo implementada ao longo do build (VoiceOver, TalkBack, contrast, touch targets)? [fonte: Designer, Compliance] [impacto: Dev, QA]
13. O tamanho do app está dentro do aceitável (<100MB para download over cellular no iOS)? [fonte: Dev] [impacto: Dev]
14. O conteúdo real está sendo usado nos testes de UI para revelar problemas de layout? [fonte: Produto, Marketing] [impacto: Dev, Designer]
15. Os builds de teste estão sendo entregues ao stakeholder com frequência alinhada (sprint) e feedback está sendo incorporado? [fonte: Produto, PM] [impacto: PM, Dev]

---

## Etapa 08 — QA

- **Teste em dispositivos reais**: Simuladores e emuladores não capturam problemas reais de performance, memória, bateria e conectividade. Testar em pelo menos: iPhone SE (tela pequena, hardware limitado) e iPhone 14/15 (tela grande, hardware moderno) para iOS; dispositivo Android de entrada (2-3GB RAM, processador budget) e flagship Samsung/Pixel para Android. O app deve funcionar de forma aceitável no dispositivo de menor especificação do público-alvo — se o público é classe C no Brasil, o dispositivo de teste deve refletir essa realidade (Samsung Galaxy A-series, Motorola Moto G).

- **Teste de performance e bateria**: Monitorar consumo de CPU, memória e bateria durante uso típico (30 minutos de sessão). Apps que consomem mais de 5% de bateria em 30 minutos de uso ativo são flagged como "battery drainer" nos rankings de sistema (iOS e Android). Testar: memory leaks em navegação repetida (ir e voltar entre telas 50 vezes), performance de scroll em listas com 1000+ itens, e tempo de resposta de API em condições de rede degradada (Network Link Conditioner no iOS, Charles Proxy para throttling). O Instruments (iOS) e Android Profiler são ferramentas essenciais para diagnóstico.

- **Teste de conectividade e offline**: Testar o app em cenários reais de conectividade: sem conexão (modo avião), conexão lenta (3G/Edge simulado), perda de conexão durante operação (desligar Wi-Fi enquanto carrega lista), e recuperação de conexão (reconexão automática após offline). Verificar que o app não crasha em nenhum cenário de conectividade, que dados cacheados são exibidos quando offline, e que operações pendentes (drafts, uploads) sincronizam corretamente quando a conexão retorna. Este é um dos testes mais frequentemente negligenciados e uma das maiores fontes de 1-star reviews.

- **Teste de edge cases de autenticação**: Testar cenários que só aparecem em produção: token expirado durante uso (refresh automático funciona?), login em novo dispositivo (sessão anterior é invalidada?), desinstalação e reinstalação (estado limpo, sem dados residuais), e login simultâneo em múltiplos dispositivos (suportado ou bloqueado?). Testar também: Apple Sign In com e-mail relay (endereço @privaterelay.appleid.com), social login com conta sem e-mail público, e cadastro com caracteres especiais no nome (acentos, emojis, caracteres CJK).

- **Teste de notificações push**: Testar push notifications em todos os cenários: app em foreground (banner in-app), app em background (notification center), app fechado (cold start após tap), permissão negada (degradação graciosa sem crash), e tap em push antiga (conteúdo referenciado ainda existe?). Testar em ambas as plataformas separadamente — o comportamento de push é fundamentalmente diferente entre iOS e Android. Verificar que o badge count está correto, que push com deep link abre a tela correta, e que o throttling funciona (não envia 10 pushes em 1 minuto).

- **Teste de acessibilidade**: Testar com VoiceOver (iOS) e TalkBack (Android) ativados — navegar por todas as telas usando apenas gestos de acessibilidade. Verificar: todos os elementos interativos são anunciados corretamente com label descritivo, a ordem de foco é lógica (top-to-bottom, left-to-right), ações de swipe e gestos customizados têm equivalentes acessíveis, e Dynamic Type (iOS) e ajuste de fonte (Android) não quebram o layout com texto 200% maior. Este teste deve ser feito por alguém que entende de acessibilidade, não apenas "ligou o VoiceOver e pareceu funcionar".

- **Teste de compliance das lojas**: Antes de submeter, verificar manualmente contra as guidelines: Apple App Review Guidelines (especialmente seções sobre privacy, in-app purchase, e login) e Google Play Developer Policy. Itens mais comuns de rejeição: ausência de Apple Sign In quando há social login, link para política de privacidade que não funciona ou está em branco, uso de API privada (mais comum em nativo), funcionalidade que depende de instalação de outro app sem fallback, e conteúdo que viola as políticas (gambling, adult content, misleading features).

### Perguntas

1. O app foi testado em dispositivos reais cobrindo o range de especificações do público-alvo (entrada e flagship)? [fonte: QA, Dev] [impacto: Dev, QA]
2. O teste de performance confirmou consumo aceitável de CPU, memória e bateria em sessão de 30 minutos? [fonte: QA, Dev] [impacto: Dev]
3. O app foi testado em cenários de conectividade degradada (offline, 3G, perda de conexão durante uso)? [fonte: QA] [impacto: Dev]
4. Os edge cases de autenticação foram testados (token expirado, novo dispositivo, reinstalação, social login edge cases)? [fonte: QA, Dev] [impacto: Dev]
5. As notificações push foram testadas em todos os cenários (foreground, background, closed, permissão negada)? [fonte: QA, Dev] [impacto: Dev]
6. O teste de acessibilidade com VoiceOver e TalkBack foi realizado em todas as telas principais? [fonte: QA, Compliance] [impacto: Dev]
7. O teste de Dynamic Type e ajuste de fonte foi realizado sem quebra de layout (200% de aumento)? [fonte: QA, Designer] [impacto: Dev]
8. A revisão contra as guidelines das lojas (Apple App Review, Google Play Policy) foi feita e não há violações? [fonte: Dev, QA] [impacto: Dev, PM]
9. Os deep links foram testados em todos os cenários (app instalado, não instalado, logado, deslogado)? [fonte: QA, Dev] [impacto: Dev]
10. O fluxo de pagamento foi testado end-to-end em sandbox com cartões de teste e cenários de falha (se aplicável)? [fonte: QA, Produto] [impacto: Dev]
11. O crash-free rate em staging está acima de 99.5% com uso intensivo durante a fase de QA? [fonte: Dev, QA] [impacto: Dev]
12. Os testes automatizados (unit + integration) estão passando e cobrem os fluxos críticos? [fonte: Dev] [impacto: Dev, QA]
13. O tamanho do app foi verificado e está dentro dos limites aceitáveis para download over cellular? [fonte: Dev] [impacto: Dev]
14. A revisão de conteúdo do app (textos, labels, mensagens de erro) foi concluída com termos consistentes? [fonte: Produto, QA] [impacto: Designer, Produto]
15. O fluxo completo de onboarding foi testado por alguém que não participou do desenvolvimento (teste cego)? [fonte: Produto, QA] [impacto: Designer, Produto]

---

## Etapa 09 — Launch Prep

- **Preparação da App Store e Google Play**: Preparar todos os metadados das lojas com antecedência — não no dia da submissão. Apple App Store: nome (30 chars), subtítulo (30 chars), keywords (100 chars), descrição (4000 chars), screenshots por device size (6.7", 6.5", 5.5" no mínimo), preview video (opcional mas recomendado), categoria, age rating, app privacy details (nutrition label), e URL de suporte. Google Play: título (30 chars), short description (80 chars), full description (4000 chars), screenshots (mínimo 2, máximo 8), feature graphic (1024x500), categoria, content rating questionnaire, e data safety section. Os textos devem ser otimizados para ASO.

- **Submissão para review e tempo de aprovação**: A Apple App Review leva de 24h a 7 dias (média 48h), mas o primeiro app de uma conta nova ou apps com funcionalidades sensíveis (saúde, finanças, menores) podem levar mais. A Google Play review é geralmente mais rápida (horas a 3 dias) mas pode rejeitar retroativamente (após aprovação). Submeter com antecedência suficiente para pelo menos uma rodada de rejeição e correção. As causas mais comuns de rejeição: crashs detectados pelo reviewer, funcionalidade de login que não funciona na review, screenshots que não correspondem ao app real, e ausência de mecanismo de delete account (obrigatório desde 2022 na Apple e 2024 no Google).

- **Configuração de analytics e eventos de conversão**: Configurar analytics de produto e marketing antes do lançamento — dados do dia 1 são irrecuperáveis. Firebase Analytics ou Amplitude para eventos de produto (onboarding_completed, first_purchase, feature_used). Adjust, AppsFlyer ou Branch para attribution de campanhas de aquisição (de qual canal o usuário veio). Facebook SDK e Google Ads SDK para eventos de conversão de campanhas pagas. Cada evento deve ser mapeado, implementado, e validado com dados reais em ambiente de staging antes do go-live.

- **Estratégia de lançamento**: Definir a estratégia de rollout: lançamento simultâneo (full release em ambas as lojas para todos os países) ou staged rollout (Google Play permite percentual gradual — 5% → 20% → 50% → 100%). Staged rollout é recomendado para reduzir risco — se um bug crítico aparecer, apenas uma fração dos usuários é afetada. No iOS, staged rollout é possível via phased release (7 dias de distribuição gradual automática). Definir também se o lançamento será hard launch (com campanha de marketing) ou soft launch (sem divulgação, para coletar métricas antes de investir em aquisição).

- **Plano de rollback e contingência**: Em app mobile, rollback é fundamentalmente diferente de web — não é possível "reverter" um app já instalado no dispositivo do usuário. As opções são: publicar nova versão com fix urgente (fast-track review na Apple leva 24-48h), usar feature flags para desativar funcionalidade problemática remotamente, ou em caso extremo, remover o app da loja temporariamente (drástico, afeta ranking permanentemente). O plano deve documentar: quem tem acesso para submeter hotfix, quem autoriza, e qual o processo para solicitar fast-track review na Apple.

- **Comunicação e suporte**: Definir o canal de suporte para os primeiros usuários — e-mail de suporte configurado, formulário de contato funcional, e processo de resposta a reviews nas lojas. Reviews negativas nos primeiros dias têm impacto desproporcional no ranking (poucos reviews = cada um pesa muito). Definir quem monitora reviews, quem responde, e com que tom. Preparar FAQ com problemas previsíveis (como fazer cadastro, como recuperar senha, quais dispositivos são suportados). Se o app tem chat de suporte integrado, garantir que há alguém do outro lado respondendo.

### Perguntas

1. Todos os metadados das lojas (screenshots, descrições, keywords, privacy labels) estão prontos e otimizados para ASO? [fonte: Marketing, Produto, Designer] [impacto: Marketing, Dev]
2. O app foi submetido para review com antecedência suficiente para pelo menos uma rodada de correção? [fonte: Dev, PM] [impacto: Dev, PM]
3. O mecanismo de delete account está implementado e funcional (obrigatório para Apple e Google)? [fonte: Dev, Produto] [impacto: Dev]
4. Os analytics de produto e attribution estão configurados e validados com dados reais em staging? [fonte: Dev, Marketing, Produto] [impacto: Dev, Marketing]
5. A estratégia de rollout foi definida (full release vs. staged/phased) com justificativa? [fonte: Produto, PM] [impacto: PM, Dev]
6. O plano de hotfix está documentado (quem submete, quem autoriza, processo de fast-track review)? [fonte: Dev, PM, Diretoria] [impacto: Dev, PM]
7. O canal de suporte está configurado e testado (e-mail, formulário, chat) com processo de resposta definido? [fonte: Produto, Atendimento] [impacto: PM, Produto]
8. O processo de monitoramento e resposta a reviews das lojas foi definido (quem monitora, tom, SLA)? [fonte: Marketing, Produto] [impacto: Marketing, Produto]
9. O treinamento da equipe de suporte foi realizado com FAQ e procedimentos para problemas previsíveis? [fonte: Atendimento, Produto] [impacto: Atendimento, PM]
10. As URLs de suporte, política de privacidade e termos de uso estão publicadas e funcionais? [fonte: Jurídico, Dev] [impacto: Dev, PM]
11. O monitoramento de disponibilidade do backend e alertas estão configurados (uptime, latência, error rate)? [fonte: DevOps, Dev] [impacto: DevOps, Dev]
12. Os feature flags estão configurados para funcionalidades que podem precisar ser desativadas remotamente? [fonte: Dev, Produto] [impacto: Dev]
13. A versão mínima do SO foi definida e comunicada (iOS 16+, Android 8+, ou outra)? [fonte: Dev, Produto] [impacto: Dev, QA]
14. Todos os stakeholders foram notificados sobre a data, horário e estratégia do lançamento? [fonte: Diretoria, PM] [impacto: PM]
15. A janela de lançamento foi escolhida estrategicamente (evitar sexta, feriado, e períodos sem equipe de suporte)? [fonte: PM, Diretoria] [impacto: PM, Dev]

---

## Etapa 10 — Go-Live

- **Publicação nas lojas e monitoramento de aprovação**: Executar a publicação conforme a estratégia definida — release ou staged rollout. Monitorar o status da review em ambas as lojas. No iOS, após aprovação, clicar em "Release This Version" (se não configurou auto-release) ou ativar phased release. No Google Play, configurar o percentual de rollout (começar com 5-10% é seguro). Verificar imediatamente após a publicação: o app aparece na busca das lojas, o deep link da loja funciona (https://apps.apple.com/..., https://play.google.com/...), e o download + instalação funcionam de um dispositivo que não participou do beta.

- **Monitoramento de crash e performance D0**: Nas primeiras 24 horas, monitorar Firebase Crashlytics em tempo real — qualquer crash com occurrence > 0.1% do total de sessões deve ser investigado imediatamente. Monitorar também: tempo de inicialização real (cold start), tempo de resposta das APIs em produção com tráfego real, e consumo de recursos do backend (CPU, memória, database connections). Se o app tem staged rollout, escalar o percentual apenas se crash-free rate está acima de 99.5% e não há erros de backend com growth rate positivo.

- **Validação de integrações em produção**: Testar todas as integrações com dados reais de produção — não confiar apenas em testes de staging. Verificar: social login funciona (Google, Apple, Facebook), push notifications chegam em dispositivos reais de usuários externos ao time (não apenas dispositivos de desenvolvimento), pagamento funciona com cartão real (fazer uma compra de teste e reembolsar), deep links de campanhas abrem corretamente, e analytics estão recebendo eventos de usuários reais (verificar no dashboard da ferramenta em real-time).

- **Monitoramento de reviews e rating**: Monitorar reviews nas lojas desde o momento da publicação. As primeiras 10-20 reviews definem a percepção inicial do app — rating abaixo de 4.0 nos primeiros dias é difícil de recuperar e afeta o ranking de busca permanentemente. Responder a reviews negativas rapidamente com tom empático e solução (ou investigação do problema). Se um bug crítico está gerando reviews negativas, priorizar hotfix sobre qualquer outra atividade. Configurar alertas de review (AppFollow, Appbot, ou manualmente) para notificar o time em tempo real.

- **Monitoramento da primeira semana**: Acompanhar as métricas definidas na Discovery com especial atenção a: retenção D1 (>40% é bom para apps consumer), taxa de conclusão do onboarding (>60% é aceitável), crash-free rate (>99.5% é obrigatório), e se há monetização, taxa de conversão do trial ou primeira compra. Comparar com os benchmarks do setor. Se retenção D1 está abaixo de 25%, há um problema fundamental de first value moment — o app não está entregando valor rápido o suficiente e isso não se resolve com marketing, apenas com melhoria de produto.

- **Entrega e handoff ao cliente**: Entregar formalmente todos os acessos e documentação: acesso ao repositório com documentação de como buildar e submeter, acesso às contas das lojas (App Store Connect, Google Play Console) com papéis definidos (Admin, Developer, Marketing), acesso ao Firebase/Supabase com instruções de operação, acesso ao dashboard de analytics com explicação das métricas, acesso ao serviço de push notifications com guia de envio, e acesso ao sistema de crash reporting. A documentação mínima deve incluir: como gerar build de produção, como submeter atualização, como responder a rejeição da loja, como enviar push, e contato de suporte técnico.

### Perguntas

1. O app foi publicado nas lojas e está disponível para download por usuários reais (não apenas testers)? [fonte: Dev, PM] [impacto: Dev, PM]
2. O crash-free rate nas primeiras 24 horas está acima de 99.5% em ambas as plataformas? [fonte: Dev, QA] [impacto: Dev]
3. As integrações críticas foram verificadas em produção com dados reais (login, pagamento, push, deep links)? [fonte: QA, Dev] [impacto: Dev]
4. O backend está operando dentro dos limites de capacidade planejados (CPU, memória, connections, latência)? [fonte: DevOps, Dev backend] [impacto: DevOps, Dev]
5. Os analytics estão recebendo eventos reais e os dashboards estão funcionais? [fonte: Dev, Produto, Marketing] [impacto: Dev, Produto]
6. As reviews nas lojas estão sendo monitoradas e reviews negativas estão recebendo resposta? [fonte: Marketing, Produto, Atendimento] [impacto: Marketing, Produto]
7. O staged rollout (se aplicável) está progredindo com métricas saudáveis antes de escalar percentual? [fonte: Produto, Dev] [impacto: PM, Dev]
8. A retenção D1 está dentro do esperado (benchmark do setor) para validar que o first value moment funciona? [fonte: Produto, Data] [impacto: Produto, PM]
9. O fluxo de hotfix está testado — o time consegue gerar build, submeter e passar por review rápida? [fonte: Dev] [impacto: Dev, PM]
10. As campanhas de aquisição (se ativas) estão gerando installs com attribution funcionando corretamente? [fonte: Marketing, Dev] [impacto: Marketing]
11. O suporte está operacional e respondendo dentro do SLA definido? [fonte: Atendimento, PM] [impacto: PM, Atendimento]
12. Todos os acessos (lojas, repositório, Firebase, analytics, push) foram entregues formalmente ao cliente? [fonte: Dev, DevOps, PM] [impacto: PM]
13. O aceite formal de entrega foi obtido do cliente (e-mail, assinatura de ata, ou confirmação documentada)? [fonte: Diretoria] [impacto: PM]
14. O plano de manutenção pós-lançamento foi ativado (canal de comunicação, SLA, equipe designada)? [fonte: Diretoria, PM] [impacto: PM, Dev]
15. O processo de submissão de atualizações futuras está documentado e foi validado com uma atualização de teste? [fonte: Dev] [impacto: Dev, PM]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos um app tipo o iFood/Uber/Instagram"** — O cliente cita um app com centenas de engenheiros e anos de maturidade como referência para o MVP. Isso indica expectativa desalinhada com o orçamento e prazo. O correto é identificar quais 2-3 funcionalidades específicas do app referência são realmente necessárias no MVP e ignorar o resto.
- **"Precisa ser iOS e Android desde o início"** — Sem validação de mercado, lançar em duas plataformas dobra custo e tempo. Se o público-alvo é predominantemente uma plataforma, iniciar nela e expandir após métricas de retenção é quase sempre a decisão mais inteligente.
- **"O crescimento vai ser orgânico, não precisamos de orçamento de marketing"** — Apps consumer sem investimento em aquisição têm probabilidade quase zero de crescer organicamente nas lojas. Sem budget de aquisição, o melhor app do mundo morre com 50 downloads.

### Etapa 02 — Discovery

- **"O onboarding pode ser simples, tipo só um cadastro"** — 25% dos usuários abandonam após o primeiro uso. Um onboarding que exige cadastro antes de mostrar valor (nome, e-mail, senha, verificação) é o principal assassino de retenção D1. Permitir exploração antes do cadastro é quase sempre melhor.
- **"Notificações push são fáceis, é só integrar o Firebase"** — A integração técnica de push é a parte fácil. A parte difícil é a estratégia: qual mensagem, para quem, quando, com qual frequência. Push mal planejado é o motivo #1 de desinstalação em apps consumer.
- **"O app precisa funcionar offline, mas não sabemos exatamente o quê"** — Offline sem definição de escopo é armadilha de complexidade infinita. Definir exatamente quais telas e quais dados ficam disponíveis offline é obrigatório antes de avançar.

### Etapa 03 — Alignment

- **"Vamos usar React Native porque o time sabe React"** — Conhecer React web não significa produtividade em React Native. Navegação, gestos, performance, e debugging são completamente diferentes. O time precisa de ramp-up de 2-4 semanas, que deve estar no cronograma.
- **"O design pode ser feito junto com o desenvolvimento"** — Em mobile, design e build em paralelo é pior do que em web. Cada mudança de design exige recompilação, teste em dispositivos reais, e frequentemente ajustes de navegação. Ter ao menos os fluxos principais finalizados antes do build é gate obrigatório.
- **"Não precisamos de TestFlight/beta, a gente testa internamente"** — Sem distribuição de builds de teste para stakeholders durante o build, o feedback vem apenas no final. Em mobile, feedback tardio é 10x mais caro de incorporar do que em web.

### Etapa 04 — Definition

- **Mapa de telas "no Figma a gente vai vendo"** — Sem mapa de navegação formal, telas são criadas ad hoc e a navegação se torna inconsistente. O mapa de telas é o equivalente do sitemap em web e deve ser aprovado antes do design de alta fidelidade.
- **"Os estados de erro a gente trata depois"** — Em mobile, estados de erro representam 30-50% do esforço de cada tela (loading, empty, error, offline). Especificá-los depois significa que o dev implementa apenas o happy path e o QA encontra dezenas de bugs.
- **"A política de privacidade a gente faz no final"** — Apple e Google exigem link funcional para política de privacidade na submissão. Política em branco ou com lorem ipsum é motivo de rejeição. Redigir com jurídico desde a Definition.

### Etapa 05 — Architecture

- **"Vamos usar o Firebase para tudo"** — Firebase é excelente para MVP, mas tem limitações sérias: queries complexas são difíceis no Firestore, custos escalam de forma não-linear com leitura, e lock-in com Google é total. Se o app vai crescer além do MVP, planejar a migração desde o início.
- **"Não precisamos de CI/CD, são só dois devs"** — Em mobile, cada build manual leva 15-30 minutos (compilação + signing + upload). Com 2-3 builds por semana para teste e release, são horas desperdiçadas. Fastlane + CI desde o setup economiza tempo desde a primeira semana.
- **"Certificate pinning é paranoia"** — Para apps que trafegam dados sensíveis (dados pessoais, pagamentos), certificate pinning é requisito de segurança básico, não paranoia. Um MITM attack em app consumer sem pinning compromete todos os usuários simultaneamente.

### Etapa 06 — Setup

- **Keystore/certificado no repositório** — A keystore do Android ou o certificado de distribuição do iOS commitados no repositório são um risco de segurança grave. Qualquer pessoa com acesso ao repo pode assinar builds maliciosos. Usar Fastlane match (iOS) e armazenar a keystore em secret manager.
- **Ambiente único para dev/staging/production** — Sem separação de ambientes, dados de teste poluem produção e bugs de desenvolvimento afetam usuários reais. Três ambientes distintos com variáveis separadas é o mínimo aceitável.
- **"Não precisa de crash reporting ainda, o app é simples"** — Crash reporting deve ser o primeiro SDK integrado, antes de qualquer feature. Sem ele, crashes em produção são invisíveis — o time só descobre via reviews negativas, quando o dano já está feito.

### Etapa 07 — Build

- **Testando apenas no simulador** — Simuladores não reproduzem: performance real de scroll, comportamento de push notifications, biometria real, comportamento de câmera/GPS, e memory pressure. Testar em dispositivo real durante o build, não apenas no QA.
- **Ignorando dark mode** — "Ninguém usa dark mode" é factualmente incorreto — 80%+ dos usuários de iOS usam dark mode. Um app que não suporta dark mode aparece com texto branco em fundo branco (ou vice-versa) para a maioria dos usuários.
- **Hardcoding textos na UI** — Textos hardcoded impossibilitam localização futura e dificultam correções de copy. Centralizar todos os textos em arquivo de strings (Localizable.strings no iOS, strings.xml no Android, i18n no React Native/Flutter) desde o primeiro componente.

### Etapa 08 — QA

- **"Funciona no meu iPhone 15, está aprovado"** — QA feito apenas no flagship do tester. O app pode crashar em iPhone SE com 3GB RAM ou em Android com 2GB RAM. Testar no dispositivo de menor especificação do público-alvo é obrigatório.
- **QA sem testar offline** — Conectividade intermitente é a realidade de mobile. O app que funciona perfeitamente em Wi-Fi de escritório pode crashar na saída do metrô. Testar offline e em conexão degradada é obrigatório.
- **"O reviewer da Apple vai testar para a gente"** — O reviewer da Apple testa por ~5 minutos se o app não crasha e não viola guidelines. Não testa funcionalidade, usabilidade, ou edge cases. O reviewer rejeita, não QA.

### Etapa 09 — Launch Prep

- **Submissão na véspera do lançamento** — Apple Review leva 24-48h na melhor das hipóteses e pode rejeitar. Sem buffer para correção, o prazo de lançamento é estourado. Submeter com pelo menos 7 dias de antecedência.
- **Screenshots da loja feitos com o simulador** — Screenshots com barra de status do simulador, dados fictícios óbvios ("John Doe", "lorem ipsum"), ou dispositivo errado transmitem amadorismo e afetam a taxa de conversão na loja.
- **"O delete account a gente implementa depois"** — Delete account é obrigatório para Apple desde 2022 e Google desde 2024. App sem delete account é rejeitado na review. Implementar antes da submissão é obrigatório.

### Etapa 10 — Go-Live

- **Go-live 100% sem staged rollout** — Liberar para 100% dos usuários sem rollout gradual. Se um crash crítico aparece, afeta todos os usuários de uma vez. Staged rollout (5% → 20% → 50% → 100%) é barato e reduz risco dramaticamente.
- **"As reviews a gente responde depois"** — As primeiras 10 reviews definem o rating inicial. Reviews negativas sem resposta afetam o ranking e a percepção de novos usuários. Monitorar e responder desde o dia 1.
- **Encerrar o projeto sem documentar o processo de atualização** — O cliente recebe o app mas não sabe como submeter atualização, como responder a rejeição da loja, ou como gerar build de produção. 6 meses depois, ninguém sabe como fazer deploy. Documentação de operação é entregável obrigatório.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é app consumer** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "O app será distribuído via MDM para os funcionários" | App enterprise, não consumer | Reclassificar para mobile-app-enterprise |
| "Não vai estar nas lojas, é só para uso interno" | App enterprise com distribuição ad-hoc | Reclassificar para mobile-app-enterprise |
| "É um app para os vendedores da empresa acessarem o CRM" | App enterprise / ferramenta interna | Reclassificar para mobile-app-enterprise |
| "Na verdade é mais um site responsivo que abre no celular" | PWA ou web app responsivo, não app nativo | Reclassificar para web-app ou progressive-web-app |
| "O app é um wrapper do nosso site com push notification" | WebView wrapper, não app nativo | Avaliar se PWA resolve ou se precisa de reclassificação |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos qual plataforma priorizar" | 01 | Escopo indefinido — impossível estimar | Definir plataforma primária com dados antes de avançar |
| "Não temos conta de desenvolvedor nas lojas" | 01 | Go-live bloqueado — Apple leva até 14 dias para aprovar conta empresa | Criar contas imediatamente, não esperar o build |
| "O modelo de receita ainda não foi definido" | 01 | Arquitetura inteira pode mudar (assinatura vs. ads vs. transação) | Definir modelo antes de iniciar Architecture |
| "Não temos backend, o app vai direto no banco" | 02 | Arquitetura inviável — app mobile não acessa banco diretamente | Incluir backend/BaaS no escopo e orçamento |
| "Não sabemos se precisamos de pagamento no app" | 02 | Afeta comissão das lojas, compliance, e escopo de desenvolvimento | Decidir antes da Definition |
| "O designer vai entregar o design depois que o build começar" | 03 | Retrabalho garantido — builds sem design são descartados | Travar build até ter ao menos fluxos principais em alta fidelidade |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O app precisa suportar Android 6.0 / iOS 13" | 02 | Suportar SOs antigos aumenta QA e limita uso de APIs modernas | Documentar impacto e negociar versão mínima mais alta |
| "O time nunca desenvolveu mobile antes" | 03 | Ramp-up de 2-4 semanas não planejado, mais bugs, mais lento | Incluir ramp-up no cronograma e considerar consultoria externa |
| "As aprovações de design passam pelo CEO" | 03 | Ciclo de feedback lento — CEO tem agenda restrita | Documentar SLA de aprovação e escalar se não cumprido |
| "Queremos animações complexas tipo Airbnb" | 04 | Animações custom consomem 3-5x mais tempo que UI padrão | Estimar separadamente e alertar sobre impacto no prazo |
| "Pode escolher qualquer stack, confiamos em vocês" | 05 | Decisão sem critério — responsabilidade transferida | Documentar critérios e decisão em ADR assinado pelo cliente |
| "Não precisamos de analytics, é só um MVP" | 05 | Sem métricas, impossível saber se MVP está funcionando | Analytics é obrigatório em qualquer MVP — sem dados não há iteração |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Modelo de receita definido (pergunta 1)
- Plataforma primária decidida com justificativa (pergunta 2)
- Personas primárias identificadas (pergunta 3)
- Competidores mapeados e diferenciação articulada (pergunta 4)
- Contas de desenvolvedor nas lojas ativas ou em processo (pergunta 12, Etapa 03)

### Etapa 02 → 03

- Fluxos críticos e first value moment mapeados (pergunta 1)
- Métricas de produto definidas (pergunta 2)
- Requisitos de offline definidos com escopo claro (pergunta 5)
- Requisitos de LGPD/GDPR identificados (pergunta 13)

### Etapa 03 → 04

- Decisão cross-platform vs. nativo tomada com critérios documentados (pergunta 1)
- Escopo de MVP aprovado com critério de corte (pergunta 2)
- Design system e linguagem visual alinhados (pergunta 3)
- Estratégia de versionamento e atualizações definida (pergunta 6)

### Etapa 04 → 05

- Mapa de telas completo e validado (pergunta 1)
- Modelos de dados com estados definidos (pergunta 2)
- Fluxo de autenticação especificado (pergunta 3)
- Termos de uso e política de privacidade aprovados (pergunta 13)
- Documentação de definição revisada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- Framework mobile escolhido e justificado (pergunta 1)
- Arquitetura de backend definida (pergunta 2)
- Pipeline de CI/CD desenhado (pergunta 7)
- Custos mensais projetados e aprovados (pergunta 9)
- ADR produzido (pergunta 15)

### Etapa 06 → 07

- Projeto configurado com estrutura de pastas e ambientes separados (perguntas 1 e 2)
- Certificados de signing gerados e armazenados com segurança (pergunta 3)
- TestFlight/Firebase App Distribution funcional com primeiro build distribuído (perguntas 6 e 7)
- Pipeline de CI/CD testado end-to-end (pergunta 15)

### Etapa 07 → 08

- Todos os fluxos de usuário implementados e navegáveis (perguntas 1 e 2)
- Autenticação e push notifications funcionais (perguntas 4 e 5)
- Acessibilidade implementada ao longo do build (pergunta 12)
- Builds de teste entregues com feedback incorporado (pergunta 15)

### Etapa 08 → 09

- Teste em dispositivos reais cobrindo range do público-alvo (pergunta 1)
- Teste offline/conectividade realizado sem crashes (pergunta 3)
- Crash-free rate >99.5% (pergunta 11)
- Guidelines das lojas revisadas sem violações (pergunta 8)
- Teste de acessibilidade com VoiceOver/TalkBack concluído (pergunta 6)

### Etapa 09 → 10

- Metadados das lojas prontos e otimizados (pergunta 1)
- App submetido para review com antecedência (pergunta 2)
- Analytics e attribution validados (pergunta 4)
- Plano de hotfix documentado (pergunta 6)
- Suporte operacional pronto (perguntas 7, 8 e 9)

### Etapa 10 → Encerramento

- App disponível nas lojas para download público (pergunta 1)
- Crash-free rate >99.5% nas primeiras 24h (pergunta 2)
- Retenção D1 dentro do benchmark esperado (pergunta 8)
- Acessos entregues e aceite formal obtido (perguntas 12 e 13)
- Documentação de operação e atualização entregue (pergunta 15)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de app consumer. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Conteúdo | V2 Marketplace | V3 Social | V4 Utilitário | V5 Saúde/IoT |
|---|---|---|---|---|---|
| 01 Inception | 2 | 3 | 3 | 1 | 3 |
| 02 Discovery | 3 | 4 | 4 | 2 | 4 |
| 03 Alignment | 2 | 3 | 3 | 2 | 3 |
| 04 Definition | 3 | 5 | 4 | 2 | 4 |
| 05 Architecture | 3 | 4 | 5 | 2 | 5 |
| 06 Setup | 2 | 3 | 3 | 2 | 3 |
| 07 Build | 4 | 5 | 5 | 3 | 5 |
| 08 QA | 3 | 4 | 4 | 2 | 4 |
| 09 Launch Prep | 3 | 3 | 3 | 2 | 3 |
| 10 Go-Live | 2 | 3 | 3 | 1 | 2 |
| **Total relativo** | **27** | **37** | **37** | **19** | **36** |

**Observações por variante:**

- **V1 Conteúdo/Mídia**: Build é o pico — múltiplos tipos de conteúdo (texto, imagem, vídeo, áudio) com cache offline. O gargalo oculto é a produção e curadoria de conteúdo inicial.
- **V2 Marketplace**: Esforço mais alto entre todas as variantes. Definition e Build são extremamente pesados — fluxo de pagamento, múltiplos atores (comprador/vendedor/entregador), e estados complexos de pedido.
- **V3 Social/Comunidade**: Architecture é o pico — real-time, escalabilidade, moderação de conteúdo. Build compete em intensidade com feed algorítmico, messaging, e upload de mídia do usuário.
- **V4 Utilitário**: O mais leve de todas as variantes. Backend mínimo, foco em UX polida da funcionalidade principal. Build é moderado porque a qualidade de cada interação precisa ser perfeita.
- **V5 Saúde/IoT**: Architecture e Build são os picos — integração BLE com dispositivos, compliance regulatório, processamento de dados em background. QA é pesado pela necessidade de testar com dispositivos físicos reais.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Apenas iOS, sem Android (Etapa 01, pergunta 2) | Etapa 04: pergunta 10 (breakpoints Android). Etapa 05: pergunta 7 (CI/CD Android). Etapa 06: perguntas 3 e 4 (keystore Android, Google Play Console). Etapa 08: perguntas com referência a TalkBack e Android Profiler. Etapa 09: metadados Google Play. |
| Sem monetização no MVP (Etapa 01, pergunta 15) | Etapa 02: pergunta 8 (detalhamento de monetização). Etapa 04: pergunta 6 (fluxo de pagamento). Etapa 05: questões de StoreKit/Play Billing. Etapa 08: pergunta 10 (teste de pagamento em sandbox). |
| App não precisa de offline (Etapa 02, pergunta 5) | Etapa 05: pergunta 3 (estratégia de cache e offline se reduz a cache básico). Etapa 08: pergunta 3 (teste offline pode ser simplificado para graceful degradation). |
| Sem notificações push (Etapa 02, pergunta 4) | Etapa 04: pergunta 5 (especificação de notificações). Etapa 05: pergunta 4 (infraestrutura de push). Etapa 06: pergunta 11 (setup de push). Etapa 08: pergunta 5 (teste de push). |
| App utilitário sem backend — V4 com storage local apenas | Etapa 05: pergunta 2 (backend). Etapa 06: pergunta 12 (backend em staging). Etapa 10: pergunta 4 (monitoramento de backend). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| App com pagamento in-app (Etapa 01, pergunta 1 = transação/assinatura) | Etapa 04: pergunta 6 (fluxo de pagamento) se torna gate obrigatório. Etapa 05: StoreKit/Play Billing na arquitetura. Etapa 08: pergunta 10 (teste de pagamento sandbox) é bloqueadora. Etapa 09: IAP configurado nas lojas antes da submissão. |
| App com conteúdo gerado por usuário — V3 Social (Etapa 02) | Etapa 04: pergunta 14 (moderação de conteúdo) se torna gate. Etapa 05: storage de mídia (pergunta 14) se torna crítica. Etapa 08: teste de moderação e report/block. Etapa 09: compliance com CSAM e guidelines das lojas. |
| Requisitos LGPD/GDPR identificados (Etapa 02, pergunta 13) | Etapa 04: pergunta 13 (política de privacidade e termos) se torna gate. Etapa 05: criptografia local e consentimento granular na arquitetura. Etapa 09: delete account (pergunta 3) é bloqueadora. |
| Integração com dispositivos BLE/IoT — V5 (Etapa 02, pergunta 6) | Etapa 05: framework nativo ou com suporte BLE forte se torna obrigatório. Etapa 07: teste com dispositivos físicos reais durante o build. Etapa 08: QA com dispositivos BLE reais em diferentes SOs e firmwares. |
| Múltiplas plataformas simultâneas — iOS + Android (Etapa 01, pergunta 2) | Etapa 03: pergunta 1 (cross-platform vs. nativo) se torna a decisão mais crítica. Etapa 06: setup duplicado (certificados, contas, distribuição). Etapa 08: QA em dobro (dispositivos reais de ambas as plataformas). Etapa 09: metadados e submissão em ambas as lojas. |
| Staged rollout escolhido (Etapa 09, pergunta 5) | Etapa 10: pergunta 7 (monitoramento de métricas por percentual) se torna obrigatória. Escalar percentual apenas com crash-free rate e métricas saudáveis. |
