import os
import shutil

def log_message(text_widget, message):
    if text_widget:
        text_widget.insert("end", message + "\n")
        text_widget.yview("end")
    else:
        print(message)

def organize_folders(parent_directory, text_widget=None):
    levels_directory = os.path.join(parent_directory, 'levels')
    collections_directory = os.path.join(parent_directory, 'collections')
    os.makedirs(levels_directory, exist_ok=True)
    os.makedirs(collections_directory, exist_ok=True)
    for folder in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, folder)
        if os.path.isdir(folder_path) and folder not in ["levels", "collections"]:
            if not any(os.path.isdir(os.path.join(folder_path, subfolder)) for subfolder in os.listdir(folder_path)):
                shutil.move(folder_path, collections_directory)
                if text_widget:
                    log_message(text_widget, f"Moved {folder} to collections.")
                else:
                    print(f"Moved {folder} to collections.")
            else:
                for subfolder in os.listdir(folder_path):
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if os.path.isdir(subfolder_path):
                        shutil.move(subfolder_path, levels_directory)
                        if text_widget:
                            log_message(text_widget, f"Moved {subfolder} to levels.")
                        else:
                            print(f"Moved {subfolder} to levels.")
                shutil.move(folder_path, collections_directory)
                if text_widget:
                    log_message(text_widget, f"Moved {folder} to collections.")
                else:
                    print(f"Moved {folder} to collections.")

if __name__ == "__main__":
    directory = input("Enter directory: ")
    organize_folders(directory) 
