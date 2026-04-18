---
title: "Mobile App (Enterprise) — Blueprint"
description: "Aplicativo corporativo distribuído via MDM. Autenticação corporativa (SSO), modo offline, conformidade com políticas de TI e integração com sistemas internos."
category: project-blueprint
type: mobile-app-enterprise
status: rascunho
created: 2026-04-13
---

# Mobile App (Enterprise)

## Descrição

Aplicativo corporativo distribuído via MDM. Autenticação corporativa (SSO), modo offline, conformidade com políticas de TI e integração com sistemas internos.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo app enterprise é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — App de Campo / Field Service

Aplicativo para equipes que trabalham em campo — técnicos de manutenção, vendedores externos, inspetores, entregadores. O uso acontece predominantemente fora do escritório, frequentemente em áreas com conectividade precária (fábricas, áreas rurais, subsolo). O modo offline robusto é requisito fundamental, não feature. A interface deve funcionar com luvas, em telas molhadas, e sob sol direto. Integrações típicas: ERP para ordens de serviço, GPS para rastreamento, câmera para evidências fotográficas, e sync bidirecional quando a conexão volta. Exemplos: app de manutenção preventiva, app de visita técnica, app de vendedor externo com catálogo offline, app de inspeção de campo.

### V2 — App de Comunicação / Portal Corporativo

Aplicativo que centraliza comunicação interna, documentos, políticas, treinamentos, e informações da empresa para todos os colaboradores. Substitui intranet e e-mail para comunicações corporativas. O público é diverso — desde diretores até operadores de chão de fábrica — o que exige interface simples e acessível. Integrações típicas: Active Directory/Azure AD para autenticação, SharePoint/Google Drive para documentos, sistema de RH para dados de funcionário, e push notifications para comunicados urgentes. Exemplos: app de comunicação interna, portal do colaborador, app de treinamento corporativo, app de políticas e compliance.

### V3 — App de Aprovação / Workflow

Aplicativo focado em workflows de aprovação empresarial — requisições de compra, aprovações de despesas, solicitações de férias, aprovações de documentos. O fluxo é estruturado (solicitar → aprovar/rejeitar → escalar) com regras de negócio definidas por alçada, valor e hierarquia. Modo offline é desejável para aprovações rápidas que sincronizam depois. Integrações típicas: ERP (SAP, Oracle, TOTVS) para dados transacionais, sistema de RH para hierarquia, e e-mail/push para notificações de pendências. Exemplos: app de aprovação de despesas, app de requisição de compras, app de workflow de documentos.

### V4 — App de Coleta de Dados / Formulários

Aplicativo para coleta estruturada de dados em campo — checklists, formulários de inspeção, pesquisas, auditorias. O volume de dados coletados pode ser alto (centenas de registros por dia por usuário) e inclui fotos, assinaturas, geolocalização e timestamps. Modo offline é obrigatório — a coleta acontece onde não há sinal. A sincronização de dados deve ser robusta com resolução de conflitos e garantia de que nenhum registro é perdido. Integrações típicas: banco de dados centralizado para consolidação, BI para relatórios, e sistemas de compliance para auditoria. Exemplos: app de checklist de segurança, app de auditoria de qualidade, app de pesquisa de campo, app de inventário.

### V5 — App de Operação / Linha de Produção

Aplicativo integrado com sistemas de operação — MES (Manufacturing Execution System), SCADA, IoT industrial, WMS (Warehouse Management System). Usado por operadores em chão de fábrica, armazéns, ou centros de distribuição. A interface deve ser extremamente simples (operadores com baixa familiaridade digital), com fluxos de poucos toques. Leitura de código de barras/QR code é funcionalidade central. O dispositivo geralmente é compartilhado entre turnos (sem dados pessoais, login rápido por crachá ou PIN). Integrações típicas: ERP para ordens de produção, WMS para movimentação de estoque, sensores IoT para dados de máquina. Exemplos: app de apontamento de produção, app de picking de armazém, app de controle de qualidade em linha, app de manutenção de equipamento.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Framework | Backend | MDM/Distribuição | Auth | Observações |
|---|---|---|---|---|---|
| V1 — Campo | React Native ou Flutter | Node.js + PostgreSQL ou .NET + SQL Server | Microsoft Intune ou VMware WS1 | Azure AD / Okta SSO | Offline-first obrigatório. Sync bidirecional com conflict resolution. |
| V2 — Portal | React Native ou Flutter | .NET ou Node.js + SharePoint API | Microsoft Intune | Azure AD SSO | Integração com Microsoft 365 é geralmente mandatória. Push para comunicados. |
| V3 — Workflow | React Native ou Flutter | .NET + SQL Server ou Java + Oracle | Microsoft Intune ou custom APK | Azure AD / SAP IDP | Integração pesada com ERP. Regras de alçada no backend, nunca no app. |
| V4 — Coleta | Flutter ou React Native | Node.js + PostgreSQL ou Firebase | MDM ou sideload controlado | Azure AD ou login simples | Offline-first com sync robusto. SQLite local com queue de upload. |
| V5 — Operação | Nativo (Kotlin) ou Flutter | .NET + SQL Server ou Java | MDM com kiosk mode | PIN/crachá + Azure AD | Dispositivo compartilhado. Interface mínima. Leitura de código de barras nativa. |

---

## Etapa 01 — Inception

- **Origem da demanda e sponsor corporativo**: Em projetos enterprise, a demanda geralmente vem de uma diretoria específica (Operações, Comercial, TI, RH) buscando digitalizar um processo que hoje é manual (papel, planilha, e-mail). O sponsor deve ter autoridade orçamentária e poder de decisão — projetos enterprise sem sponsor forte morrem na primeira disputa de prioridade com TI. Entender o gatilho real: é eficiência operacional (reduzir tempo de processo), compliance (rastrear atividades para auditoria), ou redução de erro humano (eliminar retrabalho de dados incorretos)?

- **Política de dispositivos e MDM**: Identificar se a empresa fornece dispositivos corporativos (COPE — Corporate Owned, Personally Enabled) ou permite dispositivos pessoais (BYOD — Bring Your Own Device). COPE simplifica enormemente o QA (controle total sobre modelos, SO e versões) mas tem custo de hardware. BYOD reduz custo de dispositivo mas explode a complexidade de teste (centenas de modelos/versões possíveis) e levanta questões de privacidade (dados pessoais vs. corporativos no mesmo dispositivo). A empresa usa MDM (Microsoft Intune, VMware Workspace ONE, MobileIron)? Se sim, a distribuição é via MDM e não via lojas públicas — o que elimina a necessidade de conta Apple Developer e Google Play Console públicas, mas exige integração com o MDM da empresa.

- **Landscape de TI e sistemas existentes**: Empresas enterprise têm ecossistema de TI complexo — Active Directory ou Azure AD para identidade, ERP (SAP, Oracle, TOTVS) para processos de negócio, CRM (Salesforce, Dynamics) para vendas, SharePoint para documentos, e frequentemente dezenas de sistemas legados com APIs em diversos estágios de maturidade (REST moderno, SOAP, ou até acesso direto a banco). Mapear os sistemas com os quais o app precisa se integrar é prerequisito para estimar complexidade e prazo — uma integração com API REST documentada leva dias, uma integração com sistema legado sem API pode levar semanas.

- **Requisitos de segurança e compliance corporativo**: Apps enterprise operam dentro das políticas de segurança da empresa — que podem incluir: criptografia de dados em repouso obrigatória, VPN obrigatória para acesso a APIs internas, certificate pinning, detecção de jailbreak/root com bloqueio do app, timeout de sessão (ex.: logout automático após 5 minutos de inatividade), e auditoria de todas as ações do usuário (quem fez o quê, quando, de qual dispositivo). O time de Segurança da Informação (InfoSec) deve ser envolvido desde a Inception — descobrir requisitos de segurança no QA gera retrabalho massivo.

- **Público-alvo interno e nível de maturidade digital**: Diferentemente de apps consumer, o público de apps enterprise é cativo (funcionários) e a adoção pode ser mandatória. Porém, o nível de familiaridade com tecnologia varia enormemente — um gerente financeiro usa apps diariamente, um operador de chão de fábrica pode nunca ter usado smartphone para trabalho. O nível de maturidade digital do público-alvo define: complexidade da interface (poucos botões, fluxos lineares para baixa maturidade), necessidade de treinamento presencial, e tolerância a erros de usabilidade (zero tolerância em chão de fábrica, mais flexibilidade em escritório).

- **Orçamento e modelo de custeio**: Projetos enterprise geralmente têm orçamento de CAPEX (investimento único no desenvolvimento) separado de OPEX (custo de operação recorrente — servidores, licenças, MDM, suporte). O cliente precisa entender ambos desde o início. Custos frequentemente subestimados: licença de MDM por dispositivo ($3-10/mês/dispositivo × número de usuários), infraestrutura de backend (servidores on-premise ou cloud), e manutenção contínua (atualizações de SO, patches de segurança, correções de bugs). Um app enterprise sem orçamento de manutenção contínua se torna obsoleto e inseguro em 12-18 meses.

### Perguntas

1. Qual é o processo de negócio que o app vai digitalizar e qual é o problema específico que está sendo resolvido? [fonte: Diretoria patrocinadora, Operações] [impacto: PM, Arquiteto, Dev]
2. Quem é o sponsor do projeto e esse sponsor tem autoridade orçamentária e poder de decisão? [fonte: Diretoria] [impacto: PM]
3. Os dispositivos são corporativos (COPE) ou pessoais dos funcionários (BYOD)? Qual o modelo predominante? [fonte: TI, InfoSec] [impacto: Dev, QA, Arquiteto]
4. A empresa utiliza MDM? Se sim, qual (Intune, WS1, MobileIron) e o app será distribuído por ele? [fonte: TI, InfoSec] [impacto: Dev, DevOps]
5. Quais sistemas internos o app precisará se integrar (ERP, CRM, AD, SharePoint, sistemas legados)? [fonte: TI, Operações] [impacto: Arquiteto, Dev, PM]
6. O time de Segurança da Informação (InfoSec) foi envolvido? Existem políticas de segurança já definidas? [fonte: InfoSec, TI] [impacto: Arquiteto, Dev]
7. Quantos usuários utilizarão o app e qual a distribuição geográfica (um escritório, múltiplas unidades, campo)? [fonte: RH, Operações, Diretoria] [impacto: Arquiteto, DevOps, PM]
8. Qual é o nível de maturidade digital dos usuários finais (escritório, campo, chão de fábrica)? [fonte: RH, Operações, Gestores de área] [impacto: Designer, Dev]
9. Qual é o prazo esperado e existe uma data de negócio que o justifica (auditoria, início de operação, compliance)? [fonte: Diretoria, Compliance] [impacto: PM, Dev]
10. O orçamento inclui CAPEX (desenvolvimento) e OPEX (operação: servidores, MDM, licenças, suporte)? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
11. Existem restrições de infraestrutura (cloud pública proibida, dados devem ficar on-premise, VPN obrigatória)? [fonte: TI, InfoSec, Compliance] [impacto: Arquiteto, DevOps]
12. O app funcionará apenas na rede corporativa ou precisa funcionar em qualquer rede/offline? [fonte: TI, Operações] [impacto: Arquiteto, Dev]
13. Existe processo de change management na empresa (CAB, janelas de manutenção, aprovação de deploy)? [fonte: TI, Governança] [impacto: DevOps, PM]
14. Quem será responsável pela manutenção e suporte do app após o go-live (equipe interna, terceiro, fornecedor)? [fonte: TI, Diretoria] [impacto: PM, Dev]
15. Há requisitos regulatórios do setor (SOX, HIPAA, ANVISA, BACEN, LGPD) que afetam o app? [fonte: Compliance, Jurídico, Diretoria] [impacto: Arquiteto, Dev, PM]

