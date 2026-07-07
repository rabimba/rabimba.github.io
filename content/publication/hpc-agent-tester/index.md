---
title: 'HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation'
authors:
- Rabimba Karanjai
- Lei Xu
- Weidong Shi
date: '2025-11-01T00:00:00Z'
doi: ''
publishDate: '2025-11-01T00:00:00Z'
publication_types:
- '1'
publication: ACM AIWare 2025
publication_short: ACM AIWare 2025
abstract: Unit testing in High-Performance Computing (HPC) is critical but challenged by parallelism, complex algorithms, and diverse hardware. Traditional methods often fail to address non-deterministic
  behavior and synchronization issues in HPC applications. This paper introduces HPCAgentTester, a novel multi-agent Large Language Model (LLM) framework designed to automate and enhance unit test generation
  for HPC software utilizing OpenMP and MPI. HPCAgentTester employs a unique collaborative workflow where specialized LLM agents (Recipe Agent and Test Agent) iteratively generate and refine test cases
  through a critique loop. This architecture enables the generation of context-aware unit tests that specifically target parallel execution constructs, complex communication patterns, and hierarchical parallelism.
  We demonstrate HPCAgentTester's ability to produce compilable and functionally correct tests for OpenMP and MPI primitives, effectively identifying subtle bugs that are often missed by conventional techniques.
  Our evaluation shows that HPCAgentTester significantly improves test compilation rates and correctness compared to standalone LLMs, offering a more robust and scalable solution f
tags:
- HPC
- Testing
- Agents
- First Author
featured: false
links:
- name: arXiv
  url: https://arxiv.org/pdf/2511.10860
bibtex: "@article{karanjai2025hpc-agen,\n  title={HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation},\n  author={Rabimba Karanjai and Lei Xu and Weidong Shi},\n  journal={arXiv\
  \ preprint arXiv:2511.10860},\n  year={2025}\n}"
---






