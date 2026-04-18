---
title: "Automação de Processos (RPA / Workflow) — Blueprint"
description: "Automação de tarefas repetitivas e fluxos de trabalho de negócio. Pode usar RPA, BPMN, orquestradores de workflow ou scripts agendados com lógica de negócio."
category: project-blueprint
type: process-automation
status: rascunho
created: 2026-04-13
---

# Automação de Processos (RPA / Workflow)

## Descrição

Automação de tarefas repetitivas e fluxos de trabalho de negócio. Pode usar RPA (Robotic Process Automation), engines BPMN, orquestradores de workflow, ou scripts agendados com lógica de negócio. O projeto transforma processos manuais em fluxos automatizados com triggers, condições, ações e tratamento de exceções.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda automação de processos é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — RPA (Robotic Process Automation)

Automação que emula interações humanas com interfaces gráficas de sistemas que não possuem API — cliques, preenchimento de formulários, extração de dados de tela, navegação em menus. Usado quando o sistema-alvo é legado sem integração disponível e não pode ser modificado. O foco é estabilidade dos robôs frente a mudanças na interface dos sistemas (um botão que muda de posição quebra o robô), tratamento de exceções visuais, e monitoramento de execução. Exemplos: preenchimento automático de notas fiscais em sistema legado, extração de relatórios de ERPs sem API, conciliação de dados entre dois sistemas sem integração.

### V2 — Workflow BPMN / Low-Code

Automação construída sobre engine BPMN ou plataforma low-code com designer visual de fluxos. Os processos são modelados como diagramas com etapas, condições, aprovações humanas (human tasks), e integrações via conectores nativos. O foco é a capacidade de modelar processos complexos com ramificações, subprocessos e escalações, mantendo visibilidade e governança para o time de negócio. Exemplos: processo de aprovação de compras com múltiplos níveis, onboarding de funcionários com 15 etapas, gestão de contratos com SLA e escalação.

### V3 — Orquestração de APIs / Event-Driven

Automação que coordena chamadas entre múltiplos sistemas via APIs, mensageria (filas, topics) ou eventos. Não há interação com interface gráfica — tudo é API-to-API. O foco é a confiabilidade da orquestração (idempotência, retry, compensação em caso de falha parcial), o mapeamento de dados entre schemas diferentes, e o monitoramento de cada step da cadeia. Exemplos: sincronização de pedidos entre e-commerce e ERP, pipeline de processamento de dados com múltiplos estágios, orquestração de microservices.

### V4 — Scripts Agendados / ETL

Automação baseada em scripts (Python, Node.js, Shell) executados em schedule (cron), processando dados em batch — extração, transformação e carga (ETL), geração de relatórios, limpeza de dados, ou sincronização periódica entre sistemas. O foco é a robustez do pipeline (tratamento de falhas parciais, idempotência, logging detalhado) e o monitoramento de execuções (alertas quando falha, quando demora demais, ou quando o volume de dados é anômalo). Exemplos: importação diária de dados do CRM para o data warehouse, geração semanal de relatórios PDF, limpeza mensal de registros expirados.

### V5 — Automação de DevOps / Infrastructure

Automação de processos de infraestrutura e operações — provisionamento de ambientes, deploy automatizado, scaling, backup, monitoramento e resposta a incidentes. Usa Infrastructure as Code (Terraform, Pulumi), pipelines CI/CD, e runbooks automatizados. O foco é a idempotência (executar duas vezes produz o mesmo resultado), a segurança (credentials management, least privilege), e a rastreabilidade (quem executou o quê, quando). Exemplos: pipeline de deploy multi-ambiente, provisionamento automatizado de ambientes de teste, auto-scaling baseado em métricas, backup automatizado com verificação de integridade.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Ferramenta Principal | Orquestração | Monitoramento | Hospedagem | Observações |
|---|---|---|---|---|---|
| V1 — RPA | UiPath, Automation Anywhere, Power Automate Desktop | UiPath Orchestrator, Control Room | Dashboard nativo da ferramenta | On-premises ou VM dedicada | RPA cloud ganha tração mas processos legados exigem acesso local à máquina. |
| V2 — Workflow BPMN | Camunda, n8n, Power Automate, Kissflow | Engine BPMN nativa | Cockpit / dashboard BPMN | Cloud ou on-premises | Camunda para cenários enterprise. n8n para times técnicos que querem open-source. |
| V3 — Orquestração APIs | Temporal, Apache Airflow, Step Functions | Temporal Server, Airflow Scheduler | Temporal UI, Airflow UI, CloudWatch | Cloud (AWS, GCP) ou Kubernetes | Temporal para workflows duráveis e complexos. Step Functions para quem já está em AWS. |
| V4 — Scripts/ETL | Python, dbt, Apache Airflow, Prefect | Airflow, Prefect, cron + supervisord | Grafana, Datadog, alertas via Slack | Cloud functions, Kubernetes, ou VM | dbt para transformações SQL. Airflow para pipelines complexos com dependências. |
| V5 — DevOps/Infra | Terraform, GitHub Actions, ArgoCD, Ansible | GitHub Actions, GitLab CI, ArgoCD | Grafana, PagerDuty, Datadog | CI/CD runner (cloud ou self-hosted) | GitOps (ArgoCD) para Kubernetes. Terraform para provisionamento multi-cloud. |

---

## Etapa 01 — Inception

- **Origem da demanda e processo atual**: A demanda de automação quase sempre nasce da dor de um processo manual — alguém gasta horas repetindo uma tarefa que "deveria ser automática". Entender o processo atual em detalhes é pré-requisito antes de qualquer decisão técnica. Quem executa o processo hoje, com que frequência, quanto tempo leva, quais sistemas são usados, e quais erros acontecem. Sem esse entendimento, a automação pode resolver o problema errado — automatizar um processo ineficiente em vez de redesenhá-lo.

- **Volume e frequência do processo**: O volume de execuções (diário, semanal, mensal) e o volume de dados por execução definem diretamente a abordagem técnica. Um processo executado 5 vezes por dia com 10 registros pode ser resolvido com um script simples. O mesmo processo executado 5.000 vezes por dia com 100.000 registros por execução exige orquestração robusta, processamento paralelo, e monitoramento em tempo real. A diferença entre esses cenários é de 10x a 100x em esforço de desenvolvimento — e o cliente frequentemente não sabe o volume real porque nunca mediu.

- **Stakeholders e resistência à mudança**: Automação de processos afeta diretamente as pessoas que executam o processo manual hoje. Essas pessoas podem resistir (medo de perder o emprego, medo de perder controle) ou sabotar (não fornecer informações corretas sobre o processo, reportar falsos problemas). Identificar desde a Inception quem é afetado pela automação e qual a estratégia de change management é tão importante quanto a decisão técnica. Projetos de automação que ignoram o fator humano têm taxa de adoção baixa mesmo quando tecnicamente bem-sucedidos.

- **Processo estável vs. processo em mutação**: Antes de automatizar, verificar se o processo está estável — se as regras, os sistemas envolvidos e os responsáveis não estão em processo de mudança. Automatizar um processo que está sendo redesenhado resulta em retrabalho garantido — a automação é construída para a versão atual do processo, que será descartada em 3 meses. Se o processo está em mudança, o correto é estabilizá-lo primeiro e automatizar depois.

- **Custos visíveis e invisíveis do processo manual**: O business case para automação precisa quantificar o custo do processo manual: horas-pessoa gastas por semana/mês, taxa de erro humano (registros digitados errado, etapas esquecidas), custo de retrabalho quando erros são detectados, e custo de atraso quando o processo depende de uma pessoa específica que está de férias ou doente. Esses custos são frequentemente subestimados porque estão distribuídos — ninguém percebe que 4 pessoas gastando 2h/semana cada é equivalente a 1 FTE por mês.

- **Expectativa de ROI e prazo de payback**: O cliente precisa ter expectativa realista de retorno. Automações simples (script agendado) podem ter payback em semanas. Automações complexas (RPA com múltiplos robôs, orquestração de 10 APIs) podem levar meses para o ROI positivo. Se o custo de desenvolvimento + operação da automação excede a economia gerada, o projeto não faz sentido — e isso precisa ser calculado antes de começar, não depois de entregar.

### Perguntas

1. Qual é o processo manual que será automatizado — quem executa, com que frequência, e quanto tempo leva por execução? [fonte: Área de negócio, Operações] [impacto: PM, Arquiteto]
2. Qual é o volume de execuções por dia/semana/mês e o volume de dados processados por execução? [fonte: Operações, TI] [impacto: Arquiteto, Dev]
3. Quais sistemas são usados no processo atual e eles possuem API ou apenas interface gráfica? [fonte: TI, Operações] [impacto: Arquiteto, Dev]
4. Quais são os erros mais frequentes no processo manual e qual o custo de retrabalho quando ocorrem? [fonte: Operações, Qualidade] [impacto: PM, Arquiteto]
5. O processo está estável (regras, sistemas, responsáveis fixos) ou está em processo de redesenho? [fonte: Processos, Diretoria] [impacto: PM, Arquiteto]
6. Quem são as pessoas diretamente afetadas pela automação e qual a estratégia de change management? [fonte: RH, Diretoria, Operações] [impacto: PM]
7. Existe documentação formal do processo atual (fluxograma, BPMN, SOP) ou o conhecimento é tácito? [fonte: Processos, Operações] [impacto: PM, Dev]
8. Qual é o orçamento disponível para desenvolvimento e para operação mensal recorrente da automação? [fonte: Financeiro, Diretoria] [impacto: PM, Arquiteto]
9. Qual é o prazo esperado para a automação estar em produção e existe data de negócio que justifica? [fonte: Diretoria, Operações] [impacto: PM, Dev]
10. O processo envolve aprovações humanas (human-in-the-loop) ou pode ser totalmente automatizado? [fonte: Operações, Compliance] [impacto: Arquiteto, Dev]
11. Existem requisitos regulatórios que impactam como o processo pode ser automatizado (auditoria, rastreabilidade, LGPD)? [fonte: Compliance, Jurídico] [impacto: Arquiteto, Dev]
12. O cliente já tentou automatizar este processo antes — se sim, o que deu errado? [fonte: TI, Operações] [impacto: PM, Arquiteto]
13. A automação precisa funcionar 24/7 ou apenas em horário comercial? Há janelas de manutenção permitidas? [fonte: Operações, TI] [impacto: Arquiteto, DevOps]
14. Quem será o responsável por monitorar e manter a automação após o go-live? [fonte: TI, Operações, Diretoria] [impacto: PM, DevOps]
15. O ROI estimado (economia de horas-pessoa - custo de dev e operação) foi calculado e justifica o investimento? [fonte: Financeiro, Diretoria] [impacto: PM]

