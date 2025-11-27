import os
import re
import shutil
import glob
from difflib import SequenceMatcher
import pypdf

# Paths
PUB_CONTENT_DIR = 'content/publication'
PDF_SOURCE_DIR = 'Publications'

def extract_text_from_pdf(pdf_path, max_pages=2):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for i in range(min(len(reader.pages), max_pages)):
            page_text = reader.pages[i].extract_text()
            if page_text:
                text += page_text + "\n\n"
        return text
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return ""

def clean_text(text):
    # Basic cleaning: remove multiple newlines, fix hyphenation
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # Try to remove page numbers or headers (naive)
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if len(line.strip()) > 4] # Remove very short lines
    return '\n'.join(cleaned_lines)

def find_pdf_match(title, arxiv_id, pdf_files):
    # 1. Try ArXiv ID
    if arxiv_id:
        for pdf in pdf_files:
            if arxiv_id in pdf:
                return pdf
    
    # 2. Try exact title match (normalized)
    norm_title = re.sub(r'[^\w\s]', '', title.lower())
    
    best_match = None
    best_ratio = 0.0
    
    for pdf in pdf_files:
        pdf_name = os.path.basename(pdf).lower()
        # Remove extension and common prefixes
        pdf_name_clean = re.sub(r'\.pdf$', '', pdf_name)
        pdf_name_clean = re.sub(r'^\d+_', '', pdf_name_clean) # Remove leading numbers like 8_Securing...
        
        # Calculate similarity
        ratio = SequenceMatcher(None, norm_title, pdf_name_clean).ratio()
        
        # Check for containment (if pdf filename is a substring of title or vice versa)
        if pdf_name_clean in norm_title or norm_title in pdf_name_clean:
             if len(pdf_name_clean) > 10: # Avoid matching short generic names
                 if ratio < 0.5: ratio = 0.8 # Boost if contained
        
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = pdf
            
    if best_ratio > 0.6: # Threshold
        return best_match
    return None

def process_publications():
    pdf_files = glob.glob(os.path.join(PDF_SOURCE_DIR, '*.pdf'))
    print(f"Found {len(pdf_files)} source PDFs")
    
    for root, dirs, files in os.walk(PUB_CONTENT_DIR):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            index_path = os.path.join(dir_path, 'index.md')
            
            if not os.path.exists(index_path):
                continue
                
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Extract Frontmatter
            frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
            if not frontmatter_match:
                continue
                
            frontmatter = frontmatter_match.group(1)
            body = frontmatter_match.group(2)
            
            # Extract Title and URL
            title_match = re.search(r'title: "(.*?)"', frontmatter)
            title = title_match.group(1) if title_match else ""
            
            url_pdf_match = re.search(r'url_pdf: \'(.*?)\'', frontmatter)
            url_pdf = url_pdf_match.group(1) if url_pdf_match else ""
            
            arxiv_id = ""
            if 'arxiv.org' in url_pdf:
                # Extract ID like 2511.10179
                arxiv_match = re.search(r'(\d{4}\.\d{4,5})', url_pdf)
                if arxiv_match:
                    arxiv_id = arxiv_match.group(1)
            
            print(f"Processing: {title}")
            
            # Find PDF
            matched_pdf = find_pdf_match(title, arxiv_id, pdf_files)
            
            if matched_pdf:
                print(f"  Matched PDF: {matched_pdf}")
                
                # Copy PDF
                dest_pdf_name = 'paper.pdf'
                dest_pdf_path = os.path.join(dir_path, dest_pdf_name)
                shutil.copy(matched_pdf, dest_pdf_path)
                
                # Extract Text
                extracted_text = extract_text_from_pdf(matched_pdf)
                cleaned_text = clean_text(extracted_text)
                
                # Update Frontmatter
                if "url_pdf: 'paper.pdf'" not in frontmatter:
                    # Replace or Add url_pdf
                    if re.search(r'url_pdf: .*', frontmatter):
                        new_frontmatter = re.sub(r'url_pdf: .*', "url_pdf: 'paper.pdf'", frontmatter)
                    else:
                        new_frontmatter = frontmatter + "\nurl_pdf: 'paper.pdf'"
                else:
                    new_frontmatter = frontmatter

                # Format Writeup
                writeup = f"\n\n## Paper Summary\n\n{cleaned_text[:4000]}..." if cleaned_text else ""
                if len(cleaned_text) > 0:
                     writeup += "\n\n(Text automatically extracted from paper. See PDF for full details and illustrations.)"

                # Combine
                new_content = f"---\n{new_frontmatter}\n---\n{body}{writeup}"
                
                with open(index_path, 'w') as f:
                    f.write(new_content)
            else:
                print("  No PDF match found.")

if __name__ == "__main__":
    process_publications()

