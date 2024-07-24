#!/usr/bin/env python3

import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.uic import loadUi

class ColorPaletteGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Palette_display_menu.ui", self)
        

        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower() 

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the background image to cover the entire window
        self.background_label.resize(self.size())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorPaletteGenerator()
    ex.show()
    sys.exit(app.exec_())
