---
title: 'Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation'
authors:
- Rabimba Karanjai
- Yang Lu
- Hemanth Hegadehalli Madhavarao
- Lei Xu
- Weidong Shi
date: '2026-08-01T00:00:00Z'
doi: ''
publishDate: '2026-08-01T00:00:00Z'
publication_types:
- '1'
publication: 35th USENIX Security Symposium (USENIX Security 26)
publication_short: USENIX Security 2026
abstract: 'Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks
  including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing
  services and process network logs as natural language contexts to generate security insights. We demonstrate that
  this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in
  log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term
  passive prompt injection. We present LogInject, a systematic framework for evaluating these threats. Using
  LogInject-1.0, a benchmark of 12,847 log entries including 2,569 adversarial samples, we evaluate three production
  LLMs across four attack objectives. Our findings reveal an up to 88.2% attack success rate under baseline conditions.
  We introduce Context Stitching, a novel technique that fragments payloads across multiple log entries to evade
  stateless filters, achieving a 76.4% success rate. As mitigation, we evaluate layered defenses combining input
  filtering, prompt hardening, and output validation, demonstrating a 90.4% attack reduction.'
tags:
- Security
- LLMs
- Network Security
- First Author
featured: false
links:
- name: PDF
  url: https://www.usenix.org/system/files/usenixsecurity26-karanjai.pdf
- name: arXiv
  url: https://arxiv.org/pdf/2607.14493
- name: USENIX
  url: https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai
- name: Scholar
  url: https://scholar.google.com/scholar?q=Context%20Contamination%20in%20LLM%20Analysis%20of%20Network%20Security%20Logs%3A%20Poison%20with%20Passive%20Prompt%20Injection%20and%20Mitigation%20Evaluation
bibtex: "@inproceedings{320609,\n  author    = \"Rabimba Karanjai and Yang Lu and Hemanth Hegadehalli Madhavarao and Lei Xu and Weidong Shi\",\n  title     = \"Context Contamination in {LLM} Analysis of Network\
  \ Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation\",\n  booktitle = \"35th USENIX Security Symposium (USENIX Security 26)\",\n  year      = \"2026\",\n  address   = \"Baltimore,\
  \ MD\",\n  url       = \"https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai\",\n  publisher = \"USENIX Association\",\n  month     = aug\n}"
---



