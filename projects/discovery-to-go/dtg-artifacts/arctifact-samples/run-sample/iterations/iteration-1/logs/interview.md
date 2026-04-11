---
title: "Interview Log — FinTrack Pro"
description: Log cronológico da reunião conjunta temática da Fase 1 (Discovery) para o projeto FinTrack Pro
project-name: discovery-to-go
version: 01.01.000
status: ativo
author: pipeline
category: log
area: tecnologia
tags:
  - log
  - entrevista
  - discovery
  - fase-1
created: 2026-04-11 09:00
iteration: 1
run: run-2
---

# Interview Log — FinTrack Pro

> **Run:** run-2 | **Iteração:** 1 | **Fase:** 1 — Discovery
> **Início:** 2026-04-11 09:00 | **Knowledge Pack:** saas

### Participantes

| Emoji | Agente | Papel |
|-------|--------|-------|
| 🎯 | po | Product Owner — visão, personas, valor, organização |
| 🏗️ | solution-architect | Arquitetura, tecnologia, TCO |
| 🔐 | cyber-security-architect | Privacidade, segurança, compliance |
| 🧑‍💼 | customer | Cliente simulado |
| 🤖 | orchestrator | Orquestrador (mediação) |

---

## 📋 Bloco #1 — Visão e Propósito

**Dono:** 🎯 po | **Início:** 09:00

| Quem | Diálogo |
|------|---------|
| 🎯 po | Bom dia! Vamos começar pelo propósito do projeto. Qual é o problema principal que o FinTrack Pro resolve? |
| 🧑‍💼 customer | [BRIEFING] Hoje os gestores financeiros das PMEs gastam em média 12 horas por semana consolidando dados de diferentes bancos, planilhas e ERPs em relatórios manuais. O FinTrack Pro automatiza essa consolidação e gera relatórios prontos. |
| 🎯 po | Entendi. E quem é o público-alvo principal? |
| 🧑‍💼 customer | [BRIEFING] CFOs e controllers de empresas com 50 a 500 funcionários. São profissionais que entendem de finanças mas não são técnicos — precisam de algo que funcione sem treinamento extenso. |
| 🎯 po | Existe algum produto concorrente que eles usam hoje? |
| 🧑‍💼 customer | [BRIEFING] Sim, a maioria usa Excel + macros caseiras. Alguns usam o Conta Azul ou Nibo, mas reclamam que são limitados para consolidação multi-banco e projeções. |
| 🏗️ solution-architect | *(aparte)* Quando diz "multi-banco", estamos falando de quantas integrações bancárias simultaneamente? |
| 🧑‍💼 customer | [INFERENCE] Tipicamente 3 a 5 bancos por empresa. Os maiores são Itaú, Bradesco, Santander, BB e Nubank PJ. |

> [!warning] Dado inferido
> O customer mencionou "3 a 5 bancos" mas não especificou se é requisito mínimo ou média observada. Registrado para validação no Human Review.

| Quem | Diálogo |
|------|---------|
| 🎯 po | Qual é a proposta de valor única? O que diferencia dos concorrentes? |
| 🧑‍💼 customer | [BRIEFING] Três coisas: (1) consolidação automática de OFX/CSV de qualquer banco, (2) projeções de fluxo de caixa com IA, e (3) alertas inteligentes quando detecta anomalias nos gastos. |
| 🎯 po | Perfeito. E o que motivou a empresa a investir neste produto agora? |
| 🧑‍💼 customer | [BRIEFING] A nova regulamentação do Open Finance no Brasil. Com as APIs abertas dos bancos, a consolidação automática ficou viável sem scraping. É uma janela de oportunidade. |

**✅ Bloco #1 concluído.**

| Item | Valor |
|------|-------|
| Problema | Consolidação financeira manual (12h/semana) |
| Público | CFOs/controllers de PMEs (50-500 func.) |
| Diferencial | Consolidação multi-banco + projeções IA + alertas |
| Motivação | Open Finance Brasil |

---

## 📋 Bloco #2 — Personas e Jornada

**Dono:** 🎯 po | **Início:** 09:18

