---
title: "Smart Contract Translation Concepts"
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
publication: "Foundations of Software Engineering (FSE) 2024"
publication_short: "Foundations of Software Engineering (FSE) 2024"

abstract: "Presented at Foundations of Software Engineering (FSE) 2024."

tags:
- Blockchain
- First Author
- Foundations of Software Engineering (FSE) 2024
- Software Engineering

featured: false

links:
url_pdf: 'https://arxiv.org/pdf/2412.12513.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---


## Paper Summary

CONMOVER : G ENERATING MOVE SMART CONTRACTS BASED
ON CONCEPTS
A PREPRINT
Rabimba Karanjai*
Department of Computer Science
University of Houston
Houston, TX, United States
rabimba@cs.uh.edu
Sam Blackshear
Mysten Labs
Lei Xu
Department of Computer Science
Kent State University
Kent, OH, United States
Weidong Shi
Department of Computer Science
University of Houston
Houston, TX, United States
December 18, 2024
ABSTRACT
The increasing use of formal verification for smart contracts has led to the rise of new, formally
verifiable languages, such as Move. However, the scarcity of training data for these languages poses
a challenge to code generation using large language models (LLMs). This paper introduces Con-
Mover, a framework that utilizes a knowledge graph of Move concepts and a small set of correct
Move code examples to enhance the code generation capabilities of LLMs. ConMover employs
a novel approach that combines concept retrieval, planning, coding, and debugging agents to it-
eratively refine the generated code. This framework is evaluated with different sized open-source
LLMs, demonstrating significant improvements in code generation accuracy compared to baseline
models. The results highlight the potential of ConMover to bridge the gap between natural lan-
guage descriptions and low-resource code generation for smart contracts, enabling more efficient
and reliable development processes.
Keywords Large Language Models (LLMs) · Code Generation · Smart Contracts · Move.
1 Introduction
The growing significance of code generation in automating software development has spurred extensive research into
utilizing Large Language Models (LLMs) [15, 7] for this purpose. Although LLMs have shown impressive skill in
translating natural language instructions into code, they still struggle to produce flawless code for complex tasks on the
first attempt [27, 22]. This challenge mimics the experience of human developers, who often go through several cycles
of debugging and refinement for intricate coding problems. As a result, the focus is increasingly shifting towards
enhancing LLMs’ ability to self-debug—detecting and fixing errors in their own code—thereby strengthening their
overall code generation performance.
The limitations of single-pass code generation are becoming increasingly apparent. Generating code in a single attempt
often fails to capture the nuances and intricate requirements inherent in bigger code repositories [11]. This approach
struggles to address the numerous edge cases and specific needs that arise, particularly given the high degree of
precision and complexity demanded in such projects. To address these shortcomings, researchers are transitioning
towards multi-round code generation frameworks [16] that leverage iterative refinement. These frameworks facilitate
a more robust and accurate code generation process by enabling the model to generate and refine code through multiple
iterations. This approach allows for incremental improvements and adjustments, ultimately leading to a more accurate
arXiv:2412.12513v1  [cs.SE]  17 Dec 2024
ConMover: Generating Move Smart Contracts based on Concepts A PREPRINT
and efficient development process. These advanced systems employ reflective mechanisms, such as analyzing failed
test cases and interpreting error messages, to inform subsequent code generation attempts [8]. While these techniques
have demonstrated promising improvements, they still produce considerably worse code when it comes to complex
tasks [12].
Moreover, when it comes to generating code for low-resource languages like Move[6] or Rust, prior work [9, 13] has
shown an approach of translation works best. However, that might not be sufficient for most of the use cases, and a
method that does not rely on existing code in a different programming language or vast code corpora to train a model
for these low-resource languages is needed.
We try to address the following research questions through this work.
• RQ1: Can we gen...

(Text automatically extracted from paper. See PDF for full details and illustrations.)