---
title: "Report Plan — Veezoozin"
project-name: veezoozin
version: 01.00.000
status: gerado
author: report-planner
category: delivery
created: 2026-04-12
source: delivery-report.md
blueprint: saas-discovery-blueprint.md
total-regions: 37
chart-js-required: true
reports:
  - executive-report.html
  - one-pager.html
---

# Report Plan — Veezoozin

## Resumo

| Item | Valor |
|------|-------|
| Total de regions no delivery-report | 37 |
| Regions no Executive Report (Plan A) | 30 |
| Regions no One-Pager (Plan B) | 9 |
| Regions com Chart.js | 4 |
| Regions HTML/CSS puro | 29 |
| Regions card informativo | 4 |
| Layouts grid usados | full-width, grid-2, grid-3, sidebar |

### Regions encontradas no delivery-report.md

REG-EXEC-01, REG-EXEC-02, REG-EXEC-03, REG-EXEC-04, REG-EXEC-07, REG-PROD-01, REG-PROD-02, REG-PROD-04, REG-PROD-05, REG-PROD-06, REG-PROD-07, REG-PROD-08, REG-ORG-01, REG-ORG-02, REG-ORG-04, REG-FIN-01, REG-FIN-02, REG-FIN-04, REG-FIN-05, REG-FIN-06, REG-FIN-07, REG-RISK-01, REG-RISK-02, REG-RISK-03, REG-RISK-04, REG-QUAL-01, REG-QUAL-02, REG-BACK-01, REG-PLAN-01, REG-METR-01, REG-NARR-01, REG-EXEC-03, REG-EXEC-04, REG-TECH-06, REG-SEC-01, REG-SEC-02, REG-SEC-04, REG-PRIV-01, REG-NARR-04.

### Regions extras (além do setup executive padrão)

O delivery-report inclui regions adicionais que o setup executive padrão não prevê. Estas foram incorporadas ao plano nas abas temáticas mais adequadas:

| Region | Motivo da inclusão | Aba destino |
|--------|-------------------|-------------|
| REG-EXEC-07 | Premissas — sustentam as estimativas | Tab 5 (Backlog e Decisão) |
| REG-PROD-06 | Modelo de negócio — pricing e BYOK | Tab 1 (Produto) |
| REG-PROD-08 | Roadmap — faseamento MVP/Fase 2/Fase 3 | Tab 1 (Produto) |
| REG-FIN-04 | Projeção de receita 3 anos | Tab 3 (Financeiro) |
| REG-FIN-06 | Total de horas (stat cards) | Tab 3 (Financeiro) |
| REG-TECH-06 | Build vs Buy — decisão formal | Tab 6 (Domínio) |
| REG-SEC-01 | Classificação de dados | Tab 6 (Domínio) |
| REG-SEC-02 | Autenticação e autorização | Tab 6 (Domínio) |
| REG-SEC-04 | Compliance e regulação | Tab 6 (Domínio) |
| REG-RISK-02 | Riscos técnicos (7 itens detalhados) | Tab 4 (Riscos e Qualidade) |
| REG-RISK-04 | Análise de viabilidade (5 dimensões) | Tab 4 (Riscos e Qualidade) |
| REG-PRIV-01 | Dados pessoais e LGPD | Tab 6 (Domínio) |
| REG-NARR-04 | Glossário | Tab 7 (Glossário) |

---

## Plan A — Executive Report (`executive-report.html`)

