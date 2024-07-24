#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import colorsys

palette = []

def generate_color_palette(num_colors):

    for _ in range(num_colors):

        h = np.random.rand()

        s = np.random.uniform(0.5, 1.0)

        v = np.random.uniform(0.5, 1.0)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        palette.append((r,g,b))
    return palette


def plot_palette(palette):
    sns.palplot(palette)
    plt.show()


def create_palette():

    num_colors = 6
    palette = generate_color_palette(num_colors)
    plot_palette(palette)

    palette.clear()
    
    