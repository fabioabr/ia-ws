---
title: "Report Plan — Veezoozin"
project-name: veezoozin
version: 02.00.000
status: gerado
author: report-planner
category: delivery
created: 2026-04-12
source: delivery-report.md
blueprint: saas + ai-ml + datalake-ingestion
report-setup: executive
total-regions: 26
chart-js-required: true
run: run-2
---

# Report Plan — Veezoozin

> Plano de renderizacao visual para os 2 HTMLs do setup **executive**.
> Fonte: `delivery-report.md` (26 regions) | Blueprint: saas + ai-ml + datalake-ingestion | Run: run-2

## Resumo de Outputs

| Arquivo | Regions | Descricao |
|---------|:-------:|-----------|
| `one-pager.html` | 8 | Pagina unica executiva — overview, problema, TCO, cenarios, riscos, Go/No-Go, esforco, proximos passos |
| `executive-report.html` | 22 | Relatorio corporativo completo — produto, organizacao, financeiro, cenarios, riscos, qualidade, backlog, glossario |

## Regras de Renderizacao

| Regra | Descricao |
|-------|-----------|
| **P13/P15 — Sem SVG inline** | Nenhum diagrama SVG embutido no HTML. Diagramas de arquitetura como placeholder com descricao textual |
| **P17 — 10th-man layout** | Secao do 10th-man segue o mesmo layout da secao do auditor (cards com badges, mesma estrutura visual) |
| **P18 — Radar com zonas** | Radar charts incluem zonas coloridas: verde (>=80%), amarelo (60-79%), vermelho (<60%) |
| **P12 — Glossario** | Secao de glossario renderizada como tabela estilizada ao final do executive-report |
| **P22 — Cenarios financeiros** | Cenarios alternativos de viabilidade como grouped bar chart (nao stacked) |

---

## Cobertura vs Executive Setup

| Status | Qtd | Regions |
|--------|:---:|---------|
| Presentes no delivery e no setup | 24 | REG-EXEC-01 a 05, REG-PROD-01/02/04/05/06/07, REG-ORG-01/02, REG-TECH-01/02/03, REG-SEC-01, REG-PRIV-01, REG-FIN-01/05/07, REG-RISK-01, REG-QUAL-01/02, REG-BACK-01 |
| Extras no delivery (fora do setup) | 2 | REG-EXEC-05 (Decisoes), REG-GLOSS-01 (Glossario) |

> **Nota:** REG-EXEC-05 e REG-GLOSS-01 foram adicionados pelo consolidator por relevancia. REG-EXEC-05 consolida as 56 decisoes. REG-GLOSS-01 atende P12 (glossario planejado). Ambos incluidos no executive-report.html.

---

## Tabela Geral — Plano por Region

