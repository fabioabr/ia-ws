---
title: "Briefing — {Nome do Projeto}"
project-name: "{slug-do-projeto}"
project-type: "{saas | datalake-ingestion | process-documentation | web-microservices | system-integration | migration-modernization | ai-ml | mobile-app | process-automation | platform-engineering | generic}"
client: "{nome-do-cliente}"
author: "{nome de quem preencheu}"
created: "YYYY-MM-DD"
report-setup: "complete"
status: rascunho
context-templates: []
---

# Briefing — {Nome do Projeto}

> Preencha este documento com as informações iniciais do seu projeto. Ele é o ponto de partida do processo de discovery — quanto mais completo, mais precisa será a primeira análise.
>
> **Não precisa ser perfeito.** O processo foi desenhado para extrair e refinar informações ao longo das iterações. Preencha o que souber e marque como "a definir" o que ainda não sabe.

---

## 1. Problema

**Qual problema queremos resolver?**

Descreva o problema central em 2-5 parágrafos. Foque no **problema**, não na solução.

> Exemplo: "Analistas financeiros gastam em média 12h/semana consolidando dados de 12 filiais manualmente em planilhas Excel. O processo é sujeito a erros — já tivemos 3 reapresentações ao conselho nos últimos 2 trimestres."

```
{seu texto aqui}
```

**Impacto mensurável** (se souber):
- Tempo perdido: {ex: 12h/semana por analista}
- Custo estimado: {ex: R$ 500K/ano em retrabalho}
- Risco: {ex: erros em relatórios ao conselho}
- Outro: {ex: perda de clientes, multas regulatórias}

---

## 2. Contexto e Domínio

**Em que área de negócio estamos?**

| Item | Resposta |
|------|----------|
| Setor / indústria | {ex: Financeiro, Saúde, Varejo, Tecnologia} |
| Área da empresa | {ex: Operações, RH, Financeiro, TI, Produto} |
| Tipo de projeto | {ex: Novo produto, Modernização, Automação, Integração} |
| Maturidade | {ex: Greenfield (do zero), Evolução de existente, Substituição de legado} |
| Contexto organizacional | {ex: Startup, PME, Multinacional, Empresa regulada} |

---

## 3. Público-alvo

**Quem vai usar o que será construído?**

| Perfil | Descrição | Frequência de uso |
|--------|-----------|-------------------|
| {ex: Analista financeiro} | {ex: Executa consolidação mensal} | {ex: Diário} |
| {ex: Controller / CFO} | {ex: Consome relatórios e dashboards} | {ex: Semanal} |
| {ex: Auditor externo} | {ex: Acessa trilha de auditoria} | {ex: Trimestral} |

---

## 4. Stakeholders

**Quem está envolvido no projeto?**

| Nome / Papel | Função no projeto | Poder de decisão | Disponível? |
|-------------|-------------------|-------------------|-------------|
| {ex: Maria Silva, CFO} | Patrocinadora | Aprova orçamento | Sim, quinzenal |
| {ex: João Santos, Controller} | Product Owner | Define prioridades | Sim, semanal |
| {ex: Ana Costa, Tech Lead} | Líder técnico | Decide arquitetura | Sim, diário |

---

## 5. Escopo esperado

**O que esperamos que este projeto faça?**

### Dentro do escopo (o que SIM será feito)

```
- {ex: Consolidação automática de dados de 12 filiais}
- {ex: Dashboard executivo com P&L consolidado}
- {ex: Trilha de auditoria para compliance SOX}
```

### Fora do escopo (o que NÃO será feito)

```
- {ex: Módulo de planejamento orçamentário}
- {ex: Integração com sistema de RH}
- {ex: App mobile}
```

### Resultado esperado

```
- {ex: Redução de 80% no tempo de consolidação}
- {ex: Zero erros materiais em relatórios ao conselho}
- {ex: Fechamento mensal em D+2 (hoje: D+8)}
```

---

## 6. Restrições conhecidas

**O que já sabemos que limita?**

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

> Se o orçamento é fechado, declare o valor. Se for "calcular como output", o arquiteto de solução calcula o TCO como resultado do discovery.

---

## 7. Fontes de informação disponíveis

**De onde podemos buscar mais contexto?**

- [ ] Documentos anexos — {listar arquivos}
- [ ] Sistema legado com documentação — {qual sistema, onde está a doc}
- [ ] Entrevistas prévias / pesquisas — {onde estão}
- [ ] Benchmarks / concorrentes analisados — {quais}
- [ ] Base de conhecimento corporativa (wiki, Confluence, etc.) — {URL/caminho}
- [ ] Nenhuma fonte adicional — apenas este briefing

---

## 8. Expectativa de entrega

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

## 9. Configurações (opcional)

| Configuração | Valor | Opções |
|-------------|-------|--------|
| **Nível de detalhe do report** | {complete} | `essential` (one-pager) / `executive` (corporativo) / `complete` (tudo) |
| **Rigor da validação** | {padrão} | `padrão` (≥90%) / `alto-risco` (≥95%) / `poc` (≥80%) |
| **Tipo de projeto** | {auto-detect} | Declare ou deixe auto-detect pelo conteúdo deste briefing |

---

## 10. Notas livres (opcional)

Qualquer contexto adicional que não cabe nas seções acima: história do projeto, tentativas anteriores, percepções pessoais, política interna relevante, etc.

```
{texto livre}
```

---

## Checklist antes de iniciar

- [ ] Seções 1 a 6 preenchidas
- [ ] Pelo menos 1 stakeholder com poder de decisão identificado
- [ ] Expectativa de entrega definida (seção 8)
- [ ] Arquivo salvo como `briefing.md` na pasta do projeto
