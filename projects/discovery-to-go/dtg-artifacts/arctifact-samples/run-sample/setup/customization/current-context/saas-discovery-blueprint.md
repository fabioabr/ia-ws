---
title: Discovery Blueprint — SaaS
pack-id: saas
description: Blueprint completo de discovery para projetos SaaS multi-tenant — guia de componentes, concerns, perguntas, antipatterns, especialistas disponíveis e perfil do delivery report. Documento único e auto-contido que o orchestrator carrega na Fase 1.
version: 02.00.000
status: ativo
author: claude-code
category: discovery-blueprint
area: tecnologia
tags:
  - discovery-blueprint
  - saas
  - multi-tenant
  - billing
  - context-template
  - spec-pack
  - report-profile
created: 2026-04-11
---

# Discovery Blueprint — SaaS

Documento completo e auto-contido para conduzir o discovery de um projeto SaaS multi-tenant. Organizado em **4 componentes** que representam as partes concretas da solução, seguido de antipatterns, edge cases, especialistas disponíveis e perfil do delivery report.

Serve como guia tanto para os agentes de IA (carregado pelo orchestrator na Fase 1) quanto para o humano que acompanha o processo.

---

## Quando usar este blueprint

O orchestrator deve carregar este blueprint quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Menção a "produto", "plataforma", "serviço" oferecido a múltiplos clientes/empresas
- Termos: tenant, multi-tenant, assinatura, mensalidade, plano, billing, faturamento recorrente
- Modelo comercial subscription-based ou pay-per-use
- Necessidade de onboarding self-service
- Escalabilidade horizontal mencionada
- Cliente não é dono da infraestrutura — é usuário do produto

---

## Visão geral dos componentes

```mermaid
flowchart LR
    U["Usuário Final\n(Signup, Uso)"] --> A["1. Produto e\nModelo Comercial"]
    A --> B["2. Tenancy e\nInfraestrutura"]
    B --> C["3. Billing e\nMonetização"]
    C --> D["4. Operação e\nCrescimento"]
    D --> U

    style A fill:#2EB5F5,color:#1A1923
    style B fill:#F4AC00,color:#1A1923
    style C fill:#9B96FF,color:#1A1923
    style D fill:#0ED145,color:#1A1923
```

| # | Componente | O que define | Blocos do discovery |
|---|-----------|-------------|-------------------|
| 1 | Produto e Modelo Comercial | Personas, JTBD, pricing, tiers, onboarding, time-to-value | #1, #2, #3, #4 |
| 2 | Tenancy e Infraestrutura | Multi-tenant strategy, isolamento, scaling, rate limiting, SSO | #5, #6, #7 |
| 3 | Billing e Monetização | Gateway de pagamento, planos, trial, churn, revenue recognition | #5, #7, #8 |
| 4 | Operação e Crescimento | Observabilidade per tenant, on-call, feature flags, SLA, CI/CD | #5, #7, #8 |

---

## Componente 1 — Produto e Modelo Comercial

Define **o quê** o SaaS oferece, **para quem** e **como cobra**. Sem clareza aqui, decisões técnicas ficam no vácuo — não dá pra definir isolamento de tenants sem saber quantos tiers existem, nem billing sem saber o modelo comercial.

### Concerns

- **Persona primária e secundárias** — Quem compra versus quem usa? Decisor é diferente do operador?
- **Job to be done principal** — Qual o problema central que o produto resolve?
- **Modelo comercial** — Free trial, freemium, pago direto, tiered? Combinações?
- **Planos e diferenciação entre tiers** — O que diferencia Basic de Pro de Enterprise? Features, limites, SLA?
- **Onboarding** — Self-service, assistido ou white-glove? Depende do tier?
- **Time-to-value** — Quanto tempo entre signup e o primeiro valor percebido pelo usuário?
- **OKRs e métricas norte** — Ativação, retenção, NPS, MRR, LTV, churn
- **ROI esperado** — Qual o retorno esperado do investimento no produto?
- **Diferenciação competitiva** — O que torna este SaaS diferente dos concorrentes?
- **Roadmap** — MVP, Fase 2, Fase 3 — o que entra em cada momento?

