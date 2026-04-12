---
title: TODO
description: Lista de pendências do projeto Discovery To Go — problemas identificados no teste end-to-end (Veezoozin run-1)
project-name: discovery-to-go
version: 06.00.000
status: ativo
author: claude-code
category: todo
area: tecnologia
tags:
  - todo
  - pendencia
  - pipeline-issues
created: 2026-04-11
updated: 2026-04-11
---

# TODO — Discovery To Go

20 problemas identificados durante o primeiro teste end-to-end (Veezoozin run-1). Organizados em 4 categorias por área de impacto.

---

## Concluídos

<details>
<summary>25 itens concluídos nesta sessão (clique para expandir)</summary>

- ~~1. Consolidar packs no formato único~~ DONE
- ~~2. Sample run atualizado~~ DONE
- ~~3. Terminologia "context-template"~~ DONE
- ~~4. CLAUDE.md atualizado~~ DONE
- ~~5. .gitignore (draw.io temps)~~ DONE
- ~~6. product-discovery-deliverables.md~~ DONE
- ~~7. README.md atualizado~~ DONE
- ~~8. Information Regions (85 regions, previews, chart specialist)~~ DONE
- ~~9. Consolidator com regions~~ DONE
- ~~10. HTML Writer com regions~~ DONE
- ~~11. Sample run com regions~~ DONE
- ~~12. CLAUDE.md + chart-specialist~~ DONE
- ~~13. Sync base-artifacts~~ DONE
- ~~14. Teste end-to-end (Veezoozin)~~ DONE
- ~~15. Report setups (essential/executive/complete)~~ DONE
- ~~16. Report Planner skill~~ DONE
- ~~17. quick-start.md com report setups~~ DONE
- ~~18. README.md seções atualizadas~~ DONE
- ~~READMEs em 117 subpastas~~ DONE
- ~~Client template scaffold~~ DONE
- ~~Starter-kit com briefing template~~ DONE
- ~~Docs organizados (guides/ + reference/ + diagrams/)~~ DONE
- ~~Auditoria de consistência (10 issues)~~ DONE
- ~~discovery-pipeline.md v02~~ DONE
- ~~Orchestrator: auto-detect + simulação~~ DONE

</details>

---

## Categoria A — Infraestrutura do Pipeline

Problemas na mecânica de execução do pipeline — scaffold, logs, gates, estados.

---

### P1. Scaffold da run é manual — não existe automação

**Severidade:** Alta | **Fase:** Setup | **Detectado:** Início da execução

**O que aconteceu:** O orchestrator é uma skill (SKILL.md com instruções), não código executável. Para rodar o pipeline foi necessário criar manualmente via bash: a estrutura de pastas (`setup/`, `iterations/`, `delivery/`), copiar os blueprints para `current-context/`, copiar os templates de customização, e criar `config.md` e `pipeline-state.md`.

**O que deveria ter acontecido:** Um comando como `./scripts/create-run.sh --briefing briefing.md --client veezoozin` deveria materializar toda a estrutura automaticamente, lendo o frontmatter do briefing para detectar context-templates, report-setup, e outras configurações.

**Impacto:** Sem automação, cada nova run exige ~20 comandos manuais de cópia e criação de pastas. Propenso a erros (esquecer de copiar um blueprint, usar path errado, etc.).

**Ação:**
- [ ] Criar script `support-tools/create-run/create-run.sh` (ou Python) que:
  - Recebe: `--briefing <path>` e `--client <name>`
  - Lê frontmatter do briefing (context-templates, report-setup, client-simulation, scoring)
  - Cria `custom-artifacts/{client}/runs/run-{n}/` com toda a estrutura
  - Copia blueprints de `context-templates/` para `current-context/`
  - Copia templates de `dtg-artifacts/templates/customization/` para `setup/customization/`
  - Gera `config.md` e `pipeline-state.md` a partir do briefing
  - Auto-incrementa o número da run
- [ ] Documentar uso no `docs/guides/quick-start.md`
- [ ] Adicionar ao catálogo de support-tools

---

### P2. Log da entrevista (interview.md) não foi gerado

**Severidade:** Alta | **Fase:** Fase 1 | **Detectado:** Fim da Fase 1

**O que aconteceu:** A regra `analyst-discovery-log` exige um log cronológico da entrevista com formato de tabela (colunas `Quem | Diálogo`), emojis por persona, e source tags (`[BRIEFING]`, `[RAG]`, `[INFERENCE]`). O teste gerou os 8 result files diretamente sem registrar o diálogo simulado entre os especialistas e o customer.

**O que deveria ter acontecido:** Cada bloco temático deveria produzir um trecho de log com as perguntas do especialista, as respostas do customer (com source tags), observações e decisões. O orchestrator deveria consolidar os 8 trechos em um único `iterations/iteration-1/logs/interview.md`.

**Impacto:** Sem o interview.md, perde-se a rastreabilidade de como cada informação foi obtida. O auditor não consegue verificar se as `[INFERENCE]` são justificadas. O humano no HR Review não consegue revisar o diálogo.

**Ação:**
- [ ] Cada agente da Fase 1 deve gerar, junto com o result file, um trecho de log de entrevista
- [ ] Formato: tabela `| Quem | Diálogo |` com emojis (🧑‍💼 PO, 🏗️ Architect, 🔒 Security, 👤 Customer)
- [ ] Cada resposta do customer marcada com `[BRIEFING]`, `[RAG]` ou `[INFERENCE]`
- [ ] Orchestrator consolida em `iterations/iteration-{i}/logs/interview.md`
- [ ] Em modo simulação, o log é gerado com nota: "[SIMULADO — customer gerado por IA]"

---

### P3. Pipeline seguiu para Fase 3 com scores abaixo do threshold

**Severidade:** Alta | **Fase:** Fase 2 → Fase 3 | **Detectado:** Transição entre fases

**O que aconteceu:** O auditor deu 82% e o 10th-man deu 62%. O threshold padrão configurado é ≥90%. O pipeline deveria ter pausado para HR Review antes de avançar para a Fase 3, mas seguiu direto porque o teste roda em modo simulação sem pausas.

**O que deveria ter acontecido:** Mesmo em modo simulação (`client-simulation: sim`), o pipeline deveria ter: (1) registrado o score no pipeline-state.md, (2) gerado um `hr-loop-round2-pass1.md` com flag `[BELOW-THRESHOLD]`, (3) registrado a decisão simulada "AVANÇAR — simulação, score abaixo do threshold aceito automaticamente", (4) incluído callout `[!danger]` no delivery report sinalizando que o material não passou nos gates.

**Impacto:** O delivery report final recomenda "GO CONDICIONAL" sem deixar explícito que os gates de qualidade não foram atingidos. Um stakeholder que leia apenas o report pode não perceber que o material tem ressalvas significativas.

**Ação:**
- [ ] Em modo simulação: registrar score + gerar HR loop log + avançar com flag `[BELOW-THRESHOLD]`
- [ ] Em modo real: PAUSAR obrigatoriamente quando score < threshold
- [ ] O delivery report deve incluir banner `[!danger]` quando gerado com scores abaixo do threshold
- [ ] O Go/No-Go (REG-EXEC-03) deve refletir fielmente os scores — se abaixo, veredicto não pode ser "GO"

---

### P7. HR Review logs não foram gerados

**Severidade:** Média | **Fase:** Entre fases | **Detectado:** Revisão pós-pipeline

**O que aconteceu:** Os arquivos `hr-loop-round{N}-pass{M}.md` — que registram a decisão do humano em cada pausa — não foram criados. São 3 pausas (após Fase 1, 2 e 3) e nenhuma gerou log.

