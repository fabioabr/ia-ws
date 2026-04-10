---
title: Variables
description: Variáveis globais utilizadas na geração de relatórios HTML e documentos
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: asset
area: tecnologia
tags:
  - variavel
  - template
  - relatorio
created: 2026-04-04 20:00
---

# 📋 Variables

Variáveis globais utilizadas na geração de relatórios HTML e outros documentos. Estas variáveis são lidas pela skill de geração de relatórios para preencher o rodapé e outros elementos dinâmicos.

> [!info] Como usar
> A skill de geração de relatórios lê este arquivo e substitui as variáveis nos templates HTML. Formato: `{{variable-name}}`.

---

## 🏢 Company

| Variável | Valor | Uso |
| -------- | ----- | --- |
| `{{company-name}}` | mAInd Tech | Nome da empresa no rodapé e header |
| `{{company-slogan}}` | Smart Thinking, Exponential Productivity | Slogan exibido no rodapé |

## 📅 Metadata

| Variável | Valor | Uso |
| -------- | ----- | --- |
| `{{year}}` | 2026 | Ano atual para copyright |
| `{{version}}` | 1.0 | Versão do sistema de relatórios |
| `{{generated-date}}` | (dinâmico) | Data/hora de geração do relatório — preenchido automaticamente |

## 🔐 Compliance

| Variável | Valor | Uso |
| -------- | ----- | --- |
| `{{confidentiality}}` | Interno — Uso restrito | Classificação de confidencialidade no rodapé |

## 📧 Contact

| Variável | Valor | Uso |
| -------- | ----- | --- |
| `{{contact-email}}` | tech@maind.com.br | Email de contato no rodapé |
| `{{website}}` | https://maind.com.br | Website no rodapé |

---

## 🔄 Formato do Rodapé

O rodapé gerado nos relatórios HTML segue este formato:

```
© {{year}} {{company-name}} — {{company-slogan}}
{{confidentiality}} | {{contact-email}} | {{website}}
v{{version}}
```

**Exemplo renderizado:**

```
© 2026 mAInd Tech — Smart Thinking, Exponential Productivity
Interno — Uso restrito | tech@maind.com.br  | https://www.maind.com.br/ 
v1.0
```

---

## 🔗 Documentos Relacionados

- [[behavior/rules/core/markdown-writing/markdown-writing]] — Regras de formatação dos documentos fonte

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-04 20:00 | Criação do documento |
