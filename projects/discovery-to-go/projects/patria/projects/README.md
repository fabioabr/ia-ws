# Projects

Projetos deste cliente. Cada projeto tem sua própria pasta com runs de discovery.

## Estrutura

```
projects/
├── {project-name}/
│   ├── briefing.md              ← briefing inicial do projeto
│   ├── project-type.md          ← tipo classificado (referência ao blueprint)
│   └── runs/
│       ├── run-1/
│       │   ├── setup/
│       │   ├── iterations/
│       │   ├── pipeline-state.md
│       │   └── ...
│       └── run-2/
│           └── ...
└── {another-project}/
    └── ...
```

## Como criar um novo projeto

1. Certifique-se de que o `kb/environment.md` deste cliente está preenchido
2. Crie a pasta do projeto: `mkdir -p projects/{project-name}/runs`
3. Crie o `briefing.md` com o prompt inicial do cliente
4. Classifique o tipo de projeto e registre em `project-type.md`
5. Inicie o discovery usando o blueprint correspondente ao tipo
