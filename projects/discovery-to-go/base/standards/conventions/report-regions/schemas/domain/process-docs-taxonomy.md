---
region-id: REG-DOM-PROC-01
title: "Process Docs Taxonomy"
group: domain
description: "Document types, categorization, and lifecycle for process documentation"
source: "Bloco #5/#7 (arch)"
schema: "Tipos doc + categorização + lifecycle"
template-visual: "Table com badges"
when: process-documentation
default: false
---

# Process Docs Taxonomy

Define a taxonomia de documentos de processo, incluindo tipos, categorizacao e ciclo de vida. Uma taxonomia bem definida e pre-requisito para governanca documental eficaz e para que os colaboradores encontrem o que precisam.

## Schema de dados

```yaml
docs_taxonomy:
  types:
    - type: string               # Tipo de documento
      category: string           # Categoria (operacional, tecnico, regulatorio, etc.)
      audience: string           # Publico-alvo
      lifecycle: string          # Criacao → Revisao → Publicacao → Revisao periodica → Arquivamento
      review_frequency: string
```

## Exemplo

| Tipo | Categoria | Publico | Revisao | Lifecycle |
|------|-----------|---------|---------|-----------|
| POP (Procedimento Operacional Padrao) | Operacional | Equipe operacao | Semestral | Ativo ate substituicao |
| Instrucao de Trabalho | Operacional | Executor da tarefa | Anual | Vinculado ao POP |
| Politica | Governanca | Toda a organizacao | Anual | Aprovacao diretoria |
| Manual de Sistema | Tecnico | TI e suporte | A cada release | Versionado com o software |
| Registro de Processo | Regulatorio | Auditoria | N/A (imutavel) | Retencao de 5 anos |

## Representacao Visual

### Dados de amostra

```
Documentacao de Processos
├── Governanca
│   └── Politica (3 docs)
├── Operacional
│   ├── POP (12 docs)
│   └── Instrucao de Trabalho (28 docs)
├── Tecnico
│   └── Manual de Sistema (8 docs)
└── Regulatorio
    └── Registro de Processo (15 docs)

Total: 66 documentos | 5 tipos | 4 categorias
```

### Recomendacao do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela com badges
**Tecnologia:** HTML/CSS
**Justificativa:** A taxonomia de documentos tem 5 tipos com atributos categoricos (categoria, publico, revisao, lifecycle). Uma tabela estilizada com badges coloridos para categoria e frequencia de revisao permite escaneamento rapido e funciona como catalogo de referencia para consulta operacional.
**Alternativa:** Card grid agrupado por categoria (HTML/CSS) — quando o foco for visualizar a hierarquia (categorias > tipos > quantidade) em vez do detalhamento por tipo.
