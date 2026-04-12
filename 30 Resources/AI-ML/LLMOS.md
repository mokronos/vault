# Idea

Create a [LLM Operating System](https://youtu.be/zjkBMFhNj_g?si=s-yoFpwdFC-26xJL&t=2535)

## Components
- CPU -> LLM
- RAM -> context window
- Disk -> File system 
- Programs -> Tools
- Peripherals -> Video/Audio/Text

## Important things

- Technologies
    - Use python for now
    - Use c/cuda for performance critical parts
- Implementation
    - Try to link to papers for each implementation
    - Always make the lowest level transparent and visible via DEBUG
- Testing
    - Unit test all the helper functions
- Evaluation
    - Be able to evaluate every step or operation of the system
    - Evaluate end to end
- Documentation (Mix of obsidian/nvim and mkdocs/github pages for deployment)
    - Explain every concept and implement it
        - have easy explanations with excalidraw diagrams
        - So that even non-technical people can kinda understand
    - List bugs and how they were fixed
- Iterate a lot