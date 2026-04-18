---
title: "Iteration Policy (default)"
description: "Parâmetros configuráveis de iteração, estagnação, Human Review e duração de planejamento/MVP do projeto"
project-name: discovery-to-go
category: customization
type: policy
status: ativo
version: 01.00.000
created: 2026-04-17
---

# Iteration Policy

Parâmetros configuráveis da run. Este arquivo é o **default do framework** — cada run pode copiar para `runs/run-{n}/setup/customization/rules/iteration-policy.md` e ajustar.

> [!info] Quem consome
> `orchestrator`, `po`, `solution-architect`, `auditor` e o mecanismo de Human Review. Valores declarados aqui entram no `config.md` do run e são lidos pelas skills.

---

## Parâmetros de iteração

| Parâmetro | Default | Efeito |
|-----------|---------|--------|
| `max-iterations` | `0` (sem limite) | Cap numérico de iterações por run. `0` = ilimitado |
| `stagnation-threshold` | `10%` | Mínimo de crescimento de contexto entre iterações; abaixo disso emite alerta |
| `stagnation-consecutive` | `2` | Iterações consecutivas abaixo do threshold antes de emitir o alerta |
| `hr-loop-default-answer` | `Re-executar desde a 1ª fase` | Decisão assumida quando nenhuma opção é marcada no HR Loop |
| `hr-loop-max-passes` | `0` (sem limite) | Max passagens do HR Loop em um mesmo round |
| `abort-requires-confirmation` | `true` | Exige `@` para confirmar abort |

```yaml
max-iterations: 0
stagnation-threshold: 10
stagnation-consecutive: 2
hr-loop-default-answer: "Re-executar desde a 1ª fase"
hr-loop-max-passes: 0
abort-requires-confirmation: true
```

---

## Parâmetros de duração do projeto

Declaração do prazo típico de planejamento e construção do MVP. Consumido pelas skills `po` e `solution-architect` para calibrar o escopo do backlog priorizado.

| Parâmetro | Default `[exemplo]` | Efeito |
|-----------|---------------------|--------|
| `planning-duration-months` | `1` `[exemplo]` | Meses de planejamento/discovery antes da construção começar |
| `mvp-duration-months` | `6` `[exemplo]` | Meses para entregar o MVP após o planejamento |

```yaml
planning-duration-months: 1    # [exemplo] — ajuste ao ritmo do projeto
mvp-duration-months: 6         # [exemplo] — ajuste ao ritmo do projeto
```

> [!tip] Marcação `[exemplo]`
> Os defaults `1` e `6` são ponto de partida comum, não prescrição do framework. Cada projeto deve declarar o valor real no briefing (ver seção 6 — "Restrições conhecidas") ou neste arquivo quando copiado para a run.

> [!note] Sem ação automática
> Nenhuma ação de pipeline é disparada se o backlog não couber no prazo declarado. O parâmetro alimenta **o prompt das skills** que dimensionam escopo; a conciliação entre escopo e prazo é processo humano.

---

## Combinações típicas

### Conservador (cliente exigente / alto-risco)

```yaml
max-iterations: 5
stagnation-threshold: 15
stagnation-consecutive: 1
hr-loop-default-answer: "Abortar"
abort-requires-confirmation: true
planning-duration-months: 2
mvp-duration-months: 9
```

### Rápido (POC / spike)

```yaml
max-iterations: 2
stagnation-threshold: 5
stagnation-consecutive: 3
hr-loop-default-answer: "Avançar para a próxima fase"
abort-requires-confirmation: false
planning-duration-months: 0
mvp-duration-months: 1
```

---

## Documentos relacionados

- [[rules/iteration-loop/iteration-loop]] — Regra formal de iteração (consumidora destes parâmetros)
- [[rules/discovery/discovery]] — Processo de discovery que referencia `planning-duration-months` e `mvp-duration-months`
- [[docs/guides/discovery-pipeline]] — Guia passo a passo do pipeline
