import os
import re

def log_message(text_widget, message):
    if text_widget:
        text_widget.insert("end", message + "\n")
        text_widget.yview("end")
    else:
        print(message)

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
        if re.match(r"&lv_[1-3]=", line) or re.match(r"&des_[1-3]=", line):
            continue
        if re.match(r"&inote_[1-3]=", line):
            skip_inote_section = True
            continue
        processed_lines.append(line)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

def process_directory(directory, text_widget=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                process_txt_file(os.path.join(root, file))
                if text_widget:
                    log_message(text_widget, f"Processed: {os.path.join(root, file)}")
                else:
                    print(f"Processed: {os.path.join(root, file)}")

if __name__ == "__main__":
    directory = input("Enter directory: ")
    process_directory(directory) 