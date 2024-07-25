#!/usr/bin/env python3

import sys
import os
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.uic import loadUi



current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the paths to the model and controller directories
model_dir = os.path.join(current_dir, "..", 'model')
controller_dir = os.path.join(current_dir, "..", "controller")
sys.path.append(model_dir)
sys.path.append(controller_dir)

import shared_variables



# Add the directories to sys.path
sys.path.append(model_dir)
sys.path.append(controller_dir)

class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Start_menu.ui", self)

        
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower() 

        self.random_palette_button.clicked.connect(self.prompt_palette_size)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the background image to cover the entire window
        self.background_label.resize(self.size())

    def random_palette_button_clicked(self):
        from palette_display_menu import RandomPaletteDisplay
        geometry = self.geometry()
        self.show_palette = RandomPaletteDisplay()
        self.show_palette.setGeometry(geometry)
        self.show_palette.show()
        self.hide()

    def prompt_palette_size(self):
        dialog = PaletteSizeDialog(self)
        dialog.exec_()
        if dialog.palette_size_selected:
            self.random_palette_button_clicked()

class PaletteSizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Palette Size")

        layout = QVBoxLayout()

        label = QLabel("Please select the number of colors for the palette:")
        layout.addWidget(label)

        self.button3 = QPushButton("3 Colors")
        self.button6 = QPushButton("6 Colors")
        self.button10 = QPushButton("10 Colors")

        layout.addWidget(self.button3)
        layout.addWidget(self.button6)
        layout.addWidget(self.button10)

        self.setLayout(layout)

        self.palette_size_selected = False

        self.button3.clicked.connect(self.set_palette_size_3)
        self.button6.clicked.connect(self.set_palette_size_6)
        self.button10.clicked.connect(self.set_palette_size_10)

    def set_palette_size_3(self):
        shared_variables.palette_size = 3
        self.palette_size_selected = True
        self.accept()

    def set_palette_size_6(self):
        shared_variables.palette_size = 6
        self.palette_size_selected = True
        self.accept()

    def set_palette_size_10(self):
        shared_variables.palette_size = 10
        self.palette_size_selected = True
        self.accept()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec_())