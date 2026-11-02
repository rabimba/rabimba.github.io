---
title: 'TxnQA: Benchmarking Analytical Reasoning and Evidence Grounding over Transaction Event Sequences'
authors:
- Rabimba Karanjai
- Yiming Bian
- Yun-Shiuan Chuang
- Jenna L. Ballard
- Zijie Pan
- Shivani Shekhar
- Yixi Li
- Yirou Ge
- Avinash Thangali
- Richard Williamson
- Linsey Pang
- Prakhar Mehrotra
date: '2026-10-19T00:00:00Z'
doi: ''
publishDate: '2026-10-19T00:00:00Z'
publication_types:
- '3'
publication: AAAI 2027 (Under Review)
publication_short: AAAI 2027 (Under Review)
abstract: 'Analyzing merchant transaction histories requires dynamic temporal filtering, entity resolution, and aggregation over irregular event streams--operations poorly captured by static tabular or time-series forecasting benchmarks. We introduce TxnQA, an analytical QA benchmark comprising 27 task families (81 templates) alongside a 5-scenario fraud-risk reasoning suite that evaluates both verdicts and supporting evidence over synthetic, privacy-mitigated transaction data. Ground-truth answers are computed programmatically, and model performance is decomposed into format-following rate (FFR), conditional content accuracy (CA), and end-to-end correctness (E2E). Evaluating prompted proprietary baselines and six LoRA-adapted open-weight models shows that adaptation reliably enforces output schemas but leaves arithmetic bottlenecks: Gemma-4-31B-IT and Qwen3-8B attain E2E scores of 0.867 and 0.816, whereas evaluated MoE checkpoints reach only 0.632-0.713. Furthermore, on the 500-instance fraud suite, verdict accuracy frequently exceeds 80%, yet joint accuracy (requiring exact evidence attribution) collapses to at most ~23%. These findings identify schema compliance, semantic calculation, and evidence attribution as three distinct bottlenecks in transaction-sequence QA.'
tags:
- Question Answering
- Benchmark
- Financial AI
- LLMs
- First Author
featured: false
links:
- name: arXiv
  url: https://arxiv.org/pdf/2610.27256
- name: Scholar
  url: https://scholar.google.com/scholar?q=TxnQA%3A%20Benchmarking%20Analytical%20Reasoning%20and%20Evidence%20Grounding%20over%20Transaction%20Event%20Sequences
bibtex: "@misc{karanjai2026txnqa,\n  title={TxnQA: Benchmarking Analytical Reasoning and Evidence Grounding over Transaction Event Sequences},\n  author={Rabimba Karanjai and Yiming Bian and Yun-Shiuan Chuang and Jenna L. Ballard and Zijie Pan and Shivani Shekhar and Yixi Li and Yirou Ge and Avinash Thangali and Richard Williamson and Linsey Pang and Prakhar Mehrotra},\n  howpublished={arXiv preprint arXiv:2610.27256},\n  year={2026}\n}"
---
