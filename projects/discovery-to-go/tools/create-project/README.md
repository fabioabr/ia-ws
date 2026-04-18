# create-project

Cria a estrutura de pastas para um novo projeto de discovery.

## Uso

```bash
python main.py "cliente/projeto"
```

## Exemplos

```bash
# Criar cliente "patria" com projeto "teste"
python main.py "patria/teste"

# Criar novo projeto para cliente existente
python main.py "patria/outro-projeto"
```

## Comportamento

| Cenário | Ação |
|---------|------|
| Cliente não existe | Cria pasta do cliente copiando client-template (assets, config, kb, rules) |
| Cliente já existe | Reutiliza a pasta existente |
| Projeto não existe | Cria pasta do projeto com scaffold completo + start-briefing.md |
| Projeto já existe | Aborta com mensagem de erro |

## Estrutura criada

```
projects/{cliente}/
├── assets/logos/
├── config/
├── kb/
├── rules/
├── templates/customization/
└── projects/{projeto}/
    ├── setup/
    │   ├── start-briefing.md      ← preencha este arquivo
    │   ├── config.md
    │   └── customization/
    ├── iterations/iteration-1/
    │   ├── logs/
    │   └── results/
    │       ├── 1-discovery/
    │       ├── 2-challenge/
    │       └── 3-delivery/
    └── iterations/state/
        └── pipeline-state.md
```

## Requisitos

- Python 3.10+
- Sem dependências externas
