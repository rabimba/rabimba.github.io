---
title: 'Adding All Flavors: A Hybrid Random Number Generator for dApps and Web3'
authors:
- Ranjith Chodavarapu
- Rabimba Karanjai
- Xinxin Fan
- Larry Shi
- Lei Xu
date: '2024-09-01T00:00:00Z'
doi: ''
publishDate: '2024-09-01T00:00:00Z'
publication_types:
- '1'
publication: International Symposium on Stabilization, Safety, and Security of Distributed Systems (SSS) 2024
publication_short: International Symposium on Stabilization, Safety, and Security of Distributed Systems (SSS) 2024
abstract: Random numbers play a vital role in many decentralized applications (dApps), such as gaming and decentralized finance (DeFi) applications. Existing random number provision mechanisms can be roughly
  divided into two categories, on-chain, and off-chain. On-chain approaches usually rely on the blockchain as the major input and all computations are done by blockchain nodes. The major risk for this type
  of method is that the input itself is susceptible to the adversary's influence. Off-chain approaches, as the name suggested, complete the generation without the involvement of blockchain nodes and share
  the result directly with a dApp. These mechanisms usually have a strong security assumption and high complexity. To mitigate these limitations and provide a framework that allows a dApp to balance different
  factors involved in random number generation, we propose a hybrid random number generation solution that leverages IoT devices equipped with trusted execution environment (TEE) as the randomness sources,
  and then utilizes a set of cryptographic tools to aggregate the multiple sources and obtain the final random number that can be consumed by the dApp. The new approach only needs one honest random source to guarantee the unbiasedness of the final random number and a user can configure the system to tolerate malicious participants who can refuse to respond to avoid unfavored results.
  We also provide a concrete construction that can further reduce the on-chain computation complexity to lower the cost of the solution in practice. We evaluate the computation and gas costs to demonstrate
  the effectiveness of the improvement.
tags:
- Web3
- Randomness
- dApps
- Security
featured: false
links:
- name: DOI
  url: https://link.springer.com/chapter/10.1007/978-3-031-74498-3_21
- name: arXiv
  url: https://arxiv.org/pdf/2510.12062
bibtex: "@article{karanjai2024adding-f,\n  title={Adding All Flavors: A Hybrid Random Number Generator for dApps and Web3},\n  author={Ranjith Chodavarapu and Rabimba Karanjai and Xinxin Fan and Larry Shi\
  \ and Lei Xu},\n  journal={arXiv preprint arXiv:2510.12062},\n  year={2024}\n}"
---





