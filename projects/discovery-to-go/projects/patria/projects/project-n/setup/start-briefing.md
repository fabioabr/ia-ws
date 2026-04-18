---
title: "Briefing — {Nome do Projeto}"
project-name: "{slug-do-projeto}"
project-type: "{saas | datalake-ingestion | process-documentation | web-microservices | system-integration | migration-modernization | ai-ml | mobile-app | process-automation | platform-engineering | generic}"
client: "{nome-do-cliente}"
author: "{nome de quem preencheu}"
created: "YYYY-MM-DD"
report-setup: "complete"  # legacy alias — canonical is deliverables_scope below
status: rascunho
context-templates: []
# Flags de configuração (seção 9) — consumidas pelo config.md do run
financial_model: "fundo-global"  # Patria opera com fundo global de OPEX cloud
require_roi: false
deliverables_scope: ["DR"]
---

# Briefing — {Nome do Projeto}

> Preencha este documento com as informações iniciais do seu projeto. Ele é o ponto de partida do processo de discovery — quanto mais completo, mais precisa será a primeira análise.
>
> **Não precisa ser perfeito.** O processo foi desenhado para extrair e refinar informações ao longo das iterações. Preencha o que souber e marque como "a definir" o que ainda não sabe.
>
> Cada lacuna vira `[INFERENCE]` — uma dedução justificada que será validada nas próximas fases.

---

## 1. Problema (🔴 obrigatório)

**Qual problema queremos resolver?**

Descreva o problema central em 2-5 parágrafos. Foque no **problema**, não na solução.

Exemplo:

```
> Bom: "Analistas financeiros gastam em média 12h/semana consolidando dados de 12 filiais manualmente em planilhas Excel. O processo é sujeito a erros — já tivemos 3 reapresentações ao conselho nos últimos 2 trimestres."
```

```
> Ruim: "Queremos um sistema de consolidação automática."
```

```
{seu texto aqui}
```

**Impacto mensurável** (se souber):

- Tempo perdido: {ex: 12h/semana por analista}
- Custo estimado: {ex: R$ 500K/ano em retrabalho}
- Risco: {ex: erros em relatórios ao conselho}
- Outro: {ex: perda de clientes, multas regulatórias}

---

## 2. Contexto e Domínio (🔴 obrigatório)

**Em que área de negócio estamos?**

| Item | Resposta | Exemplos |
|------|----------|----------|
| Setor / indústria | {sua resposta} | Financeiro, Saúde, Varejo, Logística, Educação, Agro, Energia, Telecomunicações, Governo, Jurídico, Seguros, Imobiliário, Indústria/Manufatura |
| Área da empresa | {sua resposta} | Operações, RH, Financeiro, Contabilidade, TI, Produto, Comercial, Marketing, Atendimento, Jurídico, Compliance, Supply Chain |
| Tipo de projeto | {sua resposta} | Novo produto (SaaS, app, plataforma), Modernização de legado, Automação de processo (RPA, BPM), Integração entre sistemas, Migração de infra/cloud, Pipeline de dados/BI, IA/ML aplicada, Documentação de processos |
| Maturidade | {sua resposta} | Greenfield (do zero, sem sistema atual), Evolução (sistema existe, precisa de melhorias), Substituição de legado (trocar sistema antigo), Migração (mover de on-prem para cloud ou trocar plataforma) |
| Contexto organizacional | {sua resposta} | Startup (time pequeno, agilidade, pouco processo), PME (recursos limitados, decisão rápida), Corporação (processos formais, comitê de aprovação), Multinacional (multi-região, compliance global), Empresa regulada (auditoria obrigatória, normas setoriais) |

---

## 3. Público-alvo (🔴 obrigatório)

**Quem vai usar o que será construído?**

