---
title: "Smarter? Empirical Study AI-based Smart Contract Creation"
authors:
- Rabimba Karanjai
- Weidong Shi
date: "2023-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-01-01T00:00:00Z"

# Publication type.
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "BRAINS 2023"
publication_short: "BRAINS 2023"

abstract: "Presented at BRAINS 2023."

tags:
- AI
- BRAINS 2023
- Blockchain
- First Author

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

Who is Smarter? An Empirical Study of AI-based Smart
Contract Creation
Rabimba Karanjai∗, Edward Li ∗, Lei Xu †, Weidong Shi∗
∗University Of Houston, TX, USA
{rkaranjai, wshi3}@uh.edu, edward.w.li@outlook.com
†Kent State University, OH, USA
xuleimath@gmail.com
Abstract—The introduction of large language models (LLMs) like
ChatGPT and Google Palm2 for smart contract generation seems to be
the first well-established instance of an AI pair programmer. LLMs have
access to a large number of open-source smart contracts, enabling them
to utilize more extensive code in Solidity than other code generation tools.
Although the initial and informal assessments of LLMs for smart contract
generation are promising, a systematic evaluation is needed to explore
the limits and benefits of these models. The main objective of this study
is to assess the quality of generated code provided by LLMs for smart
contracts. We also aim to evaluate the impact of the quality and variety
of input parameters fed to LLMs. To achieve this aim, we created an
experimental setup for evaluating the generated code in terms of validity,
correctness, and efficiency. Our study finds crucial evidence of security
bugs getting introduced in the generated smart contracts as well as the
overall quality and correctness of the code getting impacted. However,
we also identified the areas where it can be improved. The paper also
proposes several potential research directions to improve the process,
quality and safety of generated smart contract codes.
Index Terms—GPT, smart contract, code generation, large language
models, AI
I. I NTRODUCTION
In recent years, large language models (LLMs) such as generative
pre-trained transformer (GPT) models [1] and Google PaLM2 [2]
are becoming more mature and ready for deployment for real
applications [1], [3]. Among all the applications enabled by LLMs,
machine-aided source code generation from natural language is
fascinating and widely believed to have the potential to revolutionize
the way humans create programs. For instance, ChatGPT and its
derivatives (e.g., Github CoPilot [4]) have been used to generate
source code of multiple programming languages based on natural
language inputs from the programmer. But there have also been
concerns about these being used for malicious purposes [5].
One of the major concerns of LLM-generated source code is its
safety because there is a lack of rigorous understanding of the logic
that the source code is generated. Many works have been done on
analyzing the security features of the generated code for languages
such as Python, Golang, and Javascript. In most cases, LLMs rely on
the training dataset to “understand” natural language instructions to
create source code and are programming language specific, i.e., they
can only create source code of programming languages that have been
used to train the model. Accordingly, the security analysis works are
also language specific. And most security assessment results on one
programming language may not be valid for another language.
Recently, decentralized ledgers and smart contracts running atop it
are finding more applications, especially in the financial sector. For
instance, the Uniswap smart contracts process about $7.17 billion per
day in 2021 [6]. Because of the popularity of smart contracts and
their importance in various scenarios like Confidential Computing [7],
[8], Decentralized Serverless Functions [9], Event based Transactions
[10], [11], it is a natural question to ask whether LLMs can do a good
job at creating smart contracts based on user instructions and how
secure the generated smart contracts are. To fill the gap, we investigate
two popular LLMs, ChatGPT and Google PaLM2 [2], for generating
smart contract code in Solidity, which is a mainstream smart contract
programming language. We compare the code generation process and
the generated smart contracts, and conduct systematic evaluation on
the contracts. To systematically evaluate GPT 3.5 ...

(Text automatically extracted from paper. See PDF for full details and illustrations.)