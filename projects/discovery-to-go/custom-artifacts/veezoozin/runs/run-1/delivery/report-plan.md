---
title: "Report Plan — Veezoozin"
project-name: veezoozin
version: 01.00.000
status: gerado
author: report-planner
category: delivery
created: 2026-04-11
source: delivery-report.md
blueprint: saas + ai-ml + datalake-ingestion
report-setup: executive
total-regions: 24
chart-js-required: true
---

# Report Plan — Veezoozin

> Plano de renderizacao visual para os 2 HTMLs do setup **executive**.
> Fonte: `delivery-report.md` (24 regions) | Blueprint: saas + ai-ml + datalake-ingestion

## Resumo de Outputs

| Arquivo | Regions | Descricao |
|---------|---------|-----------|
| `one-pager.html` | 8 | Pagina unica executiva — overview, escopo, problema, TCO, riscos, decisao, esforco, proximos passos |
| `executive-report.html` | 20 | Relatorio corporativo completo — produto, organizacao, financeiro, riscos, qualidade, backlog, dominio, narrativa |

## Cobertura vs Executive Setup

| Status | Qtd | Regions |
|--------|-----|---------|
| Presentes no delivery e no setup | 22 | REG-EXEC-01, REG-EXEC-02, REG-EXEC-03, REG-EXEC-04, REG-PROD-01, REG-PROD-02, REG-PROD-04, REG-PROD-05, REG-PROD-06, REG-PROD-07, REG-PROD-08, REG-ORG-01, REG-ORG-02, REG-FIN-01, REG-FIN-05, REG-RISK-01, REG-RISK-03, REG-QUAL-01, REG-QUAL-02, REG-BACK-01, REG-NARR-01, REG-METR-01 |
| Ausentes no delivery (setup pedia) | 2 | REG-ORG-04 (Metodologia), REG-FIN-02 (Break-even analysis) |
| Extras no delivery (fora do setup) | 2 | REG-DOM-SAAS-01, REG-DOM-AIML-01 |

> **Nota:** REG-ORG-04 e REG-FIN-02 nao foram produzidos pelo discovery nesta iteracao. REG-DOM-SAAS-01 e REG-DOM-AIML-01 sao regions domain-specific do blueprint `saas + ai-ml` — o setup executive exclui regions `REG-DOM-*`, porem o consolidator os incluiu por relevancia ao projeto. **Decisao: incluir ambos no executive-report.html** como secao bonus "Dominio Especifico", dado que contem pricing e pipeline AI — informacoes criticas para a audiencia executiva.

---

## Tabela Geral — Plano por Region

| # | Region | HTML | Secao | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|------|-------|--------|-------------|------------|-------------|
| 1 | REG-EXEC-01 | one-pager | Overview | full-width | Hero card com callouts | HTML/CSS | Card escuro com metricas destacadas: TCO $1.63M, Recomendacao BUILD, Top 3 riscos como callout badges. Fundo gradiente escuro, texto branco, callouts em amarelo/vermelho |
| 2 | REG-PROD-07 | one-pager | Escopo | full-width | Tabela split In/Out | HTML/CSS | Duas colunas lado a lado: esquerda "Dentro" (verde), direita "Fora" (cinza). Items como chips/tags. Cortes sugeridos como linha separada com badge "10th-man" |
| 3 | REG-PROD-01 | one-pager | Problema | full-width | Tabela de 4 dimensoes + Impacto | HTML/CSS | Grid 2x2 com cards de dimensao (Barreira tecnica, Falta de contexto, Dados sem insight, Barreira linguistica). Cada card com icone, descricao e impacto. Abaixo: tabela Antes/Depois com setas |
| 4 | REG-FIN-01 | one-pager | TCO | full-width | Stacked bar chart | Chart.js | Chart.js stacked bar — 3 barras (Ano 1, 2, 3), 5 categorias: Equipe, LLM APIs, Infra GCP, Servicos Aux., Licenciamento. Cores: azul, roxo, verde, laranja, cinza. Label com total por ano. Legenda abaixo. Tooltip com valores e percentuais |
| 5 | REG-RISK-01 | one-pager | Riscos | full-width | Tabela com severity badges | HTML/CSS | Tabela compacta com Top 5 riscos criticos. Colunas: #, Risco, Prob., Impacto, Mitigacao. Badges de severidade: Critico (vermelho), Alto (laranja), Medio (amarelo). Hover com descricao completa |
| 6 | REG-EXEC-03 | one-pager | Go/No-Go | full-width | Status badges + radar 4 eixos | Chart.js | Parte superior: badge grande "GO CONDICIONAL" (amarelo/dourado). Abaixo: radar Chart.js com 4 eixos (Produto, Financeiro, Tecnico, Compliance), valores derivados dos scores do auditor e 10th-man. Ao lado: lista de 6 condicoes obrigatorias com checkboxes visuais |
| 7 | REG-FIN-05 | one-pager | Esforco | full-width | Tabela compacta | HTML/CSS | Tabela com colunas: Componente, Decisao Build/Buy, Custo Impl., Custo Op./ano. Linhas zebradas. Totais em negrito. Badge Build (azul), Buy (verde), Hibrido (roxo) |
| 8 | REG-EXEC-04 | one-pager | Proximos Passos | full-width | Timeline vertical compacta | HTML/CSS | 3 grupos visuais: "Esta semana" (4 itens), "Proximas 2 semanas" (4 itens), "Antes do Go-Live" (6 itens). Cada item com numero, acao, responsavel. Grupos com cor progressiva: verde, amarelo, vermelho |

