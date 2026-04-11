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

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela formal
**Tecnologia:** HTML/CSS
**Justificativa:** Assinaturas de aprovacao sao um artefato formal e institucional que exige sobriedade visual. Uma tabela com estilo formal (bordas, tipografia serif, linhas para assinatura) com colunas Papel, Nome, Assinatura, Data e Observacoes e o formato universalmente aceito para documentos oficiais.
**Alternativa:** Tabela formal com barra de progresso — quando o foco e no acompanhamento do status de coleta (X de Y assinaturas) em vez do documento final.
