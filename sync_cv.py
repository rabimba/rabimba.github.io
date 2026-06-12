import os
import shutil
import difflib

# 1. Structured Publications Data
publications = [
    {
        "title": "Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation",
        "date": "2026-08-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Hemanth Hegadehalli Madhavarao", "Lei Xu", "Weidong Shi"],
        "publication": "USENIX Security 2026 (To Appear)",
        "type": "1",
        "filename": "context-contamination-logs",
        "abstract": "We analyze prompt injection risks in security log analysis systems powered by LLMs, demonstrating passive injections and proposing mitigation methods.",
        "tags": ["Security", "LLMs", "Network Security", "First Author"]
    },
    {
        "title": "CausalGraphX: A Counterfactual Graph Neural Network Framework for Explainable Systemic Risk Assessment",
        "date": "2026-02-01",
        "authors": ["Rabimba Karanjai", "Hemanth Hegadehalli Madhavarao", "Lei Xu", "Weidong Shi"],
        "publication": "AAAI 2026 (AI4Finance)",
        "type": "1",
        "filename": "causalgraphx",
        "abstract": "CausalGraphX utilizes counterfactual graph neural networks to provide explainable risk assessments in complex financial and systemic environments.",
        "tags": ["AI", "Neural Networks", "Explainable AI", "First Author"]
    },
    {
        "title": "QuCoWE: Quantum Contrastive Word Embeddings with Variational Circuits for Near-Term Quantum Devices",
        "date": "2026-02-01",
        "authors": ["Rabimba Karanjai", "Hemanth Madhavarao", "Lei Xu", "Weidong Shi"],
        "publication": "AAAI 2026 (QC+AI)",
        "type": "1",
        "filename": "qucowe",
        "abstract": "We introduce QuCoWE, a framework for contrastive word embeddings designed to run on near-term quantum processors using variational circuits.",
        "tags": ["Quantum Computing", "NLP", "Word Embeddings", "First Author"]
    },
    {
        "title": "Securing the Multi-Chain Ecosystem: A Unified, Agent-Based Framework for Vulnerability Repair in Solidity and Move",
        "date": "2025-11-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Weidong Shi"],
        "publication": "ACM AIWare 2025",
        "type": "1",
        "filename": "securing-multi-chain",
        "abstract": "This work presents an agent-based framework designed to automatically detect and repair security vulnerabilities in Solidity and Move smart contracts.",
        "tags": ["Blockchain", "Security", "Smart Contracts", "First Author", "Agents"],
        "featured": True
    },
    {
        "title": "Teaching AIs to Reason and Code, Confidentially",
        "date": "2025-07-25",
        "authors": ["Rabimba Karanjai"],
        "publication": "PhD Thesis, University of Houston",
        "type": "7",
        "filename": "teaching-ais-reason-confidentially",
        "abstract": "My doctoral dissertation addresses methods and frameworks for secure and private code generation and reasoning in LLMs.",
        "tags": ["PhD Thesis", "AI Reasoning", "First Author", "Security", "Confidentiality"],
        "featured": True
    },
    {
        "title": "HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation",
        "date": "2025-11-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Weidong Shi"],
        "publication": "ACM AIWare 2025",
        "type": "1",
        "filename": "hpc-agent-tester",
        "abstract": "We explore multi-agent LLM systems to improve unit test generation for High-Performance Computing (HPC) software environments.",
        "tags": ["HPC", "Testing", "Agents", "First Author"]
    },
    {
        "title": "Evaluating the Quality of Randomness and Entropy in Tasks Supported by Large Language Models",
        "date": "2025-08-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Ranjith Chodavarapu", "Lei Xu", "Weidong Shi"],
        "publication": "KDD - Agentic & GenAI Evaluation 2025",
        "type": "1",
        "filename": "evaluating-quality-randomness",
        "abstract": "We evaluate how LLMs generate entropy and pseudorandom outputs in critical computational tasks, identifying key vulnerabilities and patterns.",
        "tags": ["LLMs", "Randomness", "Entropy", "Security", "First Author"]
    },
    {
        "title": "Collaboration is all you need: LLM Assisted Safe Code Translation",
        "date": "2025-06-01",
        "authors": ["Rabimba Karanjai", "Sam Blackshear", "Lei Xu", "Weidong Shi"],
        "publication": "ACM Foundations of Software Engineering (FSE) 2025",
        "type": "1",
        "filename": "collaboration-safe-code-translation",
        "abstract": "We present collaborative LLM strategies to safely translate source code between low-resource or domain-specific languages with formal checks.",
        "tags": ["LLMs", "Software Engineering", "Code Translation", "First Author"]
    },
    {
        "title": "Synthesizing Public Opinions with LLMs: Role Creation, Impacts, and the Future to eDemocracy",
        "date": "2025-04-01",
        "authors": ["Rabimba Karanjai", "Boris Shor", "Amanda Austin", "Ryan Kennedy", "Yang Lu", "Lei Xu", "Weidong Shi"],
        "publication": "ICEDEG 2025",
        "type": "1",
        "filename": "synthesizing-public-opinions",
        "abstract": "We investigate the potential of LLMs to model and synthesize diverse public opinions, exploring ethical dimensions and technical accuracy.",
        "tags": ["LLMs", "eDemocracy", "AI Society", "First Author"]
    },
    {
        "title": "LogBabylon: A Unified Framework for Cross-Log File Integration and Analysis",
        "date": "2025-03-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Dana Alsagheer", "Keshav Kasichainula", "Lei Xu", "Weidong Shi", "Stephen Huang"],
        "publication": "ACM SAC 2025",
        "type": "1",
        "filename": "log-babylon",
        "abstract": "LogBabylon provides a unified framework for matching and integrating log files across different systems to improve security audits and diagnostics.",
        "tags": ["Security", "Log Analysis", "First Author"]
    },
    {
        "title": "AI-Based Target for Personalized Interventions of Atherosclerosis from Gut Microbiota Signature",
        "date": "2025-02-01",
        "authors": ["Suravi Majumder", "Koushik Sen", "Rabimba Karanjai"],
        "publication": "SynBio 2025",
        "type": "1",
        "filename": "ai-personalized-interventions",
        "abstract": "We detail an AI framework that parses gut microbiota signatures to design personalized dietary or medical interventions for atherosclerosis.",
        "tags": ["AI", "Bioinformatics", "Microbiota"]
    },
    {
        "title": "Smart Contract Code Translation based on Concepts",
        "date": "2024-11-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Weidong Shi"],
        "publication": "ACM Foundations of Software Engineering (FSE) 2024",
        "type": "1",
        "filename": "smart-contract-translation",
        "abstract": "We explore using conceptual mappings to translate smart contracts safely between high-level smart contract languages.",
        "tags": ["Smart Contracts", "Blockchain", "Code Translation", "First Author"]
    },
    {
        "title": "TPU as Cryptographic Accelerator",
        "date": "2024-10-01",
        "authors": ["Rabimba Karanjai", "Sangwon Shin", "Wujie Xiong", "Xinxin Fan", "Lin Chen", "Tianwei Zhang", "Taeweon Suh", "Weidong Shi", "Veronika Kuchta", "Francesco Sica", "Lei Xu"],
        "publication": "MICRO 2024",
        "type": "1",
        "filename": "cryptographic-accelerator",
        "abstract": "We investigate leveraging Tensor Processing Units (TPUs) to accelerate intensive cryptographic primitives in blockchain and zero-knowledge systems.",
        "tags": ["TPU", "Cryptography", "Hardware Accelerator", "First Author"]
    },
    {
        "title": "Adding All Flavors: A Hybrid Random Number Generator for dApps and Web3",
        "date": "2024-09-01",
        "authors": ["Ranjith Chodavarapu", "Rabimba Karanjai", "Xinxin Fan", "Larry Shi", "Lei Xu"],
        "publication": "International Symposium on Stabilization, Safety, and Security of Distributed Systems (SSS) 2024",
        "type": "1",
        "filename": "adding-flavors-rng",
        "abstract": "We propose a hybrid on-chain and off-chain random number generator suitable for decentralized applications (dApps) requiring high entropy.",
        "tags": ["Web3", "Randomness", "dApps", "Security"]
    },
    {
        "title": "Trusted LLM Inference on the Edge with Smart Contracts",
        "date": "2024-05-01",
        "authors": ["Rabimba Karanjai", "Weidong Shi"],
        "publication": "IEEE ICBC 2024",
        "type": "1",
        "filename": "trusted-infer-edge",
        "abstract": "We propose a trust framework using smart contracts to audit and verify edge-computed LLM inference outputs.",
        "tags": ["LLMs", "Smart Contracts", "Edge Computing", "First Author"]
    },
    {
        "title": "Decentralized FaaS over Multi-Clouds",
        "date": "2024-03-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Lin Chen", "Nour Diallo", "Weidong Shi"],
        "publication": "ACM SAC 2024",
        "type": "1",
        "filename": "decentralize-multi-clouds",
        "abstract": "We introduce a decentralized Function-as-a-Service (FaaS) model that coordinates execution tasks across multiple cloud networks.",
        "tags": ["Decentralized Systems", "FaaS", "Cloud Computing", "First Author"]
    },
    {
        "title": "All We Need is Voter Feedback",
        "date": "2024-04-01",
        "authors": ["Nour Diallo", "Dana Alsagheer", "Lei Xu", "Yang Lu", "Rabimba Karanjai", "Weidong Shi", "Mohammad Kamal"],
        "publication": "IEEE ICEDEG 2024",
        "type": "1",
        "filename": "voter-blockchain",
        "abstract": "We study decentralized governance architectures that incorporate continuous feedback loops via blockchain votes.",
        "tags": ["Blockchain", "Governance", "Decentralized Voting"]
    },
    {
        "title": "DIaC: Re-imagining Decentralized Infrastructure As Code using Blockchain",
        "date": "2023-11-01",
        "authors": ["Rabimba Karanjai", "Keshav Kasichainula", "Lei Xu", "Nour Diallo", "Lin Chen", "Weidong Shi"],
        "publication": "IEEE TNSM 2023",
        "type": "2",
        "filename": "diac-infrastructure",
        "abstract": "We propose DlaC, a system that uses smart contracts to securely manage and audit cloud infrastructure deployment configurations.",
        "tags": ["Blockchain", "Infrastructure as Code", "First Author"]
    },
    {
        "title": "Who is Smarter? An Empirical Study of AI-based Smart Contract Creation",
        "date": "2023-10-01",
        "authors": ["Rabimba Karanjai", "E Li", "L Xu", "W Shi"],
        "publication": "BRAINS 2023",
        "type": "1",
        "filename": "smarter-smart-contract",
        "abstract": "We conduct a comparative study evaluating the quality, safety, and functionality of smart contracts generated by LLMs vs human engineers.",
        "tags": ["LLMs", "Smart Contracts", "Empirical Study", "First Author"]
    },
    {
        "title": "Supporting Heterogeneous TEE for Critical Infrastructure Protection",
        "date": "2023-05-01",
        "authors": ["Rabimba Karanjai", "Rowan Collier", "Zhimin Gao", "Lin Chen", "Xinxin Fan", "Taeweon Suh", "Weidong Shi", "Lei Xu"],
        "publication": "ACM AsiaCCS 2023",
        "type": "1",
        "filename": "supporting-heterogeneous-infra",
        "abstract": "We design a middleware framework to secure critical systems using multiple diverse Trusted Execution Environments (TEEs).",
        "tags": ["Security", "TEE", "Hardware Security", "First Author"]
    },
    {
        "title": "Decentralized Application Infrastructures as Smart Contract Codes",
        "date": "2022-05-01",
        "authors": ["Rabimba Karanjai", "Keshav Kasichainula", "Nour Diallo", "Mudabbir Kaleem", "Lei Xu", "Lin Chen", "Weidong Shi"],
        "publication": "IEEE ICBC 2022",
        "type": "1",
        "filename": "decentralized-apps",
        "abstract": "We introduce secure frameworks for modeling decentralized application deployment using smart contracts, earning the Distinguished Paper Award.",
        "tags": ["Blockchain", "Smart Contracts", "First Author"],
        "featured": True
    },
    {
        "title": "Privacy preserving event based transaction system in a decentralized environment",
        "date": "2021-12-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Zhimin Gao", "Lin Chen", "Mudabbir Kaleem", "Weidong Shi"],
        "publication": "ACM Middleware 2021",
        "type": "1",
        "filename": "privacy-preserving-event",
        "abstract": "We detail a middleware layer that guarantees transactional privacy in distributed event-driven architectures.",
        "tags": ["Privacy", "Distributed Transactions", "First Author"]
    },
    {
        "title": "On Conditional Cryptocurrency With Privacy",
        "date": "2021-05-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Zhimin Gao", "Lin Chen", "Mudabbir Kaleem", "Weidong Shi"],
        "publication": "IEEE ICBC 2021",
        "type": "1",
        "filename": "conditional-cryptocurrency",
        "abstract": "We design a cryptosystem that enables conditional transfers on public ledgers without revealing user balances or identity links.",
        "tags": ["Blockchain", "Cryptocurrency", "Privacy", "First Author"]
    },
    {
        "title": "Lessons Learned from Blockchain Applications of Trusted Execution Environments and Implications",
        "date": "2021-11-01",
        "authors": ["Rabimba Karanjai", "L Xu", "L Chen", "F Zhang", "Z Gao", "W Shi"],
        "publication": "ACM HASP 2021",
        "type": "1",
        "filename": "blockchain-tee",
        "abstract": "We survey the integration of TEEs in smart contract execution environments, identifying practical security pitfalls and performance trade-offs.",
        "tags": ["TEE", "Blockchain", "Hardware Security", "First Author"]
    },
    {
        "title": "An event driven framework for smart contract execution",
        "date": "2021-06-01",
        "authors": ["Mudabbir Kaleem", "Keshav Kasichainula", "Rabimba Karanjai", "Lei Xu", "Zhimin Gao", "Lin Chen", "Weidong Shi"],
        "publication": "ACM DEBS 2021",
        "type": "1",
        "filename": "event-driven-framework",
        "abstract": "We build an asynchronous event-driven system to schedule and execute smart contract actions, increasing ledger throughput.",
        "tags": ["Blockchain", "Event Driven", "Smart Contracts"]
    },
    {
        "title": "Optimizing Web Virtual Reality",
        "date": "2018-05-01",
        "authors": ["Rabimba Karanjai"],
        "publication": "Masters Thesis, Rice University",
        "type": "7",
        "filename": "optimizing-vr-thesis",
        "abstract": "My masters thesis explores optimizing resource rendering and memory models for Web VR systems built on WebGL and Three.js.",
        "tags": ["Virtual Reality", "Web Technologies", "First Author"]
    },
    # Short Papers
    {
        "title": "Empowering Smart Contracts with Real-time On-Chain AI Inferences",
        "date": "2026-05-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong (Larry) Shi"],
        "publication": "IEEE ICBC 2026",
        "type": "1",
        "filename": "empowering-smart-contracts-ai",
        "abstract": "Short Paper: We detail low-latency inference pipelines that check and execute simple models on-chain.",
        "tags": ["Smart Contracts", "AI Inference", "First Author"]
    },
    {
        "title": "Unlocking On-Chain Intelligence: A Practical Framework for GenAI-Powered Smart Contracts",
        "date": "2025-11-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong (Larry) Shi"],
        "publication": "BRAINS 2025",
        "type": "1",
        "filename": "unlocking-onchain-intelligence",
        "abstract": "Short Paper: Introducing a framework to interface Large Language Models with blockchain states safely.",
        "tags": ["Smart Contracts", "Generative AI", "First Author"]
    },
    {
        "title": "Ransomware 3.0: Enhancing Risk Management and Mitigation Options with Proof-of-Decryptability and Smart Contracts",
        "date": "2025-05-01",
        "authors": ["Xinyu Hou", "Yang Lu", "Rabimba Karanjai", "Lei Xu", "Weidong Shi"],
        "publication": "IEEE ICBC 2025",
        "type": "1",
        "filename": "ransomware-3-0",
        "abstract": "Short Paper: We design smart contracts verifying decryption keys in escrow to manage ransomware extortion threats.",
        "tags": ["Blockchain", "Security", "Ransomware"]
    },
    {
        "title": "DeFaaS: Decentralized Function-as-a-Service for Emerging dApps and Web",
        "date": "2023-05-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Nour Diallo", "Lin Chen", "Weidong Shi"],
        "publication": "IEEE ICBC 2023",
        "type": "1",
        "filename": "faas-decentralized",
        "abstract": "Short Paper: We design lightweight container orchestrators over public blockchains for serverless edge compute.",
        "tags": ["FaaS", "Blockchain", "Edge Computing", "First Author"]
    },
    {
        "title": "DHTee: Decentralized Infrastructure for Heterogeneous TEE",
        "date": "2023-05-01",
        "authors": ["Rabimba Karanjai", "Zhimin Gao", "Lin Chen", "Xinxin Fan", "Taeweon Suh", "Weidong Shi", "Lei Xu"],
        "publication": "IEEE ICBC 2023",
        "type": "1",
        "filename": "decentralize-infra-heterogeneous",
        "abstract": "Short Paper: Building structured overlays for auditing and routing data across multi-vendor secure enclaves.",
        "tags": ["TEE", "Security", "First Author"]
    },
    {
        "title": "Decentralized Machine Learning Governance: Overview, Opportunities, and Research Challenges",
        "date": "2023-05-01",
        "authors": ["Dana R Alsagheer", "Nour Diallo", "Lei Xu", "Rabimba Karanjai", "Weidong Shi"],
        "publication": "IEEE ICBC 2023",
        "type": "1",
        "filename": "ai-governance",
        "abstract": "Short Paper: We map the open questions and technical roadblocks in establishing decentralized protocols for auditing ML model weights.",
        "tags": ["AI Governance", "Security", "Decentralized Systems"]
    },
    # Workshops
    {
        "title": "Mitigating Hallucinations in AI-Driven Medical Diagnosis",
        "date": "2024-05-01",
        "authors": ["Rabimba Karanjai", "Suravi Majumder"],
        "publication": "3rd Annual AI in Health Conference, Rice University",
        "type": "1",
        "filename": "mitigating-hallucinations",
        "abstract": "Workshop Paper: We address medical hallucination mitigation in conversational diagnostic models through structured knowledge reinforcement.",
        "tags": ["AI", "Health", "LLM Hallucinations", "First Author"]
    },
    {
        "title": "Enhancing Vascular Disease Diagnosis through AI-Driven Analysis of Histopathology Images",
        "date": "2024-05-01",
        "authors": ["Rabimba Karanjai", "Suravi Majumder"],
        "publication": "3rd Annual AI in Health Conference, Rice University",
        "type": "1",
        "filename": "enhancing-vascular-diagnosis",
        "abstract": "Workshop Paper: Deep learning classifier pipelines designed to analyze histopathological tissue slides for diagnosing vascular disease.",
        "tags": ["AI", "Health", "Computer Vision", "First Author"]
    },
    {
        "title": "Evaluating Irrationality in Large Language Models and Open Research Questions",
        "date": "2024-05-01",
        "authors": ["Dana R Alsagheer", "Rabimba Karanjai", "Weidong Shi", "Nour Diallo", "Yang Lu", "Suha Beydoun", "Qiaoning Zhang"],
        "publication": "ACM CHI HEAL 2024",
        "type": "1",
        "filename": "evaluating-rationality",
        "abstract": "Workshop Paper: We examine cognitive cognitive anomalies and systematic biases in LLM choices when given human reasoning dilemmas.",
        "tags": ["LLMs", "Cognitive Bias", "AI Safety"]
    },
    # Under Review
    {
        "title": "Allocation Before Ranking: Decoupled Token Compression for OmniLLMs",
        "date": "2026-01-01",
        "authors": ["Zhenghui Guo", "Yilin Yang", "Yuanbin Man", "Miao Yin", "Weidong Shi", "Rabimba Karanjai", "Omprakash Gnawali", "Chengming Zhang"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "allocation-before-ranking",
        "abstract": "Preprint: We decouple token compression from routing in multi-modal systems, improving processing speeds by up to 30%.",
        "tags": ["LLMs", "Token Compression", "Efficiency"]
    },
    {
        "title": "Specialists Hold, Generalists Discount: Asymmetric Equilibrium in LLM Routing Auctions",
        "date": "2026-01-01",
        "authors": ["Xinyu Hou", "Yang Lu", "Rabimba Karanjai", "Pei-Chi Pan", "Sen Lin", "Lei Xu", "Weidong Shi"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "specialists-hold-routing",
        "abstract": "Preprint: Game-theoretic modeling of agent routing auctions to optimize multi-llm coordination structures.",
        "tags": ["LLMs", "Game Theory", "Routing"]
    },
    {
        "title": "Closing the Cost Gap in Verifier-Guided RL: A Smart Contract Case Study",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong Shi"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "closing-cost-gap-rl",
        "abstract": "Preprint: Reinforcement learning structures utilizing formal verification constraints as runtime guides to secure code compilation.",
        "tags": ["LLMs", "Reinforcement Learning", "Formal Verification", "First Author"]
    },
    {
        "title": "CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Qun Gu", "Hemanth Hegadehalii Madhavarao", "Wenhuan Sun", "Xiaojiao Yu", "Suryabhan Singh Hada", "Libin N. George", "Uma Kona", "Richard Williamson", "Linsey Pang", "Prakhar Mehrotra"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "cm-dpo-planning",
        "abstract": "Preprint: A preference optimization framework that forces planning paths to obey hard system limits.",
        "tags": ["LLMs", "Preference Optimization", "Planning", "First Author"]
    },
    {
        "title": "Rules That Govern: A Per-Property Analysis of Multi-Agent LLM Deliberation",
        "date": "2026-01-01",
        "authors": ["Yang Lu", "Rabimba Karanjai", "Dana Alsagheer", "Lei Xu", "Weidong Shi"],
        "publication": "EMNLP 2026 (Under Review)",
        "type": "3",
        "filename": "rules-that-govern",
        "abstract": "Preprint: Detailed modeling of rules and policy properties that constrain multi-agent discussion spaces.",
        "tags": ["Agents", "Multi-Agent Systems", "Policy"]
    },
    {
        "title": "Profiler: Per-Question Persona Conditioning of Frozen LLMs via Retrieval and Fusion of Synthesized Profiles",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong Shi"],
        "publication": "EMNLP 2026 (Under Review)",
        "type": "3",
        "filename": "profiler-persona",
        "abstract": "Preprint: A retrieval-augmented persona generation architecture that conditions frozen models dynamically.",
        "tags": ["LLMs", "Persona Tuning", "First Author"]
    },
    {
        "title": "VerifyGen-X: Secure Cross-Chain Smart Contract Generation via Scalable Reinforcement Learning from Formal Verification Feedback",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Yang Lu", "Weidong Shi"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "verifygen-x",
        "abstract": "Preprint: We use formal verification proofs in RL loops to ensure generated cross-chain contracts are bug-free.",
        "tags": ["Blockchain", "Generative AI", "Formal Verification", "First Author"]
    },
    {
        "title": "Aligning Vision Language Models via anchor",
        "date": "2026-01-01",
        "authors": ["Yilin Yang", "Yuke Wang", "Rabimba Karanjai", "Weidong Shi", "Chengming Zhang"],
        "publication": "NeurIPS 2026 (Under Review)",
        "type": "3",
        "filename": "vision-language-models-anchor",
        "abstract": "Preprint: Aligning visual tokens with semantic text anchors to enhance multi-modal reasoning capabilities.",
        "tags": ["Computer Vision", "Multi-Modal", "AI Alignment"]
    },
    {
        "title": "Unlocking On-Chain Intelligence: A Practical Framework for GenAI-Powered Smart Contracts",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong Shi"],
        "publication": "Middleware 2026 (Under Review)",
        "type": "3",
        "filename": "unlock-onchain-intel-mw",
        "abstract": "Preprint: Expanding on-chain capabilities by linking secure oracle execution paths with frozen LLM instances.",
        "tags": ["Blockchain", "AI Inference", "First Author"]
    },
    {
        "title": "Bridging Confidentiality and Reliability: Open-Weight Agents for Legal Reasoning",
        "date": "2026-01-01",
        "authors": ["Dana Alsagheer", "Yang Lu", "Lei Xu", "Weidong Shi", "Rabimba Karanjai"],
        "publication": "ACM Symposium on Computer Science and Law 2026 (Under Review)",
        "type": "3",
        "filename": "bridging-confidentiality-reliability",
        "abstract": "Preprint: Deploying open-weight local model instances to perform legal brief review without leakage.",
        "tags": ["AI Governance", "Security", "Law"]
    },
    {
        "title": "Hype or Hope? Training LLMs on Decentralized GPU Clouds",
        "date": "2026-01-01",
        "authors": ["Rabimba Karanjai", "Yang Lu", "Lei Xu", "Weidong Shi"],
        "publication": "Middleware 2026 (Under Review)",
        "type": "3",
        "filename": "training-llms-decentralized",
        "abstract": "Preprint: Benchmarking distributed deep learning pipelines across heterogeneous networks, auditing latency and security overhead.",
        "tags": ["Decentralized Systems", "GPU Clouds", "First Author"]
    }
]

# 2. Structured Talks Data
talks = [
    {"title": "Beyond the Chatbot: A Blueprint for Trustable AI", "event": "Google Deepmind", "year": "2026", "location": "Google Deepmind, CA", "date": "2026-04-15"},
    {"title": "United in Defense: Architecting Safe and Trustworthy AI Agents", "event": "BSides Seattle", "year": "2026", "location": "Seattle, WA", "date": "2026-03-20"},
    {"title": "Unmasking the Shadows: AI Red Teaming in the Age of Gemini and VertexAI, fortified by SAIF", "event": "KCDC", "year": "2025", "location": "Kansas City", "date": "2025-08-10"},
    {"title": "From Whiteboard to Users: Making Research Accessible", "event": "Google I/O GDE Summit", "year": "2025", "location": "Mountain View, CA", "date": "2025-05-18"},
    {"title": "Unmasking the Shadows: AI Red Teaming in the Age of Gemini and VertexAI, fortified by SAIF", "event": "Drexel University Seminar", "year": "2025", "location": "Philadelphia, PA", "date": "2025-04-05"},
    {"title": "LLM, Reasoning and Agentic Gemma", "event": "Google Korea Talk", "year": "2024", "location": "Seoul, South Korea", "date": "2024-11-12"},
    {"title": "Supercharging GenAI: Ray, Kubernetes, and TPUs for Lightning-Fast Inference", "event": "KubeCon", "year": "2024", "location": "Salt Lake City, UT", "date": "2024-11-15"},
    {"title": "LLMinABox: On Device Personalized Diary & Concierge using your voice and Gemma", "event": "Google Mount View Seminar", "year": "2024", "location": "Mountain View, CA", "date": "2024-09-08"},
    {"title": "Mitigating Hallucinations in AI-Driven Medical Diagnosis", "event": "Rice University Seminar", "year": "2024", "location": "Houston, TX", "date": "2024-05-10"},
    {"title": "SolMover: Smart Contract Code Translation Based on Concepts", "event": "Berkeley RDI Research Meeting", "year": "2024", "location": "Berkeley, CA", "date": "2024-04-20"},
    {"title": "Privacy aware Zero Knowledge Login using Oauth2 and Passkey", "event": "Columbia University", "year": "2024", "location": "New York, NY", "date": "2024-03-15"},
    {"title": "LLM Applications components and design patterns Hands on Workshop", "event": "University Of Washington Workshop", "year": "2024", "location": "Seattle, WA", "date": "2024-02-28"},
    {"title": "Give your web apps superpower with Generative AI and Mediapipe", "event": "University of Missouri - Kansas City", "year": "2024", "location": "Kansas City, MO", "date": "2024-02-10"},
    {"title": "An Empirical Study of AI-based Smart Contract Creation", "event": "Berkeley RDI", "year": "2023", "location": "Berkeley, CA", "date": "2023-11-05"},
    {"title": "On Device Generative AI: Building your own Dall-E in the browser, welcome WebGPU", "event": "Google San Jose Meetup", "year": "2023", "location": "San Jose, CA", "date": "2023-10-12"},
    {"title": "DeepSpeech: A Journey to <10% Word Error Rate", "event": "Google Mt. View & NC Chapel Hill", "year": "2023", "location": "Chapel Hill, NC", "date": "2023-09-22"},
    {"title": "Visualize your Data in a 3D VR world using A-Frame in WebVR", "event": "OpenVis Conf", "year": "2018", "location": "Boston, MA", "date": "2018-05-14"},
    {"title": "Turning sensors into signals", "event": "MIT Media Lab", "year": "2017", "location": "Cambridge, MA", "date": "2017-10-10"},
    {"title": "Hardening Your IoT Endpoints: A Preventive Toolkit", "event": "LinuxCon ContainerCon", "year": "2017", "location": "Los Angeles, CA", "date": "2017-09-12"},
    {"title": "Optimizing Web Virtual Reality", "event": "Web3d Conference", "year": "2017", "location": "Brisbane, Australia", "date": "2017-06-05"},
    {"title": "SecurityPI: IronClad your Raspberry PI", "event": "Linux Foundation Open IoT & ELC", "year": "2017", "location": "Portland, OR", "date": "2017-05-20"},
    {"title": "State of WebVR & aframe: Yesterday, Today, and Tomorrow Beyond Horizon", "event": "Open Networking Summit", "year": "2017", "location": "Santa Clara, CA", "date": "2017-04-03"}
]

# 3. Mappings of PDF filenames to publication titles
pdf_mappings = {
    "2101.05475v1.pdf": "On Conditional Cryptocurrency With Privacy",
    "2203.12724v1.pdf": "Decentralized Application Infrastructures as Smart Contract Codes",
    "2301.00665v1.pdf": "DIaC: Re-imagining Decentralized Infrastructure As Code using Blockchain",
    "2308.02955v2.pdf": "DeFaaS: Decentralized Function-as-a-Service for Emerging dApps and Web",
    "2403.09798v1.pdf": "Evaluating Irrationality in Large Language Models and Open Research Questions",
    "2403.10824v1.pdf": "LookALike: Human Mimicry based collaborative decision making",
    "2407.05202v1.pdf": "HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation",
    "2412.12513v1.pdf": "Smart Contract Code Translation based on Concepts",
    "2502.17604v1.pdf": "Weaving the Cosmos: WASM-Powered Interchain Communication for AI Enabled Smart Contracts",
    "3464298.3493401.pdf": "Lessons Learned from Blockchain Applications of Trusted Execution Environments and Implications",
    "3465480.3466924.pdf": "An event driven framework for smart contract execution",
    "3505253.3505259.pdf": "Privacy preserving event based transaction system in a decentralized environment",
    "3594556.3594626.pdf": "Decentralized Application Infrastructures as Smart Contract Codes",
    "3605098.3636029.pdf": "Supporting Heterogeneous TEE for Critical Infrastructure Protection",
    "3664646.3664771 (1).pdf": "Decentralized FaaS over Multi-Clouds",
    "3672608.3707883.pdf": "Smart Contract Code Translation based on Concepts",
    "3696843.3696844.pdf": "AI-Based Target for Personalized Interventions of Atherosclerosis from Gut Microbiota Signature",
    "6_evaluating_irrationality_in_la.pdf": "Evaluating Irrationality in Large Language Models and Open Research Questions",
    "8_Securing_the_Multi_Chain_Eco (1).pdf": "Securing the Multi-Chain Ecosystem: A Unified, Agent-Based Framework for Vulnerability Repair in Solidity and Move",
    "All_We_Need_is_Voter_Feedback_a_New_Paradigm_to_Realize_Politics_without_Politicians_Using_AI_Models_Aligned_with_Voter_Inputs.pdf": "All We Need is Voter Feedback",
    "Decentralized_Application_Infrastructures_as_Smart_Contract_Codes.pdf": "Decentralized Application Infrastructures as Smart Contract Codes",
    "Decentralized_Machine_Learning_Governance.pdf": "Decentralized Machine Learning Governance: Overview, Opportunities, and Research Challenges",
    "DeFaaS_Decentralized_Function-as-a-Service_for_Emerging_dApps_and_Web3.pdf": "DeFaaS: Decentralized Function-as-a-Service for Emerging dApps and Web",
    "DHTee_Decentralized_Infrastructure_for_Heterogeneous_TEEs.pdf": "DHTee: Decentralized Infrastructure for Heterogeneous TEE",
    "DIaC_Re-Imagining_Decentralized_Infrastructure_as_Code_Using_Blockchain.pdf": "DIaC: Re-imagining Decentralized Infrastructure As Code using Blockchain",
    "MSThesis.pdf": "Optimizing Web Virtual Reality",
    "On Conditional Cryptocurrency With Privacy.pdf": "On Conditional Cryptocurrency With Privacy",
    "random_number_generation_decentralized_env.pdf": "Adding All Flavors: A Hybrid Random Number Generator for dApps and Web3",
    "Ransomware_3.0_Enhancing_Risk_Management_and_Mitigation_Options_with_Proof-of-Decryptability_and_Smart_Contracts.pdf": "Ransomware 3.0: Enhancing Risk Management and Mitigation Options with Proof-of-Decryptability and Smart Contracts",
    "SolMover_Feasibility_of_Using_LLMs_for_Translating_Smart_Contracts.pdf": "Smart Contract Code Translation based on Concepts",
    "ssrn-4141949.pdf": "Decentralized Application Infrastructures as Smart Contract Codes",
    "ssrn-4141949-1.pdf": "Decentralized Application Infrastructures as Smart Contract Codes",
    "Submission 32.pdf": "Decentralized Machine Learning Governance: Overview, Opportunities, and Research Challenges",
    "Trusted_LLM_Inference_on_the_Edge_with_Smart_Contracts.pdf": "Trusted LLM Inference on the Edge with Smart Contracts",
    "Who_is_Smarter_An_Empirical_Study_of_AI-Based_Smart_Contract_Creation.pdf": "Who is Smarter? An Empirical Study of AI-based Smart Contract Creation"
}

# 4. Define arXiv URL fallbacks
arxiv_fallbacks = {
    "HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation": "https://arxiv.org/pdf/2511.10860.pdf",
    "QuCoWE: Quantum Contrastive Word Embeddings with Variational Circuits for Near-Term Quantum Devices": "https://arxiv.org/pdf/2511.10179.pdf",
    "Evaluating the Quality of Randomness and Entropy in Tasks Supported by Large Language Models": "https://arxiv.org/pdf/2510.12080.pdf",
    "Weaving the Cosmos: WASM-Powered Interchain Communication for AI Enabled Smart Contracts": "https://arxiv.org/pdf/2502.17604.pdf",
    "Securing the Multi-Chain Ecosystem: A Unified, Agent-Based Framework for Vulnerability Repair in Solidity and Move": "https://arxiv.org/pdf/2502.18515.pdf",
    "Smart Contract Code Translation based on Concepts": "https://arxiv.org/pdf/2412.12513.pdf",
    "Generating Move Smart Contracts based on Concepts": "https://arxiv.org/pdf/2412.12513.pdf",
    "Harnessing the power of llms: Automating unit test generation for high-performance computing": "https://arxiv.org/pdf/2407.05202.pdf",
    "Comparing rationality between large language models and humans: Insights and open questions": "https://arxiv.org/pdf/2403.09798.pdf",
    "Evaluating Irrationality in Large Language Models and Open Research Questions": "https://arxiv.org/pdf/2403.09798.pdf"
}

# Prepare destination directories
pdf_dest_dir = "static/uploads/publications"
os.makedirs(pdf_dest_dir, exist_ok=True)

pub_base_dir = "content/publication"
# Remove existing publications to clean up
if os.path.exists(pub_base_dir):
    shutil.rmtree(pub_base_dir)
os.makedirs(pub_base_dir, exist_ok=True)

# Generate publication _index.md
with open(os.path.join(pub_base_dir, "_index.md"), "w") as f:
    f.write("""---
title: Publications
type: landing
sections:
  - block: publication-browser
---
""")

# Match and generate publications
print("Generating publications...")
for pub in publications:
    title = pub["title"]
    folder_name = pub["filename"]
    pub_dir = os.path.join(pub_base_dir, folder_name)
    os.makedirs(pub_dir, exist_ok=True)

    # Match local PDF
    matched_pdf = None
    pdf_filename = None
    
    # Try hardcoded matching first
    for fn, t in pdf_mappings.items():
        if t.lower() == title.lower():
            pdf_filename = fn
            break
            
    # Fuzzy match fallback
    if not pdf_filename:
        for fn in os.listdir("Publications"):
            if not fn.endswith(".pdf"):
                continue
            ratio = difflib.SequenceMatcher(None, fn.lower().replace(".pdf", ""), title.lower()).ratio()
            if ratio > 0.7:
                pdf_filename = fn
                break
                
    if pdf_filename:
        src_path = os.path.join("Publications", pdf_filename)
        dest_filename = f"{folder_name}.pdf"
        dest_path = os.path.join(pdf_dest_dir, dest_filename)
        shutil.copy(src_path, dest_path)
        matched_pdf = f"/uploads/publications/{dest_filename}"
        print(f"  Matched PDF: {pdf_filename} -> {matched_pdf}")
    else:
        # Check arXiv fallback
        matched_pdf = arxiv_fallbacks.get(title, "")
        if matched_pdf:
            print(f"  Matched arXiv fallback: {matched_pdf}")

    # Generate markdown index.md
    authors_yaml = "\n".join([f"- {a}" for a in pub["authors"]])
    tags_yaml = "\n".join([f"- {t}" for t in pub["tags"]])
    featured_str = "true" if pub.get("featured", False) else "false"
    
    front_matter = f"""---
title: "{title}"
authors:
{authors_yaml}
date: "{pub['date']}T00:00:00Z"
doi: ""
publishDate: "{pub['date']}T00:00:00Z"
publication_types: ["{pub['type']}"]
publication: "{pub['publication']}"
publication_short: "{pub['publication']}"
abstract: "{pub['abstract']}"
tags:
{tags_yaml}
featured: {featured_str}
links:
url_pdf: '{matched_pdf}'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---
"""
    with open(os.path.join(pub_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(front_matter)

# Generate Talks under content/events/
print("Generating talks...")
events_dir = "content/events"
if os.path.exists(events_dir):
    shutil.rmtree(events_dir)
os.makedirs(events_dir, exist_ok=True)

# Generate event _index.md
with open(os.path.join(events_dir, "_index.md"), "w") as f:
    f.write("""---
title: Talks & Presentations
type: landing
---
""")

for talk in talks:
    # Slugify title
    slug = talk["title"].lower().replace(":", "").replace(",", "").replace("&", "and").replace(" ", "-").replace("?", "")
    slug = "".join([c for c in slug if c.isalnum() or c == "-"])
    
    # Event folder
    talk_dir = os.path.join(events_dir, slug)
    os.makedirs(talk_dir, exist_ok=True)
    
    date_start = talk["date"]
    
    content = f"""---
title: "{talk['title']}"
event: "{talk['event']}"
event_url: ""
location: "{talk['location']}"
summary: "Talk at {talk['event']} ({talk['year']})."
abstract: "Presented '{talk['title']}' at {talk['event']} in {talk['location']}."
date: "{date_start}T10:00:00Z"
date_end: "{date_start}T11:00:00Z"
all_day: false
publishDate: "2025-01-01T00:00:00Z"
authors: [admin]
tags: [{talk['event'].split()[0]}, "Talk", "{talk['year']}"]
featured: false
links: []
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
---
"""
    with open(os.path.join(talk_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)

# Update Biography in content/authors/admin/_index.md
print("Updating Biography...")
bio_path = "content/authors/admin/_index.md"
with open(bio_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_bio_content = """---
# Display name
title: Rabimba Karanjai

# Full name (for SEO)
first_name: Rabimba
last_name: Karanjai

# Pronouns
pronouns: he/him

# Status emoji
status:
  icon: 💻

superuser: true
highlight_name: true

# Role/position/tagline
role: Staff Agentic AI Researcher

# Organizations/Affiliations
organizations:
  - name: PayPal Research
    url: https://www.paypal.com/
  - name: University of Houston
    url: https://www.uh.edu/
  - name: Google
    url: https://developers.google.com/community/experts

# Social network links
profiles:
  - icon: at-symbol
    url: 'mailto:rkaranjai@uh.edu'
    label: E-mail Me
  - icon: brands/github
    url: https://github.com/rabimba
  - icon: brands/linkedin
    url: https://www.linkedin.com/in/rabimba/
  - icon: academicons/google-scholar
    url: https://scholar.google.com/citations?user=rabimba

interests:
  - Agentic AI & AI Reasoning
  - LLMs Security & Smart Contracts
  - Decentralized Systems & Blockchain
  - Formal Verification & Software Engineering
  - Web VR & High Performance Computing

education:
  - area: Ph.D. in Computer Science
    institution: University of Houston
    icon: ""
    date_start: 2020-01-01
    date_end: 2025-07-25
    summary: |
      Dissertation: "Teaching AI's to reason and Code, Confidentially" — Best Dissertation Award / Dan E. Wells Outstanding Dissertation Award.
      Advisor: Prof. Weidong (Larry) Shi
  - area: M.S. in Computer Science
    institution: Rice University
    icon: ""
    date_start: 2015-01-01
    date_end: 2018-08-31
    summary: |
      Specialized in High Performance Computing & Web VR.

work:
  - position: Staff Agentic AI Researcher
    company_name: PayPal Research
    company_url: 'https://www.paypal.com/'
    icon: ''
    date_start: 2025-09-01
    date_end: ''
    summary: |
      Lead design and deployment of production-scale voice commerce systems enabling real-time, multi-turn conversational AI for financial applications. Developed a novel preference optimization framework (CM-DPO).
  - position: Research Assistant
    company_name: University of Houston
    company_url: 'https://www.uh.edu/'
    icon: ''
    date_start: 2021-09-01
    date_end: 2025-07-25
    summary: |
      Conducted research in AI reasoning, smart contract translation, code generation, medical diagnosis, and decentralized infrastructures (DlaC, FaaS).
  - position: Senior Software Engineer
    company_name: Clearedin
    company_url: ''
    icon: ''
    date_start: 2020-12-01
    date_end: 2021-08-31
    summary: |
      Designed and implemented advanced policy threat detection engines, URL scanning, phishing detection algorithms, and maliciousemail classification.
  - position: Machine Learning Lead
    company_name: Fireflies.ai
    company_url: 'https://fireflies.ai/'
    icon: ''
    date_start: 2020-08-01
    date_end: 2020-12-31
    summary: |
      Developed and deployed an on-premise Automatic Speech Recognition (ASR) engine based on Deep Speech. Built the first ML team.
  - position: Research Associate
    company_name: Mozilla Research
    company_url: 'https://www.mozilla.org/'
    icon: ''
    date_start: 2017-09-01
    date_end: 2018-01-31
    summary: |
      Conducted in-depth research to optimize parallelism and performance of Virtual Reality in WebGL/Three.js.
  - position: Summer Research Intern
    company_name: IBM Almaden Research Center
    company_url: ''
    icon: ''
    date_start: 2017-05-01
    date_end: 2017-08-31
    summary: |
      Developed patented multi-factor authentication system (US11025643B2) integrating biometrics and blockchain.
  - position: Summer Research Intern
    company_name: IBM Almaden Research Center
    company_url: ''
    icon: ''
    date_start: 2015-05-01
    date_end: 2015-08-31
    summary: |
      Developed a tamper-evident mobile application solution verifying application integrity using ARM TrustZone and blockchain.
  - position: Researcher
    company_name: IBM T J Watson Research Lab
    company_url: ''
    icon: ''
    date_start: 2014-05-01
    date_end: 2014-11-31
    summary: |
      Embedded NLP and cognitive computing into Watson solutions.
  - position: Programmer Analyst
    company_name: Cognizant Technology Solutions
    company_url: ''
    icon: ''
    date_start: 2010-12-01
    date_end: 2013-08-31
    summary: |
      Created automated mobile hardware and software testing solutions leveraging OpenCV.

skills:
  - name: Technical Skills
    items:
      - name: Large Language Models (LLMs) & Reasoning
        percent: 98
        icon: cpu-chip
      - name: Blockchain & Smart Contracts
        percent: 95
        icon: code-bracket
      - name: Distributed & Decentralized Systems
        percent: 95
        icon: chart-bar
      - name: Systems & Security Programming
        percent: 90
        icon: cpu-chip
      - name: WebVR & WebGL Graphics
        percent: 85
        icon: code-bracket

languages:
  - name: English
    percent: 100
  - name: Bengali
    percent: 100
  - name: Hindi
    percent: 85

awards:
  - title: ACM SIGSOFT Distinguished Paper Award
    date: '2025-11-01'
    awarder: ACM
    summary: "For 'Securing the Multi-Chain Ecosystem: A Unified, Agent-Based Framework for Vulnerability Repair in Solidity and Move'."
  - title: Dan E. Wells Outstanding Dissertation Award
    date: '2025-10-01'
    awarder: University of Houston
    summary: "Awarded to the top PhD dissertation in the College of Natural Sciences and Mathematics."
  - title: Outstanding PhD Student
    date: '2024-05-01'
    awarder: University of Houston
    summary: "Recognized as Outstanding PhD Student for 2022-2023 and 2023-2024."
  - title: Google Cloud Research Innovator
    date: '2023-01-01'
    awarder: Google
  - title: Sui Academic Research Award
    date: '2025-01-01'
    awarder: Sui Foundation
    summary: "Awarded Sui Foundation Research Grants in 2023 ($15k), 2024 ($25k), and 2025 ($25k)."
  - title: Mozilla Research Fellowship
    date: '2018-01-01'
    awarder: Mozilla
---

Rabimba Karanjai is a Staff Agentic AI Researcher at PayPal Research. He completed his Ph.D. in Computer Science at the University of Houston (defended July 2025), where his research focused on the intersection of blockchain, secure AI reasoning, and LLM-assisted program analysis and repair. 
"""

with open(bio_path, "w", encoding="utf-8") as f:
    f.write(new_bio_content)

print("CV sync complete!")