### Perguntas-chave

1. Quem é a persona primária? E as secundárias? (quem compra vs quem usa)
2. Qual o job to be done principal do produto?
3. Qual o modelo comercial? (free trial / freemium / pago / tiered)
4. Quantos planos/tiers existem? O que diferencia cada um?
5. O onboarding é self-service, assistido ou white-glove? Muda por tier?
6. Qual o time-to-value esperado? (tempo entre signup e primeiro valor)
7. Quais são os OKRs? (ativação, retenção, NPS, MRR, LTV, churn)
8. Qual o ROI esperado?
9. O que diferencia este produto dos concorrentes?
10. O que entra no MVP vs Fase 2 vs Fase 3?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Modelo comercial | Free trial / Freemium / Pago / Tiered | Segmento de mercado, CAC aceitável, velocidade de adoção |
| Estratégia de onboarding | Self-service / Assistido / White-glove | Complexidade do produto, ticket médio, escala desejada |
| Diferenciação entre tiers | Por features / Por limites / Por SLA / Combinação | Willingness-to-pay por segmento |
| Roadmap de fases | MVP mínimo / MVP robusto / Big bang | Budget, time-to-market, risco aceitável |
| Métricas norte | Ativação / MRR / Churn / NPS | Estágio do produto (early vs growth vs mature) |

### Critérios de completude

- [ ] Persona primária e secundárias definidas com clareza
- [ ] Job to be done principal articulado
- [ ] Modelo comercial definido com justificativa
- [ ] Planos/tiers documentados com diferenciação clara
- [ ] Estratégia de onboarding definida por tier
- [ ] Time-to-value estimado
- [ ] OKRs mensuráveis definidos (não vagos)
- [ ] Roadmap MVP vs fases posteriores documentado

**Sinais de resposta incompleta:**
- "Para empresas em geral" (sem segmentação)
- "Vamos ver o preço depois" (ausência de modelo comercial)
- "Vai funcionar pra todo mundo" (sem persona clara)
- "Queremos ter sucesso" (OKR vago)

---

## Componente 2 — Tenancy e Infraestrutura

Define **como** os múltiplos clientes (tenants) coexistem na mesma plataforma. Decisões de isolamento, segurança e escalabilidade são tomadas aqui. Erros nesta camada são caros para corrigir depois — migrar de row-level para database-per-tenant em produção é uma refatoração massiva.

### Concerns

- **Multi-tenant strategy** — Database-per-tenant, schema-per-tenant ou row-level? Trade-off entre isolamento, custo e complexidade
- **Isolamento de dados** — Como garantir que Tenant A nunca vê dados de Tenant B?
- **Escalabilidade** — Vertical vs horizontal vs particionamento? O que acontece quando o tenant mais pesado atinge 10x o volume atual?
- **Rate limiting** — Limites por tenant, por plano, por endpoint? O que acontece ao atingir o limite?
- **Autenticação e autorização** — OAuth2, SAML, magic link? 2FA? SSO corporativo para Enterprise?
- **Secrets management** — Como gerenciar credenciais, API keys, certificados?
- **Criptografia** — At-rest e in-transit obrigatórias? BYOK para enterprise?
- **Stack tecnológica** — Cloud provider, linguagem, banco de dados (SQL vs NoSQL vs híbrido), cache, fila de mensagens
- **Arquitetura macro** — Monolito modular vs microsserviços? Sync vs async?
- **Migração de schema** — Como fazer schema migration com zero-downtime em banco multi-tenant?

### Perguntas-chave

