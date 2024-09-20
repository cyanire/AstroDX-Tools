import os
import re

def process_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    skip_inote_section = False

    for line in lines:
        if skip_inote_section:
            if line.strip() == 'E':
                skip_inote_section = False
            continue
        
        if re.match(r"&lv_[1-3]=", line):
            continue

        if re.match(r"&des_[1-3]=", line):
            continue

        if re.match(r"&inote_[1-3]=", line):
            skip_inote_section = True
            continue
        
        processed_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)
    print(f"Processed: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_txt_file(file_path)

# modify the path below to your targeted folder
directory = '/path/to/your/directory'
process_directory(directory)