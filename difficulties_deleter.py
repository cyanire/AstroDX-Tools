import os
import re

def process_txt_file(file_path, log_callback=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    skip_inote_section = False
    for line in lines:
        if skip_inote_section:
            if line.strip() == 'E':
                skip_inote_section = False
            continue
        if re.match(r"&lv_[1-3]=", line) or re.match(r"&des_[1-3]=", line):
            continue
        if re.match(r"&inote_[1-3]=", line):
            skip_inote_section = True
            continue
        processed_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)
    
    log_message = f"Processed: {file_path}"
    if log_callback:
        log_callback(log_message)
    else:
        print(log_message)

def process_directory(directory, log_callback=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                process_txt_file(os.path.join(root, file), log_callback)

if __name__ == "__main__":
    directory = input("Enter directory: ")
    process_directory(directory)