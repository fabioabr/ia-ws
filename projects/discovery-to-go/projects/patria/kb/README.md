# Knowledge Base

Knowledge base específico deste cliente — contexto de negócio, ambiente tecnológico, integrações, stack e fluxos que os agentes usam durante o discovery.

Diferente dos blueprints globais (que são por tipo de projeto), o KB do cliente é sobre **a empresa específica**.

## Arquivo obrigatório

| Arquivo | Quando criar | O que contém |
|---------|-------------|-------------|
| `environment.md` | **Primeiro passo — antes de qualquer projeto** | Cenário atual completo: infra, sistemas, stack, equipe, custos, normas. Baseado no blueprint `base/foundation/templates/projects/environment/README.md` |

## Arquivos complementares

| Arquivo | Quando criar | O que contém |
|---------|-------------|-------------|
| `business-context.md` | Cliente tem regras de negócio únicas | Modelo de negócio, regulações, restrições específicas |
| `integration-flow.md` | Cliente tem ecossistema complexo | Fluxo de dados entre sistemas, dependências entre áreas |
| `{topic}.md` | Quando necessário | Qualquer contexto relevante para o discovery |

## Fluxo de trabalho

```
1. Preencher environment.md (obrigatório)
         ↓
2. Preencher arquivos complementares (se necessário)
         ↓
3. Novo projeto chega → classificar tipo
         ↓
4. Discovery usa blueprint do tipo + KB como base de conhecimento
         ↓
5. Respostas do "cliente simulado" vêm do KB (RAG) → menos INFERENCE
```

## Como é usado

O orchestrator carrega os arquivos do KB como contexto adicional para os agentes. O customer (simulador do cliente) consulta o KB para responder perguntas que o briefing não cobre — especialmente perguntas sobre infraestrutura, stack, contratos e equipe que já estão documentadas no `environment.md`.

> **Importante:** Quanto mais completo o KB, menor o nível de INFERENCE nas respostas do discovery. O `environment.md` preenchido corretamente elimina inferência em todas as perguntas sobre o cenário atual da empresa.
