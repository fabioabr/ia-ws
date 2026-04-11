---
region-id: REG-DOM-INTEG-01
title: "Integration Map"
group: domain
description: "System integration diagram showing all external systems and data flows"
source: "Bloco #5/#7 (arch)"
schema: "Diagram de sistemas e fluxos"
template-visual: "Diagram full-width"
when: system-integration
default: false
---

# Integration Map

Diagrama de integracao mostrando todos os sistemas externos, protocolos, direcao dos fluxos e volumes estimados. Permite visualizar a complexidade de integracao e identificar pontos unicos de falha.

## Schema de dados

```yaml
integration_map:
  systems:
    - name: string
      type: string               # internal / external / saas
      protocol: string           # REST, gRPC, SOAP, webhook, file, message
      direction: string          # inbound / outbound / bidirectional
      volume: string             # Estimativa de volume
      criticality: string        # Alta / Media / Baixa
```

## Exemplo

| Sistema | Tipo | Protocolo | Direcao | Volume | Criticidade |
|---------|------|-----------|---------|--------|-------------|
| Open Finance (BACEN) | External | REST + OAuth 2.0 | Inbound | ~10k req/dia | Alta |
| Stripe | SaaS | REST + Webhooks | Bidirectional | ~500 eventos/dia | Alta |
| Auth0 | SaaS | OIDC/OAuth 2.0 | Bidirectional | ~2k auth/dia | Alta |
| SendGrid | SaaS | REST | Outbound | ~200 emails/dia | Media |
| Google Analytics | SaaS | SDK client-side | Outbound | Continuous | Baixa |
