import os
import shutil

# Paths to the newly generated visual artifacts
images_map = {
    "LLMs": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\llm_reasoning_featured_1781254966675.png",
    "AI": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\llm_reasoning_featured_1781254966675.png",
    "Blockchain": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\blockchain_featured_1781254982824.png",
    "Virtual Reality": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\web_vr_featured_1781254999092.png",
    "Web Technologies": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\web_vr_featured_1781254999092.png",
    "Quantum Computing": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\quantum_featured_1781255012510.png",
    "Security": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\security_featured_1781255027392.png",
    "Edge Computing": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\edge_iot_featured_1781255044952.png",
    "HPC": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\hpc_featured_1781255063484.png",
    "General": r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\research_featured_1781255077336.png"
}

current_cv_pdf = r"C:\Users\rabim\.gemini\antigravity\brain\d444a3a7-3d7c-447e-b455-ea985bf5293a\media__1781235668080.pdf"

# 1. Overwrite CV on site
print("Overwriting CV with the current uploaded one...")
shutil.copy(current_cv_pdf, "CV_Rabimba_Academic.pdf")
shutil.copy(current_cv_pdf, "static/uploads/resume.pdf")

# Helper to identify key topic from keywords in text
def identify_topic(text, tags=[]):
    text_lower = text.lower()
    
    # Check tags first
    for tag in tags:
        tag_lower = tag.lower()
        if "security" in tag_lower or "poison" in tag_lower:
            return "Security"
        if "llm" in tag_lower or "reasoning" in tag_lower or "agent" in tag_lower:
            return "LLMs"
        if "blockchain" in tag_lower or "contract" in tag_lower or "web3" in tag_lower:
            return "Blockchain"
        if "quantum" in tag_lower:
            return "Quantum Computing"
        if "vr" in tag_lower or "virtual" in tag_lower or "webgl" in tag_lower:
            return "Virtual Reality"
        if "edge" in tag_lower or "iot" in tag_lower or "sensor" in tag_lower:
            return "Edge Computing"
        if "hpc" in tag_lower or "parallel" in tag_lower:
            return "HPC"
        if "ai" in tag_lower or "learning" in tag_lower:
            return "AI"

    # Check text/title content
    if "quantum" in text_lower:
        return "Quantum Computing"
    if "blockchain" in text_lower or "smart contract" in text_lower or "solidity" in text_lower or "move" in text_lower or "cryptocurrency" in text_lower or "dapp" in text_lower:
        return "Blockchain"
    if "security" in text_lower or "poison" in text_lower or "vulnerability" in text_lower or "attack" in text_lower or "privacy" in text_lower or "trust" in text_lower or "verification" in text_lower:
        return "Security"
    if "llm" in text_lower or "language model" in text_lower or "reasoning" in text_lower or "agent" in text_lower or "deliberation" in text_lower:
        return "LLMs"
    if "virtual reality" in text_lower or "vr" in text_lower or "webgl" in text_lower or "three.js" in text_lower:
        return "Virtual Reality"
    if "edge" in text_lower or "iot" in text_lower or "sensor" in text_lower or "faas" in text_lower:
        return "Edge Computing"
    if "hpc" in text_lower or "parallel" in text_lower or "tpu" in text_lower:
        return "HPC"
    if "ai" in text_lower or "machine learning" in text_lower or "neural network" in text_lower or "diagnosis" in text_lower:
        return "AI"
        
    return "General"

# 2. Assign images to Projects
print("Assigning images to Projects...")
project_base = "content/projects"
projects_mapping = {
    "blockchain-security": "Blockchain",
    "edge-computing": "Edge Computing",
    "llm-reasoning": "LLMs",
    "quantum-computing": "Quantum Computing",
    "web-vr": "Virtual Reality"
}
for folder, topic in projects_mapping.items():
    dest_folder = os.path.join(project_base, folder)
    if os.path.exists(dest_folder):
        src_img = images_map[topic]
        shutil.copy(src_img, os.path.join(dest_folder, "featured.png"))
        print(f"  Project {folder} -> {topic}")

# 3. Assign images to Publications
print("Assigning images to Publications...")
pub_base = "content/publication"
for folder in os.listdir(pub_base):
    folder_path = os.path.join(pub_base, folder)
    if not os.path.isdir(folder_path):
        continue
    index_md = os.path.join(folder_path, "index.md")
    if not os.path.exists(index_md):
        continue
        
    # Read tags and title from front matter
    with open(index_md, "r", encoding="utf-8") as f:
        content = f.read()
    
    title = ""
    tags = []
    for line in content.splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"')
        if line.strip().startswith("-"):
            tags.append(line.strip("- \n"))
            
    topic = identify_topic(title + " " + folder, tags)
    src_img = images_map[topic]
    shutil.copy(src_img, os.path.join(folder_path, "featured.png"))

# 4. Assign images to Talks (Events)
print("Assigning images to Talks...")
events_base = "content/events"
for folder in os.listdir(events_base):
    folder_path = os.path.join(events_base, folder)
    if not os.path.isdir(folder_path):
        continue
    index_md = os.path.join(folder_path, "index.md")
    if not os.path.exists(index_md):
        continue
        
    with open(index_md, "r", encoding="utf-8") as f:
        content = f.read()
    
    title = ""
    for line in content.splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"')
            break
            
    topic = identify_topic(title + " " + folder)
    src_img = images_map[topic]
    shutil.copy(src_img, os.path.join(folder_path, "featured.png"))

print("All visuals and CV successfully synced!")