**O que deveria ter acontecido:** Mesmo em simulação, cada pausa de HR Review deveria gerar um arquivo com: observações (vazias em simulação), decisão ("AVANÇAR — simulação"), scores das fases anteriores, e timestamp.

**Impacto:** Sem os logs de HR Review, a trilha de auditoria do pipeline está incompleta. Não há registro formal de que o humano (ou simulação) autorizou o avanço.

**Ação:**
- [ ] Gerar `hr-loop-round1-pass1.md` após Fase 1 com decisão simulada
- [ ] Gerar `hr-loop-round2-pass1.md` após Fase 2 com scores e flag `[BELOW-THRESHOLD]` se aplicável
- [ ] Gerar `hr-loop-round3-pass1.md` após Fase 3 com resultado final
- [ ] Usar o template `human-review-template.md` como base

---

### P11. pipeline-state.md não foi atualizado durante a execução

**Severidade:** Baixa | **Fase:** Todas | **Detectado:** Revisão pós-pipeline

**O que aconteceu:** O pipeline-state.md foi criado no setup com metadata inicial mas não recebeu snapshots ao longo da execução. O pipeline exige que seja append-only — um snapshot é adicionado ao final após cada fase com: status, scores, decisão do HR, tokens consumidos.

**O que deveria ter acontecido:** 3 snapshots appendados: (1) após Fase 1 com resumo dos 8 blocos, (2) após Fase 2 com scores do auditor e 10th-man, (3) após Fase 3 com artefatos gerados e resultado final.

**Impacto:** O pipeline-state.md é a "memória viva" da run. Sem snapshots, não há registro cronológico do que aconteceu. Iterações futuras não teriam contexto do que foi feito anteriormente.

**Ação:**
- [ ] Após cada fase, appendar snapshot com: fase, status, scores (se aplicável), decisão HR, tokens
- [ ] No final, appendar snapshot de conclusão com lista de artefatos gerados e resultado
- [ ] O script de scaffold (P1) pode incluir helper para append de snapshots

---

## Categoria B — Qualidade da Fase 1 (Discovery)

Problemas na execução da Fase 1 — agentes, entrevista, consistência, blueprints.

---

### P4. Inconsistência financeira grave entre blocos 1.3 e 1.8

**Severidade:** Alta | **Fase:** Fase 1 | **Detectado:** Fase 2 (auditor)

**O que aconteceu:** O bloco 1.3 (Valor e OKRs, gerado pelo PO) projeta ARR de R$ 460K e break-even no mês 3. O bloco 1.8 (TCO e Build vs Buy, gerado pelo solution-architect) projeta ARR equivalente a ~R$ 175K e break-even no mês 14-18. Divergência de **2.6x no ARR** e **5x no break-even**. Os dois blocos foram gerados por agentes diferentes, em paralelo, sem validação cruzada.

**O que deveria ter acontecido:** O orchestrator deveria fazer uma cross-validation entre blocos financeiros ao fim da Fase 1. Se valores divergem mais de 20%, sinalizar automaticamente e pedir que os agentes conciliem antes de avançar para o HR Review.

**Impacto:** O stakeholder recebe um delivery report com números contraditórios. A credibilidade do discovery é comprometida. O auditor detectou (e penalizou na dimensão Consistência — 72%) mas não houve correção.

**Ação:**
- [ ] Adicionar passo de cross-validation no orchestrator entre blocos 1.3 e 1.8
- [ ] Se divergência > 20% em ARR, TCO, break-even ou team cost → flag automático `[INCONSISTÊNCIA-FINANCEIRA]`
- [ ] Forçar conciliação antes de avançar (solution-architect é source of truth para TCO; PO ajusta projeções)
- [ ] Considerar rodar os blocos financeiros em sequência (não paralelo) para que 1.8 tenha acesso ao output de 1.3

---

### P5. Customer não operou como agente separado

**Severidade:** Média | **Fase:** Fase 1 | **Detectado:** Durante execução

**O que aconteceu:** O pipeline define que o customer é um agente independente que simula o cliente — respondendo perguntas dos especialistas com dados do briefing, marcados com source tags. No teste, cada agente (PO, architect, security) fez tudo sozinho: entrevistou e respondeu. Não houve interação entre agentes.

**O que deveria ter acontecido:** O PO pergunta → o customer responde com `[BRIEFING]` ou `[INFERENCE]` → o PO analisa a resposta e decide a próxima pergunta. Isso cria um diálogo rastreável (registrado no interview.md) e força transparência sobre o que é dado real vs inferido.

**Impacto:** Sem o customer separado, não há separação entre "o que o cliente disse" e "o que o especialista interpretou". As source tags ficam menos confiáveis porque o mesmo agente que pergunta é quem inventa a resposta.

**Ação:**
- [ ] Implementar o customer como agente separado invocado pelo orchestrator
- [ ] Fluxo por bloco: especialista formula perguntas → customer responde → especialista analisa
- [ ] Em modo simulação, o customer pode rodar inline mas deve gerar respostas tagueadas separadamente
- [ ] O interview.md registra o diálogo entre especialista e customer

---

### P6. Agentes não consultaram os discovery-blueprints

**Severidade:** Média | **Fase:** Fase 1 | **Detectado:** Revisão pós-pipeline

**O que aconteceu:** Os 3 discovery-blueprints (saas, ai-ml, datalake-ingestion) foram copiados corretamente para `setup/customization/current-context/` durante o scaffold. Porém, nenhum dos 4 agentes da Fase 1 os leu — trabalharam apenas com o briefing.

**O que deveria ter acontecido:** Cada agente deveria ler os blueprints relevantes antes de iniciar seu bloco. O blueprint de SaaS tem seção "Componente 1 — Produto e Modelo Comercial" que guia exatamente o que o PO deve perguntar. O blueprint de AI/ML tem "Componente 2 — Desenvolvimento de Modelos" que guia o architect no bloco de arquitetura.

**Impacto:** Os agentes geraram conteúdo de qualidade (o briefing era rico), mas perderam os concerns específicos de domínio que os blueprints trazem (ex: antipatterns SaaS, edge cases de tenancy, checklist de privacy para ML). O resultado ficou genérico onde poderia ser domain-specific.

**Ação:**
- [ ] O orchestrator deve incluir no prompt de cada agente: "Leia os blueprints em {paths} antes de iniciar"
- [ ] Mapear quais blocos são cobertos por quais blueprints (já existe na seção "Mapeamento para os 8 Blocos")
- [ ] O agente deve citar o blueprint como fonte quando usar um concern de domínio

---

### P14. Projeção receita vs custo negativa — pipeline não bloqueou

**Severidade:** Alta | **Fase:** Fase 2 → Fase 3 | **Detectado:** Análise do 10th-man

**O que aconteceu:** O 10th-man identificou que no cenário "esperado" o projeto acumula **-$901K de déficit em 3 anos**. Com churn realista de 10%, o projeto **nunca atinge break-even**. Mesmo assim, o pipeline gerou um delivery report com recomendação "GO CONDICIONAL" — sugerindo que o projeto deveria prosseguir.

**O que deveria ter acontecido:** Um projeto com projeção financeira negativa em 3 anos é, por definição, inviável no modelo proposto. Isso deveria ter sido flagado como `[VIABILIDADE-NEGATIVA]` e o HR Review da Fase 2 deveria exigir que o humano aceite explicitamente o risco financeiro — com justificativa registrada (ex: "investimento estratégico", "pivot de modelo previsto").

**Impacto:** O stakeholder recebe um "GO CONDICIONAL" para um projeto que o próprio pipeline calculou como financeiramente inviável. Se o humano não ler os detalhes do 10th-man, pode aprovar um projeto que não se paga.

