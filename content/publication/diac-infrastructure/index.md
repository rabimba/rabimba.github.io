---
title: "DIaC: Re-imagining Decentralize Infrastructure using Blockchain"
authors:
- Rabimba Karanjai
- Keshav Kasichainula
- Lei Xu
- Nour Diallo
- Lin Chen
- Weidong Shi
date: "2023-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-01-01T00:00:00Z"

# Publication type.
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE TNSM 2023"
publication_short: "IEEE TNSM 2023"

abstract: "Presented at IEEE TNSM 2023."

tags:
- AI
- Blockchain
- Distributed Systems
- First Author
- IEEE TNSM 2023

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

IEEE TRANSACTIONS ON NETWORK AND SERVICE MANAGEMENT, VOL. 21, NO. 2, APRIL 2024 1319
DIaC: Re-Imagining Decentralized Infrastructure
as Code Using Blockchain
Rabimba Karanjai , Keshav Kasichainula, Lei Xu , Nour Diallo, Lin Chen,
and Weidong Shi, Senior Member, IEEE
(Invited Paper)
Abstract—With the recent advances in concepts like decentral-
ized “cloud” and blockchain-enabled decentralized computing
environments, the legacy modeling and orchestration tools
developed to support centrally managed cloud-based ICT infras-
tructures are challenged by such a new paradigm built on top
of decentralization. On the other hand, decentralized “cloud”
and computing infrastructures need to support many Dapp use
cases. As the complexity of these targeted application scenarios
increases, there is an urgent need for developing automation
and modeling tools for deploying and managing decentralized
infrastructures. Instead of creating such tools from scratch, a
natural approach is extending mature infrastructure modeling
tools for Dapps and decentralized computing environments. To
this end, in this work, we have developed extensions to the
TOSCA domain-speciﬁc language to support smart contract
speciﬁcation of decentralized computing infrastructures for sup-
porting Dapps, where smart contracts or chain codes manage a
decentralized computing environment. The result is blockchain-
based orchestration and automation for decentralized “cloud”
and computing environments that use existing infrastructure as
code tools to deploy and manage decentralized applications.
Index Terms —TOSCA, smart contracts, blockchain, infras-
tructures.
I. I NTRODUCTION
ODERN ICT (information and communication tech-
nology) infrastructures are becoming increasingly
sophisticated and infeasible to manage manually. Various
technologies have been developed to support efﬁcient and
ﬂexible physical ICT infrastructure management, such as com-
puter virtualization, software-deﬁned networks, and network
function virtualization. To further automate the deployment,
conﬁguration, and management of centralized infrastruc-
tures like a cloud-based ICT center, system administrators
have been using orchestration tools [1] to dynamically
deploy services. These orchestration tools are usually cen-
trally managed by so-called orchestrators. An administrator
Manuscript received 20 May 2023; revised 2 September 2023; accepted 26
September 2023. Date of publication 18 October 2023; date of current version
15 April 2024. The associate editor coordinating the review of this article
and approving it for publication was A. Veneris. (Corresponding author:
Rabimba Karanjai.)
Rabimba Karanjai, Keshav Kasichainula, Nour Diallo, and Weidong Shi
are with the Department of Computer Science, University of Houston,
Houston, TX 77204 USA (e-mail: rkaranjai@uh.edu; kkasichainula@uh.edu;
ndiallo@uh.edu; wshi3@uh.edu).
Lei Xu is with the Department of Computer Science, Kent State University,
Kent, OH 44240 USA (e-mail: xuleimath@gmail.com).
Lin Chen is with the Department of Computer Science, Texas Tech
University, Lubbock, TX 79409 USA (e-mail: lin.chen@ttu.edu).
Digital Object Identiﬁer 10.1109/TNSM.2023.3325768
fully trusts the orchestrator to manage and coordinate the
lifecycles of ICT components (e.g., computation, storage,
and communication resources), which constitute a deployed
service. To further improve the management of the ICT
infrastructure, the concept of “infrastructure-as-code” was
developed [2], where a system administrator describes the
target infrastructure and orchestration objectives as documents
using a domain-speciﬁc language. This concept brings several
advantages, such as faster conﬁguration and environment pro-
visioning, greater consistency, and minimized risk/enhanced
security.
One of the most popular domain-speciﬁc languages
for infrastructure deﬁnition is TOSCA (Topology and
Orchestration Speciﬁcation for Cloud Applications [3]),
which helps manage and automate the cloud-based ...

(Text automatically extracted from paper. See PDF for full details and illustrations.)