1. Como será o isolamento entre tenants? (database-per-tenant, schema-per-tenant, row-level)
2. Algum tenant pode ter SLA diferenciado? (ex: enterprise com database dedicado)
3. Qual a estratégia de rate limit por tenant? E por plano?
4. Qual o stack? Cloud provider, linguagem, banco, cache, fila?
5. Monolito modular ou microsserviços? Sync ou async?
6. Como escalar quando o tenant mais pesado atingir 10x o volume atual?
7. Autenticação: OAuth2, SAML, magic link? SSO corporativo para enterprise?
8. Criptografia at-rest e in-transit: quem gerencia as chaves?
9. Como fazer schema migration com zero-downtime?
10. Qual a estratégia de backup e disaster recovery?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Multi-tenant strategy | Database-per-tenant / Schema-per-tenant / Row-level | Isolamento regulatório, custo, complexidade operacional |
| Escalabilidade | Vertical / Horizontal / Particionamento | Volume esperado, padrão de uso, budget |
| Autenticação | OAuth2 / SAML / Magic link / Combinação | Mercado alvo (SMB = OAuth2, Enterprise = SAML) |
| Arquitetura | Monolito modular / Microsserviços | Tamanho do time, estágio do produto, complexidade |
| Cloud provider | AWS / GCP / Azure / Multi-cloud | Skills do time, integrações, pricing |

### Critérios de completude

- [ ] Multi-tenant strategy definida com justificativa
- [ ] Isolamento de dados documentado (como garantir separação)
- [ ] Estratégia de rate limiting definida por plano/tier
- [ ] Stack tecnológica definida (cloud, linguagem, banco, cache, fila)
- [ ] Arquitetura macro definida (monolito vs microsserviços)
- [ ] Estratégia de autenticação definida (incluindo SSO enterprise)
- [ ] Plano de escalabilidade documentado
- [ ] Backup e disaster recovery definidos

---

## Componente 3 — Billing e Monetização

Define **como** o SaaS cobra, processa pagamentos e gerencia o ciclo de vida financeiro do cliente. Decisões entre build vs buy (Stripe/Chargebee/custom) impactam diretamente o time-to-market e custo operacional. Billing custom no MVP é um dos antipatterns mais comuns em SaaS.

### Concerns

- **Gateway de pagamento** — Stripe, Chargebee, Adyen, custom? Build vs Buy?
- **Modelo de cobrança** — Assinatura fixa, usage-based, per-seat, híbrido?
- **Planos e upgrade/downgrade** — Proration? Mudança imediata ou no próximo ciclo?
- **Free trial** — Duração? Critério de conversão? O que acontece ao expirar?
- **Dunning** — Retry automático de pagamento falhado? Quantas tentativas? Suspensão ou cancelamento?
- **Múltiplas moedas** — Suporte a moedas internacionais? Conversão? Tax compliance?
- **Revenue recognition** — Como reconhecer receita para contabilidade? (especialmente para annual plans)
- **Churn** — Como detectar sinais precoces de churn? Métricas de engajamento como proxy?
- **Cupons e descontos** — Estratégia promocional? Cupons one-time vs recurring?
- **Invoicing** — Nota fiscal, fatura, boleto (para Brasil)? Integração com ERP?

### Perguntas-chave

1. Vale construir billing custom ou usar Stripe/Chargebee? Qual a complexidade do modelo de cobrança?
2. Qual o modelo de cobrança? (assinatura fixa, usage-based, per-seat, híbrido)
3. Como funciona upgrade/downgrade entre planos? Proration?
4. Qual a duração do free trial? O que acontece ao expirar?
5. Qual a estratégia de dunning (retry de pagamento falhado)?
6. Precisa suportar múltiplas moedas? Quais?
7. Como será a emissão de nota fiscal / fatura?
8. Como detectar churn precocemente? Quais sinais monitorar?
9. Qual a projeção de MRR/ARR por tier?
10. Se o gateway de pagamento cair por 4 horas, o que acontece?

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Billing platform | Stripe / Chargebee / Custom | Complexidade do modelo, time-to-market, custo (Stripe ~3%, Chargebee fee fixo + variável) |
| Modelo de cobrança | Assinatura fixa / Usage-based / Per-seat / Híbrido | Previsibilidade de receita vs alinhamento com valor entregue |
| Free trial | 7d / 14d / 30d / Sem trial | Complexidade do produto, time-to-value |
| Dunning strategy | 3 retries + suspensão / 5 retries + cancelamento / Manual | Ticket médio, volume de clientes |
| Invoicing | Stripe Invoice / Nota fiscal via API (NFe) / ERP | Mercado (BR exige NFe), volume |

