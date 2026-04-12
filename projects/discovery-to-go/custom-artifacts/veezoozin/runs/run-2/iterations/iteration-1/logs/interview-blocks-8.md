---
title: "Interview Log — Bloco #8"
project: veezoozin
run: run-2
iteration: 1
phase: discovery
blocks: [8]
simulation: true
depends-on: [1, 2, 3, 4, 5, 6, 7]
roles:
  solution-architect: claude-code
  customer: claude-code (simulado)
  orchestrator: claude-code
author: claude-code
created: 2026-04-12
---

# Interview Log — Bloco #8

> [SIMULADO — customer gerado por IA baseado no briefing. Respostas marcadas com `[BRIEFING]` (direto do briefing), `[INFERENCE]` (deduzido a partir do contexto). Nenhuma resposta `[RAG]` nesta sessão.]
>
> **Nota:** Bloco #8 depende de TODOS os blocos anteriores (D1–D49). O Solution Architect conduz a análise de TCO 3 anos, Build vs Buy dos componentes críticos, break-even e cenários alternativos de viabilidade.

---

## Bloco #8 — TCO e Build vs Buy

> Usando outputs dos Blocos #1-#7 como base. Todas as 49 decisões anteriores como input. Números-chave: MRR R$ 994 (lançamento) → R$ 31.862 (mês 12), ARR ~R$ 382K (ano 1), time R$ 75K/mês (6 pessoas), stack GCP (Cloud Run, Vertex AI, BigQuery, Cloud SQL, Firestore), LLM Claude/Gemini, cache 4 camadas.

