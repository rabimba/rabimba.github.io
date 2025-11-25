import os

base_path = "content/publication"

keywords = {
    "Blockchain": ["blockchain", "chain", "smart contract", "solidity", "move", "defi", "crypto", "ethereum", "ledger", "hyperledger"],
    "AI": ["ai", "artificial intelligence", "learning", "neural", "model", "vision"],
    "LLM": ["llm", "large language model", "generative", "genai", "gpt", "prompt", "hallucination"],
    "Security": ["security", "secure", "vulnerability", "attack", "defense", "privacy", "confidentiality", "trusted", "tee", "sgx", "malware", "ransomware", "red teaming"],
    "Quantum": ["quantum"],
    "Agents": ["agent", "multi-agent"],
    "IoT": ["iot", "internet of things", "edge", "sensor", "mobile"],
    "Distributed Systems": ["distributed", "cloud", "serverless", "consensus", "paxos", "raft", "infrastructure"],
    "Software Engineering": ["software", "testing", "debug", "code", "program", "verification"],
    "HPC": ["hpc", "high performance"]
}

def refine_tags(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    
    if "---" not in content:
        return

    parts = content.split("---")
    if len(parts) < 3:
        return
    
    frontmatter = parts[1]
    body = parts[2]
    
    # Extract title and abstract for keyword search
    title = ""
    abstract = ""
    
    lines = frontmatter.split("\n")
    new_lines = []
    
    existing_tags = []
    in_tags = False
    tags_indent = ""
    
    # Pass 1: Extract info
    for line in lines:
        stripped = line.strip()
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').lower()
        if line.startswith("abstract:"):
            if len(line.split(":")) > 1:
                abstract = line.split(":", 1)[1].strip().strip('"').lower()
        
        if line.strip().startswith("tags:"):
            in_tags = True
            continue
        if in_tags:
            if line.strip().startswith("-"):
                existing_tags.append(line.split("-", 1)[1].strip())
            elif ":" in line: # Next field
                in_tags = False
            elif line.strip() == "":
                pass
            else:
                pass

    # Determine new tags
    new_tags = set(existing_tags)
    text_to_search = title + " " + abstract
    
    for tag, keys in keywords.items():
        for key in keys:
            if key in text_to_search:
                new_tags.add(tag)
                break
    
    if "Research" in new_tags:
        new_tags.remove("Research")
        
    # Reconstruct frontmatter
    in_tags = False
    final_lines = []
    tags_written = False
    
    for line in lines:
        if line.strip().startswith("tags:"):
            in_tags = True
            final_lines.append("tags:")
            for tag in sorted(list(new_tags)):
                final_lines.append(f"- {tag}")
            tags_written = True
            continue
            
        if in_tags:
            if line.strip().startswith("-"):
                continue
            elif ":" in line:
                in_tags = False
                final_lines.append(line)
            elif line.strip() == "":
                final_lines.append(line)
            else:
                # Continuation of tags? or malformed
                pass
        else:
            final_lines.append(line)
            
    if not tags_written:
        # If tags section was missing, add it before the last line or featured
        # This is a simple append if missing, but create_pubs ensures tags exist.
        # If missing, we skip adding for safety or append to end.
        pass
        
    new_frontmatter = "\n".join(final_lines)
    new_content = f"---{new_frontmatter}---{body}"
    
    if new_content != content:
        with open(file_path, "w") as f:
            f.write(new_content)
        print(f"Refined tags for {file_path}")

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == "index.md":
            refine_tags(os.path.join(root, file))