**Ação:**
- [ ] Adicionar validação automática: se receita projetada < custo projetado em 3 anos → `[VIABILIDADE-NEGATIVA]`
- [ ] HR Review da Fase 2 deve mostrar callout `[!danger]` exigindo aceite explícito do risco
- [ ] O auditor deve ter dimensão "Viabilidade Financeira" que verifica TCO vs receita
- [ ] Go/No-Go (REG-EXEC-03) deve ter dimensão "Viability" como VERMELHO (não amarelo) quando projeção é negativa
- [ ] Se humano aceita: registrar justificativa no pipeline-state.md
- [ ] Se humano não aceita: voltar para Fase 1 para revisar modelo de negócio/pricing

---

### P16. Especialistas listam riscos com mitigações genéricas

**Severidade:** Alta | **Fase:** Fase 1 + Fase 3 | **Detectado:** Revisão dos results

**O que aconteceu:** Os riscos identificados pelos especialistas têm mitigações de 1 linha genérica. Exemplo: Risco "DPO não nomeado" → Mitigação "Nomear DPO". Risco "Accuracy NL-to-SQL incerta" → Mitigação "PoC na Sprint 0". Isso não dá ao stakeholder informação suficiente para agir.

**O que deveria ter acontecido:** Cada risco deveria ter um plano de mitigação detalhado com: (1) passos concretos para resolver, (2) responsável por cada passo, (3) custo estimado da mitigação, (4) timeline, (5) consequência se não resolver a tempo. Exemplo: "DPO não nomeado → 1) Avaliar DPO interno vs consultoria externa. 2) Budget: R$ 5-15K/mês se terceirizado. 3) Contratar até semana 4 do Sprint 0. 4) Responsável: CTO. 5) Se não resolver até go-live: não lançar — blocker legal."

**Impacto:** Mitigações genéricas dão falsa sensação de que os riscos estão endereçados. O stakeholder lê "PoC na Sprint 0" e assume que está coberto, mas ninguém definiu quem faz, quanto custa, e o que acontece se a PoC falhar.

**Ação:**
- [ ] Atualizar skills dos especialistas: ao identificar risco, exigir mitigação com: ação, responsável, custo, prazo, consequência
- [ ] Atualizar regra de discovery: risco sem mitigação detalhada → penalidade na dimensão "Profundidade"
- [ ] O auditor deve penalizar explicitamente mitigações de 1 linha
- [ ] O consolidator deve destacar riscos com mitigação insuficiente no delivery report
- [ ] Considerar sub-seção "Plano de Mitigação" dentro de REG-RISK-01 e REG-RISK-02

---

## Categoria C — Qualidade do HTML (Fase 3)

Problemas na renderização visual dos relatórios HTML.

---

### P8. md-writer (Fase 3.1) foi pulado

**Severidade:** Média | **Fase:** Fase 3 | **Detectado:** Durante execução

**O que aconteceu:** O pipeline define 4 sub-fases na Fase 3: md-writer → consolidator → report-planner → html-writer. No teste, o md-writer (3.1) foi pulado — o consolidator leu os result files brutos diretamente, sem polimento.

**O que deveria ter acontecido:** O md-writer deveria ter lido os 8 result files da Fase 1 e gerado versões polidas (formatação Obsidian, frontmatter padronizado, emojis semânticos, siglas expandidas, wikilinks corretos). O consolidator então leria os arquivos polidos.

**Impacto:** O delivery-report.md foi gerado a partir de conteúdo bruto. A formatação é inconsistente entre blocos (cada agente escreveu com estilo diferente). Siglas não estão expandidas. Wikilinks podem estar quebrados.

**Ação:**
- [ ] Incluir passo 3.1 (md-writer) na execução — polir os 8 drafts
- [ ] Gerar arquivos polidos em `delivery/intermediate/` ou sobrescrever em `results/`
- [ ] O consolidator deve ler os polidos, não os brutos
- [ ] O md-writer deve aplicar: frontmatter padronizado, emojis em H2, siglas expandidas, formatação consistente

---

### P12. Glossário de abreviações não gerado nos HTMLs

**Severidade:** Média | **Fase:** Fase 3.4 (HTML Writer) | **Detectado:** Revisão visual

**O que aconteceu:** Os relatórios HTML usam dezenas de siglas técnicas (TCO, MRR, ARR, LTV, CAC, LGPD, DPO, DPA, NL-to-SQL, RAG, MCP, OKR, MVP, SLA, JTBD, etc.) sem nenhum suporte visual. Não há tooltips (`<abbr>`) ao passar o mouse sobre as siglas, nem glossário no final do documento.

**O que deveria ter acontecido:** O workspace tem convenções de tratamento de siglas (`conventions/acronyms/`) e um banco de siglas (`acronym-bank.md`) com expansões. O html-writer deveria usar esses recursos para: (1) envolver cada sigla conhecida em `<abbr title="Total Cost of Ownership">TCO</abbr>` para tooltip on hover, (2) adicionar seção "Glossário" no final do HTML listando todas as siglas usadas com suas expansões.

**Impacto:** Um executivo que lê o report pela primeira vez encontra "DPA" e não sabe o que é. Precisa googlar ou perguntar. Isso reduz a acessibilidade do documento para públicos não-técnicos.

**Ação:**
- [ ] Atualizar html-writer para gerar `<abbr title="...">` em siglas conhecidas
- [ ] Consultar `acronym-bank.md` para expansões
- [ ] Siglas desconhecidas → sublinhado pontilhado sem tooltip (sinal de que precisa ser adicionada ao banco)
- [ ] Seção "Glossário" no final de cada HTML
- [ ] Considerar criar REG-NARR-04 (Glossary) como region própria

---

### P13. TCO 3 Anos — gráfico gerado como SVG ao invés de Chart.js

**Severidade:** Média | **Fase:** Fase 3.4 (HTML Writer) | **Detectado:** Revisão visual

**O que aconteceu:** Na seção TCO 3 Anos (REG-FIN-01) do `executive-report.html`, o gráfico de barras empilhadas foi renderizado como SVG inline. O `report-plan.md` especificou `Chart.js stacked bar` e a prioridade de tecnologia definida é: HTML/CSS > Chart.js > Card. SVG inline **não está na lista** de tecnologias aprovadas para gráficos de dados.

**O que deveria ter acontecido:** O html-writer deveria ter usado `<canvas>` com Chart.js (type: 'bar', stacked: true) para renderizar as 5 categorias de custo × 3 anos, conforme especificado no report-plan.md.

**Impacto:** SVG inline para gráficos de dados é difícil de manter, não tem tooltips interativos, não re-renderiza corretamente no toggle dark/light, e não segue o padrão estabelecido.

**Ação:**
- [ ] Substituir SVG por Chart.js stacked bar em REG-FIN-01
- [ ] Reforçar na skill html-writer: SVG inline NÃO é opção para gráficos de dados
- [ ] SVG inline aceito apenas para: gauges simples, progress bars, ícones custom (quando HTML/CSS não resolve)

---

### P15. Estimativa de Esforço — gráfico SVG ao invés de HTML/CSS

**Severidade:** Média | **Fase:** Fase 3.4 (HTML Writer) | **Detectado:** Revisão visual

**O que aconteceu:** Mesma issue do P13 — a seção Estimativa de Esforço (REG-FIN-05) gerou barras horizontais como SVG inline. Barras horizontais simples são triviais em HTML/CSS puro (divs com `width: X%`) e são o caso de uso mais básico de HTML/CSS.

**O que deveria ter acontecido:** Divs com CSS, cada barra com width proporcional ao valor, cor por T-shirt size (P=verde, M=azul, G=amarelo, GG=vermelho), label com horas.

