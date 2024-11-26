import os
import json

def create_manifest(directory, log_callback=None):
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
    
    log_message = f"Manifest created at: {manifest_path}"
    
    if log_callback:
        log_callback(log_message)
    else:
        print(log_message)

if __name__ == "__main__":
    directory = input("Enter directory: ")
    create_manifest(directory)