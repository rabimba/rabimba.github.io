---
title: 'One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion
  Language Models'
authors:
- Rabimba Karanjai
- Linsey Pang
- Hemanth Hegadehalli Madhavarao
- Richard Williamson
- Uma Kona
- Prakhar Mehrotra
date: '2026-11-19T00:00:00Z'
doi: ''
publishDate: '2026-11-19T00:00:00Z'
publication_types:
- '3'
publication: arXiv preprint arXiv:2611.25895
publication_short: arXiv preprint arXiv:2611.25895
abstract: Diffusion language models typically use a fixed denoising schedule across
  workloads. We show that the cheapest schedule that preserves quality depends on
  the task, model, and sampler. We propose Task-Calibrated Denoising Allocation (TCDA),
  a deployment rule with an explicit error guarantee. Given candidate samplers, paired
  calibration data, a utility tolerance, and guardrails against degeneration, TCDA
  uses simultaneous one-sided bootstrap bounds to certify which candidates meet both
  the utility and guardrail criteria. It deploys the cheapest certified candidate
  or falls back to the full schedule. The probability of deploying an infeasible schedule
  is asymptotically at most alpha. Candidates include early prefix decoding, state-reusing
  continuation, reduced time grids, and confidence-threshold decoding. Across seven
  datasets and two model families, TCDA certifies reductions in denoiser e
tags:
- LLMs
- First Author
featured: false
draft: false
links:
- name: DOI
  url: https://doi.org/10.48550/arXiv.2611.25895
- name: arXiv
  url: https://arxiv.org/pdf/2611.25895
bibtex: "@misc{karanjai2026,\n  title={One Schedule Does Not Fit All: Adaptive Inference\
  \ Schedules for Diffusion Language Models},\n  author={Karanjai, Rabimba and Pang,\
  \ Linsey and Madhavarao, Hemanth Hegadehalli and Williamson, Richard and Kona, Uma\
  \ and Mehrotra, Prakhar},\n  howpublished={arXiv preprint arXiv:2611.25895},\n \
  \ year={2026},\n  eprint={2611.25895},\n  archivePrefix={arXiv}\n}"
---

