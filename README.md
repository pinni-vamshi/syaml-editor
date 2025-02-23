# SYAML Editor

SYAML Editor is a Python package that provides:

- **Live Text Styling**: Using markers in your `.syaml` files (e.g., `||bold some text||`, `||italic some text||`, `||underline some text||`), the package converts these to Markdown/HTML formats.
- **Language Server**: Powered by pygls, it offers hover functionality in editors supporting LSP (e.g., VS Code) to show formatted text.
- **Table Preview**: A Tkinter-based GUI that previews an editable table defined by the user. For example, running `syaml-preview 3 4` opens a window with a 3x4 table.

## Folder Structure

