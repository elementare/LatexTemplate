from setuptools import setup, find_packages

setup(
    name="latexgen",
    version="1.0.0",
    author="elementare",
    description="Geração de projetos LaTeX interativos com preâmbulo customizável",
    packages=find_packages(),  # Certifique-se que a pasta tenha __init__.py
    include_package_data=True,
    install_requires=[
        "questionary",
    ],
    entry_points={
        "console_scripts": [
            "latexgen=latexgen.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
)

