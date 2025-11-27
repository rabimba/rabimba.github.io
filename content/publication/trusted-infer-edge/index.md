---
title: "Trusted Infer Edge with Smart Contracts"
authors:
- Rabimba Karanjai
- Weidong Shi
date: "2024-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-01T00:00:00Z"

# Publication type.
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE ICBC 2024"
publication_short: "IEEE ICBC 2024"

abstract: "Presented at IEEE ICBC 2024."

tags:
- Blockchain
- First Author
- IEEE ICBC 2024
- IoT
- Security

featured: false

links:
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---


## Paper Summary

Trusted LLM Inference on the Edge with
Smart Contracts
Rabimba Karanjai
Department Of Computer Science
University Of Houston
rkaranjai@uh.edu
Weidong Shi
Department Of Computer Science
University Of Houston
wshi3@uh.edu
Abstract—In this era, significant transformations in
industries and tool utilization are driven by AI/Large
Language Models (LLMs) and advancements in Machine
Learning. There’s a growing emphasis on MLOps for
managing and deploying these AI models, along with
a focus on distributed inferences. Concurrently, the im-
perative for secure on-chain computation is escalating.
Our paper introduces an innovative framework that
integrates blockchain technology, particularly the Cosmos
SDK, to facilitate distributed AI inferences on edge
devices. This system, built on WebAssembly (W ASM),
enables interchain communication and deployment of
W ASM modules executing AI inferences across multiple
blockchain nodes. We critically assess this system’s safety,
scalability, and model security, with a special focus on
its portability and engine-model agnostic deployment on
edge devices.
I. I NTRODUCTION
The field of Artificial Intelligence (AI) has witnessed
significant progress, particularly in Large Language
Models (LLMs) like Generative Pre-trained Trans-
formers (GPTs) [1] and Google PaLM 2 [2]. These
advancements have led to the integration of LLMs
into practical applications, as evidenced by research
in [3], [1]. One particularly captivating application lies
in the generation of source code from natural language
instructions. This development, exemplified by systems
like ChatGPT and Github CoPilot [4], has the potential
to revolutionize the programming process by enabling
programmers to express their intent in natural language
and have it automatically translated into functional
code across various programming paradigms.
In computer science, the exploration and integra-
tion of decentralized ledgers and smart contracts have
marked a pivotal shift within the financial sector. This
shift is highlighted by the extensive use of Uniswap’s
smart contracts, which supported transactions surpass-
ing $7.17 billion in 2021 [5]. The utility of smart
contracts extends across various domains, including
but not limited to, Confidential Computing [6], [7],
Decentralized Serverless Functions [8], and Event-
based Transactions [9], [10]. Given this backdrop, an
essential inquiry arises concerning the feasibility and
efficacy of employing artificial intelligence (AI) and
large language models (LLMs) within a distributed
and secure smart contract environment for the purpose
of financial modeling and forecasting. This inquiry
seeks to determine whether such integration could
enhance the efficiency and functionality of the financial
workflow.
In this research, we delve into the potential of
executing smart contracts on a blockchain to determine
if they can trigger AI agent operations based on those
contracts. Our investigation focuses on whether a sys-
tem can be designed to seamlessly integrate with the
existing smart contract workflow, avoiding disruptive
changes and adhering to current standards. This would
enable the application of AI-driven finance models to
produce outputs that are numerical, textual, and multi-
modal in nature. Our primary interest lies in whether
our envisioned system could integrate within estab-
lished frameworks, offering an innovative method for
interacting with AI models, including large language
models (LLMs), in a manner that is conscious of
privacy concerns.
We introduce a conceptual framework aimed at fa-
cilitating decentralized, on-device edge inferences that
are agnostic to the specific AI models, through smart
contracts. These contracts act as triggers for the AI
inference engine, which operates within a rust based
wasm runtim runtime environment. Our research is
directed at addressing several key questions:
RQ1: Can smart contracts effectively incorporate
AI and LLM inferences while maintaining reason-
able ...

(Text automatically extracted from paper. See PDF for full details and illustrations.)