**Ação:**
- [ ] Substituir SVG por HTML/CSS puro (divs com width proporcional)
- [ ] Reforçar: barras horizontais simples = HTML/CSS SEMPRE, sem exceção

---

### P17. Layout do 10th-man diferente do layout do auditor

**Severidade:** Baixa | **Fase:** Fase 3.4 (HTML Writer) | **Detectado:** Revisão visual

**O que aconteceu:** A seção REG-QUAL-01 (Score do Auditor) tem layout exemplar: radar chart com 5 dimensões à esquerda + tabela de scores à direita (sidebar layout). A seção REG-QUAL-02 (Questões do 10th-man) usa layout completamente diferente: cards com badges de severidade, sem radar chart.

**O que deveria ter acontecido:** Ambas são validações da Fase 2 e deveriam usar o mesmo padrão visual. O 10th-man tem 3 dimensões com scores (Divergência 55%, Robustez 60%, Completude Crítica 73%) que se encaixam perfeitamente num radar chart de 3 eixos.

**Impacto:** O leitor vê dois padrões visuais diferentes para o mesmo tipo de informação (validação com scores). Parece que o 10th-man é menos importante que o auditor.

**Ação:**
- [ ] REG-QUAL-02: adicionar radar chart 3 eixos (Chart.js) com as dimensões do 10th-man
- [ ] Manter cards com severity badges para as questões residuais (abaixo do radar)
- [ ] Usar sidebar layout (mesmo do auditor): radar à esquerda + detalhes à direita
- [ ] Atualizar chart-specialist recommendation e report-plan de REG-QUAL-02

---

### P18. Radar charts sem faixas visuais de escala

**Severidade:** Baixa | **Fase:** Fase 3.4 (HTML Writer) | **Detectado:** Revisão visual

**O que aconteceu:** Os radar charts (auditor, go/no-go) mostram linhas de grade (20, 40, 60, 80, 100) mas as regiões entre as linhas não têm preenchimento visual. É difícil perceber rapidamente em qual faixa cada ponto está sem ler os números.

**O que deveria ter acontecido:** Faixas de cor suave (quase transparentes) entre as linhas de grade, funcionando como zonas semânticas: 0-40 vermelho suave (zona crítica), 40-70 amarelo suave (atenção), 70-90 neutro (aceitável), 90-100 verde suave (excelência). O leitor bate o olho e sabe instantaneamente se o score está na zona verde ou vermelha.

**Ação:**
- [ ] Chart.js: adicionar datasets de background com fill entre escalas (opacity 0.03-0.05)
- [ ] Cores: danger (0-40), warning (40-70), neutro (70-90), success (90-100)
- [ ] Aplicar em TODOS os radar charts (auditor, 10th-man, go/no-go)
- [ ] Documentar como padrão no chart-specialist skill

---

### P19. Seção SaaS no executive report tem tom técnico demais

**Severidade:** Média | **Fase:** Fase 3.2 + 3.4 | **Detectado:** Revisão visual

**O que aconteceu:** A seção "SaaS — Detalhamento Multi-Tenant e Pricing" (REG-DOM-SAAS-01) no `executive-report.html` discute isolamento por schema, row-level security, service accounts dedicados — linguagem técnica para um público que é diretoria e gestão.

**O que deveria ter acontecido:** O report-setup `executive` é para **diretoria e gestão**. A seção SaaS deveria focar em: quais planos existem, quanto custa cada um, projeção de MRR/ARR, modelo de receita, diferenciação entre tiers. Detalhes de isolamento técnico pertencem ao setup `complete` (REG-DOM-SAAS-02 Tenancy Strategy).

**Impacto:** Um diretor lê sobre "service accounts dedicados por tenant com row-level security no BigQuery" e desliga. Perde a informação de negócio que está misturada no meio do conteúdo técnico.

**Ação:**
- [ ] O consolidator deve adaptar o **tom** de cada region com base no report-setup selecionado
- [ ] Para `executive`: tom "executivo-negócio" nas regions domain-specific
- [ ] Para `complete`: tom "técnico" mantido
- [ ] Considerar separar REG-DOM-SAAS-01 em dois: "Modelo Comercial" (executive) e "Estratégia de Tenancy" (complete)

---

## Categoria D — Redesign do One-Pager

Redesenho conceitual do report-setup `essential`.

---

### P20. One-Pager deve funcionar como orçamento de tempo (sem valores financeiros)

**Severidade:** Alta | **Fase:** Report Setup + Consolidator + HTML Writer | **Detectado:** Revisão conceitual

**O que aconteceu:** O one-pager atual é um resumo executivo genérico com: overview, problema, escopo, TCO, riscos, go/no-go, next steps. Funciona como "resumo do discovery" mas não como ferramenta comercial.

**O que deveria ser:** O one-pager deveria funcionar como um **orçamento de projeto baseado em tempo** — sem valores em R$, apenas horas e semanas. O objetivo é dar um "cheiro" do esforço necessário para que o comercial/gestor possa estimar custos internamente (preenchendo valor/hora por role).

**Estrutura proposta (6 blocos):**

1. **Descritivo do Projeto** — Descrição macro (2-3 frases), objetivo (1 frase), premissas (bullets), responsáveis (tabela nome/papel)

2. **Qualidade e Confiança** — Scores do auditor e 10th-man (stat cards ou radar compacto), veredicto Go/No-Go (badge), nota de confiança ("X% briefing, Y% inferido")

3. **Escopo** — IN (bullets verdes) vs OUT (bullets vermelhos), separação visual forte (split card)

4. **Atividades e Esforço** — Tabela com: atividade macro, roles envolvidas, horas/homem por role, coluna valor/hora vazia (para preenchimento manual)

5. **Planejamento (Gantt relativo)** — Gráfico de barras horizontais sem datas fixas (Semana 1, 2, ..., N), dependências visuais, marcos destacados, renderizado em HTML/CSS puro

6. **Totais** — Total de horas por role, total geral, duração em semanas (stat cards)

**Ação:**
- [ ] Redesenhar `dtg-artifacts/templates/report-setups/essential.md` com os 6 blocos
- [ ] Criar/ajustar regions:
  - REG-EXEC-01 → simplificar para descritivo + objetivo + premissas + responsáveis
  - REG-QUAL-01/02 → versão compacta (stat cards, sem radar chart)
  - REG-PROD-07 → manter split card in/out
  - REG-BACK-01 → tabela de atividades com roles e horas (sem priorização MoSCoW)
  - NOVO: REG-PLAN-01 → Gantt relativo (HTML/CSS barras com grid de semanas)
  - NOVO: REG-FIN-06 → Totais de horas (stat cards)
- [ ] Atualizar html-writer para renderizar Gantt relativo em HTML/CSS
- [ ] Atualizar report-planner para gerar plano adequado quando setup = essential
- [ ] One-pager NÃO mostra valores em R$ — coluna "Valor/Hora" vazia para preenchimento manual

---

## Categoria E — Documentação

Ajustes de documentação e paths.

---

### P9. Path das runs não está documentado

**Severidade:** Baixa | **Fase:** Estrutura | **Detectado:** Revisão pós-pipeline

**O que aconteceu:** As runs ficam em `custom-artifacts/{client}/runs/run-{n}/` mas o quick-start.md, README.md e orchestrator SKILL.md referenciam `runs/run-{n}/` genérico (sem o path do cliente).

**Ação:**
- [ ] Documentar path correto no quick-start.md, README.md e orchestrator SKILL.md

---

### P10. config.md não herda campos do briefing automaticamente

**Severidade:** Baixa | **Fase:** Setup | **Detectado:** Durante scaffold

