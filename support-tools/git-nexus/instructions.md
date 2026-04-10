# GitNexus

Sistema de indexação por knowledge graph que constrói um grafo completo de relacionamentos do codebase, dando a agentes de IA consciência arquitetural profunda antes de realizar mudanças.

## Problema que resolve

Ferramentas de IA como Cursor e Claude Code não possuem consciência do codebase como um todo. Quando um agente edita uma função, ele pode não perceber que 47 outras funções dependem dela, causando breaking changes. O GitNexus resolve isso fornecendo **inteligência relacional pré-computada** no momento da indexação, em vez de forçar o LLM a descobrir relacionamentos por múltiplas consultas.

## Como funciona

- Analisa o repositório usando Tree-sitter e constrói um grafo de dependências
- Detecta clusters funcionais via community detection (Leiden)
- Traça fluxos de execução a partir de entry points
- Expõe 16 ferramentas via MCP (Model Context Protocol) para editores de código

## Modos de uso

| Modo | Descrição |
|------|-----------|
| **CLI + MCP** (recomendado) | Indexa repos localmente, expõe ferramentas via MCP para editores |
| **Web UI** | Explorador de grafo no browser, indexação in-browser, sem servidor |

## Comandos principais

```bash
npm install -g gitnexus       # Instalar globalmente
npx gitnexus analyze           # Indexar repositório atual
npx gitnexus analyze --force   # Forçar re-indexação completa
npx gitnexus analyze --skills  # Gerar skills específicas do repo
npx gitnexus setup             # Configurar MCP para editores (uma vez)
npx gitnexus mcp               # Iniciar servidor MCP
npx gitnexus wiki              # Gerar documentação do repositório
npx gitnexus list              # Listar repos indexados
npx gitnexus clean             # Deletar índice
```

## Ferramentas expostas ao agente (via MCP)

| Ferramenta | O que faz |
|------------|-----------|
| `query` | Busca híbrida (BM25 + semântica) com agrupamento por processo |
| `context` | Visão 360° de um símbolo com referências |
| `impact` | Raio de impacto com agrupamento por profundidade |
| `detect_changes` | Mapeamento de impacto a partir de git diff |
| `rename` | Rename coordenado multi-arquivo |
| `cypher` | Queries raw no grafo |

## Integração com editores

Suporta Claude Code, Cursor, Codex, Windsurf e OpenCode via configuração MCP global por editor.

## Armazenamento

- **CLI:** LadybugDB nativo, persistente, tudo local, sem rede
- **Web UI:** WASM no browser, sem servidor, apenas sessão
- Índice armazenado em `.gitnexus/` (portátil, gitignored)

## Referência

- Repositório: [github.com/abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)
- README completo: [GitNexus README.md](https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md)
