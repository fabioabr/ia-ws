# Knowledge Base

Knowledge base específico deste cliente — contexto de negócio, integrações, stack e fluxos que os agentes usam durante a entrevista da Fase 1.

Diferente dos context-templates (que são por domínio tecnológico), o KB do cliente é sobre **a empresa específica**.

## Arquivos sugeridos

| Arquivo | Quando criar | O que contém |
|---------|-------------|-------------|
| `integration-flow.md` | Cliente tem ecossistema complexo | Fluxo de dados, sistemas, dependências entre áreas |
| `tech-stack.md` | Cliente tem stack definido | Ferramentas, plataformas, versões que já usa |
| `business-context.md` | Cliente tem regras de negócio únicas | Modelo de negócio, regulações, restrições específicas |
| `{topic}.md` | Quando necessário | Qualquer contexto relevante para o discovery |

## Como é usado

O orchestrator carrega esses arquivos como contexto adicional para os agentes na Fase 1. O customer (simulador do cliente) consulta esse KB para responder perguntas que o briefing não cobre.
