---
region-id: REG-TECH-07
title: "Requisitos Não Funcionais"
group: technical
description: "Requisitos de performance, disponibilidade, segurança e escalabilidade"
source: "Bloco #5 (arch) → 1.5"
schema: "Tabela (categoria, requisito, valor, SLA)"
template-visual: "Table com severity badges"
default: false
---

# Requisitos Não Funcionais

Consolida os requisitos não funcionais que direcionam decisões de arquitetura e infraestrutura. Cada requisito possui um valor-alvo mensurável e um SLA acordado, servindo como critério objetivo de aceite para a solução.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| categoria | enum | Performance, Disponibilidade, Segurança, Escalabilidade, etc. |
| requisito | string | Descrição do requisito |
| valor | string | Meta quantitativa |
| SLA | string | Nível de serviço acordado |

## Exemplo

| Categoria | Requisito | Valor | SLA |
|-----------|-----------|-------|-----|
| Performance | Tempo de resposta de APIs críticas | p95 < 200ms | 99% das requisições |
| Performance | Tempo de carregamento do dashboard | < 2s (First Contentful Paint) | — |
| Disponibilidade | Uptime da plataforma | 99.9% | Mensal, excluindo janelas de manutenção |
| Escalabilidade | Usuários simultâneos | Até 5.000 | Sem degradação perceptível |
| Escalabilidade | Crescimento de dados | Suportar 10x o volume atual em 2 anos | — |
| Segurança | Tempo máximo de sessão ociosa | 15 minutos | Logout automático |
| Segurança | Cobertura de vulnerabilidades críticas | Patch em até 48h | SLA de segurança |
| Recuperação | RPO (Recovery Point Objective) | < 1 hora | — |
| Recuperação | RTO (Recovery Time Objective) | < 4 horas | — |

## Representação Visual

### Dados de amostra

| Categoria | Requisito | Valor | SLA |
|-----------|-----------|-------|-----|
| Performance | Tempo de resposta de APIs críticas | p95 < 200ms | 99% das requisições |
| Performance | Tempo de carregamento do dashboard | < 2s (FCP) | — |
| Disponibilidade | Uptime da plataforma | 99.9% | Mensal |
| Escalabilidade | Usuários simultâneos | Até 5.000 | Sem degradação |
| Escalabilidade | Crescimento de dados | 10x em 2 anos | — |
| Segurança | Sessão ociosa máxima | 15 minutos | Logout automático |
| Segurança | Vulnerabilidades críticas | Patch em 48h | SLA de segurança |
| Recuperação | RPO | < 1 hora | — |
| Recuperação | RTO | < 4 horas | — |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva organizando os requisitos por categoria, explicando metas, SLAs e impacto nas decisões de arquitetura | Sempre — serve como base textual acessível para qualquer público |
| Tabela | Tabela estruturada com colunas Categoria, Requisito, Valor e SLA, com badges de severidade | Sempre — permite consulta rápida e comparação objetiva entre requisitos |
| Gauge charts por categoria | Gráficos do tipo gauge (velocímetro) agrupados por categoria (Performance, Disponibilidade, Escalabilidade, Segurança, Recuperação), mostrando o valor-alvo em relação a faixas de referência (crítico, aceitável, ideal) | Quando é necessário comunicar visualmente o nível de exigência de cada categoria para stakeholders técnicos e executivos, facilitando a identificação de áreas mais restritivas |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
