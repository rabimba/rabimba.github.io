import os

publications = [
    {
        "title": "Evaluating Quality of Randomness and Entropy in Tasks Supported by Large Language Models",
        "date": "2025-01-01",
        "authors": ["Rabimba Karanjai", "Ranjith Sarapu", "Weidong Shi"],
        "publication": "Agentic GenAI Evaluation 2025",
        "type": "1",
        "filename": "evaluating-quality-randomness"
    },
    {
        "title": "Collaboration is all you need: LLM Assisted Safe Code Translation",
        "date": "2025-01-01",
        "authors": ["Rabimba Karanjai", "Blackshear", "Weidong Shi"],
        "publication": "2025",
        "type": "1",
        "filename": "collaboration-safe-code-translation"
    },
    {
        "title": "Synthesizing Public Opinions with LLMs: Creation, Impacts, and the Future to eDemocracy",
        "date": "2025-04-01",
        "authors": ["Rabimba Karanjai", "Boris Shor", "Amanda Austin", "Kennedy", "Weidong Shi"],
        "publication": "IEEE ICEDEG 2025",
        "type": "1",
        "filename": "synthesizing-public-opinions"
    },
    {
        "title": "LogBabylon: A Unified Framework for Cross-Log File Integration and Analysis",
        "date": "2025-01-01",
        "authors": ["Rabimba Karanjai", "Dana Alsagheer", "Keshav Kasichainula", "Weidong Shi", "Stephen Huang"],
        "publication": "2025",
        "type": "1",
        "filename": "logbabylon"
    },
    {
        "title": "AI-Based Personalized Interventions for Atherosclerosis using Microbiota Signatures",
        "date": "2025-01-01",
        "authors": ["Rabimba Karanjai", "Surajumder", "Koushik Sen"],
        "publication": "SynBio 2025",
        "type": "1",
        "filename": "ai-personalized-interventions"
    },
    {
        "title": "Smart Contract Translation Concepts",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "Foundations of Software Engineering (FSE) 2024",
        "type": "1",
        "filename": "smart-contract-translation"
    },
    {
        "title": "Cryptographic Accelerator",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Sangw Shin", "Yujie Xiong", "Xinxin Chen", "Tian Zhang", "Suh", "Weidong Shi", "Veronika", "Francesco Sica"],
        "publication": "MICR 2024",
        "type": "1",
        "filename": "cryptographic-accelerator"
    },
    {
        "title": "Adding Flavors: Hybrid Random Number Generator for dApps in Web3",
        "date": "2024-01-01",
        "authors": ["Ranjith Sarapu", "Rabimba Karanjai", "Xinxin", "Larry Shi"],
        "publication": "International Symposium on Stabilization, Safety, and Security of Distributed Systems (SSS) 2024",
        "type": "1",
        "filename": "adding-flavors-rng"
    },
    {
        "title": "Trusted Infer Edge with Smart Contracts",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "IEEE ICBC 2024",
        "type": "1",
        "filename": "trusted-infer-edge"
    },
    {
        "title": "Decentralize over Multi-Clouds",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Lin Chen", "Nour Diallo", "Weidong Shi"],
        "publication": "2024",
        "type": "1",
        "filename": "decentralize-multi-clouds"
    },
    {
        "title": "Voter",
        "date": "2024-01-01",
        "authors": ["Nour Diallo", "Dana Alsagheer", "Rabimba Karanjai", "Weidong Shi", "Mohammad Kamal"],
        "publication": "IEEE ICEDEG 2024",
        "type": "1",
        "filename": "voter-blockchain"
    },
    {
        "title": "DIaC: Re-imagining Decentralize Infrastructure using Blockchain",
        "date": "2023-01-01",
        "authors": ["Rabimba Karanjai", "Keshav Kasichainula", "Lei Xu", "Nour Diallo", "Lin Chen", "Weidong Shi"],
        "publication": "IEEE TNSM 2023",
        "type": "2",
        "filename": "diac-infrastructure"
    },
    {
        "title": "Smarter? Empirical Study AI-based Smart Contract Creation",
        "date": "2023-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "BRAINS 2023",
        "type": "1",
        "filename": "smarter-smart-contract"
    },
    {
        "title": "Supporting Heterogeneous Critical Infrastructure Protection",
        "date": "2023-01-01",
        "authors": ["Rabimba Karanjai", "Collier", "Zhimin Gao", "Chen", "Xinxin", "Weidong Shi"],
        "publication": "AsiaCCS 2023",
        "type": "1",
        "filename": "supporting-heterogeneous-infra"
    },
    {
        "title": "Privacy Preserving Event Transaction System in Decentralized Environment",
        "date": "2021-01-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Zhimin Gao", "Lin Chen", "Mudabbir Kaleem", "Weidong Shi"],
        "publication": "Middleware 2021",
        "type": "1",
        "filename": "privacy-preserving-event"
    },
    {
        "title": "Conditional Crypto-currency With Privacy",
        "date": "2021-01-01",
        "authors": ["Rabimba Karanjai", "Zhimin Gao", "Chen", "Mudabbir Kaleem", "Weidong Shi"],
        "publication": "IEEE ICBC 2021",
        "type": "1",
        "filename": "conditional-cryptocurrency"
    },
    {
        "title": "Event Driven Framework Smart Contract Execution",
        "date": "2021-01-01",
        "authors": ["Mudabbir Kaleem", "Keshav Kasichainula", "Rabimba Karanjai", "Lei Xu", "Zhimin Gao", "Lin Chen", "Weidong Shi"],
        "publication": "DEBS 2021",
        "type": "1",
        "filename": "event-driven-framework"
    },
    {
        "title": "Optimizing Virtual Reality",
        "date": "2018-01-01",
        "authors": ["Rabimba Karanjai"],
        "publication": "Masters Thesis, Rice University",
        "type": "7",
        "filename": "optimizing-vr-thesis"
    },
    {
        "title": "Unlocking On-Chain Intelligence: Tactic Framework GenAI-Power Smart Contracts",
        "date": "2025-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "BRAINS 2025",
        "type": "1",
        "filename": "unlocking-onchain-intelligence"
    },
    {
        "title": "Ransomware 3.0: Enhancing Management Mitigation Options with Proof-of-Decryptability Smart Contracts",
        "date": "2025-01-01",
        "authors": ["Hou", "Rabimba Karanjai", "Weidong Shi"],
        "publication": "IEEE ICBC 2025",
        "type": "1",
        "filename": "ransomware-3-0"
    },
    {
        "title": "FaaS: Decentralized Function-as-a-Service for Emerging dApps",
        "date": "2023-01-01",
        "authors": ["Rabimba Karanjai", "Nour Diallo", "Chen", "Weidong Shi"],
        "publication": "IEEE ICBC 2023",
        "type": "1",
        "filename": "faas-decentralized"
    },
    {
        "title": "Decentralize Infrastructure Heterogeneous",
        "date": "2023-01-01",
        "authors": ["Rabimba Karanjai", "Zhimin Gao", "Chen", "Xinxin Suh", "Weidong Shi"],
        "publication": "IEEE ICBC 2023",
        "type": "1",
        "filename": "decentralize-infra-heterogeneous"
    },
    {
        "title": "Mitigating Hallucinations AI-Driven Diagnosis",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Surajumder"],
        "publication": "Annual Health Conference Rice University 2024",
        "type": "1",
        "filename": "mitigating-hallucinations"
    },
    {
        "title": "Enhancing Vascular Disease Diagnosis through AI-Driven Analysis of Histopathology Images",
        "date": "2024-01-01",
        "authors": ["Rabimba Karanjai", "Surajumder"],
        "publication": "Annual Health Conference Rice University 2024",
        "type": "1",
        "filename": "enhancing-vascular-diagnosis"
    },
    {
        "title": "Evaluating Rationality Language Models Questions",
        "date": "2024-01-01",
        "authors": ["Dana Alsagheer", "Rabimba Karanjai", "Weidong Shi", "Nour Diallo", "Suha Beydoun", "Qiaoning Zhang"],
        "publication": "HEAL 2024",
        "type": "1",
        "filename": "evaluating-rationality"
    },
    {
        "title": "VerifyGen-X: Cross-Chain Smart Contract Generation",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "SANER 2026 (Under Review)",
        "type": "3",
        "filename": "verifygen-x"
    },
    {
        "title": "Vision Language Models Anchor",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi", "Chengming Zhang"],
        "publication": "CVPR 2026 (Under Review)",
        "type": "3",
        "filename": "vision-language-models-anchor"
    },
    {
        "title": "Bridging Confidentiality Reliability: Ten-Weight Agents Reasoning",
        "date": "2026-01-01",
        "authors": ["Dana Alsagheer", "Weidong Shi", "Rabimba Karanjai"],
        "publication": "Symp Computer Science 2026 (Under Review)",
        "type": "3",
        "filename": "bridging-confidentiality-reliability"
    },
    {
        "title": "CausalGraphX: Counter-factual Neural Network Framework Explainable Systemic Assessment",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Heman Hegadehalli Madhavarao", "Weidong Shi"],
        "publication": "AAAI 2026 (Under Review)",
        "type": "3",
        "filename": "causalgraphx"
    },
    {
        "title": "Training LLMs Decentralized Clouds",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "2026 (Under Review)",
        "type": "3",
        "filename": "training-llms-decentralized"
    }
]

base_path = "content/publications"

for pub in publications:
    folder_path = os.path.join(base_path, pub["filename"])
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "index.md")
    
    authors_yaml = "\n".join([f"- {author}" for author in pub["authors"]])
    
    content = f"""---
title: "{pub['title']}"
authors:
{authors_yaml}
date: "{pub['date']}T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "{pub['date']}T00:00:00Z"

# Publication type.
publication_types: ["{pub['type']}"]

# Publication name and optional abbreviated publication name.
publication: "{pub['publication']}"
publication_short: "{pub['publication']}"

abstract: "Presented at {pub['publication']}."

tags:
- Research
- {pub['publication']}

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
"""
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created {file_path}")


