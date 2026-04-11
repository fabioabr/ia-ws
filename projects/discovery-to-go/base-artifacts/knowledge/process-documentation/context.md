---
title: Context Pack — Process Documentation
pack-id: process-documentation
description: Context pack para projetos de documentação de processos. Cobre público-alvo, granularidade, versionamento, fluxos, papéis, auditoria e aprovação de documentação operacional.
version: 00.01.000
status: ativo
author: claude-code
category: context-pack
project-name: global
area: tecnologia
tags:
  - context-pack
  - documentation
  - processes
  - knowledge-management
created: 2026-04-07 12:00
---

# Context Pack — Process Documentation

## Quando usar

O orchestrator deve carregar este pack quando o briefing apresentar **dois ou mais** dos seguintes sinais:

- Objetivo é "documentar processos", "criar manual", "padronizar operação"
- Termos: SOP, runbook, playbook, manual operacional, knowledge base, wiki, processo
- Foco em **conhecimento** mais do que em código/sistema
- Stakeholders são pessoas operacionais (analistas, técnicos, ops, suporte)
- Demanda de auditoria, compliance, certificação (ISO, SOC, etc.)
- Necessidade de onboarding de novos times via documentação

## Concerns por eixo

### Product + Valor + Organização (po) — blocos 1-4

**Tópicos obrigatórios do checklist:**

- Público-alvo primário (quem vai ler / executar)
- Nível técnico do leitor (júnior, sênior, leigo, expert)
- Idioma e tom esperado
- Granularidade (nível alto / passo-a-passo / código + comandos)
- Frequência de uso (consulta diária, eventual, emergencial)
- Modo de consumo (web, PDF, impresso, mobile, busca interna)
- OKRs: tempo de onboarding reduzido, tickets reduzidos, NPS interno, cobertura de processos
- ROI esperado
- Regulação aplicável (ISO 9001, ISO 27001, SOC 2, regulação setorial) — como contexto
- Ownership por documento (quem é o dono de cada SOP/runbook)
- Fluxo editorial (criação → revisão → aprovação → publicação)
- Ciclo de revisão obrigatório (anual, semestral, ad hoc)
- Time de redatores, revisores, aprovadores

**Sinais de resposta incompleta:**
- "Pra geral" (sem público-alvo)
- "Vamos escrever do jeito que sai" (sem padrão de tom/granularidade)
- Sem critério de "documento aprovado vs draft"

### Técnico (solution-architect) — blocos 5, 7, 8

**Categorias aplicáveis:**

- **Tecnologia:** plataforma de docs (Confluence, Notion, Obsidian, GitBook, MkDocs, Docusaurus, SharePoint, Wiki interna)
- **Segurança:** controle de acesso por documento, classificação (público / interno / confidencial / restrito), audit trail de quem aprovou/editou
- **Arquitetura:** taxonomia, hierarquia, navegação, busca, cross-references, versionamento
- **Integrações:** ticketing (Jira), monitoring (Grafana), RH, SSO corporativo
- **Build vs Buy:** plataforma SaaS (Confluence, Notion) vs self-hosted (MediaWiki, Docusaurus) vs híbrido
- **TCO:** licenças por usuário + horas de redação + horas de revisão + manutenção contínua + migração

**Perguntas recomendadas:**

- Vale pagar Confluence por usuário ou manter MkDocs self-hosted?
- Como rastrear audit trail completo de aprovações para compliance?
- Há requisito de assinatura digital?
- Idioma único ou multilíngue?
- Migração de docs legados: big bang ou strangler fig?
- Como integrar busca com outros sistemas corporativos?

### Privacidade (cyber-security-architect, **obrigatório**) — bloco 6

O cyber-security-architect sempre roda este bloco. Em projetos de documentação de processos, o **modo magro é o caso comum** — documentação interna costuma ter baixa sensibilidade de privacidade. Modo profundo se aplica quando os docs contêm dados pessoais (contratos, salários, identificação de clientes/colaboradores), quando são expostos externamente, ou quando há compliance regulatório específico.

**Concerns específicos de documentação:**

- Classificação de sensibilidade por doc (público / interno / confidencial / restrito)
- Dados pessoais em docs (masking automático? revisão manual?)
- Retenção de versões antigas com dados pessoais
- Audit trail de quem leu/exportou docs sensíveis
- Política de remoção de docs vazados

## Antipatterns conhecidos

| # | Antipattern | Por quê é ruim |
|---|---|---|
| 1 | **Documentação sem dono** | Em 6 meses está desatualizada e ninguém sabe quem mexe |
| 2 | **Tudo no mesmo template** | Runbook técnico com tom de guideline executivo confunde leitor |
| 3 | **Sem ciclo de revisão obrigatório** | Documentação envelhece silenciosamente |
| 4 | **"Vamos documentar tudo"** | Escopo infinito, nada pronto, frustração |
| 5 | **Sem busca eficiente** | Usuário desiste de procurar e cria caminho próprio |
| 6 | **Aprovação por uma pessoa só** | Bottleneck e SPOF; documentação fica em backlog do gerente |
| 7 | **Sem versionamento** | "Qual é a versão correta?" vira pergunta diária |
| 8 | **Migração big-bang de docs legados** | Projeto morre antes de migrar tudo |
| 9 | **Documentação separada do código/produto** | Drift entre o que está documentado e o que existe |
| 10 | **Sem métricas de uso** | Impossível saber o que está funcionando ou não |

## Edge cases para o 10th-man verificar

- O que acontece com docs cujo dono saiu da empresa?
- Como auditar quem aprovou determinada versão de uma SOP crítica?
- Doc com erro grave em produção — como reverter rapidamente?
- Conflito entre dois docs que descrevem o mesmo processo de formas diferentes?
- Doc traduzido fica desatualizado em relação ao original — qual é a fonte da verdade?
- Como lidar com docs internos vazados publicamente?
- Plataforma de docs cai — qual é o fallback?
- Mudança regulatória obriga revisão de 200 docs em 30 dias — como executar?
- Doc descreve processo que mudou ontem — quem é responsável por atualizar?
- Migração de plataforma — como preservar histórico de versões e aprovações?
- Auditor externo pede log de aprovações de 2 anos — como gerar?
- Doc com PII vazada por descuido — política de remoção?

## Custom-specialists disponíveis

O catálogo de custom-specialists para projetos de documentação de processos está no **spec-pack** correspondente: [[../process-documentation/specialists|knowledge/process-documentation/specialists.md]]. O orchestrator carrega o spec-pack junto com este context-pack durante o Setup.

Lembrete: LGPD/Privacidade NÃO é custom-specialist — é coberta obrigatoriamente pelo `cyber-security-architect`.

## Report Profile

Seções extras, métricas obrigatórias e diagramas específicos para o delivery report estão definidos em [[report-profile]].
