# Rules

Regras adicionais que **só se aplicam** a este cliente. Seguem o mesmo formato das rules do pipeline (`dtg-artifacts/rules/`), mas são carregadas apenas quando o orchestrator detecta que a run é para este cliente.

## Exemplos

- Regra de compliance específica do setor (SOX, PCI-DSS, HIPAA)
- Formato obrigatório de entrega
- Restrições de confidencialidade
- Terminologia obrigatória do cliente

## Prioridade

Regras aqui **sobrescrevem** regras equivalentes de `dtg-artifacts/rules/` e `base-artifacts/behavior/rules/`.
