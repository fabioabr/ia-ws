---
name: html-writer
argument-hint: "<source.md> [--output path] [--template name]"
title: html-writer
description: "Converte documentos .md em relatórios HTML auto-contidos seguindo o Design System do workspace. Use SEMPRE que precisar: gerar um relatório HTML a partir de um .md, converter documento markdown para apresentação visual, criar report HTML com dark/light theme, ou gerar HTML auto-contido com logos e estilos inline. O HTML gerado funciona abrindo direto no navegador, sem servidor. NÃO use para: formatar o .md em si (use md-writer), validar convenções (use md-validator), ou gerar diagramas (use diagram-drawio)."
project-name: global
version: 02.03.000
author: claude-code
license: MIT
status: ativo
category: report
area: tecnologia
tags:
  - report
  - html
  - design-system
  - relatorio
created: 2026-04-10 12:00
inputs:
  - name: source
    type: file-path
    required: true
    description: Caminho do(s) arquivo(s) .md a converter
outputs:
  - name: report
    type: file
    format: html
    description: Arquivo HTML self-hosted gerado no mesmo diretório do .md fonte
---

# Report Maker — Gerador de Relatórios HTML

Você é o **Report Maker** — responsável por converter documentos `.md` em relatórios HTML auto-contidos, visualmente ricos e prontos para distribuição.

**Arquivo(s) fonte:** $ARGUMENTS

Se nenhum argumento for informado, pergunte qual documento converter.

---

## Convention References

Antes de gerar o HTML, carregue as convenções abaixo para obter tokens e definições atualizadas:

| Convenção | Arquivo | O que contém |
| --------- | ------- | ------------ |
| Callouts | `conventions/markdown/callouts.md` | Tipos de callout Obsidian e sintaxe |
| Breakpoints | `conventions/responsive/breakpoints.md` | Container max-width, breakpoint mobile, comportamento de grid |
| Cores | `conventions/colors/palette.md` | Tokens de cor (primary, success, warning, danger, info, etc.) |
| Componentes | `conventions/components/*.md` | Card, alerts, badge, table, stat-card, header-footer, tabs |

## 📋 Instructions

### 1. Preparação — Carregar referências

> [!danger] Regra obrigatória — playground.html é a base
> O CSS do playground.html (`assets/ui-ux/playground.html`) DEVE ser copiado integralmente para cada HTML gerado. NÃO reinvente estilos — use as classes existentes do Design System:
>
> **Classes obrigatórias do playground:**
> - Layout: `.container`, `.header`, `.header-content`, `.header-top`, `.header-left`, `.header-right`
> - Cards: `.card`, `.card-header`, `.card-header-icon`, `.card-title`, `.card-badge`, `.card-body`
> - Stat cards: `.stats-grid`, `.stat-card`, `.stat-card-icon`, `.stat-card-info`, `.stat-card-number`, `.stat-card-label`
> - Alerts: `.alert`, `.alert-warning`, `.alert-danger`, `.alert-info`, `.alert-success`
> - Pills/Badges: `.pill`, `.pill-success`, `.pill-info`, `.pill-warning`, `.pill-danger`
> - Tabs: `.tabs-nav`, `.tab-btn`, `.tab-btn.active`, `.tab-content`, `.tab-content.active`
> - Tables: styled `<table>` with `th` using `var(--th-bg)`
> - Intro text: `.intro-text`
> - Footer: `.footer`
>
> O agente DEVE ler o playground.html **INTEIRO** (não só 200 linhas) e extrair TODO o bloco `<style>`. Componentes custom (scenario bars, radar, timeline) são **adições** ao CSS base — nunca substituições.

> [!danger] Regra de prioridade para assets (variables, logos, ui-ux)
> A caracterização visual do **projeto** tem prioridade sobre o Workspace global. Para **todo asset** (variables, logos, design system, playground), aplicar:
>
> 1. **Primeiro:** procurar em `{pasta-base-do-projeto}/assets/`
> 2. **Fallback:** se não encontrar, usar `E:/Workspace/assets/`
> 3. **Merge:** se ambos existirem, carregar os dois — assets do **projeto sobrescrevem** os globais
>
> A "pasta-base do projeto" é o diretório raiz onde o `.md` fonte está localizado (subindo até encontrar `docs/` ou `behavior-global.md` como indicador de raiz de projeto). Se não for possível identificar a raiz, usar diretamente o fallback global.

