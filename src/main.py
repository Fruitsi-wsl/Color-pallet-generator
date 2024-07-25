#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from view.start_menu import StartMenu
from view import resources_rc
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the paths to the model and controller directories
model_dir = os.path.join(current_dir, 'model')
view_dir = os.path.join(current_dir, "view")
controller_dir = os.path.join(current_dir, "controller")
sys.path.append(model_dir)
sys.path.append(controller_dir)
sys.path.append(view_dir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show_main_window = StartMenu()
        self.show_main_window.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.hide()
    app.exec_()