#!/bin/bash
set -e

# Replace all instances of '.excalidraw.md' with '.excalidraw.svg' in markdown files
find . -type f -name "*.md" -exec sed -i 's/\.excalidraw\.md/\.excalidraw\.svg/g' {} +

# Build the MkDocs site using the specified configuration
mkdocs build -f .deploy/mkdocs.yml
