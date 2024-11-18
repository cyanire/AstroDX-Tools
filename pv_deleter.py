import os

def log_message(text_widget, message):
    if text_widget:
        text_widget.insert("end", message + "\n")
        text_widget.yview("end")
    else:
        print(message)

def delete_mp4_files(directory, text_widget=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                os.remove(os.path.join(root, file))
                if text_widget:
                    log_message(text_widget, f"Deleted: {os.path.join(root, file)}")
                else:
                    print(f"Deleted: {os.path.join(root, file)}")

if __name__ == "__main__":
    directory = input("Enter directory: ")
    delete_mp4_files(directory)  # No text_widget in terminal mode
