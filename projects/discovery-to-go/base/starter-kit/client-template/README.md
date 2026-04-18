# Client Template

Template de scaffold para customizações de um cliente. Para criar uma pasta de cliente, copie este template:

```bash
cp -r _client-template/ {client-name}/
```

Depois preencha o `kb/environment.md` como primeiro passo — antes de qualquer projeto.

## Estrutura

```
{client-name}/
├── kb/                        ← Knowledge base do cliente
│   ├── environment.md         ← OBRIGATÓRIO — cenário atual (infra, stack, equipe, custos)
│   ├── business-context.md    ← contexto de negócio específico
│   └── {topic}.md             ← outros contextos relevantes
├── projects/                  ← Projetos deste cliente
│   └── {project-name}/
│       ├── briefing.md        ← prompt/briefing inicial
│       ├── project-type.md    ← tipo classificado (referência ao blueprint)
│       └── runs/              ← runs de discovery
│           └── run-1/
├── assets/                    ← Assets visuais
│   └── logos/                 ← Logos do cliente (dark.png, light.png)
├── rules/                     ← Regras adicionais
├── templates/                 ← Overrides de templates
│   └── customization/         ← Scoring, iteration, report, layout
└── config/                    ← Overrides de configuração
```

## Fluxo de trabalho

```
1. Copiar _client-template/ para {client-name}/
         ↓
2. Preencher kb/environment.md (obrigatório)
         ↓
3. Novo projeto → criar projects/{project-name}/
         ↓
4. Classificar tipo de projeto → registrar em project-type.md
         ↓
5. Rodar discovery usando blueprint do tipo + KB como base
```

## Prioridade

Esta é a **camada 3** (maior prioridade). Conteúdo aqui sobrescreve:
- `base/` (camada 2 — Pipeline)
- `base/` (camada 1 — Base)
