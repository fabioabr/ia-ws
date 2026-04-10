---
title: Project Boundaries
description: Como a IA deve buscar, respeitar e reagir a fronteiras definidas por cada projeto
project-name: global
version: 01.01.004
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - fronteira
  - projeto
  - restricao
created: 2026-04-03 11:30
---

# 🚧 Fronteiras de Projeto

Regra fundamental que define como a IA deve interagir com **fronteiras** — restrições e limites definidos por cada projeto que referencia o behavior global. Fronteiras são **absolutas**: quando existem, a IA **bloqueia** qualquer ação que as viole.

---

## 🧩 O que são Fronteiras

Fronteiras são **restrições de qualquer natureza** definidas por um projeto. Elas delimitam o que pode e o que não pode ser feito dentro daquele contexto.

| Tipo de Fronteira | Exemplos |
| ----------------- | -------- |
| 💻 **Tecnologia** | Stack obrigatória, linguagens permitidas, frameworks, bancos de dados |
| 🔐 **Segurança** | Autenticação, permissões, compliance, criptografia |
| 🏢 **Processo** | Metodologia, fluxos de aprovação, cerimônias, deploy |
| 📊 **Negócio** | Escopo do produto, regras de domínio, restrições legais |
| 🏗️ **Arquitetura** | Padrões de projeto, camadas, integrações obrigatórias |
| 📝 **Documentação** | Padrões específicos do projeto que complementam ou customizam o behavior global |

> [!info] Abrangência
> Fronteiras não se limitam a tecnologia. Qualquer restrição que o projeto defina — de negócio, legal, processo, arquitetura — é uma fronteira.

---

## 📂 Estrutura no Projeto

Todo projeto que referencia o behavior global **pode** definir suas fronteiras em:

```
projeto/
└── docs/
    └── 2-boundaries/
        ├── index.md              ← índice de todas as fronteiras
        ├── technology.md         ← stack, ferramentas, infra
        ├── security.md           ← autenticação, compliance
        ├── process.md            ← metodologia, fluxos, deploy
        ├── business.md           ← regras de domínio, escopo
        ├── architecture.md       ← padrões, camadas, integrações
        └── ...                   ← quantas forem necessárias
```

### 📏 Regras da estrutura

- 📁 A pasta **deve** ser `docs/2-boundaries/`
- 📑 **Deve** ter um `index.md` que lista todas as fronteiras
- 📄 Cada arquivo segue as regras de [[core/markdown-writing/markdown-writing]] (frontmatter, visual, etc.)
- 🏷️ Cada fronteira deve ter **título claro**, **descrição** e **exemplos** do que é permitido e proibido
- ➕ O projeto pode ter **quantos arquivos** de fronteira precisar

### 📋 Formato de um arquivo de fronteira

```markdown
---
title: Tecnologia
description: Stack e ferramentas permitidas no projeto
version: 01.00.000
status: ativo
author: identificador
category: fronteira
area: tecnologia
tags:
  - fronteira
  - stack
  - tecnologia
created: 2026-04-03 11:30
---

# 💻 Fronteiras de Tecnologia

## 🌐 Web
- ✅ Permitido: Blazor, .NET
- ❌ Proibido: Python (Django/Flask), Node.js, PHP

## 📱 Mobile
- ✅ Permitido: Flutter
- ❌ Proibido: React Native, desenvolvimento nativo

## 🗄️ Banco de Dados
- ✅ Permitido: PostgreSQL
- ❌ Proibido: MySQL, MongoDB, SQLite em produção
```

---

## 🔍 Como a IA Busca Fronteiras

### 📋 Fluxo de descoberta

Ao iniciar qualquer tarefa em um projeto, a IA deve:

**1️⃣ Verificar se existem fronteiras**

- Buscar a pasta `docs/2-boundaries/` no projeto
- Se **existir** → ler o `index.md` e carregar as fronteiras relevantes
- Se **não existir** → prosseguir normalmente (fronteiras são opcionais)

**2️⃣ Extrair contexto da demanda do usuário**

- Identificar **palavras-chave** da solicitação (ex: "web", "Python", "deploy")
- Mapear para **categorias** de fronteira (ex: "web" → `tecnologia.md`)

**3️⃣ Cruzar com as fronteiras**

- Ler os arquivos de fronteira relevantes
- Verificar se a demanda **conflita** com alguma restrição
- Se **conflitar** → bloquear (ver seção abaixo)
- Se **não conflitar** → prosseguir normalmente

