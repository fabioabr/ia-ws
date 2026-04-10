---
title: Hallucination Guard
description: Regra de proteção contra alucinação de LLM — dados não verificáveis devem ser explicitamente sinalizados
project-name: global
version: 01.01.000
status: ativo
author: claude-code
category: core
area: tecnologia
tags:
  - core
  - alucinacao
  - verificacao
  - qualidade
created: 2026-04-05 10:00
---

# 🛡️ Hallucination Guard

Regra obrigatória que define como agentes de IA devem tratar **dados factuais** que não podem ser verificados em tempo de execução. Números, datas, preços, disponibilidade de APIs, custos de infraestrutura e qualquer claim factual gerado pela IA deve ser explicitamente classificado quanto à sua confiabilidade.

> [!danger] Regra inviolável
> **A IA NUNCA apresenta dados factuais como verdade absoluta sem fonte verificável.** Todo dado não verificado deve ser sinalizado explicitamente para revisão humana.

---

## 📏 Classificação de Dados

Todo dado factual gerado pela IA deve ser classificado em uma das três categorias:

| Categoria | Indicador | Descrição | Ação necessária |
| --------- | --------- | --------- | --------------- |
| ✅ **Verificado** | Fonte citada | Dado extraído de documento do projeto, resposta do cliente ou fonte confiável | Nenhuma — dado confiável |
| ⚠️ **Estimativa** | Cálculo do agente | Dado calculado ou inferido pela IA com base em padrões conhecidos | Revisão humana recomendada |
| ❓ **Não verificável** | LLM não tem acesso à fonte | Dado que a IA não pode confirmar (preços de mercado, disponibilidade de serviços, datas futuras) | Revisão humana **obrigatória** |

---

## 💬 Formato de Sinalização

Quando a IA gerar dados classificados como ⚠️ ou ❓, deve usar o seguinte callout:

```markdown
> [!warning] Dado não verificado
> [descrição do dado e por que não pode ser verificado]
```

### Exemplos

```markdown
> [!warning] Dado não verificado
> O custo estimado de R$ 5.000/mês para infraestrutura AWS é uma estimativa baseada em padrões típicos. Consulte a calculadora AWS para valores reais.

> [!warning] Dado não verificado
> O TCO de R$ 150.000 em 12 meses é uma projeção da IA. Validar com a área financeira antes de usar em decisões.
```

---

## 📋 Tipos de Dados que Exigem Sinalização

| Tipo de dado | Exemplos | Risco se não verificado |
| ------------ | -------- | ----------------------- |
| 💰 **Custos e preços** | TCO, licenças, infraestrutura, salários | Orçamento errado, projeto inviável |
| 📅 **Datas e prazos** | Lançamento de APIs, fim de suporte, deadlines de mercado | Planejamento baseado em premissas falsas |
| 📊 **Métricas de mercado** | Market share, taxas de adoção, benchmarks | Estratégia baseada em dados falsos |
| 🔧 **Disponibilidade técnica** | APIs existentes, compatibilidade de versões, limites de serviço | Arquitetura inviável |
| 📏 **Regulamentações** | LGPD, compliance setorial, requisitos legais | Risco legal |

---

## 🔍 Papel do Revisor

Qualquer agente ou pessoa que revise um documento tem responsabilidade de:

- **Identificar claims não sinalizados** — dados factuais apresentados como verdade sem fonte
- **Verificar se estimativas são plausíveis** — valores muito altos ou baixos devem ser questionados
- **Reportar dados não sinalizados como falha** — na seção de qualidade da revisão

---

## 🔄 Checklist de Auditoria

Ao revisar qualquer documento, verificar:

- [ ] ⚠️ **Dados não verificados** sinalizados com `> [!warning] Dado não verificado`
- [ ] ✅ Dados com fonte citada estão corretos
- [ ] ❓ Nenhum dado factual apresentado como verdade absoluta sem fonte

---

## 🔗 Documentos Relacionados

- [[core/behavior-principles/behavior-principles]] — Princípios de transparência e rastreabilidade

## 📜 Histórico de Alterações

| Versão    | Timestamp        | Descrição            |
| --------- | ---------------- | -------------------- |
| 01.00.000 | 2026-04-05 10:00 | Criação do documento — resposta ao finding #4 do challenger report |
| 01.01.000 | 2026-04-05 | Pipeline v2: "Fase 6" → "mini-ciclo de cada sub-etapa". "Creation Flow" → "Fluxo de Criação" |
