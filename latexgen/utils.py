import re

FONT_OPTIONS = {
    "Latin Modern (default)": r"\usepackage{lmodern}",
    "Fourier": r"\usepackage{fourier}",
    "Libertinus": r"\usepackage{libertinus}",
    "Times (newtx)": r"\usepackage{newtxtext,newtxmath}",
    "Palatino (mathpazo)": r"\usepackage{mathpazo}",
    "Charter (mathdesign)": r"\usepackage[charter]{mathdesign}",
    "Computer Modern (default TeX)": ""
}

def extract_usepackages(text):
    matches = re.findall(r"\\usepackage(?:\[[^\]]*\])?\{([^\{\}]+)\}", text)
    pkgs = set()
    for group in matches:
        if "{{" in group or "}}" in group:
            continue
        for pkg in group.split(","):
            pkgs.add(pkg.strip())
    return sorted(pkgs)

def filter_preamble(text, allowed):
    lines = text.splitlines()
    result = []
    for line in lines:
        if "\\usepackage" in line:
            pkgs = extract_usepackages(line)
            if all(pkg in allowed for pkg in pkgs):
                result.append(line)
        else:
            result.append(line)
    return "\n".join(result)

def colored(text, color="default"):
    colors = {
        "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36", "default": "0"
    }
    return f"\033[{colors[color]}m{text}\033[0m"

def get_messages(lang="pt"):
    if lang == "en":
        return {
            "select_language": "🌐 Select language:",
            "select_type": "📄 Select document type:",
            "select_preamble": "🧠 Select preamble type:",
            "select_font": "🔤 Select math font:",
            "enter_title": "✍️ Enter document title",
            "enter_author": "✍️ Enter author name",
            "enter_institution": "🏛️ Enter institution (optional)",
            "enter_date": "📅 Enter date",
            "enter_project_folder": "📁 Enter project folder name",
            "select_theme": "🎨 Select a color theme:",
            "select_packages": "✅ Select packages to keep:",
            "success": colored("🚀 Project created successfully!", "green"),
            "created": colored("📂 Directory: {dir}", "yellow"),
            "error_exists": colored("❌ Folder already exists!", "red")
        }
    return {
        "select_language": "🌐 Selecione o idioma:",
        "select_type": "📄 Tipo de documento:",
        "select_preamble": "🧠 Tipo de preâmbulo:",
        "select_font": "🔤 Fonte matemática:",
        "enter_title": "✍️ Título do documento",
        "enter_author": "✍️ Nome do autor",
        "enter_institution": "🏛️ Instituição (opcional)",
        "enter_date": "📅 Data",
        "enter_project_folder": "📁 Nome da pasta do projeto",
        "select_theme": "🎨 Tema de cor:",
        "select_packages": "✅ Selecione os pacotes a manter:",
        "success": colored("🚀 Projeto criado com sucesso!", "green"),
        "created": colored("📂 Pasta criada: {dir}", "yellow"),
        "error_exists": colored("❌ A pasta já existe!", "red")
    }

