---
region-id: REG-DOM-MIGR-01
title: "Migration Roadmap"
group: domain
description: "Phased migration plan with go/no-go checkpoints"
source: "Bloco #5/#7 (arch)"
schema: "Faseamento visual + go/no-go"
template-visual: "Timeline horizontal"
when: migration-modernization
default: false
---

# Migration Roadmap

Apresenta o plano de migracao faseado com checkpoints de go/no-go entre cada fase. Cada fase tem escopo claro, criterios de sucesso e plano de rollback. Migracoes sao projetos de alto risco e exigem planejamento granular.

## Schema de dados

```yaml
migration_roadmap:
  phases:
    - phase: number
      name: string
      duration: string
      scope: string[]
      success_criteria: string[]
      rollback_plan: string
      go_no_go: string[]         # Criterios para avancar
```

## Exemplo

| Fase | Nome | Duracao | Escopo | Criterio Go/No-Go |
|------|------|---------|--------|--------------------|
| 1 | Pilot | 4 semanas | 1 modulo nao-critico migrado | Zero perda de dados; performance equivalente |
| 2 | Core Migration | 8 semanas | Modulos core + banco de dados | Todos os testes E2E passando; latencia < 200ms |
| 3 | Full Cutover | 2 semanas | Desligar sistema legado | 2 semanas de operacao paralela sem incidentes |
| 4 | Decommission | 4 semanas | Remover infraestrutura antiga | Backup final arquivado; custos legado zerados |

## Representacao Visual

### Dados de amostra

```
Semana:  1---4   5---------12   13--14   15-------18
         |       |              |         |
Phase 1: Pilot   |              |         |
         [====]  |              |         |
                 Phase 2: Core  |         |
                 [==============]         |
                 Go/No-Go ----> *         |
                                Phase 3:  |
                                [====]    |
                                Go/No-Go -> *
                                          Phase 4: Decommission
                                          [========]
```

### Recomendacao do Chart Specialist

**Veredicto:** GRAFICO
**Tipo:** Timeline horizontal com barras
**Tecnologia:** HTML/CSS
**Justificativa:** Fases de migracao sao sequenciais com duracao variavel e checkpoints de go/no-go entre elas. Uma timeline horizontal com barras proporcionais a duracao e marcadores de checkpoint comunica a progressao temporal e dependencias entre fases de forma intuitiva, sem necessidade de bibliotecas de charting.
**Alternativa:** Tabela com fases e duracao (HTML/CSS) — quando o documento for referencia textual e nao necessitar da dimensao temporal visual.
