---
title: "Weaving the Cosmos: WASM-Powered Interchain Communication for AI Enabled Smart Contracts"
authors:
- Rabimba Karanjai
- Lei Xu
- Weidong Shi
date: "2025-02-01T00:00:00Z"
publishDate: "2025-02-01T00:00:00Z"
publication_types: ["3"]
publication: "arXiv 2025"
publication_short: "arXiv 2025"
abstract: "arXiv Preprint."
tags:
- Blockchain
- AI
- WASM
- Interchain
- First Author
featured: false
links:
url_pdf: 'https://arxiv.org/pdf/2502.17604.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---


## Paper Summary

Weaving the Cosmos: WASM-Powered
Interchain Communication for AI Enabled
Smart Contracts
Rabimba Karanjai1[0000−0002−6705−6506], Lei Xu2, and Weidong Shi1
rkaranjai@uh.edu1, lxu12@kent.edu2, wshi3@uh.edu1
1 University Of Houston, Houston, USA
2 Kent State University, USA
Abstract. In this era, significant transformations in industries and tool
utilization are driven by AI/Large Language Models (LLMs) and ad-
vancements in Machine Learning. There’s a growing emphasis on Ma-
chine Learning Operations(MLOps) for managing and deploying these
AI models. Concurrently, the imperative for richer smart contracts and
on-chain computation is escalating. Our paper introduces an innovative
framework that integrates blockchain technology, particularly the Cos-
mos SDK, to facilitate on-chain AI inferences. This system, built on We-
bAssembly (WASM), enables interchain communication and deployment
of WASM modules executing AI inferences across multiple blockchain
nodes. We critically assess the framework from feasibility, scalability,
and model security, with a special focus on its portability and engine-
model agnostic deployment. The capability to support AI on-chain may
enhance and expand the scope of smart contracts, and as a result enable
new use cases and applications.
Keywords: Cosmos · smart contract · AI · LLM · WebGPU ·
1 Introduction
In today’s technological era, significant strides have been made in the field of ar-
tificial intelligence and large language models (LLMs), such as the advancements
seen with GPT models [9] and Google’s PaLM2 [7]. These models are now pro-
gressively utilized in real-world applications [17,9]. An exciting application of AI
and LLMs is their use in generating source code, including smart contracts, di-
rectly from natural language descriptions. This application, exemplified by tools
like ChatGPT and Github CoPilot [14], translates programmers’ instructions
into code across various languages, potentially revolutionizing the programming
landscape. Furthermore, LLMs are being applied in forecasting and modeling
time series data, outperforming traditional methods by enabling multi-modal
predictions that incorporate both time series and other forms of unstructured
data. This innovation could greatly enhance financial modeling techniques.
arXiv:2502.17604v1  [cs.SE]  24 Feb 2025
2 Karanjai et al.
Amidst this backdrop, the increasing use of decentralized ledgers and smart
contracts, particularly in the financial sector, is noteworthy. For example, Uniswap’s
smart contracts managed transactions worth approximately $7.17 billion daily
in 2021 3. Given the growing importance of smart contracts in various contexts,
such as Confidential Computing [30,18], Decentralized Serverless Functions [19],
and Event-based Transactions [21,20], it becomes crucial to investigate whether
AI and LLMs can be used effectively for finance modeling and predictions in a
distributed and safe way while augmenting a smart contract workflow.
In this research, we explore the feasibility of executing an AI agent or ma-
chine learning model through a smart contract on a blockchain. Our focus is on
developing a system that integrates with the current smart contract workflows
seamlessly, without necessitating disruptive changes to the existing infrastruc-
ture. We aim to adhere to established standards while utilizing AI-driven finan-
cial models to produce numerical, textual, and multi-modal outputs. The core
of our investigation is to determine whether our proposed system can function
within well-established frameworks and offer an innovative approach to interact-
ing with AI models, including LLMs, directly on-chain.
In our study, we introduce a framework designed to enable decentralized
on-device AI model agnostic inferences for smart contracts. These smart con-
tracts act as triggers for invoking the AI inference engine via a WebAssembly
runtime [16]. Our research primarily seeks to address the following questions:
RQ1: Can smart contra...

(Text automatically extracted from paper. See PDF for full details and illustrations.)