### Critérios de completude

- [ ] Build vs Buy para billing definido com justificativa
- [ ] Modelo de cobrança definido
- [ ] Estratégia de free trial documentada (duração, conversão, expiração)
- [ ] Dunning strategy definida
- [ ] Projeção de MRR/ARR por tier documentada
- [ ] Invoicing / nota fiscal definido
- [ ] Contingência para indisponibilidade do gateway documentada
- [ ] Custo de billing platform estimado (% sobre receita)

---

## Componente 4 — Operação e Crescimento

Define **como** o SaaS é operado, monitorado e evolui após o lançamento. Observabilidade por tenant, on-call, feature flags e SLA são críticos para a sustentabilidade do produto. Sem estes fundamentos, o time apaga incêndios em vez de construir features.

### Concerns

- **Observabilidade per tenant** — Métricas, logs e traces segmentados por tenant? Dashboards por tenant?
- **Alertas e on-call** — Quem responde quando o sistema cai? Runbook? Escalation?
- **SLA e SLO/SLI** — Disponibilidade alvo (3 nines, 4 nines)? Latência p99? Varia por plano?
- **Feature flags** — Como lançar features progressivamente? Por tenant, por plano, por %?
- **CI/CD** — Pipeline de deploy? Canary? Blue-green? Rollback automático?
- **Testes** — Unit, integration, e2e, smoke em prod, canary? Cobertura mínima?
- **Processo de deploy e releases** — Frequência? Quem aprova? Feature freeze?
- **Tamanho e senioridade do time** — Quem opera? Capacidade para on-call?
- **CAC vs LTV** — Custo de aquisição sustentável? LTV/CAC > 3?
- **Custo de observabilidade** — Custo de ferramentas (Datadog, New Relic) escala com nº de tenants?

### Perguntas-chave

1. Observabilidade é segmentada por tenant? (métricas, logs, traces)
2. Quem faz on-call? Tem runbook? Qual o processo de escalation?
3. Qual o SLA de disponibilidade? Varia por plano? (ex: Enterprise = 4 nines, Basic = 3 nines)
4. Como lançar features progressivamente? Feature flags por tenant/plano?
5. Qual a frequência de deploy? Tem canary/blue-green?
6. Qual a estratégia de testes? (unit, integration, e2e, smoke em prod)
7. Qual o tamanho do time? Tem senioridade para on-call?
8. Qual o CAC vs LTV projetado?
9. Custos variáveis por tenant: compute, storage, bandwidth — como projetar?
10. Custo de observabilidade escala como? (por host, por log volume, por tenant)

### Decisões esperadas

| Decisão | Alternativas típicas | Critério |
|---------|---------------------|----------|
| Stack de observabilidade | Datadog / New Relic / Grafana+Prometheus / Cloud nativo | Budget, features necessárias, custo por escala |
| SLA por plano | Uniforme / Diferenciado por tier | Willingness-to-pay enterprise, custo de garantir uptime |
| Feature flags | LaunchDarkly / Flagsmith / Custom | Volume de flags, complexidade de targeting |
| Deploy strategy | Canary / Blue-green / Rolling / Feature branch deploy | Risco aceitável, velocidade desejada |
| On-call | Time dedicado / Rotação / Terceirizado | Tamanho do time, maturidade |

### Critérios de completude

