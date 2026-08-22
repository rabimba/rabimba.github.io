---
title: 'PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance'
authors:
- Rabimba Karanjai
- Yang Lu
- Richard Williamson
- Hemanth Hm
- Prakhar Mehrotra
- Lei Xu
- Weidong Shi
date: '2026-08-18T00:00:00Z'
doi: ''
publishDate: '2026-08-18T00:00:00Z'
publication_types:
- '3'
publication: arXiv preprint arXiv:2608.17220
publication_short: arXiv
abstract: 'Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi)
  actions such as swaps, lending operations, and yield management. Because these agents rely
  on large language models (LLMs) to plan transactions, they inherit the LLM''s susceptibility
  to prompt injection and lack mechanisms to bind a verifier''s approval to the exact transaction
  ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a
  transaction-level authorization framework that interposes between an LLM-based agent and
  on-chain execution. PACE introduces typed transaction intents, a deterministic policy verifier,
  and signed Policy Decision Records (PDRs) that cryptographically bind the approved intent,
  policy, and simulation report to the exact execution bytes, with replay and expiration protection.
  A Solidity smart account enforces PDR signatures on-chain with a measured overhead of 29,826-31,822
  gas. We evaluate PACE against six baselines on 40 tasks spanning four attack categories plus
  benign utility (2,800 trials, 10 seeds). In our deterministic sandbox, PACE achieves a 0.00
  unsafe execution rate and 0.00 false-positive rate on benign tasks, compared to 0.80 for
  the unguarded baseline.'
tags:
- Blockchain
- Security
- AI Agents
- DeFi
- First Author
featured: true
links:
- name: arXiv
  url: https://arxiv.org/pdf/2608.17220
bibtex: "@misc{karanjai2026pace,\n  title={PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance},\n  author={Karanjai, Rabimba and Lu, Yang and Williamson, Richard and Hm, Hemanth and Mehrotra, Prakhar and Xu, Lei and Shi, Weidong},\n  howpublished={arXiv preprint arXiv:2608.17220},\n  year={2026}\n}"
---
