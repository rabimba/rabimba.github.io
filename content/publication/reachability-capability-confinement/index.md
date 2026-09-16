---
title: 'Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection'
authors:
- Wujie Xiong
- Rabimba Karanjai
- Yang Lu
- Weidong Shi
- Lei Xu
date: '2026-08-30T00:00:00Z'
doi: ''
publishDate: '2026-08-30T00:00:00Z'
publication_types:
- '3'
publication: arXiv preprint arXiv:2608.30041
publication_short: arXiv:2608.30041
abstract: 'Large language model agents place outputs from external skills into their execution
  context, allowing attacker-controlled data to influence later privileged actions. Existing
  defenses mainly classify untrusted content or authorize proposed operations. They do not
  directly address how an agent''s future authority should change once untrusted data enters
  its state. We present SkillGuard, a harness-level enforcement layer that treats this event
  as contamination and restricts future capabilities to disconnect the resulting state from
  deployer-defined forbidden states. Given sound skill summaries and policies, SkillGuard
  represents security-relevant transitions with a Skill Impact Graph, specifies admissible
  control over skill parameters via steerability signatures, and mediates invocations with
  an inline reference monitor. Following contamination, it computes weighted capability
  restrictions using binary, fractional, or fractional-flow strategies without auxiliary
  language-model inference. We evaluate SkillGuard on four AgentDojo suites with two backend
  LLMs, Gemini 2.5 Flash and Llama3.3-70B, against an LLM-only No Defense baseline and three
  defenses at different system layers: Spotlighting, CaMeL, and AttriGuard. Under AgentDojo''s
  Tool Knowledge attacks, SkillGuard eliminates attack success on three of four suites for
  both backends. Against compositional attacks, it outperforms every baseline on Llama and
  matches the strongest baseline on Gemini at higher benign utility. Across both settings,
  SkillGuard adds no model calls or token overhead.'
tags:
- Security
- AI Agents
- Prompt Injection
featured: false
links:
- name: arXiv
  url: https://arxiv.org/pdf/2608.30041
bibtex: "@article{xiong2026reachability,\n  title={Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection},\n  author={Xiong, Wujie and Karanjai, Rabimba and Lu, Yang and Shi, Weidong and Xu, Lei},\n  journal={arXiv preprint arXiv:2608.30041},\n  year={2026}\n}"
---