Leia obrigatoriamente (respeitando a prioridade acima):

| Asset | Caminho relativo dentro de `assets/` | Uso |
| ----- | ------------------------------------- | --- |
| Design System | `ui-ux/design-system.md` | Tokens de cor, tipografia, componentes, regras de contraste |
| Playground | `ui-ux/playground.html` | Modelo HTML de referência (estrutura, CSS, JS, i18n) |
| Variáveis | `variables.md` | Variáveis para rodapé e header |
| Logo dark | `logos/dark.png` | Logo para tema escuro (converter para base64) |
| Logo light | `logos/light.png` | Logo para tema claro (converter para base64) |

### 2. Ler o(s) documento(s) fonte

Leia o(s) `.md` indicado(s) em `$ARGUMENTS`. Entenda:
- O frontmatter (title, description, project-name, version, author, etc.)
- A estrutura de seções (headings, tabelas, callouts, listas, código)
- Os dados e conteúdo textual

### 3. Gerar o HTML

Crie um arquivo `.html` **auto-contido** (todo CSS e JS inline, sem dependências externas exceto CDNs de fontes e ícones).

#### Estrutura do HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} — {{project-name}}</title>
    <!-- Google Fonts: Poppins -->
    <!-- Remix Icons CDN -->
    <style>
        /* Design System tokens (copiar do playground) */
        /* Dark theme (default) + Light theme */
        /* Todos os componentes necessários */
    </style>
</head>
<body>
    <!-- HEADER -->
    <!-- CONTEÚDO -->
    <!-- FOOTER -->
    <script>
        /* Toggle theme */
        /* i18n (apenas pt-BR ativo, EN e ES desabilitados) */
    </script>
</body>
</html>
```

### 4. Regras de Conversão MD → HTML

#### Frontmatter → Header

| Campo do frontmatter | Onde no HTML |
| -------------------- | ------------ |
| `title` | `<h1>` no header |
| `description` | Subtítulo no header |
| `project-name` | Badge no header |
| `version` | Badge no header |
| `created` | Badge de data no header |
| `status` | Badge com cor semântica (ativo=success, rascunho=warning, etc.) |

#### Markdown → Componentes HTML

| Elemento Markdown | Componente HTML |
| ----------------- | --------------- |
| `# H1` | Section header com ícone |
| `## H2` | Card header |
| `### H3` | Subtítulo dentro de card |
| Tabela `\| col \|` | Tabela estilizada (`<table>` com classes do design system) |
| Callouts `> [!type]` | Alertas estilizados (ver tipos em `conventions/markdown/callouts.md`) |
| Lista `- item` | Lista estilizada |
| Lista `1. item` | Lista ordenada estilizada |
| `✅` / `❌` | Badges success / danger |
| `🔴` / `🟡` / `🟢` / `⚪` | Pills com cores semânticas |
| `` `código` `` | `<code>` inline estilizado |
| ` ```bloco``` ` | Bloco de código com syntax highlighting básico |
| `**negrito**` | `<strong>` |
| `*itálico*` | `<em>` |
| `---` | `<hr>` estilizado |
| Emojis | Mantidos como estão (Unicode) |

#### Dados numéricos → KPI Cards

Quando o conteúdo tiver tabelas com notas percentuais, scores ou métricas:
- Converter para **stat cards** (KPI) no topo da seção
- Usar cores semânticas: ≥90% success, 70-89% warning, <70% danger

#### Wikilinks

- `[[wikilink]]` → remover a formatação de link (converter para texto simples ou link interno `#`)
- Não gerar links quebrados

### 4.5. Renderização por Regions (Delivery Reports)

Quando o `.md` fonte contiver **marcadores de region** (`<!-- region: REG-XXXX-NN -->`), o html-writer opera em **modo regions** — cada bloco é renderizado com o template visual recomendado pelo chart-specialist.

#### Como detectar modo regions

Se o frontmatter contiver o campo `regions: [...]` OU o conteúdo tiver marcadores `<!-- region: -->`, ativar modo regions.

#### Leitura do html-layout.md

