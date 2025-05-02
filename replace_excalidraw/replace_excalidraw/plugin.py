import re
from mkdocs.plugins import BasePlugin
from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)

class ReplaceExcalidrawPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):

        new_markdown = markdown.replace('.excalidraw.md)', '.excalidraw.svg)')

        if markdown == new_markdown:
            return markdown

        log.info(f"Replaced .excalidraw.md with .excalidraw.svg in {page.file.src_path}")
        return new_markdown
