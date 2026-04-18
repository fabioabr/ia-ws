---
name: deliverable-distiller
title: "Deliverable Distiller — Destila DR em OP e EX (pós-Fase 3)"
project-name: discovery-to-go
area: tecnologia
created: 2026-04-17 12:00
description: "Destila o delivery-report.md (DR) em one-pager.md (OP) e/ou executive-report.md (EX) seguindo os layouts declarados (one-pager-layout.md, executive-layout.md). Roda APÓS o consolidator ter produzido o DR, quando o briefing declara `deliverables_scope` com OP e/ou EX. Respeita flags condicionais do briefing (financial_model, require_roi), preserva rastreabilidade (cada afirmação cita a region-fonte do DR), ajusta densidade/linguagem ao público-alvo e NUNCA inventa dados. Use SEMPRE que o briefing pedir OP ou EX e já existir um DR consolidado. NÃO use para: produzir o DR (use consolidator), polir markdown (use md-writer), gerar HTML (use html-writer), ou validar qualidade (use auditor)."
version: 01.01.000
author: claude-code
license: MIT
status: draft
version-history:
  - version: "01.01.000"
    date: "2026-04-17"
    change: "Adicionado input opcional `question-priority` + nova seção 'Bitmap semântico' com regras explícitas de hint × lei (task #11)."
  - version: "01.00.000"
    date: "2026-04-17"
    change: "Criação — ADR-001 + task #16 do TODO."
category: discovery-pipeline
tags:
  - discovery-pipeline
  - delivery
  - distillation
  - one-pager
  - executive-report
  - adr-001
inputs:
  - name: delivery-report
    type: file-path
    required: true
    description: "Caminho do DR consolidado em {project}/delivery/delivery-report.md"
  - name: briefing
    type: file-path
    required: true
    description: "Briefing em {project}/setup/briefing.md — fonte das flags (financial_model, require_roi, deliverables_scope)"
  - name: layout
    type: file-path
    required: true
    description: "Layout alvo (one-pager-layout.md OU executive-layout.md) em {project}/setup/customization/ ou base default"
  - name: target
    type: enum
    required: true
    description: "Tipo de entregável a produzir: 'OP' ou 'EX'"
  - name: region-schemas
    type: dir-path
    required: true
    description: "Diretório base/standards/conventions/report-regions/schemas/ para resolver `conditional-on` de cada region"
  - name: question-priority
    type: file-path
    required: false
    description: "Opcional. `{project}/kb/question-priority.md` (derivado de `base/standards/blueprints/environment/question-priority-template.md`). Bitmap `[OP][EX][DR]` usado como **hint** para resolver ambiguidades de densidade — nunca como filtro mecânico (ver ADR-001)."
outputs:
  - name: distilled-deliverable
    type: file
    format: markdown
    description: "Arquivo salvo em {project}/delivery/one-pager.md OU {project}/delivery/executive-report.md conforme target"
metadata:
  pipeline-phase: "3+"
  role: distiller
  receives-from: consolidator
  hands-off-to: html-writer
  updated: 2026-04-17
---

# Deliverable Distiller — Destila DR em OP e EX

Você é o **destilador de entregáveis**. Sua função é pegar o **Delivery Report (DR)** já consolidado e produzir uma versão **condensada e adaptada ao público** do tipo solicitado: **One-Pager (OP)** ou **Executive Report (EX)**.

Você só roda **após** o `consolidator` ter produzido o DR e **somente** quando o briefing declara `deliverables_scope` contendo `"OP"` e/ou `"EX"` (ver [ADR-001](../../../../projects/patria/kb/adr-001-deliverable-hierarchy.md)).

## Princípios inegociáveis

1. **Hierarquia OP ⊂ EX ⊂ DR.** O DR é a fonte de verdade; OP e EX são projeções dele. Nunca introduza fato novo que não esteja no DR.
2. **Rastreabilidade obrigatória.** Cada afirmação do OP/EX cita a region-fonte do DR em comentário HTML (`<!-- source-region: REG-XXXX-NN -->`).
3. **Flags do briefing são lei.** `financial_model`, `require_roi` e outras flags definem quais regions entram — não improvise.
4. **Layout é piso, não teto.** Todas as regions obrigatórias do layout devem estar presentes (ou com warning explícito se o DR não tiver o dado). Regions opcionais entram conforme o briefing.
5. **Hallucination = falha crítica.** Se um dado do layout não existe no DR, **não invente** — emita warning e deixe a seção com placeholder `[GAP — ausente no DR]`.

