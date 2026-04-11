---
title: Audit Log
description: Regra obrigatória de registro cronológico de todo processo de auditoria — cada auditor gera seu log, o orquestrador consolida
project-name: global
version: 01.03.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - auditoria
  - registro
  - rastreabilidade
created: 2026-04-04 13:00
---

# 🔍 Audit Log

Regra obrigatória que define o **registro cronológico** de todo processo de auditoria. Cada auditor especializado gera seu próprio log, e o orquestrador consolida todos em um relatório final.

> [!danger] Regra inviolável
> **Toda auditoria DEVE ser logada.** Nenhum auditor pode operar sem gerar um log. O log é a evidência do trabalho realizado e a base para o relatório consolidado.

---

## 📂 Localização

No Pipeline v0.5, os logs de auditoria ficam dentro de cada **iteração**, organizados em `draft/` e `logs/`:

```
projeto/
└── runs/
    └── run-{n}/
        └── iterations/
            └── iteration-{i}/
                ├── results/
                │   └── 2-challenge/
                │       └── 2.1-convergent-validation.md   ← relatório consolidado da auditoria
                └── logs/
                    ├── auditor-log.md                     ← log do auditor
                    └── ...                                ← demais logs de agentes
```

> [!info] Separação de responsabilidades
> No Pipeline v0.5, os artefatos ficam organizados por **iteração** em `runs/run-{n}/iterations/iteration-{i}/`. O relatório de auditoria vai em `results/2-challenge/2.1-convergent-validation.md` e os logs individuais ficam em `logs/`.

> [!tip] Histórico de auditorias
> Cada iteração contém sua própria auditoria. Iterações sucessivas permitem acompanhar a evolução da qualidade ao longo do tempo.

> [!warning] Atenção
> O `audit-report.md` é o **relatório final consolidado** gerado pelo agente `auditor`. Os demais são logs individuais de cada agente.

---

## 📋 Estrutura do Log de Cada Auditor

```markdown
---
title: Audit Log — [Tipo] — [Nome do Projeto]
description: Registro do processo de auditoria [tipo] do projeto [nome]
version: 01.00.000
status: ativo
author: claude-code
category: log
area: tecnologia
tags:
  - log
  - auditoria
  - [tipo]
  - [nome-do-projeto]
created: YYYY-MM-DD HH:mm
---

# 🔍 Audit Log — [Tipo]

## 📊 Resumo

| Item | Valor |
| ---- | ----- |
| 🎯 **Projeto** | Nome do projeto |
| 🔍 **Tipo de auditoria** | Docs / Business / Tech |
| 🤖 **Auditor** | Identificador do agente |
| 📅 **Início** | Timestamp |
| 📅 **Conclusão** | Timestamp ou "Em andamento" |
| 📊 **Resultado** | ✅ Aprovado / ⚠️ Ressalvas / ❌ Reprovado |

---

## 🕐 Timeline

| Timestamp | Tipo | Descrição |
| --------- | ---- | --------- |
| ... | ... | ... |

---

## 📊 Resultado

(Tabela de achados com severidade)

## 📜 Histórico de Alterações

| Versão | Timestamp | Descrição |
| ------ | --------- | --------- |
| 01.00.000 | YYYY-MM-DD HH:mm | Criação do log |
```

---

## 🏷️ Tipos de Entrada

| Tipo | Emoji | Quando usar |
| ---- | ----- | ----------- |
| **Início** | 🎯 | Início da auditoria ou de uma seção |
| **Verificação** | 🔎 | Item sendo verificado |
| **Aprovado** | ✅ | Check passou |
| **Falha** | ❌ | Check falhou — detalhar o que e por quê |
| **Observação** | 💡 | Insight, risco ou ponto de atenção |
| **Recomendação** | 📋 | Sugestão de melhoria |
| **Conflito** | 🚫 | Inconsistência entre documentos |
| **Cálculo** | 🧮 | Quando o auditor faz cálculos (orçamento, prazo, custo) |
| **Conclusão** | 🏁 | Término da auditoria com veredicto |

---

## 📊 Estrutura do Relatório Consolidado

O agente `auditor` gera o `audit-report.md` com:

```markdown
# 📊 Audit Report — [Nome do Projeto]

## 📋 Resumo Executivo

| Frente | Auditor | Nota | Resultado |
| ------ | ------- | ---- | --------- |
| 📋 Compliance (frontmatter, tags, visual, naming) | auditor | X% | ✅/⚠️/❌ |
| 🔄 Regras do Pipeline (requirement-priority, budget, sequencia) | auditor | X% | ✅/⚠️/❌ |

## 🏁 Nota Final: XX%

(Média ponderada das frentes)

## 🚨 Top N Achados (por prioridade)

## ✅ Pontos Fortes

## 📋 Recomendações

## 📜 Histórico de Alterações
```

> [!info] Escala de notas
> Todas as frentes de auditoria usam **nota de 0% a 100%**, indicando o grau de perfeição, clareza e respeito às regras. A nota final é a **média ponderada** das frentes.

| Faixa | Status | Significado |
| ----- | ------ | ----------- |
| 90-100% | ✅ Aprovado | Excelente — pronto para prosseguir |
| 70-89% | ⚠️ Ressalvas | Bom mas precisa de ajustes antes de prosseguir |
| 50-69% | ❌ Reprovado | Insuficiente — requer correções significativas |
| 0-49% | ❌ Reprovado crítico | Comprometido — requer retrabalho substancial |

---

## 📏 Regras de Registro

- ✅ **Toda verificação** deve ser registrada (passou ou falhou)
- ✅ Cada entrada com **timestamp** no formato `yyyy-MM-DD HH:mm`
- ✅ Falhas devem incluir **o que falhou, por quê e sugestão de correção**
- ✅ Cálculos devem mostrar **os números e a fonte**
- ❌ **Não omitir** falhas — a auditoria só tem valor se for honesta
- ❌ **Não editar** entradas anteriores — append-only

> [!danger] Regra inviolável
> Uma auditoria que diz "tudo ok" sem evidências é **inválida**. Todo check deve ter registro explícito de pass/fail com justificativa.

---

## 🔗 Documentos Relacionados

- [[rules/analyst-discovery-log/analyst-discovery-log]] — Log do processo de discovery que antecede a auditoria
- [[rules/discovery/discovery]] — Processo de discovery cujos resultados são auditados
- Behavior Principles (workspace global) — Princípios fundamentais de registro e rastreabilidade
- Markdown Writing (workspace global) — Regras de formatação para os logs

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-04 13:00 | Criação do documento                                                  |
| 01.01.000 | 2026-04-04 13:30 | Nota percentual (0-100%) para todas as frentes e nota final ponderada |
| 01.02.000 | 2026-04-05 | Atualização Pipeline v2: audit/ agora fica dentro de cada sub-etapa, não mais em pasta 5-audit/ centralizada. Referências de auditores atualizadas |
| 01.03.000 | 2026-04-11 | Pipeline v0.5: estrutura de pastas atualizada para runs/run-{n}/iteration-{i}/. Audit reports em draft/audit-report.md, logs em logs/. Agentes atualizados. Terminologia "sub-etapa" → "fase" |
