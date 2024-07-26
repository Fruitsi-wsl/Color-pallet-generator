#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication
import PyQt5.uic
import colorgram


# Set up the path to include 'src' and its subdirectories
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = current_dir  # Assuming 'main.py' is in the 'src' directory
model_dir = os.path.join(src_dir, 'model')
controller_dir = os.path.join(src_dir, 'controller')
view_dir = os.path.join(src_dir, 'view')

# Add directories to sys.path
sys.path.append(src_dir)
sys.path.append(model_dir)
sys.path.append(controller_dir)
sys.path.append(view_dir)

from app_controller import AppController
import shared_variables as shared_variables  # Make sure this import works

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.run()  # Ensure that the 'run' method exists in 'AppController'
    sys.exit(app.exec_())