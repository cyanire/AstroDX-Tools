import os

def delete_mp4_files(directory, log_callback = None):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                log_message = f"Deleted: {file_path}"
                if log_callback:
                    log_callback(log_message)
                else:
                    print(log_message)

if __name__ == "__main__":
    directory = input("Enter directory: ")
    delete_mp4_files(directory)