---

## Plano Detalhado — executive-report.html

### Secao 1 — Produto e Valor

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 9 | REG-EXEC-02 | full-width | Product brief card | HTML/CSS | Card com header (nome, empresa, tipo, maturidade), body com visao e posicionamento, tabela de diferenciais competitivos com checkmarks verde (Veezoozin) e X vermelho (concorrentes). Stack obrigatoria como badges |
| 10 | REG-PROD-04 | full-width | Value proposition canvas | HTML/CSS | Tabela estilizada com 6 linhas (dimensoes). Colunas: Dimensao, Estado Atual (cinza), Estado Futuro (verde), Metrica-alvo. Abaixo: tabela de concorrentes com colunas Limitacao vs Veezoozin |
| 11 | REG-PROD-02 | grid-2 | Persona cards | HTML/CSS | Grid 2 colunas. 4 cards (Renata P0, Lucas P0, Diego P1, Camila P1). Cada card: avatar placeholder com iniciais, cargo, nivel tecnico (badge), JTBD, dor critica (vermelho), ganho principal (verde). P0 com borda azul, P1 com borda cinza |
| 12 | REG-PROD-05 | full-width | OKRs + ROI table | HTML/CSS | 3 blocos de OKR (cards com header colorido: OKR1 azul, OKR2 verde, OKR3 roxo), cada um com KRs em lista. Abaixo: tabela ROI com colunas Indicador e Valor. Callout de atencao sobre divergencia 1.3 vs 1.8 |
| 13 | REG-PROD-06 | full-width | Pricing table | HTML/CSS | 4 colunas de pricing (Free, Starter, Business, Enterprise). Cada coluna: nome, preco destacado, features como lista com checkmarks. Enterprise com badge "Mais popular" ou highlight. Abaixo: notas de estrategia e alertas do 10th-man |

### Secao 2 — Organizacao

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 14 | REG-ORG-01 | full-width | Stakeholder matrix | HTML/CSS | Tabela estilizada com colunas: Stakeholder, Poder, Interesse, Estrategia, Comunicacao. Badges para Poder/Interesse (Alto=vermelho, Medio=amarelo, Baixo=verde). Abaixo: RACI simplificado como tabela com icones R/A/C/I |
| 15 | REG-ORG-02 | full-width | Team composition cards | HTML/CSS | Tabela principal com colunas: Papel, Qtd, Dedicacao, Responsabilidades, Salario. Abaixo: timeline de contratacao com 3 faixas (Critica, Alta, Media). Evolucao do time como mini tabela Ano 1/2/3. Callout do 10th-man sobre prazo de contratacao |