---

## Etapa 02 — Discovery

- **Mapeamento detalhado do processo de negócio**: Antes de definir funcionalidades, entender profundamente o processo que o app vai digitalizar — como funciona hoje (formulário em papel, planilha Excel, sistema legado), quais são os passos, quem executa cada passo, quais decisões são tomadas, quais exceções existem, e onde estão os gargalos. Apps enterprise que digitalizam processos sem entender o processo real acabam replicando ineficiências em formato digital, ou pior, quebrando o processo ao omitir exceções que só quem opera no dia a dia conhece.

- **Requisitos de offline e sincronização**: Em apps enterprise, offline não é "nice to have" para muitas variantes — é requisito operacional. Técnicos em campo, operadores em chão de fábrica, e vendedores em áreas remotas não podem parar de trabalhar porque o sinal caiu. Definir com precisão: quais telas e funcionalidades devem funcionar offline, quanto dado local o app precisa armazenar (catálogo de 10.000 produtos offline? Histórico de 30 dias de ordens de serviço?), como o sync acontece (manual via botão, automático ao reconectar, em background), e como conflitos são resolvidos (último-ganha, merge manual, prioridade servidor).

- **Requisitos de integração com sistemas corporativos**: Para cada sistema identificado na Inception, detalhar: qual API está disponível (REST, SOAP, OData, RFC para SAP), qual a autenticação da API (OAuth2, API key, certificado mútuo), quais endpoints são necessários (leitura, escrita, ambos), qual o SLA de disponibilidade da API, e quem é o responsável técnico do lado do cliente para cada sistema. Frequentemente, APIs de sistemas enterprise são incompletas, mal documentadas, ou têm limitações de performance (rate limiting, paginação ausente) que só aparecem durante a integração real.

- **Modelo de identidade e acesso (IAM)**: Mapear como os usuários serão autenticados e autorizados. Em ambiente enterprise, a autenticação geralmente é via SSO corporativo (Azure AD, Okta, ADFS) com protocolo SAML2 ou OpenID Connect. Definir: quais claims o token de SSO fornece (nome, e-mail, departamento, cargo, grupos), como os papéis de acesso no app são derivados (por grupo do AD, por departamento, por configuração no app), e se há necessidade de MFA (Multi-Factor Authentication) — que em muitos ambientes corporativos é obrigatório para acesso a dados sensíveis.

- **Requisitos de dispositivo e ambiente de uso**: Levantar os modelos de dispositivos em uso (se COPE, os modelos específicos; se BYOD, a distribuição estatística), versões de SO, e condições de uso. Para apps de campo: tela sob sol direto (contraste alto), operação com luvas (botões grandes, sem gestos finos), e dispositivos ruggedized (Zebra, Samsung XCover). Para chão de fábrica: dispositivos compartilhados entre turnos (login rápido, sem dados pessoais persistentes), e ambiente com barulho (sem dependência de áudio). Essas condições impactam diretamente o design e a arquitetura.

- **Requisitos de auditoria e rastreabilidade**: Sistemas enterprise frequentemente exigem rastreabilidade completa — quem criou o registro, quem alterou, quando, de qual dispositivo, e qual era o valor anterior. Isso é especialmente crítico em setores regulados (saúde, financeiro, manufatura com ISO). Definir: quais ações devem ser logadas (todas, ou apenas as críticas), qual o período de retenção dos logs (5 anos para SOX, por exemplo), e se os logs devem ser imutáveis (append-only, sem edição ou exclusão). A implementação de auditoria afeta o modelo de dados e a performance de escrita.

### Perguntas

1. O processo de negócio que será digitalizado foi mapeado em detalhe (passos, atores, decisões, exceções)? [fonte: Operações, Gestores de área, Usuários-chave] [impacto: PM, Dev, Arquiteto]
2. Quais funcionalidades devem funcionar offline e quanto dado local o app precisa armazenar? [fonte: Operações, TI, Usuários de campo] [impacto: Arquiteto, Dev]
3. Para cada sistema a integrar, a API está documentada, disponível e com responsável técnico identificado? [fonte: TI, Fornecedores de sistemas] [impacto: Dev, Arquiteto]
4. O modelo de autenticação (SSO corporativo, protocolo, claims disponíveis) foi confirmado com o time de identidade? [fonte: TI, InfoSec] [impacto: Dev, Arquiteto]
5. Os papéis de acesso e permissões por funcionalidade foram mapeados (quem pode ver, editar, aprovar, excluir)? [fonte: Operações, RH, Gestores] [impacto: Dev, Arquiteto]
6. Os modelos de dispositivos e versões de SO em uso foram inventariados? [fonte: TI, Operações] [impacto: Dev, QA]
7. As condições de uso foram consideradas (campo, fábrica, escritório, sol direto, luvas, barulho)? [fonte: Operações, Usuários de campo] [impacto: Designer, Dev]
8. Os requisitos de auditoria e rastreabilidade foram definidos (quais ações, período de retenção, imutabilidade)? [fonte: Compliance, Auditoria, InfoSec] [impacto: Arquiteto, Dev]
9. O volume de dados esperado foi estimado (registros por dia, tamanho de anexos, crescimento mensal)? [fonte: Operações, TI] [impacto: Arquiteto, DevOps]
10. Existem requisitos de performance específicos (tempo máximo de sync, tempo de resposta de tela, batch upload)? [fonte: Operações, TI] [impacto: Dev, Arquiteto]
11. Há requisitos de LGPD que afetam dados de funcionários coletados pelo app (localização, fotos, biometria)? [fonte: Jurídico, DPO, RH] [impacto: Arquiteto, Dev]
12. O app precisa gerar relatórios ou dashboards, ou isso será feito em outro sistema (BI, ERP)? [fonte: Gestores, Diretoria] [impacto: Dev, Arquiteto]
13. Existe processo de homologação de software na empresa (testes de segurança, penetration test, aprovação de TI)? [fonte: TI, InfoSec, Governança] [impacto: QA, Dev, PM]
14. Quantos idiomas o app precisa suportar (unidades em outros países, colaboradores de diferentes nacionalidades)? [fonte: RH, Operações, Diretoria] [impacto: Dev, Designer]
15. Existe treinamento presencial previsto para os usuários finais e quem será o responsável? [fonte: RH, Operações, PM] [impacto: PM, Produto]

---

## Etapa 03 — Alignment

- **Decisão cross-platform vs. nativo com restrições corporativas**: Em contexto enterprise, a decisão de framework é influenciada por fatores adicionais: política de TI pode exigir linguagens específicas (empresas Microsoft-centric podem preferir .NET MAUI ou Xamarin), integração com SDK de MDM pode ter requisitos de plataforma, e leitura de código de barras/NFC pode exigir acesso nativo. Se os dispositivos são controlados (COPE), o range de teste é limitado e cross-platform é viável. Se BYOD, a fragmentação de dispositivos torna cross-platform ainda mais atrativo. A decisão deve ser validada com TI antes de se tornar irreversível.

- **Alinhamento com políticas de TI**: Antes de iniciar o desenvolvimento, obter aprovação formal do time de TI e InfoSec para: stack tecnológica escolhida (framework, linguagem, banco de dados), modelo de hospedagem do backend (cloud pública, privada, on-premise), integrações com sistemas corporativos (quem provê credenciais, quem libera acesso à API), e modelo de distribuição do app (via MDM, via lojas, via sideload). Em empresas com governança de TI madura, um RITM (Request Item) ou RFC (Request for Change) formal pode ser necessário, e o prazo de aprovação pode ser de semanas — esse prazo deve estar no cronograma.

- **Estratégia de distribuição e deployment**: Apps enterprise geralmente não vão para lojas públicas — são distribuídos via MDM (Intune, VMware Workspace ONE) para dispositivos corporativos, ou via Apple Business Manager (ABM) + Managed Google Play para distribuição privada. O fluxo é: dev gera build assinado → upload para o MDM ou custom enterprise store → MDM distribui automaticamente para dispositivos-alvo. Se BYOD sem MDM, a distribuição pode ser via TestFlight (limite de 10.000 testers) para iOS e via link direto de APK ou custom store para Android — mas isso é menos seguro e menos gerenciável.

- **Formato e completude do design com foco operacional**: Em apps enterprise, o design deve priorizar eficiência operacional sobre estética. Formulários devem ser rápidos de preencher (defaults inteligentes, autocomplete, scan de código de barras), listas devem ser filtráveis e ordenáveis, e ações críticas devem estar acessíveis em no máximo 2 toques. O design deve considerar: operação com uma mão (dispositivo em campo), uso com luvas de proteção (botões grandes, sem gestos finos), e legibilidade sob luz solar direta (contraste alto, fonte grande). O design deve ser validado com usuários reais em condições reais de uso, não apenas em sala de reunião.

- **Plano de treinamento e change management**: A adoção de apps enterprise depende de treinamento e gestão de mudança. Definir: quem recebe treinamento (todos os usuários, apenas multiplicadores que repassam), formato (presencial, vídeo, manual impresso para campo), cronograma (antes do go-live, durante rollout gradual), e medição de adoção (taxa de uso, completude de cadastro, suporte por funcionalidade). Em projetos de chão de fábrica, o treinamento presencial com o dispositivo real é insubstituível — vídeos e manuais são ignorados. Sem change management, o app é implementado mas não adotado.

### Perguntas