**O que aconteceu:** Os campos `report-setup`, `context-templates`, `client-simulation` e `scoring-threshold` do briefing não foram copiados automaticamente para o config.md — foram preenchidos manualmente.

**Ação:**
- [ ] O script de scaffold (P1) deve ler frontmatter do briefing e propagar para config.md

---

### P21. Auditor deve alertar quando receita não cobre TCO em 3 anos

**Severidade:** Alta
**Fase:** Fase 2 (Auditor)

**O que deveria acontecer:** O auditor, ao validar os blocos 1.3 (Valor/OKRs) e 1.8 (TCO/Build vs Buy), deve comparar automaticamente a receita projetada com o TCO projetado em 3 anos. Se a receita não cobre o TCO (projeção negativa), o auditor deve:

1. Emitir alerta `[!danger]` explícito na seção de Viabilidade Financeira
2. Penalizar na dimensão "Completude" — o discovery está incompleto se não endereça a inviabilidade
3. Registrar como finding crítico com recomendação: "Receita projetada (R$ X) não cobre TCO (R$ Y) em 3 anos. Diferença: -R$ Z. O discovery precisa apresentar cenários alternativos viáveis."

**Ação:**
- [ ] Atualizar auditor SKILL.md: adicionar validação automática receita vs TCO
- [ ] Se receita < TCO → finding crítico + alerta `[!danger]` + penalidade em Completude
- [ ] O alerta deve incluir: receita projetada, TCO projetado, diferença, e recomendação de cenários

---

### P22. Gerar cenários alternativos quando solução é financeiramente inviável

**Severidade:** Alta
**Fase:** Fase 1 (Solution Architect) + Fase 3 (Consolidator)

**O que deveria acontecer:** Quando a análise do bloco 1.8 identifica que a solução proposta gera prejuízo em 3 anos, o solution-architect NÃO deve apenas registrar o número negativo e seguir. Deve **obrigatoriamente** gerar cenários alternativos que tornem o projeto viável.

**Tipos de cenários a explorar:**

| Cenário | O que muda | Exemplo |
|---------|-----------|---------|
| **Ajuste de pricing** | Aumentar preço dos planos | Pro de R$ 897 para R$ 1.497 |
| **Redução de escopo MVP** | Cortar features caras | Remover visualização AI, focar em NL-to-SQL puro |
| **Mudança de stack** | Trocar componentes caros | Substituir Vertex AI Vector Search por Firestore vectors |
| **Mudança de modelo** | Pivô de modelo de negócio | De SaaS por tenant para consultoria + licença |
| **Aumento de base** | Projeção com mais clientes | Break-even com 50 tenants ao invés de 35 |
| **Redução de equipe** | Team mais enxuto | 4 devs ao invés de 6, timeline mais longa |

**Para cada cenário alternativo, o architect deve apresentar:**
- Nome do cenário
- O que muda em relação ao cenário base
- Novo TCO 3 anos
- Nova receita projetada 3 anos
- Novo break-even (meses)
- Riscos introduzidos pela mudança
- Recomendação (viável / viável com ressalvas / inviável)

**O delivery report deve incluir:**
- Seção de cenários (nova region `REG-FIN-07 — Cenários Financeiros`)
- Tabela comparativa: cenário base vs alternativas
- Gráfico comparativo (bar chart com receita vs custo por cenário)
- Recomendação do architect sobre qual cenário seguir

**Ação:**
- [ ] Atualizar solution-architect SKILL.md: ao calcular TCO, se receita < custo → obrigatório gerar 3+ cenários alternativos
- [ ] Criar region `REG-FIN-07` (Financial Scenarios) com schema, exemplo e chart specialist recommendation
- [ ] Atualizar consolidator: incluir seção de cenários no delivery report quando existirem
- [ ] Atualizar report-setups: cenários aparecem no `executive` e `complete` (não no `essential`)
- [ ] Atualizar html-writer: renderizar tabela comparativa de cenários com bar chart (Chart.js grouped bar)
- [ ] Criar arquivo `base-artifacts/templates/report-regions/financial/financial-scenarios.md`

---

### P23. Entrevista deve ser executada na ordem — um bloco por vez

**Severidade:** Alta
**Fase:** Fase 1 (Discovery)

**O que aconteceu no teste:** Os 8 blocos temáticos foram executados em paralelo (4 agentes × 2 blocos cada). Isso causou:
- Blocos financeiros (1.3 e 1.8) geraram números contraditórios porque não viram o output um do outro
- Blocos técnicos (1.5, 1.7) não tiveram contexto do que o PO definiu nos blocos 1.1-1.4
- O customer não manteve consistência entre respostas de blocos diferentes (cada agente tinha seu próprio "customer")

**O que deveria acontecer:** Os 8 blocos DEVEM ser executados **sequencialmente**, na ordem #1 → #2 → #3 → #4 → #5 → #6 → #7 → #8. Cada bloco tem acesso ao output dos blocos anteriores. O customer mantém consistência porque é o mesmo agente ao longo de toda a entrevista.

**Por quê na ordem:**
- Bloco #1 (Visão) define o problema — blocos seguintes precisam dessa base
- Bloco #3 (OKRs) define métricas e modelo de negócio — bloco #8 (TCO) precisa desses números
- Bloco #5 (Tech) define stack — bloco #7 (Arquitetura) depende das decisões de stack
- Bloco #6 (Privacy) depende de saber quais dados pessoais existem (definidos nos blocos anteriores)

**Exceção:** Blocos #1 e #2 PODEM rodar em paralelo (ambos são PO, eixo produto). Blocos #5 e #6 PODEM rodar em paralelo (tech e privacy são eixos diferentes). Mas #7 e #8 DEVEM ser sequenciais após #5 e #6.

**Ação:**
- [ ] Atualizar orchestrator SKILL.md: blocos são sequenciais por padrão
- [ ] Definir ordem de dependência:
  ```
  #1 (Visão) → #2 (Personas) → #3 (Valor/OKRs) → #4 (Processo/Equipe)
       ↓                                                    ↓
  #5 (Tech) + #6 (Privacy) em paralelo
       ↓           ↓
  #7 (Arquitetura) → #8 (TCO/Build vs Buy)
  ```
- [ ] Cada agente recebe como input: briefing + blueprints + outputs dos blocos anteriores
- [ ] O customer mantém estado entre blocos (respostas anteriores são contexto para as seguintes)

---

### P24. Log da entrevista (interview.md) é obrigatório — sem log, fase inválida

**Severidade:** Alta
**Fase:** Fase 1 (Discovery)

**O que aconteceu no teste:** A Fase 1 gerou os 8 result files mas NÃO gerou o interview.md. O pipeline aceitou e seguiu para a Fase 2 normalmente.

**O que deveria acontecer:** O interview.md NÃO é opcional — é um artefato obrigatório da Fase 1. Sem ele, a fase é considerada **incompleta**. O orchestrator DEVE validar sua existência antes de avançar para o HR Review.

**Regra:**
- Após os 8 blocos serem executados, o orchestrator verifica se `iterations/iteration-{i}/logs/interview.md` existe e tem conteúdo
- Se não existe → flag `[FASE-INCOMPLETA]` + gerar automaticamente a partir dos result files (modo degradado)
- Se existe mas está vazio → mesmo tratamento
- O auditor na Fase 2 DEVE ler o interview.md para validar rastreabilidade das source tags

**O interview.md serve para:**
- Rastreabilidade: de onde veio cada informação (`[BRIEFING]`, `[RAG]`, `[INFERENCE]`)
- Transparência: o humano no HR Review vê exatamente o que foi perguntado e respondido
- Auditoria: o auditor verifica se as `[INFERENCE]` são justificadas
- Consistência: detectar se o customer contradisse respostas entre blocos
- Documentação: registro permanente da entrevista para consulta futura