### one-pager.html (8 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 1 | REG-EXEC-01 | full-width | Hero card com callouts + banner danger | HTML/CSS | Banner vermelho no topo: flags [BELOW-THRESHOLD] e [VIABILIDADE-NEGATIVA] com scores e deficit. Card escuro com metricas destacadas: TCO R$ 10,5M, Receita R$ 2,4M (base) a R$ 7,0M (cenario D), Break-even mes ~24 (D), Score Auditor 71,4%, Score 10th-man 57,8%. Fundo gradiente escuro, texto branco, callouts em vermelho (deficit) e amarelo (condicional). Badge "GO CONDICIONAL" em amarelo/dourado |
| 2 | REG-PROD-01 | full-width | Grid 2x2 de cards dimensionais | HTML/CSS | Grid 2x2 com 4 cards: Barreira tecnica, Falta de contexto, Dados sem insight, Multi-idioma. Cada card com icone (flaticon), descricao e impacto. Abaixo: tabela Antes/Depois com setas (dias → segundos, 5% → 100%, -80% tickets) |
| 3 | REG-FIN-01 | full-width | Stacked bar chart (TCO) | Chart.js | Chart.js stacked bar — 3 barras (Ano 1, 2, 3), 5 categorias: Equipe (azul), LLM APIs (roxo), Marketing (verde), Infra GCP (laranja), SaaS (cinza). Label com total por ano. Legenda abaixo. Tooltip com valores e percentuais. Linha pontilhada sobreposta mostrando receita acumulada (cenario base) para visualizar o gap |
| 4 | REG-FIN-07 | full-width | Grouped bar chart (cenarios) | Chart.js | Chart.js grouped bar — 5 grupos (Base, A, B, C, D), 2 barras por grupo: Receita (verde) e TCO (vermelho). Eixo Y em milhoes de R$. Label com cobertura %. Cenario D destacado com borda dourada. Abaixo: tabela compacta com gatilhos Go/No-Go |
| 5 | REG-RISK-01 | full-width | Tabela com severity badges | HTML/CSS | Tabela compacta com Top 10 riscos. Colunas: #, Risco, Prob., Impacto, Fonte, Mitigacao. Badges: Critico (vermelho), Alto (laranja), Medio (amarelo). Hover com descricao completa |
| 6 | REG-EXEC-03 | full-width | Banner Go/No-Go + radar chart com zonas | Chart.js + HTML/CSS | Parte superior: badge grande "GO CONDICIONAL" (amarelo/dourado). Abaixo: radar Chart.js com 5 eixos (Produto, Financeiro, Tecnico, Privacidade, Mercado). Zonas: verde (>=80%), amarelo (60-79%), vermelho (<60%). Valores derivados: Produto 78%, Financeiro 35%, Tecnico 85%, Privacidade 72%, Mercado 40%. Ao lado: lista de 6 condicoes obrigatorias com checkboxes visuais (todas unchecked) |
| 7 | REG-FIN-05 | full-width | Tabela Build vs Buy com badges | HTML/CSS | Tabela com colunas: Componente, Decisao, Custo 3a, TTM, Justificativa. Badge BUILD (azul) e BUY (verde). Totais em negrito |
| 8 | REG-EXEC-04 | full-width | Timeline vertical com prioridades | HTML/CSS | 3 grupos: "Bloqueante" (3 itens — vermelho), "Antes do Dev" (3 itens — amarelo), "Durante Dev" (2 itens — verde). Cada item com numero, acao, responsavel, prazo |

---

### executive-report.html (22 regions)

#### Secao 1 — Produto e Valor

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 9 | REG-EXEC-02 | full-width | Product brief card | HTML/CSS | Card com header (nome, empresa, tipo, maturidade, templates), body com visao e posicionamento. Tabela key-value estilizada com 10 campos. Flags [BELOW-THRESHOLD] e [VIABILIDADE-NEGATIVA] como badges vermelhos no header |
| 10 | REG-PROD-04 | full-width | Value proposition + alertas 10th-man | HTML/CSS | Tabela de concorrentes com colunas Limitacao vs Veezoozin. Abaixo: callout amarelo com alertas do 10th-man sobre moat fragil. Moat real (efeito de rede de contexto) destacado em callout verde |
| 11 | REG-PROD-02 | grid-2 | Persona cards | HTML/CSS | Grid 2 colunas. 4 cards (Marina P0, Rafael P0, Lucas P1, Carla P1). Cada card: iniciais como avatar, cargo, frequencia, JTBD, dor critica (vermelho), ganho principal (verde). P0 com borda azul, P1 com borda cinza. Carla com badge "Poder de veto" em vermelho |
| 12 | REG-PROD-05 | full-width | OKRs cards + ROI table | HTML/CSS | 3 blocos de OKR (O1 azul, O2 verde, O3 roxo), cada um com KRs em lista com metricas e alvos. Abaixo: tabela ROI com colunas Cenario, Custo, Economia, ROI. Callout de atencao: "10th-man alerta: meta KR1.2 > 85% e ambiciosa, realista e > 75% no MVP" |
| 13 | REG-PROD-06 | full-width | Pricing table com alertas | HTML/CSS | 3 colunas de pricing (Free, Pro, Enterprise) com nome, preco, features como lista. Callout vermelho: "Conflito D11 vs D51 — pricing nao definido. Free e confirmado, Pro e Enterprise pendentes de resolucao." Badge de alerta no header "Em definicao" |
| 14 | REG-PROD-07 | full-width | Scope split + timeline | HTML/CSS | Duas colunas lado a lado: esquerda "Dentro" (verde), direita "Fora" (cinza). Items como chips/tags. Abaixo: roadmap horizontal com 3 fases (MVP, Fase 2, Fase 3) como blocos progressivos com semanas e escopo |

