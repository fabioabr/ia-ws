---
title: "Sistema de Integração / Middleware — Blueprint"
description: "Camada que conecta sistemas heterogêneos existentes. Adaptadores, transformações de dados, orquestração de fluxos, tratamento de erros e monitoramento de integrações."
category: project-blueprint
type: integration-middleware
status: rascunho
created: 2026-04-13
---

# Sistema de Integração / Middleware

## Descrição

Camada que conecta sistemas heterogêneos existentes. Adaptadores, transformações de dados, orquestração de fluxos, tratamento de erros e monitoramento de integrações.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem toda integração é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — ETL / Sincronização de Dados

Pipeline de extração, transformação e carga de dados entre sistemas — tipicamente batch (horário, diário) ou micro-batch (a cada poucos minutos). O foco é a qualidade e consistência dos dados transformados, a performance do pipeline com volume crescente, e o monitoramento de falhas com reprocessamento automático. Não há orquestração de processos de negócio — o objetivo é manter dados sincronizados entre sistemas. Exemplos: sincronizar catálogo de produtos do ERP para o e-commerce, replicar dados de vendas do PDV para o BI, importar dados de RH do sistema legado para o novo HCM.

### V2 — API Gateway / Hub de APIs

Camada centralizada que expõe APIs internas de forma padronizada para consumidores externos ou internos, com autenticação, rate limiting, transformação de payload, e versionamento. O foco é governança de APIs, segurança (OAuth2, API keys, throttling), e observabilidade (logging, métricas, tracing). Não há lógica de negócio complexa — o gateway roteia, transforma e protege. Exemplos: API gateway corporativo que expõe serviços internos para parceiros, BFF (Backend for Frontend) que agrega múltiplas APIs para o app mobile, hub de APIs para marketplace.

### V3 — Orquestração de Processos de Negócio

Fluxo de integração que implementa lógica de negócio distribuída entre múltiplos sistemas — com sequência de passos, decisões condicionais, compensações em caso de falha, e estado persistente do processo. O foco é a confiabilidade do fluxo (cada passo é executado exatamente uma vez ou com semântica idempotente), visibilidade do estado de cada instância do processo, e tratamento de exceções de negócio. Exemplos: processo de onboarding de cliente (CRM → verificação de crédito → abertura de conta → envio de boas-vindas), fulfillment de pedido (e-commerce → ERP → WMS → transportadora → notificação), processo de sinistro de seguro.

### V4 — Event-Driven / Mensageria

Arquitetura baseada em eventos onde sistemas publicam acontecimentos (pedido criado, pagamento confirmado, estoque atualizado) e consumidores reagem de forma assíncrona e desacoplada. O foco é o design dos eventos (schema, versionamento, idempotência), a confiabilidade da entrega (at-least-once, exactly-once), e a evolução do schema ao longo do tempo sem quebrar consumidores existentes. Exemplos: arquitetura orientada a eventos para microserviços, CQRS/Event Sourcing, integração entre domínios de negócio via domain events, real-time data streaming para analytics.

### V5 — Integração Legada / Adaptador

Integração com sistemas legados que não possuem APIs modernas — comunicação via arquivo (CSV, XML, EDI, posicional), bancos de dados diretamente (stored procedures, views, database links), protocolos proprietários (SOAP com WS-Security, FTP/SFTP, mainframe CICS), ou screen scraping. O foco é a confiabilidade da comunicação com sistemas frágeis, o tratamento de formatos de dados arcaicos, e a documentação de interfaces que frequentemente não possuem especificação formal. Exemplos: integração com sistema de folha de pagamento legado via arquivo posicional, leitura de dados de mainframe via MQ Series, integração com governo via web service SOAP com certificado digital.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | Plataforma/Runtime | Broker/Bus | Observabilidade | Linguagem | Observações |
|---|---|---|---|---|---|
| V1 — ETL/Sync | Apache Airflow, dbt, Prefect | Não se aplica (batch) | Great Expectations, Airflow UI | Python, SQL | dbt para transformações SQL-first. Airflow para orquestração de pipelines complexos. |
| V2 — API Gateway | Kong, AWS API Gateway, Apigee | Não se aplica | Grafana, Datadog, ELK | Node.js, Go, Java | Kong para self-hosted. AWS API Gateway para serverless. Rate limiting e auth centralizados. |
| V3 — Orquestração | Temporal, Apache Camel, n8n | RabbitMQ, Amazon SQS | Temporal UI, Jaeger, Grafana | Java, Go, TypeScript | Temporal para workflows confiáveis com retry e compensação. n8n para low-code. |
| V4 — Event-Driven | Kafka, Amazon EventBridge, NATS | Apache Kafka, RabbitMQ, Amazon SNS/SQS | Kafka UI, Grafana, OpenTelemetry | Java, Go, TypeScript | Kafka para alto throughput. RabbitMQ para menor complexidade operacional. |
| V5 — Legada/Adaptador | Apache Camel, MuleSoft, Spring Integration | MQ Series, ActiveMQ, RabbitMQ | ELK, Grafana, Zabbix | Java, C#, Python | Apache Camel tem 300+ conectores para protocolos legados. MuleSoft para enterprise. |

---

## Etapa 01 — Inception

- **Origem da demanda e motivação de negócio**: Projetos de integração surgem de necessidades operacionais concretas — sistemas que não conversam e geram retrabalho manual (redigitação de dados), processos de negócio que dependem de intervenção humana para mover dados entre sistemas, requisitos regulatórios de reporte consolidado que exigem dados unificados, ou modernização tecnológica que substitui um sistema mas precisa manter integração com os demais. O gatilho real importa porque define o critério de sucesso: se o problema é retrabalho manual, o ROI é mensurável em horas economizadas; se é compliance, o prazo é definido por deadline regulatório; se é modernização, o risco é quebrar integrações existentes durante a transição.

- **Landscape de sistemas envolvidos**: Integração por definição conecta sistemas existentes. A Inception precisa mapear TODOS os sistemas envolvidos — não apenas os dois principais, mas também os que "talvez participem" ou "entram na fase 2". Para cada sistema: nome, versão, fornecedor, tipo de interface disponível (REST API, SOAP, banco de dados, arquivo, fila de mensagens, protocolo proprietário), nível de documentação (API documentada, sem documentação, código-fonte disponível), e quem é o responsável técnico. O landscape de sistemas é o artefato mais importante da Inception porque define a complexidade real do projeto.

- **Propriedade e governança dos sistemas**: Em projetos de integração, o time de desenvolvimento raramente tem controle sobre os sistemas que está integrando. O ERP é gerenciado pela consultoria X, o CRM pelo time Y, o sistema legado pelo fornecedor Z que cobra por hora de suporte. Cada sistema tem seu dono, seu ciclo de releases, e suas regras de acesso. Mapear a governança de cada sistema na Inception é fundamental: quem autoriza acesso à API, quem disponibiliza ambiente de homologação, quem é responsável quando o sistema fica indisponível, e quem precisa ser notificado antes de mudanças na integração.

- **Volume e frequência de dados**: A diferença entre integrar 100 registros por dia e 1 milhão de registros por hora define completamente a arquitetura. Volume baixo com frequência baixa pode ser resolvido com API REST síncrona. Volume alto com frequência alta exige mensageria assíncrona, batching, e possivelmente streaming. Volume com picos sazonais (Black Friday, fechamento mensal) exige dimensionamento para pico, não para média. Levantar volumes reais (não estimados pelo cliente, que costuma subestimar por 10x) via análise de logs ou métricas do sistema de origem é essencial.

- **Criticidade e SLA esperado**: Integração de dados de marketing que atualiza uma vez por dia tolera horas de indisponibilidade. Integração de pagamento em tempo real não tolera segundos. O SLA esperado define a arquitetura (síncrono vs. assíncrono, retry automático vs. circuit breaker, monitoramento passivo vs. alertas em tempo real) e o custo de operação (alta disponibilidade custa mais). Classificar cada fluxo de integração por criticidade na Inception permite priorizar e dimensionar corretamente.

- **Restrições de segurança e compliance**: Integrações movem dados entre sistemas — e dados em trânsito são vulneráveis. Identificar na Inception: quais dados são sensíveis (PII, dados financeiros, dados de saúde), quais regulamentações se aplicam (LGPD, GDPR, PCI-DSS, SOX), se há requisitos de criptografia em trânsito e em repouso, se há restrições de rede (VPN, firewall, whitelist de IP), e se há requisitos de auditoria (log de todas as operações com retenção por X anos). Integrações que movem dados de clientes entre sistemas sem criptografia ou sem log de auditoria são violações de LGPD esperando para acontecer.

### Perguntas

1. Qual é o problema de negócio que esta integração resolve — retrabalho manual, compliance, modernização, ou novo processo? [fonte: Diretoria, Operações, Processo] [impacto: PM, Dev]
2. Quais são TODOS os sistemas envolvidos na integração (nome, versão, fornecedor, tipo de interface disponível)? [fonte: TI, Fornecedores, Operações] [impacto: Arquiteto, Dev, PM]
3. Quem é o responsável técnico e o dono de governança de cada sistema envolvido? [fonte: TI, Diretoria de cada área] [impacto: PM, Dev]
4. Qual é o volume atual de dados trocados entre os sistemas e a projeção de crescimento? [fonte: TI, Operações, DBA] [impacto: Arquiteto, Dev, DevOps]
5. Qual é a frequência necessária da integração — tempo real, near-real-time, batch horário, batch diário? [fonte: Operações, Processo] [impacto: Arquiteto, Dev]
6. Qual é a criticidade de cada fluxo de integração e o SLA esperado (tempo de indisponibilidade tolerável)? [fonte: Operações, Diretoria] [impacto: Arquiteto, DevOps, PM]
7. Quais dados são sensíveis (PII, financeiros, saúde) e quais regulamentações se aplicam (LGPD, PCI-DSS)? [fonte: Jurídico, DPO, Compliance, Segurança da Informação] [impacto: Arquiteto, Dev, DevOps]
8. Existem restrições de rede entre os sistemas (firewall, VPN, whitelist de IP, DMZ)? [fonte: Infra/Redes, Segurança da Informação] [impacto: DevOps, Arquiteto]
9. Existe alguma integração atual entre esses sistemas (manual, planilha, script, ferramenta de ETL) que será substituída? [fonte: TI, Operações] [impacto: Dev, PM]
10. O cliente tem acesso a ambientes de homologação de todos os sistemas envolvidos? [fonte: TI, Fornecedores de cada sistema] [impacto: Dev, QA, PM]
11. Há janelas de manutenção ou indisponibilidade planejada nos sistemas de origem/destino? [fonte: TI, Fornecedores] [impacto: Arquiteto, DevOps]
12. O orçamento contempla custos de licença de middleware, conectores, e infraestrutura de execução? [fonte: Financeiro, TI] [impacto: PM, Arquiteto]
13. Existe time interno com experiência em integração de sistemas ou o conhecimento será todo externo? [fonte: RH, TI] [impacto: PM, Dev]
14. Qual é o prazo esperado e existe deadline regulatório ou de negócio que o justifica? [fonte: Diretoria, Compliance] [impacto: PM, Dev]
15. Existem contratos com fornecedores de sistemas que limitam acesso a APIs ou banco de dados? [fonte: Jurídico, TI, Fornecedores] [impacto: Arquiteto, PM, Dev]

