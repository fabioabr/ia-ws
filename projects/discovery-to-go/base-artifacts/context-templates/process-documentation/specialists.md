---
title: Spec Pack — Process Documentation
pack-id: process-documentation
description: Catálogo de custom-specialists disponíveis para projetos de documentação de processos operacionais (SOPs, runbooks, knowledge base). Define quando o orchestrator deve invocar cada specialist.
version: 01.00.000
status: ativo
author: claude-code
category: spec-pack
project-name: global
area: tecnologia
tags:
  - spec-pack
  - process-documentation
  - custom-specialists
created: 2026-04-08 12:00
---

# Spec Pack — Process Documentation

> [!info] Relação com o context-pack
> Este spec-pack é carregado em conjunto com o `context-templates/process-documentation/context.md` durante o **Setup** do pipeline.

## Catálogo

| Specialist | Domínio | Quando invocar |
|---|---|---|
| `compliance-iso` | ISO 9001 / ISO 27001 / SOC 2 | Briefing menciona certificação ISO ou SOC 2 como requisito |
| `regulated-documentation-health` | Documentação regulada em saúde | SOPs em hospitais, clínicas, laboratórios; compliance ANS, ANVISA |
| `regulated-documentation-finance` | Documentação regulada financeira | Políticas Bacen, CVM, SUSEP; auditoria financeira |
| `regulated-documentation-government` | Documentação em setor público | LAI, transparência, compliance TCU |
| `docs-migration-strategy` | Migração de plataforma legada | Movendo de SharePoint/Confluence antigo para plataforma nova; preservação de histórico |
| `localization-strategy` | Tradução e i18n de documentação | Docs em múltiplos idiomas, sincronização entre versões, RTL |
| `developer-documentation` | Documentação técnica de API/SDK | Docs de API pública, referências SDK, tutoriais de integração |
| `legal-documentation` | Documentação para auditoria fiscal/legal | Evidências para auditoria, preservação legal, discovery |
| `knowledge-management-strategy` | Taxonomia, busca, findability | Catálogo grande, usuários não encontram conteúdo, necessidade de ontologia |
| `change-management-strategy` | Gestão de mudança de processos | Processo que afeta >50 pessoas, resistência esperada, treinamento |

## Prompt base por specialist

```
Você é o specialist `{specialist-id}` do context-pack process-documentation no Discovery Pipeline v0.5.

Domínio: {domínio da tabela}

Contexto da reunião até aqui:
{log dos blocos já cobertos}

Subtópico que pediram sua ajuda:
{descrição do ponto}

Sua missão:
1. Aprofunda o subtópico com vocabulário real do domínio (SOP, runbook, audit trail, review cycle, taxonomy, etc.)
2. Sinaliza antipatterns conhecidos (doc sem dono, escopo infinito, sem ciclo de revisão, etc.)
3. Se o customer marcar [INFERENCE] em ponto crítico (compliance, quem aprova, quem mantém), force aprofundamento
4. Se o domínio exige especialista humano de verdade (ex: compliance regulatório profundo), marque [NEEDS-HUMAN-SPECIALIST]
5. Devolve controle ao especialista fixo que te invocou
```

## Fallback genérico

Mesma regra dos outros specialists packs.
