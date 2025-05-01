from setuptools import setup, find_packages

setup(
    name='replace_excalidraw',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'replace-excalidraw = replace_excalidraw.plugin:ReplaceExcalidrawPlugin'
        ]
    },
)
