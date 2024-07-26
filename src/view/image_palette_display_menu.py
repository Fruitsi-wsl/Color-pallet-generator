#!/usr/bin/env python3




import os
import sys
import resources_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QGraphicsScene, QGraphicsRectItem, QFileDialog
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np


current_dir = os.path.dirname(os.path.abspath(__file__))

ui_path = os.path.join(current_dir, "Image_palette_display.ui")

import shared_variables

from model.generate_random_palette import generate_color_palette



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
        self.palette = self.generate_palette_from_image(shared_variables.image_path, shared_variables.palette_size)
    # Create a new QGraphicsScene
        scene = QGraphicsScene()

    # Set the scene rect to match the view size
        width = self.palette_display.width()
        height = self.palette_display.height()
        scene.setSceneRect(0, 0, width, height)

    # Calculate item width based on the number of colors
        item_width = width / len(self.palette)

        for i, color in enumerate(self.palette):
            r, g, b = color
            rect_item = QGraphicsRectItem(i * item_width, 0, item_width, height)
            rect_item.setBrush(QBrush(QColor(r, g, b)))
            scene.addItem(rect_item)

    # Set the scene to the QGraphicsView
        self.palette_display.setScene(scene)

        self.palette_display.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)



    def push_GoBackButton(self):
        shared_variables.palette_size_selected = False
        self.controller.show_start_menu()

    def push_ReselectButton(self):
        self.palette = self.generate_palette_from_image(shared_variables.image_path, shared_variables.palette_size)
        self.update_palette_display()
    

    def generate_palette_from_image(self, image_path, num_colors):
        img = Image.open(image_path)
        img = img.convert('RGB')
        img = img.resize((img.width // 10, img.height // 10))
        img_array = np.array(img)
        pixels = img_array.reshape(-1, 3)
        kmeans = KMeans(n_clusters=num_colors).fit(pixels)
        colors = kmeans.cluster_centers_

    # Scale colors from 0-1 range to 0-255 range
        colors = np.clip(colors, 0, 255)
        colors = colors.astype(int)
        return colors


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

            image_path = file_path
            self.push_ReselectButton()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImagePaletteDisplay()
    ex.show()
    sys.exit(app.exec_())
