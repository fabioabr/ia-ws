---
title: "Report Plan — Veezoozin"
project-name: veezoozin
version: 03.00.000
status: gerado
author: report-planner
category: delivery
created: 2026-04-12
source: delivery-report.md
blueprint: saas + ai-ml + datalake-ingestion
report-setup: executive
total-regions: 26
chart-js-required: true
run: run-3
---

# Report Plan — Veezoozin

> Plano de renderização visual para os 2 HTMLs do setup **executive**.
> Fonte: `delivery-report.md` (26 regions) | Blueprint: saas + ai-ml + datalake-ingestion | Run: run-3

## Resumo de Outputs

| Arquivo | Regions | Descrição |
|---------|:-------:|-----------|
| `one-pager.html` | 8 | Página única executiva — overview, problema, TCO, cenários, riscos, Go/No-Go, esforço, próximos passos |
| `executive-report.html` | 22 | Relatório corporativo completo — produto, organização, financeiro, cenários, riscos, qualidade, backlog, glossário |

## Regras de Renderização

| Regra | Descrição |
|-------|-----------|
| **P13/P15 — Sem SVG inline** | Nenhum diagrama SVG embutido no HTML. Diagramas de arquitetura como placeholder com descrição textual |
| **P17 — 10th-man layout** | Seção do 10th-man segue o mesmo layout da seção do auditor (radar com mesma estrutura visual, mas 3 eixos) |
| **P18 — Radar com zonas** | Radar charts incluem zonas coloridas: verde (>=80%), amarelo (60-79%), vermelho (<60%) |
| **P12 — Glossário** | Seção de glossário renderizada como tabela estilizada ao final do executive-report |
| **P22 — Cenários financeiros** | Cenários alternativos como grouped bar chart (não stacked) |
| **P31 — Tabs executivas** | Seções agrupadas em tabs no executive-report (Produto, Organização, Técnico, Segurança, Financeiro, Riscos, Qualidade, Backlog) |
| **P32 — PT-BR com acentos** | Todo texto renderizado em português brasileiro com acentuação correta |
| **P33 — Playground CSS** | Classes CSS playground-compatible: `.region-card`, `.stat-badge`, `.score-radar`, `.risk-table`, `.pricing-grid` |
| **P34 — Barras horizontais** | Barras de progresso/score como HTML/CSS horizontal (não Chart.js) para elementos simples |

---

## Cobertura vs Executive Setup

| Status | Qtd | Regions |
|--------|:---:|---------|
| Presentes no delivery e no setup | 24 | REG-EXEC-01 a 04, REG-PROD-01/02/04/05/06/07, REG-ORG-01/02, REG-TECH-01/02/03, REG-SEC-01, REG-PRIV-01, REG-FIN-01/05/07, REG-RISK-01, REG-QUAL-01/02, REG-BACK-01 |
| Extras no delivery (adicionados por relevância) | 2 | REG-EXEC-05 (Decisões consolidadas), REG-GLOSS-01 (Glossário P12) |

---

## Tabela Geral — Plano por Region

