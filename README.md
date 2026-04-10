# ia-ws

Workspace compartilhado e agnóstico a projetos que centraliza regras de comportamento, convenções, design system e skills para assistentes de IA (Claude Code, OpenCode, Antigravity). Qualquer projeto pode herdar este workspace via template de dependência.

## Estrutura

```
ia-ws/
├── behavior/rules/          Regras de comportamento da IA (o que fazer e quando)
│   ├── foundations/          Princípios e fronteiras
│   ├── writing/              Markdown, naming, siglas, hallucination guard
│   ├── organization/         Tags, índices, ciclo de vida
│   └── code/                 Estrutura de skills
├── conventions/              Padrões concretos (como fazer)
│   ├── naming/               Kebab-case, inglês
│   ├── versioning/           Formato XX.YY.ZZZ
│   ├── frontmatter/          Schemas de documentos e skills
│   ├── tags/                 Taxonomia pt-BR sem acentos
│   ├── markdown/             Headings, callouts, diagramas, wikilinks, emojis, seções
│   ├── acronyms/             Tratamento MD/HTML, banco de siglas
│   ├── colors/               Paleta, sequencial, charts, contraste
│   ├── typography/           Escala tipográfica
│   ├── spacing/              Tokens, border-radius, shadows
│   ├── components/           Card, table, alerts, badges, tabs, stat-card, header-footer
│   ├── charts/               Chart.js config
│   ├── variables/            Variáveis de report
│   ├── file-structure/       Seções, boundaries, index, dependency template
│   ├── icons/                Remix Icon
│   ├── responsive/           Breakpoints
│   └── skills/               Estrutura do corpo de SKILL.md
├── assets/                   Assets globais compartilhados
│   ├── icons/                Icon packs
│   ├── logos/                Logos dark/light + base64
│   ├── ui_ux/                Design system, playground, paleta de barras
│   └── variables/            Variáveis de reports
├── .claude/skills/           Skills globais para Claude Code
│   ├── md-writer/            Formata qualquer .md seguindo convenções
│   ├── skill-writer/         Cria/formata SKILL.md (Obsidian + Claude + OpenCode + Antigravity)
│   ├── html-writer/          Converte .md em HTML auto-contido
│   ├── diagram-drawio/       Gera diagramas draw.io
│   └── get-flaticon/         Baixa ícones do Flaticon
├── support-tools/            Ferramentas de suporte recomendadas
│   └── git-nexus/            Knowledge graph para codebase
└── CLAUDE.md                 Entry point para Claude Code
```

## Conceitos

### Rules vs Conventions

| | Rules (`behavior/rules/`) | Conventions (`conventions/`) |
|---|---|---|
| **O que define** | Como a IA deve se comportar | Padrões concretos e schemas |
| **Exemplo** | "Toda sigla deve ser tratada" | "Primeira ocorrência por extenso + (SIGLA)" |
| **Quem consome** | A IA (instruções comportamentais) | Qualquer pessoa ou ferramenta |
| **Formato** | Frontmatter + instruções + changelog | Referência pura (tabelas, listas) |

### Skills

Skills seguem um formato universal compatível com 4 plataformas:

- **Obsidian** — documentação navegável
- **Claude Code** — trigger via `/skill-name`
- **OpenCode** — agent config
- **Antigravity** — execution config

Estrutura: frontmatter (inputs/outputs) + Instructions + Examples + Constraints + seções por plataforma.

### Herança por projeto

Projetos herdam regras, convenções e assets deste workspace. Para vincular um projeto:

1. Copie `conventions/file-structure/dependency.md` para a raiz do projeto
2. Preencha os campos `{{project-name}}` e `{{project-path}}`
3. Declare overrides e regras locais

Assets do projeto sobrescrevem os globais (logos, design system, variáveis).

## Compatibilidade

| Plataforma | Suporte |
|------------|---------|
| Claude Code | Skills via `.claude/skills/`, rules via `CLAUDE.md` |
| OpenCode | Skills com seção `## open-code` |
| Antigravity | Skills com seção `## antigravity` |
| Obsidian | Leitura e navegação nativa (wikilinks, frontmatter, callouts) |
| Qualquer editor | Todos os `.md` seguem convenções universais de Markdown |

> As convenções de escrita (headings, callouts, wikilinks, frontmatter, emojis, section-order) se aplicam a **todo arquivo .md** do workspace — não são exclusivas do Obsidian. O Obsidian é apenas uma das ferramentas compatíveis.