> [!tip] Dica
> A IA não precisa ler **todas** as fronteiras para cada demanda. Deve focar nas fronteiras **relevantes ao contexto** da solicitação.

---

## 🚫 Comportamento em Caso de Conflito

> [!danger] Regra absoluta
> Quando uma fronteira é violada, a IA **bloqueia a execução**. Não existe desvio, não existe exceção. A fronteira deve ser alterada para que a IA prossiga.

### 📋 Fluxo de bloqueio

```
👤 "Quero um sistema web em Python"
        │
        ▼
🔍 IA consulta fronteiras:
   tecnologia.md → "Web = Blazor, Python proibido"
        │
        ▼
🚫 BLOQUEIO
   IA informa:
   - ⚠️ Qual fronteira foi violada
   - 📄 Onde está definida
   - ✅ O que é permitido pela fronteira
   - 🔧 Como alterar a fronteira se necessário
        │
        ▼
👤 Usuário decide:
   ├── ✅ Ajustar a demanda → fluxo continua
   └── 🔧 Alterar a fronteira → altera, depois continua
```

### 📝 Mensagem de bloqueio

A IA deve informar de forma clara:

> [!example] Exemplo de bloqueio
> **🚫 Fronteira violada: Tecnologia**
>
> Sua solicitação pede **Python para web**, mas a fronteira do projeto define:
> - ✅ Permitido: **Blazor, .NET**
> - ❌ Proibido: **Python (Django/Flask), Node.js, PHP**
>
> 📄 Definido em: `docs/2-boundaries/technology.md`
>
> **Opções:**
> 1. Ajustar a demanda para usar Blazor
> 2. Alterar a fronteira em `docs/2-boundaries/technology.md`

> [!warning] Atenção
> A IA **nunca sugere ignorar** a fronteira. As únicas opções são ajustar a demanda ou alterar a fronteira.

---

## 🔄 Fronteiras e o Behavior Global

### 📌 Hierarquia

Fronteiras de projeto **podem customizar** regras do behavior global para melhor atender o contexto específico do projeto.

| Cenário | O que acontece |
| ------- | -------------- |
| Fronteira **adiciona** restrição | ✅ Normal — projeto é mais restritivo que o global |
| Fronteira **customiza** regra global | ✅ Permitido — adaptação legítima ao contexto do projeto |
| Sem fronteiras definidas | ✅ IA trabalha normalmente, porém mais permissiva |

> [!info] Proteção proativa
> Quando **não existem fronteiras**, a IA funciona normalmente mas deve atuar para **diminuir a possibilidade do usuário cometer erros** — fazendo mais perguntas de validação e sendo mais cautelosa nas sugestões.

---

## 🤖 Papel da IA

### Quando fronteiras existem

- 🔍 **Sempre consultar** fronteiras antes de agir
- 🚫 **Bloquear** quando houver conflito
- 📝 **Informar claramente** qual fronteira foi violada
- ✅ **Sugerir alternativas** dentro do que é permitido

### Quando fronteiras não existem

- 🧠 **Ser mais cautelosa** nas sugestões
- ❓ **Fazer mais perguntas** de validação
- 💡 **Sugerir a criação** de fronteiras quando identificar decisões importantes que deveriam ser documentadas como restrição

---

## 🔗 Documentos Relacionados

- [[core/behavior-principles/behavior-principles]] — Princípios fundamentais que governam o comportamento da IA, incluindo fronteiras
- [[core/document-management/document-management]] — Ciclo de vida aplicável aos arquivos de fronteira
- [[core/markdown-writing/markdown-writing]] — Regras de formatação que os arquivos de fronteira devem seguir

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-03 11:30 | Criação do documento                                                      |
| 01.01.000 | 2026-04-03 13:00 | Localização alterada de `.claude/fronteiras/` para `docs/fronteiras/`     |
| 01.01.001 | 2026-04-03 13:00 | Adição de backlink para levantamento-de-projeto                           |
| 01.01.002 | 2026-04-03 13:30 | Correção do diagrama de estrutura para `docs/fronteiras/`                 |
| 01.01.003 | 2026-04-04 09:30 | Renomeação de fronteiras-de-projeto para project-boundaries (naming-convention) |
| 01.01.004 | 2026-04-05 | Atualização terminologia v1 para v2: "Nível 2" substituído por "Sub-etapa 2" |