Ler o arquivo `html-layout.md` para determinar:
- **Quais regions** renderizar (regions no `.md` que não estão no layout são omitidas do HTML)
- **Em que ordem** (a ordem do layout prevalece sobre a ordem do `.md`)
- **Com que disposição** (full-width, grid-2, grid-3, grid-4, sidebar)

Prioridade de leitura:
1. `{project}/setup/customization/html-layout.md` (override do cliente)
2. `dtg-artifacts/templates/customization/html-layout.md` (default)
3. Se nenhum existir: renderizar todas as regions na ordem do `.md` como full-width

#### Templates visuais por region

Cada region tem uma recomendação de visualização no catálogo (`base-artifacts/templates/report-regions/{grupo}/{region}.md` → seção "Recomendação do Chart Specialist"). Aplicar:

| Veredicto | Como renderizar |
|-----------|----------------|
| **CARD** | Componente card do Design System (card-header + card-body) com ícone e conteúdo |
| **TABELA** | `<table>` estilizada com badges, pills e cores semânticas conforme dados |
| **GRÁFICO (Chart.js)** | `<canvas>` com Chart.js inline — tipos: radar, bubble, pie, donut, line |
| **GRÁFICO (HTML/CSS)** | Barras horizontais, progress bars, timelines, heatmaps — tudo em CSS puro |

Prioridade de tecnologia: **HTML/CSS puro > Chart.js > Card informativo**

> [!danger] SVG inline NÃO é permitido para gráficos de dados
> SVG inline não está na lista de tecnologias aprovadas. Para gráficos de dados:
> - **Barras horizontais simples** → HTML/CSS puro (divs com width proporcional)
> - **Stacked bars, line, radar, bubble, pie** → Chart.js
> - **Progress bars, gauges** → HTML/CSS puro
>
> SVG inline só é aceito para ícones custom quando Remix Icon não tem o ícone necessário.

> [!danger] Gráficos de barras = SEMPRE HTML/CSS horizontal
> Chart.js NÃO é usado para gráficos de barras (simples, agrupadas, empilhadas). Barras são SEMPRE renderizadas em HTML/CSS com orientação horizontal.
>
> CSS padrão para barras:
> ```css
> .bar-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
> .bar-label { width: 120px; font-size: 0.75rem; text-align: right; flex-shrink: 0; }
> .bar-track { flex: 1; background: var(--border); border-radius: 4px; height: 20px; overflow: hidden; }
> .bar-fill { height: 100%; border-radius: 4px; transition: width 0.3s; }
> .bar-value { width: 60px; font-size: 0.72rem; text-align: right; }
> ```
>
> Chart.js fica APENAS para: radar, pie/donut, line/area, scatter, bubble.

#### Layouts de grid

```html
<!-- full-width -->
<div class="region-row">
    <div class="region-col-12">...</div>
</div>

<!-- grid-2 -->
<div class="region-row">
    <div class="region-col-6">...</div>
    <div class="region-col-6">...</div>
</div>

<!-- grid-3 -->
<div class="region-row">
    <div class="region-col-4">...</div>
    <div class="region-col-4">...</div>
    <div class="region-col-4">...</div>
</div>

<!-- grid-4 -->
<div class="region-row">
    <div class="region-col-3">...</div>
    <div class="region-col-3">...</div>
    <div class="region-col-3">...</div>
    <div class="region-col-3">...</div>
</div>
```

CSS para o grid:
```css
.region-row { display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap; }
.region-col-12 { flex: 0 0 100%; }
.region-col-6 { flex: 0 0 calc(50% - 8px); }
.region-col-4 { flex: 0 0 calc(33.333% - 11px); }
.region-col-3 { flex: 0 0 calc(25% - 12px); }
@media (max-width: 768px) {
    .region-col-6, .region-col-4, .region-col-3 { flex: 0 0 100%; }
}
```

#### Navegação por tabs (executive e complete)

| Setup | Navegação |
|-------|-----------|
| `essential` (one-pager) | **SEM tabs** — página única contínua |
| `executive` | **COM tabs** — cada seção do html-layout.md vira uma aba |
| `complete` | **COM tabs** — mesma estrutura, mais abas |

