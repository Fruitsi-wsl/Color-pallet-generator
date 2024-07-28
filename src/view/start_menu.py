#!/usr/bin/env python3

import sys
import os
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QDialog, QFileDialog, QColorDialog, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi





current_dir = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_dir, "Start_menu.ui")

import shared_variables as shared_variables
from model.generate_color_coded_palette import generate_complementary_palette



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

        

        self.random_palette_button.clicked.connect(lambda: (self.prompt_palette_size(), self.random_palette_button_clicked() ))
        self.image_palette_button.clicked.connect(lambda: (self.prompt_palette_size(), self.select_image()))
        self.select_color_button.clicked.connect(lambda: (self.prompt_palette_size(), self.prompt_color_selection(), self.color_coded_palette_button_clicked(), self.create_color_coded_palette()))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the background image to cover the entire window
        self.background_label.resize(self.size())

    def random_palette_button_clicked(self):
        if shared_variables.palette_size_selected:
            self.controller.show_random_palette_display()

    def image_palette_button_clicked(self):
        self.controller.show_image_palette_display()

    def color_coded_palette_button_clicked(self):
        if shared_variables.selected_color != []:
            self.controller.show_color_coded_palette_display()


    def create_color_coded_palette(self):
        if shared_variables.selected_color != []:
            self.palette = generate_complementary_palette(shared_variables.selected_color, shared_variables.palette_size)
        

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



    def prompt_color_selection(self):
        if shared_variables.palette_size_selected:
            color = QColorDialog.getColor()
            if color.isValid():
            # Convert QColor to RGB tuple
                shared_variables.selected_color = (color.red() / 255.0, color.green() / 255.0, color.blue() / 255.0)
    
            

        


    

    

class PaletteSizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Palette Size")

        layout = QVBoxLayout()

        label = QLabel("Please select the number of colors for the palette:")
        layout.addWidget(label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(3, 10)
        self.slider.setValue(6)  # Default value
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider)

        self.value_label = QLabel("6")
        self.slider.valueChanged.connect(self.update_value_label)
        layout.addWidget(self.value_label)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.set_palette_size)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def update_value_label(self, value):
        self.value_label.setText(str(value))

    def set_palette_size(self):
        shared_variables.palette_size = self.slider.value()
        shared_variables.palette_size_selected = True
        self.accept()



        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec_())