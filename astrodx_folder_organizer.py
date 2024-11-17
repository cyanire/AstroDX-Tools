import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog

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
    if os.path.exists(manifest_path):
        os.remove(manifest_path)
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=4)
    print(f"Manifest saved at: {manifest_path}")

def move_folders(parent_directory):
    levels_directory = os.path.join(parent_directory, 'levels')
    collections_directory = os.path.join(parent_directory, 'collections')
    if not os.path.exists(levels_directory):
        os.makedirs(levels_directory)
    if not os.path.exists(collections_directory):
        os.makedirs(collections_directory)
    for folder in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, folder)
        if os.path.isdir(folder_path):
            if folder == "levels" or folder == "collections":
                continue
            create_manifest(folder_path)
            if not any(os.path.isdir(os.path.join(folder_path, subfolder)) for subfolder in os.listdir(folder_path)):
                new_location = os.path.join(collections_directory, folder)
                shutil.move(folder_path, new_location)
                print(f" {folder} Moved to {collections_directory}")
            else:
                for subfolder in os.listdir(folder_path):
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if os.path.isdir(subfolder_path):
                        new_location = os.path.join(levels_directory, subfolder)
                        shutil.move(subfolder_path, new_location)
                        print(f" {subfolder} Moved to {levels_directory}")
                new_location = os.path.join(collections_directory, folder)
                shutil.move(folder_path, new_location)
                print(f" {folder} Moved to {collections_directory}")

def choose_directory_and_process():
    root = tk.Tk()
    root.withdraw()
    parent_directory = filedialog.askdirectory(title="choose the folder")
    if parent_directory:
        move_folders(parent_directory)

choose_directory_and_process()
