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

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada integracao com protocolo, volume e criticidade | Documentos de escopo, relatorios executivos |
| Tabela | Tabela com sistemas, protocolos, direcao, volume e criticidade | Inventario de integracoes, documentacao tecnica |
| Diagrama de rede/fluxo | Diagrama mostrando o sistema central conectado a sistemas externos com setas indicando direcao, protocolo e volume | Apresentacoes de arquitetura, analise de dependencias, identificacao de pontos de falha |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
