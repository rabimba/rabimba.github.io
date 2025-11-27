---
title: "Decentralized Application Infrastructures as Smart Contract Codes"
authors:
- Rabimba Karanjai
- Keshav Kasichainula
- Nour Diallo
- Mudabbir Kaleem
- Lei Xu
- Lin Chen
- Weidong Shi
date: "2022-05-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-05-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE International Conference on Blockchain and Cryptocurrency (ICBC 2022)"
publication_short: "IEEE ICBC 2022"

abstract: "This paper proposes a novel approach to decentralized application infrastructures by treating them as smart contract codes, enabling more secure and scalable dApps."

tags:
- Blockchain
- Decentralized Applications
- Distributed Systems
- First Author
- Security
- Smart Contracts
- Software Engineering

featured: true

links:
url_pdf: 'https://ieeexplore.ieee.org/document/9789334'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---



## Paper Summary

Decentralized Application Infrastructures as Smart
Contract Codes
Rabimba Karanjai∗, Keshav Kasichainula∗, Nour Diallo∗, Mudabbir Kaleem∗, Lei Xu†, Lin Chen‡, Weidong Shi∗
∗University Of Houston, TX, USA
{rkaranjai, kkasichainula, ndiallo, mkaleem, wshi3}@uh.edu
†Kent State University, OH, USA , ‡ Texas Tech University, TX, USA
xuleimath@gmail.com, lin.chen@ttu.edu
Abstract—With the recent advance in concepts like decent-
ralized “cloud” and blockchain-enabled decentralized com-
puting environments, the legacy modeling and orchestration
tools developed to support centrally managed cloud-based ICT
infrastructures are challenged by such a new paradigm built
on top of decentralization. On the other hand, decentralized
“cloud” and computing infrastructures need to support many
Dapp use cases. As the complexity of these targeted application
scenarios increases, there is an urgent need for developing
automation and modeling tools for deploying and managing
decentralized infrastructures. Instead of creating such tools
from scratch, a natural approach is extending mature infra-
structure modeling tools for Dapps and decentralized comput-
ing environments. To this end, in this work, we have developed
extensions to the TOSCA domain-specific language to support
smart contract specification of decentralized computing in-
frastructures for supporting Dapps, where smart contracts or
chain codes manage a decentralized computing environment.
The result is blockchain-based orchestration and automation
for decentralized “cloud” and computing environments, which
is a step forward for achieving full decentralization in general-
purpose computing.
Index Terms—TOSCA, Smart Contracts, Blockchain, Infra-
structures
I. Introduction
Modern ICT (information and communication technology)
infrastructures are becoming increasingly sophisticated and
infeasible to manage manually. Various technologies have
been developed to support efficient and flexible physical ICT
infrastructure management, such as computer virtualization,
software-defined network, and network function virtualiz-
ation. To further automate the deployment, configuration,
and management of centralized infrastructures like a cloud-
based ICT center, system administrators, have been using
orchestration tools [1] to dynamically deploy services. These
orchestration tools are usually centrally managed by so-
called orchestrators. An administrator fully trusts the or-
chestrator to manage and coordinate the lifecycles of ICT
components (e.g., computation, storage, and communication
resources), which constitute a deployed service. To further
improve the management of the ICT infrastructure, the
concept of “infrastructure-as-code” was developed [2], where
a system administrator describes the target infrastructure
and orchestration objectives as documents using a domain-
specific language. This concept brings several advantages,
such as faster configuration and environment provisioning,
greater consistency, and minimized risk/enhanced security.
One of the most popular domain-specific languages for in-
frastructure definition is TOSCA (Topology and Orchestration
Specification for Cloud Applications [3])), which helps man-
age and automate the cloud-based deployment of services.
With TOSCA, administrators can focus on the intended func-
tionalities of the infrastructure and only need to describe the
end goal of the envisioned service deployment environment.
The interpretation and implementation of the description are
delegated to the orchestrator. One of the TOSCA’s funda-
mental properties is cloud platform agnostic, which makes
it ideal for managing multi-cloud ICT infrastructure. There
are numerous implementations of TOSCA based on its stand-
ards (e.g., Alien4Cloud(https://alien4cloud.github.io/), Cloud-
ify(https://github.com/c loudify-cosmo), and OpenTOSCA [4]).
With the introduction of blockchains [5], smart contracts
[6] and the recent advance in decentralized “cloud” and
blockchain-enabled de...

(Text automatically extracted from paper. See PDF for full details and illustrations.)