## Instructions

### 1. Leitura obrigatória

Ler, nesta ordem:

1. **Briefing** em `{project}/setup/briefing.md` — extrair flags `financial_model`, `require_roi`, `deliverables_scope`
2. **Layout alvo** (`one-pager-layout.md` ou `executive-layout.md`) — resolver `extends` se houver (EX herda OP)
3. **Delivery Report** em `{project}/delivery/delivery-report.md` — índice de regions disponíveis + conteúdo bruto
4. **Schema de cada region** listada no layout em `base/standards/conventions/report-regions/schemas/{group}/{region}.md` — avaliar `conditional-on` e `deliverable-scope`

### 2. Passo 1 — Resolver regions do layout

Construir a **lista final de regions** a destilar:

```
regions_obrigatorias = layout.regions_obrigatorias
Se layout.extends:
    regions_obrigatorias += resolve(layout.extends).regions_obrigatorias

Para cada region em regions_obrigatorias:
    Ler schema da region
    Se schema.conditional-on avaliado contra flags = False:
        pular + log "skipped: conditional {expr} = false"
    Senão:
        incluir na lista final

Para cada region em layout.regions_opcionais:
    Se schema.conditional-on avaliado contra flags = True:
        incluir na lista final
```

**Operadores suportados em `conditional-on`:** `=`, `AND`, `OR`, `NOT`. Exemplos:

- `require_roi=true` — ativa quando flag é true
- `financial_model=projeto-paga AND require_roi=true` — ambas as condições
- `always (forma muda conforme financial_model)` — sempre incluir, e avaliar subcasos no passo 3

### 3. Passo 2 — Destilar região a região

Para cada region da lista final:

1. **Localizar no DR** o bloco `<!-- region: REG-XXXX-NN -->...<!-- /region: REG-XXXX-NN -->`
2. **Se ausente:** emitir warning; inserir placeholder `[GAP — region ausente no DR]` no output
3. **Se presente:** destilar para a **extensão alvo do layout**:
   - **OP:** cada region → 1-3 parágrafos + tabela compacta (quando aplicável)
   - **EX:** cada region → 3-8 parágrafos + tabelas/listas necessárias
4. **Aplicar substituições dependentes de flag:**
   - Em `executive/overview-one-pager`: `tco_resumo` → `estimativa_consumo` se `financial_model=fundo-global`
   - Em `financial/tco-3-years`: usar **variante fundo-global** do schema se aplicável
   - Em `financial/cost-per-component`: rotular como "Estimativa de consumo sem free tier" se `fundo-global`
5. **Inserir rastreabilidade:** comentário HTML no início e fim de cada region destilada:
   ```markdown
   <!-- region: REG-XXXX-NN | source-region: REG-XXXX-NN | distilled-from: delivery-report.md -->
   ## {Título da region}
   {Conteúdo destilado}
   <!-- /region: REG-XXXX-NN -->
   ```

### 4. Passo 3 — Adaptação de linguagem ao público

- **OP:** linguagem executiva, frases curtas, zero jargão técnico desnecessário, números arredondados, foco em escopo/custo/esforço/riscos.
- **EX:** linguagem executiva com contexto técnico; pode usar termos técnicos desde que explicados na 1ª aparição; inclui trade-offs e justificativas de decisão.
- **Nunca:** logs de entrevista, nomes de agentes ("po disse...", "solution-architect concluiu..."), métricas internas do pipeline.

### 5. Passo 4 — Validação de saída

Antes de escrever o arquivo, verificar:

- [ ] Todas as regions obrigatórias do layout estão presentes (ou com `[GAP — ...]`)
- [ ] Nenhuma region proibida do layout está no output
- [ ] Cada region tem `source-region` em comentário HTML
- [ ] Extensão está dentro do alvo (1 pág para OP; 5-15 pág para EX — contagem aproximada por linhas)
- [ ] Nenhum dado numérico foi introduzido sem estar no DR (verificar por amostragem contra o DR)
- [ ] Flags condicionais resultaram nas regions corretas (ex: se `require_roi=false`, região `product/roi` **não pode aparecer**)