1. A stack tecnológica foi validada e aprovada pelo time de TI e InfoSec da empresa? [fonte: TI, InfoSec] [impacto: Dev, PM]
2. A decisão cross-platform vs. nativo foi tomada considerando as restrições corporativas (MDM, SDK, políticas)? [fonte: TI, Dev, Arquiteto] [impacto: Dev]
3. O modelo de distribuição do app foi definido (MDM, ABM, Managed Google Play, sideload) e aprovado por TI? [fonte: TI, InfoSec] [impacto: Dev, DevOps]
4. O RFC ou RITM necessário para aprovação de TI foi submetido e tem prazo de aprovação no cronograma? [fonte: TI, Governança] [impacto: PM]
5. O design prioriza eficiência operacional e foi validado com usuários reais nas condições reais de uso? [fonte: Designer, Operações, Usuários-chave] [impacto: Designer, Dev]
6. O design considera as restrições do ambiente (luvas, sol, barulho, dispositivo compartilhado)? [fonte: Designer, Operações] [impacto: Designer, Dev]
7. O design inclui todos os estados de tela (loading, error, offline, sync em progresso, conflito de dados)? [fonte: Designer] [impacto: Dev]
8. O plano de treinamento e change management foi definido com formato, cronograma e responsável? [fonte: RH, Operações, PM] [impacto: PM, Produto]
9. O modelo de manutenção pós-lançamento foi formalizado (equipe interna, terceiro, SLA, escalonamento)? [fonte: TI, Diretoria] [impacto: PM, Dev]
10. As dependências de TI (credenciais de API, acesso a ambientes, liberação de firewall) foram listadas com prazos? [fonte: TI] [impacto: PM, Dev]
11. O processo de entrega e revisão durante o build está alinhado (frequência de builds, canal de feedback, UAT)? [fonte: Produto, Operações, Diretoria] [impacto: PM, Dev]
12. A janela de change management foi considerada (deploy em horário de baixo uso, comunicação prévia aos usuários)? [fonte: TI, Operações, Governança] [impacto: PM, DevOps]
13. Os requisitos de acessibilidade foram definidos considerando o perfil dos usuários (baixa visão, daltonismo)? [fonte: RH, Compliance] [impacto: Designer, Dev]
14. O time de desenvolvimento tem acesso ao ambiente corporativo (VPN, APIs de staging, MDM de teste)? [fonte: TI] [impacto: Dev, DevOps]
15. O cliente entende que mudanças de escopo em app enterprise (novas integrações, novos workflows) têm impacto amplificado no prazo? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Mapa de telas com fluxos operacionais**: Produzir o mapa completo de telas alinhado com os fluxos do processo de negócio — cada passo do processo se traduz em uma ou mais telas. A navegação deve seguir a sequência natural do trabalho: em app de campo, o fluxo é lista de ordens → selecionar ordem → executar checklist → registrar evidências → finalizar. Em app de aprovação, é notificação de pendência → visualizar detalhe → aprovar/rejeitar. A eficiência de navegação é medida em toques — se o operador precisa de mais de 3 toques para chegar à ação mais frequente, a navegação está errada.

- **Modelo de dados com integração**: Para cada entidade do app, definir: campos locais (que existem apenas no app), campos sincronizados (que vêm do backend ou de sistemas integrados), regras de validação, e mapeamento com os campos equivalentes nos sistemas de origem. Exemplo: uma ordem de serviço pode ter 50 campos no SAP, mas o app mobile mostra apenas 15 — a seleção de quais campos são relevantes deve ser feita com o usuário operacional, não com o analista de sistemas. Definir também a direção da sincronização: read-only (dados vêm do ERP), write-only (dados vão para o ERP), ou bidirecional (com regras de conflito).

- **Especificação de offline com cenários de conflito**: Para cada funcionalidade offline, definir o cenário de conflito mais provável e a resolução. Exemplo: o técnico atualizou a ordem de serviço offline, mas enquanto estava offline, o gestor cancelou a mesma ordem no ERP. Quando o técnico reconecta, o que acontece? O sistema aceita a atualização do técnico (prioridade campo), rejeita silenciosamente (prioridade servidor), ou notifica o técnico e pede resolução manual? Cada cenário deve ser documentado — resolver conflitos ad hoc durante o build gera inconsistências e bugs de dados que são difíceis de rastrear.

- **Regras de permissão e alçada**: Definir a matriz de permissões completa: qual papel (técnico, supervisor, gerente, admin) pode executar qual ação (criar, visualizar, editar, aprovar, excluir) em qual entidade e em qual estado. Em apps de workflow/aprovação, definir regras de alçada: até R$5.000 o supervisor aprova, acima disso vai para o gerente, acima de R$50.000 vai para a diretoria. Essas regras devem ser parametrizáveis no backend (não hardcoded no app) para permitir ajustes sem nova versão do app.

- **Especificação de relatórios e exportação**: Definir quais relatórios o app deve gerar (PDF de ordem de serviço, relatório de auditoria, comprovante de entrega) e qual o formato de exportação (PDF para compartilhamento, CSV/Excel para análise, integração direta com BI). Relatórios gerados no app devem funcionar offline se o app funciona offline — gerar PDF localmente e enviar quando reconectar. Definir também: quem tem acesso a quais relatórios (gerente vê consolidado, técnico vê apenas seus registros) e se há necessidade de assinatura digital (juridicamente válida, não apenas imagem de assinatura).

- **Requisitos de notificação e alertas operacionais**: Em apps enterprise, notificações são operacionais, não de engajamento. Definir: quais eventos geram notificação (nova ordem de serviço atribuída, aprovação pendente, prazo de SLA próximo de vencer, alerta de sistema), qual o canal (push, in-app, e-mail, SMS para críticos), e qual a prioridade (alta = som e vibração imediata, normal = badge silencioso). Em ambientes de fábrica, notificações podem ser ineficazes (barulho, dispositivo no bolso) — considerar alternativas como alertas visuais em tela (se o dispositivo fica em dock) ou integração com sistemas de chamado (Pager).

### Perguntas

1. O mapa de telas reflete fielmente os fluxos do processo de negócio e foi validado com usuários operacionais? [fonte: Operações, Usuários-chave] [impacto: Dev, Designer, PM]
2. O modelo de dados foi definido com mapeamento para os campos dos sistemas de origem (ERP, CRM, AD)? [fonte: TI, Operações, Arquiteto] [impacto: Dev]
3. Os cenários de conflito de dados offline foram documentados com regras de resolução para cada caso? [fonte: Operações, Produto, Arquiteto] [impacto: Dev, Arquiteto]
4. A matriz de permissões por papel foi definida para todas as ações e entidades? [fonte: Operações, Gestores, RH] [impacto: Dev]
5. As regras de alçada (se app de workflow) são parametrizáveis no backend, não hardcoded no app? [fonte: Operações, TI] [impacto: Dev, Arquiteto]
6. Os relatórios e exportações foram especificados com formato, conteúdo, permissões e funcionamento offline? [fonte: Operações, Gestores] [impacto: Dev]
7. As notificações operacionais foram mapeadas com evento, canal, prioridade e público-alvo? [fonte: Operações, Produto] [impacto: Dev]
8. Os wireframes foram testados com usuários reais nas condições reais de uso (campo, fábrica, escritório)? [fonte: Designer, Operações, Usuários-chave] [impacto: Designer, Dev]
9. As regras de validação de campos foram definidas (formatos, obrigatoriedade, ranges, dependências entre campos)? [fonte: Operações, Produto] [impacto: Dev]
10. O fluxo de login rápido foi definido para dispositivos compartilhados (PIN, crachá, biometria sem dados pessoais)? [fonte: Operações, TI, InfoSec] [impacto: Dev, Designer]
11. O volume de registros em cenários de pico foi estimado e validado com os gestores operacionais? [fonte: Operações] [impacto: Arquiteto, Dev]
12. Os requisitos de assinatura digital (se necessário) foram definidos com validade jurídica? [fonte: Jurídico, Compliance] [impacto: Dev, Arquiteto]
13. Os campos de geolocalização, timestamp e foto de evidência foram especificados com regras de obrigatoriedade? [fonte: Operações, Compliance] [impacto: Dev]
14. A estratégia de busca e filtro de dados foi definida (busca local offline vs. busca no servidor)? [fonte: Operações, Produto] [impacto: Dev, Arquiteto]
15. A documentação de definição foi revisada e aprovada por operações, TI e diretoria antes do Setup? [fonte: Operações, TI, Diretoria] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Arquitetura offline-first**: Para apps enterprise com requisito de offline, a arquitetura deve ser desenhada com offline como cenário primário, não como fallback. Isso significa: banco de dados local robusto (SQLite com camada de abstração, Realm, ou WatermelonDB para React Native), queue de operações pendentes (FIFO com retry e dead letter queue para operações que falharam permanentemente), sync engine com resolução de conflitos (timestamp-based, ou vector clock para cenários complexos), e indicador de estado de sync visível para o usuário (sincronizado, pendente, erro). A complexidade da sync engine é frequentemente o maior componente de esforço do projeto.

- **Arquitetura de integração com sistemas corporativos**: Definir a camada de integração: o app mobile fala diretamente com as APIs dos sistemas corporativos, ou existe um backend intermediário (BFF — Backend for Frontend) que abstrai a complexidade? BFF é fortemente recomendado em contexto enterprise porque: APIs corporativas frequentemente têm formatos diferentes (ERP retorna XML, CRM retorna JSON), a lógica de transformação e agregação de dados não deve estar no app mobile (performance e segurança), e o BFF pode implementar cache, retry e circuit breaker para proteger contra indisponibilidade de sistemas legados.

- **Segurança em profundidade (defense in depth)**: Apps enterprise exigem múltiplas camadas de segurança: autenticação via SSO corporativo (Azure AD com tokens OAuth2/OIDC), autorização por claims/roles validada no backend (nunca confiar no app), comunicação via TLS 1.2+ com certificate pinning, dados sensíveis criptografados em repouso (SQLCipher para SQLite, ou criptografia de arquivo), detecção de jailbreak/root (com bloqueio ou limitação de funcionalidade), e timeout de sessão configurável por política. Para ambientes regulados (financeiro, saúde), considerar: app attestation (DeviceCheck/App Attest no iOS, SafetyNet/Play Integrity no Android) e app wrapping via SDK de MDM.

- **Backend e infraestrutura**: A escolha de infraestrutura em contexto enterprise é frequentemente restrita: cloud pública pode ser proibida (dados devem ficar on-premise), a empresa pode ter contrato com cloud provider específico (Azure se Microsoft-centric, AWS se Amazon-centric), e o deployment pode exigir pipeline aprovado pela governança de TI. Definir: onde o backend será hospedado (Kubernetes on-premise, VM em cloud privada, PaaS gerenciado), como os logs e métricas serão centralizados (Datadog, Grafana, ELK — frequentemente a empresa já tem stack de observability), e como o scaling será gerenciado (auto-scaling em cloud, capacity planning em on-premise).

