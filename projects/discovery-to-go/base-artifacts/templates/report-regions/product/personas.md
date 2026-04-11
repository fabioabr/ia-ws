---
region-id: REG-PROD-02
title: "Personas"
group: product
description: "Perfis de usuário com JTBD, dores, ganhos esperados, comportamentos"
source: "Bloco #2 (po) → 1.2"
schema: "text"
template-visual: "Grid de persona cards"
default: true
---

# Personas

Perfis representativos dos usuários do produto, construídos a partir de entrevistas e dados do discovery. Cada persona inclui nome fictício, perfil demográfico-profissional, Jobs to Be Done (JTBD), dores atuais, ganhos esperados e comportamentos relevantes. As personas orientam decisões de UX, priorização de features e comunicação com stakeholders.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| personas | list | Cada item: `{ nome: string, cargo: string, perfil: string, jtbd: list, dores: list, ganhos: list, comportamentos: list, frequencia_uso: string }` |

## Exemplo

```markdown
## Personas

### Persona 1 — Roberto Almeida (CFO)

- **Cargo:** Chief Financial Officer
- **Perfil:** 52 anos, 20 anos de experiência em finanças corporativas, responde ao CEO e ao conselho. Consome relatórios — não opera sistemas diretamente.
- **JTBD:**
  - Ter visibilidade consolidada da saúde financeira do grupo em tempo real
  - Apresentar relatórios confiáveis ao conselho sem risco de reapresentação
- **Dores:**
  - Recebe dados consolidados com 8 dias de atraso
  - Já precisou reapresentar relatórios 3 vezes — impacto na credibilidade
  - Não consegue fazer drill-down por filial sem pedir relatórios adicionais
- **Ganhos esperados:**
  - Fechamento em D+2 com dados confiáveis
  - Dashboard executivo com drill-down por filial e período
  - Trilha de auditoria automática
- **Comportamentos:** Acessa relatórios no celular em reuniões; prefere gráficos a tabelas; delega detalhes ao controller.
- **Frequência de uso:** Semanal (dashboard), mensal (relatório consolidado)

---

### Persona 2 — Juliana Ferreira (Controller)

- **Cargo:** Controller Corporativo
- **Perfil:** 38 anos, CPA, gerencia equipe de 4 analistas. Responsável pela consolidação mensal e interface com auditoria.
- **JTBD:**
  - Garantir que a consolidação esteja correta e dentro do prazo
  - Reduzir retrabalho da equipe e liberar tempo para análise
- **Dores:**
  - Gasta 60% do tempo revisando planilhas em vez de analisar resultados
  - Não tem confiança nos dados — sempre refaz cálculos de eliminação
  - Processo de auditoria é desgastante por falta de rastreabilidade
- **Ganhos esperados:**
  - Consolidação automatizada com regras auditáveis
  - Tempo para análise estratégica em vez de trabalho operacional
  - Relatórios de auditoria gerados automaticamente
- **Comportamentos:** Power user de Excel; valida tudo manualmente antes de aprovar; documenta processos em wikis internos.
- **Frequência de uso:** Diária

---

### Persona 3 — Marcos Oliveira (Analista Financeiro)

- **Cargo:** Analista Financeiro Sênior
- **Perfil:** 29 anos, 5 anos de experiência, executa a consolidação operacional. Um dos 4 analistas da equipe.
- **JTBD:**
  - Coletar dados das filiais e consolidar sem erros
  - Entregar a consolidação no prazo para o controller
- **Dores:**
  - Processo manual e repetitivo — 12h/semana em trabalho mecânico
  - Formatos diferentes por filial exigem normalização manual
  - Erros são descobertos tarde e geram retrabalho em cascata
- **Ganhos esperados:**
  - Automação da coleta e normalização de dados
  - Alertas de inconsistência antes da consolidação final
  - Mais tempo para análise de variações e exceções
- **Comportamentos:** Técnico, aprende ferramentas novas rápido; frustra-se com processos manuais; sugere melhorias frequentemente.
- **Frequência de uso:** Diária
```
