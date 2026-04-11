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

## Representacao Visual

### Dados de amostra

```
                    +------------------+
                    |   FinTrack Pro   |
                    +--------+---------+
                             |
         +----------+--------+--------+----------+
         |          |        |        |          |
         v          v        v        v          v
   Open Finance  Stripe    Auth0  SendGrid  Google
   (BACEN)                                 Analytics
   REST+OAuth   REST+WH   OIDC    REST     SDK
   10k req/d    500 ev/d  2k/d    200/d    Continuo
   ALTA         ALTA      ALTA    MEDIA    BAIXA
```

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela de fluxos
**Tecnologia:** HTML/CSS
**Justificativa:** Os dados de integracao sao multidimensionais (sistema, tipo, protocolo, direcao, volume, criticidade) e cada linha e independente. Uma tabela estilizada com badges de criticidade (cores), icones de direcao e agrupamento por tipo permite escaneamento rapido e funciona melhor que diagramas de rede em HTML estatico.
**Alternativa:** Card grid por sistema (HTML/CSS) — quando houver poucos sistemas (3-4) e o foco for detalhar cada integracao individualmente.