---

## Etapa 02 — Discovery

- **Mapeamento detalhado do processo AS-IS**: Documentar o processo atual passo a passo, com nível de detalhe suficiente para que um desenvolvedor consiga reproduzir cada ação. Para cada step: qual sistema é acessado, qual tela, quais campos são lidos/escritos, quais decisões são tomadas (e com base em quais dados), quais exceções podem ocorrer, e qual a ação corretiva quando ocorrem. Este mapeamento é o artefato mais importante do Discovery — erros aqui se propagam para todo o projeto. Observação direta (sentar ao lado de quem executa o processo) é mais confiável que entrevista (as pessoas omitem steps que fazem no "piloto automático").

- **Identificação de exceções e edge cases**: Todo processo manual tem exceções que quem executa resolve intuitivamente — um campo que vem vazio, um formato inesperado, um sistema que está fora do ar, um caso que não se encaixa na regra padrão. Essas exceções representam a maior fonte de complexidade da automação. O operador humano faz julgamento caso a caso; o robô/script precisa de regra explícita para cada cenário. Levantar exceções exaustivamente é obrigatório — cada exceção não mapeada será um bug em produção.

- **Inventário de sistemas e interfaces**: Mapear todos os sistemas envolvidos no processo com detalhes técnicos: sistema X (versão, acesso via browser/desktop, requer VPN), sistema Y (API REST disponível, autenticação OAuth2), sistema Z (legado mainframe, acesso via terminal emulator, sem API). Para cada sistema, verificar: quem controla as credenciais de acesso, quais são os rate limits ou restrições de uso, e se há janelas de indisponibilidade programada. Sistemas sem API direcionam para RPA; sistemas com API direcionam para orquestração.

- **Requisitos de confiabilidade e tolerância a falhas**: Definir o nível de confiabilidade necessário — qual o impacto se a automação falhar em uma execução? Em processos financeiros (conciliação, pagamento), uma falha pode causar prejuízo direto. Em processos de relatório, uma falha pode ser tolerada até a próxima execução. O nível de confiabilidade define a complexidade do tratamento de erros: retry simples com alerta, retry com backoff e dead letter queue, ou compensação transacional com rollback.

- **Requisitos de rastreabilidade e auditoria**: Verificar se o processo exige trilha de auditoria — quem executou, quando, quais dados foram processados, qual foi o resultado. Processos regulados (financeiros, saúde, governo) geralmente exigem logs detalhados, imutáveis e com retenção definida. Processos internos sem regulação podem ter logging mais simples. O nível de logging impacta a arquitetura (onde armazenar logs, por quanto tempo, com que granularidade) e o custo de operação (armazenamento, queries em logs).

- **Fronteira entre automação e redesenho de processo**: Descobrir durante o mapeamento que o processo manual é ineficiente é comum. A pergunta é: automatizar o processo como está (preservando a ineficiência mas eliminando o esforço manual) ou redesenhar o processo antes de automatizar (mais eficiente mas com escopo maior)? A decisão deve ser consciente — automatizar um processo ruim é rápido mas cria uma "dívida de processo" que será cara de resolver depois. Redesenhar é mais lento mas entrega mais valor. Em ambos os casos, a decisão deve ser documentada.

### Perguntas

1. O processo AS-IS foi mapeado passo a passo com nível de detalhe suficiente para reprodução por desenvolvedor? [fonte: Operações, Processos] [impacto: Dev, Arquiteto]
2. As exceções e edge cases do processo foram levantados exaustivamente (campos vazios, formatos inesperados, sistemas fora do ar)? [fonte: Operações] [impacto: Dev, QA]
3. Todos os sistemas envolvidos foram inventariados com tipo de acesso (API, UI, terminal), versão e credenciais? [fonte: TI, Operações] [impacto: Arquiteto, Dev]
4. Para cada sistema: há API disponível ou apenas interface gráfica? Se API, qual protocolo, autenticação e rate limits? [fonte: TI, Fornecedores] [impacto: Arquiteto, Dev]
5. Qual é o impacto de falha em uma execução — financeiro, operacional, reputacional, regulatório? [fonte: Operações, Compliance, Financeiro] [impacto: Arquiteto, Dev]
6. Existem requisitos de auditoria e rastreabilidade — quem executou, quando, o que foi processado, qual o resultado? [fonte: Compliance, Auditoria] [impacto: Arquiteto, Dev]
7. O processo será automatizado como está ou será redesenhado antes da automação? [fonte: Processos, Diretoria] [impacto: PM, Arquiteto]
8. Quais são os SLAs do processo (tempo máximo de execução, prazo de entrega do resultado, horário de corte)? [fonte: Operações, Área de negócio] [impacto: Arquiteto, Dev]
9. O processo envolve manipulação de dados sensíveis (PII, dados financeiros, dados de saúde)? [fonte: Compliance, DPO] [impacto: Arquiteto, Dev, Segurança]
10. Existem dependências temporais (processo X precisa terminar antes de processo Y, janelas de horário)? [fonte: Operações, TI] [impacto: Arquiteto, Dev]
11. O volume de dados vai crescer ao longo do tempo? Qual a projeção de crescimento em 6-12 meses? [fonte: Operações, Diretoria] [impacto: Arquiteto, Dev]
12. Há processos similares na organização que poderiam usar a mesma automação com configuração diferente? [fonte: Operações, Processos] [impacto: Arquiteto, PM]
13. Quais métricas de sucesso definirão se a automação está entregando valor (tempo economizado, erros reduzidos, throughput)? [fonte: Diretoria, Operações] [impacto: PM, DevOps]
14. Existem integrações com parceiros externos (fornecedores, clientes, órgãos reguladores) com SLAs ou formatos específicos? [fonte: Operações, Comercial] [impacto: Arquiteto, Dev]
15. Os requisitos cabem inteiramente em automação de processo ou há indicação de que deveria ser um sistema/aplicação completa? [fonte: TI, Arquiteto] [impacto: Arquiteto, PM]

---

## Etapa 03 — Alignment

- **Escolha da abordagem técnica**: Alinhar a abordagem com base no inventário do Discovery. Se os sistemas não têm API, RPA é obrigatório. Se todos têm API, orquestração é mais robusta e mais barata que RPA. Se há mix, abordagem híbrida (orquestração para APIs + RPA para sistemas legados). Se o processo é predominantemente transformação de dados, ETL/scripts é suficiente. Se envolve human-in-the-loop com aprovações e escalação, workflow BPMN é o mais adequado. A escolha deve ser justificada com base em critérios técnicos, não em preferência de ferramenta.

- **Definição do processo TO-BE**: Produzir o desenho do processo automatizado — o TO-BE — que pode diferir significativamente do AS-IS. Etapas manuais são substituídas por etapas automatizadas, mas novas etapas podem ser adicionadas (logging, validação de dados de entrada, tratamento de exceções, notificação de resultado). O TO-BE deve ser documentado em formato visual (BPMN, fluxograma) e revisado com os stakeholders de negócio para validar que a automação preserva a lógica de negócio correta — não basta ser tecnicamente funcional se o resultado de negócio está errado.

- **Modelo de operação pós-automação**: Definir quem monitora a automação em produção, quem é notificado quando falha, quem intervém manualmente quando exceção não-automatizada ocorre, e quem decide quando a automação deve ser pausada. A automação não elimina pessoas — realoca. O operador que antes executava o processo manualmente se torna o operador que monitora a automação, trata exceções, e valida resultados. Sem modelo de operação definido, automações em produção falham silenciosamente até que alguém perceba dias depois.

- **Estratégia de tratamento de exceções**: Alinhar explicitamente como cada tipo de exceção será tratada: retry automático (para erros transientes como timeout), retry com backoff (para rate limits), escalação humana (para exceções de negócio que exigem julgamento), skip com logging (para registros inválidos que não devem travar o batch inteiro), e rollback/compensação (para transações parciais que precisam ser revertidas). A ausência de estratégia de exceções resulta em automações que param no primeiro erro e requerem intervenção manual constante — eliminando o benefício da automação.

- **Definição de KPIs de automação**: Alinhar como o sucesso será medido: taxa de execuções sem intervenção humana (automation rate), tempo médio de execução vs. processo manual, taxa de erros vs. taxa de erros manual, volume processado por unidade de tempo (throughput), e tempo de indisponibilidade (downtime). Esses KPIs devem ser mensuráveis — o que significa que a automação precisa gerar dados para alimentar esses indicadores (logs, timestamps, contadores).

### Perguntas

