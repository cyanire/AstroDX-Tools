import os
import json

def create_manifest(directory):
    name = os.path.basename(directory)
    
    level_ids = sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])
    
    manifest_data = {
        "name": name,
        "id": None,
        "serverUrl": None,
        "levelIds": level_ids
    }
    
    manifest_path = os.path.join(directory, "manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=4)
    
    print(f"Manifest saved at: {manifest_path}")

# modify the path below to your targeted folder
directory = '/path/to/your/directory'
create_manifest(directory)