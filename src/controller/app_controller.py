#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from view.start_menu import StartMenu
from view.palette_display_menu import RandomPaletteDisplay
from view.image_palette_display_menu import ImagePaletteDisplay

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.start_menu = StartMenu(self)
        self.random_palette_display = RandomPaletteDisplay(self)
        self.image_palette_display = ImagePaletteDisplay(self)

        self.current_geometry = None

        # Set initial visibility
        self.start_menu.show()

    def show_start_menu(self):
        self.update_geometry(self.start_menu)
        self.start_menu.show()
        self.random_palette_display.hide()
        self.image_palette_display.hide()

    def show_random_palette_display(self):
        self.update_geometry(self.start_menu)
        self.random_palette_display.show()
        self.start_menu.hide()
        self.image_palette_display.hide()

    def show_image_palette_display(self):
        self.update_geometry(self.start_menu)
        self.image_palette_display.show()
        self.start_menu.hide()
        self.random_palette_display.hide()

    def update_geometry(self, window):
        if self.current_geometry:
            window.setGeometry(self.current_geometry)

    def store_geometry(self, window):
        self.current_geometry = window.geometry()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    controller = AppController()
    sys.exit(controller.app.exec_())