1. A abordagem técnica (RPA, workflow BPMN, orquestração API, scripts/ETL) foi escolhida com justificativa baseada no inventário de sistemas? [fonte: Arquiteto, TI] [impacto: Dev, PM]
2. O processo TO-BE foi desenhado em formato visual (BPMN, fluxograma) e aprovado pelos stakeholders de negócio? [fonte: Processos, Diretoria] [impacto: Dev, PM]
3. O modelo de operação pós-automação está definido (quem monitora, quem trata exceções, quem decide pausar)? [fonte: Operações, TI, Diretoria] [impacto: PM, DevOps]
4. A estratégia de tratamento de exceções está documentada para cada tipo de erro previsível? [fonte: Arquiteto, Operações] [impacto: Dev]
5. Os KPIs de automação foram definidos e são mensuráveis com os dados que a automação produzirá? [fonte: Diretoria, Operações] [impacto: PM, DevOps]
6. O modelo de change management para os operadores afetados pela automação foi definido e comunicado? [fonte: RH, Diretoria] [impacto: PM]
7. As dependências de sistemas externos (disponibilidade, rate limits, janelas de manutenção) foram mapeadas e aceitas? [fonte: TI, Fornecedores] [impacto: Arquiteto, Dev]
8. O SLA da automação foi definido (tempo máximo de execução, tempo máximo de indisponibilidade, tempo de recuperação)? [fonte: Operações, Diretoria] [impacto: Arquiteto, DevOps]
9. O escopo do MVP foi definido — quais cenários (happy path + exceções prioritárias) entram na primeira versão? [fonte: Diretoria, Operações] [impacto: PM, Dev]
10. Os requisitos de segurança (credentials management, acesso a dados sensíveis, audit trail) foram alinhados com Segurança/Compliance? [fonte: Segurança, Compliance] [impacto: Arquiteto, Dev]
11. O custo de operação mensal da automação (infraestrutura, licenças, monitoramento, suporte) foi estimado e aprovado? [fonte: Financeiro, TI] [impacto: PM]
12. A estratégia de rollback (reverter para processo manual) foi documentada para cenário de falha prolongada? [fonte: Operações, TI] [impacto: PM, DevOps]
13. Os ambientes necessários (desenvolvimento, teste, staging, produção) foram definidos e orçados? [fonte: TI, Financeiro] [impacto: Dev, DevOps]
14. O time de desenvolvimento tem experiência na ferramenta/plataforma escolhida ou precisa de capacitação? [fonte: TI, RH] [impacto: PM, Dev]
15. O cliente entende que a automação requer manutenção contínua (ajustes quando sistemas mudam, tratamento de novas exceções)? [fonte: Diretoria] [impacto: PM]

---

## Etapa 04 — Definition

- **Especificação do fluxo automatizado step by step**: Detalhar cada step do processo automatizado TO-BE com precisão técnica: qual sistema é acessado, qual API/endpoint/tela é chamada, quais dados de entrada são necessários, qual operação é realizada (ler, criar, atualizar, deletar), qual dado de saída é produzido, e qual é o próximo step. Para decisões condicionais: qual campo é avaliado, quais são os valores possíveis, e qual caminho corresponde a cada valor. Para loops: qual é o critério de iteração e qual o limite máximo de iterações. Esta especificação é o "código em prosa" — quanto mais precisa, mais rápido o build.

- **Mapeamento de dados entre sistemas**: Definir o mapeamento campo a campo entre os sistemas envolvidos — campo X do sistema A corresponde ao campo Y do sistema B, com transformação Z (formatação de data, conversão de moeda, normalização de texto). Documentar inconsistências entre sistemas: formatos diferentes para o mesmo dado (data DD/MM/YYYY vs. YYYY-MM-DD), unidades diferentes (reais vs. centavos), e codificações diferentes para a mesma entidade (código 001 no sistema A = código ABC no sistema B). Essas inconsistências são a fonte número um de bugs em automações de integração.

- **Especificação de credenciais e acessos**: Para cada sistema que a automação acessa, definir: tipo de credencial (service account, token de API, certificado digital, usuário/senha de aplicação), nível de permissão necessário (somente leitura, leitura/escrita, admin), política de rotação de credenciais, e procedimento de renovação. Credenciais são o maior risco de segurança de automações — service accounts com permissões excessivas, senhas hardcoded em scripts, tokens sem expiração. A especificação deve seguir o princípio de least privilege e definir quem é responsável por manter cada credencial.

- **Especificação de triggers e scheduling**: Definir quando e como cada automação é disparada: por schedule (cron expression específica — "todos os dias úteis às 7h", "primeira segunda-feira do mês"), por evento (novo registro criado, arquivo depositado em SFTP, mensagem em fila), por trigger manual (operador aciona quando necessário), ou por API (sistema externo invoca a automação). Para cada trigger, definir: timezone, tratamento de feriados, comportamento quando o trigger dispara e a execução anterior ainda está em andamento (esperar, pular, executar em paralelo).

- **Especificação de notificações e alertas**: Definir todos os pontos de notificação do fluxo: início de execução (opcional, útil para processos longos), conclusão com sucesso (com resumo de registros processados), falha com erro (com detalhes da exceção e step que falhou), necessidade de intervenção humana (com contexto suficiente para o operador decidir), e SLA em risco (execução demorando mais que o esperado). Para cada notificação: canal (e-mail, Slack, SMS, Teams), destinatários, formato da mensagem, e nível de urgência.

- **Especificação de logging e observabilidade**: Definir o que será registrado em cada execução: timestamp de início e fim de cada step, volume de dados processados por step, erros e exceções com stack trace, dados de entrada e saída resumidos (não dados sensíveis em texto plano), e métricas de performance (latência de cada step, tempo total). Os logs devem ser estruturados (JSON) para facilitar consultas e dashboards. Definir retenção de logs (30 dias? 1 ano? depende de requisitos regulatórios) e onde serão armazenados.

### Perguntas

1. Cada step do fluxo automatizado foi especificado com sistema, API/tela, dados de entrada/saída e operação? [fonte: Arquiteto, Operações] [impacto: Dev]
2. O mapeamento campo a campo entre sistemas foi documentado com transformações e tratamento de inconsistências? [fonte: TI, Operações] [impacto: Dev]
3. As credenciais necessárias para cada sistema foram especificadas com tipo, permissão e responsável por manutenção? [fonte: TI, Segurança] [impacto: Dev, DevOps, Segurança]
4. Os triggers de execução foram definidos com cron expressions, timezones, tratamento de feriados e concorrência? [fonte: Operações, TI] [impacto: Dev, DevOps]
5. As notificações e alertas foram especificados com canal, destinatários, formato e nível de urgência? [fonte: Operações, TI] [impacto: Dev, DevOps]
6. A especificação de logging foi definida com campos, formato (JSON), retenção e local de armazenamento? [fonte: Arquiteto, Compliance] [impacto: Dev, DevOps]
7. Os cenários de exceção foram especificados com ação de tratamento para cada um (retry, skip, escalação, rollback)? [fonte: Operações, Arquiteto] [impacto: Dev]
8. Os critérios de aceitação de cada step foram definidos em formato testável? [fonte: Operações, QA] [impacto: QA, Dev]
9. O volume de dados por execução e a projeção de crescimento foram documentados para dimensionar a infraestrutura? [fonte: Operações, TI] [impacto: Arquiteto, DevOps]
10. As dependências temporais entre automações foram mapeadas (processo X antes de Y, janelas de horário)? [fonte: Operações, TI] [impacto: Dev, DevOps]
11. O tratamento de dados sensíveis foi especificado (masking em logs, encryption at rest, tokenização)? [fonte: Segurança, DPO] [impacto: Dev, DevOps]
12. O plano de rollback para o processo manual foi documentado caso a automação precise ser desativada? [fonte: Operações] [impacto: PM, DevOps]
13. As regras de negócio embutidas no processo foram documentadas isoladamente (não apenas no fluxo) para facilitar manutenção? [fonte: Operações, Área de negócio] [impacto: Dev]
14. Os limites operacionais foram definidos (timeout por step, limite de retries, tamanho máximo de batch)? [fonte: Arquiteto, Operações] [impacto: Dev]
15. A documentação de definição foi revisada e aprovada pelos stakeholders de negócio e pelo time técnico? [fonte: Diretoria, Operações, TI] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Escolha da plataforma de automação**: A seleção da plataforma deve ser baseada nos requisitos do Discovery: se RPA é necessário, UiPath ou Power Automate Desktop são as opções mais maduras (UiPath para volumes altos e orquestração complexa, Power Automate para organizações já no ecossistema Microsoft). Se workflow BPMN é a abordagem, Camunda é a referência enterprise (open-source com suporte comercial) e n8n é a referência para times técnicos que querem flexibilidade. Se orquestração de APIs é o foco, Temporal para workflows duráveis com garantia de execução e Step Functions para quem já está em AWS. A escolha impacta o perfil do time, o custo de licença e a complexidade de operação.

- **Arquitetura de resiliência**: A automação deve ser projetada para falhar graciosamente — porque vai falhar. A arquitetura de resiliência inclui: idempotência (executar a mesma operação duas vezes produz o mesmo resultado — crítico para retries), compensação (se o step 5 falha, os steps 1-4 precisam ser revertidos?), dead letter queue (mensagens/registros que falharam após todos os retries são armazenados para análise manual), e circuit breaker (se um sistema externo está fora do ar, parar de tentar até que volte). Automações sem resiliência são bomba-relógio — funcionam por semanas e explodem no primeiro incidente do sistema externo.

- **Estratégia de secrets management**: Credenciais usadas por automações precisam de gerenciamento centralizado — nunca em variáveis de ambiente em texto plano, nunca em código, nunca em arquivos de configuração commitados. Soluções adequadas: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, ou o secrets manager nativo da plataforma de automação (UiPath Credential Store, Camunda secrets). A estratégia deve cobrir: rotação automática de credenciais, audit trail de quem acessou qual segredo, e alertas de expiração de certificados/tokens.

- **Estratégia de monitoramento e observabilidade**: Definir a stack de monitoramento: onde os logs serão centralizados (ELK, Grafana Loki, CloudWatch Logs, Datadog), como as métricas serão coletadas (Prometheus, StatsD, CloudWatch Metrics), como os alertas serão configurados (PagerDuty, OpsGenie, Slack webhooks), e quais dashboards serão criados para operação diária. O monitoramento deve cobrir três dimensões: saúde da infraestrutura (CPU, memória, disco), saúde da automação (execuções com sucesso vs. falha, tempo de execução, throughput), e saúde do negócio (registros processados por dia, taxa de exceções, SLA cumprido).

- **Estratégia de escalabilidade**: Projetar a automação para o volume atual com capacidade de escalar. Se o volume dobrar em 6 meses (o que é comum em automações bem-sucedidas que são estendidas para novos cenários), a arquitetura suporta sem refatoração? Horizontal scaling (mais workers/robôs em paralelo) é preferível a vertical scaling (máquina mais potente) por ser mais resiliente e mais elástico. Para RPA, escalar significa mais licenças de robôs (custo). Para scripts, escalar pode significar containerização com Kubernetes (complexidade).