---

## Etapa 02 — Discovery

- **Mapeamento detalhado de interfaces**: Para cada sistema envolvido, documentar com precisão as interfaces disponíveis: endpoints de API (URL, método, autenticação, rate limits, formato de payload, documentação OpenAPI/Swagger), schemas de banco de dados (tabelas, views, stored procedures, triggers que podem ser afetadas), formatos de arquivo (encoding, delimitador, header, tamanho máximo, frequência de geração), e protocolos de mensageria (tópicos, filas, formato de mensagem, política de retry). Cada interface que não tem documentação formal precisa ser investigada — e o custo dessa investigação deve ser incluído no cronograma como spike técnico.

- **Mapeamento de dados e transformações**: Levantar o modelo de dados de cada sistema envolvido e mapear as correspondências campo a campo (de-para). Identificar: campos que existem na origem mas não no destino (serão descartados ou criarão necessidade de extensão no destino?), campos obrigatórios no destino que não existem na origem (de onde vem o valor? default? cálculo? enriquecimento?), diferenças de formato (data DD/MM/YYYY vs. ISO 8601, encoding UTF-8 vs. Latin1, monetário com vírgula vs. ponto), e regras de negócio de transformação (status "A" no sistema A = "Ativo" no sistema B; CPF com pontos na origem, sem pontos no destino). O mapeamento de-para é o artefato que mais consome tempo na Discovery e o que mais gera bugs quando feito superficialmente.

- **Identificação de cenários de erro e exceção**: Integração é primordialmente sobre o que acontece quando dá errado. Mapear todos os cenários de falha previsíveis: sistema de origem indisponível (timeout, 503), dados inválidos na origem (campo obrigatório nulo, formato inesperado, valor fora da faixa), rejeição pelo sistema de destino (registro duplicado, violação de constraint, regra de negócio não atendida), e falha de infraestrutura (rede, DNS, certificado expirado). Para cada cenário, definir: como detectar, como o erro é reportado, e qual a ação correta (retry automático, dead letter queue, alerta para operação manual, rollback/compensação).

- **Requisitos de idempotência e consistência**: Quando uma mensagem é processada duas vezes (por retry após timeout, por reprocessamento de erro, ou por duplicação na origem), o resultado deve ser o mesmo — não pode gerar registro duplicado, cobrança duplicada, ou e-mail duplicado. Levantar quais operações precisam de idempotência (quase todas), qual é a chave de idempotência natural de cada entidade (ID do pedido, número do documento, hash do payload), e como o sistema de destino se comporta com operações duplicadas (ignora? retorna erro? sobrescreve?). Idempotência não tratada é a causa #1 de bugs em integração.

- **Requisitos de observabilidade e auditoria**: Integrações são invisíveis por natureza — quando funcionam, ninguém percebe; quando falham, ninguém sabe por quê. Levantar os requisitos de observabilidade: logging estruturado de cada operação (origem, destino, payload, resultado, duração), métricas de throughput e latência por fluxo, tracing distribuído para correlacionar operações entre sistemas, alertas de falha com SLA de notificação, e dashboard de saúde das integrações. Para compliance, levantar se há requisito de auditoria (retenção de logs por X anos, rastreabilidade de quem/quando/o quê em cada operação).

- **Dependências de sequência e ordering**: Alguns dados têm dependência de ordem — o pedido precisa existir antes dos itens do pedido, o cliente precisa ser cadastrado antes da primeira compra, o contrato precisa estar ativo antes de gerar cobrança. Se a integração processa eventos fora de ordem (item do pedido chega antes do pedido), o sistema de destino rejeita. Mapear todas as dependências de sequência e definir a estratégia: garantir ordem no transporte (partição por chave no Kafka, FIFO queue no SQS), ou tratar fora de ordem no consumidor (retry com delay, buffer de reordenação).

### Perguntas

1. Todas as interfaces de todos os sistemas foram documentadas com precisão (URLs, autenticação, formatos, rate limits)? [fonte: TI, Fornecedores, DBA] [impacto: Dev, Arquiteto]
2. O mapeamento de dados campo a campo (de-para) foi concluído para cada fluxo de integração? [fonte: Operações, Analista de Negócio, DBA] [impacto: Dev, QA]
3. As regras de transformação de dados foram documentadas para cada campo com diferença de formato ou semântica? [fonte: Operações, Analista de Negócio] [impacto: Dev]
4. Todos os cenários de erro previsíveis foram mapeados com ação correta para cada um (retry, DLQ, alerta, compensação)? [fonte: TI, Operações] [impacto: Dev, Arquiteto]
5. A estratégia de idempotência foi definida para cada fluxo — qual chave natural, como detectar duplicatas? [fonte: Analista de Negócio, Dev] [impacto: Dev, Arquiteto]
6. Os requisitos de observabilidade foram levantados (logging, métricas, tracing, alertas, dashboard)? [fonte: TI, Operações, Compliance] [impacto: Dev, DevOps]
7. Os requisitos de auditoria foram identificados (retenção de logs, rastreabilidade, compliance)? [fonte: Compliance, Jurídico, DPO] [impacto: Dev, DevOps]
8. As dependências de sequência entre entidades foram mapeadas (ordem de processamento obrigatória)? [fonte: Analista de Negócio, DBA] [impacto: Dev, Arquiteto]
9. O volume de dados por fluxo foi medido com dados reais (não estimativas), incluindo picos sazonais? [fonte: DBA, TI, Operações] [impacto: Arquiteto, DevOps]
10. As janelas de disponibilidade de cada sistema foram documentadas (horários de manutenção, batch noturno)? [fonte: TI, Fornecedores] [impacto: Arquiteto, DevOps]
11. Os ambientes de homologação de todos os sistemas foram verificados — existem, estão atualizados, o time tem acesso? [fonte: TI, Fornecedores] [impacto: Dev, QA, PM]
12. As limitações conhecidas de cada sistema foram documentadas (rate limits, tamanho máximo de payload, timeout)? [fonte: TI, Fornecedores, DBA] [impacto: Dev, Arquiteto]
13. Os processos manuais atuais que a integração substituirá foram mapeados passo a passo? [fonte: Operações, Processo] [impacto: Dev, PM, Analista de Negócio]
14. As regras de negócio que governam a integração são estáveis ou mudam frequentemente? [fonte: Operações, Diretoria] [impacto: Arquiteto, Dev]
15. Existe expectativa de extensão futura (novos sistemas, novos fluxos, aumento de volume) que impacte a arquitetura? [fonte: Diretoria, TI] [impacto: Arquiteto, PM]

---

## Etapa 03 — Alignment

- **Acordo de responsabilidades entre times/fornecedores**: Em projetos de integração, raramente um único time controla todos os sistemas. O time do ERP é diferente do time do CRM, que é diferente do time do e-commerce. Alinhar formalmente: quem configura o acesso às APIs (time do sistema de origem), quem adapta endpoints quando o formato não atende (time do sistema de origem ou time de integração?), quem investiga quando dados chegam errados (ambos, com critérios de triagem claros), e quem é acionado fora do horário comercial quando a integração crítica falha. Sem este acordo, bugs de integração ficam em ping-pong entre times indefinidamente.

- **Contrato de interface (API contract)**: Definir formalmente o contrato de cada interface como artefato versionado — schema de request/response (OpenAPI/Swagger para REST, WSDL para SOAP, Avro/Protobuf para eventos, JSON Schema para mensagens), códigos de erro e seus significados, comportamento de paginação, e política de versionamento (URL versioning /v1/, header versioning, ou semantic versioning de eventos). O contrato deve ser acordado e assinado por ambos os times antes do Build — mudanças posteriores precisam seguir processo formal de change request para evitar quebra silenciosa.

- **Estratégia de tratamento de erros e reprocessamento**: Alinhar com todos os stakeholders o que acontece quando a integração falha. Para cada fluxo crítico: retry automático (quantas vezes, com qual intervalo, com backoff exponencial?), dead letter queue (onde ficam mensagens que falharam após todos os retries, quem monitora, qual o processo de reprocessamento manual?), alertas (quem recebe, em qual canal, em qual SLA?), e compensação (se o passo A executou mas o passo B falhou, como desfazer o A?). A estratégia de erro é a decisão mais importante do Alignment para projetos de integração — mais do que o happy path, que geralmente é simples.

- **Modelo de deploy e versionamento**: Alinhar como a integração será versionada e deployada sem interromper fluxos em produção. Definir: deploy blue-green (duas versões rodando em paralelo, switch instantâneo), canary (nova versão recebe % do tráfego gradualmente), ou deploy com downtime planejado (aceitável para batch noturno, inaceitável para real-time). Alinhar também a compatibilidade backward — versão N da integração precisa funcionar com versão N-1 do sistema de destino durante o período de transição? Rolling update sem backward compatibility é a causa mais comum de incidente em integração.

- **SLA operacional e modelo de suporte**: Definir o modelo de operação pós-go-live: quem monitora a saúde das integrações no dia a dia (NOC, DevOps, time de integração), qual é o processo de escalonamento quando um alerta dispara (L1 verifica dashboard → L2 investiga logs → L3 aciona desenvolvedor), qual é o SLA de resolução por severidade (crítico: 1h, alto: 4h, médio: 24h, baixo: 72h), e qual é o processo para solicitar mudanças na integração (novo campo, nova regra, novo sistema). Integrações sem dono operacional definido degradam silenciosamente até quebrarem de forma catastrófica.

### Perguntas

