
# General

`~/.aider.conf.yml`

```yaml
# model: azure/gpt-4.1-mini
model: openrouter/deepseek/deepseek-r1:free
# model: openrouter/google/gemini-2.5-pro-exp-03-25:free
# weak-model: openrouter/deepseek/deepseek-r1:free
weak-model: azure/gpt-4.1-mini
set-env:
  - AZURE_API_KEY=<api_key>
  - AZURE_API_VERSION=
  - AZURE_API_BASE=https://models.inference.ai.azure.com
  - OPENROUTER_API_KEY=<api_key>
cache-prompts: true


auto-commits: false
gitignore: true
auto-lint: true
auto-test: true
watch-files: true

dark-mode: true
editor: nvim
vim: true


read: [CONVENTIONS.md]

```

# Workspace specific

`./.aider.conf.yml`

```yaml
# add files to read only
read: [CONVENTIONS.md, README.md]

# add files to edit/add
file: []

# linting and testing commands
# lint-cmd:
test-cmd: uv run pytest
```