from mkdocs.plugins import BasePlugin, get_plugin_logger

log = get_plugin_logger(__name__)

class ReplaceExcalidrawPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        new_markdown = markdown.replace('.excalidraw]', '.excalidraw.svg]')
        if markdown != new_markdown:
            log.info(f"Replaced '.excalidraw]' with '.excalidraw.svg]' on page: {page.file.src_path}")
        return new_markdown