1. As responsabilidades entre o time de integração e os times de cada sistema foram formalizadas por escrito? [fonte: TI, Diretoria de cada área, Fornecedores] [impacto: PM, Dev]
2. Os contratos de interface (API contract) foram definidos, versionados e acordados por todos os envolvidos? [fonte: Dev, Arquiteto, Fornecedores] [impacto: Dev, QA]
3. A estratégia de tratamento de erros foi alinhada para cada fluxo (retry, DLQ, alerta, compensação)? [fonte: Arquiteto, Operações, Dev] [impacto: Dev, DevOps]
4. O modelo de reprocessamento de mensagens falhadas foi definido (manual, automático, com aprovação)? [fonte: Operações, Arquiteto] [impacto: Dev, Operações]
5. A estratégia de deploy sem downtime foi definida (blue-green, canary, rolling update)? [fonte: DevOps, Arquiteto] [impacto: Dev, DevOps]
6. A compatibilidade backward entre versões da integração e dos sistemas foi acordada? [fonte: Dev, Fornecedores, Arquiteto] [impacto: Dev, DevOps]
7. O SLA operacional por severidade foi definido e aceito por todos os stakeholders? [fonte: Operações, Diretoria, TI] [impacto: PM, DevOps, Dev]
8. O processo de escalonamento de incidentes foi documentado (L1 → L2 → L3, responsáveis, canais)? [fonte: Operações, TI] [impacto: DevOps, PM]
9. O processo de change request para alterações na integração foi definido? [fonte: TI, Processo, Diretoria] [impacto: PM, Dev]
10. Os ambientes de homologação são representativos de produção (mesma versão dos sistemas, dados realistas)? [fonte: TI, Fornecedores, DBA] [impacto: QA, Dev]
11. O time de integração tem acesso a logs e métricas de todos os sistemas envolvidos para diagnóstico? [fonte: TI, Fornecedores] [impacto: Dev, DevOps]
12. O horário de operação da integração foi definido (24/7, horário comercial, janelas de batch)? [fonte: Operações, TI] [impacto: Arquiteto, DevOps]
13. O impacto da integração na performance dos sistemas de origem e destino foi avaliado e aceito pelos donos? [fonte: TI, DBA, Fornecedores] [impacto: Arquiteto, DevOps]
14. As dependências externas (conectividade VPN, certificados, tokens) foram listadas com responsáveis e validade? [fonte: TI, Segurança da Informação] [impacto: DevOps, Dev]
15. O cliente entende que mudanças unilaterais nos sistemas de origem/destino podem quebrar a integração? [fonte: TI, Diretoria] [impacto: PM, Dev]

---

## Etapa 04 — Definition

- **Especificação dos fluxos de integração**: Para cada fluxo, produzir uma especificação completa: sistema de origem, sistema de destino, trigger (evento, schedule, API call), mapeamento campo a campo com regras de transformação, critérios de filtro (quais registros entram no fluxo), validações de entrada (formato, obrigatoriedade, faixa de valores), tratamento de cada tipo de erro, e resultado esperado (registro criado, atualizado, ou mensagem enfileirada). A especificação deve ser detalhada o suficiente para que um desenvolvedor implemente sem perguntar nada — cada ambiguidade na especificação será resolvida pelo dev de forma ad-hoc, frequentemente incorreta.

- **Schema de eventos e mensagens**: Para cada mensagem ou evento trocado entre sistemas, definir o schema formal — campos, tipos de dados, obrigatoriedade, enumerações válidas, e versionamento. Para sistemas event-driven, o schema é o contrato público do evento — todos os consumidores dependem dele. Usar schema registry (Confluent Schema Registry para Kafka, AWS Glue Schema Registry) para garantir que produtores não publiquem mensagens que violem o contrato. Definir a estratégia de evolução do schema (backward compatible, forward compatible, full compatible) antes do Build — mudar a estratégia com consumidores já em produção é caro.

- **Mapeamento de dados com regras de transformação**: Produzir o de-para completo para cada fluxo — campo de origem, campo de destino, tipo de transformação (direto, formatação, lookup, cálculo, concatenação, split, default), e exemplos concretos com dados reais. Especial atenção a: tratamento de nulos (campo ausente vs. campo com valor null vs. campo com string vazia — cada sistema trata de forma diferente), conversão de encoding (Latin1 → UTF-8, acentos e caracteres especiais), e normalização de identificadores (CPF com e sem pontos, telefone com e sem código de país). O mapeamento de dados é o coração da integração — erros aqui se manifestam como dados corrompidos ou inconsistentes nos sistemas de destino.

- **Definição de SLAs técnicos por fluxo**: Para cada fluxo, especificar os SLAs técnicos concretos: latência máxima end-to-end (do momento em que o dado muda na origem até estar disponível no destino), throughput mínimo (registros por segundo em pico), disponibilidade (% uptime por mês — 99.9% = ~43min de downtime/mês), e tempo máximo de recuperação após falha (RTO). Estes SLAs direcionam decisões de arquitetura — latência de 1 segundo exige integração síncrona com circuit breaker; latência de 1 hora permite batch com retry. SLAs não definidos são SLAs infinitos — e ninguém reclama até o dia em que a latência de 2 minutos vira 2 horas.

- **Diagramas de sequência e fluxo**: Para cada fluxo complexo (especialmente os de orquestração com múltiplos passos), produzir diagrama de sequência mostrando: a ordem exata das chamadas entre sistemas, os payloads trocados, os pontos de decisão (se condição X, vai para sistema A; se condição Y, vai para sistema B), os pontos de checkpoint/commit (onde o estado é persistido), e os fluxos de compensação (o que acontece quando o passo 3 de 5 falha — como desfazer os passos 1 e 2). O diagrama de sequência é o artefato que mais revela complexidade oculta — fluxos que pareciam simples no Discovery se revelam complexos quando cada interação é desenhada.

- **Plano de migração de dados iniciais**: Se a integração substitui um processo manual existente, frequentemente há backlog de dados que precisam ser migrados/sincronizados antes do go-live — o sistema de destino não tem os dados históricos que o sistema de origem tem. Definir: qual o volume de dados a migrar, qual o período histórico (últimos 6 meses, 2 anos, tudo), qual o formato da migração (carga inicial via script one-shot, export/import, ou replay de eventos), e quais validações serão aplicadas nos dados migrados. A migração inicial frequentemente é subestimada — pode levar dias de execução e semanas de validação.

### Perguntas

1. A especificação de cada fluxo de integração está completa com trigger, mapeamento, validações e tratamento de erros? [fonte: Analista de Negócio, Dev, Arquiteto] [impacto: Dev, QA]
2. Os schemas de eventos/mensagens foram definidos formalmente e versionados? [fonte: Arquiteto, Dev] [impacto: Dev, QA]
3. O mapeamento de dados campo a campo inclui regras de transformação com exemplos concretos? [fonte: Analista de Negócio, Operações] [impacto: Dev, QA]
4. O tratamento de nulos, encoding e normalização de identificadores foi especificado para cada campo? [fonte: Dev, Analista de Negócio] [impacto: Dev]
5. Os SLAs técnicos por fluxo foram especificados (latência, throughput, disponibilidade, RTO)? [fonte: Operações, TI, Diretoria] [impacto: Arquiteto, DevOps]
6. Os diagramas de sequência dos fluxos complexos foram produzidos e validados por todos os envolvidos? [fonte: Arquiteto, Dev, Analista de Negócio] [impacto: Dev, QA]
7. Os fluxos de compensação para cenários de falha parcial foram especificados? [fonte: Arquiteto, Analista de Negócio] [impacto: Dev]
8. O plano de migração de dados iniciais foi definido (volume, período, formato, validações)? [fonte: DBA, Operações, Analista de Negócio] [impacto: Dev, QA, PM]
9. A estratégia de evolução de schema foi definida (backward/forward/full compatible)? [fonte: Arquiteto] [impacto: Dev]
10. As validações de entrada de cada fluxo foram especificadas com exemplos de dados válidos e inválidos? [fonte: Analista de Negócio, Dev] [impacto: Dev, QA]
11. Os cenários de concorrência foram analisados (dois eventos para o mesmo registro chegando simultaneamente)? [fonte: Arquiteto, Dev] [impacto: Dev]
12. O volume de dados da migração inicial foi estimado e o tempo de execução projetado? [fonte: DBA, Dev] [impacto: Dev, PM, DevOps]
13. As regras de negócio de transformação foram validadas com dados reais (não apenas com exemplos teóricos)? [fonte: Operações, Analista de Negócio] [impacto: Dev, QA]
14. Os critérios de aceite de cada fluxo foram definidos de forma verificável (não ambíguos)? [fonte: Operações, PM, Analista de Negócio] [impacto: QA, Dev]
15. A documentação de definição foi revisada e aprovada por todos os stakeholders (incluindo donos de cada sistema)? [fonte: TI, Operações, Diretoria] [impacto: PM, Dev]

---

## Etapa 05 — Architecture

- **Padrão de integração (síncrono vs. assíncrono)**: A escolha entre integração síncrona (request-response — o chamador espera a resposta) e assíncrona (fire-and-forget com confirmação posterior via evento ou callback) é a decisão arquitetural mais fundamental. Síncrono é simples de implementar e debugar, mas cria acoplamento temporal (se o destino está lento ou fora, a origem é impactada) e não escala bem sob carga. Assíncrono desacopla temporalmente (a origem não espera o destino), mas adiciona complexidade de garantia de entrega, ordering, e eventual consistency. A maioria dos projetos de integração usa ambos — síncrono para consultas (preciso da resposta agora) e assíncrono para comandos (processar quando possível).

- **Escolha do message broker / event bus**: Se a arquitetura inclui comunicação assíncrona, a escolha do broker define as garantias de entrega e o modelo de consumo. Apache Kafka é indicado para alto throughput, retenção de eventos como log imutável, replay de mensagens, e múltiplos consumidores independentes — mas tem complexidade operacional alta (ZooKeeper/KRaft, partições, rebalanceamento). RabbitMQ é mais simples de operar, oferece routing flexível e suporte nativo a dead letter queues — adequado para a maioria dos projetos com throughput moderado. Amazon SQS/SNS é a opção serverless (zero infraestrutura para gerenciar) com custo por mensagem — ideal para projetos em AWS que não precisam de replay ou ordering estrito.

- **Plataforma de orquestração / runtime**: Para fluxos simples (A → B com transformação), código custom em container é suficiente. Para fluxos complexos com múltiplos passos, retry, compensação e estado persistente, uma plataforma de workflow é mais adequada. Temporal (open-source) oferece durabilidade de estado, retry built-in, timeouts, e visibilidade de cada instância — é a escolha mais robusta para orquestração de processos de negócio. Apache Camel é indicado quando há muitos protocolos diferentes (300+ conectores — SOAP, FTP, SFTP, JMS, JDBC, MQTT, LDAP). n8n/Zapier são indicados para integrações de baixa complexidade que não-técnicos precisam configurar.

- **Estratégia de circuit breaker e resiliência**: Quando o sistema de destino fica lento ou indisponível, a integração não deve continuar tentando indefinidamente — isso consome recursos e pode derrubar o sistema de origem por backpressure. Implementar circuit breaker (Hystrix, Resilience4j, Polly): após N falhas consecutivas, o circuito "abre" e chamadas são rejeitadas imediatamente (fail fast) por T segundos antes de tentar novamente (half-open). Combinar com retry com backoff exponencial (1s, 2s, 4s, 8s, max 60s) e dead letter queue para mensagens que esgotaram todos os retries. A estratégia de resiliência deve ser definida por fluxo — um fluxo crítico pode ter 10 retries, um fluxo informativo pode ter 3.

