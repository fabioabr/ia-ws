---
region-id: REG-ORG-01
title: "Mapa de Stakeholders"
group: organization
description: "Matriz de stakeholders com papel, influência e estratégia de engajamento"
source: "Bloco #4 (po) → 1.4"
schema: "Tabela (stakeholder, papel, influência, interesse, engajamento)"
template-visual: "Table com badges"
default: true
---

# Mapa de Stakeholders

Identifica todos os stakeholders relevantes do projeto, classificando-os por nível de influência e interesse. Essa visão permite definir estratégias de comunicação e engajamento adequadas para cada perfil, reduzindo riscos políticos e garantindo alinhamento contínuo.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| stakeholder | string | Nome ou papel da pessoa/grupo |
| papel | string | Função no projeto (sponsor, owner, user, etc.) |
| influência | enum | Alta, Média, Baixa |
| interesse | enum | Alto, Médio, Baixo |
| engajamento | string | Estratégia recomendada |

## Exemplo

| Stakeholder | Papel | Influência | Interesse | Engajamento |
|-------------|-------|------------|-----------|-------------|
| Diretor de Produto | Sponsor executivo | Alta | Alto | Reunião quinzenal de status + relatório mensal |
| Head de Engenharia | Technical Owner | Alta | Alto | Participação ativa em reviews de arquitetura |
| Time de Compliance | Consultor | Média | Alto | Consultoria sob demanda + validação de entregas |
| Equipe de Suporte N2 | Usuário final | Baixa | Médio | Treinamento pré-go-live + documentação |
| CFO | Influenciador | Alta | Baixo | Report trimestral de ROI e custos |
