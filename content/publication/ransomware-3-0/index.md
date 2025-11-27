---
title: "Ransomware 3.0: Enhancing Management Mitigation Options with Proof-of-Decryptability Smart Contracts"
authors:
- Hou
- Rabimba Karanjai
- Weidong Shi
date: "2025-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-01T00:00:00Z"

# Publication type.
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE ICBC 2025"
publication_short: "IEEE ICBC 2025"

abstract: "Presented at IEEE ICBC 2025."

tags:
- Blockchain
- IEEE ICBC 2025
- Security

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

Ransomware 3.0: Enhancing Risk Management and
Mitigation Options with Proof-of-Decryptability and
Smart Contracts
Xinyu Hou
University of Science and Technology of China
houxinyu123@mail.ustc.edu.cn
Yang Lu
University of Houston
ylu17@central.uh.edu
Rabimba Karanjai
University of Houston
rkaranjai@uh.edu
Lei Xu
Kent State University
xuleimath@gmail.com
Larry Shi
University of Houston
wshi3@uh.edu
Abstract—Ransomware attacks have become increasingly so-
phisticated and dangerous, severely impacting individuals and
businesses. Traditional ransomware payout models lack trust and
security, leaving victims vulnerable to extortion even after paying
the ransom. We proposes Ransomware 3.0, a novel blockchain-
based ransomware framework that leverages zero-knowledge
proofs and smart contracts to overcome these challenges. By inte-
grating these cryptographic techniques, Ransomware 3.0 ensures
secure and verifiable data recovery for victims while reducing
the risk of data exposure or resale by ransomware attackers.
This framework also introduces a contract-based multi-round
payment scheme that allows victims to optimize their payout
strategy based on the evolving value of their data over time.
Counterintuitively, both attackers and victims are motivated
to adopt the new model, as the victim is motivated to pay
when uncertainty is reduced. We also explore the theoretical
decision-making foundations of Ransomware 3.0, analyze its
potential benefits and limitations, and discuss its implications
for ransomware risk management and mitigation strategies.
Index Terms—ransomware, ZKPs, smart contract
I. I NTRODUCTION
In recent years, ransomware has gradually evolved into one
of the most widely used types of malicious software [1],
[2]. This type of malicious software encrypts the victim’s
important data, making it impossible to access the system and
retrieve the data, and then demands a ransom from the victim
in exchange for restoring system functionality and data files.
More and more people are falling victim to the ransomware
attacks. The potential cost of these attacks is estimated to reach
$7.5 billion [3]. Traditional ransomware encrypts information
on a victim’s computer to demand a ransom payment. It has
been modeled in ransomware 1.0. The attacker only demands a
ransom and decides whether to return the decryption key to the
victim. Ransomware 1.5 introduced data-threat ransomware.
In ransomware 2.0 [4], [5], attackers can choose to sell the
victim’s data for extra profit. With the situation for victims
increasingly helpless, We are trying to foretell the coming
and likely evolution of ransomware attacks, avoid surprises,
provide analysis and decision making tools to help the victims.
The current ransomware model will certainly evolve to take
advantage of the advances in technologies in order to attain a
new equilibrium between the attacker and the victim. Based
on this trend, we predict an emerging ransomware framework
built on top of zero-knowledge protocols [6] and smart con-
tracts [7]. We show that there exists significant incentive for
the ransom attacker to adopt this new framework. On the
other hand, the new framework provides certain benefits to
the victim as well such as better assurance of data recovery,
more options in terms of risk management, while maintaining
the attacker’s expected profit. We refer to this blockchain
ransomware as 3.0, to distinguish it from the prior ransomware
models.
II. B LOCKCHAIN BASED RANSOMWARE FRAMEWORK
Motivated by the observation that the emerging direction
of ransomware could leverage recent advances in blockchain-
based technologies and go beyond the practice of using
cryptocurrencies for ransom payments, we present a likely ad-
vanced ransomware attack framework that applies blockchain
fair data exchange and smart contracts.
A. Blockchain Fair Data Exchange and Verifiable Encryption
Researchers have recently applied blockchains and verifi-
able encryption to achieve Fair Data Exchange (FDE) ...

(Text automatically extracted from paper. See PDF for full details and illustrations.)