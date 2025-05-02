import re
from mkdocs.plugins import BasePlugin
from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)

class ReplaceAnchorLinksPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):

        # Pattern to find markdown links with anchors
        pattern = re.compile(r'\[([^\]]+)\]\((?!https?://)([^)#]+)#([^)]+)\)')

        def replace_anchor(match):
            text, path, anchor = match.groups()
            # Transform anchor to lowercase and replace spaces/%20 with hyphens
            transformed_anchor = re.sub(r'[\s%20]+', '-', anchor.lower())
            original_link = f"{path}#{anchor}"
            new_link = f"{path}#{transformed_anchor}"

            log.info(f"[{page.file.src_path}] Rewriting anchor: {original_link} → {new_link}")
            return f'[{text}]({new_link})'

        return pattern.sub(replace_anchor, markdown)
