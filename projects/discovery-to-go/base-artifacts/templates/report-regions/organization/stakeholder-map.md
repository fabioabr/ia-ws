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

## Representação Visual

### Dados de amostra

| Stakeholder | Influência | Interesse |
|-------------|:----------:|:---------:|
| Diretor de Produto | Alta | Alto |
| Head de Engenharia | Alta | Alto |
| Time de Compliance | Média | Alto |
| Equipe de Suporte N2 | Baixa | Médio |
| CFO | Alta | Baixo |

**Quadrantes (Influência x Interesse):**
- **Alta Influência + Alto Interesse:** Diretor de Produto, Head de Engenharia → Gerenciar de perto
- **Alta Influência + Baixo Interesse:** CFO → Manter satisfeito
- **Média/Baixa Influência + Alto Interesse:** Time de Compliance → Manter informado
- **Baixa Influência + Baixo/Médio Interesse:** Equipe de Suporte N2 → Monitorar

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa descritiva listando stakeholders agrupados por estratégia de engajamento | Relatórios executivos textuais ou contextos onde gráficos não são suportados |
| Tabela | Tabela com colunas de stakeholder, influência, interesse e engajamento | Visão detalhada para planejamento operacional de comunicação |
| Gráfico de quadrantes (Influência x Interesse) | Matriz 2x2 posicionando cada stakeholder conforme seu nível de influência e interesse | Apresentações estratégicas para definir prioridades de engajamento e comunicação |
| Mapa de bolhas | Bolhas posicionadas nos eixos influência/interesse, com tamanho representando criticidade | Quando há muitos stakeholders e é preciso destacar os mais críticos visualmente |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
