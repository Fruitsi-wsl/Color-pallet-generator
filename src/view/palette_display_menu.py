#!/usr/bin/env python3




import os
import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsScene, QGraphicsRectItem, QGraphicsProxyWidget
from PyQt5.QtGui import QPixmap, QBrush, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer

current_dir = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_dir, "Palette_display_menu.ui")

import shared_variables as shared_variables

from model.generate_random_palette import generate_color_palette

class RandomPaletteDisplay(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        loadUi(ui_path, self)
    
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower()       

        self.palette = []

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
        self.palette = generate_color_palette(shared_variables.palette_size)

        # Create a new QGraphicsScene
        scene = QGraphicsScene()

        # Set the scene rect to match the view size
        width = self.palette_display.width()
        height = self.palette_display.height()
        scene.setSceneRect(0, 0, width, height)

        # Calculate item width based on the number of colors
        item_width = width / len(self.palette)
        item_height = height * 0.75  # 75% for the color rectangles, 25% for the labels

        for i, color in enumerate(self.palette):
            r, g, b = [int(c * 255) for c in color]
            color_code = f'#{r:02x}{g:02x}{b:02x}'

            rect_item = QGraphicsRectItem(i * item_width, 0, item_width, item_height)
            rect_item.setBrush(QBrush(QColor(r, g, b)))
            scene.addItem(rect_item)

            label = QLabel(color_code)
            label.setAlignment(Qt.AlignCenter)
            label_proxy = QGraphicsProxyWidget(rect_item)
            label_proxy.setWidget(label)
            label_proxy.setPos(i * item_width, item_height)

        # Set the scene to the QGraphicsView
        self.palette_display.setScene(scene)

        self.palette_display.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def push_GoBackButton(self):
        shared_variables.palette_size_selected = False
        self.controller.show_start_menu()

    def push_RegenerateButton(self):
        self.palette = generate_color_palette(shared_variables.palette_size)
        self.update_palette_display()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPaletteDisplay()
    ex.show()
    sys.exit(app.exec_())
