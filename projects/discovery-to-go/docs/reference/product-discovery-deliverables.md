# Entregáveis de um Product Discovery

> **Propósito deste documento:** Definir o que deve ser produzido, como deve ser estruturado e qual o critério de qualidade de cada artefato ao final de um discovery de produto de software.

---

## Princípio Fundamental

> Discovery não entrega especificação completa. Entrega **redução de incerteza suficiente** para comprometer recursos com confiança.
>
> — Inspirado em Marty Cagan (SVPG) e Teresa Torres (*Continuous Discovery Habits*)

Antes de iniciar qualquer entrega, o time deve ter mitigado os **4 riscos fundamentais** (Cagan):

| Risco | Pergunta central |
|---|---|
| **Value** | O usuário vai querer isso? |
| **Usability** | O usuário consegue usar? |
| **Feasibility** | O time consegue construir? |
| **Viability** | Funciona para o negócio? |

Se algum desses riscos ainda for alto ao final do discovery, o produto **não está pronto para entrar em desenvolvimento**.

---

## Estrutura dos Entregáveis

```
Discovery Output
├── 1. Product Brief (executivo)
├── 2. Pesquisa & Evidências
├── 3. Definição do Produto
├── 4. Requisitos
├── 5. Arquitetura & Decisões Técnicas
├── 6. Viabilidade & Riscos
├── 7. Planejamento Inicial
└── 8. Decisão de Continuidade
```

---

## 1. Product Brief

**O quê:** Documento de 1 a 2 páginas para alinhamento executivo e comunicação ampla.

**Formato:** Narrativa curta + tabela de dados-chave.

**Conteúdo obrigatório:**

```markdown
## Product Brief — [Nome do Produto]

**Versão:** 1.0  
**Data:** YYYY-MM-DD  
**Owner:** [Nome]  
**Status:** [ ] Rascunho  [ ] Revisado  [x] Aprovado

### Problema
[1–2 parágrafos descrevendo a dor real, quem sofre e o impacto mensurável]

### Solução Proposta
[1 parágrafo descrevendo a abordagem sem entrar em detalhes de implementação]

### Usuário-Alvo Principal
[Persona ou segmento com uma frase de caracterização]

### Resultado Esperado
[Métrica principal que define sucesso — ex: reduzir X de Y% para Z%]

### MVP
[O que será entregue na primeira versão e o que fica fora]

### Investimento Estimado
[Ordem de grandeza: equipe, tempo, custo]

### Recomendação
[ ] Prosseguir  [ ] Pivotar  [ ] Cancelar
```

**Critério de qualidade:** Um executivo que não participou do discovery deve ler e tomar uma decisão de investimento com base neste documento.

---

## 2. Pesquisa & Evidências

**O quê:** Base factual que justifica todas as decisões do discovery.

### 2.1 Relatório de Entrevistas

**Como conduzir:** Mínimo de 5 a 8 entrevistas com usuários reais usando o framework JTBD (*Jobs To Be Done*).

**Estrutura do relatório:**

```markdown
## Relatório de Entrevistas

### Metodologia
- Perfil dos entrevistados: [critérios de seleção]
- Quantidade: [N entrevistas]
- Período: [data início] a [data fim]
- Formato: [presencial / remoto / assíncrono]

### Perfis Entrevistados
| # | Perfil | Empresa/Contexto | Data |
|---|--------|-----------------|------|
| 1 | ...    | ...             | ...  |

### Achados por Tema
#### Tema 1: [nome]
- **Observação:** [o que foi dito/observado]
- **Frequência:** [X de Y entrevistados mencionaram]
- **Impacto percebido:** [alto / médio / baixo]

### Citações Representativas
> "[Citação literal de alta relevância]" — Entrevistado #3, Gerente de Operações

### Padrões Identificados
[Lista de comportamentos e motivações recorrentes]

### O que surpreendeu
[Achados que contradizem hipóteses iniciais]
```

### 2.2 Mapa de Oportunidades (Opportunity Solution Tree)

