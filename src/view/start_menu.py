#!/usr/bin/env python3

import sys
import os
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi





current_dir = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_dir, "Start_menu.ui")

import shared_variables as shared_variables
from model.generate_random_palette import generate_color_palette



class StartMenu(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        loadUi(ui_path, self)

        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower() 

        

        self.random_palette_button.clicked.connect(lambda: (self.prompt_palette_size(), self.random_palette_button_clicked(), self.set_palette_size() ))
        self.image_palette_button.clicked.connect(lambda: (self.prompt_palette_size(), self.select_image()))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the background image to cover the entire window
        self.background_label.resize(self.size())

    def random_palette_button_clicked(self):
        self.controller.show_random_palette_display()

    def image_palette_button_clicked(self):
        self.controller.show_image_palette_display()

    def set_palette_size(self):
        self.palette = generate_color_palette(shared_variables.palette_size)
        

    def prompt_palette_size(self):
        dialog = PaletteSizeDialog(self)
        dialog.exec_()

    def select_image(self):

        if shared_variables.palette_size_selected:
        # Create a QFileDialog to let the user select an image file
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            "",
            "Image Files (*.jpg *.jpeg *.png *.gif);;All Files (*)",
            options=options
        )

            shared_variables.image_path = file_path
            self.image_palette_button_clicked()
        


    

    

class PaletteSizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Palette Size")

        layout = QVBoxLayout()

        label = QLabel("Please select the number of colors for the palette:")
        layout.addWidget(label)

        self.button3 = QPushButton("3 Colors")
        self.button6 = QPushButton("6 Colors")
        self.button10 = QPushButton("9 Colors")

        layout.addWidget(self.button3)
        layout.addWidget(self.button6)
        layout.addWidget(self.button10)

        self.setLayout(layout)


        self.button3.clicked.connect(self.set_palette_size_3)
        self.button6.clicked.connect(self.set_palette_size_6)
        self.button10.clicked.connect(self.set_palette_size_9)

    def set_palette_size_3(self):
        shared_variables.palette_size = 3
        shared_variables.palette_size_selected = True
        self.accept()

    def set_palette_size_6(self):
        shared_variables.palette_size = 6
        shared_variables.palette_size_selected = True
        self.accept()

    def set_palette_size_9(self):
        shared_variables.palette_size = 9
        shared_variables.palette_size_selected = True
        self.accept()

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec_())