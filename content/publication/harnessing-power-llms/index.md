---
title: "Harnessing the power of llms: Automating unit test generation for high-performance computing"
authors:
- Rabimba Karanjai
- A Hussain
- MRI Rabin
- L Xu
- W Shi
- MA Alipour
date: "2024-07-01T00:00:00Z"
publishDate: "2024-07-01T00:00:00Z"
publication_types: ["3"]
publication: "arXiv 2024"
publication_short: "arXiv 2024"
abstract: "arXiv Preprint."
tags:
- LLM
- HPC
- Testing
- First Author
featured: false
links:
url_pdf: 'paper.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---


## Paper Summary

HARNESSING THE POWER OF LLM S: AUTOMATING UNIT TEST
GENERATION FOR HIGH -PERFORMANCE COMPUTING
A PREPRINT
Rabimba Karanjai∗
Department of Computer Science
University Of Houston
rkaranjai@uh.edu
Aftab Hussain
Department of Computer Science
University Of Houston
ahussain27@uh.edu
Md Rafiqul Islam Rabin
Department of Computer Science
University Of Houston
mrabin@uh.edu
Lei Xu
Department of Computer Science
Kent State University
xuleimath@gmail.com
Weidong Shi
Department of Computer Science
University Of Houston
wshi3@uh.edu
Mohammad Amin Alipour
Department of Computer Science
University Of Houston
maalipou@central.uh.edu
October 9, 2023
ABSTRACT
Unit testing is a standard practice in software engineering and is critical for ensuring software quality.
However, for parallel and high-performance computing software, especially scientific computing
applications, unit testing is not widely implemented. Compared with typical commercial software,
high performance software usually have a smaller user base, and they are diverse and usually involve
complex logic. These characteristics create several challenges for conducting unit testing for parallel
and high performance software. On one hand, it is economically expensive to have a dedicated
testing team to do unit testing considering the number of users. On the other hand, it is hard for
a quality engineer without domain knowledge to design effective unit testings. Similarly, existing
automated unit testing tools are usually not effective for such software. Therefore, it is vital to devise
an automated method for generating unit testing cases for parallel and high performance software,
which considers the unique features of these software, including complex logic and sophisticated
parallel processing techniques. Recently, large language models (LLMs) have attracted more attention
and are believed to be a powerful tool for coding and testing, but its application in producing unit
tests for parallel and high performance applications remains uncertain. To fill this gap, we explore
the capabilities of two well-known generative models, Davinci (text-davinci-002) and ChatGPT
(gpt-3.5-turbo), in crafting unit testing cases for parallel and high performance software. Specifically,
we proposed novel ways to utilize LLMs to develop unit testing cases for high performance software
with C++ parallel programs and assessed their effectiveness on extensiveOpenMP/MPI projects. Our
findings indicate that in the context of parallel programming, LLMs can create unit testing cases that
are mostly syntactically correct and offer substantial coverage, while they exhibit some limitations
like repetitive assertions and blank test cases.
Keywords First keyword · Second keyword · More
1 Introduction
Fueled by advancements in deep learning, Large Language Models (LLMs) have surged in development. Their versatility
stretches across various applications, with a prominent one being software code generation. LLMs specializing in this
domain are trained on vast datasets of source code gleaned from software repositories like GitHub and programming
communities like Stack Overflow. OpenAI Codex Chen et al. [2021a], Meta’s Code Llama (a code-centric variant
∗www.rabimba.me
arXiv:2407.05202v1  [cs.SE]  6 Jul 2024
arXiv Template A PREPRINT
of Llama 2 trained on dedicated code datasets), and HuggingFace’s StarCoder Li et al. [2023] stand out as notable
examples. Early research and evaluations suggest that these code-tailored LLMs exhibit impressive competency in
generating programming code from user-provided natural language queries Chen et al. [2021a], Xu et al. [2022].
Incorporating Large Language Models (LLMs) into the realm of software development holds the potential to unlock
remarkable benefits, spanning a diverse range of tasks, including code creation, documentation, summarization, analysis,
and troubleshooting Tarassow [2023]. The capabilities of LLMs extend to practical assistance in code restructuring,
choosing suita...

(Text automatically extracted from paper. See PDF for full details and illustrations.)