Usar as classes do playground.html:
```html
<div class="tabs-nav">
    <button class="tab-btn active" data-tab="produto">
        <i class="ri-lightbulb-line"></i> Produto
        <span class="tab-count">6</span>
    </button>
    <button class="tab-btn" data-tab="financeiro">
        <i class="ri-money-dollar-circle-line"></i> Financeiro
        <span class="tab-count">3</span>
    </button>
    ...
</div>
<div class="tab-content active" id="produto">
    <!-- regions desta seção -->
</div>
<div class="tab-content" id="financeiro">
    <!-- regions desta seção -->
</div>
```

**Tabs padrão para executive:**
- Produto e Valor (ícone: ri-lightbulb-line)
- Organização (ícone: ri-team-line)
- Financeiro (ícone: ri-money-dollar-circle-line)
- Riscos e Qualidade (ícone: ri-shield-check-line)
- Decisão (ícone: ri-checkbox-circle-line)
- Domain-specific (ícone: ri-apps-line) — se houver
- Glossário (ícone: ri-book-open-line) — se houver

**JS para tabs:**
```javascript
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById(btn.dataset.tab).classList.add('active');
    });
});
```

#### Chart.js (quando necessário)

Incluir CDN apenas se houver regions que usam Chart.js:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
```

Regions que usam Chart.js (conforme chart-specialist):
- REG-EXEC-03 (radar 4 eixos)
- REG-FIN-02 (line com crossover)
- REG-FIN-04 (line)
- REG-RISK-01 (bubble)
- REG-RISK-04 (radar 4 eixos)
- REG-QUAL-01 (radar 5 eixos)
- REG-PESQ-05 (donut)

#### Previews de referência

HTMLs de referência com exemplos visuais de cada grupo estão em `base-artifacts/templates/report-regions/_previews/`. Consultar para entender como cada region deve ser renderizada.

### 4.6. Glossário e Tooltips de Siglas

Toda sigla conhecida no texto DEVE ser envolvida em `<abbr>`:

```html
<abbr title="Total Cost of Ownership">TCO</abbr>
```

**Processo:**
1. Consultar `base-artifacts/conventions/acronyms/acronym-bank.md` para expansões
2. Na primeira ocorrência de cada sigla: gerar `<abbr>` com tooltip
3. Ocorrências subsequentes: manter `<abbr>` (tooltip sempre disponível)
4. Siglas NÃO encontradas no banco: usar estilo diferente (`text-decoration: underline dotted; cursor: help;`) sem tooltip
5. No final de cada HTML: gerar seção "Glossário" listando todas as siglas usadas com expansões

**CSS para tooltips:**
```css
abbr[title] { text-decoration: underline dotted; cursor: help; }
abbr[title]:hover { text-decoration: underline solid; }
```

### 5. Header

Seguir o padrão do playground:
- **Logo**: embutir as imagens como base64 (usar logos carregados na Preparação, respeitando prioridade projeto → global)
- **Título**: do frontmatter `title`
- **Subtítulo**: do frontmatter `description`
- **Badges**: project-name, version, data de geração, status
- **Seletor de idioma**: PT ativo, **EN e ES desabilitados** (`disabled`, `opacity:0.35`, `cursor:not-allowed`)
- **Toggle dark/light**: funcional

### 6. Footer

Preencher com variáveis carregadas na etapa de Preparação (respeitando a ordem de prioridade: projeto → global):
- **Author**: `{{company-name}}`
- **Role**: `{{company-slogan}}`
- **Data**: `{{generated-date}}` — usar data/hora atual no momento da geração
- **Doc title**: do frontmatter `title`
- **Doc detail**: do frontmatter `description`
- **Seal**: `Documento gerado automaticamente — {{company-name}}`

### 7. Temas Dark/Light

- **Dark** é o tema padrão (seguir tokens do playground `:root`)
- **Light** theme via `[data-theme="light"]` (seguir tokens do playground)
- Toggle funcional via botão no header
- **Header e footer mantêm visual escuro** em ambos os temas (conforme design system)

### 8. Idioma

> [!danger] Regra inviolável
> O relatório é **exclusivamente em pt-BR**. Toda acentuação portuguesa **deve** ser respeitada (não usar "organizacao" — usar "organização"). O conteúdo fonte em .md pode não ter acentos nos campos técnicos (tags, nomes de arquivo), mas o conteúdo textual renderizado DEVE ter acentuação correta.

> [!danger] Reforço — acentuação é OBRIGATÓRIA em TODOS os textos
> Esta regra se aplica a TODOS os textos gerados — títulos de seções, labels de tabelas, labels de gráficos, tooltips, legendas, badges, cards, e texto corrido. Exemplos de erros comuns:
>
> | ERRADO | CORRETO |
> |--------|---------|
> | Descricao | Descrição |
> | Organizacao | Organização |
> | Projecao | Projeção |
> | Cenarios | Cenários |
> | Analise | Análise |
> | Financeiro (ok) | Financeiro (ok) |
> | Tecnico | Técnico |
> | Viabilidade (ok) | Viabilidade (ok) |
> | Estimativa (ok) | Estimativa (ok) |
>
> Se o texto fonte (.md) não tem acentos, o html-writer DEVE corrigir ao renderizar.

- Seletor de idioma visível no header com 3 bandeiras (BR, US, ES)
- **PT** ativo e selecionado por padrão
- **EN e ES desabilitados** (`disabled`, `opacity:0.35`, `cursor:not-allowed`)
- Manter a estrutura i18n do playground (variável `T` no JS) mesmo que só PT seja usado — facilita expansão futura

### 9. Output

- Salvar o HTML no **mesmo diretório** do `.md` fonte, com o mesmo nome mas extensão `.html`
  - Exemplo: `challenger-report.md` → `challenger-report.html`
- O HTML deve ser **100% auto-contido**:
  - CSS inline no `<style>`
  - JS inline no `<script>`
  - Logos como base64 no `<img src="data:image/png;base64,...">`
  - Fontes via CDN (Google Fonts) — única dependência externa
  - Ícones via CDN (Remix Icon) — única dependência externa

### 10. Responsividade

Aplicar os breakpoints e container definidos em `conventions/responsive/breakpoints.md`. O relatório deve ser **legível em tela e imprimível** (considerar `@media print`).

#### Responsividade mobile (< 768px)

Quando a viewport é menor que 768px:

**1. Hamburger menu (substitui tabs + tema):**
- Ocultar `.tabs-nav` e `.theme-toggle` do header
- Mostrar botão hamburger (`ri-menu-line`) no header-right
- Ao clicar: toggle `.mobile-menu` (dropdown abaixo do header)
- Menu contém: lista das tabs como itens + botão de tema como último item
- Ao selecionar tab: fechar menu + ativar tab
- Fechar ao clicar fora

CSS:
```css
.hamburger-btn { display: none; width: 40px; height: 40px; border-radius: 8px; background: rgba(255,255,255,0.1); border: none; color: white; font-size: 1.2rem; cursor: pointer; align-items: center; justify-content: center; }
.mobile-menu { display: none; position: absolute; top: 100%; left: 0; right: 0; background: var(--card-bg); border-bottom: 1px solid var(--border); z-index: 100; padding: 8px 0; }
.mobile-menu.open { display: flex; flex-direction: column; }
.mobile-menu-item { display: flex; align-items: center; gap: 10px; padding: 12px 24px; color: var(--text); font-size: 0.85rem; cursor: pointer; border: none; background: none; width: 100%; text-align: left; }
.mobile-menu-item:hover { background: var(--th-bg-hover); }
.mobile-menu-item.active { color: var(--primary); font-weight: 600; }
.mobile-menu-item i { font-size: 1.1rem; width: 20px; }

