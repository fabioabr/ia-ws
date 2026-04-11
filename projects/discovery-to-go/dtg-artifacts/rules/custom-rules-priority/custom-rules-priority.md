---
title: Custom Rules Priority
description: Regra de prioridade de carregamento — custom-rules do cliente sempre sobrescreve defaults do pipeline e do workspace global
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - regra
  - prioridade
  - customizacao
  - cliente
created: 2026-04-11 12:00
---

# Custom Rules Priority

Regra que define a **cadeia de prioridade** para carregamento de configurações, knowledge base, assets e regras. Custom-rules do cliente **sempre** têm prioridade sobre os defaults do pipeline e do workspace global.

> [!danger] Regra fundamental
> Quando existir um recurso tanto em `custom-rules/{client}/` quanto nos defaults, o orchestrator **DEVE** usar o do cliente. Os defaults são **fallback**, nunca override.

---

## 📏 Cadeia de Prioridade

A prioridade segue a ordem: **cliente > projeto > workspace global**. O recurso mais específico sempre vence.

```
1. custom-rules/{client}/    ← MAIOR prioridade (cliente)
2. templates/                ← fallback do pipeline (projeto)
3. E:\Workspace/             ← fallback global (workspace)
```

### Por tipo de recurso

#### Configurações

| Prioridade | Local | Exemplo |
|------------|-------|---------|
| 1 (maior) | `custom-rules/{client}/config/` | `scoring-thresholds.md` do cliente |
| 2 | `templates/customization/` | `scoring-thresholds.md` default do pipeline |

Arquivos afetados:
- `scoring-thresholds.md` — pisos de nota
- `iteration-policy.md` — política de iteração
- `final-report-template.md` — estrutura do relatório
- `human-review-template.md` — formato do Human Review

#### Knowledge Base

| Prioridade | Local | Conteúdo |
|------------|-------|----------|
| 1 (maior) | `custom-rules/{client}/kb/` | Contexto específico do cliente (ecossistema, integrações, regras de negócio) |
| 2 | `knowledge/{domain}/` (workspace global) | Contexto do domínio tecnológico (SaaS, datalake, etc.) |

> [!info] KB do cliente complementa, não substitui
> O KB do cliente e o knowledge pack global são **complementares**. Ambos são carregados. Se houver conflito entre uma informação do KB do cliente e do knowledge pack, prevalece o do cliente.

#### Assets

| Prioridade | Local | Conteúdo |
|------------|-------|----------|
| 1 (maior) | `custom-rules/{client}/assets/` | Logo, templates visuais do cliente |
| 2 | `assets/` (projeto) | Assets do pipeline |
| 3 | `E:\Workspace\assets/` (workspace global) | Assets globais (design system, logos default) |

#### Regras

| Prioridade | Local | Conteúdo |
|------------|-------|----------|
| 1 (maior) | `custom-rules/{client}/rules/` | Regras adicionais do cliente (compliance, formato, restrições) |
| 2 | `rules/` (projeto) | Regras do pipeline |
| 3 | `E:\Workspace\behavior\rules/` (workspace global) | Regras globais do workspace |

> [!warning] Regras do cliente são aditivas
> Regras em `custom-rules/{client}/rules/` **não substituem** as regras do pipeline ou do workspace — elas **adicionam** restrições. Se o pipeline exige X e o cliente exige X + Y, ambos se aplicam.
>
> A única exceção é quando uma regra do cliente **explicitamente** declara que sobrescreve uma regra específica, usando:
> ```yaml
> overrides: rules/{rule-name}/{rule-name}.md
> ```

---

## 🔧 Como o orchestrator aplica

### Durante o Setup

1. Lê o campo `client` no frontmatter do `briefing.md`
2. Se `client` está definido:
   - Verifica se `custom-rules/{client}/` existe
   - Se existe, carrega recursos na ordem de prioridade
   - Copia configs de `custom-rules/{client}/config/` para `setup/customization/` (sobrescrevendo defaults)
   - Registra no `pipeline-state.md`: `client: {client-name}, custom-rules: loaded`
3. Se `client` não está definido ou pasta não existe:
   - Usa defaults de `templates/customization/`
   - Registra no `pipeline-state.md`: `client: none, custom-rules: not loaded`

### Durante a Fase 1 (Discovery)

- Agentes recebem o KB do cliente como contexto adicional
- O customer usa o KB do cliente para enriquecer respostas
- Dados do KB são marcados como `[KB-CLIENT]` no interview log

### Durante a Fase 3 (Delivery)

- O html-writer usa os assets do cliente (logo) se disponíveis
- O consolidator usa o `final-report-template.md` do cliente se disponível
- O pipeline-md-writer aplica regras adicionais do cliente

---

## 📋 Checklist para o orchestrator

Antes de iniciar qualquer fase, verificar:

- [ ] Campo `client` lido do briefing
- [ ] Pasta `custom-rules/{client}/` verificada
- [ ] Se existir `config/`: copiado para `setup/customization/` (sobrescrevendo defaults)
- [ ] Se existir `kb/`: carregado como contexto adicional para os agentes
- [ ] Se existir `assets/`: registrado para uso no delivery
- [ ] Se existir `rules/`: carregado como regras adicionais
- [ ] Registrado no `pipeline-state.md` o que foi carregado

---

## 🔗 Documentos Relacionados

- `custom-rules/README.md` — Guia de como estruturar custom-rules por cliente
- `skills/orchestrator/SKILL.md` — Como o orchestrator carrega e aplica custom-rules
- `templates/customization/` — Defaults de configuração (fallback)
- `knowledge/` — Knowledge packs globais por domínio

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 01.00.000 | 2026-04-11 | Criação — cadeia de prioridade cliente > projeto > workspace para configs, KB, assets e regras |