### Secao 3 — Financeiro e Prazos

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 16 | REG-FIN-01 | full-width | Stacked bar chart + tabela | Chart.js | Reutiliza o chart do one-pager (stacked bar 5 categorias x 3 anos). Adiciona: tabela de premissas de crescimento, tabela Receita vs Custo com linha de resultado acumulado em destaque vermelho, tabela de divergencias 1.3 vs 1.8 com highlight |
| 17 | REG-FIN-05 | full-width | Tabela detalhada + sprint effort | HTML/CSS | Tabela Build vs Buy completa (5 componentes). Abaixo: tabela de esforco por sprint com barra de intensidade visual (cor proporcional ao esforco). Callout do 10th-man sobre timeline 16-20 semanas |
| 18 | REG-PROD-08 | full-width | Timeline horizontal | HTML/CSS | Timeline horizontal com 6 sprints do MVP (S1-S6) como blocos coloridos com semanas, foco e entregaveis. Abaixo: timeline pos-MVP com Fase 2, Fase 3, Escalabilidade, Enterprise como blocos progressivos. Cores do mais claro ao mais escuro |

### Secao 4 — Riscos e Decisao

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 19 | REG-RISK-01 | full-width | Tabela com severity badges | HTML/CSS | Tabela completa com 18 riscos em 3 grupos: Criticos (5), Altos (7), Medios (6). Colunas: #, Risco, Prob., Impacto, Fonte, Mitigacao. Severity badges: Critico (vermelho), Alto (laranja), Medio (amarelo). Linhas colapsaveis por grupo |
| 20 | REG-RISK-03 | full-width | Tabela + callout | HTML/CSS | Tabela de hipoteses com colunas: #, Hipotese, Fonte, Status (badge "Nao validada" vermelho), Acao de Validacao. Abaixo: tabela de perguntas residuais para CTO/Sponsor com badge de impacto |
| 21 | REG-BACK-01 | full-width | Tabela com priority badges | HTML/CSS | Tabela de 14 epicos com colunas: #, Epico, Prioridade (badge P0 vermelho, P1 azul, P2 cinza), Sprint, Justificativa. Agrupamento visual por sprint. Nota sobre candidatos a corte em destaque |
| 22 | REG-QUAL-01 | sidebar | Radar chart 5 eixos | Chart.js | Radar Chart.js com 5 eixos: Cobertura (90%), Profundidade (87%), Consistencia (72%), Fundamentacao (80%), Completude (83%). Preenchimento semi-transparente azul. Label central: "82%". Ao lado: tabela de score por bloco com barras de progresso horizontais. Forcas/Fraquezas como listas |
| 23 | REG-QUAL-02 | full-width | Tabela + summary cards | HTML/CSS | Header com badge "62% — Aprovado com Ressalvas". 3 cards de dimensao (Divergencia 55%, Robustez 60%, Completude 73%). Tabela das 10 QH com colunas: QH, Tema, Avaliacao (badge REJEITADA/Aceita/Parcial). Tabela de 14 pontos cegos com severidade. Tabela de 6 MON com prazo |

### Secao 5 — Narrativa

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 24 | REG-NARR-01 | full-width | Timeline + info cards | HTML/CSS | Timeline vertical com 2 fases (Discovery 8 blocos, Challenge 2 blocos). Cada fase com card descritivo. Tabela de veredictos com badges (82% verde, 62% amarelo). Tabela de maturidade da informacao com barras proporcionais (55% BRIEFING, 40% INFERENCE, 5% RAG). Callout de alerta sobre 40% inferencias |
| 25 | REG-EXEC-03 | full-width | Go/No-Go detalhado | Chart.js | Radar Chart.js com 4 eixos (Produto, Financeiro, Tecnico, Compliance). Badge "GO CONDICIONAL" grande. Tabela de 6 condicoes obrigatorias com colunas: #, Condicao, Prazo, Owner. Tabela de criterios pos-benchmark: 4 linhas com badges (GO verde, GO COM AJUSTE amarelo, PIVOT laranja, NO-GO vermelho) |
| 26 | REG-EXEC-04 | full-width | Timeline vertical detalhada | HTML/CSS | 3 blocos temporais: Imediatos (4 acoes), Proximas 2 semanas (4 acoes), Antes do Go-Live (6 acoes). Cada acao com #, descricao, responsavel, resultado. Icones de urgencia por bloco |