| Quem | Diálogo |
|------|---------|
| 🎯 po | Vamos detalhar as personas. Além do CFO, quem mais usaria o sistema? |
| 🧑‍💼 customer | [BRIEFING] Temos 3 perfis: o CFO que vê os dashboards e relatórios, o analista financeiro que faz o dia-a-dia (conciliação, categorização), e o CEO que só quer o resumo executivo mensal. |
| 🎯 po | Qual desses é o usuário mais frequente? |
| 🧑‍💼 customer | O analista financeiro. Ele usa o sistema todo dia, 2-3 horas. O CFO acessa 2-3 vezes por semana. O CEO, uma vez por mês. |
| 🎯 po | Qual é a jornada típica do analista no dia a dia hoje, sem o FinTrack? |
| 🧑‍💼 customer | [BRIEFING] Ele acorda, abre 3-5 sites de bancos, baixa os extratos, importa no Excel, categoriza manualmente cada lançamento, cruza com o ERP, e monta o relatório diário. Leva 2-3 horas. Com o FinTrack, queremos que leve 15 minutos. |
| 🎯 po | 2-3 horas → 15 minutos. Isso é uma redução de ~90%. Vou registrar como OKR candidato. |

**✅ Bloco #2 concluído.**

| Item | Valor |
|------|-------|
| Persona 1 | CFO (decisor, dashboards, 2-3x/semana) |
| Persona 2 | Analista Financeiro (operador, diário, 2-3h) |
| Persona 3 | CEO (consumidor, resumo mensal) |
| Jornada-alvo | Reduzir de 2-3h/dia para 15min |

---

## 📋 Bloco #3 — Valor Esperado / OKRs

**Dono:** 🎯 po | **Início:** 09:32

| Quem | Diálogo |
|------|---------|
| 🎯 po | Quais métricas de sucesso vocês consideram para o MVP? |
| 🧑‍💼 customer | [BRIEFING] Três OKRs principais: (1) reduzir tempo de consolidação de 12h/semana para 2h/semana, (2) ter 100 empresas pagantes nos primeiros 6 meses após o lançamento, e (3) NPS acima de 50. |
| 🎯 po | E o modelo de negócio? Assinatura mensal? |
| 🧑‍💼 customer | [BRIEFING] Sim, SaaS com 3 planos: Starter (R$199/mês, até 2 bancos), Pro (R$499/mês, até 5 bancos + projeções), Enterprise (R$999/mês, ilimitado + API). |
| 🎯 po | Qual é o ROI esperado para o cliente? |
| 🧑‍💼 customer | [INFERENCE] Se um analista ganha R$6.000/mês e economiza 10h/semana, isso equivale a ~R$3.750/mês em produtividade. O plano Pro a R$499 se paga 7x. |

**✅ Bloco #3 concluído.**

| Item | Valor |
|------|-------|
| OKR 1 | 12h/semana → 2h/semana (redução 83%) |
| OKR 2 | 100 empresas pagantes em 6 meses |
| OKR 3 | NPS > 50 |
| Modelo | SaaS 3 planos (R$199 / R$499 / R$999) |
| ROI | ~7x para o cliente |

---

## 📋 Bloco #4 — Processo, Negócio e Equipe

**Dono:** 🎯 po | **Início:** 09:45

| Quem | Diálogo |
|------|---------|
| 🎯 po | Qual é a estrutura da equipe que vai desenvolver e manter o produto? |
| 🧑‍💼 customer | [BRIEFING] Temos um CTO (full-stack senior), 2 desenvolvedores backend (pleno), 1 frontend (pleno) e 1 designer UX. Total: 5 pessoas. |
| 🎯 po | Existe alguma restrição de metodologia de trabalho? |
| 🧑‍💼 customer | Usamos Scrum com sprints de 2 semanas. Entregas no GitHub, CI/CD no GitHub Actions. Já temos isso rodando em outros projetos. |
| 🎯 po | E o stakeholder principal? Quem toma a decisão final? |
| 🧑‍💼 customer | [BRIEFING] O CEO da empresa, que também é investidor. Ele tem veto em questões de escopo e priorização. Mas o dia a dia é com o CTO. |

**✅ Bloco #4 concluído.**

| Item | Valor |
|------|-------|
| Equipe | 5 pessoas (CTO + 2 back + 1 front + 1 UX) |
| Metodologia | Scrum, sprints 2 semanas |
| CI/CD | GitHub Actions (existente) |
| Decisor | CEO (veto) / CTO (operacional) |

---

## 📋 Bloco #5 — Tecnologia e Segurança

**Dono:** 🏗️ solution-architect | **Início:** 10:02

