# Project Dependency Template

Template para projetos que herdam regras, convenções e assets do workspace global. Copie este arquivo para a raiz do seu projeto como `dependency.md` e preencha os campos marcados com `{{...}}`.

## Template

```markdown
# Dependency — {{project-name}}

Este projeto herda regras, convenções e assets do workspace global.

## Workspace Global

| Item | Caminho |
|------|---------|
| Workspace | `E:/Workspace/` |
| Regras (behavior) | `E:/Workspace/behavior/rules/index.md` |
| Convenções | `E:/Workspace/conventions/` |
| Assets globais | `E:/Workspace/assets/` |
| Skills globais | `E:/Workspace/.claude/skills/` |
| Banco de siglas | `E:/Workspace/conventions/acronyms/acronym-bank.md` |

## O que é herdado

### Regras (obrigatórias)

A IA DEVE ler `behavior/rules/index.md` no início de cada sessão. As regras têm prioridade absoluta. Desvios devem ser registrados conforme o processo definido nas regras.

| Categoria | O que governa |
|-----------|--------------|
| foundations/ | Princípios de comportamento, fronteiras de projeto |
| writing/ | Markdown, naming, siglas, hallucination guard |
| organization/ | Tags, índices, ciclo de vida de documentos |
| code/ | Estrutura de skills |

### Convenções (obrigatórias)

A IA DEVE consultar `conventions/` para padrões concretos antes de gerar qualquer artefato.

| Categoria | O que define |
|-----------|-------------|
| naming/ | Kebab-case, inglês |
| versioning/ | Formato XX.YY.ZZZ |
| frontmatter/ | Schema de documentos e skills |
| tags/ | Taxonomia pt-BR sem acentos |
| markdown/ | Headings, callouts, diagramas, wikilinks, emojis, seções |
| acronyms/ | Tratamento MD/HTML, banco de siglas |
| colors/ | Paleta, sequencial, charts, contraste |
| typography/ | Escala tipográfica |
| spacing/ | Tokens, border-radius, shadows |
| components/ | Card, table, alerts, badges, tabs, stat-card, header-footer |
| charts/ | Chart.js config |
| variables/ | Variáveis de report (empresa, footer) |
| file-structure/ | Seções de documento, boundaries, index |
| skills/ | Estrutura do corpo de SKILL.md |

### Assets (com override local)

| Prioridade | Caminho |
|------------|---------|
| 1. Projeto | `{{project-path}}/assets/` |
| 2. Global (fallback) | `E:/Workspace/assets/` |

Se ambos existirem, assets do projeto sobrescrevem os globais.

| Asset | Caminho relativo em `assets/` |
|-------|-------------------------------|
| Design System | `ui_ux/design_system.md` |
| Playground | `ui_ux/playground.html` |
| Variáveis | `variables.md` |
| Logo dark | `logos/dark.png` |
| Logo light | `logos/light.png` |

### Skills (com extensão local)

| Prioridade | Caminho |
|------------|---------|
| 1. Projeto | `{{project-path}}/skills/` |
| 2. Global | `E:/Workspace/.claude/skills/` |

Skills do projeto estendem ou substituem as globais.

## Overrides do projeto

Listar aqui o que este projeto customiza em relação ao global:

| Item | Override | Descrição |
|------|----------|-----------|
| — | — | Nenhum override definido |

## Regras locais do projeto

Listar aqui regras adicionais que só se aplicam a este projeto:

| Regra | Caminho | Descrição |
|-------|---------|-----------|
| — | — | Nenhuma regra local definida |
```

## Como usar

1. Copie o bloco acima para `{seu-projeto}/dependency.md`
2. Substitua `{{project-name}}` pelo nome do projeto
3. Substitua `{{project-path}}` pelo caminho do projeto
4. Preencha a seção **Overrides** se o projeto customiza algo
5. Preencha a seção **Regras locais** se o projeto tem regras próprias
6. A IA deve ler este arquivo no início da sessão para saber de onde herda
