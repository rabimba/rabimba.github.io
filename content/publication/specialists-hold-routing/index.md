---
title: 'Specialists Hold, Generalists Discount: Asymmetric Equilibrium in LLM Routing Auctions'
authors:
- Xinyu Hou
- Yang Lu
- Rabimba Karanjai
- Pei-Chi Pan
- Sen Lin
- Lei Xu
- Weidong Shi
date: '2026-09-27T00:00:00Z'
doi: ''
publishDate: '2026-09-27T00:00:00Z'
publication_types:
- '1'
publication: The Fortieth Annual Conference on Neural Information Processing Systems (NeurIPS 2026)
publication_short: NeurIPS 2026
abstract: 'Routing systems for large language models, such as MasRouter, RouteLLM, FrugalGPT, and others, match queries to suppliers based on cost-quality tradeoffs. Most prior work optimizes this problem from the demand side, while the supplier-side question of how LLM suppliers should price their services within a routing mechanism has received little formal treatment. We provide the first systematic analysis of this problem. In our setup, the LLM is the priced commodity: supplier organizations set price functions for the services they offer, rather than acting as strategic agents that generate bids per query. We model supplier-side pricing as a sealed-bid first-price reverse auction over a router that allocates each query to one supplier based on cost and quality. This framework applies to any cost-quality routing system rather than to a specific implementation. Using calibrated profiles from 12 open-weight models and MasRouter as a case-study router, we characterize equilibrium behavior. Our main finding is that the Bayesian Nash equilibrium is asymmetric: capability-differentiated suppliers adopt flat, non-discounted strategies, while marginal-quality suppliers compete primarily on price. A mechanism-baseline experiment, where the case-study router is replaced by an analytical rational-decision rule, confirms that this pattern is a property of the auction mechanism rather than an artifact of router training. We further observe that price differentiation can emerge in equilibrium even under capability symmetry, because private-cost types alone produce nontrivial bid functions. The practical implication is that auction-based pricing alone does not discipline specialist rents. Achieving that goal requires additional mechanism elements, such as reserve prices or capability-blind tie-breaking.'
tags:
- LLMs
- Game Theory
- Routing
- Distinguished
featured: true
links:
- name: OpenReview
  url: https://openreview.net/forum?id=Dz9fIFWFd9
- name: Scholar
  url: https://scholar.google.com/scholar?q=Specialists%20Hold%2C%20Generalists%20Discount%3A%20Asymmetric%20Equilibrium%20in%20LLM%20Routing%20Auctions
bibtex: "@inproceedings{anonymous2026specialists,\n  title={Specialists Hold, Generalists Discount: Asymmetric Equilibrium in {LLM} Routing Auctions},\n  author={Anonymous},\n  booktitle={The Fortieth Annual Conference on Neural Information Processing Systems},\n  year={2026},\n  url={https://openreview.net/forum?id=Dz9fIFWFd9}\n}"
---