**Ação:**
- [ ] Atualizar orchestrator SKILL.md: interview.md é OBRIGATÓRIO — validar existência antes de avançar
- [ ] Se ausente: flag `[FASE-INCOMPLETA]` + tentar gerar modo degradado
- [ ] Atualizar auditor SKILL.md: ler interview.md para validar rastreabilidade
- [ ] Atualizar regra discovery.md: interview.md listado como output obrigatório da Fase 1
- [ ] O interview.md deve ser o PRIMEIRO artefato verificado no checklist de conclusão da Fase 1

---

### P25. Especialistas devem ser consultores ativos — não coletores passivos

**Severidade:** Alta
**Fase:** Fase 1 (Discovery)

**O que aconteceu nos testes:** Os especialistas (PO, solution-architect, cyber-security-architect) operam em modo **coleta passiva** — fazem perguntas ao customer, registram as respostas, e seguem para o próximo tópico. Quando encontram uma lacuna (`[INFERENCE]` fraca ou resposta vaga), apenas documentam a lacuna e avançam.

**O que deveria acontecer:** Cada especialista é um **consultor sênior** — não um entrevistador junior. Ao identificar um problema, lacuna ou risco durante a entrevista, o especialista deve **imediatamente** propor soluções, alternativas e recomendações. O discovery não é apenas "descobrir o que existe" — é "descobrir e recomendar o que fazer".

**Comportamento esperado por situação:**

| Situação na entrevista | Coleta passiva (ERRADO) | Consultor ativo (CORRETO) |
|------------------------|------------------------|--------------------------|
| Customer descreve problema | Registra o problema | Registra + propõe 2-3 abordagens de solução com prós/contras |
| Customer não sabe responder | Marca `[INFERENCE]` e segue | Apresenta opções baseadas no domínio + recomenda a melhor + justifica |
| Resposta vaga do customer | Aceita e documenta | Aprofunda com perguntas específicas + sugere benchmark do mercado |
| Lacuna técnica identificada | Lista como gap | Propõe solução técnica + estima esforço + identifica riscos |
| Risco identificado | Lista risco + mitigação genérica | Propõe plano de mitigação detalhado (P16) + alternativa se falhar |
| Inconsistência entre respostas | Documenta conflito | Confronta o customer + propõe resolução + registra decisão |
| Oportunidade não mencionada | Ignora | Sugere proativamente ("Considerando o domínio SaaS, vocês já pensaram em...") |

**Impacto direto nas notas:**
- **Profundidade** (auditor): sobe quando blocos têm análise + recomendação, não apenas coleta
- **Completude** (auditor): sobe quando lacunas são preenchidas com propostas, não deixadas vazias
- **Divergência** (10th-man): sobe quando alternativas são exploradas durante o discovery, não apenas o caminho feliz
- **Robustez** (10th-man): sobe quando decisões são fundamentadas com prós/contras, não apenas declaradas

**O que cada especialista deve fazer PROATIVAMENTE:**

### PO (blocos #1-#4)
- Propor modelo de negócio quando o briefing não define (freemium vs paid vs enterprise)
- Sugerir personas quando o briefing é genérico ("para empresas" → propor 3-4 perfis concretos)
- Calcular ROI preliminar quando o customer não tem números
- Sugerir OKRs quando o customer diz "queremos ter sucesso"
- Propor faseamento MVP quando o escopo é amplo demais

### Solution Architect (blocos #5, #7, #8)
- Recomendar stack quando o briefing diz "a definir" (baseado no context-template + team skills)
- Propor arquitetura com diagrama quando o customer descreve funcionalidades
- Calcular TCO mesmo quando o customer não pede (é output obrigatório)
- Apresentar Build vs Buy para cada componente com recomendação explícita
- Propor cenários alternativos quando a viabilidade é questionável (P22)
- Sugerir integrações que o customer não mencionou mas que o domínio exige

### Cyber Security Architect (bloco #6)
- Classificar dados mesmo quando o customer não sabe quais são pessoais
- Propor estratégia de DPO quando o customer não tem um
- Mapear sub-operadores mesmo quando o customer não listou
- Recomendar base legal LGPD por tratamento
- Propor timeline de compliance com marcos e responsáveis

**Ação:**
- [ ] Atualizar PO SKILL.md: adicionar seção "Modo consultor ativo" com os comportamentos esperados
- [ ] Atualizar solution-architect SKILL.md: idem
- [ ] Atualizar cyber-security-architect SKILL.md: idem
- [ ] Atualizar customer SKILL.md: quando o customer marca `[INFERENCE]` fraca, o especialista deve reagir propondo solução (não apenas aceitar)
- [ ] Atualizar orchestrator SKILL.md: instruir que cada bloco deve ter seção "Recomendações do especialista" além da coleta
- [ ] Atualizar regra discovery.md: cada bloco DEVE ter: (1) dados coletados, (2) análise do especialista, (3) recomendações com justificativa
- [ ] Atualizar auditor SKILL.md: bonificar +5 na dimensão "Profundidade" quando bloco tem recomendações proativas

---

### P26. Siglas sem tooltip — precisa de arquivo de siglas alimentável

**Severidade:** Média | **Fase:** HTML Writer

Várias siglas no one-pager e executive-report não receberam `<abbr>` tooltip (ex: PLG, RBAC, LOI, SCC). O `acronym-bank.md` existente não contém todas as siglas que aparecem nos reports de discovery.

**Ação:**
- [ ] Enriquecer `base-artifacts/conventions/acronyms/acronym-bank.md` com todas as siglas encontradas nos reports (PLG, RBAC, LOI, SCC, RLS, WAF, SSO, OIDC, SAML, CDN, etc.)
- [ ] Criar processo: ao fim de cada pipeline run, listar siglas sem tooltip e adicioná-las ao banco
- [ ] O html-writer deve marcar siglas sem tooltip com estilo visual diferente (sublinhado pontilhado) para fácil identificação

---

### P27. Alert CSS — ícone e texto desalinhados verticalmente

**Severidade:** Baixa | **Fase:** HTML Writer

A classe `.alert` tem `display: flex; align-items: center;` mas na prática o ícone e o texto não ficam alinhados verticalmente quando o texto quebra em múltiplas linhas.

**Ação:**
- [ ] Ajustar CSS: `.alert { display: flex; align-items: flex-start; }` com `.alert i { margin-top: 2px; }` para alinhar ícone com primeira linha
- [ ] Ou usar `align-items: center` com `line-height` consistente entre ícone e texto
- [ ] Atualizar no playground.html e propagar para os templates

---

### P28. Radar Go/No-Go — pontos não conectados + legenda incorreta

**Severidade:** Média | **Fase:** HTML Writer

O radar do Go/No-Go (REG-EXEC-03) no one-pager foi renderizado em CSS puro, mas:
- a) Os pontos dos scores não estão conectados por linhas (parecem pontos soltos)
- b) A legenda mostra cores (verde/amarelo/vermelho) que não correspondem às zonas desenhadas no fundo

**Ação:**
- [ ] Substituir o radar CSS por **Chart.js radar** (mesmo no one-pager) — é a única forma de ter pontos conectados + zonas corretas
- [ ] Atualizar regra: radar charts SEMPRE usam Chart.js, nunca CSS puro (CSS não consegue conectar pontos num radar)
- [ ] Garantir que a legenda do Chart.js use as mesmas cores das zonas de fundo (P18)
- [ ] Atualizar chart-specialist e html-writer: radar = Chart.js obrigatório

---

### P29. Gráficos de barras verticais — preferir horizontais

