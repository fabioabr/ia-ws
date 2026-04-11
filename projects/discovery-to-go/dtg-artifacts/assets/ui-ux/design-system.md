---
id: DOC-000002
doc_type: architecture-doc
title: Design System
system: Todos
module: UI
domain: Design
owner: fabio
team: arquitetura
status: approved
confidentiality: internal
tags: [design-system, cores, tipografia, componentes, ui, ux]
created_at: 2026-03-17
updated_at: 2026-03-26
---

# Design System 

Este documento define os padrões visuais e de interface para todos os produtos, documentos e aplicações. Serve como referência única para garantir consistência visual entre equipes e projetos.

> **Referência visual:** O playground de componentes (`.claude/behavior/ui-ux/playground.html`) é o modelo interativo oficial. Este documento descreve os tokens e regras; o playground os demonstra.

---

## 1. Paleta de Cores

### 1.1 Cores Primárias (Brand)

| Nome / Token     | Hex (Dark)  | Hex (Light) | Uso principal                                  |
|------------------|-------------|-------------|-------------------------------------------------|
| `$primary`       | `#4DA8DA`   | `#4DA8DA`   | Cor principal da marca, destaques, CTAs          |
| `$primary-dark`  | `#3A8BB8`   | `#3A8BB8`   | Hover de elementos primários                     |
| `$primary-light` | `rgba(77,168,218,0.12)` | `rgba(77,168,218,0.1)` | Backgrounds sutis, badges |

### 1.2 Escala de Cinzas (Estrutural)

| Nome / Token            | Hex       | Uso principal                          |
|-------------------------|-----------|----------------------------------------|
| `$dark-gray`            | `#1A1923` | Background principal (dark)            |
| `$medium-gray`          | `#2E2D32` | Cards, header, footer (dark)           |
| `$faint-readable-gray`  | `#88878C` | Texto secundário, placeholders         |
| `$second-light-gray`    | `#B9B7BD` | Bordas (light), elementos neutros      |
| `$light-gray`           | `#E0DFE3` | Background principal (light), texto (dark) |
| White                   | `#FFFFFF` | Background de cards (light)            |

### 1.3 Cores Semânticas

| Nome / Token | Hex (Dark)  | Hex (Light) | Uso                                  |
|-------------|-------------|-------------|--------------------------------------|
| `$success`  | `#0ED145`   | `#0A9E35`   | Confirmações, status positivo        |
| `$warning`  | `#F4AC00`   | `#E67E22`   | Alertas, ações que requerem atenção  |
| `$danger`   | `#8B1A1A`   | `#E74C3C`   | Erros, validações negativas          |
| `$accent`   | `#2EB5F5`   | `#1E95CC`   | Informações, links, elementos interativos |

> **Nota:** No tema dark, o texto sobre danger usa `#E85D54` (danger-text) para garantir legibilidade.

> **Nota:** A cor primária é `#4DA8DA` (azul) em ambos os temas (dark e light). As cores de warning e danger diferem entre temas para garantir contraste adequado em cada background.

### 1.4 Cores de Gráficos

Paleta vibrante dedicada a visualizações de dados (Chart.js, barras CSS, progress bars):

| Token      | Hex (Dark)  | Hex (Light) | Identificação |
|------------|-------------|-------------|---------------|
| `--chart-1`| `#4DA8DA`   | `#4DA8DA`   | Azul (primário, ambos os temas) |
| `--chart-2`| `#2EB5F5`   | `#1E95CC`   | Azul          |
| `--chart-3`| `#0ED145`   | `#0A9E35`   | Verde         |
| `--chart-4`| `#FF6B6B`   | `#D44040`   | Coral/Vermelho|
| `--chart-5`| `#A78BFA`   | `#7C6BD4`   | Roxo          |

### 1.5 Cores Auxiliares

| Token      | Hex       | Uso                        |
|------------|-----------|----------------------------|
| `--purple` | `#9B96FF` | Badges, destaques          |
| `--orange` | `#FF9473` | Acentos secundários        |
| `--teal`   | `#2DD4BF` | Indicadores complementares |

---

## 2. Regra de Contraste (Obrigatória)

**Regra geral:** texto sobre fundo claro deve ser escuro e vice-versa.