### one-pager.html (8 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 1 | REG-EXEC-01 | full-width | Hero card com callouts + stat badges | HTML/CSS | Card com fundo gradiente escuro. Métricas destacadas: TCO R$ 1,2M, Receita R$ 1,36M, Resultado +R$ 155K, Break-even mês 19, Margem 86-94%, Score Auditor 88,8%, Score 10th-man 75,8%. Badge "GO — PROJETO VIÁVEL" em verde. Sem banner de alerta (nenhum flag ativo). |
| 2 | REG-PROD-01 | full-width | Grid 2x2 de cards dimensionais | HTML/CSS | 4 cards: Barreira técnica, Falta de contexto, Dados sem ação, Multi-idioma. Cada card com ícone, descrição e impacto. Abaixo: tabela Antes/Depois com setas (dias→segundos, 5%→100%, -80% tickets). |
| 3 | REG-FIN-01 | full-width | Stacked bar chart (TCO vs Receita) | Chart.js | Chart.js stacked bar — 3 barras (Ano 1, 2, 3), categorias: Equipe (azul), Infra GCP (laranja), Ferramentas (cinza). Linha sobreposta: receita acumulada (verde). Ano 3 em verde forte (resultado positivo). Labels com totais. |
| 4 | REG-FIN-07 | full-width | Grouped bar chart (cenários) | Chart.js | Chart.js grouped bar — 5 grupos (Base, A, B, C, D), 2 barras: Receita (verde) e Investimento até break-even (azul). Label com mês de break-even. Cenário base destacado com borda verde. Abaixo: tabela de Go/No-Go gates. |
| 5 | REG-RISK-01 | full-width | Tabela com severity badges | HTML/CSS | Tabela Top 10 riscos. Colunas: #, Risco, Prob., Impacto, Mitigação. Badges: Crítico (vermelho), Alto (laranja), Médio (amarelo). Hover com mitigação completa. |
| 6 | REG-EXEC-03 | full-width | Banner Go/No-Go + radar chart com zonas | Chart.js + HTML/CSS | Badge "GO — PROJETO VIÁVEL" (verde). Radar Chart.js com 5 eixos do auditor: Cobertura (92%), Profundidade (88%), Consistência (93%), Fundamentação (85%), Completude (85%). **Zonas P18:** verde (>=80%), amarelo (60-79%), vermelho (<60%). Ao lado: 5 recomendações de fortalecimento como checklist. |
| 7 | REG-FIN-05 | full-width | Tabela Build vs Buy com badges | HTML/CSS | Tabela: Componente, Decisão, Custo, Economia tempo. Badge BUILD (azul) e BUY (verde). Total: 840h economizadas em negrito. |
| 8 | REG-EXEC-04 | full-width | Timeline vertical com prioridades | HTML/CSS | 3 grupos: "Antes do dev" (3 itens — azul), "Durante dev" (3 itens — verde), "Pós-launch" (3 itens — laranja). Cada item: número, ação, prazo. |

---

### executive-report.html (22 regions)

#### Seção 1 — Produto e Valor (tab "Produto")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 9 | REG-EXEC-02 | full-width | Product brief card | HTML/CSS | Card com header (nome, empresa, tipo, maturidade, templates), body com visão e posicionamento. Tabela key-value estilizada. Sem flags (nenhum ativo). Badge "Run 3" e "Executive" no header. |
| 10 | REG-PROD-04 | full-width | Value proposition + alerta 10th-man | HTML/CSS | Tabela de concorrentes (4 linhas). Abaixo: callout verde com moat real (efeito de rede de contexto). Callout amarelo com alerta 10th-man sobre moat replicável. |
| 11 | REG-PROD-02 | grid-2 | Persona cards | HTML/CSS | Grid 2 colunas. 4 cards (Marina P0, Rafael P0, Lucas P1, Carla P1). Cada card: iniciais como avatar, cargo, frequência, JTBD, relação com BYOK. P0 com borda azul, P1 com borda cinza. Carla com badge "Poder de veto" em vermelho. |
| 12 | REG-PROD-05 | full-width | OKRs cards + métricas norte | HTML/CSS | 3 blocos OKR (O1 azul, O2 verde, O3 roxo), cada um com KRs. Abaixo: 4 estágios com métrica norte (Precisão→Ativação→MRR→NRR) como timeline horizontal com setas. |
| 13 | REG-PROD-06 | full-width | Pricing table 3 colunas | HTML/CSS | 3 colunas (Free, Pro, Enterprise) com preço, features como lista, badges. Pro destacado como "Recomendado". Enterprise com nota "Base + variável por usuário". Trial Pro 14 dias em destaque. |
| 14 | REG-PROD-07 | full-width | Scope split + timeline | HTML/CSS | Duas colunas: "Dentro" (verde) e "Fora" (cinza) como chips. Abaixo: roadmap horizontal 3 fases (MVP 12sem, Fase 2 +3m, Fase 3 +3m). |

