import os

def delete_mp4_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# modify the path below to your targeted folder
directory = '/path/to/your/directory'
delete_mp4_files(directory)