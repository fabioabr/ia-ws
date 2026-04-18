---
title: "Sistema Embarcado / IoT — Blueprint"
description: "Firmware, software embarcado ou aplicação edge. Dispositivos conectados, telemetria, OTA updates, protocolos IoT (MQTT, CoAP) e integração com plataforma cloud."
category: project-blueprint
type: embedded-iot
status: rascunho
created: 2026-04-13
---

# Sistema Embarcado / IoT

## Descrição

Firmware, software embarcado ou aplicação edge. Dispositivos conectados, telemetria, OTA updates, protocolos IoT (MQTT, CoAP) e integração com plataforma cloud.

> **Convenção de roles nas perguntas:**
> - `[fonte: ...]` — quem o cliente pode procurar internamente para ajudar a chegar na resposta
> - `[impacto: ...]` — qual role do time é mais afetado pela resposta e precisa prestar atenção

---

## Variantes

Nem todo sistema embarcado é igual. A variante define quais etapas são mais pesadas, quais perguntas ganham ou perdem relevância, e quais stacks fazem mais sentido.

### V1 — Sensor Node / Telemetria

Dispositivo com função primária de coletar dados de sensores (temperatura, umidade, pressão, vibração, GPS) e transmiti-los periodicamente para uma plataforma cloud. Hardware tipicamente de baixo custo e baixo consumo, operando por bateria ou energy harvesting. O firmware é relativamente simples — leitura de sensor, empacotamento de dados, envio via protocolo leve (MQTT, CoAP, LoRaWAN). O foco é autonomia de bateria, confiabilidade de transmissão em ambientes adversos, e custo unitário para viabilizar deploy em escala (centenas a milhares de unidades). Exemplos: monitoramento ambiental em agro, sensores industriais de vibração, rastreadores de ativos logísticos.

### V2 — Gateway / Edge Computing

Dispositivo intermediário entre sensor nodes e a nuvem, com capacidade de processamento local (filtragem, agregação, inferência leve). Roda Linux embarcado (Yocto, Buildroot, Raspberry Pi OS) e gerencia a comunicação com múltiplos dispositivos via protocolos de campo (BLE, Zigbee, Modbus, CAN). O foco é processamento edge para reduzir volume de dados enviados à nuvem, resiliência em caso de perda de conectividade (store-and-forward), e gerenciamento remoto do próprio gateway (OTA, logs, diagnóstico). Exemplos: gateway industrial coletando dados de sensores de chão de fábrica, hub residencial de automação, concentrador de dados em operação agrícola.

### V3 — Atuador / Dispositivo de Controle

Dispositivo que, além de coletar dados, executa ações no mundo físico — aciona relés, controla válvulas, ajusta motores, dispara alarmes. Exige firmware com lógica de controle em tempo real (frequentemente com RTOS), comunicação bidirecional confiável com a plataforma cloud ou gateway local, e mecanismos de segurança críticos (fail-safe, watchdog, limites operacionais hardcoded). O foco é latência de comando, segurança operacional e certificações de produto. Exemplos: controlador de irrigação inteligente, sistema de dosagem industrial, dispositivo de automação predial (HVAC), fechadura eletrônica conectada.

### V4 — Wearable / Dispositivo Pessoal

Dispositivo vestível ou portátil com interação direta com o usuário — display, LEDs, botões, vibração, speaker. Restrições severas de consumo de energia, tamanho físico e ergonomia. O firmware precisa gerenciar interface com o usuário, conectividade BLE com app mobile (companion app), e processamento local de dados biométricos ou de movimento. O foco é experiência do usuário no hardware, duração de bateria, e sincronização confiável com o app. Exemplos: pulseira fitness, crachá inteligente com localização indoor, dispositivo de segurança pessoal, sensor médico vestível.

### V5 — Produto Conectado com OTA

Produto de hardware com ciclo de vida longo (anos) que precisa receber atualizações de firmware remotamente (OTA — Over-The-Air). Pode ser qualquer combinação dos tipos anteriores, mas a complexidade adicional está na infraestrutura de atualização segura — assinatura de firmware, rollback automático em caso de falha, versionamento, deploy gradual (canary release por frota), e monitoramento pós-atualização. O foco é gestão de frota de dispositivos, segurança da cadeia de atualização, e resiliência a falhas durante o update. Exemplos: câmera de segurança IP, medidor inteligente de energia, equipamento médico conectado, eletrodoméstico smart.

---

## Stack de Referência

Combinações testadas por variante. Não é prescrição obrigatória — é ponto de partida para quem não tem restrição técnica.

| Variante | MCU/SoC | RTOS/OS | Conectividade | Cloud/Backend | Observações |
|---|---|---|---|---|---|
| V1 — Sensor Node | ESP32, STM32L4, nRF52 | FreeRTOS, Zephyr | MQTT sobre Wi-Fi/LoRaWAN/NB-IoT | AWS IoT Core, Azure IoT Hub | Foco em deep sleep e consumo mínimo. LoRaWAN para alcance km sem infra. |
| V2 — Gateway/Edge | Raspberry Pi, BeagleBone, i.MX8 | Yocto Linux, Buildroot | Ethernet/Wi-Fi/4G (uplink) + BLE/Zigbee/Modbus (campo) | AWS Greengrass, Azure IoT Edge | Edge computing local. Container support para workloads de ML. |
| V3 — Atuador | STM32F4/F7, ESP32, PLC industrial | FreeRTOS, Zephyr, bare-metal | MQTT/Modbus TCP/CAN | AWS IoT Core, plataforma SCADA | RTOS obrigatório para controle em tempo real. Fail-safe em hardware. |
| V4 — Wearable | nRF52840, ESP32-S3, STM32WB | Zephyr, FreeRTOS | BLE 5.x (com app companion) | Firebase, backend próprio via API | BLE como protocolo primário. Otimização extrema de bateria. |
| V5 — Produto com OTA | Depende do tipo base | Qualquer com bootloader dual-bank | Wi-Fi/4G/Ethernet | Mender, Balena, Golioth, AWS IoT Jobs | Bootloader seguro com A/B partition. Assinatura criptográfica de firmware. |

---

## Etapa 01 — Inception

- **Origem da demanda e contexto de negócio**: Projetos de IoT/embarcado surgem de necessidades muito distintas — automação de um processo manual existente, criação de um produto novo para comercialização, requisito regulatório de monitoramento, ou digitalização de operações industriais. O gatilho real importa porque define o critério de sucesso: se o objetivo é reduzir custo operacional, o ROI é mensurável e o prazo é definido pela operação; se é um produto novo para mercado, o prazo é definido por janela competitiva e o sucesso depende de validação com usuário final. Projetos que misturam "produto para vender" com "solução interna" sem clareza geram conflitos de prioridade durante todo o ciclo.

- **Hardware existente vs. hardware a desenvolver**: A distinção mais fundamental na Inception de um projeto embarcado é se o hardware já existe (placa de desenvolvimento, módulo comercial, dispositivo legado a ser atualizado) ou se precisa ser projetado do zero (design de PCB, seleção de componentes, prototipação). Hardware custom adiciona meses ao cronograma, requer engenheiro de hardware dedicado, e introduz riscos de supply chain (componentes fora de estoque, lead time de PCBs). Se o hardware ainda não existe, o projeto precisa ser planejado em fases — firmware e cloud não podem avançar sem hardware funcional para testar.

- **Escala de produção e custo unitário**: Um protótipo funcional com Raspberry Pi a $50/unidade resolve para PoC, mas não escala para 10.000 unidades — o custo unitário precisa ser discutido na Inception para alinhar expectativas. A diferença entre protótipo e produção em volume envolve seleção de MCU/SoC otimizada para custo, design de PCB para fabricação automatizada (DFM), certificações obrigatórias (ANATEL, FCC, CE), e cadeia de suprimentos confiável. Clientes frequentemente subestimam o salto de complexidade entre "funciona no meu protótipo" e "pronto para produção".

- **Requisitos regulatórios e certificações**: Dispositivos que emitem rádio-frequência (Wi-Fi, BLE, LoRa, NB-IoT, 4G) precisam de homologação na ANATEL (Brasil), FCC (EUA) ou CE (Europa). Dispositivos médicos precisam de registro na ANVISA. Dispositivos industriais podem precisar de certificação ATEX/IECEx para ambientes explosivos. Cada certificação tem custo (milhares a dezenas de milhares de reais), prazo (semanas a meses), e pode exigir modificações no hardware ou firmware. Ignorar certificações na Inception e descobrir na Launch Prep é um dos erros mais caros em projetos IoT.

- **Conectividade disponível no ambiente de operação**: O ambiente onde o dispositivo vai operar determina as opções de conectividade — e frequentemente elimina as opções mais óbvias. Wi-Fi não existe em campo agrícola. 4G não funciona em subsolo de mina. Ethernet não chega a dispositivos móveis. LoRaWAN precisa de gateway com cobertura. A escolha de protocolo de comunicação não é decisão de desenvolvimento — é restrição do ambiente operacional que precisa ser mapeada antes de qualquer decisão técnica.

- **Segurança do dispositivo e dos dados**: Dispositivos IoT são alvos frequentes de ataques — botnets (Mirai), acesso físico não autorizado, interceptação de dados em trânsito, e clonagem de firmware. A Inception precisa identificar o nível de segurança necessário: criptografia de comunicação (TLS/DTLS), armazenamento seguro de credenciais (secure element, eFuse), boot seguro (secure boot chain), e proteção contra acesso físico (tamper detection). Projetos que tratam segurança como "a gente adiciona depois" acabam com dispositivos em campo impossíveis de atualizar com segurança.

### Perguntas

1. Qual é o problema de negócio que este dispositivo resolve — é automação interna, produto para comercialização, ou requisito regulatório? [fonte: Diretoria, Engenharia de Produto] [impacto: PM, Dev Firmware]
2. O hardware já existe (placa de dev, módulo comercial) ou precisa ser projetado do zero (PCB custom)? [fonte: Engenharia de Hardware, TI] [impacto: Dev Firmware, PM, Engenheiro de Hardware]
3. Qual é a escala de produção esperada (unidades) e qual o custo unitário máximo aceitável por dispositivo? [fonte: Diretoria, Comercial, Financeiro] [impacto: Engenheiro de Hardware, Dev Firmware, PM]
4. Existem certificações regulatórias obrigatórias para o mercado-alvo (ANATEL, FCC, CE, ANVISA, ATEX)? [fonte: Engenharia de Produto, Jurídico, Regulatório] [impacto: Engenheiro de Hardware, PM, Financeiro]
5. Qual é o ambiente físico de operação (temperatura, umidade, vibração, poeira, exposição a intempéries)? [fonte: Engenharia de Campo, Operações] [impacto: Engenheiro de Hardware, Dev Firmware]
6. Qual conectividade está disponível no ambiente de operação (Wi-Fi, celular, LoRa, Ethernet, nenhuma)? [fonte: Operações, TI de Campo, Engenharia de Rede] [impacto: Dev Firmware, Arquiteto IoT]
7. Qual é a fonte de energia do dispositivo (rede elétrica, bateria, solar, energy harvesting) e a autonomia mínima esperada? [fonte: Engenharia de Produto, Operações] [impacto: Engenheiro de Hardware, Dev Firmware]
8. Quantos dispositivos serão implantados na fase inicial e qual a projeção de crescimento da frota? [fonte: Diretoria, Operações, Comercial] [impacto: Arquiteto IoT, Dev Cloud, PM]
9. Existe infraestrutura cloud/backend existente à qual o dispositivo precisa se integrar? [fonte: TI, Arquitetura de Sistemas] [impacto: Dev Cloud, Arquiteto IoT]
10. Quem é o usuário final do dispositivo e qual o nível de interação esperado (instala e esquece, monitora dashboard, opera diariamente)? [fonte: Operações, Comercial, UX] [impacto: Dev Firmware, Designer, PM]
11. O dispositivo precisa receber atualizações de firmware remotamente (OTA) após o deploy em campo? [fonte: Engenharia de Produto, Diretoria] [impacto: Dev Firmware, Arquiteto IoT, Dev Cloud]
12. Qual é o nível de segurança exigido — dados sensíveis, controle de acesso físico, proteção contra clonagem? [fonte: Segurança da Informação, Engenharia de Produto, Jurídico] [impacto: Dev Firmware, Arquiteto IoT]
13. Existe time interno com experiência em firmware/embarcado ou o conhecimento será todo externo? [fonte: RH, Engenharia, Diretoria] [impacto: PM, Dev Firmware]
14. Qual é o prazo esperado para o primeiro protótipo funcional e para o início da produção em série? [fonte: Diretoria, Comercial] [impacto: PM, Engenheiro de Hardware, Dev Firmware]
15. O projeto tem dependência de fornecedores de componentes com lead time longo (chips, módulos de rádio, sensores específicos)? [fonte: Engenharia de Hardware, Compras] [impacto: PM, Engenheiro de Hardware]

