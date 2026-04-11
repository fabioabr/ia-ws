---
title: Custom Rules
description: Guia de como estruturar regras e artefatos customizados por cliente dentro do Discovery Pipeline
project-name: discovery-to-go
version: 01.00.000
status: ativo
author: claude-code
category: guia
area: tecnologia
tags:
  - customizacao
  - cliente
  - estrutura
  - guia
created: 2026-04-11 12:00
---

# Custom Rules

Guia para estruturar regras, knowledge base e assets customizados por cliente no Discovery Pipeline.

## 📋 Quando usar

Use esta pasta quando um cliente precisa de:

- Knowledge base próprio (fluxos, integrações, ecossistema)
- Assets visuais (logos, templates de report)
- Regras adicionais que só se aplicam a ele
- Configurações de scoring ou iteração específicas

## 📂 Estrutura por cliente

Cada cliente tem uma pasta própria com nome em kebab-case:

```
custom-rules/
├── README.md                          ← este arquivo
├── {client-name}/
│   ├── kb/                            ← knowledge base do cliente
│   │   ├── integration-flow.md        ← fluxo de integração / ecossistema
│   │   ├── tech-stack.md              ← stack e ferramentas do cliente
│   │   └── business-context.md        ← contexto de negócio específico
│   ├── assets/                        ← assets visuais
│   │   └── logo.png                   ← logo do cliente (para reports)
│   ├── rules/                         ← regras adicionais
│   │   └── {rule-name}.md             ← regra específica do cliente
│   └── config/                        ← overrides de configuração
│       ├── scoring-thresholds.md       ← pisos de nota customizados
│       ├── iteration-policy.md         ← política de iteração
│       └── final-report-template.md    ← estrutura de report customizada
└── {another-client}/
    └── ...
```

## 📏 Regras de organização

### Naming

- Pasta do cliente: **kebab-case**, nome curto em inglês (ex: `acme-corp`, `patria`, `fintech-abc`)
- Arquivos: seguem as mesmas convenções do workspace (kebab-case, lowercase, inglês)

### KB — Knowledge Base (`kb/`)

Contém o conhecimento de negócio do cliente que os agentes usam durante a entrevista. Diferente dos knowledge packs globais (que são por domínio tecnológico), o KB do cliente é sobre **o contexto específico da empresa**.

| Tipo de arquivo | O que contém | Quando criar |
|-----------------|-------------|--------------|
| `integration-flow.md` | Fluxo de dados, sistemas, dependências entre áreas | Cliente tem ecossistema complexo |
| `tech-stack.md` | Ferramentas, plataformas, versões que o cliente já usa | Cliente tem stack definido |
| `business-context.md` | Modelo de negócio, regulações, restrições específicas | Cliente tem regras de negócio únicas |
| `{topic}.md` | Qualquer outro contexto relevante | Quando necessário |

> [!tip] KB vs Knowledge Packs
> **Knowledge packs** (em `knowledge/` na raiz do workspace) são por **domínio tecnológico** (SaaS, datalake, etc.) — qualquer cliente pode usar.
> **KB do cliente** (aqui em `custom-rules/{client}/kb/`) é sobre **a empresa específica** — só se aplica a esse cliente.
> Ambos são carregados durante o setup. O orchestrator copia o knowledge pack para `setup/customization/current-context/` e o KB do cliente fica acessível via referência direta.

### Assets (`assets/`)

Assets visuais do cliente usados na geração de reports.

| Arquivo | Uso |
|---------|-----|
| `logo.png` | Logo do cliente para header/footer do delivery report |
| `logo-dark.png` | Variante dark (se disponível) |
| `logo-light.png` | Variante light (se disponível) |

> [!info] Prioridade de assets
> Se o cliente tem logo próprio, o html-writer usa o logo do cliente no report. Caso contrário, usa o logo global do workspace.

### Rules (`rules/`)

Regras adicionais que **só se aplicam** a este cliente. Seguem o mesmo formato das rules do pipeline, mas são carregadas apenas quando o orchestrator detecta que a run é para este cliente.

Exemplos:
- Regra de compliance específica do setor
- Formato obrigatório de entrega
- Restrições de confidencialidade

### Config (`config/`)

Overrides de configuração que substituem os defaults do `templates/customization/`. Mesmos arquivos, valores diferentes.

| Arquivo | O que controla |
|---------|----------------|
| `scoring-thresholds.md` | Pisos de nota do auditor e 10th-man |
| `iteration-policy.md` | Limites de iteração, política de restart |
| `final-report-template.md` | Estrutura/seções do relatório final |

> [!warning] Prioridade
> Durante o setup, o orchestrator copia configs nesta ordem de prioridade:
> 1. `custom-rules/{client}/config/` — se existir, sobrescreve
> 2. `templates/customization/` — fallback (defaults)

## 🚀 Como usar

### 1. Criar pasta do cliente

```bash
mkdir -p custom-rules/{client-name}/{kb,assets,rules,config}
```

### 2. Popular com conteúdo

- Adicione KB relevante em `kb/`
- Coloque o logo em `assets/`
- Crie regras específicas em `rules/` se necessário
- Copie e ajuste configs de `templates/customization/` para `config/` se necessário

### 3. Informar o orchestrator

No `briefing.md` da run, adicione no frontmatter:

```yaml
client: {client-name}
```

O orchestrator detecta e carrega automaticamente o conteúdo de `custom-rules/{client-name}/`.

### 4. O que o orchestrator faz com isso

| Recurso | Ação do orchestrator |
|---------|---------------------|
| `kb/` | Carrega como contexto adicional para os agentes na Fase 1 |
| `assets/logo.png` | Passa para o html-writer ao gerar o delivery report |
| `rules/` | Carrega como regras adicionais para toda a run |
| `config/` | Copia para `setup/customization/` sobrescrevendo os defaults |

## 📄 Exemplo

```
custom-rules/
└── acme-corp/
    ├── kb/
    │   ├── integration-flow.md      ← "Acme usa SAP + Salesforce + Snowflake"
    │   └── business-context.md      ← "Regulado pela CVM, compliance SOX obrigatório"
    ├── assets/
    │   └── logo.png                 ← Logo da Acme Corp
    ├── rules/
    │   └── sox-compliance.md        ← "Todo artefato deve ter trilha de auditoria SOX"
    └── config/
        └── scoring-thresholds.md    ← "Profile high-risk: pisos mais altos"
```

## 🔗 Documentos Relacionados

- `templates/customization/` — Defaults de configuração (fallback)
- `knowledge/` — Knowledge packs globais por domínio tecnológico
- `skills/orchestrator/SKILL.md` — Como o orchestrator carrega custom-rules
- `docs/quick-start.md` — Como iniciar uma run (campo `client` no briefing)