#### Seção 2 — Organização (tab "Organização")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 15 | REG-ORG-01 | full-width | Team card + milestones de contratação | HTML/CSS | Card "1 pessoa + IA" com avatar e custo. Abaixo: timeline horizontal de contratação por MRR (R$ 25K→SRE, R$ 40K→CS, R$ 60K→Dev). Badge bus factor com callout de mitigação. |
| 16 | REG-ORG-02 | full-width | Metodologia + SLOs | HTML/CSS | Tabela de metodologia (7 aspectos). Abaixo: tabela de SLOs por tier (3 métricas x 3 tiers). Rituais anti-burnout como lista com ícones. |

#### Seção 3 — Arquitetura Técnica (tab "Técnico")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 17 | REG-TECH-01 | full-width | Stack table com badges por camada | HTML/CSS | Tabela 14 tecnologias agrupadas por camada (Cloud, Backend, Frontend, Dados, AI, Serviços). Badges: GCP-native (azul), Open-source (verde), Terceiro (cinza). |
| 18 | REG-TECH-02 | full-width | Pipeline 6 etapas + cache + budget latência | HTML/CSS | Tabela 6 etapas com latência alvo. Barra horizontal (P34) mostrando distribuição de latência por etapa (total <5s). Cache: economia 30-50%. **Sem diagrama SVG** — placeholder textual para arquitetura. |
| 19 | REG-TECH-03 | full-width | Módulos do Monolith + ADRs | HTML/CSS | Tabela 15 módulos agrupados (core vs suporte). Lista de 12 ADRs como badges. **Sem diagrama SVG** — card placeholder: "Modular Monolith: 15 módulos, deploy único em Cloud Run". |

#### Seção 4 — Segurança e Privacidade (tab "Segurança")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 20 | REG-SEC-01 | full-width | Security controls table | HTML/CSS | Tabela 10 controles de segurança com badges de prioridade. BYOK flow como texto descritivo (sem SVG). |
| 21 | REG-PRIV-01 | full-width | LGPD card completo | HTML/CSS | Card com seções: Modo (Profundo), Papéis LGPD, Sub-processadores, Bases legais, Retenção por tier, Direitos dos titulares, DPO strategy. Compliance por estágio de receita como timeline. |

#### Seção 5 — Financeiro (tab "Financeiro")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 22 | REG-FIN-01 | full-width | TCO stacked bar + projeção 36 meses | Chart.js + HTML/CSS | Reutiliza chart do one-pager. Adiciona: tabela de projeção mês a mês (marcos: primeiro MRR mês 5, break-even mês 19, payback mês 36). Comparativo run-2 vs run-3 como callout verde. |
| 23 | REG-FIN-05 | full-width | Build vs Buy detalhado | HTML/CSS | Reutiliza tabela do one-pager com 12 componentes. Total 840h. |
| 24 | REG-FIN-07 | full-width | Cenários + Go/No-Go + análise sensibilidade | Chart.js + HTML/CSS | Reutiliza grouped bar do one-pager. Adiciona: tabela completa 5 cenários x 5 métricas, Go/No-Go gates, análise de sensibilidade (custo fixo vs variável). |

#### Seção 6 — Riscos e Qualidade (tab "Riscos e Qualidade")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 25 | REG-RISK-01 | full-width | Risk table completa | HTML/CSS | Reutiliza tabela do one-pager com 10 riscos completos + mitigações |
| 26 | REG-QUAL-01 | sidebar | Radar chart auditor 5 eixos com zonas | Chart.js | Chart.js radar: Cobertura (92%), Profundidade (88%), Consistência (93%), Fundamentação (85%), Completude (85%). **Zonas P18:** verde (>=80%), amarelo (60-79%), vermelho (<60%). Score 88,8% como stat card. Findings F1-F3 como badges abaixo. |
| 27 | REG-QUAL-02 | full-width | 10th-man — **mesmo layout do auditor (P17)** | HTML/CSS + Chart.js | Radar Chart.js com 3 eixos: Divergência (70%), Robustez (78%), Completude Crítica (80%). **Zonas P18** iguais ao auditor. Score 75,8% como stat card. Premissas desafiadas (3) como cards com badges. Pontos cegos (4) como lista. Reconhecimento de pontos fortes como callout verde. |