- **Observabilidade e monitoramento**: Definir a stack de observabilidade: logging estruturado com correlation ID que permite rastrear uma operação através de todos os sistemas (ELK/Loki para log aggregation), métricas de throughput/latência/erros por fluxo (Prometheus + Grafana), tracing distribuído (Jaeger, Zipkin, ou AWS X-Ray) para visualizar a cadeia de chamadas, e dashboard de saúde das integrações com indicadores de SLA. Para integrações críticas, definir também synthetic monitoring (agente que executa o fluxo periodicamente com dados de teste e verifica o resultado) para detectar falhas antes que os usuários percebam.

- **Segurança em trânsito e em repouso**: Definir os controles de segurança para cada trecho da integração: TLS 1.3 para todas as comunicações entre sistemas, autenticação adequada por fluxo (OAuth2 client credentials para API-to-API, certificado mTLS para integrações bancárias, API key para integrações simples), autorização (cada integração acessa apenas os dados necessários — principle of least privilege), criptografia de dados sensíveis no payload da mensagem (field-level encryption para PII mesmo dentro do broker), e mascaramento de dados sensíveis nos logs (não logar CPF, número de cartão, ou senhas em texto plano). Para compliance LGPD, garantir que existe log de quem acessou dados pessoais e quando.

### Perguntas

1. O padrão de integração (síncrono/assíncrono) foi definido para cada fluxo com justificativa documentada? [fonte: Arquiteto] [impacto: Dev, DevOps]
2. O message broker foi escolhido considerando throughput, garantias de entrega, complexidade operacional e custo? [fonte: Arquiteto, DevOps, Financeiro] [impacto: Dev, DevOps]
3. A plataforma de orquestração/runtime foi escolhida com base na complexidade dos fluxos? [fonte: Arquiteto, Dev] [impacto: Dev, DevOps]
4. A estratégia de circuit breaker e resiliência foi definida por fluxo (retries, backoff, DLQ, fallback)? [fonte: Arquiteto, Dev] [impacto: Dev]
5. A stack de observabilidade foi definida (logging, métricas, tracing, dashboard, alertas)? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
6. O correlation ID foi definido para permitir rastreamento de uma operação através de todos os sistemas? [fonte: Arquiteto, Dev] [impacto: Dev]
7. A segurança em trânsito e em repouso foi definida para cada fluxo (TLS, autenticação, autorização, encryption)? [fonte: Segurança da Informação, Arquiteto] [impacto: Dev, DevOps]
8. O mascaramento de dados sensíveis nos logs foi definido (PII, cartão, senhas)? [fonte: DPO, Segurança da Informação] [impacto: Dev]
9. A estratégia de escalabilidade horizontal foi definida (como adicionar capacity sob carga)? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
10. Os custos mensais da arquitetura foram calculados para volume atual e projeção de pico? [fonte: Financeiro, Arquiteto] [impacto: PM, DevOps]
11. A estratégia de deploy sem downtime para integrações 24/7 foi definida? [fonte: Arquiteto, DevOps] [impacto: Dev, DevOps]
12. O schema registry foi planejado para controle de versão de schemas de eventos? [fonte: Arquiteto, Dev] [impacto: Dev]
13. A estratégia de rate limiting no lado do consumidor foi definida para não sobrecarregar os sistemas de destino? [fonte: Arquiteto, Dev, Fornecedores] [impacto: Dev]
14. O plano de disaster recovery foi definido (broker/database replica em outra região, RTO/RPO)? [fonte: Arquiteto, DevOps, TI] [impacto: DevOps, PM]
15. O modelo de branches, ambientes (dev, staging, produção) e pipeline de CI/CD foi documentado e aprovado? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 06 — Setup

- **Infraestrutura de middleware**: Provisionar o message broker (Kafka cluster, RabbitMQ, SQS queues), a plataforma de orquestração (Temporal server, Airflow), e o runtime de execução (containers, serverless functions) em ambientes separados (dev, staging, produção). Usar Infrastructure as Code (Terraform, Pulumi, CloudFormation) desde o primeiro recurso — ambientes de integração são complexos (múltiplos componentes, conectividades cruzadas, configurações por ambiente) e recriar manualmente é propenso a erro. Cada ambiente deve ter conexões isoladas para os sistemas de origem e destino — staging da integração se conecta ao homologação do ERP, não ao produção.

- **Conectividade com sistemas externos**: Configurar todas as conexões com os sistemas de origem e destino: VPN site-to-site (se sistemas estão em redes diferentes), firewall rules (whitelist de IPs da integração nos sistemas de destino), certificados TLS client (para mTLS), API keys/tokens com permissões mínimas, e database users com acesso restrito (apenas as tabelas e operações necessárias — SELECT sem DELETE). Testar cada conexão individualmente antes de qualquer implementação de fluxo — problemas de conectividade são a causa #1 de atraso em projetos de integração, e frequentemente dependem de terceiros com SLA próprio.

- **Pipeline de CI/CD**: Configurar o pipeline automatizado: lint e análise estática para cada push, testes unitários (transformações, validações), testes de integração com mocks dos sistemas externos (WireMock, LocalStack), build e publicação do artefato (container image, pacote de deploy), e deploy automático no ambiente de staging. Para projetos com múltiplos fluxos de integração, cada fluxo deve ter sua suite de testes independente — um fluxo quebrado não deve bloquear o deploy dos demais. GitHub Actions, GitLab CI, ou Jenkins são adequados.

- **Configuração de observabilidade**: Instalar e configurar a stack de observabilidade definida na Architecture antes de qualquer implementação de fluxo: agregador de logs (ELK, Loki, CloudWatch Logs) com parsing de log estruturado, coletor de métricas (Prometheus, CloudWatch Metrics) com métricas custom por fluxo, tracing distribuído (Jaeger, X-Ray) com propagação de correlation ID, e dashboards base no Grafana com painéis por fluxo (throughput, latência p50/p95/p99, taxa de erro, tamanho de DLQ). Ter a observabilidade pronta desde o Setup permite que o time identifique problemas durante o Build, não apenas no QA.

- **Dead letter queue e mecanismo de reprocessamento**: Configurar a DLQ para cada fluxo que usa comunicação assíncrona — mensagens que falharam após todos os retries devem ser encaminhadas para uma fila separada com metadados de diagnóstico (razão da falha, número de tentativas, timestamp, payload original). Implementar o mecanismo de reprocessamento: interface ou script que permite ao operador visualizar mensagens na DLQ, corrigir se necessário, e re-enfileirar para processamento. O mecanismo de DLQ deve estar funcional antes do Build — testar o caminho de erro é tão importante quanto testar o caminho de sucesso.

- **Variáveis de ambiente e secrets management**: Configurar todas as credenciais, tokens, API keys, connection strings e certificados como secrets gerenciados (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault, ou variáveis de ambiente criptografadas no CI/CD). NUNCA hardcoded no código, NUNCA em arquivo de configuração não-criptografado commitado no repositório. Cada ambiente deve ter seu próprio conjunto de secrets — a mesma variável de ambiente DATABASE_URL aponta para o banco de dev, staging ou produção dependendo do ambiente. Rotacionar credenciais deve ser possível sem redesploy da aplicação.

### Perguntas

1. O message broker e a plataforma de orquestração foram provisionados em ambientes separados (dev, staging, produção)? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
2. A infraestrutura está definida como código (Terraform/Pulumi) e versionada no repositório? [fonte: DevOps] [impacto: DevOps, Dev]
3. Todas as conexões com sistemas externos foram configuradas e testadas individualmente (VPN, firewall, certificados)? [fonte: DevOps, TI, Fornecedores] [impacto: Dev, DevOps, PM]
4. Os API keys/tokens têm permissões mínimas (least privilege) e estão armazenados como secrets gerenciados? [fonte: Segurança da Informação, DevOps] [impacto: Dev, DevOps]
5. O pipeline de CI/CD está configurado com lint, testes unitários, testes de integração com mocks e deploy automático? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
6. A stack de observabilidade (logs, métricas, tracing, dashboards) está configurada e funcional? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
7. O correlation ID está configurado para propagação entre todos os componentes do fluxo de integração? [fonte: Dev] [impacto: Dev, DevOps]
8. A DLQ está configurada para cada fluxo assíncrono com mecanismo de reprocessamento funcional? [fonte: Dev, DevOps] [impacto: Dev, Operações]
9. Os dashboards base de monitoramento por fluxo estão criados (throughput, latência, erros, DLQ size)? [fonte: DevOps, Dev] [impacto: Dev, DevOps, Operações]
10. O schema registry está configurado (se aplicável) com schemas iniciais publicados? [fonte: Dev, Arquiteto] [impacto: Dev]
11. Os ambientes de staging da integração estão conectados aos ambientes de homologação dos sistemas externos? [fonte: DevOps, TI, Fornecedores] [impacto: Dev, QA]
12. As variáveis de ambiente estão documentadas e cada ambiente tem seu conjunto isolado de configurações? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
13. O .gitignore exclui credenciais, secrets, e arquivos de configuração local? [fonte: Dev] [impacto: Dev]
14. O processo de rotação de credenciais foi testado (é possível trocar um token sem redesploy)? [fonte: DevOps, Segurança da Informação] [impacto: DevOps, Dev]
15. O pipeline de CI/CD foi testado end-to-end (push → build → test → deploy em staging)? [fonte: Dev, DevOps] [impacto: Dev, DevOps]

---

## Etapa 07 — Build

- **Implementação dos adaptadores de origem e destino**: Implementar a camada de comunicação com cada sistema externo — cliente HTTP/REST, cliente SOAP, conector de banco de dados, leitor/escritor de arquivo, produtor/consumidor de mensagens. Cada adaptador deve encapsular os detalhes do protocolo e expor uma interface limpa para a lógica de integração — se o sistema de origem mudar de SOAP para REST no futuro, apenas o adaptador muda, não o fluxo inteiro. Implementar retry, timeout, e circuit breaker em cada adaptador externo — chamadas a sistemas de terceiros falham, e o adaptador deve ser resiliente por design, não por adição posterior.

- **Implementação das transformações de dados**: Codificar as regras de transformação especificadas no mapeamento de-para — conversão de formatos, normalização, enriquecimento, validação. Cada transformação deve ser uma função pura (entrada → saída, sem efeitos colaterais) que pode ser testada unitariamente com dados reais extraídos dos ambientes de homologação. Dar atenção especial a: tratamento de caracteres especiais e encoding (o acento que vira ? no sistema de destino), conversão de datas e fusos horários (a meia-noite UTC é 21h de Brasília — um pedido feito às 23h aparece com data do dia seguinte?), e precisão numérica (arredondamento de valores monetários — R$ 10,005 arredonda para R$ 10,00 ou R$ 10,01?).

