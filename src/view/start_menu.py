#!/usr/bin/env python3

import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.uic import loadUi


class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Start_menu.ui", self)

        self.palette_size = 0
        

        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower() 

        self.random_palette_button.clicked.connect(self.random_palette_button_clicked)

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
        # Create a message box to prompt for palette size
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Select Palette Size")
        msg_box.setText("Please select the number of colors for the palette:")
        msg_box.setIcon(QMessageBox.Question)

        # Add custom buttons for palette size options
        button3 = msg_box.addButton("3 Colors", QMessageBox.ActionRole)
        button6 = msg_box.addButton("6 Colors", QMessageBox.ActionRole)
        button10 = msg_box.addButton("10 Colors", QMessageBox.ActionRole)

        # Show the message box and wait for user interaction
        msg_box.exec_()

        if msg_box.clickedButton() == button3:
            self.palette_size = 3
        elif msg_box.clickedButton() == button6:
            self.palette_size = 6
        elif msg_box.clickedButton() == button10:
            self.palette_size = 10



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec_())