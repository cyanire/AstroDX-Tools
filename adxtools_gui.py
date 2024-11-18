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

def load_sun_valley_theme(root):
    sv_ttk.set_theme("light")

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

languages = {
    'en': {
        'choose_directory': 'Choose Directory',
        'generate_json': 'Generate JSON',
        'organize_folders': 'Organize Folders',
        'delete_difficulties': 'Delete Difficulties',
        'delete_pv': 'Delete PV Files',
        'error': 'Error',
        'no_tasks': 'Please select at least one task.',
        'confirm': 'Confirm Tasks',
        'success': 'Processing complete!'
    },
    'zh': {
        'choose_directory': '选择目录',
        'generate_json': '生成 JSON',
        'organize_folders': '整理文件夹',
        'delete_difficulties': '删除难度',
        'delete_pv': '删除 PV 文件',
        'error': '错误',
        'no_tasks': '请选择至少一个任务。',
        'confirm': '确认任务',
        'success': '处理完成！'
    }
}
current_language = 'en'

def toggle_language(event):
    global current_language
    current_language = 'zh' if lang_combobox.get() == '中文' else 'en'
    update_ui_language()

def update_ui_language():
    root.title("AstroDX Tools")
    entry_button.config(text=languages[current_language]['choose_directory'])
    json_check.config(text=languages[current_language]['generate_json'])
    organize_check.config(text=languages[current_language]['organize_folders'])
    difficulty_check.config(text=languages[current_language]['delete_difficulties'])
    pv_check.config(text=languages[current_language]['delete_pv'])
    lang_combobox.set("English" if current_language == 'en' else "中文")

def execute_functions():
    directory = filedialog.askdirectory(title=languages[current_language]['choose_directory'])
    if not directory:
        return
    tasks = []
    if var_json.get():
        tasks.append('generate_json')
    if var_difficulty.get():
        tasks.append('delete_difficulties')
    if var_pv.get():
        tasks.append('delete_pv')
    if var_organize.get():
        tasks.append('organize_folders')
    if not tasks:
        messagebox.showwarning(languages[current_language]['error'], languages[current_language]['no_tasks'])
        return
    if messagebox.askyesno(languages[current_language]['confirm'], "\n".join([languages[current_language][task] for task in tasks])):
        threading.Thread(target=run_tasks, args=(directory, tasks, output_text), daemon=True).start()

root = tk.Tk()
root.title("AstroDX Tools")
root.geometry("600x800")
load_sun_valley_theme(root)

frame = ttk.Frame(root)
frame.pack(pady=20)

font_large = ("Microsoft YaHei", 14)
font_small = ("Microsoft YaHei", 10)

var_json = tk.BooleanVar(value=True)
var_organize = tk.BooleanVar(value=True)
var_difficulty = tk.BooleanVar()
var_pv = tk.BooleanVar()

json_check = ttk.Checkbutton(frame, text=languages['en']['generate_json'], variable=var_json)
json_check.pack(anchor='w')
organize_check = ttk.Checkbutton(frame, text=languages['en']['organize_folders'], variable=var_organize)
organize_check.pack(anchor='w')
difficulty_check = ttk.Checkbutton(frame, text=languages['en']['delete_difficulties'], variable=var_difficulty)
difficulty_check.pack(anchor='w')
pv_check = ttk.Checkbutton(frame, text=languages['en']['delete_pv'], variable=var_pv)
pv_check.pack(anchor='w')

entry_button = ttk.Button(root, text=languages['en']['choose_directory'], command=execute_functions)
entry_button.pack(pady=10)

lang_combobox = ttk.Combobox(root, values=["English", "中文"], state="readonly", font=font_small)
lang_combobox.set("English")
lang_combobox.pack(pady=10)
lang_combobox.bind("<<ComboboxSelected>>", toggle_language)

output_text = tk.Text(root, wrap="word", height=10, font=font_small)
output_text.pack(fill="both", expand=True, padx=20, pady=10)

entry_button.configure(style="Large.TButton")
entry_button.pack(pady=20)

style = ttk.Style()
style.configure("Large.TButton", font=font_large, padding=10)
style.configure("Large.TCheckbutton", font=font_large)

json_check.configure(style="Large.TCheckbutton")
organize_check.configure(style="Large.TCheckbutton")
difficulty_check.configure(style="Large.TCheckbutton")
pv_check.configure(style="Large.TCheckbutton")

root.mainloop()