**O quê:** Diagrama hierárquico que conecta o objetivo de negócio → oportunidades → soluções → experimentos.

**Formato visual recomendado:** Diagrama em árvore (FigJam, Miro, draw.io).

```
[Objetivo de Negócio]
    └── Oportunidade A (dor/necessidade identificada)
        ├── Solução A1
        │   └── Experimento de validação
        └── Solução A2
            └── Experimento de validação
    └── Oportunidade B
        └── Solução B1
```

**Critério de qualidade:** Cada solução proposta deve ter origem rastreável em pelo menos uma oportunidade, que por sua vez deve ter origem rastreável em evidências de pesquisa.

### 2.3 Dados Quantitativos

```markdown
## Base Quantitativa

### Fontes utilizadas
- Analytics existente: [ferramenta + período]
- Dados de mercado: [fonte + referência]
- Benchmarks: [concorrentes / substitutos]

### Métricas-chave identificadas
| Métrica | Valor atual | Fonte | Relevância |
|---------|-------------|-------|------------|
| ...     | ...         | ...   | ...        |

### Tamanho do problema
[Quantificação: quantas pessoas afetadas, com qual frequência, com qual custo]
```

---

## 3. Definição do Produto

### 3.1 Personas

**Formato por persona:**

```markdown
## Persona: [Nome fictício]

**Perfil:** [cargo, contexto, nível técnico]  
**Faixa etária:** [se relevante]  
**Contexto de uso:** [quando e onde usa o produto]

### Jobs-to-be-done
- **Job funcional:** [tarefa que precisa executar]
- **Job emocional:** [como quer se sentir ao executar]
- **Job social:** [como quer ser percebido]

### Dores atuais
1. [Dor principal com evidência de pesquisa]
2. ...

### Ganhos esperados
1. [Resultado desejado]
2. ...

### Comportamentos relevantes
- [Ferramentas que usa hoje]
- [Workarounds que adota]
- [Critérios de decisão]
```

### 3.2 Mapa de Stakeholders

```markdown
## Mapa de Stakeholders

| Stakeholder | Papel | Influência | Interesse | Estratégia de engajamento |
|-------------|-------|-----------|-----------|--------------------------|
| [Nome/Grupo] | Sponsor | Alta | Alto | Reuniões quinzenais de alinhamento |
| [Nome/Grupo] | Usuário final | Baixa | Alto | Envolver em testes de usabilidade |
| [Nome/Grupo] | Área regulatória | Alta | Médio | Validação de compliance no início |
```

### 3.3 Visão do Produto

```markdown
## Visão do Produto

### Elevator Pitch
Para [usuário-alvo] que [necessidade ou problema],
o [nome do produto] é um [categoria do produto]
que [benefício principal].
Diferente de [alternativa atual],
nosso produto [diferencial].

### Horizonte de 3 anos
[Narrativa de onde o produto estará, sem entrar em roadmap detalhado]

### Princípios de Produto
1. [Princípio guia para decisões de escopo — ex: "simplicidade antes de completude"]
2. ...
```

### 3.4 Escopo do MVP

```markdown
## Escopo do MVP

### Hipótese Central
Acreditamos que [solução] resolverá [problema] para [usuário].
Saberemos que estamos certos quando [métrica] atingir [valor] em [prazo].

### Dentro do MVP
| Funcionalidade | Justificativa | Prioridade |
|----------------|---------------|-----------|
| ...            | ...           | Must-have |

### Fora do MVP (explícito)
| Item | Motivo da exclusão | Fase prevista |
|------|-------------------|---------------|
| ...  | Não valida hipótese central | Fase 2 |

### Critério de Go/No-Go do MVP
[Métrica + valor + prazo que define se o produto evolui ou pivota]
```

---

## 4. Requisitos

### 4.1 Épicos e User Stories de Alto Nível

**Não é necessário refinamento completo para sprint.** O objetivo é comunicar escopo e intenção.

