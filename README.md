# AstroDX Tools

Welcome to the **AstroDX Tools**! / 欢迎使用 **AstroDX 工具**！

You can read this document in English or 中文. / 你可以选择阅读英文或中文版本。

## Language / 语言选择

- [English Version](README.md)
- [中文版](README.zh.md)

---

## Tools

### 1. **PV Deleter**
This script deletes all of the `pv.mp4` files in your folder.

To use, simply run the script and it will delete all `.mp4` files within the specified folder and its subdirectories.

### 2. **Difficulties Deleter**
This script deletes all the difficulties of easy, basic, and advance in `.txt` files.

Run this script to clean up `.txt` files by removing the sections related to easy, basic, and advance difficulties.

### 3. **Folder Organizer**
This script helps organize your folder structure for AstroDX.

**Important:** The folder structure must follow these rules:
- **Second-level folders** should be collections (e.g., folders representing different groups or categories of songs).
- **Third-level folders** should contain the actual song files.

The script will automatically move files into the appropriate `levels` and `collections` directories based on the folder structure.

### 4. **Collections Converter**
This script is designed to create a `manifest.json` file in a specified directory.

## How to Use
### 1. Download the latest release and run directly
### 2. Run with Python:
1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the script you want to use by executing the following command in your terminal:

   ```bash
   python pv_deleter.py
   ```

   
   ```bash
   python difficulties_deleter.py
   ```


   ```bash
   python folder_organizer.py
   ```
   
   ```bash
   python collections_converterr.py
   ```
   or running the `GUI` to select function :
   1. First, install the dependency `PyQt6`
      ```bash
      pip install PyQt6
      ```
   2. Run the `GUI`
      ```bash
      python adxtools_gui.py
      ```
## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

