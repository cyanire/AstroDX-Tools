import os
import shutil

def create_directory(path):
    """Creates a directory if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)

def move_folder_to_directory(folder_path, target_directory, log_callback=None, log_message=None):
    """Moves a folder to a target directory and logs the action."""
    shutil.move(folder_path, target_directory)
    log_message = log_message or f"Moved {os.path.basename(folder_path)}"
    if log_callback:
        log_callback(log_message)
    else:
        print(log_message)

def organize_folders(parent_dir, log_callback=None):
    """Organizes folders in the specified parent directory by moving them to 'levels' or 'collections'."""
    parent_dir = os.path.normpath(parent_dir).encode('utf-8').decode('utf-8')
    levels_dir = os.path.join(parent_dir, 'levels')
    collections_dir = os.path.join(parent_dir, 'collections')

    create_directory(levels_dir)
    create_directory(collections_dir)

    for folder in os.listdir(parent_dir):
        folder_path = os.path.join(parent_dir, folder)
        
        # Skip 'levels' and 'collections' directories
        if os.path.isdir(folder_path) and folder not in ["levels", "collections"]:
            # If no subdirectories are found, move to collections
            if not any(os.path.isdir(os.path.join(folder_path, subfolder)) for subfolder in os.listdir(folder_path)):
                move_folder_to_directory(folder_path, collections_dir, log_callback, f"Moved {folder} to collections.")
            else:
                # Otherwise, move subdirectories to 'levels'
                for subfolder in os.listdir(folder_path):
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if os.path.isdir(subfolder_path):
                        move_folder_to_directory(subfolder_path, levels_dir, log_callback, f"Moved {subfolder} to levels.")
                
                # After processing subfolders, move the parent folder to 'collections'
                move_folder_to_directory(folder_path, collections_dir, log_callback, f"Moved {folder} to collections.")

if __name__ == "__main__":
    directory = input("Enter directory: ")
    organize_folders(directory)