| Fundo                    | Cor do texto       | Exemplos                          |
|--------------------------|--------------------|-----------------------------------|
| Claro (azul, verde, laranja, teal, warning, secondary) | `#1A1923` | Ícones, badges, bar segments |
| Escuro (danger, purple, info/azul) | `#FFFFFF` | Ícones, badges |
| `$dark-gray` / `$medium-gray`     | `#E0DFE3` | Texto principal no dark theme |
| White / `$light-gray`             | `#1A1923` | Texto principal no light theme |

**Para textos em cards e blocos descritivos:** usar `--text` com `opacity: 0.85`.

---

## 3. Tipografia

### 3.1 Família Tipográfica

| Contexto    | Família               | Fallback                    |
|-------------|-----------------------|-----------------------------|
| Interface   | **Poppins**           | `system-ui, sans-serif`     |
| Código      | **Consolas**          | `'Courier New', monospace`  |
| Documentos  | **Poppins**           | `system-ui, sans-serif`     |

### 3.2 Escala Tipográfica

| Elemento     | Tamanho    | Peso       | Line Height | Uso                         |
|--------------|------------|------------|-------------|-----------------------------|
| Display      | `1.5rem`   | Bold (700) | `1.2`       | Títulos de página           |
| H1           | `1.15rem`  | Semi (600) | `1.3`       | Títulos de seção            |
| H2           | `0.95rem`  | Semi (600) | `1.3`       | Títulos de card             |
| Body         | `0.88rem`  | Regular (400) | `1.5`    | Texto principal             |
| Body Small   | `0.82rem`  | Regular (400) | `1.5`    | Texto secundário            |
| Caption      | `0.72rem`  | Semi (600) | `1.4`       | Labels, KPIs, uppercase     |
| Code         | `0.78rem`  | Regular (400) | `1.6`    | Blocos de código            |

---

## 4. Espaçamento

Base de espaçamento: **4px**

| Token  | Valor   | Uso                                 |
|--------|---------|-------------------------------------|
| `xs`   | `4px`   | Espaço mínimo entre ícone e texto   |
| `sm`   | `8px`   | Padding interno de badges, gaps     |
| `md`   | `16px`  | Padding de inputs, gaps de grid     |
| `lg`   | `24px`  | Padding de cards, margem entre seções |
| `xl`   | `32px`  | Separação entre blocos              |
| `2xl`  | `48px`  | Margem de seções principais         |

---

## 5. Bordas e Sombras

### 5.1 Border Radius

| Token     | Valor    | Uso                        |
|-----------|----------|----------------------------|
| `sm`      | `6px`    | Inputs, badges, bar charts |
| `md`      | `8px`    | Cards internos             |
| `lg`      | `12px`   | Cards, modais              |
| `full`    | `9999px` | Avatares, pills            |

### 5.2 Sombras (Elevation)

| Nível | Dark Theme                                                       | Light Theme                                            |
|-------|------------------------------------------------------------------|--------------------------------------------------------|
| 1     | `0 2px 12px rgba(46,181,245,0.06), 0 1px 4px rgba(0,0,0,0.4)`  | `0 2px 8px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.06)` |
| 2     | `0 4px 16px rgba(46,181,245,0.1), 0 2px 8px rgba(0,0,0,0.5)`   | `0 4px 12px rgba(0,0,0,0.15)`                         |

> **Nota:** No tema dark, as sombras usam brilho azul (`rgba(46,181,245,...)`) para consistência com a cor primária.

---

## 6. Componentes Base

### 6.1 Header e Footer

- Background: gradiente `#2E2D32 → #252428 → #1A1923` (igual nos dois temas)
- Texto: `#FFFFFF`
- Badges internos: `rgba(255,255,255,0.15)` com backdrop-filter blur
- **Header mantém o mesmo visual em dark e light**
- Footer avatar usa o logo da empresa (dark/light swap automatico)
- Botao back-to-top usa `--info` (azul) em vez de `--primary`, em ambos os temas. Hover: `#1E95CC`.

### 6.2 Tabs (Navegação por abas)

| Estado   | Background                  | Texto (Dark)     | Texto (Light)  |
|----------|-----------------------------|------------------|----------------|
| Inativa  | `rgba(255,255,255,0.1)`    | `rgba(255,255,255,0.7)` | `rgba(255,255,255,0.7)` |
| Hover    | `rgba(255,255,255,0.18)`   | `#FFFFFF`        | `#FFFFFF`      |
| Ativa    | `var(--bg)`                 | `var(--text)` (`#E0DFE3`) | `#2E2D32` |

- Badge de contagem (`.tab-count`): herda a cor do texto da aba pai
- Scrollbar horizontal: fina (4px), translúcida

