---
name: get-flaticon
argument-hint: "<pack-url> <output-folder>"
title: get-flaticon
description: "Baixa em lote ícones PNG 128px de um pack do Flaticon para uma pasta local usando Playwright stealth. Use SEMPRE que precisar: baixar ícones de um pack do Flaticon, fazer download em lote de ícones PNG, ou obter ícones para usar em projetos/reports. Requer URL do pack e pasta de destino. NÃO use para: criar diagramas (use diagram-drawio), gerar HTML (use html-writer), ou buscar ícones de outras fontes (Remix Icon já está no design system via CDN)."
project-name: global
version: 01.01.000
author: claude-code
license: MIT
status: ativo
category: utility
area: tecnologia
tags:
  - scraping
  - flaticon
  - download
  - icons
  - playwright
created: 2026-04-10 12:00
inputs:
  - name: url
    type: string
    required: true
    description: URL da página de pack do Flaticon (ex. https://www.flaticon.com/packs/files-8)
  - name: base-folder
    type: file-path
    required: true
    description: Pasta raiz onde será criada a subpasta {set-name}/ com os ícones
outputs:
  - name: icons
    type: file
    format: png
    description: Arquivos PNG 128px baixados na pasta {base-folder}/{set-name}/
---

# Get Flaticon — Scraper de Ícones

Você é o **Get Flaticon** — responsável por extrair e baixar em lote todos os ícones PNG 128px de uma página de pack do Flaticon, organizando-os em uma pasta local nomeada pelo set.

**Argumentos:** $ARGUMENTS

Esperados (nesta ordem):

1. `url` — URL da página de pack do Flaticon (ex.: `https://www.flaticon.com/packs/files-8`)
2. `base-folder` — pasta raiz onde será criada a subpasta `{set-name}/` com os ícones

Se **qualquer** argumento estiver faltando, **pergunte ao usuário** antes de continuar. Nunca infira valores.

---

## 📋 Instructions

### 0. Pré-requisitos

> [!danger] Flaticon usa Akamai Bot Manager
> A página **NÃO** pode ser obtida com `curl`, `WebFetch`, `urllib` ou mesmo `curl_cffi`. O Akamai exige execução real de JavaScript para liberar o HTML. A única forma confiável é **Playwright + playwright-stealth** com Chromium headless.

Pacotes Python necessários (instalar uma única vez no ambiente):

```bash
pip install playwright playwright-stealth
python -m playwright install chromium
```

Se já estiverem instalados (verificável com `python -c "import playwright_stealth"`), pule esta etapa.



### 1. Validar argumentos

- Confirme que `url` e `base-folder` foram informados em `$ARGUMENTS`.
- Se faltar qualquer um, pergunte ao usuário qual é o valor. **Não chute.**
- Verifique que a `url` começa com `https://www.flaticon.com/`. Se não começar, avise e pare.

### 2. Verificar dependências

Execute `python -c "from playwright_stealth import Stealth; from playwright.sync_api import sync_playwright"` via `Bash`. Se falhar com `ModuleNotFoundError`, rode o bloco de instalação da seção **Pré-requisitos** e repita a verificação.

### 3. Executar o script de scraping e download

Rode o script abaixo via `Bash` com `python`, substituindo `<URL>` e `<BASE_FOLDER>` pelos valores reais. O script faz tudo: abre Chromium stealth, resolve o challenge do Akamai, extrai o `set-name` e as `contentUrl` usando o DOM real da página, cria a pasta e baixa cada PNG.

```python
import re, sys, urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

URL         = r"<URL>"
BASE_FOLDER = Path(r"<BASE_FOLDER>")
UA          = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

# -- 1) Abrir Chromium stealth e extrair dados via DOM
with Stealth().use_sync(sync_playwright()) as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--disable-blink-features=AutomationControlled"],
    )
    ctx = browser.new_context(
        user_agent=UA,
        locale="en-US",
        viewport={"width": 1366, "height": 900},
    )
    page = ctx.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    try:
        page.wait_for_selector(
            "#pack-view__inner section.search-result ul > li",
            state="attached",
            timeout=45000,
        )
    except Exception as e:
        print(f"ERRO: grid nao carregou (possivel bloqueio): {e}", file=sys.stderr)
        browser.close()
        sys.exit(2)

    data = page.evaluate(r"""
    () => {
        const out = {urls: [], setName: null};
        const h1 = document.querySelector('#pack-view__inner section h1');
        if (h1) {
            const sp = h1.querySelector('span');
            out.setName = (sp ? sp.textContent : h1.textContent).replace(/\s+/g, ' ').trim();
        }
        const lis = document.querySelectorAll('#pack-view__inner section.search-result ul > li');
        const seen = new Set();
        for (const li of lis) {
            const sc = li.querySelector('script[type="application/ld+json"]');
            if (!sc) continue;
            try {
                const j = JSON.parse(sc.textContent);
                const arr = Array.isArray(j) ? j : [j];
                for (const o of arr) {
                    if (o && o.contentUrl && !seen.has(o.contentUrl)) {
                        seen.add(o.contentUrl);
                        out.urls.push(o.contentUrl);
                    }
                }
            } catch (e) {}
        }
        return out;
    }
    """)
    browser.close()

set_name = data.get("setName") or "flaticon-pack"
urls     = data.get("urls") or []

if not urls:
    print("ERRO: nenhum contentUrl encontrado no grid", file=sys.stderr)
    sys.exit(3)

# -- 2) Sanitizar set-name para nome de pasta valido no Windows
safe_set = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", set_name).strip(" .") or "flaticon-pack"
dest     = BASE_FOLDER / safe_set
dest.mkdir(parents=True, exist_ok=True)

# -- 3) Download em lote (idempotente + resiliente)
downloaded = skipped = errors = 0
failed = []
for cu in urls:
    fname = cu.rsplit("/", 1)[-1].split("?", 1)[0] or "icon.png"
    out   = dest / fname
    if out.exists() and out.stat().st_size > 0:
        skipped += 1
        continue
    try:
        req = urllib.request.Request(cu, headers={"User-Agent": UA, "Referer": URL})
        with urllib.request.urlopen(req, timeout=30) as r, open(out, "wb") as f:
            f.write(r.read())
        downloaded += 1
    except Exception as e:
        errors += 1
        failed.append((cu, str(e)))
        try:
            if out.exists() and out.stat().st_size == 0:
                out.unlink()
        except Exception:
            pass

print(f"set-name        : {set_name}")
print(f"pasta destino   : {dest}")
print(f"total encontrado: {len(urls)}")
print(f"baixados        : {downloaded}")
print(f"pulados (existia): {skipped}")
print(f"erros           : {errors}")
if failed:
    print("\nFALHAS:")
    for u, e in failed:
        print(f"  - {u}  ->  {e}")
```

### 4. Relatório final ao usuário

Apresente, de forma compacta:

- ✅ **Set:** `{set-name}`
- 📁 **Pasta:** `{base-folder}/{safe-set}/`
- 📦 **Total encontrado:** N
- ⬇️ **Baixados:** N
- ⏭️ **Pulados (já existiam):** N
- ❌ **Erros:** N (listar URLs que falharam, se houver)

## 📄 Examples

### Exemplo 1 — Download de pack completo (primeira execução)

**Input:** `/get-flaticon https://www.flaticon.com/packs/files-8 E:\assets\flaticon`
**Output:**
```
set-name        : Icon Pack: Files
pasta destino   : E:\assets\flaticon\Icon Pack Files
total encontrado: 40
baixados        : 40
pulados (existia): 0
erros           : 0
```

### Exemplo 2 — Re-execução idempotente (mesma URL)

**Input:** `/get-flaticon https://www.flaticon.com/packs/files-8 E:\assets\flaticon`
**Output:**
```
set-name        : Icon Pack: Files
pasta destino   : E:\assets\flaticon\Icon Pack Files
total encontrado: 40
baixados        : 0
pulados (existia): 40
erros           : 0
```
Todos os 40 ícones já existiam na pasta — nenhum re-download realizado.

## 🚫 Constraints

- Nunca inferir argumentos — se `url` ou `base-folder` não vierem em `$ARGUMENTS`, perguntar ao usuário
- A URL deve começar com `https://www.flaticon.com/` — rejeitar qualquer outra
- Playwright + playwright-stealth é obrigatório — `curl`, `curl_cffi`, `WebFetch` e Playwright puro falham contra o Akamai Bot Manager
- Usar `page.evaluate()` com DOM real e seletor `#pack-view__inner section.search-result ul > li`, nunca regex em HTML
- `wait_for_selector` deve usar `state="attached"` (não `visible`, pois `<script>` não é visível)
- Sanitizar o `set-name` removendo caracteres inválidos para o FS do Windows (`<>:"/\\|?*`)
- Idempotência: se o arquivo já existe e tem tamanho > 0, pular sem sobrescrever
- Resiliência: um download falho não interrompe o batch — acumular erros e reportar no final
- Download dos PNGs usa `urllib` normal (CDN não tem WAF) — Playwright só para a página de listagem
- Conteúdo em pt-BR com acentuação correta em toda comunicação com o usuário

## 🔧 claude-code

### Trigger
Keywords no `description` do frontmatter: flaticon, ícones, icons, scraper, download icons. O Claude Code usa o campo `description` para decidir quando invocar a skill automaticamente.

### Arguments
Usar `$ARGUMENTS` no corpo para capturar os parâmetros passados pelo usuário via `/get-flaticon <url> <base-folder>`. Espera dois argumentos posicionais na ordem: URL do pack e pasta base de destino.

### Permissions
- bash: true
- file-read: true
- file-write: true
- web-fetch: false

## 🔗 Documentos Relacionados

- `conventions/frontmatter/document-schema.md` — Schema de frontmatter para documentos
- `conventions/frontmatter/skill-schema.md` — Schema de frontmatter para skills

## 📜 Histórico de Alterações

| Versão | Data | Descrição |
|--------|------|-----------|
| 01.01.000 | 2026-04-10 | Adequação ao skill-schema com herança de document-schema; adição de campos title, project-name, area, created, license; emojis em H2; seções Documentos Relacionados e Histórico |