```markdown
## Épico: [Nome]

**Narrativa:** Como [persona], quero [capacidade], para que [benefício de negócio].

**Critérios de aceitação de alto nível:**
- [ ] [Comportamento observável que indica entrega]
- [ ] ...

**Histórias filhas (resumo):**
- US-01: [título]
- US-02: [título]

**Dependências:** [outros épicos ou sistemas]
**Estimativa:** [P / M / G / GG — T-shirt sizing]
```

### 4.2 Requisitos Não-Funcionais Críticos

```markdown
## Requisitos Não-Funcionais

### Performance
- Tempo de resposta máximo: [Xms para operações críticas]
- Throughput esperado: [N requisições/segundo no pico]

### Disponibilidade
- SLA target: [ex: 99,5% — exclui janelas de manutenção]
- RTO (Recovery Time Objective): [X horas]
- RPO (Recovery Point Objective): [X minutos]

### Segurança
- Nível de classificação dos dados: [público / interno / confidencial / restrito]
- Requisitos de autenticação: [ex: MFA obrigatório]
- Regulamentações aplicáveis: [LGPD, SOC2, PCI-DSS, etc.]

### Escalabilidade
- Volume inicial: [N usuários / N transações/dia]
- Volume esperado em 12 meses: [projeção]

### Compatibilidade
- Browsers/plataformas suportados
- Integrações obrigatórias com sistemas existentes
```

---

## 5. Arquitetura & Decisões Técnicas

### 5.1 Diagrama de Contexto (C4 — Nível 1)

**O quê:** Visão de caixas-pretas mostrando o sistema e seus vizinhos.

```
[Usuário Final] ──► [Sistema Novo] ──► [Sistema Legado A]
                         │
                         └──────────► [API Externa B]
                         │
                    [Administrador]
```

**Ferramenta recomendada:** draw.io, Mermaid, PlantUML, C4-PlantUML.

**Critério de qualidade:** Qualquer desenvolvedor sênior deve conseguir identificar todas as integrações e atores sem precisar perguntar.

### 5.2 Diagrama de Containers (C4 — Nível 2, quando aplicável)

Detalha os principais containers técnicos: aplicação web, API, banco de dados, filas, etc.

```
[Sistema Novo]
├── Frontend (Blazor WebAssembly)
├── API Gateway
├── Serviço de Domínio A (.NET 8 / ASP.NET Core)
├── Serviço de Domínio B
├── Banco de Dados Principal (SQL Server / MongoDB)
└── Message Broker (RabbitMQ / Azure Service Bus)
```

### 5.3 ADR — Architecture Decision Records

**Formato por decisão:**

```markdown
## ADR-001: [Título da Decisão]

**Data:** YYYY-MM-DD  
**Status:** [ ] Proposto  [x] Aceito  [ ] Depreciado  [ ] Substituído por ADR-XXX

### Contexto
[Situação que tornou esta decisão necessária]

### Decisão
[O que foi decidido, de forma afirmativa e direta]

### Opções Consideradas
| Opção | Prós | Contras |
|-------|------|---------|
| A     | ...  | ...     |
| B     | ...  | ...     |

### Consequências
**Positivas:**
- ...

**Negativas / Trade-offs aceitos:**
- ...

### Referências
- [Links, documentos, experimentos que embasaram a decisão]
```

**ADRs mínimas esperadas num discovery:**
- Escolha de stack / linguagem principal
- Modelo de persistência (relacional vs. documental vs. híbrido)
- Estratégia de integração com sistemas legados
- Modelo de autenticação e autorização
- Estratégia de deployment (cloud provider, containers, serverless)

### 5.4 Riscos Técnicos

```markdown
## Riscos Técnicos Identificados

| # | Risco | Probabilidade | Impacto | Mitigação proposta |
|---|-------|--------------|---------|-------------------|
| 1 | [Descrição] | Alta | Alto | [Ação concreta] |
| 2 | ...  | Média | Médio | ... |
```

---

## 6. Viabilidade & Riscos

### 6.1 Análise de Viabilidade