- [ ] Observabilidade per tenant definida (métricas, logs, traces)
- [ ] On-call definido (quem, runbook, escalation)
- [ ] SLA/SLO/SLI definidos por plano
- [ ] Feature flags strategy definida
- [ ] CI/CD pipeline documentado (deploy, canary, rollback)
- [ ] Estratégia de testes documentada
- [ ] Projeção de custos variáveis por tenant documentada
- [ ] CAC vs LTV estimados

---

## Concerns transversais — Produto e Organização

Além dos 4 componentes, o discovery precisa cobrir aspectos de produto e organização que atravessam todos os componentes. Estes são endereçados principalmente nos blocos #1 a #4 pelo **po**.

### Valor e métricas

- OKRs mensuráveis: ativação, retenção, NPS, MRR, LTV, churn
- ROI esperado
- CAC vs LTV (cruzando com custos do Componente 4)

### Organização

- Tamanho e senioridade do time
- Processo de deploy e releases
- On-call pós-MVP
- Roadmap MVP vs Fase 2 vs Fase 3

### Sinais de resposta incompleta

- "Para empresas em geral" (sem segmentação)
- "Vamos ver o preço depois" (ausência de modelo comercial)
- "Vai funcionar pra todo mundo" (sem persona clara)
- "Queremos ter sucesso" (OKR vago)

---

## Concerns transversais — Privacidade (bloco #6)

O **cyber-security-architect** sempre roda este bloco. Em SaaS o **modo profundo é quase sempre o caso** porque há dados de contato, uso e telemetria de usuários finais. O modo magro é raro mas possível em produtos B2B puramente técnicos (ex: ferramenta de build, sem dados de pessoa identificáveis).

### Concerns específicos SaaS

- LGPD/GDPR com múltiplas jurisdições (se SaaS global)
- Residência de dados por região (EU → na EU, BR → no BR)
- Política de retenção por tenant e por tier
- Direito ao esquecimento em banco multi-tenant
- Papel de controlador vs operador (quando o cliente é outra empresa)
- Sub-operadores (Stripe, SendGrid, Datadog) — contratos DPA
- Transferência internacional de dados (SCC/cláusulas contratuais padrão)
- Isolamento de dados pessoais entre tenants

---

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|-------------|----------------|
| 1 | **Multi-tenant sem isolamento de dados** | Vazamento de dados entre clientes — risco regulatório e reputacional |
| 2 | **Billing custom no MVP** | Reinventa a roda; Stripe/Chargebee resolvem 90% dos casos |
| 3 | **Sem rate limit por tenant** | Um tenant pesado degrada todos os outros |
| 4 | **Microsserviços antes de validar produto** | Overhead operacional sem benefício; monolito modular cobre o MVP |
| 5 | **Onboarding manual sem self-service** | Custo de aquisição alto, escalabilidade limitada |
| 6 | **Métricas de negócio só no fim do mês** | Decisões reativas; precisa real-time pra detectar churn cedo |
| 7 | **Sem feature flag** | Lançamento all-or-nothing; impossível rollback parcial |
| 8 | **Esquema único sem migração planejada** | Mudanças de schema viram outage |
| 9 | **Free trial sem critério de conversão** | Usuários ficam para sempre no trial, MRR não cresce |
| 10 | **SSO corporativo só "depois"** | Bloqueia vendas enterprise; deveria estar no roadmap desde cedo |

---

## Edge cases para o 10th-man verificar

- O que acontece quando um tenant atinge o limite do plano dele em pleno Black Friday?
- Como recuperar dados de um tenant que cancelou e voltou 3 meses depois?
- Se o gateway de pagamento (Stripe) cair por 4 horas, o que rola com o billing?
- Como migrar um tenant grande (TB de dados) para outra região por compliance?
- Quem responde quando dados de Tenant A vazam para Tenant B?
- Como lidar com um tenant que abusa do rate limit consistentemente?
- Política de quebra de contrato — o que rola com os dados após cancelamento?
- Suporte multi-região: como lidar com latência entre regiões?
- Ataque DDoS direcionado a um tenant específico — afeta os outros?
- Tenant que solicita exclusão LGPD — como remover dados sem quebrar referências históricas?

