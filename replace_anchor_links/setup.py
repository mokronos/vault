from setuptools import setup, find_packages

setup(
    name='replace_anchor_links',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'replace-anchor-links = replace_anchor_links.plugin:ReplaceAnchorLinksPlugin'
        ]
    },
)
