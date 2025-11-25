import os
import difflib

base_path = "content/publication"

# Map of titles to PDF URLs (from Google Scholar/arXiv)
pdf_map = {
    "HPCAgentTester: Multi-Agent Approach for Enhancing Unit Test Generation": "https://arxiv.org/pdf/2511.10860.pdf",
    "HPCAgentTester: A Multi-Agent LLM Approach for Enhanced HPC Unit Test Generation": "https://arxiv.org/pdf/2511.10860.pdf",
    "QuCoWE: Quantum Contrastive Embeddings with Variational Circuits for Near-Term Quantum Devices": "https://arxiv.org/pdf/2511.10179.pdf",
    "Evaluating Quality of Randomness and Entropy in Tasks Supported by Large Language Models": "https://arxiv.org/pdf/2510.12080.pdf",
    "Evaluating the Quality of Randomness and Entropy in Tasks Supported by Large Language Models": "https://arxiv.org/pdf/2510.12080.pdf",
    "Weaving the Cosmos: WASM-Powered Interchain Communication for AI Enabled Smart Contracts": "https://arxiv.org/pdf/2502.17604.pdf",
    "Securing Multi-Chain Ecosystem: Unified Agent-Based Framework for Vulnerability Detection in Solidity and Move": "https://arxiv.org/pdf/2502.18515.pdf",
    "A Multi-Agent Framework for Automated Vulnerability Detection and Repair in Solidity and Move Smart Contracts": "https://arxiv.org/pdf/2502.18515.pdf",
    "Generating Move Smart Contracts based on Concepts": "https://arxiv.org/pdf/2412.12513.pdf",
    "Smart Contract Translation Concepts": "https://arxiv.org/pdf/2412.12513.pdf", 
    "Harnessing the power of llms: Automating unit test generation for high-performance computing": "https://arxiv.org/pdf/2407.05202.pdf",
    "LookALike: Human Mimicry based collaborative decision making": "https://arxiv.org/pdf/2403.10824.pdf",
    "Comparing rationality between large language models and humans: Insights and open questions": "https://arxiv.org/pdf/2403.09798.pdf",
    "Evaluating rationality": "https://arxiv.org/pdf/2403.09798.pdf"
}

# Missing papers to create found on Scholar
new_papers = [
    {
        "title": "Weaving the Cosmos: WASM-Powered Interchain Communication for AI Enabled Smart Contracts",
        "date": "2025-02-01",
        "authors": ["Rabimba Karanjai", "Lei Xu", "Weidong Shi"],
        "publication": "arXiv 2025",
        "tags": ["Blockchain", "AI", "WASM", "Interchain", "First Author"],
        "url_pdf": "https://arxiv.org/pdf/2502.17604.pdf",
        "filename": "weaving-the-cosmos"
    },
    {
        "title": "Generating Move Smart Contracts based on Concepts",
        "date": "2024-12-01",
        "authors": ["Rabimba Karanjai", "Blackshear", "Lei Xu", "Weidong Shi"],
        "publication": "arXiv 2024",
        "tags": ["Blockchain", "Smart Contracts", "Move", "Generative AI", "First Author"],
        "url_pdf": "https://arxiv.org/pdf/2412.12513.pdf",
        "filename": "generating-move-smart-contracts"
    },
     {
        "title": "Harnessing the power of llms: Automating unit test generation for high-performance computing",
        "date": "2024-07-01",
        "authors": ["Rabimba Karanjai", "A Hussain", "MRI Rabin", "L Xu", "W Shi", "MA Alipour"],
        "publication": "arXiv 2024",
        "tags": ["LLM", "HPC", "Testing", "First Author"],
        "url_pdf": "https://arxiv.org/pdf/2407.05202.pdf",
        "filename": "harnessing-power-llms"
    }
]

# Update existing
count = 0
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == "index.md":
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()
            
            # Parse title
            title = ""
            for line in content.splitlines():
                if line.strip().startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"')
                    break
            
            # Find matching PDF
            best_match = None
            highest_ratio = 0
            for key in pdf_map:
                ratio = difflib.SequenceMatcher(None, title.lower(), key.lower()).ratio()
                if ratio > 0.8 and ratio > highest_ratio:
                    highest_ratio = ratio
                    best_match = key
            
            if best_match:
                pdf_url = pdf_map[best_match]
                # Update content
                if "url_pdf: ''" in content:
                     new_content = content.replace("url_pdf: ''", f"url_pdf: '{pdf_url}'")
                     with open(path, "w") as f:
                         f.write(new_content)
                     print(f"Updated PDF for {title}")
                     count += 1
                elif "url_pdf: \"\"" in content:
                     new_content = content.replace("url_pdf: \"\"", f"url_pdf: '{pdf_url}'")
                     with open(path, "w") as f:
                         f.write(new_content)
                     print(f"Updated PDF for {title}")
                     count += 1

# Create new
for paper in new_papers:
    folder = os.path.join(base_path, paper["filename"])
    if not os.path.exists(folder):
        os.makedirs(folder)
        content = f"""---
title: "{paper['title']}"
authors:
{chr(10).join(["- " + a for a in paper['authors']])}
date: "{paper['date']}T00:00:00Z"
publishDate: "{paper['date']}T00:00:00Z"
publication_types: ["3"]
publication: "{paper['publication']}"
publication_short: "{paper['publication']}"
abstract: "arXiv Preprint."
tags:
{chr(10).join(["- " + t for t in paper['tags']])}
featured: false
links:
url_pdf: '{paper['url_pdf']}'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
---
"""
        with open(os.path.join(folder, "index.md"), "w") as f:
            f.write(content)
        print(f"Created {paper['filename']}")