- **Pipeline de CI/CD com restrições corporativas**: O pipeline de CI/CD em ambiente enterprise enfrenta restrições adicionais: o repositório pode precisar estar em plataforma específica (Azure DevOps se Microsoft-centric, GitLab se on-premise), o build runner pode precisar estar dentro da rede corporativa (para acessar APIs internas durante build/test), e o deploy para MDM pode exigir aprovação manual (CAB — Change Advisory Board). Definir: CI/CD tool (Azure DevOps Pipelines, GitLab CI, Jenkins — frequentemente ditado pela empresa), gerenciamento de certificados de signing (Fastlane match em repositório corporativo ou vault), e processo de promoção de build (dev → staging → UAT → produção com gates de aprovação).

- **Estratégia de monitoramento e observabilidade**: Em apps enterprise, a observabilidade vai além de crash reporting — inclui: monitoramento de sync (quantos dispositivos estão sincronizados, quanto dado está pendente de sync, falhas de sync por tipo), monitoramento de integrações (disponibilidade e latência de cada API de sistema corporativo), monitoramento de compliance (dispositivos com jailbreak, SO desatualizado, certificado próximo de expiração), e dashboards operacionais para o time de suporte (quem está usando, de onde, últimas ações). A integração com ferramentas de monitoramento corporativo existentes (ServiceNow, Zabbix, Datadog) deve ser considerada.

### Perguntas

1. A arquitetura offline-first foi desenhada com sync engine, queue de operações e resolução de conflitos? [fonte: Arquiteto, Dev] [impacto: Dev]
2. O BFF (Backend for Frontend) foi projetado para abstrair a complexidade das APIs corporativas? [fonte: Arquiteto, Dev backend] [impacto: Dev]
3. A segurança foi desenhada em profundidade (SSO, certificate pinning, criptografia local, jailbreak detection)? [fonte: Arquiteto, InfoSec] [impacto: Dev]
4. A infraestrutura foi definida dentro das restrições corporativas (cloud pública/privada, on-premise, provider)? [fonte: TI, InfoSec, Arquiteto] [impacto: DevOps, Dev]
5. O pipeline de CI/CD foi desenhado dentro das ferramentas e processos da empresa (Azure DevOps, GitLab, CAB)? [fonte: TI, DevOps, Governança] [impacto: Dev, DevOps]
6. O monitoramento de sync, integrações e compliance foi incluído na arquitetura? [fonte: Arquiteto, Operações] [impacto: Dev, DevOps]
7. Os custos de infraestrutura e licenças foram projetados em cenário atual e de crescimento? [fonte: Financeiro, TI, Arquiteto] [impacto: PM, DevOps]
8. A arquitetura suporta o crescimento previsto (mais usuários, mais unidades, mais dados) sem redesign? [fonte: Arquiteto, Diretoria] [impacto: Dev, DevOps]
9. A estratégia de versionamento de API foi definida para suportar múltiplas versões do app em produção? [fonte: Arquiteto] [impacto: Dev backend]
10. A integração com MDM foi projetada (distribuição de app, configuração remota, wipe seletivo)? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
11. O modelo de logs e auditoria foi projetado com retenção, formato e integração com SIEM corporativo? [fonte: InfoSec, Compliance, Arquiteto] [impacto: Dev]
12. A estratégia de backup e disaster recovery foi definida e aprovada pelo time de TI? [fonte: TI, Arquiteto] [impacto: DevOps]
13. O comportamento de force update foi projetado (versão mínima obrigatória, comunicação de manutenção)? [fonte: Arquiteto, Produto] [impacto: Dev]
14. O teste de carga foi planejado para validar a arquitetura com o volume de dados e usuários projetado? [fonte: Arquiteto, QA] [impacto: Dev, QA]
15. O ADR (Architecture Decision Record) foi produzido e aprovado por TI, InfoSec e diretoria do projeto? [fonte: Arquiteto, TI, InfoSec] [impacto: Dev, PM]

---

## Etapa 06 — Setup

- **Estrutura do projeto com camadas de integração**: Organizar o projeto com separação clara entre: UI/presentation, domain/business logic, data layer (repositórios, cache, sync), e integration layer (clients de API para cada sistema corporativo). A camada de integração deve ser isolada para que mudanças em APIs corporativas (frequentes em ambiente enterprise — SAP atualiza, CRM muda endpoint) afetem apenas os clients de integração, sem impactar o restante do app. Cada client de integração deve ter interface abstrata (para mocking em testes) e implementação concreta.

- **Configuração de ambientes com rede corporativa**: Em ambiente enterprise, a configuração de ambientes é mais complexa: development pode exigir VPN para acessar APIs internas, staging pode exigir estar dentro da rede corporativa, e production pode estar em infra completamente separada. Configurar pelo menos: development (mock APIs ou APIs de sandbox, fora da rede corporativa para dev ágil), staging/UAT (APIs de staging dos sistemas corporativos, dentro da rede — requer VPN ou jump box), e production (APIs de produção, infra definitiva). A separação de ambientes no MDM deve espelhar a do backend.

- **Setup de integração com MDM**: Configurar o canal de distribuição via MDM: criar o app no console do MDM (Intune, WS1), configurar os grupos de dispositivos/usuários que receberão o app, definir políticas de instalação (obrigatória ou opcional), e testar o fluxo end-to-end (upload de build → MDM distribui → dispositivo recebe e instala automaticamente). Para Intune: criar um app wrapper (.ipa para iOS, .apk para Android), configurar app protection policies (impedir copy-paste para apps não gerenciados, exigir PIN do app), e definir compliance policies (SO mínimo, criptografia obrigatória, jailbreak bloqueado).

- **Setup de SSO e autenticação corporativa**: Configurar a integração com o Identity Provider corporativo: registrar o app no Azure AD (ou outro IDP), configurar redirect URIs, definir os scopes e permissions necessários, e testar o fluxo de login em dispositivo real. Para apps que precisam de tokens para múltiplas APIs (Graph API para dados do usuário, API do backend para dados de negócio), configurar token exchange ou on-behalf-of flow. O setup de SSO frequentemente depende de ações do time de TI do cliente (registrar app, liberar permissões) — esse prazo deve estar no cronograma.

- **Configuração de banco de dados local e sync**: Configurar o banco de dados local (SQLite com ORM, Realm, WatermelonDB) com o schema definido na etapa de Definition, incluindo: tabelas de dados de negócio, tabela de queue de operações pendentes (com status: pending, syncing, synced, failed), tabela de metadados de sync (último sync timestamp por entidade), e triggers ou observers para detectar mudanças locais que precisam ser sincronizadas. O sync engine deve ser configurado e testado com cenários básicos nesta etapa — não deixar para o Build.

- **Setup de monitoramento e crash reporting**: Configurar Firebase Crashlytics (ou alternativa corporativa como Sentry/New Relic) com symbolication correta para ambas as plataformas, e analytics básico (evento de abertura, login, sync). Configurar alertas para: crash rate acima de threshold, erros de sync acima de threshold, e indisponibilidade de APIs integradas. Em ambiente enterprise, a integração com sistema de incidentes existente (ServiceNow, Jira Service Management) pode ser necessária — cada crash crítico deve gerar um ticket automaticamente.

### Perguntas

1. A estrutura do projeto foi definida com camada de integração isolada para cada sistema corporativo? [fonte: Dev, Arquiteto] [impacto: Dev]
2. Os ambientes (dev, staging/UAT, production) foram configurados com acesso à rede corporativa quando necessário? [fonte: Dev, TI] [impacto: Dev, DevOps]
3. O acesso às APIs corporativas de staging foi liberado e testado (VPN, firewall, credenciais)? [fonte: TI, Dev] [impacto: Dev]
4. O app foi registrado no MDM e o fluxo de distribuição foi testado end-to-end em dispositivo real? [fonte: TI, Dev] [impacto: Dev, DevOps]
5. O SSO corporativo foi integrado, o app foi registrado no IDP e o login funciona em dispositivo real? [fonte: TI, InfoSec, Dev] [impacto: Dev]
6. O banco de dados local está configurado com schema, queue de sync e metadados de sincronização? [fonte: Dev] [impacto: Dev]
7. O sync engine básico está funcionando (sync manual, verificação de conflitos, queue processing)? [fonte: Dev, Arquiteto] [impacto: Dev]
8. O crash reporting e analytics estão integrados e enviando eventos de teste com symbolication correta? [fonte: Dev] [impacto: Dev, QA]
9. O .gitignore está configurado para excluir secrets, keystores, certificados e arquivos de ambiente? [fonte: Dev] [impacto: Dev, InfoSec]
10. O pipeline de CI/CD está funcionando dentro das ferramentas corporativas (build → test → distribuição via MDM)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
11. Os certificados de signing foram gerados, armazenados em vault seguro, e o backup foi confirmado? [fonte: Dev, InfoSec] [impacto: Dev]
12. O primeiro build de teste foi distribuído via MDM e instalado com sucesso em dispositivo real? [fonte: Dev, QA, TI] [impacto: Dev, PM]
13. O processo de onboarding de novos desenvolvedores inclui acesso a VPN, APIs e MDM de teste? [fonte: Dev, TI] [impacto: Dev]
14. O backend está deployado em ambiente de staging com dados de teste e APIs funcionais? [fonte: Dev backend, DevOps] [impacto: Dev]
15. Os usuários-chave de UAT foram identificados e convocados para o período de teste? [fonte: Operações, PM] [impacto: PM, QA]

---

## Etapa 07 — Build

- **Interface operacional otimizada**: Implementar a interface priorizando eficiência para o operador — formulários com defaults inteligentes (preencher data atual, última localização, último equipamento usado), campos com scan de código de barras/QR integrado (evitar digitação manual de códigos longos), listas com busca local instantânea e filtros pré-definidos, e ações frequentes acessíveis em 1-2 toques. Para apps de campo/fábrica: botões de no mínimo 48x48dp, contraste alto (AA+ no mínimo), e textos de no mínimo 16sp. Cada segundo economizado por interação se multiplica por centenas de operadores × centenas de interações por dia = impacto operacional significativo.

- **Sync engine e gerenciamento de conflitos**: Implementar a sync engine como componente central: sincronização incremental (enviar apenas mudanças desde o último sync, não o dataset inteiro), compressão de payloads para conexões lentas, retry com backoff exponencial para falhas de rede, queue persistente de operações pendentes (sobrevive a kill do app e reboot do dispositivo), e resolução de conflitos conforme especificado na Definition. O indicador de sync deve ser visível para o usuário: ícone de status (sincronizado/pendente/erro), número de operações pendentes, e hora do último sync bem-sucedido. O operador precisa confiar que seus dados não serão perdidos.

