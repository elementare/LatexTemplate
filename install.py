#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
from pathlib import Path

# Detect OS
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"
IS_MAC = platform.system() == "Darwin"

# Define paths
if IS_WINDOWS:
    CONFIG_DIR = Path(os.getenv("APPDATA")) / "latexgen"
else:
    CONFIG_DIR = Path.home() / ".config" / "latexgen"

REPO_DIR = Path(__file__).resolve().parent
SRC_DIR = REPO_DIR / "latexgen"

def print_color(text, color="0"):
    print(f"\033[{color}m{text}\033[0m")

def install_config_files():
    print_color("📁 Copying config files...", "34")
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    for item in ["config/general.tex", "config/themes", "config/templates"]:
        src = REPO_DIR / item
        dst = CONFIG_DIR / item
        if dst.exists():
            shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
        shutil.copytree(src, dst) if src.is_dir() else shutil.copy2(src, dst)

def install_with_pipx():
    print_color("🐍 Installing with pipx...", "36")
    try:
        subprocess.run(["pipx", "install", "."], cwd=REPO_DIR, check=True)
    except subprocess.CalledProcessError:
        print_color("❌ pipx install failed. Is pipx installed?", "31")
        exit(1)

def main():
    print_color("🔧 Installing latexgen...", "35")
    install_config_files()
    install_with_pipx()
    print_color("✅ Installation complete! Run 'latexgen' to start.", "32")

if __name__ == "__main__":
    main()