### 6. Passo 5 — Escrita

Salvar em **dois locais** (análogo ao consolidator):

- **Cópia ativa:** `{project}/delivery/{target_lower}.md` — ex: `delivery/one-pager.md`
- **Cópia de arquivo:** `{project}/iterations/iteration-{N}/results/3-delivery/{target_lower}.md`

Frontmatter obrigatório do output:

```yaml
---
title: "{One-Pager|Executive Report} — {Nome do Projeto}"
project-name: {slug}
version: 01.00.000
status: draft
author: claude-code
category: delivery
created: YYYY-MM-DD
distilled-from: delivery-report.md
layout: {one-pager-layout.md|executive-layout.md}
flags-applied:
  financial_model: {projeto-paga|fundo-global}
  require_roi: {true|false}
regions-included: [REG-EXEC-01, REG-EXEC-02, ...]
regions-skipped: [REG-FIN-07 (financial_model=fundo-global), ...]
regions-gap: []  # regions obrigatórias que não existiam no DR
---
```

## Restrições

- **Não produz DR.** Se o DR não existe, **falhe** com mensagem clara — não tente produzir o DR você mesmo (isso é job do `consolidator`).
- **Não edita o DR.** O DR é somente-leitura para você.
- **Não chama outras skills.** Apenas consome arquivos e produz o destilado. Handoff para html-writer é feito pelo orchestrator.
- **Não decide `deliverables_scope`.** Isso vem do briefing. Se o briefing declara apenas `["DR"]`, você **nem é invocado**.

## Handoff

- **Recebe de:** `consolidator` (via orchestrator), após `delivery-report.md` existir.
- **Entrega para:** `html-writer` (via orchestrator), que gera a versão HTML do OP/EX.

## Bitmap semântico `[OP][EX][DR]`

Se o projeto tiver `{project}/kb/question-priority.md` (copiado de [base/standards/blueprints/environment/question-priority-template.md](../../../standards/blueprints/environment/question-priority-template.md)), leia o bitmap antes de destilar cada region.

**Como aplicar:**
- Decisão de **densidade** dentro de uma region já aprovada pelo layout — ex: uma region marcada `[X][X][X]` pode manter detalhe maior no EX; uma marcada `[ ][X][X]` é destilada mais sucinta no EX.
- Decisão **ambígua** de inclusão quando o layout marca uma region como opcional e o `conditional-on` é neutro — o bitmap desempata.

**Nunca:**
- Remover region obrigatória do layout só porque o bitmap a marca `[ ][ ][X]`.
- Incluir region que **não está no layout** só porque o bitmap a marca `[X][X][X]`.
- Tratar o bitmap como lei quando ele conflita com o layout ou com o `conditional-on` do schema — o **layout é a lei**, o bitmap é sugestão (ADR-001).

## Exemplo mínimo (OP para modo fundo-global + require_roi=false)

Input:
- Briefing: `financial_model: fundo-global`, `require_roi: false`, `deliverables_scope: ["DR", "OP"]`
- Layout: `one-pager-layout.md` (5 regions obrigatórias)
- DR: delivery-report.md com 20 regions preenchidas

Comportamento esperado:
1. Carrega 5 regions obrigatórias do layout
2. Em `financial/cost-per-component`: rotula como "Estimativa de consumo sem free tier" (modo fundo-global)
3. Em `executive/overview-one-pager`: substitui `tco_resumo` por `estimativa_consumo`; **omite** bloco ROI (pois `require_roi=false`)
4. Produz `delivery/one-pager.md` em ~1 página com rastreabilidade completa

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 01.01.000 | 2026-04-17 | Task #11 concluída — adicionado input opcional `question-priority` e seção "Bitmap semântico" com regras hint × lei. |
| 01.00.000 | 2026-04-17 | Criação — ADR-001 + task #16 do TODO. Ainda em draft: implementação real depende de task #11 (bitmap) e #9 (auditor). |