- **Integrações com sistemas corporativos**: Implementar cada integração via client isolado com: timeout configurável (sistemas legados podem ser lentos — 30s timeout pode ser necessário), retry com backoff exponencial, circuit breaker (se a API do SAP está down, não enviar 1000 requests — abrir circuito e informar o usuário), fallback para dados cacheados quando a API está indisponível, e logging detalhado de cada chamada (request/response time, status, payload size) para diagnóstico de problemas. A integração deve ser testada com cenários de indisponibilidade do sistema de origem — o app não pode crashar porque o SAP reiniciou.

- **Autenticação SSO e gerenciamento de sessão**: Implementar o fluxo de SSO com MSAL (Microsoft Authentication Library) para Azure AD, ou equivalente para outro IDP. Tratar cenários que o fluxo padrão não cobre: token expirado durante operação offline (renovar quando reconectar, sem perder o trabalho em progresso), revogação de acesso pelo admin de TI (logout forçado no próximo sync), e conditional access policies (MFA requerido por política, dispositivo não-compliant bloqueado). Para dispositivos compartilhados, implementar login rápido por PIN ou crachá (após autenticação SSO inicial) para evitar que o operador precise digitar credenciais corporativas a cada troca de turno.

- **Coleta de dados e evidências**: Implementar a coleta robusta de dados em campo: captura de fotos com compressão inteligente (qualidade suficiente para evidência, tamanho reduzido para upload), geolocalização com fallback (GPS → rede → última conhecida), timestamp imutável (gerado no momento da coleta, não editável pelo operador), e assinatura digital no dispositivo (tela de captura de assinatura com pressão e velocidade). Todos os dados coletados devem ser salvos localmente primeiro (nunca depender de upload imediato) e entrar na queue de sync. A perda de dados coletados em campo é inaceitável — implementar proteção contra perda (save automático a cada campo preenchido, não apenas no submit).

- **Relatórios e exportação**: Implementar geração de relatórios localmente no dispositivo (para funcionamento offline): PDF de ordem de serviço completada, relatório de checklist com fotos e assinaturas, e comprovante de entrega. Usar bibliotecas de geração de PDF (react-native-pdf-lib, Flutter pdf package) com templates pré-definidos. O compartilhamento deve ser via share sheet do SO (e-mail, WhatsApp, salvar em Files) — não forçar um canal específico. Relatórios consolidados (dashboards gerenciais) devem ser gerados no backend/BI, não no app mobile.

- **Testes com dados reais de staging**: A partir do momento que as integrações estão funcionais, testar com dados reais de staging (não mocks). Isso revela problemas que mocks não capturam: campos com encoding inesperado (caracteres especiais em nomes), registros com dados incompletos (campo obrigatório null no ERP), payloads maiores que o esperado (ordem de serviço com 200 itens), e latência real de APIs corporativas (que pode ser 10x maior que o mock local).

### Perguntas

1. A interface operacional foi otimizada para eficiência (defaults inteligentes, scan, busca local, ações em 1-2 toques)? [fonte: Operações, Usuários-chave] [impacto: Dev, Designer]
2. O sync engine está implementado com queue persistente, retry, compressão e indicador de status visível? [fonte: Dev, Arquiteto] [impacto: Dev]
3. A resolução de conflitos está implementada conforme especificado e foi testada com cenários reais? [fonte: Dev, Operações] [impacto: Dev, QA]
4. As integrações com sistemas corporativos estão implementadas com circuit breaker, timeout e fallback? [fonte: Dev, Arquiteto] [impacto: Dev]
5. O SSO está funcional com tratamento de token expirado offline, revogação e conditional access? [fonte: Dev, InfoSec] [impacto: Dev]
6. O login rápido (PIN/crachá) está implementado para dispositivos compartilhados (se aplicável)? [fonte: Dev, Operações] [impacto: Dev]
7. A coleta de dados (foto, geolocalização, timestamp, assinatura) funciona offline com save automático? [fonte: Dev, QA] [impacto: Dev]
8. A geração de relatórios PDF funciona localmente no dispositivo sem dependência de conexão? [fonte: Dev] [impacto: Dev]
9. Os testes estão sendo feitos com dados reais de staging (não mocks) para revelar problemas de integração? [fonte: Dev, QA] [impacto: Dev]
10. A acessibilidade está sendo implementada ao longo do build (contraste, tamanho de fonte, touch targets)? [fonte: Designer, Compliance] [impacto: Dev, QA]
11. O comportamento de força de atualização (force update) está implementado e configurável remotamente? [fonte: Dev, Produto] [impacto: Dev]
12. Os estados de sync (sincronizado, pendente, erro, conflito) estão visíveis e compreensíveis para o operador? [fonte: Dev, Designer, Operações] [impacto: Dev]
13. A leitura de código de barras/QR/NFC está funcional com os formatos reais usados na operação? [fonte: Dev, Operações] [impacto: Dev]
14. O app está sendo testado em dispositivos reais do parque do cliente (não apenas simulador)? [fonte: Dev, QA] [impacto: Dev, QA]
15. Os builds de UAT estão sendo distribuídos via MDM para usuários-chave com feedback sendo incorporado? [fonte: PM, Operações, QA] [impacto: PM, Dev]

---

## Etapa 08 — QA

- **UAT com usuários operacionais reais**: O User Acceptance Testing em apps enterprise é fundamentalmente diferente do QA técnico — deve ser feito por operadores reais, nas condições reais de uso, executando o processo de negócio real (ou o mais próximo possível com dados de staging). Para app de campo: o técnico vai ao campo com o app e executa ordens de serviço reais em staging. Para chão de fábrica: o operador usa o app na linha de produção real com dados de staging. O feedback de UAT é ouro — problemas de usabilidade que o dev nunca imaginaria aparecem nos primeiros 10 minutos de uso real.

- **Teste de sync e offline intensivo**: Este é o teste mais crítico em apps enterprise com offline. Cenários obrigatórios: trabalhar offline por 8h (jornada completa) e sincronizar ao final, perder conexão durante sync (os dados ficam consistentes?), sincronizar 500+ registros de uma vez (performance e memória), conflito de dados simultâneo (dois usuários editam o mesmo registro offline), e reconexão após 7 dias offline (cenário de férias ou licença). Cada cenário deve ser executado e documentado com resultado (pass/fail/issue). Falha de sync com perda de dados é bug severity 1 — bloqueia o lançamento.

- **Teste de integração end-to-end**: Para cada sistema integrado, testar o ciclo completo: dado criado no app → sync com backend → reflexo no sistema de origem (aparece no SAP/CRM/ERP) → dado alterado no sistema de origem → sync com backend → reflexo no app. Testar também: indisponibilidade do sistema de origem durante sync (circuit breaker funciona?), payload com dados inesperados (campo null, encoding especial, registro muito grande), e performance sob carga (100 dispositivos sincronizando simultaneamente).

- **Teste de segurança e compliance**: Para apps enterprise com dados corporativos sensíveis, o teste de segurança pode ser obrigatório antes do go-live. Itens mínimos: verificar que dados sensíveis não aparecem em logs, confirmar que o banco local é criptografado (tentativa de leitura direta do SQLite deve falhar), testar certificate pinning (proxy como Charles deve ser rejeitado), verificar que jailbreak/root detection funciona, e confirmar que timeout de sessão funciona corretamente. Para empresas que exigem penetration test, planejar com antecedência — pentests profissionais levam 2-4 semanas e podem gerar findings que exigem correção antes do go-live.

- **Teste em dispositivos do parque corporativo**: Testar nos modelos exatos de dispositivos que os usuários terão. Se a empresa usa Samsung Galaxy XCover para campo, testar nesse dispositivo. Se usa iPad 9th gen para gestores, testar nesse modelo. Simuladores e outros modelos não substituem — cada dispositivo tem particularidades de câmera, GPS, BLE, e performance que afetam o comportamento do app. Para apps com leitura de código de barras, testar com os formatos reais de barcode usados na operação (Code128, EAN-13, QR, DataMatrix).

- **Teste de performance sob carga**: Testar o backend e sync engine com o volume de dados e usuários projetado: 100-500 dispositivos sincronizando simultaneamente (início de turno), upload de 1000 fotos em batch (final de jornada de campo), consulta de catálogo com 50.000 itens (se catálogo offline), e geração de relatório consolidado com 10.000 registros. Identificar o ponto de saturação da infra (em quantos sync simultâneos o backend começa a degradar) e planejar scaling ou otimização antes do go-live.

### Perguntas

1. O UAT foi realizado com usuários operacionais reais, nas condições reais de uso, executando o processo de negócio real? [fonte: Operações, Usuários-chave, QA] [impacto: Dev, PM]
2. O teste de offline intensivo foi executado (8h offline, sync massivo, conflito, reconexão após dias)? [fonte: QA, Dev] [impacto: Dev]
3. O ciclo completo de integração foi testado para cada sistema (app → backend → sistema → backend → app)? [fonte: QA, Dev, TI] [impacto: Dev]
4. O teste de segurança foi realizado (dados em logs, criptografia local, certificate pinning, jailbreak detection)? [fonte: InfoSec, QA] [impacto: Dev]
5. O penetration test foi realizado (se exigido pela empresa) e findings foram corrigidos? [fonte: InfoSec, QA] [impacto: Dev, PM]
6. O app foi testado nos dispositivos exatos do parque corporativo (modelos, SO, condições de uso)? [fonte: QA, TI, Operações] [impacto: Dev, QA]
7. A leitura de código de barras/QR/NFC foi testada com os formatos reais usados na operação? [fonte: QA, Operações] [impacto: Dev]
8. O teste de performance sob carga foi realizado com o volume projetado de dados e usuários simultâneos? [fonte: QA, DevOps, Arquiteto] [impacto: Dev, DevOps]
9. O crash-free rate em UAT está acima de 99.5% com uso intensivo? [fonte: Dev, QA] [impacto: Dev]
10. Os relatórios gerados pelo app foram validados por gestores (formato, conteúdo, legibilidade)? [fonte: Operações, Gestores] [impacto: Dev]
11. O fluxo de login rápido (PIN/crachá) foi testado em cenário de troca de turno com múltiplos operadores? [fonte: QA, Operações] [impacto: Dev]
12. O comportamento do app ao receber force update foi testado (interrompe uso, preserva dados pendentes)? [fonte: QA, Dev] [impacto: Dev]
13. Os logs de auditoria estão sendo gerados corretamente e podem ser consultados pelo time de compliance? [fonte: Compliance, Auditoria, QA] [impacto: Dev]
14. O teste de acessibilidade foi realizado com os perfis de usuário mais limitados (baixa visão, daltonismo)? [fonte: QA, RH] [impacto: Dev]
15. Os bugs encontrados no UAT foram priorizados e os severity 1 e 2 foram corrigidos antes do go-live? [fonte: QA, Dev, PM] [impacto: Dev, PM]

---

## Etapa 09 — Launch Prep

