---
title: "Scoring Thresholds"
description: Thresholds de scoring para validação de completude
project-name: fintrack-pro
version: 01.00.000
status: ativo
author: orchestrator
category: customization
area: tecnologia
tags:
  - customization
  - scoring
  - thresholds
created: 2026-04-11 09:00
---

# Scoring Thresholds

> Usando thresholds padrão. Nenhum override aplicado para este run.

## Critérios de Completude

| Dimensão | Threshold Mínimo | Peso |
|----------|-----------------|------|
| Visão e propósito | 80% | 20% |
| Personas | 70% | 15% |
| Requisitos funcionais | 75% | 20% |
| Arquitetura | 70% | 15% |
| Segurança e compliance | 80% | 15% |
| TCO e viabilidade | 70% | 15% |

## Regras

- Score global minimo para avançar: **70%**
- Dados marcados como `[INFERENCE]` reduzem o score da dimensão em 10%
- Dimensões abaixo do threshold geram alerta no HR Review
