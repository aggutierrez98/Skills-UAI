#!/usr/bin/env python3
"""Chequeos locales de estructura y enlaces, sin dependencias externas ni red."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "tp-uml-y-casos-de-uso/SKILL.md",
    "tp-delivery-standards/SKILL.md",
    "tp-delivery-standards/embedded-skills/plantuml/SKILL.md",
    "publicar-diagramas-google-docs/SKILL.md",
)


def prose(text):
    """Omitir ejemplos de enlaces dentro de fences y codigo inline."""
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append(re.sub(r"(`+).*?\1", "", line))
    return "\n".join(result)


def main():
    errors = []
    for name in SKILLS:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"Falta skill: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        front = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
        if not front or any(not re.search(rf"^{key}:\s*\S", front[1], re.M)
                            for key in ("name", "description")):
            errors.append(f"Frontmatter incompleto: {name}")
    checked = 0
    for path in ROOT.rglob("*.md"):
        if any(part in (".git", ".venv", "venv", "node_modules", "salidas", ".tmp")
               for part in path.relative_to(ROOT).parts):
            continue
        checked += 1
        for dest in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose(path.read_text(encoding="utf-8"))):
            url = urlsplit(dest)
            if url.scheme or dest.startswith("//") or not url.path:
                continue
            target = path.parent / unquote(url.path)
            if not target.exists():
                errors.append(f"Enlace local roto: {path.relative_to(ROOT)} -> {dest}")
    examples = list((ROOT / "ejemplos" / "diagramas").glob("*.puml"))
    if not examples:
        errors.append("Faltan ejemplos PlantUML")
    for path in examples:
        text = path.read_text(encoding="utf-8")
        if len(re.findall(r"^@startuml\s*$", text, re.M)) != 1 or len(re.findall(r"^@enduml\s*$", text, re.M)) != 1:
            errors.append(f"Ejemplo sin un bloque UML completo: {path.name}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(SKILLS)} skills, {checked} Markdown y {len(examples)} ejemplos; enlaces locales validos.")
    print("No se verificaron URLs externas, sintaxis PlantUML ni conectores de Google.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
