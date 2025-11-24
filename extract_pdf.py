import re
import zlib

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        content = f.read()

    # Regex to find streams
    # PDF streams are usually: stream\r\n...data...\r\nendstream
    # But can be just \n.
    # We look for 'stream' and 'endstream' byte markers.
    
    start_marker = b'stream'
    end_marker = b'endstream'
    
    current_pos = 0
    extracted_text = []
    
    while True:
        start_pos = content.find(start_marker, current_pos)
        if start_pos == -1:
            break
        
        # Move past 'stream'
        data_start = start_pos + len(start_marker)
        
        # Check for newline (CR LF or LF)
        if content[data_start:data_start+2] == b'\r\n':
            data_start += 2
        elif content[data_start:data_start+1] == b'\n':
            data_start += 1
            
        end_pos = content.find(end_marker, data_start)
        if end_pos == -1:
            break
            
        # Extract chunk
        chunk = content[data_start:end_pos]
        
        # Remove trailing newline before endstream if present
        if chunk.endswith(b'\r\n'):
            chunk = chunk[:-2]
        elif chunk.endswith(b'\n'):
            chunk = chunk[:-1]
            
        # Try decompress
        try:
            decompressed = zlib.decompress(chunk)
            # Now look for text strings in the decompressed data.
            # Text is usually in ( ) or < > hex.
            # Simple regex for (Text) Tj or (Text) TJ
            # We'll just look for ( ... ) patterns.
            
            text_chunk = decompressed.decode('latin1', errors='ignore')
            
            # Find text in parentheses
            # This is a naive parser, handling escaped parens is hard with regex
            matches = re.findall(r'\((.*?)\)', text_chunk)
            if matches:
                extracted_text.extend(matches)
                
        except Exception as e:
            # Not a zlib stream or other error
            pass
            
        current_pos = end_pos + len(end_marker)
        
    return "\n".join(extracted_text)

try:
    text = extract_text_from_pdf('CV_Rabimba_Academic.pdf')
    # Filter out short garbage strings
    clean_text = "\n".join([line for line in text.split('\n') if len(line) > 3])
    
    with open('cv_extracted_python.txt', 'w') as f:
        f.write(clean_text)
    print("Extraction complete.")
except Exception as e:
    print(f"Error: {e}")