---

## Custom-specialists disponíveis

Quando po, solution-architect ou cyber-security-architect precisarem de profundidade em subtópico específico durante a reunião, o orchestrator pode invocar um dos specialists abaixo:

| Specialist | Domínio | Quando invocar |
|-----------|---------|----------------|
| `cloud-architecture-aws` | Arquitetura AWS avançada | Stack definida como AWS com requisitos de multi-region, EKS, serverless, ou custo-otimização |
| `cloud-architecture-gcp` | Arquitetura GCP avançada | Stack definida como GCP com Cloud Run, GKE, BigQuery, ou integração com Workspace |
| `cloud-architecture-azure` | Arquitetura Azure avançada | Stack definida como Azure com AKS, Cosmos DB, ou integração com M365/Entra ID |
| `payments-compliance` | Compliance de pagamentos e billing | Pagamentos internacionais, múltiplas moedas, PCI-DSS, anti-fraude, chargebacks, compliance Bacen |
| `enterprise-identity` | SSO corporativo, SAML, federação | Vendas enterprise exigem SAML/SCIM, federação com AD/Okta, ou certificações SOC 2 |
| `ml-engineering` | ML/IA como feature do produto | Produto tem componente de ML (recomendação, classificação, scoring, LLM wrapper) |
| `performance-engineering` | Performance crítica, baixa latência | SLA < 100ms p99, volumes altos, otimização de hot path |
| `multi-tenancy-architect` | Isolamento multi-tenant avançado | Decisão entre database-per-tenant, schema-per-tenant, row-level; isolamento regulatório |
| `billing-platform-advisor` | Escolha e design de billing | Decisão Stripe vs Chargebee vs custom; modelo de cobrança complexo; dunning; revenue recognition |
| `regulated-industry-health` | Compliance em saúde (HIPAA, ANS) | SaaS em saúde com dados clínicos |
| `regulated-industry-finance` | Compliance financeiro (Bacen, CVM) | SaaS financeiro, fintech, crédito |

> [!info] Fallback genérico
> Se o subtópico não casa com nenhum specialist acima, o orchestrator gera um specialist genérico e registra `[CUSTOM-SPECIALIST-GENERIC]` no log.

LGPD/Privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect` (agente fixo, bloco 6).

### Prompt base de invocação

```
Você é o specialist `{specialist-id}` do blueprint saas no Discovery Pipeline v0.5.

Domínio: {domínio da tabela}

Contexto da reunião até aqui:
{log dos blocos já cobertos}

Subtópico que pediram sua ajuda:
{descrição do ponto}

Sua missão:
1. Aprofunda o subtópico com vocabulário real do domínio
2. Sinaliza antipatterns conhecidos
3. Se o customer marcar [INFERENCE] em ponto crítico, force aprofundamento
4. Se o domínio exige especialista humano de verdade, marque [NEEDS-HUMAN-SPECIALIST] e justifique
5. Devolve controle ao especialista fixo que te invocou