#### Secao 2 — Organizacao

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 15 | REG-ORG-01 | full-width | Team table + stakeholders | HTML/CSS | Tabela de time com colunas: Papel, Qtd, Senioridade, Custo/mes, Status. Badges de status (Existente=verde, A contratar=amarelo, Freelancer=azul). Abaixo: stakeholders com badges de poder de decisao. Callout 10th-man: bus factor critico |
| 16 | REG-ORG-02 | full-width | Metodologia + SLOs | HTML/CSS | Tabela de metodologia com 6 aspectos. Abaixo: tabela de SLOs por tier (Free/Pro/Enterprise) com 3 metricas. Badges de tier coloridos |

#### Secao 3 — Arquitetura Tecnica

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 17 | REG-TECH-01 | full-width | Stack table com badges | HTML/CSS | Tabela de 14 tecnologias com colunas: Camada, Tecnologia, Justificativa. Badges por tipo: Obrigatorio (vermelho), Inferido (amarelo), Open-source (azul). Agrupamento visual por camada (Cloud, Backend, Frontend, Dados, AI, Servicos) |
| 18 | REG-TECH-02 | full-width | Pipeline 8 etapas + alertas | HTML/CSS | Tabela de 8 etapas com colunas: #, Etapa, Responsabilidade, Latencia. Abaixo: descricao textual do cache de 4 camadas com economia projetada. Callout 10th-man: cache hit rate pode ser 15-20% (nao 35-50%). **Sem diagrama SVG** — placeholder textual para arquitetura do pipeline |
| 19 | REG-TECH-03 | full-width | Modulos do monolith + placeholder | HTML/CSS | Tabela de 7 modulos com colunas: Modulo, Responsabilidade, Fase. Abaixo: descricao textual da arquitetura modular monolith e justificativa. **Sem diagrama SVG** — card placeholder com descricao: "Modular Monolith: 6 modulos + Shared Kernel, deploy unico em Cloud Run" |

#### Secao 4 — Privacidade e Seguranca

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 20 | REG-SEC-01 | full-width | Security layers table | HTML/CSS | Tabela de 9 camadas de seguranca com badges. Abaixo: 3 controles especificos NL-to-SQL com badges de prioridade Alta |
| 21 | REG-PRIV-01 | full-width | LGPD card com alertas | HTML/CSS | Card com secoes: Modo (Profundo), Papeis (Controladora/Operadora), Sub-processadores (tabela com residencia), Classificacao (4 niveis com badges coloridos), Retencao (por plano), Pendencias (checklist com status). Callout danger: DPO — risco regulatorio, recomendacao de contratar antes do lancamento |

