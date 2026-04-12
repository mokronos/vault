
## General

Why/When to choose H100 over A100
https://www.reddit.com/r/MachineLearning/comments/17hsjdt/d_why_choose_an_h100_over_an_a100_for_llm/

- Hardware
	- H100 > A100

## A100
- A100 [Whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf)
	- not supporting fp8bit precision (only 16/32), see page 27
- More versatility, as H100 is optimized for LLMs (Transformers)
- like a 3070ti with 80GB vram (same cuda cores)

## H100
- H100 [Whitepaper](https://www.advancedclustering.com/wp-content/uploads/2022/03/gtc22-whitepaper-hopper.pdf)
	- supporting fp8bit precision datatype, see page 11
- H100 has double max Flops
- like a 4090ti with 80GB vram (same cuda cores)
- https://lambdalabs.com/blog/flashattention-2-lambda-cloud-h100-vs-a100H100 8x faster than A100 while training with FlashAttention-2 and multi GPU setup. Without those 2 it's only 2x faster.