---

## Etapa 02 — Discovery

- **Mapeamento de sensores e atuadores**: Levantar com precisão quais grandezas físicas serão medidas (temperatura, umidade relativa, pressão barométrica, aceleração, corrente elétrica, luminosidade, GPS) e quais ações serão executadas (acionar relé, controlar motor PWM, emitir alarme sonoro/visual). Para cada sensor, definir faixa de medição, resolução necessária, frequência de amostragem e precisão exigida. Essas especificações determinam diretamente a seleção de componentes de hardware — um sensor de temperatura com precisão de ±0.1°C custa 10x mais que um com ±1°C, e a diferença pode ser irrelevante para o caso de uso.

- **Requisitos de consumo de energia e autonomia**: Para dispositivos alimentados por bateria, o consumo de energia é a restrição mais crítica do projeto. Levantar: autonomia mínima esperada (dias, meses, anos), capacidade da bateria disponível (mAh), e perfil de uso (sempre ligado, duty cycle com deep sleep, wake-on-event). O orçamento de energia precisa ser calculado na Discovery — cada componente (MCU, rádio, sensor, LED, display) tem consumo especificado no datasheet, e a soma deve caber no budget energético. Descobrir na fase de Build que a bateria dura 2 dias em vez de 6 meses é redesign de hardware.

- **Protocolos de comunicação e topologia de rede**: Mapear a cadeia completa de dados: dispositivo → gateway/cloud → backend → dashboard/aplicação. Para cada trecho, definir o protocolo (MQTT, CoAP, HTTP, LoRaWAN, BLE, Modbus RTU/TCP, CAN), a topologia (ponto-a-ponto, estrela, mesh), e o comportamento em caso de falha de conectividade (buffer local, retry com backoff exponencial, descarte). Protocolos de campo (Modbus, CAN) exigem compatibilidade com equipamentos legados existentes — testar com o equipamento real, não apenas com simulador.

- **Requisitos de tempo real e latência**: Identificar se o sistema tem requisitos de tempo real hard (deadline absoluto, como controle de motor) ou soft (tolerância a atraso, como telemetria). Requisitos hard real-time exigem RTOS ou bare-metal — Linux não é adequado para deadlines abaixo de milissegundos. Definir a latência máxima aceitável para cada caminho: sensor → firmware (microsegundos a milissegundos), firmware → cloud (segundos a minutos), cloud → dashboard (segundos), comando cloud → atuador (depende da criticidade — abrir uma válvula de emergência tem requisito diferente de ajustar um setpoint de climatização).

