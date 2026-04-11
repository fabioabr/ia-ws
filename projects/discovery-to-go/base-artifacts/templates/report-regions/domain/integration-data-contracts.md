---
region-id: REG-DOM-INTEG-02
title: "Integration Data Contracts"
group: domain
description: "Schema contracts and versioning strategy for system integrations"
source: "Bloco #5/#7 (arch)"
schema: "Contratos schema/versioning"
template-visual: "Table"
when: system-integration
default: false
---

# Integration Data Contracts

Define os contratos de dados para cada integracao, incluindo formato do schema, estrategia de versionamento e responsabilidades. Contratos claros reduzem falhas de integracao e facilitam evolucao independente dos sistemas.

## Schema de dados

```yaml
data_contracts:
  contracts:
    - integration: string        # Nome da integracao
      schema_format: string      # JSON Schema, Protobuf, Avro, OpenAPI
      versioning: string         # Semantic / URL path / Header
      owner: string              # Time responsavel pelo contrato
      breaking_change_policy: string
```

## Exemplo

| Integracao | Formato | Versionamento | Owner | Politica de Breaking Change |
|-----------|---------|---------------|-------|---------------------------|
| API Publica FinTrack | OpenAPI 3.1 | URL path (/v1/, /v2/) | Time Backend | Deprecacao com 90 dias de aviso; 2 versoes simultaneas |
| Webhooks Stripe | JSON Schema | Header (Stripe-Version) | Stripe (externo) | Stripe mantem backward compatibility |
| Eventos internos (Kafka) | Avro + Schema Registry | Schema evolution (backward) | Time que publica | Apenas adicao de campos opcionais |
| Open Finance | OpenAPI (BACEN) | URL path | BACEN (externo) | Seguir calendario do BACEN |

## Representacao Visual

### Dados de amostra

| Integracao | Formato | Versao Atual | Status | Owner |
|-----------|---------|-------------|--------|-------|
| API Publica FinTrack | OpenAPI 3.1 | v2 | `Ativa` | Backend |
| Webhooks Stripe | JSON Schema | 2024-01-01 | `Ativa` | Stripe |
| Eventos Kafka | Avro | 3.2.0 | `Ativa` | Publisher |
| Open Finance | OpenAPI | v1 | `Em migracao` | BACEN |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa de cada contrato com formato, versionamento e politicas | ADRs, documentacao de governanca de APIs |
| Tabela com badges de versao | Tabela com integracoes, formato, versao atual (badge), status e owner | Catalogo de contratos, dashboards de integracao, portais de API |
| Matriz de compatibilidade | Grid mostrando compatibilidade entre versoes de contratos e sistemas consumidores | Planejamento de deprecacao, analise de impacto de breaking changes |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
