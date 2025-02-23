from pylsp import lsp, LanguageServer
from syaml_editor.formatter import format_text

server = LanguageServer()

@server.feature(lsp.HOVER)
def on_hover(params):
    """
    When hovering over text, return the formatted version.
    """
    doc = server.workspace.get_document(params['textDocument']['uri'])
    # Process the SYAML content (e.g. converting ||bold text|| to markdown)
    styled_text = format_text(doc.source)
    return {'contents': styled_text}

def main():
    server.start_io()

if __name__ == '__main__':
    main()
