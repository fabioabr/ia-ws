---
region-id: REG-PROD-09
title: "Product Vision"
group: product
description: "Elevator pitch + horizonte 3 anos + princípios de produto"
source: "Bloco #1 (po) → 1.1"
schema: "text"
template-visual: "Card com quote style"
default: false
---

# Product Vision

Declaração aspiracional de longo prazo do produto, combinando o elevator pitch com a visão de onde o produto estará em 3 anos e os princípios que guiarão a evolução. Diferente da proposta de valor (focada no presente e na diferenciação), a visão de produto olha para o futuro e define a direção estratégica. Serve como norte para decisões de roadmap e para atrair talentos e parceiros.

## Schema de dados

| Campo | Tipo | Formato |
|-------|------|---------|
| elevator_pitch | string | 2-3 frases descrevendo o produto e seu valor central |
| visao_3_anos | string | Descrição narrativa de como o produto será em 3 anos |
| principios | list | 3-5 princípios que guiam decisões de produto |

## Exemplo

```markdown
## Visão do Produto

### Elevator Pitch

> O FinTrack Pro transforma a consolidação financeira de um processo manual, lento e propenso a erros em uma operação automatizada, auditável e em tempo real. Equipes de controladoria deixam de ser operadoras de planilhas para se tornarem analistas estratégicas do negócio.

### Onde estaremos em 3 anos (2029)

Em 2029, o FinTrack Pro será a plataforma de referência para consolidação financeira de empresas mid-market na América Latina. Mais de 200 empresas utilizarão a plataforma para consolidar dados de milhares de filiais em tempo real, com compliance automático para IFRS, CPC e regulações locais.

A plataforma terá evoluído de uma ferramenta de consolidação para um **hub de inteligência financeira**, com:
- Predição de fechamento (estimativa de resultado antes do fechamento oficial)
- Detecção de anomalias com ML (identificação automática de lançamentos atípicos)
- Benchmarking anônimo entre clientes do mesmo segmento
- Marketplace de conectores para ERPs e sistemas contábeis regionais

O time-to-value será de **2 dias** para empresas com ERPs suportados, com onboarding self-service e templates por indústria.

### Princípios de produto

1. **O controller é o herói** — toda feature deve empoderar o controller, nunca complicar seu trabalho
2. **Dados confiáveis ou nada** — preferimos atrasar uma feature a entregar dados que não são 100% rastreáveis
3. **Complexidade no motor, simplicidade na tela** — regras IFRS complexas devem ser abstraídas em configurações simples
4. **Latin America first** — priorizamos regulações, moedas e ERPs da América Latina antes de expandir globalmente
5. **Open by default** — APIs abertas, exports flexíveis, sem lock-in de dados
```
