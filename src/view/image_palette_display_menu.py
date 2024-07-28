#!/usr/bin/env python3



import os
import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsScene, QGraphicsRectItem, QFileDialog, QGraphicsProxyWidget
from PyQt5.QtGui import QPixmap, QBrush, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
import colorgram
import numpy as np
import logging


current_dir = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_dir, "Image_palette_display.ui")

import shared_variables as shared_variables


class ImagePaletteDisplay(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        loadUi(ui_path, self)

        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(":/Project_image_assets/Background.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower()
        self.palette = np.array([])

        self.GoBackButton.clicked.connect(self.push_GoBackButton)
        self.ReselectButton.clicked.connect(self.select_image)

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
        if os.path.isfile(shared_variables.image_path):
            self.palette = self.generate_palette_from_image(shared_variables.image_path, shared_variables.palette_size)
        else:
            self.push_GoBackButton()

        # Create a new QGraphicsScene
        scene = QGraphicsScene()

        # Set the scene rect to match the view size
        width = self.palette_display.width()
        height = self.palette_display.height()
        scene.setSceneRect(0, 0, width, height)

        # Calculate item width based on the number of colors
        if not self.palette:
            self.push_GoBackButton()
        else:
            item_width = width / len(self.palette)
            item_height = height * 0.75  # 75% for the color rectangles, 25% for the labels

            for i, color in enumerate(self.palette):
                r, g, b = color
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

    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    def generate_palette_from_image(self, image_path, n_colors):
        colors = colorgram.extract(image_path, n_colors)
        palette = [color.rgb for color in colors]
        return palette

    def select_image(self):
        if shared_variables.palette_size_selected:
            # Create a QFileDialog to let the user select an image file
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Select an Image",
                "",
                "Image Files (*.jpg *.jpeg *.png *.gif);;All Files (*)",
                options=options
            )
            if file_path and os.path.isfile(file_path):
                shared_variables.image_path = file_path
                self.update_palette_display()
            else:
                # User canceled the dialog or didn't select a file
                shared_variables.image_path = ""
                self.push_GoBackButton()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImagePaletteDisplay()
    ex.show()
    sys.exit(app.exec_())
