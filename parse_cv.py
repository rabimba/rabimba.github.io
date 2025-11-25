import re

def parse_cv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    cleaned_lines = []
    buffer = ""
    
    for line in lines:
        line = line.strip()
        
        # Skip garbage/metadata
        if not line or line.startswith("/") or line.startswith("CIDInit") or "TeX-" in line or "<http" in line or line.startswith("Item."):
            continue
            
        # Handle special chars
        line = line.replace('\\050', '(').replace('\\051', ')').replace('\\014', 'fi').replace('\\013', 'ff').replace('\\210', '-').replace('\\134', '"').replace('\\016', 'fi').replace('\\017', 'fl')

        if not buffer:
            buffer = line
        else:
            # Join heuristic
            # If current line starts with lowercase, likely continuation of word
            if line[0].islower() and buffer[-1].isalpha():
                buffer += line
            # If buffer ends with hyphen, join without space
            elif buffer.endswith("-"):
                buffer += line
            # Otherwise join with space
            else:
                buffer += " " + line
                
    # Split buffer back into paragraphs/sections based on keywords
    # This is a bit rough because we lost line breaks.
    # But we can look for known headers.
    
    content = buffer
    
    # Headers to look for
    headers = [
        "EDUCATION", "RESEARCH INTERESTS", "EXPERIENCE", "RESEARCH EXPERIENCE", 
        "TEACHING EXPERIENCE", "PUBLICATIONS", "ACADEMIC HONORS", "AWARDS",
        "PROFESSIONAL ACTIVITIES", "SERVICE", "SKILLS", "LANGUAGES", "REFERENCES", "PATENTS", "TALKS"
    ]
    
    markdown_content = "# Rabimba Karanjai\n\n"
    
    # Create a regex pattern to find headers
    # We look for the header words, potentially with some noise around them
    
    for header in headers:
        # Replace Header with \n## Header\n
        # Use regex to be case insensitive or handle spacing
        # "E D U C A T I O N" or "EDUCATION"
        # The join logic might have made it "EDUCATION" or "E DU C A T ION"
        
        # Simple approach: just replace the exact string if found
        if header in content:
            content = content.replace(header, f"\n\n## {header}\n\n")
        # Also try variations like "R E S E A R C H" -> "RESEARCH" might have been fixed by join? 
        # Actually, if the PDF had wide spacing, "R E S E A R C H" -> "R E S E A R C H".
        # But the input `cv_extracted.txt` seems to have chunks.
        
    markdown_content += content
    
    # Further cleanup
    markdown_content = markdown_content.replace("Univ ersit", "University")
    markdown_content = markdown_content.replace("Universit", "University")
    markdown_content = markdown_content.replace("Technol ogy", "Technology")
    markdown_content = markdown_content.replace("Comp uter", "Computer")
    
    with open(output_file, 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    parse_cv("cv_extracted_python.txt", "CV_Rabimba_Academic.md")