- **Implementação da orquestração de fluxos**: Para fluxos com múltiplos passos, implementar o orquestrador conforme os diagramas de sequência da Definition. Cada passo deve ser idempotente (executar duas vezes produz o mesmo resultado), com timeout configurado, retry em caso de falha transiente, e compensação em caso de falha definitiva. O estado do fluxo deve ser persistido a cada passo — se o orquestrador reiniciar, a instância do fluxo deve retomar de onde parou, não recomeçar do zero. Implementar dead letter para instâncias de fluxo que falharam em todos os retries — com informação suficiente para diagnóstico (qual passo falhou, qual o erro, qual o payload).

- **Implementação de idempotência**: Para cada fluxo que pode receber a mesma mensagem mais de uma vez (retry, reprocessamento, duplicação na origem), implementar verificação de idempotência: antes de processar, verificar se a operação já foi executada (por chave natural — ID do pedido, hash do payload, ou idempotency key gerada pelo produtor). Se já foi executada, retornar sucesso sem executar novamente. Armazenar a chave de idempotência com TTL (ex.: 24h) para não acumular infinitamente. Testar idempotência explicitamente — enviar a mesma mensagem duas vezes e verificar que o resultado é idêntico e que não há duplicação no destino.

- **Implementação de observabilidade no código**: Integrar logging estruturado, métricas e tracing em cada componente do fluxo. Para cada operação: logar início e fim com correlation ID, sistema de origem/destino, duração, resultado (sucesso/erro), e tamanho do payload (não o payload inteiro — evitar logar dados sensíveis). Emitir métricas de throughput (mensagens processadas/segundo), latência (tempo de processamento por mensagem), e erros (taxa de falha por tipo de erro). Propagar o correlation ID entre todos os sistemas — ele é a chave para rastrear uma operação do início ao fim quando algo dá errado.

- **Implementação de alertas**: Configurar alertas automáticos baseados nas métricas coletadas: taxa de erro acima de threshold (ex.: >5% nos últimos 5 minutos), latência acima do SLA (ex.: p95 > 30 segundos), fila de DLQ crescendo (mensagens acumulando sem reprocessamento), throughput caindo abruptamente (indica problema no sistema de origem ou na conectividade), e integração parada (zero mensagens processadas em janela esperada). Cada alerta deve ter runbook associado — documento que explica o que o alerta significa e quais ações tomar, escrito para operadores que não conhecem o código.

### Perguntas

1. Todos os adaptadores de sistemas externos foram implementados com retry, timeout e circuit breaker? [fonte: Dev] [impacto: Dev, QA]
2. As transformações de dados foram implementadas como funções puras e testadas unitariamente com dados reais? [fonte: Dev, QA] [impacto: Dev, QA]
3. O tratamento de encoding, datas/timezone e precisão numérica foi implementado e validado? [fonte: Dev, QA] [impacto: Dev, QA]
4. A orquestração de fluxos multi-step está implementada com idempotência, checkpoint de estado e compensação? [fonte: Dev] [impacto: Dev, QA]
5. A verificação de idempotência foi implementada e testada (mesma mensagem processada duas vezes = resultado idêntico)? [fonte: Dev, QA] [impacto: Dev, QA]
6. O logging estruturado com correlation ID está implementado em todos os componentes? [fonte: Dev] [impacto: Dev, DevOps]
7. As métricas de throughput, latência e taxa de erro estão sendo emitidas por fluxo? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
8. O tracing distribuído está funcionando e permite rastrear uma operação do início ao fim? [fonte: Dev, DevOps] [impacto: Dev, DevOps]
9. Os alertas foram configurados com thresholds definidos e runbooks associados? [fonte: Dev, DevOps] [impacto: DevOps, Operações]
10. O mascaramento de dados sensíveis nos logs foi implementado e verificado? [fonte: Dev, DPO] [impacto: Dev]
11. A DLQ está recebendo mensagens falhadas com metadados suficientes para diagnóstico? [fonte: Dev] [impacto: Dev, Operações]
12. O mecanismo de reprocessamento de DLQ foi testado end-to-end? [fonte: Dev, Operações] [impacto: Dev, Operações]
13. Os testes de integração com mocks dos sistemas externos estão cobrindo happy path e cenários de erro? [fonte: Dev, QA] [impacto: Dev, QA]
14. A migração de dados iniciais foi implementada e testada com volume representativo? [fonte: Dev, DBA] [impacto: Dev, QA, PM]
15. O código de cada fluxo está documentado com diagrama de sequência atualizado? [fonte: Dev] [impacto: Dev]

---

## Etapa 08 — QA

- **Testes end-to-end com sistemas reais (homologação)**: Executar cada fluxo de integração completo contra os ambientes de homologação dos sistemas reais — não apenas mocks. Verificar: dados chegam ao destino com transformação correta, campos obrigatórios preenchidos, formato adequado, e regras de negócio respeitadas. Testar com dados representativos de produção — dados de teste artificiais não revelam problemas de encoding, truncamento de campos longos, ou valores inesperados que existem nos dados reais. Documentar cada caso de teste com dados de entrada, resultado esperado, e resultado obtido.

- **Testes de cenários de erro e resiliência**: Simular TODOS os cenários de falha mapeados na Discovery: sistema de destino indisponível (desligar o endpoint de homologação e verificar retry + DLQ), dados inválidos na origem (enviar payload com campo obrigatório nulo, formato errado, valor fora da faixa), timeout (simular latência alta com proxy de delay), duplicatas (enviar mesma mensagem duas vezes e verificar idempotência), e falha parcial em fluxos multi-step (falhar propositalmente no passo 3 e verificar compensação dos passos 1 e 2). Cada cenário de erro que não é testado é um incidente em produção esperando para acontecer.

- **Testes de volume e performance**: Gerar carga equivalente ao volume de produção (pico, não média) e medir: throughput real (mensagens/segundo processadas), latência end-to-end (p50, p95, p99), consumo de recursos (CPU, memória, conexões), e comportamento sob backpressure (o que acontece quando o produtor gera mais rápido que o consumidor consegue processar). Comparar resultados com os SLAs definidos na Definition. Para integrações batch, medir o tempo total de execução com volume completo — um pipeline que processa 1.000 registros em 5 minutos pode levar 50 horas para processar 1 milhão se a complexidade é O(n²) em vez de O(n).

- **Validação de dados migrados**: Se houve migração de dados iniciais, validar os dados migrados no sistema de destino: contagem de registros (origem vs. destino — todos migraram?), integridade referencial (IDs de relacionamento são válidos no destino?), precisão de dados (valores numéricos, datas, textos com acentos — todos corretos?), e amostragem manual (selecionar N registros aleatórios e verificar campo a campo manualmente). Dados migrados com erro são particularmente perigosos porque ficam silenciosos até que alguém toma uma decisão de negócio baseada em dados errados.

- **Teste de observabilidade e alertas**: Verificar que toda a stack de observabilidade funciona em cenário real: provocar um erro e verificar que aparece nos logs com correlation ID correto, que a métrica de erro incrementa no dashboard, que o tracing mostra a cadeia de chamadas que levou ao erro, e que o alerta é disparado no canal correto dentro do SLA definido. Verificar também que os runbooks dos alertas são claros e acionáveis — dar o runbook para alguém que não conhece o sistema e pedir para seguir os passos.

- **Teste de rollback e disaster recovery**: Simular cenários de recovery: parar o message broker e reiniciar (mensagens em trânsito são preservadas?), parar o orquestrador e reiniciar (instâncias de fluxo retomam de onde pararam?), e reverter o deploy para versão anterior (a versão antiga é compatível com dados/schemas da versão nova?). Para integrações críticas, testar também o failover para região secundária (se aplicável) e medir o tempo real de recovery (RTO medido vs. RTO prometido).

### Perguntas

1. Todos os fluxos foram testados end-to-end contra ambientes de homologação dos sistemas reais? [fonte: QA, Dev] [impacto: QA, Dev]
2. Os testes usaram dados representativos de produção (não apenas dados artificiais de teste)? [fonte: QA, Operações, DBA] [impacto: QA, Dev]
3. Todos os cenários de erro mapeados na Discovery foram testados (indisponibilidade, dados inválidos, timeout, duplicatas)? [fonte: QA, Dev] [impacto: QA, Dev]
4. O comportamento de compensação em fluxos multi-step foi testado (falha no passo N, desfazer passos 1 a N-1)? [fonte: QA, Dev] [impacto: Dev, QA]
5. O teste de volume com carga de pico foi executado e os SLAs técnicos foram atendidos? [fonte: QA, Dev, DevOps] [impacto: Dev, DevOps]
6. A idempotência foi testada explicitamente (mesma mensagem processada duas vezes = sem duplicação no destino)? [fonte: QA, Dev] [impacto: Dev, QA]
7. Os dados migrados foram validados (contagem, integridade referencial, amostragem manual)? [fonte: QA, Operações, DBA] [impacto: Dev, QA, PM]
8. Os logs, métricas, tracing e alertas foram testados com cenário real de erro? [fonte: QA, DevOps] [impacto: Dev, DevOps]
9. Os runbooks dos alertas foram validados por alguém que NÃO é desenvolvedor? [fonte: Operações, QA] [impacto: Operações]
10. O rollback para versão anterior foi testado e a compatibilidade backward foi confirmada? [fonte: QA, DevOps] [impacto: Dev, DevOps]
11. O broker/orquestrador foi reiniciado sob carga e as mensagens/instâncias foram preservadas? [fonte: QA, DevOps] [impacto: DevOps, Dev]
12. O comportamento sob backpressure foi testado (produtor mais rápido que consumidor)? [fonte: QA, Dev] [impacto: Dev, Arquiteto]
13. Os rate limits dos sistemas de destino foram respeitados sob carga máxima? [fonte: QA, Dev, Fornecedores] [impacto: Dev]
14. O tempo de execução da migração de dados com volume completo foi medido e está dentro do prazo? [fonte: QA, Dev, DBA] [impacto: Dev, PM]
15. Todos os bugs encontrados no QA foram corrigidos e re-testados, sem workarounds aceitos? [fonte: Dev, QA] [impacto: Dev, QA]

---

## Etapa 09 — Launch Prep