### 6.3 Cards

- Background: `var(--card-bg)` — `#2E2D32` (dark) / `#FFFFFF` (light)
- Borda: `1px solid var(--border)`
- Border radius: `lg` (12px)
- Header: `var(--card-header-bg)` com ícone colorido e título
- Body: texto `var(--text)` com `opacity: 0.85`
- Hover: sombra + borda `var(--primary)`

### 6.4 Stat Cards (KPI)

- Layout: ícone (44x44px, border-radius 10px) + valor + label
- Valor: cor semântica correspondente (primary, info, success, warning)
- Label: `var(--text-muted)`, uppercase, 0.72rem

### 6.5 Alertas

| Variante | Background            | Borda                  | Texto                       |
|----------|-----------------------|------------------------|-----------------------------|
| Success  | `var(--success-light)`| `var(--success-border)`| `var(--alert-success-text)` |
| Warning  | `var(--warning-light)`| `var(--warning-border)`| `var(--alert-warning-text)` |
| Danger   | `var(--danger-light)` | `var(--danger-border)` | `var(--alert-danger-text)`  |
| Info     | `var(--info-light)`   | `var(--info-border)`   | `var(--alert-info-text)`    |

### 6.6 Pills / Badges

Mesma lógica de cores dos alertas, em formato inline compacto (border-radius 12px, font-size 0.7rem).

### 6.7 Tabelas

- Header: `var(--th-bg)`, texto `var(--text-muted)`, uppercase, 0.75rem
- Linhas: hover com `var(--primary-light)`
- Textos destacados (nomes/links): usar `var(--info)` ou `var(--primary)` (ambos são azul)
- Valores numéricos: font monospace (`Consolas`), alinhados à direita

### 6.8 Seletor de Idioma

- Botão ativo: borda branca, fundo `rgba(255,255,255,0.22)`, cor branca
- Botão desabilitado: `disabled`, `opacity: 0.35`, `cursor: not-allowed`
- Sempre sobre fundo escuro do header

---

## 7. Componentes de Dashboard

### 7.1 KPI Strip (`.dash-kpi-strip`)

Grid 4 colunas com cards de indicador. Variante `.highlight` com borda acentuada e fundo diferenciado.

### 7.2 Highlight Box (`.dash-highlight-box`)

Seção hero com gradiente do header, até 3 métricas separadas por divisores verticais.

### 7.3 Ranking Table

Tabela com badges circulares de posição (`.dash-rank-1` a `.dash-rank-5`), cada um com cor distinta.

### 7.4 Bar Charts (CSS)

- Horizontais empilhados (`.dash-bar-*`): segmentos coloridos com texto escuro
- Verticais (`.dash-vbar-*`): barras com cores chart-1 a chart-5

### 7.5 Progress Bars (`.dash-progress-*`)

Barras finas (8px) com header informativo (dot + label + percentual + valor).

### 7.6 Distribution Cards (`.dash-dist-*`)

Boxes comparativos lado a lado. Variante `.active` com borda primária.

### 7.7 Insight Cards (`.dash-insight`)

Grid 4 colunas com ícone emoji, título e descrição. Variantes: `.warn` (borda warning), `.ok` (borda success).

### 7.8 Chart.js (Gráficos Interativos)

Biblioteca: **Chart.js v4.4.7** (CDN standalone).

**Regras gerais:**
- Usar a paleta `--chart-1` a `--chart-5`
- Ler cores via `getComputedStyle` para respeitar o tema ativo
- Reconstruir ao alternar tema (dark ↔ light) via hook no `toggleTheme()`
- Tooltips: fundo `var(--card-bg)`, borda `var(--border)`, border-radius 8px
- Grid lines: `var(--border)`
- Labels de eixo: `var(--text-muted)`, font Poppins 11px
- Legendas: `usePointStyle: true`, `pointStyle: 'circle'`

**Layout no playground:**
- Charts organizados em grid 2 colunas (`grid-2`), com `playground-label` + `playground-section`
- Cards com `padding: 12px` no body e `margin-bottom: 0`
- Proporção compacta: ~4 de largura × 2 de altura

**Regras por tipo de gráfico:**

