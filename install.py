#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
from pathlib import Path

# ==========================
# 🔍 OS detection
# ==========================
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"
IS_MAC = platform.system() == "Darwin"

# ==========================
# 📁 Config directory
# ==========================
if IS_WINDOWS:
    CONFIG_DIR = Path.home() / ".latexgen"  # Avoid AppData, keep it clean
else:
    CONFIG_DIR = Path.home() / ".config" / "latexgen"  # Follow XDG spec

REPO_DIR = Path(__file__).resolve().parent
SRC_DIR = REPO_DIR / "latexgen"

# ==========================
# 🎨 Colored terminal output
# ==========================
def print_color(text, color="0"):
    print(f"\033[{color}m{text}\033[0m")

# ==========================
# 📂 Install config files
# ==========================
def install_config_files():
    print_color("📁 Copying config files...", "34")
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    for item in ["general.tex", "themes", "templates"]:
        src = REPO_DIR / "config" / item
        dst = CONFIG_DIR / item
        if dst.exists():
            if dst.is_dir():
                shutil.rmtree(dst)
            else:
                dst.unlink()
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

# ==========================
# 🐍 Install CLI via pipx
# ==========================
def install_with_pipx():
    print_color("🐍 Installing with pipx...", "36")
    try:
        subprocess.run(["pipx", "install", "."], cwd=REPO_DIR, check=True)
    except subprocess.CalledProcessError:
        print_color("❌ pipx install failed. Is pipx installed?", "31")
        exit(1)

# ==========================
# 🚀 Main installation
# ==========================
def main():
    print_color("🔧 Installing latexgen...", "35")
    install_config_files()
    install_with_pipx()
    print_color("✅ Installation complete! Run 'latexgen' to start.", "32")

if __name__ == "__main__":
    main()

