import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog
import sys
import io

# Force Python to use utf-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_manifest(directory):
    name = os.path.basename(directory)
    
    # Get subdirectories as levelIds
    level_ids = sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])
    
    # Manifest data
    manifest_data = {
        "name": name,
        "id": None,
        "serverUrl": None,
        "levelIds": level_ids
    }
    
    # Delete existing manifest.json if exists
    manifest_path = os.path.join(directory, "manifest.json")
    if os.path.exists(manifest_path):
        os.remove(manifest_path)
    
    # Write the new manifest.json file
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=4)
    
    print(f"Manifest saved at: {manifest_path}")

def move_folders(parent_directory):
    # Create levels and collections folders if not exist
    levels_directory = os.path.join(parent_directory, 'levels')
    collections_directory = os.path.join(parent_directory, 'collections')
    
    if not os.path.exists(levels_directory):
        os.makedirs(levels_directory)
        
    if not os.path.exists(collections_directory):
        os.makedirs(collections_directory)
    
    # Traverse subfolders of the parent directory
    for folder in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, folder)
        
        if os.path.isdir(folder_path):
            if folder == "levels" or folder == "collections":
                continue  # Skip the levels and collections folders
            
            # Create manifest for the subfolder
            create_manifest(folder_path)
            
            if not any(os.path.isdir(os.path.join(folder_path, subfolder)) for subfolder in os.listdir(folder_path)):
                # Move to collections if no sub-subfolders exist
                shutil.move(folder_path, collections_directory)
                print(f"Folder {folder} moved to {collections_directory}")
            else:
                # Move sub-subfolders to levels
                for subfolder in os.listdir(folder_path):
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if os.path.isdir(subfolder_path):
                        shutil.move(subfolder_path, levels_directory)
                        print(f"Folder {subfolder} moved to {levels_directory}")
                
                # Move the main folder to collections
                shutil.move(folder_path, collections_directory)
                print(f"Folder {folder} moved to {collections_directory}")

def choose_directory_and_process():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Choose the parent directory
    parent_directory = filedialog.askdirectory(title="Please choose the parent directory")
    
    if parent_directory:
        move_folders(parent_directory)

# Run the folder selection and processing
choose_directory_and_process()
