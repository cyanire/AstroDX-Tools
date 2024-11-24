import os
import json

def log_message(text_widget, message):
    if text_widget:
        text_widget.insert("end", message + "\n")
        text_widget.yview("end")
    else:
        print(message)

def create_manifest(directory, text_widget=None):
    name = os.path.basename(directory)
    level_ids = sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])
    manifest_data = {
        "name": name,
        "id": None,
        "serverUrl": None,
        "levelIds": level_ids
    }
    manifest_path = os.path.join(directory, "manifest.json")
    if os.path.exists(manifest_path):
        os.remove(manifest_path)
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=4)
    if text_widget:
        log_message(text_widget, f"Manifest created at: {manifest_path}")
    else:
        print(f"Manifest created at: {manifest_path}")

if __name__ == "__main__":
    directory = input("Enter directory: ")
    create_manifest(directory)  