- **Estratégia de versionamento e deploy**: Definir como a automação é versionada (Git para código e configuração, versionamento de pacotes para RPA), como é feito o deploy entre ambientes (promoção de dev → teste → produção), e como é feito o rollback (reverter para versão anterior da automação). O pipeline de CI/CD para automações deve incluir: lint, execução de testes automatizados em ambiente de teste, validação de credenciais e conectividade com sistemas-alvo, e deploy automatizado com aprovação manual para produção.

### Perguntas

1. A plataforma de automação foi escolhida com base nos requisitos técnicos (API vs. UI, volume, complexidade) e não por preferência? [fonte: Arquiteto, TI] [impacto: Dev]
2. A arquitetura de resiliência inclui idempotência, compensação, dead letter queue e circuit breaker? [fonte: Arquiteto] [impacto: Dev]
3. A estratégia de secrets management usa ferramenta centralizada com rotação automática e audit trail? [fonte: Arquiteto, Segurança] [impacto: Dev, DevOps, Segurança]
4. A stack de monitoramento cobre infraestrutura, automação e métricas de negócio com alertas configurados? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
5. A arquitetura suporta escalabilidade horizontal para acomodar crescimento de volume sem refatoração? [fonte: Arquiteto] [impacto: Dev, DevOps]
6. O pipeline de CI/CD para automação inclui lint, testes, validação de conectividade e deploy com aprovação? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
7. A estratégia de processamento (síncrono vs. assíncrono, serial vs. paralelo) foi definida com base no volume e SLA? [fonte: Arquiteto] [impacto: Dev]
8. A arquitetura isola regras de negócio do código de orquestração para facilitar manutenção por pessoas diferentes? [fonte: Arquiteto] [impacto: Dev]
9. O armazenamento de dados intermediários (staging area) foi definido com política de retenção e limpeza? [fonte: Arquiteto, TI] [impacto: Dev, DevOps]
10. A estratégia de retry inclui backoff exponencial, limite máximo de tentativas e dead letter para falhas permanentes? [fonte: Arquiteto] [impacto: Dev]
11. Os custos mensais de operação (infraestrutura, licenças, monitoramento) foram calculados em cenário esperado e pior caso? [fonte: Financeiro, TI] [impacto: PM]
12. A arquitetura foi validada contra os rate limits e políticas de uso dos sistemas externos integrados? [fonte: TI, Fornecedores] [impacto: Dev, Arquiteto]
13. A estratégia de data masking/tokenização para dados sensíveis em logs e staging foi definida? [fonte: Segurança, DPO] [impacto: Dev, Segurança]
14. Existe plano de contingência para indisponibilidade prolongada de sistemas externos críticos? [fonte: TI, Operações] [impacto: Arquiteto, DevOps]
15. O modelo de ambientes (dev, teste, staging, produção) e a estratégia de deploy entre eles foi documentada e aprovada? [fonte: Arquiteto, TI] [impacto: Dev, DevOps, PM]

---

## Etapa 06 — Setup

- **Provisionamento de infraestrutura**: Configurar os ambientes conforme a arquitetura definida. Para RPA: instalar o orquestrador (UiPath Orchestrator) e provisionar as máquinas dos robôs (VMs com acesso aos sistemas-alvo, resolução de tela definida, sem protetor de tela). Para workflows BPMN: provisionar o engine (Camunda, n8n) com banco de dados e workers. Para orquestração: provisionar o servidor de orquestração (Temporal Server, Airflow) com workers e storage. Para scripts: configurar o ambiente de execução (containers, cron, scheduler). A infraestrutura de automação é frequentemente subestimada — não é "só um script", é infraestrutura que precisa rodar 24/7 com confiabilidade.

- **Configuração de secrets e credenciais**: Cadastrar todas as credenciais no secrets manager escolhido — service accounts para cada sistema integrado, tokens de API, certificados digitais, credenciais de banco de dados. Verificar que cada credencial funciona: testar acesso a cada sistema usando as credenciais configuradas, verificar permissões (a service account tem acesso ao que precisa — nem mais, nem menos), e documentar a data de expiração de cada credencial com alerta de renovação configurado.

- **Configuração do pipeline de CI/CD**: Montar o pipeline de deploy automatizado adaptado ao tipo de automação. Para RPA: versionamento do projeto no repositório, build do pacote, deploy no orquestrador via API. Para workflows: deploy do modelo BPMN no engine, deploy de código de workers. Para scripts: build de container (Dockerfile), push para registry, deploy no ambiente de execução. O pipeline deve incluir testes automatizados — testes que executam a automação em ambiente de teste com dados controlados e verificam o resultado esperado.

- **Configuração de monitoramento e alertas**: Implementar o monitoramento definido na Etapa 05: instalar agentes de coleta de métricas, configurar dashboards, criar alertas para os cenários definidos (falha de execução, SLA em risco, sistema externo indisponível, credencial expirando). Testar cada alerta: provocar a condição e verificar que a notificação chega no canal correto com informação suficiente para diagnóstico. Alertas que nunca foram testados são alertas que podem não funcionar quando necessário.

- **Dados de teste e ambiente de teste**: Criar ou provisionar dados de teste que representam os cenários reais — happy path, exceções mapeadas, e dados inválidos. Para automações que processam dados de produção, criar uma cópia sanitizada (sem PII) no ambiente de teste. Para RPA: configurar o ambiente de teste com as mesmas aplicações e versões do ambiente de produção (incluindo resolução de tela, que afeta posicionamento de elementos). Automações testadas em ambiente diferente do de produção produzem falsa confiança.

- **Documentação operacional**: Criar o runbook operacional antes do build, não depois. O runbook deve cobrir: como iniciar/parar a automação manualmente, como verificar o status de uma execução, como diagnosticar uma falha (onde estão os logs, como interpretar), como reprocessar registros que falharam, como acionar o rollback para processo manual, e contatos de suporte por sistema integrado. O runbook é o artefato que permite que o time de operação mantenha a automação sem depender do time de desenvolvimento.

### Perguntas

1. A infraestrutura foi provisionada conforme a arquitetura (orquestrador, workers, storage, banco de dados)? [fonte: DevOps, TI] [impacto: Dev, DevOps]
2. Todas as credenciais foram cadastradas no secrets manager e testadas com acesso real a cada sistema? [fonte: DevOps, Segurança] [impacto: Dev, DevOps]
3. O pipeline de CI/CD para automação está configurado com build, testes automatizados e deploy? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
4. Os dashboards de monitoramento foram criados e todos os alertas foram testados (provocando a condição real)? [fonte: DevOps] [impacto: DevOps, Dev]
5. Os dados de teste foram criados e cobrem happy path, exceções mapeadas e dados inválidos? [fonte: QA, Dev] [impacto: QA, Dev]
6. O runbook operacional foi criado com procedimentos para iniciar, parar, diagnosticar e reprocessar? [fonte: Dev, DevOps] [impacto: DevOps, Operações]
7. O ambiente de teste replica fielmente o ambiente de produção (versões de sistemas, resolução de tela para RPA)? [fonte: TI, DevOps] [impacto: Dev, QA]
8. As permissões de rede (firewall, VPN, whitelist de IPs) foram configuradas para que a automação acesse todos os sistemas? [fonte: TI, Segurança] [impacto: DevOps, Dev]
9. O scheduler/cron/trigger de execução foi configurado e testado no ambiente de teste? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
10. O processo de onboarding de novos desenvolvedores foi documentado com instruções de setup do ambiente? [fonte: Dev] [impacto: Dev]
11. O .gitignore e as políticas de repositório excluem credenciais, logs e dados de teste do versionamento? [fonte: Dev] [impacto: Dev, Segurança]
12. Os ambientes de teste e produção estão isolados (credenciais diferentes, dados diferentes, sistemas-alvo diferentes)? [fonte: DevOps, Segurança] [impacto: Dev, DevOps]
13. As dependências externas (bibliotecas, pacotes, imagens de container) foram versionadas e fixadas (pinned)? [fonte: Dev] [impacto: Dev, DevOps]
14. O alerta de expiração de credenciais está configurado com antecedência suficiente para renovação? [fonte: DevOps, Segurança] [impacto: DevOps]
15. O fluxo completo de commit → build → teste → deploy foi validado end-to-end no ambiente de teste? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Implementação step by step com testes**: Implementar cada step do fluxo automatizado seguindo a especificação da Etapa 04, com teste automatizado para cada step isoladamente antes de integrar no fluxo completo. Cada step deve ser implementado como unidade independente que recebe dados de entrada, executa a operação, e retorna dados de saída ou erro tipado. A implementação step by step com testes permite identificar problemas de integração com cada sistema individualmente — não na primeira execução do fluxo completo quando todos os problemas aparecem juntos.

- **Tratamento de exceções robusto**: Implementar o tratamento de exceções conforme a estratégia definida na Etapa 03. Cada step deve ter: try/catch com captura de exceções específicas (não genéricas), retry configurável com backoff para erros transientes, logging detalhado do contexto quando exceção ocorre (dados de entrada, step, timestamp, ID da execução), e escalação para dead letter ou alerta humano quando retries se esgotam. O tratamento de exceções geralmente representa 40-60% do código total de uma automação robusta — se o tratamento de exceções é só um catch genérico que loga e para, a automação não está pronta para produção.

- **Implementação de idempotência**: Garantir que cada step pode ser executado múltiplas vezes sem efeito colateral indesejado. Se o step cria um registro, verificar se o registro já existe antes de criar novamente (usando ID único de negócio, não timestamp). Se o step envia e-mail, garantir que o reenvio em retry não gera e-mail duplicado para o destinatário. Idempotência é o que permite retry seguro — sem ela, cada retry é uma aposta.

- **Mapeamento e transformação de dados**: Implementar as transformações de dados definidas na Etapa 04 com validação rigorosa de entrada e saída. Cada transformação deve: validar que o dado de entrada está no formato esperado antes de transformar (não assumir), tratar valores nulos ou vazios explicitamente, logar a transformação quando os valores forem críticos para auditoria, e falhar com mensagem clara quando o dado não pode ser transformado (não silenciosamente converter para valor errado).

