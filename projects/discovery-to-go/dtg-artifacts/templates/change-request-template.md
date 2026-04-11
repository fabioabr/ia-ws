---
title: Change Request Template
description: Template do change request compilado pelo orchestrator quando qualquer passagem pelo Human Review compartilhado é reprovada (Fase 1, 2 ou 3 macro). Lista pontos afetados, possíveis impactos cross-eixo e instruções para a próxima iteração. Usado como entrada do Update State na Pipeline Memory.
project-name: discovery-to-go
version: 02.00.000
status: ativo
author: claude-code
category: template
area: tecnologia
tags:
  - template
  - change-request
  - orchestrator
  - pipeline-v05
created: 2026-04-07
---

# Change Request Template

> [!info] Quando é gerado
> Este template é preenchido pelo `orchestrator` sempre que uma passagem pelo Human Review compartilhado termina em reprova:
> - **Fase 1 (Discovery)** reprovou no HR (humano não aceitou os drafts da reunião)
> - **Fase 2 (Challenge)** reprovou no HR (auditor/10th-man não passaram OU humano reprovou as observações dos gates)
> - **Fase 3 (Delivery)** reprovou no HR (cliente final não aprovou o Delivery Report)
>
> O change request é salvo dentro do arquivo de memory correspondente: `iteration-{i}/memory/after-phase-{N}.md`. O orchestrator faz **Update State** na Pipeline Memory. A próxima iteração consome este arquivo como input principal.

---

## Frontmatter

```markdown
---
title: Change Request — Iteration {i}, after Phase {N}
project-name: {slug}
iteration: {i}
phase-macro-rejected: {1 | 2 | 3}
generated-at: YYYY-MM-DD HH:mm
generated-by: orchestrator
next-iteration: {i+1}
update-state-target: pipeline-memory
sources:
  - {ex: human-review-after-discovery.md}
  - {ex: audit-report.md}
  - {ex: challenge-report.md}
---
```

---

## 1. Contexto da reprova

**Quem reprovou:** {humano | auditor | 10th-man | múltiplos}

**Motivação principal:** {1-3 frases sobre o motivo dominante}

**Severidade geral:** {baixa | média | alta | crítica}

**Posição no fluxo:**
```
Iteração {i}
  ├── Setup  ✅ (one-shot, não refaz)
  ├── Fase 1 (Discovery)  {✅/❌ no HR}
  ├── Fase 2 (Challenge)  {✅/❌ no HR / skipped}
  └── Fase 3 (Delivery)   {✅/❌ no HR / skipped}
       │
       └── Reprova → Update State → próxima iteração: {i+1}
```

---

## 2. Itens explicitamente apontados

### 2.1 Críticos (precisam ser corrigidos)

| # | Onde | O que mudar | Origem |
|---|---|---|---|
| 1 | `privacy.md` seção "Retenção" | Política precisa de definição com base em LGPD | humano (HR da Fase 1) |
| 2 | `strategic-analysis.md` seção "Build vs Buy" | Avaliar 3 SaaS alternativas antes de fechar custom | 10th-man (Fase 2 — Challenge) |

### 2.2 Importantes

| # | Onde | O que mudar | Origem |
|---|---|---|---|
| 1 | {ref} | {mudança} | {origem} |

### 2.3 Sugestões (não bloqueiam)

| # | Onde | Sugestão | Origem |
|---|---|---|---|
| 1 | {ref} | {sugestão} | {origem} |

---

## 3. Análise de impacto cross-eixo

> [!info] D3 do blueprint — ciência obrigatória
> O orchestrator analisa cada item do change request e identifica **possíveis impactos colaterais** em outros eixos. Mesmo que um item afete só `privacy.md`, pode reverberar em `product-vision.md` e/ou `tech-and-security.md`. Esta análise é levada à entrevista da próxima iteração.

| Item original | Eixo afetado diretamente | Eixos potencialmente impactados | Quem precisa agir | Quem só toma ciência |
|---|---|---|---|---|
| 1 | privacidade | product-vision (compliance), tech-and-security (storage) | cyber-security-architect (primário), po + solution-architect (impacto) | customer |
| 2 | strategic-analysis (build vs buy) | tech-and-security (stack), product-vision (cronograma) | solution-architect (primário), po (impacto) | customer |