- **Execução da migração de dados iniciais em produção**: Se há carga inicial a ser feita, executar a migração de dados em produção durante janela acordada — tipicamente fora do horário comercial para minimizar impacto nos sistemas de origem. Monitorar a execução em tempo real (registros processados, taxa de erro, tempo estimado de conclusão). Ter rollback preparado — se a migração corrupta dados no destino, como reverter? Após a conclusão, executar as validações definidas no QA (contagem, integridade referencial, amostragem) nos dados de produção, não apenas assumir que "se funcionou em homologação, vai funcionar em produção".

- **Validação de conectividade em produção**: Testar cada conexão com os sistemas de produção individualmente — a conectividade que funciona em homologação pode não funcionar em produção por diferenças de rede (firewall rules diferentes, VPN com routing diferente, certificados diferentes). Fazer um smoke test leve de cada fluxo (enviar um registro de teste e verificar que chega ao destino corretamente) sem impactar dados reais de produção. Se possível, usar feature flag para ativar cada fluxo gradualmente — primeiro apenas lendo da origem (sem escrever no destino), depois escrevendo em modo shadow (escreve mas não usa), depois ativando completamente.

- **Plano de cutover detalhado**: Documentar a sequência exata de ações para ativar a integração em produção: quem ativa cada componente, em qual ordem, qual o critério de sucesso de cada passo, e qual a ação se algo falhar. Se a integração substitui um processo manual existente, definir o período de operação em paralelo (integração automática rodando simultaneamente com o processo manual para comparar resultados) antes de desligar o processo manual. Definir o point-of-no-return — após qual passo não é mais possível reverter para o processo anterior sem perda de dados.

- **Treinamento da equipe de operações**: Treinar a equipe que vai monitorar e operar as integrações no dia a dia — não apenas os desenvolvedores. O treinamento deve cobrir: como ler o dashboard de saúde das integrações, o que cada alerta significa e qual ação tomar (seguir o runbook), como acessar e diagnosticar mensagens na DLQ, como re-processar mensagens falhadas, e quando escalar para o time de desenvolvimento. Simular cenários de falha durante o treinamento — operador recebe alerta simulado e segue o runbook na prática.

- **Certificados e credenciais com validade**: Verificar a data de expiração de todos os certificados TLS, tokens OAuth2, API keys e credenciais de banco de dados usados pela integração. Certificados que expiram silenciosamente são a causa mais comum de falha catastrófica em integrações em produção — tudo funciona perfeitamente por meses até o certificado expirar e TODOS os fluxos param simultaneamente. Configurar alertas de expiração com pelo menos 30 dias de antecedência e definir responsável pela renovação.

- **Plano de rollback e contingência**: Documentar o plano de rollback: como desativar a integração rapidamente (kill switch), como reverter para o processo manual anterior, como re-sincronizar dados que ficaram dessincronizados durante a falha, e quem tem autoridade para tomar a decisão de rollback. Definir critérios claros de acionamento — taxa de erro acima de X%, latência acima de Y, ou qualquer indicação de corrupção de dados. O plano deve ser exequível em menos de 30 minutos para integrações críticas.

### Perguntas

1. A migração de dados iniciais em produção foi executada com sucesso e validada (contagem, integridade, amostragem)? [fonte: Dev, DBA, Operações] [impacto: Dev, QA, PM]
2. Todas as conexões com sistemas de produção foram testadas individualmente com smoke test? [fonte: DevOps, Dev] [impacto: Dev, DevOps]
3. O plano de cutover está documentado com sequência, responsáveis, critérios de sucesso e ações de fallback? [fonte: PM, Dev, Operações] [impacto: PM, Dev, Operações]
4. O período de operação em paralelo (integração + processo manual) foi definido e acordado? [fonte: Operações, Diretoria] [impacto: PM, Operações]
5. A equipe de operações foi treinada em monitoramento, diagnóstico de DLQ, reprocessamento e escalonamento? [fonte: Dev, PM] [impacto: Operações]
6. Cenários de falha foram simulados durante o treinamento e os operadores conseguiram seguir os runbooks? [fonte: Dev, QA, Operações] [impacto: Operações]
7. A validade de todos os certificados, tokens e credenciais foi verificada e alertas de expiração configurados? [fonte: DevOps, Segurança da Informação] [impacto: DevOps, Operações]
8. O plano de rollback está documentado com kill switch, critérios de acionamento e responsável autorizado? [fonte: Dev, Operações, Diretoria] [impacto: PM, Dev, Operações]
9. O monitoramento de disponibilidade e os alertas estão todos ativos e testados? [fonte: DevOps, Dev] [impacto: DevOps, Operações]
10. Os feature flags para ativação gradual estão implementados (se aplicável)? [fonte: Dev] [impacto: Dev, PM]
11. Todos os stakeholders foram notificados sobre data, horário e impactos esperados do go-live? [fonte: PM, Diretoria] [impacto: PM]
12. O processo manual anterior está documentado para que possa ser reativado como fallback? [fonte: Operações] [impacto: Operações, PM]
13. A janela de cutover foi escolhida estrategicamente (fora do pico, horário com time disponível)? [fonte: Operações, TI] [impacto: PM, DevOps]
14. O capacity planning do cloud/infra está validado para suportar a carga real de produção? [fonte: DevOps, Arquiteto] [impacto: DevOps, PM]
15. A lista de contatos de emergência de todos os fornecedores/times de sistemas está atualizada e acessível? [fonte: PM, TI] [impacto: PM, Operações]

---

## Etapa 10 — Go-Live

- **Ativação da integração em produção**: Executar o cutover conforme o plano documentado — ativar cada fluxo na ordem definida, verificar o critério de sucesso de cada um, e avançar para o próximo. Se algum fluxo falhar na ativação, seguir o procedimento de fallback antes de continuar. Manter comunicação ativa com os donos de todos os sistemas envolvidos durante o cutover — eles podem perceber impacto nos seus sistemas (aumento de carga, registros novos aparecendo) e precisam saber que é esperado. Logar o timestamp de ativação de cada fluxo para referência posterior.

- **Monitoramento intensivo das primeiras 24-48h**: Monitorar ativamente todos os dashboards de integração nas primeiras 48h: throughput real vs. esperado (se está processando 50% do volume esperado, algo está errado), latência vs. SLA (picos de latência nas primeiras horas podem indicar cold start ou cache miss), taxa de erro (qualquer erro acima de 1% precisa de investigação imediata), tamanho da DLQ (deve ser próximo de zero — DLQ crescendo indica problema sistemático), e feedback dos usuários dos sistemas de destino (dados chegando? corretos? no tempo esperado?). Ter um dev e um operador de plantão durante este período.

- **Validação de dados em produção**: Comparar dados processados pela integração com o resultado esperado — selecionar N registros processados nas primeiras horas e verificar campo a campo no sistema de destino. Comparar com o processo manual anterior (se existia) — os resultados são idênticos? Se houver divergências, investigar imediatamente — pode ser bug de transformação que não apareceu em homologação devido a diferenças de dados. Para integrações financeiras ou regulatórias, essa validação é obrigatória e deve ser documentada como evidência de compliance.

- **Desativação do processo manual**: Após o período de operação em paralelo (tipicamente 1-2 semanas), com validação de que a integração está produzindo resultados corretos e estáveis, desativar o processo manual anterior. Esta decisão deve ser formalizada — não basta "parar de fazer manualmente". Documentar a data de desativação, o responsável pela decisão, e as evidências de validação que justificam a desativação. Manter a capacidade de reativar o processo manual por mais 2-4 semanas como última contingência.

- **Handoff e documentação de operação**: Entregar formalmente ao time de operações: acesso a todos os dashboards de monitoramento com permissões adequadas, runbooks atualizados com os aprendizados do go-live, documentação de arquitetura com diagramas de sequência e decisões de design, inventário de credenciais/certificados com datas de expiração, e contato de suporte técnico com SLA. A documentação mais importante é o troubleshooting guide — documento organizado por sintoma ("mensagens acumulando na DLQ", "latência acima do SLA", "sistema X retornando 401") com passos de diagnóstico e resolução.

- **Revisão pós-go-live e ajustes**: Após 1-2 semanas de operação estável, realizar revisão formal: métricas reais vs. projetadas (volume, latência, taxa de erro), custos reais vs. orçados (cloud, licenças, operação), incidentes ocorridos e lições aprendidas, e ajustes necessários (re-dimensionamento de infra, ajuste de thresholds de alertas, melhoria de runbooks). Esta revisão é o encerramento formal do projeto e a transição para operação contínua — a partir daqui, mudanças na integração seguem o processo de change request definido no Alignment.

### Perguntas

1. Todos os fluxos de integração foram ativados em produção conforme o plano de cutover? [fonte: Dev, Operações] [impacto: Dev, Operações, PM]
2. O monitoramento intensivo das primeiras 48h foi executado com dev e operador de plantão? [fonte: Dev, DevOps, Operações] [impacto: Dev, DevOps, Operações]
3. O throughput, latência e taxa de erro reais estão dentro dos SLAs definidos? [fonte: DevOps, Dev] [impacto: Dev, DevOps, PM]
4. A DLQ está próxima de zero ou as mensagens falhadas foram investigadas e reprocessadas? [fonte: Dev, Operações] [impacto: Dev, Operações]
5. A validação de dados em produção foi executada com amostragem e comparação campo a campo? [fonte: QA, Operações] [impacto: QA, Dev]
6. O feedback dos usuários dos sistemas de destino confirma que os dados estão corretos e no prazo esperado? [fonte: Operações, Usuários] [impacto: PM, Dev]
7. O período de operação em paralelo (integração + manual) foi executado com resultados comparados? [fonte: Operações] [impacto: PM, Operações]
8. A desativação do processo manual foi formalizada com data, responsável e evidências de validação? [fonte: Operações, Diretoria] [impacto: PM, Operações]
9. O handoff formal ao time de operações foi realizado com entrega de acessos, runbooks e documentação? [fonte: Dev, PM] [impacto: PM, Operações]
10. O aceite formal de entrega foi obtido do cliente (documentado por escrito)? [fonte: Diretoria] [impacto: PM]
11. A revisão pós-go-live foi realizada com métricas reais vs. projetadas e lições aprendidas? [fonte: PM, Dev, Operações] [impacto: PM, Dev]
12. Os thresholds de alertas foram ajustados com base nos dados reais de produção? [fonte: DevOps, Dev] [impacto: DevOps, Operações]
13. O contrato de suporte pós-go-live foi ativado com SLA comunicado? [fonte: Diretoria, PM] [impacto: PM, Dev]
14. O inventário de credenciais/certificados com datas de expiração foi entregue com alertas configurados? [fonte: DevOps] [impacto: DevOps, Operações]
15. O troubleshooting guide foi atualizado com cenários reais encontrados durante o go-live? [fonte: Dev, Operações] [impacto: Operações]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"São só dois sistemas, é simples"** — O cliente diz dois sistemas, mas a investigação revela que o "ERP" na verdade são 3 módulos com interfaces diferentes, o "CRM" tem versão desatualizada com API incompleta, e há um terceiro sistema "que só consulta" mas também precisa de dados sincronizados. Projetos de integração que parecem simples na Inception se revelam complexos na Discovery. Nunca estimar sem mapear o landscape completo.
- **"A gente tem API pra tudo"** — "Ter API" pode significar REST documentada com Swagger, endpoint SOAP sem WSDL, stored procedure que alguém chamou de API, ou planilha exportada pelo sistema. Verificar o que "API" significa para cada sistema antes de aceitar como premissa.
- **"O volume é baixo, não precisa de infra robusta"** — Volume "baixo" hoje pode ser alto amanhã (Black Friday, fechamento de ano, aquisição de empresa). E mesmo volume baixo com dados sensíveis (pagamentos, dados pessoais) precisa de segurança, auditoria e resiliência robustas. Volume não define a criticidade — SLA e sensibilidade dos dados definem.

