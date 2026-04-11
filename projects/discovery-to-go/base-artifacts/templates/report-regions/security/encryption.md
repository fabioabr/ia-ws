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

### Recomendação do Chart Specialist

**Veredicto:** TABELA
**Tipo:** Tabela simples com colunas camada, método e gestão de chaves
**Tecnologia:** HTML/CSS
**Justificativa:** Dados de criptografia são técnicos e textuais (algoritmos, protocolos, políticas de chaves), sem valores numéricos ou categorias que justifiquem gráficos. Uma tabela simples e limpa é o formato mais eficiente para referência técnica e auditorias.
**Alternativa:** Scorecard com percentual de cobertura (HTML/CSS) — quando o público for executivo e o objetivo for mostrar a postura geral de criptografia em vez do detalhe por camada.