```markdown
## Análise de Viabilidade

### Técnica
**Veredicto:** [ ] Viável  [ ] Viável com ressalvas  [ ] Inviável
**Justificativa:** [O time tem capacidade? Existem dependências críticas não controláveis?]

### Financeira
**Veredicto:** [ ] Viável  [ ] Viável com ressalvas  [ ] Inviável
**Custo estimado total:** [ordem de grandeza]
**Break-even estimado:** [prazo ou volume]

### Operacional
**Veredicto:** [ ] Viável  [ ] Viável com ressalvas  [ ] Inviável
**Justificativa:** [A organização consegue operar o produto após o lançamento?]

### Regulatória / Compliance
**Veredicto:** [ ] Viável  [ ] Viável com ressalvas  [ ] Inviável
**Regulamentações mapeadas:** [LGPD, setor específico, etc.]
```

### 6.2 Risk Register

```markdown
## Risk Register

| # | Risco | Categoria | Probabilidade (1-5) | Impacto (1-5) | Score | Resposta | Dono |
|---|-------|-----------|--------------------|--------------:|------:|----------|------|
| 1 | [Descrição] | Técnico | 3 | 4 | 12 | Mitigar: [ação] | [nome] |
| 2 | ...   | Negócio   | 2 | 5 | 10 | Aceitar | [nome] |

**Score = Probabilidade × Impacto**  
**Threshold de atenção:** Score ≥ 9 requer plano de resposta documentado.
```

### 6.3 Hipóteses Críticas Não Validadas

```markdown
## Hipóteses em Aberto

| Hipótese | Risco se falsa | Como validar | Prazo |
|----------|---------------|-------------|-------|
| [Usuários pagarão X/mês] | Alto — modelo de negócio inviável | Teste de preço com landing page | Sprint 1 |
| [Integração com sistema Y é possível via API] | Alto — retrabalho de arquitetura | PoC técnico | Sprint 1–2 |
```

---

## 7. Planejamento Inicial

### 7.1 Estimativa de Esforço

```markdown
## Estimativa de Esforço (T-shirt sizing)

| Épico | Complexidade | Estimativa | Premissas |
|-------|-------------|-----------|-----------|
| Épico 1 | Alta | GG (> 3 sprints) | Depende de integração X |
| Épico 2 | Baixa | P (< 1 sprint) | — |

**Esforço total estimado para MVP:** [X a Y sprints com equipe de Z pessoas]

> ⚠️ Esta é uma estimativa de ordem de grandeza. Refinamento detalhado ocorre no Sprint 0.
```

### 7.2 Proposta de Faseamento

```markdown
## Fases de Entrega

### Fase 0 — Sprint 0 (Semanas 1–2)
- Setup de ambiente e infraestrutura
- Refinamento do backlog do MVP
- Spike de validação de riscos técnicos críticos

### Fase 1 — MVP (Semanas 3–N)
**Objetivo:** Validar hipótese central com usuários reais
**Funcionalidades:** [lista de épicos incluídos]
**Critério de saída:** [métrica de sucesso]

### Fase 2 — Evolução (pós-validação MVP)
**Objetivo:** Expandir com base no aprendizado
**Funcionalidades:** [lista de épicos diferidos]

### Fase N — Escala
[Visão de longo prazo]
```

### 7.3 Equipe Necessária

```markdown
## Composição de Equipe

| Papel | Dedicação | Fase | Observação |
|-------|-----------|------|-----------|
| Product Manager | 100% | Todas | |
| Tech Lead / Solutions Architect | 100% | Fase 0–1, parcial após | |
| Desenvolvedor Backend | 100% | Fase 1+ | .NET / C# |
| Desenvolvedor Frontend | 100% | Fase 1+ | Blazor |
| QA Engineer | 50–100% | Fase 1+ | |
| UX Designer | 50% | Fase 0–1 | |
| DevOps / SRE | 25% | Fase 0, on-demand | |
```

---

## 8. Decisão de Continuidade

**Este é o artefato mais importante do discovery.** Deve ser um documento simples, direto e assinável.