| Perfil | Descrição | Frequência de uso |
|--------|-----------|-------------------|
| {ex: Analista financeiro} | {ex: Executa consolidação mensal} | {ex: Diário} |
| {ex: Controller / CFO} | {ex: Consome relatórios e dashboards} | {ex: Semanal} |
| {ex: Auditor externo} | {ex: Acessa trilha de auditoria} | {ex: Trimestral} |

---

## 4. Stakeholders (🔴 obrigatório)

**Quem está envolvido no projeto?**

Pelo menos 1 dono do produto e 1 dono do orçamento.

| Nome / Papel | Função no projeto | Poder de decisão | Disponível? |
|-------------|-------------------|-------------------|-------------|
| {ex: Maria Silva, CFO} | Patrocinadora | Aprova orçamento | Sim, quinzenal |
| {ex: João Santos, Controller} | Product Owner | Define prioridades | Sim, semanal |
| {ex: Ana Costa, Tech Lead} | Líder técnico | Decide arquitetura | Sim, diário |

---

## 5. Escopo esperado (🔴 obrigatório)

**O que espera que seja entregue neste projeto?**

```
- {ex: Consolidação automática de dados de 12 filiais}
- {ex: Dashboard executivo com P&L consolidado}
- {ex: Trilha de auditoria para compliance SOX}
```

### Resultado esperado

```
- {ex: Redução de 80% no tempo de consolidação}
- {ex: Zero erros materiais em relatórios ao conselho}
- {ex: Fechamento mensal em D+2 (hoje: D+8)}
```

---

## 6. Restrições conhecidas (🟡 recomendado)

**O que já sabemos que limita?**

Anote tudo que **não pode mudar** ou **tem peso forte** na decisão. Quanto mais aqui, menos `[INFERENCE]` será necessário.

| Tipo | Restrição |
|------|-----------|
| **Prazo** | {ex: Precisa estar em produção até Q4 2026} |
| **Orçamento** | {ex: Até R$ 800K no primeiro ano — ou "calcular como output"} |
| **Stack obrigatória** | {ex: Azure, .NET 8, SQL Server} |
| **Stack proibida** | {ex: AWS, MongoDB} |
| **Equipe disponível** | {ex: 4 devs internos + 1 PO; sem budget para contratação} |
| **Compliance** | {ex: LGPD obrigatório, dados ficam no Brasil} |
| **Integrações obrigatórias** | {ex: SAP S/4HANA, Salesforce} |
| **Outros limites** | {ex: Aprovação do comitê de TI necessária} |
| **Uso de IA como aceleradora?** | {ex: SIM, no desenvolvimento de ferramentas de software} |

> [!warning] Orçamento
> Se o orçamento é fechado, declare o valor. Se for "calcular como output", o solution-architect calcula o TCO como resultado do discovery. Ambos os modos são suportados.

---

## 7. Fontes de informação disponíveis (🟡 recomendado)

**De onde podemos buscar mais contexto?**

- [ ] Base de conhecimento corporativa (rag, wiki, Confluence, etc.) — {URL/caminho do manual de como acessar}
- [ ] Nenhuma fonte adicional — apenas este briefing

---

## 8. Expectativa de entrega (🔴 obrigatório)

**O que você espera receber no final do discovery?**

- [ ] Resumo executivo (one-pager para apresentação rápida)
- [ ] Relatório corporativo (visão de negócio, custos, prazos, riscos)
- [ ] Relatório técnico completo (arquitetura, stack, integrações, privacidade)
- [ ] Backlog priorizado (épicos para o time de implementação)
- [ ] Relatório HTML visual (para apresentar ao sponsor/comitê)

**Público da entrega final:**

```
{ex: Comitê executivo + time técnico de implementação}
```

---

## 9. Configurações (🟢 opcional)

### 9.1 Entregáveis (`deliverables_scope`)

Ver [[projects/patria/kb/adr-001-deliverables-model]]. O **Delivery Report (DR)** é sempre gerado pela Fase 3. **One-Pager (OP)** e **Executive Report (EX)** são destilações opcionais pós-Fase 3.

