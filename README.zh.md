# AstroDX Tools

Welcome to the **AstroDX Tools**! / 欢迎使用 **AstroDX 工具**！

You can read this document in English or 中文. / 你可以选择阅读英文或中文版本。

## Language / 语言选择

- [English Version](README.md)
- [中文版](README.zh.md)

---
# AstroDX 工具

用于 AstroDX 音乐游戏的 Python 小工具

该仓库包含几个 Python 脚本，旨在帮助管理和整理与 AstroDX 音乐游戏相关的文件。

## 安装

在使用这些工具之前，**请更改默认路径为你的 "levels" 文件夹路径！**

## 工具

### 1. **PV 删除器** (PV Deleter)
该脚本会删除文件夹中的所有 `pv.mp4` 文件。

使用时，运行脚本后，它会删除指定文件夹及其子文件夹中的所有 `.mp4` 文件。

### 2. **难度删除器**(Difficulties Deleter)
该脚本会删除 `.txt` 文件中的 easy、basic 和 advance 难度。

运行该脚本后，它会清理 `.txt` 文件，删除与 easy、basic 和 advance 难度相关的部分。

### 3. **AstroDX 文件夹整理器**(AstroDX Folder Organizer)
该脚本帮助整理你的 AstroDX 文件夹结构。

**重要：** 文件夹结构必须遵循以下规则：
- **二级文件夹** 应该是收藏夹（例如，代表不同歌曲分组或类别的文件夹）。
- **三级文件夹** 应该包含实际的歌曲文件。

该脚本会根据文件夹结构自动将文件移动到适当的 `levels` 和 `collections` 文件夹。
### 4. **合集转换器** (Collections Converter)
此脚本用于在指定目录中创建 `manifest.json` 文件。
## 如何使用

1. 克隆或下载该仓库到你的本地机器。
2. 确保你安装了 Python 3.x。
3. 运行你想使用的脚本，通过终端执行以下命令：
   
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
   或者运行 `GUI` 以选择功能 :
   
   ```bash
   python adxtools_gui.py
   ```

## 许可证

本项目采用 MIT 许可证 - 请参阅 [LICENSE](./LICENSE) 文件以了解详细信息。