#### Secao 5 — Financeiro

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 22 | REG-FIN-01 | full-width | TCO stacked bar + receita + deficit | Chart.js + HTML/CSS | Reutiliza chart do one-pager (stacked bar 5 categorias x 3 anos). Adiciona: tabela de receita por periodo, callout vermelho com deficit R$ -8M, nota sobre inconsistencia breakeven 1.3 vs 1.8 |
| 23 | REG-FIN-05 | full-width | Build vs Buy table detalhada | HTML/CSS | Reutiliza tabela do one-pager com mais detalhe: 6 componentes completos |
| 24 | REG-FIN-07 | full-width | Cenarios grouped bar + gatilhos + investimento | Chart.js + HTML/CSS | Reutiliza grouped bar do one-pager. Adiciona: tabela completa de cenarios (7 metricas x 5 cenarios), tabela de gatilhos Go/No-Go (4 marcos), tabela de investimento necessario por fase. Callout 10th-man: stress-test do cenario D (se 2 premissas falharem, cobertura cai para ~34%) |

#### Secao 6 — Riscos e Qualidade

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 25 | REG-RISK-01 | full-width | Risk table completa | HTML/CSS | Reutiliza tabela do one-pager com 10 riscos completos |
| 26 | REG-QUAL-01 | sidebar | Radar chart 5 eixos com zonas | Chart.js | Chart.js radar com 5 eixos: Cobertura (85%), Profundidade (68%), Consistencia (78%), Fundamentacao (72%), Completude (55%). **Zonas coloridas (P18):** verde (>=80%), amarelo (60-79%), vermelho (<60%). Score global 71,4% como stat card ao lado. Abaixo: tabela de findings criticos (F1-F3) com badges |
| 27 | REG-QUAL-02 | full-width | 10th-man cards — **mesmo layout do auditor (P17)** | HTML/CSS + Chart.js | **Layout identico ao REG-QUAL-01:** Radar Chart.js com 3 eixos: Divergencia (45%), Robustez (60%), Completude Critica (70%). Zonas coloridas (P18). Score global 57,8% como stat card. Abaixo: 6 premissas desafiadas como cards com badges (Risco Alto/Medio/Baixo). 6 pontos cegos como lista com icones de alerta. Callout de modelo alternativo (open-core) |

#### Secao 7 — Backlog e Encerramento

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 28 | REG-BACK-01 | full-width | Sprint timeline horizontal | HTML/CSS | Timeline horizontal com 8 blocos de sprint (S1-S16) como blocos coloridos com semanas e foco. Cores do mais claro (Setup) ao mais escuro (Launch). Badge de fase em cada bloco |
| 29 | REG-EXEC-04 | full-width | Next steps timeline vertical | HTML/CSS | Reutiliza timeline do one-pager com mais detalhe |
| 30 | REG-EXEC-05 | full-width | Tabela de decisoes consolidada | HTML/CSS | Tabela com 14 decisoes-chave (D1-D56 selecionadas). Colunas: #, Decisao, Status. Badges: Confirmada (verde), Recomendacao (amarelo), Conflito (vermelho). D11/D51 com badge vermelho "Conflito" |
| 31 | REG-GLOSS-01 | full-width | Glossario estilizado (P12) | HTML/CSS | Tabela de 20 termos com colunas: Termo (negrito), Definicao. Alternancia de cores de fundo (zebra). Agrupamento alfabetico |

---

## Resumo Tecnico

| Metrica | Valor |
|---------|-------|
| **Total regions** | 26 (delivery) → 31 (com duplicacoes entre one-pager e executive) |
| **Chart.js regions** | 5 (REG-FIN-01, REG-FIN-07, REG-EXEC-03, REG-QUAL-01, REG-QUAL-02) |
| **HTML/CSS only regions** | 21 |
| **Layout full-width** | 24 |
| **Layout grid-2** | 1 (REG-PROD-02 — personas) |
| **Layout sidebar** | 1 (REG-QUAL-01 — radar auditor) |
| **SVG inline** | 0 (P13/P15 — sem SVG) |
| **Radar charts com zonas** | 3 (REG-EXEC-03, REG-QUAL-01, REG-QUAL-02) — todas com P18 |
| **Grouped bar chart** | 1 (REG-FIN-07 — cenarios) |
| **Stacked bar chart** | 1 (REG-FIN-01 — TCO) |
