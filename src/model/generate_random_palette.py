#!/usr/bin/env python3


import numpy as np
import colorsys



def generate_color_palette(num_colors):
    palette = []
    for _ in range(num_colors):

        h = np.random.rand()

        s = np.random.uniform(0.5, 1.0)

        v = np.random.uniform(0.5, 1.0)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        palette.append((r,g,b))
    return palette