### Etapa 02 — Discovery

- **"O mapeamento de dados é direto, campo por campo"** — Em sistemas reais, o mapeamento nunca é direto. Campos com mesmo nome têm semânticas diferentes ("status" no sistema A ≠ "status" no sistema B), formatos variam (data, encoding, decimal separator), e campos obrigatórios no destino não existem na origem. O mapeamento de-para é o artefato mais subestimado em projetos de integração.
- **"O sistema de destino aceita qualquer coisa"** — Nenhum sistema aceita qualquer coisa. Restrições de tipo, tamanho, formato, unicidade e integridade referencial existem — e quando violadas, a rejeição pode ser silenciosa (dado descartado sem erro) ou ruidosa (exception que para o fluxo inteiro). Testar com dados reais na Discovery, não apenas perguntar.
- **"A documentação da API está atualizada"** — A documentação da API está quase certamente desatualizada. Campos que foram adicionados, removidos ou que mudaram de comportamento sem atualização da documentação são a norma, não a exceção. Validar cada campo da documentação contra a API real em ambiente de homologação.

### Etapa 03 — Alignment

- **"Se der erro, manda e-mail pro suporte"** — E-mail como canal de alerta para integração crítica significa que o problema será visto quando alguém ler o e-mail — horas depois. Integrações críticas precisam de alertas em tempo real (Slack, PagerDuty, SMS) com SLA de resposta definido. E-mail é aceitável apenas para alertas informativos de baixa severidade.
- **"A gente alinha com o fornecedor quando precisar"** — Fornecedores de sistemas têm seu próprio backlog e prioridades. Se o time de integração precisa que o fornecedor configure acesso, crie endpoint, ou corrija bug — isso tem prazo do fornecedor, não do projeto. Alinhar com TODOS os fornecedores na Inception, não durante o Build.
- **"Backward compatibility não é necessária, todo mundo atualiza junto"** — Em integrações com múltiplos sistemas, "todo mundo atualiza junto" nunca acontece. Cada sistema tem seu ciclo de release e janela de manutenção. A integração precisa funcionar com N-1 de cada sistema durante o período de transição.

### Etapa 04 — Definition

- **De-para feito em reunião, não documentado** — Mapeamento de dados "acordado verbalmente" resulta em implementação baseada na memória do dev, que invariavelmente difere da memória do analista de negócio. De-para precisa ser documento formal, revisado e assinado.
- **"Os cenários de erro são poucos, a gente trata no código"** — Cenários de erro em integração são SEMPRE mais numerosos que cenários de sucesso. Para cada campo, para cada sistema, para cada conexão — o que acontece se falhar? Documentar na Definition é obrigatório.
- **SLAs definidos como "rápido" ou "quase real-time"** — SLA sem número é SLA infinito. "Rápido" pode significar 1 segundo para quem pede e 1 hora para quem implementa. Definir em milissegundos ou segundos, com percentis (p95, p99), para evitar conflito de expectativas.

### Etapa 05 — Architecture

- **"Kafka porque é enterprise e escalável"** — Kafka é a escolha certa para alto throughput, event log, e múltiplos consumidores. Mas para integração simples de dois sistemas com 100 mensagens/hora, Kafka é overkill que adiciona complexidade operacional desnecessária (ZooKeeper/KRaft, partições, consumer groups). RabbitMQ ou SQS resolvem com fração da complexidade.
- **"Integração síncrona porque é mais simples"** — Integração síncrona é mais simples de implementar, mas cria acoplamento temporal — se o sistema de destino está lento, o sistema de origem fica lento; se está fora, o sistema de origem falha. Para fluxos tolerantes a latência de segundos, assíncrono é quase sempre a escolha correta.
- **"A gente usa o banco de dados como fila de mensagens"** — Padrão "polling table" (tabela com flag "processado" que a integração consulta periodicamente) é simples de implementar mas não escala, não tem garantia de ordering, gera lock contention, e polui o schema do sistema de origem. Usar message broker adequado.

### Etapa 06 — Setup

- **Credenciais de produção usadas no desenvolvimento** — Dev testando com credenciais de produção pode alterar dados reais, disparar processos reais, ou atingir rate limits que afetam a operação. Ambientes isolados com credenciais específicas são obrigatórios.
- **"Observabilidade a gente configura depois do build"** — Sem observabilidade desde o Setup, o dev implementa fluxos sem visibilidade do que está acontecendo. Bugs são descobertos por "não funciona" em vez de "o log mostra erro 422 no passo 3". Dashboards e logs prontos antes do primeiro fluxo implementado.
- **"VPN com o fornecedor a gente configura na semana do go-live"** — Configuração de VPN site-to-site depende de equipes de rede de ambas as empresas, tem processo de aprovação, e frequentemente leva 2-4 semanas. Iniciar na Launch Prep é tarde demais — iniciar no Setup.

### Etapa 07 — Build

- **Transformações de dados sem testes unitários** — Transformação que "parece funcionar" com dados de teste pode falhar com dados reais (campo com 500 caracteres quando o teste usou 10, data em formato inesperado, valor negativo quando o teste usou apenas positivos). Cada transformação deve ter suite de testes com dados realistas.
- **"Log de tudo para facilitar o debug"** — Logar payload completo de cada mensagem gera volume de logs insustentável (custo, performance, storage) e potencialmente viola LGPD (dados pessoais nos logs). Logar metadados (IDs, timestamps, tamanho, resultado) — logar payload apenas em modo debug, não em produção.
- **Happy path implementado, error path "deixa pro QA achar"** — Em integração, o error path é usado com mais frequência que parece. Sistemas ficam indisponíveis, dados vêm errados, rede falha. Implementar retry, circuit breaker, DLQ e compensação durante o Build, não como correção pós-QA.

### Etapa 08 — QA

- **"Testou com mocks, tá validado"** — Mocks simulam o comportamento esperado, não o comportamento real. O sistema real tem latência variável, retorna erros inesperados, tem rate limits, e se comporta diferente com carga. Teste com mock é necessário no CI — mas insuficiente como validação final. Teste com sistema real em homologação é obrigatório.
- **QA com 10 registros quando produção terá 10.000** — Performance é não-linear. Pipeline que processa 10 registros em 1 segundo pode levar 100 horas para processar 10.000 se houver N+1 query, lock contention, ou memory leak. Teste de volume com carga representativa de produção é obrigatório.
- **"DLQ vazia no teste, então tá funcionando"** — DLQ vazia no teste significa apenas que o happy path funciona. Os cenários de erro que populam a DLQ precisam ser testados explicitamente — enviar dados inválidos, simular timeout, duplicar mensagens. Se a DLQ nunca foi populada no teste, ela provavelmente não foi testada.

### Etapa 09 — Launch Prep

- **"A gente liga a integração e desliga o processo manual no mesmo dia"** — Sem período de operação em paralelo, não há como validar que a integração produz os mesmos resultados que o processo manual. Se a integração estiver errada, os dados de negócio já foram corrompidos. Operação em paralelo por 1-2 semanas é o padrão mínimo para integrações críticas.
- **Treinamento apenas para o time de dev** — Quem vai operar a integração no dia a dia não é o dev — é o NOC, a operação, ou o time de suporte. Se eles não conhecem os dashboards, não sabem ler os alertas, e não sabem reprocessar a DLQ, vão escalar tudo para o dev. Treinar operadores é obrigatório.
- **Certificados verificados "quando configuramos"** — Certificados TLS e tokens OAuth2 têm data de expiração. Se ninguém monitora, a integração vai parar silenciosamente quando o certificado expirar. Alertas de expiração com 30 dias de antecedência são obrigatórios.

### Etapa 10 — Go-Live

- **Go-live na sexta à tarde antes do fechamento mensal** — Se a integração falhar no fim de semana durante o fechamento mensal, o impacto no negócio é máximo e o time não está disponível. Go-live em dia útil, no início da semana, com buffer de pelo menos 3 dias antes de qualquer evento crítico de negócio.
- **"Os dados estão passando, projeto encerrado"** — Dados passando não significa dados corretos. Validação de amostragem em produção é obrigatória nas primeiras semanas. Dados errados sendo processados silenciosamente é pior que dados não sendo processados — porque geram decisões de negócio incorretas.
- **Processo manual desligado sem formalização** — Se a integração falhar 2 semanas depois e o processo manual foi desligado sem documentação de como reativá-lo, a operação fica sem alternativa. Manter capacidade de reativar o processo manual por pelo menos 4 semanas e formalizar a desativação com aprovação.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é integração/middleware** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "Na verdade precisamos reconstruir o sistema de origem" | Projeto de desenvolvimento de software, não integração | Reclassificar para web-app ou saas |
| "Queremos uma tela para os operadores gerenciarem os dados" | Aplicação com frontend, não middleware puro | Adicionar componente de web-app ao escopo ou reclassificar |
| "O sistema de destino ainda não existe, vamos construir junto" | Projeto de desenvolvimento + integração | Separar em dois projetos ou reclassificar como plataforma |
| "Precisamos de um data warehouse para analytics" | Projeto de dados/BI, não integração operacional | Reclassificar para data-platform ou analytics |
| "É basicamente um dispositivo que coleta dados de sensores" | Projeto IoT/embarcado, não middleware | Reclassificar para embedded-iot |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "Não temos acesso à API do sistema X" | 01 | Integração impossível sem acesso ao sistema | Resolver acesso antes de qualquer estimativa |
| "O fornecedor do ERP não coopera" | 01 | Dependência crítica de terceiro hostil | Escalar para nível executivo ou replanejar sem essa integração |
| "Não sabemos o formato dos dados do sistema legado" | 02 | Mapeamento impossível sem conhecer a origem | Investir em spike técnico de investigação antes de estimar |
| "Os ambientes de homologação estão desatualizados" | 03 | QA inválido — homologação não representa produção | Exigir atualização dos ambientes antes de iniciar Build |
| "Não temos documentação da API, mas o dev antigo sabe" | 02 | Dependência de pessoa — se sair, conhecimento perdido | Documentar antes de começar — incluir como pré-requisito |
| "O sistema de origem não tem como notificar mudanças" | 02 | Sem eventos nem webhooks, a integração só funciona por polling | Avaliar impacto de polling no SLA e no sistema de origem |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "São 15 sistemas para integrar" | 01 | Complexidade exponencial — cada sistema adicional multiplica cenários de erro | Priorizar e fazer em fases — nunca todos de uma vez |
| "O sistema legado roda COBOL no mainframe" | 02 | Integração com mainframe exige skills específicos (MQ Series, CICS, flat files) | Verificar se o time tem a expertise necessária |
| "Os dados mudam retroativamente (correção de lançamento)" | 02 | Integração precisa lidar com updates e deletes, não apenas inserts | Definir estratégia de change data capture (CDC) |
| "Cada filial usa uma versão diferente do sistema" | 02 | Múltiplas versões = múltiplas interfaces = múltiplos adaptadores | Mapear todas as versões e avaliar se é viável unificar antes de integrar |
| "O SLA é real-time com zero perda de dados" | 04 | SLA extremo exige arquitetura de alta disponibilidade com custo correspondente | Calcular custo da infra necessária e apresentar ao cliente |
| "A integração precisa funcionar 24/7/365 sem manutenção" | 03 | Zero downtime exige blue-green deployment, failover automático e multi-region | Dimensionar infra e custo para alta disponibilidade |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Problema de negócio identificado com critério de sucesso mensurável (pergunta 1)
- Landscape completo de sistemas mapeado (pergunta 2)
- Governança e responsáveis técnicos de cada sistema identificados (pergunta 3)
- Criticidade e SLA esperado definidos por fluxo (pergunta 6)
- Acesso a ambientes de homologação confirmado (pergunta 10)

