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
```

## Exemplo

- **[Critica] 10M-01:** "Se o Open Finance nao atingir 80% de cobertura bancaria, o produto ainda entrega valor suficiente para justificar o investimento?" — *Em aberto*

- **[Critica] 10M-02:** "O mercado de PMEs ja tem players estabelecidos (ContaAzul, Nibo). Qual e o diferencial defensavel do FinTrack Pro que impede copia em 6 meses?" — *Parcialmente respondida: diferencial e a integracao nativa com Open Finance, mas nao ha barreira de entrada tecnica.*

- **[Alta] 10M-03:** "A estimativa de churn de 3% e baseada em benchmark de mercado ou em dados proprios? Produtos financeiros para PMEs tipicamente tem churn de 5-7%." — *Respondida: benchmark de mercado; sera validado com cohort do beta.*

- **[Alta] 10M-04:** "O time nunca trabalhou com multi-tenancy por schema. Isso nao deveria ser um risco tecnico critico em vez de 'alta complexidade'?" — *Respondida: spike tecnico planejado para sprint 1; fallback para row-level isolation.*

- **[Media] 10M-05:** "Os custos de suporte e customer success estao ausentes do TCO. Quem faz onboarding dos clientes no ano 1?" — *Em aberto*

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
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo narrativo listando as questoes por severidade, destacando as em aberto e seus impactos potenciais | Relatorios executivos, documentos formais onde formato livre e preferido |
| Tabela | Tabela com colunas ID, Questao, Severidade, Status e Resposta | Visao completa para revisao tecnica, rastreamento de resolucao |
| Card list com severity badges | Cards individuais por questao, com badge colorido de severidade (vermelho=Critica, laranja=Alta, amarelo=Media) e indicador de status | Dashboards, apresentacoes visuais, revisoes de qualidade onde destaque visual de severidade e importante |
| Lista agrupada por severidade | Questoes organizadas em grupos (Critica, Alta, Media) com contagem por grupo e indicador de questoes em aberto | Priorizacao de resolucao, reunioes de triagem |
| Kanban por status | Colunas Em aberto, Parcialmente respondida, Respondida com cards das questoes | Acompanhamento do progresso de resolucao das questoes |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
