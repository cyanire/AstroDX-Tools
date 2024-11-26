import sys
import os
import logging
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox, QFrame, QFileDialog, QMessageBox, QProgressBar
)
from PyQt6.QtCore import Qt, pyqtSignal, QThread
from PyQt6.QtGui import QFont, QIcon

from collections_converter import create_manifest
from folder_organizer import organize_folders
from difficulties_deleter import process_directory
from pv_deleter import delete_mp4_files

class Worker(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, tasks, directory):
        super().__init__()
        self.tasks = tasks
        self.directory = directory
        self.stop_flag = False

    def stop(self):
        self.stop_flag = True

    def run(self):
        try:
            self.progress.emit("Task execution started...")
            if 'generate_json' in self.tasks and not self.stop_flag:
                self.progress.emit("Generating JSON files...")
                for folder in os.listdir(self.directory):
                    folder_path = os.path.join(self.directory, folder)
                    if os.path.isdir(folder_path):
                        try:
                            create_manifest(folder_path, lambda msg: self.progress.emit(msg))
                            self.progress.emit(f"Created manifest file for {folder_path}.")
                        except Exception as e:
                            self.progress.emit(f"Error creating manifest file for {folder_path}: {e}")

            if 'delete_difficulties' in self.tasks and not self.stop_flag:
                self.progress.emit("Deleting difficulty files...")
                try:
                    process_directory(self.directory, lambda msg: self.progress.emit(msg))
                except Exception as e:
                    self.progress.emit(f"Error deleting difficulty files: {e}")

            if 'delete_pv' in self.tasks and not self.stop_flag:
                self.progress.emit("Deleting PV files...")
                try:
                    delete_mp4_files(self.directory, lambda msg: self.progress.emit(msg))
                except Exception as e:
                    self.progress.emit(f"Error deleting PV files: {e}")

            if 'organize_folders' in self.tasks and not self.stop_flag:
                self.progress.emit("Organizing folders...")
                try:
                    organize_folders(self.directory, lambda msg: self.progress.emit(msg))
                except Exception as e:
                    self.progress.emit(f"Error organizing folders: {e}")

            if not self.stop_flag:
                self.progress.emit("Task processing completed!")
                self.finished.emit()
        except Exception as e:
            self.progress.emit(f"Error: {str(e)}")
            self.finished.emit()


