---
title: 'CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning'
authors:
- Rabimba Karanjai
- Qun Gu
- Hemanth Hegadehalli Madhavarao
- Wenhuan Sun
- Xiaojiao Yu
- Suryabhan Singh Hada
- Libin N. George
- Uma Kona
- Richard Williamson
- Linsey Pang
- Prakhar Mehrotra
date: '2026-10-06T00:00:00Z'
doi: ''
publishDate: '2026-10-06T00:00:00Z'
publication_types:
- '3'
publication: NeurIPS 2026 (Under Review)
publication_short: NeurIPS 2026 (Under Review)
abstract: 'Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal. It is also susceptible to length and style bias when preference pairs come from different model families. We introduce Constraint-Margin DPO (CM-DPO), which replaces DPO''s binary preference signal with a continuous margin derived from a deterministic symbolic verifier and scaled by violation severity. Hard and soft constraints are separated through a lexicographic objective, ensuring hard constraints are never traded off against preferences. To supply CM-DPO with bias-reduced training pairs, we generate preference data through procedurally generated constraint profiles (DCCG) and minimal-edit distillation from a reasoning teacher (RT-MED), within a framework we call SynPlan-R. On TravelPlanner, NaturalPlan, and out-of-distribution PlanBench, an 8B model fine-tuned with CM-DPO achieves 89.2% pass rate and 93.4% solve rate, matching multi-agent systems at 13x lower latency while outperforming GPT-4o on unseen Blocksworld by 9.2 points.'
tags:
- LLMs
- Preference Optimization
- Planning
- First Author
featured: false
links:
- name: arXiv
  url: https://arxiv.org/pdf/2610.09219
- name: Scholar
  url: https://scholar.google.com/scholar?q=CM-DPO%3A%20Constraint-Margin%20Direct%20Preference%20Optimization%20for%20LLM%20Planning
---


