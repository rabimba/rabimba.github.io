---
title: "Decentralize Infrastructure Heterogeneous"
authors:
- Rabimba Karanjai
- Zhimin Gao
- Chen
- Xinxin Suh
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
- Distributed Systems
- First Author
- IEEE ICBC 2023

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

DHTee: Decentralized Infrastructure for
Heterogeneous TEEs
Rabimba Karanjai∗, Zhimin Gao §,Lin Chen‡ Xinxin Fan¶, Teweon Suh∥, Weidong Shi∗, Lei Xu †
∗University Of Houston,USA, †Kent State University,USA , ‡ Texas Tech University,USA
{rkaranjai, wshi3}@uh.edu, xuleimath@gmail.com, lin.chen@ttu.edu
§ Auburn University at Montgomery,USA, ¶ IoTeX,USA, ∥ Korea University,South Korea
xinxin@iotex.io, suhtw@korea.ac.kr
Abstract—Trusted execution environment (TEE) technology has
many uses, such as protecting data in the cloud and improving
security for industrial IoT. However, there are technical challenges
that limit its widespread adoption. These challenges include the
fact that different TEE vendors have incompatible solutions, and
devices equipped with the same TEE technology may belong to
different owners, making it difficult to establish trust between
them. To address these challenges and fully utilize TEE technology,
a decentralized coordination mechanism called DHTee is proposed.
DHTee uses blockchain technology to support key TEE functions
in a heterogeneous TEE environment, especially attestation service.
Devices equipped with TEE can interact securely with the
blockchain to determine whether potential collaborating devices
meet the requirements. DHTee is also flexible and can support
new TEE schemes without affecting existing TEEs.
Index Terms—TEE, blockchain, heterogeneous
A device only needs to be modified to support this common
format to interact with other devices in the ecosystem. When
a new type of TEE scheme is introduced, only the blockchain
system needs to be updated and will not affect existing devices.
DHTee brings several benefits: (i) It offers a unified framework
to support heterogeneous TEE systems; (ii) It reduces the
system management complexity and can easily support new
TEE systems; (iii) It eliminates the single point of failure in
the attestation process; and (iv) It protects information stored
on the blockchain without affecting the function to support
heterogeneous TEEs. In summary, our contributions in the
paper include:
• We clarify the essential requirements on the design of a
heterogeneous TEE system.
• We propose the detailed design of DHTee that leverages
blockchain technology to support the collaboration of
multiple TEE schemes.
• Analysis and evaluations are done to demonstrate the
security and practicability of DHTee.
II. O VERVIEW OF DHT EE
This section provides an overview of DHTee and outlines
its design goals.
A. Major Participants
Fig. 1 provides an overview of the abstract structure of
DHTee, and there are mainly two types of participants involved:
• Devices. The system consists of multiple computation
devices equipped with different TEE solutions, owned
and managed by different entities. They work together
to complete a secure computing task, exchanging results
between TEEs without leakage to non-TEE devices, as
required by the task.
• Blockchain. The system uses a blockchain as a coordinator
between devices and for attestation services. Blockchain
nodes run a consensus protocol, and only authorized
nodes maintain the permissioned blockchain, which has a
public/private key identity system.
B. Assumptions and Design Goals of DHTee
Design goals of DHTee. DHTee is designed to support the
interoperation of heterogeneous TEE schemes, and devices
I. INTRODUCTION
New computing paradigms and application scenarios such 
as cloud computing and edge computing, smart manufacturing 
[1], federated machine learning [2], and general data trading 
[3] emphasize resource sharing and collaboration, leading 
to improved system efficiency, fl exibility, an d robustness. 
However, collaborative computing brings security and privacy 
challenges. Various techniques have been developed to mitigate 
these challenges, including cryptographic tools like fully ho-
momorphic encryption [4] and secure multi-party computation 
[5], and access control and isolation mechanisms. Trusted 
execution environment (TEE) t...

(Text automatically extracted from paper. See PDF for full details and illustrations.)