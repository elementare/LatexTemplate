#!/usr/bin/env python3
import questionary
from datetime import datetime
from pathlib import Path

from latexgen.core import generate_project, PREAMBLE_OPTIONS, FONT_OPTIONS
from latexgen.utils import colored, extract_usepackages, get_messages

CONFIG_DIR = Path.home() / ".config" / "latexgen"


def main():
    messages = get_messages()

    lang = questionary.select(messages["select_language"], choices=["pt", "en"]).ask()
    msg = get_messages(lang)

    tipos = {
        "pt": ["Relatório", "Artigo", "Notas"],
        "en": ["Report", "Article", "Notes"]
    }
    tipo = questionary.select(msg["select_type"], choices=tipos[lang]).ask()
    preamb = questionary.select(msg["select_preamble"], choices=list(PREAMBLE_OPTIONS.keys())).ask()
    fonte = questionary.select(msg["select_font"], choices=list(FONT_OPTIONS.keys())).ask()

    titulo = questionary.text(msg["enter_title"]).ask()
    autor = questionary.text(msg["enter_author"]).ask()
    instituicao = ""
    if tipo.lower() in {"artigo", "article"}:
        instituicao = questionary.text(msg["enter_institution"]).ask()
    data = questionary.text(msg["enter_date"], default=datetime.today().strftime("%Y-%m-%d")).ask()
    pasta = questionary.text(msg["enter_project_folder"]).ask()

    themes = ["Default"] + sorted(f.stem for f in (CONFIG_DIR / "themes").glob("*.tex"))
    tema = questionary.select(msg["select_theme"], choices=themes).ask()

    selected_packages = None
    if PREAMBLE_OPTIONS[preamb] == "custom":
        raw = (CONFIG_DIR / "general.tex").read_text(encoding="utf-8")
        pkgs = extract_usepackages(raw)
        selected_packages = questionary.checkbox(msg["select_packages"], choices=pkgs).ask()

    config = {
        "general_tex": CONFIG_DIR / "general.tex",
        "templates_dir": CONFIG_DIR / "templates",
        "themes_dir": CONFIG_DIR / "themes"
    }

    generate_project(
        config, lang, tipo, preamb, fonte,
        titulo, autor, instituicao, data, pasta, tema, selected_packages, msg
    )

if __name__ == "__main__":
    main()