```markdown
## Decisão de Continuidade — [Nome do Produto]

**Data:** YYYY-MM-DD  
**Facilitador do Discovery:** [Nome]

---

### Resumo da Recomendação

**[ ] PROSSEGUIR** — Os 4 riscos estão mitigados. Aprovado para desenvolvimento.  
**[ ] PIVOTAR** — [Descrever o que deve mudar antes de prosseguir]  
**[ ] CANCELAR** — [Justificativa]

---

### Evidências que embasam a decisão

| Risco | Status | Evidência |
|-------|--------|-----------|
| Value | ✅ Mitigado | Entrevistas com 7 usuários confirmaram disposição de uso |
| Usability | ✅ Mitigado | Protótipo testado com 5 usuários, taxa de conclusão de tarefa: 80% |
| Feasibility | ⚠️ Parcial | PoC de integração com sistema X pendente — Sprint 0 |
| Viability | ✅ Mitigado | ROI estimado positivo em 18 meses |

---

### Condições para prosseguir

1. [Condição obrigatória antes do início do desenvolvimento]
2. ...

---

### Próximos Passos Imediatos

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Kick-off do Sprint 0 | Tech Lead | [data] |
| PoC de integração com X | Dev Backend | Fim do Sprint 0 |
| Contratação de QA | RH + PM | [data] |

---

### Assinaturas de Aprovação

| Papel | Nome | Assinatura | Data |
|-------|------|-----------|------|
| Product Owner / Sponsor | | | |
| Tech Lead / Arquiteto | | | |
| Gestor de Negócio | | | |
```

---

## Checklist Final de Discovery

Use este checklist antes de declarar o discovery concluído:

```markdown
## Checklist de Conclusão

### Pesquisa & Problema
- [ ] Mínimo de 5 entrevistas com usuários reais realizadas
- [ ] Problem statement validado com evidências (não só hipóteses)
- [ ] Mapa de oportunidades (OST) construído e revisado
- [ ] Dados quantitativos coletados e documentados

### Produto
- [ ] Personas documentadas com jobs-to-be-done
- [ ] Mapa de stakeholders completo
- [ ] Visão do produto escrita e aprovada
- [ ] Escopo do MVP definido (dentro E fora explícitos)
- [ ] Hipótese central declarada com critério de validação

### Requisitos
- [ ] Épicos de alto nível documentados
- [ ] Requisitos não-funcionais críticos mapeados
- [ ] Compliance e regulamentações verificados

### Técnico
- [ ] Diagrama de contexto (C4 L1) produzido
- [ ] ADRs das decisões críticas documentadas
- [ ] Riscos técnicos mapeados com mitigação
- [ ] Stack tecnológica definida e justificada

### Viabilidade
- [ ] Viabilidade técnica, financeira e operacional avaliadas
- [ ] Risk register completo (probabilidade × impacto)
- [ ] Hipóteses não validadas listadas com plano de validação

### Planejamento
- [ ] Estimativa de esforço para MVP (T-shirt sizing)
- [ ] Faseamento proposto
- [ ] Equipe necessária definida

### Decisão
- [ ] Product Brief escrito e revisado
- [ ] Documento de decisão de continuidade preenchido
- [ ] Aprovação dos stakeholders obtida
```

---

## Referências

| Framework | Autor | Aplicação neste documento |
|-----------|-------|--------------------------|
| Dual-Track Agile | Jeff Patton, Marty Cagan | Separação discovery/delivery |
| Continuous Discovery Habits | Teresa Torres | OST, entrevistas contínuas, assumption mapping |
| INSPIRED / EMPOWERED | Marty Cagan (SVPG) | Os 4 riscos como checklist de prontidão |
| Jobs To Be Done | Christensen / Moesta | Estrutura das personas e entrevistas |
| Architecture Decision Records | Michael Nygard | Formato de ADR |
| C4 Model | Simon Brown | Diagramas de arquitetura |
| Shape Up | Ryan Singer (Basecamp) | Conceito de apetite e shaping |

---

*Documento mantido por: [nome/time]*  
*Última revisão: YYYY-MM-DD*  
*Versão: 1.0*
