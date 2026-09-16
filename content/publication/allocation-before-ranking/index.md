---
title: 'Allocation Before Ranking: Decoupled Token Compression for OmniLLMs'
authors:
- Zhenghui Guo
- Yilin Yang
- Yuanbin Man
- Miao Yin
- Weidong Shi
- Rabimba Karanjai
- Omprakash Gnawali
- Chengming Zhang
date: '2026-08-03T00:00:00Z'
doi: ''
publishDate: '2026-08-03T00:00:00Z'
publication_types:
- '3'
publication: NeurIPS 2026 (Under Review)
publication_short: NeurIPS 2026 (Under Review)
abstract: 'Token compression in OmniLLMs is typically posed as a single saliency-ranking problem:
  score each multimodal token, keep the top-K. We argue this abstraction is mis-specified. The same attention
  score simultaneously decides two things: how much retained capacity each modality receives, and which
  tokens within a modality are kept. A shared top-K rule therefore inherits this audio-favoring allocation
  prior, spending retained capacity on audio before video tokens have a chance to compete. We propose Macer,
  a training-free compressor that first assigns explicit audio and video budgets, then performs
  allocation-normalized ranking within each modality at modality-specific shallow layers. Macer significantly
  reduces token cost while preserving accuracy across audio-grounded, audio-video joint, visual-dominant,
  and video-centric benchmarks. At 25% retention, Macer preserves 98.7% of full-token performance on
  Qwen2.5-Omni-7B and 97.3% on Qwen2.5-Omni-3B.'
tags:
- LLMs
- Token Compression
- Efficiency
featured: false
links:
- name: Scholar
  url: https://scholar.google.com/scholar?q=Allocation%20Before%20Ranking%3A%20Decoupled%20Token%20Compression%20for%20OmniLLMs
---