- **Condições ambientais e robustez mecânica**: Levantar as condições reais de operação: faixa de temperatura operacional (ambientes industriais podem chegar a -40°C ou +85°C), exposição a umidade e líquidos (IP rating necessário — IP65 para poeira e jatos d'água, IP67 para submersão temporária), vibração e choque mecânico (transporte, maquinário industrial), e interferência eletromagnética (proximidade de motores, inversores de frequência, linhas de alta tensão). Cada requisito impacta o design do enclosure, a seleção de componentes (industrial grade vs. commercial grade), e o custo.

- **Integração com sistemas legados**: Em ambientes industriais e corporativos, o dispositivo IoT raramente opera isolado — precisa se integrar com sistemas existentes (SCADA, MES, ERP, CRM). Mapear todas as integrações previstas, seus protocolos (OPC-UA, Modbus, REST API, MQTT), e a disponibilidade de documentação técnica. Integrações com sistemas legados fechados (proprietários, sem API documentada) são o maior risco oculto — podem exigir engenharia reversa, adaptadores custom, ou negociação com o fornecedor do sistema legado para obter acesso.

### Perguntas

1. Quais grandezas físicas serão medidas e com qual precisão, faixa e frequência de amostragem? [fonte: Engenharia de Produto, Operações, Processo] [impacto: Engenheiro de Hardware, Dev Firmware]
2. Quais ações o dispositivo precisa executar no mundo físico (relés, motores, alarmes, displays)? [fonte: Engenharia de Produto, Operações] [impacto: Engenheiro de Hardware, Dev Firmware]
3. Qual a autonomia mínima de bateria esperada e qual o perfil de uso (sempre ligado, duty cycle, wake-on-event)? [fonte: Engenharia de Produto, Operações] [impacto: Engenheiro de Hardware, Dev Firmware]
4. Quais protocolos de comunicação são obrigatórios para integrar com equipamentos existentes (Modbus, CAN, BLE, OPC-UA)? [fonte: TI Industrial, Engenharia de Automação] [impacto: Dev Firmware, Arquiteto IoT]
5. Existe requisito de tempo real hard (deadline absoluto) para alguma função do dispositivo? [fonte: Engenharia de Processo, Segurança do Trabalho] [impacto: Dev Firmware, Arquiteto IoT]
6. Quais são as condições ambientais reais de operação (temperatura, umidade, vibração, poeira, IP rating)? [fonte: Engenharia de Campo, Manutenção, Operações] [impacto: Engenheiro de Hardware, Engenheiro Mecânico]
7. O dispositivo precisa operar em área classificada (explosiva) ou ambiente com requisitos especiais de segurança? [fonte: Segurança do Trabalho, Engenharia de Processo] [impacto: Engenheiro de Hardware, Regulatório, PM]
8. Quais sistemas legados o dispositivo precisa integrar e qual a documentação técnica disponível para cada um? [fonte: TI, Engenharia de Automação, Fornecedores] [impacto: Dev Firmware, Dev Cloud, Arquiteto IoT]
9. Qual é o volume de dados gerado por dispositivo por dia e qual a largura de banda disponível no ambiente? [fonte: Engenharia de Produto, TI de Rede] [impacto: Arquiteto IoT, Dev Cloud]
10. O dispositivo precisa funcionar offline (sem conectividade) por períodos prolongados? Quanto tempo e quanta informação precisa armazenar localmente? [fonte: Operações, Engenharia de Campo] [impacto: Dev Firmware, Arquiteto IoT]
11. Existe necessidade de localização do dispositivo (GPS outdoor, BLE beacon indoor, triangulação celular)? [fonte: Operações, Logística] [impacto: Engenheiro de Hardware, Dev Firmware]
12. Quais dados são sensíveis e precisam de criptografia em trânsito e em repouso (dados pessoais, segredos industriais)? [fonte: Segurança da Informação, Jurídico, DPO] [impacto: Dev Firmware, Arquiteto IoT]
13. O cliente tem acesso a equipamentos e ambientes reais para testes durante o desenvolvimento ou apenas no deploy? [fonte: Operações, Engenharia de Campo] [impacto: Dev Firmware, QA, PM]
14. Quais dashboards, relatórios ou alertas são esperados a partir dos dados coletados pelo dispositivo? [fonte: Operações, Diretoria, Engenharia de Processo] [impacto: Dev Cloud, Designer, PM]
15. Existe expectativa de integração com plataformas de ML/IA para análise preditiva dos dados coletados? [fonte: Engenharia de Dados, Diretoria] [impacto: Arquiteto IoT, Dev Cloud, Data Engineer]

---

## Etapa 03 — Alignment

- **Divisão de responsabilidades hardware/firmware/cloud**: Alinhar formalmente os limites de responsabilidade entre os times (ou fornecedores): quem entrega o hardware funcional com esquemático e documentação de pinout, quem desenvolve o firmware com quais interfaces de hardware disponíveis, quem implementa o backend/cloud com qual protocolo de ingestão de dados, e quem constrói o dashboard/aplicação consumindo quais APIs. Em projetos IoT, a zona cinzenta entre essas camadas é onde os bugs mais difíceis vivem — "o dado chega errado no cloud" pode ser problema de sensor, calibração no firmware, serialização no protocolo, ou parsing no backend. Sem ownership claro de cada camada, bugs de integração ficam sem dono.

- **Definição do protocolo de dados (payload)**: Alinhar o formato exato dos dados trocados entre dispositivo e cloud — campos, tipos, unidades, encoding (JSON, CBOR, Protobuf, binário custom), e versionamento do payload. Protobuf e CBOR são mais eficientes em bandwidth (crítico para LoRaWAN e NB-IoT com payload limitado), mas JSON é mais fácil de debugar e integrar. O formato do payload é contrato entre firmware e cloud — mudar depois do deploy de dispositivos em campo exige OTA, que pode não estar disponível ou ser arriscado. Definir e versionar o payload antes do Build é essencial.

- **Estratégia de testes com hardware real**: Alinhar como e quando o firmware será testado com hardware real (não apenas simulador ou emulador). Definir: quantas unidades de teste estão disponíveis para o time de desenvolvimento, se há ambiente de teste que simule condições reais (câmara climática, gerador de vibração, atenuador de sinal), e qual o processo para provisionar dispositivos de teste com credenciais e certificados. Firmware testado apenas em emulador tem alta taxa de falha no hardware real — especialmente em timing, consumo de energia, e comunicação com periféricos reais.

- **Modelo de provisionamento de dispositivos**: Alinhar como cada dispositivo receberá sua identidade única, credenciais de acesso ao cloud, e certificados TLS. Em escala pequena (dezenas), pode ser feito manualmente via cabo serial durante o setup. Em escala média a grande (centenas a milhares), precisa de processo automatizado na linha de produção — flash de firmware com ID único, injeção de certificado client-side, e registro automático na plataforma cloud (just-in-time provisioning). O modelo de provisionamento impacta diretamente a segurança e a escalabilidade da solução.

- **SLA de monitoramento e manutenção em campo**: Dispositivos IoT em campo falham — bateria acaba, sensor degrada, conectividade cai, firmware trava. Alinhar o modelo de monitoramento (heartbeat, watchdog cloud-side, alertas de inatividade) e o modelo de manutenção (quem vai até o dispositivo, em quanto tempo, com qual skill técnico). Se o dispositivo está em local de difícil acesso (torre, campo remoto, subsolo), o custo de manutenção presencial pode ser maior que o custo do dispositivo — o que reforça a importância de OTA e diagnóstico remoto.

### Perguntas

1. As responsabilidades entre hardware, firmware, cloud e aplicação estão formalmente divididas com donos claros para cada camada? [fonte: Engenharia, TI, Diretoria] [impacto: PM, Dev Firmware, Dev Cloud]
2. O formato do payload de dados (campos, tipos, encoding, versionamento) foi definido e documentado como contrato entre firmware e cloud? [fonte: Dev Firmware, Dev Cloud, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud]
3. Quantas unidades de hardware de teste estão disponíveis para o time de desenvolvimento durante o Build? [fonte: Engenharia de Hardware, Compras] [impacto: Dev Firmware, QA, PM]
4. Existe ambiente de teste que simule condições reais de operação (temperatura, vibração, atenuação de sinal)? [fonte: Engenharia de Campo, Laboratório] [impacto: QA, Dev Firmware, Engenheiro de Hardware]
5. O modelo de provisionamento de dispositivos foi definido (identidade única, credenciais, certificados)? [fonte: Segurança da Informação, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud, Engenheiro de Hardware]
6. O processo de OTA foi alinhado — quem autoriza, como é validado, qual a estratégia de rollback? [fonte: Engenharia de Produto, Diretoria] [impacto: Dev Firmware, Arquiteto IoT, Dev Cloud]
7. O SLA de manutenção em campo foi definido (quem vai, em quanto tempo, com qual equipamento)? [fonte: Operações, Diretoria, Manutenção] [impacto: PM, Operações]
8. O modelo de monitoramento de saúde dos dispositivos foi acordado (heartbeat, alertas, dashboard de frota)? [fonte: Operações, TI] [impacto: Dev Cloud, Arquiteto IoT]
9. A estratégia de versionamento de firmware foi definida (semantic versioning, changelog, compatibilidade com payload)? [fonte: Dev Firmware, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud]
10. O processo de homologação e certificação (ANATEL, CE, etc.) foi mapeado com prazos e responsável? [fonte: Engenharia de Produto, Regulatório, Jurídico] [impacto: PM, Engenheiro de Hardware]
11. As dependências externas críticas (componentes de hardware, módulos, licenças de SDK) foram listadas com lead time? [fonte: Compras, Engenharia de Hardware] [impacto: PM, Engenheiro de Hardware]
12. O cliente entende que mudanças de hardware após início da produção são ordens de magnitude mais caras que mudanças de software? [fonte: Diretoria, Engenharia de Produto] [impacto: PM, Engenheiro de Hardware]
13. A cadeia de aprovação técnica foi definida — quem revisa code de firmware, quem aprova mudança de hardware, quem libera OTA? [fonte: Engenharia, Diretoria] [impacto: Dev Firmware, Engenheiro de Hardware, PM]
14. O escopo do MVP foi definido com clareza — quais sensores, quais funcionalidades cloud, qual a frota mínima? [fonte: Diretoria, Engenharia de Produto] [impacto: PM, Dev Firmware, Dev Cloud]
15. Existe acordo sobre o nível de documentação técnica esperado (esquemático, pinout, API, manual de campo)? [fonte: Engenharia de Produto, Operações] [impacto: Dev Firmware, Engenheiro de Hardware, PM]

---

## Etapa 04 — Definition

- **Especificação de hardware (BOM e esquemático)**: Produzir o Bill of Materials completo com componentes selecionados — MCU/SoC (modelo exato, variante de memória, package), módulo de rádio (Wi-Fi, BLE, LoRa, celular), sensores (modelo, interface — I2C, SPI, ADC), reguladores de tensão, conectores, componentes passivos, e enclosure. Cada componente deve ter ao menos um substituto equivalente (second source) para mitigar risco de supply chain. O esquemático define a interface entre hardware e firmware — pinout, barramentos, GPIOs disponíveis — e é o artefato que permite ao dev de firmware começar a trabalhar em paralelo com a fabricação da placa.

- **Modelo de dados e telemetria**: Definir o schema completo de cada mensagem de telemetria que o dispositivo envia ao cloud — campos, tipos de dados, unidades de medida, frequência de envio, e tamanho máximo do payload. Para cada campo, especificar: se é obrigatório ou opcional, faixa de valores válidos, resolução (quantas casas decimais), e formato de timestamp (Unix epoch, ISO 8601). Este schema é o contrato formal entre firmware e cloud — ambos os times implementam contra esta especificação. Qualquer mudança posterior requer versionamento (ex.: campo "version" no payload) para manter compatibilidade com dispositivos já em campo.

- **Máquina de estados do firmware**: Documentar formalmente os estados operacionais do dispositivo e as transições entre eles — boot → inicialização de periféricos → leitura de sensores → transmissão → deep sleep → wake-up. Para dispositivos com atuadores, adicionar estados de controle com condições de entrada e saída. Para dispositivos com OTA, documentar o fluxo de atualização como sub-máquina de estados (check update → download → verify signature → apply → reboot → validate → commit ou rollback). A máquina de estados é o documento mais importante para o dev de firmware — qualquer ambiguidade aqui gera bugs difíceis de reproduzir em campo.

- **Estratégia de armazenamento local**: Definir como o dispositivo armazena dados quando não há conectividade — tipo de memória (flash interna, SD card, EEPROM), formato de armazenamento (ring buffer, filesystem, banco key-value), capacidade necessária (calculada pelo volume de dados × tempo máximo offline), e política de descarte quando o buffer enche (FIFO, prioridade por tipo de dado, compactação). Para dispositivos em ambientes com conectividade intermitente, o armazenamento local é o que garante zero perda de dados — e seu dimensionamento depende de informações levantadas na Discovery.

- **Especificação de interfaces de usuário no dispositivo**: Se o dispositivo tem interface local (LEDs, botões, display, buzzer), especificar o comportamento de cada elemento — qual LED indica qual estado, qual sequência de piscar indica erro, qual botão faz reset de fábrica e por quanto tempo precisa ser pressionado, o que o display mostra em cada estado. Interfaces de dispositivo embarcado têm recursos extremamente limitados (um LED RGB e dois botões, por exemplo) e cada combinação de cor, frequência de piscar e duração precisa ter significado único e documentado. Sem essa especificação, o dev de firmware inventa comportamentos ad-hoc que são impossíveis de suportar em campo.

- **Requisitos de segurança por camada**: Especificar os controles de segurança para cada camada do sistema — dispositivo (secure boot, encrypted storage, tamper detection, disable JTAG em produção), comunicação (TLS 1.3/DTLS, certificate pinning, mutual authentication), cloud (IAM com least privilege, device shadow com access control, audit logging), e OTA (firmware signing, anti-rollback counter, dual-bank com fallback). Cada controle tem custo de implementação e pode exigir hardware específico (secure element, TPM, eFuse) — que precisa estar no BOM definido acima.

### Perguntas

1. O BOM completo foi produzido com componentes selecionados e pelo menos uma second source para itens críticos? [fonte: Engenharia de Hardware, Compras] [impacto: Engenheiro de Hardware, PM]
2. O schema de telemetria foi especificado campo a campo com tipos, unidades, faixa válida e formato de timestamp? [fonte: Arquiteto IoT, Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
3. A máquina de estados do firmware foi documentada formalmente com todos os estados e transições? [fonte: Dev Firmware, Engenharia de Produto] [impacto: Dev Firmware, QA]
4. A estratégia de armazenamento local offline foi dimensionada (capacidade = volume/hora × horas sem conectividade)? [fonte: Dev Firmware, Operações] [impacto: Dev Firmware, Engenheiro de Hardware]
5. As interfaces de usuário no dispositivo (LEDs, botões, display) têm especificação de comportamento documentada? [fonte: Engenharia de Produto, UX] [impacto: Dev Firmware, Documentação]
6. Os requisitos de segurança foram especificados por camada (dispositivo, comunicação, cloud, OTA)? [fonte: Segurança da Informação, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud, Engenheiro de Hardware]
7. O fluxo de OTA foi especificado com assinatura, verificação, dual-bank, rollback e anti-rollback counter? [fonte: Arquiteto IoT, Dev Firmware] [impacto: Dev Firmware, Dev Cloud]
8. O protocolo de comunicação bidirecional (comandos cloud → dispositivo) foi especificado com retry, timeout e ACK? [fonte: Arquiteto IoT, Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
9. Os critérios de calibração de sensores foram definidos (procedimento, frequência, tolerância aceitável)? [fonte: Engenharia de Processo, Metrologia] [impacto: Dev Firmware, QA, Operações]
10. O formato de logs do dispositivo foi definido para facilitar diagnóstico remoto (severity, timestamp, código de erro)? [fonte: Dev Firmware, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud]
11. As condições de fail-safe foram especificadas para cada atuador (o que acontece se perder comunicação, energia, firmware crash)? [fonte: Engenharia de Processo, Segurança do Trabalho] [impacto: Dev Firmware, Engenheiro de Hardware]
12. O versionamento de firmware e payload foi definido com regras de compatibilidade (versão N-1 do cloud aceita payload versão N?)? [fonte: Arquiteto IoT, Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
13. O enclosure foi especificado com IP rating, material, dimensões máximas e pontos de fixação? [fonte: Engenharia Mecânica, Engenharia de Campo] [impacto: Engenheiro de Hardware, Engenheiro Mecânico]
14. Os testes automatizados de firmware foram planejados (unit tests, hardware-in-the-loop, integration tests)? [fonte: Dev Firmware, QA] [impacto: Dev Firmware, QA]
15. A documentação de definição foi revisada e aprovada por todas as disciplinas (hardware, firmware, cloud, operações)? [fonte: Engenharia, Diretoria] [impacto: PM, Dev Firmware, Dev Cloud, Engenheiro de Hardware]

---

## Etapa 05 — Architecture

- **Seleção do MCU/SoC e ambiente de desenvolvimento**: A escolha do microcontrolador define o ecossistema de desenvolvimento e as capacidades do dispositivo. ESP32 é popular para prototipação rápida com Wi-Fi/BLE integrados e SDK maduro (ESP-IDF), mas tem consumo de energia alto para aplicações de deep sleep prolongado. STM32 (família L4/L0 para low power, F4/F7 para processamento) oferece excelente ecossistema de ferramentas (STM32CubeIDE, HAL) e opções para cada faixa de consumo/performance. nRF52/nRF53 (Nordic) é referência para BLE com SDK nRF Connect/Zephyr. Para gateway com Linux, i.MX8 ou Raspberry Pi Compute Module oferecem poder de processamento com suporte a containers. A escolha deve considerar: disponibilidade de componente no mercado (verificar lead time real em distribuidores), suporte do fabricante (datasheet, errata, application notes), e experiência do time.

- **Arquitetura de firmware (RTOS vs. bare-metal vs. Linux)**: Bare-metal é adequado para dispositivos simples com uma única função sequencial (ler sensor → transmitir → dormir). RTOS (FreeRTOS, Zephyr) é necessário quando há múltiplas tarefas concorrentes com prioridades diferentes (leitura de sensor a 100Hz + comunicação BLE + display + watchdog) ou requisitos de tempo real. Linux embarcado (Yocto, Buildroot) é indicado para gateways e dispositivos com necessidade de networking complexo, filesystem, e suporte a containers. A decisão impacta profundamente o perfil do desenvolvedor necessário — firmware bare-metal/RTOS exige conhecimento de registradores, interrupções e gerenciamento de memória manual; Linux embarcado exige conhecimento de kernel, device tree e cross-compilation.

- **Plataforma cloud IoT**: AWS IoT Core oferece MQTT broker gerenciado, device shadow (digital twin), regras de roteamento de mensagens para S3/DynamoDB/Lambda, e integração nativa com AWS Greengrass para edge computing. Azure IoT Hub oferece funcionalidades equivalentes com integração ao ecossistema Azure (Stream Analytics, Time Series Insights, Digital Twins). Para projetos menores ou que não querem vendor lock-in, alternativas open-source como EMQX (MQTT broker), Thingsboard, ou Chirpstack (para LoRaWAN) podem ser self-hosted com custo de infraestrutura e operação. A escolha deve considerar: escala da frota, budget, expertise do time em cloud, e requisitos de data residency (LGPD pode exigir dados em datacenter no Brasil).

- **Arquitetura de OTA (Over-The-Air updates)**: Para dispositivos com ciclo de vida longo, OTA é crítico. A arquitetura deve definir: mecanismo de bootloader (A/B partition com fallback automático se a nova versão não boota), assinatura criptográfica de firmware (chave pública no dispositivo, chave privada no servidor de build — NUNCA no dispositivo), anti-rollback counter (impedir que firmware antigo vulnerável seja reinstalado), estratégia de deploy (canary release — atualizar 1% da frota, monitorar, expandir gradualmente), e monitoramento pós-update (verificar que dispositivos atualizados estão reportando normalmente). Soluções gerenciadas como Mender, Golioth, Balena ou AWS IoT Jobs simplificam a implementação, mas adicionam custo e dependência.

- **Pipeline de dados (ingestão → processamento → armazenamento → visualização)**: Definir a arquitetura do pipeline de dados completo: ingestão via MQTT broker → processamento (filtragem, enriquecimento, detecção de anomalias) via stream processing (AWS Kinesis, Azure Stream Analytics, ou Apache Kafka para self-hosted) → armazenamento em time-series database (InfluxDB, TimescaleDB, ou DynamoDB/Timestream na AWS) → visualização via dashboard (Grafana, Metabase, ou aplicação custom). Para cada trecho, definir: latência aceitável, volume de dados (mensagens/segundo × tamanho médio × número de dispositivos), política de retenção (dados brutos por X dias, dados agregados por Y meses), e custo de armazenamento projetado.

- **Segurança end-to-end**: Definir a cadeia de segurança completa: certificados X.509 por dispositivo (provisionados na fábrica ou via just-in-time provisioning), TLS 1.3 para MQTT, mutual authentication (dispositivo autentica cloud e cloud autentica dispositivo), secure element ou eFuse para armazenamento de chaves privadas, secure boot chain (bootloader verifica assinatura do firmware antes de executar), e política de rotação de certificados. Para dispositivos em campo acessíveis fisicamente, considerar tamper detection (sensor de abertura do enclosure que apaga chaves) e desabilitação de interfaces de debug (JTAG, UART) na versão de produção.

### Perguntas

1. O MCU/SoC foi selecionado considerando consumo de energia, periféricos necessários, disponibilidade e experiência do time? [fonte: Engenharia de Hardware, Dev Firmware] [impacto: Dev Firmware, Engenheiro de Hardware]
2. A decisão entre bare-metal, RTOS e Linux embarcado foi tomada com justificativa documentada? [fonte: Dev Firmware, Arquiteto IoT] [impacto: Dev Firmware]
3. A plataforma cloud IoT foi escolhida considerando escala, custo projetado, data residency e lock-in? [fonte: TI, Arquiteto IoT, Financeiro] [impacto: Dev Cloud, Dev Firmware, PM]
4. A arquitetura de OTA foi definida com bootloader A/B, assinatura de firmware e estratégia de rollback? [fonte: Arquiteto IoT, Dev Firmware] [impacto: Dev Firmware, Dev Cloud]
5. O pipeline de dados foi arquitetado de ponta a ponta (ingestão → processamento → armazenamento → visualização)? [fonte: Arquiteto IoT, Dev Cloud] [impacto: Dev Cloud, Data Engineer]
6. A time-series database foi escolhida considerando volume projetado, queries esperadas e custo de retenção? [fonte: Dev Cloud, Arquiteto IoT, Financeiro] [impacto: Dev Cloud]
7. A estratégia de segurança end-to-end foi documentada (certificados, TLS, secure boot, secure element)? [fonte: Segurança da Informação, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud, Engenheiro de Hardware]
8. O provisionamento de dispositivos em escala foi arquitetado (identidade, certificados, registro no cloud)? [fonte: Arquiteto IoT, Engenharia de Produção] [impacto: Dev Firmware, Dev Cloud, Engenheiro de Hardware]
9. A estratégia de edge computing foi definida — quais processamentos acontecem no dispositivo vs. no cloud? [fonte: Arquiteto IoT, Engenharia de Produto] [impacto: Dev Firmware, Dev Cloud]
10. O custo mensal da arquitetura cloud foi calculado para frota atual e frota projetada em 12 meses? [fonte: Financeiro, Arquiteto IoT] [impacto: PM, Dev Cloud]
11. A arquitetura suporta crescimento da frota sem redesign (10x mais dispositivos com qual impacto em custo e performance)? [fonte: Arquiteto IoT, Diretoria] [impacto: Dev Cloud, PM]
12. O modelo de conectividade foi validado no ambiente real (teste de sinal Wi-Fi/LoRa/celular no local de operação)? [fonte: Engenharia de Campo, TI de Rede] [impacto: Engenheiro de Hardware, Dev Firmware]
13. A estratégia de logging e diagnóstico remoto foi definida (o que é logado, onde é armazenado, como é acessado)? [fonte: Dev Firmware, Dev Cloud, Operações] [impacto: Dev Firmware, Dev Cloud]
14. O plano de contingência para indisponibilidade do cloud foi definido (dispositivo opera standalone? por quanto tempo?)? [fonte: Operações, Arquiteto IoT] [impacto: Dev Firmware, Dev Cloud]
15. O modelo de branches, ambientes (dev, staging, produção) e pipeline de CI/CD para firmware e cloud foi documentado? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud, DevOps]

---

## Etapa 06 — Setup

- **Ambiente de desenvolvimento de firmware**: Configurar o toolchain completo de cross-compilation — compilador (GCC ARM, Xtensa para ESP32), SDK do fabricante (ESP-IDF, STM32 HAL, nRF Connect SDK), ferramenta de flash e debug (OpenOCD, J-Link, ESP-PROG), e IDE ou editor (VS Code com extensões, PlatformIO, STM32CubeIDE). Garantir que todos os desenvolvedores do time consigam compilar e flashar o firmware em hardware real a partir do repositório clonado — a reprodutibilidade do ambiente de build é crítica em embarcado porque variações de versão de SDK ou compilador podem causar bugs sutis. Documentar as versões exatas de todas as ferramentas no README do repositório.

- **Infraestrutura cloud e ambientes**: Provisionar a infraestrutura de cloud IoT separada em ambientes — development (para testes do dev), staging (para QA e integração), e production (para dispositivos reais em campo). Cada ambiente deve ter seu próprio MQTT broker endpoint, database, e conjunto de credenciais — nunca reutilizar o mesmo broker para dev e produção. Usar Infrastructure as Code (Terraform, CloudFormation, Pulumi) para garantir que os ambientes sejam reproduzíveis e auditáveis. Configurar billing alerts no cloud desde o dia 1 — projetos IoT podem acumular custos silenciosamente à medida que a frota cresce e o volume de dados aumenta.

- **Pipeline de CI/CD para firmware**: Configurar build automatizado para cada push — compilação cross-platform, execução de testes unitários (em host, não no target), análise estática de código (cppcheck, clang-tidy), e geração do artefato de firmware com hash e assinatura. O pipeline deve produzir um binário versionado pronto para deploy (OTA ou flash manual) a cada merge para main. Para projetos com OTA, o pipeline também deve gerar o pacote de atualização no formato esperado pela plataforma de OTA (Mender artifact, Golioth release, AWS IoT Job document). GitHub Actions ou GitLab CI são adequados — a parte de compilação roda em container Docker com toolchain pré-configurado.

- **Provisionamento de dispositivos de teste**: Provisionar as unidades de hardware de teste com firmware base, credenciais de acesso ao ambiente de desenvolvimento, e certificados TLS. Documentar o procedimento de provisionamento passo a passo — desde conexão do cabo USB/JTAG até verificação de que o dispositivo está comunicando com o cloud. Este procedimento será repetido muitas vezes durante o Build e QA — automatizá-lo com scripts (esptool.py, STM32_Programmer_CLI, nrfjprog) economiza horas. Cada dispositivo de teste deve ter identificador único registrado no cloud para rastreabilidade.

- **Repositório e estrutura de código**: Organizar o repositório de firmware com separação clara entre: HAL/drivers de hardware (camada que abstrai periféricos), lógica de aplicação (máquina de estados, processamento de dados), camada de comunicação (MQTT client, serialização de payload), e configuração (pinout, constantes, variáveis de build). Usar o padrão de abstração de hardware (HAL pattern) desde o início — isso permite que testes unitários rodem no host (PC) sem hardware real, mockando a camada de HAL. O repositório de cloud/backend pode ser separado ou monorepo — ambos funcionam, desde que o CI/CD esteja configurado para cada componente independentemente.

- **Setup de monitoramento e observabilidade**: Configurar o dashboard de monitoramento da frota de dispositivos antes de iniciar o Build — mesmo que a frota seja de apenas 2-3 unidades de teste. O dashboard deve mostrar: último heartbeat de cada dispositivo, versão de firmware de cada dispositivo, métricas de comunicação (taxa de sucesso de envio, latência), e alertas de inatividade (dispositivo não reportou há X minutos). Grafana + InfluxDB/Prometheus é a combinação mais comum. Ter o dashboard rodando desde o Setup permite que o time identifique problemas de comunicação e estabilidade desde os primeiros testes.

### Perguntas

1. O toolchain de cross-compilation está configurado e todos os devs conseguem compilar e flashar firmware em hardware real? [fonte: Dev Firmware] [impacto: Dev Firmware]
2. As versões exatas de SDK, compilador e ferramentas estão documentadas e são reproduzíveis (Docker, lockfile)? [fonte: Dev Firmware] [impacto: Dev Firmware, DevOps]
3. Os ambientes de cloud estão provisionados separadamente (dev, staging, production) com credenciais isoladas? [fonte: Dev Cloud, DevOps] [impacto: Dev Cloud, Dev Firmware]
4. A infraestrutura de cloud está definida como código (Terraform, CloudFormation) e versionada no repositório? [fonte: DevOps, Dev Cloud] [impacto: DevOps, Dev Cloud]
5. O pipeline de CI/CD de firmware está gerando binário versionado com hash e assinatura a cada push? [fonte: Dev Firmware, DevOps] [impacto: Dev Firmware, DevOps]
6. Os dispositivos de teste foram provisionados com credenciais e estão comunicando com o ambiente de desenvolvimento? [fonte: Dev Firmware, Engenheiro de Hardware] [impacto: Dev Firmware, QA]
7. O procedimento de provisionamento de dispositivos está documentado e automatizado via script? [fonte: Dev Firmware] [impacto: Dev Firmware, Engenheiro de Hardware, Operações]
8. O repositório de firmware está organizado com separação HAL/aplicação/comunicação e testes unitários configurados? [fonte: Dev Firmware] [impacto: Dev Firmware]
9. O dashboard de monitoramento de frota está configurado e mostrando dados dos dispositivos de teste? [fonte: Dev Cloud, DevOps] [impacto: Dev Cloud, Dev Firmware, Operações]
10. Os billing alerts do cloud estão configurados para evitar surpresas de custo durante o desenvolvimento? [fonte: DevOps, Financeiro] [impacto: PM, DevOps]
11. O MQTT broker está configurado com políticas de acesso por dispositivo (cada device só publica/assina em seus tópicos)? [fonte: Arquiteto IoT, Dev Cloud] [impacto: Dev Cloud, Dev Firmware]
12. O .gitignore exclui binários gerados, credenciais e arquivos de configuração local da IDE? [fonte: Dev Firmware] [impacto: Dev Firmware]
13. O ambiente de staging está configurado para receber OTA de teste com firmware de development? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, QA]
14. O processo de onboarding de novos desenvolvedores (firmware e cloud) está documentado no README? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
15. O pipeline de CI/CD foi testado end-to-end (push → build → artefato → deploy em device de teste)? [fonte: Dev Firmware, DevOps] [impacto: Dev Firmware, DevOps]

---

## Etapa 07 — Build

- **Implementação da camada HAL e drivers**: Implementar os drivers de hardware para cada periférico do sistema — sensores (I2C, SPI, ADC), módulos de comunicação (UART, SPI para módulo LoRa, driver Wi-Fi/BLE), atuadores (GPIO, PWM, DAC), e storage (SPI Flash, SD card, EEPROM). Cada driver deve ter interface definida por contrato (header com funções init, read, write, deinit) que permite mock para testes unitários. Testar cada driver isoladamente com hardware real antes de integrar — um driver de sensor I2C que funciona no scope mas falha sob carga do RTOS é um bug clássico que consome dias de debug. Documentar quirks do hardware descobertos durante a implementação (ex.: "sensor X precisa de 10ms delay após power-on antes de aceitar comandos").

- **Implementação da máquina de estados principal**: Codificar a máquina de estados documentada na Definition — com transições explícitas, timeouts por estado, e logging de cada transição para diagnóstico. Usar um framework de state machine (se disponível no RTOS) ou implementação manual com switch/case e tabela de transições. Cada estado deve ter critérios de entrada e saída verificáveis, e o watchdog timer deve ser configurado para resetar o dispositivo se a máquina de estados ficar travada em qualquer estado por mais tempo que o timeout máximo definido. O estado de erro/recuperação é o mais negligenciado e o mais importante — definir o que acontece quando qualquer componente falha.

- **Implementação da comunicação com cloud**: Integrar o MQTT client (ou CoAP, HTTP — conforme definido na Architecture) com a plataforma cloud, implementando: conexão TLS com certificate pinning, publicação de telemetria no formato de payload definido, subscrição de tópicos de comando (cloud → device), tratamento de desconexão com reconnect automático e backoff exponencial, e buffer local com retry para mensagens que falharam durante desconexão. Testar com simulação de conectividade intermitente (desligar e religar o Wi-Fi/rede durante operação) — o comportamento do dispositivo durante e após perda de conectividade é onde a maioria dos bugs de produção aparece.

- **Implementação de OTA (se aplicável)**: Integrar o mecanismo de OTA definido na Architecture — download de nova versão via HTTPS ou MQTT, verificação de assinatura criptográfica, escrita na partição B (A/B scheme), reboot para nova versão, self-test na nova versão (verificar que sensores e comunicação funcionam), e commit da nova versão ou rollback automático para a versão anterior se o self-test falhar. Testar cenários de falha: OTA interrompido no meio do download (deve retomar ou abortar limpo), firmware corrompido (assinatura inválida — deve rejeitar), e nova versão que não passa no self-test (deve reverter automaticamente). OTA mal implementado é o risco mais alto em IoT — pode brickar toda a frota.

- **Implementação do backend/cloud**: Implementar os componentes de cloud conforme a arquitetura definida: regras de roteamento de mensagens (MQTT → processamento → storage), APIs REST para dashboard e aplicação, lógica de processamento de dados (agregação, detecção de anomalias, alertas), e gerenciamento de dispositivos (registro, status, envio de comandos). Implementar rate limiting e throttling para proteger o backend contra floods de dispositivos — um bug de firmware que cause loop de publicação pode derrubar o broker MQTT se não houver proteção. Implementar dead letter queue para mensagens que falham no processamento.

- **Otimização de consumo de energia**: Para dispositivos battery-powered, a otimização de energia não é fase final — é constraint que permeia todo o Build. Medir o consumo real com multímetro de precisão ou power profiler (Nordic PPK2, Joulescope) em cada estado da máquina de estados. Identificar e eliminar consumos desnecessários: periféricos não desligados durante deep sleep, pull-ups internos ativados sem necessidade, LED de debug ligado em produção, conversão DC-DC com eficiência subótima. A diferença entre firmware otimizado e não-otimizado pode ser de 10x em autonomia de bateria — de semanas para meses.

### Perguntas

1. Todos os drivers de hardware foram implementados e testados isoladamente com hardware real? [fonte: Dev Firmware] [impacto: Dev Firmware, QA]
2. A máquina de estados principal está implementada com logging de transições e watchdog configurado? [fonte: Dev Firmware] [impacto: Dev Firmware, QA]
3. A comunicação com cloud funciona com TLS, reconnect automático e buffer local durante desconexão? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
4. O comportamento do dispositivo foi testado com perda e retomada de conectividade (simulação de queda de rede)? [fonte: Dev Firmware, QA] [impacto: Dev Firmware, QA]
5. O mecanismo de OTA foi implementado e testado com cenários de falha (download interrompido, assinatura inválida, rollback)? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
6. O consumo de energia foi medido com instrumentação real em cada estado da máquina de estados? [fonte: Dev Firmware, Engenheiro de Hardware] [impacto: Dev Firmware, Engenheiro de Hardware]
7. A autonomia de bateria calculada com consumo real está dentro do requisito definido na Discovery? [fonte: Dev Firmware, Engenheiro de Hardware] [impacto: Dev Firmware, Engenheiro de Hardware, PM]
8. O backend/cloud está implementado com rate limiting, dead letter queue e monitoramento de saúde? [fonte: Dev Cloud] [impacto: Dev Cloud, DevOps]
9. As APIs REST para dashboard e aplicação estão implementadas e documentadas (OpenAPI/Swagger)? [fonte: Dev Cloud] [impacto: Dev Cloud, Dev Frontend]
10. Os testes unitários de firmware estão passando no CI com cobertura mínima definida? [fonte: Dev Firmware] [impacto: Dev Firmware, QA]
11. A análise estática de código (cppcheck, clang-tidy) está integrada no CI e sem warnings críticos? [fonte: Dev Firmware] [impacto: Dev Firmware]
12. O provisionamento em série (múltiplos dispositivos) foi testado com o procedimento automatizado? [fonte: Dev Firmware, Engenharia de Produção] [impacto: Dev Firmware, Operações]
13. A calibração de sensores foi implementada e validada contra referência metrológica? [fonte: Dev Firmware, Engenharia de Processo] [impacto: Dev Firmware, QA]
14. O formato de log do dispositivo permite diagnóstico remoto eficaz (timestamp, severity, contexto)? [fonte: Dev Firmware] [impacto: Dev Firmware, Dev Cloud, Operações]
15. A documentação técnica do firmware (pinout, registradores, protocolos) está atualizada com a implementação real? [fonte: Dev Firmware] [impacto: Dev Firmware, Engenheiro de Hardware]

---

## Etapa 08 — QA

- **Testes de integração hardware-firmware-cloud**: Executar o ciclo completo de dados end-to-end — sensor lê valor → firmware empacota → MQTT publica → cloud recebe → pipeline processa → database armazena → dashboard exibe. Verificar que o valor exibido no dashboard corresponde ao valor real do sensor com precisão esperada. Testar com múltiplos dispositivos simultâneos para identificar problemas de concorrência no broker ou no backend. Este teste é o mais importante do QA em IoT — ele valida que todas as camadas funcionam juntas, não apenas isoladamente.

- **Testes de stress e estabilidade (soak test)**: Deixar o dispositivo operando continuamente por período prolongado (mínimo 72h, idealmente 1-2 semanas) monitorando: estabilidade da conexão MQTT (reconecta automaticamente?), consumo de memória do firmware (memory leak?), precisão dos sensores ao longo do tempo (drift?), e taxa de perda de mensagens (todas as leituras chegam ao cloud?). Bugs de memory leak, stack overflow e buffer overrun frequentemente não aparecem em testes curtos — eles se manifestam após horas ou dias de operação contínua. O soak test é o que separa protótipo de produto.

- **Testes em condições ambientais reais**: Testar o dispositivo nas condições reais de operação — não apenas no lab com temperatura controlada a 25°C. Se o dispositivo vai operar a 45°C, testar a 45°C (câmara climática ou ambiente real). Se vai operar com vibração, testar com vibração. Se a conectividade é via LoRaWAN a 500m, testar a 500m com obstáculos reais. Problemas que aparecem apenas em condições de campo são os mais caros de resolver — especialmente se o dispositivo já está instalado e precisa de manutenção presencial.

- **Testes de segurança**: Validar os controles de segurança implementados: tentar conectar ao MQTT broker com credenciais inválidas (deve ser rejeitado), tentar enviar firmware OTA sem assinatura válida (deve ser rejeitado), tentar ler credenciais da flash via JTAG (deve estar desabilitado ou protegido), e verificar que o TLS está configurado corretamente (via SSL Labs ou testssl.sh no endpoint cloud). Para dispositivos com acesso físico em campo, tentar extrair firmware da flash e verificar que segredos (chaves, senhas, tokens) não estão em texto plano.

- **Testes de OTA em campo simulado**: Simular o cenário real de atualização OTA — dispositivo operando normalmente, recebe notificação de update, baixa firmware, instala, reboota, valida, e volta a operar. Testar com conectividade degradada (download lento, conexão intermitente), com firmware que falha no self-test (deve reverter automaticamente), e com múltiplos dispositivos atualizando simultaneamente. Se o OTA falhar em qualquer cenário de teste, NÃO é seguro fazer deploy para frota real — o risco de brickar dispositivos em campo é inaceitável.

- **Testes de escalabilidade do cloud**: Simular a carga esperada da frota completa no cloud — se a frota terá 1.000 dispositivos enviando dados a cada 30 segundos, gerar tráfego equivalente (33 mensagens/segundo) e verificar: latência de ingestão, throughput do pipeline de processamento, performance das queries no dashboard, e custo estimado do cloud com essa carga. Ferramentas como MQTT bench (mosquitto_pub em loop), Locust ou k6 podem simular a carga. Descobrir que o cloud não escala apenas quando a frota real cresce é o cenário de pior caso.

### Perguntas

1. O teste end-to-end (sensor → firmware → cloud → dashboard) foi executado com validação de precisão dos dados? [fonte: QA, Dev Firmware, Dev Cloud] [impacto: QA, Dev Firmware, Dev Cloud]
2. O soak test foi executado por pelo menos 72h contínuas sem memory leak, crash ou perda de mensagens? [fonte: QA, Dev Firmware] [impacto: Dev Firmware, QA]
3. O dispositivo foi testado nas condições ambientais reais de operação (temperatura, umidade, vibração, distância)? [fonte: QA, Engenharia de Campo] [impacto: Dev Firmware, Engenheiro de Hardware, QA]
4. Os testes de segurança foram executados (credenciais inválidas, firmware não assinado, extração de flash)? [fonte: Segurança da Informação, QA] [impacto: Dev Firmware, Dev Cloud]
5. O OTA foi testado com cenários de falha (download interrompido, firmware inválido, rollback automático)? [fonte: QA, Dev Firmware] [impacto: Dev Firmware, Dev Cloud]
6. A escalabilidade do cloud foi testada com carga simulada equivalente à frota projetada? [fonte: Dev Cloud, QA] [impacto: Dev Cloud, DevOps]
7. O consumo de energia real foi validado contra o orçamento de bateria definido na Discovery? [fonte: Dev Firmware, Engenheiro de Hardware] [impacto: Dev Firmware, Engenheiro de Hardware]
8. A reconexão automática do MQTT foi testada com múltiplos cenários de perda de conectividade? [fonte: QA, Dev Firmware] [impacto: Dev Firmware]
9. O comportamento fail-safe dos atuadores foi testado (perda de comunicação, crash de firmware, falta de energia)? [fonte: QA, Engenharia de Processo, Segurança do Trabalho] [impacto: Dev Firmware, Operações]
10. O procedimento de provisionamento em série foi validado com um lote de teste representativo? [fonte: Engenharia de Produção, Dev Firmware] [impacto: Dev Firmware, Operações]
11. Os alertas do dashboard de monitoramento foram testados (dispositivo inativo, bateria baixa, erro de sensor)? [fonte: Dev Cloud, Operações] [impacto: Dev Cloud, Operações]
12. A performance das queries do dashboard foi testada com volume de dados equivalente a 6 meses de operação? [fonte: Dev Cloud, QA] [impacto: Dev Cloud]
13. O backup e restauração do banco de dados de telemetria foram testados? [fonte: DevOps, Dev Cloud] [impacto: DevOps, Dev Cloud]
14. A documentação de operação em campo foi validada por alguém que NÃO participou do desenvolvimento? [fonte: Operações, QA] [impacto: Operações, Documentação]
15. Todos os bugs encontrados no QA foram corrigidos e re-testados, sem workarounds aceitos como solução? [fonte: Dev Firmware, Dev Cloud, QA] [impacto: Dev Firmware, Dev Cloud, QA]

---

## Etapa 09 — Launch Prep

- **Homologação e certificações**: Submeter o dispositivo final (hardware + firmware de produção) para certificação nos órgãos regulatórios necessários. ANATEL para dispositivos com rádio no Brasil (prazo típico: 4-8 semanas, custo: R$ 5.000-30.000 dependendo do tipo de dispositivo e laboratório). A submissão deve ser feita com o hardware de produção, não com o protótipo — qualquer alteração no hardware após a homologação pode invalidar o certificado. Manter cópia de toda a documentação técnica submetida (relatórios de teste EMC, SAR, manual do usuário) como evidência de compliance.

- **Firmware de produção (release candidate)**: Congelar o firmware em versão release candidate — sem features novas, apenas correções de bugs críticos. Compilar com flags de produção (otimização -O2 ou -Os, sem debug symbols, sem assertions, sem logs de debug que consumam flash/RAM). Gerar o binário final assinado e com hash publicado. O firmware de produção deve ser EXATAMENTE o binário que foi testado no QA — compilar novamente "para ter certeza" pode introduzir diferenças sutis. Versionar e arquivar o binário com sua cadeia de build completa (commit hash, versão de SDK, flags de compilação).

- **Plano de deploy da frota inicial**: Documentar o procedimento completo de deploy em campo: quem instala, com qual ferramenta (app mobile, console serial, provisionamento automático), em qual sequência (instalar hardware → provisionar → testar comunicação → confirmar no dashboard), e qual o critério de aceite por dispositivo (está reportando dados? dados fazem sentido?). Para frotas grandes, definir estratégia de deploy gradual — instalar 10% primeiro, monitorar por 24-48h, expandir. Definir também o procedimento de rollback em campo — se o dispositivo não funciona após instalação, qual é o plano B.

- **Treinamento da equipe de campo/operações**: Treinar as pessoas que vão instalar, operar e manter os dispositivos em campo — não apenas os desenvolvedores. O treinamento deve cobrir: instalação física (montagem, conexão, posicionamento de antena), provisionamento inicial (flash de firmware, registro no cloud), verificação de funcionamento (como confirmar que está transmitindo), troubleshooting básico (LED piscando vermelho = erro de conectividade, não reportou há 1h = verificar energia), e procedimento de substituição (remover dispositivo defeituoso, instalar novo, re-provisionar). Entregar manual de campo impresso ou em PDF — em locais remotos não há acesso à internet para consultar documentação online.

- **Monitoramento e alertas pré-go-live**: Configurar todos os alertas de monitoramento antes do deploy em campo: dispositivo offline há mais de X minutos, bateria abaixo de Y%, valor de sensor fora da faixa esperada, taxa de perda de mensagens acima de Z%, e erro de OTA. Definir os canais de notificação (e-mail, Slack, SMS, PagerDuty) e os responsáveis por cada tipo de alerta. Testar cada alerta antes do go-live — desligar um dispositivo de teste e verificar que o alerta é disparado dentro do tempo esperado.

- **Plano de rollback e contingência**: Documentar o plano de contingência para cada cenário de falha: firmware com bug crítico (rollback via OTA para versão anterior), cloud indisponível (dispositivos operam em modo offline com buffer local), dispositivo brickado em campo (procedimento de recovery via JTAG/UART, ou substituição), e falha de hardware (processo de RMA, estoque de unidades de reposição). Definir quem tem autoridade para acionar o rollback de OTA para toda a frota e em quais condições.

### Perguntas

1. As certificações regulatórias foram obtidas para o hardware e firmware de produção? [fonte: Regulatório, Engenharia de Produto] [impacto: PM, Jurídico]
2. O firmware release candidate foi compilado com flags de produção e é EXATAMENTE o binário testado no QA? [fonte: Dev Firmware] [impacto: Dev Firmware, QA]
3. O binário de produção está versionado, assinado e arquivado com cadeia de build completa? [fonte: Dev Firmware, DevOps] [impacto: Dev Firmware, DevOps]
4. O plano de deploy da frota inicial está documentado com procedimento passo a passo e critério de aceite? [fonte: Dev Firmware, Operações] [impacto: Operações, Dev Firmware, PM]
5. A estratégia de deploy gradual foi definida (% da frota por fase, tempo de observação entre fases)? [fonte: PM, Operações, Dev Firmware] [impacto: PM, Operações]
6. A equipe de campo/operações foi treinada em instalação, provisionamento, verificação e troubleshooting básico? [fonte: Dev Firmware, Operações] [impacto: Operações]
7. O manual de campo foi entregue em formato acessível offline (PDF, impresso)? [fonte: Dev Firmware, Documentação] [impacto: Operações]
8. Todos os alertas de monitoramento foram configurados e testados (offline, bateria, erro de sensor, falha de OTA)? [fonte: Dev Cloud, DevOps] [impacto: DevOps, Operações]
9. Os canais de notificação e responsáveis por cada tipo de alerta foram definidos e testados? [fonte: PM, DevOps, Operações] [impacto: Operações, DevOps]
10. O estoque de dispositivos de reposição para a frota inicial está disponível? [fonte: Compras, Operações] [impacto: Operações, PM]
11. O plano de rollback via OTA está documentado com critérios de acionamento e responsável autorizado? [fonte: Dev Firmware, Diretoria, Operações] [impacto: Dev Firmware, Operações, PM]
12. O procedimento de recovery de dispositivo brickado (JTAG/UART) está documentado e testado? [fonte: Dev Firmware] [impacto: Dev Firmware, Operações]
13. A infraestrutura cloud de produção foi validada com smoke test antes do deploy da frota real? [fonte: Dev Cloud, DevOps] [impacto: Dev Cloud, DevOps]
14. Todos os stakeholders foram notificados sobre data, local e procedimento do deploy da frota inicial? [fonte: PM, Diretoria] [impacto: PM, Operações]
15. O processo de RMA (devolução e substituição de dispositivo defeituoso) foi definido com fluxo e responsável? [fonte: Operações, Comercial, Jurídico] [impacto: Operações, PM]

---

## Etapa 10 — Go-Live

- **Deploy da frota inicial e validação em campo**: Executar a instalação dos dispositivos conforme o plano documentado na Launch Prep — seguindo o procedimento passo a passo, validando cada dispositivo individualmente (está reportando? dados fazem sentido?), e registrando qualquer desvio encontrado. O deploy inicial deve ser presenciado por pelo menos um engenheiro de firmware e um engenheiro de campo — o dev identifica problemas técnicos que o operador não percebe, e o operador identifica problemas práticos de instalação que o dev não antecipa. Documentar TUDO: fotos da instalação, posição de antena, qualidade de sinal medida, ID do dispositivo por localização.

- **Monitoramento intensivo pós-deploy (primeiras 48h)**: Monitorar ativamente todos os dispositivos nas primeiras 48h — taxa de report (todos estão enviando no intervalo esperado?), qualidade dos dados (valores dentro da faixa esperada?), estabilidade de conexão (reconexões frequentes indicam problema de sinal), e consumo de bateria (se aplicável — está alinhado com a projeção?). Ter um engenheiro de firmware e um engenheiro de cloud de plantão durante este período — problemas que aparecem nas primeiras horas com dispositivos reais em campo real são diferentes dos que aparecem no lab. Definir critérios claros de quando acionar o rollback da frota.

- **Validação de dados e calibração em campo**: Comparar os dados reportados pelos dispositivos com medições de referência no local de instalação — se o sensor reporta 28°C, confirmar com termômetro calibrado que a temperatura é realmente ~28°C. Diferenças sistemáticas indicam necessidade de calibração em campo (offset de sensor por condições locais). Diferenças aleatórias indicam problema de hardware ou firmware. Esta validação é especialmente crítica em aplicações industriais e agrícolas onde decisões de negócio serão tomadas com base nos dados — dados imprecisos são piores que dados ausentes.

- **Validação do pipeline de dados em produção**: Verificar que o pipeline completo funciona em produção com dados reais: telemetria chega ao broker → é processada corretamente → armazenada no database → exibida no dashboard com latência aceitável → alertas são disparados quando condições são atingidas. Verificar também que o volume de dados em produção está alinhado com o dimensionamento do cloud (billing, quotas, performance de queries). Discrepâncias entre o tráfego esperado e o real podem indicar dispositivos com firmware mal configurado (enviando dados com frequência errada) ou perda de dados silenciosa.

- **Handoff e documentação de operação**: Entregar formalmente ao cliente/operações: acesso ao dashboard de monitoramento com treinamento, acesso ao cloud com documentação de arquitetura, repositório de firmware com instruções de build e deploy, manual de operação em campo (instalação, troubleshooting, substituição), procedimento de OTA (como autorizar atualização, como monitorar, como reverter), e contrato de suporte com SLA definido. A documentação mais importante é o runbook de operação — documento que responde "o que fazer quando X acontece" para cada cenário de falha previsível, escrito para operadores que não são desenvolvedores.

- **Planejamento da expansão da frota**: Com a frota inicial validada, planejar a expansão — qual o cronograma de deploy das próximas fases, quantos dispositivos por fase, qual a capacidade de produção (se hardware custom), e qual o impacto no custo de cloud (escalar de 50 para 500 dispositivos pode mudar a tier de pricing). Documentar as lições aprendidas do deploy inicial (problemas de instalação, ajustes de firmware necessários, melhorias no procedimento) e incorporar no plano de expansão. O deploy da frota inicial é, na prática, um piloto — os aprendizados aqui definem o sucesso da escala.

### Perguntas

1. Todos os dispositivos da frota inicial foram instalados, provisionados e estão reportando dados ao cloud? [fonte: Operações, Dev Firmware] [impacto: Operações, Dev Firmware, PM]
2. A validação individual de cada dispositivo foi realizada (está reportando, dados fazem sentido, sinal adequado)? [fonte: Operações, Engenharia de Campo] [impacto: Operações, Dev Firmware]
3. O monitoramento intensivo das primeiras 48h foi executado com engenheiro de plantão disponível? [fonte: Dev Firmware, Dev Cloud, PM] [impacto: Dev Firmware, Dev Cloud, Operações]
4. Os dados dos dispositivos foram comparados com medições de referência no local de instalação? [fonte: Operações, Engenharia de Processo] [impacto: Dev Firmware, QA, Operações]
5. O pipeline de dados em produção foi validado end-to-end (broker → processamento → storage → dashboard → alertas)? [fonte: Dev Cloud, Operações] [impacto: Dev Cloud, Operações]
6. O volume de dados em produção está alinhado com o dimensionamento e o custo do cloud? [fonte: Dev Cloud, Financeiro] [impacto: Dev Cloud, PM]
7. Todos os alertas de monitoramento foram validados em produção com cenários reais? [fonte: DevOps, Operações] [impacto: DevOps, Operações]
8. O handoff formal ao cliente/operações foi realizado com entrega de todos os acessos e documentação? [fonte: PM, Dev Firmware, Dev Cloud] [impacto: PM, Operações]
9. O runbook de operação foi entregue e validado pelo time de operações? [fonte: Dev Firmware, Operações] [impacto: Operações]
10. O aceite formal de entrega foi obtido do cliente (documentado por escrito)? [fonte: Diretoria] [impacto: PM]
11. As lições aprendidas do deploy inicial foram documentadas para informar a expansão da frota? [fonte: PM, Operações, Dev Firmware] [impacto: PM, Operações]
12. O plano de expansão da frota (próximas fases, cronograma, capacidade de produção) foi elaborado? [fonte: Diretoria, Operações, Comercial] [impacto: PM, Operações]
13. O contrato de suporte pós-go-live foi ativado com SLA comunicado ao cliente? [fonte: Diretoria, PM] [impacto: PM, Operações, Dev Firmware]
14. A infraestrutura de OTA está validada em produção e pronta para enviar atualizações à frota? [fonte: Dev Firmware, Dev Cloud] [impacto: Dev Firmware, Dev Cloud]
15. O estoque de dispositivos de reposição é suficiente para cobrir falhas estimadas durante o período de suporte? [fonte: Compras, Operações] [impacto: Operações, PM]

---

## Anti-patterns por Etapa

Erros recorrentes que o entrevistador deve saber reconhecer. Se qualquer um desses padrões aparecer durante a conversa, é sinal de que algo precisa ser endereçado antes de avançar.

### Etapa 01 — Inception

- **"Vamos usar Raspberry Pi em produção"** — Raspberry Pi é excelente para prototipação, mas inadequado para produção em escala: custo unitário alto ($35-75), consumo de energia alto para battery-powered, sem certificação ANATEL/FCC por padrão, e supply chain instável (crise de chips 2021-2023 provou isso). O correto é prototipar com Raspberry Pi e migrar para MCU/SoC otimizado para produção.
- **"Certificação a gente vê depois"** — Certificações regulatórias (ANATEL, FCC, CE) podem exigir modificações no hardware, adicionar meses ao prazo, e custar dezenas de milhares de reais. Descobrir requisitos de certificação na Launch Prep significa redesign de hardware. Mapear na Inception é obrigatório.
- **"O hardware tá pronto, só falta o software"** — Hardware "pronto" sem firmware testado não é hardware pronto. Em projetos embarcados, hardware e firmware são interdependentes — bugs de hardware aparecem durante o desenvolvimento de firmware, e a interface entre os dois é definida iterativamente. Tratar como sequencial é garantia de retrabalho.

### Etapa 02 — Discovery

- **"O sensor é simples, é só ler o valor"** — Sensores no mundo real precisam de calibração, filtragem de ruído, tratamento de outliers, compensação de temperatura, e monitoramento de degradação. Um sensor de temperatura "simples" que retorna lixo a cada 100 leituras por interferência eletromagnética quebra toda a cadeia de decisão downstream se o firmware não tratar.
- **"Wi-Fi resolve, todo lugar tem"** — Wi-Fi não existe em campo agrícola, subsolo, área industrial afastada, ou veículos em movimento. Assumir Wi-Fi sem validar no local de operação é o erro mais comum em projetos IoT. Visita ao local de instalação para medir cobertura é requisito, não luxo.
- **"Não precisa funcionar offline, sempre vai ter internet"** — Em qualquer ambiente real, a conectividade falha periodicamente. Se o dispositivo não tem buffer local e retry, dados são perdidos silenciosamente. "Sempre tem internet" é premissa que será invalidada em campo.

### Etapa 03 — Alignment

- **"O time de hardware entrega a placa e o time de firmware faz funcionar"** — Sem colaboração contínua entre hardware e firmware, problemas de interface (pinout errado, timing de barramento, ruído em ADC) são descobertos tarde e custam caro. Hardware e firmware devem trabalhar juntos desde o primeiro protótipo.
- **"O formato dos dados a gente define quando chegar na implementação"** — Payload sem especificação formal gera incompatibilidade entre firmware e cloud — firmware envia em CBOR e cloud espera JSON, firmware usa Celsius e cloud assume Fahrenheit, timestamp sem timezone. Definir antes do Build é obrigatório.
- **"OTA é nice-to-have, a gente implementa depois"** — OTA precisa ser projetado no bootloader desde o início. Adicionar OTA a um firmware já em campo sem bootloader com A/B partition é impossível sem recall físico de todos os dispositivos. Decidir na Architecture, não no Build.

### Etapa 04 — Definition

- **Máquina de estados "na cabeça do dev"** — Sem documentação formal, cada desenvolvedor implementa transições diferentes, estados de erro são esquecidos, e o comportamento do dispositivo é inconsistente. A máquina de estados deve ser um diagrama aprovado antes de escrever uma linha de código.
- **"O payload é flexível, JSON com campos variáveis"** — Payload sem schema fixo torna o backend frágil (como parsear o que não tem contrato?) e desperdiça bandwidth em dispositivos com conectividade limitada (JSON verboso sobre LoRaWAN com 11 bytes de payload). Definir schema com versionamento é fundamental.
- **"Segurança a gente adiciona na versão 2"** — Sem secure boot, firmware pode ser clonado. Sem TLS, dados podem ser interceptados. Sem autenticação mútua, dispositivos falsos podem injetar dados. Segurança não é feature — é fundação que precisa existir desde a primeira versão.

### Etapa 05 — Architecture

- **"ESP32 porque é barato e todo mundo usa"** — ESP32 é excelente para muitos casos, mas tem consumo de energia em deep sleep (~10µA) muito superior a alternativas como nRF52 (~1µA) ou STM32L0 (~0.3µA). Para dispositivos battery-powered com anos de autonomia, ESP32 pode ser inadequado. Escolher por requisito, não por popularidade.
- **"Vamos hospedar o MQTT broker no nosso servidor"** — Self-hosting de MQTT broker (Mosquitto, EMQX) exige gestão de TLS, autenticação, alta disponibilidade, scaling, e monitoring. Para frotas pequenas e médias, serviços gerenciados (AWS IoT Core, HiveMQ Cloud) são mais confiáveis e frequentemente mais baratos que o custo de operação de infra própria.
- **"Os dados ficam no dispositivo, não precisa de cloud"** — Dispositivos sem cloud são silos de dados inacessíveis. Sem telemetria centralizada, não há visibilidade da frota, não há alertas, não há OTA, e não há analytics. Cloud não é obrigatório em todo projeto IoT, mas a decisão de não ter cloud precisa ser consciente e documentada com suas consequências.

### Etapa 06 — Setup

- **"Cada dev configura o ambiente como preferir"** — Variações de versão de toolchain entre desenvolvedores causam bugs irreproduciveis ("funciona na minha máquina"). Container Docker com toolchain fixo e versões lockadas é o padrão mínimo para firmware embarcado.
- **"Usa o mesmo broker para dev e produção"** — Dispositivo de teste publica dados inválidos no tópico de produção, ou regra de processamento em teste dispara alerta real. Ambientes separados são obrigatórios — broker, database e credenciais devem ser completamente isolados.
- **"A gente testa no hardware quando a placa chegar"** — Sem hardware disponível desde o Setup, o firmware é desenvolvido "no escuro" baseado apenas em datasheet. Testes unitários no host cobrem lógica de aplicação, mas não cobrem timing de periféricos, comportamento de deep sleep, e comunicação real com sensores. Hardware de teste disponível desde o dia 1 do Build é requisito.

### Etapa 07 — Build

- **"Funciona no protótipo, tá pronto"** — Protótipo funciona em condições ideais (25°C, Wi-Fi forte, alimentação USB estável). Produção opera em condições reais (45°C, sinal fraco, bateria com tensão variável). A diferença entre os dois é onde moram os bugs mais caros — testes com condições reais são obrigatórios antes de declarar o Build completo.
- **"OTA funciona, testei uma vez"** — OTA precisa ser testado em TODOS os cenários de falha — download interrompido, firmware corrompido, nova versão que não boota, queda de energia durante flash. Uma falha de OTA em campo pode brickar toda a frota. Testar cenários de sucesso não é suficiente.
- **"O consumo de energia a gente otimiza depois"** — Otimização de energia retrofitada é ordens de magnitude mais difícil que projetada desde o início. Periféricos que deveriam ser desligados em deep sleep, pull-ups que consomem corrente desnecessária, e firmware que não usa modos de low-power do MCU — tudo isso precisa ser implementado durante o Build, medido com power profiler, e validado contra o budget.

### Etapa 08 — QA

- **"Testou no lab, tá validado"** — Lab tem temperatura controlada, Wi-Fi forte, energia estável. Campo tem temperatura extrema, sinal fraco, vibração. Dispositivo que passa 100% no lab pode falhar 30% em campo. Testes em condições reais (ou simuladas com câmara climática e atenuador) são obrigatórios.
- **"Soak test de 4 horas é suficiente"** — Memory leak que consome 100 bytes por hora leva 40h para estourar um buffer de 4KB. Stack overflow que acontece em 1 a cada 1000 execuções de uma task pode levar dias para se manifestar. Soak test mínimo é 72h, idealmente 1-2 semanas.
- **"O cloud aguenta, é autoscaling"** — Autoscaling resolve para web apps com tráfego HTTP. IoT tem padrões diferentes — thundering herd quando toda a frota reconecta após queda de rede, burst de mensagens quando dispositivos enviam buffer acumulado durante offline, e conexões MQTT persistentes que consomem recursos constantes. Teste de carga IoT-specific é necessário.

### Etapa 09 — Launch Prep

- **"Vamos instalar tudo de uma vez"** — Deploy de toda a frota sem piloto é aposta de alto risco. Se o firmware tem bug que só aparece em campo, TODA a frota é afetada. Deploy gradual (10% → observar → 50% → observar → 100%) é a única abordagem responsável.
- **"O manual de campo é o README do GitHub"** — Operadores de campo não acessam GitHub, muitas vezes não têm internet no local de instalação, e precisam de instruções visuais passo a passo (fotos de como conectar, onde posicionar antena, qual LED indica sucesso). Manual em PDF/impresso com fotos é obrigatório.
- **"A equipe de operações entende de tecnologia"** — A equipe que instala e mantém dispositivos em campo tem skill set diferente de desenvolvedores. Assumir que entendem de firmware, MQTT, ou provisionamento é erro. Treinamento prático, presencial, com dispositivo real, é insubstituível.

### Etapa 10 — Go-Live

- **"Tá instalado e reportando, projeto encerrado"** — As primeiras 48h pós-deploy são as mais críticas. Dispositivos que funcionam na primeira hora podem falhar na décima segunda por thermal throttling, bateria drenando mais rápido que o esperado, ou buffer de armazenamento local enchendo. Monitoramento intensivo pós-deploy é parte do projeto.
- **"Se der problema, a gente faz OTA"** — OTA resolve problemas de firmware, mas não resolve problemas de hardware (sensor mal calibrado, antena mal posicionada, enclosure com infiltração). Se o problema é de hardware, a solução é visita presencial — e isso precisa estar previsto no plano de contingência.
- **"A expansão da frota é com o time de operações"** — Sem documentação das lições aprendidas do deploy inicial (problemas encontrados, ajustes necessários, melhorias no procedimento), a equipe de operações vai repetir os mesmos erros. Handoff sem knowledge transfer é projeto inacabado.

---

## Red Flags nas Respostas

Respostas que devem acionar alerta imediato durante a entrevista. Se o entrevistador ouvir qualquer uma destas, deve registrar como risco e escalar antes de avançar.

### Respostas de Reclassificação

Indicam que o projeto **não é sistema embarcado/IoT** e precisa ser reclassificado antes de continuar.

| Resposta do cliente | O que realmente significa | Ação |
|---|---|---|
| "O dispositivo é um app que roda num tablet fixo na parede" | App mobile/kiosk, não embarcado | Reclassificar para mobile-app ou web-app |
| "Os dados são inseridos manualmente pelo operador no dispositivo" | Sistema de coleta de dados manual, não IoT automatizado | Reclassificar para mobile-app ou web-app com formulários |
| "Precisa de tela touch grande com interface gráfica complexa" | HMI/kiosk, não embarcado típico | Reclassificar para aplicação de quiosque ou avaliar HMI industrial |
| "O dispositivo roda Android com apps do Google Play" | Smartphone/tablet, não embarcado | Reclassificar para mobile-app |
| "É basicamente uma integração entre dois sistemas existentes via API" | Middleware/integração, não IoT | Reclassificar para integration-middleware |

### Respostas de Bloqueio

Indicam que uma **dependência crítica não está resolvida** e o projeto não deve avançar sem resolver.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "O hardware ainda não existe, precisamos projetar tudo" | 01 | Cronograma subestimado em meses — design de PCB + fabricação + testes leva 3-6 meses | Replanejar cronograma incluindo hardware design como fase separada |
| "Não sabemos qual conectividade teremos no local" | 01 | Toda a arquitetura de comunicação depende disso | Realizar site survey antes de qualquer decisão técnica |
| "Precisamos de certificação ANVISA" | 01 | Dispositivo médico tem regulamentação própria que pode mudar todo o escopo | Consultar especialista regulatório antes de continuar |
| "Não temos hardware de teste disponível para o time de dev" | 03 | Firmware será desenvolvido sem testar em hardware real | Adquirir hardware de desenvolvimento antes de iniciar Build |
| "Os componentes têm lead time de 16 semanas" | 04 | Cronograma bloqueado por supply chain | Encomendar componentes imediatamente ou buscar alternativas |
| "Não temos expertise em firmware, vamos aprender durante o projeto" | 01 | Risco técnico extremo para projeto de produção | Contratar especialista ou reclassificar como PoC/aprendizado |

### Respostas de Alerta

Não bloqueiam, mas indicam **risco elevado** que deve ser monitorado.

| Resposta do cliente | Etapa | Risco | Ação |
|---|---|---|---|
| "A bateria precisa durar 5 anos" | 02 | Requisito extremo que restringe severamente MCU, protocolo e frequência de envio | Calcular budget de energia na Discovery antes de comprometer |
| "São 10.000 dispositivos na primeira fase" | 01 | Escala grande sem piloto validado é risco alto | Exigir piloto de 50-100 unidades antes da produção em massa |
| "O dispositivo vai ficar em área de difícil acesso" | 02 | Manutenção presencial é cara e demorada — firmware precisa ser ultra-robusto | Investir mais em OTA, diagnóstico remoto e testes de estabilidade |
| "Precisamos integrar com o sistema SCADA legado que roda DOS" | 02 | Integração com sistema legado sem documentação é risco técnico alto | Mapear protocolo exato e testar integração antes de estimar |
| "O firmware pode ser open-source, sem problema" | 05 | Firmware exposto facilita engenharia reversa e clonagem | Avaliar riscos de IP e segurança antes de decidir |
| "A gente atualiza o firmware via USB quando der problema" | 03 | Sem OTA, cada update exige visita presencial a cada dispositivo | Calcular custo de manutenção presencial × tamanho da frota |

---

## Critérios de Saída por Etapa (Gates)

Perguntas que **obrigatoriamente precisam ter resposta** antes de avançar para a próxima etapa. Se qualquer pergunta gate estiver sem resposta, a etapa não está concluída.

### Etapa 01 → 02

- Natureza do projeto definida — automação interna, produto para venda, ou PoC (pergunta 1)
- Status do hardware definido — existente ou a desenvolver (pergunta 2)
- Escala de produção e custo unitário alinhados (pergunta 3)
- Certificações regulatórias mapeadas (pergunta 4)
- Conectividade no ambiente de operação identificada (pergunta 6)

### Etapa 02 → 03

- Sensores e atuadores especificados com precisão e frequência (perguntas 1 e 2)
- Requisitos de autonomia de bateria quantificados (pergunta 3)
- Protocolos de comunicação obrigatórios identificados (pergunta 4)
- Condições ambientais de operação documentadas (pergunta 6)

### Etapa 03 → 04

- Divisão de responsabilidades hardware/firmware/cloud formalizada (pergunta 1)
- Formato de payload acordado entre firmware e cloud (pergunta 2)
- Hardware de teste disponível para o time de desenvolvimento (pergunta 3)
- Modelo de provisionamento de dispositivos definido (pergunta 5)

### Etapa 04 → 05

- BOM completo com second sources aprovado (pergunta 1)
- Schema de telemetria especificado campo a campo (pergunta 2)
- Máquina de estados documentada e aprovada (pergunta 3)
- Requisitos de segurança por camada especificados (pergunta 6)
- Documentação revisada por todas as disciplinas (pergunta 15)

### Etapa 05 → 06

- MCU/SoC e RTOS/OS escolhidos e justificados (perguntas 1 e 2)
- Plataforma cloud IoT escolhida com custo projetado (perguntas 3 e 10)
- Arquitetura de OTA definida (pergunta 4)
- Pipeline de dados arquitetado end-to-end (pergunta 5)
- Segurança end-to-end documentada (pergunta 7)

### Etapa 06 → 07

- Toolchain configurado e reproduzível por todos os devs (perguntas 1 e 2)
- Ambientes de cloud provisionados e isolados (perguntas 3 e 4)
- Dispositivos de teste provisionados e comunicando com cloud dev (pergunta 6)
- Pipeline de CI/CD testado end-to-end (pergunta 15)

### Etapa 07 → 08

- Drivers de hardware testados com hardware real (pergunta 1)
- Comunicação com cloud funcional incluindo cenários de desconexão (perguntas 3 e 4)
- Consumo de energia medido e dentro do budget (perguntas 6 e 7)
- Testes unitários passando no CI (pergunta 10)

### Etapa 08 → 09

- Teste end-to-end validado com dados reais (pergunta 1)
- Soak test de 72h+ sem falhas (pergunta 2)
- Testes em condições ambientais reais executados (pergunta 3)
- OTA testado com cenários de falha (pergunta 5)
- Escalabilidade do cloud validada (pergunta 6)

### Etapa 09 → 10

- Certificações obtidas (pergunta 1)
- Firmware de produção congelado e assinado (perguntas 2 e 3)
- Equipe de campo treinada (pergunta 6)
- Alertas de monitoramento configurados e testados (perguntas 8 e 9)
- Plano de rollback documentado (pergunta 11)

### Etapa 10 → Encerramento

- Frota inicial instalada e reportando (pergunta 1)
- Monitoramento intensivo de 48h executado (pergunta 3)
- Dados validados contra referência (pergunta 4)
- Handoff formal realizado com documentação (perguntas 8 e 9)
- Aceite formal obtido (pergunta 10)

---

## Estimativa de Esforço Relativo

Distribuição típica de esforço por etapa para cada variante de sistema embarcado/IoT. Escala de 1 (leve) a 5 (pesado). Ajuda o PM a planejar alocação e o entrevistador a calibrar a profundidade das perguntas.

| Etapa | V1 Sensor Node | V2 Gateway/Edge | V3 Atuador | V4 Wearable | V5 Produto OTA |
|---|---|---|---|---|---|
| 01 Inception | 2 | 2 | 3 | 3 | 3 |
| 02 Discovery | 3 | 3 | 4 | 3 | 3 |
| 03 Alignment | 2 | 3 | 3 | 3 | 3 |
| 04 Definition | 3 | 3 | 4 | 4 | 4 |
| 05 Architecture | 3 | 4 | 3 | 3 | 4 |
| 06 Setup | 2 | 3 | 2 | 3 | 3 |
| 07 Build | 3 | 4 | 5 | 5 | 4 |
| 08 QA | 3 | 3 | 5 | 4 | 4 |
| 09 Launch Prep | 2 | 2 | 3 | 3 | 3 |
| 10 Go-Live | 2 | 2 | 3 | 2 | 3 |
| **Total relativo** | **25** | **29** | **35** | **33** | **34** |

**Observações por variante:**

- **V1 Sensor Node**: Esforço concentrado na Discovery (requisitos de sensores e energia) e Build (drivers, otimização de consumo). Setup e Launch Prep são relativamente leves porque o dispositivo é simples e a frota é homogênea.
- **V2 Gateway/Edge**: Pico na Architecture (decisões de edge computing, protocolos de campo, Linux embarcado) e Build (múltiplas interfaces de comunicação, processamento local). A complexidade está na variedade de protocolos que o gateway precisa suportar.
- **V3 Atuador/Controle**: O mais pesado de todas as variantes — Build e QA são os maiores porque envolvem segurança operacional (fail-safe), testes de tempo real, e validação em condições reais. Um bug em atuador pode causar dano físico.
- **V4 Wearable**: Pico na Definition (interface de usuário com recursos limitados) e Build (BLE, app companion, otimização extrema de bateria e tamanho). A complexidade está na experiência do usuário com hardware fisicamente restrito.
- **V5 Produto com OTA**: Esforço distribuído uniformemente com pico na Architecture (OTA seguro, bootloader, versionamento) e QA (testes de OTA em todos os cenários de falha). A qualidade do OTA define se o produto pode evoluir ou fica congelado na versão de fábrica.

---

## Dependências entre Etapas

Respostas em etapas anteriores que tornam perguntas em etapas posteriores **irrelevantes** ou **obrigatórias**. O entrevistador deve usar esta tabela para pular perguntas que não se aplicam e reforçar as que se tornaram críticas.

### Decisões que eliminam perguntas

| Decisão (etapa) | Perguntas que se tornam irrelevantes |
|---|---|
| Hardware existente / módulo comercial (Etapa 01, pergunta 2) | Etapa 04: pergunta 1 (BOM e design de PCB), pergunta 13 (enclosure). Etapa 09: pergunta 1 (certificação — se módulo já é certificado). |
| Dispositivo alimentado por rede elétrica (Etapa 01, pergunta 7) | Etapa 02: pergunta 3 (autonomia de bateria). Etapa 07: pergunta 6 (medição de consumo) e pergunta 7 (validação de autonomia). Etapa 08: pergunta 7 (consumo vs. budget de bateria). |
| Sem OTA — firmware fixo (Etapa 01, pergunta 11) | Etapa 04: pergunta 7 (fluxo de OTA). Etapa 05: pergunta 4 (arquitetura de OTA). Etapa 06: pergunta 13 (ambiente de staging para OTA). Etapa 07: pergunta 5 (implementação de OTA). Etapa 08: pergunta 5 (testes de OTA). Etapa 09: pergunta 11 (rollback via OTA). |
| Dispositivo sem atuadores — apenas sensores (Etapa 02, pergunta 2) | Etapa 04: pergunta 11 (condições de fail-safe de atuadores). Etapa 05: RTOS pode não ser necessário se não há controle em tempo real. Etapa 08: pergunta 9 (teste de fail-safe de atuadores). |
| Sem necessidade de cloud — dados processados localmente (Etapa 01, pergunta 9) | Etapa 05: perguntas 3, 5, 6 (plataforma cloud, pipeline de dados, time-series DB). Etapa 06: perguntas 3, 4, 10, 11 (ambientes cloud, IaC, billing, MQTT policies). Etapa 08: pergunta 6 (escalabilidade cloud). |

### Decisões que adicionam perguntas obrigatórias

| Decisão (etapa) | Perguntas que se tornam obrigatórias ou críticas |
|---|---|
| Hardware custom a desenvolver (Etapa 01, pergunta 2) | Etapa 04: pergunta 1 (BOM com second sources) se torna bloqueadora. Etapa 09: pergunta 1 (certificações) se torna gate. Etapa 01: pergunta 15 (lead time de componentes) se torna crítica. |
| Dispositivo battery-powered com autonomia >1 mês (Etapa 01, pergunta 7) | Etapa 02: pergunta 3 (budget de energia) se torna gate. Etapa 05: pergunta 1 (MCU low-power) se torna crítica. Etapa 07: perguntas 6 e 7 (medição e validação de consumo) se tornam gates. |
| OTA habilitado (Etapa 01, pergunta 11) | Etapa 04: pergunta 7 (especificação de OTA) se torna gate. Etapa 05: pergunta 4 (arquitetura de OTA com A/B, rollback, assinatura) se torna bloqueadora. Etapa 07: pergunta 5 (testes de OTA com cenários de falha) se torna gate. Etapa 08: pergunta 5 (validação completa de OTA) se torna gate. |
| Dispositivo com atuadores de segurança crítica (Etapa 02, pergunta 2) | Etapa 04: pergunta 11 (condições de fail-safe) se torna bloqueadora. Etapa 05: pergunta 2 (RTOS obrigatório para real-time). Etapa 08: pergunta 9 (teste de fail-safe) se torna gate. |
| Frota >100 dispositivos (Etapa 01, pergunta 8) | Etapa 05: pergunta 8 (provisionamento em escala) se torna bloqueadora. Etapa 06: pergunta 7 (automação de provisionamento) se torna gate. Etapa 08: pergunta 6 (teste de escalabilidade cloud) se torna gate. Etapa 09: pergunta 5 (deploy gradual) se torna obrigatória. |
| Integração com sistema legado sem API documentada (Etapa 02, pergunta 8) | Etapa 03: pergunta 2 (formato de dados) requer investigação adicional. Etapa 04: spike técnico de integração se torna pré-requisito. Etapa 07: build da integração se torna o maior risco do cronograma. |