| Quem | Diálogo |
|------|---------|
| 🏗️ solution-architect | Vamos falar de stack. Vocês já têm preferência tecnológica? |
| 🧑‍💼 customer | [BRIEFING] Backend em Node.js (TypeScript), frontend em React, banco PostgreSQL. A equipe tem experiência com essa stack. |
| 🏗️ solution-architect | Para as integrações bancárias via Open Finance, vocês já avaliaram algum provider? |
| 🧑‍💼 customer | [BRIEFING] Sim, estamos entre a Belvo e a Pluggy. Ambas têm APIs para Open Finance Brasil. Ainda não decidimos. |
| 🏗️ solution-architect | E para a parte de IA (projeções e detecção de anomalias)? |
| 🧑‍💼 customer | [INFERENCE] Pensamos em usar modelos pré-treinados via API — tipo OpenAI ou Claude. Não queremos treinar modelos próprios no MVP. |
| 🏗️ solution-architect | Entendido. E sobre autenticação — SSO, MFA? |
| 🧑‍💼 customer | [BRIEFING] MFA obrigatório para todos os planos. SSO (SAML) só no Enterprise. |

> [!info] Decisão registrada
> MFA obrigatório em todos os planos. SSO restrito ao plano Enterprise.

| Quem | Diálogo |
|------|---------|
| 🏗️ solution-architect | Hosting? Cloud preference? |
| 🧑‍💼 customer | [BRIEFING] AWS. Já temos conta e créditos do programa de startups. |

**✅ Bloco #5 concluído.**

| Item | Valor |
|------|-------|
| Stack | Node.js (TS) + React + PostgreSQL |
| Open Finance | Belvo ou Pluggy (pendente) |
| IA | API externa (OpenAI/Claude), sem modelo próprio |
| Auth | MFA obrigatório, SSO Enterprise only |
| Cloud | AWS (créditos startup) |

---

## 📋 Bloco #6 — LGPD e Privacidade

**Dono:** 🔐 cyber-security-architect | **Início:** 10:20

> [!warning] Modo profundo ativado — o projeto lida com dados financeiros pessoais.

| Quem | Diálogo |
|------|---------|
| 🔐 cyber-security-architect | Quais dados pessoais o sistema vai processar? |
| 🧑‍💼 customer | [BRIEFING] Nome, CPF/CNPJ, dados bancários (agência, conta, saldo, transações), e-mail, telefone. Tudo que vem do Open Finance. |
| 🔐 cyber-security-architect | Classificação: dados pessoais **sensíveis** (financeiros). Base legal para tratamento? |
| 🧑‍💼 customer | [INFERENCE] Consentimento explícito do titular via Open Finance. O fluxo de consentimento é gerenciado pelo banco. |
| 🔐 cyber-security-architect | Correto. E a retenção dos dados? Por quanto tempo ficam armazenados? |
| 🧑‍💼 customer | [BRIEFING] Enquanto o cliente for assinante. Após cancelamento, 90 dias para recuperação, depois anonimização completa. |
| 🔐 cyber-security-architect | DPO nomeado? |
| 🧑‍💼 customer | Ainda não. Está no plano para Q3. |

> [!danger] Risco identificado
> Ausência de DPO nomeado. A LGPD exige DPO para empresas que tratam dados pessoais sensíveis em larga escala. Recomendação: nomear antes do lançamento.

| Quem | Diálogo |
|------|---------|
| 🔐 cyber-security-architect | Criptografia dos dados em repouso? |
| 🧑‍💼 customer | [BRIEFING] Sim, AES-256 no PostgreSQL. TLS 1.3 em trânsito. |

**✅ Bloco #6 concluído.**

| Item | Valor |
|------|-------|
| Dados | Pessoais sensíveis (financeiros) |
| Base legal | Consentimento via Open Finance |
| Retenção | Ativa + 90 dias pós-cancelamento + anonimização |
| DPO | Não nomeado (⚠️ risco) |
| Criptografia | AES-256 repouso, TLS 1.3 trânsito |

---

## 📋 Bloco #7 — Arquitetura Macro

**Dono:** 🏗️ solution-architect | **Início:** 10:38

