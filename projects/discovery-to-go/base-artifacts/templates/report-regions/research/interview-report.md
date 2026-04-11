---
region-id: REG-PESQ-01
title: "Interview Report"
group: research
description: "Metodologia, perfis entrevistados, achados por tema, padrões, surpresas"
source: "Interview log + Blocos #1-#4"
schema: "text"
template-visual: "Accordion por tema"
default: false
---

# Interview Report

Relatório estruturado das entrevistas realizadas durante o discovery, cobrindo metodologia utilizada, perfis dos entrevistados, achados organizados por tema, padrões identificados entre as respostas e surpresas que desafiaram premissas iniciais. Este artefato garante que as decisões de produto e arquitetura estejam fundamentadas em evidências primárias, não em suposições.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| metodologia | object | `{ tipo: string, duracao: string, n_entrevistas: number, periodo: string, formato: string }` |
| perfis | list | Cada item: `{ papel: string, quantidade: number, senioridade: string }` |
| achados_por_tema | list | Cada item: `{ tema: string, achados: list, frequencia: string }` |
| padroes | list | Padrões que apareceram em múltiplas entrevistas |
| surpresas | list | Achados inesperados que desafiaram premissas |

## Exemplo

```markdown
## Relatório de Entrevistas

### Metodologia

- **Tipo:** Entrevista semiestruturada em 8 blocos temáticos
- **Duração média:** 90 minutos por sessão
- **Total de entrevistas:** 6 sessões com 8 participantes
- **Período:** 01/04/2026 a 08/04/2026
- **Formato:** Videoconferência (Teams) com gravação autorizada

### Perfis entrevistados

| Papel | Quantidade | Senioridade |
|-------|-----------|-------------|
| CFO | 1 | C-level |
| Controller | 1 | Gerência |
| Analista financeiro | 4 | Sênior/Pleno |
| Gerente de TI | 1 | Gerência |
| Auditor interno | 1 | Sênior |

### Achados por tema

#### Tema 1: Processo de consolidação (mencionado por 8/8)

- Processo atual é 100% manual com planilhas Excel
- Tempo médio de fechamento: D+8 (varia de D+6 a D+12 dependendo de retrabalho)
- 3 pontos de falha principais: coleta, conversão cambial, eliminação intercompany
- Analistas gastam ~60% do tempo em coleta e normalização, não em análise

#### Tema 2: Qualidade e confiança nos dados (mencionado por 7/8)

- Controller revisa 100% dos cálculos manualmente — "não confio no processo"
- 3 reapresentações ao conselho nos últimos 6 meses por erros de eliminação
- Auditores reclamam da falta de trilha — reconstrução manual leva 2 semanas

#### Tema 3: Ferramentas e tecnologia (mencionado por 6/8)

- SAP R/3 é o ERP de 10/12 filiais; 2 filiais menores usam TOTVS
- Tentativa anterior de automação com macros VBA fracassou por manutenibilidade
- TI tem capacidade para manter integrações, mas não para construir solução completa

### Padrões identificados

1. **Unanimidade sobre a dor:** todos os entrevistados classificaram a consolidação manual como "o maior gargalo da área financeira"
2. **Desconfiança no processo:** mesmo os analistas que executam não confiam — sempre refazem cálculos
3. **Demanda por rastreabilidade:** auditoria é o segundo driver depois de velocidade

### Surpresas

1. **Filiais TOTVS são o maior risco:** esperávamos que SAP fosse o problema, mas as 2 filiais TOTVS enviam dados em formato completamente diferente e sem API disponível
2. **CFO quer predição, não só consolidação:** "eu quero saber o resultado antes do fechamento oficial" — escopo além do MVP, mas sinaliza direção de produto
3. **Analistas já têm workarounds sofisticados:** macros, scripts Python informais, validações cruzadas — indicando alta capacidade técnica e potencial para adoção rápida
```

## Representação Visual

### Dados de amostra

- **Metodologia:** Entrevista semiestruturada, 6 sessões, 8 participantes, 90 min/sessão
- **Perfis:** CFO (1), Controller (1), Analista financeiro (4), Gerente de TI (1), Auditor interno (1)
- **Temas principais:** Processo de consolidação (8/8), Qualidade e confiança nos dados (7/8), Ferramentas e tecnologia (6/8)
- **Padrões:** Unanimidade sobre a dor, desconfiança no processo, demanda por rastreabilidade
- **Surpresas:** Filiais TOTVS como maior risco, CFO quer predição, analistas com workarounds sofisticados

### Recomendação do Chart Specialist

**Veredicto:** CARD
**Tipo:** Card com accordion por tema
**Tecnologia:** HTML/CSS
**Justificativa:** Dados qualitativos e textuais com múltiplos temas aninhados se beneficiam de seções colapsáveis que permitem navegação seletiva sem sobrecarga visual, preservando o contexto narrativo de cada achado.
**Alternativa:** Tabela cruzada (HTML/CSS) — quando stakeholders precisam comparar frequência de temas entre perfis de forma rápida e tabulada