- **Piloto controlado com grupo restrito**: Em apps enterprise, go-live raramente é "big bang" — o padrão é piloto com grupo restrito. Selecionar uma unidade, equipe ou turno para usar o app em produção real enquanto o restante mantém o processo manual. O piloto deve durar tempo suficiente para cobrir o ciclo completo do processo de negócio (se o ciclo de uma ordem de serviço é 1 semana, o piloto deve durar no mínimo 2 semanas). O piloto revela problemas que o UAT não captura — volume real de dados, exceções reais do processo, e resistência à mudança dos operadores.

- **Configuração de MDM para produção**: Configurar o MDM para distribuição de produção: criar grupo de produção separado do grupo de piloto/teste, configurar políticas de compliance (SO mínimo, criptografia, jailbreak detection), definir política de atualização (automática ou manual com aprovação), e configurar app protection policies (DLP — Data Loss Prevention). Testar o fluxo completo de distribuição para produção: upload do build de release → MDM distribui para grupo de produção → dispositivo recebe, instala e registra → operador faz login com SSO → primeiro sync completa.

- **Preparação de suporte e escalonamento**: Definir a cadeia de suporte com SLA: nível 1 (helpdesk de TI — resolve problemas de acesso, reset de senha, reinstalação), nível 2 (time de desenvolvimento — investiga bugs, problemas de sync, falhas de integração), nível 3 (fornecedor de sistema integrado — quando o problema está no SAP, CRM, ou outro sistema). Documentar: como o operador reporta problema (telefone, ticket, chat), qual o SLA por severidade (S1 - app parado = 2h, S2 - funcionalidade degradada = 8h, S3 - cosmético = próxima release), e quem tem acesso para diagnóstico remoto (logs de crash, status de sync por dispositivo).

- **Treinamento presencial dos operadores**: Para apps enterprise, o treinamento presencial é insubstituível — especialmente para operadores de campo e chão de fábrica com baixa maturidade digital. O treinamento deve: usar o dispositivo real que o operador vai usar, usar dados de staging que se parecem com o cenário real, cobrir o fluxo completo do dia a dia (não funcionalidades isoladas), incluir cenários de problema (sem conexão, erro de sync, como reportar bug), e ter uma sessão de prática supervisionada onde o operador executa o fluxo sozinho. Entregar material de referência rápida (folha plastificada A5 com os passos principais — não manual de 50 páginas).

- **Plano de rollback e contingência operacional**: Em apps enterprise, rollback significa voltar ao processo manual anterior (papel, planilha, sistema legado). O plano deve garantir que o processo manual pode ser retomado a qualquer momento durante o piloto e as primeiras semanas de rollout. Isso significa: não desativar o sistema legado, manter formulários em papel disponíveis como backup, e definir critério claro de quando acionar rollback (perda de dados, sync parado por mais de 4h, taxa de erro acima de 5%). O rollback de app enterprise é operacional, não apenas técnico — envolve comunicar aos operadores que devem voltar ao processo anterior.

- **Comunicação e change management pré-lançamento**: Comunicar a todos os usuários afetados: o que está mudando (novo app para o processo X), quando (data do piloto, data do rollout geral), por que (benefícios concretos — menos papel, menos retrabalho, mais velocidade), como (treinamento, suporte, canal de dúvidas), e o que acontece se der problema (fallback para processo anterior). A comunicação deve vir do sponsor (diretoria), não do time de TI — isso dá legitimidade e sinaliza que a adoção é estratégica, não opcional.

### Perguntas

1. O piloto controlado está planejado com grupo restrito, duração definida e métricas de sucesso? [fonte: Operações, PM, Diretoria] [impacto: PM, Dev]
2. O grupo de piloto foi selecionado com critérios claros (unidade representativa, operadores dispostos, gestor engajado)? [fonte: Operações, RH] [impacto: PM]
3. O MDM está configurado para produção com políticas de compliance, DLP e distribuição para grupo de produção? [fonte: TI, InfoSec] [impacto: DevOps, Dev]
4. A cadeia de suporte foi definida com SLA por severidade e escalonamento claro (N1 → N2 → N3)? [fonte: TI, PM] [impacto: PM, Dev]
5. O treinamento presencial foi realizado com dispositivos reais e dados realistas para todos os operadores do piloto? [fonte: RH, Operações, PM] [impacto: PM]
6. O material de referência rápida (quick reference card) foi produzido e distribuído? [fonte: PM, Designer] [impacto: PM, Operações]
7. O plano de rollback operacional foi documentado (voltar ao processo manual, manter sistema legado ativo)? [fonte: Operações, TI, PM] [impacto: PM, Dev]
8. O sistema legado / processo manual está mantido como backup durante o período de piloto e rollout? [fonte: TI, Operações] [impacto: PM]
9. A comunicação pré-lançamento foi enviada pelo sponsor com mensagem clara sobre o que muda, quando e por quê? [fonte: Diretoria, Comunicação interna] [impacto: PM]
10. O monitoramento de sync e integrações está configurado com alertas automáticos para o time de suporte? [fonte: Dev, DevOps] [impacto: DevOps, Dev]
11. O backend está preparado para o volume de produção (scaling, database indexing, connection pooling)? [fonte: DevOps, Arquiteto] [impacto: DevOps, Dev]
12. O diagnóstico remoto está funcional (visualizar status de sync por dispositivo, logs de crash, estado de queue)? [fonte: Dev] [impacto: Dev]
13. O process de deploy de hotfix está testado e tem prazo definido (build → aprovação → MDM → dispositivo)? [fonte: Dev, TI, Governança] [impacto: Dev, DevOps]
14. Os KPIs de adoção foram definidos (taxa de uso, registros por dia, completude de formulário, erros de sync)? [fonte: Operações, PM] [impacto: PM, Produto]
15. A janela de go-live foi escolhida estrategicamente (evitar final de mês, pico de operação, feriado)? [fonte: Operações, PM, Diretoria] [impacto: PM]

---

## Etapa 10 — Go-Live

- **Execução do piloto e monitoramento intensivo**: Iniciar o piloto com o grupo restrito definido e monitorar intensivamente nas primeiras 48h: crash-free rate em tempo real (Crashlytics), taxa de sync com sucesso vs. falha por dispositivo, uso real por operador (quantos registros por dia, quais telas são mais usadas), e incidentes reportados ao helpdesk. Designar um membro do time de desenvolvimento como "ponto focal" disponível durante o horário operacional do piloto para resolver problemas em tempo real. O piloto não é "liga e esquece" — é acompanhamento ativo.

- **Coleta de feedback estruturado do piloto**: Após 1 semana de piloto, realizar sessão de feedback estruturado com os operadores: o que funciona bem, o que é difícil de usar, o que está faltando, e o que precisa mudar. Feedback deve ser coletado de forma padronizada (formulário com perguntas fixas + espaço livre) e priorizado com o sponsor. Itens que são bloqueadores operacionais (impedimento para executar o trabalho) devem ser corrigidos antes de expandir o rollout. Itens que são inconveniências (trabalhoso mas funciona) podem ser corrigidos na próxima versão.

- **Expansão gradual do rollout**: Após piloto bem-sucedido (métricas dentro dos critérios de sucesso, bugs S1/S2 corrigidos), expandir o rollout em ondas: segunda unidade/equipe → demais unidades → todas as unidades. Cada onda deve ter período de estabilização (mínimo 1 semana) antes de avançar para a próxima. O MDM facilita a expansão — basta adicionar novos grupos de dispositivos ao perfil de distribuição. O treinamento deve ser realizado antes de cada onda, não apenas na primeira.

- **Desativação do processo anterior**: A desativação do processo manual/legado só deve acontecer após: todas as ondas de rollout estarem concluídas, métricas de adoção confirmarem que todos os operadores estão usando o app consistentemente (>90% de aderência), e um período de sobreposição ter passado sem incidentes graves. A desativação deve ser comunicada formalmente e com antecedência ("a partir da data X, apenas o app será aceito para registro de ordens de serviço"). Manter backup do sistema legado por pelo menos 90 dias após desativação — para acesso histórico e contingência.

- **Monitoramento de adoção e métricas operacionais**: Acompanhar as métricas de adoção definidas na Launch Prep: taxa de uso diário por operador, volume de registros criados no app vs. no processo anterior (se ainda existir), tempo médio de conclusão do processo no app vs. no processo anterior, e taxa de erro de sync. Comparar com os KPIs de negócio que justificaram o projeto: se o app foi feito para reduzir tempo de inspeção, medir se o tempo de inspeção realmente reduziu. Se foi para reduzir erros de preenchimento, medir a taxa de registros com dados inválidos.

- **Entrega e handoff ao time de operação**: Entregar formalmente: acesso ao repositório com documentação de build e deploy, acesso ao console do MDM com guia de distribuição, acesso ao dashboard de monitoramento com explicação das métricas e alertas, documentação de troubleshooting (problemas comuns e como resolver), runbook de operações (como gerar build, como distribuir via MDM, como verificar status de sync, como escalar incidente), e contato de suporte N3 (time de desenvolvimento para bugs complexos). O handoff deve incluir sessão presencial com o time de operação que assumirá a manutenção.

### Perguntas

1. O piloto foi iniciado com monitoramento intensivo e ponto focal de desenvolvimento disponível? [fonte: PM, Dev, Operações] [impacto: Dev, PM]
2. O crash-free rate no piloto está acima de 99.5% e a taxa de sync com sucesso está acima de 98%? [fonte: Dev, QA] [impacto: Dev]
3. Os operadores do piloto estão conseguindo executar o processo de negócio completo usando apenas o app? [fonte: Operações, Usuários-chave] [impacto: PM, Dev]
4. A sessão de feedback estruturado foi realizada e os bloqueadores operacionais foram corrigidos? [fonte: PM, Operações] [impacto: Dev, PM]
5. A expansão do rollout está seguindo o plano de ondas com período de estabilização entre cada onda? [fonte: PM, Operações] [impacto: PM]
6. O treinamento está sendo realizado para cada nova onda antes da ativação? [fonte: RH, PM, Operações] [impacto: PM]
7. As métricas de adoção estão dentro dos KPIs definidos (taxa de uso, registros por dia, aderência)? [fonte: PM, Operações, Data] [impacto: PM, Produto]
8. Os KPIs de negócio estão melhorando conforme esperado (tempo de processo, taxa de erro, retrabalho)? [fonte: Operações, Diretoria] [impacto: PM]
9. A desativação do processo anterior está planejada com comunicação, data definida e backup por 90 dias? [fonte: Operações, TI, Diretoria] [impacto: PM]
10. O monitoramento está estável e os alertas estão calibrados (sem falsos positivos excessivos)? [fonte: DevOps, Dev] [impacto: DevOps]
11. O suporte está operando dentro do SLA definido e os incidentes estão sendo resolvidos nos prazos? [fonte: TI, PM] [impacto: PM]
12. Todos os acessos foram entregues formalmente (repositório, MDM, monitoramento, documentação, runbook)? [fonte: Dev, DevOps, PM] [impacto: PM]
13. O aceite formal de entrega foi obtido do sponsor e da operação? [fonte: Diretoria, Operações] [impacto: PM]
14. O plano de manutenção contínua foi ativado (equipe designada, SLA, canal de comunicação)? [fonte: Diretoria, TI, PM] [impacto: PM, Dev]
15. O processo de atualização do app via MDM está documentado e foi validado com uma atualização de teste? [fonte: Dev, TI] [impacto: Dev, DevOps]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos digitalizar tudo de uma vez"** — O cliente quer colocar 10 processos no mesmo app no lançamento. Projetos enterprise com escopo amplo demais atrasam indefinidamente e entregam UX ruim. O correto é digitalizar 1-2 processos prioritários, validar, e expandir em fases.
- **"InfoSec a gente envolve depois"** — Descobrir requisitos de segurança no QA (criptografia, certificate pinning, penetration test) gera semanas de retrabalho. InfoSec deve ser envolvido desde a Inception para definir requisitos antes da Architecture.
- **"Os funcionários vão usar o celular pessoal, sem problema"** — BYOD sem política formal de MDM e separação de dados pessoais/corporativos é risco de compliance (LGPD) e segurança. Se BYOD, definir políticas formais antes de avançar.

