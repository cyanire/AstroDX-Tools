# AstroDX Tools

Welcome to the **AstroDX Tools**! / 欢迎使用 **AstroDX 工具**！

You can read this document in English or 中文. / 你可以选择阅读英文或中文版本。

## Language / 语言选择

- [English Version](README.md)
- [中文版](README.zh.md)

---

## Setup

Before using the tools, **please change the default path to your "levels" folder's path!**

## Tools

### 1. **PV Deleter**
This script deletes all of the `pv.mp4` files in your folder.

To use, simply run the script and it will delete all `.mp4` files within the specified folder and its subdirectories.

### 2. **Difficulties Deleter**
This script deletes all the difficulties of easy, basic, and advance in `.txt` files.

Run this script to clean up `.txt` files by removing the sections related to easy, basic, and advance difficulties.

### 3. **AstroDX Folder Organizer**
This script helps organize your folder structure for AstroDX.

**Important:** The folder structure must follow these rules:
- **Second-level folders** should be collections (e.g., folders representing different groups or categories of songs).
- **Third-level folders** should contain the actual song files.

The script will automatically move files into the appropriate `levels` and `collections` directories based on the folder structure. It will also generate the necessary `manifest.json` files for the collections.

You do **not** need to modify any paths in this script; it will prompt you to select the folder when executed. The script will organize your files accordingly, creating `levels` and `collections` directories, and generating `manifest.json` files for the collections.

## How to Use

1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the script you want to use by executing the following command in your terminal:

   ```bash
   python pv_deleter.py
   ```

   or
   
   ```bash
   python difficulties_deleter.py
   ```

   or

   ```bash
   python astrodx_folder_organizer.py
   ```
