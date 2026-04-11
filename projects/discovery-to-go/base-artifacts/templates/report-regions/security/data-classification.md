---
region-id: REG-SEC-01
title: "Classificação de Dados"
group: security
description: "Inventário de dados com classificação de sensibilidade e tratamento requerido"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (dado, classificação, tratamento)"
template-visual: "Table com color-coded badges"
default: true
---

# Classificação de Dados

Categoriza todos os dados manipulados pelo sistema segundo seu nível de sensibilidade, definindo o tratamento de segurança adequado para cada categoria. Essa classificação é a base para decisões de criptografia, controle de acesso e conformidade regulatória.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| dado | string | Nome ou tipo do dado |
| classificação | enum | Público, Interno, Confidencial, Restrito |
| tratamento | string | Medidas de proteção requeridas |

## Exemplo

| Dado | Classificação | Tratamento |
|------|---------------|------------|
| Nome completo do usuário | Confidencial | Criptografia em repouso, acesso via RBAC, mascaramento em logs |
| CPF | Restrito | Criptografia AES-256, acesso restrito a perfis autorizados, tokenização em integrações |
| Saldo de conta | Restrito | Criptografia em trânsito e repouso, audit trail obrigatório |
| Histórico de transações | Confidencial | Criptografia em repouso, retenção de 5 anos, acesso auditado |
| Preferências de dashboard | Interno | Controle de acesso padrão, sem criptografia adicional |
| Documentação pública da API | Público | Sem restrições de acesso |

## Representação Visual

### Dados de amostra

O inventário de classificação de dados pode ser representado como texto corrido contextualizando a estratégia de classificação adotada, complementado por uma tabela detalhada e um heatmap de sensibilidade.

**Texto corrido:** "O FinTrack Pro adota um modelo de classificação em quatro níveis (Público, Interno, Confidencial, Restrito), alinhado à norma ISO 27001. Dos 6 tipos de dados mapeados, 2 são classificados como Restritos, 2 como Confidenciais, 1 como Interno e 1 como Público, evidenciando que a maior parte dos dados exige controles elevados de proteção."

**Tabela de classificação:**

| Dado | Classificação | Tratamento |
|------|---------------|------------|
| Nome completo do usuário | Confidencial | Criptografia em repouso, acesso via RBAC, mascaramento em logs |
| CPF | Restrito | Criptografia AES-256, acesso restrito a perfis autorizados, tokenização em integrações |
| Saldo de conta | Restrito | Criptografia em trânsito e repouso, audit trail obrigatório |
| Histórico de transações | Confidencial | Criptografia em repouso, retenção de 5 anos, acesso auditado |
| Preferências de dashboard | Interno | Controle de acesso padrão, sem criptografia adicional |
| Documentação pública da API | Público | Sem restrições de acesso |

**Heatmap de sensibilidade:**

| Nível | Quantidade | Intensidade |
|-------|:----------:|-------------|
| Restrito | 2 | Alta — exige criptografia forte, acesso mínimo, auditoria completa |
| Confidencial | 2 | Média-alta — criptografia e RBAC obrigatórios |
| Interno | 1 | Média — controle de acesso padrão |
| Público | 1 | Baixa — sem restrições |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo resumindo a estratégia de classificação e a distribuição dos dados por nível | Para contextualizar a abordagem de classificação e fornecer visão executiva |
| Tabela detalhada | Tabela com dado, classificação e tratamento requerido | Para documentação completa e referência técnica |
| Heatmap por sensibilidade | Mapa de calor com gradiente de cores por nível de classificação (vermelho = Restrito, amarelo = Interno, verde = Público) | Para visualização rápida da distribuição de sensibilidade e priorização de controles |
| Gráfico de barras empilhadas | Barras agrupadas por nível de classificação mostrando quantidade de dados | Para apresentações executivas e comparação entre projetos |
| Diagrama de bolhas | Bolhas dimensionadas pela criticidade, agrupadas por classificação | Para mapear volume vs. sensibilidade em um dashboard interativo |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
