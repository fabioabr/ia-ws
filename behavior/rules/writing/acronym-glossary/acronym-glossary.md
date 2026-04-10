---
title: Acronym Glossary
description: Regra mandatória para tratamento de siglas em documentos HTML e Markdown. Toda sigla deve ter destaque visual, tooltip com significado e seção/aba de glossário no final do documento.
project-name: global
version: 01.02.000
status: ativo
author: claude-code
category: rule
area: tecnologia
tags:
  - rule
  - core
  - acronym
  - glossary
  - html
  - markdown
  - accessibility
created: 2026-04-10
---

# Acronym Glossary — Regra Mandatória

> [!danger] Regra obrigatória para TODA geração de HTML e Markdown
> Esta regra se aplica a **todos** os documentos gerados pelo sistema — reports, relatórios, apresentações, ou qualquer outro artefato em `.md` ou `.html`. Não existe exceção.

---

## 1. O que é uma sigla

Qualquer palavra formada por iniciais ou abreviação que **não seja autoexplicativa** para um leitor generalista.

> [!info] Na dúvida, trate como sigla
> Se o leitor médio (gerente não-técnico) pode não saber o significado, inclua no glossário.

---

## 2. Convenções Aplicáveis

Ao gerar qualquer documento, aplique o tratamento de siglas conforme o formato do artefato:

| Convenção | Referência | Quando aplicar |
| --------- | ---------- | -------------- |
| Tratamento em Markdown | `conventions/acronyms/markdown-treatment.md` | Todo arquivo `.md` — primeira ocorrência por extenso, glossário se 3+ siglas |
| Tratamento em HTML | `conventions/acronyms/html-treatment.md` | Todo arquivo `.html` — tag `<abbr>` com tooltip, CSS obrigatório, aba de glossário como última tab |
| Banco de Siglas | `conventions/acronyms/acronym-bank.md` | Consultar **sempre** antes de gerar qualquer documento. Fonte de verdade para significados e tooltips. |

---

## 3. Processo de coleta de siglas

O agente ou skill que gera o documento deve:

1. **Varrer** todo o conteúdo em busca de palavras com 2+ letras maiúsculas consecutivas OU termos técnicos conhecidos
2. **Consultar o banco** (`conventions/acronyms/acronym-bank.md`) para obter significado e tooltip corretos
3. **Montar a lista** de siglas únicas encontradas
4. **Aplicar o tratamento** conforme o formato do documento (MD ou HTML), seguindo a convenção correspondente
5. **Gerar o glossário** ao final do documento (como última seção/aba)
6. **Não inventar significados** — se não souber o significado de uma sigla, marcar como `[?]` e sinalizar
7. **Adicionar siglas novas** ao banco se encontrar alguma que não esteja registrada

> [!warning] Banco de Siglas é a fonte de verdade
> Se houver divergência entre o banco e um documento, o banco prevalece. Ao encontrar uma sigla nova que não está no banco, adicione-a após usar no documento.

---

## Changelog

| Versão | Data | Descrição |
|---|---|---|
| 01.00.000 | 2026-04-10 | Versão inicial. Regra mandatória para siglas em HTML e MD: destaque visual, tooltip, glossário como última aba/seção. |
| 01.01.000 | 2026-04-09 | Adição da seção 6 (Banco de Siglas) e criação do assets/acronym-bank.md com 66 siglas |
| 01.02.000 | 2026-04-10 | Refatoração: conteúdo de convenções extraído para `conventions/acronyms/`; regra agora referencia convenções via tabela |
