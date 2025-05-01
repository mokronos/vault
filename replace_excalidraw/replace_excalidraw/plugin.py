import re
from mkdocs.plugins import BasePlugin
from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)

class ReplaceExcalidrawPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):

        # Regex pattern to match ![text](filename.excalidraw)
        pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+\.excalidraw)\)')

        def replacer(match):
            text = match.group(1)  # Text inside the square brackets, e.g., "data_science" or empty
            filename = match.group(2)  # Filename inside the parentheses, e.g., "data_science_2025-05-01.excalidraw"
            new_path = f'excalidraw/{filename}.svg'  # New path with .svg
            log.info(f"Rewriting: {match.group(0)} → ![{text}]({new_path}) (in {page.file.src_path})")
            return f'![{text}]({new_path})'

        new_markdown = pattern.sub(replacer, markdown)
        if markdown == new_markdown:
            return markdown
        return new_markdown
