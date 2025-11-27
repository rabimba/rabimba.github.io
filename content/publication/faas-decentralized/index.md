---
title: "FaaS: Decentralized Function-as-a-Service for Emerging dApps"
authors:
- Rabimba Karanjai
- Nour Diallo
- Chen
- Weidong Shi
date: "2023-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-01-01T00:00:00Z"

# Publication type.
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE ICBC 2023"
publication_short: "IEEE ICBC 2023"

abstract: "Presented at IEEE ICBC 2023."

tags:
- First Author
- IEEE ICBC 2023

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

DeFaaS: Decentralized Function-as-a-Service
for Emerging dApps and Web3
Rabimba Karanjai∗,Lei Xu†, Nour Diallo∗, Lin Chen‡, Weidong Shi∗
∗University Of Houston, TX, USA
{rkaranjai, ndiallo, wshi3}@uh.edu
†Kent State University, OH, USA , ‡ Texas Tech University, TX, USA
xuleimath@gmail.com, lin.chen@ttu.edu
to encompass both managed and volunteer-contributed
computing resources, a topic of future research.
II. Detailed Design of DeFaaS
In this section, we describe the details of the main
components of the system.
A. Decentralized Scheduling and Load Balancing
DeFaaS utilizes a decentralized front-end for
scheduling API calls, avoiding any centralized
component. API calls can be made to any API gateway,
with the management blockchain tracking reputation
and supporting trust management of gateway nodes.
API gateways need to be registered and may require
a minimal stake. To prevent fragmentation, policies
are enforced for gateway providers. Randomized load
balancing is used to dispatch API calls across cloud
data centers, with the power of two heuristic achieving
good performance with low overhead [8], [9].
B. Decentralized Event Distribution
In DeFaaS, event distribution for dApps and Web3 ap-
plications is implemented using GossipSub [10], which
is a message propagation system that relies on a mesh
network structure and a score function to disseminate
messages in a decentralized manner across multiple
cloud service providers. GossipSub is adopted by sev-
eral important blockchain systems including Filecoin
and ETH2.0 Network. Function triggers can be imple-
mented as a connector module in OpenFaaS, which
is flexible enough to support multiple event trigger
sources. The GossipSub connector maps topic-based
events to the registered functions in OpenFaaS.
C. API Registration and Access Control
API providers register their API end-points on the
management blockchain through a smart contract with
a mapping to the provider’s account. End-points can be
public or private, with access control policies set for
each end-point. Policies are stored in a map associated
with the end-point and wallet address, and can be
verified by querying the on-chain state. For public end-
points, access verification is not needed.
Abstract—Function-as-a-service (FaaS) is an emerg-
ing computation architecture, which provides high scal-
ability and flexibility. A ll t he e xisting FaaS s ystems are 
owned and managed by a single cloud service provider. 
While this is not an issue for most existing enterprise 
applications, such character is not compatible with the 
decentralization principle of dApp/Web3 applications, 
more of which are being deployed in the cloud envi-
ronment. Therefore, there is an urgent need to build 
a decentralized FaaS, which is managed by multiple 
cloud service providers and allows a decentralized ap-
plication to take advantages of FaaS. In this research 
paper, we propose DeFaaS, a novel system for managing 
decentralized FaaS using blockchain technology and 
decentralized API management, where functions are 
executed on a distributed network of nodes by multi-
cloud data centers, rather than on a centralized server. 
This allows for greater scalability and flexibility, as well 
as improved security and reliability.
Index Terms—cloud, FaaS, blockchain, Web3, dApp, 
decentralization
I. Introduction
The future of Web3 [1] and blockchain will likely 
be supported by both decentralized ICT (Informa-
tion and Communications Technology) infrastructures
like computation and storage resources contributed
by volunteers [2] and managed ICT infrastructures 
like general-purpose computing resources provided by
cloud service providers. In recent years, there are a
number of projects proposing decentralized electronic 
marketplaces for computing resources, for instance,
iEXEC [3], Golem [4], SONM [5], DRIVE (Distributed
Resource Infrastructure for a Virtual Economy) [6],
DFinity network [7], and many others.
In this work, we propose a transfo...

(Text automatically extracted from paper. See PDF for full details and illustrations.)