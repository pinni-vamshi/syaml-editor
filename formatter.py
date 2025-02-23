import re

def format_text(text):
    """
    Convert style indicators in the SYAML file to Markdown/HTML.
    
    Examples:
      ||bold some text||       => **some text**
      ||italic some text||     => _some text_
      ||underline some text||  => <u>some text</u>
    """
    # Bold: convert to Markdown bold
    text = re.sub(r"\|\|bold\s+([^|]+)\|\|", r"**\1**", text)
    # Italic: convert to Markdown italic
    text = re.sub(r"\|\|italic\s+([^|]+)\|\|", r"_\1_", text)
    # Underline: convert to HTML underline (LLMs may support HTML)
    text = re.sub(r"\|\|underline\s+([^|]+)\|\|", r"<u>\1</u>", text)
    return text