@media (max-width: 768px) {
    .tabs-nav { display: none !important; }
    .theme-toggle { display: none !important; }
    .hamburger-btn { display: flex; }
}
@media (min-width: 769px) {
    .hamburger-btn { display: none !important; }
    .mobile-menu { display: none !important; }
}
```

JS:
```javascript
const hamburgerBtn = document.querySelector('.hamburger-btn');
const mobileMenu = document.querySelector('.mobile-menu');
if (hamburgerBtn) {
    hamburgerBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        mobileMenu.classList.toggle('open');
        hamburgerBtn.innerHTML = mobileMenu.classList.contains('open')
            ? '<i class="ri-close-line"></i>'
            : '<i class="ri-menu-line"></i>';
    });
    document.addEventListener('click', () => mobileMenu.classList.remove('open'));
    mobileMenu.querySelectorAll('.mobile-menu-item[data-tab]').forEach(item => {
        item.addEventListener('click', () => {
            const tabId = item.dataset.tab;
            // activate tab
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelector(`.tab-btn[data-tab="${tabId}"]`)?.classList.add('active');
            document.getElementById(tabId)?.classList.add('active');
            // update mobile menu active
            mobileMenu.querySelectorAll('.mobile-menu-item').forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            // close menu
            mobileMenu.classList.remove('open');
        });
    });
}
```

**2. Footer centralizado:**
```css
@media (max-width: 768px) {
    .footer { text-align: center; }
    .footer .container { flex-direction: column; align-items: center; gap: 8px; }
}
```

## 📄 Examples

### Exemplo 1 — Conversão simples de um único .md

**Input:** `/report-maker E:\projetos\alpha\docs\status-report.md`
**Output:** Arquivo `E:\projetos\alpha\docs\status-report.html` gerado com Design System do projeto alpha (encontrado em `E:\projetos\alpha\assets\`), logos do projeto em base64, variáveis do projeto, tema dark como padrão, seletor de idioma com PT ativo.

### Exemplo 2 — Fallback para assets globais

**Input:** `/report-maker E:\temp\notas\analise.md`
**Output:** Arquivo `E:\temp\notas\analise.html` gerado. Como não foi possível identificar uma raiz de projeto com assets próprios, utilizou fallback global (`E:\Workspace\assets\`) para Design System, playground, variáveis e logos. Conteúdo em pt-BR com acentuação correta, KPI cards gerados a partir de tabelas com métricas percentuais.

## 🚫 Constraints

- Em modo regions: renderizar apenas as regions listadas no `html-layout.md` — o `.md` é completo, o HTML é configurável
- Em modo padrão (sem regions): nunca omitir seções, tabelas ou informações do `.md` fonte
- Usar exclusivamente cores, tipografia e componentes do Design System carregado — não inventar estilos
- Acentuação pt-BR é obrigatória em todo texto renderizado
- O HTML deve funcionar abrindo o arquivo direto no navegador, sem servidor
- Logos devem ser embutidos como base64, nunca como paths relativos
- Não gerar links quebrados a partir de wikilinks
- Assets do projeto sempre têm prioridade sobre os globais
- Na dúvida sobre como renderizar um componente, consultar o playground.html

## 🔧 claude-code

### Trigger
Keywords no `description` do frontmatter: report, relatório, HTML, converter md, gerar relatório. O Claude Code usa o campo `description` para decidir quando invocar a skill automaticamente.

### Arguments
Usar `$ARGUMENTS` no corpo para capturar o caminho do(s) arquivo(s) .md passados pelo usuário via `/report-maker caminho/do/arquivo.md`.

### Permissions
- bash: true
- file-read: true
- file-write: true
- web-fetch: false

## 🔗 Documentos Relacionados

- `conventions/frontmatter/document-schema.md` — Schema de frontmatter para documentos
- `conventions/frontmatter/skill-schema.md` — Schema de frontmatter para skills
- `conventions/markdown/callouts.md` — Tipos de callout Obsidian e sintaxe
- `conventions/responsive/breakpoints.md` — Breakpoints e container responsivo
- `conventions/colors/palette.md` — Tokens de cor do Design System
- `conventions/components/*.md` — Componentes do Design System (card, alerts, badge, table, etc.)

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 02.03.000 | 2026-04-12 | P36: responsividade mobile — hamburger menu substitui tabs+tema em viewports < 768px, footer centralizado em mobile |
| 02.02.000 | 2026-04-12 | P33: playground.html é base obrigatória — CSS copiado integralmente, classes listadas. P34: barras sempre HTML/CSS horizontal, REG-FIN-01 removido do Chart.js |
| 02.01.000 | 2026-04-11 | P12: glossário e tooltips de siglas com `<abbr>`. P13/P15: proibição explícita de SVG inline para gráficos de dados |
| 02.00.000 | 2026-04-11 | Adição de modo regions: renderização por regions com marcadores, leitura de html-layout.md, grid responsivo, Chart.js condicional, referência a previews |
| 01.01.000 | 2026-04-10 | Adequação ao skill-schema com herança de document-schema; adição de campos title, project-name, area, created, license; emojis em H2; seções Documentos Relacionados e Histórico |
