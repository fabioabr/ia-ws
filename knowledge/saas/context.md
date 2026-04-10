---
title: Context Pack — SaaS
pack-id: saas
description: Context pack para projetos SaaS multi-tenant. Cobre concerns de tenancy, billing, rate limit, autenticação, escalabilidade, observabilidade, onboarding e SLAs.
version: 00.01.000
status: ativo
author: claude-code
category: context-pack
project-name: global
area: tecnologia
tags:
  - context-pack
  - saas
  - multi-tenant
  - billing
created: 2026-04-07 12:00
---

# Context Pack — SaaS

## Quando usar

O orchestrator deve carregar este pack quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Menção a "produto", "plataforma", "serviço" oferecido a múltiplos clientes/empresas
- Termos: tenant, multi-tenant, assinatura, mensalidade, plano, billing, faturamento recorrente
- Modelo comercial subscription-based ou pay-per-use
- Necessidade de onboarding self-service
- Escalabilidade horizontal mencionada
- Cliente não é dono da infraestrutura — é usuário do produto

## Concerns por eixo

### Product + Valor + Organização (po) — blocos 1-4

**Tópicos obrigatórios do checklist:**

- Persona primária e secundárias (quem compra × quem usa)
- Job to be done principal
- Modelo comercial (free trial / freemium / pago / tiered)
- Planos e diferenciação entre tiers
- Onboarding (self-service × assistido × white-glove)
- Time-to-value esperado
- OKRs / métricas norte: ativação, retenção, NPS, MRR, LTV, churn
- ROI esperado
- Diferenciação competitiva
- Roadmap MVP × Fase 2 × Fase 3
- Processo de deploy e releases
- Tamanho e senioridade do time
- On-call pós-MVP

**Sinais de resposta incompleta:**
- "Para empresas em geral" (sem segmentação)
- "Vamos ver o preço depois" (ausência de modelo comercial)
- "Vai funcionar pra todo mundo" (sem persona clara)
- "Queremos ter sucesso" (OKR vago)

### Técnico (solution-architect) — blocos 5, 7, 8

**Categorias aplicáveis:**

- **Tecnologia:** stack permitida, cloud provider, banco de dados (SQL × NoSQL × híbrido), cache, fila de mensagens
- **Segurança:** autenticação (OAuth2, SAML, magic link), 2FA, SSO corporativo, criptografia at-rest e in-transit, secrets management
- **Arquitetura:** monolito × microsserviços, sync × async, multi-tenant strategy (database × schema × row level), separação de planos
- **Integrações:** gateway de pagamento (Stripe, Chargebee), APIs externas, webhooks, regiões suportadas
- **Observabilidade:** métricas por tenant, tracing distribuído, SLO/SLI
- **Build vs Buy:** billing (Stripe/Chargebee/custom), auth (Auth0/Cognito/custom), search (Algolia/Elasticsearch)
- **TCO:** custo variável por tenant (compute, storage, bandwidth) + custo fixo por tier

**Perguntas recomendadas:**

- Como será o isolamento entre tenants? (database-per-tenant, schema-per-tenant, row-level)
- Algum tenant pode ter SLA diferenciado?
- Qual a estratégia de rate limit por tenant?
- Vale construir billing custom ou usar Stripe/Chargebee?
- Como escalar quando o tenant mais pesado atingir 10x o volume atual?

### Privacidade (cyber-security-architect, **obrigatório**) — bloco 6

O cyber-security-architect sempre roda este bloco, em qualquer projeto SaaS. Em SaaS o **modo profundo é quase sempre o caso** porque há dados de contato, uso e telemetria de usuários finais. O modo magro é raro mas possível em produtos B2B puramente técnicos (ex: ferramenta de build, sem dados de pessoa identificáveis).

**Concerns específicos SaaS:**

- LGPD/GDPR com múltiplas jurisdições (se SaaS global)
- Residência de dados por região (EU → na EU, BR → no BR)
- Política de retenção por tenant e por tier
- Direito ao esquecimento em banco multi-tenant
- Papel de controlador × operador (quando o cliente é outra empresa)
- Sub-operadores (Stripe, SendGrid, Datadog) — contratos DPA
- Transferência internacional de dados (SCC/cláusulas contratuais padrão)
- Isolamento de dados pessoais entre tenants

### Tópicos adicionais do solution-architect (aprofundamento nos blocos 5, 7 e 8)

**Arquitetura + Observabilidade:**

- Arquitetura macro de tenancy (database × schema × row level)
- Observabilidade (métricas, logs, traces, alertas) segmentada por tenant
- Backup e disaster recovery
- Escalabilidade (vertical × horizontal × particionamento)
- Migração de schema com zero-downtime
- Pipeline CI/CD com feature flags
- Estratégia de testes (unit, integration, e2e, smoke em prod, canary)

**TCO específico SaaS:**

- Custos variáveis por tenant (compute, storage, bandwidth)
- Custo fixo por tier de plano
- CAC vs LTV (cruzando com OKRs do po)
- Custo de billing platform (Stripe ~3%, Chargebee fee fixo + variável)
- Custo de observabilidade que escala com nº de tenants

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|---|---|
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

## Custom-specialists disponíveis

O catálogo de custom-specialists para projetos SaaS está no **spec-pack** correspondente: [[../saas/specialists|knowledge/saas/specialists.md]]. O orchestrator carrega o spec-pack junto com este context-pack durante o Setup. Quando po, solution-architect ou cyber-security-architect pedirem `help` em subtópico específico durante a reunião, o orchestrator consulta aquele catálogo.

Lembrete: LGPD/Privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect` (agente fixo, bloco 6).

## Métricas-chave para incluir no delivery

O consolidator (Round 3) deve garantir que estas métricas apareçam no `delivery-report.md` consolidado:

- MRR/ARR projetado por tier
- Churn rate aceitável
- LTV/CAC mínimo viável
- Time-to-value alvo
- Disponibilidade alvo (3 9s, 4 9s, 5 9s)
- Custo de infraestrutura por tenant