> [!warning] Regra do v0.5
> Agentes fora do domínio **tomam ciência** do change request mas **não agem** sobre suas próprias seções a menos que o orchestrator instrua explicitamente. Se durante a entrevista um agente detectar impacto colateral, ele **pede ao orchestrator** ativar o agente correspondente.

---

## 4. Contexto novo a injetar

Informações que o humano forneceu no momento da reprova (devem virar `[BRIEFING]` na próxima iteração):

- {ex: "DPO confirmou que retenção é 5 anos para dados financeiros, 1 ano para o resto"}
- {ex: "Cronograma pode escorregar 30 dias, não mais"}

> [!danger] Promoção de tags
> Toda informação aqui listada vira `[BRIEFING]` automaticamente para o `customer` na próxima iteração. Ele **não pode** marcar como `[INFERENCE]` novamente.

---

## 5. O que NÃO deve mudar

Drafts ou seções que estão aprovados e devem ser **mantidos intactos** na próxima iteração (reaproveitamento parcial — D3 do blueprint):

- ✅ `product-vision.md` — manter intacto (nada apontado)
- ✅ `organization.md` — manter intacto
- ⚠️ `tech-and-security.md` — alterar apenas seções "Storage Architecture" e "Compliance" (impacto cross-eixo)
- ⚠️ `strategic-analysis.md` — alterar apenas seção "Build vs Buy"
- ⚠️ `privacy.md` — alterar seção "Retenção" (item crítico)

---

## 6. Instruções para a próxima iteração (i+1)

### 6.1 Setup da iteração

- [ ] Orchestrator cria `iteration-{i+1}/setup.md` com este change request como input principal
- [ ] Drafts da iteração anterior são copiados intactos para `iteration-{i+1}/draft/`
- [ ] Logs e memory permanecem em `iteration-{i}/` (imutáveis)

### 6.2 Notificação aos agentes

- [ ] **Todos os agentes** (customer + po + solution-architect + cyber-security-architect) recebem o change request como ciência obrigatória no início da reunião
- [ ] **Agentes primários** (marcados na seção 3): instruídos a agir sobre suas seções
- [ ] **Agentes secundários** (impacto cross-eixo): instruídos a observar; ativam se detectarem impacto adicional
- [ ] **Customer** atualizado: respostas listadas na seção 4 viram `[BRIEFING]` obrigatório

### 6.3 Foco da entrevista

- [ ] Entrevista da iteração {i+1} foca **prioritariamente** nos itens críticos (seção 2.1)
- [ ] Itens importantes (2.2) entram se houver tempo/contexto
- [ ] Sugestões (2.3) só se naturalmente surgirem
- [ ] Tópicos não relacionados ao change request **não são revisitados** (regra do reaproveitamento parcial)

---

## 7. Métrica de progresso

> [!info] Detecção de estagnação
> O orchestrator usa esta seção pra calcular se a iteração {i+1} está progredindo ou estagnando.

- **Itens críticos resolvidos na iteração anterior (i-1 → i):** {N}
- **Itens críticos novos descobertos nesta iteração (i):** {M}
- **Crescimento de contexto da iteração i em relação a i-1:** {percentual ou "n/a se i=1"}

**Alerta de estagnação:** {ativo se crescimento < 10%, senão inativo}

Se ativo, o orchestrator notifica o humano antes de iniciar a iteração {i+1}.

---

## 8. Token consumption acumulado

| Iteração | Fase 1 (Discovery) | Fase 2 (Challenge) | Fase 3 (Delivery) | Total |
|---|---|---|---|---|
| 1 | {N} | {N} | — | {N} |
| 2 | {N} | {N} | {N} | {N} |
| ... | | | | |
| **Total** | | | | **{N}** |

> O Human Review compartilhado tem custo 0 tokens (é humano). Fase 3 só conta na iteração final aprovada pelo cliente.

---

## 9. Próxima ação esperada

> ⏸️ **Pipeline pausado.**
>
> Aguardando comando humano de **restart manual** da Fase 1 para iniciar a iteração {i+1}.
>
> Antes de comandar restart, o humano deve:
> 1. Revisar este change request
> 2. Confirmar que as informações novas (seção 4) estão completas
> 3. Adicionar contexto extra se necessário
> 4. Comandar: `iniciar iteração {i+1}`
