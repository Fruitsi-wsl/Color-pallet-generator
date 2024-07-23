#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi

class ColorPaletteGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Start_menu.ui", self)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorPaletteGenerator()
    ex.show()
    sys.exit(app.exec_())