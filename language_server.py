from pygls.lsp.server import LanguageServer
from lsprotocol.types import Hover, HoverParams
from syaml_editor.formatter import format_text

server = LanguageServer("syaml-language-server", "1.0")

@server.feature("textDocument/hover")
def on_hover(params: HoverParams) -> Hover:
    """
    When hovering over text, return the formatted version.
    """
    doc = server.workspace.get_document(params.text_document.uri)
    # Process the SYAML content (e.g., converting ||bold text|| to markdown)
    styled_text = format_text(doc.source)
    return Hover(contents=styled_text)

def main():
    server.start_io()

if __name__ == '__main__':
    main()
