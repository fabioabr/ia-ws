---
region-id: REG-PROD-03
title: "User Journeys"
group: product
description: "Mapa de jornada por persona — passos, touchpoints, dores, oportunidades"
source: "Bloco #2 (po) → 1.2"
schema: "diagram"
template-visual: "Stepped timeline ou diagram"
default: false
---

# User Journeys

Mapeamento visual da jornada de cada persona ao longo do processo que o produto pretende melhorar. Cada jornada descreve os passos sequenciais, os touchpoints com sistemas e pessoas, as dores sentidas em cada etapa e as oportunidades de melhoria identificadas. É o artefato que conecta personas a features concretas e permite priorizar funcionalidades pelo impacto na experiência do usuário.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| jornadas | list | Cada item: `{ persona: string, cenario: string, passos: list }` |
| passos[n] | object | `{ etapa: string, acao: string, touchpoint: string, emocao: string, dor: string | null, oportunidade: string | null }` |

## Exemplo

```markdown
## Jornadas de Usuário

### Jornada: Marcos Oliveira — Consolidação mensal

**Cenário:** Marcos precisa coletar dados financeiros de 3 filiais, normalizar formatos e entregar a consolidação ao controller até D+5.

| Etapa | Ação | Touchpoint | Emoção | Dor | Oportunidade |
|-------|------|------------|--------|-----|---------------|
| 1. Coleta | Exporta relatório de cada SAP local via email ao responsável da filial | Email + SAP GUI | Frustração | Espera 1-2 dias por respostas; formatos inconsistentes | Integração direta via API — eliminar dependência humana |
| 2. Normalização | Abre cada planilha e converte para formato padrão (plano de contas, moeda) | Excel | Tédio | Trabalho mecânico, 3h por filial; erros de conversão cambial | Regras de mapeamento automáticas |
| 3. Eliminação | Aplica regras de eliminação intercompany manualmente em planilha-mestre | Excel | Ansiedade | Regras complexas, fácil de errar; sem validação automática | Engine de eliminação com regras configuráveis |
| 4. Consolidação | Soma tudo e gera P&L consolidado | Excel | Concentração | Qualquer erro nas etapas anteriores propaga aqui | Consolidação automática com check de integridade |
| 5. Revisão | Envia para Juliana (controller) revisar e aprovar | Email + Excel | Expectativa | Se houver erro, volta para a etapa 2 — retrabalho de 4-6h | Alertas de inconsistência pré-revisão |
| 6. Entrega | Juliana aprova e repassa ao CFO | Email + PowerPoint | Alívio | Formatting manual para a apresentação ao conselho | Geração automática de relatório executivo |
```

## Representação Visual

### Dados de amostra

| Etapa | Ação | Touchpoint | Emoção | Tem dor? | Tem oportunidade? |
|-------|------|------------|--------|----------|-------------------|
| 1. Coleta | Exporta relatório de cada SAP | Email + SAP GUI | Frustração | Sim | Sim |
| 2. Normalização | Converte para formato padrão | Excel | Tédio | Sim | Sim |
| 3. Eliminação | Aplica regras intercompany | Excel | Ansiedade | Sim | Sim |
| 4. Consolidação | Soma e gera P&L consolidado | Excel | Concentração | Sim | Sim |
| 5. Revisão | Envia para controller revisar | Email + Excel | Expectativa | Sim | Sim |
| 6. Entrega | Controller aprova e repassa ao CFO | Email + PowerPoint | Alívio | Sim | Sim |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Narrativa sequencial descrevendo cada passo da jornada com contexto e dores | Quando o leitor precisa entender o fluxo completo com nuances |
| Tabela | Matriz com etapas nas linhas e dimensões (ação, touchpoint, emoção, dor) nas colunas | Para análise comparativa entre etapas |
| Stepped timeline / flowchart | Diagrama de fluxo horizontal com etapas sequenciais, ícones de emoção e marcadores de dor/oportunidade | Para apresentações e comunicação visual da jornada completa |
| Swimlane diagram | Raias por persona/sistema mostrando interações e handoffs entre atores | Para evidenciar dependências e gargalos entre personas |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