**Severidade:** Baixa | **Fase:** HTML Writer

O gráfico de cenários de viabilidade (REG-FIN-07) usa barras verticais. Para comparação entre cenários, barras horizontais são mais legíveis (labels longos não ficam truncados, leitura natural esquerda→direita).

**Ação:**
- [ ] Atualizar chart-specialist: para comparações entre categorias com labels longos, preferir barras horizontais
- [ ] Atualizar html-writer: barras de cenários = horizontais (HTML/CSS) ou Chart.js horizontal bar
- [ ] Aplicar em REG-FIN-07 no próximo run

---

### P30. TCO 3 Anos — gráfico Chart.js não renderizado

**Severidade:** Alta | **Fase:** HTML Writer

O gráfico stacked bar do TCO (REG-FIN-01) no executive-report.html tem o canvas mas as barras não aparecem — apenas os labels (Ano 1, Ano 2, Ano 3) e a legenda. O Chart.js provavelmente não está inicializando corretamente (erro de JS, dados com formato errado, ou canvas com height 0).

**Ação:**
- [ ] Verificar o JS do executive-report.html: o Chart.js está sendo chamado corretamente?
- [ ] Verificar se o canvas tem dimensões definidas (width/height)
- [ ] Verificar se os dados estão no formato correto para Chart.js stacked bar
- [ ] Testar isoladamente o snippet do gráfico para identificar o erro
- [ ] Corrigir e validar que as barras aparecem em dark e light theme

---

### P31. Reports executive e complete precisam de tabs — apenas one-pager é página única

**Severidade:** Alta
**Fase:** HTML Writer

**O que aconteceu:** Todos os HTMLs gerados (one-pager, executive-report) renderizam as regions numa página contínua vertical, scrollando infinitamente. Isso funciona para o one-pager (que é curto, ~8 regions), mas NÃO funciona para executive (22+ regions) nem complete (90+ regions) — ficam enormes e difíceis de navegar.

**O que deveria acontecer:**

| Setup | Navegação |
|-------|-----------|
| `essential` (one-pager) | **SEM tabs** — página única contínua, tudo visível |
| `executive` | **COM tabs** — cada seção é uma aba (Produto, Organização, Financeiro, Riscos, etc.) |
| `complete` | **COM tabs** — mesma estrutura de abas, mais seções |

**Estrutura de tabs para executive-report:**
- Tab 1: Produto e Valor (REG-EXEC-02, PROD-04, PROD-02, PROD-05, PROD-06, PROD-07, PROD-08)
- Tab 2: Organização (REG-ORG-01, ORG-02)
- Tab 3: Financeiro (REG-FIN-01, FIN-05, FIN-07)
- Tab 4: Riscos e Qualidade (REG-RISK-01, RISK-03, QUAL-01, QUAL-02)
- Tab 5: Decisão (REG-BACK-01, NARR-01, EXEC-03, EXEC-04)
- Tab 6: Domain-specific (REG-DOM-*)
- Tab 7: Glossário (REG-GLOSS-01)

O playground.html já tem CSS de tabs (`.tabs-nav`, `.tab-btn`, `.tab-content`) — usar esse padrão.

**Ação:**
- [ ] Atualizar html-writer SKILL.md: one-pager = sem tabs; executive e complete = com tabs
- [ ] Definir no html-layout.md quais seções são tabs (já tem a estrutura "Seção 1", "Seção 2", etc.)
- [ ] Atualizar report-planner: incluir informação de tab no report-plan.md
- [ ] JS: tab navigation com prev/next buttons + keyboard arrows
- [ ] Tab ativa com indicador visual (cor primary na borda inferior)
- [ ] URL hash para deep linking (ex: `#financeiro`)

---

### P32. HTMLs gerados ignoram acentuação PT-BR

**Severidade:** Alta
**Fase:** HTML Writer + Consolidator

**O que aconteceu:** Os relatórios HTML têm texto sem acentuação portuguesa. Exemplos: "Descricao" em vez de "Descrição", "Organizacao" em vez de "Organização", "Projecao" em vez de "Projeção", "Cenarios" em vez de "Cenários". Isso ocorre em títulos de seções, labels de tabelas, texto corrido e labels de gráficos.

**O que deveria acontecer:** O html-writer SKILL.md já tem a regra (seção 8 — Idioma):

> [!danger] Regra inviolável
> O relatório é **exclusivamente em pt-BR**. Toda acentuação portuguesa **deve** ser respeitada.

Mas os agentes que geram o conteúdo (consolidator, report-planner, html-writer) nem sempre respeitam. O problema pode estar:
1. No consolidator gerando delivery-report.md sem acentos
2. No html-writer copiando texto sem acentos
3. Nos agentes que rodam em modo que não preserva acentos

**Ação:**
- [ ] Reforçar no consolidator SKILL.md: todo texto em PT-BR DEVE ter acentuação correta
- [ ] Reforçar no html-writer SKILL.md: ao gerar HTML, verificar e corrigir acentuação
- [ ] Reforçar no report-planner SKILL.md: labels e configurações em PT-BR com acentos
- [ ] Incluir no prompt de cada agente: "Escreva em PT-BR com acentuação correta — 'organização' não 'organizacao'"
- [ ] Considerar um passo de pós-processamento que verifica palavras comuns sem acento e corrige

---

### P33. Reports HTML não seguem o playground.html (Design System ignorado)

**Severidade:** Alta
**Fase:** HTML Writer

**O que aconteceu:** Os HTMLs gerados (one-pager, executive-report) recriam CSS do zero — cada agente inventa seus próprios estilos, classes e tokens. O playground.html (`base-artifacts/assets/ui-ux/playground.html`) já tem um Design System completo com:
- Tokens de cor (`:root` com `--primary`, `--bg`, `--card-bg`, etc. para dark e light)
- Componentes prontos (`.card`, `.card-header`, `.card-body`, `.stat-card`, `.alert`, `.pill`, `.tabs-nav`, `.tab-btn`, etc.)
- Tipografia (Poppins, tamanhos, pesos)
- Header e footer patterns
- Tabelas estilizadas (`.th-bg`, hover states)
- Toggle dark/light com JS

Os agentes recebem instrução para "consultar o playground.html" mas na prática copiam apenas os tokens de cor e reinventam todo o resto. O resultado é CSS inconsistente entre reports, classes diferentes para o mesmo componente, e aparência que não segue o Design System.

**O que deveria acontecer:** O html-writer DEVE:
1. **Copiar o CSS inteiro do playground.html** (tokens + componentes) para cada HTML gerado
2. **Usar as classes do playground** (`.card`, `.stat-card`, `.alert`, `.pill`, `.tabs-nav`, etc.) em vez de inventar novas
3. **Seguir a estrutura HTML do playground** (header, container, cards, footer)
4. O playground é o **template de referência** — não uma sugestão, é a base obrigatória

**Ação:**
- [ ] Atualizar html-writer SKILL.md: regra explícita "COPIAR CSS do playground.html, não reinventar"
- [ ] Listar as classes obrigatórias que devem ser usadas (card, stat-card, alert, pill, tabs-nav, tab-btn, tab-content, etc.)
- [ ] O agente deve ler o playground.html inteiro (não só 200 linhas) e extrair TODO o CSS
- [ ] Componentes custom (scenario bars, radar, timeline) são adições — mas a base DEVE ser o playground

---

### P34. TODOS os gráficos de barras devem ser horizontais em HTML/CSS

**Severidade:** Média
**Fase:** HTML Writer + Chart Specialist

**O que aconteceu:** Alguns gráficos de barras foram gerados verticais (Chart.js) ou com largura desproporcional. As barras horizontais em HTML/CSS são mais legíveis (labels longos não truncam, leitura natural esquerda→direita) e mais simples de implementar.

