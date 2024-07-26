#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy
from view.start_menu import StartMenu
from view.palette_display_menu import RandomPaletteDisplay
from view.image_palette_display_menu import ImagePaletteDisplay


class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.stacked_widget = QStackedWidget()
        self.window.setCentralWidget(self.stacked_widget)

        self.start_menu = StartMenu(self)
        self.random_palette_display = RandomPaletteDisplay(self)
        self.image_palette_display = ImagePaletteDisplay(self)

        self.stacked_widget.addWidget(self.start_menu)
        self.stacked_widget.addWidget(self.random_palette_display)
        self.stacked_widget.addWidget(self.image_palette_display)

        # Set initial size for the main window
        self.window.resize(800, 700)  # Adjust size as needed

        # Optionally, set a size policy for the stacked widget
        self.stacked_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.show_start_menu()

    def show_start_menu(self):
        self.stacked_widget.setCurrentWidget(self.start_menu)

    def show_random_palette_display(self):
        self.stacked_widget.setCurrentWidget(self.random_palette_display)

    def show_image_palette_display(self):
        self.stacked_widget.setCurrentWidget(self.image_palette_display)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    controller = AppController()
    controller.run()
