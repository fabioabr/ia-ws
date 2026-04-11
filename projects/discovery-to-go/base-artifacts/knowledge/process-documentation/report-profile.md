---
title: Report Profile — Process Documentation
pack-id: process-documentation
description: Perfil de relatório para projetos de documentação de processos — define seções extras, métricas obrigatórias, diagramas e ênfases que o consolidator aplica ao delivery report
version: 01.00.000
status: ativo
author: claude-code
category: report-profile
area: tecnologia
tags:
  - report-profile
  - process-documentation
  - delivery
  - consolidator
created: 2026-04-11
---

# Report Profile — Process Documentation

Perfil de relatório específico para projetos de documentação de processos. O `consolidator` lê este arquivo durante a Fase 3 (Delivery) e faz merge com o template base (`final-report-template.md`) para montar a estrutura final do `delivery-report.md`.

> [!info] Como funciona o merge
> O template base define 11 seções obrigatórias. Este report-profile **adiciona** seções extras, **define** métricas obrigatórias do domínio e **ajusta** ênfases nas seções base. Se o cliente tiver um override total em `custom-artifacts/{client}/config/final-report-template.md`, este profile é ignorado.

---

## Seções extras

| Seção | Posição | Conteúdo esperado |
|-------|---------|-------------------|
| **Taxonomia e Governança de Docs** | Entre Organização e Tecnologia e Segurança | Taxonomia de tipos de documento (SOP, runbook, playbook, knowledge base), ciclo de revisão obrigatório, RACI de manutenção, políticas de aprovação, audit trail |

---

## Métricas obrigatórias

| Métrica | Onde incluir | Descrição |
|---------|-------------|-----------|
| Tempo médio de publicação | Métricas-chave | Tempo entre criação e publicação de um documento novo |
| % docs com revisão em dia | Métricas-chave | Percentual de documentos dentro do ciclo de revisão obrigatório |
| % docs com dono claro | Métricas-chave | Percentual de documentos com owner designado e ativo |
| Taxa de busca sem resultado | Métricas-chave | % de buscas que não retornam documentos relevantes |
| NPS de documentação | Métricas-chave | Satisfação dos usuários com a base de conhecimento |
| Custo total mensal | Métricas-chave + Análise Estratégica | Plataforma + horas dedicadas à manutenção de docs |

---

## Diagramas

| Diagrama | Obrigatório? | Seção destino | Descrição |
|----------|-------------|---------------|-----------|
| Arquitetura macro | Sim (base) | Tecnologia e Segurança | Já obrigatório no template base |
| RACI simplificado | Opcional | Taxonomia e Governança | Matriz RACI de quem cria, revisa, aprova e consome cada tipo de documento |

---

## Ênfases por seção base

| Seção base | Ênfase Process-Docs |
|------------|---------------------|
| **Organização** | Destacar RACI de manutenção de documentação, ciclo de revisão obrigatório, papéis de governance (doc owner, reviewer, approver) |
| **Visão de Produto** | Focar em taxonomia de documentos (SOP, runbook, playbook, FAQ, knowledge base), categorização, e descoberta (search/browse) |
| **Tecnologia e Segurança** | Destacar plataforma de docs (Confluence, Notion, GitBook, custom), versionamento, controle de acesso por tipo de doc, integração com ferramentas de workflow |
| **Backlog Priorizado** | Priorizar por criticidade do processo documentado: compliance/regulatório primeiro, operacional segundo, conhecimento tácito terceiro |
| **Matriz de Riscos** | Incluir riscos específicos: docs desatualizados sendo seguidos como verdade, knowledge silos, perda de conhecimento tácito por turnover |

---

## Documentos Relacionados

- [[context|knowledge/process-documentation/context.md]] — Concerns e perguntas recomendadas para a Fase 1
- [[specialists|knowledge/process-documentation/specialists.md]] — Catálogo de custom-specialists para documentação de processos
- `dtg-artifacts/templates/customization/final-report-template.md` — Template base (11 seções obrigatórias)
