import os
import glob

base_path = "content/publication"

def update_publication(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    is_yaml = False
    authors = []
    tags = []
    title = ""
    featured = False
    
    new_lines = []
    in_authors = False
    in_tags = False
    
    # Simple parsing
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---":
            is_yaml = not is_yaml
        
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"')
        
        if line.startswith("authors:"):
            in_authors = True
            continue
        if in_authors:
            if line.strip().startswith("-"):
                authors.append(line.strip("- \n"))
            elif not line.startswith(" ") and line.strip() != "":
                in_authors = False
        
        if line.startswith("tags:"):
            in_tags = True
            continue
        if in_tags:
            if line.strip().startswith("-"):
                tags.append(line.strip("- \n"))
            elif not line.startswith(" ") and line.strip() != "":
                in_tags = False
                
        if line.startswith("featured:"):
            if "true" in line.lower():
                featured = True

    # Check first author
    is_first_author = False
    if authors and "Rabimba Karanjai" in authors[0]:
        is_first_author = True
    
    # Determine if needs update
    needs_update = False
    
    # Read content again to modify
    content_str = "".join(lines)
    
    # Add First Author tag
    if is_first_author and "First Author" not in content_str:
        if "tags:" not in content_str:
            # Add tags section if missing (unlikely based on my creation script)
            content_str = content_str.replace("featured:", "tags:\n- First Author\nfeatured:")
        else:
            # Add to existing tags
            content_str = content_str.replace("tags:", "tags:\n- First Author")
        needs_update = True
        
    # Ensure distinguished are featured
    distinguished_keywords = ["Securing Multi-Chain", "Decentralized Application Infrastructures"]
    for key in distinguished_keywords:
        if key in title and not featured:
            content_str = content_str.replace("featured: false", "featured: true")
            needs_update = True

    if needs_update:
        with open(file_path, "w") as f:
            f.write(content_str)
        print(f"Updated {file_path}")

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == "index.md":
            update_publication(os.path.join(root, file))

