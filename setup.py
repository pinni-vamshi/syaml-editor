from setuptools import setup, find_packages

setup(
    name="syaml-editor",
    version="1.0.0",
    description="A tool for live SYAML styling and table preview (with a language server and Tkinter preview).",
    author="Your Name",
    packages=find_packages(),
    install_requires=["pygls"],  # Tkinter is included in the Python stdlib
    entry_points={
        "console_scripts": [
            "syaml-language-server = syaml_editor.language_server:main",
            "syaml-preview = syaml_editor.preview:main"
        ]
    },
)
