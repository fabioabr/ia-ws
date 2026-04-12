---
region-id: REG-QUAL-02
title: "10th Man Questions"
group: quality
description: "Contrarian questions raised by the 10th-man challenging key assumptions"
source: "Fase 2 (10th-man) → 2.2"
schema: "Lista de questões com severidade"
template-visual: "Card list com severity badges"
default: true
---

# 10th Man Questions

Lista as questoes provocativas levantadas pelo 10th-man — o agente que deliberadamente desafia as premissas do discovery. Cada questao tem severidade associada e indica se foi respondida satisfatoriamente ou permanece em aberto. Questoes criticas nao respondidas podem bloquear a aprovacao.

## Schema de dados

```yaml
tenth_man_questions:
  questions:
    - id: string                 # Identificador (ex: 10M-01)
      question: string           # A questao provocativa
      severity: string           # Critica / Alta / Media
      target_block: string       # Bloco do pipeline que a questao desafia
      status: string             # Respondida / Parcialmente respondida / Em aberto
      response: string           # Resposta (se houver)
  findings:
    - title: string              # Titulo da ressalva (ex: "Bus Factor — Risco de Pessoa Unica")
      dimension: string          # Dimensao afetada (Divergencia / Robustez / Completude Critica)
      score_impact: string       # Como afeta o score (ex: "Robustez: 78%")
      severity: string           # Critica / Alta / Media
      description: string        # 2-3 frases: O QUE foi identificado
      why_important: string      # 1-2 frases: impacto se nao enderecado
      recommendation: string     # O que fazer para resolver
```

## Exemplo

### Questoes

- **[Critica] 10M-01:** "Se o Open Finance nao atingir 80% de cobertura bancaria, o produto ainda entrega valor suficiente para justificar o investimento?" — *Em aberto*

- **[Critica] 10M-02:** "O mercado de PMEs ja tem players estabelecidos (ContaAzul, Nibo). Qual e o diferencial defensavel do FinTrack Pro que impede copia em 6 meses?" — *Parcialmente respondida: diferencial e a integracao nativa com Open Finance, mas nao ha barreira de entrada tecnica.*

- **[Alta] 10M-03:** "A estimativa de churn de 3% e baseada em benchmark de mercado ou em dados proprios? Produtos financeiros para PMEs tipicamente tem churn de 5-7%." — *Respondida: benchmark de mercado; sera validado com cohort do beta.*

- **[Alta] 10M-04:** "O time nunca trabalhou com multi-tenancy por schema. Isso nao deveria ser um risco tecnico critico em vez de 'alta complexidade'?" — *Respondida: spike tecnico planejado para sprint 1; fallback para row-level isolation.*

- **[Media] 10M-05:** "Os custos de suporte e customer success estao ausentes do TCO. Quem faz onboarding dos clientes no ano 1?" — *Em aberto*

### Findings detalhados

**Finding 1 — Bus Factor: Risco de Pessoa Unica**
- **Dimensao:** Robustez | **Score impact:** Robustez: 72%
- **Severidade:** Critica
- **Descricao:** O discovery identifica apenas 1 desenvolvedor senior com conhecimento em Open Finance no time. Toda a arquitetura de integracao bancaria depende dessa pessoa. Nao ha plano de redundancia ou documentacao de transferencia de conhecimento.
- **Por que e importante:** Se essa pessoa sair ou ficar indisponivel, o projeto perde a capacidade de entregar a feature core (integracao Open Finance), atrasando o roadmap em 3-6 meses ate contratar e capacitar substituto.
- **Recomendacao:** Exigir plano de pair-programming obrigatorio nas sprints 1-3 para transferencia de conhecimento + documentacao de decisoes arquiteturais de integracao.

**Finding 2 — TCO sem Custos de Suporte e Customer Success**
- **Dimensao:** Completude Critica | **Score impact:** Completude Critica: 65%
- **Severidade:** Alta
- **Descricao:** O TCO apresentado no bloco 1.8 nao inclui custos de suporte tecnico, customer success e onboarding. Para um SaaS B2B com 200+ clientes projetados no ano 1, esses custos representam tipicamente 15-25% do custo operacional total.
- **Por que e importante:** A analise financeira esta subestimada. O ponto de break-even pode estar 6-12 meses adiante do projetado, tornando o caso de negocio fragil.
- **Recomendacao:** Incluir no TCO: 1 analista de suporte (R$ 8k/mes), 1 CS (R$ 12k/mes) a partir do mes 3, ferramentas de suporte (Zendesk/Intercom ~R$ 2k/mes). Recalcular break-even.

