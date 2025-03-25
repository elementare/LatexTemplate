import shutil
from pathlib import Path

from latexgen.utils import extract_usepackages, filter_preamble, FONT_OPTIONS

PREAMBLE_OPTIONS = {
    "Default (Completo)": None,
    "Física": {
        "amsmath", "amssymb", "amsthm", "mathtools", "physics", "tikz",
        "graphicx", "circuitikz", "pgfplots", "geometry", "hyperref",
        "babel", "inputenc", "fontenc"
    },
    "Matemática": {
        "amsmath", "amssymb", "amsthm", "mathtools", "mathrsfs",
        "esint", "esvect", "geometry", "hyperref", "babel", "fontenc", "inputenc"
    },
    "Química": {
        "amsmath", "amssymb", "mhchem", "chemfig", "graphicx", "geometry",
        "babel", "inputenc", "fontenc", "hyperref"
    },
    "Customizado": "custom"
}

def generate_project(config, lang, tipo, preamb, fonte, titulo, autor, instituicao, data, pasta, tema, selected_packages, msg):
    general_raw = config["general_tex"].read_text(encoding="utf-8")

    if PREAMBLE_OPTIONS[preamb] == "custom":
        general_filtered = filter_preamble(general_raw, set(selected_packages))
    elif PREAMBLE_OPTIONS[preamb] is None:
        general_filtered = general_raw
    else:
        general_filtered = filter_preamble(general_raw, PREAMBLE_OPTIONS[preamb])

    idioma_babel = "brazilian" if lang == "pt" else "english"
    general_filtered = general_filtered.replace(r"\usepackage[main={lang}]{babel}", rf"\usepackage[main={idioma_babel}]{{babel}}")
    general_filtered = general_filtered.replace("{fontpkg}", FONT_OPTIONS[fonte])

    template_path = config["templates_dir"] / lang / f"{tipo.lower()}.tex"
    template = template_path.read_text(encoding="utf-8")
    template = (
        template.replace("{titulo}", titulo)
                .replace("{autor}", autor)
                .replace("{instituicao}", instituicao)
                .replace("{data}", data)
                .replace("{general}", general_filtered)
                .replace("{theme}", "color_theme.tex")
    )

    project_dir = Path.cwd() / pasta
    if project_dir.exists():
        print(msg["error_exists"])
        return

    (project_dir / "text").mkdir(parents=True)
    (project_dir / "images").mkdir()
    (project_dir / "references.bib").write_text("% Bibliografia", encoding="utf-8")
    (project_dir / "main.tex").write_text(template, encoding="utf-8")

    if tema == "Default":
        (project_dir / "color_theme.tex").write_text("% Tema padrão", encoding="utf-8")
    else:
        shutil.copy(config["themes_dir"] / f"{tema}.tex", project_dir / "color_theme.tex")

    section_map = {
        "Relatório": ["introducao", "objetivos", "metodologia", "resultados", "conclusao"],
        "Artigo": ["resumo", "introducao", "metodologia", "resultados", "conclusao"],
        "Notas": ["notas"],
        "Report": ["intro", "objectives", "methodology", "results", "conclusion"],
        "Article": ["abstract", "intro", "methodology", "results", "conclusion"],
        "Notes": ["notes"]
    }
    for sec in section_map.get(tipo, []):
        (project_dir / "text" / f"{sec}.tex").write_text(f"% {sec.capitalize()} content", encoding="utf-8")

    print(msg["success"])
    print(msg["created"].format(dir=project_dir))

