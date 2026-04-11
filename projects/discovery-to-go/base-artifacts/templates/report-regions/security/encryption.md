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
