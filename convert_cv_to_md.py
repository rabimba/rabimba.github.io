import re

def is_header(line):
    headers = ["EDUCATION", "EXPERIENCE", "RESEARCH INTERESTS", "PUBLICATIONS", "AWARDS", "SKILLS", "PROJECTS", "TALKS", "GRANTS", "SERVICE", "REFERENCES", "PATENTS"]
    return any(h in line.upper() for h in headers) and len(line) < 30

def clean_cv_text(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []
    current_line = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip garbage/font names
        if "Computer Modern" in line or "http://www.ams.org" in line or "CIDInit" in line or "TeX-" in line or line.startswith("/"):
            continue
            
        if is_header(line):
            if current_line:
                cleaned_lines.append(current_line)
            cleaned_lines.append(f"\n## {line}\n")
            current_line = ""
        elif line.startswith("•") or line.startswith("\\210"): # Bullet points
            if current_line:
                cleaned_lines.append(current_line)
            current_line = "- " + line.replace("\\210", "").strip()
        else:
            # Heuristic to join lines: if previous line ends with letter and this starts with letter, join with space
            if current_line and not current_line.endswith(".") and not current_line.endswith(":"):
                 current_line += " " + line
            else:
                if current_line:
                    cleaned_lines.append(current_line)
                current_line = line
                
    if current_line:
        cleaned_lines.append(current_line)

    with open(output_file, 'w') as f:
        f.write("\n".join(cleaned_lines))

try:
    clean_cv_text('cv_extracted_python.txt', 'CV.md')
    print("CV.md created.")
except Exception as e:
    print(e)

