#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class ColorPaletteGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Palette Generator')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout
        layout = QVBoxLayout()

        # Add widgets
        button = QPushButton('Generate Colors')
        layout.addWidget(button)

        central_widget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorPaletteGenerator()
    ex.show()
    sys.exit(app.exec_())