---
title: Scoring Thresholds — Default
description: Thresholds padrão dos gates automatizados (auditor e 10th-man) do Discovery Pipeline. Define média mínima, pisos por dimensão e profiles pré-configurados (standard, POC, high-risk). Projetos podem customizar localmente.
project-name: global
version: 01.00.000
status: ativo
author: claude-code
category: customization
area: tecnologia
tags:
  - customization
  - scoring
  - auditor
  - 10th-man
  - pipeline-v05
created: 2026-04-10
---

# Scoring Thresholds — Default

> [!info] Como este arquivo é usado
> O `auditor` e o `10th-man` leem este arquivo (ou a cópia local em `{projeto}/customization/`) para saber quais **pisos por dimensão** e **média mínima** aplicar. Se o arquivo não existir, usam os defaults hardcoded nos próprios SKILLs (que são iguais ao profile `standard` abaixo).
>
> **Prioridade:** `{projeto}/customization/scoring-thresholds.md` > `behavior/templates/customization/scoring-thresholds.md` > fallback do SKILL.md.

---

## 1. Profile ativo

```
active-profile: standard
```

Altere a linha acima para trocar o profile. Profiles disponíveis: `standard`, `poc`, `high-risk`, `custom`.

---

## 2. Profiles pré-configurados

### standard (padrão)

Usado na maioria dos projetos. Balanceia rigor e praticidade.

**Auditor — 5 dimensões:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Completude | 25% | 80% |
| Fundamentação | 25% | 70% |
| Coerência interna | 20% | 70% |
| Profundidade | 15% | 60% |
| Neutralidade | 15% | 70% |

**Média mínima auditor:** ≥ 90%

**10th-man — 3 dimensões:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Cobertura divergente | 50% | 70% |
| Fundamentação áreas sensíveis | 30% | 70% |
| Antipatterns e edge cases | 20% | 50% |

**Média mínima 10th-man:** ≥ 90%

---

### poc (provas de conceito, MVPs exploratórios)

Thresholds relaxados — aceita mais inferência, foco em velocidade.

**Auditor:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Completude | 25% | 65% |
| Fundamentação | 25% | 55% |
| Coerência interna | 20% | 60% |
| Profundidade | 15% | 45% |
| Neutralidade | 15% | 60% |

**Média mínima auditor:** ≥ 80%

**10th-man:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Cobertura divergente | 50% | 55% |
| Fundamentação áreas sensíveis | 30% | 55% |
| Antipatterns e edge cases | 20% | 40% |

**Média mínima 10th-man:** ≥ 80%

---

### high-risk (projetos regulados, alto impacto, compliance crítico)

Thresholds elevados — exige fundamentação forte, tolera pouca inferência.

**Auditor:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Completude | 25% | 90% |
| Fundamentação | 25% | 85% |
| Coerência interna | 20% | 80% |
| Profundidade | 15% | 75% |
| Neutralidade | 15% | 80% |

**Média mínima auditor:** ≥ 95%

**10th-man:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Cobertura divergente | 50% | 80% |
| Fundamentação áreas sensíveis | 30% | 80% |
| Antipatterns e edge cases | 20% | 65% |

**Média mínima 10th-man:** ≥ 95%

---

### custom (definido pelo projeto)

Se nenhum profile pré-configurado serve, o projeto pode definir valores específicos. Preencha a tabela abaixo:

**Auditor custom:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Completude | ___% | ___% |
| Fundamentação | ___% | ___% |
| Coerência interna | ___% | ___% |
| Profundidade | ___% | ___% |
| Neutralidade | ___% | ___% |

**Média mínima auditor:** ≥ ___%

**10th-man custom:**

| Dimensão | Peso | Piso mínimo |
|---|---|---|
| Cobertura divergente | ___% | ___% |
| Fundamentação áreas sensíveis | ___% | ___% |
| Antipatterns e edge cases | ___% | ___% |

**Média mínima 10th-man:** ≥ ___%

---

## 3. Regras gerais (aplicam a todos os profiles)

1. **Pisos são absolutos.** Qualquer dimensão abaixo do piso = reprova automática, independente da média.
2. **Média ponderada é o segundo filtro.** Só é considerada se todos os pisos foram atendidos.
3. **Quando o auditor reprova, o 10th-man continua** (rodam em paralelo — ambos sempre terminam).
4. **Pesos podem mudar entre profiles** mas os **nomes das dimensões são fixos** na v0.5.

---

## Changelog

| Versão | Data | Descrição |
|---|---|---|
| 01.00.000 | 2026-04-10 | Versão inicial. 3 profiles (standard, poc, high-risk) + custom. |
