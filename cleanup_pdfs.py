import os
import glob

# Map of titles to PDF URLs (restoring external links)
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
    "Evaluating rationality": "https://arxiv.org/pdf/2403.09798.pdf",
    # Recovered links for older papers
    "DIaC: Re-imagining Decentralized Infrastructure using Blockchain": "https://arxiv.org/pdf/2301.00665.pdf",
    "FaaS: Decentralized Function-as-a-Service for Emerging dApps": "https://arxiv.org/pdf/2203.12724.pdf",
    "Decentralized Machine Learning Governance: Overview, Opportunities, and Challenges": "https://arxiv.org/pdf/2308.02955.pdf",
    "Conditional Crypto-currency With Privacy": "https://ieeexplore.ieee.org/document/9464298",
    "Decentralized Application Infrastructures as Smart Contract Codes": "https://ieeexplore.ieee.org/document/9789334",
    "Event Driven Framework Smart Contract Execution": "https://dl.acm.org/doi/10.1145/3465480.3466924",
    "Privacy Preserving Event Transaction System in Decentralized Environment": "https://dl.acm.org/doi/10.1145/3464298.3493401"
}

def cleanup_and_restore():
    pub_dir = 'content/publication'
    
    # 1. Delete all paper.pdf files
    for root, dirs, files in os.walk(pub_dir):
        for file in files:
            if file == 'paper.pdf':
                path = os.path.join(root, file)
                try:
                    os.remove(path)
                    print(f"Deleted {path}")
                except Exception as e:
                    print(f"Error deleting {path}: {e}")

    # 2. Restore links in index.md
    for root, dirs, files in os.walk(pub_dir):
        for file in files:
            if file == 'index.md':
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                if "url_pdf: 'paper.pdf'" in content:
                    # Find title
                    title = ""
                    for line in content.splitlines():
                        if line.startswith("title:"):
                            title = line.split(':', 1)[1].strip().strip('"')
                            break
                    
                    # Lookup URL
                    url = pdf_map.get(title, "")
                    if not url:
                        # Try partial match
                        for k, v in pdf_map.items():
                            if k in title or title in k:
                                url = v
                                break
                    
                    # Replace
                    new_content = content.replace("url_pdf: 'paper.pdf'", f"url_pdf: '{url}'")
                    
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"Restored link for {title} -> {url}")

if __name__ == "__main__":
    cleanup_and_restore()

