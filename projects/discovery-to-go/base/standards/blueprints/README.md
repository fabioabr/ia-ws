# Project Blueprints

Guias de entrevista por tipo de projeto. Cada blueprint contém: variantes, stack de referência, 10 etapas com perguntas direcionadas, anti-patterns, red flags, gates, estimativa de esforço e dependências entre etapas.

## Como usar

1. Identifique o tipo de projeto do cliente a partir de um prompt simples
2. Execute o **Environment Discovery** para mapear o cenário atual do cliente
3. Use o blueprint do tipo identificado como guia de entrevista nas etapas 01-10

## Índice

### Pré-Discovery

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Environment Discovery | Levantamento do cenário atual: infra, sistemas, stack, equipe, custos, normas e boas práticas | [environment/](environment/) |

### Sites & Portais

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Site Estático / Landing Page | Site institucional, marketing, portfólio ou documentação. Sem backend. CDN. | [static-site/](static-site/) |
| Web Portal | Portal web com autenticação, múltiplos perfis, integrações com sistemas internos | [web-portal/](web-portal/) |

### Aplicações Web

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Web App — Monólito | Aplicação web full-stack em monólito. Backend e frontend acoplados. | [web-app-monolith/](web-app-monolith/) |
| Web App — Microsserviços | Aplicação web distribuída em microsserviços independentes. | [web-app-microservices/](web-app-microservices/) |

### Mobile

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Mobile App — Consumer (B2C) | Aplicativo móvel para consumidor final. App Store / Google Play. | [mobile-app-consumer/](mobile-app-consumer/) |
| Mobile App — Enterprise (B2B) | Aplicativo móvel corporativo. MDM, SSO, offline-first. | [mobile-app-enterprise/](mobile-app-enterprise/) |

### SaaS & Plataformas

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| SaaS B2B | Software como serviço para empresas. Multi-tenant, billing, onboarding. | [saas-b2b/](saas-b2b/) |
| SaaS B2C | Software como serviço para consumidor final. Freemium, growth, retenção. | [saas-b2c/](saas-b2c/) |
| Internal SaaS | Sistema interno da empresa. RBAC, SSO, integrações ERP/CRM. | [internal-saas/](internal-saas/) |
| Marketplace | Plataforma multi-sided. Compradores, vendedores, split payment, KYC. | [marketplace/](marketplace/) |
| E-commerce | Loja virtual. Catálogo, carrinho, pagamento, logística. | [e-commerce/](e-commerce/) |

### APIs & Integrações

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| API Platform | Plataforma de APIs. Developer portal, rate limiting, monetização. | [api-platform/](api-platform/) |
| Integration Middleware | Sistema de integração entre sistemas. ETL, mensageria, orquestração. | [integration-middleware/](integration-middleware/) |

### Dados & AI

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Data Pipeline | Pipeline de ingestão, transformação e carga de dados. Batch ou streaming. | [data-pipeline/](data-pipeline/) |
| Data Platform | Plataforma de dados centralizada. DW, lakehouse, data mesh, analytics. | [data-platform/](data-platform/) |
| AI/ML Application | Aplicação com inteligência artificial. Chatbot, RAG, inference API, ML pipeline. | [ai-ml-application/](ai-ml-application/) |
| Conversational Agent | Agente conversacional. FAQ bot, transacional, LLM, multicanal, voz. | [conversational-agent/](conversational-agent/) |

### Automação & Extensões

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Process Automation | Automação de processos. RPA, workflow BPMN, orquestração de APIs. | [process-automation/](process-automation/) |
| Platform Extension | Extensão de plataforma existente. Plugin, connector, módulo ERP/CRM. | [platform-extension/](platform-extension/) |

### Especializado

| Tipo | Descrição | Pasta |
|------|-----------|-------|
| Embedded / IoT | Sistema embarcado ou IoT. Firmware, edge, sensores, OTA, telemetria. | [embedded-iot/](embedded-iot/) |
