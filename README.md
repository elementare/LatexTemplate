# 📄 LatexGen

`latexgen` is a CLI tool to generate pre-configured LaTeX project structures for reports, articles, and notes, with intelligent preamble customization for Physics, Chemistry, and Math. It supports multilingual templates (Portuguese and English), package selection, font customization, and color themes.

---

## ✨ Features

- 🇧🇷🇺🇸 Supports Portuguese and English templates
- 📁 Automatic creation of folder structure (`text/`, `images/`, `references.bib`)
- 🧠 Intelligent preambles (Physics, Math, Chemistry, or Custom)
- 🧩 Package selector for custom builds
- 🎨 Theme support for color schemes
- 🔤 Math font selector (Fourier, Palatino, Times, etc.)
- ⚙️ Works with `pipx` on **Linux, macOS, and Windows**

---

## 🚀 Installation

### 📦 Requirements

- Python 3.8+
- [pipx](https://pypa.github.io/pipx/) installed

### ✅ Linux/macOS

```bash
git clone https://github.com/your-user/latexgen.git
cd latexgen
python3 install.py
```

### ✅ Windows

Open **PowerShell** and run:

```powershell
git clone https://github.com/your-user/latexgen.git
cd latexgen
python install.py
```

Make sure you’ve installed `pipx`:

```powershell
pip install --user pipx
pipx ensurepath
```

---

## 🧪 Usage

After installation, run:

```bash
latexgen
```

You’ll be guided through:

- Language selection
- Document type (report, article, notes)
- Preamble type (Physics, Math, Chemistry, Custom)
- Font choice
- Title, author, institution, date
- Color theme
- Folder name

---

## 🛠 File Structure

```
project/
│
├── main.tex
├── references.bib
├── color_theme.tex
├── images/
└── text/
    ├── introducao.tex
    ├── metodologia.tex
    └── ...
```

---

## 📁 Configuration Directory

All templates, themes, and the general preamble live in:

- Linux/macOS: `~/.config/latexgen`
- Windows: `%APPDATA%\latexgen`

You can customize them freely.

---

## 💖 License

MIT — do whatever you want, no warranty.