- **Implementação de logging estruturado**: Implementar logging em formato estruturado (JSON) conforme a especificação da Etapa 04. Cada log entry deve conter: execution_id (ID único da execução para correlacionar todos os logs de uma execução), step (nome do step que gerou o log), timestamp (ISO 8601 com timezone), level (info, warn, error), message (descrição humana), e data (dados contextuais em campos estruturados). Logs não estruturados (string concatenada) são impossíveis de consultar em volume — investir em logging estruturado desde o primeiro step é obrigatório.

- **Testes de integração com sistemas reais**: Após implementar e testar cada step isoladamente, executar o fluxo completo no ambiente de teste com conexão real aos sistemas-alvo (ambiente de teste dos sistemas, não produção). Este teste revela problemas que testes unitários com mocks não capturam: latência real de API, formatos de dados que diferem da documentação, rate limits que disparam sob volume, e timezones que afetam dados de forma inesperada. Executar o fluxo completo ao menos 3 vezes: uma com dados do happy path, uma com exceção conhecida, e uma com volume próximo ao de produção.

### Perguntas

1. Cada step do fluxo foi implementado como unidade independente com teste automatizado isolado? [fonte: Dev] [impacto: Dev, QA]
2. O tratamento de exceções cobre retry com backoff, dead letter, escalação humana e logging contextual? [fonte: Dev, Arquiteto] [impacto: Dev]
3. A idempotência foi implementada em cada step que cria ou modifica dados? [fonte: Dev] [impacto: Dev, QA]
4. As transformações de dados validam entrada antes de transformar e falham com mensagem clara em dados inválidos? [fonte: Dev] [impacto: Dev, QA]
5. O logging está em formato estruturado (JSON) com execution_id, step, timestamp, level e data contextual? [fonte: Dev] [impacto: Dev, DevOps]
6. O fluxo completo foi testado com conexão real aos sistemas de teste (não apenas com mocks)? [fonte: Dev, QA] [impacto: Dev, QA]
7. O fluxo foi testado com volume próximo ao de produção para identificar problemas de performance e rate limits? [fonte: Dev, QA] [impacto: Dev, QA]
8. Os cenários de exceção mapeados na Etapa 02 foram reproduzidos e o tratamento validado? [fonte: QA, Dev] [impacto: Dev, QA]
9. As notificações (sucesso, falha, SLA em risco) estão implementadas e entregam no canal correto com informação útil? [fonte: Dev, Operações] [impacto: Dev, DevOps]
10. As regras de negócio estão isoladas em módulos configuráveis (não hardcoded no código de orquestração)? [fonte: Dev, Arquiteto] [impacto: Dev]
11. O circuit breaker para sistemas externos está implementado e testado (simular indisponibilidade)? [fonte: Dev] [impacto: Dev]
12. O mecanismo de reprocessamento de registros falhados está implementado (dead letter → retry manual ou automático)? [fonte: Dev] [impacto: Dev, DevOps]
13. O scheduling (cron, event trigger) foi testado com verificação de timezone, feriados e concorrência? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
14. A documentação inline do código explica o "porquê" das decisões (especialmente tratamento de exceções e edge cases)? [fonte: Dev] [impacto: Dev]
15. O progresso do build está sendo comunicado com demos regulares para os stakeholders? [fonte: PM, Operações] [impacto: PM, Dev]

---

## Etapa 08 — QA

- **Testes end-to-end com dados representativos**: Executar o fluxo completo em ambiente de teste com dados que representam a realidade de produção — volume, variedade de formatos, e presença de exceções. Não testar apenas o happy path: incluir registros com dados inválidos, registros duplicados, registros com campos nulos, e registros que devem ser rejeitados. O objetivo não é verificar que a automação funciona com dados perfeitos (isso os testes unitários já cobrem), mas verificar que ela se comporta corretamente com dados imperfeitos (que é o que encontrará em produção).

- **Testes de falha e recuperação**: Simular falhas de cada componente da cadeia e verificar o comportamento: sistema externo retorna erro 500, API timeout após 30 segundos, serviço de mensageria indisponível, banco de dados com disco cheio, e credencial expirada durante a execução. Para cada cenário: a automação falhou graciosamente (não perdeu dados), o alerta foi disparado corretamente, o log registrou informação suficiente para diagnóstico, e o reprocessamento funciona quando o sistema volta. Esses testes são frequentemente negligenciados e representam a maior fonte de incidentes em produção.

- **Testes de performance e volume**: Executar a automação com o volume máximo esperado em produção e medir: tempo total de execução (cabe dentro da janela definida no SLA?), consumo de recursos (CPU, memória, disco, rede), comportamento sob rate limits (a automação respeita e faz backoff?), e impacto nos sistemas integrados (a automação não degrada a performance do ERP para outros usuários?). Se a automação processa dados em batch, testar com o dobro do volume esperado para ter margem de crescimento.

- **Testes de concorrência**: Se a automação pode ser executada em paralelo (múltiplos workers, múltiplas instâncias), testar cenários de concorrência: dois workers processando o mesmo registro (idempotência deve garantir resultado correto), execuções sobrepostas (novo trigger enquanto a anterior ainda roda), e contenção de recursos (workers competindo por acesso ao banco ou API). Deadlocks e racing conditions são os bugs mais difíceis de diagnosticar em produção — melhor encontrá-los no QA.

- **Validação do monitoramento e alertas em cenário real**: Executar a automação no ambiente de teste e verificar que todos os dashboards, logs e alertas funcionam como esperado: dashboard mostra execuções em andamento, métricas de throughput estão corretas, alertas de falha disparam no canal certo, e o operador consegue usar o runbook para diagnosticar um problema simulado. O monitoramento que nunca foi testado com execução real frequentemente tem gaps — campos de log faltando, alertas com threshold errado, ou dashboard que não atualiza.

- **User Acceptance Testing com operadores**: Colocar a automação nas mãos dos operadores que vão monitorá-la em produção. Eles devem executar os cenários do runbook: iniciar uma execução manual, acompanhar pelo dashboard, diagnosticar uma falha simulada, reprocessar registros falhados, e parar a automação em caso de emergência. O UAT do operador é diferente do UAT de negócio — o foco é operabilidade, não funcionalidade. Se o operador não consegue diagnosticar um problema em 5 minutos usando o runbook e os logs, a automação não está pronta para produção.

### Perguntas

1. Os testes end-to-end foram executados com dados representativos de produção (volume, variedade, exceções)? [fonte: QA, Operações] [impacto: QA, Dev]
2. As falhas de cada componente externo foram simuladas e o comportamento de recuperação validado? [fonte: QA, Dev] [impacto: Dev]
3. Os testes de performance foram executados com volume máximo esperado e o SLA de tempo foi atendido? [fonte: QA, Dev] [impacto: Dev, Arquiteto]
4. Os testes de concorrência (execuções paralelas, workers concorrentes) foram executados sem deadlocks ou duplicações? [fonte: QA, Dev] [impacto: Dev]
5. Os dashboards, logs e alertas foram validados com execução real e confirmados funcionais? [fonte: QA, DevOps] [impacto: DevOps]
6. Os operadores executaram o UAT usando o runbook e conseguiram diagnosticar problemas simulados? [fonte: Operações, QA] [impacto: DevOps, Operações]
7. A automação foi testada com dados inválidos, duplicados e nulos para verificar tratamento correto? [fonte: QA] [impacto: Dev, QA]
8. O mecanismo de retry e dead letter foi testado end-to-end com reprocessamento bem-sucedido? [fonte: QA, Dev] [impacto: Dev]
9. O impacto da automação nos sistemas integrados foi medido (a automação não degrada performance para outros usuários)? [fonte: QA, TI] [impacto: Dev, Arquiteto]
10. A automação respeita rate limits dos sistemas externos e faz backoff corretamente quando atingidos? [fonte: QA, Dev] [impacto: Dev]
11. O teste de credencial expirada foi executado — a automação falha com mensagem clara e alerta, não silenciosamente? [fonte: QA, DevOps] [impacto: Dev, DevOps]
12. O scheduling foi testado em cenários reais (virada de mês, feriado, horário de verão, execução concorrente)? [fonte: QA, Dev] [impacto: Dev, DevOps]
13. Os KPIs de automação definidos na Etapa 03 estão sendo calculados corretamente pelos dashboards? [fonte: QA, DevOps] [impacto: DevOps, PM]
14. Os critérios de aceitação de negócio foram validados — o resultado da automação é equivalente ou melhor que o processo manual? [fonte: Operações, QA] [impacto: PM, Operações]
15. Todos os bugs encontrados foram classificados, os críticos corrigidos e re-testados? [fonte: QA, PM] [impacto: Dev, PM]

---

## Etapa 09 — Launch Prep

- **Execução paralela (shadow mode)**: Antes de substituir o processo manual, executar a automação em paralelo — o processo manual continua rodando normalmente enquanto a automação processa os mesmos dados em shadow mode. Os resultados são comparados: a automação produziu o mesmo resultado que o processo manual? Onde divergiu? A divergência é um bug da automação ou um erro no processo manual? O shadow mode é a validação mais confiável possível — dados reais, volume real, sistemas reais, sem risco (porque o processo manual continua sendo o oficial). Duração recomendada: 1-2 semanas para processos diários, 1-2 ciclos completos para processos mensais.

- **Plano de cutover**: Documentar a sequência exata para a transição do processo manual para o automatizado: quem desativa o processo manual, quem ativa a automação em modo produção, quem verifica a primeira execução, quais são os critérios de sucesso da primeira execução, e quem autoriza manter a automação ativa. O cutover deve ter horário definido, responsáveis designados, e checklist de verificação. Se a automação falhar na primeira execução em produção, quem executa o processo manual como fallback?

- **Plano de rollback para processo manual**: Documentar como reverter para o processo manual se a automação apresentar problemas persistentes. Isso inclui: quem são as pessoas que sabem executar o processo manual (se foram realocadas, como acionar), quais acessos aos sistemas elas precisam (se foram revogados, como restaurar), e qual o tempo necessário para reativar o processo manual (se for instantâneo ou levar horas). O plano de rollback tem prazo de validade — depois de 6 meses com automação funcionando, as pessoas que executavam o processo manual podem ter saído da empresa ou esquecido os detalhes.