### Etapa 02 — Discovery

- **"Offline não é tão importante, sempre tem Wi-Fi"** — Em empresas, "sempre tem Wi-Fi" ignora: fábricas com zonas mortas, campos sem cobertura, e Wi-Fi corporativo que cai durante manutenção. Se o operador não pode trabalhar quando a rede cai, o app tem um SPoF (Single Point of Failure). Mapear cenários reais de conectividade com operadores reais.
- **"A API do SAP está documentada, é só integrar"** — API "documentada" em contexto enterprise frequentemente significa: documentação de 3 anos atrás, endpoints deprecados não removidos, e comportamentos não-documentados que só o analista que configurou conhece. Planejar 2-3x o tempo estimado para cada integração com sistema legado.
- **"Todos os usuários têm o mesmo acesso"** — Ignorar modelo de permissões em app enterprise gera risco de segurança (operador acessa dados de outro departamento) e compliance (auditor questiona quem alterou qual registro). Matriz de permissões é obrigatória.

### Etapa 03 — Alignment

- **"TI vai liberar os acessos quando precisarmos"** — Liberação de VPN, firewall, credenciais de API, e registro de app no Azure AD em ambiente corporativo leva de dias a semanas, e passa por processos de aprovação. Solicitar todos os acessos na Inception, não no Setup.
- **"O design pode ser simples, os operadores não ligam para visual"** — Operadores não ligam para estética, mas ligam muito para eficiência. Um formulário com 20 campos sem defaults, sem scan de barcode, e com botões pequenos em app de campo faz o operador odiar o app e resistir à adoção. Design operacional precisa de validação com operadores reais.
- **"Não precisamos de MDM, é só instalar manualmente"** — Distribuição manual de app enterprise (enviar APK por e-mail, instalar manualmente) é insustentável com mais de 20 dispositivos. Atualizações dependem do operador, dispositivos ficam em versões diferentes, e não há controle de compliance. MDM é investimento obrigatório.

### Etapa 04 — Definition

- **"O sync pode ser simples, é só upload e download"** — Sync "simples" ignora: conflitos quando dois operadores editam o mesmo registro offline, retry de upload que falha no meio, e consistência de dados quando o servidor rejeita uma operação da queue. Sync é a funcionalidade mais complexa de apps enterprise offline — especificação detalhada é obrigatória.
- **"As regras de aprovação são fixas, não vão mudar"** — Regras de alçada e workflow mudam o tempo todo em empresas (novo diretor, nova política, nova regulação). Hardcodar regras no app significa nova versão a cada mudança. Regras devem ser parametrizáveis no backend.
- **"O relatório pode ser só uma tela com dados"** — Se o operador precisa compartilhar o resultado (enviar para gestor, arquivar para auditoria), uma tela não basta — precisa ser PDF ou formato exportável. Definir o uso do relatório antes de decidir o formato.

### Etapa 05 — Architecture

- **"Vamos usar Firebase, é mais rápido"** — Firebase para apps enterprise tem problemas sérios: dados em cloud pública do Google (pode violar política de dados da empresa), lock-in com plataforma, queries limitadas no Firestore, e sem controle de onde os dados ficam geograficamente. Para enterprise, backend on-premise ou cloud privada é geralmente obrigatório.
- **"O app fala direto com o SAP"** — App mobile fazendo chamadas diretas para API de ERP é anti-pattern: sem camada de cache (cada requisição vai para o ERP), sem isolamento de falha (ERP down = app down), e sem possibilidade de transformar dados. BFF (Backend for Frontend) é obrigatório.
- **"Não precisamos de monitoramento de sync"** — Sem monitoramento, o time só descobre que o sync está falhando quando o operador liga reclamando. Com 200 dispositivos em campo, monitorar proativamente (dashboards de sync rate, alertas de falha) é obrigatório.

### Etapa 06 — Setup

- **"O time de TI vai liberar o ambiente na semana que vem"** — "Semana que vem" em TI corporativa vira 3-4 semanas com facilidade. Dependências de TI (VPN, APIs, MDM, Azure AD) devem ser solicitadas com 4-6 semanas de antecedência, com tracking formal no projeto.
- **Ambientes não isolados** — Usar APIs de produção durante desenvolvimento porque "staging não tem dados". Além do risco de poluir produção, viola políticas de segurança. Insistir em ambientes de staging com dados de teste realistas.
- **"O MDM já está configurado, é só subir o app"** — Configuração de MDM para novo app envolve: criar perfil, definir políticas, configurar grupos, testar distribuição — não é "só subir". Planejar 1-2 sprints para setup completo de MDM.

### Etapa 07 — Build

- **Testando sync apenas com 5 registros** — Sync que funciona com 5 registros pode falhar com 5.000. Testar com volume realista desde o início do build — incluir stress test de sync no pipeline de testes.
- **Ignorando estados de sync na UI** — O operador não sabe se seus dados foram sincronizados. Sem indicador claro de status (pendente, enviando, sincronizado, erro), o operador registra o mesmo dado duas vezes ou pensa que enviou quando não enviou. Indicador de sync é obrigatório em cada tela com dados.
- **Dependendo de APIs de staging que estão instáveis** — APIs de staging em ambiente enterprise são frequentemente instáveis (reiniciam no fim de semana, ficam sem dados após limpeza). O build não pode ficar bloqueado por indisponibilidade de staging — mocks locais devem existir como fallback.

### Etapa 08 — QA

- **"O UAT vai ser o time de TI testando"** — TI testa se funciona tecnicamente. Operadores testam se funciona operacionalmente. UAT sem operadores reais perde o principal objetivo: validar que o app serve para o trabalho real. Insistir em operadores reais no UAT.
- **QA sem testar offline por jornada completa** — Testar offline por 5 minutos é diferente de testar por 8 horas. Queue de sync cresce, memória acumula, e problemas que não aparecem em teste curto aparecem em jornada real. Testar jornada completa é obrigatório.
- **"O penetration test pode ficar para depois do go-live"** — Em ambiente enterprise, descobrir vulnerabilidade de segurança após o go-live pode resultar em: app desativado por InfoSec, incidente de segurança reportado, e responsabilização contratual. Pentest antes do go-live.

### Etapa 09 — Launch Prep

- **"Vamos lançar para todo mundo de uma vez"** — Big bang em app enterprise é alto risco. Se o sync tem um bug que afeta 5% dos registros, com 500 operadores = centenas de registros perdidos ou corrompidos. Piloto controlado com grupo restrito antes do rollout geral é obrigatório.
- **Treinamento apenas em sala com slides** — Operador de campo/fábrica não absorve treinamento em PowerPoint. Treinamento deve ser com o dispositivo real, executando o processo real, supervisionado. Material de referência rápida (laminated quick card) substitui manual de 50 páginas.
- **"O sistema legado pode ser desligado no dia do go-live"** — Sem período de sobreposição, não há fallback se o app tiver problema. O sistema legado deve permanecer ativo durante todo o piloto e pelo menos 30 dias após o rollout geral completo.

### Etapa 10 — Go-Live

- **Piloto sem métricas de sucesso definidas** — "O piloto foi bem" baseado em feeling. Sem métricas objetivas (crash rate, sync rate, registros/dia, tickets de suporte), não há critério para expandir ou recuar. Métricas antes do piloto, revisão de métricas antes da expansão.
- **Expandir rollout antes de corrigir problemas do piloto** — Pressão de prazo leva a expandir mesmo com bugs conhecidos. Se o piloto revelou bug de sync que afeta 2% dos registros, expandir para 500 operadores significa 10 registros perdidos por dia. Corrigir antes de expandir.
- **Encerrar o projeto sem runbook de operações** — O time de desenvolvimento vai embora e ninguém sabe: como gerar build, como distribuir via MDM, como verificar sync, como resolver incidentes. Runbook de operações é entregável obrigatório antes do encerramento.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é app enterprise** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "O app vai estar nas lojas para qualquer pessoa baixar" | App consumer, não enterprise | Reclassificar para mobile-app-consumer |
| "Os clientes da empresa vão usar para fazer pedidos" | App consumer (B2C) ou e-commerce | Reclassificar para mobile-app-consumer ou e-commerce |
| "É um app para os clientes finais, não para funcionários" | App consumer, público externo | Reclassificar para mobile-app-consumer |
| "Na verdade não precisa ser app, pode ser um site responsivo" | Web app responsivo | Reclassificar para web-app |
| "É mais um sistema desktop que queremos acessar do celular" | Remote desktop ou web app com responsividade | Avaliar se web-app ou Citrix/RDP resolve |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos qual é o processo que o app vai digitalizar" | 01 | Sem processo definido, app não tem escopo | Mapear processo antes de iniciar Discovery |
| "TI não foi envolvida ainda" | 01 | Todas as integrações, segurança e infra bloqueadas | Envolver TI imediatamente — sem TI, o projeto não avança |
| "Não temos MDM e não pretendemos comprar" | 01 | Distribuição e gerenciamento de 200+ dispositivos inviável | MDM é prerequisito para apps enterprise em escala |
| "A API do sistema X não existe, vamos precisar criar" | 02 | Escopo de backend dobra ou triplica | Incluir desenvolvimento de API no escopo e orçamento |
| "Não sabemos como o processo funciona exatamente" | 02 | App vai digitalizar processo errado | Fazer mapeamento de processo antes do Discovery |
| "InfoSec exige penetration test mas não temos fornecedor" | 03 | Go-live bloqueado por pentest não planejado | Contratar fornecedor de pentest e incluir 4-6 semanas no cronograma |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Os operadores de campo resistem a mudanças" | 01 | Baixa adoção — app implementado mas não usado | Planejar change management robusto com sponsor forte |
| "O ERP é customizado e só uma pessoa sabe como funciona" | 02 | Dependência de pessoa única para integração — bus factor = 1 | Documentar integração e envolver backup |
| "Os dispositivos corporativos são antigos (Android 8, 3GB RAM)" | 02 | Performance e compatibilidade limitadas | Testar em dispositivos representativos desde o setup |
| "O processo manual funciona, mas é lento" | 01 | ROI do app depende de ganho de eficiência — precisa ser mensurável | Medir baseline do processo manual para comparar pós-app |
| "Cada unidade tem suas particularidades no processo" | 02 | Customização por unidade explode complexidade | Documentar variações e decidir: padronizar ou parametrizar |
| "Não temos orçamento para manutenção contínua" | 01 | App obsoleto e inseguro em 12-18 meses | Incluir OPEX no business case ou alertar sobre risco |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Processo de negócio a digitalizar identificado (pergunta 1)
- Sponsor com autoridade orçamentária definido (pergunta 2)
- Política de dispositivos (COPE/BYOD) e MDM definida (perguntas 3 e 4)
- Sistemas a integrar identificados (pergunta 5)
- InfoSec envolvido e requisitos de segurança mapeados (pergunta 6)
- Orçamento CAPEX + OPEX aprovado (pergunta 10)

