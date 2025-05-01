#!/bin/bash
set -e

# Replace all instances of '.excalidraw.md' with '.excalidraw.svg' in markdown files
find docs/ -type f -name "*.md" -exec sed -i 's/\.excalidraw]/\.excalidraw\.svg]/g' {} +

# Build the MkDocs site using the specified configuration
uv run mkdocs build