- **Treinamento de operadores**: Realizar treinamento prático com os operadores que monitorarão a automação em produção. O treinamento deve cobrir: como interpretar o dashboard de monitoramento, como identificar uma execução com problema, como usar o runbook para diagnosticar, como reprocessar registros falhados, como parar a automação em emergência, e quem escalar quando o problema está fora do seu alcance. Usar cenários reais do shadow mode para o treinamento — não cenários fictícios.

- **Comunicação para stakeholders e áreas afetadas**: Comunicar a todos os afetados: quem preenchia os dados manualmente e não vai mais precisar, quem recebia o resultado e agora vai receber de forma automática (formato pode mudar), quem dependia do processo e vai ter SLA diferente, e gestores que precisam saber que o processo mudou para ajustar expectativas e cobranças. Comunicação pobre gera confusão, resistência e percepção de que "a automação deu problema" quando na verdade o processo mudou e ninguém foi avisado.

- **Verificação de credenciais e acessos em produção**: Verificar que todas as credenciais de produção estão configuradas, ativas e com permissões corretas. Credenciais de produção são diferentes das de teste — e é surpreendentemente comum descobrir no dia do go-live que a service account de produção não tem permissão para escrever no sistema-alvo, ou que o certificado digital de produção expirou na semana passada. Teste de conectividade com cada sistema em produção é obrigatório antes do go-live.

### Perguntas

1. O shadow mode foi executado por período suficiente e os resultados comparados com o processo manual? [fonte: Operações, QA] [impacto: PM, Dev]
2. O plano de cutover está documentado com sequência exata, responsáveis, horário e critérios de sucesso? [fonte: PM, Operações, Dev] [impacto: PM, Dev, DevOps]
3. O plano de rollback para processo manual está documentado com pessoas, acessos e tempo de reativação? [fonte: Operações, PM] [impacto: PM, Operações]
4. O treinamento de operadores foi realizado com cenários reais do shadow mode e material de referência entregue? [fonte: PM, DevOps] [impacto: Operações, DevOps]
5. A comunicação para todos os stakeholders e áreas afetadas foi enviada com antecedência? [fonte: PM, Change Management] [impacto: PM]
6. Todas as credenciais de produção foram verificadas e testadas com acesso real a cada sistema? [fonte: DevOps, Segurança] [impacto: DevOps, Dev]
7. O monitoramento e alertas em produção foram configurados e testados (provocando alerta real)? [fonte: DevOps] [impacto: DevOps]
8. O runbook operacional foi revisado e validado pelo time de operações que vai usá-lo em produção? [fonte: Operações, DevOps] [impacto: Operações]
9. A janela de cutover foi escolhida em horário de baixo volume com time de suporte disponível? [fonte: Operações, TI] [impacto: PM, DevOps]
10. O processo manual continua funcional e executável como fallback durante as primeiras semanas? [fonte: Operações] [impacto: PM, Operações]
11. As licenças e custos recorrentes de produção (infraestrutura, ferramenta de automação, monitoramento) estão ativos? [fonte: Financeiro, TI] [impacto: PM]
12. O backup da configuração da automação (código, credenciais, scheduling, alertas) foi realizado? [fonte: DevOps] [impacto: DevOps]
13. Os resultados do shadow mode foram apresentados e aprovados pelos stakeholders de negócio? [fonte: Operações, Diretoria] [impacto: PM]
14. O time de suporte/helpdesk sabe da mudança e tem procedimento para escalar problemas relacionados à automação? [fonte: Suporte, PM] [impacto: Suporte, PM]
15. Todos os stakeholders foram notificados sobre data, horário e impactos do cutover? [fonte: Diretoria, PM] [impacto: PM]

---

## Etapa 10 — Go-Live

- **Execução do cutover conforme plano**: Executar o cutover seguindo exatamente o plano documentado — desativar o processo manual (ou colocá-lo em standby), ativar a automação em modo produção, e monitorar a primeira execução completa em tempo real. A equipe técnica e o operador devem estar disponíveis simultaneamente durante a primeira execução. Qualquer desvio do plano deve ser comunicado e avaliado antes de prosseguir. Se a primeira execução falhar, acionar o fallback para processo manual conforme o plano de rollback — não improvisar correções em produção sob pressão.

- **Monitoramento intensivo da primeira semana**: A primeira semana é crítica. Monitorar: taxa de execuções com sucesso vs. falha (target: >99% para processos críticos), tempo de execução por step (identificar steps que estão mais lentos que o esperado), volume de exceções escaladas para intervenção humana (deve diminuir ao longo da semana à medida que edge cases são tratados), consumo de recursos (CPU, memória, disco — verificar se há tendência de crescimento que indica leak), e feedback dos operadores (dificuldades de monitoramento, runbook incompleto, alertas excessivos ou insuficientes).

- **Ajustes e tuning pós-lançamento**: As primeiras execuções em produção sempre revelam ajustes necessários — thresholds de timeout que precisam ser aumentados, rate limits que são mais restritivos do que o documentado, exceções não mapeadas que aparecem com dados reais, e alertas que disparam demais (false positives) ou de menos (false negatives). Esses ajustes devem ser tratados como parte do go-live, não como bugs — são refinamentos esperados que só podem ser feitos com dados e condições reais.

- **Coleta de métricas de baseline**: Registrar as métricas da primeira semana como baseline para comparação futura: tempo médio de execução, volume processado, taxa de erro, taxa de intervenção humana, e economia de horas-pessoa em relação ao processo manual. Essas métricas são a base para calcular o ROI real da automação e para identificar degradação de performance ao longo do tempo. Sem baseline, não é possível provar que a automação está entregando valor nem identificar quando ela começa a degradar.

- **Entrega e handoff formal**: Entregar formalmente ao cliente: código-fonte e configuração no repositório, documentação técnica (arquitetura, fluxo, integrações, secrets), runbook operacional, material de treinamento, dashboards de monitoramento, e todos os acessos (repositório, infraestrutura, monitoramento, secrets manager). A transferência de conhecimento deve incluir sessão prática com o time de operação cobrindo cenários de manutenção: como ajustar um threshold, como adicionar uma nova exceção, e como investigar uma falha usando logs e dashboard.

- **Aceite formal e encerramento**: Obter aceite formal do cliente baseado nos critérios de aceitação e nos resultados do shadow mode e da primeira semana de produção. Documentar o backlog de ajustes pendentes (melhorias, novas exceções a tratar, cenários a cobrir) em backlog formal entregue ao cliente. Definir o modelo de suporte pós-projeto: contrato de manutenção, SLA de atendimento, canal de comunicação, e escopo de o que está coberto vs. o que é escopo de novo projeto.

### Perguntas

1. O cutover foi executado conforme o plano documentado, sem improvisos? [fonte: Dev, Operações] [impacto: Dev, DevOps]
2. A primeira execução em produção foi monitorada em tempo real pela equipe técnica e pelo operador? [fonte: Dev, Operações] [impacto: Dev, DevOps]
3. A taxa de execuções com sucesso na primeira semana está dentro do target definido (>99% para processos críticos)? [fonte: DevOps, Operações] [impacto: Dev, PM]
4. Os ajustes pós-lançamento (timeouts, thresholds, novas exceções) foram implementados e deployados? [fonte: Dev] [impacto: Dev]
5. As métricas de baseline foram registradas (tempo de execução, volume, taxa de erro, economia de horas-pessoa)? [fonte: DevOps, PM] [impacto: PM]
6. O processo manual continua funcional como fallback durante as primeiras semanas pós-go-live? [fonte: Operações] [impacto: PM, Operações]
7. Os dashboards de monitoramento estão operacionais e o time de operação os consulta diariamente? [fonte: DevOps, Operações] [impacto: DevOps, Operações]
8. Os alertas estão calibrados — sem excesso de false positives nem ausência de alertas em falhas reais? [fonte: DevOps] [impacto: DevOps, Dev]
9. O ROI real (economia medida vs. custo de dev + operação) foi calculado e apresentado aos stakeholders? [fonte: PM, Financeiro] [impacto: PM]
10. Todos os acessos foram entregues formalmente e cada responsável confirmou que consegue acessar? [fonte: Dev, DevOps] [impacto: PM]
11. A documentação técnica e o runbook operacional foram entregues ao time de operação? [fonte: Dev, PM] [impacto: Operações, PM]
12. O aceite formal foi obtido com base nos critérios de aceitação e nos resultados da primeira semana? [fonte: Diretoria, Operações] [impacto: PM]
13. O backlog de ajustes pendentes foi documentado e entregue ao cliente com priorização? [fonte: PM, Dev] [impacto: PM]
14. O modelo de suporte pós-projeto foi formalizado (contrato, SLA, canal, escopo)? [fonte: Diretoria, PM] [impacto: PM]
15. A automação foi confirmada como estável e o time de operação opera de forma independente sem suporte do dev? [fonte: Operações, PM] [impacto: PM, Dev]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Queremos automatizar tudo"** — Escopo ilimitado. Automação "de tudo" não é um projeto — é um programa multi-ano. Cada processo precisa ser avaliado individualmente por ROI, complexidade e estabilidade. Começar pelo processo com maior ROI e menor complexidade, não por "tudo".
- **"O processo é simples, é só copiar e colar entre sistemas"** — Copiar e colar entre sistemas é a descrição simplificada de um processo que tem exceções, validações, decisões condicionais e tratamento de erros. A simplificação excessiva gera estimativas irrealistas. Mapear o processo em detalhe antes de aceitar a descrição do cliente.
- **"Não precisamos de ROI, a diretoria já aprovou"** — Projeto sem ROI quantificado não tem critério de sucesso mensurável. Mesmo com aprovação da diretoria, sem métricas claras o projeto será considerado "caro" no primeiro problema e sem defesa para justificar o investimento.

### Etapa 02 — Discovery

