#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication
from view.start_menu import StartMenu
from view.palette_display_menu import RandomPaletteDisplay
from view.image_palette_display_menu import ImagePaletteDisplay
from controller import shared_variables

# Correctly set the path to the parent directory of 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)  # Add the project root to sys.path

# For additional clarity, add the following paths explicitly (if needed)
sys.path.append(os.path.join(project_root, 'src'))
sys.path.append(os.path.join(project_root, 'src', 'model'))
sys.path.append(os.path.join(project_root, 'src', 'controller'))
sys.path.append(os.path.join(project_root, 'src', 'view'))

def main():
    app = QApplication(sys.argv)
    window = StartMenu()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()