**Finding 3 — Premissa de Churn Otimista sem Base Propria**
- **Dimensao:** Divergencia | **Score impact:** Divergencia: 78%
- **Severidade:** Alta
- **Descricao:** O discovery assume churn mensal de 3% baseado em benchmark generico de SaaS. Produtos financeiros para PMEs no Brasil tipicamente apresentam churn de 5-7% nos primeiros 18 meses. Nao ha dados proprios ou validacao com potenciais clientes para sustentar a premissa otimista.
- **Por que e importante:** A diferenca entre 3% e 6% de churn muda o tamanho da base ativa em 12 meses de ~1.500 para ~900 clientes, impactando diretamente receita projetada e viabilidade financeira.
- **Recomendacao:** Modelar cenarios com churn de 3%, 5% e 7%. Validar premissa de churn com entrevistas de 5-10 PMEs do segmento-alvo antes de fechar o business case.

## Representacao Visual

### Dados de amostra

```yaml
tenth_man_questions:
  questions:
    - id: "10M-01"
      question: "Se o Open Finance nao atingir 80% de cobertura bancaria, o produto ainda entrega valor suficiente?"
      severity: "Critica"
      status: "Em aberto"
    - id: "10M-02"
      question: "Qual e o diferencial defensavel que impede copia em 6 meses?"
      severity: "Critica"
      status: "Parcialmente respondida"
    - id: "10M-03"
      question: "A estimativa de churn de 3% e baseada em dados proprios?"
      severity: "Alta"
      status: "Respondida"
    - id: "10M-04"
      question: "Multi-tenancy por schema nao deveria ser risco critico?"
      severity: "Alta"
      status: "Respondida"
    - id: "10M-05"
      question: "Custos de suporte e CS estao ausentes do TCO?"
      severity: "Media"
      status: "Em aberto"
  findings:
    - title: "Bus Factor — Risco de Pessoa Unica"
      dimension: "Robustez"
      score_impact: "Robustez: 72%"
      severity: "Critica"
      description: "Apenas 1 dev senior com conhecimento em Open Finance. Sem plano de redundancia."
      why_important: "Saida dessa pessoa atrasa roadmap em 3-6 meses."
      recommendation: "Pair-programming obrigatorio + documentacao de decisoes arquiteturais."
    - title: "TCO sem Custos de Suporte e CS"
      dimension: "Completude Critica"
      score_impact: "Completude Critica: 65%"
      severity: "Alta"
      description: "TCO nao inclui suporte, CS e onboarding — 15-25% do custo operacional."
      why_important: "Break-even pode estar 6-12 meses adiante do projetado."
      recommendation: "Incluir suporte + CS + ferramentas no TCO e recalcular break-even."
    - title: "Premissa de Churn Otimista sem Base Propria"
      dimension: "Divergencia"
      score_impact: "Divergencia: 78%"
      severity: "Alta"
      description: "Churn de 3% baseado em benchmark generico; mercado real e 5-7%."
      why_important: "Diferenca muda base ativa de 1.500 para 900 clientes em 12 meses."
      recommendation: "Modelar cenarios 3%/5%/7% e validar com entrevistas de PMEs."
```

### Recomendação do Chart Specialist

**Veredicto:** GRÁFICO + CARD
**Tipo:** Radar chart 3 eixos (Chart.js) + cards detalhados por ressalva (HTML/CSS) com borda colorida por severidade
**Tecnologia:** Chart.js (radar) + HTML/CSS (cards com borda colorida)
**Justificativa:** O 10th-man tem 3 dimensões com scores numéricos — mesmo padrão do auditor (5 dimensões). Usar radar chart para consistência visual entre as duas validações da Fase 2. Cards mantidos abaixo para as questões individuais.
**Alternativa:** Stat cards com scores (sem radar) — quando há apenas 2 dimensões ou menos
