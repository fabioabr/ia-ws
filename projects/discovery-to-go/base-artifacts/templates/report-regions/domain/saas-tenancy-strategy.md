---
region-id: REG-DOM-SAAS-02
title: "SaaS Tenancy Strategy"
group: domain
description: "Multi-tenant architecture approach and isolation strategy"
source: "Bloco #5/#7 (arch)"
schema: "Multi-tenant approach + diagram"
template-visual: "Card com diagrama"
when: saas
default: false
---

# SaaS Tenancy Strategy

Define a estrategia de multi-tenancy adotada, incluindo modelo de isolamento, particionamento de dados e implicacoes de custo e seguranca. A escolha de tenancy impacta diretamente escalabilidade, custo e compliance.

## Schema de dados

```yaml
tenancy_strategy:
  model: string                  # Shared DB / Schema-per-tenant / DB-per-tenant
  isolation_level: string        # Row / Schema / Database / Infrastructure
  routing: string                # Como o sistema identifica o tenant
  data_residency: string         # Regras de residencia de dados
  scaling_strategy: string       # Como escala com novos tenants
```

## Exemplo

**Modelo:** Schema-per-tenant no PostgreSQL

- **Isolamento:** Cada tenant tem seu proprio schema; queries sempre filtradas por `tenant_id` + schema isolation
- **Roteamento:** Subdominio (empresa.fintrackpro.com.br) resolvido para tenant_id via middleware
- **Residencia de dados:** Todos os dados em regiao `sa-east-1` (Sao Paulo) para compliance LGPD
- **Escalabilidade:** Ate 500 tenants por instancia RDS; alem disso, nova instancia com roteamento automatico

## Representacao Visual

### Dados de amostra

| Modelo | Isolamento | Custo/Tenant | Seguranca | Complexidade |
|--------|-----------|-------------|-----------|-------------|
| Shared DB (row-level) | Baixo | Baixo | Media | Baixa |
| Schema-per-tenant | Medio | Medio | Alta | Media |
| DB-per-tenant | Alto | Alto | Muito Alta | Alta |

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Descricao narrativa do modelo escolhido com justificativas tecnicas e trade-offs | Documentos de decisao arquitetural (ADR) ou relatorios executivos |
| Tabela | Matriz comparativa de modelos com criterios de isolamento, custo e seguranca | Comparacao de alternativas, documentacao tecnica |
| Diagrama de arquitetura | Diagrama mostrando a estrutura de isolamento entre tenants (DB, schema, infra) | Apresentacoes tecnicas, onboarding de novos desenvolvedores |
| Matriz de comparacao | Grid com modelos vs criterios, usando indicadores visuais (cores, icones) | Decisoes de arquitetura, workshops de trade-off analysis |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
