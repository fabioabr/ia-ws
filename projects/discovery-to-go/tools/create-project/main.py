#!/usr/bin/env python3
"""
create-project — Cria a estrutura de pastas para um novo projeto de discovery.

Uso via CLI:
    python main.py "cliente/projeto"

Uso via skill:
    /po create-project "patria/teste"

Comportamento:
    - Se a pasta do cliente nao existe, cria copiando o client-template
    - Se a pasta do cliente ja existe, reutiliza
    - Se a pasta do projeto ja existe, aborta com mensagem
    - Se nao existe, cria copiando o project-template e o start-briefing.md

Requer: Python 3.10+
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # discovery-to-go/

PROJECTS_DIR = PROJECT_ROOT / "projects"
CLIENT_TEMPLATE = PROJECT_ROOT / "base" / "starter-kit" / "client-template"
PROJECT_TEMPLATE = CLIENT_TEMPLATE / "projects" / "project-n"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def copy_template(src: Path, dst: Path, exclude: set[str] | None = None) -> None:
    """Copy directory tree, skipping excluded folder names."""
    if exclude is None:
        exclude = set()
    for item in src.iterdir():
        if item.name in exclude:
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=False)
        else:
            shutil.copy2(item, target)


def slugify(name: str) -> str:
    """Convert name to kebab-case slug."""
    return name.strip().lower().replace(" ", "-").replace("_", "-")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def create_project(client_slug: str, project_slug: str) -> None:
    client_dir = PROJECTS_DIR / client_slug
    project_dir = client_dir / "projects" / project_slug

    # --- Client ---
    if client_dir.exists():
        print(f"[OK] Cliente '{client_slug}' ja existe em: {client_dir}")
    else:
        print(f"[+] Criando cliente '{client_slug}'...")
        client_dir.mkdir(parents=True, exist_ok=True)
        # Copy client-level folders (assets, config, kb, rules, templates)
        # but NOT the projects/ subfolder (we create the specific project below)
        copy_template(CLIENT_TEMPLATE, client_dir, exclude={"projects", "README.md"})
        # Create client README
        readme = client_dir / "README.md"
        readme.write_text(
            f"# {client_slug}\n\n"
            f"Pasta do cliente **{client_slug}**. "
            f"Projetos de discovery ficam em `projects/`.\n",
            encoding="utf-8",
        )
        # Create empty projects/ dir
        (client_dir / "projects").mkdir(exist_ok=True)
        (client_dir / "projects" / "README.md").write_text(
            f"# Projects — {client_slug}\n\n"
            f"Projetos de discovery do cliente {client_slug}.\n",
            encoding="utf-8",
        )
        print(f"[OK] Cliente criado: {client_dir}")

    # --- Project ---
    if project_dir.exists():
        print(f"\n[ERRO] Projeto '{project_slug}' ja existe em: {project_dir}")
        print("       Nenhuma alteracao foi feita.")
        sys.exit(1)

    print(f"[+] Criando projeto '{project_slug}'...")
    shutil.copytree(PROJECT_TEMPLATE, project_dir)

    # Verify start-briefing.md was copied
    setup_dir = project_dir / "setup"
    briefing_dst = setup_dir / "start-briefing.md"
    if briefing_dst.exists():
        print(f"[OK] start-briefing.md disponivel em: {briefing_dst}")
    else:
        print(f"[WARN] start-briefing.md nao encontrado no template. Verifique: {PROJECT_TEMPLATE / 'setup'}")

    # Update project README
    project_readme = project_dir / "README.md"
    project_readme.write_text(
        f"# {project_slug}\n\n"
        f"Projeto de discovery **{project_slug}** do cliente **{client_slug}**.\n\n"
        f"## Quick Start\n\n"
        f"1. Preencha `setup/start-briefing.md`\n"
        f"2. Execute `/orchestrator setup/start-briefing.md`\n"
        f"3. Acompanhe as 3 fases + Human Reviews\n",
        encoding="utf-8",
    )

    print(f"[OK] Projeto criado: {project_dir}")
    print()
    print("Proximos passos:")
    print(f"  1. Preencha: {briefing_dst}")
    print(f"  2. Execute:  /orchestrator {briefing_dst}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python main.py \"cliente/projeto\"")
        print("     python main.py patria/teste")
        sys.exit(1)

    arg = sys.argv[1].strip().strip('"').strip("'")

    if "/" not in arg:
        print(f"[ERRO] Formato invalido: '{arg}'")
        print("       Use: \"cliente/projeto\" (ex: patria/teste)")
        sys.exit(1)

    parts = arg.split("/", 1)
    client_slug = slugify(parts[0])
    project_slug = slugify(parts[1])

    if not client_slug or not project_slug:
        print("[ERRO] Cliente e projeto nao podem ser vazios.")
        sys.exit(1)

    print(f"=== create-project: {client_slug}/{project_slug} ===")
    print()
    create_project(client_slug, project_slug)


if __name__ == "__main__":
    main()
