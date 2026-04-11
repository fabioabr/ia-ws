---
title: "HR Loop Template"
description: Template para o ponto de revisão humana entre fases
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: customization
area: tecnologia
tags:
  - customization
  - hr-loop
  - template
created: 2026-04-11 09:00
---

# HR Loop Template

> Usando template padrão. Nenhum override aplicado para este run.

## Estrutura do HR Review

Ao final de cada fase, o orchestrator apresenta ao humano:

1. **Resumo da fase** — o que foi produzido
2. **Score de completude** — por dimensão e global
3. **Riscos identificados** — com severidade
4. **Dados inferidos** — que precisam de confirmação
5. **Pendências** — itens não respondidos

## Opções de Decisão

| Opção | Efeito |
|-------|--------|
| Avançar | Próxima fase inicia |
| Refazer | Nova iteração da fase atual |
| Abortar | Run encerrado |

## Formato de Resposta

O humano responde com a opção escolhida e comentários opcionais.
