---
region-id: REG-NARR-03
title: "Approval Signatures"
group: narrative
description: "Formal sign-off table for stakeholder approval"
source: "Consolidator"
schema: "Tabela (papel, nome, assinatura, data)"
template-visual: "Table formal"
default: false
---

# Approval Signatures

Tabela formal para coleta de aprovacoes dos stakeholders. Cada aprovador registra seu papel, nome, assinatura e data. Este artefato formaliza o comprometimento organizacional com o projeto e encerra a fase de discovery.

## Schema de dados

```yaml
approval_signatures:
  document: string               # Nome do documento aprovado
  version: string                # Versao do documento
  signatures:
    - role: string               # Papel do aprovador
      name: string               # Nome completo
      signature: string          # Assinatura (ou "Pendente")
      date: string               # Data da aprovacao
      notes: string              # Observacoes ou ressalvas
```

## Exemplo

**Documento:** Relatorio de Discovery — FinTrack Pro SaaS
**Versao:** 1.2 (pos-auditoria)

| Papel | Nome | Assinatura | Data | Observacoes |
|-------|------|-----------|------|-------------|
| Product Sponsor | Ana Silva | _Pendente_ | | |
| CTO | Carlos Mendes | _Pendente_ | | |
| Engineering Manager | Rafael Costa | _Pendente_ | | Condicionado a contratacao dos 2 devs |
| Product Owner | Juliana Ferreira | _Pendente_ | | |
| Security Officer | Marcos Almeida | _Pendente_ | | Condicionado a designacao de DPO |

## Representacao Visual

### Dados de amostra

```
Documento: Relatorio de Discovery — FinTrack Pro SaaS (v1.2)

Aprovacoes: 0 de 5 coletadas

  Product Sponsor     Ana Silva          [ ] Pendente
  CTO                 Carlos Mendes      [ ] Pendente
  Engineering Manager Rafael Costa       [ ] Pendente  (condicionado)
  Product Owner       Juliana Ferreira   [ ] Pendente
  Security Officer    Marcos Almeida     [ ] Pendente  (condicionado)
```

### Formatos de exibicao possiveis

| Formato | Descricao | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Paragrafo formal listando aprovadores e status de assinatura | Comunicacoes formais, atas de reuniao |
| Tabela formal | Tabela com colunas Papel, Nome, Assinatura, Data, Observacoes com estilo formal | Documentos oficiais, relatorios finais de discovery, impressao |
| Tabela formal com status | Tabela formal com indicadores visuais de status (assinado/pendente) por linha | Acompanhamento de coleta de assinaturas |
| Tabela formal com contagem | Tabela com barra de progresso de assinaturas coletadas (X de Y) | Dashboards de aprovacao, visao executiva |
| Tabela formal com ressalvas destacadas | Tabela com coluna de observacoes em destaque para condicoes e ressalvas | Analise de riscos de aprovacao, preparacao para go/no-go |

> [!info] Avaliacao pendente
> Um especialista em visualizacao de dados deve avaliar qual formato grafico melhor representa esta informacao, considerando o publico-alvo e o contexto de uso.