#### Seção 7 — Backlog e Encerramento (tab "Backlog")

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|------------|-------------|
| 28 | REG-BACK-01 | full-width | Sprint timeline horizontal | HTML/CSS | Timeline horizontal 6 blocos (semanas 1-2 a 12) como blocos progressivos com cores (claro→escuro). Badge de foco em cada bloco. |
| 29 | REG-EXEC-04 | full-width | Next steps timeline vertical | HTML/CSS | Reutiliza timeline do one-pager com detalhamento |
| 30 | REG-EXEC-05 | full-width | Tabela de decisões consolidada | HTML/CSS | Tabela 14 decisões-chave. Colunas: #, Decisão, Status. Badges: Confirmada (verde), Recomendada→Aceita (azul). |
| 31 | REG-GLOSS-01 | full-width | Glossário estilizado (P12) | HTML/CSS | Tabela 20 termos. Colunas: Termo (negrito), Definição. Zebra striping. |

---

## Distribuição de Regions por Output

### one-pager.html (8 sections — essential setup equivalent)

| # | Region | Seção |
|---|--------|-------|
| 1 | REG-EXEC-01 | Resumo executivo + métricas-chave |
| 2 | REG-PROD-01 | Problema central |
| 3 | REG-FIN-01 | TCO e projeção financeira |
| 4 | REG-FIN-07 | Cenários de viabilidade |
| 5 | REG-RISK-01 | Top 10 riscos |
| 6 | REG-EXEC-03 | Go/No-Go + radar auditor |
| 7 | REG-FIN-05 | Build vs Buy |
| 8 | REG-EXEC-04 | Próximos passos |

### executive-report.html (22 sections — todas as regions)

Inclui as 8 do one-pager + 14 adicionais organizadas em tabs (P31):

| Tab | Regions |
|-----|---------|
| Produto | REG-EXEC-02, REG-PROD-01, REG-PROD-02, REG-PROD-04, REG-PROD-05, REG-PROD-06, REG-PROD-07 |
| Organização | REG-ORG-01, REG-ORG-02 |
| Técnico | REG-TECH-01, REG-TECH-02, REG-TECH-03 |
| Segurança | REG-SEC-01, REG-PRIV-01 |
| Financeiro | REG-FIN-01, REG-FIN-05, REG-FIN-07 |
| Riscos e Qualidade | REG-RISK-01, REG-QUAL-01, REG-QUAL-02 |
| Backlog | REG-BACK-01, REG-EXEC-04, REG-EXEC-05, REG-GLOSS-01 |

---

## Resumo Técnico

| Métrica | Valor |
|---------|-------|
| **Total regions** | 26 (delivery) → 31 (com duplicações entre one-pager e executive) |
| **Chart.js regions** | 5 (REG-FIN-01, REG-FIN-07, REG-EXEC-03, REG-QUAL-01, REG-QUAL-02) |
| **HTML/CSS only regions** | 21 |
| **Layout full-width** | 24 |
| **Layout grid-2** | 1 (REG-PROD-02 — personas) |
| **Layout sidebar** | 1 (REG-QUAL-01 — radar auditor) |
| **SVG inline** | 0 (P13/P15 — sem SVG) |
| **Radar charts com zonas (P18)** | 3 (REG-EXEC-03, REG-QUAL-01, REG-QUAL-02) |
| **Grouped bar chart** | 1 (REG-FIN-07 — cenários) |
| **Stacked bar chart** | 1 (REG-FIN-01 — TCO) |
| **Barras horizontais CSS (P34)** | 2 (REG-TECH-02 latência, REG-EXEC-01 scores) |
| **Tabs (P31)** | 7 tabs no executive-report |
| **PT-BR com acentos (P32)** | Sim — todo texto em português com acentuação |
| **Playground CSS (P33)** | Classes: `.region-card`, `.stat-badge`, `.score-radar`, `.risk-table`, `.pricing-grid`, `.timeline-horizontal`, `.persona-card` |
