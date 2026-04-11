---
title: "Briefing — FinTrack Pro"
description: Briefing inicial do projeto FinTrack Pro, plataforma SaaS de consolidação financeira para PMEs
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: humano
category: briefing
area: tecnologia
tags:
  - briefing
  - fintrack-pro
  - saas
  - fintech
created: 2026-04-11 08:30
---

# Briefing — FinTrack Pro

## Contexto

Gestores financeiros de PMEs gastam em média 12 horas por semana consolidando dados de diferentes bancos, planilhas e ERPs em relatórios manuais. A nova regulamentação do Open Finance no Brasil abre uma janela de oportunidade para automatizar esse processo via APIs bancárias abertas.

## Problema

Consolidação financeira manual é lenta, propensa a erros e não escala. As ferramentas existentes (Conta Azul, Nibo) são limitadas para consolidação multi-banco e não oferecem projeções inteligentes.

## Produto

**FinTrack Pro** — plataforma SaaS que automatiza a consolidação financeira multi-banco e gera projeções de fluxo de caixa com IA.

## Público-alvo

- **CFOs e controllers** de empresas com 50 a 500 funcionários
- **Analistas financeiros** que fazem conciliação diária
- **CEOs** que consomem resumos executivos mensais

## Funcionalidades Esperadas

1. Consolidação automática de extratos bancários (OFX/CSV) via Open Finance
2. Categorização inteligente de lançamentos
3. Projeções de fluxo de caixa com IA (LLM via API)
4. Alertas de anomalias em gastos
5. Dashboard executivo e relatórios prontos
6. MFA obrigatório; SSO (SAML) no plano Enterprise

## Modelo de Negócio

SaaS com 3 planos:
- **Starter:** R$199/mês (até 2 bancos)
- **Pro:** R$499/mês (até 5 bancos + projeções)
- **Enterprise:** R$999/mês (ilimitado + API + SSO)

## Restrições Conhecidas

| Dimensão | Detalhe |
|----------|---------|
| Equipe | 5 pessoas (CTO + 2 back + 1 front + 1 UX) |
| Stack | Node.js (TypeScript), React, PostgreSQL |
| Cloud | AWS (créditos de startup) |
| Metodologia | Scrum, sprints de 2 semanas |
| Open Finance | Provider pendente (Belvo ou Pluggy) |
| IA | API externa (OpenAI/Claude), sem modelo próprio no MVP |
| Segurança | AES-256 repouso, TLS 1.3 trânsito |

## OKRs do MVP

1. Reduzir tempo de consolidação de 12h/semana para 2h/semana
2. 100 empresas pagantes nos primeiros 6 meses
3. NPS acima de 50

## Perguntas em Aberto

- Quantos bancos simultâneos são requisito mínimo vs. meta?
- Belvo ou Pluggy como provider de Open Finance?
- DPO ainda não nomeado — necessário antes do lançamento (LGPD)
- Frequência de atualização dos dados no MVP (tempo real vs. batch)?
