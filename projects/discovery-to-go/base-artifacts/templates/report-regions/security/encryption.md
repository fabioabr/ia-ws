---
region-id: REG-SEC-03
title: "Criptografia"
group: security
description: "Estratégia de criptografia em trânsito e em repouso"
source: "Bloco #6 (cyber) → 1.6"
schema: "Tabela (camada, método, chave)"
template-visual: "Table simples"
default: false
---

# Criptografia

Documenta a estratégia de criptografia aplicada em cada camada do sistema, cobrindo dados em trânsito e em repouso. Assegura conformidade com padrões regulatórios e protege informações sensíveis contra acessos não autorizados.

## Schema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| camada | string | Onde a criptografia é aplicada |
| método | string | Algoritmo ou protocolo utilizado |
| chave | string | Gestão e rotação de chaves |

## Exemplo

| Camada | Método | Gestão de Chaves |
|--------|--------|-----------------|
| Trânsito (cliente → API) | TLS 1.3 | Certificados gerenciados via AWS Certificate Manager, renovação automática |
| Trânsito (serviço → serviço) | mTLS | Certificados internos via AWS Private CA |
| Repouso (banco de dados) | AES-256 (RDS encryption) | AWS KMS, CMK dedicada, rotação anual automática |
| Repouso (arquivos S3) | AES-256 (SSE-KMS) | AWS KMS, CMK dedicada, rotação anual automática |
| Campos sensíveis (CPF, dados bancários) | AES-256-GCM (application-level) | Envelope encryption via AWS KMS, rotação trimestral |
| Backups | AES-256 | Mesma CMK do banco, backups criptografados por padrão |

## Representação Visual

### Dados de amostra

A estratégia de criptografia pode ser representada como texto corrido resumindo a cobertura, complementado por uma tabela detalhada com status por camada.

**Texto corrido:** "Todas as camadas do FinTrack Pro possuem criptografia ativa. Dados em trânsito são protegidos por TLS 1.3 (cliente-API) e mTLS (serviço-serviço). Dados em repouso utilizam AES-256 via AWS KMS com chaves dedicadas (CMK) e rotação automática. Campos sensíveis como CPF e dados bancários recebem criptografia adicional em nível de aplicação (AES-256-GCM com envelope encryption)."

**Tabela com status de criptografia:**

| Camada | Método | Gestão de Chaves | Status |
|--------|--------|-----------------|--------|
| Trânsito (cliente → API) | TLS 1.3 | AWS Certificate Manager, renovação automática | Ativo |
| Trânsito (serviço → serviço) | mTLS | AWS Private CA | Ativo |
| Repouso (banco de dados) | AES-256 (RDS encryption) | AWS KMS, CMK dedicada, rotação anual | Ativo |
| Repouso (arquivos S3) | AES-256 (SSE-KMS) | AWS KMS, CMK dedicada, rotação anual | Ativo |
| Campos sensíveis (CPF, dados bancários) | AES-256-GCM (application-level) | Envelope encryption via AWS KMS, rotação trimestral | Ativo |
| Backups | AES-256 | Mesma CMK do banco, criptografia por padrão | Ativo |

### Formatos de exibição possíveis

| Formato | Descrição | Quando usar |
|---------|-----------|-------------|
| Texto corrido | Parágrafo narrativo resumindo a cobertura de criptografia por camada | Para visão executiva e contexto em documentos de compliance |
| Tabela com status | Tabela listando camada, método, gestão de chaves e status (Ativo/Pendente/Planejado) | Para documentação técnica completa e auditorias de segurança |
| Matriz de cobertura | Grid visual com ícones de cadeado mostrando quais camadas têm criptografia ativa | Para dashboards de postura de segurança |
| Diagrama em camadas | Diagrama mostrando as camadas do sistema com indicadores de criptografia em cada nível | Para apresentações de arquitetura de segurança |
| Scorecard | Card com percentual de cobertura e indicadores por tipo (trânsito, repouso, aplicação) | Para relatórios executivos de conformidade |

> [!info] Avaliação pendente
> Um especialista em visualização de dados deve avaliar qual formato gráfico melhor representa esta informação, considerando o público-alvo e o contexto de uso.
