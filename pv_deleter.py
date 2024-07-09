import os

def delete_mp4_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mp4'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# replace the defalut path to your "levels" folder's path
folder_path = 'your/folder/path'
delete_mp4_files(folder_path)