### Secao 6 — Dominio Especifico (bonus)

| # | Region | Layout | Tipo visual | Tecnologia | Configuracao |
|---|--------|--------|-------------|------------|-------------|
| 27 | REG-DOM-SAAS-01 | full-width | Pricing table + margin analysis | HTML/CSS | Tabela de arquitetura multi-tenant (7 camadas com estrategia de isolamento). Tabela de billing por consumo (5 componentes com custo unitario). Tabela de margem por plano com barras de progresso (45%, 59%, 64%). Highlight na margem do Free como negativa |
| 28 | REG-DOM-AIML-01 | full-width | Pipeline stages card | HTML/CSS | Card com 4 modelos LLM (Gemini Flash, Claude Sonnet, Gemini Pro, Vertex Embeddings) com % de uso e custo. Pipeline de 6 fases como stepper horizontal: cada fase com nome, tecnologia e latencia. Barra de latencia total P95 (3-12.5s). Tabela de cache semantico (5 camadas) com TTL e economia. Callout do 10th-man sobre < 5s |

---

## Regras de Tecnologia

| Prioridade | Tecnologia | Quando usar |
|------------|-----------|-------------|
| 1 (preferida) | HTML/CSS | Tabelas, cards, badges, timelines, layouts estaticos |
| 2 | Chart.js | Dados quantitativos com 4+ categorias, radares, barras empilhadas |
| 3 | Card (HTML/CSS) | Agrupamentos visuais, personas, product brief |
| **Proibido** | Mermaid | Nunca — nao usar em nenhum contexto |

## Uso de Chart.js

| Region | Tipo de chart | Eixos/Categorias | Justificativa |
|--------|--------------|-----------------|---------------|
| REG-FIN-01 | Stacked bar | 3 barras x 5 categorias | TCO com 5 categorias de custo — ideal para comparacao proporcional |
| REG-QUAL-01 | Radar | 5 eixos (Cobertura, Profundidade, Consistencia, Fundamentacao, Completude) | Score multidimensional do auditor — radar e o padrao para quality scores |
| REG-EXEC-03 | Radar | 4 eixos (Produto, Financeiro, Tecnico, Compliance) | Decisao Go/No-Go com multiplas dimensoes — visualizacao equilibrada |

## Distribuicao Final

| HTML | Regions | Chart.js | HTML/CSS puro |
|------|---------|----------|---------------|
| `one-pager.html` | 8 | 2 (REG-FIN-01, REG-EXEC-03) | 6 |
| `executive-report.html` | 20 | 3 (REG-FIN-01, REG-QUAL-01, REG-EXEC-03) | 17 |
| **Total** | **28 posicoes (24 regions unicas)** | **3 regions com Chart.js** | **21 regions HTML/CSS** |

> **Nota:** REG-FIN-01, REG-EXEC-03, REG-EXEC-04 e REG-FIN-05 aparecem em ambos os HTMLs — versao compacta no one-pager, versao completa no executive-report.

## Regions Ausentes (nao produzidas pelo discovery)

| Region | Descricao no setup | Acao |
|--------|-------------------|------|
| REG-ORG-04 | Metodologia (se definida) | Omitir — nao ha dados. Nota de rodape no HTML |
| REG-FIN-02 | Break-even analysis (se aplicavel) | Omitir — dados de break-even estao incorporados em REG-FIN-01 e REG-PROD-05 |

## Region Extra (nao prevista no setup)

| Region | Descricao | Acao |
|--------|-----------|------|
| REG-METR-01 | KPIs de Negocio (North Star, Ativacao, Engajamento, Retencao, Qualidade, Financeiro) | Incluir no executive-report.html, Secao 1 (Produto e Valor), apos REG-PROD-05. Layout: full-width, tabelas agrupadas por categoria com badges de meta |
