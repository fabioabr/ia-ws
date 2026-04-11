---
region-id: REG-RISK-02
title: "Technical Risks"
group: risk
description: "Technology-specific risks identified during architecture analysis"
source: "Bloco #5/#7 (arch)"
schema: "Tabela (risco, probabilidade, impacto, mitigação)"
template-visual: "Table com severity"
default: true
---

# Technical Risks

Lista os riscos especificamente tecnicos identificados durante a analise arquitetural, incluindo dependencias de terceiros, limitacoes de stack e desafios de integracao. Complementa a risk matrix geral com o foco em viabilidade tecnica.

## Schema de dados

```yaml
technical_risks:
  risks:
    - id: string                 # Identificador (ex: TRISK-01)
      description: string        # Descricao do risco tecnico
      area: string               # Area (infraestrutura, integracao, seguranca, performance, dados)
      probability: string        # Alta / Media / Baixa
      impact: string             # Critico / Alto / Medio / Baixo
      mitigation: string         # Estrategia de mitigacao
      fallback: string           # Plano B caso a mitigacao falhe
```

## Exemplo

| ID | Risco | Area | Prob | Impacto | Mitigacao | Fallback |
|----|-------|------|------|---------|-----------|----------|
| TRISK-01 | API do Open Finance com latencia >2s em horario de pico | Integracao | Alta | Critico | Cache agressivo + request coalescing | Exibir dados com delay de ate 15min |
| TRISK-02 | PostgreSQL atingir limite de conexoes com multi-tenancy | Infraestrutura | Media | Alto | PgBouncer + connection pooling por tenant | Migrar para modelo database-per-tenant |
| TRISK-03 | Auth0 free tier insuficiente antes do break-even | Licenca | Media | Medio | Monitorar MAU e migrar plano com 30 dias de antecedencia | Implementar auth proprio com Keycloak |
| TRISK-04 | Bundle size do SPA acima de 500KB | Performance | Baixa | Medio | Code splitting por rota + lazy loading | SSR com Next.js |

## Representação Visual

### Dados de amostra

| ID | Risco | Área | Probabilidade | Impacto |
|----|-------|------|--------------|---------|
| TRISK-01 | API do Open Finance com latência >2s | Integração | Alta | Crítico |
| TRISK-02 | PostgreSQL limite de conexões multi-tenancy | Infraestrutura | Média | Alto |
| TRISK-03 | Auth0 free tier insuficiente antes do break-even | Licença | Média | Médio |
| TRISK-04 | Bundle size do SPA acima de 500KB | Performance | Baixa | Médio |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descrevendo cada risco técnico, seu contexto arquitetural, mitigação e fallback | Relatórios onde o leitor precisa entender o raciocínio técnico por trás de cada risco |
| Tabela | Matriz completa com área, probabilidade, impacto, mitigação e fallback, como no exemplo acima | Quando o leitor precisa de todos os detalhes para planejamento técnico e priorização |
| Horizontal bar chart por severidade | Barras horizontais por risco técnico, comprimento proporcional à severidade (combinação de probabilidade e impacto), coloridas por área | Comparar visualmente a gravidade relativa dos riscos técnicos e identificar os que exigem ação imediata |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