Seja honesto sobre suas limitações: você é o mesmo modelo de linguagem assumindo um papel. Não invente profundidade que não tem.
```

### Fallback genérico

Se o orchestrator não encontrar um specialist neste catálogo para o subtópico pedido, ele gera um custom-specialist **on-the-fly** em modo genérico com o prompt:

```
Você é um specialist genérico em {domínio inferido} do Discovery Pipeline v0.5.
Não há prompt curado para este domínio neste spec-pack — você opera em modo genérico.
Priorize clareza sobre profundidade. Marque [NEEDS-HUMAN-SPECIALIST] facilmente.
```

E registra no log: `[CUSTOM-SPECIALIST-GENERIC] invocado para {domínio}`.

---

## Perfil do Delivery Report

Configurações específicas que o `consolidator` aplica ao delivery report na Fase 3 para projetos SaaS.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este perfil **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este perfil é ignorado.

### Seções extras no relatório

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Modelo Comercial e Pricing** | Entre Overview e Visão de Produto | Modelo de monetização (free trial / freemium / pago / tiered), planos e diferenciação entre tiers, estratégia de pricing, projeção de MRR/ARR por tier, break-even analysis |

### Métricas obrigatórias no relatório

| Métrica | Onde incluir | Descrição |
|---------|-------------|-----------|
| MRR / ARR | Métricas-chave + Modelo Comercial | Receita recorrente mensal/anual projetada por tier |
| Churn rate | Métricas-chave | Taxa de cancelamento aceitável |
| LTV / CAC | Métricas-chave + Análise Estratégica | Lifetime value / custo de aquisição mínimo viável |
| Time-to-value | Métricas-chave + Visão de Produto | Tempo entre signup e primeiro valor percebido |
| Disponibilidade alvo | Métricas-chave + Tech | SLA de uptime (3 9s, 4 9s, 5 9s) |
| Custo por tenant | Métricas-chave + Análise Estratégica | Custo de infra variável por tenant (compute, storage, bandwidth) |
| Ativação | Métricas-chave | % de usuários que completam onboarding com sucesso |
| Retenção | Métricas-chave | % de usuários ativos após 30/60/90 dias |

### Diagramas obrigatórios no relatório

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| Fluxo de onboarding | Opcional | Visão de Produto | Jornada do signup ao primeiro valor — útil quando onboarding é self-service |

### Ênfases por seção base

| Seção base | Ênfase SaaS |
|------------|-------------|
| **Visão de Produto** | Destacar modelo de onboarding (self-service vs assistido vs white-glove), time-to-value, diferenciação competitiva por tier |
| **Backlog Priorizado** | Priorização por tier: MVP → Growth → Enterprise. Identificar features que diferenciam planos |
| **Tecnologia e Segurança** | Destacar estratégia de tenancy (database-per-tenant vs schema vs row-level), rate limiting por tenant, SSO corporativo (SAML) para Enterprise |
| **Privacidade e Compliance** | Destacar isolamento de dados entre tenants, sub-operadores (Stripe, SendGrid) com DPA, direito ao esquecimento em banco multi-tenant |
| **Análise Estratégica** | Incluir análise Build vs Buy para billing (Stripe/Chargebee/custom), auth (Auth0/Cognito/custom), search (Algolia/Elasticsearch) |
| **Matriz de Riscos** | Incluir riscos específicos: vendor lock-in do gateway de pagamento, tenant abusando rate limit, DDoS em um tenant afetando outros |

---

## Mapeamento para os 8 Blocos do Discovery

| Componente | Bloco(s) principal(is) | Agente responsável |
|------------|----------------------|-------------------|
| **1. Produto e Modelo Comercial** | #1 (Visão), #2 (Personas), #3 (Valor), #4 (Processo e Equipe) | po |
| **2. Tenancy e Infraestrutura** | #5 (Tecnologia e Segurança), #6 (LGPD e Privacidade), #7 (Arquitetura Macro) | solution-architect, cyber-security-architect |
| **3. Billing e Monetização** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro), #8 (TCO) | solution-architect |
| **4. Operação e Crescimento** | #5 (Tecnologia e Segurança), #7 (Arquitetura Macro), #8 (TCO) | solution-architect |

> [!tip] Concerns transversais
> Alguns temas atravessam todos os componentes:
> - **Privacidade (bloco #6)** — Dados pessoais existem em todos os componentes, do signup ao billing ao logging
> - **Custo (bloco #8)** — Cada componente tem custo próprio (infra per tenant, billing platform fee, observabilidade)
> - **Governança (bloco #4)** — Processo de releases, on-call e roadmap afetam todos os componentes