| Quem | Diálogo |
|------|---------|
| 🏗️ SA | Vamos construir o TCO de 3 anos. Preciso que a gente seja brutalmente honesto com os números — se a conta não fechar, precisamos saber agora. Começando pela infraestrutura GCP. O Bloco #3 estimou R$ 4K/mês no MVP. Vamos detalhar com preços reais. |
| 👤 Customer | [BRIEFING] A stack definida no Bloco #5 é: Cloud Run (compute), Cloud SQL PostgreSQL (metadata), BigQuery (queries read-only dos tenants), Vertex AI (embeddings), Firestore (cache e sessões), Cloud Storage (exports). Tudo em GCP southamerica-east1 porque temos créditos e incentivos enterprise. |
| 🏗️ SA | Cloud Run primeiro. Preço real: US$ 0.00002400/vCPU-second, US$ 0.00000250/GiB-second. No MVP com 1-2 instâncias, 1 vCPU, ~9.000 requests/mês... dá cerca de US$ 80/mês, ou R$ 400. O Bloco #3 estimou R$ 800 — a estimativa era conservadora, o real é menor. |
| 👤 Customer | [INFERENCE] Cloud Run escala a zero para instâncias excedentes, então no MVP com pouco tráfego o custo é realmente baixo. O problema vem na escala: com 300+ tenants no mês 36, estimamos 30-50 instâncias com 16 vCPUs — aí chega a R$ 22.500/mês. É o componente de infra que mais escala. |
| 🏗️ SA | Cloud SQL. O db-f1-micro custa ~US$ 10/mês. Para MVP com row-level tenancy (D24) é suficiente. |
| 👤 Customer | [INFERENCE] Sim, mas conforme crescemos precisamos de db-custom com read replicas e HA. No mês 36 com 300+ tenants: db-custom-4-16384 com 2 read replicas e HA, mais database dedicado para Enterprise — uns R$ 5.500/mês. Storage SSD a US$ 0.17/GiB. |
| 🏗️ SA | BigQuery — o Veezoozin não armazena dados, apenas executa queries. US$ 5/TB scanned. Qual o volume estimado? |
| 👤 Customer | [INFERENCE] Cada query simples escaneia em média ~55 KB. Com 9.000 queries/mês no MVP: ~0.5 TB — custo quase zero, R$ 13. Em escala com 3 milhões de queries/mês no ano 3: ~150 TB — R$ 3.750/mês. E o cache de resultado (D46, camada 4) reduz ~30% das execuções. Os créditos GCP reduzem ainda mais. |
| 🏗️ SA | Agora o elefante na sala: custo de LLM APIs. São 2 chamadas por query — SQL gen e insight gen. Qual o custo real? |
| 👤 Customer | [INFERENCE] Com Claude Sonnet para produção: ~R$ 15/1M tokens input, ~R$ 75/1M tokens output. Cada query usa ~2.300 tokens input e ~600 output nas 2 chamadas combinadas. Custo unitário: ~R$ 0,08 por query com prompt otimizado. Gemini Pro é ~60% mais barato. No MVP sem cache: R$ 1.200/mês para 9.000 queries. No ano 3 com 3M queries, cache de 50% e mix 65/35 Claude/Gemini: R$ 65.000/mês. |
| 🏗️ SA | 💡 *Observação: LLM APIs são o segundo maior custo variável após equipe. O cache (D46) é literalmente um projeto de redução de custo — sem cache de 50%, o custo LLM no ano 3 seria R$ 130.000/mês, o dobro. A migração gradual para Gemini (mais barato + créditos GCP) é outra alavanca.* |
| 🏗️ SA | Equipe. O Bloco #4 definiu R$ 75K/mês para 6 pessoas no MVP. Qual a projeção de 3 anos? |
| 👤 Customer | [INFERENCE] MVP: 6 pessoas (R$ 75K/mês). Fase 2: +2, total 8 (R$ 105K). Fase 3: +2, total 10 (R$ 135K). Mês 12: 12 pessoas (R$ 165K). Ano 2: 15 pessoas com reajuste anual de ~8% (R$ 210K). Ano 3: 18 pessoas (R$ 260K). Total em 3 anos: R$ 6.990.000. Isso é 66,5% do TCO total. |
| 🏗️ SA | 💡 *Observação: equipe é dois terços do TCO. Qualquer otimização de infra ou LLM é marginal perto do impacto do headcount. Precisamos ser disciplinados: não contratar por antecipação. Revisar headcount trimestralmente.* |
| 🏗️ SA | Consolidando o TCO total de 3 anos? |
| 👤 Customer | [INFERENCE] Equipe R$ 6.990.000 + Infra GCP R$ 973.000 + LLM APIs R$ 1.464.000 + SaaS terceiros R$ 363.000 + Marketing R$ 1.390.000 = **R$ 10.510.000**. Com 30% de créditos GCP sobre infra + Vertex AI: ~R$ 9.778.000. |
| 🏗️ SA | Agora Build vs Buy. Quais componentes temos que decidir? |
| 👤 Customer | [INFERENCE] Seis componentes críticos: (1) NL-to-SQL Engine, (2) Vector Store, (3) LLM, (4) Auth, (5) Visualização, (6) Billing. Para cada um: Build é diferencial competitivo? Buy tem custo justificável? Time de 6 (D17) consegue operar? |
| 🏗️ SA | NL-to-SQL Engine — a decisão mais importante. Existem soluções prontas: Vanna.ai, Dataherald, Text2SQL. Por que não usar? |
| 👤 Customer | [INFERENCE] Porque o engine É o produto. O pipeline de 8 etapas com glossário por tenant, RLS injection, cache semântico, privacy guard, multi-idioma — isso não existe em nenhuma solução pronta. Vanna.ai tem glossário básico mas sem RLS, sem privacy guard, sem multi-idioma. Comprar isso commoditiza nosso valor. Qualquer concorrente pode plugar Vanna.ai e ter o mesmo resultado. Nosso moat é o contexto por tenant (Bloco #1). |
| 🏗️ SA | 💡 *Observação: decisão correta. Build apenas o que é moat. O NL-to-SQL Engine com contexto por tenant é a única coisa que diferencia o Veezoozin de "ChatGPT + SQL". Todo o resto pode ser commodity.* |
| 🏗️ SA | Vector Store? |
| 👤 Customer | [INFERENCE] Buy — Vertex AI Vector Search. Não é diferencial. É infraestrutura. Self-hosted (Qdrant, Weaviate) custa menos em 3 anos (~R$ 120K vs R$ 180K) mas requer SRE para operar backup, scaling, monitoring. Com time de 6 pessoas (D17), não temos capacity. Vertex AI é GCP-native, zero operação, créditos aplicáveis. |
| 🏗️ SA | LLM? |
| 👤 Customer | [BRIEFING] Buy — D3 é decisão do briefing. Sem fine-tune, sem modelo próprio. APIs Claude + Gemini. Custo em 3 anos: R$ 1.464.000. Hosting de modelo próprio seria ~R$ 800K (GPU) mas qualidade inferior e time de ML inexistente. |
| 🏗️ SA | Auth? |
| 👤 Customer | [INFERENCE] Buy — Firebase Auth (D28). Implementação custom de auth é risco de segurança desnecessário. Firebase é free tier generoso, GCP-native, suporte SAML/OIDC para Enterprise. Auth é o componente que menos devemos arriscar implementar do zero — um bug de auth é catastrófico. Persona Carla (Bloco #2 — poder de veto) exige segurança comprovada. |
| 🏗️ SA | Visualização? |
| 👤 Customer | [INFERENCE] Buy — Recharts ou Nivo (open-source, custo zero). São React-based (D25 — Next.js), altamente customizáveis. Implementar rendering engine custom é desvio de foco. O moat não é o gráfico — é o contexto + SQL generation + insight. Se precisar trocar de biblioteca no futuro, é trivial. |
| 🏗️ SA | Billing? |
| 👤 Customer | [INFERENCE] Buy — Stripe (D27). Antipattern #2 do blueprint SaaS: "billing custom no MVP é armadilha". Stripe custa ~R$ 340K em 3 anos em fees (2.9% sobre receita), mas evita 6-10 semanas de dev + PCI compliance + dunning custom + usage metering custom. Se o fee ficar pesado na escala, Lago (open-source) é alternativa para Fase 3. |
| 🏗️ SA | 💡 *Observação: padrão claro — Build o moat (NL-to-SQL), Buy todo o resto. Seis componentes, apenas 1 é Build. Isso é disciplina para time enxuto (D17). Registrar como D50.* |
| 🏗️ SA | Agora o momento da verdade. Receita vs TCO em 3 anos. |
| 👤 Customer | [INFERENCE] Receita cenário conservador do Bloco #3: MRR cresce de R$ 994 (lançamento) para R$ 31.862 (mês 12), projetando R$ 173.250 (mês 36). Total de receita em 3 anos: ~R$ 2.447.000. TCO: R$ 10.510.000. Déficit: R$ -8.063.000. Receita cobre apenas 23,3% do TCO. |
| 🏗️ SA | Isso é preocupante. Vamos ser claros: o projeto NÃO se paga em 3 anos no cenário conservador. |
| 👤 Customer | [INFERENCE] Correto. Mas isso é esperado para SaaS B2B greenfield. A maioria dos SaaS leva 3-5 anos para break-even total. O ponto relevante é: (1) a operação mensal se torna sustentável antes disso? (2) o crescimento justifica captação de investimento? |
| 🏗️ SA | 💡 *Observação: P22 acionado — receita < TCO em 3 anos. Precisamos de cenários alternativos. Vamos explorar 3+.* |
| 🏗️ SA | Cenário A: pricing mais alto. O Bloco #3 definiu Pro R$ 497 e Enterprise R$ 1.997. ThoughtSpot cobra US$ 95/user/mês. Há espaço? |
| 👤 Customer | [INFERENCE] Sim. Pro a R$ 697 (+40%) ainda posiciona o Veezoozin ~30% abaixo do ThoughtSpot por usuário. Enterprise a R$ 2.997 (+50%) com add-ons de R$ 4.500 ticket médio é competitivo para o valor entregue (democracia de dados, multi-idioma, contexto por tenant). Receita 3 anos sobe para ~R$ 3.436.000. Melhora mas não resolve sozinho. |
| 🏗️ SA | Cenário B: redução de escopo. O que cortar? |
| 👤 Customer | [INFERENCE] O maior candidato a corte é a insight generation automática (etapa 7 do pipeline). Remove uma chamada LLM por query — corta ~50% do custo LLM. O usuário ainda recebe gráfico e dados, mas sem o insight textual automático. Team reduzido para 4 no MVP (sem Designer e sem PO dedicado, Fabio acumula). Time máximo 8 no ano 3. Marketing 50% menor. TCO cai para R$ 6.617.000. Mas receita pode cair ~10% sem insights (NPS menor → conversão menor). |
| 🏗️ SA | 💡 *Observação: Cenário B é o "modo sobrevivência". Funciona para bootstrap, mas sacrifica diferenciação. O insight textual é parte do momento "Aha!" da persona Marina (Bloco #2). Cortar isso pode matar a ativação. Usar apenas se os cenários de crescimento falharem.* |
| 🏗️ SA | Cenário C: crescimento acelerado. O que precisa acontecer? |
| 👤 Customer | [INFERENCE] Product-market fit forte desde o lançamento. 50 Pro + 10 Enterprise no mês 12 (vs 46 no base). 250 Pro + 50 Enterprise no mês 36. Enterprise ticket médio de R$ 4.500 com upsell agressivo. Receita 3 anos: R$ 4.937.000. Mas TCO também sobe ~13% porque mais tráfego = mais LLM e infra. |
| 🏗️ SA | E se combinarmos A + C? |
| 👤 Customer | [INFERENCE] Cenário D — o mais realista para viabilidade. Pricing ajustado (Pro R$ 697, Enterprise R$ 2.997) E crescimento acelerado. Receita 3 anos: R$ 7.016.000. TCO: ~R$ 11.860.000. Break-even mensal (MRR > custos mensais) no mês ~24 pós-lançamento. Não recupera o investimento acumulado em 3 anos, mas a operação se torna sustentável. Isso é financiável via rodadas de investimento. |
| 🏗️ SA | 💡 *Observação: Cenário D é o "target scenario". Exige execution forte: pricing validado nos primeiros 3 meses, foco em Enterprise desde o mês 6, cache agressivo para controlar custo LLM, headcount disciplinado. Registrar gatilhos Go/No-Go nos meses 8, 12 e 24.* |
| 🏗️ SA | Falando em gatilhos — quais são os marcos de decisão? |
| 👤 Customer | [INFERENCE] Quatro marcos: (1) Mês 8 (3 meses pós-lançamento): ≥ 8 Pro + 1 Enterprise. Se não atingir, rever pricing e posicionamento. (2) Mês 12: MRR ≥ R$ 30K. Se não, rever equipe e considerar cenário B. (3) Mês 18: MRR ≥ R$ 80K. Se < R$ 50K, cenário B agressivo. (4) Mês 24: break-even mensal. Se não, avaliar captação ou redução para equipe mínima. |
| 🏗️ SA | Investimento necessário? |
| 👤 Customer | [INFERENCE] MVP: ~R$ 338K — bootstrap dos sócios. Ano 1 total: R$ 1.845.000 — precisa de Pre-seed/Angel de ~R$ 1.5M. Ano 2: Seed round de R$ 3-5M. Ano 3: Series A se métricas confirmarem. O MRR de R$ 500K+ no mês 36 (cenário D) é pitch atraente para Series A. |
| 🏗️ SA | 💡 *Observação: a história de investimento faz sentido se os marcos forem atingidos. MRR R$ 500K+ com 300 tenants pagantes é um SaaS B2B saudável para Series A. O TCO de R$ 10M em 3 anos não é assustador nesse contexto — é o custo de construir um SaaS com margem bruta de 60%+ projetada. O ponto é: os marcos do mês 8 e 12 são o teste real de viabilidade.* |
| 🏗️ SA | Uma última recomendação: D11 definiu pricing Pro R$ 497 e Enterprise R$ 1.997. Os números de TCO sugerem que deveríamos lançar com Pro R$ 697 e Enterprise R$ 2.997 desde o início. Isso atualiza D11. |
| 👤 Customer | [INFERENCE] Concordo, com uma ressalva: validar nos primeiros 3 meses com early adopters. Se o mercado resistir, podemos baixar. Mas é mais fácil baixar preço do que subir. Registrar como D51 — recomendação de pricing, sujeita a validação. |
| 🏗️ SA | Consolidando. Bloco #8 gera 7 novas decisões: D50 (Build apenas NL-to-SQL, Buy todo o resto), D51 (pricing recomendado Pro R$ 697 / Enterprise R$ 2.997), D52 (TCO R$ 10.5M — equipe é 66,5%), D53 (break-even mensal mês ~24 no cenário D), D54 (gatilhos Go/No-Go), D55 (investimento necessário), D56 (migração gradual para Gemini). Total acumulado: 56 decisões (D1-D56). |

---

## Resumo de Decisões do Bloco #8

| # | Decisão | Fonte |
|---|---------|-------|
| D50 | NL-to-SQL Engine é o único componente BUILD — todo o resto é BUY | [INFERENCE] — moat competitivo, D3, D17, D27, D28 |
| D51 | Pricing recomendado: Pro R$ 697, Enterprise R$ 2.997 (atualiza D11) | [INFERENCE] — TCO exige receita maior, benchmark ThoughtSpot |
| D52 | TCO 3 anos estimado R$ 10.5M — equipe é 66,5% do custo | [INFERENCE] — consolidação de todos os blocos |
| D53 | Break-even mensal no cenário D (pricing + crescimento) no mês ~24 | [INFERENCE] — cenário combinado A+C |
| D54 | Gatilhos Go/No-Go: mês 8 (≥ 8 Pro + 1 Ent), mês 12 (MRR ≥ R$ 30K), mês 24 (break-even) | [INFERENCE] — marcos de viabilidade |
| D55 | Investimento necessário: ~R$ 1.8M Ano 1, Pre-seed/Angel ~R$ 1.5M | [INFERENCE] — projeção financeira |
| D56 | Migração gradual para Gemini (40% até mês 12) para reduzir custo LLM | [INFERENCE] — Gemini ~60% mais barato, créditos GCP |

---

## Rastreabilidade de Fontes

| Informação-chave | Fonte | Tag |
|------------------|-------|:---:|
| Stack GCP obrigatória | Briefing seção 6 | [BRIEFING] |
| Créditos e incentivos GCP | Briefing seção 10 | [BRIEFING] |
| Claude/Gemini APIs sem modelo próprio | Briefing seção 6 (D3) | [BRIEFING] |
| MRR R$ 994 → R$ 31.862 (mês 12) | Bloco #3 seção 4 | [BRIEFING] |
| Time R$ 75K/mês (6 pessoas) | Bloco #4 seção 2 | [BRIEFING] |
| Cache 4 camadas reduz 35-50% LLM calls | Bloco #7 seção 6 (D46) | [INFERENCE] |
| Preços GCP (Cloud Run, BigQuery, etc.) | GCP Pricing públic (abr/2026) | [INFERENCE] |
| Cenários A, B, C, D | Análise de sensibilidade | [INFERENCE] |
| Gatilhos Go/No-Go | Análise de viabilidade | [INFERENCE] |