class AstroDXTools(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_language = 'zh'
        self.languages = {
            'en': {
                'choose_directory': 'Choose Path',
                'start': 'Start',
                'generate_json': 'Generate JSON',
                'organize_folders': 'Organize Folders',
                'delete_difficulties': 'Delete Difficulties',
                'delete_pv': 'Delete PV Files',
                'success': 'Processing complete!',
                'browse':'Browse',
            },
            'zh': {
                'choose_directory': '选择路径',
                'start': '开始',
                'generate_json': '生成 JSON',
                'organize_folders': '整理文件夹',
                'delete_difficulties': '删除难度',
                'delete_pv': '删除 PV 文件',
                'success': '处理完成！',
                'browse':'浏览',
            }
        }

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AstroDX Tools - v2.2.0")
        self.setGeometry(200, 200, 1000, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        top_bar = QHBoxLayout()
        language_label = QLabel("Language: ")
        language_label.setFont(QFont("微软雅黑", 10))
        self.language_combobox = QComboBox()
        self.language_combobox.addItems(["中文", "English"])
        self.language_combobox.setFont(QFont("微软雅黑", 10))
        self.language_combobox.setFixedWidth(80)
        self.language_combobox.setCurrentText("中文" if self.current_language == "zh" else "English")
        self.language_combobox.currentTextChanged.connect(self.toggle_language)
        top_bar.addStretch()
        top_bar.addWidget(language_label)
        top_bar.addWidget(self.language_combobox)
        main_layout.addLayout(top_bar)

        content_layout = QHBoxLayout()

        left_frame = QFrame()
        left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        left_layout = QVBoxLayout(left_frame)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.path_label = QLabel(self.languages[self.current_language]['choose_directory'])
        self.path_label.setFont(QFont("微软雅黑", 12))
        self.path_input = QLineEdit()
        self.path_input.setFont(QFont("微软雅黑", 10))
        self.browse_button = QPushButton(self.languages[self.current_language]['browse'])
        self.browse_button.setFont(QFont("微软雅黑", 10))
        self.browse_button.clicked.connect(self.choose_directory)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.browse_button)
        left_layout.addWidget(self.path_label)
        left_layout.addLayout(path_layout)

        self.json_checkbox = QCheckBox(self.languages[self.current_language]['generate_json'])
        self.json_checkbox.setFont(QFont("微软雅黑", 12))
        self.json_checkbox.setChecked(True)

        self.organize_checkbox = QCheckBox(self.languages[self.current_language]['organize_folders'])
        self.organize_checkbox.setFont(QFont("微软雅黑", 12))
        self.organize_checkbox.setChecked(True)

        self.difficulty_checkbox = QCheckBox(self.languages[self.current_language]['delete_difficulties'])
        self.difficulty_checkbox.setFont(QFont("微软雅黑", 12))

        self.pv_checkbox = QCheckBox(self.languages[self.current_language]['delete_pv'])
        self.pv_checkbox.setFont(QFont("微软雅黑", 12))

        left_layout.addWidget(self.json_checkbox)
        left_layout.addWidget(self.organize_checkbox)
        left_layout.addWidget(self.difficulty_checkbox)
        left_layout.addWidget(self.pv_checkbox)

        self.start_button = QPushButton(self.languages[self.current_language]['start'])
        self.start_button.setFont(QFont("微软雅黑", 14))
        self.start_button.setFixedSize(150, 50)
        self.start_button.clicked.connect(self.execute_tasks)
        left_layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        content_layout.addWidget(left_frame)

        right_frame = QFrame()
        right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        right_layout = QVBoxLayout(right_frame)

        self.log_output = QTextEdit()
        self.log_output.setFont(QFont("微软雅黑", 10))
        self.log_output.setReadOnly(True)
        right_layout.addWidget(self.log_output)

        content_layout.addWidget(right_frame)

        main_layout.addLayout(content_layout)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        right_layout.addWidget(self.progress_bar)

    def log_message(self, message):
        self.log_output.append(message)
        logging.debug(message)

    def choose_directory(self):
        directory = QFileDialog.getExistingDirectory(self, self.languages[self.current_language]['choose_directory'])
        if directory:
            self.path_input.setText(directory)

    def execute_tasks(self):
        directory = self.path_input.text()
        if not directory:
            QMessageBox.warning(self, "警告", self.languages[self.current_language]['choose_directory'])
            return

        tasks = []
        if self.json_checkbox.isChecked():
            tasks.append('generate_json')
        if self.organize_checkbox.isChecked():
            tasks.append('organize_folders')
        if self.difficulty_checkbox.isChecked():
            tasks.append('delete_difficulties')
        if self.pv_checkbox.isChecked():
            tasks.append('delete_pv')

        self.worker = Worker(tasks, directory)
        self.worker.progress.connect(self.log_message)
        self.worker.finished.connect(self.on_finish)
        self.worker.start()

        self.progress_bar.setVisible(True)

    def on_finish(self):
        self.worker.stop()
        self.worker.wait()
        self.worker = None
        self.progress_bar.setVisible(False)
        self.log_message(self.languages[self.current_language]['success'])

    def toggle_language(self, language):
        self.current_language = 'zh' if language == '中文' else 'en'
        self.update_ui_text()

    def update_ui_text(self):
        self.path_label.setText(self.languages[self.current_language]['choose_directory'])
        self.json_checkbox.setText(self.languages[self.current_language]['generate_json'])
        self.organize_checkbox.setText(self.languages[self.current_language]['organize_folders'])
        self.difficulty_checkbox.setText(self.languages[self.current_language]['delete_difficulties'])
        self.pv_checkbox.setText(self.languages[self.current_language]['delete_pv'])
        self.start_button.setText(self.languages[self.current_language]['start'])
        self.browse_button.setText(self.languages[self.current_language]['browse'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.ico'))
    window = AstroDXTools()
    window.show()
    sys.exit(app.exec())