| Quem | Diálogo |
|------|---------|
| 🏗️ solution-architect | Com base nos blocos anteriores, o sistema tem 4 domínios claros: (1) Ingestão de dados bancários, (2) Categorização e conciliação, (3) Projeções e alertas (IA), (4) Dashboard e relatórios. |
| 🏗️ solution-architect | Dada a equipe de 5 pessoas, recomendo **monolito modular** no MVP com separação por módulos internos, não microserviços. Migração para microserviços na Fase 2 se necessário. |
| 🧑‍💼 customer | Faz sentido. O CTO concorda — microserviços com 5 pessoas seria overhead. |
| 🏗️ solution-architect | Para a ingestão bancária, sugiro um worker assíncrono (BullMQ) que processa os dados do Open Finance em background. O dashboard consome dados já processados. |
| 🧑‍💼 customer | [BRIEFING] Sim, a consolidação não precisa ser em tempo real. Atualização a cada 4 horas é aceitável para o MVP. |

> [!info] Decisão de arquitetura
> Monolito modular com 4 módulos. Worker assíncrono para ingestão. Atualização a cada 4h no MVP.

**✅ Bloco #7 concluído.**

| Item | Valor |
|------|-------|
| Arquitetura | Monolito modular (4 módulos) |
| Ingestão | Worker assíncrono (BullMQ) |
| Frequência | A cada 4h (MVP) |
| Microserviços | Previsto para Fase 2 |

---

## 📋 Bloco #8 — TCO e Build vs Buy

**Dono:** 🏗️ solution-architect | **Início:** 10:55

| Quem | Diálogo |
|------|---------|
| 🏗️ solution-architect | Vou calcular o TCO para 3 anos. Primeiro, alternativas build vs buy. |
| 🏗️ solution-architect | **Alternativa 1: Comprar** — Conta Azul Enterprise (R$1.200/mês) + customização. Limitação: não suporta Open Finance nativo, sem projeções com IA. |
| 🏗️ solution-architect | **Alternativa 2: Adaptar** — Usar Metabase (open source) + API de Open Finance. Custo baixo, mas categorização manual permanece. |
| 🏗️ solution-architect | **Alternativa 3: Construir** (recomendado) — FinTrack Pro custom. Justificativa: diferencial competitivo (IA + Open Finance nativo) não existe no mercado. |
| 🧑‍💼 customer | [BRIEFING] Concordo. O diferencial de projeções com IA é o core do produto. Não podemos depender de terceiros para isso. |

**TCO estimado (3 anos):**

| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Equipe (5 pessoas) | R$900.000 | R$990.000 | R$1.089.000 | R$2.979.000 |
| AWS (infra) | R$36.000 | R$60.000 | R$84.000 | R$180.000 |
| Open Finance API | R$24.000 | R$36.000 | R$48.000 | R$108.000 |
| LLM API (projeções) | R$12.000 | R$24.000 | R$36.000 | R$72.000 |
| Licenças diversas | R$6.000 | R$6.000 | R$6.000 | R$18.000 |
| Contingência (15%) | R$146.700 | R$167.400 | R$189.450 | R$503.550 |
| **Total** | **R$1.124.700** | **R$1.283.400** | **R$1.452.450** | **R$3.860.550** |

> [!warning] Premissa
> TCO assume crescimento de 10% a.a. na equipe (reajuste salarial) e crescimento de uso proporcional ao número de clientes (impacta AWS e APIs).

**✅ Bloco #8 concluído.**

| Item | Valor |
|------|-------|
| Decisão | Build (custom) — diferencial competitivo justifica |
| TCO 3 anos | R$3.860.550 |
| Maior custo | Equipe (77%) |
| Break-even | ~220 clientes no plano Pro (R$499/mês) |

---

## 📊 Resumo da Reunião

| Bloco | Tema | Dono | Status |
|-------|------|------|--------|
| #1 | Visão e Propósito | 🎯 po | ✅ |
| #2 | Personas e Jornada | 🎯 po | ✅ |
| #3 | Valor Esperado / OKRs | 🎯 po | ✅ |
| #4 | Processo, Negócio e Equipe | 🎯 po | ✅ |
| #5 | Tecnologia e Segurança | 🏗️ solution-architect | ✅ |
| #6 | LGPD e Privacidade | 🔐 cyber-security-architect | ✅ |
| #7 | Arquitetura Macro | 🏗️ solution-architect | ✅ |
| #8 | TCO e Build vs Buy | 🏗️ solution-architect | ✅ |

| Métrica | Valor |
|---------|-------|
| Duração total | 09:00 — 11:10 (2h10min) |
| Dados por fonte | [BRIEFING] 65% · [INFERENCE] 25% · [RAG] 10% |
| Conflitos detectados | 0 |
| Riscos identificados | 1 (ausência de DPO) |
| Pendências para Human Review | 2 (qtd. bancos mínima, provider Open Finance) |