**Regra a partir de agora:**

| Tipo de gráfico | Tecnologia | Orientação |
|----------------|-----------|------------|
| Barras simples (1 série) | HTML/CSS (`div` com `width: X%`) | **Horizontal** |
| Barras agrupadas (2 séries) | HTML/CSS (2 divs por linha) | **Horizontal** |
| Barras empilhadas (stacked) | HTML/CSS (divs lado a lado) | **Horizontal** |
| Radar | Chart.js | N/A |
| Pie/Donut | Chart.js | N/A |
| Line/Area | Chart.js | N/A |

**Chart.js NÃO é usado para gráficos de barras.** Barras são sempre HTML/CSS horizontal.

**Implementação CSS padrão:**
```css
.bar-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.bar-label { width: 120px; font-size: 0.75rem; text-align: right; flex-shrink: 0; }
.bar-track { flex: 1; background: var(--border); border-radius: 4px; height: 20px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 4px; transition: width 0.3s; }
.bar-value { width: 60px; font-size: 0.72rem; text-align: right; }
```

**Ação:**
- [ ] Atualizar chart-specialist SKILL.md: barras = SEMPRE HTML/CSS horizontal, NUNCA Chart.js
- [ ] Atualizar html-writer SKILL.md: incluir CSS padrão de barras horizontais
- [ ] Remover qualquer menção a Chart.js bar/stacked bar nas recommendations
- [ ] Chart.js fica APENAS para: radar, pie/donut, line/area, scatter, bubble

---

### P35. Ressalvas dos auditores devem ser detalhadas com explicação do impacto

**Severidade:** Alta
**Fase:** Fase 2 (Auditor + 10th-man) + Fase 3 (HTML)

**O que aconteceu:** O 10th-man mostra um radar chart com 3 eixos (Divergência 70%, Robustez 78%, Completude Crítica 80%) e lista as ressalvas como bullets curtos. O leitor vê que "Robustez" tem 78% mas não entende **por quê** é 78% e **o que isso significa** para o projeto.

**O que deveria acontecer:** Abaixo do radar chart, cada ressalva deve ser apresentada como um card expandido com:

1. **Título da ressalva** (ex: "Bus Factor — Risco de Pessoa Única")
2. **Score/dimensão afetada** (ex: "Robustez: 78%")
3. **Descrição detalhada** — 2-3 frases explicando O QUE foi identificado
4. **Por que é importante** — 1-2 frases sobre o impacto se não for endereçado
5. **Recomendação** — o que fazer para resolver

Exemplo:
```
🟡 Bus Factor — Risco de Pessoa Única
Robustez: 78%

O projeto depende de uma única pessoa (Fabio) para toda a operação:
arquitetura, desenvolvimento, deploy, suporte e decisões de produto.
Se Fabio ficar indisponível por 2+ semanas, o projeto para completamente.

POR QUE É IMPORTANTE: Um investidor ou cliente enterprise vai questionar
a sustentabilidade. O bus factor = 1 é o maior risco operacional do projeto.

RECOMENDAÇÃO: Documentar todas as decisões (ADRs), manter código com
testes automatizados, e definir milestone de receita para primeira
contratação (sugerido: R$ 25K MRR para DevOps/SRE).
```

**Ação:**
- [ ] Atualizar 10th-man SKILL.md: cada ressalva deve ter os 5 campos (título, score, descrição, importância, recomendação)
- [ ] Atualizar auditor SKILL.md: idem para findings do auditor
- [ ] Atualizar region REG-QUAL-02: layout = radar + lista de cards detalhados (não apenas bullets)
- [ ] Atualizar region REG-QUAL-01: idem para findings do auditor
- [ ] Atualizar html-writer: renderizar ressalvas como cards expandidos com borda colorida por severidade

---

### P36. Responsividade mobile — hamburger menu + footer centralizado

**Severidade:** Média
**Fase:** HTML Writer

**O que aconteceu:** Quando a página é redimensionada para menos de 50% da tela (~768px ou menos):
- As tabs continuam visíveis e quebram o layout (overflow horizontal)
- O botão de tema fica perdido no header
- O footer fica alinhado à esquerda

**O que deveria acontecer:**

#### 1) Hamburger menu (< 768px)
- Ocultar `.tabs-nav` e o botão de tema do header
- Mostrar um botão hamburger (☰ `ri-menu-line`) no header
- Ao clicar: abrir menu lateral (drawer) ou dropdown com:
  - Lista das tabs como itens de menu (com ícone e nome)
  - Botão de tema como último item do menu
- Ao selecionar uma tab no menu: fechar menu + ativar a tab

```css
@media (max-width: 768px) {
    .tabs-nav { display: none; }
    .theme-toggle { display: none; }
    .hamburger-btn { display: flex; }
    .mobile-menu { display: none; } /* shown via JS toggle */
    .mobile-menu.open { display: flex; flex-direction: column; }
}
```

#### 2) Footer centralizado (< 768px)
```css
@media (max-width: 768px) {
    .footer { text-align: center; }
    .footer-content { flex-direction: column; align-items: center; }
}
```

**Ação:**
- [ ] Atualizar html-writer SKILL.md: seção de responsividade com hamburger menu spec
- [ ] Incluir no playground.html o CSS e JS do hamburger menu como padrão
- [ ] Footer: `text-align: center` + `flex-direction: column` em mobile

---

## Ordem sugerida de resolução

```
INFRAESTRUTURA:
P1  (scaffold script)          ← desbloqueia tudo
P11 (pipeline-state snapshots) ← tracking correto
P7  (HR Review logs)           ← trilha de auditoria
P3  (threshold + flags)        ← gates funcionando

FASE 1:
P2  (interview.md)             ← log da entrevista
P5  (customer separado)        ← separação de papéis
P6  (blueprints lidos)         ← contexto de domínio
P4  (cross-validation)         ← consistência financeira
P14 (viabilidade negativa)     ← gate financeiro
P16 (mitigações detalhadas)    ← profundidade dos riscos

FASE 3 — HTML:
P8  (md-writer 3.1)            ← polimento dos drafts
P12 (glossário + tooltips)     ← acessibilidade de siglas
P13 (TCO: SVG → Chart.js)     ← gráfico correto
P15 (Esforço: SVG → CSS)      ← barras corretas
P17 (10th-man = auditor)       ← layout consistente
P18 (radar zones)              ← faixas visuais
P19 (SaaS tom executivo)       ← adaptar público

REDESIGN:
P20 (one-pager como orçamento) ← nova proposta de valor

FASE 1 — EXECUÇÃO:
P23 (blocos sequenciais)         ← 1 bloco por vez, na ordem
P24 (interview.md obrigatório)   ← sem log = fase inválida
P25 (especialistas proativos)    ← propor soluções, não apenas coletar
P26-P30 (bugs visuais HTML)      ← tooltips, alerts, radar, barras, TCO chart
P31 (tabs nos reports)           ← executive e complete precisam de tabs
P32 (acentuação PT-BR)           ← HTMLs sem acentos
P33 (playground.html ignorado)   ← reports não seguem o Design System
P34 (barras sempre horizontais CSS) ← Chart.js proibido para barras
P35 (ressalvas detalhadas)       ← auditor e 10th-man devem detalhar cada ressalva
P36 (responsividade mobile)      ← hamburger menu + footer centralizado

VIABILIDADE:
P21 (auditor alerta receita<TCO) ← finding crítico
P22 (cenários alternativos)      ← solution-architect gera alternativas viáveis

DOCS:
P9  (paths documentados)       ← polish
P10 (config herda briefing)    ← automatização
```