### Etapa 02 → 03

- Processo de negócio mapeado em detalhe (pergunta 1)
- Requisitos de offline definidos com escopo claro (pergunta 2)
- APIs disponíveis e responsáveis técnicos identificados (pergunta 3)
- Modelo de autenticação SSO confirmado com TI (pergunta 4)
- Dispositivos e condições de uso inventariados (perguntas 6 e 7)

### Etapa 03 → 04

- Stack validada e aprovada por TI e InfoSec (pergunta 1)
- Modelo de distribuição definido e aprovado (pergunta 3)
- Design validado com usuários reais nas condições de uso (pergunta 5)
- Plano de treinamento e change management definido (pergunta 8)

### Etapa 04 → 05

- Mapa de telas validado com usuários operacionais (pergunta 1)
- Cenários de conflito offline documentados com regras de resolução (pergunta 3)
- Matriz de permissões por papel definida (pergunta 4)
- Documentação de definição aprovada por operações, TI e diretoria (pergunta 15)

### Etapa 05 → 06

- Arquitetura offline-first desenhada com sync engine (pergunta 1)
- BFF projetado para isolar integrações corporativas (pergunta 2)
- Segurança em profundidade validada por InfoSec (pergunta 3)
- Pipeline de CI/CD desenhado dentro das ferramentas corporativas (pergunta 5)
- ADR aprovado por TI, InfoSec e diretoria (pergunta 15)

### Etapa 06 → 07

- Ambientes configurados com acesso à rede corporativa (perguntas 2 e 3)
- MDM configurado e fluxo de distribuição testado (pergunta 4)
- SSO integrado e login funcional em dispositivo real (pergunta 5)
- Sync engine básico funcionando (pergunta 7)
- Pipeline de CI/CD testado end-to-end (pergunta 10)

### Etapa 07 → 08

- Sync engine implementado com queue, retry e resolução de conflitos (perguntas 2 e 3)
- Integrações com sistemas corporativos implementadas com circuit breaker (pergunta 4)
- Testes com dados reais de staging (não mocks) realizados (pergunta 9)
- Builds de UAT sendo distribuídos via MDM com feedback incorporado (pergunta 15)

### Etapa 08 → 09

- UAT realizado com operadores reais em condições reais (pergunta 1)
- Teste de offline intensivo concluído sem perda de dados (pergunta 2)
- Teste de segurança e pentest concluídos (perguntas 4 e 5)
- Crash-free rate >99.5% (pergunta 9)
- Bugs S1 e S2 do UAT corrigidos (pergunta 15)

### Etapa 09 → 10

- Piloto planejado com grupo, duração e métricas de sucesso (pergunta 1)
- MDM configurado para produção (pergunta 3)
- Treinamento presencial realizado para grupo do piloto (pergunta 5)
- Plano de rollback operacional documentado (pergunta 7)
- Backend preparado para volume de produção (pergunta 11)

### Etapa 10 → Encerramento

- Piloto concluído com métricas dentro dos critérios de sucesso (perguntas 2 e 7)
- Rollout geral concluído em todas as ondas (pergunta 5)
- KPIs de negócio mostrando melhoria (pergunta 8)
- Acessos e runbook entregues formalmente (pergunta 12)
- Aceite formal do sponsor e operação (pergunta 13)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de app enterprise. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Campo | V2 Portal | V3 Workflow | V4 Coleta | V5 Operação |
|---|---|---|---|---|---|
| 01 Inception | 3 | 2 | 3 | 2 | 3 |
| 02 Discovery | 4 | 3 | 4 | 3 | 4 |
| 03 Alignment | 3 | 3 | 3 | 2 | 3 |
| 04 Definition | 4 | 3 | 5 | 3 | 4 |
| 05 Architecture | 5 | 3 | 4 | 4 | 5 |
| 06 Setup | 3 | 3 | 3 | 3 | 3 |
| 07 Build | 5 | 3 | 4 | 4 | 4 |
| 08 QA | 4 | 3 | 3 | 4 | 4 |
| 09 Launch Prep | 4 | 3 | 3 | 3 | 4 |
| 10 Go-Live | 4 | 3 | 3 | 3 | 4 |
| **Total relativo** | **39** | **29** | **35** | **31** | **38** |

**Observações por variante:**

- **V1 Campo**: O mais pesado. Architecture e Build são dominados pela sync engine offline e integração com ERP. QA e Go-Live são pesados pela necessidade de testar em campo real e fazer piloto com equipe externa.
- **V2 Portal**: O mais leve. Backend simples (conteúdo + auth), sem offline pesado, sem integrações complexas. O desafio é mais de change management (adoção por todos os colaboradores) do que técnico.
- **V3 Workflow**: Definition é o pico — regras de alçada, fluxos de aprovação, estados complexos. Build é moderado porque a lógica pesada está no backend (regras parametrizáveis), não no app. Integração com ERP pode ser o maior risco.
- **V4 Coleta**: Architecture é pesada por causa do offline-first com volume alto de dados e fotos. QA é pesado pela necessidade de testar sync com centenas de registros e fotos em cenários de campo real.
- **V5 Operação**: Compete com V1 em complexidade. Architecture inclui integrações IoT/MES que são instáveis e mal documentadas. Go-Live é pesado pela necessidade de treinamento de operadores com baixa maturidade digital em chão de fábrica.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| App funciona apenas online, sem offline (Etapa 02, pergunta 2) | Etapa 04: pergunta 3 (cenários de conflito offline). Etapa 05: pergunta 1 (arquitetura offline-first se reduz a cache básico). Etapa 06: pergunta 6 (banco local e queue de sync). Etapa 07: perguntas 2, 3 e 12 (sync engine, conflitos, indicador de sync). Etapa 08: pergunta 2 (teste offline intensivo). |
| Dispositivos COPE com modelo único (Etapa 01, pergunta 3) | Etapa 02: pergunta 6 (inventário de dispositivos simplificado — modelo único). Etapa 08: pergunta 6 (teste em parque diverso — apenas um modelo). |
| Sem integração com sistemas legados — backend próprio apenas (Etapa 01, pergunta 5) | Etapa 02: pergunta 3 (APIs de sistemas corporativos). Etapa 05: pergunta 2 (BFF para abstrair integrações). Etapa 07: pergunta 4 (circuit breaker para sistemas corporativos). Etapa 08: pergunta 3 (teste de integração end-to-end com sistemas). |
| Sem relatórios no app — consolidação em BI (Etapa 02, pergunta 12) | Etapa 04: pergunta 6 (especificação de relatórios). Etapa 07: pergunta 8 (geração de PDF offline). Etapa 08: pergunta 10 (validação de relatórios). |
| Dispositivo individual, não compartilhado — V1, V2, V3 | Etapa 04: pergunta 10 (login rápido por PIN/crachá). Etapa 07: pergunta 6 (login rápido). Etapa 08: pergunta 11 (troca de turno). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Offline obrigatório — V1, V4, V5 (Etapa 02, pergunta 2) | Etapa 04: pergunta 3 (cenários de conflito) se torna gate obrigatório. Etapa 05: pergunta 1 (arquitetura offline-first) é a decisão mais crítica. Etapa 07: perguntas 2 e 3 (sync engine e conflitos) dominam o esforço de build. Etapa 08: pergunta 2 (teste offline 8h) é bloqueadora. |
| Integração com ERP/sistema legado (Etapa 01, pergunta 5) | Etapa 02: pergunta 3 (documentação e responsável de API) se torna bloqueadora. Etapa 05: pergunta 2 (BFF obrigatório). Etapa 06: pergunta 3 (acesso a APIs de staging antes do build). Etapa 08: pergunta 3 (teste de integração end-to-end). |
| Setor regulado — SOX, HIPAA, ANVISA, BACEN (Etapa 01, pergunta 15) | Etapa 02: pergunta 8 (auditoria e rastreabilidade) se torna gate. Etapa 05: pergunta 11 (logs imutáveis, SIEM). Etapa 08: perguntas 4 e 5 (teste de segurança e pentest) se tornam bloqueadoras. Etapa 09: homologação regulatória antes do go-live. |
| Dispositivos compartilhados — V5 Operação (Etapa 02, pergunta 7) | Etapa 04: pergunta 10 (login rápido) se torna gate. Etapa 07: pergunta 6 (implementação de login PIN/crachá). Etapa 08: pergunta 11 (teste de troca de turno). |
| BYOD confirmado (Etapa 01, pergunta 3) | Etapa 02: pergunta 6 (inventário de dispositivos) se torna crítica — range enorme de modelos. Etapa 05: pergunta 3 (segurança com foco em separação de dados pessoais/corporativos). Etapa 08: pergunta 6 (teste em dispositivos diversos) se torna significativamente mais pesada. Etapa 09: app protection policies no MDM (DLP, prevent copy-paste). |
| Volume alto de dados/fotos — V4 Coleta (Etapa 02, pergunta 9) | Etapa 05: storage e compressão na arquitetura. Etapa 07: pergunta 7 (coleta com compressão e save automático). Etapa 08: pergunta 8 (teste de performance com volume real). Etapa 09: pergunta 11 (backend preparado para batch upload). |
