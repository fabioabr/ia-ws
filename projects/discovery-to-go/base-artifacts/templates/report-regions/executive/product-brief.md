---
region-id: REG-EXEC-02
title: "Product Brief"
group: executive
description: "Documento de 1-2 páginas para alinhamento executivo — problema, solução, usuário-alvo, resultado esperado, MVP, investimento, recomendação"
source: "Consolidator"
schema: "text"
template-visual: "Card com seções"
default: true
---

# Product Brief

Documento conciso de alinhamento executivo que conecta o problema de negócio à solução proposta. Estruturado em seções claras — problema, solução, público-alvo, resultado esperado, escopo do MVP, investimento e recomendação — permite que stakeholders entendam rapidamente o que será construído, para quem e por quê. É o artefato de referência para aprovações de budget e kick-off de projeto.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| problema | string | 1-2 parágrafos descrevendo dor e impacto mensurável |
| solucao | string | 1 parágrafo com descrição da solução proposta |
| usuario_alvo | list | Perfis de usuário primário e secundário |
| resultado_esperado | list | Benefícios mensuráveis esperados (métricas + prazo) |
| mvp | object | `{ descricao: string, epicos: list, prazo: string }` |
| investimento | object | `{ valor: string, faixa: string, modelo: string }` |
| recomendacao | string | Parecer final com justificativa |

## Exemplo

```markdown
## Product Brief — FinTrack Pro

### Problema

A Acme Corp consolida dados financeiros de 12 filiais manualmente usando planilhas Excel. O processo consome 12h/semana por analista (4 analistas), totaliza ~2.500h/ano e já produziu 3 erros materiais em relatórios ao conselho nos últimos 6 meses. A empresa precisa de um processo automatizado antes do próximo ciclo de auditoria (Q4 2026).

### Solução proposta

Plataforma web de consolidação financeira automatizada que centraliza dados de ERPs das filiais, aplica regras de eliminação intercompany e gera relatórios IFRS-compliant em tempo real.

### Usuário-alvo

- **Primário:** Analistas financeiros (4 pessoas) — executam consolidação mensal
- **Secundário:** Controller e CFO — consomem relatórios e dashboards
- **Terciário:** Auditores externos — acessam trilha de auditoria

### Resultado esperado

- Redução de 80% no tempo de consolidação (de 12h para 2h/semana por analista)
- Zero erros materiais em relatórios ao conselho
- Trilha de auditoria completa para compliance SOX
- Fechamento mensal em D+2 (hoje: D+8)

### MVP (Fase 1)

**Escopo:** Consolidação automática de 3 filiais principais + relatório P&L consolidado + eliminação intercompany básica.

**Épicos:**
1. Ingestão de dados via API do SAP
2. Engine de eliminação intercompany
3. Geração de P&L consolidado
4. Dashboard executivo
5. Trilha de auditoria

**Prazo:** 16 semanas (4 sprints de 4 semanas)

### Investimento

**R$ 680K — R$ 850K** para o MVP (Fase 1), incluindo equipe de 5 pessoas + infraestrutura cloud. TCO 3 anos estimado em R$ 2,1M — R$ 2,8M.

### Recomendação

**Prosseguir com build customizado.** O problema é crítico (risco regulatório), as soluções de mercado não atendem às regras específicas de eliminação da Acme, e o ROI projetado é positivo em 14 meses. Recomenda-se aprovar a Fase 1 e reavaliar após validação da integração SAP na Sprint 0.
```
