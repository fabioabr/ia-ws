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
