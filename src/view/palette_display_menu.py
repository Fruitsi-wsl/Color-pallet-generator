#!/usr/bin/env python3




import os
import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer



current_dir = os.path.dirname(os.path.abspath(__file__))

model_dir = os.path.join(current_dir, "..", 'model')
controller_dir = os.path.join(current_dir, "..", "controller")
sys.path.append(model_dir)
sys.path.append(controller_dir)


ui_path = os.path.join(current_dir, "Palette_display_menu.ui")


import shared_variables

from generate_random_palette import generate_color_palette



class RandomPaletteDisplay(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(ui_path, self)
    
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower() 

        self.palette = generate_color_palette(shared_variables.palette_size)

        self.GoBackButton.clicked.connect(self.push_GoBackButton)
        self.Regenerate_Button.clicked.connect(self.push_RegenerateButton)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self.setup_view)
        self.update_palette_display()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Resize the background image to cover the entire window
        self.background_label.resize(self.size())

        self.update_palette_display()

    def setup_view(self):
        if self.palette_display:
            self.update_palette_display()


    def update_palette_display(self):   
        if not self.palette_display:
            return

        # Create a new QGraphicsScene
        scene = QGraphicsScene()

        # Set the scene rect to match the view size
        width = self.palette_display.width()
        height = self.palette_display.height()
        scene.setSceneRect(0, 0, width, height)

        # Calculate item width based on the number of colors
        item_width = width / len(self.palette)

        for i, color in enumerate(self.palette):
            r, g, b = [int(c * 255) for c in color]
            rect_item = QGraphicsRectItem(i * item_width, 0, item_width, height)
            rect_item.setBrush(QBrush(QColor(r, g, b)))
            scene.addItem(rect_item)

        # Set the scene to the QGraphicsView
        self.palette_display.setScene(scene)

        self.palette_display.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)


    def push_GoBackButton(self):
        from view.start_menu import StartMenu
        shared_variables.palette_size_selected = False
        geometry = self.geometry()
        self.goback = StartMenu()
        self.goback.setGeometry(geometry)   
        self.goback.show()
        self.hide()

    def push_RegenerateButton(self):
        self.palette = generate_color_palette(shared_variables.palette_size)
        self.update_palette_display()
    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPaletteDisplay()
    ex.show()
    sys.exit(app.exec_())