### Etapa 02 → 03

- Interfaces de todos os sistemas documentadas com precisão (pergunta 1)
- Mapeamento de dados campo a campo concluído (pergunta 2)
- Cenários de erro mapeados com ação definida (pergunta 4)
- Volume medido com dados reais (pergunta 9)

### Etapa 03 → 04

- Responsabilidades entre times formalizadas (pergunta 1)
- Contratos de interface acordados e versionados (pergunta 2)
- Estratégia de tratamento de erros alinhada (pergunta 3)
- SLA operacional definido e aceito (pergunta 7)

### Etapa 04 → 05

- Especificação completa de cada fluxo aprovada (pergunta 1)
- Schemas de eventos/mensagens definidos (pergunta 2)
- SLAs técnicos especificados com números (pergunta 5)
- Diagramas de sequência produzidos e validados (pergunta 6)
- Documentação revisada por todos os stakeholders (pergunta 15)

### Etapa 05 → 06

- Padrão síncrono/assíncrono definido por fluxo (pergunta 1)
- Message broker e plataforma de orquestração escolhidos (perguntas 2 e 3)
- Stack de observabilidade definida (pergunta 5)
- Segurança e compliance definidos por fluxo (pergunta 7)
- Custos mensais calculados (pergunta 10)

### Etapa 06 → 07

- Infraestrutura provisionada em ambientes separados (pergunta 1)
- Conectividade com sistemas externos testada (pergunta 3)
- Stack de observabilidade funcional (pergunta 6)
- DLQ e mecanismo de reprocessamento configurados (pergunta 8)
- Pipeline de CI/CD testado end-to-end (pergunta 15)

### Etapa 07 → 08

- Adaptadores implementados com retry, timeout e circuit breaker (pergunta 1)
- Transformações testadas unitariamente com dados reais (pergunta 2)
- Idempotência implementada e testada (pergunta 5)
- Observabilidade integrada no código (perguntas 6, 7 e 8)

### Etapa 08 → 09

- Testes end-to-end com sistemas reais executados (pergunta 1)
- Todos os cenários de erro testados (pergunta 3)
- Teste de volume com carga de pico executado e SLAs atendidos (pergunta 5)
- Idempotência validada explicitamente (pergunta 6)
- Rollback testado (pergunta 10)

### Etapa 09 → 10

- Migração de dados iniciais executada e validada (pergunta 1)
- Conectividade com produção testada (pergunta 2)
- Plano de cutover documentado (pergunta 3)
- Operadores treinados (pergunta 5)
- Plano de rollback documentado com critérios (pergunta 8)

### Etapa 10 → Encerramento

- Todos os fluxos ativados em produção (pergunta 1)
- Monitoramento intensivo de 48h executado (pergunta 2)
- SLAs atendidos em produção (pergunta 3)
- Validação de dados em produção executada (pergunta 5)
- Aceite formal obtido (pergunta 10)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de integração/middleware. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 ETL/Sync | V2 API Gateway | V3 Orquestração | V4 Event-Driven | V5 Legada/Adaptador |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 3 | 2 | 3 |
| 02 Discovery | 4 | 2 | 4 | 3 | 5 |
| 03 Alignment | 2 | 2 | 3 | 3 | 3 |
| 04 Definition | 4 | 2 | 5 | 4 | 5 |
| 05 Architecture | 2 | 3 | 4 | 4 | 3 |
| 06 Setup | 2 | 3 | 3 | 3 | 3 |
| 07 Build | 3 | 3 | 5 | 4 | 5 |
| 08 QA | 3 | 2 | 4 | 3 | 4 |
| 09 Launch Prep | 3 | 2 | 3 | 2 | 3 |
| 10 Go-Live | 2 | 1 | 3 | 2 | 3 |
| **Total relativo** | **27** | **22** | **37** | **30** | **37** |

**Observações por variante:**

- **V1 ETL/Sync**: Pico na Discovery e Definition (mapeamento de dados campo a campo é o maior esforço) e Launch Prep (migração de dados iniciais pode levar dias). Build é relativamente leve porque as transformações são diretas — a complexidade está no volume e na qualidade dos dados, não na lógica.
- **V2 API Gateway**: O mais leve de todas as variantes — sem lógica de negócio complexa, sem transformações pesadas, sem orquestração. O esforço está na Architecture (segurança, rate limiting, versionamento de APIs) e Setup (configuração de gateway, políticas de acesso). Projetos de API Gateway que ficam pesados geralmente são orquestrações disfarçadas.
- **V3 Orquestração**: O mais pesado junto com V5 — Definition e Build são os maiores porque envolvem lógica de negócio distribuída com múltiplos pontos de falha, compensação, e estado persistente. QA é pesado porque cada cenário de falha em cada passo precisa ser testado.
- **V4 Event-Driven**: Pico na Architecture (design de eventos, schema registry, garantias de entrega) e Definition (schema de eventos, estratégia de evolução, idempotência). Build é moderado porque consumidores são relativamente simples — a complexidade está no design, não na implementação.
- **V5 Legada/Adaptador**: Empatado como mais pesado — Discovery é o pico porque investigar interfaces de sistemas legados sem documentação consome semanas de spike técnico. Build é pesado porque adaptar formatos arcaicos (positional files, EDI, COBOL copybooks) exige parsing custom que não tem biblioteca pronta.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Integração puramente síncrona, sem mensageria (Etapa 05, pergunta 1) | Etapa 05: perguntas 2 e 12 (broker, schema registry). Etapa 06: perguntas 1 (broker), 8 (DLQ), 10 (schema registry). Etapa 07: pergunta 11 (DLQ). Etapa 08: pergunta 12 (backpressure). |
| Sem migração de dados iniciais (Etapa 04, pergunta 8) | Etapa 04: perguntas 12 e 14 (volume e tempo de migração). Etapa 07: pergunta 14 (implementação de migração). Etapa 08: perguntas 7 e 14 (validação e tempo de migração). Etapa 09: pergunta 1 (execução de migração em produção). |
| Integração batch única (um sistema → outro, sem orquestração) | Etapa 04: perguntas 6 e 7 (diagramas de sequência complexos, compensação). Etapa 05: perguntas 3 e 9 (plataforma de orquestração, escalabilidade horizontal). Etapa 07: pergunta 4 (orquestração multi-step). |
| Sem requisito de compliance/auditoria (Etapa 01, pergunta 7) | Etapa 02: pergunta 7 (requisitos de auditoria). Etapa 05: pergunta 8 (mascaramento de dados). Etapa 07: pergunta 10 (mascaramento nos logs). |
| Sistemas acessíveis na mesma rede, sem VPN (Etapa 01, pergunta 8) | Etapa 06: pergunta 3 (conectividade VPN/firewall — apenas parte de rede). Etapa 09: pergunta 7 (certificados de VPN). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Dados sensíveis identificados — PII, financeiros (Etapa 01, pergunta 7) | Etapa 05: perguntas 7 e 8 (segurança e mascaramento) se tornam gates. Etapa 07: pergunta 10 (mascaramento nos logs) se torna gate. Etapa 08: verificação de compliance se torna obrigatória. |
| Integração substitui processo manual existente (Etapa 01, pergunta 9) | Etapa 04: pergunta 8 (migração de dados) se torna obrigatória. Etapa 09: pergunta 4 (período de operação em paralelo) se torna gate. Etapa 10: pergunta 7 (comparação com processo manual) se torna gate. |
| SLA de real-time ou near-real-time (Etapa 01, pergunta 5) | Etapa 05: pergunta 1 (assíncrono quase certamente necessário). Etapa 05: perguntas 4 e 9 (resiliência e escalabilidade) se tornam críticas. Etapa 06: stack de observabilidade com latência de detecção em segundos se torna obrigatória. |
| Sistema legado sem API documentada (Etapa 02, pergunta 1) | Etapa 02: spike técnico de investigação se torna pré-requisito antes de estimar. Etapa 04: especificação do fluxo pode exigir engenharia reversa. Etapa 07: build do adaptador legado se torna o maior risco do cronograma. |
| Múltiplos fornecedores envolvidos (Etapa 01, pergunta 3) | Etapa 03: pergunta 1 (responsabilidades entre times/fornecedores) se torna gate. Etapa 06: pergunta 3 (conectividade com cada fornecedor) se torna bloqueadora — cada VPN/firewall tem seu prazo. Etapa 09: pergunta 15 (contatos de emergência de fornecedores) se torna obrigatória. |
| Volume >1 milhão de registros/dia (Etapa 01, pergunta 4) | Etapa 05: pergunta 2 (broker adequado para throughput) se torna crítica. Etapa 05: pergunta 9 (escalabilidade horizontal) se torna gate. Etapa 08: pergunta 5 (teste de volume com carga de pico) se torna gate. Etapa 10: pergunta 12 (ajuste de thresholds) se torna obrigatória. |