| Valor | Entregáveis gerados | Público |
|-------|---------------------|---------|
| `["DR"]` (default) | delivery-report.md/html | Time técnico, PO |
| `["DR", "OP"]` | + one-pager.md/html | + C-level, sponsor |
| `["DR", "EX"]` | + executive-report.md/html | + Diretoria, comitê |
| `["DR", "OP", "EX"]` | todos | Todos os públicos |

```
deliverables_scope: ["DR"]
```

> [!info] OP ⊂ EX ⊂ DR
> Cada nível é superconjunto semântico do anterior. DR contém tudo; OP e EX são destilações adaptadas ao público.

> [!info] Legacy: `report-setup` (alias aceito)
> O flag antigo `report-setup: essential | executive | complete` ainda é aceito como alias — se `deliverables_scope` estiver presente, ele vence. Mapeamento:
> - `essential` → `["DR", "OP"]`
> - `executive` → `["DR", "OP", "EX"]`
> - `complete` → `["DR", "OP", "EX"]`

### 9.2 Rigor da validação

| Modo | Threshold | Quando usar |
|------|-----------|-------------|
| `alto-risco` | ≥ 90% | Projetos críticos / regulados |
| `padrao` | ≥ 85% | Maioria dos projetos |
| `poc` | ≥ 75% | Validação rápida / prova de conceito |

```
threshold: poc
```

### 9.3 Tipo de projeto

```
project-type: auto-detect
```

> Declare o tipo ou deixe `auto-detect` — o orchestrator detecta pelo conteúdo do briefing. Se errar, você corrige no 1º Human Review.

### 9.4 Simulação do cliente

| Modo | Comportamento |
|------|---------------|
| `sim` | IA simula o cliente na Fase 1 usando este briefing como base |
| `nao` | Pipeline pausa e espera o cliente humano responder |

```
simulacao-cliente: sim
```

> Útil para testes ou quando o cliente não está disponível para a entrevista.

### 9.5 Modelo financeiro (`financial_model`)

| Valor | Significado |
|-------|-------------|
| `projeto-paga` (default) | Projeto aloca budget dedicado; TCO completo com receita projetada quando aplicável |
| `fundo-global` | Cliente opera com fundo corporativo de OPEX cloud; projeto estima consumo sem free tier |

```
financial_model: fundo-global
```

> Para Patria, o default é `fundo-global` — não há budget por projeto; o consumo cloud do projeto é absorvido pelo fundo de OPEX corporativo. O bloco 1.8 passa a reportar **estimativa de consumo** em vez de TCO completo.

### 9.6 Exigência de ROI (`require_roi`)

| Valor | Significado |
|-------|-------------|
| `false` (default) | Discovery ocorre após aprovação global do investimento; não precisa justificar ROI |
| `true` | Briefing exige ROI/payback explícito; auditor valida receita × TCO |

```
require_roi: false
```

> Para Patria, o default é `false` — Discovery acontece após aprovação global. Use `true` apenas se o briefing específico exigir business case com justificativa de retorno.

---

## 10. Notas livres (🟢 opcional)

Qualquer contexto adicional que não cabe nas seções acima: história do projeto, tentativas anteriores, percepções pessoais, política interna relevante, etc.

```
{texto livre}
```

---

## Checklist antes de iniciar

**Preenchimento:**

- [ ] Seções 1 a 5 e 8 preenchidas (🔴 obrigatórias)
- [ ] Pelo menos 1 stakeholder com poder de decisão identificado
- [ ] Escopo com "dentro" e "fora" definidos
- [ ] Expectativa de entrega definida

**Revisores identificados:**

- [ ] Stakeholder para Human Review da Fase 1 (Discovery) identificado
- [ ] Stakeholder para Human Review da Fase 2 (Challenge) identificado
- [ ] Cliente final como revisor da Fase 3 (Delivery) identificado

**Arquivo:**

- [ ] Briefing salvo como `start-briefing.md` na pasta do projeto
