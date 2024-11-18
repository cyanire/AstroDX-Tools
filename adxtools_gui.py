import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from collections_converter import create_manifest
from folder_organizer import organize_folders
from difficulties_deleter import process_directory
from pv_deleter import delete_mp4_files
import sv_ttk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

languages = {
    'en': {
        'choose_directory': 'Choose Path',
        'start': 'Start',
        'generate_json': 'Generate JSON',
        'organize_folders': 'Organize Folders',
        'delete_difficulties': 'Delete Difficulties',
        'delete_pv': 'Delete PV Files',
        'success': 'Processing complete!',
    },
    'zh': {
        'choose_directory': '选择路径',
        'start': '开始',
        'generate_json': '生成 JSON',
        'organize_folders': '整理文件夹',
        'delete_difficulties': '删除难度',
        'delete_pv': '删除 PV 文件',
        'success': '处理完成！',
    }
}

current_language = 'zh'
directory = ""
tasks = []


def log_message(text_widget, message):
    text_widget.insert(tk.END, message + '\n')
    text_widget.see(tk.END)


def run_tasks(directory, tasks, text_widget):
    try:
        if 'generate_json' in tasks:
            for folder in os.listdir(directory):
                folder_path = os.path.join(directory, folder)
                if os.path.isdir(folder_path):
                    create_manifest(folder_path, text_widget)
        if 'delete_difficulties' in tasks:
            process_directory(directory, text_widget)
        if 'delete_pv' in tasks:
            delete_mp4_files(directory, text_widget)
        if 'organize_folders' in tasks:
            organize_folders(directory, text_widget)
        log_message(text_widget, languages[current_language]['success'])
    except Exception as e:
        log_message(text_widget, f"Error: {str(e)}")


def execute_tasks():
    global directory, tasks
    if not directory:
        messagebox.showwarning("Warning", languages[current_language]['choose_directory'])
        return
    tasks = []
    if var_json.get():
        tasks.append('generate_json')
    if var_organize.get():
        tasks.append('organize_folders')
    if var_difficulty.get():
        tasks.append('delete_difficulties')
    if var_pv.get():
        tasks.append('delete_pv')
    threading.Thread(target=run_tasks, args=(directory, tasks, output_text), daemon=True).start()


def choose_directory():
    global directory
    directory = filedialog.askdirectory()
    directory_entry.set(directory)


def toggle_language(event=None):
    global current_language
    selected_language = lang_combobox.get()
    current_language = 'en' if selected_language == 'English' else 'zh'
    update_labels()


def update_labels():
    directory_label.config(text=languages[current_language]['choose_directory'])
    json_check.config(text=languages[current_language]['generate_json'])
    organize_check.config(text=languages[current_language]['organize_folders'])
    difficulty_check.config(text=languages[current_language]['delete_difficulties'])
    pv_check.config(text=languages[current_language]['delete_pv'])
    start_button.config(text=languages[current_language]['start'])


root = tk.Tk()
root.title("AstroDX Manager")
root.geometry("1000x600")
sv_ttk.set_theme("light")

# Main Layout
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left Panel
left_frame = ttk.Frame(main_frame, width=300)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Directory Selection
directory_entry = tk.StringVar()
directory_label = ttk.Label(left_frame, text=languages[current_language]['choose_directory'], font=("Microsoft YaHei", 12))
directory_label.grid(row=0, column=0, pady=10, sticky="w")
directory_box = ttk.Entry(left_frame, textvariable=directory_entry, font=("Microsoft YaHei", 10), width=25)
directory_box.grid(row=1, column=0, pady=5, sticky="w")
directory_button = ttk.Button(left_frame, text="Browse", command=choose_directory)
directory_button.grid(row=1, column=1, padx=5)

# Task Options
var_json = tk.BooleanVar(value=True)
var_organize = tk.BooleanVar(value=True)
var_difficulty = tk.BooleanVar()
var_pv = tk.BooleanVar()

style = ttk.Style()
style.configure("Large.TCheckbutton", font=("Microsoft YaHei", 12), padding=5)

json_check = ttk.Checkbutton(left_frame, text=languages[current_language]['generate_json'], variable=var_json, style="Large.TCheckbutton")
json_check.grid(row=2, column=0, pady=5, sticky="w")
organize_check = ttk.Checkbutton(left_frame, text=languages[current_language]['organize_folders'], variable=var_organize, style="Large.TCheckbutton")
organize_check.grid(row=3, column=0, pady=5, sticky="w")
difficulty_check = ttk.Checkbutton(left_frame, text=languages[current_language]['delete_difficulties'], variable=var_difficulty, style="Large.TCheckbutton")
difficulty_check.grid(row=4, column=0, pady=5, sticky="w")
pv_check = ttk.Checkbutton(left_frame, text=languages[current_language]['delete_pv'], variable=var_pv, style="Large.TCheckbutton")
pv_check.grid(row=5, column=0, pady=5, sticky="w")

# Start Button
style.configure("Large.TButton", font=("Microsoft YaHei", 14), padding=10)
start_button = ttk.Button(left_frame, text=languages[current_language]['start'], command=execute_tasks, style="Large.TButton", width=15)
start_button.grid(row=6, column=0, pady=30, columnspan=2)

# Language Combobox
lang_combobox = ttk.Combobox(root, values=["English", "中文"], state="readonly", width=8, font=("Microsoft YaHei", 10))
lang_combobox.set("English" if current_language == "en" else "中文")
lang_combobox.bind("<<ComboboxSelected>>", toggle_language)
lang_combobox.place(relx=0.01, rely=0.97, anchor="sw")

# Right Panel - Log Output with Scrollbar
right_frame = tk.Frame(main_frame, bd=0)  # Set borderwidth to 0
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Create vertical scrollbar with a thinner design
scrollbar = ttk.Scrollbar(right_frame, style="TScrollbar")
scrollbar.pack(side="right", fill="y")

# Create a Text widget for the output, making it read-only
output_text = tk.Text(right_frame, wrap="word", font=("Microsoft YaHei", 10), height=20, yscrollcommand=scrollbar.set)
output_text.pack(fill="both", expand=True)

# Set the scrollbar command
scrollbar.config(command=output_text.yview)

# Custom scrollbar style (adjusting thickness)
style = ttk.Style()
style.configure("TScrollbar", gripcount=0, thickness=8)  # Set thickness of scrollbar



root.mainloop()