- **"O processo está documentado no manual"** — Manuais de processo descrevem o happy path. Exceções, workarounds e edge cases vivem na cabeça de quem executa o processo diariamente. Observação direta (sentar ao lado do operador) é obrigatória — o manual é ponto de partida, não fonte da verdade.
- **"São só 5 etapas"** — Cinco etapas no nível macro se desdobram em 50 steps no nível de detalhe que a automação precisa. Cada "copiar de A para B" envolve: abrir sistema A, autenticar, navegar, buscar, selecionar, copiar, abrir sistema B, autenticar, navegar, colar, validar, salvar. A complexidade está nos detalhes.
- **"Os sistemas nunca ficam fora do ar"** — Todo sistema fica fora do ar. A pergunta não é "se", é "quando e por quanto tempo". Automação que não trata indisponibilidade de sistemas externos não é automação — é script que funciona quando tudo está perfeito.

### Etapa 03 — Alignment

- **"Vamos usar RPA para tudo"** — RPA é a abordagem mais frágil (depende de posição de pixels na tela) e mais cara (licenças de robôs por máquina). Se o sistema tem API, orquestração via API é mais robusta, mais barata e mais rápida. RPA é último recurso para sistemas sem API, não primeira escolha.
- **"Não precisamos de monitoramento, se falhar a gente vê"** — "A gente vê" significa "a gente descobre quando o resultado não aparece e alguém reclama". Sem monitoramento proativo, falhas de automação são detectadas com atraso de horas ou dias — quando o dano já está feito.
- **"O operador atual monitora a automação no tempo livre"** — Monitorar automação não é tarefa secundária. Se o operador está fazendo outras coisas e a automação falha às 3h da manhã, quem vê? Modelo de operação precisa ter responsável dedicado ou alertas automáticos que acionam independente de quem está olhando.

### Etapa 04 — Definition

- **"Os dados entre os sistemas são iguais"** — Raramente são. Mesmo campos com o mesmo nome têm formatos diferentes (data, moeda, encoding), valores diferentes para a mesma entidade (códigos internos), e regras de validação diferentes. O mapeamento detalhado campo a campo sempre revela inconsistências que precisam de tratamento explícito.
- **"Não precisa de logging detalhado, é processo simples"** — Processo "simples" que falha em produção sem logging vira investigação de dias. Quando funciona, ninguém lê os logs. Quando falha, logs são a única forma de diagnóstico. O custo de logging é mínimo comparado ao custo de investigação sem logs.
- **"O schedule é só um cron, não precisa especificar"** — Cron expressions sem definição de timezone, tratamento de feriados, e comportamento de concorrência (nova execução enquanto a anterior roda) geram bugs sutis que aparecem uma vez por mês ou por ano — os mais difíceis de diagnosticar.

### Etapa 05 — Architecture

- **"Um script Python em cron resolve"** — Para automações simples, talvez. Mas script sem retry, sem logging estruturado, sem monitoramento e sem alertas é a versão mais primitiva de automação — funciona até a primeira falha, e depois ninguém sabe o que aconteceu. A sofisticação da arquitetura deve ser proporcional ao impacto da falha.
- **"Vamos usar Kubernetes para um robô"** — Over-engineering na direção oposta. Um robô RPA que roda uma vez por dia não precisa de orquestração containerizada com autoscaling. A complexidade da infra deve ser proporcional ao volume e à criticidade.
- **"Segredos ficam em variáveis de ambiente no servidor"** — Variáveis de ambiente em texto plano em VM compartilhada é risco de segurança. Qualquer processo no servidor pode ler, qualquer dump de ambiente expõe. Secrets manager centralizado é o mínimo aceitável.

### Etapa 06 — Setup

- **"O ambiente de teste usa o mesmo banco de produção"** — Automação de teste que lê/escreve em dados de produção é incidente esperando acontecer. Ambientes de teste devem usar dados isolados — cópia sanitizada ou dados sintéticos. Sem exceção.
- **"As credenciais de produção são as mesmas de teste"** — Credenciais compartilhadas entre ambientes significam que um erro no ambiente de teste afeta produção. Service accounts separadas por ambiente são obrigatórias.
- **"Não precisa de runbook, o dev sabe operar"** — O dev não vai estar disponível às 3h de sábado quando a automação falhar. Quem vai diagnosticar é o operador de plantão que nunca viu o código. Runbook com procedimentos passo a passo é obrigatório.

### Etapa 07 — Build

- **"O tratamento de erro é um try/catch genérico que loga"** — Catch genérico que loga "erro na execução" sem contexto (qual registro, qual step, quais dados) é inútil para diagnóstico. Cada exceção deve capturar contexto suficiente para que alguém consiga diagnosticar sem acessar o ambiente de produção.
- **"A idempotência é complicada, depois a gente adiciona"** — Sem idempotência, retry duplica dados. Duplicar registros financeiros, enviar e-mails em dobro, ou processar o mesmo pedido duas vezes são consequências reais de automação sem idempotência. Implementar desde o primeiro step.
- **"Testamos com 10 registros, em produção são 50.000"** — Teste com volume 5.000x menor que produção não testa nada relevante — não testa rate limits, não testa performance, não testa timeout, não testa consumo de recursos. Volume de teste deve ser pelo menos 50% do volume de produção.

### Etapa 08 — QA

- **"Todos os testes passaram no ambiente de teste"** — O ambiente de teste não é produção. APIs de teste podem ter rate limits diferentes, dados de teste são mais limpos que dados reais, e a latência de rede pode ser diferente. Testes que passam no ambiente de teste e falham em produção são a norma, não a exceção.
- **"O operador disse que entendeu o runbook"** — Entender ≠ executar. O operador precisa executar os cenários do runbook durante o QA — diagnosticar uma falha simulada, reprocessar registros, e parar a automação. Leitura passiva do runbook não é validação.
- **"Não precisa testar concorrência, a automação roda uma vez por dia"** — Uma vez por dia até a execução de ontem atrasar e sobrepor com a de hoje. Ou até alguém disparar manualmente enquanto a agendada está rodando. Cenários de concorrência devem ser testados mesmo em automações "seriais".

### Etapa 09 — Launch Prep

- **"O shadow mode não é necessário, já testamos bastante"** — Testes em ambiente de teste com dados de teste não substituem execução com dados reais em condições reais. O shadow mode é a última oportunidade de encontrar divergências antes de o processo automatizado se tornar oficial. Pular o shadow mode é assumir risco desnecessário.
- **"O processo manual já pode ser desativado, a automação está pronta"** — Desativar o processo manual antes de validar a automação em produção por pelo menos uma semana é eliminar o fallback. Se a automação falhar de forma não-prevista, não há como voltar. Manter processo manual como fallback por 2-4 semanas mínimo.
- **"Não precisa treinar o operador, é só olhar o dashboard"** — Dashboard sem contexto não é monitoramento. O operador precisa saber: o que é normal vs. anormal, quando intervir vs. quando esperar, e como escalar. Treinamento prático com cenários reais é obrigatório.

### Etapa 10 — Go-Live

- **"A automação está rodando há 2 dias sem erro, projeto encerrado"** — Dois dias sem erro é amostra insuficiente. Processos que rodam mensalmente podem ter bugs que só aparecem na virada do mês. Processos com exceções raras podem funcionar por semanas até o primeiro edge case aparecer. Monitoramento da primeira semana (mínimo) é parte do projeto.
- **"O ROI a gente calcula depois"** — Se o ROI não é calculado agora (com baseline da primeira semana), nunca será. Sem dados concretos de economia, a automação vira custo puro na percepção de quem controla o orçamento — e será cortada na próxima rodada de redução de custos.
- **"Entregamos a automação, o time de operação assume"** — Handoff sem transferência de conhecimento formal resulta em operação que não sabe manter. A primeira exceção não prevista gera chamado para o time de dev, que já está em outro projeto. Sessão de transferência com cenários práticos é investimento de proteção.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é automação de processo** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Precisamos de uma tela para o operador preencher dados e o sistema processar" | Aplicação web com workflow, não automação de processo | Reclassificar para web-app |
| "Queremos um sistema completo para gerenciar nossos processos" | Plataforma de BPM/workflow, não automação pontual | Reclassificar para platform-implementation ou saas |
| "A automação precisa de um portal onde clientes acompanhem o status" | Aplicação web com backend, não automação | Reclassificar para web-app |
| "Precisa de dashboards interativos para análise de dados" | Projeto de BI/analytics, não automação de processo | Reclassificar para data-analytics |
| "Queremos que a IA decida o que fazer em cada caso" | Projeto de ML/AI, não automação de regras | Avaliar se regras determinísticas resolvem ou reclassificar para ai-ml |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não sabemos exatamente como o processo funciona hoje" | 01 | Sem AS-IS, o TO-BE será baseado em suposições | Mapear processo AS-IS antes de avançar |
| "O sistema legado vai ser substituído em 6 meses" | 01 | Automação para sistema que será desativado — investimento perdido | Esperar novo sistema ou automatizar sobre o novo |
| "Não temos acesso às APIs dos sistemas" | 02 | Sem API e sem acesso à interface, automação é impossível | Resolver acesso antes de estimar escopo |
| "O processo muda toda semana" | 01 | Processo instável = automação com retrabalho constante | Estabilizar processo antes de automatizar |
| "Não temos quem monitore a automação" | 03 | Automação sem monitoramento falha silenciosamente | Definir modelo de operação antes do build |
| "O orçamento cobre só o desenvolvimento, operação é com a gente" | 01 | Cliente não tem capacidade de operar automação | Incluir operação no escopo ou definir modelo de suporte |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O pessoal que faz o processo manual não sabe que vamos automatizar" | 01 | Resistência à mudança, sabotagem informacional | Iniciar change management imediatamente |
| "O sistema tem API mas ninguém nunca usou" | 02 | API pode estar incompleta, instável ou mal documentada | Fazer prova de conceito com a API antes de comprometer escopo |
| "Precisa funcionar em horário comercial, 8h-18h" | 03 | Automação e operadores humanos competindo pelo mesmo sistema | Planejar execução em horário de baixo uso ou isolar acessos |
| "Os dados entre os sistemas são 'praticamente' iguais" | 04 | 'Praticamente' significa que têm diferenças não mapeadas | Fazer mapeamento campo a campo antes de aceitar como premissa |
| "Já tentamos RPA antes e não deu certo" | 01 | Pode haver problema organizacional, não apenas técnico | Investigar causas da falha anterior antes de repetir abordagem |
| "O volume vai triplicar no próximo trimestre" | 02 | Automação dimensionada para volume atual pode não escalar | Arquitetar para volume projetado, não apenas atual |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Processo manual identificado com frequência, volume e responsável (pergunta 1)
- Volume de execuções e dados quantificado (pergunta 2)
- Sistemas envolvidos listados com tipo de acesso (API ou UI) (pergunta 3)
- Processo estável confirmado (pergunta 5)
- ROI estimado e justificado (pergunta 15)

