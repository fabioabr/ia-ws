---
title: Briefing Template
description: Template do briefing inicial que o cliente humano escreve antes de iniciar a Fase 1 do Discovery Pipeline v0.5. É a única pré-condição obrigatória do pipeline.
project-name: discovery-to-go
version: 00.01.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - briefing
  - discovery
  - pipeline-v05
created: 2026-04-07
---

# Briefing Template

> [!info] Como usar
> Copie este template para `{seu-projeto}/briefing.md` e preencha. Sem este arquivo o pipeline **não inicia**. Quanto mais rico e específico, melhor a primeira iteração — cada lacuna vira `[INFERENCE]` do customer.
>
> Não precisa ser perfeito. O pipeline tem 2 gates humanos justamente para corrigir lacunas em iterações seguintes. Mas o briefing precisa ter o mínimo de cada seção marcada como obrigatória.

---

## Frontmatter (obrigatório)

```markdown
---
title: Briefing — {Nome do Projeto}
project-name: {slug-do-projeto}
project-type: {saas | datalake-ingestion | process-documentation | web-microservices | generic}
author: {nome do cliente}
created: YYYY-MM-DD
status: ativo
---
```

> [!tip] project-type
> Se você sabe o tipo, declare. Se não souber, deixe `generic` ou omita — o orchestrator tenta auto-detectar pelo conteúdo do briefing. Se ele errar, você corrige no próximo restart manual.

---

## 1. Problema (🔴 obrigatório)

**O que queremos resolver?**

Descreva em 2-5 parágrafos o problema central. Foque no **problema**, não na solução. Bom: "analistas perdem 3 dias por mês conciliando dados manualmente". Ruim: "queremos um sistema de conciliação automática".

```
{seu texto aqui}
```

---

## 2. Domínio (🔴 obrigatório)

**Em que área de negócio estamos?**

- Setor / indústria
- Função organizacional (RH, Financeiro, Operações, Tech, Produto, etc.)
- Maturidade da área (greenfield, evolução, modernização, substituição)
- Contexto organizacional relevante (empresa familiar, startup, multinacional, regulada)

```
{seu texto aqui}
```

---

## 3. Stakeholders conhecidos (🔴 obrigatório)

**Quem está envolvido?**

Liste pessoas/papéis com nome ou função. Pelo menos 1 dono do produto e 1 dono do orçamento.

| Nome / Papel | Função no projeto | Disponível para entrevista? |
|---|---|---|
| {ex: Maria, Head de Operações} | Patrocinadora, decisora final | Sim, semanalmente |
| {ex: João, Analista Sênior} | Usuário primário | Sim, em call de 30min |
| {ex: TI Corporativa} | Aprova stack e infra | Não — comunicação por email |

---

## 4. Restrições conhecidas (🟡 recomendado)

**O que já sabemos que limita?**

Anote tudo que **não pode mudar** ou **tem peso forte** na decisão. Quanto mais aqui, menos `[INFERENCE]` o customer precisa fazer nas áreas do solution-architect e cyber-security-architect.

- **Prazo:** {ex: precisa estar em produção até 30/06/2026}
- **Stack obrigatória:** {ex: Azure, .NET 8, SQL Server}
- **Stack proibida:** {ex: AWS, MongoDB, qualquer NoSQL}
- **Equipe:** {ex: time interno de 4 devs Python; sem orçamento para contratar}
- **Compliance:** {ex: LGPD obrigatório, dados ficam no Brasil}
- **Orçamento aproximado:** {ex: até R$ 800k no primeiro ano — ou "calcular como output"}
- **Integrações obrigatórias:** {ex: SAP S/4HANA, Salesforce}
- **Outros limites:** {qualquer coisa relevante}

> [!warning] Se o orçamento é fechado
> Declare. Se for "calcular como output", o `solution-architect` calcula TCO no bloco 8 e entrega como resultado. Os dois modos são suportados.

---

## 5. Fontes de conhecimento disponíveis (🟡 recomendado)

**De onde a IA pode buscar informação além deste briefing?**

- [ ] **Enterprise RAG configurado?** Qual base? Caminho?
- [ ] **Documentos anexos?** Lista de arquivos
- [ ] **Entrevistas prévias?** Transcritas? Onde?
- [ ] **Sistemas legados?** Documentação técnica disponível?
- [ ] **Concorrentes / benchmarks?** Algum estudo prévio?

```
{liste tudo que tiver — se não tiver nada, declare "apenas este briefing"}
```

---

## 6. Expectativa de entrega (🔴 obrigatório)

**O que o cliente espera ver no final do discovery?**

Marque com [x] o que se aplica e adicione específicos:

- [ ] Product Vision Document (visão executiva)
- [ ] Definição clara de fronteiras (tecnologia, segurança, processo)
- [ ] Arquitetura macro do projeto
- [ ] Análise estratégica (build vs buy + TCO calculado)
- [ ] Backlog priorizado (MVP + Fase 2 + Fase 3)
- [ ] Matriz de riscos
- [ ] Apresentação HTML para sponsor
- [ ] Outros: {especificar}

**Quem é o público desta entrega final?**

```
{ex: comitê executivo / comitê técnico / time de implementação / cliente final}
```

---

## 7. Configurações opcionais (🟢 opcional)

### 7.1 Threshold dos gates (default: ≥ 90%)

Por padrão o auditor e o 10th-man precisam de **nota média ≥ 90%** + **pisos por dimensão**. Você pode ajustar:

- **Modo padrão:** ≥ 90% (recomendado)
- **Modo alto risco:** ≥ 95% (projetos críticos / regulados)
- **Modo POC:** ≥ 80% (validação rápida)

```
threshold: padrão
```

### 7.2 Modo de participação do cliente humano

- **Observador passivo (padrão):** cliente acompanha entrevistas mas só comenta no resultado
- Outros modos não disponíveis na v0.5

```
modo: observador passivo
```

---

## 8. Notas livres (🟢 opcional)

Qualquer contexto adicional que não cabe nas seções acima. História do projeto, tentativas anteriores, percepções pessoais, política interna relevante, etc.

```
{texto livre}
```

---

## ✅ Checklist antes de iniciar

Antes de mandar o orchestrator iniciar a Fase 1, confirme:

- [ ] Seções 1, 2, 3 e 6 preenchidas (obrigatórias)
- [ ] Project-type declarado ou aceito como auto-detect
- [ ] Stakeholder com autoridade para revisar o Human Review das Fases 1 (Discovery) e 2 (Challenge) está identificado
- [ ] Cliente final identificado como revisor do Human Review da Fase 3 (Delivery)
- [ ] Cliente humano sabe que vai acompanhar como observador durante a reunião da Fase 1
- [ ] Briefing salvo em `{projeto}/briefing.md`

**Pronto. Comande o orchestrator: `iniciar discovery v0.5`**