Relatório executivo completo com 7 abas. Navegação por tabs no topo. Design dark theme com paleta do design system (primary #4DA8DA, success #0ED145, warning #F4AC00, danger #8B1A1A). Font: Poppins. Ícones: Remix Icon.

---

### Tab 1 — Produto (8 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-EXEC-02 | full-width | Card informativo com seções | HTML/CSS | Card com header "Product Brief". Seções: Visão do Produto (texto), Elevator Pitch (blockquote destaque, borda --primary), Problema (texto + lista numerada de 4 dores), Solução (texto), Usuário-alvo (texto), Resultado MVP (bullets com check), Investimento (stat inline TCO R$925.658 cor --primary), Recomendação (badge BUILD cor --success). Ícone: ri-lightbulb-line |
| 2 | REG-PROD-01 | full-width | Card com callout de métrica | HTML/CSS | Card "Problema e Contexto". Callout lateral: "2-5 dias → segundos" (stat destaque --primary). Seção "Quem Sofre" como tabela 3 colunas (Persona, Dor, Severidade) com badges de severidade (Crítica=--danger, Alta=--warning). Seção "Alternativas" como tabela comparativa 3 colunas com destaque na coluna "Veezoozin". Ícone: ri-search-eye-line |
| 3 | REG-PROD-04 | full-width | Card com destaque de pitch | HTML/CSS | Card "Proposta de Valor". Elevator pitch em blockquote grande com tipografia destaque. Tabela "Diferenciação" 3 colunas (Eixo, Veezoozin, Mercado) com check/X icons por célula. Seção "Princípios" como lista numerada com ícones. Seção "BYOK" como callout info (borda --info). Ícone: ri-trophy-line |
| 4 | REG-PROD-02 | grid-2 | Persona cards | HTML/CSS | 4 persona cards (Ana, Carlos, Daniel, Eduardo), 2 por linha. Cada card: nome + ícone de avatar (ri-user-line), função (subtítulo --text-muted), badge de frequência, JTBD em blockquote, Dores como lista com ri-close-circle-line (cor --danger), Ganhos como lista com ri-checkbox-circle-line (cor --success). Card de Ana e Carlos com borda --primary (primária/secundária). Card de Daniel e Eduardo com borda --secondary. Seção "Gaps" abaixo como alert-warning com tabela 3 colunas |
| 5 | REG-PROD-07 | full-width | Split card (IN/OUT) | HTML/CSS | Card "Escopo". Header com objetivo do projeto (1 frase destaque). Split horizontal 50/50: coluna esquerda "DENTRO DO ESCOPO" (fundo --success-light, borda --success-border, bullets com ri-checkbox-circle-line verde), coluna direita "FORA DO ESCOPO" (fundo --danger-light, borda --danger-border, bullets com ri-close-circle-line vermelho). Abaixo: "Hipótese Central" em blockquote --warning-light com ícone ri-alert-line. Tabela "Critérios Go/No-Go" (4 linhas × 3 colunas) |
| 6 | REG-PROD-05 | full-width | Tabelas OKR + stat cards ROI | HTML/CSS | 3 blocos OKR como accordion (OKR 1 expandido, 2-3 collapsed). Cada OKR: título + tabela com KRs. Seção "ROI Consolidado" como grid-3 de stat cards: (1) TCO 3 anos R$925.658 cor --danger, (2) Receita 3 anos R$1.015.500 cor --success, (3) ROI 9,7% cor --warning. Tabela detalhada ROI abaixo. Callout "Nota sobre ROI" como alert-warning |
| 7 | REG-PROD-06 | full-width | Pricing table + tabela de custos | HTML/CSS | Pricing table 3 colunas (Starter/Pro/Enterprise) com destaque no Pro (borda --primary, badge "POPULAR"). Cada coluna: preço grande, lista de features com checks. Seção "Custos Fixos" como tabela compacta. Seção "Custos Variáveis" como tabela compacta. Seção "ARPU e Margem" como grid-3 stat cards: ARPU R$857 (--primary), Custo R$70 (--secondary), Margem 92% (--success). Ícone: ri-money-dollar-circle-line |
| 8 | REG-PROD-08 | full-width | Timeline horizontal (fases) | HTML/CSS | Roadmap com 3 fases horizontais. Cada fase como barra horizontal colorida com largura proporcional: MVP (semanas 1-16, cor --primary, 55% width), Fase 2 (mês 5-8, cor --purple, 25% width), Fase 3 (mês 9-12+, cor --teal, 20% width). Dentro de cada barra: lista de features com prioridade. Sprint breakdown como tabela abaixo (Sprint, Semanas, Entrega, Requisitos). Ícone: ri-road-map-line |

---

### Tab 2 — Organização (3 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-ORG-01 | full-width | Tabela de stakeholders + card contexto | HTML/CSS | Tabela stakeholders com 7 colunas (Nome, Função, Decisão, Influência, Interesse, Disponibilidade, Engajamento). Nota apenas 1 stakeholder — card de observação abaixo em alert-info explicando a estrutura atípica de 1 pessoa. Seção "Contexto Organizacional" como tabela 2 colunas key-value. Ícone: ri-team-line |
| 2 | REG-ORG-02 | full-width | Tabela de equipe + cards de gaps | HTML/CSS | Tabela "Composição do Time" com 6 colunas (Papel, Quem, Dedicação, Horas/Semana, Fase, Observações). Destaque visual: toda linha mostra "Fabio" — visual emphasis que é 1 pessoa acumulando 9 papéis. Linha "Claude Code" com badge especial "IA Assistant" cor --purple. Seção "Skills" como tabela com badges de nível (Expert=--success, Avançado=--primary, Intermediário=--warning, Básico=--danger). Seção "Gaps" como grid-2 de alert cards (cada gap: título, severidade badge, mitigação MVP, mitigação pós-MVP). Seção "Triggers de Contratação" como tabela com 3 triggers. Ícone: ri-user-settings-line |
| 3 | REG-ORG-04 | full-width | Card informativo | HTML/CSS | Card "Metodologia" com tabela key-value 2 colunas (Aspecto, Decisão). Callout info: "Kanban pessoal — sem overhead de Scrum para equipe de 1". Ícone: ri-kanban-view-2 |

---

### Tab 3 — Financeiro (7 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-FIN-01 | full-width | Tabela TCO + barras horizontais empilhadas | HTML/CSS | Tabela completa TCO com 5 colunas (Categoria, Ano 1, Ano 2, Ano 3, Total). Agrupamento visual: Equipe (fundo --primary-light), Infra (fundo --info-light), Licenças (fundo --purple-light). Linha Total com contingência em destaque (fundo --warning-light, negrito). Abaixo: barras horizontais empilhadas (HTML/CSS) mostrando proporção Equipe/Infra/Licenças por ano. 3 barras (Ano 1, Ano 2, Ano 3), cada segmento colorido: Equipe=--primary, Infra=--info, Licenças=--purple, Contingência=--warning (pattern hatched). Label de valor à direita de cada barra. Total geral como stat card grande: R$925.658 cor --danger. Ícone: ri-funds-line |
| 2 | REG-FIN-02 | full-width | KPI card + tabela de projeção | HTML/CSS | Stat card destaque: "Break-even: 22-25 tenants (mês 14-18)" com ícone ri-scales-line, cor --warning. Fórmula de cálculo em monospace box. Tabela "Projeção de Crescimento" com 6 períodos × 6 colunas, badges de cor: Resultado negativo=--danger, positivo=--success. Tabela "Sensibilidade" com destaque na variável mais sensível (ARPU). Callout 10th-man como alert-danger. Ícone: ri-scales-line |
| 3 | REG-FIN-04 | full-width | Tabela de receita + chart de linha | Chart.js (line) | Tabela "Receita por Período" com 7 linhas e 7 colunas. Totais de ano em negrito. Chart.js line chart abaixo: eixo X = meses (agrupados por período: MVP, Early, Tração, Break-even, Crescimento, Escala), eixo Y = MRR (R$). Linha de receita cor --success. Linha horizontal tracejada de custo fixo mensal cor --danger (R$17K). Ponto de interseção destacado = break-even. Fill area entre as linhas: vermelho quando custo > receita, verde quando receita > custo. Tooltip com MRR e tenants. Seção "Premissas" como tabela com badges de risco. Seção "Cenário Pessimista" como alert-danger. Config Chart.js: `type: 'line', datasets: [{label: 'MRR', borderColor: '#0ED145', fill: false}, {label: 'Custo Fixo', borderColor: '#E85D54', borderDash: [5,5]}], scales: {y: {ticks: {callback: 'R$'}}}` |
| 4 | REG-FIN-05 | full-width | Tabela de esforço + barras horizontais | HTML/CSS | Tabela "T-Shirt Sizing por Épico" com 12 épicos × 5 colunas (Épico, Complexidade, Horas, Sprint, Premissas). Badges de complexidade: S=--success, M=--primary, L=--warning, XL=--danger. Abaixo: barras horizontais HTML/CSS por épico, largura proporcional às horas (máx 120h = 100% width). Cor das barras por sprint: S1-S2=--primary, S3-S5=--info, S6-S7=--purple, S8=--teal. Tabela "Resumo por Papel" com barras de progresso inline (% do total). Ícone: ri-timer-line |
| 5 | REG-FIN-06 | grid-3 | Stat cards | HTML/CSS | 6 stat cards em grid: (1) "Total MVP" 656h (card grande, cor --primary, ícone ri-time-line), (2) "Duração" 16 semanas (cor --info, ícone ri-calendar-line), (3) "Horas/Semana" ~41h (cor --warning, ícone ri-speed-line), (4) "Backend" 280h (cor --primary), (5) "Frontend" 160h (cor --purple), (6) "DevOps + Testes + Design" 216h (cor --teal). Cards 1-3 maiores (primeira linha), cards 4-6 menores (segunda linha) |
| 6 | REG-FIN-07 | full-width | Tabela comparativa de cenários + barras | HTML/CSS | Tabela "Cenários" com 4 cenários × 6 colunas. Badges de veredicto: Viável=--success, Inviável=--danger, "Viável Fase 2"=--warning. Cenário Base com destaque (borda --primary). Barras horizontais comparativas (HTML/CSS): 4 barras (uma por cenário) mostrando TCO vs Receita. Segmento TCO cor --danger, segmento Receita cor --success. Se Receita > TCO, barra de lucro em --success-light. Seção "Cenário A detalhado" como card com stat cards inline: ARPU R$1.197, Break-even 15 tenants, ROI 53%. Tabela "Sensibilidade" abaixo. Ícone: ri-line-chart-line |
| 7 | REG-PLAN-01 | full-width | Gantt relativo (barras horizontais) | HTML/CSS | Gantt chart HTML/CSS com grid de 16 semanas (eixo X). 12 barras horizontais (uma por épico), posicionadas por sprint. Cores por fase: Fundação (S1-S2)=--primary, Core (S3-S5)=--info, Output (S6-S7)=--purple, Polimento (S8)=--teal. Marcos como diamantes no eixo: M0 (S2), M1 (S4), M2 (S8, destaque --warning "DECISION POINT"), M3 (S14), M4 (S16, destaque --success "MVP LAUNCH"). Seção "Atividades Paralelas" como tabela abaixo do Gantt. Grid background com linhas verticais tracejadas a cada semana. Labels de épico à esquerda, duração à direita. Ícone: ri-bar-chart-horizontal-line |

---

### Tab 4 — Riscos e Qualidade (5 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-RISK-01 | full-width | Tabela de riscos com heatmap badges + detalhamento | HTML/CSS | Tabela "Top 10 Riscos" com 7 colunas. Badges de score: >= 8 = --danger, 6-7.9 = --warning, < 6 = --info. Badges de probabilidade: Alta = --danger, Média = --warning, Baixa = --success. Badges de categoria com cores distintas: Mercado=--orange, Regulatório=--purple, Organizacional=--teal, Execução=--info, Financeiro=--warning, Produto=--primary, Técnico=--secondary, Segurança=--danger, Comercial=--orange. Detalhamento dos 4 riscos críticos (R1, R2, R3, R10) como accordions expandíveis abaixo da tabela. Cada accordion: tabela key-value com campos (Descrição, Probabilidade, Impacto, Plano de Mitigação, Responsável, Timeline, Indicador, Custo). Ícone: ri-alarm-warning-line |
| 2 | REG-RISK-02 | full-width | Tabela de riscos técnicos com accordions | HTML/CSS | 7 riscos técnicos (RT1-RT7) como cards compactos empilhados. Cada card: título à esquerda, badges (Probabilidade + Impacto) à direita, barra de mitigação abaixo. Accordion expandível para cada risco com tabela key-value detalhada. Cor da borda por impacto: Crítico=--danger, Alto=--warning, Médio=--info. Ícone: ri-bug-line |
| 3 | REG-RISK-03 | full-width | Tabela de hipóteses + lista de perguntas | HTML/CSS | Tabela "Hipóteses Críticas" com 10 linhas × 6 colunas (Hipótese, Risco se Falsa, Como Validar, Prazo, Status). Todas com badge "NÃO VALIDADA" cor --danger. Seção "Perguntas Residuais" como lista numerada com ícone ri-question-line, cada pergunta em card compacto. Ícone: ri-question-answer-line |
| 4 | REG-QUAL-01 | sidebar (70/30) | Radar chart + tabelas | Chart.js (radar) | **Sidebar (30%):** Radar chart Chart.js com 5 dimensões (Completude, Fundamentação, Coerência, Profundidade, Neutralidade). Escala 0-100. Área fill cor --primary (opacity 0.2), borda --primary. Linha de threshold 90% tracejada cor --danger. Ponto de score real por dimensão. Config Chart.js: `type: 'radar', data: {labels: ['Completude','Fundamentação','Coerência','Profundidade','Neutralidade'], datasets: [{data: [90,75,90,78,100], backgroundColor: 'rgba(77,168,218,0.2)', borderColor: '#4DA8DA'}, {data: [90,90,90,90,90], borderColor: '#E85D54', borderDash: [3,3], pointRadius: 0}]}, options: {scales: {r: {max: 100, min: 0}}}`. **Conteúdo principal (70%):** Stat card grande "87,15%" cor --warning, badge "APROVADO COM RESSALVAS". Tabela de dimensões 6 colunas com cores: score >= piso = --success, score < piso = --danger. Tabela "Distribuição de tags" com sparkline de % inference por bloco (barras inline HTML/CSS, vermelho quando > 50%). 12 ressalvas como tabela compacta. Ícone: ri-shield-check-line |
| 5 | REG-RISK-04 | full-width | Tabela de viabilidade com badges | HTML/CSS | Tabela "Viabilidade por Dimensão" com 5 linhas × 4 colunas (Dimensão, Veredicto, Justificativa, Condição). Badges de veredicto: VIÁVEL=--success, VIÁVEL COM RESSALVAS=--warning, ALTO RISCO=--danger. Stat card final "VIÁVEL COM CONDIÇÕES" cor --warning, borda larga. Ícone: ri-checkbox-multiple-line |

---

### Tab 5 — Backlog e Decisão (5 regions)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-EXEC-07 | full-width | Tabela de premissas com alertas | HTML/CSS | Tabela "Premissas" com 12 linhas × 3 colunas (#, Premissa, Impacto se Falsa). Coluna "Impacto se Falsa" com cor de texto --danger. Premissas 1-5 (mais críticas) com borda esquerda --danger. Callout "Nota crítica do 10th-man" como alert-danger. Ícone: ri-error-warning-line |
| 2 | REG-BACK-01 | full-width | Tabela de épicos com MoSCoW badges | HTML/CSS | Tabela "Épicos MVP" com 12 linhas × 6 colunas. Badges MoSCoW: MUST=--danger, SHOULD=--warning. Barras de estimativa inline (largura proporcional às horas). Seções Fase 2 e Fase 3 como tabelas colapsáveis. Seção "User Stories" como accordion por épico (E1, E4, E6, E7, E11 expandíveis). Seção "Requisitos Mandatórios vs Desejáveis" como duas tabelas (Mandatórios com badges verdes, Desejáveis com badges azuis, Opcionais com badges cinza). Tabela "Dependências" com setas visuais (De → Para). Ícone: ri-list-check-3 |
| 3 | REG-QUAL-02 | full-width | Score card + tabela de ressalvas | HTML/CSS | Stat card "10th-man: 41,85%" cor --danger, badge "REJEITADO". Tabela de floors 3 linhas com badges "VIOLADO" cor --danger. Blockquote do diagnóstico. Tabela "10 Ressalvas" com badges de severidade: CRITICAL=--danger, IMPORTANT=--warning. Seção "Recomendações Prioritárias" como lista numerada em alert-info. Ícone: ri-spy-line |
| 4 | REG-EXEC-03 | full-width | Card de decisão com badges por dimensão | HTML/CSS | Grid-2 de stat cards: (1) "Value" ALTO RISCO badge --danger, (2) "Usability" MÉDIO RISCO badge --warning, (3) "Feasibility" MÉDIO RISCO badge --warning, (4) "Viability" ALTO RISCO badge --danger. Seção "Recomendação" como card com texto "AVANÇAR COM CONDIÇÕES" em destaque --warning. Lista numerada de condições obrigatórias com checks. Seção "Runway" como tabela de 10 períodos com burn acumulado em --danger. Stat card "Capital necessário: ~R$190K-R$250K" cor --warning. Tabela "Critérios Decision Point" com 3 colunas (GO=--success, CAUTION=--warning, NO-GO=--danger). Ícone: ri-compass-3-line |
| 5 | REG-EXEC-04 | full-width | Tabela de próximos passos + decisões pendentes | HTML/CSS | Tabela "Ações Imediatas" com 10 linhas × 6 colunas. Badges de prioridade: Crítica=--danger, Alta=--warning. Destaque visual nas ações de custo R$0. Tabela "Decisões Pendentes" com 6 linhas × 4 colunas (Decisão, Quem, Quando, Impacto). Ícone: ri-route-line |

---

### Tab 6 — Domínio: Segurança, Privacidade e Tecnologia (5 regions)

> **Nota:** O Veezoozin tem context-templates `saas`, `ai-ml` e `datalake-ingestion`, mas nenhuma region REG-DOM-* foi gerada no delivery-report (provavelmente absorvidas nos blocos temáticos). As regions de segurança, privacidade e Build vs Buy foram agrupadas aqui como conteúdo de domínio técnico.

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-TECH-06 | full-width | Tabela comparativa Build vs Buy | HTML/CSS | Card "Decisão: BUILD" com stat card "Score 8,8/10" cor --success, badge "RECOMENDADA". 4 alternativas como cards colapsáveis (Build expandido, demais collapsed). Cada alternativa: tabela key-value (Descrição, Prós, Contras, TCO, Mandatórios). Tabela "Scoring Comparativo" 6 critérios × 4 alternativas com barras horizontais inline (pontuação proporcional). Destaque na coluna Build (fundo --success-light). Seção "Por que Buy não funciona" como callout --info. Ícone: ri-hammer-line |
| 2 | REG-SEC-01 | full-width | Tabela de classificação de dados + fluxo | HTML/CSS | Tabela "Inventário de Dados" com 9 linhas × 6 colunas. Badges de classificação: Público=--success, Interno=--info, Confidencial=--warning, Restrito=--danger. Seção "Fluxo de Dados Sensíveis" como diagrama vertical HTML/CSS (boxes conectados por setas, pontos críticos destacados com borda --danger e label "PONTO CRÍTICO"). Tabela "Tratamento por Classificação" com 4 colunas. Ícone: ri-database-2-line |
| 3 | REG-SEC-02 | full-width | Cards de auth + tabela RBAC | HTML/CSS | Card "Autenticação" com tabela key-value 3 colunas (Aspecto, Decisão, Justificativa). Badge "Firebase Auth" cor --primary. Card "Autorização" com tabela RBAC 4 roles × 3 colunas (Role, Permissões, Quem). Badges por role: admin-plataforma=--danger, admin-tenant=--warning, user=--primary, viewer=--secondary. Callout sobre isolamento multi-tenant em alert-info. Ícone: ri-shield-keyhole-line |
| 4 | REG-SEC-04 | full-width | Tabela de compliance + tabela de bases legais | HTML/CSS | Tabela "Regulamentações" com 5 linhas × 5 colunas. Badges de status: Parcial=--warning, N/A=--secondary. Tabela "Bases Legais LGPD" com 7 linhas × 4 colunas, todas com label "[INFERIDO]" cor --warning. Callout "Transferência Internacional" como alert-danger com texto sobre art. 33 LGPD. Tabela "Sub-operadores" com 5 linhas × 5 colunas, badges de DPA status. Ícone: ri-government-line |
| 5 | REG-PRIV-01 | full-width | Tabela de dados pessoais + timeline de incidentes | HTML/CSS | Card explicativo "Papel duplo: Controlador + Operador" com diagrama 2 boxes lado a lado. Tabela "Mapeamento de Dados Pessoais" com 8 linhas × 6 colunas (Dado, Titular, Controlador, Base Legal, Volume, Retenção). Tabela "Direitos do Titular" com 6 linhas × 5 colunas, badges Automatizado: Sim=--success, Parcial=--warning, Não=--danger. Tabela "Retenção e Descarte" com 6 linhas × 4 colunas. Seção "DPIA" como alert-warning "A REALIZAR". Seção "Plano de Incidentes" como timeline vertical HTML/CSS com 7 fases (Detecção → Contenção → Investigação → Notificação → Comunicação → Remediação → Post-mortem). Cada fase com prazo e cor: < 1h=--success, < 24h=--warning, < 72h=--danger. Seção "Pseudonimização" como card com diagrama de 4 passos + callout 10th-man alert-danger. Ícone: ri-user-unfollow-line |

---

### Tab 7 — Glossário (1 region)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-NARR-04 | full-width | Tabela de glossário + tabela de siglas | HTML/CSS | Tabela "Glossário" com 2 colunas (Termo, Definição), ~37 termos. Termos em negrito, definição em texto normal. Zebra striping para legibilidade. Tabela "Siglas e Acrônimos" separada abaixo com 2 colunas (Sigla, Significado), ~25 siglas. Ambas as tabelas com busca/filtro inline (input text no topo que filtra linhas). Ícone: ri-book-2-line |

---

### Region adicional — Header do Executive Report

Não é uma region do delivery-report, mas o html-writer deve renderizar como hero section:

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 0 | REG-NARR-01 | full-width | Timeline do discovery (hero) | HTML/CSS | Timeline horizontal HTML/CSS com 3 marcos: "Briefing" (início), "Fase 1 — Discovery (8 blocos)" (meio), "Fase 2 — Challenge (auditor + 10th-man)" (fim). Texto narrativo abaixo. Tabela "O que Mudou" com 10 linhas × 3 colunas (Aspecto, Briefing, Após Discovery), destaque nas diferenças. Este conteúdo aparece como primeira seção ao abrir o relatório, ANTES das tabs, como contexto narrativo. Ícone: ri-history-line |

---

## Plan B — One-Pager (`one-pager.html`)

Página única contínua, SEM tabs. 8 seções em scroll vertical. Design compacto e orientado a decisão. Mesmo design system (dark theme, Poppins, Remix Icon). Formato de orçamento/proposta.

Lógica da ordem: **o quê** (1-2) → **sob quais condições e riscos** (3-4) → **quem e quanto** (5-6) → **quando** (7) → **quão confiável** (8).

---

### Seção 1 — Descritivo (REG-EXEC-01 simplificado)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 1 | REG-EXEC-01 | full-width | Card informativo compacto | HTML/CSS | Card com 4 campos: **Projeto:** "Veezoozin — Plataforma SaaS de consulta em linguagem natural para BigQuery". **Cliente:** "mAInd Tech (startup de tecnologia, produto próprio)". **Objetivo:** "Construir e lançar MVP em 16 semanas — converter perguntas humanas em queries SQL contextualizadas, retornando gráficos e insights em segundos." **Contexto:** 2-3 frases sobre problema + solução proposta + BYOK + 1 dev. Omitir: TCO, riscos, recomendação (vão em seções próprias). Borda --primary, ícone ri-information-line. Sem tabela de números |

---

### Seção 2 — Escopo (REG-PROD-07 simplificado)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 2 | REG-PROD-07 | full-width | Split card (IN verde / OUT vermelho) | HTML/CSS | Split horizontal 50/50. Coluna esquerda "DENTRO" com fundo --success-light, borda --success-border, ícone ri-checkbox-circle-line. Bullets das features do MVP: NL-to-SQL, multi-idioma, BYOK, gráficos, BigQuery, 3 planos Stripe, multi-tenant. Coluna direita "FORA" com fundo --danger-light, borda --danger-border, ícone ri-close-circle-line. Bullets do que NÃO será feito: escrita, fine-tuning, ETL, app mobile, MCP/RAG, relatórios PDF, plano Free, outros bancos, SSO. Omitir: hipótese central, critérios go/no-go |

---

### Seção 3 — Premissas (REG-EXEC-07)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 3 | REG-EXEC-07 | full-width | Lista de premissas com ícones de atenção | HTML/CSS | Lista de 12 premissas como bullets com ícone ri-alert-line cor --warning antes de cada item. Texto da premissa em negrito, impacto em texto normal --text-muted abaixo. Nota de rodapé: "Se qualquer premissa mudar, as estimativas precisam ser recalculadas" em alert-warning. Compacto — sem tabela completa, apenas premissa + impacto em 1 linha |

---

### Seção 4 — Riscos Principais (REG-RISK-01 compacto)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 4 | REG-RISK-01 | full-width | Tabela compacta com severity badges | HTML/CSS | Tabela compacta com top 5 riscos (R1, R2, R3, R10, R4) × 3 colunas: Risco (texto curto), Impacto no Prazo (texto curto), Severidade (badge: CRÍTICA=--danger, ALTA=--warning). Omitir: probabilidade numérica, mitigação detalhada, dono. Foco em: o que pode dar errado e como afeta prazo/custo. Limite de 5 linhas |

---

### Seção 5 — Equipe e Papéis (REG-ORG-02 adaptado)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 5 | REG-ORG-02 | full-width | Tabela de equipe compacta | HTML/CSS | Tabela com 4 colunas: Papel, Quem, Dedicação, Horas/Semana. 9 linhas (9 papéis de Fabio + 1 linha Claude Code). Destaque visual: todas as linhas de "Quem" mostram "Fabio" para enfatizar que é 1 pessoa. Linha Claude Code com badge "IA" cor --purple. Linha total no rodapé: "Total: 40h/semana × 16 semanas = 640h" |

---

### Seção 6 — Estimativa de Esforço (REG-FIN-06)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 6 | REG-FIN-06 | grid-3 | Stat cards | HTML/CSS | Grid de 6 stat cards (2 linhas × 3 colunas). Primeira linha (cards grandes): (1) "Total MVP" **656h** cor --primary ícone ri-time-line, (2) "Duração" **16 semanas** cor --info ícone ri-calendar-line, (3) "Horas/Semana" **~41h** cor --warning ícone ri-speed-line. Segunda linha (cards menores): (4) "Backend" **280h** cor --primary, (5) "Frontend" **160h** cor --purple, (6) "DevOps+Testes+UX" **216h** cor --teal |

---

### Seção 7 — Planejamento (REG-PLAN-01)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 7 | REG-PLAN-01 | full-width | Gantt relativo com barras horizontais | HTML/CSS | Gantt HTML/CSS com eixo X em semanas (Semana 1, 2, ..., 16). 12 barras horizontais (uma por épico E1-E12). Cores por fase: Fundação=--primary, Core=--info, Output=--purple, Polimento=--teal. 2 marcos em destaque: "Walking Skeleton (S8)" como diamante --warning, "MVP Launch (S16)" como diamante --success. Labels de épico à esquerda (nome curto). Sem tabela de atividades paralelas (compacto). Grid background sutil. Responsivo |

---

### Seção 8 — Confiança dos Auditores IA (REG-QUAL-01 + REG-QUAL-02 compacto)

| # | Region | Layout | Tipo visual | Tecnologia | Configuração |
|---|--------|--------|-------------|-----------|--------------|
| 8a | REG-QUAL-01 | grid-2 (50/50) | Stat card auditor | HTML/CSS | Stat card: "Auditor: **87,15%**", subtítulo "APROVADO COM RESSALVAS", badge --warning. Abaixo: "Threshold: 90% (modo simulação)". Sem radar, sem tabela de dimensões |
| 8b | REG-QUAL-02 | grid-2 (50/50) | Stat card 10th-man | HTML/CSS | Stat card: "10th-man: **41,85%**", subtítulo "REJEITADO", badge --danger. Abaixo: "6 questões CRÍTICAS, 4 IMPORTANTES". Sem tabela de ressalvas |

**Nota de rodapé do One-Pager:** "Material gerado com 54% de dados do briefing, 46% inferidos pelo especialista. Iteração 1 do discovery pipeline v0.5."

---

## Especificações Técnicas Globais

### Chart.js — Configurações compartilhadas

```javascript
// Registrar apenas os componentes necessários
// Chart.js v4.4.7+ via CDN

const chartDefaults = {
    font: { family: 'Poppins', size: 12 },
    color: '#E0DFE3',           // --text
    backgroundColor: '#2E2D32',  // --card-bg
    plugins: {
        legend: {
            labels: { color: '#E0DFE3', font: { family: 'Poppins' } }
        },
        tooltip: {
            backgroundColor: '#1A1923',
            titleColor: '#E0DFE3',
            bodyColor: '#B9B7BD',
            borderColor: '#3E3D44',
            borderWidth: 1
        }
    },
    scales: {
        r: { // radar
            grid: { color: '#3E3D44' },
            angleLines: { color: '#3E3D44' },
            pointLabels: { color: '#E0DFE3', font: { family: 'Poppins', size: 11 } },
            ticks: { color: '#88878C', backdropColor: 'transparent' }
        }
    }
};
```

### Charts no plano

| # | Region | Tipo Chart.js | Justificativa (por que não HTML/CSS) |
|---|--------|--------------|--------------------------------------|
| 1 | REG-FIN-04 | Line chart | Tendência de MRR vs custo fixo ao longo de 36 meses — HTML/CSS não representa tendências com áreas de fill |
| 2 | REG-QUAL-01 | Radar chart | 5 dimensões de qualidade em pattern multi-dimensional — HTML/CSS não comunica o padrão geral |

> Total Chart.js: 2 charts (apenas no Executive Report). O One-Pager não usa Chart.js.

### Paleta de cores

| Token | Valor | Uso no plano |
|-------|-------|-------------|
| --primary | #4DA8DA | Destaques principais, bordas ativas, labels |
| --success | #0ED145 | Badges GO, viável, check, aprovado, IN do escopo |
| --warning | #F4AC00 | Badges caution, ressalvas, risco médio, premissas |
| --danger | #8B1A1A (dark) / #E85D54 (text) | Badges NO-GO, crítico, rejeitado, OUT do escopo |
| --info | #2EB5F5 | Callouts informativos, infra, core |
| --purple | #9B96FF | IA/Claude Code, frontend, output, Fase 2 |
| --teal | #2DD4BF | Polimento, Fase 3, DevOps |
| --orange | #FF9473 | Mercado, comercial |

### Ícones Remix por aba (Executive Report)

| Tab | Ícone do tab |
|-----|-------------|
| Produto | ri-product-hunt-line |
| Organização | ri-team-line |
| Financeiro | ri-money-dollar-circle-line |
| Riscos e Qualidade | ri-alarm-warning-line |
| Backlog e Decisão | ri-list-check-3 |
| Domínio | ri-shield-keyhole-line |
| Glossário | ri-book-2-line |

---

## Regions omitidas

Nenhuma region do delivery-report foi omitida — todas as 37 regions encontradas estão mapeadas nos planos A e B.

> **Nota:** REG-NARR-01 aparece como hero section PRÉ-TABS no Executive Report (não como tab separada). REG-EXEC-03 e REG-EXEC-04 aparecem tanto no Executive (Tab 5) quanto são referenciadas pelo One-Pager (setup essencial as prevê, mas com conteúdo diferente: no One-Pager, o descritivo do REG-EXEC-01 já cobre o essencial, e próximos passos não entram no one-pager de orçamento).