### Etapa 02 → 03

- Processo AS-IS mapeado step by step com detalhamento técnico (pergunta 1)
- Exceções e edge cases levantados exaustivamente (pergunta 2)
- Sistemas inventariados com tipo de acesso, versão e credenciais (pergunta 3)
- Fronteira entre automação e sistema completo validada (pergunta 15)

### Etapa 03 → 04

- Abordagem técnica escolhida com justificativa baseada em dados (pergunta 1)
- Processo TO-BE desenhado e aprovado pelos stakeholders (pergunta 2)
- Modelo de operação pós-automação definido (pergunta 3)
- Estratégia de tratamento de exceções documentada (pergunta 4)
- Custo de operação estimado e aprovado (pergunta 11)

### Etapa 04 → 05

- Fluxo automatizado especificado step by step com sistemas, APIs e dados (pergunta 1)
- Mapeamento campo a campo entre sistemas documentado (pergunta 2)
- Credenciais especificadas com tipo, permissão e responsável (pergunta 3)
- Triggers e scheduling definidos com timezone e concorrência (pergunta 4)
- Documentação aprovada por stakeholders técnicos e de negócio (pergunta 15)

### Etapa 05 → 06

- Plataforma de automação escolhida e justificada (pergunta 1)
- Arquitetura de resiliência desenhada (idempotência, retry, dead letter, circuit breaker) (pergunta 2)
- Secrets management com ferramenta centralizada definido (pergunta 3)
- Stack de monitoramento definida com alertas (pergunta 4)
- Modelo de ambientes e deploy documentado (pergunta 15)

### Etapa 06 → 07

- Infraestrutura provisionada e funcional (pergunta 1)
- Credenciais configuradas e testadas com acesso real (pergunta 2)
- Pipeline CI/CD testado end-to-end (pergunta 15)
- Ambiente de teste com dados representativos (pergunta 5)
- Runbook operacional criado (pergunta 6)

### Etapa 07 → 08

- Cada step implementado com teste automatizado (pergunta 1)
- Tratamento de exceções robusto (retry, dead letter, escalação) (pergunta 2)
- Idempotência implementada em steps que modificam dados (pergunta 3)
- Fluxo completo testado com conexão real aos sistemas de teste (pergunta 6)

### Etapa 08 → 09

- Testes end-to-end com dados representativos aprovados (pergunta 1)
- Testes de falha e recuperação executados (pergunta 2)
- Testes de performance com volume máximo dentro do SLA (pergunta 3)
- Monitoramento e alertas validados com execução real (pergunta 5)
- UAT do operador aprovado com cenários do runbook (pergunta 6)

### Etapa 09 → 10

- Shadow mode executado e resultados aprovados pelos stakeholders (perguntas 1 e 13)
- Plano de cutover documentado com sequência e responsáveis (pergunta 2)
- Plano de rollback documentado com processo manual funcional (pergunta 3)
- Treinamento de operadores realizado com cenários reais (pergunta 4)
- Credenciais de produção verificadas e testadas (pergunta 6)

### Etapa 10 → Encerramento

- Cutover executado conforme plano (pergunta 1)
- Monitoramento da primeira semana com taxa de sucesso dentro do target (pergunta 3)
- Métricas de baseline registradas (pergunta 5)
- Aceite formal obtido (pergunta 12)
- Acessos entregues e documentação transferida (perguntas 10 e 11)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de automação de processos. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 RPA | V2 Workflow BPMN | V3 Orquestração APIs | V4 Scripts/ETL | V5 DevOps/Infra |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 2 | 1 | 2 |
| 02 Discovery | 4 | 3 | 3 | 2 | 2 |
| 03 Alignment | 3 | 3 | 3 | 2 | 2 |
| 04 Definition | 4 | 4 | 4 | 3 | 3 |
| 05 Architecture | 2 | 3 | 4 | 2 | 4 |
| 06 Setup | 3 | 3 | 3 | 2 | 3 |
| 07 Build | 5 | 4 | 4 | 3 | 4 |
| 08 QA | 5 | 3 | 4 | 3 | 3 |
| 09 Launch Prep | 4 | 3 | 3 | 2 | 3 |
| 10 Go-Live | 3 | 2 | 2 | 2 | 2 |
| **Total relativo** | **35** | **30** | **32** | **22** | **28** |

**Observações por variante:**

- **V1 RPA**: Build e QA são os mais pesados — robôs são frágeis (dependem de posição de elementos na tela), o tratamento de exceções visuais é complexo, e os testes precisam cobrir variações de resolução, velocidade de rede e estado da interface. Discovery também é pesado porque exige observação direta de cada interação com a tela.
- **V2 Workflow BPMN**: Esforço distribuído, com pico na Definition (modelagem do processo TO-BE com todas as ramificações, aprovações e escalações) e no Build (implementação de human tasks, formulários de aprovação, e integrações com conectores). Menor esforço de QA porque engines BPMN têm boa testabilidade nativa.
- **V3 Orquestração APIs**: Architecture e Build são os picos — projetar resiliência (retry, compensação, circuit breaker) e implementar mapeamento de dados entre schemas diferentes. QA é pesado por exigir simulação de falhas de cada API na cadeia.
- **V4 Scripts/ETL**: O mais leve de todas as variantes. Escopo geralmente bem definido (extrair de A, transformar, carregar em B). O risco principal está na qualidade dos dados (exceções no ETL) e no monitoramento de execuções agendadas.
- **V5 DevOps/Infra**: Architecture é o pico — Infrastructure as Code exige planejamento cuidadoso de state management, secrets, e idempotência. Build é pesado pelo rigor de testes (um erro de infra pode derrubar produção). Setup também é relevante pela complexidade de ambientes multi-cloud.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Todos os sistemas têm API — sem RPA necessário (Etapa 02, pergunta 4) | Etapa 06: configuração de VMs com resolução de tela. Etapa 07: testes de posicionamento de elementos visuais. Etapa 08: testes de variação de resolução/velocidade. |
| Processo totalmente automatizado — sem human-in-the-loop (Etapa 01, pergunta 10) | Etapa 04: especificação de formulários de aprovação e escalação humana. Etapa 07: implementação de human tasks. Etapa 08: UAT com aprovadores humanos no fluxo. |
| Sem dados sensíveis envolvidos (Etapa 02, pergunta 9) | Etapa 04: pergunta 11 (data masking). Etapa 05: pergunta 13 (tokenização). Etapa 06: sanitização de dados de teste. |
| Processo executado uma vez por dia — sem concorrência (Etapa 04, pergunta 4) | Etapa 08: pergunta 4 (testes de concorrência) — reduzida em importância, mas não eliminada (execuções sobrepostas por atraso ainda são possíveis). |
| Sem integração com sistemas externos — processo interno (Etapa 01, pergunta 3) | Etapa 05: perguntas 10 e 12 (retry de APIs externas, rate limits). Etapa 07: pergunta 11 (circuit breaker). Etapa 08: pergunta 10 (teste de rate limits). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Abordagem RPA escolhida (Etapa 03, pergunta 1) | Etapa 06: configuração de VMs com resolução de tela e acesso aos sistemas é gate. Etapa 07: testes de estabilidade de elementos visuais são obrigatórios. Etapa 08: testes em ambiente idêntico ao de produção (resolução, SO, browser) são gate. Etapa 09: shadow mode é critical path (RPA é mais frágil que API). |
| Dados sensíveis envolvidos — PII, financeiros (Etapa 02, pergunta 9) | Etapa 04: pergunta 11 (masking em logs) é gate. Etapa 05: pergunta 3 (secrets management) e pergunta 13 (data masking) se tornam obrigatórias. Etapa 06: sanitização de dados de teste é pré-requisito. |
| Processo com impacto financeiro em caso de falha (Etapa 02, pergunta 5) | Etapa 05: pergunta 2 (idempotência e compensação) é gate. Etapa 07: pergunta 3 (idempotência implementada) é bloqueadora. Etapa 08: perguntas 2 e 3 (testes de falha e performance) são gates. Etapa 09: pergunta 1 (shadow mode) é obrigatório e deve ter duração estendida. |
| Volume de dados >100K registros por execução (Etapa 01, pergunta 2) | Etapa 05: pergunta 5 (escalabilidade horizontal) se torna gate. Etapa 07: pergunta 7 (teste com volume representativo) é bloqueador. Etapa 08: pergunta 3 (teste de performance com volume máximo) é gate. |
| Human-in-the-loop com aprovações (Etapa 01, pergunta 10) | Etapa 04: especificação de formulários de aprovação e regras de escalação é gate. Etapa 07: implementação de human tasks com SLA e escalação é obrigatória. Etapa 08: UAT com aprovadores humanos reais no fluxo é gate. |
| Múltiplos processos similares (Etapa 02, pergunta 12) | Etapa 05: pergunta 8 (regras de negócio isoladas e configuráveis) se torna gate. Etapa 07: pergunta 10 (regras isoladas em módulos) é obrigatória. |
| Requisitos regulatórios (auditoria, LGPD) (Etapa 01, pergunta 11) | Etapa 04: pergunta 6 (logging com retenção definida) é gate. Etapa 05: pergunta 3 (secrets management com audit trail) é gate. Etapa 08: verificação de compliance de logs e trilha de auditoria é obrigatória antes do go-live. |