| Tipo          | Legenda          | Observações                                      |
|---------------|------------------|--------------------------------------------------|
| Bar (vertical)| Oculta           | `borderRadius: 6`, `borderSkipped: false`        |
| Bar (horizontal)| Oculta         | `indexAxis: 'y'`                                 |
| Doughnut      | Direita          | `cutout: '55%'`, `maintainAspectRatio: false`, container `height: 180px` |
| Pie           | Direita          | `maintainAspectRatio: false`, container `height: 180px` |
| Line          | Topo             | `fill: true`, `tension: 0.4`, área com opacidade `22` |
| Stacked Bar   | Topo             | `stacked: true` em ambos os eixos               |
| Radar         | Topo             | Grid e angleLines com `var(--border)`, ticks `backdropColor: 'transparent'` |

**Legenda lateral (Doughnut/Pie):**
- `position: 'right'`
- `boxWidth: 10`, `padding: 10`, `font.size: 10`
- Gráfico fica à esquerda, legenda à direita dentro do mesmo card

Tipos disponíveis no playground: Bar, Horizontal Bar, Doughnut, Pie, Line (com fill), Stacked Bar, Radar.

---

## 8. Ícones

- Biblioteca: **Remix Icon** (CDN: `remixicon@4.1.0`)
- Tamanhos: `1rem` (card headers), `1.1rem` (tabs, section headers), `1.3rem` (stat cards)
- Cor: herdada do `.bg-*` (contraste automático via regra da seção 2)

---

## 9. Responsividade

### Breakpoints

| Nome   | Largura máxima | Ajustes                               |
|--------|----------------|---------------------------------------|
| Mobile | `768px`        | Grid 1 col, tabs wrap, stats 1 col    |

### Container

- Max-width: `1400px`
- Padding lateral: `24px`

---

## 10. Tokens CSS (Referência Rápida)

```css
:root {
  /* Primárias */
  --primary: #4DA8DA;
  --primary-dark: #3A8BB8;
  --primary-light: rgba(77, 168, 218, 0.12);

  /* Estruturais */
  --bg: #1A1923;
  --card-bg: #2E2D32;
  --text: #E0DFE3;
  --text-muted: #88878C;
  --border: #3E3D44;
  --card-header-bg: #252428;

  /* Semânticas */
  --success: #0ED145;
  --warning: #F4AC00;
  --danger: #8B1A1A;
  --danger-text: #E85D54;
  --info: #2EB5F5;

  /* Gráficos */
  --chart-1: #4DA8DA;
  --chart-2: #2EB5F5;
  --chart-3: #0ED145;
  --chart-4: #FF6B6B;
  --chart-5: #A78BFA;

  /* Auxiliares */
  --purple: #9B96FF;
  --orange: #FF9473;
  --teal: #2DD4BF;

  /* Tipografia */
  --font-family: 'Poppins', sans-serif;
  --font-family-mono: 'Consolas', 'Courier New', monospace;

  /* Sombra */
  --card-shadow: 0 2px 12px rgba(46,181,245,0.06), 0 1px 4px rgba(0,0,0,0.4);
}
```

> **Nota:** A cor primária é `#4DA8DA` (azul) em ambos os temas. Tokens como `--primary`, `--primary-dark`, `--primary-light` e `--chart-1` são idênticos em dark e light. As cores de warning e danger diferem entre temas para garantir contraste adequado.

---

## 11. Princípios de Design

1. **Clareza** — Interfaces devem comunicar com precisão. Priorizar legibilidade e hierarquia visual.
2. **Consistência** — Usar os mesmos padrões em todos os produtos. Componentes reutilizáveis, tokens centralizados.
3. **Confiança** — O visual deve transmitir solidez e segurança, adequado ao contexto bancário.
4. **Contraste** — Todo texto deve ser legível: fundo claro → texto escuro, fundo escuro → texto claro. Sem exceções.
5. **Simplicidade** — Menos é mais. Reduzir ruído visual e focar no que importa.

---

## 12. Checklist de Validação

Antes de publicar qualquer material visual, verificar:

- [ ] Usa exclusivamente cores da paleta definida (seções 1.1 a 1.5)
- [ ] Regra de contraste respeitada (seção 2)
- [ ] Tipografia segue família Poppins e escala definida (seção 3)
- [ ] Espaçamentos usam os tokens do sistema (seção 4)
- [ ] Header/footer mantêm visual escuro em ambos os temas
- [ ] Gráficos usam `--chart-*`, não tokens de UI
- [ ] Textos destacados em tabelas usam `--info` ou `--primary` (ambos azul)
- [ ] Textos em cards usam `--text` com `opacity: 0.85`
- [ ] Hierarquia visual está clara (títulos > subtítulos > corpo > captions)
- [ ] Material se adapta corretamente aos temas dark e light
